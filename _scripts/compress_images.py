#!/usr/bin/env python3
"""
Compress PNG images by reducing resolution
"""
from PIL import Image
import os
import sys

def compress_image(input_path, output_path=None, scale_factor=0.5):
    """
    Compress an image by reducing its resolution.
    
    Args:
        input_path: Path to input image
        output_path: Path to output image (if None, overwrites input)
        scale_factor: Factor to scale down (0.5 = 50% of original size)
    """
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found")
        return False
    
    try:
        # Open image
        img = Image.open(input_path)
        original_size = img.size
        original_file_size = os.path.getsize(input_path)
        
        # Calculate new size
        new_width = int(original_size[0] * scale_factor)
        new_height = int(original_size[1] * scale_factor)
        
        # Resize image using high-quality resampling
        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Save compressed image
        output = output_path if output_path else input_path
        img_resized.save(output, 'PNG', optimize=True)
        
        new_file_size = os.path.getsize(output)
        compression_ratio = (1 - new_file_size / original_file_size) * 100
        
        print(f"✓ {os.path.basename(input_path)}")
        print(f"  Original: {original_size[0]}x{original_size[1]} ({original_file_size/1024/1024:.2f} MB)")
        print(f"  Compressed: {new_width}x{new_height} ({new_file_size/1024/1024:.2f} MB)")
        print(f"  Compression: {compression_ratio:.1f}% reduction")
        print()
        
        return True
    except Exception as e:
        print(f"✗ Error processing {input_path}: {e}")
        return False

def main():
    """Main function to compress the four research images"""
    images = [
        'assets/img/figures/_backup/correlated_quantum_manybody.png',
        'assets/img/figures/_backup/machine_learning_physics.png',
        'assets/img/figures/_backup/quantum_infomation_dynamics.png',
        'assets/img/figures/_backup/topological_phases_of_matter.png'
    ]
    
    # Get project root (assuming script is in _scripts/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    print("Compressing images by reducing resolution to 50%...")
    print("=" * 60)
    print()
    
    success_count = 0
    for img_path in images:
        full_path = os.path.join(project_root, img_path)
        if compress_image(full_path, scale_factor=0.5):
            success_count += 1
    
    print("=" * 60)
    print(f"Compression complete: {success_count}/{len(images)} images processed")

if __name__ == '__main__':
    main()

