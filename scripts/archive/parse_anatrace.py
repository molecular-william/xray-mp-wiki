#!/usr/bin/env python3
"""
Parse Anatrace Detergent Brochure PDF → structured JSON.

Extracts detergent property tables from pages 18-25 of the brochure,
producing a JSON file with product code, name, type, FW, CMC,
aggregation number for each entry.

Output: references/anatrace_detergent_data.json
"""

import json
import re
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PDF_PATH = BASE / "raw" / "miscellaneous" / "Anatrace-Detergents-Brochure.pdf"
OUTPUT_PATH = BASE / "references" / "anatrace_detergent_data.json"

# Approximate column x-positions (from pdfplumber word coordinates)
# ProductNo | PageNo | Name | Type | FW | CMC_mM | CMC_% | AggregationNo
# x0 ranges (empirical from the PDF):
# Col 0 (Product): x0 ~20-85
# Col 1 (Page): x0 ~85-110
# Col 2 (Name): x0 ~110-250
# Col 3 (Type): x0 ~250-270
# Col 4 (FW): x0 ~270-320
# Col 5 (CMC/aggr): x0 ~320-500

# Type codes used in the catalog
TYPE_CODES = {"N": "nonionic", "Z": "zwitterionic", "A": "anionic", "C": "cationic"}


def clean(s):
    """Remove artifact dots/spaces from PDF character-spaced text."""
    if not s:
        return ""
    s = s.strip()
    # Remove trailing dots that are just space-holders in the PDF
    # e.g. "N ." -> "N", "508 .5 ." -> "508.5"
    while s.endswith(".") or s.endswith(" "):
        s = s.rstrip(". ")
    # Remove leading dots e.g. ".56" -> ".56" (keep for now)
    return s


def _join_number(s):
    """Join spaced-out digits: '508 .5' -> '508.5'"""
    # Handle "508 .5" -> "508.5"
    s = re.sub(r"(\d)\s*\.\s*(\d)", r"\1.\2", s)
    # Handle "0 .56" -> "0.56"
    s = re.sub(r"(\d)\s*\.\s*(\d)", r"\1.\2", s)
    return s


def parse_fw(s):
    """Parse molecular weight string, handling 'avg.' and ranges."""
    s = s.strip()
    s = re.sub(r"avg\s*\.?\s*", "", s, flags=re.IGNORECASE).strip()
    s = re.sub(r"~", "", s).strip()
    try:
        return float(s)
    except ValueError:
        return None


def parse_cmc(s):
    """Parse CMC value, returning {'mM': float|None, 'pct': float|None}."""
    result = {"mM": None, "pct": None}
    if not s or s.strip() in ("N/A", "—", "-"):
        return result

    # Remove leading ~
    s = s.replace("~", "").strip()

    # Match patterns like: "0.56 (0.028%)" or "0.56(0.028%)" or "0.56 mM"
    m = re.search(r"([\d.]+)\s*\(?\s*([\d.]+)\s*%\)?", s)
    if m:
        try:
            result["mM"] = float(m.group(1))
            result["pct"] = float(m.group(2))
        except ValueError:
            pass
        return result

    # Plain number
    try:
        result["mM"] = float(s)
    except ValueError:
        pass

    return result


def parse_aggregation(s):
    """Parse aggregation number."""
    if not s or s.strip() in ("N/A", "—", "-"):
        return None
    s = s.replace("~", "").strip()

    # Handle ranges: "75-165"
    m = re.match(r"([\d.]+)\s*[-–]\s*([\d.]+)", s)
    if m:
        return (float(m.group(1)) + float(m.group(2))) / 2

    try:
        return float(s)
    except ValueError:
        return None


def extract_table_rows():
    """Extract all rows from the property table pages."""
    import pdfplumber

    rows = []
    table_pages = list(range(18, 26))  # Pages 18-25 (0-indexed)

    with pdfplumber.open(PDF_PATH) as pdf:
        for pg in table_pages:
            page = pdf.pages[pg]
            words = page.extract_words()

            # Group words into lines by y-position
            lines = defaultdict(list)
            for w in words:
                # Round to nearest 4px for line grouping
                y_key = round(w["top"] / 4) * 4
                lines[y_key].append((w["x0"], w["text"]))

            # Process each line
            for y in sorted(lines):
                line = sorted(lines[y], key=lambda x: x[0])
                line_text = " ".join(w[1] for w in line)

                # Skip headers and metadata
                if any(
                    skip in line_text
                    for skip in [
                        "Product No",
                        "Detergent Properties",
                        "listed alphabetically",
                        "general",
                        "information",
                        "www.anatrace",
                    ]
                ):
                    continue

                # Need at least a product code + some data
                product_candidate = clean(line[0][1])
                if len(product_candidate) < 2 or len(product_candidate) > 12:
                    continue
                if not product_candidate[0].isalpha():
                    continue

                # Parse structured data
                entry = _parse_line(line)
                if entry:
                    rows.append(entry)

    return rows


def _parse_line(line):
    """
    Parse a line of word-position tuples into structured data.

    Actual columns from the PDF (x0 positions):
    0: Product No (x0 ~45)
    1: Page No (x0 ~92-98)
    2: Detergent Name (x0 ~130-349)
    3: Type code (N/Z/A/C) at x0 ~349
    4: FW at x0 ~377-380
    5+: CMC + Aggregation data at x0 ~428-508
    """
    if len(line) < 5:
        return None

    # The text values include artifact dots: "C326 ." means "C326"
    # Strip dots and filter out empty tokens
    tokens = [(x, clean(t)) for (x, t) in line if clean(t)]

    if len(tokens) < 5:
        return None

    product_no = tokens[0][1]
    if not product_no or len(product_no) < 2:
        return None

    # Page number is the second non-empty token
    page_no = tokens[1][1]

    # Find the type code: single letter N/Z/A/C near x0 ~349
    type_idx = None
    type_code = None
    for i, (x, t) in enumerate(tokens):
        t_stripped = t.strip(". ")
        if t_stripped in ("N", "Z", "A", "C") and len(t_stripped) == 1 and 330 < x < 370:
            type_code = t_stripped
            type_idx = i
            break

    if type_code is None or type_idx is None:
        return None

    # Name is everything between page_no (idx 1) and type_code (idx type_idx)
    name_parts = []
    for w in tokens[2:type_idx]:
        name_parts.append(w[1])
    name = " ".join(name_parts).strip(" ,;:-.")
    name = re.sub(r"\s+", " ", name)
    # Remove trailing dots
    name = name.rstrip(". ")

    # Properties come after the type code
    prop_tokens = tokens[type_idx + 1 :]

    # Parse remaining data
    fw_val = None
    cmc_mM = None
    cmc_pct = None
    aggregation = None

    # Reconstruct the properties string, joining spaced-out numbers
    prop_text = " ".join(t[1] for t in prop_tokens)
    prop_text = _join_number(prop_text)

    # Try to parse FW (first number-like token after type code)
    fw_val = None
    for t in prop_tokens:
        t_clean = t[1].replace("~", "").strip()
        t_clean = _join_number(t_clean)
        if t_clean in ("N/A", ""):
            continue
        try:
            v = float(t_clean)
            # FW values are usually > 100 (smallest detergent FW ~180)
            # CMC values are usually < 100 mM (except very soluble ones)
            if v > 100:
                fw_val = v
                break
        except ValueError:
            continue

    # Parse CMC and aggregation from the later columns (x0 > 410)
    cmc_tokens = [t for t in prop_tokens if t[0] > 410]
    cmc_text = " ".join(t[1] for t in cmc_tokens)
    cmc_text = _join_number(cmc_text)

    cmc_mM = None
    cmc_pct = None
    aggregation = None

    # Extract CMC from "~ 1.8 (0.087%)" pattern
    cmc_match = re.search(r"~?\s*([\d.]+)\s*\(?\s*([\d.]+)\s*%\)?", cmc_text)
    if cmc_match:
        try:
            cmc_mM = float(cmc_match.group(1))
            cmc_pct = float(cmc_match.group(2))
        except ValueError:
            pass

    # If no CMC found via pattern, look for a plain number < 1000 at x0 > 410
    if cmc_mM is None:
        for t in cmc_tokens:
            t_clean = t[1].replace("~", "").strip()
            t_clean = _join_number(t_clean)
            if t_clean in ("N/A", ""):
                continue
            try:
                v = float(t_clean)
                if v < 1000 and v > 0:
                    cmc_mM = v
                    break
            except ValueError:
                continue

    # Aggregation number: last "~ N" token, not part of CMC
    for t in reversed(cmc_tokens):
        t_clean = t[1].replace("~", "").strip()
        t_clean = _join_number(t_clean)
        if t_clean in ("N/A", ""):
            continue
        try:
            v = float(t_clean)
            if v >= 1:  # Aggregation numbers are typically > 1
                aggregation = v
                break
        except ValueError:
            continue

    return {
        "product_no": product_no,
        "page_no": page_no,
        "name": name,
        "type": TYPE_CODES.get(type_code, type_code),
        "type_code": type_code,
        "fw": fw_val,
        "cmc_mM": cmc_mM,
        "cmc_pct": cmc_pct,
        "aggregation_no": aggregation,
    }


def main():
    print(f"Parsing {PDF_PATH}...")
    rows = extract_table_rows()
    print(f"Extracted {len(rows)} entries")

    # Deduplicate by product_no (some products appear on multiple pages)
    seen = {}
    for r in rows:
        pn = r["product_no"]
        if pn not in seen:
            seen[pn] = r
        elif seen[pn].get("fw") is None and r.get("fw") is not None:
            seen[pn] = r  # Keep the version with more data

    output = sorted(seen.values(), key=lambda x: x["product_no"])
    print(f"Unique entries: {len(output)}")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, indent=2))
    print(f"Written to {OUTPUT_PATH}")

    # Summary
    with_data = sum(1 for r in output if r["cmc_mM"] is not None or r["cmc_pct"] is not None)
    with_fw = sum(1 for r in output if r["fw"] is not None)
    with_aggr = sum(1 for r in output if r["aggregation_no"] is not None)
    print(f"\n  With CMC: {with_data}")
    print(f"  With FW:  {with_fw}")
    print(f"  With Aggr: {with_aggr}")


if __name__ == "__main__":
    main()
