---
title: KdpFABC Potassium-Importing Complex
created: 2017-06-21
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature22970]
verified: false
---

# KdpFABC Potassium-Importing Complex

## Overview

The KdpFABC complex is a four-subunit potassium pump from Escherichia coli that maintains intracellular K+ homeostasis under conditions in which potassium is limiting. The complex consists of a channel-like subunit (KdpA) belonging to the superfamily of potassium transporters (SKT) and a pump-like subunit (KdpB) belonging to the superfamily of P-type ATPases, together with two auxiliary subunits KdpC and KdpF, each having a single transmembrane helix. The 2.9 A X-ray crystal structure (Huang et al., 2017, PDB 5MRW) of the complete complex revealed a potassium ion within the selectivity filter of KdpA and a water molecule at a canonical cation site in the transmembrane domain of KdpB. The structure identified two structural elements mediating coupling between these subunits: a protein-embedded tunnel running between the K+ and water sites, and a helix controlling the cytoplasmic gate of KdpA linked to the phosphorylation domain of KdpB. A mechanism was proposed that repurposes protein channel architecture for active transport by using charge transfer through the intramembrane tunnel to trigger ATP hydrolysis and gating.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature22970 | 5MRW | 2.9 A | I222 | Full-length E. coli KdpFABC complex (KdpA Q116R mutant), with 8xHis tag on KdpC C-terminus; selenomethionine-substituted | K+ ion in S3 site of KdpA selectivity filter |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Ultracentrifugation (90,140g, 2 h) | — | 50 mM Tris pH 7.5, 1.2 M NaCl, 10 mM MgCl2, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/) | Cells lysed by Emulsiflex C3 homogenizer |
| Solubilization | Detergent solubilization | — | 50 mM Tris pH 7.5, 600 mM NaCl, 10 mM MgCl2, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/) + 1.2% [n-Decyl-β-D-maltoside](/xray-mp-wiki/reagents/detergents/dm/) (DM) | Incubated at 4C for at least 2 h |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Gradient elution (20-500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/)) | Ni2+-charged HiTrap chelating column (GE Healthcare) | 50 mM Tris pH 7.5, 600 mM NaCl, 10 mM MgCl2, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.15% DM, 20-500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |  |
| Size-exclusion chromatography | Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL | 50 mM Tris pH 7.5, 600 mM NaCl, 10 mM MgCl2, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.15% DM |  |


## Crystallization

### doi/10.1038##nature22970

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Reservoir | 100 mM [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) (pH 5.0), 50 mM NaCl, 20 mM CaCl2, 30% [PEG](/xray-mp-wiki/reagents/additives/peg/) 550 MME |
| Temperature | 20 C |
| Notes | Plate-like morphology with birefringence; crystals appeared within 1-2 weeks |


## Biological / Functional Insights

### Coupling mechanism between KdpA and KdpB

The structure reveals a 1.4 A radius intramembrane tunnel connecting the K+ binding site in KdpA to a water molecule bound at the canonical cation site in KdpB. This tunnel likely facilitates proton charge transfer that triggers ATP hydrolysis in KdpB in response to K+ binding in KdpA. Key residues include Asp583 and Lys586 in KdpB, and Glu370 and Arg493 in KdpA.

### KdpA as a repurposed K+ channel

KdpA uses a selectivity filter architecture descended from the [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) K+ channel, but repurposes it for active transport rather than passive diffusion. Unlike [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), KdpA has a gating loop at the cytoplasmic end derived from the D3M2 helix, and the S1 site of the selectivity filter is occupied by Arg116 (Q116R in this construct).

### E1 state of KdpB

KdpB adopts an E1 conformational state with the A domain decoupled from the P domain, the N and P domains juxtaposed, Asp307 unphosphorylated, and the bM4 helix unwound at the conserved Pro264 motif. A phosphoserine (Ser162) in the A domain forms a salt bridge with Lys357 and Arg363 of the N domain, suggesting an autoinhibited state.

### KdpC as a periplasmic gate

The soluble domain of KdpC is held by two loops from D2 and D3 repeats of KdpA via a robust hydrogen bond network. This interaction suggests that relative movements between KdpA repeats could move KdpC into an occluding position in response to conformational changes in KdpB, acting as a periplasmic gate.


## Cross-References

- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Related protein structure
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) — Buffer component in purification or crystallization
- [n-Decyl-β-D-maltoside](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used in purification or crystallization
