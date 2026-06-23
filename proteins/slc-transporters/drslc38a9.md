---
title: Zebrafish SLC38A9 (drSLC38A9)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2020.11.014, doi/10.1038##s41594-018-0072-2]
verified: false
---

# Zebrafish SLC38A9 (drSLC38A9)

## Overview

Zebrafish SLC38A9 (drSLC38A9) is a lysosomal amino acid transporter from Danio rerio that functions as a sensor for luminal arginine and an activator of mTORC1 signaling. drSLC38A9 belongs to the SLC38 family of amino acid transporters and adopts a characteristic [LEUT](/xray-mp-wiki/proteins/leut)-like pseudo-symmetry fold with five transmembrane-helix inverted topology repeats. Two crystal structures have been determined: an arginine-bound cytosol-open state at 2.8 A (PDB 6C08) and an N-plug inserted cytosol-closed state at 3.4 A (PDB 7KGV). The arginine-bound structure revealed the transporter in a cytosol-open conformation with the N-terminal domain released from the binding pocket, allowing substrate transport. The protein exhibits a unique N-plug mechanism in which its N-terminal domain inserts into the substrate-binding pocket in the absence of arginine, blocking transport. Upon arginine binding, the N-plug is released, allowing both arginine transport and interaction with the Rag GTPase complex to activate mTORC1. This ball-and-chain mechanism provides a direct link between lysosomal amino acid availability and cellular growth signaling.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2020.11.014 | 7KGV | 3.40 | P 1 21 1 | drSLC38A9 residues 71-549 with N-terminal octa-his tag, complexed with Fab fragment | none |
| doi/10.1038##s41594-018-0072-2 | 6C08 | 2.80 | P 1 21 1 | drSLC38A9 residues 71-549 with N-terminal deletion (Delta-N), complexed with Fab fragment | arginine |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf-9 insect cells
- **Construct**: drSLC38A9 residues 71-549 from NP_001073468.1 with N-terminal octa-his tag and thrombin cleavage site

### Purification Workflow

- **Expression system**: Spodoptera frugiperda Sf-9 insect cells

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Bac-to-Bac Baculovirus Expression System | — | — | Sf-9 cells infected, harvested at 60 hours post-infection |
| Cell lysis | Homogenization in low salt buffer | — | 20 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 150 mM NaCl, cOmplete Protease Inhibitor Cocktail | Homogenized and ultra-centrifuged at 130,000 x g for 1 hour |
| Membrane fractionation | Ultra-centrifugation and high salt wash | — | 1.0 M NaCl, 20 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0 | Pellet washed and resuspended in low salt buffer, frozen in liquid nitrogen at -80 C |
| Solubilization | Detergent extraction at 4 C for 4 hours | — | 20 mM Tris pH 8.0, 500 mM NaCl, 5% [GLYCEROL](/xray-mp-wiki/reagents/additives/glycerol), 2% DDM, 0.2% CHS | Ultra-centrifuged at 130,000 x g for 1 hour after solubilization |
| Affinity capture | [TALON](/xray-mp-wiki/reagents/additives/talon) Metal Affinity Resin incubation at 4 C overnight | [TALON](/xray-mp-wiki/reagents/additives/talon) Metal Affinity Resin (Clontech) | 20 mM Tris pH 8.0, 500 mM NaCl, 5% [GLYCEROL](/xray-mp-wiki/reagents/additives/glycerol), 2% DDM, 0.2% CHS | Incubated overnight at 4 C |
| Wash | Column wash | [TALON](/xray-mp-wiki/reagents/additives/talon) Metal Affinity Resin (Clontech) | 50 mM [IMIDAZOLE](/xray-mp-wiki/reagents/additives/imidazole), 20 mM Tris pH 8.0, 500 mM NaCl, 0.1% DDM | 5 column volumes wash |
| Tag removal | In-column thrombin digestion | [TALON](/xray-mp-wiki/reagents/additives/talon) Metal Affinity Resin (Clontech) | 20 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 500 mM NaCl, 0.4% DM, 0.02% DDM | Thrombin at enzyme:protein molar ratio of 1:1000, overnight at 4 C. Cleaved protein in flow-through. |
| Size exclusion chromatography | SEC | Superdex 200 Increase 10/300 GL (GE Healthcare) | 20 mM [TRIS-HCL](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl, 0.2% DM | Peak fractions pooled and concentrated to 5 mg/mL for crystallization |


## Crystallization

### doi/10.1016##j.str.2020.11.014

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | drSLC38A9-Fab complex at 5 mg/mL in 20 mM [TRIS-HCL](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl, 0.2% DM |
| Temperature | not reported |
| Growth time | not reported |


## Biological / Functional Insights

### Arginine-bound cytosol-open state (PDB 6C08)

The crystal structure of drSLC38A9 bound to arginine at 2.8 A resolution revealed the transporter in a cytosol-open conformation. In this state, the N-terminal domain is released from the substrate-binding pocket, and arginine is bound in a binding site located approximately halfway across the membrane. The binding site is formed by residues from TM1a, TM3, TM6a, and TM8. The structure shows a wide vestibule open to the cytosolic side, consistent with a cytosol-open state of the transport cycle. The Delta-N-truncated construct (residues 71-549) was used to obtain the arginine-bound structure, complexed with a Fab fragment that binds on the luminal side. Comparison with the bacterial arginine transporter AdiC (PDB 3L1L) shows structural similarity (r.m.s.d. 3.57 A over 72 C-alpha residues). Two luminal gating clusters were identified: cluster 1 (W128, K131, Q132, R344, E411, P415) and cluster 2 (P348, G491, R495, N542, Q546) that may regulate substrate access from the lysosomal lumen.

### N-plug inserted conformation blocks substrate binding site

The N-terminal domain (residues 1-96) of drSLC38A9 folds into a beta hairpin structure that inserts deep into the transmembrane domain, occupying the substrate binding pocket where arginine normally binds. The N-plug is stabilized by inter-domain hydrogen bonds with the transmembrane bundle and intra-domain hydrogen bonds between Ser80 and Glu82, His76, and Tyr85. This inserted state represents a cytosol-closed conformation of the transporter, effectively blocking substrate access from the cytoplasmic side. The vestibule into which the N-plug inserts measures approximately 20 A in diameter.

### Ball-and-chain model for mTORC1 activation

drSLC38A9 operates via a ball-and-chain mechanism linking luminal arginine levels to mTORC1 activation. At low luminal arginine, the N-plug dynamically samples both inserted and released states as an equilibrium. When arginine concentration increases, arginine molecules enter the substrate binding site from the luminal side, and the N-plug remains in the exposed state while arginine transport occurs. In the released state, the N-plug becomes available for binding to the Rag GTPase complex (drRagA and drRagC), which activates mTORC1 signaling. The 85PDH87 motif on the N-plug is essential for Rag GTPase interaction, corresponding to a conserved region on the beta hairpin structure.

### N-plug modulates arginine transport efficiency

Functional assays in reconstituted proteoliposomes demonstrated that the N-plug plays an inhibitory role in downregulating arginine transport. Mutants with disrupted N-plug binding (V77W, H81W, Y87F single mutants and V77W+H81W+Y87F triple mutant) displayed significantly higher arginine transport efficiency. The triple site mutant showed a 2-fold decrease in Km for arginine without significant change in Vmax. The superposition of the N-plug bound structure with the arginine-bound structure (PDB: 6C08) showed that the same set of backbone atoms are used for binding both the N-plug and arginine, supporting competitive binding between the N-plug and arginine.

### Arginine-enhanced leucine transport requires intact N-plug

drSLC38A9 exhibits higher affinity for leucine than arginine, and transport of leucine is arginine-regulated. The characteristic arginine-enhanced leucine transport was lost when the N-plug was deleted or its structure altered by mutation. Only drSLC38A9 with an intact N-terminal plug in its native beta hairpin structure showed enhanced leucine uptake in the presence of supplemented arginine. This indicates that the N-plug conformational change is required for the coordinated efflux of multiple essential amino acids from lysosomes.


## Cross-References

- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization and purification
- [Cholesterol Hydrogen Succinate](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Lipid additive used during solubilization
- [Decylmaltoside](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used in SEC buffer and tag removal
- [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) — Affinity resin for His-tag purification
- [Superdex 200 Increase](/xray-mp-wiki/reagents/additives/superdex-200/) — SEC resin for final purification step
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer used throughout purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Stabilizer in solubilization buffer
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Eluent competitor in TALON affinity purification
- [LEUT](/xray-mp-wiki/proteins/leut) — Structurally related membrane protein
- [TRIS-HCL](/xray-mp-wiki/reagents/buffers/tris-hcl) — Reagent used in this study
