"""
Tests for maintenance scripts: rebuild_entity_catalog, wiki_manifest, enrich_wikilinks, base utilities.

These tests modify real project files (wiki_manifest.json, entity_catalog.json) with
save/restore patterns. Marked slow.
"""

import json
import os
import subprocess
import sys

import pytest

from scripts.tests.conftest import PROJECT_ROOT, SCRIPTS_DIR

pytestmark = pytest.mark.slow


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def saved_manifest():
    """Save real manifest, write a test one, restore on exit."""
    path = PROJECT_ROOT / "wiki_manifest.json"
    saved = path.read_text() if path.exists() else None
    # Write test manifest
    test_mf = {
        "last_run": "2026-06-18",
        "entity_index": {
            "test_protein": {"type": "proteins", "source_dois": ["10.1038##test123"]},
            "kcsa": {"type": "proteins", "source_dois": ["10.1073##pnas.123"]},
        },
        "processed": {},
        "current_batch": {},
    }
    path.write_text(json.dumps(test_mf))
    yield path
    if saved is not None:
        path.write_text(saved)
    elif path.exists():
        path.unlink()


@pytest.fixture
def saved_catalog():
    """Save and restore references/entity_catalog.json."""
    path = PROJECT_ROOT / "references" / "entity_catalog.json"
    saved = path.read_text() if path.exists() else None
    yield path
    if saved is not None:
        path.write_text(saved)
    elif path.exists():
        path.unlink()


@pytest.fixture
def temp_enrich_yamls():
    """Create and clean up test YAML/page for enrichment tests."""
    yaml_path = PROJECT_ROOT / "xray-mp-wiki/proteins_yaml/aaa_enrich_test.yaml"
    page_path = PROJECT_ROOT / "xray-mp-wiki/proteins/aaa_enrich_test.md"
    yield yaml_path, page_path
    yaml_path.unlink(missing_ok=True)
    page_path.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------


def run_script(script_name, args, expect_success=True, timeout=60):
    """Run a script via subprocess and return (success, stdout, stderr)."""
    cmd = [sys.executable, str(SCRIPTS_DIR / script_name)] + args
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(PROJECT_ROOT),
        timeout=timeout,
    )
    ok = (result.returncode == 0) == expect_success
    return ok, result.stdout, result.stderr


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestRebuildEntityCatalog:
    """Test rebuild_entity_catalog.py's --from-filesystem reads YAMLs correctly."""

    def test_filesystem_mode_with_tmp_catalog(self, tmp_path):
        """--from-filesystem with TEST_BASE_DIR for safe testing."""
        # Write test yaml in temp dir
        yaml_dir = tmp_path / "xray-mp-wiki" / "proteins_yaml"
        yaml_dir.mkdir(parents=True)
        (yaml_dir / "test_protein.yaml").write_text(
            'title: "Test Protein"\ncreated: "2026-06-18"\nupdated: "2026-06-18"\n'
            "tags:\n  - transporter\n  - membrane-protein\n"
            'sources:\n  - "doi/10.1038##test"\noverview: "Test."\n'
        )
        env = os.environ.copy()
        env["TEST_BASE_DIR"] = str(tmp_path)
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "rebuild_entity_catalog.py"), "--from-filesystem"],
            capture_output=True,
            text=True,
            env=env,
            cwd=str(PROJECT_ROOT),
        )
        assert result.returncode == 0, f"failed: {result.stderr}"
        assert "entries written" in result.stdout


class TestWikiManifest:
    """Test wiki_manifest.py commands (modifies real manifest with save/restore)."""

    def test_check_entity_existing(self, saved_manifest):
        """check-entity: existing protein returns exit 0."""
        ok, out, err = run_script("wiki_manifest.py", ["check-entity", "test_protein"])
        assert ok, f"check-entity failed: {err}"

    def test_check_entity_missing(self, saved_manifest):
        """check-entity: nonexistent returns exit 1."""
        ok, out, err = run_script("wiki_manifest.py", ["check-entity", "no_such_protein"], expect_success=False)
        assert ok, f"should have failed: {err}"

    def test_status_runs(self, saved_manifest):
        """status command runs successfully."""
        ok, out, err = run_script("wiki_manifest.py", ["status"])
        assert ok, f"status failed: {err}"
        assert "processed" in out.lower() or "status" in out.lower() or "doi" in out.lower(), (
            f"Unexpected output: {out[:200]}"
        )


class TestEnrich:
    """Test enrich_wikilinks.py dry-run mode."""

    def test_enrich_dry_run(self, saved_catalog, temp_enrich_yamls):
        """Dry-run enrichment processes a test file without modifying it."""
        yaml_path, page_path = temp_enrich_yamls

        # Create test YAML
        yaml_path.write_text(
            'title: "AAA Enrich Test"\n'
            'created: "2026-06-18"\n'
            'updated: "2026-06-18"\n'
            "tags:\n"
            "  - transporter\n"
            "  - membrane-protein\n"
            "sources:\n"
            '  - "doi/10.1038##enrich"\n'
            'overview: "A test for enrichment. Uses DDM."\n'
        )
        page_path.write_text("---\ntitle: AAA Enrich Test\n---\n# AAA Enrich Test\nUses DDM.\n")

        # Set up test catalog
        test_catalog = {
            "test_protein": {"type": "proteins", "title": "Test Protein", "filename": "test_protein.md"},
        }
        saved_catalog.write_text(json.dumps(test_catalog))

        # Run dry-run enrichment
        env = os.environ.copy()
        env["YAML_TYPE"] = "proteins_yaml"
        env["DRY_RUN"] = "1"
        env["FIRST_N"] = "1"
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "enrich" / "enrich_wikilinks.py")],
            capture_output=True,
            text=True,
            cwd=str(PROJECT_ROOT),
            env=env,
        )
        assert result.returncode == 0, f"enrich dry-run failed: {result.stderr}"
        assert "aaa_enrich_test" in result.stdout, f"Expected file in output: {result.stdout[:200]}"

        # Verify YAML was NOT modified
        original = yaml_path.read_text()
        assert "[AAA Enrich Test](" not in original, "Dry run modified the YAML!"


class TestBaseUtilities:
    """Test _base.py utility functions through generate_page.py."""

    def test_build_paths_via_generate(self, tmp_project):
        """build_paths produces correct output path."""
        yaml_dir = tmp_project["yaml"]["proteins"]
        yaml_dir.mkdir(parents=True, exist_ok=True)
        (yaml_dir / "path_test.yaml").write_text(
            'title: "Path Test"\n'
            'created: "2026-06-18"\n'
            'updated: "2026-06-18"\n'
            "tags:\n"
            "  - transporter\n"
            "  - membrane-protein\n"
            "sources:\n"
            '  - "doi/10.1038##pathtest"\n'
            'overview: "Testing path construction."\n'
        )
        env = os.environ.copy()
        env["TEST_BASE_DIR"] = str(tmp_project["base"])
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "generate_page.py"), "protein", "path_test", "--dry-run"],
            capture_output=True,
            text=True,
            cwd=str(PROJECT_ROOT),
            env=env,
        )
        assert result.returncode == 0, f"dry-run failed: {result.stderr}"
        assert "xray-mp-wiki/proteins/path_test.md" in result.stdout or "/proteins/path_test.md" in result.stdout, (
            f"Expected path in output: {result.stdout[:300]}"
        )
