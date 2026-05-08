# X-ray MP Wiki — Reference Guide (Cave)

## Domain

Wiki covers **reagents, methods, protocols** for X-ray crystallography of **membrane proteins**.

1. **Solubilization** — detergents, lipids, additives for extraction
2. **Cell lysis** — microfluidizer, French press, sonication
3. **Expression systems** — E. coli, Pichia, Sf9, HEK293
4. **Purification** — affinity, SEC, resins (TALON, Superdex), Amicon
5. **Protein tags** — BRIL, T4L, TEV protease
6. **Crystallization** — precipitants, additives, vapor diffusion, LCP
7. **Structure determination** — X-ray collection, phasing, refinement
8. **Membrane protein class** — GPCRs, ion channels, transporters
9. **Concepts** — general ideas, mechanisms, families, principles

## Entity Types

| Type | Directory | Frontmatter `type` | Frontmatter `category` | Count |
|------|-----------|-------------------|----------------------|-------|
| **Proteins** | `proteins/` (flat) | `protein` | `proteins` | ~43 |
| **Reagents** | `reagents/<subdir>/` | `reagent` | `reagents` | ~87 |
| **Methods** | `methods/<subdir>/` | `method` | `methods` | ~26 |
| **Concepts** | `concepts/` (flat) | `concept` | `concepts` | ~7 |

## Concept Entity

Concepts = general ideas, mechanisms, families, principles. Not proteins/reagents/methods.

**NOT concepts:**
- Specific proteins (→ Proteins)
- Chemical compounds (→ Reagents)
- Protocols with steps (→ Methods)
- Broad topics (→ tags, e.g., "GPCR")

**IS concepts:**
- Protein families (ABC transporters, SLC families)
- Membrane mimetics (bicelles, nanodiscs, lipid polymorphism)
- Crystallography principles (twinning, NCS, crystal contacts)
- Construct design (truncation, thermostabilization, glycosylation engineering)
- Mechanistic concepts (biased agonism, allosteric regulation)
- Antibody tech (nanobody engineering, epitope mapping)

## Directory Structure

```
xray-mp-wiki/
├── _config.yml         (baseurl: "/xray-mp-wiki", kramdown)
├── Gemfile             (github-pages gem)
├── index.md            (homepage)
├── _layouts/default.html (renders References from sources:)
├── categories/         (index pages)
│   ├── proteins/index.md
│   ├── reagents/index.md
│   ├── methods/index.md
│   └── concepts/index.md
├── proteins/           (flat)
├── reagents/           (hierarchical)
│   ├── detergents/
│   ├── lipids/
│   ├── buffers/
│   ├── additives/
│   ├── ligands/
│   ├── protein-tags/
│   └── antibodies/
├── methods/            (hierarchical)
│   ├── crystallization/
│   ├── expression-systems/
│   ├── purification/
│   ├── structure-determination/
│   ├── solubilization/
│   ├── cell-lysis/
│   └── quality-assessment/
├── concepts/           (flat)
├── proteins_yaml/
├── reagents_yaml/
├── methods_yaml/
└── concepts_yaml/
```

## Wiki Catalog

In `index.md`, wrapped in `<!-- WIKI CATALOG -->` / `<!-- END WIKI CATALOG -->`. Jekyll ignores (HTML comments). Auto-maintained by generate/update scripts.

**Columns:** `type` (protein|reagent|method|concept) | `path` (relative, ends `/`) | `title` | `summary` (≤80 chars)

**Agent usage:** load `index.md` at session start. Parse catalog to search entities. Read only relevant pages.

## File Naming

- lowercase-hyphen, no spaces: `lipidic-cubic-phase.md`
- full names, no abbreviations
- `.md` extension required

## Internal Links

- absolute paths: `[title](/xray-mp-wiki/proteins/filename/)`
- **NO `[[wikilink]]`** — GitHub Pages doesn't support
- **≥2 outbound links** per page
- wikilinks for entities with pages; plain text for others
- **NO links to non-existent pages** — create or leave plain text
- Cross-References: max 8 entries, grouped (proteins → reagents → methods), one-line reason. After Pass 2 entity discovery, Cross-References should include ALL entities that now have wiki pages.

## Frontmatter

```yaml
---
title: Human-Readable Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: protein | reagent | method | concept
category: proteins | reagents | methods | concepts
layout: default
tags: [tag1, tag2, tag3]
sources: [doi/10.xxxx##yyyy]
---
```

**Rules:** `layout: default` mandatory. Bump `updated` on every edit. `sources` uses `doi/` prefix + `##` separator. `category` matches parent dir. `tags`/`sources` = lists. Frontmatter = first block, no blank lines before `---`.

### References Section

Layout auto-renders from `sources:`. DOIs: `doi/10.xxxx##yyyy` → `https://doi.org/10.xxxx/yyyy`. Paper details appear as "Paper Details" subsection below content.

## Capitalization

- **BRIL** — always uppercase (protein name)
- **T4L** / **T4 lysozyme** — uppercase
- Protein/gene names, acronyms → standard scientific convention
- Ligand names (SMILES, compound IDs) → case-sensitive, exact

## Tables

- valid Kramdown: header row, separator row (`|---|---|`), data rows
- **NO empty rows** after headers (breaks table)
- no data → remove table and heading
- populate from source papers, not placeholders
- **NO markdown in cells**: no `**bold**`, no wikilinks, no `|` pipes
- missing data → leave cell empty, **NO "N/A" or "—"**

## Entity Classification (Step 1.5)

Classify every entity from raw paper:

| Question | If Yes → |
|----------|----------|
| specific solved structure (PDB ID, construct, purification protocol)? | **Protein** |
| chemical compound (detergent, salt, buffer, drug, lipid, tag)? | **Reagent** |
| protocol/technique with steps (how to do)? | **Method** |
| mechanism, family, principle, design strategy (how/why works)? | **Concept** |

**Concept threshold:** create page when paper introduces new protein family/subfamily, discusses mechanism central to work, uses design strategy worth documenting, references biophysical phenomenon explaining why something works. Skip passing mentions, tags.

**Ambiguity rules:**
- "LCP crystallization" → Method (has steps)
- "Lipid polymorphism" → Concept (principle, no protocol)
- "BRIL fusion" → Reagent (fusion protein) or Method (fusion strategy) — context-dependent
- "MFS transporter" → Concept (family taxonomy)
- "MFS transporter crystallization" → Method (technique)

**BUFFER ENTITIES (CRITICAL):** Common buffers are reagents, NOT background chemicals. ALWAYS create pages for: Tris, HEPES, MOPS, Sodium phosphate, Cacodylate, Acetate, Citrate, PIPES, Bicine, TES, Glycine, Ammonium acetate. Buffer YAML tags MUST use "buffer-" prefix (e.g., buffer-mops, buffer-phosphate) so the system auto-places them in reagents/buffers/. These buffers appear in purification buffers, crystallization reservoirs, and storage buffers — they are central reagents, not trivial details.

### Two-Pass Entity Classification

**Pass 1 (primary):** When first reading a raw paper, extract the main protein and its directly associated reagents/methods. Write YAMLs for these.

**Pass 2 (discovery):** After generating primary pages, re-read the raw paper. Identify ALL other entities mentioned — every detergent, ligand, lipid, additive, protein tag, method, and concept. For each:
- Does a wiki page already exist? → Load `index.md` and search the wiki catalog. Yes = note for cross-reference. No = proceed to threshold check.
- Does it meet the page threshold? → See Page Thresholds below.
- Can it be confidently classified? → Skip ambiguous entities (e.g., "DM" could be detergent or misread residue abbreviation).

**Page Thresholds** (note the two-pass context):
- Create page when entity appears in 2+ sources OR central to one source
- Add to existing page when source mentions something already covered
- DON'T create page for passing mentions, minor details, outside domain

## Page Thresholds

- **Create page** when entity appears in 2+ sources OR central to one source
- **Add to existing page** when source mentions something already covered
- **DON'T create page** for passing mentions, minor details, outside domain
- **Split page** when >200 lines — break into sub-topics with cross-links
- **Archive page** when fully superseded — move to `_archive/`, remove from index

## Entity Page Structures

### Protein Pages

**Sections (order):** 1. **Overview** — organism (italicized species), gene name, class, function, significance. 2. **Structure Determination** — table: Source | PDB ID | Resolution | Space Group | Construct | Ligand. 3. **Expression and Purification** — system, construct, Purification Workflow table (Step | Method | Resin | Buffer+Detergent | Notes), Final sample line. 4. **Crystallization** — table per paper: Parameter | Value. 5. **Biological / Functional Insights** — sub-sections per finding. 6. **Cross-References** — max 8.

**Quality:** PDB IDs accurate. Construct = truncation boundaries + fusion partners. Detergents/buffers/lipids wikilinked. All reagent names linked.

### Reagent Pages

**Sections (order):** 1. **Overview** — chemical class, function. 2. **Properties** — type-specific (see YAML schemas in WIKI-WORKFLOW.md). 3. **Use in Membrane Protein Work** — sub-sections per use case. 4. **Examples from This Wiki** — table: Protein | Concentration | Context | Result. 5. **Advantages and Disadvantages**. 6. **Comparison with Related Reagents** — optional (2+ reagents). 7. **Cross-References** — max 8.

**Quality:** Detergent pages: CMC, class, carbon chain length. Ligand pages: Ki/IC50/Kd, selectivity. Every reagent page links to ≥2 proteins.

### Method Pages

**Specific methods:** 1. **Overview** — 1-2 sentences. 2. **Principle**. 3. **Protocol** — Reagents, Steps, Conditions. 4. **Advantages**. 5. **Disadvantages**. 6. **Proteins Using This Method** — table: Protein | Resolution | PDB | Notes. 7. **Related Methods**. 8. **Related Reagents**.

**Overview/parent pages** (e.g., `crystallization.md`): 1. **Overview**. 2. **Methods** — table of sub-methods. 3. **Workflow Overview**. 4. **Comparison of Methods**. 5. **Related Resources**.

**Quality:** ≥3 outbound links. Overview ≥25 lines. Cite papers explicitly.

### Concept Pages

**Sections (order):** 1. **Overview** — definition, significance. 2. **Mechanism/Details** — biophysical basis, motifs, key residues. 3. **Examples in Membrane Protein Work** — bulleted list with links. 4. **Related Concepts**. 5. **Cross-References**.

**Quality:** ≥3 outbound links. Specific and actionable. Skip for things better as tags. ~50-100 lines. Split if >150. **NO properties tables or protocol steps** — narrative, not tabular.

## Tag Taxonomy

### Proteins
- Class: `gpcr`, `ion-channel`, `transporter`, `enzyme`, `receptor`, `channel`, `pump`, `porin`
- General: `membrane-protein`, `xray-crystallography`
- Pick ≥1 class tag + `membrane-protein`

### Reagents — Detergents
- `detergent-nonionic`, `detergent-zwitterionic`, `detergent-ionic`, `detergent-mild`, `detergent-strong`

### Reagents — Lipids
- `lipid`, `lipid-monoacyl`, `lipid-diacyl`, `lipid-sterol`, `lipid-analog`

### Reagents — Additives
- `additive-stabilizer`, `additive-reductant`, `additive-precipitant`, `additive-salt`, `additive-ph`, `additive-ligand`, `additive-antibody`

### Reagents — Buffers
- `buffer-tris`, `buffer-hepes`, `buffer-phosphate`, `buffer-acetate`, `buffer-citrate`, `buffer-mops`, `buffer-pipes`, `buffer-bicine`, `buffer-tes`, `buffer-glycine`, `buffer-ammonium-acetate`

### Reagents — Ligands / Antibodies / Protein Tags
- No fixed taxonomy; use descriptive tags

### Methods — Solubilization
- `solubilization-detergent`, `solubilization-lcp`, `solubilization-bicelle`, `solubilization-nanodisc`, `solubilization-smalp`, `solubilization-maltoside`

### Methods — Purification
- `purification-affinity`, `purification-ion-exchange`, `purification-size-exclusion`, `purification-tag`, `purification-fractionation`

### Methods — Cell Lysis
- `cell-lysis`, `cell-lysis-pressure`, `cell-lysis-mechanical`

### Methods — Crystallization
- `crystallization-vapor-diffusion`, `crystallization-lcp`, `crystallization-microbatch`, `crystallization-dialysis`, `crystallization-sitting-drop`, `crystallization-hanging-drop`

### Methods — Structure Determination
- `structure-xray`, `structure-sad`, `structure-mad`, `structure-molecular-replacement`, `structure-cryoem`, `structure-refinement`, `structure-model-building`

### Methods — Expression Systems
- `expression-system`

### Methods — Quality Assessment
- `quality-assessment`

### General
- `membrane-protein`, `xray-crystallography`, `sample-preparation`, `cryoprotection`, `seeding`, `additive-screen`

### Concepts
- `concept-transport-mechanism` (alternating access, rocker-switch)
- `concept-protein-family` (MFS, MIT, DHA, ABC, SLC)
- `concept-membrane-mimetic` (bicelles, nanodiscs, lipid polymorphism)
- `concept-crystallography-principle` (twinning, NCS, anomalous dispersion, crystal contacts)
- `concept-construct-design` (thermostabilization, truncation, glycosylation engineering, fusion partners)
- `concept-functional` (biased agonism, allosteric regulation, conformational dynamics)
- `concept-antibody-technology` (nanobody engineering, epitope mapping)

### Tag Governance

Curated, not freeform. New tags → 3-step: **Align** → use existing tag if fits. **Propose** → agent proposes with examples, user approves, adds to taxonomy, then uses. **Default** → too narrow? Don't create. Use closest existing or plain text. Missing > sprawl.

**Rule: every tag on page must appear in taxonomy.** New tag → add here first, then use.

## Correction Policy

When new info conflicts with existing wiki:

1. **Different conditions for same protein** — add as alternative, label with paper date. Keep old.
2. **Superseding paper** (same group, same protein, better resolution) — update page, note supersession in `log.md`.
3. **Factual error** (paper doesn't support claim) — remove/correct claim, log correction in `log.md`.
4. **Never retain unsupported claims** — if paper doesn't mention it, it doesn't belong.

## Source-Truth Verification

1. Read wiki page. Extract every claim: entity names, numbers (PDB IDs, resolutions, CMC, concentrations, MW), chemical properties, conditions, qualitative statements.
2. For each DOI in `sources:`, strip `doi/` → look up `raw/papers/<doi>.md`. Missing or short (<200 lines)? Flag.
3. Read each raw paper. Search for supporting evidence.
4. **Supported** (explicitly states or strongly implies) or **unsupported** (doesn't mention, contradicts, too vague).
5. Remove/correct all unsupported claims. Log corrections in `log.md`.

**Example:** GNP page lists CMC `0.17 mM` from `doi/10.1038##nature13074`. Raw paper has zero GNP mentions. Remove CMC and citation.

### Comments Column as Triage Signal

`Comments` column in `protein_doi_checklist.csv` = triage for Pass 2:
- **`ok`** → Low priority. **`no purification detergent/buffer`** → Medium. **`abstract only`, `data insufficient`** → High (manual review). **`skip —`** → verify skip correct. **`duplicate`** → check canonical variant. Sort CSV by Comments to prioritize audits.

## Page Checklist + What NOT to Do

**Before creating/editing:**
- [ ] Entity warrants own page? (2+ sources OR central to one)
- [ ] Filename lowercase-hyphen, no spaces
- [ ] `layout: default` in frontmatter
- [ ] `category` matches parent directory
- [ ] `created` and `updated` dates correct
- [ ] DOIs use `doi/` prefix + `##` separator
- [ ] Every table valid Kramdown (no empty rows after headers)
- [ ] ≥2 outbound wikilinks
- [ ] Cross-References trimmed to top 5-8, all wikilinks to existing pages
- [ ] Content verified against source papers
- [ ] `updated` date bumped

**NEVER:** push to git remotes (user only). Create pages for generic/broad topics (use tags). Leave empty tables. Add speculative content. Link to non-existent pages. Mix wikilinks and plain text in Cross-References. Use markdown links in auto-rendered References section. Use `echo`/`cat`/Python scripts for multi-file writes (use `write_file`, one page per call).