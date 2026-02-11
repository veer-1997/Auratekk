#!/usr/bin/env python3
"""
Replace Tailwind CSS CDN with local built CSS in all HTML files.
"""

import os
import re
from pathlib import Path

def replace_tailwind_cdn(file_path):
    """Replace Tailwind CDN script with local CSS link."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file contains Tailwind CDN
        if 'cdn.tailwindcss.com' not in content:
            return False
        
        # Pattern to match Tailwind CDN script tag
        pattern = r'<script\s+src="https://cdn\.tailwindcss\.com[^"]*"[^>]*></script>'
        
        # Determine the correct relative path based on file location
        if '/services/' in str(file_path) or '/demos/' in str(file_path):
            css_path = '../dist/tailwind.min.css'
        else:
            css_path = 'dist/tailwind.min.css'
        
        # Replacement CSS link
        replacement = f'<link rel="stylesheet" href="{css_path}">'
        
        # Replace the CDN script with CSS link
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all HTML files."""
    base_dir = Path(__file__).parent
    fixed_count = 0
    
    # Find all HTML files
    for html_file in base_dir.rglob('*.html'):
        # Skip node_modules
        if 'node_modules' in str(html_file):
            continue
            
        if replace_tailwind_cdn(html_file):
            print(f"✓ Fixed: {html_file.relative_to(base_dir)}")
            fixed_count += 1
    
    print(f"\n✅ Fixed {fixed_count} files")
    print(f"📦 Built CSS: dist/tailwind.min.css")
    print(f"🚀 Your site should now load correctly!")

if __name__ == '__main__':
    main()
