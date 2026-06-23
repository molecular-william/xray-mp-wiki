---
title: Urea Transporter from Desulfovibrio vulgaris (dvUT)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08558]
verified: false
---

# Urea Transporter from Desulfovibrio vulgaris (dvUT)

## Overview

The [UREA](/xray-mp-wiki/reagents/substrates/urea) transporter from *Desulfovibrio vulgaris* (dvUT) is a bacterial
homologue of mammalian [UREA](/xray-mp-wiki/reagents/substrates/urea) transporters (UTs). It forms a homotrimeric
channel that facilitates rapid and selective [UREA](/xray-mp-wiki/reagents/substrates/urea) permeation across
biological membranes. Each subunit contains a continuous membrane-spanning
pore with a constricted selectivity filter that coordinates dehydrated [UREA](/xray-mp-wiki/reagents/substrates/urea)
molecules through hydrogen bonding with oxygen ladder residues. The structure
establishes that [UREA](/xray-mp-wiki/reagents/substrates/urea) transporters operate by a channel-like mechanism rather
than a carrier-mediated alternating-access mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature08558 | 3B6R | 2.3 | P65 | Full-length dvUT (residues 1-334) with N-terminal His6-SUMO tag | N,N'-dimethylurea (DMU) |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: N-terminal His6-SUMO-dvUT fusion (Smt3 system)
- **Notes**: Expressed using pET-SUMO plasmid with N-terminal polyhistidine tag and SUMO domain. Solubilized with 30 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm).

### Purification Workflow

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: His6-SUMO-dvUT fusion

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and solubilization | Cell disruption | — | 30 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Cells resuspended and solubilized in 30 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| Cobalt affinity chromatography | IMAC | Cobalt affinity column (Clontech) | 30 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm) | [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) captured on cobalt column |
| Tag cleavage | Proteolytic cleavage | — |  | His tag and SUMO domain cleaved with SUMO protease |
| Size-exclusion chromatography | Gel filtration | Superdex 200 10/300 GL | 300 mM NaCl, 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) + 40 mM [OM](/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-maltoside) (OM) |  |


## Crystallization

### doi/10.1038##nature08558

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 8 mg/ml in 300 mM NaCl, 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol), 40 mM OM |
| Reservoir | 22% [PEG](/xray-mp-wiki/reagents/additives/peg)1500, 100 mM sodium [Cacodylate (Sodium Dimethylarsenate)](/xray-mp-wiki/reagents/buffers/cacodylate) pH 6.5 |
| Mixing ratio | 61 |
| Temperature | 20 C |
| Cryoprotection | Gradually increased [PEG](/xray-mp-wiki/reagents/additives/peg)1500 to 45% over 30 h |
| Notes | Native crystals in P31 space group (3.8 A). Heavy atom derivatives (Hg, Au) in P65 space group with improved resolution to 2.3 A. DMU-bound crystals obtained by incubating protein with 10 mM DMU at 20 C for 30 min before crystallization. |


## Biological / Functional Insights

### Channel-like mechanism of urea transport

The dvUT structure reveals a continuous solvent-accessible pore running
through each subunit, demonstrating that [UREA](/xray-mp-wiki/reagents/substrates/urea) transporters operate by a
channel-like mechanism rather than a carrier-mediated alternating-access
mechanism. The pore allows dehydrated [UREA](/xray-mp-wiki/reagents/substrates/urea) molecules to permeate in
single file at rates between 10^4 and 10^6 s^-1, consistent with channel
diffusion. This finding resolves a long-standing question about how UTs
achieve rapid and selective [UREA](/xray-mp-wiki/reagents/substrates/urea) permeation.

### Oxygen ladder selectivity filter

The selectivity filter of dvUT contains two linear arrays of oxygen atoms
(oxygen ladders) from backbone and side-chain oxygens of residues in
pore helices (Pa, Pb) and transmembrane helices T3 and T5. These oxygen
ladders provide continuous hydrogen-bond coordination to [UREA](/xray-mp-wiki/reagents/substrates/urea) as it
progresses through the filter, compensating for dehydration energy. The
filter is flanked by phenylalanine side chains that compress it into a
slot-like shape, and valine/leucine residues create a central constriction.
The symmetry of the filter is remarkable: with one exception (Gln24/Glu187
pair), every residue has an identical symmetry-related partner.

### Helix dipole stabilization of urea binding

The alpha-helix dipole of pore helix b (Pb) provides additional
stabilization for [UREA](/xray-mp-wiki/reagents/substrates/urea) binding. The partial negative charge at the C
terminus of the helix compensates for the partial positive charge on [UREA](/xray-mp-wiki/reagents/substrates/urea)
amide nitrogens. This mechanism, previously noted in potassium channels
and chloride transporters, represents a general principle for stabilizing
polar substrates within membrane protein pores.


## Cross-References

- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/) — Related maltoside/glucoside detergent used for membrane protein solubilization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Another nonionic detergent used for solubilizing membrane proteins
- [Urea](/xray-mp-wiki/reagents/additives/urea/) — Substrate and ligand of the urea transporter
- [N,N'-Dimethylurea (DMU)](/xray-mp-wiki/reagents/ligands/n-n-dimethylurea/) — Urea analogue used in structural studies of dvUT
- [SUMO Tag](/xray-mp-wiki/reagents/protein-tags/sumo-tag/) — N-terminal fusion tag used in the dvUT expression construct
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer component (20 mM, pH 7.5) used in purification and crystallization
- [Cacodylate Buffer](/xray-mp-wiki/reagents/buffers/cacodylate/) — Buffer (100 mM, pH 6.5) used in crystallization reservoir
- [Channel-like Mechanism](/xray-mp-wiki/concepts/channel-like-mechanism/) — Transport mechanism established by the dvUT structure
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) — Entity mentioned in text
- [PEG](/xray-mp-wiki/reagents/additives/peg) — Entity mentioned in text
