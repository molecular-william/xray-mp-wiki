---
title: "EmrD Multidrug MFS Transporter from Escherichia coli"
created: 2026-06-21
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1125629]
verified: false
---

# EmrD Multidrug MFS Transporter from Escherichia coli

## Overview

EmrD is a multidrug resistance (MDR) Major Facilitator Superfamily (MFS)
transporter from Escherichia coli. It functions as a drug/H+ antiporter
(DHA12 subfamily) that exports a broad spectrum of hydrophobic compounds,
including the protonophore CCCP (carbonyl cyanide
m-chlorophenylhydrazone) and detergents such as benzalkonium and sodium
dodecylsulfate. The 3.5 A crystal structure reveals 12 transmembrane
helices forming a compact structure with a hydrophobic internal cavity,
consistent with its role in transporting lipophilic compounds. Unlike the
V-shaped inward-open conformations of LacY and GlpT, EmrD adopts an
intermediate state conformation with a hydrophobic interior lined by
bulky aromatic residues. A cytoplasmic selectivity filter region (H4,
L4-5, H5 and H10, L10-11, H11) provides additional substrate
specificity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1125629 | 2GFP | 3.5 | Not specified in raw paper | Full-length EmrD (394 residues, ~42.2 kDa) | No bound ligand/substrate in structure |

## Expression and Purification

- **Expression system**: E. coli (recombinant)
- **Construct**: Full-length EmrD

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Full-length EmrD

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | Not specified in detail | — | beta-Dodecyl-maltoside | Crystals grown in presence of beta-D-maltoside (DDM) |


## Crystallization

### doi/10.1126##science.1125629

| Parameter | Value |
|---|---|
| Method | Not specified in detail |
| Protein sample | Purified EmrD in beta-D-maltoside |
| Notes | Crystals grown in presence of beta-dodecyl-maltoside. Gold thiomalate derivative used for phasing. |


## Biological / Functional Insights

### Hydrophobic internal cavity for multidrug recognition

Unlike LacY and GlpT, which have hydrophilic interiors, EmrD's
internal cavity comprises mostly hydrophobic residues, consistent
with its function of transporting lipophilic compounds. Key
hydrophobic residues include Ile28, Ile217, Ile253, Tyr52, Tyr56,
Trp300, and Phe249. Two pairs of stacked aromatic groups
(Tyr52/Tyr56 and Trp300/Phe249) may play a key role in multisubstrate
binding through stacking interactions with aromatic drugs.

### Intermediate conformational state

Unlike the V-shaped inward-open conformations of LacY and GlpT, EmrD
is not in a V shape and probably represents an intermediate state.
The periplasmic loops are more imbedded in the cell membrane, and the
central loop L6-7 is considerably shorter. This structural arrangement
may reflect a general architecture of MDR MFS transporters.

### Cytoplasmic selectivity filter

Two long helical regions (H4, L4-5, H5 and H10, L10-11, H11) are
arranged much closer to the central cavity and extend farther into
the cytoplasm than in LacY and GlpT. The cytoplasmic end of H4
contains charged residues (Arg118, Arg122, Asp123, Glu126, Arg127,
Arg131) that may play a role in defining transporter topology and
substrate recognition. Functional studies of the EmrD homolog MdfA
indicate that several residues in this region are important for
substrate recognition.

### Dual location model for proton and drug translocation

Based on the structure, proton translocation and drug transport may
occur at different locations in EmrD. The periplasmic side contains
Thr25, Asp33, and Glu227 that could reorient into the cavity during
the transport cycle and participate in H+ translocation. This dual
location model has also been proposed for MdfA.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — EmrD is a DHA12 drug efflux subfamily member of the MFS with MDR-specific features
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — EmrD likely uses a rocker-switch mechanism for alternating access during drug/H+ antiport
- [AcrB Multidrug Efflux Transporter (E. coli)](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Another E. coli multidrug efflux system; EmrD represents the MFS-based mechanism distinct from RND-type efflux
- [n-Dodecyl-beta-D-Maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for EmrD purification and crystallization
