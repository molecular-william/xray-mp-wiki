"""
Tests for the page generation pipeline (generate_page.py).

All tests run scripts via subprocess with TEST_BASE_DIR pointing to a
temporary directory to isolate file operations.
"""

from scripts.tests.conftest import run_script


class TestGenerateProtein:
    """Protein page generation tests."""

    def test_dry_run(self, tmp_project):
        ok, out, _ = run_script("generate_page.py", ["protein", "test_protein", "--dry-run"], tmp_project["base"])
        assert ok, "dry-run should exit 0"
        assert "Generated page for test_protein (dry run)" in out

    def test_generates_page(self, tmp_project):
        out_path = tmp_project["output"]["proteins"] / "test_protein.md"
        ok, out, _ = run_script("generate_page.py", ["protein", "test_protein", "--yes"], tmp_project["base"])
        assert ok, f"generate should exit 0. stderr: {_}"
        assert out_path.exists(), f"page should exist at {out_path}"

    def test_page_content(self, tmp_project):
        out_path = tmp_project["output"]["proteins"] / "test_protein.md"
        run_script("generate_page.py", ["protein", "test_protein", "--yes"], tmp_project["base"])
        content = out_path.read_text()
        assert "Test Protein" in content
        assert "A test protein for unit testing" in content
        assert "1ABC" in content
        assert "DDM" in content

    def test_overwrite_with_yes(self, tmp_project):
        ok, _, _ = run_script("generate_page.py", ["protein", "test_protein", "--yes"], tmp_project["base"])
        assert ok, "overwrite with --yes should succeed"

    def test_diff_shows_changes(self, tmp_project):
        yaml_dir = tmp_project["yaml"]["proteins"]
        output_dir = tmp_project["output"]["proteins"]

        # Create existing page with old content
        (output_dir / "test_protein_diff.md").write_text("---\ntitle: Old Title\n---\n# Old Title\n")
        (yaml_dir / "test_protein_diff.yaml").write_text(
            'title: "New Title"\ncreated: "2026-06-18"\n'
            'updated: "2026-06-18"\n'
            "tags:\n  - transporter\n  - membrane-protein\n"
            'sources:\n  - "doi/10.1038##diff123"\n'
            'overview: "New overview for diff test."\n'
        )
        ok, out, _ = run_script(
            "generate_page.py", ["protein", "test_protein_diff", "--diff", "--yes"], tmp_project["base"]
        )
        assert ok, "--diff should exit 0"
        assert "Diff for test_protein_diff" in out, "diff output should show filename"

    def test_missing_yaml_fails(self, tmp_project):
        ok, _, _ = run_script("generate_page.py", ["protein", "nonexistent"], tmp_project["base"], expect_success=False)
        assert ok, "missing YAML should exit with error"

    def test_skip_catalog(self, tmp_project):
        yaml_dir = tmp_project["yaml"]["proteins"]
        (yaml_dir / "test_skipcat.yaml").write_text(
            'title: "Skip Catalog Test"\ncreated: "2026-06-18"\n'
            'updated: "2026-06-18"\n'
            "tags:\n  - transporter\n  - membrane-protein\n"
            'sources:\n  - "doi/10.1038##skipcat"\n'
            'overview: "Testing skip-catalog flag."\n'
        )
        ok, _, _ = run_script(
            "generate_page.py", ["protein", "test_skipcat", "--yes", "--skip-catalog"], tmp_project["base"]
        )
        assert ok, "--skip-catalog should exit 0"
        index_content = tmp_project["index"].read_text()
        assert "Skip Catalog Test" not in index_content, "catalog should not be updated"

    def test_unknown_type_fails(self, tmp_project):
        ok, out, _ = run_script(
            "generate_page.py", ["unknown", "test_protein"], tmp_project["base"], expect_success=False
        )
        assert ok, "unknown type should exit with error"


class TestGenerateReagent:
    """Reagent page generation tests."""

    def test_dry_run(self, tmp_project):
        ok, out, _ = run_script("generate_page.py", ["reagent", "test_reagent", "--dry-run"], tmp_project["base"])
        assert ok, "dry-run should exit 0"

    def test_generates_in_subdirectory(self, tmp_project):
        out_path = tmp_project["output"]["reagents"] / "detergents" / "test_reagent.md"
        ok, _, _ = run_script("generate_page.py", ["reagent", "test_reagent", "--yes"], tmp_project["base"])
        assert ok, "generate should exit 0"
        assert out_path.exists(), f"page should exist at {out_path}"

    def test_page_content(self, tmp_project):
        out_path = tmp_project["output"]["reagents"] / "detergents" / "test_reagent.md"
        run_script("generate_page.py", ["reagent", "test_reagent", "--yes"], tmp_project["base"])
        content = out_path.read_text()
        assert "Test Detergent" in content
        assert "Test Use" in content


class TestGenerateMethod:
    """Method page generation tests."""

    def test_dry_run(self, tmp_project):
        ok, out, _ = run_script("generate_page.py", ["method", "test_method", "--dry-run"], tmp_project["base"])
        assert ok, "dry-run should exit 0"

    def test_generates_in_subdirectory_from_tag(self, tmp_project):
        out_path = tmp_project["output"]["methods"] / "crystallization" / "test_method.md"
        ok, _, _ = run_script("generate_page.py", ["method", "test_method", "--yes"], tmp_project["base"])
        assert ok, "generate should exit 0"
        assert out_path.exists(), f"page should exist at {out_path}"

    def test_page_content(self, tmp_project):
        out_path = tmp_project["output"]["methods"] / "crystallization" / "test_method.md"
        run_script("generate_page.py", ["method", "test_method", "--yes"], tmp_project["base"])
        content = out_path.read_text()
        assert "Test Method" in content
        assert "Test principle" in content


class TestGenerateConcept:
    """Concept page generation tests."""

    def test_dry_run(self, tmp_project):
        ok, out, _ = run_script("generate_page.py", ["concept", "test_concept", "--dry-run"], tmp_project["base"])
        assert ok, "dry-run should exit 0"

    def test_generates_page(self, tmp_project):
        # concept-structural tag maps to structural-mechanisms subdirectory
        out_path = tmp_project["output"]["concepts"] / "structural-mechanisms" / "test_concept.md"
        ok, _, _ = run_script("generate_page.py", ["concept", "test_concept", "--yes"], tmp_project["base"])
        assert ok, "generate should exit 0"
        assert out_path.exists(), f"page should exist at {out_path}"

    def test_page_content(self, tmp_project):
        out_path = tmp_project["output"]["concepts"] / "structural-mechanisms" / "test_concept.md"
        run_script("generate_page.py", ["concept", "test_concept", "--yes"], tmp_project["base"])
        content = out_path.read_text()
        assert "Test Concept" in content
        assert "A test concept for unit testing" in content
        assert "Structural transitions" in content
