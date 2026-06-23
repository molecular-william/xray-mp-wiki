---
title: Melibiose Transporter MelB from Salmonella typhimurium (MelB_St)
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s42003-021-02462-x, doi/10.1038##ncomms4009]
verified: false
---

# Melibiose Transporter MelB from Salmonella typhimurium (MelB_St)

## Overview

MelB is a [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose/) transporter from Salmonella typhimurium belonging to the glycoside-pentoside-hexuronide:cation symporter (GPH) family, a subgroup of the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/)). It catalyzes the stoichiometric symport of galactose or galactosides with monovalent cations (Na+, Li+, or H+). MelB has served as a model system for studying cation-coupled transport mechanisms in [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) transporters. The D59C mutant uncouples cation binding from sugar transport, converting the symporter into a uniporter that retains sugar binding and translocation. Two high-resolution X-ray crystal structures of the D59C MelB_St mutant were solved — one bound to α-NPG at 3.05 Å resolution (PDB 7L17) and one bound to DDMB at 3.15 Å resolution (PDB 7L16) — revealing the molecular recognition mechanism for sugar binding and the spatial relationship between the sugar specificity pocket and the cation-binding pocket.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s42003-021-02462-x | 7L17 | 3.05 | P 31 2 1 | D59C MelB_St mutant with bound α-NPG | α-NPG (4-nitrophenyl-α-D-galactopyranoside) |
| doi/10.1038##s42003-021-02462-x | 7L16 | 3.15 | P 31 2 1 | D59C MelB_St mutant with bound DDMB | DDMB (dodecyl-β-D-melibioside) |
| doi/10.1038##ncomms3009 |  | 4.0 | P 31 2 1 | WT MelB_St, outward-facing conformation (no ligand resolved) |  |

## Expression and Purification

- **Expression system**: E. coli DW2 strain (melA+, melB-, lacZ-Y-)
- **Construct**: MelB_St with C-terminal His-tag from pK95ΔAH/MelB_St/CHis
- **Induction**: Constitutive expression
- **Media**: 2× YT medium

### Purification Workflow

*Source: doi/10.1038##s42003-021-02462-x*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | — |  | E. coli DW2 cells expressing MelB_St were grown in 2× YT medium |
| Membrane preparation | Cell lysis and membrane isolation | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), pH 7.5 | Standard membrane protein preparation protocol |
| Solubilization | Detergent extraction | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), pH 7.5, 100 mM CholCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% [UDM](/xray-mp-wiki/reagents/detergents/udm/) (undecyl-β-D-maltopyranoside) |  |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA resin | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), pH 7.5, 100 mM CholCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.03% [UDM](/xray-mp-wiki/reagents/detergents/udm/) | Purified D59C MelB_St in [UDM](/xray-mp-wiki/reagents/detergents/udm/) solution, Tm of 60°C by CD spectroscopy |

### Purification Workflow

*Source: doi/10.1038##ncomms3009*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | — |  | E. coli DW2 cells grown in 2× YT medium |
| Membrane preparation | Cell lysis and membrane isolation | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), pH 7.5 |  |
| Solubilization | Detergent extraction | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), pH 7.5, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% [UDM](/xray-mp-wiki/reagents/detergents/udm/) |  |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Ni-NTA resin | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), pH 7.5, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [UDM](/xray-mp-wiki/reagents/detergents/udm/) | Eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), pH 7.5, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [UDM](/xray-mp-wiki/reagents/detergents/udm/) |  |


## Crystallization

### doi/10.1038##s42003-021-02462-x

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified D59C MelB_St in 0.03% [UDM](/xray-mp-wiki/reagents/detergents/udm/), 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 100 mM CholCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Reservoir | 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 50 mM NaCl, 30% (v/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 |
| Mixing ratio | 1:1 |
| Temperature | 20°C |
| Cryoprotection | 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) or 20% [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) |
| Notes | Crystals grown with 10 mM α-NPG or 0.7 mM DDMB (below CMC of 295 µM) for ligand-bound structures. SeMet-labeled protein used for phasing. |


## Biological / Functional Insights

### Sugar specificity determinant pocket

Two high-resolution structures of D59C MelB_St bound to α-NPG (7L17) or DDMB (7L16) reveal a narrow sugar specificity determinant pocket formed by residues from five transmembrane helices (I, IV, V, X, and XI). The galactosyl moiety is recognized through a comprehensive salt-bridge-assisted H-bonding network involving Lys18, Asp19 (helix I), Tyr120, Asp124, Trp128 (helix IV), Arg149 (helix V), Trp342 (helix X), and Thr373, Val376 (helix XI). The galactosyl ring is sandwiched between hydrophobic residues (Ile22, Tyr26, Trp342, Val376) while all four OH groups form hydrogen bonds with charged/polar residues. This arrangement explains MelB's specificity for galactosides over glucosides.

### Cation-binding pocket and cooperative coupling

The conserved cation-binding pocket is proposed based on the D59C structures, involving residues Asp55, Asp59, Gly117, Thr121, and Lys377 from helices II, IV, and XI. The C6-OH of the galactosyl ring approaches within 6.9 Å of the cation site, suggesting a direct structural connection between the two binding pockets. This physical proximity explains the positive cooperativity between sugar and cation binding observed by [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/), where Na+ or Li+ binding enhances sugar affinity and vice versa. Four out of six cation-site positions are conserved in the human MFSD2A transporter, suggesting a common cation-binding mechanism across the GPH family.

### D59C mutation converts symport to uniport

The D59C mutation in MelB abolishes cation binding and all three modes of cation-coupled [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose/) transport (Na+-coupled, Li+-coupled, and H+-coupled symport) while retaining sugar binding and translocation, effectively converting the symporter into a uniporter. Asp59 is proposed as the H+-binding residue, and the D59C mutant lacks affinity for all three cations (Na+, Li+, H+). This uncoupling made crystallization feasible, as the WT MelB with sugar bound proved challenging due to its greater conformational dynamics. The D59C mutant exhibits improved thermostability (Tm = 60°C, 6°C higher than WT) and yields reproducible high-quality crystals.

### Broad sugar specificity explained by two-pocket architecture

The structures explain MelB's ability to recognize a wide variety of galactosides from mono- to tri-saccharides. The narrow sugar specificity determinant pocket recognizes the common galactosyl moiety, while a large non-specific binding cavity accommodates the structural/chemical variations on the non-galactosyl moiety (e.g., nitrophenyl, dansyl, or melibiosyl groups). The non-specific interactions can increase binding affinity, as exemplified by α-NPG which exhibits ~100-fold greater affinity than [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose/) (Kd ~43 µM vs ~9 mM). This two-pocket architecture suggests potential drug delivery strategies using glycoside-based substrates transported by sugar active transporters.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) — MelB belongs to the GPH family within the MFS superfamily
- [LeuT Amino Acid Transporter](/xray-mp-wiki/proteins/enzymes/leut/) — LeuT is another model secondary transporter with resolved substrate-binding mechanism
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — MelB transport follows the alternating-access model
- [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) — Method used in structure determination or purification
- [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
