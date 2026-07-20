#!/usr/bin/env python3
"""Classify score-2 raw paper markdowns: 0=needs re-OCR, 1=usable as-is.

score-2 = has Methods but no DOI-bearing reference list.

Classification:
  0 = needs re-OCR — Methods section absent, OR Methods exists but is an
      empty stub (e.g. "see online version" with no follow-up content).
  1 = usable as-is — Methods has actual detergent/purification/crystallization
      details, even if references after it are partially truncated.
"""

import json
import re
import sys
from pathlib import Path

RAW = Path("raw/papers")
chunk_files = [
    Path("scripts/.score2_chunk_0.txt"),
    Path("scripts/.score2_chunk_1.txt"),
    Path("scripts/.score2_chunk_2.txt"),
]

filenames = []
for cf in chunk_files:
    for line in cf.read_text().splitlines():
        name = line.strip()
        if name:
            filenames.append(name)

METHOD_RE = re.compile(
    r"^##+\s*(?:\d+(?:\.\d+)*\.?\s*)?(?:materials?\s+and\s+methods?|method[s]?|experimental\s*(?:procedures?)?|"
    r"expression\s+and\s+puri|crystalli|protein\s+puri|data\s+collection|"
    r"sample\s+prepar|online\s+methods?|purification|cloning(?:,?\s*expression)?(?:,?\s*and\s*puri)?|"
    r"expression\s+and\s+purif)",
    re.I,
)

DETERGENT_RE = re.compile(
    r"(dodecyl|maltoside|glucoside|sucrose|lauryl|sarcosin|CHAPS|CHAPSO|"
    r"LAPAO|DDM|LMNG|OG|NG|DM|FC[- ]?\d+|fos-choline|cymal|"
    r"Triton|Tween|Brij|octyl|decyl|nonyl|lauryl|sulfobetaine)",
    re.I,
)

SCIENCE_METHODS_RE = re.compile(
    r"(purif|crystalli|chromatograph|concentrat|centrifug|incubat|buffer|"
    r"membrane\s*solubil|affinit|precipitant|imidazol|his-tag|NTA)",
    re.I,
)

EMPTY_STUB_RE = re.compile(
    r"methods?\s+and\s+any\s+associated\s+references?\s+are\s+available\s+in\s+the\s+online",
    re.I,
)

results = []

for fname in sorted(set(filenames)):
    fpath = RAW / fname
    if not fpath.exists():
        results.append((fname, 0, "FILE NOT FOUND"))
        continue

    text = fpath.read_text("utf-8", errors="replace")
    lines = text.splitlines()
    n = len(lines)

    if n < 20:
        results.append((fname, 0, f"Very short ({n} lines)"))
        continue

    # Find first Methods-section header
    method_start = None
    for i, line in enumerate(lines):
        if METHOD_RE.match(line):
            method_start = i
            break

    if method_start is None:
        results.append((fname, 0, "No Methods header"))
        continue

    # Find where this section ends (next top-level ##, ignoring ###)
    method_end = n
    for i in range(method_start + 1, n):
        line = lines[i].strip()
        if re.match(r"^## (?![#])", line):
            method_end = i
            break

    methods_text = "\n".join(lines[method_start:method_end])

    # Check for empty stub ("see online version")
    if EMPTY_STUB_RE.search(methods_text):
        # Maybe there's an Online Methods section later?
        online_start = None
        for i in range(method_end, n):
            if re.match(r"^##+\s*online\s+methods?", lines[i], re.I):
                online_start = i
                break
        if online_start is not None:
            om_end = n
            for i in range(online_start + 1, n):
                lline = lines[i].strip()
                if re.match(r"^## (?![#])", lline):
                    om_end = i
                    break
            om_text = "\n".join(lines[online_start:om_end])
            if DETERGENT_RE.search(om_text) or SCIENCE_METHODS_RE.search(om_text):
                results.append((fname, 1, "Online Methods OK"))
            else:
                results.append((fname, 0, "Online Methods has no content"))
        else:
            # Check if there's real methods content after the stub
            remaining = "\n".join(lines[method_start:])
            if DETERGENT_RE.search(remaining) or SCIENCE_METHODS_RE.search(remaining):
                results.append((fname, 1, "Methods stub but content found"))
            else:
                results.append((fname, 0, "Methods = empty stub"))
        continue

    # Does Methods have real content?
    has_det = bool(DETERGENT_RE.search(methods_text))
    has_sci = bool(SCIENCE_METHODS_RE.search(methods_text))

    if has_det or has_sci:
        parts = []
        if has_det:
            parts.append("detergent")
        if has_sci:
            parts.append("purification/crystallization")
        results.append((fname, 1, ", ".join(parts)))
    else:
        results.append((fname, 0, "Methods header but no real content"))

# Output table
print(f"{'filename':70s} | score | reason")
print("-" * 120)
for fname, score, reason in sorted(results, key=lambda x: (x[1], x[0])):
    print(f"{fname:70s} | {score}     | {reason}")

counts = {0: 0, 1: 0}
for _, s, _ in results:
    counts[s] = counts.get(s, 0) + 1
print(file=sys.stderr)
print(f"Score 0 (needs re-OCR): {counts[0]}", file=sys.stderr)
print(f"Score 1 (usable as-is): {counts[1]}", file=sys.stderr)
print(f"Total: {sum(counts.values())}", file=sys.stderr)

# Save
cache = {fname: score for fname, score, _ in results}
Path("scripts/score2_re_ocr_verdict.json").write_text(json.dumps(cache, indent=2))
