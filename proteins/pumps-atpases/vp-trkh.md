---
title: "TrkH from Vibrio parahaemolyticus (VpTrkH)"
created: 2026-06-09
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09731]
verified: false
---

# TrkH from Vibrio parahaemolyticus (VpTrkH)

## Overview

[TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) from Vibrio parahaemolyticus (VpTrkH) is a potassium ion channel belonging to the Trk/Ktr/Kdp superfamily of cation transport systems. The structure reveals a homodimeric architecture with each protomer composed of four transmembrane domains (D0-D3) surrounding a central pore domain (D4). The selectivity filter is structurally similar to that of [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), with a conserved TVGYG signature sequence, but the pore helix dipole is oriented differently. VpTrkH is the first high-resolution structure of a Trk family potassium channel and provides insight into potassium uptake mechanisms in bacteria.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09731 | 3PJZ | 3.5 | P2(1)2(1)2(1) | Full-length VpTrkH with C-terminal deca-histidine tag; expressed in Escherichia coli; SeMet-labeled for phasing | K+ |
| doi/10.1038##nature09731 | 3PJZ | 3.5 | P2(1)2(1)2(1) | Full-length VpTrkH with C-terminal deca-histidine tag | Rb+ |
| doi/10.1038##nature09731 | 3PJZ | 4.2 | P2(1)2(1)2(1) | Full-length VpTrkH with C-terminal deca-histidine tag | Ba2+ |
| doi/10.1038##nature09731 | 3PJZ | 3.9 | P2(1)2(1)2(1) | SeMet-labeled full-length VpTrkH with C-terminal deca-histidine tag; used for SAD phasing | -- |

## Expression and Purification

### Purification Workflow

- **Expression system**: Escherichia coli BL21(DE3)
- **Expression construct**: Full-length VpTrkH with C-terminal deca-histidine tag; expressed with [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction; SeMet-labeled for phasing in minimal medium supplemented with [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/)
- **Tag info**: C-terminal deca-histidine tag, cleaved by TEV protease

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer or French press | -- | Not specified in supp info + -- | Cells harvested and lysed for membrane preparation |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Co2+ IMAC column ([TALON](/xray-mp-wiki/reagents/additives/talon/) resin) | Not specified in supp info + -- | Deca-histidine tagged VpTrkH purified on cobalt affinity column |
| Tag cleavage | TEV protease digestion | — | Not specified in supp info + -- | Deca-histidine tag removed by TEV protease |
| Size-exclusion chromatography | Size-exclusion chromatography | Not specified | Not specified in supp info + -- | VpTrkH elutes as a single peak on gel filtration (see Supp Fig 2a) |

**Final sample**: Purified VpTrkH, confirmed as dimer by chemical crosslinking
**Yield**: --
**Purity**: >95% by SDS-PAGE


## Crystallization

### doi/10.1038##nature09731

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified VpTrkH (SeMet-labeled or native) |
| Temperature | Not specified |
| Notes | Crystals belong to space group P2(1)2(1)2(1). Four data sets: SeMet SAD (3.9 A), native K+ (3.5 A), native Ba2+ (4.2 A), native Rb+ (3.5 A). Data collected at APS. Structure solved by SeMet SAD phasing. Substrate ions (K+, Rb+, Ba2+) soaked or included in crystallization conditions. |


## Biological / Functional Insights

### First structure of a Trk family potassium channel

VpTrkH represents the first high-resolution crystal structure of a Trk family
potassium ion channel. The structure reveals a homodimeric architecture with
each protomer containing five domains (D0-D4). Domains D0-D3 each consist of
two transmembrane helices (M1-M2) forming a peripheral ring around the central
ion conduction pore formed by D4. The overall fold is distinct from other
potassium channels but the selectivity filter shares structural similarity with
[KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/).

### Selectivity filter architecture

The VpTrkH selectivity filter contains the conserved TVGYG sequence motif,
similar to [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) and other K+ channels. However, the pore helix dipole is
oriented differently compared to [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), with the positive end of the helix
dipole directed away from the selectivity filter rather than toward it. This
suggests that the mechanism of ion selectivity and conduction in [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) may
differ from canonical potassium channels. The electron density in the
selectivity filter reveals a single K+ ion binding site rather than the
multiple sites observed in [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/).

### Dimeric architecture and domain organization

VpTrkH forms a homodimer with each protomer comprising ~480 residues organized
into five domains (D0-D4). Domains D0-D3 form a peripheral collar surrounding
the central D4 pore domain. The D4 domain from each protomer contributes a
pore helix and selectivity filter. The dimer interface is formed primarily by
D4M1 and the D4 pore helix from both protomers, creating a hydrophobic seal
at the center of the dimer interface. An intramembrane loop between D3M2 and
D4M1 contains conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues and forms a constriction at the
permeation pathway.

### Ion permeation pathway

The ion conduction pathway of VpTrkH passes through the D4 pore domain, with
the selectivity filter at the extracellular side. The permeation pathway is
constricted at the intracellular side by an intramembrane loop, with Arg468
and Glu470 forming a narrow constriction. This constriction may regulate ion
access to the selectivity filter. The large central cavity is sealed off from
the lipid bilayer by hydrophobic residues at the dimer interface.

### Comparison with KcsA potassium channel

Despite sharing the TVGYG selectivity filter motif, VpTrkH and [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) have
markedly different overall architectures. [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) is a tetramer with each subunit
contributing one pore domain, while VpTrkH is a dimer with each protomer
contributing its own pore domain. The pore helix orientation differs between
the two channels, with the [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) pore helix dipole oriented away from the
selectivity filter. These differences suggest that [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) may utilize a distinct
mechanism for K+ selectivity and conduction compared to the canonical KcsA-like
channels.


## Cross-References

- [TrkH (Potassium Channel from Klebsiella pneumoniae)](/xray-mp-wiki/proteins/pumps-atpases/trkh/) — Homologous TrkH potassium channel from a different bacterial species; VpTrkH provides the first high-resolution structure defining the TrkH fold
- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — KcsA is the canonical potassium channel used for structural comparison of selectivity filter architecture
- [TrkA (ATP-binding Regulatory Subunit from Klebsiella pneumoniae)](/xray-mp-wiki/proteins/pumps-atpases/trka/) — TrkA is the cytoplasmic regulatory subunit that associates with TrkH to form the functional K+ transporter complex
- [Single-Wavelength Anomalous Diffraction](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Structure solved by SeMet SAD phasing (3.9 A SeMet data)
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Additive used in purification or crystallization buffers
- [TALON](/xray-mp-wiki/reagents/additives/talon/) — Additive used in purification or crystallization buffers
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Buffer component in purification or crystallization
