"""
Pytest shared fixtures for xray-mp-wiki scripts tests.

All generation/validation tests use subprocess with TEST_BASE_DIR env var
pointing to a temporary directory. WikiQuery tests import directly and
operate on real project data (read-only).
"""

import json
import os
import sys
from pathlib import Path

import pytest

# Project root (real) — ensure scripts is importable as a package
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ---------------------------------------------------------------------------
# Fixtures for subprocess tests (generation, validation)
# ---------------------------------------------------------------------------


@pytest.fixture
def tmp_project(tmp_path):
    """Create a temporary project with test YAML files for subprocess tests.

    Sets TEST_BASE_DIR env var so _base.py uses the temp dir.
    Returns dict with paths: base, wiki, raw, ref, yaml_dirs, output_dirs.
    """
    wiki = tmp_path / "xray-mp-wiki"
    raw = tmp_path / "raw" / "papers"
    ref = tmp_path / "references"

    yaml_dirs = {}
    output_dirs = {}
    for t in ["proteins", "reagents", "methods", "concepts"]:
        (wiki / f"{t}_yaml").mkdir(parents=True)
        (wiki / t).mkdir(parents=True)
        yaml_dirs[t] = wiki / f"{t}_yaml"
        output_dirs[t] = wiki / t

    raw.mkdir(parents=True)
    ref.mkdir(parents=True)

    # Raw paper (for manifest tests)
    (raw / "10.1038##test123.md").write_text("# Test Paper\nSome content.\n")

    # index.md with catalog markers
    (wiki / "index.md").write_text(
        "---\ntitle: Wiki Index\n---\n"
        "# Membrane Protein Structure Wiki\n\n"
        "<!-- WIKI CATALOG\n"
        "| type | path | title | summary |\n"
        "|------|------|-------|---------|\n"
        "END WIKI CATALOG -->\n"
    )

    # Write test YAMLs
    _write_test_yamls(yaml_dirs)

    # Write DDM reagent (needed for cross-ref resolution)
    (yaml_dirs["reagents"] / "ddm.yaml").write_text(
        'title: "n-Dodecyl-beta-D-maltopyranoside (DDM)"\n'
        'created: "2026-06-18"\n'
        'updated: "2026-06-18"\n'
        "tags:\n"
        "  - detergent-nonionic\n"
        "  - subdirectory-detergents\n"
        "sources:\n"
        '  - "doi/10.1016##ddm001"\n'
        'overview: "DDM is a mild non-ionic detergent."\n'
    )

    # Write catalog for enrichment tests
    test_catalog = {
        "test_protein": {"type": "proteins", "title": "Test Protein", "filename": "test_protein.md"},
        "ddm": {"type": "reagents", "title": "DDM", "filename": "ddm.md"},
    }
    (ref / "entity_catalog.json").write_text(json.dumps(test_catalog))

    paths = {
        "base": tmp_path,
        "wiki": wiki,
        "raw": raw,
        "ref": ref,
        "yaml": yaml_dirs,
        "output": output_dirs,
        "index": wiki / "index.md",
    }

    return paths


def _write_test_yamls(yd):
    """Write canonical test YAMLs for all 4 entity types."""
    # Protein
    (yd["proteins"] / "test_protein.yaml").write_text(
        'title: "Test Protein"\n'
        'created: "2026-06-18"\n'
        'updated: "2026-06-18"\n'
        "tags:\n"
        "  - transporter\n"
        "  - membrane-protein\n"
        "sources:\n"
        '  - "doi/10.1038##test123"\n'
        'overview: "A test protein for unit testing."\n'
        "publications:\n"
        '  - source: "doi/10.1038##test123"\n'
        "    structures:\n"
        '      - pdb_id: "1ABC"\n'
        '        resolution: "2.5"\n'
        '        space_group: "P2_1"\n'
        "    purifications:\n"
        '      - source: "doi/10.1038##test123"\n'
        "        steps:\n"
        '          - step: "Affinity"\n'
        '            method: "Ni-NTA chromatography"\n'
        '            resin: "Ni-NTA"\n'
        '            buffer: "50 mM Tris pH 8.0"\n'
        '            notes: ""\n'
        "cross_references:\n"
        '  - path: "/xray-mp-wiki/reagents/detergents/ddm/"\n'
        '    title: "DDM"\n'
        '    reason: "Used in purification"\n'
    )
    # Reagent
    (yd["reagents"] / "test_reagent.yaml").write_text(
        'title: "Test Detergent"\n'
        'created: "2026-06-18"\n'
        'updated: "2026-06-18"\n'
        "tags:\n"
        "  - detergent-nonionic\n"
        "  - subdirectory-detergents\n"
        "sources:\n"
        '  - "doi/10.1016##test456"\n'
        'overview: "A test detergent for unit testing."\n'
        "uses:\n"
        '  - title: "Test Use"\n'
        '    content: "Used in membrane protein purification."\n'
    )
    # Method
    (yd["methods"] / "test_method.yaml").write_text(
        'title: "Test Method"\n'
        'created: "2026-06-18"\n'
        'updated: "2026-06-18"\n'
        "tags:\n"
        "  - crystallization-vapor-diffusion\n"
        "  - subdirectory-crystallization\n"
        "sources:\n"
        '  - "doi/10.1038##test789"\n'
        'overview: "A test method for unit testing."\n'
        'principle: "Test principle."\n'
    )
    # Concept
    (yd["concepts"] / "test_concept.yaml").write_text(
        'title: "Test Concept"\n'
        'created: "2026-06-18"\n'
        'updated: "2026-06-18"\n'
        "tags:\n"
        "  - concept-structural\n"
        "  - subdirectory-concepts\n"
        "sources:\n"
        '  - "doi/10.1038##test_concept"\n'
        'overview: "A test concept for unit testing."\n'
        'mechanism: "Structural transitions."\n'
    )


def run_script(script_name, args, tmp_base, expect_success=True):
    """Run a script via subprocess with TEST_BASE_DIR and return results.

    Returns (success: bool, stdout: str, stderr: str).
    success is True if (returncode == 0) == expect_success.
    """
    import subprocess

    cmd = [sys.executable, str(SCRIPTS_DIR / script_name)] + args
    env = os.environ.copy()
    env["TEST_BASE_DIR"] = str(tmp_base)
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(PROJECT_ROOT),
        env=env,
    )
    ok = (result.returncode == 0) == expect_success
    return ok, result.stdout, result.stderr


# ---------------------------------------------------------------------------
# Fixtures for direct-import tests (WikiQuery, renderers)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def wiki_query():
    """Provide a WikiQuery instance for read-only tests against real data.

    Loaded once per session since WikiQuery builds indices from real YAMLs.
    This is a read-only fixture — it never modifies real project files.
    Its side effect is creating references/entity_index.json (precomputed index).
    """
    sys.path.insert(0, str(SCRIPTS_DIR))
    from wiki_query import WikiQuery

    # Use existing index if available; do NOT force rebuild
    wq = WikiQuery(rebuild=False)
    return wq
