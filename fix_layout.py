#!/usr/bin/env python3
"""Fix 'layout: default' visible text on all wiki pages.

Pattern to fix:
  ---
  ...
  category: xxx
  ---
  layout: default

Becomes:
  ---
  ...
  category: xxx
  layout: default
  ---
"""
import os
import re

WIKI_DIR = os.path.join(os.path.dirname(__file__), 'xray-mp-wiki') if os.path.basename(os.getcwd()) == 'xray-mp-wiki' else os.getcwd()
WIKI_DIR = '/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki'

categories = ['proteins', 'reagents', 'methods', 'concepts']
fixed = 0
skipped = 0
errors = []

for cat in categories:
    cat_dir = os.path.join(WIKI_DIR, cat)
    if not os.path.isdir(cat_dir):
        continue
    for root, dirs, files in os.walk(cat_dir):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(root, fname)
            if 'index.md' in fname:
                continue
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                errors.append(f"{fpath}: read error: {e}")
                continue

            # Pattern: closing --- followed by layout: default
            # The layout: default line appears after --- and before the content
            pattern = r'(---\n(?:.*?\n)*?)(---)\n(\s*layout: default\s*\n)'
            
            match = re.search(pattern, content, re.DOTALL)
            if not match:
                # Check if layout: default appears after --- at all
                if '---\nlayout: default' in content or '---\n\nlayout: default' in content:
                    # Simple pattern: ---\nlayout: default
                    new_content = re.sub(r'(---)\n(\s*layout: default\s*\n)', r'\1\n\2', content, count=1)
                    # Now insert layout: default before ---
                    # Find the last --- that closes frontmatter
                    # Strategy: find "category:" line, insert layout: default before closing ---
                    cat_pattern = r'(category:\s*\w+)\n(---)'
                    new_content = re.sub(cat_pattern, r'\1\nlayout: default\n\2', new_content, count=1)
                    
                    if new_content != content:
                        with open(fpath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        fixed += 1
                        print(f"  FIXED: {os.path.relpath(fpath, WIKI_DIR)}")
                    else:
                        skipped += 1
                        print(f"  SKIP (no change): {os.path.relpath(fpath, WIKI_DIR)}")
                else:
                    skipped += 1
                continue
            
            # More complex: find the closing --- that's followed by layout: default
            # Split content into frontmatter and body
            # Find the closing ---
            parts = content.split('---')
            if len(parts) < 3:
                skipped += 1
                continue
            
            # parts[0] = before first ---, parts[1] = frontmatter, parts[2] = after closing ---
            frontmatter = parts[1].strip()
            after_closing = parts[2]
            
            # Check if after_closing starts with layout: default
            if 'layout: default' not in after_closing.split('\n')[0].strip() and \
               'layout: default' not in after_closing.split('\n')[1].strip() if len(after_closing.split('\n')) > 1 else False:
                # Check more broadly
                lines_after = after_closing.lstrip('\n').split('\n')
                first_nonempty = ''
                for line in lines_after:
                    if line.strip():
                        first_nonempty = line.strip()
                        break
                if 'layout: default' not in first_nonempty:
                    skipped += 1
                    continue
            
            # Remove layout: default from after frontmatter
            after_lines = after_closing.split('\n')
            new_after_lines = []
            layout_removed = False
            for line in after_lines:
                if not layout_removed and 'layout: default' in line:
                    layout_removed = True
                    continue  # skip this line
                new_after_lines.append(line)
            
            new_after = '\n'.join(new_after_lines)
            
            # Add layout: default to frontmatter
            new_frontmatter = frontmatter + '\nlayout: default'
            
            # Reassemble
            new_content = '---\n' + new_frontmatter + '\n---\n' + new_after
            
            if new_content != content:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixed += 1
                print(f"  FIXED: {os.path.relpath(fpath, WIKI_DIR)}")
            else:
                skipped += 1

print(f"\n=== Summary ===")
print(f"Fixed: {fixed}")
print(f"Skipped: {skipped}")
if errors:
    print(f"Errors: {len(errors)}")
    for e in errors[:5]:
        print(f"  {e}")