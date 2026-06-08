---
title: Fluoride Channel from E. coli (Ec2)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NATURE14981]
verified: false
---

# Fluoride Channel from E. coli (Ec2)

## Overview

The fluoride channel from Escherichia coli (Ec2) is a member of the Fluc family of fluoride-specific ion channels. Ec2 is a bacterial fluoride-exporting membrane protein that shares identical fold and dual-topology dimeric architecture with the Bordetella pertussis Fluc homologue (Bpe), despite only 33% sequence identity. Ec2 forms a double-barrelled channel with two F- permeation pathways and exhibits the same antiparallel transmembrane topology characteristic of the Fluc family. Ec2 was crystallized in complex with the monobody S9, providing structural confirmation of the conserved F- binding site across Fluc homologues.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NATURE14981 | 5A43 | 2.6 | P 41 | Ec2 fluoride channel homodimer from E. coli with monobody S9 bound to both ends | Monobody S9, Na+ (centrally coordinated in plug), F- (putative, at F1 sites) |

## Expression and Purification

- **Expression system**: Escherichia coli. Ec2 from E. coli was expressed with an N-terminal His3 tag that was left on for purification, as described in Stockbridge et al. 2013, 2014. The R25K expression-enhancing mutation was introduced, and for selenomethionine incorporation an additional methionine was introduced (A51M) to enhance phasing power.

- **Construct**: Ec2 fluoride channel homodimer from E. coli with N-terminal His3 tag, R25K mutation for enhanced expression, and A51M mutation for SeMet phasing.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression | -- | -- + -- | Ec2 expressed from E. coli with N-terminal His3 tag, R25K and A51M mutations |
| Purification | Affinity chromatography | TALON (via N-terminal His3 tag) | -- + -- | Purification as described in Stockbridge et al. 2013, 2014 |
| Size-exclusion chromatography | Size-exclusion chromatography | S200 SEC column | 100 mM NaF, 10 mM HEPES pH 7.0 + 5 mM n-decyl-beta-D-maltoside (DDM) | Final purification step, eluted in buffer containing 100 mM NaF for F- channel activity |


## Crystallization

### doi/10.1038##NATURE14981

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | Ec2-Fluc homodimer in detergent, co-complexed with monobody S9 |
| Reservoir | Not specified in detail |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Crystals grown from detergent micelles in the presence of F- (NaF). Structure solved using SAD phasing with selenomethionine-labelled protein. Space group P41. Diffraction to 2.6 Angstrom resolution. |


## Biological / Functional Insights

### Conserved F- binding site across Fluc homologues

The Ec2-S9 structure confirms that the F- binding sites identified in Bpe are conserved across the Fluc family. Two strong difference densities appear at precisely the same locations as the F1 ions in Bpe, coordinated identically. These sites are located in crevices between TM2, TM3b, and TM4 near the periphery of the channel, distant from the vestibules and the central Na+ plug. The conservation of these sites across homologues with only 33% sequence identity strengthens the assignment of these densities as F- ions.

### Dual-topology homodimer architecture

The Ec2 fold is identical to Bpe (C-alpha r.m.s.d., 0.6 Angstrom), with the inferred Na+ density appearing in equivalent locations. This confirms that the dual-topology dimeric architecture with a centrally coordinated cation in the plug region is a conserved feature of the Fluc family, not specific to Bpe.


## Cross-References

- [Fluoride Channel from B. pertussis (Bpe)](/xray-mp-wiki/proteins/bpe-fluoride-channel/) — Bpe is the closest Fluc homologue; identical fold with 33% sequence identity; both share dual-topology architecture
- [Monobody S9](/xray-mp-wiki/reagents/protein-tags/monobody-s9/) — Engineered protein inhibitor used to crystallize Ec2 (PDB 5A43)
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for Ec2 purification and crystallization (5 mM)
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in Ec2 purification and crystallization (10 mM, pH 7.0)
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — NaF used in Ec2 purification buffer (100 mM) for fluoride channel activity
- [Dual-Topology Channels](/xray-mp-wiki/concepts/dual-topology-channels/) — Ec2 is a dual-topology homodimer; Ec2-S9 structure confirms conserved dual-topology architecture
- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — SAD phasing with selenomethionine-labelled Ec2 used to solve the structure and avoid model bias
