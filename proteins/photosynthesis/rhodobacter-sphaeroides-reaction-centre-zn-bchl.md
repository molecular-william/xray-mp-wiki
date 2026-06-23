---
title: Rhodobacter sphaeroides Reaction Centre with Zinc-Bacteriochlorophyll
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.bbabio.2013.11.015]
verified: false
---

# Rhodobacter sphaeroides Reaction Centre with Zinc-Bacteriochlorophyll

## Overview

The Zn-BChl-containing reaction center (RC) from Rhodobacter sphaeroides, produced in a bchD (magnesium chelatase) mutant, assembles with six Zn-bacteriochlorophylls replacing all native Mg-containing bacteriochlorophylls and bacteriopheophytins. This engineered system provides unique opportunities for studying how metal coordination state and coordination geometry affect biological electron transfer. The first crystal structures of Zn-BChl-containing RCs were solved at 2.85 A resolution, revealing partial occupancy and disorder in the H_B cofactor pocket.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.bbabio.2013.11.015 | 4N7K | 2.85 A | P43212 | Wild-type RC with six Zn-bacteriochlorophylls replacing all native BChls and BPhes | Zn-[Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) |
| doi/10.1016##j.bbabio.2013.11.015 | 4N7L | 2.85 A | P43212 | RC with (M)L214H mutation; five-coordinate H_A Zn-BChl coordinated by His(M)214 | Zn-[Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/), His(M)214 |

## Expression and Purification

- **Expression system**: Rhodobacter sphaeroides bchD (magnesium chelatase) mutant
- **Construct**: Native RC assembled with Zn-bacteriochlorophylls instead of Mg-bacteriochlorophylls and bacteriopheophytins; no affinity tags

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Crude membrane preparation | Cell lysis and differential centrifugation | -- | -- + -- | Crude membranes isolated from Rhodobacter sphaeroides bchD mutant; detailed protocol in Saer et al. (2009) [9] and Saer et al. (2012) [20] |
| RC solubilization and purification | Detergent solubilization and chromatography | -- | -- + -- | RC solubilized from membranes using detergent; further purification details and chromatography conditions not described in this paper — refer to Saer et al. [9,20] |


## Crystallization

### doi/10.1016##j.bbabio.2013.11.015

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | Zn-BChl-containing reaction center purified as described in Saer et al. [9,20] |
| Reservoir | Not specified in this paper; see Saer et al. [20] for detailed hanging drop crystallization protocol |
| Temperature | Not specified in this paper |
| Growth time | Not specified in this paper |
| Cryoprotection | Not specified in this paper |
| Notes | Crystals isomorphous with wild-type RC (PDB 2J8C). Data collected at Stanford Synchrotron Light Source (SSRL) beamline 7.1 at wavelength 1.12709 A. Initial phases obtained from 2J8C by removing Mg2+ ions; for Zn-β-RC, side chain atoms of (M)214 were also modified. Refinement performed with Refmac5 and Coot. Zn-BChl modeled at P, B, and H cofactor sites in both A and B branches based on Fo-Fc and anomalous difference maps. |


## Biological / Functional Insights

### 4-coordinate Zn-BChl at H_A exhibits BPhe-like electron transfer kinetics

The 4-coordinate Zn-BChl at the H_A site in the Zn-RC functions kinetically more like a [Bacteriopheophytin](/xray-mp-wiki/reagents/cofactors/bacteriopheophytin/) (BPhe) than a 5-coordinate [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/). The electron transfer from H_A to Q_A proceeds with a time constant of 290 ps, compared to 210 ps in the wild-type RC. This is consistent with the Q_x transition absorption spectrum of the 4-coordinate Zn-BChl being similar to BPhe.

### Histidine coordination at H_A slows electron transfer and reduces charge separation yield

Coordination of the Zn2+ ion at H_A by a fifth ligand (His from the M214H mutation) results in a larger decrease in electron transfer rate (640 ps in Zn-β-RC vs. 290 ps in Zn-RC) and significantly reduces charge separation yield to 10% (vs. 74% in Zn-RC). The 5-coordinate Zn-BChl behaves differently from the 4-coordinate form, demonstrating that coordination geometry is a key determinant of electron transfer efficiency.

### H_B cofactor pocket shows partial occupancy and structural disorder

Crystal structures reveal that the Zn-BChl in the H_B pocket is bound at less than full occupancy or is highly disordered in both Zn-RC and Zn-β-RC. This is evidenced by weaker density in omit difference maps, large B-factors for the Zn2+ in the H_B pocket, and low anomalous signal intensities. This disorder likely explains the absence of a Q_x transition H_B absorption peak in the spectra.

### Zn2+ ion confers resistance to dechelation compared to Mg2+

The Zn2+ ion is more tightly bound to the bacteriochlorin macrocycle than Mg2+, making Zn-BChl resistant to the dechelation mechanism that converts BChl to BPhe in wild-type RCs. This explains why the H_A Zn-BChl is not converted to BPhe even in the absence of a fifth ligand, unlike the Mg2+ in wild-type BChl which can be dechelated.

### RC protein structure is rigid despite cofactor absence at H_B

The B-factors for protein residues surrounding the H_B Zn-BChl are comparable to the average B-factor of the structure, indicating the RC is a relatively rigid protein that does not rearrange its folding due to changes in cofactor composition or even when a cavity is created by the lack of a cofactor at H_B.

### Charge separation yields are lower in all Zn-RC variants compared to wild-type

All mutant RCs show lower P+QA- yields than wild-type on the nanosecond time scale. The Zn-RC retains 74% of the P+QA- bleaching amplitude (vs. wild-type at ~100%), while WT-β-RC and Zn-β-RC retain only 14% and 10% respectively. Charge recombination from P+I_A- occurs with a calculated lifetime of 1.1 ns in the Zn-RC, compared to 20 ns in wild-type RC with QA removed.


## Cross-References

- [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) — Primary cofactor in the reaction center; Zn-substituted in this variant
- [Bacteriopheophytin](/xray-mp-wiki/reagents/ligands/bacteriopheophytin/) — Native H_A and H_B cofactors replaced by Zn-BChl in this variant
- [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) — Native electron acceptor Q_A and Q_B in the reaction center
- [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) — Native antenna and photoprotective cofactors in the reaction center
- [Rhodobacter sphaeroides Reaction Centre with Zinc-Bacteriochlorophyll](/xray-mp-wiki/proteins/photosynthesis/rhodobacter-sphaeroides-reaction-centre-zn-bchl/) — This protein entity
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Related purple bacterial membrane protein with retinal chromophore
- [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) — Related membrane protein structural biology and crystallography methods
- [Rps. viridis Photosynthetic Reaction Centre](/xray-mp-wiki/proteins/photosynthesis/rps-viridis-reaction-centre/) — Related photosynthetic reaction centre structure from a different purple bacterium
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Alternative membrane protein crystallization method relevant to RC structural studies
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Method used in structure determination or purification
