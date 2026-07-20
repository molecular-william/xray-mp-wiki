"""
Tests for YAML validation (validate_yaml.py).

All tests run scripts via subprocess with TEST_BASE_DIR isolation.
"""

from scripts.tests.conftest import run_script


class TestValidate:
    """YAML schema validation tests for all 4 entity types."""

    def test_valid_protein_passes(self, tmp_project):
        ok, out, _ = run_script("validate_yaml.py", ["protein", "test_protein", "--strict"], tmp_project["base"])
        assert ok, "valid protein should pass strict"
        assert "schema valid" in out

    def test_valid_reagent_passes(self, tmp_project):
        ok, out, _ = run_script("validate_yaml.py", ["reagent", "test_reagent", "--strict"], tmp_project["base"])
        assert ok, "valid reagent should pass strict"
        assert "schema valid" in out

    def test_valid_method_passes(self, tmp_project):
        ok, out, _ = run_script("validate_yaml.py", ["method", "test_method", "--strict"], tmp_project["base"])
        assert ok, "valid method should pass strict"
        assert "schema valid" in out

    def test_valid_concept_passes(self, tmp_project):
        ok, out, _ = run_script("validate_yaml.py", ["concept", "test_concept", "--strict"], tmp_project["base"])
        assert ok, "valid concept should pass strict"
        assert "schema valid" in out

    def test_invalid_yaml_fails(self, tmp_project):
        bad = tmp_project["yaml"]["proteins"] / "bad_protein.yaml"
        bad.write_text('title: "Bad"\n')
        ok, _, _ = run_script(
            "validate_yaml.py", ["protein", "bad_protein", "--strict"], tmp_project["base"], expect_success=False
        )
        assert ok, "invalid YAML (missing tags, sources) should fail strict"

    def test_nonexistent_file_fails(self, tmp_project):
        ok, _, _ = run_script("validate_yaml.py", ["protein", "ghost"], tmp_project["base"], expect_success=False)
        assert ok, "nonexistent file should exit with code 2"

    def test_unknown_type_fails(self, tmp_project):
        ok, _, _ = run_script("validate_yaml.py", ["alien", "test_protein"], tmp_project["base"], expect_success=False)
        assert ok, "unknown type should fail"

    def test_wikilink_syntax_rejected(self, tmp_project):
        """[[wikilink]] syntax should be caught by validator."""
        bad = tmp_project["yaml"]["proteins"] / "wikilink_bad.yaml"
        bad.write_text(
            'title: "Bad Wikilink"\n'
            'created: "2026-06-18"\n'
            'updated: "2026-06-18"\n'
            "tags:\n  - transporter\n  - membrane-protein\n"
            'sources:\n  - "doi/10.1038##wltest"\n'
            'overview: "Uses [[ddm]] for purification."\n'
        )
        ok, out, _ = run_script(
            "validate_yaml.py", ["protein", "wikilink_bad", "--strict"], tmp_project["base"], expect_success=False
        )
        assert ok, "YAML with [[wikilink]] syntax should fail validation"
        assert "non-Jekyll wikilink" in out or "[[ddm]]" in out
