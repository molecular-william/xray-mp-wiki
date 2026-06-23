---
title: Mouse 5-HT3A Receptor
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13552]
verified: false
---

# Mouse 5-HT3A Receptor

## Overview

The mouse [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) 5-HT3A receptor is a pentameric ligand-gated ion channel (pLGIC) belonging to the Cys-loop receptor superfamily. It mediates fast excitatory neurotransmission in the central and peripheral nervous systems. This page covers the first high-resolution X-ray crystal structure of a mammalian Cys-loop receptor, solved at 3.5 Å resolution in complex with the [VHH15 Nanobody](/xray-mp-wiki/reagents/antibodies/vhh15/). The structure reveals the complete architecture including part of the intracellular domain, providing key insights into ion permeation, neurotransmitter binding, and the gating mechanism of serotonin-gated channels.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13552 | 4HHZ | 3.5 | P2₁2₁2₁ | residues 9-275, 280-334, 399-459 with N-terminal Strept-tag (trypsin-split construct) | [VHH15 Nanobody](/xray-mp-wiki/reagents/antibodies/vhh15/) |

## Expression and Purification

- **Expression system**: T-REX-293 (human embryonic kidney 293 derivative)
- **Construct**: N-terminal Strept-tag with TEV cleavage site, mouse 5-HT3A subunit

### Purification Workflow

- **Expression system**: T-REX-293
- **Expression construct**: N-terminal Strept-tag with TEV cleavage site

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Suspension culture | — |  | Serum-free, orbital agitation, 4 L culture volume |
| Protein induction | Chemical induction | — |  | 4 µg/mL tetracycline and 4 mM [Sodium Butyrate](/xray-mp-wiki/reagents/additives/sodium-butyrate/) at 4×10^6 cells/mL |
| Membrane isolation | Centrifuration | — |  | Ultra-Turrax T25 disruption, 100,000g for 45 min |
| Solubilization | Detergent solubilization | -- | 50 mM Tris pH 7.4, 500 mM NaCl + 1% [C12E9](/xray-mp-wiki/reagents/detergents/c12e9/) | 2 h solubilization |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Streptactin affinity | Streptactin Superflow (IBA) | 50 mM Tris pH 7.4, 125 mM NaCl, 0.02% [C12E9](/xray-mp-wiki/reagents/detergents/c12e9/) | Wash with buffer A, elute with 5 mM D-[Desthiobiotin](/xray-mp-wiki/reagents/ligands/desthiobiotin/) |
| Deglycosylation | Enzymatic treatment | — |  | PNGase F, 5 units/µg, 2 h at 37°C |
| [Limited Proteolysis](/xray-mp-wiki/methods/purification/limited-proteolysis/) | [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) digestion | — |  | 1 µg [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) per 80 µg receptor, 2 h at 30°C |
| Size-exclusion chromatography | SEC | Superose 6 column (GE Healthcare) | 50 mM Tris pH 7.4, 125 mM NaCl, 0.02% [C12E9](/xray-mp-wiki/reagents/detergents/c12e9/) | Pentameric receptor-detergent complex pooled |

**Final sample**: ~4 mg/mL in 50 mM Tris pH 7.4, 125 mM NaCl, 0.02% [C12E9](/xray-mp-wiki/reagents/detergents/c12e9/)


## Crystallization

### doi/10.1038##nature13552

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 5-HT3 receptor-[VHH15 Nanobody](/xray-mp-wiki/reagents/antibodies/vhh15/) complex (~4 mg/mL) with 0.56 mM [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) |
| Reservoir | 20-25% [PEG](/xray-mp-wiki/reagents/additives/peg/) 10000, 0.1 M Na2SO4, 0.1 M Tris pH 8.5 |
| Mixing ratio | 1:1 |
| Temperature | 12 |
| Growth time | 2-5 days |
| Cryoprotection | 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) or 40% [PEG](/xray-mp-wiki/reagents/additives/peg/) 10000 in mother solution |
| Notes | Recombination in SUVs with [POPC](/xray-mp-wiki/reagents/lipids/popc/):[POPG](/xray-mp-wiki/reagents/lipids/popg/):[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) (8.75:1:2.5) before complex formation with [VHH15 Nanobody](/xray-mp-wiki/reagents/antibodies/vhh15/) |


## Biological / Functional Insights

### Ion Permeation Pathway

The structure reveals a 60-Å high and 20-Å wide extracellular vestibule with a constriction at residues D105 and K108 of loop β4-β5. The M2 helices line the ~40-Å-long transmembrane pore, with hydrophobic residues at positions 16', 13', and 9' defining a funnel. A 4.6-Å hydrophobic constriction is located at L9' (L260). Below the constriction, the vestibule exhibits an electronegative surface that increases local cation concentration.

### Intracellular Domain Architecture

The intracellular domain comprises post-M3 loops, MX helices, and MA helices forming a tight bundle. The MA helices create a closed vestibule where lateral portals are obstructed by the post-M3 loops, leaving only a narrow tunnel (3.3 Å at thinnest). A tight hydrophobic juncture at the bottom of the MA helices (L402, L406, I409, L413) creates a 17-Å-long zone with minimum diameter of 4.2 Å. This structure does not offer an exit pathway for ions, suggesting conformational changes are required for ion exit during gating.

### Conductance-Defining Arginine Triplet

Three arginine residues (R416, R420, R424) in helix MA of the A subunit are responsible for the low conductance of homomeric 5-HT3A receptors (0.4 pS vs. 16 pS for heteromeric AB receptors). R416 faces the pore lumen; R420 is within salt-bridge distance to D312; R424 is exterior to the post-M3 loop. These arginines are surrounded by negatively charged residues (E414, D417, E418, E421, D425) creating a ladder of negative charges along the outer face of the MA helix.

### Neurotransmitter Binding Site

Each of the five equivalent [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) binding sites is located between two subunits in an electronegative cleft. Loops A, B, and C from the principal subunit and portions of β-strands D, E, G and loop F from the complementary subunit contribute to the site. The binding site is capped by the [VHH15 Nanobody](/xray-mp-wiki/reagents/antibodies/vhh15/), which binds at the subunit interfaces with sub-nanomolar affinity. Loop C adopts an extended conformation, intermediate between the contracted (agonist-bound) and open (antagonist-bound) states.

### Interface and Quaternary Structure

The pre-M1 loop arginine R218 is surrounded by negatively charged residues E53 (β1-β2 loop), D145 (Cys-loop), and E186 (β8-β9 loop), forming a charged sandwich with the conserved aromatic residue W187. This arrangement is conserved among Cys-loop receptors and may indicate the channel state. The Cys-loop penetrates into the four-helix bundle of the transmembrane domain. The M1 helix is broken at conserved proline P230, providing flexibility to the extracellular domain orientation relative to the transmembrane domain.


## Cross-References

- [ELIC](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Bacterial pLGIC homolog used as search model for molecular replacement; structure comparison shows 5-HT3A is intermediate between open and closed states
- [GLIC](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Prokaryotic pLGIC homolog; M2 helix bundle in 5-HT3A resembles open GLIC conformation
- [GluCl](/xray-mp-wiki/proteins/cys-loop-receptors/glucl/) — C. elegans pLGIC homolog; used in structural superposition to trace closed-to-open conformational trajectory
- [Acetylcholine-Binding Protein (AChBP)](/xray-mp-wiki/proteins/cys-loop-receptors/acetylcholine-binding-protein/) — Soluble surrogate for Cys-loop receptor extracellular domains; used to explore binding site anatomy
- [Cys-Loop Receptor Family](/xray-mp-wiki/concepts/cys-loop-receptor-family/) — 5-HT3A belongs to the Cys-loop receptor superfamily of pentameric ligand-gated ion channels
- [VHH15 Nanobody](/xray-mp-wiki/reagents/antibodies/vhh15/) — Llama-derived nanobody used as crystallization chaperone; binds with sub-nanomolar affinity to stabilize non-conducting state
- [C12E9 (Nonyl Glucoside)](/xray-mp-wiki/reagents/detergents/c12e9/) — Nonionic detergent used for solubilization of membrane fractions containing the 5-HT3A receptor
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Limited Proteolysis](/xray-mp-wiki/methods/purification/limited-proteolysis/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
