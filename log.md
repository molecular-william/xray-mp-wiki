# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-04-26] create | Wiki initialized
- Domain: X-ray crystallography reagents for membrane protein structure determination
- Structure: SCHEMA.md, index.md, log.md
- Raw papers: 399 markdown files in raw/papers/
- DOIs: 399 to process, 0 incorporated

## [2026-04-26] ingest | Batch 1 (5 DOIs)
- DOIs: 10.1002/1873-3468.14136 (NtMATE2, LCP), 10.1002/anie.201302374 (Opsin GPCR, OG), 10.1002/anie.202115545 (A2AAR, single-mutation, Preladenant), 10.1006/jmbi.1994.0097 (Rps. viridis RC, LDAO, 2.3A), 10.1016/j.bbabio.2023.148986 (PSI-LHCI, β-DDM→GDN, resting state)
- Pages: 18 (5 proteins, 9 reagents/methods, 4 methods)
- DOIs incorporated: 5

## [2026-04-26] ingest | Buffer salts + purification entities (Batch 1 follow-up)
- Pages: 15 (buffer reagents, purification media, expression systems, methods)
- Total pages: 33 | DOIs: 5

## [2026-04-26] ingest | Batch 2 (5 DOIs)
- DOIs: 10.1016/j.bbrc.2023.149393 (A2AAR-Rag31+photoNECA, 3.34A), 10.1016/j.bcp.2022.115291 (P2Y12+selatogrel, 2.8A), 10.1016/j.cell.2015.06.002 (LPA1+3 antagonists, 2.9-3.0A), 10.1016/j.cell.2016.09.056 (CD81+cholesterol, 2.95A), 10.1016/j.cell.2016.12.033 (5-HT2B+LSD, 2.9A)
- Pages: 10 (5 proteins, 5 reagents)
- Total: 43 pages | DOIs: 10

## [2026-04-26] ingest | Batch 1 missing entity pages
- Pages: 6 (NG, HpG, PEG 400, Dialysis, Microbatch, Cryo-EM)
- Updated: 6 (opsin, PSI-LHCI, PEG 400, Cryo-EM, Dialysis, Microbatch, NG, HpG)
- Total: 49 pages | DOIs: 10

## [2026-04-26] lint | Batch 1 missing entity audit
- Created pages for all genuinely missing entities from lint output
- False positives: NaCl→sodium-chloride, Rhodopseudomonas→rps-viridis-reaction-center, crystallization-lcp→lipidic-cubic-phase, structure-xray→xray-crystallography
- structure-mad/sad consolidated under xray-crystallography.md
- Remaining issues: none

## [2026-04-27] ingest | Batch 3a — SemiSWEET (DOI 10.1016/j.cell.2017.03.010)
- DOI: LbSemiSWEET alternating access transporter
- Pages: 2 (LbSemiSWEET, Glucose)
- Updated: 1 (xray-crystallography.md)
- Total: 51 pages | DOIs: 11

## [2026-04-27] ingest | Batch 3b — Kappa Opioid Receptor (DOI 10.1016/j.cell.2017.12.011)
- DOI: Kappa opioid receptor active-state structure
- Pages: 4 (Kappa OPR, MP1104, Salvinorin A)
- Updated: 1 (xray-crystallography.md)
- Total: 55 pages | DOIs: 12

## [2026-04-27] ingest | Batch 3c — ADP/ATP Carrier (DOI 10.1016/j.cell.2018.11.025)
- DOI: Mitochondrial ADP/ATP carrier matrix-open state
- Pages: 4 (ADP/ATP Carrier, Bongkrekic acid, Carboxyatractyloside, Cardiolipin)
- Updated: 1 (xray-crystallography.md)
- Total: 59 pages | DOIs: 13

## [2026-04-27] ingest | Batch 3d — MmpL3 (DOI 10.1016/j.cell.2019.01.003)
- DOI: MmpL3 anti-TB drug target
- Pages: 5 (MmpL3, SQ109, AU1235, ICA38, Rimonabant)
- Updated: 1 (xray-crystallography.md)
- Total: 64 pages | DOIs: 14

## [2026-04-27] ingest | Batch 3e — AT1R (DOI 10.1016/j.cell.2018.12.006)
- DOI: AT1R active-state with S1I8+Nb.AT110i1, 2.9A
- Pages: 4 (AT1R, MNG, S1I8, Nb.AT110i1)
- Updated: 4 (monoolein, CHS, LCP, xray-crystallography)
- Total: 68 pages | DOIs: 24

## [2026-04-27] ingest | Batch 3e-2 — NaVAb (DOI 10.1016/j.cell.2019.06.031)
- DOI: NaVAb resting-state, 4.0A cryo-EM
- Pages: 2 (NaVAb, Digitonin)
- Updated: 1 (cryoem.md)
- Total: 70 pages | DOIs: 25

## [2026-04-27] reorganize | Wiki directory structure reorganization
- Reagents subcategories: detergents/(9), buffers/(2), lipids/(2), additives/(5), ligands/(14), purification/(4)
- Methods subcategories: purification/(4), crystallization/(4), structure-determination/(3)
- Moved monoolein.md: crystallization/ → reagents/lipids/
- Moved cardiolipin.md: lipids/ → reagents/lipids/
- Deleted empty dirs: conditions/, detergents/, purification/, screens/, solvents/, templates/, crystallization/, lipids/
- Deleted .ipynb_checkpoints
- Updated index.md (69 entries), SCHEMA.md
- Total: 69 pages (15 proteins, 42 reagents, 12 methods)

## [2026-04-27] ingest | Batch 4 — AcrB + Linezolid (DOI 10.1007/s10969-013-9154-x)
- DOI: AcrB-Linezolid complex, 3.5A, PDB 4K7Q
- Pages: 4 (AcrB, Linezolid, PEG 4000, Sodium phosphate)
- Updated: 6 (DDM, Tris, Glycerol, Imidazole, Vapor diffusion, X-ray crystallography)
- Total: 73 pages | DOIs: 26

## [2026-04-27] ingest | Batch 5 — KirBac (DOI 10.1016/j.cell.2010.05.003)
- DOI: KirBac interdependent gating, polyamine block
- Pages: 6 (KirBac, Spermine, Anzergent 3,12, Structural phospholipids, IMAC, Ion channels)
- Updated: 4 (X-ray crystallography, Vapor diffusion, LCP, NaVAb)
- Total: 79 pages | DOIs: 27

## [2026-04-27] ingest | Batch 6 — ETB Receptor (DOI 10.1016/j.bbrc.2019.12.091)
- DOI: ETB-S6b complex, 3.0A, PDB 6LRY
- Pages: 5 (ETB, Sarafotoxin S6b, Sf9, T4 lysozyme, Baculovirus)
- Updated: 13 (DDM, LMNG, CHS, TALON, Tris, Glycerol, NaCl, Imidazole, TEV, Superdex, Affinity chromatography, IMAC, SEC, Vapor diffusion, X-ray crystallography, LCP, A2AAR, Nb.AT110i1)
- Total: 84 pages | DOIs: 28

## [2026-04-27] ingest | Batch 7a — SotB (DOI 10.1016/j.bbrc.2020.11.096)
- DOI: SotB 4 conformations (occluded, inward-facing, inward-open)
- Pages: 4 (SotB, MFS Transporter, Alternating Access, DHA Antiporter)
- Updated: 3 (nTMATE2, ADP/ATP Carrier, X-ray crystallography)
- Total: 88 pages | DOIs: 29

## [2026-04-27] ingest | Batch 7b — AT1R ZD7155 by SFX/XFEL (DOI 10.1016/j.cell.2015.04.011)
- DOI: AT1R-ZD7155, 2.9A, PDB 4YAY; serial femtosecond crystallography at XFEL
- Pages: 4 (ZD7155, Losartan, Candesartan, BRIL, SFX method)
- Updated: 6 (AT1R, X-ray crystallography, DDM, CHS, Sf9, BRIL)
- Total: 93 pages | DOIs: 30

## [2026-04-27] LINT | Post-batch 7
- DOI format: All 139 files fixed — slashes → ##
- Wikilink orphans: 88 → 20 (fixed 68 via title→filename mapping + manual)
- Index coverage: 45 → 93 links (all 93 pages)
- Remaining 20 orphans: a2a-star2, nanobody-nb39, bril-fusion, NH4H2PO4, Li2SO4, DM, GNP, mmpL3, elinogrel, clopidogrel, valsartan, irbesartan, telmisartan
- All frontmatter present, no empty pages, no duplicates
- Total: 93 pages | DOIs: 45

## [2026-04-27] LINT | Orphan page creation
- Created 13 orphan pages: valsartan, irbesartan, telmisartan, elinogrel, clopidogrel, selatogrel, mmpL3, A2A-STAR2, dm, gnp, nh4h2po4, li2so4, nanobody-nb39, bril-fusion
- All DOI formats fixed (slashes → ##)
- All existing files updated with correct wikilinks
- Remaining orphans: 0
- Total: 106 pages

## [2026-04-27] create | Solubilization method page
- Created wiki/methods/solubilization/solubilization.md
- Synthesized from 12 raw papers: CusA (JMB 2009), DraNramp (eLife 2023), A1-AR (Cell 2017), ETB (BBRC 2019), CCR2A (Structure 2018), MdfA (JMB 2018), LacY (PNAS 2011), nTMATE2 (Proteins 2014), MmpL3 (Cell 2018), NMDA (Nature 2018), MastR (JBC 2012)
- Covers: cell lysis, membrane isolation, detergent selection, standard protocols, stabilizers, clarification, detergent exchange
- SCHEMA.md updated, index.md rebuilt (105→106)
- Total: 106 pages

## [2026-04-27] ingest | Batch 8 — ZntB, NupG, ADP/ATP Carrier
- DOIs: 10.1002/pro.215 (ZntB, V. parahaemolyticus, 1.90A, pentameric), 10.1016/J.FEBSLET.2005.09.061 (ADP/ATP Carrier, bovine, cardiolipin, 2.8A), 10.1016/j.febslet.2008.07.063 (DsbB — skipped, outside scope), 10.1016/j.immuni.2020.02.004 (IL-17RC/IL-17F — skipped), 10.1016/j.jbc.2021.100479 (NupG, E. coli, MFS, 3.0A, LCP)
- Pages: 3 (ZntB, NupG, LAPAO)
- Updated: 1 (ADP/ATP Carrier — bovine AAC, cardiolipin dimerization, LAPAO solubilization, Jeffamine crystallization)
- Skipped: DsbB (redox enzyme), IL-17RC (cytokine complex)
- DOIs incorporated: 34
- Index: 106→108 | Total: 108 pages

## [2026-04-27] lint | Batch 8
- Created: cora-mg-transporter.md, metal-ion-transporter.md
- Orphans: 2→0
- Lint: 0 issues
- Index: 108→110 | Total: 110 pages

## [2026-04-27] update | Protein pages — reagent enrichment (6 pages)
- 5ht2b-receptor: HEK293, MNG-3, Ni-NTA, LCP (monoolein, MgCl2, PEG 400)
- cd81-tetraspanin: Sf9, DDM, Ni-NTA, Superdex 200, LCP (monoolein, sodium acetate, PEG 400)
- kappa-opioid-receptor: HEK293S, DDM, FLAG/Ni-NTA, Superdex 200, LCP (monoolein, Tris/MgCl2, PEG 300)
- lpa1-receptor: HEK293S, DDM, Ni-NTA, Superose 6, CHS, LCP (monoolein+cholesterol)
- p2y12-receptor: Sf9, DDM, IMAC+selatogrel, Superdex 200, LCP (monoolein, sodium citrate, PEG 400), D294N
- a2a-adenosine-receptor: HEK293S, DDM, Ni-NTA, Superdex 200, PEG 400 sitting-drop
- All pages now include solubilization, purification, crystallization sections
- Lint: 0 issues | Total: 110 pages

## [2026-04-27] update | Protein pages — reagent enrichment (4 pages)
- lb-semisweet: E. coli BL21, DDM, Ni-NTA, Superdex 200, LCP (monoolein, sodium acetate, PEG 400)
- navab-sodium-channel: Sf9, DDM, FLAG/Ni-NTA, SEC, digitonin cryo-EM prep, activated-state crystallization
- mmpL3: Major rewrite — 3 structure sources (Su PNAS 2019, Zhang Cell 2019, Yang JMB 2020), M. smegmatis, DDM, Ni-NTA, Superose-6, vapor diffusion (PEG 400/PEGMME 350), NITD-349/SPIRO inhibitors, resistance mutations
- sotb: Truncated source noted, needs enrichment
- All 10 pages now have solubilization, purification, crystallization
- Lint: 0 issues | Total: 110 pages

## [2026-04-27] bug-fix | Comprehensive content audit
- Fixed "ng" word-boundary bug (~150 pages): bindi[[ng]]→binding, usi[[ng]]→using, ra[[ng]]e→range, homol[[og]]→homolog, etc.
- Fixed double brackets `]]]` (~17 pages) → `]]`
- Fixed wikilink bleeding into text (~15 pages)
- Fixed index.md duplicate wikilink targets (nanobody→nanobody-nb-at110i1, nanobody-nb39)
- Fixed empty sources arrays (9 pages) → added TODO notes
- Fixed invalid/incorrect DOIs (ddm.md placeholder removed, dm.md invalid nature13074 removed)
- Fixed DOI format inconsistency (ogng.md: doi: → doi/)
- Fixed excessive blank lines in frontmatter (~8 pages)
- Fixed duplicate table entries (bril.md, angiotensin-ii-type-1-receptor.md)
- Fixed missing/truncated content (sotb.md, nupg-nucleoside-transporter.md)
- Fixed self-referencing wikilinks (~10 pages): li2so4, peg-400, nanobody
- Fixed missing tags (nanobody-nb-at110i1.md) → [additive-antibody, sample-preparation]
- Removed stale .ipynb_checkpoints
- Lint: 3 issues (checklist.md no frontmatter — intentional; checklist/nanobody not in index — intentional)
- Page count: 128→120 (2 checkpoint files removed, 120 wiki pages remain)

## [2026-04-28] reorganize | Directory structure (3 new subdirectories)
- Created reagents/antibodies/ — moved 4 files: nanobody.md, nanobody-nb39.md, nanobody-nb-at110i1.md, fab-fragments.md
- Created methods/expression-systems/ — moved 3 files: baculovirus-expression.md (from methods/purification/), hek293-cells.md (from reagents/), pichia-pastoris.md (from reagents/)
- Created methods/quality-assessment/ — moved 1 file: coomassie-staining.md (from reagents/)
- Moved cholesterol-hydrogen-succinate.md: reagents/ → reagents/lipids/
- Fixed frontmatter tags/types for all moved files
- Removed imidazole.md from "Other Reagents" — kept at root (cross-category)
- Removed monoolein.md from crystallization/ in index — kept in crystallization/ (primarily LCP medium)
- Updated SCHEMA.md: added directory tree + expression-system/quality-assessment tag taxonomy
- Rebuilt index.md: CHS→Lipids, nanobodies/Fab→Antibodies, baculovirus/HEK293/Pichia→Expression Systems, coomassie→Quality Assessment
- Directory counts: proteins/(20), reagents/detergents/(13), reagents/buffers/(3), reagents/lipids/(4), reagents/additives/(12), reagents/ligands/(25), reagents/purification/(7), reagents/antibodies/(4), reagents/imidazole.md(root/1), methods/purification/(5), methods/expression-systems/(3), methods/crystallization/(4), methods/solubilization/(1), methods/structure-determination/(4), methods/quality-assessment/(1), concepts/(7), root meta(4)
- Total: 120 pages

## [2026-04-28] source-audit | Empty sources + raw paper enrichment
- Added sources to 9 pages: sodium-acetate, jeffamine, peg-2000, peg-300, sodium-citrate, dm, ion-channels, cora-mg-transporter, metal-ion-transporter
- Skipped: nh4h2po4.md (no source in incorporated papers)
- Enriched 4 pages from raw paper re-reads:
  - cd81-tetraspanin.md: MD simulation details (EC2 open/closed, cholesterol stabilization, D196-K201 salt bridge)
  - navab-sodium-channel.md: Resting-state VS details (S3-S4 loop new fold, S4 inward ~11.5A, S4-S5 linker elbow, KAV electrophysiology)
  - zntb-transporter.md: Pentamer formation (α6 stalk critical, buried surface areas, truncation artifact)
  - cora-mg-transporter.md: Pentamer formation section from ZntB comparison
- Pages modified: 13 | Total: 120 pages

## [2026-04-28] source-audit | Paper 1 re-read: NtMATE2 (10.1002##1873-3468.14136)
- Updated: nTMATE2-transporter.md — major enrichment (Expression: Pichia strain/plasmid/selection/Microfluidizer; Purification: exact TALON buffer compositions; Amicon concentration; beamline/software; 6-section format)
- Created: microfluidizer.md (M-110EH cell lysis), nicotine-ligand.md (co-crystallization ligand)
- Fixed: nh4h2po4.md (added source DOI, removed TODO)
- Already had NtMATE2 content (no changes): lmng, CHS, tev-protease, amicon-filters, superdex-columns, monoolein, pichia-pastoris, tris-buffer, hepes-buffer, sodium-chloride, glycerol, mfs-transporter, xray-crystallography
- Total: 118 pages

## [2026-04-28] reorganize | Purification directory restructuring
- Merged imac.md into affinity-chromatography.md (IMAC is subtype of affinity chromatography)
- Moved talon-resin.md, superdex-columns.md, amicon-filters.md: reagents/purification/ → methods/purification/
- Created reagents/protein-tags/ — moved tev-protease.md, bril.md, t4-lysozyme.md (GPCR fusion partners)
- Created methods/cell-lysis/ — moved microfluidizer.md (upstream of purification)
- Moved sf9-cells.md: to methods/expression-systems/
- Deleted empty reagents/purification/
- Updated index.md, SCHEMA.md, scripts/index-rebuild.py
- Total: 117 pages (imac.md merged, no pages lost)

## [2026-04-28] protein-page-audit | Focused on reagent/structural resolution workflow
- Re-read SCHEMA.md + all 21 protein pages against expected structure
- Expected: Overview, Structure Determination, Solubilization reagents, Purification strategy, Crystallization conditions, Key findings
- Fixed:
  - angiotensin-ii-type-1-receptor.md: Added Expression/Purification section; reorganized 1% DDM+0.2% CHS solubilization; added Crystallization (4YAY + 6DO1)
  - kirbac.md: Expanded solubilization/purification (1% Anzergent 3,12, 20,000 psi homogenizer, Ni-IMAC+SEC, ~8mg/mL, 19°C vapor diffusion Bio21 C3)
  - psi-lhci-supercomplex.md: Removed empty Cross-References; converted bare wikilinks to proper Cross-References with descriptions; added related photosynthetic complexes
  - sotb.md: Added PDB IDs (6Y5X–6Y5C); noted truncated source; added MFS convention-based solubilization/purification estimates
  - rps-viridis-reaction-center.md: Added Luzzati error (0.26A), Ramachandran stats, OG solubilization, LDAO crystal detergent, key reagents table
- Unchanged (already focused): 5ht2b-receptor, a2a-adenosine-receptor, a2a-star2, acrB, adenine-nucleotide-transporter, cd81-tetraspanin, etb-receptor, kappa-opioid-receptor, lb-semisweet, lpa1-receptor, mmpL3, navab-sodium-channel, nTMATE2-transporter, nupg-nucleoside-transporter, opsin-gpcr, p2y12-receptor, zntb-transporter
- index.md updated

## [2026-04-28] ingest | 10.1016##J.JMB.2004.08.090 — Bovine Rhodopsin Trigonal Form
- Raw: Structure of Bovine Rhodopsin in Trigonal Crystal Form (2.65A, P3₁)
- Created: bovine-rhodopsin.md — native bovine rod outer segment disk membranes
  - C8E4 + 0.05% LDAO solubilization; ordered LDAO at H6 kink; structural phospholipids; helix kink analysis; water-mediated H-bond networks
- Updated: opsin-gpcr.md (DOI sources, cross-ref to bovine-rhodopsin, LDAO cross-ref)
- Updated: lDAO.md (DOI sources, Bovine Rhodopsin section with binding data)
- index.md: 117→118 pages

## [2026-04-28] ingest | 10.1016##J.JMB.2007.03.007 — Recombinant Rhodopsin N2C/D282C
- Raw: Crystal Structure of Thermally Stable Rhodopsin Mutant
- Key: First recombinant GPCR structure (COS-1 cells)
- Updated bovine-rhodopsin.md — Recombinant N2C/D282C section:
  - COS-1 expression (~0.6mg yield, 10% higher than native)
  - 1D4 immunoaffinity, Sephadex G50 DDM→C8E4 exchange
  - Crystallization: 1.2–1.7M Li2SO4, 0.1M Hepes pH 7.5, 0.05% LDAO, 10mg/ml
  - Microcrystallography (5µm beam, ESRF ID13), P3₁, 3.4A, PDB 2J4Y
  - Engineered C2-C282 disulfide: +10°C stability, fixes N-terminal cap
  - Triple mutant N2C/N15D/D282C (deglycosylated): no improvement
- Updated: opsin-gpcr.md, li2so4.md, lDAO.md
- checklist.csv: Updated both DOIs

## [2026-04-28] ingest | 10.1016##J.JMB.2008.04.017 — PorB Porin
- Raw: A Putative α-Helical Porin from Corynebacterium glutamicum
- Created: porb-porin.md — First α-helical porin from bacterial outer envelope; detergent-free purification
  - E. coli GST fusion, factor Xa cleavage, GST affinity + SEC (S75-26/60), NO DETERGENT
  - 4 crystal forms, 16 molecules, 1.8A (Form I, P4₁2₁2), BESSY/SLS
  - Pentameric (C₅) α-helical channel model, polar interior
  - Ca²⁺/Zn²⁺ intersubunit cross-links; citrate blocks by chelation
  - Crystallization: Hampton/Jena/Emerald screens, MPD cryoprotection
- checklist.csv: Updated

## [2026-04-28] ingest | 10.1016##J.JMB.2009.04.001 — MexB RND Multidrug Exporter
- Raw: Crystal Structure of Multidrug Exporter MexB from Pseudomonas aeruginosa
- Created: mexb.md — Inner membrane component of MexAB-OprM tripartite efflux pump
  - E. coli C43(DE3), pET28, C-terminal His-tag
  - 1% DDM (Anatrace D310LA); Ni-NTA + Superdex 200 SEC (0.03% DDM maintained)
  - P1, 3.0A, MR from AcrB (2J8S), 2 trimers in AU
  - Asymmetric homotrimer: 3 conformational states
  - DDM bound in multidrug cavity (Val47, Ser48, Gln125, Val177, Gly179, Ser180, Gln273, Arg620)
  - Proton translocation: Asp407, Asp408 (TM4), Lys939 (TM10)
  - Unique subunit A vs AcrB — PC2 shift closes periplasmic portal
- Updated: acrB.md, ddm.md
- index.md: 119→120 pages | checklist.csv: Updated

## [2026-04-28] ingest | 10.1016##J.JMB.2009.05.082 — c-Ring Rotor
- Raw: Complete Ion-Coordination Structure in Rotor Ring of Na+-Dependent F-ATP Synthases
- Note: Re-refinement of Meier et al. 2005 Science (PDB 1YCE→2WGM). Original methods in 2005 Science paper (not in raw papers).
- Created: c-ring-rotor.md — c11 rotor ring from Ilyobacter tartaricus Na+-ATP synthase
  - 2.35A, P2₁, 4 rings in AU (44 c-subunits)
  - Complete Na+ coordination: 5 ligands (Gln32, Val63, Glu65, Ser66, + buried structural water)
  - Thr67 hydroxyl coordinates water — KEY distinction Na+ vs H+-ATP synthases
  - 44 fatty acid chains (membrane lipids)
  - MD confirms water essential for Na+ selectivity
  - Action needed: Download Science paper (10.1126/science.1108259) for purification/crystallization methods
- index.md: 120→121 pages | checklist.csv: Updated

## [2026-04-28] create | imac.md — Immobilized Metal Affinity Chromatography
- Created: imac.md — IMAC for His-tag purification
  - Ni-NTA, TALON (Co2+), IDA variants
  - Protocol: equilibration, binding, wash (10-40mM imidazole), elution (150-500mM imidazole)
  - Applications: E. coli, Sf9, HEK293, Pichia
  - Detergent compatibility: DDM, LMNG, OG, etc.
- Updated: imidazole.md (affinity-chromatography→imac), p2y12-receptor.md (affinity-chromatography→imac)
- index.md: Added IMAC to Purification Methods

## [2026-04-28] batch | 5 DOIs incorporated (DOI 6-10)

### DOI 6: 10.1016##J.MOLCEL.2011.10.020 — ICMT
- Created: icmt — Integral membrane SAM-dependent methyltransferase
  - Ma-ICMT (Methanosarcina acetivorans), 5 TM helices + cytosolic helix, 3.4A, PDB 4A2N
  - SAM pocket in catalytic subdomain, substrate access tunnel from membrane
  - Arg163 (M2 motif) positions substrate carboxylate
  - E. coli C41(DE3), Ma-ICMT-GFP-His7, 20°C overnight
  - Ni-NTA → IEC → SEC; 0.024% DDM
  - Crystallization: 8mg/ml, 20mM MES pH 6.5, 200mM NaCl, 10% glycerol, 0.024% DDM, 5mM SAH, 0.5mg/ml polar lipids
  - SAD: KAu(CN)2/EMTS, Diamond I02/I03

### DOI 7: 10.1016##J.STR.2012.03.014 — β1-Adrenoceptor Biased Agonists
- Created: beta1ar-biased-agonists — β1AR-m23 + bucindolol (3.2A) + carvedilol (2.3A)
  - PDB 4AMI/4AMJ, P2₁
  - Biased agonism: G protein-independent activation, inverse/partial G protein antagonism
  - EL2+TM7 interactions unique to biased agonists
  - Ser215⁵,⁴⁶ interhelical H-bond (partial agonist-like); no binding pocket contraction
  - H8-H1: Arg355⁸,⁵⁶ H-bonds Ser68¹,⁵⁹/Thr69¹,⁶⁰
  - Arg/Gly389 polymorphism structural explanation
  - 5 detergent molecules (bucindolol), 12 (carvedilol)

### DOI 8: 10.1016##J.STR.2014.12.012 — PepTSo
- Created: peptso — POT family transporter, S. oneidensis, 3.0A, PDB 4UVM
  - 12 TM helices, two inverted 6-helix repeats, P4₁2₁2
  - Double scissor-switch gating: periplasmic (H1,H2,H7,H8), cytoplasmic (H4,H5,H10,H11)
  - Salt bridges: D136-K439, K84-D79 stabilize outward-facing
  - Proline kinks H8 (P345, P353) essential for transport
  - DEER confirms conformational dynamics; MD: inward/occluded/outward states

### DOI 9: 10.1016##S0022-2836(03)00024-X — LH2
- Created: lh2-rps-acidophila — LH2 from Rps. acidophila at 2.0A (100K), TLS refinement
  - C₉ nonameric ring, 18 B850 BChl a (9 dimers), 9 B800, 2 rhodopin glucoside/unit
  - TLS: 48 tensors optimal, functionally relevant pigment motions
  - B850-Ueq=0.4A², B800-Ueq=0.6A², inter-pigment displacements ~0.7A
  - Ligands: B850→α-His31/β-His30, B800→α-Met1 (carboxy-modified)
  - Detergent: β-octyl glucoside (BOG)
  - TLS motions (3-7ps) may drive energy transfer

### DOI 10: 10.1016##S0969-2126(99)80118-X — Bacteriorhodopsin
- Created: bacteriorhodopsin-19a — bR from Halobacterium salinarum in LCP at 1.9A
  - 7 TM helices, retinal→Lys216 Schiff base
  - 8 ordered waters in proton pathway (Schiff base→Asp85→Asp212→Arg82→Glu194→Glu204)
  - 9 lipid phytanyl moieties modeled (native PM lipids)
  - MALDI-MS single crystal: PGP-Me, TGD, S-TGA-1, S-TeGa
  - LCP in monoolein — preserves native lipid environment
  - Cytoplasmic side more flexible (B-factors 24-33 vs 19-26A²)
  - No cytoplasmic waters — hydrophobic seal (Val49-Leu93)

### Updates
- index.md: 121→126 pages (5 new proteins + monoolein lipid + IMAC method)
- checklist.csv: 5 rows updated (no→yes)

## [2026-04-28] create | Batch: 5 DOIs incorporated (asic1a, adenosine-a1-receptor, mce-proteins, a2a-adenosine-receptor update, rps-viridis-reaction-center update)

### New Pages Created
- **asic1a.md** — ASIC1a (Acid-Sensing Ion Channel 1a) from chicken, open state structure with MitTx toxin
  - Trimeric Na⁺-selective ion channel, DEG/ENaC superfamily
  - Resolutions: 2.1 Å (native), 2.3 Å (amiloride-bound), 2.6 Å (Cs⁺-soaked)
  - PDB IDs: 4NTW, 4NTX, 4NTY
  - Key features: Discontinuous TM2 (TM2a/TM2b swap), GAS selectivity filter, ion sites (Cs⁺, amiloride)
  - Expression: Δ13 cASIC1a + MitTx (native snake toxin or recombinant in E. coli Rosetta-gamiB)
  - MitTx recombinant: pET32b, 0.1 mM IPTG, inclusion bodies with 300 mM β-mercaptoethanol solubilization

- **adenosine-a1-receptor.md** — Human A1-AR with covalent antagonist DU172 at 3.2 Å
  - GPCR, class A
  - Construct: M4 muscarinic N-terminus (22 aa) + 3C site + A1-AR + BRIL in ICL3 + N159A + TM6 aa replacement
  - Expression: Sf9 cells, Baculovirus (Best-Bac), pVL1392 vector, 200–400 μg/L yield
  - Purification: DDM + 0.03% CHS → Ni-NTA → anti-Flag M1 → MNG detergent exchange → SEC (Superdex S200)
  - Crystallization: LCP (lipidic cubic phase), 29 crystals merged
  - Key: Covalent DU172 binding, larger binding pocket vs A2A-AR, ECL2 conformation difference

- **mce-proteins.md** — MCE family lipid transport systems (Mla, YebT, PqiB)
  - MlaFEDB complex: IM ABC transporter, DDM solubilization, ~10 Å cryo-EM
  - MlaC: Periplasmic lipid shuttle, mixed α/β fold, deep hydrophobic pocket, sitting drop vapor diffusion (0.1 M citric acid pH 3.5, 1.6 M NH₄H₂PO₄)
  - YebT: 7-ring barrel (~230 Å × 90 Å), Rosetta 2 (DE3) expression
  - PqiB: Tube/syringe architecture with 6-helix coiled coil needle

### Existing Pages Updated
- **rps-viridis-reaction-center.md**: Added DOI 10.1016##j.bbabio.2013.11.015 as source; added Zn-BChl RC reference (2.85 Å, hanging drop, isomorphous with PDB 2J8C)
- **a2a-adenosine-receptor.md**: Added DOI 10.1016##j.bbrc.2023.149393 as source; added A2AAR-Rag31-photoNECA construct details (3.34 Å, PDB 8WDT, SF9 cells, LCP, BL32XU 391 datasets)
- **photoNECA.md**: Already had this DOI as source — no changes needed

### Index & Checklist
- index.md: 130 pages (added asic1a, adenosine-a1-receptor, mce-proteins; removed duplicate bovine-rhodopsin entry; removed "Proteins (New)" section — all merged into main list)
- checklist.csv: 5 rows updated (no→yes):
  - 10.1016##j.bbabio.2013.11.015 → rps-viridis-reaction-center
  - 10.1016##j.bbrc.2023.149393 → a2a-adenosine-receptor
  - 10.1016##j.cell.2014.01.011 → asic1a
  - 10.1016##j.cell.2017.01.042 → adenosine-a1-receptor
  - 10.1016##j.cell.2017.03.019 → mce-proteins

## [2026-04-28] ingest | CB1/CB2 cannabinoid receptor structures (Cell 2020)

Source: 10.1016##j.cell.2020.01.008 — Hua et al., "Activation and Signaling Mechanism Revealed by Cannabinoid Receptor-Gi Complex Structures", Cell 180, 2020

### New Protein Pages Created
- **cb1-receptor.md** — Cannabinoid Receptor CB1 (Class A GPCR, CNS-expressed). Cryo-EM 3.0 Å (6KPG), crystal active-like state. Twin toggle switch activation, cholesterol allosteric modulation, G(i)/(s)/(q) coupling. LMNG/CHS/GDN solubilization, scFv16 stabilization, Superdex 200 SEC. LCP crystallization with monoolein.
- **cb2-receptor.md** — Cannabinoid Receptor CB2 (Class A GPCR, immune/peripheral). Cryo-EM 2.9 Å (6KPF), crystal 3.2 Å (6KPC). Single toggle switch activation, G(i)-selective. BRIL N-terminal fusion, Sf9 baculovirus co-expression (CB2:Gi 1:2:2), TALON IMAC purification. LCP crystallization with monoolein.

### New Reagent Pages Created
- **am12033.md** — CB2-selective synthetic cannabinoid agonist (Ki=0.37 nM). L-shape binding pose in orthosteric pocket.
- **am841.md** — THC-like cannabinoid agonist for CB1 structural studies.
- **hu-308.md** — CB2-selective agonist (~5000x over CB1, Ki=22.7 nM). MD simulation stability in CB2 vs CB1.
- **l-759,656.md** — CB2-selective agonist (406x over CB1, Ki=11.8 nM CB2 vs 4.8 μM CB1).
- **scfv16.md** — scFv16 antibody fragment for GPCR-Gi complex stabilization. Hi5 cell expression, Ni-NTA purification, 3C protease tag cleavage, Superdex 75 SEC.

### Reagent Pages Referenced (existing)
- [[lmng]] — Detergent for CB1/CB2 solubilization
- [[cholesterol-hydrogen-succinate]] — CHS for membrane protein stability
- [[gdn]] — Glycol-diosgenin in cryo-EM buffer
- [[monoolein]] — Lipid matrix for LCP crystallization
- [[imac]] — TALON IMAC resin for purification
- [[size-exclusion-chromatography]] — SEC for complex purification
- [[bril-fusion]] — BRIL N-terminal fusion for CB2 expression
- [[sf9-cells]] — Sf9 insect cells for co-expression
- [[cryoem]] — Cryo-EM structure determination
- [[xray-crystallography]] — X-ray crystallography
- [[lipidic-cubic-phase]] — LCP crystallization method

### Index & Checklist
- index.md: 130 → 137 pages (added cb1-receptor, cb2-receptor, am12033, am841, hu-308, l-759,656, scfv16)
- checklist.csv: 1 row updated (no→yes):
  - 10.1016##j.cell.2020.01.008 → cb1-receptor;cb2-receptor

## [2026-04-28] ingest | SARS-CoV-2 CTD + hACE2 complex structure (Cell 2020)

Source: 10.1016##j.cell.2020.03.045 — Wang et al., "Structural and Functional Basis of SARS-CoV-2 Entry by Using Human ACE2", Cell 181, 2020

### New Protein Pages Created
- **ace2.md** — ACE2 (Angiotensin-Converting Enzyme 2), type II membrane protein, SARS-CoV-2 receptor. 2.5 Å complex structure (6LZG, P41212). Sf9 baculovirus expression (residues 19–615), HisTrap HP + Superdex 200 purification. Sitting-drop vapor diffusion in MES/PEG5000MME/1-propanol. SSRF BL17U data collection.
- **sars-cov-2-s-ctd.md** — SARS-CoV-2 Spike CTD/RBD (residues 319–541), ACE2-binding domain. 2.5 Å with hACE2. Sf9 expression as mFc fusion. 4 disulfide bonds, N343 glycan. Antigenically distinct from SARS-RBD. Key residue mapping for hACE2 interface (Y489, Q493, Q498, N501, etc.).

### New Reagent Pages Created
- **peg-5000.md** — PEG 5000 MME (monomethyl ether), crystallization precipitant. Methyl capping reduces crystallization, smoother phase behavior. 10% w/v used for SARS-CoV-2-CTD/hACE2 crystallization.
- **mes-buffer.md** — MES (2-(N-morpholino)ethanesulfonic acid), pKa ~6.1, pH range 5.5–6.7. 0.1 M pH 6.5 used in SARS-CoV-2-CTD/hACE2 crystallization.

### Reagent Pages Referenced (existing)
- [[peg-6000]] — Related PEG precipitant
- [[glycerol]] — Cryoprotectant (20% in reservoir)
- [[vapor-diffusion]] — Sitting-drop method
- [[xray-crystallography]] — Structure determination
- [[molecular-replacement]] — Phaser MR (PDB: 2AJF)
- [[superdex-columns]] — Superdex 200 SEC
- [[imac]] — HisTrap HP affinity
- [[sf9-cells]] — Sf9 expression
- [[tris-buffer]] — Tris-HCl SEC buffer
- [[sodium-chloride]] — NaCl in SEC buffer

### Index & Checklist
- index.md: 137 → 141 pages (added ace2, sars-cov-2-s-ctd, peg-5000, mes-buffer)
- checklist.csv: 1 row updated (no→yes):
  - 10.1016##j.cell.2020.03.045 → ace2;sars-cov-2-s-ctd

## [2026-04-28] ingest | M1 muscarinic receptor structures with 3 agonists (Cell 2021)

Source: 10.1016##j.cell.2021.11.001 — Brown et al., "From structure to clinic: Design of a muscarinic M1 receptor agonist with the potential to treat Alzheimer's disease", Cell 184, 2021

### New Protein Pages Created
- **m1-muscarinic-receptor.md** — M1 muscarinic acetylcholine receptor (Class A GPCR, Gq-coupled, cognitive function target). 3 structures: 77-LH-28-1 (2.17 Å, 6ZG8), HTL9936 (2.4 Å, 6ZG9), GSK1034702 (2.5 Å, 6ZG9). M1-StaR-T4L construct with 12 thermostabilizing mutations + T4L in ICL3. Sf21 baculovirus expression, DDM solubilization, Ni-NTA + Superdex 200 purification. LCP crystallization. Tyrosine cage disruption mechanism. MD simulations of ligand binding.

### New Reagent Pages Created
- **htl9936.md** — Selective M1 partial agonist (EC50 32 nM M1, >20 μM M2/M3). SBDD-designed with azepine + homopiperidine scaffold. Carbamate and amide groups form water-mediated polar networks. Phase 1 clinical candidate for Alzheimer's disease. CSF/plasma ratio 21%. Reversed scopolamine-induced memory deficits in preclinical models.

### Reagent Pages Referenced (existing)
- [[ddm]] — DDM detergent for M1 solubilization (1.5% w/v)
- [[t4-lysozyme]] — T4L fusion in ICL3 for crystallization
- [[superdex-columns]] — Superdex 200 SEC purification
- [[lipidic-cubic-phase]] — LCP crystallization
- [[molecular-replacement]] — Phaser MR (PDB: 2VT4)
- [[imidazole]] — Imidazole gradient for Ni-NTA elution
- [[microfluidizer]] — Cell disruption at 15,000 psi
- [[baculovirus-expression]] — Sf21 baculovirus expression

### Index & Checklist
- index.md: 141 → 143 pages (added m1-muscarinic-receptor, htl9936)
- checklist.csv: 1 row updated (no→yes):
  - 10.1016##j.cell.2021.11.001 → m1-muscarinic-receptor

## [2026-04-28] ingest | DAP12 TM domain structures in LCP (Cell Reports 2015)

Source: 10.1016##j.celrep.2015.04.045 — Knoblich et al., "Transmembrane Complexes of DAP12 Crystallized in Lipid Membranes Provide Insights into Control of Oligomerization in Immunoreceptor Assembly", Cell Reports 11, 2015

### New Protein Pages Created
- **dap12.md** — DAP12 (DNAX-Activating Protein 12 kDa), immunoreceptor signaling module. Trimer (1.77 Å, PDB: 4WOL) and tetramer (2.14 Å, PDB: 4WO1) TM domain structures in LCP. Polar core of Asp23/Thr27 with K+ (trimer) and Ca2+ (tetramer) coordination. E. coli trpLE fusion, CB digestion, HPLC purification. LCP in monoolein. Glycine zipper motif on exterior. Competitive with receptor assembly in ER.

### New Reagent Pages Created
- **peg-3350.md** — PEG 3350, medium MW PEG crystallization precipitant. 12.4% w/v (trimer), 19.7% w/v (tetramer).
- **bis-tris-propane.md** — Bis-Tris Propane Chloride (BTP), pKa ~7.5. 0.1 M pH 6.07 in tetramer crystallization.
- **potassium-thiocyanate.md** — KSCN, 0.149 M. K+ source for trimer ion coordination.
- **calcium-chloride.md** — CaCl2, 0.269 M. Ca2+ source for tetramer ion coordination.
- **cholesterol.md** — Cholesterol, 10% in trimer crystallization. Stabilizes lipid bilayer in LCP.

### Reagent Pages Referenced (existing)
- [[monoolein]] — LCP lipid matrix
- [[lipidic-cubic-phase]] — LCP crystallization method
- [[molecular-replacement]] — Phaser MR (PDB: 1AFO, Glycophorin A)
- [[peg-5000]] — Related PEG precipitant
- [[peg-6000]] — Related PEG precipitant
- [[peg-400]] — Related PEG precipitant
- [[glycerol]] — Related additive

### Index & Checklist
- index.md: 143 → 148 pages (added dap12, peg-3350, bis-tris-propane, potassium-thiocyanate, calcium-chloride, cholesterol)
- checklist.csv: 1 row updated (no→yes):
  - 10.1016##j.celrep.2015.04.045 → dap12

## [2026-04-28] ingest | SecYEG translocon structures in LCP (Cell Reports 2015)

Source: 10.1016##j.celrep.2015.10.025 — Tanaka et al., "Crystal Structures of SecYEG in Lipidic Cubic Phase Elucidate a Precise Resting and a Peptide-Bound State", Cell Reports 13, 2015

### New Protein Pages Created
- **secyeg-translocon.md** — SecYEG translocon (protein-conducting channel, bacterial homolog of Sec61). Resting state 2.7 Å (5AWW, I222) + peptide-bound state 3.6 Å (5CH4, C222₁). *Thermus thermophilus*. SecG cytoplasmic loop covers pore ring. Lateral gate opening mechanism. DDM solubilization + DM crystallization. LCP in monoolein. Ni-NTA + Superdex 200 + HiTrap SP HP purification.

### New Reagent Pages Created
- **mops-buffer.md** — MOPS (3-(N-morpholino)propanesulfonic acid), pKa ~7.2. 50 mM in SecYEG crystallization.
- **magnesium-sulfate.md** — MgSO4, 100 mM. Crystallization salt for SecYEG.
- **sodium-sulfate.md** — Na2SO4, 100 mM. Salting-out precipitant for SecYEG.

### Reagent Pages Referenced (existing)
- [[ddm]] — DDM detergent for solubilization (2% w/v)
- [[dm]] — DM detergent for crystallization (0.25% w/v)
- [[monoolein]] — LCP lipid matrix (2:3 protein:lipid ratio)
- [[lipidic-cubic-phase]] — LCP crystallization method
- [[superdex-columns]] — Superdex 200 SEC
- [[imac]] — Ni-NTA affinity chromatography
- [[molecular-replacement]] — Phaser MR (PDB: 2ZJS)
- [[peg-5000]] — PEG 500 MME precipitant (30–32%)
- [[amicon-filters]] — Amicon Ultra 50-kDa cutoff filters

### Index & Checklist
- index.md: 148 → 154 pages (added secyeg-translocon, mops-buffer, magnesium-sulfate, sodium-sulfate)
- checklist.csv: 1 row updated (no→yes):
  - 10.1016##j.celrep.2015.10.025 → secyeg-translocon