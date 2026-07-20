#!/usr/bin/env python3
"""Classify each raw paper markdown by section completeness (Phase 2).

Scores:
  0 — <10 lines, nearly empty
  1 — Has content but no Methods section
  2 — Has Methods but no DOI-bearing reference list
  3 — Full article: Methods + DOI-bearing references

Output: stdout table + scripts/raw_completeness_cache.json
"""
import json, re
from pathlib import Path

RAW = Path("raw/papers")
NUMBERED_PREFIX = r"(?:\d+(?:\.\d+)*\.?\s*)?"
METHOD_RE = re.compile(
    rf"^##+\s*{NUMBERED_PREFIX}(?:material|method[s]?|experimental|"
    rf"expression\s+and\s+puri|crystalli|protein\s+puri|data\s+collection)",
    re.I,
)
DOI_RE = re.compile(r"10\.\d{4,}/[^\s)]+")
REF_SECTION_RE = re.compile(r"^##+\s*(?:reference|acknowledg|author\s+contrib)", re.I)

results = {}

for f in sorted(RAW.glob("*.md")):
    text = f.read_text("utf-8", errors="replace")
    lines = text.splitlines()
    n = len(lines)

    if n < 10:
        results[f.name] = 0
        continue

    has_methods = any(METHOD_RE.match(l) for l in lines)
    has_refs = bool(DOI_RE.search(text[max(0, n - 150) :]))

    if not has_methods:
        results[f.name] = 1
    elif not has_refs:
        results[f.name] = 2
    else:
        results[f.name] = 3

# Cache for downstream tools
Path("scripts/raw_completeness_cache.json").write_text(
    json.dumps(results, indent=2)
)

# Summary
counts = {k: sum(1 for v in results.values() if v == k) for k in (0, 1, 2, 3)}
print(f"0={counts[0]} 1={counts[1]} 2={counts[2]} 3={counts[3]}  total={len(results)}")
print()

# Detail: worst first
for name, score in sorted(results.items(), key=lambda x: x[1]):
    print(f"{score}  {name}")
