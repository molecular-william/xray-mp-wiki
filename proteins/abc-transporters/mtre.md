---
title: MtrE Outer Membrane Channel from Neisseria gonorrhoeae
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [porin, membrane-protein, xray-crystallography]
sources: [doi/10.1371##journal.pone.0097475]
verified: false
---

# MtrE Outer Membrane Channel from Neisseria gonorrhoeae

## Overview

MtrE is the outer membrane channel component of the [MtrCDE Tripartite Multidrug Efflux Pump](/xray-mp-wiki/concepts/mtrcde-tripartite-efflux-pump/) from Neisseria gonorrhoeae. It belongs to the hydrophobic and amphiphilic efflux resistance-nodulation-cell division (HAE-RND) family of outer membrane channels. MtrE forms a homotrimeric channel that creates a vertical tunnel extending from the outer membrane surface down to the periplasmic end, representing an open conformational state. An aspartate ring (D402/D405 from each protomer) at the periplasmic entrance acts as a selectivity gate.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1371##journal.pone.0097475 |  | 3.29 | P6_3_22 | Full-length MtrE (residues 1-445) with C-terminal 6xHis tag |  |

## Expression and Purification

- **Expression system**: E. coli C43(DE3)
- **Construct**: Full-length MtrE with C-terminal 6xHis tag in pBAD22b vector
- **Notes**: Cells grown in LB medium with 100 ug/ml [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) at 37 C to OD600=0.5, then cooled to 25 C for induction.
- **Induction**: 0.2% (w/v) arabinose at 25 C for 16 h

### Purification Workflow

- **Expression system**: E. coli C43(DE3)
- **Expression construct**: Full-length MtrE with C-terminal 6xHis tag
- **Tag info**: C-terminal 6xHis tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | French press | — | 20 mM Na-HEPES pH 7.5, 300 mM NaCl, 1 mM PMSF |  |
| Membrane collection | Ultracentrifugation | — |  | Total membrane fraction collected |
| Pre-extraction | Detergent wash | — | 0.5% (w/v) sodium lauroyl sarcosinate, 20 mM Na-HEPES pH 7.5, 50 mM NaCl | 30 min incubation at room temperature to pre-extract inner membrane proteins |
| Outer membrane collection | Ultracentrifugation and wash | — | 20 mM Na-HEPES pH 7.5, 50 mM NaCl | Washed twice |
| Solubilization | Detergent extraction | — | 2% (w/v) n-dodecyl beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Insoluble material removed by ultracentrifugation at 100,000xg |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni2+-affinity column | — |  | Purified protein >95% pure by SDS-PAGE |

**Final sample**: 15 mg/ml in 20 mM Na-HEPES pH 7.5, 200 mM NaCl, 0.05% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/)
**Purity**: >95% by SDS-PAGE


## Crystallization

### doi/10.1371##journal.pone.0097475

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 15 mg/ml MtrE in 20 mM Na-HEPES pH 7.5, 200 mM NaCl, 0.05% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 20% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 0.2 M [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) pH 4.6, 0.25 M MgSO4, 2% (w/v) [OG](/xray-mp-wiki/reagents/detergents/og/) (OG) |
| Temperature | Room temperature |
| Cryoprotection | 30% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 0.2 M [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) pH 4.6, 0.25 M MgSO4, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 2% OG |
| Notes | 2 ul protein + 2 ul reservoir. Crystals grew within two weeks to 0.2 x 0.2 x 0.2 mm. Diffraction data to 3.29 A. |


## Biological / Functional Insights

### Open conformational state of MtrE

The MtrE structure reveals a fully open channel with a continuous vertical tunnel from the outer membrane surface to the periplasmic tip. The interior diameter at the widest section (outer membrane surface) is ~22 A. The volume of the continuous channel is ~45,000 A^3. The dilation of MtrE is higher than any reported open state of TolC, with D405 side chain O(delta2) atoms 11.8 A apart (vs 6.2-9.9 A in TolC).

### Periplasmic aspartate selectivity gate

An aspartate ring composed of six aspartate residues (D402 and D405 from each of three protomers) is located at the periplasmic entrance. The internal diameter is ~12 A, creating the narrowest region of the tunnel. This ring acts as a selectivity gate and can be blocked by large cations such as hexamminecobalt(III). The open state likely reflects the low-pH form (crystallized at pH 4.6), which neutralizes the aspartate ring.

### Intra- and inter-protomer grooves for MtrC interaction

The periplasmic domain of the MtrE trimer forms three intra-protomer and three inter-protomer grooves lined with charged and polar residues (E161, R168, E407, E414, Q421 at intra-protomer; Q167, N178, E198, E202, R215, R219 at inter-protomer). Residues E414, Q421, and N178 are important for MtrCDE function. These grooves likely provide interaction sites for the MtrC membrane fusion protein.

### MtrC-mediated gating of the MtrE channel

The opening and closing of the MtrE channel may be regulated by conformational changes in the MtrC membrane fusion protein, which propagate motion from the MtrD inner membrane efflux pump. As MtrD is a PMF-dependent pump, active proton translocation likely provides the energy to open and close MtrE.


## Cross-References

- [MtrCDE Tripartite Multidrug Efflux Pump](/xray-mp-wiki/concepts/mtrcde-tripartite-efflux-pump/) — MtrE is the outer membrane channel component of this tripartite efflux system
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used for MtrE solubilization and purification
- [n-Octyl-beta-D-glucoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Used as crystallization additive
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) — Antibiotic used in selection
- [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) — Buffer component in purification or crystallization
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
