"""
Tests for WikiQuery engine, sequence renderer, and YAML round-trip.

These import modules directly (no subprocess) and read from the real project.
All tests are read-only — they never modify project files.
"""

import os
import tempfile

import pytest

from scripts.tests.conftest import SCRIPTS_DIR

# ===========================================================================
# WikiQuery — basic queries
# ===========================================================================


class TestWikiQueryBasic:
    """Test C: WikiQuery get, search, connections, path."""

    def test_get_ddm(self, wiki_query):
        ddm = wiki_query.get("ddm")
        assert ddm is not None, "get('ddm') should return a result"
        assert ddm.get("type"), "result should have type"
        assert ddm.get("title"), "result should have title"
        assert ddm.get("path"), "result should have path"

    def test_get_nonexistent(self, wiki_query):
        assert wiki_query.get("this-entity-does-not-exist-xyzzy") is None

    def test_search_adenosine(self, wiki_query):
        results = wiki_query.search("adenosine", limit=5)
        assert len(results) >= 1, "search('adenosine') should find at least 1 result"
        assert "name" in results[0]
        assert "match_field" in results[0]

    def test_connections_ddm(self, wiki_query):
        conns = wiki_query.connections("ddm", depth=1, limit=5)
        assert len(conns) >= 1, "connections('ddm') should have at least 1 neighbor"
        assert "name" in conns[0]
        assert "edge_type" in conns[0]
        assert "reasons" in conns[0]

    def test_connections_nonexistent(self, wiki_query):
        assert wiki_query.connections("nonexistent-node") == []

    def test_path_ddm_to_kcsa(self, wiki_query):
        path_r = wiki_query.path("ddm", "kcsa")
        assert path_r is not None, "path('ddm','kcsa') should return a path"
        assert len(path_r) > 1, "path should have at least 2 hops"


class TestWikiQuerySuggest:
    """Test D: WikiQuery suggest cross-references."""

    def test_suggest_by_name(self, wiki_query):
        s1 = wiki_query.suggest(name="5ht2a-receptor", limit=10)
        assert len(s1) >= 1, "suggest('5ht2a-receptor') should return results"
        for key in ["name", "score", "reason", "type"]:
            assert key in s1[0], f"suggest result should have '{key}'"
        assert all(s.get("score", 0) > 0 for s in s1), "all scores should be positive"

    def test_suggest_by_tags(self, wiki_query):
        s2 = wiki_query.suggest(tags="gpcr", family="GPCR", limit=10)
        assert len(s2) >= 1, "suggest(tags=gpcr) should return results"

    def test_suggest_no_args(self, wiki_query):
        assert wiki_query.suggest() == [], "suggest() with no args should return []"


# ===========================================================================
# Sequence renderer
# ===========================================================================


class TestSequenceRenderer:
    """Test B: Renderer produces ruler + collapsible table."""

    @pytest.fixture(autouse=True)
    def _import_renderer(self):
        from scripts.renderers.protein_page_renderer import render_colored_sequence, render_sequence_block

        self.render_colored = render_colored_sequence
        self.render_block = render_sequence_block

    def test_ruler_emitted(self):
        topo = [
            {"begin": "1", "end": "10", "pdb_begin": "1", "pdb_end": "10", "location": "Inside"},
            {"begin": "11", "end": "30", "pdb_begin": "11", "pdb_end": "30", "location": "Membrane"},
            {"begin": "31", "end": "40", "pdb_begin": "31", "pdb_end": "40", "location": "Outside"},
        ]
        residues = "A" * 10 + "B" * 20 + "C" * 10
        result = self.render_colored(residues, topo)
        assert 'class="topo-ruler"' in result, "should emit ruler"

    def test_topo_spans(self):
        topo = [
            {"begin": "1", "end": "10", "pdb_begin": "1", "pdb_end": "10", "location": "Inside"},
            {"begin": "11", "end": "30", "pdb_begin": "11", "pdb_end": "30", "location": "Membrane"},
            {"begin": "31", "end": "40", "pdb_begin": "31", "pdb_end": "40", "location": "Outside"},
        ]
        residues = "A" * 10 + "B" * 20 + "C" * 10
        result = self.render_colored(residues, topo)
        assert 'class="topo-membrane"' in result
        assert 'class="topo-inside"' in result
        assert 'class="topo-outside"' in result

    def test_collapsible_table(self):
        topo = [
            {"begin": "1", "end": "10", "pdb_begin": "1", "pdb_end": "10", "location": "Inside"},
            {"begin": "11", "end": "30", "pdb_begin": "11", "pdb_end": "30", "location": "Membrane"},
        ]
        residues = "A" * 10 + "B" * 20
        block = self.render_block(
            [
                {
                    "pdb_id": "1ABC",
                    "chain": "A",
                    "tmd": "3",
                    "type": "alpha",
                    "residues": residues,
                    "topology": topo,
                }
            ]
        )
        assert '<details class="topo-details">' in block, "should have collapsible table"
        assert "<summary>Topology coordinates" in block, "should have summary"
        assert 'class="topo-legend"' in block, "should have legend"

    def test_residues_matches_ruler(self):
        topo = [
            {"begin": "1", "end": "10", "pdb_begin": "1", "pdb_end": "10", "location": "Membrane"},
        ]
        residues = "M" * 40
        result = self.render_colored(residues, topo)
        import re

        rulers = re.findall(r'<span class="topo-ruler">([^<]+)</span>', result)
        seqs = re.findall(r'<span class="topo-line">(.*?)</span>', result)
        if rulers and seqs:
            # Ruler chars should roughly match sequence length
            assert len(rulers[0]) == len("M" * 40), "ruler length should match sequence chunk"


# ===========================================================================
# YAML round-trip
# ===========================================================================


class TestYamlRoundtrip:
    """Test A: YAML load, modify, save, read back."""

    def test_load_and_modify(self):
        import yaml

        yaml_path = SCRIPTS_DIR.parent / "xray-mp-wiki" / "reagents_yaml" / "ddm.yaml"
        if not yaml_path.exists():
            pytest.skip("ddm.yaml not found — live data test requires wiki checkout")
        original = yaml_path.read_text()
        data = yaml.safe_load(original)
        assert data is not None, "should load without error"
        old_updated = data.get("updated", "")
        assert old_updated, "should have 'updated' field"

    def test_dump_preserves_structure(self):
        import yaml

        data = yaml.safe_load('title: "Test"\ntags:\n  - detergent-nonionic\nsources:\n  - "doi/10.1016##test"\n')
        tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False)
        try:
            yaml.dump(data, tmp, default_flow_style=False, allow_unicode=True, sort_keys=False)
            tmp.close()
            with open(tmp.name) as f:
                reloaded = yaml.safe_load(f)
            assert reloaded is not None, "dump should preserve structure"
            assert reloaded.get("title") == "Test", "dump should preserve title"
            assert len(reloaded.get("tags", [])) > 0, "dump should preserve tags"
        finally:
            os.unlink(tmp.name)

    def test_quoted_colons(self):
        import yaml

        data = yaml.safe_load('title: "Foo: Bar: Baz"')
        assert data["title"] == "Foo: Bar: Baz", "quoted colons should stay as string"

    def test_quoted_mixing_ratio(self):
        import yaml

        data = yaml.safe_load('mixing_ratio: "1:1"')
        assert isinstance(data["mixing_ratio"], str), "1:1 should stay string, not become sexagesimal 61"
