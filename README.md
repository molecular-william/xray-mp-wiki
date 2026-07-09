# xray-mp-wiki

Reagents and procedures for X-ray crystallography of membrane proteins.

Structured YAML corpus of ~1,290 publications, each decomposed into proteins, reagents, methods, and concepts with cross-referenced experimental details — purification, crystallization, detergents, buffers, additives, lipids.

Built with [Jekyll](https://jekyllrb.com/) and hosted on GitHub Pages.

## Layout

```
.github/workflows/    CI — Jekyll build + deploy
xray-mp-wiki/         Jekyll site source
  _config.yml         Site config
  proteins_yaml/      YAML corpus
  reagents_yaml/
  methods_yaml/
  concepts_yaml/
  categories/         Generated site pages
scripts/              Data tools
  normalize_*.py      Structure extraction (buffers, detergents, expression)
  aggregate_stats.py  Corpus analysis
  validate_yaml.py    Schema validation
references/           Schema docs, agent manifest
```

## Development

Local build:

```
cd xray-mp-wiki
gem install bundler
bundle install
bundle exec jekyll serve
```

Validate YAML:

```
python3 scripts/validate_yaml.py
python3 scripts/generate_page.py  # regenerate site pages from YAML
```

## Data

`raw/`, `protein_doi_checklist.csv`, and `snapshot-*.zip` are gitignored — not in the repo.
