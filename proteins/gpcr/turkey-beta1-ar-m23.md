---
title: "Turkey Beta1-Adrenergic Receptor M23"
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2012.01.032, doi/10.1038##NATURE09746]
verified: false
---

# Turkey Beta1-Adrenergic Receptor M23

## Overview

The turkey beta1-adrenergic receptor (beta1AR) is a class A G protein-coupled receptor that mediates sympathetic nervous system responses including increased heart rate and contractility. The thermostabilized mutant beta1AR-M23, incorporating a 25-60 helix insertion, 292-303 deletion, point mutations, and a [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion on the third intracellular loop, was crystallized using the [lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) method. Crystal structures of both the apo form at 2.9 A (PDB: 4LDE) and a complex with the antagonist [carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) at 3.0 A (PDB: 4LDF) were solved, representing the first GPCR structures without a bound G-protein or Fab fragment.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2012.01.032 | 4LDE | 2.9 A | P 21 21 21 | Turkey beta1AR-M23 with BRIL fusion on ICL3 | None (apo form) |
| doi/10.1016##j.jmb.2012.01.032 | 4LDF | 3.0 A | P 21 21 21 | Turkey beta1AR-M23 with BRIL fusion on ICL3 | Carvedilol |
| doi/10.1038##NATURE09746 | iso327 | 2.85 A | P21 | Turkey beta1AR-M23 with carmoterol | Isoprenaline |
| doi/10.1038##NATURE09746 | car7 | 2.6 A | P21 | Turkey beta1AR-M23 with carmoterol | Carmoterol |
| doi/10.1038##NATURE09746 | dob92 | 2.5 A | P21 | Turkey beta1AR-M23 with dobutamine | Dobutamine (R-isomer) |
| doi/10.1038##NATURE09746 | dob102 | 2.6 A | P21 | Turkey beta1AR-M23 with dobutamine | Dobutamine (R-isomer) |
| doi/10.1038##NATURE09746 | sal109 | 3.05 A | P21 | Turkey beta1AR-M23 with salbutamol | Salbutamol (R-isomer) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression vector system)
- **Construct**: Turkey beta1AR-M23 thermostabilized mutant with His6-tag for purification. The construct includes a 25-60 helix insertion, 292-303 deletion, point mutations (F88A, T89A, T90A, F92A, F194A, F198A), and a BRIL fusion on the third intracellular loop.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | Sf9 cells were infected with baculovirus expressing beta1AR-M23 and harvested 48 hours post-infection. Cell membranes were prepared by homogenization and ultracentrifugation. | -- | -- + -- | Membranes were solubilized in 50 mM Tris-HCl pH 7.5, 150 mM NaCl, 10 mM MgCl2, 1 mM EDTA, 10% glycerol, and 1% [n-dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) for 1 hour at 4 degrees Celsius. |
| Ni-NTA affinity chromatography | [Affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) using [Ni-NTA agarose](/xray-mp-wiki/reagents/additives/nickel-nta/) resin | Ni-NTA agarose | 50 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.05% DDM + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Column was washed with buffer containing 0.05% DDM and eluted with 250 mM imidazole. |
| Size-exclusion chromatography | [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) on a Superdex 200 column | Superdex 200 | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.05% DDM + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted fractions containing monodisperse protein were pooled and concentrated. |


## Crystallization

### doi/10.1016##j.jmb.2012.01.032

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified beta1AR-M23 at approximately 20 mg/mL in 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.05% DDM. For the carvedilol complex, the receptor was incubated with 100 microM carvedilol for 30 minutes prior to mixing with the lipid matrix. |
| Temperature | 20 degrees Celsius |
| Growth time | Crystals appeared within 1-2 weeks |
| Cryoprotection | Crystals were flash-cooled in liquid nitrogen directly from the reservoir solution (no additional cryoprotectant was needed). |
| Notes | Both apo and carvedilol-bound structures were obtained under identical crystallization conditions. The monoolein lipid matrix was mixed with protein sample at a 1:1 ratio before dispensing into reservoir drops via the LCP robot. X-ray diffraction data were collected at beamline 23-ID-B at APS. The apo structure (4LDE) was solved by molecular replacement at 2.9 A resolution. The carvedilol-bound structure (4LDF) was solved at 3.0 A resolution by molecular replacement using the apo structure as a search model. |

### doi/10.1038##NATURE09746

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization |
| Protein sample | Purified turkey beta1AR-M23 at 14.5-16.0 mg/ml in varying buffer conditions. CHS added from a 10 mg/ml stock in 2% HEGA-10 immediately prior to crystallization. |
| Reservoir | Varied by ligand: salbutamol (sal109) - 28% PEG 400 in bicine pH 9.0; isoprenaline (iso327) - 28% PEG 600 in tris-HCl pH 8.5; carmoterol (car7) - 26% PEG 600 in bicine pH 9.0; dobutamine (dob92) - 25% PEG 600 in tris-HCl pH 8.5; dobutamine (dob102) - 25% PEG 600 in bicine pH 9.0 |
| Cryoprotection | PEG 600 at 55% used as cryoprotectant |
| Notes | All structures crystallized in space group P21 with two monomers per asymmetric unit. The two monomers make similar crystal contacts, but crystal contacts at the top of helix 7 differ between monomers A and B. This causes different orientations of the methylphenoxy group in carmoterol and the methylhydroxyl substituent in salbutamol between the two monomers. CHS concentrations ranged from 0.45 to 1.9 mg/ml depending on the ligand. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization |
| Protein sample | Purified turkey beta1AR-M23 at 16.5 mg/ml |
| Reservoir | 28% PEG 400, bicine pH 9.0 |
| Cryoprotection | 60% PEG 400 |
| Notes | Crystallization of beta1AR-M23 with salbutamol (sal109). Racemic (R,S)-salbutamol was used in crystallization, but the (R)-isomer was found in the resulting structure. Wilson B factor: 70.6 A^2. Resolution range: 38.6-3.05 A. Rmerge: 0.119 (0.509). |


## Biological / Functional Insights

### Antagonist binding pocket architecture

The structure of beta1AR-M23 in complex with carvedilol reveals the molecular details of antagonist binding in a beta1-adrenergic receptor. Carvedilol binds deep within the transmembrane bundle, with its carbazole moiety making hydrophobic contacts with transmembrane helices 3, 5, 6, and 7, while the cyclohexyl group interacts with helix 3. The hydroxyl groups of carvedilol form hydrogen bonds with Ser193(5.42) and Ser197(5.46) in transmembrane helix 5, a conserved feature of catecholamine binding in beta-adrenergic receptors.

### Thermostabilization mechanism

The beta1AR-M23 mutant shows dramatically improved thermal stability compared to wild-type turkey beta1AR. The melting temperature increases from approximately 40 degrees Celsius for wild-type to over 55 degrees Celsius for the M23 mutant. The stabilizing mutations are distributed throughout the receptor, with the 25-60 helix filling a cavity in the intracellular region and the BRIL fusion providing additional structural rigidity to the intracellular loops.

### GPCR conformational state

The apo structure of beta1AR-M23 reveals a receptor conformation that is intermediate between the inactive and active states. The intracellular surface shows partial rearrangement of the ionic lock (Arg3.50-Glu6.30 interaction), suggesting that the thermostabilization mutations may bias the receptor toward a specific conformational ensemble. This intermediate state may explain why beta1AR-M23 can crystallize without a bound G-protein or Fab fragment.

### BRIL fusion strategy

The [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (brucellae lysozyme) fusion protein was found to be an effective strategy for GPCR crystallization. BRIL is a small, thermostable protein that fuses to the ICL3 without disrupting the receptor's structural integrity or ligand binding. The BRIL fusion replaces flexible ICL3 loops with a rigid alpha-helical domain, reducing conformational heterogeneity and promoting crystal contacts.

### Comparison with other GPCR structures

The turkey beta1AR-M23 structure shares the canonical seven-transmembrane helix architecture with other class A GPCR structures, including bovine rhodopsin, the human adenosine A2A receptor, and the human beta2-adrenergic receptor. The carvedilol binding mode is consistent with the conserved catecholamine-binding pharmacophore observed in other beta-adrenergic receptor structures.


## Cross-References

- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — Another class A GPCR crystallized using the LCP method by the same group (RCSB)
- [A2A-PSB1-bRIL](/xray-mp-wiki/proteins/gpcr/a2a-psb1-bril/) — Related thermostabilized GPCR construct using the BRIL fusion strategy
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used as the matrix for LCP crystallization
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and all purification steps
- [Carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) — Antagonist ligand co-crystallized with beta1AR-M23 in structure 4LDF
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for both apo and ligand-bound structures
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final purification step to obtain monodisperse protein sample
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA affinity chromatography used for initial purification of His6-tagged receptor
