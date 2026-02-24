#!/usr/bin/env python3
"""MCP server exposing PDF split tool for Cursor AI."""

from pathlib import Path

from mcp.server.fastmcp import FastMCP

from process_pdf import (
    BOOK_PAGE_OFFSET,
    SOURCE_PDF,
    WORK_DIR,
    collect_all_figures,
    convert_to_markdown,
    extract_figure,
    extract_section,
    split_pdf_by_range,
)

mcp = FastMCP("phys2c-textbook", json_response=True)


@mcp.tool()
def split_textbook_pdf(
    start_page: int,
    end_page: int,
    output_filename: str,
    use_book_pages: bool = False,
) -> str:
    """
    Extract a page range from the textbook PDF and save to a named file.
    Source: textbook.pdf. Output saved in _references/ (working directory).

    Args:
        start_page: First page (1-indexed, inclusive).
        end_page: Last page (1-indexed, inclusive).
        output_filename: Output PDF filename (e.g. "forematter.pdf", "ch14.pdf").
        use_book_pages: If True, add 26 to start/end (TOC uses book page numbers).

    Returns:
        Absolute path to the created PDF file.
    """
    if use_book_pages:
        start_page += BOOK_PAGE_OFFSET
        end_page += BOOK_PAGE_OFFSET
    path = split_pdf_by_range(
        start_page, end_page, output_filename, SOURCE_PDF, WORK_DIR
    )
    return str(path.resolve())


@mcp.tool()
def convert_to_markdown_tool(
    pdf_path: str,
    start_page: int | None = None,
    end_page: int | None = None,
    output_path: str | None = None,
) -> dict:
    """
    Convert PDF (or page range) to markdown text.

    Args:
        pdf_path: Path to PDF file.
        start_page: First page (1-indexed). None = page 1.
        end_page: Last page (1-indexed). None = last page.
        output_path: If set, write markdown to file.

    Returns:
        dict with "markdown" and "metadata" keys.
    """
    result = convert_to_markdown(
        pdf_path,
        start_page=start_page,
        end_page=end_page,
        output_path=Path(output_path) if output_path else None,
    )
    result["metadata"]["source"] = str(Path(pdf_path).resolve())
    return result


@mcp.tool()
def extract_figure_tool(
    pdf_path: str,
    figure_label: str,
    output_dir: str | None = None,
    include_caption: bool = True,
) -> dict:
    """
    Extract a figure by numbering (e.g. "14-1", "4-19") from a PDF.
    Input is numbering only; "Figure " is prepended automatically.

    Args:
        pdf_path: Path to PDF file.
        figure_label: Figure numbering only, e.g. "14-1", "4-19".
        output_dir: Where to save. Default: _references/figs.
        include_caption: If True, return caption text.

    Returns:
        dict with page, images (path without extension), caption.
    """
    return extract_figure(
        pdf_path,
        figure_label=figure_label,
        output_dir=Path(output_dir) if output_dir else None,
        include_caption=include_caption,
    )


@mcp.tool()
def collect_all_figures_tool(
    pdf_path: str,
    output_dir: str | None = None,
    extract_figures: bool = False,
) -> dict:
    """
    Scan a PDF for all figures (Figure ##-#). By default only lists them;
    set extract_figures=True to extract each to file.

    Args:
        pdf_path: Path to PDF file.
        output_dir: Where to save. Default: _references/figs.
        extract_figures: If True, extract each figure. Default False.

    Returns:
        dict with output_dir, figures, manifest, metadata.
    """
    return collect_all_figures(
        pdf_path,
        output_dir=Path(output_dir) if output_dir else None,
        extract_figures=extract_figures,
    )


@mcp.tool()
def extract_section_tool(
    chapter_pdf_path: str,
    section_title: str,
    forematter_path: str | None = None,
    output_markdown: bool = True,
    extract_images: bool = False,
) -> dict:
    """
    Extract a section by title from a chapter PDF.
    Uses TOC for page range.

    Args:
        chapter_pdf_path: Path to chapter PDF (e.g. ch14_fluids.pdf).
        section_title: Section title or number (e.g. "14-1" or "14-1 FLUIDS, DENSITY, AND PRESSURE").
        forematter_path: Path to forematter.pdf. Default: _references/forematter.pdf.
        output_markdown: If True, return markdown text.
        extract_images: If True, extract images.

    Returns:
        dict with content, images, metadata.
    """
    return extract_section(
        chapter_pdf_path,
        section_title=section_title,
        forematter_path=Path(forematter_path) if forematter_path else None,
        output_markdown=output_markdown,
        extract_images=extract_images,
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
