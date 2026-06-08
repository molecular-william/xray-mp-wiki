---
title: Rat Neurotensin Receptor 1 (NTSR1)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11558, doi/10.1038##ncomms8895]
verified: false
---

# Rat Neurotensin Receptor 1 (NTSR1)

## Overview

The rat neurotensin receptor 1 (NTSR1) is a class A G protein-coupled receptor that binds the tridecapeptide neurotensin. NTSR1 is involved in various physiological processes including neurotransmission, pain modulation, and regulation of body temperature. The thermostabilized NTSR1-GW5 construct, with six point mutations (A86L, E166A, G215A, L310A, F358A, V360A) and T4 lysozyme (T4L) fused into the third intracellular loop, enabled the first crystal structure of a neurotensin receptor in complex with its agonist peptide NTS(8-13) at 2.80 A resolution. The structure revealed the molecular basis for agonist binding and provided insights into neurotensin receptor pharmacology.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11558 | Not specified (see main paper) | 2.80 A | P21 | Rat NTSR1-GW5-T4L: GW5 thermostabilizing mutations (A86L, E166A, G215A, L310A, F358A, V360A), T4 lysozyme replacing ICL3 residues H269-R299, expressed in Sf9 insect cells
 | NTS(8-13) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: NTSR1-GW5-T4L construct with six thermostabilizing mutations (A86L, E166A, G215A, L310A, F358A, V360A) and T4 lysozyme replacing most of ICL3 (residues H269-R299)


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 insect cells | — | Not specified | NTSR1-GW5 construct produced at Protein Expression Laboratory, SAIC-Frederick, NCI |
| Membrane preparation | Urea-washed P2 insect cell membranes | — | Not specified | Membranes washed with urea to reduce background binding |
| Solubilization | DM or LMNG detergent | — | DM or LMNG | Solubilized in either n-decyl-beta-D-maltopyranoside or lauryl maltose neopentyl glycol |
| Purification | Not specified | — | Not specified | Purification details not provided in supplementary information |


## Crystallization

### doi/10.1038##nature11558

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Notes | NTSR1-GW5-T4L crystallized in LCP at Diamond Light Source beamline I24. Data collected at wavelength 1.0 A. Space group P21 with cell dimensions a=46.96, b=69.62, c=97.53, alpha=90, beta=101.7, gamma=90 degrees. Resolution 30-2.80 A (shell 2.90-2.80 A). Completeness 93.1% (86.4% in shell). Redundancy 2.4 (2.1). Rsym 0.15 (0.65). I/sigma(I) 5.6 (1.3). Refinement R/Rfree 0.23/0.28 for resolution range 15-2.80 A with 14956 reflections. 3435 protein atoms, 88 ligand atoms, 23 waters. B-factors: NTSR1-GW5-T4L 88.2, NTSR1-GW5 85.6 A^2.
 |


## Biological / Functional Insights

### Thermostabilization of NTSR1 by GW5 mutations

The NTSR1-GW5 construct contains six thermostabilizing mutations: A86L (1.54), E166A (3.49), G215A, L310A (6.37), F358A (7.42), and V360A (7.44), using Ballesteros-Weinstein numbering. These mutations increased the apparent melting temperature by 23.9 C in DM (from 26.0 to 49.9 C) and 18.9 C in LMNG (from 39.8 to 58.7 C) compared to wild-type NTSR1. The thermostabilized receptor showed reduced sensitivity to Na+ ions and limited G protein coupling, suggesting stabilization in a high-affinity agonist conformation.

### NTS(8-13) agonist binding site architecture

The NTS(8-13) peptide binds deep within the transmembrane bundle of NTSR1. Key interactions include: Arg8 side chain forms van der Waals contacts with Phe344 (TM7); Phe331 (TM6) intercalates between Arg9 and Leu13 of the peptide; Pro10 forms van der Waals contacts with Trp339 (ECL3); Tyr11 forms a hydrogen bond with Leu55 (N-terminal region); the C-terminal carboxylate of Leu13 forms a salt bridge with Arg327 (TM6) and a hydrogen bond with Tyr146 (TM3). Site-directed mutagenesis studies confirm these interactions, with F344A, F331A, W339A, and M208A mutants each showing 10-fold reduced agonist binding.

### Sodium ion allosteric modulation in NTSR1

Wild-type NTSR1 shows Na+ sensitivity with IC50 of 43 mM for NaCl inhibition of [3H]NTS binding. The thermostabilized NTSR1-GW5 shows 5-fold reduced Na+ sensitivity (IC50 184-205 mM). Na+ ions act as negative allosteric effectors binding to a conserved site involving Asp113 (2.50), consistent with the mechanism first described for the adenosine A2A receptor. The Na+ binding pocket collapses in the active state, making high-affinity agonist binding and Na+ binding mutually exclusive. The reduced Na+ sensitivity of NTSR1-GW5 suggests stabilization in a high-affinity agonist conformation that prevents Na+ ion entry.

### Pharmacological profile of thermostabilized NTSR1

NTSR1-GW5 maintains similar affinity for the agonist NTS (Kd 2.5 nM) compared to wild-type (Kd 1.5 nM), but shows a 130-200 fold increase in IC50 for the neutral antagonist SR48692 (1247 nM vs 9.3 nM for wild-type). The construct does not catalyze nucleotide exchange at Galpha q in response to NTS, suggesting the stabilizing mutations limit conformational propagation required for G protein activation. This pharmacological profile is similar to thermostabilized A2A receptor locked in an agonist-bound state.


## Cross-References

- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion replacing ICL3 in NTSR1-GW5-T4L construct
- [Decyl Maltoside (DM)](/xray-mp-wiki/reagents/detergents/decyl-maltoside/) — Detergent used for NTSR1 solubilization and thermostability measurement
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for NTSR1 solubilization and thermostability measurement
- [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/) — Non-peptide neurotensin receptor antagonist used in pharmacological characterization
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/allosteric-regulation/) — Na+ ion acts as negative allosteric effector on NTSR1 agonist binding
