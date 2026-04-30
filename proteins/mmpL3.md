---
title: MmpL3
created: 2026-04-27
updated: 2026-04-30
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, pump]
sources: [doi/10.1073##pnas.1901346116, doi/10.1016##j.cell.2019.01.003, doi/10.1016##j.jmb.2020.05.019]
---

# MmpL3 (Mycobacterial Membrane Protein Large 3)

## Overview

MmpL3 is an essential membrane protein transporter in *Mycobacterium tuberculosis* and *M. smegmatis* required for cell-wall biogenesis. It transports trehalose monomycolates (TMMs), precursors of mycolic acids, across the inner membrane. MmpL3 is a validated drug target for anti-tuberculosis therapy.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| Su et al. (PNAS 2019) | 6Q74 | 2.59 Å | P2₁ | MmpL3₇₇₃ (residues 1–773, C-terminal truncation) | Phosphatidylethanolamine (PE) |
| Zhang et al. (Cell 2019) | 6N6R | 2.59 Å | P2₁2₁2₁ | MmpL3₁₋₇₄₈aa-T4 (C-terminal domain substituted by [t4-lysozyme](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)) | 6-DDTre (substrate mimic) |
| Yang et al. (JMB 2020) | 7C2M | 3.1 Å | P2₁2₁2₁ | MmpL3₁₋₇₄₈aa-T4 | NITD-349 (indole-2-carboxamide, Kd = 0.05 μM) |
| Yang et al. (JMB 2020) | 7C2N | 2.8 Å | P2₁2₁2₁ | MmpL3₁₋₇₄₈aa-T4 | SPIRO (spiropiperidine, Kd = 0.8 μM) |

## Expression and Purification

- **Expression system**: *E. coli* BL21(DE3)Δ*acrB* (Su et al.); *M. smegmatis* mc²155 (Zhang et al., Yang et al.)
- **Construct**: MmpL3₇₇₃ (residues 1–773, C-terminal proline-rich region 733–1013 proteolytically clipped); MmpL3₁₋₇₄₈aa-T4 (C-terminal domain substituted by [t4-lysozyme](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), 10×His or 6×His tag)

### Purification Workflow

#### Su et al. (PNAS 2019)

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Solubilization | Detergent | — | 1% [ddm](/xray-mp-wiki/reagents/detergents/ddm/) | — |
| 2. Affinity | Ni²⁺ IMAC | Ni²⁺ resin | — | 6×His-tag, elution with imidazole |
| 3. SEC | Size-exclusion | Superdex | 20 mM [hepes-buffer](/xray-mp-wiki/reagents/buffers/hepes-buffer/) pH 7.5, 150 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 0.05% [ddm](/xray-mp-wiki/reagents/detergents/ddm/) | — |

**Final sample**: MmpL3₇₇₃ in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% DDM

#### Zhang et al. (Cell 2019) / Yang et al. (JMB 2020)

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Cell lysis | French Press | — | 20 mM [tris-buffer](/xray-mp-wiki/reagents/buffers/tris-buffer/)-HCl pH 8.0, 150 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) | 1,200 bars |
| 2. Solubilization | Detergent | — | 1% [ddm](/xray-mp-wiki/reagents/detergents/ddm/) (Anatrace) | — |
| 3. Affinity | IMAC | Agarose (GE Healthcare) | Wash: 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% DDM, 50 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) | Elution: 300 mM imidazole |
| 4. SEC | Size-exclusion | [superdex-columns](/xray-mp-wiki/methods/purification/superdex-columns/)-6 increase 10/300 GL | 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 10% glycerol, 0.05% DDM, 6-DDTre | Substrate mimic added |
| 5. Concentration | Spin filter | [amicon-filters](/xray-mp-wiki/methods/purification/amicon-filters/) (100 kDa cut-off) | Same as step 4 | 15 mg/mL |

**Final sample**: 15 mg/mL in 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 10% glycerol, 0.05% DDM, 6-DDTre

## Crystallization

### Su et al. (PNAS 2019)

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 20 mg/mL MmpL3₇₇₃ in 20 mM HEPES pH 7.5, 0.05% DDM |
| Reservoir | 25% [peg-400](/xray-mp-wiki/reagents/additives/peg-400/), 0.1 M [sodium-acetate](/xray-mp-wiki/reagents/additives/sodium-acetate/) pH 5.4, 0.05 M magnesium acetate |
| Temperature | 25 °C |
| Cryoprotection | Raised [peg-400](/xray-mp-wiki/reagents/additives/peg-400/) to 30% |

### Yang et al. (JMB 2020)

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 6–8 mg/mL MmpL3-T4L + 0.5 mM ligand (NITD-349 or SPIRO), incubated 30 min at 4 °C |
| Reservoir | 10–20% PEGMME 350, 50 mM ADA pH 6.0–7.0, 7.5–17.5% [peg-2000](/xray-mp-wiki/reagents/additives/peg-2000/) |
| Temperature | 16 °C |
| Cryoprotection | 25% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |

## Biological / Functional Insights

### Architecture

- 12 transmembrane helices (TMs 1–12) with two periplasmic loops (loops 1 and 2)
- Periplasmic domains: PD1 (4 α-helices + 3 β-strands) and PD2 (3 α-helices + 3 β-strands)
- PD2 subdomains: PN and PC, both adopt β-α-β-α-β fold
- Three openings: G_T (funnel at top), G_F (opening in front), G_B (opening at back)
- Oligomerization: Monomeric in detergent solution (confirmed by native MS)

### Substrate Binding

- **Trehalose monomycolate (TMM)**: Native MS Kd = 3.7 ± 1.3 μM for first TMM binding; prefers short-chain TMM lipids (~1,428 Da); does NOT bind TDM (trehalose dimycolate)
- **Phosphatidylethanolamine (PE)**: Native MS Kd = 19.5 ± 6.3 μM for first PE binding; second PE molecule binds at ≥20 μM
- **Other lipids**: Native MS shows binding to PG (phosphatidylglycerol), PI (phosphatidylinositol), DAG (diacylglycerol), [cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/)

### Proton-Relay Network

MmpL3 is a proton-motive-force–dependent transporter that functions via an antiport mechanism:

- Key residues: D256–Y646, Y257–D645, S293–D645, E647–K591
- Conserved residues form a hydrogen-bonded network for proton transfer
- Proton import into cytoplasm is coupled to substrate export toward periplasm

### Drug Targets and Inhibitors

All inhibitors bind deep in the central transmembrane channel, disrupting the proton-relay network:

- **SQ109** (diamine, Kd = 1.65 μM): Extended conformation; geranyl tail in hydrophobic subsite; adamantine group held by "V"-shaped Phe260-Phe649; pocket volume ~282 Å³
- **AU1235** (adamantyl urea, Kd = 0.29 μM): Similar binding position to SQ109
- **ICA38** (indolcarboxamide): Bulky indole group in hydrophobic subsite; amide H-bonds to Asp645; carbonyl H-bonds to Tyr646
- **Rimonabant** (CB1 antagonist, Kd = 29 μM): Three "arms" — 2,4-dichlorophenyl, 4-chlorophenyl, pi-peridinyl-1-carbamoyl; pyrazole core inserts at TMH bundle center; pocket volume ~305 Å³
- **NITD-349** (indole-2-carboxamide, Kd = 0.05 μM): Indole group in hydrophobic subsite; amide N and indole N H-bond to Asp645; amide O H-bond to Asp256
- **SPIRO** (spiropiperidine, Kd = 0.8 μM): Benzodioxane in hydrophobic subsite; 4-oxygen H-bonds to Leu642 main chain; thiophene π-π stacks with Tyr257 and Phe649; piperidine N H-bonds to Asp645; pocket volume ~214 Å³

### Resistance Mutations

- **NITD-349 resistance**: L194R, G258E, S293T, T316I, S596I, V688G, V689G
- **SPIRO resistance**: Y257C, F260V/L, I297S/T, S596I
- Aromatic residues Tyr257 and Phe260: critical for inhibitor binding

## Cross-References

- [sotb](/xray-mp-wiki/proteins/sotb/) — E. coli antiporter (MFS family)
- [nTMATE2-transporter](/xray-mp-wiki/proteins/nTMATE2-transporter/) — Tobacco MATE family transporter
- [sq109](/xray-mp-wiki/reagents/ligands/sq109/) — Anti-TB diamine drug; MmpL3 inhibitor in clinical trials
- [rimonabant](/xray-mp-wiki/reagents/ligands/rimonabant/) — CB1 antagonist repurposed as MmpL3 inhibitor
- [ica38](/xray-mp-wiki/reagents/ligands/ica38/) — Indolcarboxamide MmpL3 inhibitor
- [au1235](/xray-mp-wiki/reagents/ligands/au1235/) — Adamantyl urea MmpL3 inhibitor
- [cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) — Lipid that binds to MmpL3
- [bril](/xray-mp-wiki/reagents/protein-tags/bril/) — BRIL fusion used for thermostabilization of GPCRs