---
title: GtACR1 Anion Channelrhodopsin from Guillardia theta
created: 2026-06-09
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.41741, doi/10.7554##eLife.65903]
verified: false
---

# GtACR1 Anion Channelrhodopsin from Guillardia theta

## Overview

GtACR1 is a natural light-gated anion channelrhodopsin from the cryptophyte alga Guillardia theta. It is the most potent neuron-silencing optogenetic tool available, exhibiting 25-fold higher unitary conductance than the cation channelrhodopsin CrChR2. The X-ray crystal structure of the dark (closed) state was determined at 2.9 A resolution (Li et al., 2019, PDB 6EDQ). The structure reveals a continuous intramolecular tunnel traversing the protein from the extracellular surface to a large cytoplasmic cavity, lined primarily by small polar and aliphatic residues essential for anion conductance. A disulfide-immobilized extracellular cap facilitates channel closing, and the ion path is blocked mid-membrane by the photoactive retinylidene chromophore. The structure also reveals a novel photoactive site configuration that maintains the retinylidene Schiff base protonated in the open-channel state, in contrast to cation channelrhodopsins where Schiff base deprotonation precedes channel opening. GtACR1 forms a disulfide-crosslinked homodimer stabilized by TM3 and TM4 interactions and an intermolecular C6-C6 disulfide bridge. The bromide-bound structure at 3.2 A resolution (Li et al., 2021, PDB 7L1E) revealed structural changes that relax the C1 and C3 tunnel constrictions, including a novel salt-bridge switch mechanism involving Arg94, providing direct evidence that the tunnel is the closed form of the channel and shedding light on the light-gated channel activation mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.41741 | 6EDQ | 2.9 A | P2(1)2(1)2 | GtACR1 from G. theta, residues 1-295, dark (closed) state | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) lipids |
| doi/10.7554##eLife.65903 | 7L1E | 3.2 A | P 2(1) | GtACR1 from G. theta, residues 1-295, bromide-bound pre-activated state | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), bromide ion |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: GtACR1 (GenBank KP171708, residues 1-295) with C-terminal His8 tag in pPIC9K

### Purification Workflow

*Source: doi/10.7554##eLife.41741*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and harvesting | Baculovirus expression in Sf9 cells | not applicable | 350 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 20 mM HEPES pH 7.5 (Buffer A) with 0.1 mM PMSF + not specified | Sf9 cells infected at ~2x10^6 cells/ml with GtACR1-encoding baculovirus at 15:1 (v/v); 5 uM all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) added; 3 days in spinner flasks at 27 C. Pink-colored cells harvested by centrifugation. |
| Cell lysis and membrane isolation | High-pressure homogenization and ultracentrifugation | not applicable | Buffer A (350 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 20 mM HEPES pH 7.5) with 0.1 mM PMSF + not specified | Cells ruptured by 3 passes through EmulsiFlex-C3 homogenizer; low-speed spin at 5000 rpm for 10 min to remove debris; membranes pelleted at 40,000 rpm for 1 hr in Ti45 rotor. |
| Membrane solubilization | Detergent solubilization | not applicable | Buffer A + 1% n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membranes suspended in Buffer A and solubilized with 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for 1 hr at 4 C with shaking; undissolved material removed by ultracentrifugation at 45,000 rpm for 1 hr. |
| Ni-NTA affinity chromatography | Immobilized metal ion affinity chromatography | Ni-NTA resin (Qiagen) | Buffer A with 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/); 15 mM and 40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) for washes; 400 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) for elution + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Supernatant supplemented with 15 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) incubated with Ni resin for 1 hr at 4 C; step-wise washes with 15 mM and 40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); eluted with 400 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in Buffer A + 0.03% DDM. |
| Size exclusion chromatography | Size exclusion chromatography | Superdex Increase 10/300 GL column (GE Healthcare) | Buffer B (350 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/)) + not specified | Eluted protein further purified on Superdex Increase 10/300 GL column equilibrated with Buffer B. |

### Purification Workflow

*Source: doi/10.7554##eLife.65903*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|


## Crystallization

### doi/10.7554##eLife.41741

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | GtACR1 in buffer, ~unknown concentration |
| Temperature | 100 K (data collection) |
| Growth time | not specified |
| Notes | Crystals grown in lipidic cubic phase (LCP). Continuous grid-scan method used for X-ray data collection at SLS X06SA-PXI beamline (Swiss Light Source). Four partial datasets merged to 2.9 A. Space group P2(1)2(1)2, cell dimensions a=77.79 A, b=149.55 A, c=62.41 A, alpha=beta=gamma=90 degrees. Data processed with XDS/XSCALE. Structure solved by molecular replacement using CrChR2 (PDB 6EID) as search model. |

### doi/10.7554##eLife.65903

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization in IMISX plates |
| Protein sample | GtACR1 in purification buffer (350 mM NaBr, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/)) |
| Temperature | 100 K (data collection) |
| Growth time | 1 month |
| Notes | LCP crystallization set up in IMISX glass plates to facilitate high-throughput data collection. Crystals harvested using micromesh loops and 3D-printed holders. Data collected by serial synchrotron crystallography at SLS X06SA-PXI beamline. 217 datasets collected using EIGER 16M detector; 31 IMISX and 5 loop-mounted datasets merged to 3.2 A. Space group P 2(1). Structure solved by molecular replacement using 6EDQ as search model. Rwork/Rfree = 0.24/0.29. |


## Biological / Functional Insights

### Anion conductance pathway architecture

The GtACR1 structure reveals a continuous tunnel traversing the protein from extracellular to cytoplasmic surface, assembled by TM1-3 and TM7. The tunnel is lined by small polar and aliphatic residues (A75, T71, S97) in contrast to charged residues at corresponding positions in cation channelrhodopsins C1C2 and CrChR2. Three constrictions (C1 at extracellular port, C2 near the Schiff base, C3 at cytoplasmic side) regulate anion flux. The C1 constriction is stabilized by an H-bond network involving Y81, R94 and E223.

### Disulfide-immobilized extracellular cap

An intramolecular disulfide bridge between C21 (N-terminal loop) and C219 (TM6-7 loop) immobilizes the extracellular cap domain, encapsulating a hydrophobic segment on the tunnel entry port. This disulfide is conserved in ACRs but absent in CCRs. Disruption by [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) (Delta1-25) or C21S/C219S mutations results in slowed channel closing, establishing the cap's role in gating kinetics.

### Protonated Schiff base in open-channel state

In GtACR1, the retinylidene Schiff base remains protonated throughout the lifetime of the open-channel state, with deprotonation correlated with the initial phase of channel closing (~20 ms). This is fundamentally different from cation channelrhodopsins where Schiff base deprotonation precedes channel opening. A triad of residues (E68, N259, S263, ENS) forms a hydrogen bond network that stabilizes the protonated Schiff base.

### Anion selectivity mechanism

Anion selectivity in GtACR1 is governed by pore-surface electrostatics. The tunnel is lined by small polar and aliphatic residues with sparse positive charges, creating an electropositive pathway that favors anion conduction. The R94A mutation nearly abolishes Cl- conductance. The retinylidene Schiff base itself serves not only as a gate but also as a direct mediator for anion flux.

### Dimeric architecture and cytoplasmic cavity

GtACR1 forms a disulfide-crosslinked homodimer stabilized by TM3 and TM4 interactions and a C6-C6 intermolecular disulfide bridge. The TM5-7 helices are longer than TM1-4, creating a large funnel-shaped cytoplasmic cavity (~18 A deep and ~28 A wide). Each protomer contains 7 transmembrane helices (TM1-7), an extracellular cap domain, and a C-terminal cytoplasmic loop.

### Conserved 7-TM scaffold of channelrhodopsins

Despite only ~24% sequence identity, each GtACR1 protomer superposes well with C1C2 and CrChR2 (RMSD ~0.9 A), indicating that functionally distinct channelrhodopsins share a common TM helical scaffold in their closed states. This conserved scaffold was used for molecular replacement phasing.

### Bromide binding reveals pre-activated state at C3 constriction

The bromide-bound GtACR1 structure (PDB 7L1E, 3.2 A) reveals a bromide ion bound at the cytoplasmic port of the transmembrane tunnel, stabilized by H-bond interactions with Trp250 and Pro58. Bromide binding pushes Pro58 outward by ~1.8 A, widening the C3 constriction by ~1 A in diameter. This demonstrates that substrate binding induces a transition from an inactivated state to a pre-activated state in the dark that facilitates channel opening by reducing free energy in the tunnel constrictions. The data provide direct evidence that the tunnel is the closed form of the channel.

### Salt-bridge switch mechanism at C1 constriction

In chain A of the bromide-bound structure, Arg94 at the C1 constriction undergoes a ~180 degree side-chain rotation, switching from a salt-bridge with Glu223 (apo form conformation) to an alternative salt-bridge with Asp234 near the photoactive site. This rotation widens the C1 constriction by ~1 A and creates a conformation similar to the chloride-binding site of the CIR chloride pump (PDB 5G2A, Arg95). Chain B retains the apo-form Arg94 conformation, demonstrating intrinsic flexibility of the C1 constriction between protomers.

### Larger bromide conductance explained by tunnel widening

The conformational changes induced by bromide binding expand the tunnel in both C1 and C3 constrictions, while C2 remains the narrowest constriction due to the trans-configured [Retinal](/xray-mp-wiki/reagents/ligands/retinal/). This pre-activating conformational change reduces the free energy barrier for channel opening, consistent with GtACR1 exhibiting larger conductance for bromide than chloride. FTIR data confirm that bromide binding alters the electron conjugation of the retinylidene polyene chain in the dark state without perturbing the all-trans to 13-cis photoisomerization.


## Cross-References

- [Channelrhodopsin C1C2 Chimera](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — Closely related cation channelrhodopsin chimera used for structural comparison
- [iC++ Designed Anion Channelrhodopsin](/xray-mp-wiki/proteins/rhodopsins/ic-plus-plus/) — Designed ACR created by structure-guided engineering for comparison with natural ACR GtACR1
- [Channelrhodopsin Photocycle](/xray-mp-wiki/concepts/transport-mechanisms/channelrhodopsin-photocycle/) — GtACR1 exhibits a distinct photocycle mechanism with protonated Schiff base in open state
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — GtACR1 structure determined by LCP crystallization method
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for GtACR1 purification and solubilization
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Referenced in gtacr1 text
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Referenced in gtacr1 text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in gtacr1 text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in gtacr1 text
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in gtacr1 text
