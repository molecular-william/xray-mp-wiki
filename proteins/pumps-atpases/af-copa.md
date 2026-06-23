---
title: "CopA from Archaeoglobus fulgidus (AfCopA)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-022-32751-w]
verified: false
---

# CopA from Archaeoglobus fulgidus (AfCopA)

## Overview

CopA from Archaeoglobus fulgidus (AfCopA) is a copper-transporting P1B-type ATPase that facilitates cellular export of copper. P1B-ATPases are present in all kingdoms of life and are essential for copper homeostasis. This paper presents the first inward-facing E1 conformation structure of a P1B-ATPase at 2.7 A resolution, revealing the mechanism of Cu+ uptake from cytosolic chaperones. The structure shows a unique A-domain arrangement and identifies a methionine (M158) that plays a key role in chaperone-mediated Cu+ transfer to the transmembrane core, together with the CPC signature motif cysteines (C380, C382).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-022-32751-w | 7ROI | 2.7 | Not specified | AfCopA truncated construct lacking N- and C-terminal heavy metal binding domains (residues G80-G736), expressed in E. coli | Cu+ (in the presence of copper) |
| doi/10.1038##s41467-022-32751-w | 7ROH | 3.3 | Not specified | AfCopA truncated construct (residues G80-G736) | Cu+ (data collected at copper absorption edge, 1.37 A) |
| doi/10.1038##s41467-022-32751-w | 7ROG | 2.8 | Not specified | AfCopA truncated construct (residues G80-G736) | Apo (no copper) |

## Expression and Purification

- **Expression system**: Escherichia coli C43 strain
- **Construct**: AfCopA deltaNdeltaC (residues G80-G736, UniProtKB O29777) cloned into pET-22b(+); expression induced with 1 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg) at 20 C for 16 h
- **Induction**: 1 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg), 20 C, 16 h

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization (25 kpsi) | — | 20 mM Tris-HCl pH 7.6, 200 mM KCl, 20% glycerol, 5 mM [Beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol), 1 mM PMSF | Cells disrupted at 25 kpsi, debris removed by centrifugation, membranes collected by ultracentrifugation at 185,500 x g for 3 h |
| Solubilization | [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm) solubilization | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.6, 200 mM KCl, 1% DDM | Membranes solubilized for 2 h |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | Ni-Sepharose resin | Ni-Sepharose loose resin (Cytiva) | 20 mM Tris-HCl pH 7.6, 200 mM KCl, 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) (wash), 500 mM imidazole (elution) | Sample loaded twice; [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease) added for tag cleavage |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [Superose 6 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superose-6-increase) column | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.6, 200 mM KCl, 0.02% DDM |  |


## Crystallization

### doi/10.1038##s41467-022-32751-w

| Parameter | Value |
|---|---|
| Method | HiLiDe (high lipid and detergent) crystallization |
| Protein sample | AfCopA at 2.25 mg/mL DOPC and 5 mg/mL [Octaethylene Glycol Monododecyl Ether (C12E8)](/xray-mp-wiki/reagents/detergents/c12e8), incubated 16 h at 4 C; 1 mM CuSO4 added for Cu+ bound structures |
| Reservoir | 1.5 M ammonium citrate, 0.1 M MES pH 5.5, 5 mM [Beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) |
| Temperature | 4 C |
| Notes | Hanging drop vapor diffusion; 5.0 mM 06:0 Lyso PC additive used for final data collection; crystals flash-frozen in liquid nitrogen |


## Biological / Functional Insights

### E1 inward-facing conformation

The AfCopA E1 structure represents the first metal-bound conformation of a P1B-ATPase. The A-domain arrangement differs from classical P2-ATPases (like SERCA), suggesting the P-type ATPase transport mechanism is less conserved than previously assumed. MA-M2 and M3-M6 form two helix bundles that shift relative to each other in the E2 to E1 transition, exposing the CPC motif of M4 to the cytoplasm.

### Chaperone-mediated copper delivery

The structure reveals a mechanism for direct Cu+ transfer from the cytosolic chaperone CopZ to the ATPase core. M158 at the MB'-M1 transition forms a transient entry site together with C380 and C382 of the CPC motif in M4. Computational docking shows CopZ fits in the groove between MB' and M2-4, with M158 conformations positioned within 6 A of the CopZ-bound Cu+ ion, enabling direct Cu+ transfer.

### CPC motif exposure in E1 state

In the E1 conformation, C380 and C382 of the conserved CPC motif in M4 are surface exposed and oriented toward M1-2 including M158, indicative of an early E1 conformation congruent with ion uptake. Molecular dynamics simulations support trigonal-planar Cu+ coordination by M158, C380, and C382 following uptake from the aqueous environment.


## Cross-References

- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) — Purification method used in protein preparation
- [Size-Exclusion Chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) — Purification method used in protein preparation
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) — Additive used in purification or crystallization buffers
- [Superose 6 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superose-6-increase) — Additive used in purification or crystallization buffers
- [C12E8](/xray-mp-wiki/reagents/detergents/c12e8) — Detergent used for membrane protein solubilization
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris-hcl) — Buffer component in purification and crystallization
- [Beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) — Additive used in purification or crystallization buffers
- [Iptg](/xray-mp-wiki/reagents/additives/iptg) — Additive used in purification or crystallization buffers
- [Tev Protease](/xray-mp-wiki/reagents/additives/tev-protease) — Additive used in purification or crystallization buffers
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm) — Detergent used for membrane protein solubilization
