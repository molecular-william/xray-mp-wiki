#!/usr/bin/env python3
"""Generate wiki health report as HTML."""

import os
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

WIKI_DIR = Path(__file__).parent.parent
SITE_DIR = WIKI_DIR / '_site'
CATEGORIES = {
    'proteins': 'Proteins',
    'reagents': 'Reagents',
    'methods': 'Methods',
    'concepts': 'Concepts',
}

def count_pages():
    """Count pages in each category."""
    counts = defaultdict(int)
    all_pages = []
    for cat_dir, cat_name in CATEGORIES.items():
        dir_path = WIKI_DIR / cat_dir
        if dir_path.exists():
            for md_file in dir_path.rglob('*.md'):
                counts[cat_name] += 1
                all_pages.append(md_file)
    return counts, all_pages

def get_wikilinks(md_file):
    """Extract wikilinks from markdown file."""
    with open(md_file) as f:
        content = f.read()
    # Pattern: [text](/category/file/)
    links = re.findall(r'\[([^\]]+)\]\(/([^/]+)/([^/]+)/', content)
    return links

def generate_html(counts, all_pages):
    """Generate HTML health report."""
    total = sum(counts.values())
    
    # Find pages without wikilinks
    no_links = [p for p in all_pages if not get_wikilinks(p)]
    
    # Find pages with fewer than 2 wikilinks
    few_links = [(p, get_wikilinks(p)) for p in all_pages if 0 < len(get_wikilinks(p)) < 2]
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Wiki Health Report</title>
<style>
body {{ font-family: system-ui, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; }}
h1 {{ color: #333; }}
h2 {{ color: #666; border-bottom: 1px solid #ddd; padding-bottom: 5px; }}
ul {{ line-height: 1.8; }}
li {{ padding: 2px 0; }}
.empty {{ color: #888; font-style: italic; }}
.time {{ color: #999; font-size: 0.9em; }}
</style>
</head>
<body>
<h1>Wiki Health Report</h1>

<h2>Statistics</h2>
<ul>
  <li>Total pages: {total}</li>
"""
    for cat, cnt in counts.items():
        html += f'  <li>{cat}: {cnt}</li>\n'
    
    html += f"""
<h2>Pages without Wikilinks</h2>
<p>Pages that have no outbound wikilinks (potential orphan pages):</p>
<ul>
"""
    if no_links:
        for p in no_links:
            html += f'  <li>{p.relative_to(WIKI_DIR)}</li>\n'
    else:
        html += '  <li class="empty">None - all pages have at least one wikilink!</li>\n'
    
    html += f"""
</ul>

<h2>Pages with Fewer Than 2 Wikilinks</h2>
<p>Pages that should have more internal links:</p>
<ul>
"""
    if few_links:
        for p, links in few_links:
            link_text = ', '.join(f'[{t}]' for t, _, _ in links)
            html += f'  <li>{p.relative_to(WIKI_DIR)}: {len(links)} link(s) - {link_text}</li>\n'
    else:
        html += '  <li class="empty">None - all pages have 2+ wikilinks!</li>\n'
    
    html += f"""
</ul>

<p class="time">Report generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

<script>
// Auto-refresh every 60 seconds
setTimeout(() => window.location.reload(), 60000);
</script>
</body>
</html>
"""
    return html

def main():
    counts, pages = count_pages()
    html = generate_html(counts, pages)
    
    # Ensure _site directory exists
    SITE_DIR.mkdir(exist_ok=True)
    
    output_path = SITE_DIR / 'health.html'
    with open(output_path, 'w') as f:
        f.write(html)
    
    print(f'Generated health report: {output_path}')

if __name__ == '__main__':
    main()
