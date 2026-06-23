---
title: Bovine Urea Transporter B (UT-B)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [channel, transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1207362109]
verified: false
---

# Bovine Urea Transporter B (UT-B)

## Overview

Bovine UT-B is a mammalian urea transporter encoded by the SLC14A1 gene. It is a homotrimeric facilitative urea channel that mediates rapid passive diffusion of urea across cell membranes. UT-B is expressed in kidney vasa recta, erythrocytes, heart, colon, and brain, and plays a critical role in the urinary concentrating mechanism by preventing osmotic diuresis. The first X-ray crystal structure of a mammalian urea transporter was solved at 2.36 Å resolution, revealing a trimeric architecture with each protomer containing a urea conduction pore lined by a narrow selectivity filter with two urea-binding sites (So and Si) separated by a ~5.0 kcal/mol energy barrier at the Sm constriction site. UT-B function is modulated by hypoosmotic stress, with the Sm site serving as the site of osmoregulation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1207362109 | 4EZC | 2.36 | -- | Full-length bovine UT-B (AAI05334.1) with C-terminal TEV protease recognition site and octohistidine tag | Apo (substrate-free) |
| doi/10.1073##pnas.1207362109 | 4EZD | 2.5 | -- | Full-length bovine UT-B with C-terminal TEV-octohistidine tag | Selenourea (urea analog) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus system)
- **Construct**: Full-length bovine UT-B gene (AAI05334.1) subcloned into modified pFastBac Dual vector with C-terminal TEV protease recognition site and octohistidine tag
- **Notes**: Infected Sf9 cells harvested 48-60 h post-infection

### Purification Workflow

- **Expression system**: Sf9 insect cells
- **Expression construct**: C-terminal TEV-octohistidine tagged UT-B

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvesting and lysis | Baculovirus infection of Sf9 insect cells | — |  | Infected cells harvested 48-60 h post-infection |
| Affinity chromatography | Immobilized metal affinity chromatography (IMAC) | -- (octohistidine tag) |  | C-terminal octohistidine tag used for purification |
| Tag cleavage | TEV protease cleavage | — |  | TEV recognition site between UT-B and octohistidine tag |
| Size-exclusion chromatography | Gel filtration | — |  | Final polishing step |

**Final sample**: Purified UT-B in detergent solution
**Yield**: --
**Purity**: --


## Crystallization

### doi/10.1073##pnas.1207362109

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified bovine UT-B in detergent solution |
| Reservoir | -- |
| Mixing ratio | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Native UT-B crystals diffracted to 2.36 Å. Selenourea-bound crystals obtained by cocrystallization with 20 mM selenourea, diffracted to 2.5 Å. Data collected at selenium K-absorption edge for anomalous signal. |

| Parameter | Value |
|---|---|
| Method | Co-crystallization with selenourea |
| Protein sample | Bovine UT-B with 20 mM selenourea |
| Reservoir | -- |
| Mixing ratio | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Selenourea used as a urea analog that produces strong anomalous signal for unambiguous identification of binding sites |


## Biological / Functional Insights

### Trimeric architecture and pore structure

UT-B forms a homotrimer with each protomer containing an independent urea conduction pore. The pore is formed at the interface of two pseudo-symmetrical halves (TM1-5 and TM6-10), lined by conserved urea signature sequence residues. The selectivity filter contains three regions: So (rectangular, oxygen ladder), Si (rectangular, oxygen ladder), and Sm (constricted, hydrophobic region with pseudo-symmetry-related threonine residues T172 and T334).

### Two urea-binding sites with an energy barrier

The selectivity filter has two urea-binding sites (So and Si) separated by an approximately 5.0 kcal/mol energy barrier at the Sm site. So and Si sites contain oxygen ladders (arrays of carbonyl and side-chain oxygen atoms) that coordinate urea via hydrogen bonds. MD simulations show that urea molecules are partially hydrated in So and Si (1.5-2.0 hydrogen bonds with water) but become completely dehydrated at the Sm site, accounting for the energetic barrier.

### Osmoregulation at the Sm site

UT-B function is modulated by hypoosmotic stress. Oocyte uptake assays showed ~2-fold increase in urea uptake under hypotonic conditions. The T172S/T334S double mutant (conserving hydrogen bonding at the Sm site) had similar basal activity to wild-type but lacked the hypoosmotic response, demonstrating that the Sm site is the site of osmoregulation. The T334V mutant (removing hydrogen bond capacity) abolished urea transport, confirming the functional importance of the Sm site threonine residues.

### Comparison with bacterial dvUT

The mammalian UT-B structure is similar to the bacterial dvUT (Desulfovibrio vulgaris urea transporter) but with key differences. The largest difference is a phenylalanine-to-glycine mutation in the So site (position 230 in UT-B), compensated by a leucine residue on helix TM3a that takes the place of the aromatic ring. The N-terminal amphipathic helix orientation also differs, though this may be affected by crystal contacts in the bacterial structure.


## Cross-References

- [Urea Transporter from Desulfovibrio vulgaris (dvUT)](/xray-mp-wiki/proteins/other-ion-channels/urea-transporter-dvut/) — Bacterial homolog of mammalian UT-B; comparison of pore architecture and selectivity filter
- [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — Structural and mechanistic parallels between urea transporters and aquaporins (ar/R motif, Sm site analogy)
- [Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — The oxygen ladder and Sm site selectivity mechanism of UT-B is a key example of filter-based substrate discrimination
- [Channel-like Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/channel-like-mechanism/) — UT-B operates by a channel-like mechanism rather than alternating-access transport
