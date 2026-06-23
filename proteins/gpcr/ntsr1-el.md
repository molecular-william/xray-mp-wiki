---
title: NTSR1-EL Constitutively Active Mutant
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##srep38564]
verified: false
---

# NTSR1-EL Constitutively Active Mutant

## Overview

NTSR1-EL is a constitutively active mutant of the rat [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) receptor 1 ([NTSR1](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/)), a class A GPCR. It contains three thermostabilizing mutations from the parent NTSR1-GW5 construct (A86L, G215A, V360A) with the F358A mutation (7.42) retained, while wild-type residues are present at positions E166 (3.49) and L310 (6.37). The F358A mutation severs the hydrophobic cascade linking the ligand-binding pocket to the connector region, resulting in pronounced constitutive activity (IP production in the absence of agonist) but reduced [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) efficacy compared to wild-type. The crystal structure of NTSR1-EL-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) with bound NTS(8-13) was determined at 3.3 A resolution (PDB 5T04). Molecular dynamics simulations show that the connector residues remain tightly packed regardless of agonist presence, explaining the constitutive activity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##srep38564 | 5T04 | 3.3 | unknown | Rat NTSR1-EL-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/): Residues T43-K396 with mutations A86L(1.54), G215A(ECL2), F358A(7.42), V360A(7.44); ICL3 residues H269-E296 replaced by cysteine-free T4 lysozyme (N2-Y161, C54T, C97A) with GSGS linker; C-terminal deca-histidine tag | NTS(8-13) agonist peptide |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: NTSR1-EL-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) with hemagglutinin signal peptide and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) replacing ICL3

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 insect cells | — | Not specified | NTSR1-EL-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) construct expressed via baculovirus |
| Membrane preparation | Urea-washed P2 insect cell membranes | — | Not specified | Membranes washed with [UREA](/xray-mp-wiki/reagents/substrates/urea/) to remove peripherally bound proteins |
| Solubilization | [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/CHS detergent | — | 50 mM TrisHCl pH 7.4, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 200 mM NaCl, 1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 uM NTS(8-13) + 1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Solubilized for 2 h at 4 C. NaCl adjusted to 200 mM. Final volume 280 mL. Clarified by centrifugation at 125,000 g for 1 h. |
| Affinity purification | [TALON](/xray-mp-wiki/reagents/additives/talon/) resin (Co-NTA) | — | 50 mM TrisHCl pH 7.4, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 200 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 1 uM NTS(8-13), 0.1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Batch incubation overnight. Washed with Talon-A+ and Talon-A2+ buffers. Eluted with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in Talon-B+ buffer (0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 uM NTS(8-13)). Peak fractions collected (2.5 mL). |
| Desalting | PD10 desalting column | — | 50 mM TrisHCl pH 7.4, 200 mM NaCl, 0.003% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.0003% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.003% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.0003% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Desalted into PD10 buffer. NTS(8-13) added to 20 uM after desalting. ~3.3 mg from 3 L culture. |


## Crystallization

### doi/10.1038##srep38564

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Temperature | 20 |
| Notes | Purified NTSR1-EL-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) adjusted to 100 uM TCEP and 350 uM NTS(8-13), concentrated to ~60 mg/mL. Mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/):[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) (10:1) in LCP using two-syringe method. 60-70 nL drops dispensed onto Laminex plates. Crystals grown at 20 C. |


## Biological / Functional Insights

### F358A severs the hydrophobic cascade

In NTSR1-EL, the F358A mutation removes the aromatic side chain at position 7.42, severing a network of van der Waals contacts (the hydrophobic cascade) involving Y324(6.51), F358(7.42), W321(6.48), and F317(6.44). This network is intact in NTSR1-ELF. The disruption causes W321(6.48) to adopt a perpendicular side chain orientation (chi2 angle of 103 deg) compared to the parallel orientation in NTSR1-ELF (chi2 ~55 deg).

### Constitutive activity from tight connector packing

MD simulations show that NTSR1-EL maintains tight packing of connector residues A157(3.40)-P249(5.50)-F317(6.44) regardless of agonist presence. In contrast, NTSR1-ELF shows tight packing only with agonist and looser packing without agonist. This constitutively packed connector correlates with the pronounced basal IP production of NTSR1-EL in the absence of [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/).

### Reduced NTS efficacy due to uncoupled binding pocket

The severing of the hydrophobic cascade in NTSR1-EL uncouples the ligand-binding pocket from the connector region. This reduces the ability of bound NTS to propagate conformational changes, explaining the reduced fold-stimulation of IP production by NTS in NTSR1-EL compared to NTSR1-ELF and wild-type.

### Increased flexibility at G protein interface

MD simulations show that NTSR1-EL displays a more open intracellular cleft between TM3 and TM6 and fewer interhelical contacts in the intracellular half of the receptor compared to NTSR1-ELF. This suggests that the constitutively active conformation has higher conformational flexibility that facilitates the initial docking of G protein in the absence of agonist.

### Distinct agonist binding mode

The NTSR1-EL crystal structure reveals subtle differences in NTS(8-13) binding compared to NTSR1-ELF. TM5 movement allows Arg9 of NTS to form a hydrogen bond with T231(5.32) that is absent in NTSR1-ELF. Hydrogen bonds between the NTS C-terminal carboxylate of Leu13 and Y351(7.35)/R328(6.55) are lost in NTSR1-EL. Instead, R328(6.55) engages N241(5.42).


## Cross-References

- [Rat Neurotensin Receptor 1 (NTSR1)](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/) — NTSR1-EL is a constitutively active mutant derivative of NTSR1
- [NTSR1-LF Mutant](/xray-mp-wiki/proteins/gpcr/ntsr1-lf/) — Related thermostabilized mutant; NTSR1-EL compared with NTSR1-LF and NTSR1-ELF for G protein activation
- [TM86V-deltaIC3A NTSR1 Mutant](/xray-mp-wiki/proteins/gpcr/tm86v-delta-ic3a/) — Inactive-state NTSR1 mutant used for comparison with NTSR1-EL connector region
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion replacing ICL3 in NTSR1-EL-T4L crystallization construct
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for solubilization, purification, and crystallization of NTSR1-EL-T4L
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — CHS used in combination with LMNG for solubilization and LCP crystallization
- [Neurotensin (NTS)](/xray-mp-wiki/reagents/ligands/neurotensin/) — Endogenous agonist peptide used in co-crystallization of NTSR1-EL
- [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/) — Non-peptide antagonist used in docking studies with NTSR1 for comparison
- [GPCR Activation Mechanism](/xray-mp-wiki/concepts/gpcr-activation-mechanism/) — NTSR1-EL provides insights into the structural basis of GPCR constitutive activity
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
