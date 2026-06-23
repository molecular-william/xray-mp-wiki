---
title: Plant Vacuolar Iron Transporter 1 (VIT1)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41477-019-0367-2]
verified: false
---

# Plant Vacuolar Iron Transporter 1 (VIT1)

## Overview

Vacuolar [IRON](/xray-mp-wiki/reagents/additives/iron/) transporter 1 (VIT1) from rose gum Eucalyptus grandis (EgVIT1) is a H+-dependent antiporter that transports cytoplasmic ferrous ions (Fe2+) and other transition metal ions into vacuoles, playing a critical role in [IRON](/xray-mp-wiki/reagents/additives/iron/) homeostasis in plants. VIT1 adopts a novel protein fold forming a dimer of five membrane-spanning domains, with an ion-translocating pathway constituted by conserved methionine and carboxylate residues at the dimer interface. The second transmembrane helix protrudes from the lipid membrane by about 40 Å and connects to a three-helical bundle, triangular cytoplasmic domain (metal binding domain, MBD), which binds to substrate metal ions and stabilizes their soluble form. Modification of the VIT1 gene leads to increased [IRON](/xray-mp-wiki/reagents/additives/iron/) content in crops (biofortification), and a VIT1 homologue from Plasmodium falciparum is considered a potential drug target for malaria.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41477-019-0367-2 | 6IU3 | 2.7 A | Not specified | EgVIT1(23-249) full-length construct, wild-type, crystallized in LCP in presence of zinc ions | Zn2+ (bound to MBD) |
| doi/10.1038##s41477-019-0367-2 | 6IU4 | 2.25 A | Not specified | Isolated cytoplasmic metal binding domain (MBD, EgVIT1 70-144), crystallized by vapor diffusion | Zn2+ (three zinc ions clustered within 2.5 A) |
| doi/10.1038##s41477-019-0367-2 | 6IU5 | Not specified | Not specified | EgVIT1(23-249) Co2+-soaked crystal | Co2+ (bound within hydrophilic pocket near Glu72) |
| doi/10.1038##s41477-019-0367-2 | 6IU6 | Not specified | Not specified | Isolated MBD (EgVIT1 70-144) Ni2+-soaked | Ni2+ (bound to M2 site) |
| doi/10.1038##s41477-019-0367-2 | 6IU8 | Not specified | Not specified | Isolated MBD (EgVIT1 70-144) Co2+-soaked | Co2+ (bound to M2 site) |
| doi/10.1038##s41477-019-0367-2 | 6IU9 | Not specified | Not specified | Isolated MBD (EgVIT1 70-144) Fe2+-soaked | Fe2+ (bound to M2 site) |

## Expression and Purification

- **Expression system**: Escherichia coli (for EgVIT1 full-length and MBD constructs)
- **Construct**: EgVIT1(23-249) with N-terminal His8 tag and TEV cleavage site; EgVIT1(70-144) isolated MBD with N-terminal His8 tag and TEV cleavage site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl | E. coli cells expressing EgVIT1 were lysed by high-pressure homogenization. |
| Membrane isolation | Ultracentrifugation | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl | Membranes pelleted by ultracentrifugation at 100,000 x g. |
| Solubilization | Detergent solubilization | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + 1% (w/v) n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membranes solubilized in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for 1 h at 4°C. |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (IMAC) | Ni-NTA agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash), 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) | His8-tagged EgVIT1 purified by Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/). |
| TEV cleavage | Protease cleavage | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | His8 tag removed by TEV protease digestion overnight at 4°C, followed by reverse Ni-NTA to remove cleaved tag and uncleaved protein. |
| Size-exclusion chromatography | Size-exclusion chromatography (SEC) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) Increase 10/300 GL | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final polishing step yielded pure monomeric EgVIT1. |


## Crystallization

### doi/10.1038##s41477-019-0367-2

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | EgVIT1(23-249) in [DDM](/xray-mp-wiki/reagents/detergents/ddm/), reconstituted into [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) LCP |
| Temperature | 20°C |
| Growth time | One month |
| Notes | Crystals grown in LCP using the protein:[Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) ratio of 42:58. Hg-derivative crystals obtained using EgVIT1(G242C) mutant with 1.0 mM CH3HgCl. Co2+-soaked crystals obtained by soaking in 30 mM CoCl2 for 10 min. Diffraction data collected at SPring-8 BL32XU using EIGER X 9M detector. |


## Biological / Functional Insights

### Novel protein fold for transition metal transport

VIT1 adopts a distinct protein fold from any known transporter structures, featuring five transmembrane segments per protomer with TM1 at the center surrounded by TM2-5 in clockwise order. The long TM2 segment protrudes ~40 Å from the membrane to connect to a cytoplasmic metal binding domain (MBD). This architecture is likely conserved among the CCC1/VIT1 family.

### Cytoplasmic MBD captures and stabilizes ferrous ions

The MBD binds three transition metal ions (Zn2+ in crystallization conditions) via five glutamic acids (Glu102, Glu105, Glu113, Glu116, Glu153) and one methionine (Met149). The three zinc ions are clustered within 2.5 Å with a central water molecule in OH- or O2- form. Metal-soaking experiments showed that Fe2+, Co2+, and Ni2+ differentially occupy the M1-M3 sites, with the M2 site (involving Met149) being commonly occupied by all transition metals tested.

### H+-coupled antiport mechanism

The ion-translocating pathway is sealed on the vacuolar side by hydrophobic residues (Leu51, Leu55 on TM1; Ile64, Ala68 on TM3), indicating an inward-open conformation. Substrate binding involves Asp43, Met80, and Glu72 along the central pathway. Conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (Gly44, Gly76) and proline (Pro48) residues create transmembrane kinks that initiate opening of vacuolar hydrophobic seals for metal release, coupled with proton re-protonation of Glu72 for H+/metal antiport.

### Methionine residue provides transition metal selectivity

Met80 at the substrate-binding site provides selectivity for transition metal ions while discriminating against alkaline earth metals (e.g., Ca2+), similar to the mechanism in NRAMP transporters. The intermediate property of the methionine thioether group is suitable for both selective binding to substrate metal ions and preventing proton leakage through the central pathway.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/n-dodecyl-beta-d-maltopyranoside/) — Detergent used for membrane protein solubilization and purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA IMAC used for His8-tagged protein purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC used as final purification step
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — EgVIT1 crystallized in monoolein LCP
- [SLC11/NRAMP Family](/xray-mp-wiki/concepts/slc11-nramp-family/) — Related transition metal transporter family with conserved methionine selectivity mechanism
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IRON](/xray-mp-wiki/reagents/additives/iron/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Buffer component in purification or crystallization
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
