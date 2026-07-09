"""
Full-scan integration tests for data integrity.

These tests read every YAML and every page in the wiki. They are slow
(~30-60s) and are marked with @pytest.mark.slow.

Run with: python -m pytest scripts/ -v --run-slow
Or:       python -m pytest scripts/test_data_integrity.py -v
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

from scripts.conftest import PROJECT_ROOT, SCRIPTS_DIR

# Mark all tests in this module as slow
pytestmark = pytest.mark.slow


class TestCrossRefIntegrity:
    """Test E: Every cross-reference resolves to a real entity."""

    @pytest.mark.xfail(
        strict=False,
        reason="Known data debt: 327/10831 cross-refs target 193 entities with no YAML on disk (e.g. aquaporin, rotary-atpase-mechanism). Needs entity creation or link removal.",
    )
    def test_all_crossrefs_resolve(self):
        import glob

        import yaml

        catalog_path = PROJECT_ROOT / "references" / "entity_catalog.json"
        catalog = json.loads(catalog_path.read_text()) if catalog_path.exists() else {}
        bad_refs, total_refs = 0, 0
        for d in ["proteins_yaml", "reagents_yaml", "methods_yaml", "concepts_yaml"]:
            for f in sorted(glob.glob(str(PROJECT_ROOT / "xray-mp-wiki" / d / "*.yaml"))):
                data = yaml.safe_load(open(f))
                if not data:
                    continue
                for cr in data.get("cross_references", []):
                    total_refs += 1
                    name = cr.get("path", "").rstrip("/").split("/")[-1] if cr.get("path") else ""
                    if name and name not in catalog:
                        bad_refs += 1
        assert bad_refs == 0, f"{bad_refs} broken cross-refs out of {total_refs}"

    def test_graph_edges_resolve(self):
        graph_path = PROJECT_ROOT / "xray-mp-wiki" / "assets" / "graph.json"
        if not graph_path.exists():
            pytest.skip("graph.json not found — run rebuild_graph.py first")
        graph = json.loads(graph_path.read_text())
        graph_nodes = {n["id"] for n in graph.get("nodes", [])}
        bad_edges, total_edges = 0, 0
        for e in graph.get("edges", []):
            total_edges += 1
            if e["source"] not in graph_nodes or e["target"] not in graph_nodes:
                bad_edges += 1
        assert bad_edges == 0, f"{bad_edges} broken graph edges out of {total_edges}"

    @pytest.mark.xfail(
        strict=False,
        reason="Known data debt: 3/877 sampled DOIs lack raw paper files. 28 hallucinated DOIs removed from YAMLs. Remaining 3 are legitimate references not yet acquired.",
    )
    def test_dois_have_raw_papers(self):
        import glob

        import yaml

        bad_dois, total_dois = 0, 0
        for d in ["proteins_yaml", "reagents_yaml", "methods_yaml", "concepts_yaml"]:
            for f in sorted(glob.glob(str(PROJECT_ROOT / "xray-mp-wiki" / d / "*.yaml")))[:100]:
                data = yaml.safe_load(open(f))
                if not data:
                    continue
                for src in data.get("sources", []):
                    total_dois += 1
                    doi_path = PROJECT_ROOT / "raw" / "papers" / f"{src.replace('doi/', '').lower()}.md"
                    if not doi_path.exists():
                        bad_dois += 1
        assert bad_dois == 0, f"{bad_dois} DOIs missing raw papers (sampled {total_dois})"


class TestCatalogSync:
    """Test F: Entity catalog matches YAML files on disk."""

    def test_all_yamls_have_catalog_entries(self):
        import glob

        catalog_path = PROJECT_ROOT / "references" / "entity_catalog.json"
        catalog = json.loads(catalog_path.read_text()) if catalog_path.exists() else {}
        yaml_on_disk = set()
        for d in ["proteins_yaml", "reagents_yaml", "methods_yaml", "concepts_yaml"]:
            for f in glob.glob(str(PROJECT_ROOT / "xray-mp-wiki" / d / "*.yaml")):
                yaml_on_disk.add(Path(f).stem)
        catalog_entries = set(catalog.keys())
        missing = yaml_on_disk - catalog_entries
        assert len(missing) == 0, f"{len(missing)} YAMLs missing from catalog: {list(missing)[:5]}"

    def test_all_catalog_entries_have_yamls(self):
        catalog_path = PROJECT_ROOT / "references" / "entity_catalog.json"
        catalog = json.loads(catalog_path.read_text()) if catalog_path.exists() else {}
        yaml_on_disk = set()
        for d in ["proteins_yaml", "reagents_yaml", "methods_yaml", "concepts_yaml"]:
            for f in (PROJECT_ROOT / "xray-mp-wiki" / d).glob("*.yaml"):
                yaml_on_disk.add(f.stem)
        catalog_entries = set(catalog.keys())
        extra = catalog_entries - yaml_on_disk
        assert len(extra) == 0, f"{len(extra)} catalog entries without YAMLs: {list(extra)[:5]}"

    def test_proteins_have_required_fields(self):
        import yaml

        missing_fields = 0
        for f in sorted((PROJECT_ROOT / "xray-mp-wiki" / "proteins_yaml").glob("*.yaml"))[:200]:
            data = yaml.safe_load(f.read_text())
            if not data:
                continue
            for field in ["title", "tags", "sources"]:
                if field not in data:
                    missing_fields += 1
        assert missing_fields == 0, f"{missing_fields} proteins missing required fields (sampled 200)"


class TestLint:
    """Lint runs without crashing and reports issues."""

    def test_lint_runs_and_parses_pages(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "lint.py")],
            capture_output=True,
            text=True,
            cwd=str(PROJECT_ROOT),
            timeout=120,
        )
        assert "Total pages checked:" in result.stdout, "lint should report page count"
        assert "Parsing frontmatter..." in result.stdout, "lint should parse frontmatter"
        assert "TOTAL ISSUES:" in result.stdout or "wiki is clean" in result.stdout, "lint should have summary line"
