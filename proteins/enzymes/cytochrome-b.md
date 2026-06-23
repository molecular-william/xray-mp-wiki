---
title: "Cytochrome b (EcHyd-1 Partner)"
created: 2026-05-28
updated: 2026-05-28
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2012.11.010]
verified: false
---

# Cytochrome b (EcHyd-1 Partner)

## Overview

Cytochrome b is the physiological partner of Escherichia coli Hydrogenase 1 (EcHyd-1). It serves primarily as a membrane anchor for the hydrogenase complex and participates in the electron-transfer pathway. The structure of the EcHyd-1-cytochrome b complex was solved at 3.3 A resolution, revealing approximately 6,800 A2 of buried surface area between the two proteins. The proximal [HEME](/xray-mp-wiki/reagents/ligands/heme) of cytochrome b is connected to the distal [Fe4S4] cluster of the hydrogenase S subunit via a 5 A pathway.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2012.11.010 | 4GD3 | 3.3 | P212121 | Cytochrome b subunit in complex with EcHyd-1 (SL)2 dimer | Proximal heme (single Fe atom per cytochrome b) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Native cytochrome b (B subunit) associated with EcHyd-1

### Purification Workflow

- **Expression system**: Escherichia coli

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Co-purification with EcHyd-1 | Detergent solubilization and SEC | Superdex 200 | 0.02% Triton X-100 + 0.02% Triton X-100 | Cytochrome b co-eluted with EcHyd-1 in the second peak; homogenizer treatment dissociates cytochrome b from EcHyd-1 |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Membrane anchoring role

The main role of cytochrome b in the EcHyd-1 complex is to anchor the
hydrogenase to the membrane rather than sending electrons to the respiratory
chain. The mainly hydrophobic interaction between one S subunit C-terminal
alpha helix and the cytochrome is very similar to the one observed in
formate dehydrogenase-N (EcFDH-N).

### Electron transfer to proximal heme

The histidine ligand of the distal [Fe4S4] cluster and one of the
carboxylate groups of the proximal heme are separated by about 5 A.
It is possible to partially reduce the cytochrome with H2, which implies
a viable electron-transfer pathway from the H2ase distal [Fe4S4] cluster
to the proximal heme. The cytochrome becomes oxidized under air and can
be partially reduced again by H2.

### Extensive interaction surface

About 6,800 A2 of the cytochrome b surface is buried in the [B(SL)2]2
complex. This value is much higher than those obtained for a symmetrical
(BSL)2 structure, explaining the stability of the crystallized complex.
The interface between the two proteins contains numerous conserved residues
and shows extensive charge and shape complementarity.


## Cross-References

- [Escherichia coli Hydrogenase 1 (EcHyd-1)](/xray-mp-wiki/proteins/enzymes/ec-hyd-1/) — Forms 2:1 complex; cytochrome b is the physiological partner
- [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/) — Related cytochrome with similar heme-containing electron transfer function
- [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100/) — Detergent used for co-purification of the complex
- [Heme](/xray-mp-wiki/reagents/ligands/heme/) — Proximal heme cofactor in cytochrome b
