---
title: Chicken Kir2.2 Inward Rectifier K+ Channel
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, potassium-channel]
sources: [doi/10.1126##science.1180310, doi/10.1038##nature10370, doi/10.1085##jgp.201611616]
verified: false
---

# Chicken Kir2.2 Inward Rectifier K+ Channel

## Overview

Chicken Kir2.2 (cKir2.2) is a classical inward rectifier potassium channel whose gating is controlled by plasma membrane lipids. The first atomic structure of a eukaryotic Kir channel was determined by X-ray crystallography at 3.1 A resolution (Science 2009), revealing the TXGYGFR selectivity filter stabilized by disulfide bridges and salt bridges, multiple ion binding sites on the intracellular side of the filter that explain voltage-dependent block by multivalent cations, and distinctive turrets on the extracellular surface accounting for toxin insensitivity. Phosphatidylinositol-4,5-bisphosphate (PIP2) is the primary agonist for Kir2 channels, through which this lipid can regulate a cell's resting membrane potential. Subsequent PIP2-bound structures revealed that PIP2 binds at an interface between the transmembrane domain (TMD) and the cytoplasmic domain (CTD). On PIP2 binding, a flexible expansion linker contracts to a compact helical structure, the CTD translates 6 A and becomes tethered to the TMD, and the inner helix gate begins to open. Studies of the K62W mutant (PDB 5KUK, 5KUM) revealed a refined two-site lipid gating model with a primary PIP2 site and a second site for bulk anionic phospholipids (PL-).

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1180310 | 3JYC | 3.10 | I4 | Chicken Kir2.2 wild-type, residues 46-370 (N- and C-termini truncated) | Rb+, Sr2+, Eu3+ used for ion binding site mapping |
| doi/10.1038##nature10370 | 3SPI | 3.30 | I4 | Chicken Kir2.2 wild-type, with disordered N- and C-termini truncated; complexed with short-chain (dioctanoyl) PIP2 | dioctanoyl PIP2 |
| doi/10.1038##nature10370 | 3SPC | 3.00 | I4 | Chicken Kir2.2 I223L mutant with PIP2 | dioctanoyl PIP2 |
| doi/10.1038##nature10370 | 3SPG | 2.60 | I4 | Chicken Kir2.2 R186A mutant with PIP2 | dioctanoyl PIP2 |
| doi/10.1038##nature10370 | 3SPJ | 2.45 | I4 | Chicken Kir2.2 wild-type complexed with PPA (dioctanoyl glycerol pyrophosphatidic acid) | dioctanoyl PPA |
| doi/10.1085##jgp.201611616 | 5KUK | 2.00 | I 2 2 2 | Chicken Kir2.2 K62W mutant, C-terminal FLAG Tag replaced with 1D4 sequence, PreScission Protease site | decyl-maltoside (DM) detergent head group at second site |
| doi/10.1085##jgp.201611616 | 5KUM | 2.80 | I 2 2 2 | Chicken Kir2.2 K62W mutant with added PIP2 | PIP2 (primary site), decyl-maltoside (DM) detergent head group (second site) |

## Expression and Purification

- **Expression system**: Pichia pastoris (Pichia)
- **Construct**: Chicken Kir2.2 with C-terminal GFP and 1D4 epitope tag; also with C-terminal GFP and 1D4 epitope for K62W mutant studies

### Purification Workflow

*Source: doi/10.1038##nature10370*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Affinity chromatography | 1D4 antibody affinity chromatography | — | n-decyl-beta-D-maltopyranoside (DM) buffer | Protein expressed in Pichia pastoris with C-terminal GFP and 1D4 epitope |
| 2. Protease cleavage | PreScission protease cleavage | — | DM-containing buffer | Cleavage to remove GFP and affinity tags |
| 3. Size-exclusion chromatography | Gel filtration (Superdex 200) | — | DM-containing buffer | Purified protein concentrated to 9 mg/mL for crystallization |

### Purification Workflow

*Source: doi/10.1085##jgp.201611616*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Affinity chromatography | 1D4 antibody affinity chromatography | — |  | K62W mutant with C-terminal 1D4 tag |
| 2. Protease cleavage | PreScission protease cleavage | — |  |  |
| 3. Size-exclusion chromatography | Gel filtration | — | 150 mM KCl, 20 mM Tris-HCl pH 8.0, 4 mM DM, 20 mM DTT, 3 mM TCEP |  |


## Crystallization

### doi/10.1126##science.1180310

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | Purified Kir2.2 at 9 mg/mL in 150 mM KCl, 20 mM Tris-HCl pH 8.0, 4 mM n-decyl-beta-D-maltopyranoside (DM), 20 mM DTT, 3 mM TCEP. For ion soaks: 650 mM RbCl, 10-200 mM SrCl2, or 10 mM EuCl3 added. |
| Reservoir | 0.2-0.8 M KCl, 50 mM HEPES pH 6.5-7.5, 10-20% PEG 400 |
| Temperature | 20 C |
| Growth time | 48 hours |
| Notes | Crystals in space group I4 with one subunit per asymmetric unit. Data collected at NSLS beamline X29. Structure solved by single-wavelength anomalous dispersion (SAD) using selenomethionine-substituted protein. Native data to 3.1 A, selenomethionine data to 3.5 A. |

### doi/10.1038##nature10370

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | Purified Kir2.2 at 8 mg/mL in 4 mM DM, 20 mM DTT, 3 mM TCEP, 150 mM KCl, 20 mM Tris-HCl pH 8.0, with 0.6-1 mM dioctanoyl PIP2 (or 5 mM PPA for PPA complex) |
| Reservoir | 0.3-0.6 M KCl, 50 mM HEPES pH 6.5-7.5, 10-20% PEG 400 or 3-8% PEG 4000 |
| Temperature | 4 C |
| Growth time | 48 hours |
| Notes | Diamond-shaped crystals, 150-350 um in longest dimension. Cryoprotected in reservoir solution with 25-30% glycerol. Data collected at NSLS beamlines X29 and X25. Phases by molecular replacement using apo-Kir2.2 (PDB 3JYC). Space group I4 with one subunit per asymmetric unit. |

### doi/10.1085##jgp.201611616

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Kir2.2 K62W mutant in 150 mM KCl, 20 mM Tris-HCl pH 8.0, 4 mM DM, 20 mM DTT, 3 mM TCEP |
| Reservoir | Not specified in detail |
| Temperature | Not specified |
| Notes | Crystals diffracted to 2.0 A (apo) and 2.8 A (with added PIP2). Space group I222. Data collected at APS beamline 24-ID-C/E. |


## Biological / Functional Insights

### First atomic structure of a eukaryotic Kir channel

The 2009 Science paper (doi/10.1126/science.1180310) determined the first X-ray crystal structure of a eukaryotic inward-rectifier K+ channel, Kir2.2 from chicken, at 3.1 A resolution. The structure revealed the TXGYGFR selectivity filter sequence (versus the canonical TXGYGDX), which gives rise to distinct structural features including a disulfide bridge between C123 and C155 and an ionized hydrogen bond between R149 (in the filter) and E139. Multiple ion binding sites on the intracellular side of the selectivity filter (cavity, upper ring of charges, lower ring of charges) explain the mechanism of voltage-dependent block by intracellular multivalent cations (Mg2+, polyamines). The channel's extracellular surface features large structured turrets that constrict the pore entryway and explain the relative insensitivity of eukaryotic Kir channels to venom toxins.

### Ion binding sites for conduction and inward rectification

Crystals containing Rb+ (K+ analog), Sr2+ (Mg2+ mimic), and Eu3+ revealed distinct ion binding sites along the conduction pathway. Rb+ binds at multiple sites in the selectivity filter and at three positions intracellular to the filter (below the activation gate, at the upper ring of charges E225/E300, and at the lower ring of charges D256). Sr2+ binds in the cavity (weak, at D173), the upper ring (strong), and the lower ring (strong). Eu3+ binds only at the upper ring, which contains two concentric rings of acidic amino acids (E225 and E300). These sites are formed by planar rings of acidic amino acids too wide for direct ion coordination, suggesting ions at these positions interact through bridging water molecules. The strong electric field created by multiple negatively charged carboxyl groups favors multivalent cations, explaining the mechanism of inward rectification.

### PIP2 binding site at TMD-CTD interface

PIP2 binds at an interface between the transmembrane domain (TMD) and the cytoplasmic domain (CTD). The PIP2-binding site consists of a conserved non-specific phospholipid-binding region in the TMD and a specific phosphatidylinositol-binding region in the CTD. The acyl chains, glycerol backbone and 1' phosphate of PIP2 interact with the TMD, while the inositol head group makes interactions with the CTD.

### Conformational change on PIP2 binding

On PIP2 binding, a flexible expansion linker contracts to a compact helical structure, the CTD translates 6 A towards the TMD, and the inner helix gate begins to open (6.3 A at Ile177 in PIP2-bound vs 4.9 A in PPA-bound). The conformational changes include formation of two new helices: an N-terminal extension of the 'interfacial' helix and a 'tether' helix at the C terminus of the inner helix.

### PPA binds TMD but fails to activate

The small anionic lipid PPA (dioctanoyl glycerol pyrophosphatidic acid) binds to the non-specific TMD region but not to the specific phosphatidylinositol region, and thus fails to engage the CTD or open the channel. The PPA-bound structure (PDB 3SPJ) shows a closed conformation similar to apo-Kir2.2 (PDB 3JYC) with the CTD unengaged and the inner helix gate tightly closed (4.9 A at Ile177).

### Conserved RWR sequence for 1' phosphate binding

The sequence arginine-tryptophan-arginine (R78-W79-R80) at the N terminus of the outer helix forms a binding site in which the 1' phosphate of PIP2 caps the helix and is cradled by main-chain amide nitrogen atoms and guanidinium groups. This sequence is conserved as RWR or KWR among many Kir channels.

### Two-site lipid gating model from K62W studies

Kir2 channels have two distinct lipid-binding sites: a primary PIP2 site at the TMD-CTD interface and a second site for bulk anionic phospholipids (PL-) at the N-terminal slide helix (K62 in cKir2.2). PL- binding at the second site pulls the CTD toward the membrane, inducing formation of the high-affinity primary PIP2 site. This explains the positive allostery between PL- binding and PIP2 sensitivity.


## Cross-References
