# Wiki Schema — X-ray Detergent Wiki

## Domain

This wiki documents the **reagents, methods, and protocols** used in the X-ray crystallography of membrane proteins. The focus is on the practical workflow:

1. **Solubilization** — detergents, lipids, additives used to extract membrane proteins from membranes
2. **Cell lysis** — cell disruption methods (microfluidizer, French press, sonication)
3. **Expression systems** — E. coli, Pichia, Sf9, HEK293 for recombinant protein production
4. **Purification** — affinity chromatography, SEC, resins (TALON, Superdex), concentration (Amicon)
5. **Protein tags** — fusion partners (BRIL, T4L), cleavage enzymes (TEV protease)
6. **Crystallization** — precipitants, additives, crystallization methods (vapor diffusion, lipid cubic phase, etc.)
7. **Structure determination** — X-ray data collection, phasing methods, refinement reagents
5. **Membrane protein class** — specific types of membrane proteins (GPCRs, ion channels, transporters, etc.)

Entity types:
- **Proteins**: Specific membrane proteins whose structures were determined
- **Reagents**: Detergents, lipids, additives, buffers, ligands, protein tags (BRIL, T4L, TEV), antibodies
- **Methods**: Solubilization, cell lysis, expression systems, purification, crystallization, structure determination
- **Conditions**: Screen components, crystallization conditions
- **Concepts**: General topics (e.g., LCP, bicelle, nanodisc, SMALP)

## Conventions

- File names: lowercase, hyphens, no spaces (e.g., `dodecyl-maltoside.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- Source DOI references use forward slashes: `10.1016/j.cell.2015.06.002`
- Raw source file names use double-hash: `10.1016##j.cell.2015.06.002.md`

## Directory Structure

The wiki uses a hierarchical directory structure that mirrors the index organization:

```
wiki/
├── proteins/                 — Protein entity pages
├── reagents/
│   ├── detergents/           — Detergent pages (DDM, OG, LMNG, etc.)
│   ├── lipids/               — Lipid pages (cholesterol, monoolein, cardiolipin, CHS)
│   ├── buffers/              — Buffer pages (Tris, HEPES)
│   ├── additives/            — Additive pages (NaCl, glycerol, PEGs, Li2SO4)
│   ├── ligands/              — Ligand/drug pages (selatogrel, MP1104, etc.)
│   ├── protein-tags/         — Protein tag tools (BRIL, T4L fusion partners, TEV protease)
│   └── antibodies/           — Antibody-based crystallization facilitators (nanobodies, Fab fragments)
├── methods/
│   ├── purification/         — Purification methods and resins (affinity, SEC, TALON, Superdex, Amicon)
│   ├── cell-lysis/           — Cell disruption methods (microfluidizer, French press)
│   ├── crystallization/      — Crystallization method pages
│   ├── structure-determination/ — Structure determination method pages
│   ├── solubilization/       — Solubilization method pages
│   ├── expression-systems/   — Expression system pages (baculovirus, HEK293, Pichia, Sf9)
│   └── quality-assessment/   — Quality assessment methods (Coomassie staining)
├── SCHEMA.md
├── index.md
└── log.md
```


## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: protein | reagent | method | concept | comparison
tags: [from taxonomy below]
sources: [doi/10.xxxx/xxxxx]
---
```

## Tag Taxonomy

### Proteins
- gpcr, ion-channel, transporter, enzyme, receptor, channel, pump, porin

### Reagents — Detergents
- detergent-nonionic, detergent-zwitterionic, detergent-ionic, detergent-mild, detergent-strong

### Reagents — Lipids
- lipid, lipid-monoacyl, lipid-diacyl, lipid-sterol, lipid-analog

### Reagents — Additives
- additive-stabilizer, additive-reductant, additive-precipitant, additive-salt, additive-ph, additive-ligand, additive-antibody

### Reagents — Buffers
- buffer-tris, buffer-hepes, buffer-phosphate, buffer-acetate, buffer-citrate

### Methods — Solubilization
- solubilization-detergent, solubilization-lcp, solubilization-bicelle, solubilization-nanodisc, solubilization-smalp, solubilization-maltoside

### Methods — Purification
- purification-affinity, purification-ion-exchange, purification-size-exclusion, purification-tag, purification-fractionation

### Methods — Cell Lysis
- cell-lysis, cell-lysis-pressure, cell-lysis-mechanical

### Methods — Crystallization
- crystallization-vapor-diffusion, crystallization-lcp, crystallization-microbatch, crystallization-dialysis, crystallization-sitting-drop, crystallization-hanging-drop

### Methods — Structure Determination
- structure-xray, structure-sad, structure-mad, structure-molecular-replacement, structure-cryoem, structure-refinement, structure-model-building

### Methods — Expression Systems
- expression-system

### Methods — Quality Assessment
- quality-assessment

### General
- membrane-protein, xray-crystallography, sample-preparation, cryoprotection, seeding, additive-screen

## Page Thresholds

- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Page Structure

### Protein Pages
- Overview (gene name, organism, function, class)
- Structure determination (PDB ID, resolution, method)
- Solubilization reagents used
- Purification strategy
- Crystallization conditions
- Key findings

### Reagent Pages (Detergent/Lipid/Additive)
- Chemical class and structure
- Properties (CMC, HLB, transition temp)
- Common uses in membrane protein work
- Advantages and disadvantages
- Proteins successfully solubilized/purified/crystallized with this reagent
- Related reagents

### Method Pages
- Description of the technique
- When to use it
- Key reagents/equipment
- Advantages and limitations
- Examples from the literature

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report

## Lint Audit (Every 5 DOIs)

After ingesting every 5 raw papers, audit the wiki for:
1. **Orphan pages** — pages with no inbound `[[wikilinks]]` from other pages
2. **Missing pages** — concepts referenced but don't have their own page
3. **Contradictions** — claims that conflict across pages
4. **Stale claims** — things superseded by a more recent source in raw/
5. Suggest fixes for user to decide on