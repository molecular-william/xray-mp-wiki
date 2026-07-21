#!/usr/bin/env python3
"""
Lint script for xray-mp-wiki.
Checks: broken links, orphans, duplicate sections,
frontmatter consistency, minimum outbound links, DOI format,
stale pages, cross-ref consistency.

Run from scripts/: python scripts/lint.py
Or from project root: python scripts/lint.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import re
from collections import defaultdict
from datetime import date as date_type
from datetime import datetime, timedelta

import yaml
from _base import BASE_DIR, fast_load_str

WIKI_ROOT = BASE_DIR / "xray-mp-wiki"
CATEGORIES = ["proteins", "reagents", "methods", "concepts"]
VALID_TYPES = {"protein", "reagent", "method", "concept"}

# Map category/subdir -> expected category for frontmatter
CATEGORY_DIR_MAP = {}
for cat in CATEGORIES:
    CATEGORY_DIR_MAP[cat] = cat
    subdir_path = WIKI_ROOT / cat
    if subdir_path.is_dir():
        for sd in subdir_path.iterdir():
            if sd.is_dir():
                CATEGORY_DIR_MAP[str(sd)] = cat

# Valid page types per category
CATEGORY_TO_TYPE = {
    "proteins": "protein",
    "reagents": "reagent",
    "methods": "method",
    "concepts": "concept",
}


# All wiki pages (non-index, non-schema)
def find_pages():
    pages = []
    for cat in CATEGORIES:
        cat_path = WIKI_ROOT / cat
        if not cat_path.is_dir():
            continue
        for md in cat_path.rglob("*.md"):
            if md.name == "index.md":
                continue
            if md.name == "SCHEMA.md":
                continue
            pages.append(md)
    return pages


def parse_frontmatter(path):
    """Parse YAML frontmatter from a markdown file.

    Handles two formats:
    1. Standard: ---\nYAML\n---\ncontent
    2. Jekyll legacy: ---\nYAML\n---\nlayout: default\ncontent
       (layout after closing ---)
    """
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"^---\s*\n(.*?)\n---\s*", content, re.DOTALL)
    if not match:
        return None, content
    try:
        fm = fast_load_str(match.group(1))
    except yaml.YAMLError:
        fm = {}
    if fm is None:
        fm = {}
    # Also check for layout: default after frontmatter closing ---
    # This is a common pattern in this wiki
    after_fm = content[match.end() :]
    layout_match = re.match(r"\s*layout:\s+default", after_fm)
    if not fm.get("layout") and layout_match:
        fm["layout"] = "default"
    return fm, content


def parse_all_pages(pages):
    """Parse frontmatter for all pages at once. Returns dict {page: (fm, content)}."""
    parsed = {}
    for page in pages:
        fm, content = parse_frontmatter(page)
        parsed[page] = (fm, content)
    return parsed


def extract_internal_links(content):
    """Extract all internal wiki links: [text](/xray-mp-wiki/...)"""
    pattern = r"\[([^\]]+)\]\(/xray-mp-wiki/([^)]+?)/\)"
    return [(match[0], match[1], match[2]) for match in re.finditer(pattern, content)]


def link_to_path(link_url):
    """Convert /xray-mp-wiki/proteins/foo/ to proteins/foo.md"""
    # Strip leading slash
    url = link_url.lstrip("/")
    # Remove trailing slash
    url = url.rstrip("/")
    return Path(url + ".md")


def get_parent_category(path):
    """Get the top-level category from a file path."""
    parts = Path(path).parts
    for i, part in enumerate(parts):
        if part in CATEGORIES:
            return part
    return None


def check_broken_links(parsed_pages):
    """Check for internal links pointing to non-existent files."""
    issues = []
    for page, (fm, content) in parsed_pages.items():
        if not fm:
            continue
        links = extract_internal_links(content)
        for full_link, text, url in links:
            target = link_to_path(url)
            if not target:
                continue
            if not (WIKI_ROOT / target).exists():
                issues.append(
                    {
                        "type": "broken_link",
                        "file": str(page.relative_to(WIKI_ROOT)),
                        "link": full_link,
                        "target": str(target),
                    }
                )
    return issues


def check_orphans(parsed_pages, catalog_paths):
    """Find pages with zero inbound links from other pages.

    Checks markdown links [text](url) from wiki pages. Uses the
    catalog (index.md) as a whitelist.
    """
    # Build set of all linked-to paths from wiki page links
    linked_to = set()
    for page, (_, content) in parsed_pages.items():
        links = extract_internal_links(content)
        for _, text, url in links:
            target = link_to_path(url)
            if target:
                linked_to.add(target)

    orphans = []
    for page in parsed_pages:
        rel = Path(page).relative_to(WIKI_ROOT)
        rel_no_ext = str(rel).removesuffix(".md")
        if rel not in linked_to and rel_no_ext not in catalog_paths:
            orphans.append(str(rel))
    return orphans


def check_duplicate_sections(parsed_pages):
    """Find pages with duplicate heading text."""
    issues = []
    for page, (_, content) in parsed_pages.items():
        headings = re.findall(r"^(#{1,4})\s+(.+)$", content, re.MULTILINE)
        seen = defaultdict(list)
        for level, text in headings:
            seen[text].append(level)
        for text, levels in seen.items():
            if len(levels) > 1:
                issues.append(
                    {
                        "type": "duplicate_section",
                        "file": str(page.relative_to(WIKI_ROOT)),
                        "heading": text,
                        "count": len(levels),
                    }
                )
    return issues


def check_frontmatter(parsed_pages):
    """Check frontmatter consistency: category, type, required fields."""
    issues = []
    for page, (fm, content) in parsed_pages.items():
        if not fm:
            issues.append(
                {
                    "type": "missing_frontmatter",
                    "file": str(page.relative_to(WIKI_ROOT)),
                }
            )
            continue

        rel = Path(page).relative_to(WIKI_ROOT)
        parent_cat = get_parent_category(rel)

        # Check required fields
        for field in ["title", "created", "updated", "type", "category", "layout", "tags", "sources"]:
            if field not in fm:
                issues.append(
                    {
                        "type": "missing_field",
                        "file": str(rel),
                        "field": field,
                    }
                )

        # Check category matches parent directory
        if parent_cat and fm.get("category") and fm["category"] != parent_cat:
            issues.append(
                {
                    "type": "category_mismatch",
                    "file": str(rel),
                    "expected": parent_cat,
                    "actual": fm["category"],
                }
            )

        # Check type matches category
        if parent_cat and fm.get("type"):
            expected_type = CATEGORY_TO_TYPE.get(parent_cat)
            if expected_type and fm["type"] != expected_type:
                issues.append(
                    {
                        "type": "type_mismatch",
                        "file": str(rel),
                        "expected": expected_type,
                        "actual": fm["type"],
                    }
                )

        # Check layout
        if fm.get("layout") != "default":
            issues.append(
                {
                    "type": "wrong_layout",
                    "file": str(rel),
                    "actual": fm.get("layout", "missing"),
                }
            )

        # Check tags is a list
        if fm.get("tags") and not isinstance(fm["tags"], list):
            issues.append(
                {
                    "type": "tags_not_list",
                    "file": str(rel),
                }
            )

        # Check sources is a list
        if fm.get("sources") and not isinstance(fm["sources"], list):
            issues.append(
                {
                    "type": "sources_not_list",
                    "file": str(rel),
                }
            )

    return issues


def check_min_outbound(parsed_pages):
    """Check that every page has at least 2 outbound wiki links."""
    issues = []
    for page, (_, content) in parsed_pages.items():
        links = extract_internal_links(content)
        if len(links) < 2:
            issues.append(
                {
                    "type": "low_outbound",
                    "file": str(page.relative_to(WIKI_ROOT)),
                    "count": len(links),
                }
            )
    return issues


def check_doi_format(parsed_pages):
    """Check that all DOIs in sources use doi/10.xxxx format."""
    issues = []
    for page, (fm, _) in parsed_pages.items():
        if not fm or "sources" not in fm:
            continue
        for src in fm["sources"]:
            if not isinstance(src, str):
                continue
            if src.startswith("doi/"):
                doi = src[4:]
                if not re.match(r"^10\.[0-9A-Za-z]+([/#][0-9A-Za-z._()\-+@&%/=]*)*$", doi):
                    issues.append(
                        {
                            "type": "bad_doi_format",
                            "file": str(page.relative_to(WIKI_ROOT)),
                            "source": src,
                        }
                    )
    return issues


def check_age(parsed_pages):
    """Flag pages older than 30 days."""
    issues = []
    cutoff = datetime.now().date() - timedelta(days=30)

    for page, (fm, _) in parsed_pages.items():
        if not fm or "updated" not in fm:
            continue
        updated_val = fm["updated"]
        if isinstance(updated_val, datetime):
            updated = updated_val.date()
        elif isinstance(updated_val, date_type):
            updated = updated_val
        elif isinstance(updated_val, str):
            try:
                updated = datetime.strptime(updated_val, "%Y-%m-%d").date()
            except ValueError:
                issues.append(
                    {
                        "type": "bad_date_format",
                        "file": str(page.relative_to(WIKI_ROOT)),
                        "updated": str(updated_val),
                    }
                )
                continue
        else:
            issues.append(
                {
                    "type": "bad_date_format",
                    "file": str(page.relative_to(WIKI_ROOT)),
                    "updated": str(updated_val),
                }
            )
            continue
        if updated < cutoff:
            issues.append(
                {
                    "type": "stale_page",
                    "file": str(page.relative_to(WIKI_ROOT)),
                    "updated": str(updated),
                    "days_old": (datetime.now().date() - updated).days,
                }
            )
    return issues


def _get_catalog_paths():
    """Read catalog from index.md and return set of valid paths (e.g., 'proteins/foo/')."""
    index_path = WIKI_ROOT / "index.md"
    if not index_path.exists():
        return set()

    with open(index_path) as f:
        content = f.read()

    start_marker = "<!-- WIKI CATALOG"
    end_marker = "END WIKI CATALOG -->"
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx + len(start_marker))

    if start_idx == -1 or end_idx == -1:
        return set()

    catalog_section = content[start_idx + len(start_marker) : end_idx]
    lines = catalog_section.strip().split("\n") if catalog_section.strip() else []

    # Find separator row
    sep_idx = -1
    for i, line in enumerate(lines):
        if "---" in line and "|" in line and i > 0:
            sep_idx = i
            break

    if sep_idx == -1:
        return set()

    # Extract paths from data rows (column 3 = path, due to leading ||)
    valid_paths = set()
    for line in lines[sep_idx + 1 :]:
        parts = [p.strip() for p in line.split("|")]
        # Catalog table has || prefix: || type | path | title | summary |
        # parts[0]='', parts[1]=type, parts[2]=path, parts[3]=title, parts[4]=summary
        if len(parts) >= 4:
            path_col = parts[2]
            if path_col:
                # Normalize: strip trailing slash for comparison
                valid_paths.add(path_col.rstrip("/"))

    return valid_paths


def check_cross_refs_consistent(parsed_pages, catalog_paths):
    """Check that all internal links point to pages in the catalog."""
    issues = []

    if not catalog_paths:
        return issues  # No catalog, skip check

    for page, (_, content) in parsed_pages.items():
        links = extract_internal_links(content)
        for full_link, text, url in links:
            path = url.strip("/")
            if path not in catalog_paths:
                issues.append(
                    {
                        "type": "stale_cross_ref",
                        "file": str(page.relative_to(WIKI_ROOT)),
                        "link": full_link,
                        "target": path,
                    }
                )

    return issues


def main():
    print("=" * 60)
    print("xray-mp-wiki Lint Report")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    pages = find_pages()
    print(f"\nTotal pages checked: {len(pages)}")
    print()

    # Parse all frontmatter ONCE — avoids 7x redundant file reads
    print("Parsing frontmatter...", end=" ", flush=True)
    parsed_pages = parse_all_pages(pages)
    print(f"{len(parsed_pages)} pages parsed")

    # Cache catalog paths — avoid re-parsing index.md
    catalog_paths = _get_catalog_paths()

    all_issues = []

    # 1. Broken links
    broken = check_broken_links(parsed_pages)
    if broken:
        print(f"!! BROKEN LINKS ({len(broken)}):")
        for i in broken:
            print(f"   {i['file']}: {i['link']} -> {i['target']}")
        all_issues.extend(broken)
    else:
        print("✓ No broken links")
    print()

    # 2. Orphan pages
    orphans = check_orphans(parsed_pages, catalog_paths)
    if orphans:
        print(f"!! ORPHAN PAGES ({len(orphans)}):")
        for o in orphans:
            print(f"   {o} (no inbound links)")
        all_issues.extend([{"type": "orphan", "file": o} for o in orphans])
    else:
        print("✓ No orphan pages")
    print()

    # 3. Duplicate sections
    dups = check_duplicate_sections(parsed_pages)
    if dups:
        print(f"!! DUPLICATE SECTIONS ({len(dups)}):")
        for d in dups:
            print(f"   {d['file']}: '{d['heading']}' appears {d['count']} times")
        all_issues.extend(dups)
    else:
        print("✓ No duplicate sections")
    print()

    # 4. Frontmatter consistency
    fm_issues = check_frontmatter(parsed_pages)
    if fm_issues:
        print(f"!! FRONTMATTER ISSUES ({len(fm_issues)}):")
        for f in fm_issues:
            if f["type"] == "missing_field":
                print(f"   {f['file']}: missing '{f['field']}'")
            elif f["type"] == "category_mismatch":
                print(f"   {f['file']}: category '{f['actual']}' should be '{f['expected']}'")
            elif f["type"] == "type_mismatch":
                print(f"   {f['file']}: type '{f['actual']}' should be '{f['expected']}'")
            elif f["type"] == "wrong_layout":
                print(f"   {f['file']}: layout is '{f['actual']}' (should be 'default')")
            elif f["type"] == "missing_frontmatter":
                print(f"   {f['file']}: no YAML frontmatter")
            else:
                print(f"   {f['file']}: {f['type']}")
        all_issues.extend(fm_issues)
    else:
        print("✓ Frontmatter consistent")
    print()

    # 5. Minimum outbound links
    low_out = check_min_outbound(parsed_pages)
    if low_out:
        print(f"!! LOW OUTBOUND LINKS ({len(low_out)}):")
        for issue in low_out:
            print(f"   {issue['file']}: {issue['count']} links (need >= 2)")
        all_issues.extend(low_out)
    else:
        print("✓ All pages have >= 2 outbound links")
    print()

    # 6. DOI format
    doi_issues = check_doi_format(parsed_pages)
    if doi_issues:
        print(f"!! DOI FORMAT ISSUES ({len(doi_issues)}):")
        for d in doi_issues:
            print(f"   {d['file']}: {d['source']}")
        all_issues.extend(doi_issues)
    else:
        print("✓ DOI format OK")
    print()

    # 7. Stale pages
    stale = check_age(parsed_pages)
    if stale:
        print(f"!! STALE PAGES ({len(stale)}):")
        for s in stale:
            if "days_old" in s:
                print(f"   {s['file']}: last updated {s['updated']} ({s['days_old']} days ago)")
            elif "updated" in s:
                print(f"   {s['file']}: bad date format '{s['updated']}'")
        all_issues.extend(stale)
    else:
        print("✓ No stale pages")
    print()

    # 8. Cross-ref consistency
    cross_refs = check_cross_refs_consistent(parsed_pages, catalog_paths)
    if cross_refs:
        print(f"!! STALE CROSS-REFS ({len(cross_refs)}):")
        for cr in cross_refs:
            print(f"   {cr['file']}: {cr['link']} -> {cr['target']}")
        all_issues.extend(cross_refs)
    else:
        print("✓ All cross-refs consistent with catalog")
    print()

    # Summary
    print("=" * 60)
    type_counts = defaultdict(int)
    for i in all_issues:
        type_counts[i["type"]] += 1
    if type_counts:
        print(f"TOTAL ISSUES: {len(all_issues)}")
        for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
            print(f"  {t}: {c}")
    else:
        print("TOTAL ISSUES: 0 — wiki is clean!")
    print("=" * 60)

    if all_issues:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
