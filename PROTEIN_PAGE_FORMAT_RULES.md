# Protein Page Format Rules — X-ray MP Wiki

## 1. Link Format

**NEVER use `[[wikilink]]` syntax.** GitHub Pages does not support it.

**ALWAYS use markdown links with absolute paths:**
- Protein: `[page-title](/xray-mp-wiki/proteins/filename/)`
- Reagent: `[page-title](/xray-mp-wiki/reagents/detergents/filename/)`
- Method: `[page-title](/xray-mp-wiki/methods/crystallization/filename/)`
- Concept: `[page-title](/xray-mp-wiki/concepts/filename/)`

**Rule:** Every reagent, method, or protein mentioned in a page that has its own wiki page MUST be linked. No exceptions. If no page exists, create one or leave as plain text.

---

## 2. Required Sections (in order)

Every protein page MUST contain these sections, in this exact order:

1. **Overview**
2. **Structure Determination** (table)
3. **Expression and Purification**
4. **Crystallization** (table)
5. **Biological / Functional Insights**
6. **Cross-References**

No variations. No extra sections. No missing sections.

---

## 3. Section Specifications

### 3.1 Overview

Prose paragraph. Include:
- Organism (species name, italicized)
- Gene name
- Protein class (GPCR, transporter, ion-channel, enzyme, etc.)
- Biological function
- Therapeutic/scientific significance

### 3.2 Structure Determination

**Table format. One row per paper/structure.**

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| Su et al. (PNAS 2019) | 7C2M | 3.1 Å | P2₁2₁2₁ | MmpL3₇₇₃ | NITD-349 |
| Zhang et al. (Cell 2019) | 6XYZ | 2.59 Å | P2₁2₁2₁ | MmpL3-T4L | 6-DDTre |

**Column rules:**
- **Source**: Author et al. (Journal Year) — link to the raw paper's DOI in `sources:` frontmatter, not in this column
- **PDB ID**: Always include. If multiple structures from same paper, one row per PDB
- **Resolution**: X–Y Å range or single value with Å symbol
- **Space Group**: Always include if available
- **Construct**: Full construct name with truncation boundaries (residues), fusion partners (BRIL, T4L), and mutations
- **Ligand/Co-factor**: All ligands, cofactors, or substrate analogs co-crystallized

**Below table (optional):** Data collection notes, R-factors (R-work/R-free), beamlines, cryo-cooling temperature.

**Rule:** If a paper describes multiple structures (e.g., different ligand-bound states), each gets its own row.

### 3.3 Expression and Purification

- **Expression system** line
- **Construct** line
- **Purification Workflow table**

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Lysis | French Press | — | 20 mM Tris-HCl pH 8.0, 150 mM NaCl | 1,200 bars |
| 2. Solubilization | Detergent | — | 1% DDM in Tris buffer | 2 h, 4 °C |
| 3. Affinity | Ni-NTA | Talon resin | Wash: 50 mM imidazole in Tris buffer | Elution: 300 mM imidazole |
| 4. SEC | Size-exclusion | Superdex-6 | 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 10% glycerol, 0.05% DDM | 6-DDTre added |
| 5. Final SEC | Size-exclusion | Superdex-200 | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% DDM | Buffer exchange |

**Column rules:**
- **Step**: Numbered. `1. Lysis`, `2. Solubilization`, `3. Affinity`, `4. SEC`, etc.
- **Method**: Technique name (French Press, Ultrasonication, Detergent, Ni-NTA, SEC, etc.)
- **Resin / Column**: Specific product name (Talon, Superdex-6, Ni-NTA, etc.) or `—` if N/A
- **Buffer + Detergent**: FULL composition. Every salt, buffer, detergent, additive, concentration, pH. This is the most important column — if information is missing from the paper, leave empty. Never summarize.
- **Notes**: Temperatures, times, speeds, protease cleavage, buffer exchanges, concentration changes, ligand additions

**Below table (required):**
**Final sample**: [concentration] in [complete buffer + detergent + ligand composition]

**Rules:**
- Show every step described in the paper. If the paper skips a step, do NOT invent it.
- If purification refers to a previous publication, add: "See [linked paper] for full protocol."
- If no purification described (native extraction), state: "No purification described; direct solubilization from membranes."
- Document EVERY reagent mentioned. Link to its wiki page if one exists.

### 3.4 Crystallization

**Table format.**

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 20 mg/mL in 20 mM HEPES pH 7.5, 0.05% DDM |
| Reservoir | 25% PEG400, 0.1 M sodium acetate pH 5.4, 0.05 M magnesium acetate |
| Mixing ratio | 1:1 protein:reservoir |
| Temperature | 25 °C |
| Growth time | 1–2 weeks |
| Cryoprotection | Mother liquor + 5% PEG400 |

**Parameter rules:**
- **Method**: Vapor diffusion (hanging drop / sitting drop), LCP, microbatch, dialysis
- **Protein sample**: What went into the drop. Must match the final purification sample (or note if different). Include concentration, buffer, detergent, ligand.
- **Reservoir**: Full composition. Every precipitant, salt, buffer, additive, concentration.
- **Mixing ratio**: Protein:reservoir ratio (e.g., 1:1, 1:2)
- **Temperature**: °C
- **Growth time**: Duration if described
- **Protein-to-lipid ratio**: For LCP only (e.g., 1:2 w/w)
- **Cryoprotection**: How crystals were prepared for data collection

**Rules:**
- If multiple crystal forms from different papers, add a section header per paper (e.g., `### Su et al. (PNAS 2019)`) and include the table under it.
- All reagents in the table MUST be linked to their wiki pages.

### 3.5 Biological / Functional Insights

Prose + bulleted sub-sections. One sub-section per major finding.

**Sub-section naming:** Use descriptive names based on the actual content:
- "Ligand Binding"
- "Gating Mechanism"
- "Drug Targets and Inhibitors"
- "Proton-Relay Network"
- "Resistance Mutations"
- "Binding Pocket Features"

**Rules:**
- All reagent names mentioned in prose MUST be linked to their wiki pages.
- All protein names mentioned MUST be linked.
- All method names mentioned MUST be linked.
- If a ligand has a known Ki/Kd/IC50, include it.
- If structural features (residues, helices) are discussed, link to related concept pages where applicable.

### 3.6 Cross-References

**Bulleted list. Wikilinks NOT used — use markdown links.**

- `[a2a-adenosine-receptor](/xray-mp-wiki/proteins/a2a-adenosine-receptor/) — GPCR with BRIL fusion, similar crystallization`
- `[etb-receptor](/xray-mp-wiki/proteins/etb-receptor/) — ETB-Y5-T4L: thermostabilized GPCR construct`
- `[bril](/xray-mp-wiki/reagents/protein-tags/bril/) — Thermostabilized apocytochrome b562RIL fusion partner`
- `[lipidic-cubic-phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method`

**Rules:**
- Max 8 entries. Trim to most relevant.
- Group by type: proteins first, then reagents, then methods.
- Each entry has a one-line reason describing the connection.
- Every linked entity MUST have its own wiki page. If no page exists, do NOT link — either create one or leave as plain text in the prose.
- Links are absolute paths: `/xray-mp-wiki/<category>/<subdir>/<filename>/`

---

## 4. Frontmatter

```yaml
---
title: Human-Readable Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, transporter]
sources: [doi/10.1016##j.cell.2019.01.003, doi/10.1073##pnas.1901346116]
---
```

**Rules:**
- `layout: default` MUST be inside the frontmatter block (between the two `---` lines)
- `category` MUST be `proteins`
- `tags` use the taxonomy from SCHEMA.md (see below)
- `sources` uses `doi/` prefix with `##` as DOI separator (matches raw file naming)
- `updated` date MUST be bumped on every edit
- Multiple sources: comma-separated, all with `doi/` prefix

---

## 5. Tag Taxonomy (Proteins)

Use these tags from SCHEMA.md. Pick all that apply:

**Class tags:** `gpcr`, `ion-channel`, `transporter`, `enzyme`, `receptor`, `channel`, `pump`, `porin`

**General tags:** `membrane-protein`, `xray-crystallography`

**Pick at least one class tag + `membrane-protein`. Add `xray-crystallography` if structure was solved by X-ray.**

---

## 6. Table Formatting Rules (CRITICAL)

- **Valid Kramdown syntax only**: header row, separator row (`|---|---|`), data rows
- **Never leave empty rows after headers** — renders as broken table
- **No markdown inside cells**: no `**bold**`, no `[[wikilinks]]`, no `|` pipes
- **If a cell needs emphasis**, use plain text or put it in the `Notes` column
- **If data is missing from the paper**, leave the cell empty — do NOT write "N/A", "—", or "not described"
- **If a table has no data**, remove the entire table and its heading
- **Tables should be populated from source papers**, not left as empty placeholders

---

## 7. Reagent Documentation Rule (STRICT)

**Every reagent mentioned in a protein page MUST be documented.** This includes:

**Detergents:** DDM, OG, LMNG, CHS, digitonin, etc.
**Buffers:** Tris, HEPES, sodium acetate, etc.
**Salts/Additives:** NaCl, KCl, MgCl₂, glycerol, PEG400, PEG2000, imidazole, DTT, etc.
**Ligands:** Drug compounds, cofactors, substrate analogs, chromophores
**Lipids:** Monoolein, cholesterol, cardiolipin, phosphatidylcholine, etc.
**Protein tags:** BRIL, T4L, TEV protease, nanobodies, Fab fragments
**Expression media:** Any specific media or induction agents mentioned

**Rule:** If a reagent is mentioned in ANY section of a protein page AND a wiki page does NOT exist for it, the reagent page MUST be created. No exceptions.

**Linking rule:** Every reagent mention in prose, tables, or notes MUST be linked to its wiki page using markdown links.

---

## 8. Cross-Reference Rules

- **Maximum 8 entries** per page
- **Group by type**: proteins → reagents → methods
- **Each entry has a one-line reason**
- **All linked entities must have wiki pages**
- **No generic entries already discussed in the page body** (e.g., don't link `lipidic-cubic-phase` in Cross-References if LCP is described in the Crystallization section)
- **All Cross-Reference entries must be wikilinks to existing pages** — nothing else

---

## 9. Capitalization Rules

- **BRIL** — always uppercase in prose (the protein is "BRIL" or "bRIL" in construct names like `A2A-PSB1-bRIL`)
- **T4L** / **T4 lysozyme** — uppercase
- Protein names, gene names, and technical acronyms follow standard scientific convention
- Ligand names (SMILES codes, compound IDs) are case-sensitive and exact

---

## 10. Source-Truth Verification

- **If the raw paper doesn't mention it, it doesn't belong in the wiki**
- **Never infer or speculate** — if the paper is silent on a detail, leave the cell/field empty
- **Different experimental conditions for the same protein** — add as an alternative, label with paper date. Do not remove old conditions.
- **Superseding paper** (same group, same protein, better resolution) — update the page, note the supersession in `log.md`
- **Factual error** (paper doesn't support the claim) — remove or correct the claim and log the correction in `log.md`

---

## 11. Minimum Quality Standards

- **At least 2 outbound links** to other wiki pages (preferably more)
- **PDB IDs must be accurate** and linked to the correct structure
- **Construct details must include truncation boundaries and fusion partners**
- **Detergents, buffers, and lipids must be linked** to their reagent pages
- **Every page must have `layout: default` in frontmatter**
- **Category must match the parent directory** (file in `proteins/` → `category: proteins`)
- **Updated date must be bumped on every edit**