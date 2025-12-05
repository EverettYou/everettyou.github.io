#!/usr/bin/env python3
"""
Convert first page of PDF files to PNG images.
Reads talks from _data/talks.yml and converts each PDF's first page to PNG.
"""

import yaml
import os
from pathlib import Path
try:
    from pdf2image import convert_from_path
except ImportError:
    print("Error: pdf2image is not installed.")
    print("Please install it with: pip install pdf2image")
    print("Also install poppler: brew install poppler (macOS) or apt-get install poppler-utils (Linux)")
    exit(1)

def convert_pdf_to_png(pdf_path, output_path, dpi=150):
    """
    Convert first page of PDF to PNG image.
    
    Args:
        pdf_path: Path to PDF file
        output_path: Path to output PNG file
        dpi: Resolution for output image (default: 150)
    """
    try:
        # Convert first page only
        images = convert_from_path(pdf_path, dpi=dpi, first_page=1, last_page=1)
        if images:
            images[0].save(output_path, 'PNG')
            print(f"✓ Converted: {pdf_path.name} -> {output_path.name}")
            return True
        else:
            print(f"✗ Failed: No pages found in {pdf_path.name}")
            return False
    except Exception as e:
        print(f"✗ Error converting {pdf_path.name}: {e}")
        return False

def main():
    """Main function to process all talks from talks.yml"""
    # Get project root (assuming script is in _scripts/)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Paths
    talks_yml = project_root / '_data' / 'talks.yml'
    pdf_dir = project_root / 'assets' / 'pdf' / 'talks'
    output_dir = project_root / 'assets' / 'img' / 'talks'
    
    # Check if talks.yml exists
    if not talks_yml.exists():
        print(f"Error: {talks_yml} not found")
        return
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load talks data
    with open(talks_yml, 'r') as f:
        talks = yaml.safe_load(f)
    
    print(f"Found {len(talks)} talks in talks.yml\n")
    
    success_count = 0
    fail_count = 0
    
    for talk in talks:
        talk_id = talk.get('id')
        pdf_filename = talk.get('pdf')
        cover_filename = talk.get('cover')
        
        if not pdf_filename:
            print(f"⚠ Skipping {talk_id}: No PDF filename specified")
            fail_count += 1
            continue
        
        pdf_path = pdf_dir / pdf_filename
        output_path = output_dir / cover_filename if cover_filename else output_dir / f"{talk_id}.png"
        
        if not pdf_path.exists():
            print(f"⚠ Skipping {talk_id}: PDF not found at {pdf_path}")
            fail_count += 1
            continue
        
        if convert_pdf_to_png(pdf_path, output_path):
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n{'='*50}")
    print(f"Conversion complete: {success_count} succeeded, {fail_count} failed")

if __name__ == '__main__':
    main()

