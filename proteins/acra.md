---
title: AcrA multidrug efflux pump periplasmic protein
created: 2026-05-28
updated: 2026-05-28
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1016##j.str.2005.11.015]
verified: false
---

# AcrA multidrug efflux pump periplasmic protein

## Overview

AcrA is a periplasmic membrane fusion protein from Escherichia coli that partners with the inner membrane RND transporter AcrB and the outer membrane channel TolC to form the AcrAB-TolC tripartite multidrug efflux system. The crystal structure of the stable core construct AcrA(45-312) with quadruple methionine substitution was determined at 2.71 A resolution by multi-wavelength anomalous diffraction (MAD). AcrA adopts an elongated sickle-shaped monomer composed of three domains: a beta-barrel domain, a lipoyl domain, and an alpha-helical hairpin domain. The alpha-helical hairpin exhibits unsuspected conformational flexibility with four distinct orientations captured in the crystal, which has mechanistic significance for coupling AcrA conformations to TolC channel opening.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2005.11.015 | 2HJ9 | 2.71 A | C222 | AcrA(45-312) quadruple methionine mutant (F223M/L224M/L287M/L288M) | None |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: AcrA(26-397) with C-terminal His tag (LEHHHHHH), or AcrA(45-312) with quadruple methionine substitution (F223M/L224M/L287M/L288M)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication of E. coli BL21(DE3) cells expressing AcrA(26-397) | -- | 50 mM Tris-HCl (pH 8.0), 150 mM NaCl, 10 mM imidazole + -- | Cytoplasmic expression of soluble AcrA fragment |
| Ni-NTA affinity chromatography | Ni2+ chelation chromatography | Poros MC (Ni-NTA) | 50 mM Tris-HCl (pH 8.0), 150 mM NaCl, 10 mM imidazole + -- | His-tagged AcrA purified from soluble fraction |
| Dialysis and concentration | Dialysis and Amicon ultrafiltration | -- | 50 mM Tris (pH 8.0), 150 mM NaCl + -- | Concentrated using Amicon ultrafiltration (MW cutoff 30 kDa; Millipore) |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 | 10 mM Tris (pH 8.0) + -- | Purified to homogeneity, concentrated to 30 mg/mL |


## Crystallization

### doi/10.1016##j.str.2005.11.015

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 30 mg/mL AcrA(45-312)-4M in 10 mM Tris (pH 8.0) |
| Reservoir | 30% MPD, 20 mM MgCl2, 100 mM citrate (pH 5.4), 1 mM TCEP |
| Temperature | 4 C |
| Growth time | not specified |
| Cryoprotection | Well buffer supplemented with 1 mM TCEP, flash cooled in liquid nitrogen |
| Notes | Space group C222, cell dimensions a=88.7 A, b=100.0 A, c=332.6 A. Four molecules per asymmetric unit, 60% solvent content. Data collected at APS-BM19 and ALS-8.2.2 beamlines. Multi-wavelength MAD phasing with selenomethionine-labeled protein. 16 Se sites located with SHELXL, refined with SHARP. R_work 23.7%, R_free 27.5% at 2.71 A resolution. |


## Biological / Functional Insights

### Conformational flexibility of the alpha-helical hairpin domain

Four distinct conformations of AcrA(45-312)-4M were captured in the crystal, providing
evidence for flexibility of the hinge between the alpha-helical hairpin and lipoyl
domain. The greatest variation is between molecules B and C, which differ by ~15 degrees
overall in alpha-helical hairpin orientation and by 21 A at the loop at the tip of
the hairpin. The lipoyl domain superposes with high structural similarity in all four
molecules (rmsd 0.12 A, 66 C-alpha atoms). The alpha-helical hairpin domains alone
also show similarity (rmsd 0.46 A, 51 C-alpha atoms).

The hinge is located at the base of the hairpin, composed of residues 99-106 in helix
1 and residues 169-173 in helix 2. In molecules A and C, this region is underwound,
having a ~200 A pitch that is greater than the 150 A pitch of a canonical alpha-helical
coiled-coil. In molecules B and D, the hinge regions have a nearly canonical coiled-coil
pitch. This flexibility coincides with conformational changes predicted to occur during
opening of the TolC channel by an iris-like mechanism.

In contrast, the homologous protein MexA from Pseudomonas aeruginosa shows essentially
the same conformation in all 13 copies captured in its crystal structure (maximum rmsd
1.17 A, 230 C-alpha atoms). Molecule D of AcrA has nearly the same alpha-helical hairpin
orientation as the one seen in MexA (rmsd 0.85 A, 183 C-alpha atoms).

### Oligomeric state and crystal packing

The four molecules of AcrA(45-312)-4M in the asymmetric unit pack as an apparent
dimer of dimers. Molecules A and B are related by approximate dyad symmetry, as are
molecules C and D; each set of dimers is related by another approximate 2-fold axis.
The alpha-helical hairpin of AcrA has five heptad repeats per helix, longer than the
four heptad repeats of MexA. Packing between the two helices resembles canonical knobs-into-holes
packing of hydrophobic side chains in the a and d positions of the heptad repeat.

In addition to parallel associations, extensive antiparallel associations are observed
in the crystallographic packing. For antiparallel association, adjacent equivalent helices
(alpha1 for MexA and alpha2 for AcrA) pack in antiparallel fashion and contribute residues
predominantly at the c and f positions to the interface. This suggests that the propensity
of MFP alpha-helical hairpins to interact homotypically reconciles the observation that
MFPs are monomeric in solution but oligomeric in the high-concentration environment
of crystals.

### Functional residues and interaction domains

The C-terminal region (residues 313-397) of AcrA, removed by proteolysis in the crystallized
construct, is required for association with both the inner membrane RND protein AcrB
and the outer membrane channel TolC. The proteolytically sensitive C-terminal region
is also implicated in conferring association with AcrB.

The beta-barrel domain of AcrA has also been implicated in TolC association, based on
suppressor mutations that restore function in a TolC mutant strain. The stoichiometry
of AcrA remains uncertain, with a trimeric form found in vivo but a monomeric form
in vitro.

Site-directed mutagenesis of hydrophobic residues in the alpha-helical hairpin (F223M/L224M
and L287M/L288M) significantly increased susceptibility to multiple antibiotics and
detergents (erythromycin, novobiocin, ethidium bromide, SDS, puromycin), confirming
that these positions are critical for AcrA function in the efflux system.


## Cross-References

- [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/acrB/) — Inner membrane RND partner in the AcrAB-TolC tripartite efflux system
- [MexB Efflux Pump](/xray-mp-wiki/proteins/mexB/) — P. aeruginosa RND inner membrane partner of MexA, homologous to AcrB
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Used for MAD phasing via selenomethionine labeling of quadruple methionine mutant
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer (50 mM Tris pH 8.0) used in expression, purification, and crystallization
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/mgcl2/) — 20 mM MgCl2 component of crystallization reservoir
- [Citrate Buffer](/xray-mp-wiki/reagents/buffers/citrate/) — 100 mM citrate (pH 5.4) component of crystallization reservoir
- [2-Methyl-2,4-pentanediol (MPD)](/xray-mp-wiki/reagents/additives/mpd/) — 30% MPD used as precipitant in crystallization
- [Thermolysin](/xray-mp-wiki/reagents/additives/thermolysin/) — Used for limited proteolytic digestion to map AcrA domain architecture
