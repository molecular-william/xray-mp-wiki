---
title: CC Chemokine Receptor 2A (CCR2A)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2018.10.027]
verified: false
---

# CC Chemokine Receptor 2A (CCR2A)

## Overview

CC chemokine receptor 2A (CCR2A) is a class A G protein-coupled receptor and the major isoform of CCR2 expressed by mononuclear cells and vascular smooth muscle cells. CCR2 is a widely studied chemokine receptor involved in inflammatory diseases. CCR2A serves as the primary binding target for the chemokine CCL2 (monocyte chemoattractant protein-1) and is implicated in atherosclerosis, rheumatoid arthritis, and multiple sclerosis. Two crystal structures of CCR2A in complex with the orthosteric antagonist MK-0812 were solved, providing structural insights into antagonist binding and selectivity over CCR5.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2018.10.027 | 6GPS | 3.30 | P21 | Full-length CCR2A with rubredoxin fusion in ICL3 (residues L226-R240 replaced) and five point mutations: N14Q, C70Y(1.60), G175N(4.60), A241D(6.33), K311E(8.49). C-terminal His6/FLAG tag. Truncated at C-terminus residue R313(8.51). | MK-0812 (orthosteric antagonist) |
| doi/10.1016##j.str.2018.10.027 | 6GPX | 2.70 | P21 | N- and C-terminally truncated CCR2A. Removed 28 N-terminal residues and 53 C-terminal residues. Rubredoxin fusion in ICL3. Reverted K311E mutation back to WT K311. C-terminal end resolved up to residue G321. Chain A selected for highest quality data. | MK-0812 (orthosteric antagonist) |

## Expression and Purification

- **Expression system**: High Five insect cells (BTI-TN-5B1-4, Trichoplusia ni ovarian cells), baculovirus expression system
- **Construct**: Full-length and truncated CCR2A constructs with rubredoxin fusion in ICL3, point mutations for stabilization (N14Q, C70Y, G175N, A241D, K311E), C-terminal His6/FLAG tag. High Five cells infected at 10^6 cells/mL, grown in Wave cultivation bags up to 8.5 L.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Thawing in hypotonic buffer (10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl), N2 disruption bomb at 50 bar | -- | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 0.5 mg/mL DNase, EDTA-free protease inhibitor cocktail + -- | Membranes washed, supplemented with 30% glycerol and 2 mg/mL iodoacetamide, incubated 1 h at 4 C |
| Solubilization | Solubilization of membranes with detergent | -- | Membrane preparation buffer + 1.0% DDM, 0.1% CHS | Solubilized for at least 2 hours at 4 C; clarified by centrifugation at 100,000 x g for 1 h |
| Affinity chromatography | TALON Superflow Metal Affinity Resin (Ni-IMAC) | TALON Superflow | 25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol, 0.05% DDM, 0.05% CHS, 30 mM imidazole (wash); 200 mM imidazole (elution) + 0.05% DDM, 0.05% CHS | 6 eluates of 10 min each; 1 mL resin per 1 L culture. Elution buffer: 25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol, 0.05% DDM, 0.005% CHS, 200 mM imidazole, 10 mM MgCl2 |
| Tag cleavage | PreScission protease treatment overnight at 4 C | -- | Buffer without imidazole (post PD-10 desalting) + -- | 10 U/mg protein; removed C-terminal FLAG and His tags |
| Size exclusion chromatography | HiLoad Superdex 200 pg 200 column | Superdex 200 pg 200 | 25 mM HEPES pH 7.5, 150 mM NaCl, 0.05% DDM, 0.005% CHS, 1 uM MK-0812 + 0.05% DDM, 0.005% CHS | Concentrated to 40-50 mg/mL using 30 kDa MWCO concentrator; yields varied 0.5-2 mg/L depending on construct |


## Crystallization

### doi/10.1016##j.str.2018.10.027

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP), conventional glass sandwich plates |
| Temperature | 20 C |

| Parameter | Value |
|---|---|
| Method | LCP crystallization with IMISX in-situ plates |
| Temperature | not specified |


## Biological / Functional Insights

### E291(7.39) is a key residue for orthosteric antagonist binding

The side chain of E291(7.39) forms a charge-reinforced hydrogen bond (2.5 A) with the secondary amine of MK-0812 in the orthosteric pocket. This interaction is absent with BMS-681, where the tertiary amine cannot form this bond. E291(7.39) is present in most chemokine receptors and mutation studies have shown it is important for small-molecule ligand binding to CXCR4, CCR5, CCR2, and US28. Previous mutations of E291(7.39) to alanine in CCR2 reduced binding affinities for INCB3344, SB-282241, TAK-779, and Teijin antagonists. This residue is a key determinant for high-affinity orthosteric antagonist binding in chemokine receptors.

### H121(3.33) confers CCR2 selectivity over CCR5

The non-conserved residue H121(3.33) is located in the orthosteric pocket and shows divergent sequences between CCR2 and CCR5. Structural modeling of pyrimidine amide (PA) class antagonists revealed that these ligands interact with H121(3.33), providing a basis for CCR2 selectivity over CCR5. Mutation of H121(3.33) affected the CCR2-selective Teijin ligand but not the dual antagonist TAK-779, indicating that interaction with H121(3.33) can be exploited for designing selective CCR2 antagonists.

### Stabilization by combined mutations and rubredoxin fusion

Full-length CCR2A was stabilized by a combination of rubredoxin fusion in ICL3 and five point mutations (N14Q, C70Y, G175N, A241D, K311E), achieving a melting temperature (Tm) of 55.6 C by DSF. Rubredoxin fusion alone gave Tm 43.7 C, and mutations alone gave Tm 51.0 C, showing synergistic stabilization. MK-0812 binding further increased Tm to 68.1 C, a 12.5 C shift. Multiple antagonists were tested by DSF, with MK-0812 giving the highest thermal shift (68.1 C), followed by AZD-6942 (63.2 C), INCB3344 (62.2 C), INCB3284 (60.4 C), and cpd 8c (58.2 C).

### Inactive conformation confirmed

Both CCR2A structures adopt the inactive chemokine receptor signature: intracellular ends of TM3 and TM6 are close together, and the conserved R138(3.50) of the DRY motif interacts with D137(3.49) and T77(2.39), disrupting the G-protein binding site. Y305(7.53) on TM7 is twisted outward and points toward TM2, identical to the inactive CCR2B structure. This conformation is consistent with antagonist-bound states.


## Cross-References

- [MK-0812](/xray-mp-wiki/reagents/ligands/mk-0812/) — Co-crystallized orthosteric antagonist; highest thermal stabilization (Tm 68.1 C)
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component of LCP crystallization matrix
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Co-component of LCP matrix (10:1 monoolein:cholesterol)
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane solubilization and purification
- [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Co-detergent used during solubilization and purification
- [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) — Ni-IMAC resin used for affinity purification of His-tagged CCR2A
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Size exclusion chromatography resin for final purification step
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Primary crystallization method used for both CCR2A structures
