---
title: CpTRIC Channel from Clostridium perfringens
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms15103]
verified: false
---

# CpTRIC Channel from Clostridium perfringens

## Overview

CpTRIC is a Trimeric Intracellular Cation (TRIC) channel from the bacterium Clostridium perfringens. It forms a homotrimeric complex with each monomer containing seven transmembrane helices. The channel was crystallized in both native and [Selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/) (Se-Met) labeled forms at similar resolution, enabling SAD phasing. A distinctive feature of CpTRIC is the binding of Cd2+ ions at four distinct sites per protomer, including a site at the protomer interface and sites within the ion-conducting pore.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms15103 | not specified | 2.4 A | R32 | CpTRIC residues 1-219, wild-type, Se-Met labeled | Cd2+ (4 binding sites per protomer), Se-Met for phasing |
| doi/10.1038##ncomms15103 | not specified | 2.4 A | R32 | CpTRIC residues 1-219, wild-type, Native | Cd2+ (4 binding sites per protomer) |

## Expression and Purification

- **Expression system**: not specified in supplementary tables
- **Construct**: CpTRIC from Clostridium perfringens. The crystallization construct covers residues 1-219, encompassing the transmembrane domain. [Selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/) (Se-Met) labeled protein was prepared for SAD phasing.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein solution | not specified | -- | [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) 20 mM pH 7.5, NaCl 200 mM + not specified | Protein solution for CpTRIC crystallization |


## Crystallization

### doi/10.1038##ncomms15103

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | CpTRIC residues 1-219 WT, Se-Met labeled, in [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) 20 mM pH 7.5, NaCl 200 mM |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | CpTRIC Se-Met crystal form. Wavelength 0.97876 A, space group R32, resolution ~2.4 A. Se-Met used for SAD phasing. Cd2+ bound at four distinct sites per protomer. |


## Biological / Functional Insights

### Cd2+ binding at four distinct sites

CpTRIC binds Cd2+ ions at four distinct sites per protomer, as revealed by anomalous diffraction at 3.5 sigma contour level. Site 1 is located near the protomer interface and involves coordination by Asp40 residues from adjacent protomers. Site 2 is involved in molecular packing in the R32 crystal lattice. Site 3 is positioned near the cytoplasmic side of the membrane, and Site 4 is located at the entrance of the ion-conducting pore near the extracellular side. The Cd2+ binding network involves specific residues that coordinate the metal ion, providing structural insight into divalent cation selectivity in TRIC channels.

### Prokaryotic TRIC structure with ion-binding sites

The CpTRIC structure (R32, 2.4 A) reveals the overall architecture of a prokaryotic TRIC channel with bound Cd2+ ions. The structure shares the characteristic 7-TM per monomer topology with SaTRIC and eukaryotic TRIC-B channels. The Cd2+ binding sites provide a model for understanding how TRIC channels discriminate between different cation species. The protomer interface site (Site 1) is particularly notable as it involves inter-protomer coordination by Asp40, suggesting that trimeric assembly is critical for metal ion binding.

### Structural comparison with SaTRIC

CpTRIC structure was superimposed onto SaTRIC (Type 2a, Na+ bound) for structural comparison. The overall fold is conserved, with the characteristic hourglass-shaped pore and 3+3+1 helix organization. The comparison reveals both conserved features of the TRIC channel fold and species-specific differences in the ion-binding environment, particularly in the pore region where different cations (Na+ in SaTRIC vs. Cd2+ in CpTRIC) occupy distinct binding sites.


## Cross-References

- [SaTRIC Channel from Sulfolobus acidocaldarius](/xray-mp-wiki/proteins/voltage-gated-channels/sa-tric/) — Homologous prokaryotic TRIC channel; structural comparison between prokaryotic TRIC channels from different organisms
- [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) — Eukaryotic TRIC channel homolog; shared 7-TM hourglass architecture
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — CpTRIC crystallized by LCP method with PEG400 precipitant
- [TRIC Channel Gating Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/tric-channel-gating/) — CpTRIC belongs to the TRIC channel family with ion-dependent gating
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer component (20 mM, pH 7.5) used in protein solution and crystallization
- [Selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/) — Se-Met labeled CpTRIC used for SAD phasing at 0.97876 A wavelength
- [Selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/) — Referenced in the context of Selenomethionine
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in the context of Hepes
- [PEG400](/xray-mp-wiki/reagents/peg400/) — Referenced in the context of PEG400
