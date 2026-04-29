#!/usr/bin/env python3
"""Generate a JSON file of all pages for random page functionality."""
import json
import os
import glob

def main():
    # Find all .html files in _site (excluding _site itself)
    site_path = os.path.join(os.path.dirname(__file__), '..', '_site')
    
    html_files = glob.glob(os.path.join(site_path, '**', '*.html'), recursive=True)
    
    # Convert to relative URLs
    pages = []
    for f in html_files:
        # Remove _site prefix and .html suffix
        rel_path = os.path.relpath(f, site_path)
        # Remove .html extension
        url = rel_path[:-5] if rel_path.endswith('.html') else rel_path
        # Skip index files (use directory path instead)
        if url.endswith('/index'):
            url = url[:-6]  # Remove /index
        # Skip debug directory and other non-content
        if '/debug/' in url or '/SCHEMA/' in url:
            continue
        pages.append(url + '/')
    
    # Write JSON
    output_path = os.path.join(site_path, 'random_pages.json')
    with open(output_path, 'w') as f:
        json.dump(pages, f, indent=2)
    
    print(f"Generated {len(pages)} pages to {output_path}")

if __name__ == '__main__':
    main()
