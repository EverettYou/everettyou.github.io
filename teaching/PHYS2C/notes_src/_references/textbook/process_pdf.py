#!/usr/bin/env python3
"""Process Halliday & Resnick Fundamentals of Physics PDF."""

import re
from pathlib import Path

import fitz

WORK_DIR = Path(__file__).resolve().parent
FIGS_DIR = WORK_DIR / "figs"
SOURCE_PDF = WORK_DIR / "textbook.pdf"
BOOK_PAGE_OFFSET = 26
APPENDIX_START_PAGE = 1395


def convert_to_markdown(
    pdf_path: Path | str,
    start_page: int | None = None,
    end_page: int | None = None,
    output_path: Path | None = None,
) -> dict:
    """
    Convert PDF (or page range) to markdown text.
    Uses PyMuPDF4LLM for structured layout preservation.

    Args:
        pdf_path: Path to PDF.
        start_page: First page (1-indexed). None = page 1.
        end_page: Last page (1-indexed). None = last page.
        output_path: If set, write markdown to file.

    Returns:
        dict: {"markdown": str, "metadata": {...}}
    """
    pdf_path = Path(pdf_path)
    doc = fitz.open(pdf_path)
    n_pages = len(doc)
    start = (start_page or 1) - 1
    end = (end_page or n_pages) - 1
    start = max(0, min(start, n_pages - 1))
    end = max(start, min(end, n_pages - 1))
    pages = list(range(start, end + 1))

    try:
        import pymupdf.layout  # noqa: F401 - activates layout analysis for pymupdf4llm
    except ImportError:
        pass
    try:
        from pymupdf4llm import to_markdown

        md = to_markdown(doc, pages=pages)
    except ImportError:
        md = ""
        for i in pages:
            md += doc[i].get_text("text") + "\n\n"

    doc.close()

    if output_path:
        Path(output_path).write_text(md, encoding="utf-8")

    return {
        "markdown": md,
        "metadata": {
            "source": str(pdf_path.name),
            "start_page": start + 1,
            "end_page": end + 1,
            "page_count": len(pages),
        },
    }


def _get_layout_picture_boxes(
    doc: "fitz.Document",
    page_idx: int,
    caption_rect: fitz.Rect,
) -> list[fitz.Rect]:
    """
    Use pymupdf_layout to get picture bounding boxes above the caption.
    Returns empty list if layout is unavailable or no matching pictures found.
    """
    try:
        import pymupdf.layout  # noqa: F401
    except ImportError:
        return []
    try:
        from pymupdf4llm import to_markdown
    except ImportError:
        return []

    chunks = to_markdown(doc, pages=[page_idx], page_chunks=True)
    if not chunks:
        return []

    boxes = chunks[0].get("page_boxes", [])
    caption_y0 = caption_rect.y0

    def _horizontal_overlap(bbox: tuple) -> bool:
        x0, y0, x1, y1 = bbox
        return x1 > caption_rect.x0 and x0 < caption_rect.x1

    result = []
    for b in boxes:
        if b.get("class") != "picture":
            continue
        bbox = b.get("bbox")
        if not bbox or len(bbox) < 4:
            continue
        x0, y0, x1, y1 = bbox[:4]
        if y1 >= caption_y0:
            continue
        if not _horizontal_overlap(bbox):
            continue
        result.append(fitz.Rect(x0, y0, x1, y1))
    return result


def extract_figure(
    pdf_path: Path | str,
    figure_label: str,
    output_dir: Path | None = None,
    include_caption: bool = True,
) -> dict:
    """
    Extract a figure by label from a PDF.
    The figure is the content directly above the figure caption.

    Uses pymupdf_layout (GNN-based) when available for accurate picture bounding
    boxes; otherwise falls back to heuristics (get_images, cluster_drawings).

    Args:
        pdf_path: Path to chapter PDF or full textbook.
        figure_label: Figure numbering only, e.g. "14-1", "4-19". The program
            prepends "Figure " automatically; do not include the prefix.
        output_dir: Where to save extracted figures. Default: WORK_DIR / "figs"
            (i.e. _references/figs).
        include_caption: If True, return caption text in result.

    Returns:
        dict: {
            "figure": str,
            "caption": str | None,
            "images": list[dict],  # [{"path": "..."}] path without extension
            "metadata": dict,
        }
    """
    m = re.match(r"^(\d+)-(\d+)$", figure_label.strip())
    if not m:
        raise ValueError(f"Invalid figure label: {figure_label!r}. Use format ##-# (e.g. 14-1).")

    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir) if output_dir else FIGS_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    search_str = f"Figure {figure_label}"
    doc = fitz.open(pdf_path)

    caption_block = None
    caption_page = None
    caption_rect = None

    for p in range(len(doc)):
        page = doc[p]
        rects = page.search_for(search_str)
        if not rects:
            continue

        blocks = page.get_text("dict")["blocks"]
        candidates = []

        for rect in rects:
            for b in blocks:
                bbox = b.get("bbox", (0, 0, 0, 0))
                br = fitz.Rect(bbox)
                if not br.intersects(rect):
                    continue
                txt = ""
                for line in b.get("lines", []):
                    for span in line.get("spans", []):
                        txt += span.get("text", "")
                if len(txt) > 10:
                    candidates.append((br.y0, len(txt), b))

        if candidates:
            candidates.sort(key=lambda x: (-x[0], -x[1]))
            best = candidates[0]
            caption_block = best[2]
            caption_page = p
            caption_rect = fitz.Rect(caption_block["bbox"])
            break

    if caption_block is None:
        doc.close()
        raise ValueError(f"Figure {figure_label} not found in {pdf_path}")

    page = doc[caption_page]
    caption_y0 = caption_rect.y0
    caption_y1 = caption_rect.y1

    ADJACENT_GAP = 250

    def _horizontal_overlap(r: fitz.Rect) -> bool:
        return r.x1 > caption_rect.x0 and r.x0 < caption_rect.x1

    def _adjacent_to_caption(r: fitz.Rect) -> bool:
        return r.y1 > caption_y0 - ADJACENT_GAP

    candidates = []
    blocks = page.get_text("dict")["blocks"]

    # Prefer pymupdf_layout picture boxes when available (GNN-based, more accurate)
    layout_boxes = _get_layout_picture_boxes(doc, caption_page, caption_rect)
    if layout_boxes:
        candidates.extend(layout_boxes)

    if not candidates:
        for img in page.get_images(full=True):
            xref = img[0]
            try:
                for r in page.get_image_rects(xref):
                    if r.y1 < caption_y0 and _horizontal_overlap(r):
                        candidates.append(r)
            except Exception:
                pass

        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if b.get("type") == 1:
                br = fitz.Rect(b.get("bbox", (0, 0, 0, 0)))
                if br.y1 < caption_y0 and _horizontal_overlap(br):
                    candidates.append(br)

        try:
            for bbox in page.cluster_drawings():
                if (
                    bbox.y1 < caption_y0
                    and _horizontal_overlap(bbox)
                    and _adjacent_to_caption(bbox)
                ):
                    candidates.append(bbox)
        except Exception:
            pass

    if candidates:
        clip_rect = caption_rect
        for r in candidates:
            clip_rect = clip_rect | r
        clip_top = min(r.y0 for r in candidates)
    else:
        prev_y1 = 0
        for b in blocks:
            br = fitz.Rect(b.get("bbox", (0, 0, 0, 0)))
            if br.y1 < caption_y0 and br.width > 200 and br.height > 12:
                prev_y1 = max(prev_y1, br.y1)
        if prev_y1 == 0:
            prev_y1 = max(
                (fitz.Rect(b.get("bbox", (0, 0, 0, 0))).y1 for b in blocks if fitz.Rect(b.get("bbox", (0, 0, 0, 0))).y1 < caption_y0),
                default=caption_y0 - 100,
            )
        clip_top = prev_y1
        clip_rect = fitz.Rect(caption_rect.x0, clip_top, caption_rect.x1, caption_y1)

    clip_rect = fitz.Rect(clip_rect.x0, clip_top, clip_rect.x1, caption_y1)

    base_name = f"fig_{figure_label}"
    pdf_path_out = output_dir / f"{base_name}.pdf"
    png_path_out = output_dir / f"{base_name}.png"

    new_doc = fitz.open()
    new_page = new_doc.new_page(width=clip_rect.width, height=clip_rect.height)
    new_page.show_pdf_page(new_page.rect, doc, caption_page, clip=clip_rect)
    new_doc.save(pdf_path_out)
    new_doc.close()

    pix = page.get_pixmap(clip=clip_rect, dpi=150)
    pix.save(png_path_out)

    caption_text = None
    if include_caption:
        for line in caption_block.get("lines", []):
            for span in line.get("spans", []):
                caption_text = (caption_text or "") + span.get("text", "")

    path_no_ext = str((output_dir / base_name).resolve())

    doc.close()

    return {
        "figure": figure_label,
        "caption": caption_text.strip() if caption_text else None,
        "images": [{"path": path_no_ext}],
        "metadata": {
            "source": str(pdf_path.name),
            "page": caption_page + 1,
        },
    }


def _parse_toc_from_forematter(forematter_path: Path) -> dict:
    """Parse forematter TOC. Returns {chapter_num: [(section_title, book_page), ...]}."""
    doc = fitz.open(forematter_path)
    toc = {}
    for p in range(len(doc)):
        text = doc[p].get_text()
        for m in re.finditer(r"(\d+-\d+)\s+([A-Z][A-Z0-9\s,—'\u2019\.\-]+?)\s+(\d+)\b", text):
            sec, title, page = m.group(1), m.group(2).strip(), int(m.group(3))
            ch = int(sec.split("-")[0])
            if ch not in toc:
                toc[ch] = []
            toc[ch].append((f"{sec} {title}", page))
        for m in re.finditer(r"\b(\d{1,2})\s+([A-Za-z][A-Za-z\s—\-]+?)\s+(\d{3,4})\s*$", text, re.M):
            ch, title, page = int(m.group(1)), m.group(2).strip(), int(m.group(3))
            if "-" in title:
                continue
            if ch not in toc:
                toc[ch] = []
            if not any(t[0].startswith(f"{ch}-") or t[0].startswith(f"{ch} ") for t in toc[ch]):
                toc[ch].insert(0, (f"{ch} {title}", page))
    doc.close()
    for ch in toc:
        toc[ch].sort(key=lambda x: x[1])
    return toc


def extract_section(
    chapter_pdf_path: Path | str,
    section_title: str,
    forematter_path: Path | None = None,
    output_markdown: bool = True,
    extract_images: bool = False,
    images_dir: Path | None = None,
) -> dict:
    """
    Extract a section by title from a chapter PDF.
    Uses TOC for page range; refines with section header styling.

    Args:
        chapter_pdf_path: Path to chapter PDF (e.g. ch14_fluids.pdf).
        section_title: Section title or number (e.g. "14-1 FLUIDS, DENSITY, AND PRESSURE" or "14-1").
        forematter_path: Path to forematter.pdf for TOC. Default: WORK_DIR / forematter.pdf.
        output_markdown: If True, use convert_to_markdown for text.
        extract_images: If True, extract images.
        images_dir: Where to save images. Default: temp or FIGS_DIR.

    Returns:
        dict: {content: {text, tables}, images: [...], metadata: {...}}
    """
    chapter_pdf_path = Path(chapter_pdf_path)
    forematter_path = forematter_path or WORK_DIR / "forematter.pdf"
    images_dir = Path(images_dir) if images_dir else FIGS_DIR
    images_dir.mkdir(parents=True, exist_ok=True)

    m = re.search(r"ch(\d+)", chapter_pdf_path.name, re.I)
    chapter_num = int(m.group(1)) if m else None
    if not chapter_num:
        raise ValueError(f"Cannot infer chapter number from {chapter_pdf_path}")

    toc = _parse_toc_from_forematter(forematter_path)
    sections = toc.get(chapter_num, [])
    if not sections:
        start_page, end_page = 1, 999
        chapter_start_book = 386
    else:
        chapter_start_book = sections[0][1]
        start_page = end_page = None
        section_title_norm = section_title.lower().replace("  ", " ").strip()
        for i, (title, book_page) in enumerate(sections):
            title_norm = title.lower().replace("  ", " ")
            if (
                section_title_norm in title_norm
                or title_norm.startswith(section_title_norm)
                or (section_title_norm.isdigit() and title.startswith(section_title_norm + " "))
            ):
                start_page = book_page - chapter_start_book + 1
                if i + 1 < len(sections):
                    end_page = sections[i + 1][1] - 1 - chapter_start_book + 1
                else:
                    end_page = start_page + 20
                break
        if start_page is None:
            start_page, end_page = 1, 5

    result = convert_to_markdown(
        chapter_pdf_path,
        start_page=max(1, start_page),
        end_page=min(end_page or 999, 999),
    )
    text = result["markdown"]
    tables = []
    images = []

    doc = fitz.open(chapter_pdf_path)
    for p in range(max(0, start_page - 1), min(len(doc), end_page or 999)):
        page = doc[p]
        if extract_images:
            for img in page.get_images(full=True):
                xref = img[0]
                try:
                    base = doc.extract_image(xref)
                    ext = base.get("ext", "png")
                    out_path = images_dir / f"sec_{chapter_num}_{p+1}_{xref}.{ext}"
                    with open(out_path, "wb") as f:
                        f.write(base["image"])
                    images.append({
                        "path": str((images_dir / f"sec_{chapter_num}_{p+1}_{xref}").resolve()),
                        "figure_ref": None,
                        "caption": None,
                    })
                except Exception:
                    pass
        try:
            finder = page.find_tables()
            for tbl in finder.tables:
                md = getattr(tbl, "to_markdown", lambda: "")() or ""
                tables.append({"markdown": md, "caption": None})
        except Exception:
            pass
    doc.close()

    return {
        "content": {"text": text, "tables": tables},
        "images": images,
        "metadata": {
            "section": section_title,
            "source": str(chapter_pdf_path.name),
            "pages": [start_page, end_page],
            "image_count": len(images),
            "table_count": len(tables),
        },
    }


def collect_all_figures(
    pdf_path: Path | str,
    output_dir: Path | None = None,
    extract_figures: bool = False,
) -> dict:
    """
    Scan a PDF for all figures (Figure ##-#). Optionally extract each to a file.

    By default (extract_figures=False) only discovers and lists figure numbers;
    does not call extract_figure. Set extract_figures=True to extract.

    Args:
        pdf_path: Path to chapter PDF or full textbook.
        output_dir: Folder for extracted figures. Default: WORK_DIR / "figs"
            (i.e. _references/figs).
        extract_figures: If True, call extract_figure for each. Default False.

    Returns:
        dict: {
            "output_dir": str,
            "figures": list[dict],  # [{"number": "14-1", "path": "fig_14-1"} or {"number": "14-1"}]
            "manifest": dict,       # {"14-1": "fig_14-1", ...} or {}
            "metadata": dict,
        }
    """
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir) if output_dir else FIGS_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    seen = set()
    figure_nums = []

    for p in range(len(doc)):
        text = doc[p].get_text()
        for m in re.finditer(r"Figure\s+(\d+-\d+)", text, re.IGNORECASE):
            num = m.group(1)
            if num not in seen:
                seen.add(num)
                figure_nums.append(num)

    doc.close()

    figures = []
    manifest = {}
    if extract_figures:
        for num in figure_nums:
            try:
                extract_figure(pdf_path, num, output_dir=output_dir)
                base = f"fig_{num}"
                figures.append({"number": num, "path": base})
                manifest[num] = base
            except ValueError:
                pass
    else:
        figures = [{"number": num} for num in figure_nums]

    return {
        "output_dir": str(output_dir.resolve()),
        "figures": figures,
        "manifest": manifest,
        "metadata": {
            "source": str(pdf_path.name),
            "total": len(figure_nums),
            "extracted": extract_figures,
        },
    }


def split_pdf_by_range(
    start_page: int,
    end_page: int,
    output_filename: str,
    pdf_path: Path = SOURCE_PDF,
    output_dir: Path = WORK_DIR,
) -> Path:
    """
    Extract a page range from the textbook PDF and save to a named file.

    Args:
        start_page: First page (1-indexed, inclusive).
        end_page: Last page (1-indexed, inclusive).
        output_filename: Exact output filename (e.g. "forematter.pdf", "ch14.pdf").
        pdf_path: Source PDF. Defaults to textbook.pdf in working dir.
        output_dir: Output directory. Defaults to working dir.

    Returns:
        Path to the created PDF file.
    """
    if not output_filename.lower().endswith(".pdf"):
        output_filename += ".pdf"

    doc = fitz.open(pdf_path)
    new_doc = fitz.open()
    # PyMuPDF uses 0-indexed pages; insert_pdf to_page is inclusive
    new_doc.insert_pdf(doc, from_page=start_page - 1, to_page=end_page - 1)
    output_path = output_dir / output_filename
    new_doc.save(output_path)
    new_doc.close()
    doc.close()

    return output_path


if __name__ == "__main__":
    split_pdf_by_range(1, 26, "forematter.pdf")
