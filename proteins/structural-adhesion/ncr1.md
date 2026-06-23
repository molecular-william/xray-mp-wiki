---
title: Saccharomyces cerevisiae Niemann-Pick Type C-Related Protein 1 (NCR1)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2019.08.038]
verified: false
---

# Saccharomyces cerevisiae Niemann-Pick Type C-Related Protein 1 (NCR1)

## Overview

NCR1 (Niemann-Pick type C-Related protein 1) from Saccharomyces cerevisiae is a member of the Resistance-Nodulation-Division (RND) superfamily and the functional yeast homolog of human [NPC1](/xray-mp-wiki/proteins/structural-adhesion/human-niemann-pick-c1/). It is a membrane protein essential for sterol homeostasis, mediating the integration of sterols into the vacuolar membrane after receiving sterols from the soluble carrier NPC2. NCR1 consists of 13 transmembrane helices, an N-terminal domain (NTD) that accepts sterols from NPC2, a Middle Luminal Domain (MLD), a C-terminal Domain (CTD), and a Sterol Sensing Domain (SSD). A key feature of NCR1 is a tunnel through the MLD/CTD core that connects the NTD to the SSD and the membrane leaflet, allowing sterols to bypass the ~60 A thick glycocalyx layer. The transmembrane domain contains a conserved proton-relay network (Asp631/Glu1068/His1072) that drives sterol transport through pincer-like movements of the MLD and CTD, analogous to the mechanism in the bacterial RND exporter [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2019.08.038 | 6R4L | 3.5 | Not specified | Saccharomyces cerevisiae NCR1 residues 21-1159 with C-terminal deca-histidine tag; expressed in S. cerevisiae DSY-5 | Ergosterol (observed in MLD/CTD tunnel at 0.87 occupancy) |
| doi/10.1016##j.cell.2019.08.038 | 6R4M | 2.8 | P6_1 | Saccharomyces cerevisiae NPC2 residues 24-195 with C-terminal deca-histidine tag; expressed in S. cerevisiae DSY-5; sterol-free form | None |
| doi/10.1016##j.cell.2019.08.038 | 6R4N | 2.9 | P6_1 | Saccharomyces cerevisiae NPC2 residues 24-195 with C-terminal deca-histidine tag; expressed in S. cerevisiae DSY-5; sterol-bound form | Ergosterol |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae DSY-5
- **Construct**: NCR1 with C-terminal thrombin cleavage site and deca-histidine tag in p423_GAL1 vector

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation and solubilization | Detergent extraction | — | 500 mM NaCl, 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.6% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Solubilized for 30 min at 4 C with 1.5 mg/mL [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (His-tag) | HisTrap HP 5mL | 500 mM NaCl, 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 70 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.017% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | On-column thrombin cleavage and Endo-H deglycosylation overnight |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex200 10/300 GL Increase | 200 mM NaCl, 20 mM MES pH 6.5, 0.01% DM-NG (decyl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol) | Followed by PNGase F treatment at 4 C overnight and second SEC step |
| Size-exclusion chromatography (second) | Size-exclusion chromatography | Superdex200 10/300 GL Increase | 200 mM NaCl, 20 mM MES pH 6.5, 0.01% DM-NG | Final sample concentrated to ~10 mg/mL for crystallization |


## Crystallization

### doi/10.1016##j.cell.2019.08.038

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) |
| Protein sample | Purified NCR1 at ~10 mg/mL in 0.01% DM-NG |
| Temperature | 20 |
| Growth time | Not specified |
| Cryoprotection | Cryocooled to 100 K |
| Notes | NCR1 crystal structure (6R4L); 3.5 A resolution; Rfree 30.1%; residues 21-1159 modeled; single molecule in asymmetric unit; four N-linked glycosylations; fourteen disulfide bridges |


## Biological / Functional Insights

### MLD/CTD tunnel enables sterol bypass of the glycocalyx

The NCR1 crystal structure reveals a tunnel through the pseudo two-fold symmetry point of the MLD and CTD domains, extending from the membrane leaflet and SSD shelf to the NTD loop-helix gate. An ergosterol molecule (0.87 occupancy) is observed inside this tunnel, positioned 24 A from the start of the membrane with its hydroxyl group pointing toward the NTD. The tunnel provides a pathway for sterols to bypass the ~60 A thick glycocalyx layer coating the vacuolar membrane. This tunnel-based mechanism is distinct from previous models involving NTD decoupling and direct membrane insertion. Analogous tunnels exist in hNPC1 structures and the related Patched protein family, suggesting a conserved transport mechanism within the RND superfamily.

### Proton-relay network drives sterol transport

The transmembrane domain contains a fully conserved cluster of charged residues: Asp631(M5), Glu1068(M11), and His1072(M11) at the pseudo two-fold symmetry axis. Mutagenesis of H1072A and D631N reduces sterol transfer from NPC2 to NCR1 by approximately 50%, despite being ~80 A from the NTD, demonstrating allosteric coupling from the proton-relay site to the sterol loading region. This network is analogous to the Asp407/Lys940 proton-relay pair in [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/), where proton translocation drives pincer-like movements of the coupling helices and Porter domain. The coupling loops connecting MLD/CTD to the transmembrane acidic cluster are proposed to transduce proton-driven conformational changes.

### NTD conformational flexibility enables sterol loading

The NTD of NCR1 adopts a distinct rotated conformation compared to the [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of hNPC1, with the sterol binding pocket rotated ~20 degrees and tilted ~40 degrees toward the MLD/CTD two-fold point. A loop-helix motif (residues 157-172) moves ~14 A toward the CTD, forming an interaction surface mediated by Ser162(NDT)-Asn865(CTD). Mutation of Asn865 (N865A) or deletion/mutation of the [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) hinge (residues 173-175) strongly reduces sterol transfer from NPC2, confirming that NTD conformational shifts are essential for sterol loading and unloading.


## Cross-References

- [RND Efflux Pumps](/xray-mp-wiki/concepts/rnd-efflux-pumps/) — NCR1 belongs to the RND superfamily; the sterol transport tunnel mechanism is analogous to the AcrB Porter domain transport pathway
- [Thermus thermophilus SecYEG Translocon Complex](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) — SecDF, another RND superfamily member, uses a similar remote coupling mechanism linking transmembrane proton transport to extracytoplasmic domain movements
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for membrane solubilization of NCR1
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for NCR1 structure determination
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Method used in structure determination or purification
- [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Related protein structure
- [NPC1](/xray-mp-wiki/proteins/structural-adhesion/human-niemann-pick-c1/) — Related protein structure
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
