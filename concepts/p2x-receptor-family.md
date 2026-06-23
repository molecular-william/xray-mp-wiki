---
title: P2X Receptor Family
created: 2026-06-02
updated: 2026-06-02
type: concept
category: concepts
layout: default
tags: [concept-protein-family, membrane-protein]
sources: [doi/10.1038##nature08198, doi/10.1038##nature11010]
verified: false
---

# P2X Receptor Family

## Overview
The P2X receptor family comprises a group of ligand-gated ion channels activated by extracellular adenosine triphosphate (ATP). P2X receptors form homotrimers (and potentially heterotrimers in some cases), with each subunit containing two transmembrane helices (TM1 and TM2), a large extracellular ATP-binding domain, and intracellular N- and C-terminal tails. They are widespread in the nervous system, immune system, and cardiovascular system, mediating fast excitatory neurotransmission, inflammation, pain sensation, and vasodilation. Seven mammalian P2X subtypes have been identified (P2X1 through P2X7), each with distinct pharmacological properties, ion selectivity, and tissue distribution.


## Mechanism/Details
P2X receptors belong to the Cys-loop superfamily of ligand-gated ion channels, sharing a common extracellular domain architecture with nicotinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptors, GABA_A receptors, [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) receptors, and 5-HT3 receptors. The extracellular domain contains a canonical ATP-binding site located at the interface between subunits, involving a conserved asparagine residue (N78 in [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/)) and surrounding loop structures.
The transmembrane domain consists of two alpha helices per subunit. TM1 and TM2 each span the membrane approximately once, with a short re-entrant loop between TM1 and TM2 that contributes to the pore lining. The gate is located in the TM2 helix around residue L340 ([Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/) numbering), with additional gate residues including G343, A344, and A347. The pore is closed in the resting state and opens upon ATP binding, allowing monovalent and divalent cations (Na+, K+, Ca2+) to pass.
P2X receptors are divided into three functional classes based on desensitization kinetics: fast-desensitizing (P2X1, P2X3, P2X5), intermediate-desensitizing (P2X2, P2X4, P2X6), and slow-desensitizing (P2X7). P2X7 is unique in forming a large pore upon prolonged ATP activation, associated with inflammatory responses.
The [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/) crystal structure (PDB 3PHV) revealed the overall fold of the P2X receptor extracellular domain, the arrangement of transmembrane helices, and the closed conformation of the ion channel pore. The structure was solved from two crystal forms (R3 and R32 space groups) using [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) MAD phasing, providing atomic-resolution insights into ATP-gated ion channel architecture.
The ATP binding site in [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/) exhibits strong nucleotide base selectivity. Competition assays showed IC50 values of 14.2 nM for ATP, 391.0 nM for CTP, 55.5 uM for GTP, and 64.8 uM for UTP. The binding pocket involves hydrogen bonding interactions with residues including T189, K72, R143, K70, K193 and hydrophobic interactions with I232, L191, L217, A292, V291. Comparison of ATP-bound and apo zfP2X4-C structures reveals a 5 degree rotation movement of the lower body domain upon ATP binding, classified as 99.9% closure motion by Dyndom analysis. Structural coupling between the dorsal fin, left flipper, and lower body domains transmits the ATP-binding signal to the transmembrane domain.


## Examples in Membrane Protein Work
- **[Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/) (zebrafish P2X4)**: First P2X receptor structure solved (PDB 3PHV).
  The wild-type receptor has an EC50 of 1730 uM for ATP. [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) of flexible
  termini (Delta N27/Delta C8) improved ATP sensitivity (EC50 = 27.4 uM).
  Additional mutations (C51F/N78K/N187R) further improved sensitivity (EC50 = 3.4 uM)
  and enabled crystallization in a higher-resolution form.
- **hP2X4 (human P2X4)**: Shares approximately 86% sequence identity with [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/).
  Involved in pain sensation, neuroinflammation, and synaptic plasticity.
- **rP2X4 (rat P2X4)**: Used extensively in electrophysiological studies.
  Western blot analysis confirmed glycosylation and trimeric assembly.
- **hP2X1, hP2X2, hP2X3, hP2X5**: Other human P2X subtypes showing conserved
  cysteine disulfide bonds and transmembrane architecture. Sequence alignment
  with [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/) reveals highly conserved residues in the transmembrane domain
  and ATP-binding region.


## Related Concepts
- Ligand-gated ion channels (pLGIC superfamily)
- ATP-gated ion channels
- Ion channel gating mechanisms
- Pentameric ligand-gated ion channels
- Cys-loop receptor superfamily


## Cross-References
- [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Bacterial pLGIC homolog; shared extracellular domain fold with Cys-loop receptors
- [GluCl (GABA-Gated Chloride Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glucl/) — Pentameric ligand-gated ion channel; comparison of gating mechanisms
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — Orthosteric agonist for all P2X receptors
- [Channel Gating via Plug Domain Displacement](/xray-mp-wiki/concepts/channel-gating/) — Gating mechanism comparison across ion channel families
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/allosteric-regulation/) — P2X receptors exhibit allosteric modulation by various ligands and ions
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) — Related biological concept
- [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/) — Related protein structure
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Additive used in purification or crystallization buffers
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Buffer component used in purification or crystallization
- [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) — Related ligand or cofactor
