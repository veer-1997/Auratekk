#!/usr/bin/env python3
"""
Fix favicon references in all HTML files.
Replaces broken Artech_I.SVG references with proper favicon-96x96.png configuration.
"""

import os
import re
from pathlib import Path

# Define the old and new favicon HTML
OLD_FAVICON = '''    <link rel="icon" type="image/svg+xml" href="Artech_I.SVG">
    <link rel="icon" type="image/x-icon" href="favicon.ico?v=2">
    <link rel="shortcut icon" href="favicon.ico?v=2">'''

NEW_FAVICON = '''    <link rel="icon" type="image/png" sizes="96x96" href="../favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="32x32" href="../favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="../favicon-96x96.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../favicon-96x96.png">
    <link rel="shortcut icon" href="../favicon.ico">'''

def fix_favicon_in_file(file_path):
    """Fix favicon references in a single HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file needs fixing
        if 'Artech_I.SVG' not in content:
            return False
        
        # Replace old favicon with new
        new_content = content.replace(OLD_FAVICON, NEW_FAVICON)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to fix all HTML files."""
    base_dir = Path(__file__).parent
    fixed_count = 0
    
    # Find all HTML files in services directory
    services_dir = base_dir / 'services'
    if services_dir.exists():
        for html_file in services_dir.glob('*.html'):
            if fix_favicon_in_file(html_file):
                print(f"✓ Fixed: {html_file.name}")
                fixed_count += 1
    
    # Fix other HTML files in root
    for html_file in base_dir.glob('*.html'):
        if html_file.name not in ['index.html', 'subpage_template.html']:
            if fix_favicon_in_file(html_file):
                print(f"✓ Fixed: {html_file.name}")
                fixed_count += 1
    
    print(f"\n✅ Fixed {fixed_count} files")

if __name__ == '__main__':
    main()
