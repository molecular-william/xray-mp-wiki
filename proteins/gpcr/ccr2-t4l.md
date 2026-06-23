---
title: "CC Chemokine Receptor 2 with T4 Lysozyme Fusion (CCR2-T4L)"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature20605]
verified: false
---

# CC Chemokine Receptor 2 with T4 Lysozyme Fusion (CCR2-T4L)

## Overview

CC chemokine receptor 2 (CCR2) is a class A G protein-coupled receptor expressed on monocytes, immature dendritic cells, and T-cell subpopulations. It mediates cell migration towards CC chemokine ligands such as CCL2 and is implicated in inflammatory and neurodegenerative diseases including atherosclerosis, multiple sclerosis, asthma, neuropathic pain, and diabetic nephropathy. The CCR2-T4L construct is an engineered version of human CCR2 isoform B with T4 lysozyme (T4L) inserted into the third intracellular loop (ICL3), enabling crystal structure determination at 2.8 A resolution. This structure revealed both an orthosteric and a novel intracellular allosteric antagonist binding site.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature20605 | 5T1A | 2.80 | P212121 | Human CCR2 isoform B (Uniprot P41597-2) with C-terminal [Truncation](/xray-mp-wiki/concepts/truncation) (residues 329-360 removed) and T4 lysozyme (T4L) inserted into ICL3. Native CCR2 residues L226(5.62)-R240(6.32) replaced with M2 muscarinic receptor residues (PDB 3UON): S226(5.62)-RASKSRI-T4L-PPPSREK-K240(6.32). N-terminal HA signal sequence, Flag tag, PreScission protease site, and C-terminal 10xHis tag plus Flag tag. Crystallized in ternary complex with orthosteric antagonist BMS-681 and allosteric antagonist CCR2-RA-[R]. | [Bms 681](/xray-mp-wiki/reagents/ligands/bms-681) (orthosteric antagonist), CCR2-RA-[R] (allosteric antagonist) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (Spodoptera frugiperda), baculovirus expression system
- **Construct**: CCR2-T4L coding sequence cloned into modified pFastBac1 vector with HA signal sequence, N-terminal Flag tag, PreScission protease site, and C-terminal 10xHis tag plus Flag tag. High-titre recombinant baculovirus (>10^9 viral particles/mL) obtained using Bac-to-Bac Baculovirus Expression System (Invitrogen). Sf9 cells infected at 2-3 x 10^6 cells/mL with P1 virus at multiplicity of infection of 5. Cells harvested 48 h post-infection, stored at -80 C.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Hypotonic buffer lysis with repeated douncing and centrifugation | -- | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 10 mM MgCl2, 20 mM KCl, EDTA-free protease inhibitor + -- | Membranes washed in hypotonic buffer, then in high osmotic buffer (1.0 M NaCl) to separate soluble from integral membrane proteins |
| Solubilization | Solubilization of membranes with detergent | -- | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 400 mM NaCl + 1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm), 0.2% (w/v) CHS | Solubilized at 4 C for 3 h with 50 uM BMS-681 and 2 mg/mL [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide); clarified by centrifugation at 50,000g for 30 min |
| Affinity chromatography | [TALON](/xray-mp-wiki/reagents/additives/talon) IMAC (Ni-IMAC) | [TALON](/xray-mp-wiki/reagents/additives/talon) IMAC resin (Clontech) | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 400 mM NaCl + -- | Incubated with resin overnight at 4 C; washed without ligands with ten column volumes of Wash I Buffer (50 mM HEPES pH 7.5, 400 mM NaCl, 0.05% DDM, 0.05% CHS); eluted with [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) gradient |


## Crystallization

### doi/10.1038##nature20605

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) (LCP matrix) |
| Protein-to-lipid ratio | not specified |
| Temperature | 4 C |
| Notes | Crystal also contains a Zn2+ ion coordinated by H144(3.56) from CCR2, E238(6.30) from engineered region, and E1005 from T4L, identified by X-ray fluorescence emission analysis |


## Biological / Functional Insights

### Novel intracellular allosteric pocket in CCR2

CCR2-RA-[R] binds in a highly enclosed allosteric pocket more than 30 A away from the orthosteric site, located at the intracellular side caged by helices I-III and VI-VIII. This pocket buries 297.8 A^2 of surface area and is formed by hydrophobic residues (V63^1.53, L67^1.57, L81^2.43, L134^3.46, A241^6.33, V244^6.36, I245^6.37, Y305^7.53, F312^8.50) and polar residues (T77^2.39, R138^3.50, G309^8.47, K311^8.49, Y315^8.53). This site overlaps the G-protein-binding interface in homologous GPCRs, representing the most intracellular allosteric site observed in class A GPCRs to date. The pocket is druggable due to balanced hydrophobic and polar features.

### Bi-directional allosteric communication between orthosteric and allosteric sites

[Bms 681](/xray-mp-wiki/reagents/ligands/bms-681) and CCR2-RA-[R] cooperatively stabilize an inactive conformation of CCR2. BMS-681 occupies the orthosteric pocket and prevents chemokine binding, while CCR2-RA-[R] prevents G-protein coupling at the intracellular allosteric site. This creates bi-directional communication: BMS-681 allosterically inhibits CCL2 binding (which requires active receptor), while CCR2-RA-[R] sterically blocks G-protein binding. The double-antagonist-bound structure shows pronounced inactive-state conformational signatures, including the most inactive GPCR conformation solved to date.

### Inactive-state conformational microswitches

Double-antagonist-bound CCR2 exhibits the full inactive-state conformational signature: intracellular ends of TM3 and TM6 are close together, conserved R138^3.50 (DRY motif) interacts with D137^3.49 and T77^2.39, Y305^7.53 (NPxxY motif) is twisted outward toward TM2, and helix VII is in a repositioned inactive conformation. This contrasts with agonist-bound active states (e.g., US28) where helix VI moves outward and Y7.53 rotates inward. The double-antagonist structure represents the most inactive chemokine receptor conformation solved.


## Cross-References

- [BMS-681](/xray-mp-wiki/reagents/ligands/bms-681/) — Co-crystallized orthosteric antagonist; occupies orthosteric pocket
- [CCR2-RA-[R]](/xray-mp-wiki/reagents/ligands/ccr2-ra-r/) — Co-crystallized allosteric antagonist; binds intracellular allosteric pocket
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — Fusion partner inserted into ICL3 for crystallization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component of LCP crystallization matrix
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane solubilization
- [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Co-detergent used during solubilization and purification
- [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) — Ni-IMAC resin used for His-tag affinity purification
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Primary crystallization method used
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation) — Entity mentioned in overview or biological insights
- [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide) — Entity mentioned in overview or biological insights
