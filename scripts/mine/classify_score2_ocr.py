#!/usr/bin/env python3
"""Classify score-2 files by OCR quality: 'usable' (1) vs 'needs-re-OCR' (0).

Heuristic: a file is usable if it has a Methods section AND ends naturally
(period, bracket, or empty line).  Otherwise it may be truncated mid-flow.
"""
import json, re, sys
from pathlib import Path

results = json.loads(Path("scripts/raw_completeness_cache.json").read_text())
score2 = sorted(k for k, v in results.items() if v == 2)

NATURAL_END = re.compile(r"[.\]})\"']\s*$")
METHOD_HEADER = re.compile(r"##+\s*(?:\d+(?:\.\d+)*\.?\s*)?(?:material|method[s]?|experimental)", re.I)
DOI_NEAR_END = re.compile(r"10\.\d{4,}/\S+")

verdict = {}

for fname in score2:
    p = Path(f"raw/papers/{fname}")
    if not p.exists():
        verdict[fname] = (0, "file_missing")
        continue
    
    text = p.read_text("utf-8", errors="replace")
    lines = text.splitlines()
    n = len(lines)
    
    if n < 30:
        verdict[fname] = (0, "too_short")
        continue
    
    has_methods = bool(METHOD_HEADER.search(text))
    last_content = next((l for l in reversed(lines) if l.strip()), "")
    ends_naturally = bool(NATURAL_END.match(last_content))
    has_doi_refs = bool(DOI_NEAR_END.search("\n".join(lines[-100:])))
    
    if has_methods and (ends_naturally or has_doi_refs or n > 400):
        verdict[fname] = (1, "ok")
    elif has_methods and not ends_naturally and not has_doi_refs and n < 200:
        verdict[fname] = (0, "truncated_methods")
    elif not has_methods:
        verdict[fname] = (0, "no_methods_header")
    else:
        # borderline — large file that ends abruptly but has methods
        # likely refs were cut, methods are intact — still usable
        verdict[fname] = (1, "ok_borderline")

# Write cache
Path("scripts/score2_ocr_verdict.json").write_text(
    json.dumps({k: v[0] for k, v in verdict.items()}, indent=2)
)

# Summary
counts = {0: 0, 1: 0}
reasons = {}
for f, (s, r) in verdict.items():
    counts[s] += 1
    reasons[s] = reasons.get(s, {})
    reasons[s][r] = reasons[s].get(r, 0) + 1

print(f"usable (1): {counts[1]}  needs-re-OCR (0): {counts[0]}  total: {sum(counts.values())}")
for s in (0, 1):
    print(f"\n  Score {s} breakdown:")
    for r, c in sorted(reasons[s].items()):
        print(f"    {r}: {c}")

# List the ones needing re-OCR
print("\n\n=== Needs re-OCR ===")
for f, (s, r) in sorted(verdict.items()):
    if s == 0:
        print(f"  {f}  ({r})")
