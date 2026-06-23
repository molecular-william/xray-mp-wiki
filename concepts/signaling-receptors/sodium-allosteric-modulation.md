---
title: Sodium Ion Allosteric Modulation in GPCRs
created: 2026-06-02
updated: 2026-06-10
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-concepts]
sources: [doi/10.1038##nature11558, doi/10.1038##nature12944, doi/10.1038##nchembio.2547, doi/10.1126##science.1219218]
verified: false
---

# Sodium Ion Allosteric Modulation in GPCRs

## Overview
Sodium ions (Na+) act as negative allosteric modulators of many class A G protein-coupled receptors, stabilizing the inactive conformation and reducing agonist binding affinity. A highly conserved aspartate residue at position 2.50 (D2.50) serves as the key coordination site for a structurally bound Na+ ion within the transmembrane bundle. The Na+ binding pocket is located near the orthosteric ligand-binding site and its occupancy is mutually exclusive with high-affinity agonist binding, as the pocket collapses in the active receptor conformation. In opioid receptors, additional non-conserved residues (e.g., Asn131 at position 3.35 in the δ-OR) contribute to sodium coordination, creating subtype-specific modulation mechanisms.


## Mechanism/Details
The Na+ ion binds to a conserved site in the transmembrane core of class A GPCRs, coordinated primarily by the carboxylate side chain of Asp2.50. Additional coordinating residues include backbone carbonyls from nearby helices and, in some receptor subtypes, polar side chains. The Na+ ion stabilizes the inactive state by constraining the conformational freedom of the transmembrane helices. Upon agonist binding, the receptor undergoes conformational changes that collapse the Na+ binding pocket, making Na+ binding and high-affinity agonist binding mutually exclusive. This mechanism explains why Na+ ions decrease agonist binding affinity and why thermostabilizing mutations that lock receptors in high-affinity agonist conformations reduce Na+ sensitivity. In the δ-OR, the non-conserved Asn131 (3.35) side chain uniquely coordinates the sodium ion, and mutations at this position create "efficacy switches" that modulate biased signaling.


## Examples in Membrane Protein Work
- Human Delta-Opioid Receptor (OPRD1) — High-resolution (1.8 A) structure reveals allosteric sodium site coordinated by Asp95 (2.50), Ser135 (3.39), Asn131 (3.35), and two water molecules. Non-conserved Asn131 (3.35) is unique to opioid receptors; ~70% of class A GPCRs have a hydrophobic residue at this position. Sodium affinity K_B = 13.3 mM; physiological concentration (140 mM) saturates the site. Mutations Asn131Ala and Asn131Val augment constitutive beta-arrestin signaling. Asp95Ala, Asn310Ala, Asn314Ala mutations transform classical antagonists into beta-arrestin-biased agonists, establishing sodium-coordinating residues as efficacy switches.

- Rat Neurotensin Receptor 1 (NTSR1) — Wild-type NTSR1 shows Na+ sensitivity with IC50 of 43 mM for NaCl inhibition of [3H]NTS binding. The thermostabilized NTSR1-GW5 construct shows 5-fold reduced Na+ sensitivity (IC50 184-205 mM). Mutation of D113 (2.50) to alanine abolishes the Na+ ion effect, confirming the conserved Na+ binding site. The reduced Na+ sensitivity suggests NTSR1-GW5 is stabilized in a high-affinity agonist conformation.

- Adenosine A2A Receptor — First high-resolution structure (PDB 3EML) identified a structurally bound Na+ ion coordinated by D2.50 in the antagonist-bound inactive state. The Na+ binding pocket is located between TM3, TM5, and TM6, near the orthosteric site. Leu87 (3.35) points toward the lipidic membrane, in contrast to the polar Asn131 (3.35) in the δ-OR.
- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — The 1.8 A crystal structure of A2AAR-BRIL (PDB 4EY) revealed the sodium ion in the central water cluster coordinated by Asp52(2.50), Ser91(3.39), and three water molecules. The pocket involves highly conserved residues Asn24(1.50), Asp52(2.50), Ser91(3.39), Trp246(6.48), Asn280(7.45), Asn284(7.49), and Tyr288(7.53). Comparison with the active-like state (PDB 3QAK) shows the pocket collapses from 200 to 70 A^3 upon activation, precluding Na+ binding. Amiloride was docked into the Na+ site, with its guanidinium group interacting with Asp52(2.50).
- Guinea Pig Leukotriene B4 Receptor 1 (BLT1) — The crystal structure of BLT1 in complex with BIIL260 (PDB 5X33, 3.7 A) revealed that the benzamidine moiety of BIIL260 occupies the sodium ion-binding site, coordinating with D66 (2.50), V69 (2.53), S106 (3.39), W236 (6.48), and S276 (7.45). Biochemical assays confirmed that sodium ions decrease LTB4 binding to BLT1 in a concentration- dependent manner (IC50 in the millimolar range), and that BIIL260 competes with sodium ions for the allosteric site. Higher NaCl concentrations can displace BIIL260 from the sodium-binding site, restoring LTB4 binding. This demonstrates that BLT1 follows the conserved pattern of sodium ion-mediated allosteric modulation in class A GPCRs.


## Related Concepts


## Cross-References
- [Human Delta-Opioid Receptor (OPRD1)](/xray-mp-wiki/proteins/gpcr/delta-opioid-receptor/) — Detailed characterization of allosteric sodium site at 1.8 A
- [Adenosine A2A Receptor D52N Mutant](/xray-mp-wiki/proteins/gpcr/a2aar-d52n/) — Key residue D2.50 identified as Na+ coordination site in A2A receptor
- [Rat Neurotensin Receptor 1 (NTSR1)](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/) — NTSR1-D113 (2.50) mutation abolishes Na+ sensitivity
- [Efficacy Switches in GPCR Signaling](/xray-mp-wiki/concepts/signaling-receptors/efficacy-switches/) — Sodium-coordinating residues function as efficacy switches
- [Guinea Pig Leukotriene B4 Receptor 1 (BLT1)](/xray-mp-wiki/proteins/gpcr/blt1/) — BLT1 shows conserved sodium ion allosteric modulation; benzamidine moiety of BIIL260 mimics the sodium ion
- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — 1.8 A structure reveals Na+ coordination by Asp52(2.50), Ser91(3.39) and three waters in the central cluster
