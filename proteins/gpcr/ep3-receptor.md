---
title: Prostaglandin E2 Receptor EP3 (Prostanoid EP3 Receptor)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41589-018-0160-y, doi/10.1038##s41589-018-0171-8]
verified: false
---

# Prostaglandin E2 Receptor EP3 (Prostanoid EP3 Receptor)

## Overview

The [Prostaglandin E2 (PGE2, Dinoprostone)](/xray-mp-wiki/reagents/ligands/prostaglandin-e2/) receptor EP3 is a class A G protein-coupled receptor (GPCR) that mediates the physiological actions of [Prostaglandin E2 (PGE2, Dinoprostone)](/xray-mp-wiki/reagents/ligands/prostaglandin-e2/) (PGE2), a major bioactive lipid involved in inflammation, pain, fever, and labor. EP3 is the primary target of , a life-saving uterotonic drug used to prevent postpartum hemorrhage. Two independent crystal structures of the human EP3 receptor were determined in the active-like state: the  free-acid (-FA) bound structure at 2.5 A resolution by [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) at an X-ray free electron laser (XFEL), and the endogenous agonist PGE2-bound structure at 2.9 A resolution by synchrotron [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/). Both structures reveal a completely enclosed ligand-binding pocket with a structured water molecule coordinating the ligand's ring structure, providing the first atomic description of prostaglandin recognition by a prostanoid receptor.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41589-018-0160-y | Not specified in paper | 2.50 A | Not specified | Human EP3 isoform A (modified), initial Met removed, ICL3 (residues 260-272) replaced with [T4L](/xray-mp-wiki/reagents/t4-lysozyme/) (T4L, A73T), C-terminus truncated after Leu353, Gly286(6.39)Ala mutation | -FA (free acid form of ) |
| doi/10.1038##s41589-018-0171-8 | Not specified in paper | 2.90 A | P 21 | Human EP3 with mbIIG2 fusion (modified ) in ICL2/ICL3, quadruple thermostabilizing mutations A173I(4.41), V185S(4.53), S258D(5.65), C289L(6.42) | [Prostaglandin E2 (PGE2, Dinoprostone)](/xray-mp-wiki/reagents/ligands/prostaglandin-e2/) (PGE2) |

## Expression and Purification

- **Expression system**: Baculovirus/Sf9 insect cells (Bac-to-Bac system, Invitrogen)
- **Construct**: Human EP3 receptor. Paper 1 (0160-y): N-terminal HA signal peptide + [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), C-terminal [PreScission Protease](/xray-mp-wiki/reagents/pre-scission-protease/) + 10xHis tag, ICL3 replaced with [T4L](/xray-mp-wiki/reagents/t4-lysozyme/) (A73T). Paper 2 (0171-8): Codon-optimized human EP3 isoform I with N-terminal HA signal + [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) + 3C site, C-terminal 10xHis tag, mbIIG2 fusion in ICL2/ICL3 with GS-rich linker

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and infection | Sf9 cells infected with recombinant baculovirus at 2x10^6 cells/ml | — |  | Grown in the presence of 1 uM  methyl ester |
| Membrane preparation | Three rounds of washing and ultracentrifugation at 250,000g | — | 10 mM  pH 7.5, 10 mM , 20 mM KCl, -free protease inhibitor cocktail | Second wash: 10 mM  pH 7.5, 1 M NaCl, 10 mM , 20 mM KCl |
| Alkylation | Incubation with 2 mg/ml  at room temperature for 1 h, then 30 min at 4C | — |  | After resuspending membranes in lysis buffer with 20%  |
| Solubilization | Stirred for 2 h at 4C | — | 50 mM  pH 7.5, 800 mM NaCl, 1% , 0.2% [CHS](/xray-mp-wiki/reagents/cholesteryl-hemisuccinate/) |  |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) |  resin (Clontech), overnight batch binding at 4C |  IMAC resin | Wash 1: 50 mM  pH 7.2, 150 mM NaCl, 10 mM , 8 mM , 0.1% , 0.01% [CHS](/xray-mp-wiki/reagents/cholesteryl-hemisuccinate/), 10% , 20 mM . Wash 2: 50 mM  pH 7.5, 150 mM NaCl, 0.05% , 0.01% [CHS](/xray-mp-wiki/reagents/cholesteryl-hemisuccinate/), 10% , 20 mM  | Eluted with 2.5 CV of elution buffer |
| Concentration | Concentration for LCP crystallization | — |  | Protein concentrated for LCP reconstitution |


## Crystallization

### doi/10.1038##s41589-018-0160-y

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified EP3-T4L with -FA |
| Temperature | Room temperature |
| Notes | Crystallized in LCP. Diffraction data collected at LCLS XFEL using [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) (SFX) at room temperature. Structure determined at 2.5 A resolution. |

### doi/10.1038##s41589-018-0171-8

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified EP3-mbIIG2 with PGE2 |
| Temperature | Not specified |
| Notes | Crystallized in LCP. Data collected at SPring-8 synchrotron. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/). Space group P21, unit cell a=66.1, b=42.3, c=161.3 A, beta=96.1 deg. |


## Biological / Functional Insights

### First atomic structures of a prostanoid receptor

The EP3--FA (2.5 A) and EP3-PGE2 (2.9 A) structures represent the first crystal structures of a prostanoid receptor bound to prostaglandin ligands, providing the first atomic description of prostaglandin recognition and signaling through a GPCR. The structures reveal how the prostaglandin scaffold interacts with the receptor and explain the molecular basis for ligand selectivity among EP receptor subtypes.

### Completely enclosed ligand-binding pocket

Both structures reveal a completely enclosed binding pocket for the prostaglandin ligand. ECL2 forms a lid that occludes access to the orthosteric site, making the binding pocket totally enclosed. This closed conformation likely contributes to the long residence time of  on EP3 and may represent an induced-fit mechanism upon ligand binding. The enclosed pocket contrasts with many other GPCRs that have solvent-exposed binding sites.

### Structured water molecule in the binding pocket

A structured water molecule is observed coordinating the E-ring of -FA (and PGE2) in the binding pocket, forming hydrogen bonds with the ligand hydroxyl groups and receptor side chains. This water molecule, resolved at 2.5 A resolution, plays a key role in stabilizing the ligand-receptor interaction. The ability to detect this water was enabled by the high resolution of the XFEL structure.

### Key binding pocket residues for ligand recognition

The prostaglandin binding pocket is formed by residues from TM1 (P55, M58), TM2 (Q103, T106, T107, V110, Y114), TM3 (M137, G141), ECL2 (T206, W207, F209), TM5 (F234), TM6 (W295, L298), and TM7 (L329, V332, R333, S336, Q339). Arg333(7.40) forms a critical salt bridge with the ligand carboxylate and is conserved among all prostaglandin receptors. Gly141(3.36) at the bottom of the pocket interacts with the omega-chain of the ligand, and mutation to larger residues reduces signaling potency by three orders of magnitude.

### ECL2 as a determinant of ligand selectivity

ECL2 in EP3 adopts a unique conformation that forms the lid of the binding pocket. Comparison with EP4 and rhodopsin ECL2 conformations reveals structural differences that contribute to ligand selectivity among EP receptor subtypes. The ECL2 residues T206, W207, and F209 are directly involved in ligand coordination.

### Active-like receptor conformation

Both structures exhibit active-like conformational features including displacement of TM6 relative to inactive-state GPCRs. The canonical toggle switch W295(6.48) is in an active conformation. Comparison with Gi/o-coupled active GPCRs (, mu-opioid receptor, A1 adenosine receptor, 5-HT1B) shows TM6 displacement of 2.1-7.6 A depending on the reference structure.

### Structural basis for EP3-selective agonists

The structures explain how prostaglandin derivatives achieve EP3 selectivity. Branched carbon 16 substitutions (-FA, TEI-3356) contact Gly141(3.36) constraining the omega-chain. Bulky groups at the omega-chain extremity (MB-28767, sulprostone, -63799) form additional hydrophobic interactions. EP1 and EP2 have larger residues at position 6.51 (Met, Phe) that would clash with constrained omega-chains, conferring selectivity toward EP3 and EP4.

### Thermostabilization of EP3 for crystallography

The Morimoto et al. structure used a quadruple mutant (A173I, V185S, S258D, C289L) identified through fluorescence-detection [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) (FSEC) thermostability screening. V185S forms a hydrogen bond with S143(3.38), contributing to . These mutations did not significantly affect PGE2 binding affinity or signaling activity.


## Cross-References

- [GPCR Active Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/) — EP3 structures represent active-like state of a prostanoid receptor
- [n-Dodecyl-beta-D-Maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for EP3 solubilization and purification
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Lipid additive for EP3 stabilization during purification
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion in ICL3 used in the EP3-misoprostol structure (Audet et al.)
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for both EP3 crystal structures
- [Serial Femtosecond Crystallography (SFX)](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — XFEL data collection used for the 2.5 A EP3-misoprostol structure
- [Misoprostol](/xray-mp-wiki/reagents/misoprostol/) — Referenced in ep3-receptor text
- [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) — Referenced in ep3-receptor text
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Referenced in ep3-receptor text
- [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Referenced in ep3-receptor text
