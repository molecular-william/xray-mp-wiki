# X-ray MP Wiki — Reference Guide

**This file is a quick reference.** The authoritative source is `references/AGENT-MANIFEST.md` which consolidates all schema, tag taxonomy, conventions, and prohibitions. The formal JSON Schema is at `references/entity_schema.json`.

---

## Domain
Wiki covers **reagents, methods, protocols** for X-ray crystallography of **membrane proteins**.

## Entity Types

| Type | Directory | Subdirs | Count |
|------|-----------|---------|-------|
| **Proteins** | `proteins/<subdir>/` | 16 | ~783 |
| **Reagents** | `reagents/<subdir>/` | 10 | ~768 |
| **Methods** | `methods/<subdir>/` | 7 | ~63 |
| **Concepts** | `concepts/<subdir>/` | 10 | ~424 |

## Directory Structure

```
xray-mp-wiki/
├── _config.yml, Gemfile, index.md, graph.md
├── _layouts/default.html, _layouts/graph.html
├── assets/wiki.css
├── categories/{proteins,reagents,methods,concepts}/index.md
├── proteins/       (16 subdirs: gpcr, rhodopsins, voltage-gated-channels, ...)
├── concepts/       (10 subdirs: transport-mechanisms, structural-mechanisms, ...)
├── reagents/       (10 subdirs: detergents, lipids, buffers, additives, ...)
├── methods/        (7 subdirs: crystallization, expression-systems, purification, ...)
├── {proteins,reagents,methods,concepts}_yaml/  (flat YAML source)
└── categories/     (auto-generated index pages)
```

## Entity Classification (2-Pass)

| Question | → Entity |
|----------|----------|
| Specific solved structure (PDB, construct, purification)? | **Protein** |
| Chemical compound (detergent, salt, buffer, drug, lipid, tag)? | **Reagent** |
| Protocol/technique with steps? | **Method** |
| Mechanism, family, principle, design strategy? | **Concept** |

## Validation

All YAML validated before render:
```bash
python3 scripts/validate_yaml.py <type> <name> --strict
```

## Source-Truth Verification
1. Extract claims from wiki page → 2. Read `raw/papers/<doi>.md` → 3. Verify each claim → 4. Remove unsupported. Log in `log.md`.

## Correction Policy
1. **Different conditions** — add as alternative, keep old
2. **Superseding paper** — update, log supersession
3. **Factual error** — remove claim, log
4. **Never retain unsupported claims**
