---
title: NupG Nucleoside Proton Symporter from Escherichia coli
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jbc.2021.100479]
verified: false
---

# NupG Nucleoside Proton Symporter from Escherichia coli

## Overview

NupG is a nucleoside proton symporter from Escherichia coli belonging to the nucleoside proton symporter (NHS) family within the Major Facilitator Superfamily (MFS). It mediates the transport of nucleosides across the bacterial inner membrane and was recognized as a prototype MFS transporter. The first crystal structure of an NHS transporter was solved in this work, revealing an inward-open conformation with 12 transmembrane helices and identifying the uridine binding site.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jbc.2021.100479 | not specified | 3.0 A | P21 | Full-length NupG from E. coli K12, wild-type | none (apo state) |
| doi/10.1016##j.jbc.2021.100479 | not specified | 3.0 A | P1 | Full-length NupG from E. coli K12, D323A mutant | none (apo state, nucleoside-containing crystallization conditions but no visible electron density) |

## Expression and Purification

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: Full-length nupG cloned from E. coli K12, subcloned into pET21b

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Cell lysis and membrane fractionation | -- | 25 mM MES pH 6.0, 150 mM NaCl + 2% DDM | Membranes incubated 2 h with 2% DDM at 4 C |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA affinity resin (Qiagen) | 25 mM MES pH 6.0, 150 mM NaCl, 20 mM imidazole (wash), 250 mM imidazole (elution) + 0.02% DDM (wash), 0.4% NG (elution) | Eluted with 250 mM imidazole, 0.4% NG |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 10/300 Increase column (GE Healthcare) | 25 mM MES pH 6.0, 150 mM NaCl, 0.4% NG + 0.4% NG | Peak fractions concentrated to 30 mg/ml for crystallization |


## Crystallization

### doi/10.1016##j.jbc.2021.100479

| Parameter | Value |
|---|---|
| Method | lipidic cubic phase (LCP, in meso) |
| Protein sample | WT NupG at 30 mg/ml, mixed with monoolein at 1:1.5 protein-to-lipid ratio (w/w) |
| Lipid | monoolein (Nu-Chek, M-239) |
| Protein-to-lipid ratio | 1:1.5 |
| Temperature | not specified |
| Growth time | 1 week |
| Notes | P21 crystal form, diffraction to 3.8 A, solved by molecular replacement using predicted structure as search model |

| Parameter | Value |
|---|---|
| Method | lipidic cubic phase (LCP, in meso) |
| Protein sample | WT NupG at 30 mg/ml, mixed with monoolein at 1:1.5 protein-to-lipid ratio (w/w) |
| Lipid | monoolein (Nu-Chek, M-239) |
| Protein-to-lipid ratio | 1:1.5 |
| Temperature | not specified |
| Growth time | 1 week |
| Notes | P1 crystal form, two molecules in asymmetric unit with reversed orientations, RMSD 0.21 A over 387 Ca atoms, molecule A selected for analysis |

| Parameter | Value |
|---|---|
| Method | lipidic cubic phase (LCP, in meso) |
| Protein sample | NupG D323A mutant at 30 mg/ml, mixed with monoolein at 1:1.5 protein-to-lipid ratio (w/w) |
| Lipid | monoolein (Nu-Chek, M-239) |
| Protein-to-lipid ratio | 1:1.5 |
| Temperature | not specified |
| Growth time | 1 week |
| Notes | Solved at 3.0 A resolution, identical conformation to WT (RMSD 0.3 A over 384 Ca atoms), no visible uridine electron density despite nucleoside-containing crystallization conditions |


## Biological / Functional Insights

### Uridine binding site residues

The uridine binding site locates in the central cavity between N and C domains of NupG. It is constituted by R136, T140, F143, Q225, N228, Q261, E264, Y318, and F322. Mutagenesis by ITC showed that N228A and E264A dramatically reduced uridine-binding ability, while Q225A had similar affinity. All other tested mutants (R136A, T140A, F143A, Q261A, Y318A, F322A) abolished binding affinity, indicating these hydrogen-bonded interactions are essential for substrate recognition. F143 and F322 likely form pi-pi interactions with uridine.

### D323A mutation enhances uridine binding

The D323A mutant bound uridine with a Kd of 9.67 +/- 2.87 uM, a 20-fold increase compared to WT NupG (Kd 199.67 +/- 15.01 uM). D323 does not directly contact uridine but is important for substrate binding. The D323A mutant maintained binding affinity across different pH values unlike WT, which decreased at alkaline pH. D323 may be a proton-escaping site during proton-coupling, analogous to E325 in LacY. The D323N mutant showed reduced affinity (Kd 1109 +/- 192.21 uM), mimicking the protonation state.

### Substrate selectivity profile

NupG binds nucleosides with varying affinity: guanosine (Kd 46.67 +/- 6.66 uM) > adenosine (Kd 99.67 +/- 14.57 uM) > cytidine (Kd 143.67 +/- 19.66 uM) > thymidine (Kd 162.5 +/- 19.16 uM) > uridine (Kd 199.67 +/- 15.01 uM). NupG could not bind xanthosine. Binding affinity was approximately 200 uM in sodium citrate at pH 5.0 and MES at pH 6.0, but reduced to approximately 3 mM in 25 mM Tris at pH 8.0.

### Inward-open conformation of NHS transporter

Both WT and D323A NupG structures reveal identical inward-open conformations, consistent with the MFS alternating-access mechanism. The N domain (TM1-6) and C domain (TM7-12) are linked by a flexible loop, with the cavity between domains facing the cytoplasm. Comparison with well-characterized MFS transporters XylE and LacY confirms this inward-open state.

### Comparison with other NHS transporters

Three NHS transporters exist in E. coli: NupG, XapB (58% sequence identity, 76% similarity), and YegT (27% identity, 50% similarity). XapB is a xanthosine-specific transporter. The uridine binding pocket residues are identical between NupG and XapB, but other residues surrounding the pocket contribute to substrate recognition differences. The Q225 and N228 residues of NupG correspond to A226 and Y310 in YegT.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) — NupG belongs to the MFS family, specifically the NHS (nucleoside proton symporter) family
- [POT Family](/xray-mp-wiki/concepts/pot-family/) — Related MFS transporter family with similar 12 TM helix architecture
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Core transport mechanism shared by MFS transporters
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — MFS-specific variant of alternating access mechanism
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — NupG crystallized by LCP method with monoolein
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane solubilization of NupG
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component of LCP crystallization matrix for NupG
- [2-(N-Morpholino)ethanesulfonic Acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Buffer used throughout NupG purification at pH 6.0
