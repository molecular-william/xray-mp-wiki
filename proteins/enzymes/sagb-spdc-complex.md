---
title: SagB-SpdC Complex
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##s41564-020-00808-5]
verified: false
---

# SagB-SpdC Complex

## Overview

The SagB-SpdC complex from Staphylococcus aureus is a membrane protein complex that functions as a peptidoglycan release factor during cell wall assembly. SagB is a membrane-anchored glucosaminidase (N-acetylglucosaminidase) that cleaves nascent peptidoglycan strands, while SpdC is an eight-transmembrane-helix protein similar to eukaryotic CAAX proteases that scaffolds SagB and regulates its cleavage activity. The crystal structure of the complex was determined at 2.6 A resolution (PDB: 6U0O) using the lipidic cubic phase (LCP) method, revealing that SpdC scaffolds SagB through its single transmembrane helix and orients the hydrolase active site at the membrane interface.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41564-020-00808-5 | 6U0O | 2.6 | C2 | Full-length SagB with SpdC residues 1-256 (truncated C-terminal domain) |  |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: SagB-His6 and Flag-SpdC co-expressed from pDUET vector; Ulp1 protease co-expressed for SUMO tag removal
- **Notes**: Co-expression system with arabinose-inducible Ulp1 protease for Flag-SpdC

### Purification Workflow

- **Expression system**: Escherichia coli BL21(DE3)
- **Expression construct**: SagB-His6 + Flag-SpdC (co-expression)
- **Tag info**: His6 tag on SagB, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) on SpdC

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | — |  | Grown at 30°C to A600=0.6, shifted to 24°C, induced at A600=1.1 with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) and 0.2% arabinose for 16 h |
| Membrane preparation | Differential centrifugation | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl | Cells lysed by microfluidizer; membranes collected by ultracentrifugation at 100,000g |
| Solubilization | Detergent extraction | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% n-dodecyl-β-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membranes rocked at 4°C for 1 h |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA agarose | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Wash with 10 mM and 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); elute with 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 2 mM CaCl2 |
| Anti-Flag [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | M1 anti-Flag resin | 50 mM HEPES pH 7.5, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mM CaCl2 + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted with 20 mM HEPES pH 7.5, 500 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Size-exclusion chromatography | SEC | Sephadex S200 Increase 10/300 GL | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final polishing step |

**Final sample**: 35-40 mg/mL SagB-SpdC complex in crystallization buffer
**Yield**: Not reported
**Purity**: >95% by SDS-PAGE


## Crystallization

### doi/10.1038##s41564-020-00808-5

| Parameter | Value |
|---|---|
| Method | LCP |
| Protein sample | SagB-SpdC complex at 35-40 mg/mL |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | 1:1.5 |
| Temperature | 293 |
| Growth time | 3-7 days |
| Notes | Most crystals appeared within 36 h; complete in 3-7 days. Crystals flash-frozen in liquid nitrogen without additional cryoprotectant. |


## Biological / Functional Insights

### Peptidoglycan release mechanism

The SagB-SpdC complex cleaves nascent peptidoglycan strands internally to produce free oligomers as well as lipid-linked oligomers that can undergo further elongation. The cleavage products retain a diphospholipid anchor at the reducing end, consistent with glucosaminidase cleavage leaving a terminal N-acetylmuramic acid. This complex meets the criteria for a peptidoglycan release factor, detaching newly synthesized peptidoglycan from the cell membrane for integration into the cell wall matrix.

### SpdC as a non-catalytic scaffold

SpdC functions primarily as a scaffolding protein rather than an active enzyme. Despite its similarity to eukaryotic CAAX proteases, SpdC lacks conserved catalytic residues required for proteolytic activity. The SagB catalytic glutamate (Glu155) is essential for cleavage activity, while conserved CAAX protease residues in SpdC (E135, R139, H210) are dispensable. SpdC controls the length of cleavage products through its scaffolding function.

### Structural basis of complex formation

The 2.6 A crystal structure shows SpdC as an eight-transmembrane-helix protein that scaffolds SagB through its single transmembrane helix and a juxtamembrane interface. The transmembrane domain of SpdC has similar topology to the eukaryotic CAAX protease Rce1, but the helices differ in length and loop conformations. The SagB-SpdC interface is crucial for complex formation - the SagB TM helix makes close contacts with SpdC TM3, and removing the TM helix or swapping it with the SagA TM helix disrupts complex formation.


## Cross-References

- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in purification or crystallization
- [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) — Buffer component in purification or crystallization
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
