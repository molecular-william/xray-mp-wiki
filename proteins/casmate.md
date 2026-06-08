---
title: CasMATE (Camelina sativa MATE Transporter)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.07.009]
verified: false
---

# CasMATE (Camelina sativa MATE Transporter)

## Overview

CasMATE is a multidrug and toxic compound extrusion (MATE) family transporter from the plant Camelina sativa (false flax). It represents the first crystal structure of a eukaryotic MATE protein, providing structural insight into the architecture and substrate recognition mechanism of plant MATE transporters. CasMATE consists of 12 transmembrane helices assembled pseudo-symmetrically into an outward-facing V-shaped conformation with a negatively charged internal pocket for ligand binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2017.07.009 | 5XJJ | 2.9 A | P212121 | CasMATE residues 15-468 (N-terminal 1-14 and C-terminal 469-475 deleted), C-terminal GFP-His8 tag (TEV-cleaved) | None (apo form) |

## Expression and Purification

- **Expression system**: Pichia pastoris yeast strain SMD1168
- **Construct**: C-terminal GFP-His8 tag fusion, NCBI Reference sequence XP_010514235, linearized pPIC9K vector transformed by electroporation, induced with methanol in BMMY medium at 20 C for 72 h

### Purification Workflow

- **Expression system**: Pichia pastoris strain SMD1168
- **Expression construct**: CasMATE(15-468)-EFPGENLYFQGQFSKGE-GFP-His8
- **Tag info**: C-terminal GFP-His8 tag, cleaved with TEV protease at 4 C overnight

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and induction | Fermentation in Pichia pastoris | -- | BMGY medium for growth; BMMY medium for induction | Transformants selected with G418; cultivated in 10 mL BMGY at 30 C for 24 h, then induced in 1 L BMMY at 20 C for 72 h |
| Cell disruption and membrane fractionation | Microfluidizer cell lysis and ultracentrifugation | -- | 300 mM sodium-chloride, 20 mM HEPES-Na pH 8.0, 10% glycerol, 1 mM PMSF, 5 mM beta-ME | Cells disrupted by M-110EH Microfluidizer 5 times at 22,000 p.s.i.; supernatant ultracentrifuged at 40,000 rpm (Beckman 45 Ti rotor) for 2 h |
| Solubilization | Detergent solubilization of membrane fraction | -- | 300 mM sodium-chloride, 20 mM HEPES-Na pH 8.0, 10% glycerol + 2% DDM (Glycon), 2 h incubation at 4 C | Pellet resuspended in buffer with 2% DDM; centrifuged at 130,000 x g at 4 C for 30 min; supernatant collected |
| Affinity chromatography | TALON cobalt affinity chromatography | TALON cobalt affinity resin (Clontech) | 300 mM sodium-chloride, 20 mM HEPES-Na pH 7.0, 10% glycerol + 0.03% LMNG (Anatrace), 0.003% CHS (Anatrace), 20 mM imidazole | Washed with LMNG/CHS buffer containing 20 mM imidazole; eluted with 200 mM imidazole |
| Tag cleavage | TEV protease cleavage | TALON cobalt affinity resin (Clontech) | 300 mM sodium-chloride, 20 mM HEPES-Na pH 7.0, 10% glycerol + 0.03% LMNG, 0.003% CHS | GFP-His8 tag cleaved with TEV protease at 4 C overnight; flow-through collected (tag-free protein) |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 Increase 10/30 GL (GE Healthcare) | 300 mM sodium-chloride, 20 mM HEPES-Na pH 7.0, 1% glycerol, 0.03% LMNG, 0.003% CHS | Major peak pooled and concentrated to 25 mg/mL |


## Crystallization

### doi/10.1016##j.str.2017.07.009

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified CasMATE(15-468) at 25 mg/mL in 300 mM sodium-chloride, 20 mM HEPES-Na pH 7.0, 1% glycerol, 0.03% LMNG, 0.003% CHS; mixed with liquefied monoolein using twin-syringe mixing method |
| Lipid | monoolein (NU-CHEK-PREP) |
| Protein-to-lipid ratio | 2:3 (w/w) |
| Temperature | 20 C |
| Notes | Crystals grown in reservoir solutions: (1) 30% PEG400, 100 mM sodium-chloride, 100 mM lithium-sulfate, 100 mM HEPES-Na pH 7.5; (2) 30% PEG400, 100 mM ADA pH 6.5, 300 mM lithium-sulfate; (3) 30% PEG300, 200 mM ammonium-sulfate, 100 mM HEPES-Na pH 7.5 |


## Biological / Functional Insights

### Negatively charged internal pocket for cation binding

The internal pocket of CasMATE provides a negatively charged surface for ligand
binding. Key residues include E270, N74, E296, D383, E265, Q160, Q443, N406,
N390, R168, R394, and E89. The pocket size is approximately 13 x 22 x 22 A
(length x width x depth), sufficient for binding of metal ions such as cadmium
and organic cations like berberine (molecular weight 336). The position of amino
acid clusters is similar to the metal ion binding site of Vc-NorM. Water molecules
bind to residues E265, F269, E296, Y300, S379, D383, Y410, and V436, with E265
and D383 being conserved.

### V-shaped architecture with pseudo-symmetry

CasMATE consists of 12 transmembrane helices (TM 1-12), with the N-terminal
TM 1-6 (N lobe) and C-terminal TM 7-12 (C lobe) assembled pseudo-symmetrically.
The overall structure shows a V-shaped architecture formed by N-lobe and C-lobe
bundles. The extracellular and intracellular sides are open and closed, respectively,
in a manner similar to the outward-facing form of bacterial MATE proteins. TM 1,
2, and 4 of the N lobe and TM 7, 8, and 10 of the C lobe form the central pocket.

### NorM-like cation-binding site in eukaryotic MATE

Phylogenetic analysis shows CasMATE is classified into group B of plant MATE
proteins and is more closely related to prokaryotic group D (NorM-like) than
group E (DinF-like). Residue E261 (equivalent to Ng-NorM E270) is important
for cation binding and is conserved in groups A-D. Residues D41 and D184,
important for cation binding in Pf-DinF, are highly conserved in groups E and
F. The amino acid sequence of CasMATE is more closely related to prokaryote
group D, suggesting CasMATE possesses a NorM-like cation-binding site.


## Cross-References

- [NtMATE2 (Nicotiana tabacum MATE2)](/xray-mp-wiki/proteins/ntmate2/) — Another eukaryotic MATE transporter from tobacco; NtMATE2 was crystallized using CasMATE (PDB 5XJJ) as the molecular replacement search model
- [Major Facilitator Superfamily](/xray-mp-wiki/concepts/mfs-transporter/) — MATE transporters are secondary transporters related to MFS family in structural and mechanistic features
- [Rocker-Switch Mechanism in MFS Transporters](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — MATE transporters operate via the rocker-switch alternating-access mechanism
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — 2% DDM used for initial membrane solubilization of CasMATE
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — 0.03% LMNG used throughout purification for protein stabilization
- [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — 0.003% CHS used during purification and LCP crystallization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Monoolein used as the lipidic cubic phase matrix for LCP crystallization at 2:3 protein-to-lipid ratio
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to grow CasMATE crystals
