---
title: "DltB (Membrane-Bound O-Acyltransferase)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-018-0568-2]
verified: false
---

# DltB (Membrane-Bound O-Acyltransferase)

## Overview

DltB is a membrane-bound O-acyltransferase (MBOAT) from Streptococcus thermophilus responsible for the D-alanylation of cell-wall teichoic acid in Gram-positive bacteria. Crystal structures of DltB were determined in the apo state (PDB 6BUG, 3.30 Å; PDB 6BUI, 3.30 Å) and in complex with the D-alanyl carrier protein DltC-Ppant (PDB 6BUH, 3.15 Å). DltB contains a ring of 11 peripheral transmembrane helices that shield a highly conserved extracellular structural funnel extending into the middle of the lipid bilayer. The conserved catalytic histidine residue (His336) is located at the bottom of this funnel and is connected to the intracellular DltC through a narrow tunnel. Mutation of either the catalytic histidine or the DltC-binding site abolishes D-alanylation of lipoteichoic acid and sensitizes Bacillus subtilis to cell-wall stress, suggesting cross-membrane catalysis involving the tunnel. Structure-guided sequence comparison reveals a conserved structural core among MBOATs from different organisms, providing a template for understanding structure-function relationships and for developing therapeutic MBOAT inhibitors targeting proteins such as PORCN, HHAT, and DGAT1.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-018-0568-2 | 6BUG | 3.30 A | P2_1 | Full-length DltB from Streptococcus thermophilus | None (apo state) |
| doi/10.1038##s41586-018-0568-2 | 6BUH | 3.15 A | P2_1 | DltB in complex with DltC-Ppant (4'-phosphopantetheine-modified DltC) | 4'-phosphopantetheine (Ppant) on DltC Ser35 |
| doi/10.1038##s41586-018-0568-2 | 6BUI | 3.30 A | P2_1_2_1_2 | Full-length DltB from Streptococcus thermophilus | None (apo state) |

## Expression and Purification

- **Expression system**: Escherichia coli C43 (DE3)
- **Construct**: Full-length S. thermophilus DltB subcloned into pET21b. Expression induced with 0.4 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) at OD600 = 1.0, 37°C for 5 h. DltC subcloned into pQLink with N-terminal GST-tag for complex studies.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Sonication and ultracentrifugation | -- | 25 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + -- | Cells disrupted by sonication, debris removed at 20,000g for 10 min, membranes collected at 100,000g for 1.5 h |
| Solubilization | Detergent solubilization | -- | 25 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + 1.5% (w/v) n-decyl-β-D-maltopyranoside ([DM](/xray-mp-wiki/reagents/detergents/dm/)) | Incubated for 2 h at 4°C, then ultracentrifuged at 100,000g for 30 min |
| Affinity chromatography | Ni-NTA affinity | Ni-NTA (Qiagen) | 25 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl, 25 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.2% (w/v) [DM](/xray-mp-wiki/reagents/detergents/dm/) | Wash buffer; eluted with 400 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/30 (GE Healthcare) | 25 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + 0.2% [DM](/xray-mp-wiki/reagents/detergents/dm/) (or other detergents from Anatrace) | Concentrated to 10 mg/ml before SEC; peak fractions collected |


## Crystallization

### doi/10.1038##s41586-018-0568-2

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | DltB purified in n-nonyl-β-D-glucopyranoside (Anatrace) at ~10 mg/ml |
| Reservoir | 21% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 100 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 100 mM NaCl, 100 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) |
| Temperature | 20°C (room temperature) |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystal form I (P2₁, 3.30 Å): native DltB apo. Crystal form II (P2₁, 3.15 Å): DltB-DltC-Ppant complex, DltB and DltC mixed at 1:2 molar ratio. Crystal form III (P2₁2₁2, 3.30 Å): DltB apo. Au-SAD phasing used for structure determination (Au derivative for crystal form I). |


## Biological / Functional Insights

### Novel MBOAT fold with ring of peripheral helices

DltB contains 17 helices arranged with 11 peripheral transmembrane helices forming an external ring-shaped ridge that shields a central basin thinner than the lipid bilayer. The structure can be divided into three parts: the N-terminal helical ridge (N-ridge), the central core, and the C-terminal helical ridge (C-ridge). A Dali search found no similar structures, revealing a novel protein fold for the MBOAT superfamily.

### Conserved extracellular funnel and catalytic histidine

A deep extracellular structural funnel extends from the extracellular surface into the middle of the lipid bilayer. The completely conserved catalytic histidine (His336) is located at the bottom of this funnel. The funnel surface is highly conserved among MBOATs, suggesting it serves as the substrate-binding site for the acyl-group acceptor (e.g., LTA for DltB).

### Cross-membrane catalysis via a narrow tunnel

A narrow tunnel connects the extracellular funnel to the intracellular side where DltC-Ppant binds. The distance between the Ser35-Ppant phosphate group and His336 is approximately 21 Å — the length of the Ppant-D-Ala chain (~20 Å). This suggests a cross-membrane catalytic mechanism where the Ppant chain delivers D-Ala from DltC through the tunnel to His336 for transfer to LTA in the extracellular funnel.

### DltC binding interface

DltC-Ppant binds to the cytoplasmic side of DltB primarily through a mostly hydrophobic interface formed by DltB residues Met302, Val305, Ile306, and Met309 on the C-terminal half of helix H13, and DltC residues Met36, Val39, Val43, and Val55 on helix α3 and the α3-α4 loop. Arg317 forms charged hydrogen bonds with DltC Glu40, and the Ppant phosphate group forms a salt bridge with DltB Lys282.

### Conserved MBOAT core across species

Despite low overall sequence homology, the MBOAT central core (funnel, tunnel, His336, and key helices H6, H10, H12) is conserved among vertebrate MBOATs including PORCN (Wnt acyltransferase), HHAT (hedgehog acyltransferase), GOAT (ghrelin O-acyltransferase), DGAT1, and ACAT. The peripheral ridges are non-conserved and likely mediate distinct substrate recognition, enabling targeted drug development against individual MBOAT family members.

### Functional validation of catalytic mechanism

Mutation of His336 (catalytic His) or the DltC-binding interface residues (V305D/I306D) completely abolished LTA D-alanylation and reduced B. subtilis viability under lysozyme stress. The DltB-specific inhibitor m-AMSA also blocked D-alanylation, confirming the functional importance of the observed structural features for DltB activity.


## Cross-References

- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — DltB was crystallized using hanging-drop vapor diffusion
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA affinity chromatography used for DltB purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC (Superdex-200) used for final purification step
- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Au-SAD phasing used for experimental structure determination
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Purification and crystallization buffer (Tris-HCl pH 7.5-8.0)
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Crystallization additive (100 mM MgCl2)
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant (21% PEG400)
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used for elution in Ni-NTA affinity chromatography
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in context related to Iptg
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in context related to Tris Hcl
