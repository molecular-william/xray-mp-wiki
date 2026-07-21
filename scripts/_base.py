#!/usr/bin/env python3
"""Shared base functionality for wiki page generation.

Provides:
- build_paths(type_name, name) -> (yaml_path, output_path)
- parse_args(argv, type_name, extra_flags) -> (name, dry_run, show_diff, yes, force)
- generate_main(renderer_module, name, yaml_path, output_path, subdir_fn=None)
- Subdirectory finders: find_protein_subdir, find_reagent_subdir, find_method_subdir, find_concept_subdir
- HOST_MAP, normalize_host, normalize_hosts — expression system normalization
- render_frontmatter, maintain_catalog, rebuild_catalog — page rendering helpers
"""

import difflib
import logging
import os
import sys
from pathlib import Path
from typing import Any, Callable, Optional

import yaml

# Fast YAML loader: use CSafeLoader (C libyaml, ~8x faster) when available
try:
    from yaml import CSafeLoader as _FastLoader
    def fast_load_file(path):
        """Load a YAML file using the fastest available loader."""
        return yaml.load(open(path, "rb"), Loader=_FastLoader)
    def fast_load_str(text):
        """Parse a YAML string using the fastest available loader."""
        return yaml.load(text, Loader=_FastLoader)
except ImportError:
    def fast_load_file(path):
        """Load a YAML file using the fastest available loader (fallback)."""
        return yaml.safe_load(open(path))
    def fast_load_str(text):
        """Parse a YAML string using the fastest available loader (fallback)."""
        return yaml.safe_load(text)

def parallel_load_yamls(file_paths, workers=6):
    """Load multiple YAML files in parallel using multiprocessing.
    
    Args:
        file_paths: iterable of Path objects
        workers: number of parallel processes (default 6)
    
    Yields:
        (path, data_or_None) tuples
    """
    import multiprocessing as mp
    
    n_workers = min(workers, len(list(file_paths)) if hasattr(file_paths, '__len__') else workers)
    n_workers = max(1, n_workers)
    
    paths = list(file_paths)
    if n_workers <= 1:
        for p in paths:
            yield _load_one_yaml(p)
        return
    
    with mp.Pool(n_workers) as pool:
        yield from pool.imap_unordered(_load_one_yaml, paths)


# Module-level helper for multiprocessing (must be picklable)
def _load_one_yaml(path):
    """Load a single YAML file, returning (path, data_or_None)."""
    try:
        from yaml import CSafeLoader as _L
        return path, yaml.load(open(path, "rb"), Loader=_L)
    except ImportError:
        try:
            return path, yaml.safe_load(open(path))
        except Exception:
            return path, None
    except Exception:
        return path, None

# Logging: warnings and errors go to stderr; info is silent by default.
# Set env LOG_LEVEL=INFO for verbose mode.
logging.basicConfig(
    level=getattr(logging, os.environ.get("LOG_LEVEL", "WARNING")),
    format="%(levelname)s: %(message)s",
)

# Base directory: one level up from scripts/
# Can be overridden by TEST_BASE_DIR env var for testing
_BASE_DIR = os.environ.get("TEST_BASE_DIR", None)
if _BASE_DIR:
    BASE_DIR = Path(_BASE_DIR)
else:
    BASE_DIR = Path(__file__).parent.parent

# Type -> (yaml_dir, output_dir) mapping
TYPE_PATHS = {
    "protein": ("proteins_yaml", "proteins"),
    "reagent": ("reagents_yaml", "reagents"),
    "method": ("methods_yaml", "methods"),
    "concept": ("concepts_yaml", "concepts"),
}


def build_paths(type_name: str, name: str) -> tuple[Path, Path]:
    """Build (yaml_path, output_path) for a given type and name.

    Args:
        type_name: "protein", "reagent", or "method"
        name: entity name (e.g., "atpcc1", "ddm", "lipidic-cubic-phase")

    Returns:
        (yaml_path, output_path) as Path objects
    """
    if type_name not in TYPE_PATHS:
        print(f"Error: Unknown type '{type_name}'. Must be one of: {', '.join(TYPE_PATHS.keys())}")
        sys.exit(1)

    yaml_dir, output_dir = TYPE_PATHS[type_name]
    yaml_path = BASE_DIR / "xray-mp-wiki" / yaml_dir / f"{name}.yaml"
    output_path = BASE_DIR / "xray-mp-wiki" / output_dir / f"{name}.md"
    return yaml_path, output_path


def parse_args(argv: list[str], type_name: str, extra_flags: Optional[list[str]] = None) -> dict[str, Any]:
    """Parse command-line arguments.

    Args:
        argv: sys.argv[1:]
        type_name: "protein", "reagent", or "method"
        extra_flags: optional list of additional flag names (e.g., ["force"])

    Returns:
        dict with: name, dry_run, show_diff, yes, force (bool)
    """
    if len(argv) < 1:
        flags_str = " ".join(f"[--{f}]" for f in ["dry-run", "diff", "yes"] + (extra_flags or []))
        print(f"Usage: <script> <{type_name}_name> {flags_str}")
        sys.exit(1)

    name = argv[0]
    dry_run = "--dry-run" in argv
    show_diff = "--diff" in argv
    yes = "--yes" in argv
    force = False
    if extra_flags:
        for flag in extra_flags:
            if f"--{flag}" in argv:
                force = True
                break

    return {
        "name": name,
        "dry_run": dry_run,
        "show_diff": show_diff,
        "yes": yes,
        "force": force,
    }


def load_yaml(yaml_path: Path) -> dict:
    """Load and parse a YAML file.

    Args:
        yaml_path: Path to YAML file

    Returns:
        Parsed YAML data dict

    Exits with error if file not found or invalid YAML.
    """
    import yaml  # noqa: E402

    if not yaml_path.exists():
        print(f"Error: YAML file not found: {yaml_path}")
        sys.exit(1)

    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    if data is None:
        print(f"Error: Empty YAML file: {yaml_path}")
        sys.exit(1)

    return data


def _validate_before_render(data, type_name, name):
    """Validate YAML schema before rendering.

    Called from generate_main() after loading YAML.
    Exits with error if validation fails.

    Args:
        data: Parsed YAML dict
        type_name: Entity type (protein/reagent/method/concept)
        name: Entity name for error messages
    """
    from validate_yaml import validate_entity

    # Always strict: reject empty/missing tags and unknown taxonomy tags
    errors = validate_entity(data, type_name, strict=True)
    if errors:
        print(f"Schema validation FAILED for {name} ({type_name}):", file=sys.stderr)
        for i, err in enumerate(errors, 1):
            print(f"  {i}. {err}", file=sys.stderr)
        print(f"\n  {len(errors)} error(s). Fix YAML before generating/updating page.", file=sys.stderr)
        sys.exit(1)


def show_diff(fromfile: str, tofile: str, old_content: str, new_content: str) -> bool:
    """Display unified diff between two content strings.

    Args:
        fromfile: label for old content
        tofile: label for new content
        old_content: existing file content
        new_content: new file content

    Returns:
        True if diff is non-empty, False otherwise
    """
    diff = difflib.unified_diff(
        old_content.splitlines(keepends=True),
        new_content.splitlines(keepends=True),
        fromfile=fromfile,
        tofile=tofile,
    )
    diff_text = "".join(diff)
    if diff_text:
        print(f"--- Diff for {fromfile} ---")
        print(diff_text)
        return True
    return False


def confirm_overwrite(output_path: Path, yes: bool = False) -> bool:
    """Ask user confirmation before overwriting an existing file.

    Args:
        output_path: Path to file
        yes: If True, skip confirmation

    Returns:
        True if user confirms (or --yes given), False otherwise
    """
    if not output_path.exists():
        return True

    if yes:
        return True

    confirm = input(f"File exists: {output_path}. Overwrite? [y/N]: ").strip().lower()
    if confirm != "y":
        print("Aborted.")
        return False
    return True


def write_page(output_path: Path, content: str) -> Path:
    """Write content to file, creating directories as needed.

    Args:
        output_path: Path to write to
        content: String content to write

    Returns:
        output_path
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(content)
    print(f"Generated {output_path}")
    return output_path


def render_frontmatter(data: dict, entity_type: str, category: str) -> str:
    """Render YAML frontmatter for any entity type.

    Args:
        data: Parsed YAML dict
        entity_type: "protein", "reagent", "method", or "concept"
        category: "proteins", "reagents", "methods", or "concepts"

    Returns:
        Frontmatter string
    """
    from datetime import datetime

    lines = ["---"]
    lines.append(f'title: "{data["title"]}"')
    lines.append(f"created: {data.get('created', datetime.now().strftime('%Y-%m-%d'))}")
    lines.append(f"updated: {data.get('updated', datetime.now().strftime('%Y-%m-%d'))}")
    lines.append(f"type: {entity_type}")
    lines.append(f"category: {category}")
    lines.append("layout: default")
    tags = data.get("tags", [])
    lines.append(f"tags: [{', '.join(tags)}]")
    sources = data.get("sources", [])
    lines.append(f"sources: [{', '.join(sources)}]")
    verified = data.get("verified", "none")
    if isinstance(verified, bool):
        verified_tier = "agent" if verified else "none"
    else:
        verified_tier = verified if verified in ("none", "regex", "agent", "human") else "none"
    lines.append(f"verified: {verified_tier}")
    uniprot = data.get("uniprot_id", "")
    if uniprot:
        # Normalize for frontmatter: extract accessions from object list
        if isinstance(uniprot, list) and uniprot and isinstance(uniprot[0], dict):
            accs = [u.get("accession", "") for u in uniprot if u.get("accession")]
            if accs:
                lines.append(f"uniprot_id: {accs}")
        else:
            lines.append(f"uniprot_id: {uniprot}")
    lines.append("---")
    return "\n".join(lines)


def _extract_catalog_markers(content):
    """Extract start/end indices for catalog section in index.md.

    Handles both marker formats:
    - Start: '<!-- WIKI CATALOG' (no trailing -->)
    - End: 'END WIKI CATALOG -->' (no leading <!--)
    """
    # Try the actual format used in index.md
    start_marker = "<!-- WIKI CATALOG"
    end_marker = "END WIKI CATALOG -->"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx + len(start_marker)) if start_idx >= 0 else -1

    # Fallback: try with full markers
    if start_idx == -1 or end_idx == -1:
        start_marker = "<!-- WIKI CATALOG -->"
        end_marker = "<!-- END WIKI CATALOG -->"
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker, start_idx + len(start_marker)) if start_idx >= 0 else -1

    if start_idx >= 0 and end_idx >= 0:
        return start_idx, end_idx, start_marker, end_marker
    return -1, -1, "", ""


def maintain_catalog(type_name: str, name: str, title: str, summary: str, output_path: Path) -> bool:
    """Maintain the wiki catalog section in index.md.

    Adds or updates the entry for a given entity in the catalog table.
    The catalog is a markdown table between <!-- WIKI CATALOG --> markers.

    Args:
        type_name: Entity type ("protein", "reagent", "method", "concept")
        name: Entity name
        title: Human-readable title
        summary: One-line description
        output_path: Path to the generated/updated page

    Returns:
        True if catalog was updated, False otherwise
    """
    index_path = BASE_DIR / "xray-mp-wiki" / "index.md"
    if not index_path.exists():
        logging.warning("index.md not found at %s, skipping catalog update", index_path)
        return False

    with open(index_path) as f:
        content = f.read()

    start_idx, end_idx, start_marker, end_marker = _extract_catalog_markers(content)

    if start_idx == -1 or end_idx == -1:
        logging.warning("Catalog markers not found in index.md, skipping update")
        return False

    # Extract existing catalog lines
    catalog_section = content[start_idx + len(start_marker) : end_idx]
    lines = catalog_section.strip().split("\n") if catalog_section.strip() else []

    # Find the header row and separator row
    header_idx = 0
    sep_idx = 1
    if len(lines) >= 2 and "|" in lines[0] and "---" in lines[1]:
        header_idx = 0
        sep_idx = 1
    else:
        # No header found, add one
        lines = ["| type | path | title | summary |", "|------|------|-------|---------|"]
        header_idx = 0
        sep_idx = 1

    # Build the new entry row
    # Path is relative to wiki root, e.g., "proteins/bmrA/"
    rel_path = str(output_path.relative_to(BASE_DIR / "xray-mp-wiki"))
    # Remove .md extension if present, ensure single trailing slash
    if rel_path.endswith(".md"):
        rel_path = rel_path[:-3]
    if not rel_path.endswith("/"):
        rel_path += "/"

    new_row = f"| {type_name} | {rel_path} | {title} | {summary} |"

    # Check if entry already exists (match on path column)
    existing_row_idx = None
    for i, line in enumerate(lines):
        if i <= sep_idx:
            continue
        if rel_path in line:
            existing_row_idx = i
            break

    if existing_row_idx is not None:
        # Replace existing entry
        lines[existing_row_idx] = new_row
    else:
        # Append new entry
        lines.append(new_row)

    # Sort data rows by path (after separator row)
    header = lines[header_idx]
    sep = lines[sep_idx]
    data_rows = lines[sep_idx + 1 :]
    # Filter out empty lines and sort by path (column 2), skip malformed rows
    valid_rows = [r for r in data_rows if r.strip() and len(r.split("|")) >= 3]
    data_rows = sorted(valid_rows, key=lambda x: x.split("|")[2].strip())

    new_catalog = "\n".join([header, sep] + data_rows)

    # Rebuild content
    new_content = content[: start_idx + len(start_marker)] + "\n" + new_catalog + "\n" + content[end_idx:]

    with open(index_path, "w") as f:
        f.write(new_content)

    return True


def generate_main(
    renderer_module,
    name: str,
    yaml_path: Path,
    output_path: Path,
    subdir_fn: Optional[Callable] = None,
    skip_catalog: bool = False,
) -> None:
    """Execute a generate script's main flow.

    Args:
        renderer_module: The renderer module (e.g., protein_page_renderer)
        name: Entity name
        yaml_path: Path to YAML input
        output_path: Path to output file
        subdir_fn: Optional function to adjust output_path (for methods with subdirs)

    Returns:
        None (exits on error)
    """
    if subdir_fn:
        output_path = subdir_fn(yaml_path, output_path, name)

    # Load YAML
    data = load_yaml(yaml_path)

    # Determine entity type from renderer module name
    type_name = renderer_module.__name__.replace("_renderer", "").replace("generate_", "").replace("update_", "")
    if "_page_renderer" in renderer_module.__name__:
        type_name = renderer_module.__name__.split("_")[0]
    else:
        for t in TYPE_PATHS:
            if t in yaml_path.parts:
                type_name = t
                break

    # Validate schema before rendering
    _validate_before_render(data, type_name, name)

    # Generate page
    page = renderer_module.generate_page(data)

    # Dry run
    if "--dry-run" in sys.argv[1:]:
        print(f"# Generated page for {name} (dry run)")
        print(f"# YAML: {yaml_path}")
        print(f"# Output: {output_path}")
        print("=" * 60)
        print(page)
        return

    # Show diff if requested and page exists
    if "--diff" in sys.argv[1:] and output_path.exists():
        with open(output_path) as f:
            existing = f.read()
        has_diff = show_diff(name, name, existing, page)
        if not has_diff:
            print("No changes detected.")
            return

    # Safety: confirm overwrite
    if not confirm_overwrite(output_path, "--yes" in sys.argv[1:]):
        return

    # Write output
    write_page(output_path, page)

    # Update wiki catalog
    title = data.get("title", name)
    summary = data.get("overview", "")[:80] if data.get("overview") else ""
    if not summary:
        # Fallback: extract from page content
        lines = page.split("\n")
        for line in lines:
            if line.startswith("# "):
                summary = line[2:82]
                break
    if not summary:
        summary = f"{type_name.capitalize()}: {name}"
    if not skip_catalog:
        maintain_catalog(type_name, name, title, summary, output_path)


# ─── Expression host normalization (shared between wiki_query and renderer) ────

# Canonical host map: lowercase key → canonical display name
HOST_MAP: dict[str, str] = {
    "e. coli": "E. coli",
    "escherichia": "E. coli",
    "bl21": "E. coli",
    "dh5": "E. coli",
    "sf9": "Sf9",
    "sf21": "Sf9",
    "spodoptera": "Sf9",
    "baculovirus": "Sf9",
    "insect": "Sf9",
    "hek": "HEK293",
    "hek293": "HEK293",
    "human embryonic kidney": "HEK293",
    "pichia": "P. pastoris",
    "p. pastoris": "P. pastoris",
    "saccharomyces": "S. cerevisiae",
    "cerevisiae": "S. cerevisiae",
    "lactococcus": "L. lactis",
    "l. lactis": "L. lactis",
    "thermus": "T. thermophilus",
    "t. thermophilus": "T. thermophilus",
    "mammalian": "Mammalian",
    "cho": "Mammalian",
    "cos": "Mammalian",
    "cell-free": "Cell-free",
    "in vitro": "Cell-free",
    "native": "Native tissue",
}


def normalize_host(sys_str: str) -> str:
    """Normalize an expression system string to its canonical host name.

    Maps common variations (e.g. 'bl21', 'escherichia') to one display name
    (e.g. 'E. coli'). Returns the first matching canonical host.
    """
    sl = sys_str.lower()
    for key, host in HOST_MAP.items():
        if key in sl:
            return host
    parts = sys_str.split()
    return parts[0].capitalize() if parts else "Other"


def normalize_hosts(sys_str: str) -> list[str]:
    """Normalize expression system string to ALL matching canonical hosts.

    Unlike normalize_host() which returns the first match, this returns
    every matching host (for rendering multiple badges).
    """
    sl = sys_str.lower()
    results: list[str] = []
    seen: set[str] = set()
    for key, host in HOST_MAP.items():
        if key in sl and host not in seen:
            seen.add(host)
            results.append(host)
    return results


# ─── Method subdirectory ──────────────────────────────────────


def find_method_subdir(yaml_data: dict, method_name: str) -> Optional[str]:
    """Detect the subdirectory for a method page.

    Tries:
    1. explicit 'subdirectory-*' tag in tags list (e.g., subdirectory-crystallization)
    2. tags with known method prefixes (crystallization-, purification-, etc.)
    3. scans existing methods subdirectories for a matching file

    Args:
        yaml_data: Parsed YAML data
        method_name: Method name

    Returns:
        Subdirectory name or None
    """
    # Valid method subdirectories
    VALID_SUBDIRS = {
        "crystallization",
        "expression-systems",
        "purification",
        "structure-determination",
        "quality-assessment",
        "solubilization",
        "cell-lysis",
    }

    # Check for explicit subdirectory-* tag (highest priority)
    tags = yaml_data.get("tags", [])
    for tag in tags:
        if tag.startswith("subdirectory-"):
            candidate = tag[len("subdirectory-") :]
            if candidate in VALID_SUBDIRS:
                return candidate

    # Check method-specific tag prefixes
    METHOD_TAG_TO_SUBDIR = {
        "crystallization-": "crystallization",
        "crystallization-lcp": "crystallization",
        "crystallization-vapor-diffusion": "crystallization",
        "expression-": "expression-systems",
        "purification-": "purification",
        "purification-method": "purification",
        "purification-size-exclusion": "purification",
        "structure-": "structure-determination",
        "quality-": "quality-assessment",
        "solubilization-": "solubilization",
    }
    for tag in tags:
        for prefix, subdir in METHOD_TAG_TO_SUBDIR.items():
            if tag.startswith(prefix):
                return subdir

    # Scan existing directories
    methods_dir = BASE_DIR / "xray-mp-wiki" / "methods"
    if methods_dir.exists():
        for subdir in methods_dir.iterdir():
            if subdir.is_dir():
                candidate = subdir / f"{method_name}.md"
                if candidate.exists():
                    return subdir.name

    return None


# ─── Reagent subdirectory ─────────────────────────────────────


def find_reagent_subdir(yaml_data: dict, reagent_name: str) -> Optional[str]:
    """Detect the subdirectory for a reagent page.

    Tries:
    1. explicit 'subdirectory-*' tag in tags list (e.g., subdirectory-detergents)
    2. tags with known reagent prefixes (detergent-, buffer-, ligand-, etc.)
    3. scans existing reagent subdirectories for a matching file

    Args:
        yaml_data: Parsed YAML data
        reagent_name: Reagent name

    Returns:
        Subdirectory name or None
    """
    # Valid reagent subdirectories
    VALID_SUBDIRS = {
        "detergents",
        "lipids",
        "buffers",
        "additives",
        "ligands",
        "protein-tags",
        "antibodies",
        "cofactors",
        "antibiotics",
        "substrates",
    }

    # Check for explicit subdirectory-* tag (highest priority)
    tags = yaml_data.get("tags", [])
    for tag in tags:
        if tag.startswith("subdirectory-"):
            candidate = tag[len("subdirectory-") :]
            if candidate in VALID_SUBDIRS:
                return candidate

    # Check reagent-specific tag prefixes
    TAG_TO_SUBDIR = {
        "detergent-": "detergents",
        "detergent-nonionic": "detergents",
        "detergent-zwitterionic": "detergents",
        "detergent-mild": "detergents",
        "detergent": "detergents",
        "solubilization-detergent": "detergents",
        "lipid": "lipids",
        "membrane-lipid": "lipids",
        "mitochondrial-lipid": "lipids",
        "buffer-": "buffers",
        "additive-": "additives",
        "additive-stabilizer": "additives",
        "crystallization-precipitant": "additives",
        "ligand": "ligands",
        "cofactor": "cofactors",
        "antibiotic": "antibiotics",
        "substrate": "substrates",
        "protein-tag": "protein-tags",
        "antibody": "antibodies",
    }
    for tag in tags:
        for prefix, subdir in TAG_TO_SUBDIR.items():
            if tag.startswith(prefix):
                return subdir

    # Scan existing directories
    reagents_dir = BASE_DIR / "xray-mp-wiki" / "reagents"
    if reagents_dir.exists():
        for subdir in reagents_dir.iterdir():
            if subdir.is_dir():
                candidate = subdir / f"{reagent_name}.md"
                if candidate.exists():
                    return subdir.name

    return None


# ─── Protein subdirectory mapping (from mpstruc classification) ────

PROTEIN_SUBDIR_MAP = {
    "gpcr": [
        "G Protein-Coupled Receptors: Class A",
        "G Protein-Coupled Receptors: Class B1",
        "G Protein-Coupled Receptors: Class B2",
        "G Protein-Coupled Receptors: Class C",
        "G Protein-Coupled Receptors: Class D",
        "G Protein-Coupled Receptors: Class F",
        "G Protein-Coupled Receptors: Class T",
    ],
    "rhodopsins": [
        "Bacterial, Algal, Viral, and Unusual Rhodopsins",
    ],
    "voltage-gated-channels": [
        "Channels: Potassium, Sodium, & Proton Ion-Selective",
        "Channels: Calcium Ion-Selective",
        "Channels: Transient Receptor Potential (TRP)",
        "Channels:  Mechanosensitive",
        "Channels: Gap Junctions and Related Channels",
        "Channels:  Intercellular",
    ],
    "cys-loop-receptors": [
        "Cys-Loop Receptor Family",
    ],
    "other-ion-channels": [
        "Channels: Other Ion Channels",
        "Channels: Aquaporins and Glyceroporins",
        "Channels: Amt/Mep/Rh proteins",
        "Channels: Urea Transporters",
        "Channels: Fluc Family",
        "Channels : Formate/Nitrite Transporter (FNT) Family",
    ],
    "abc-transporters": [
        "ATP Binding Cassette (ABC) Transporters",
        "Multi-Drug Efflux Transporters",
    ],
    "mfs-transporters": [
        "Major Facilitator Superfamily (MFS) Transporters",
    ],
    "slc-transporters": [
        "Solute Carrier (SLC) Transporter Superfamily",
        "Solute Sodium Symporter (SSS) Family",
        "Amino Acid Secondary Transporters",
        "Amino Acid/Polyamine/Organocation (APC) Superfamily",
        "Betaine/Choline/Carnitine Transporter (BCCT) Family",
        "Ca<sup>2+</sup>:Cation Antiporter (CaCA) Family",
        "Nucleobase-Cation-Symport-1 (NCS1) Family",
        "Nucleobase-Cation-Symport-2 (NCS2) Family",
        "Apical Sodium-Dependent Bile Acid Transporters (ASBT)",
        "Solute Carrier Family 4 (anion exchanger)",
        "Cation Diffusion Facilitator (CDF) Family",
        "Drug/Metabolite Transporter (DMT) Superfamily",
        "Sulfate-Uptake Transporters/Permeases",
        "AbgT Family of Transporters",
        "H<sup>+</sup>/Cl<sup>-</sup> or F<sup>-</sup> Exchange Transporters",
        "Antiporters",
        "CorA Superfamily Ion Transporters",
        "Cyclin M/CorC Family of Mg<sup>2+</sup> Transporters",
    ],
    "pumps-atpases": [
        "F-type ATPase",
        "P-type ATPase",
        "Vacuolar ATPase (V-ATPase)",
        "Bacterial V-type ATPase",
        "Membrane-Integral Pyrophosphatases (M-PPases)",
        "Superfamily of K<sup>+</sup> Transporters (SKT proteins)",
        "Energy-Coupling Factor (ECF) Transporters",
        "Vacuolar Iron Transporter (VIT) Family",
    ],
    "secretion-translocon": [
        "Sec, Translocase, and Insertase Proteins",
        "Type VII Secretion Systems",
        "Shape, Elongation, Division, and Sporulation (SEDS) Proteins",
        "AAA-ATPAse Membrane Translocators",
        "Bacterial Cell Divison Proteins",
    ],
    "photosynthesis": [
        "Photosystems",
        "Photosystem+Light-Harvesting Complex Supercomplex",
        "Light-Harvesting Complexes",
        "Light-Harvesting+Reaction Center Complexes",
        "Photosynthetic Reaction Centers",
        "Photoprotection Proteins",
    ],
    "enzymes": [
        "Oxidoreductases",
        "Hydrolases",
        "Transferases",
        "Lyases",
        "Isomerases",
        "Ligases",
        "Membrane-Bound Multi-Enzyme Complexes",
        "Soluble Multi-Enzyme Complexes",
        "Mucin Family of Membrane-Bound O-Glycosyltransferases",
        "Cytochrome bc1 Complex",
        "Cytochrome b6f Complex",
        "Cytochrome c Oxidase (Mitochondrial)",
        "Cytochrome c Oxidase (Bacterial)",
        "Cytochrome bd Oxidase",
        "Alternative Complex III",
        "Alternative Oxidase",
        "NADH Dehydrogenase (Complex I)",
        "Succinate Dehydrogenase (Complex II)",
        "Succinate Dehydrogenase (Complex II) + Complex II-like",
        "Succinate Dehydrogenase (Complex II): Fumarate Reductase",
        "Cytochrome P450",
    ],
    "porins-beta-barrel": [
        "Porins",
        "Porin: Autotransporter",
        "Porin: General Bacterial Porin",
        "Porin: Monomeric and Multimeric",
        "Porin: Outer Membrane Factor (OMF)",
        "Porin: OmpA-like",
        "Porin: Outer Membrane Phospholipase A1",
        "Porin: Outer Membrane Protein Insertion Machinery (BAM)",
    ],
    "miscellaneous": [
        "Miscellaneous",
        "Mitochondrial Membrane Proteins: Other",
        "Outer Membrane Proteins: Lipocalin Family",
        "Mitochondrial membrane proteins - other",
        "Lipoproteins and Lipid-Anchored Proteins",
        "Membrane-Anchored/Associated Proteins",
        "Soluble Proteins in MP-structures",
    ],
    "coiled-coil": [
        "Membrane-Anchored Coiled-Coil Proteins",
    ],
    "membrane-penetrating": [
        "Membrane-Penetrating Proteins (Toxins and Effectors)",
    ],
}

# Build reverse mapping: subgroup → protein subdirectory
_SUBGROUP_TO_PROTEIN_SUBDIR: dict[str, str] = {}
for subdir, subgroups in PROTEIN_SUBDIR_MAP.items():
    for sg in subgroups:
        _SUBGROUP_TO_PROTEIN_SUBDIR[sg] = subdir


def find_protein_subdir(yaml_data: dict, protein_name: str) -> Optional[str]:
    """Detect the subdirectory for a protein page from mpstruc classification.

    Uses the mpstruc_classification.subgroup field added by
    enrich_protein_classification.py. Falls back to 'miscellaneous' as default.

    Args:
        yaml_data: Parsed YAML data
        protein_name: Protein name (unused, kept for interface consistency)

    Returns:
        Subdirectory name or 'miscellaneous'
    """
    m = yaml_data.get("mpstruc_classification", {})
    if m:
        subgroup = m.get("subgroup", "")
        if subgroup:
            # Check for exact match first
            if subgroup in _SUBGROUP_TO_PROTEIN_SUBDIR:
                return _SUBGROUP_TO_PROTEIN_SUBDIR[subgroup]
            # Check for partial match
            for sg_pattern, subdir in _SUBGROUP_TO_PROTEIN_SUBDIR.items():
                if sg_pattern.lower() in subgroup.lower() or subgroup.lower() in sg_pattern.lower():
                    return subdir
    return None


# ─── Concept subdirectory ─────────────────────────────────────

CONCEPT_TAG_TO_SUBDIR = {
    "concept-transport-mechanism": "transport-mechanisms",
    "concept-protein-family": "protein-families",
    "concept-membrane-mimetic": "membrane-mimetics",
    "concept-crystallography-principle": "methods-techniques",
    "concept-construct-design": "construct-design",
    "concept-functional": "miscellaneous",
    "concept-antibody-technology": "miscellaneous",
    "concept-structural": "structural-mechanisms",
    "concept-enzyme-mechanism": "enzyme-mechanisms",
}

CONCEPT_DIRECT_MAP = {
    "transport-mechanisms": "transport-mechanisms",
    "signaling-receptors": "signaling-receptors",
    "structural-mechanisms": "structural-mechanisms",
    "protein-families": "protein-families",
    "enzyme-mechanisms": "enzyme-mechanisms",
    "rhodopsin-mechanisms": "rhodopsin-mechanisms",
    "membrane-mimetics": "membrane-mimetics",
    "methods-techniques": "methods-techniques",
    "construct-design": "construct-design",
    "miscellaneous": "miscellaneous",
}


def find_concept_subdir(yaml_data: dict, concept_name: str) -> Optional[str]:
    """Detect the subdirectory for a concept page from its tags.

    Uses the subdirectory-* tag added by the classification script.
    Falls back to 'miscellaneous' as default.

    Args:
        yaml_data: Parsed YAML data
        concept_name: Concept name

    Returns:
        Subdirectory name or 'miscellaneous'
    """
    tags = yaml_data.get("tags", [])
    for tag in tags:
        if tag.startswith("subdirectory-"):
            candidate = tag[len("subdirectory-") :]
            if candidate in CONCEPT_DIRECT_MAP:
                return candidate
    for tag in tags:
        if tag in CONCEPT_TAG_TO_SUBDIR:
            return CONCEPT_TAG_TO_SUBDIR[tag]
    return "miscellaneous"


# ─── Rebuild catalog entry point ─────────────────────────────


# ─── Catalog table management ──────────────────────────────────────


def rebuild_catalog(entries, force=False):
    """Rebuild wiki catalog table in index.md.

    Scans category directories, reads frontmatter, builds table rows,
    and inserts into index.md. Works with maintain_catalog() (which
    handles single-entry updates) but covers the full table rebuild.

    Args:
        entries: list of dicts with keys: rel_path, rel_url, title, summary, type_name
        force: if True, rebuild entire table from scratch. If False, merge (add only missing).

    Returns:
        Number of new entries added
    """
    index_path = BASE_DIR / "xray-mp-wiki" / "index.md"
    if not index_path.exists():
        print(f"Error: index.md not found at {index_path}")
        return 0

    with open(index_path) as f:
        content = f.read()

    start_idx, end_idx, start_marker, end_marker = _extract_catalog_markers(content)

    if start_idx == -1 or end_idx == -1:
        print(f"Error: Catalog markers not found in {index_path}")
        return 0

    # Build the catalog table
    header = "| type | path | title | summary |"
    sep = "|------|------|-------|---------|"

    if force:
        # Start fresh — build entire table from entries
        data_rows = []
        added = 0
        for entry in entries:
            row = f"| {entry['type_name']} | {entry['rel_url']} | {entry['title']} | {entry['summary']} |"
            data_rows.append(row)
            added += 1
    else:
        # Merge mode — keep existing entries, add only missing ones
        existing_header, existing_sep, existing_rows, existing_paths = _get_existing_catalog_lines(content, index_path)
        if existing_header is None:
            existing_header = header
            existing_rows = []
            existing_paths = set()

        data_rows = list(existing_rows)  # Preserve existing entries
        added = 0
        for entry in entries:
            if entry["rel_url"] not in existing_paths:
                row = f"| {entry['type_name']} | {entry['rel_url']} | {entry['title']} | {entry['summary']} |"
                data_rows.append(row)
                added += 1

    # Sort data rows by path column (column 2)
    data_rows.sort(key=lambda r: r.split("|")[2].strip())

    catalog_table = "\n".join([header, sep] + data_rows)

    # Rebuild content
    new_content = content[: start_idx + len(start_marker)] + "\n" + catalog_table + "\n" + content[end_idx:]

    with open(index_path, "w") as f:
        f.write(new_content)

    return added


def _get_existing_catalog_lines(content, index_path):
    """Read existing catalog data rows from index.md content string.

    Args:
        content: Full index.md content string
        index_path: Path to index.md (for error messages)

    Returns:
        (header, sep, data_rows, existing_paths) or (None, None, [], set()) if not found
    """
    start_idx, end_idx, start_marker, end_marker = _extract_catalog_markers(content)

    if start_idx == -1 or end_idx == -1:
        return None, None, [], set()

    catalog_section = content[start_idx + len(start_marker) : end_idx]
    lines = catalog_section.strip().split("\n") if catalog_section.strip() else []

    # Find header and separator rows
    header_idx = -1
    sep_idx = -1
    for i, line in enumerate(lines):
        if "|" in line and line.startswith("|"):
            header_idx = i
            break
    for i in range(header_idx + 1, len(lines)):
        if "---" in lines[i] and "|" in lines[i]:
            sep_idx = i
            break

    if header_idx == -1 or sep_idx == -1:
        return None, None, [], set()

    header = lines[header_idx]
    sep = lines[sep_idx]

    # Extract data rows and paths
    data_rows = []
    existing_paths = set()
    for line in lines[sep_idx + 1 :]:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 3:
            path_col = parts[2]  # path column
            if path_col:
                existing_paths.add(path_col)
                data_rows.append(line)

    return header, sep, data_rows, existing_paths


def collect_pages():
    """Scan all category directories, return list of entry dicts for catalog.

    Reads manifest's entity_index for titles (fast — avoids reading every .md).
    Falls back to reading .md frontmatter for pages not in the manifest.

    Returns:
        List of dicts with keys: rel_path, rel_url, title, summary, type_name
    """
    import json as _json
    import re as _re

    import yaml as _yaml

    wiki_dir = BASE_DIR / "xray-mp-wiki"
    categories = ["proteins", "reagents", "methods", "concepts"]
    type_paths = {
        "protein": ("proteins_yaml", "proteins"),
        "reagent": ("reagents_yaml", "reagents"),
        "method": ("methods_yaml", "methods"),
        "concept": ("concepts_yaml", "concepts"),
    }

    # Load manifest entity_index for fast title lookup
    manifest_path = BASE_DIR / "wiki_manifest.json"
    manifest_index = {}
    if manifest_path.exists():
        try:
            with open(manifest_path) as f:
                mf = _json.load(f)
            manifest_index = mf.get("entity_index", {})
        except Exception:
            pass

    entries = []

    for cat in categories:
        cat_dir = wiki_dir / cat
        if not cat_dir.is_dir():
            continue

        for md in cat_dir.rglob("*.md"):
            if md.name in ("index.md", "SCHEMA.md"):
                continue

            rel_path = str(md.relative_to(wiki_dir))
            rel_url = rel_path.replace(".md", "/")

            stem = md.stem
            entity_type = cat.rstrip("s")

            # Get title from manifest (fast), fall back to reading .md
            manifest_entry = manifest_index.get(stem, {})
            title = manifest_entry.get("title", "")

            summary = ""
            if not title:
                with open(md, "r", encoding="utf-8") as f:
                    fm_content = f.read()
                fm_match = _re.match(r"^---\s*\n(.*?)\n---\s*", fm_content, _re.DOTALL)
                fm = {}
                if fm_match:
                    try:
                        fm = _yaml.safe_load(fm_match.group(1)) or {}
                    except Exception:
                        pass
                title = fm.get("title") or _extract_title_from_body(fm_content) or stem.replace("-", " ").title()

                # Try to get summary from YAML
                yaml_dir, _ = type_paths.get(entity_type, (None, None))
                if yaml_dir:
                    yaml_path = wiki_dir / yaml_dir / f"{stem}.yaml"
                    if yaml_path.exists():
                        try:
                            with open(yaml_path) as f:
                                ydata = _yaml.safe_load(f)
                            if ydata and "overview" in ydata:
                                summary = str(ydata["overview"])[:80]
                        except Exception:
                            pass
            else:
                # Title from manifest — get overview from YAML for summary
                yaml_dir, _ = type_paths.get(entity_type, (None, None))
                if yaml_dir:
                    yaml_path = wiki_dir / yaml_dir / f"{stem}.yaml"
                    if yaml_path.exists():
                        try:
                            with open(yaml_path) as f:
                                ydata = _yaml.safe_load(f)
                            if ydata and "overview" in ydata:
                                summary = str(ydata["overview"])[:80]
                        except Exception:
                            pass

            if not summary:
                summary = f"{entity_type.capitalize()}: {stem}"

            entries.append(
                {
                    "rel_path": rel_path,
                    "rel_url": rel_url,
                    "title": title,
                    "summary": summary,
                    "type_name": entity_type,
                }
            )

    # Sort by relative path for consistent ordering
    entries.sort(key=lambda e: e["rel_path"])
    return entries


def _extract_title_from_body(content):
    """Extract title from first H1 heading in body content."""
    for line in content.split("\n"):
        if line.startswith("# ") and not line.startswith("## "):
            return line[2:].strip()
    return None
