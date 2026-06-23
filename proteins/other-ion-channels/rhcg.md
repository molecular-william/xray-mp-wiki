---
title: "Human Rhesus C Glycoprotein (RhCG)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1003587107]
verified: false
---

# Human Rhesus C Glycoprotein (RhCG)

## Overview

RhCG (Rhesus C glycoprotein) is a human ammonia channel belonging to the Rh family of proteins. It forms a homotrimeric complex that plays an essential role in ammonia excretion and renal pH regulation. Each monomer contains 12 transmembrane helices, one more than bacterial homologs. The X-ray structure of human RhCG determined at 2.1 Å resolution reveals the mechanism of ammonia transport. RhCG conducts NH3 through a hydrophobic channel lumen featuring twin coplanar histidines (H185 and H344) that facilitate substrate passage. A unique feature not present in Amt proteins is a lateral "shunt" pocket extending from the cytosolic aperture to the membrane hydrocarbon region.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1003587107 | 3HD6 | 2.1 A | -- | Human RhCG expressed in HEK293S cells | -- |

## Expression and Purification

- **Expression system**: HEK293S (Mammalian)
- **Construct**: Full-length human RhCG with [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/)
- **Notes**: Expressed using tetracycline-inducible system (Reeves et al., 2002). Predicted mass 55.163 kDa, measured 55.1+/-0.1 kDa by MALDI mass spectroscopy, confirming singly glycosylated species.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| FLAG affinity purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | FLAG affinity resin | -- + -- | RhCG purified using FLAG affinity tag |
| Size-exclusion chromatography | SEC | -- | -- + -- | Purified by SEC after FLAG affinity |


## Crystallization

### doi/10.1073##pnas.1003587107

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified RhCG |
| Reservoir | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | Cryoprotected crystals |
| Notes | Crystals grown by vapor diffusion. Data collected at beamline 8.3.1 of the Advanced Light Source (Lawrence Berkeley National Laboratories). |


## Biological / Functional Insights

### NH3 transport mechanism

RhCG conducts NH3 through a hydrophobic channel lumen. Conserved features include acidic residues lining the channel apertures (E166, D218, D278, E329) that attract NH4+, a largely hydrophobic lumen that excludes NH4+ and facilitates passage of neutral NH3, and twin coplanar histidines (H185 and H344) in the center of the channel that are essential for optimal NH3 permeation. The absence of ordered water molecules in the hydrophobic lumen further supports exclusion of charged NH4+.

### Phe gate and extracellular aperture

The extracellular pore is gated by phenylalanines F130 and F235. Unlike Amt proteins where F130 obstructs the pore, in RhCG, F130 is locked in an open conformation by interactions with D129, which is hydrogen-bonded to Y254 of an adjacent monomer and H67. This restricts F130 mobility, keeping the gate constitutively open. F235 retains freedom of motion, and mutation to valine reduces NH3 transport.

### The RhCG shunt

A unique feature of RhCG not present in Amt proteins is a lateral pocket termed the "shunt" extending from the cytosolic aperture to the membrane hydrocarbon region. This shunt is lined by residues conserved among human Rh glycoproteins and is also present in NeRh, suggesting it is common to the Rh subfamily. The cytosolic aperture features an acidic residue E329 that may recruit charged NH4+.

### Renal pH regulation model

In kidney epithelial cells, RhCG is expressed on both apical and basal surfaces of acid-secreting intercalated cells. NH3 transport through RhCG is driven by the progressively lowered pH from interstitium to epithelial cell cytosol to urinary space. Urinary acidification by V-type H+-ATPase and H+/K+-ATPase shifts the NH4+/NH3 equilibrium, trapping NH4+ in urine (up to 200 mM) while maintaining low intracellular NH4+ (~8 mM), enabling net NH4+ excretion essential for acid-base homeostasis.


## Cross-References

- [Ammonium Transporter AmtB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/amt-b/) — RhCG is structurally and functionally related to AmtB; both are trimeric ammonia channels with conserved twin-His motifs
- [Rh/Amt/MEP Protein Family](/xray-mp-wiki/concepts/protein-families/rh-amt-mep-protein-family/) — RhCG is a member of the Rh family within the broader Rh/Amt/MEP superfamily
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) — Fusion tag for crystallization or purification
