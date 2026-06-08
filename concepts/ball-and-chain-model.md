---
title: Ball-and-Chain Model for SLC38A9
created: 2026-05-29
updated: 2026-05-29
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, subdirectory-concepts]
sources: [doi/10.1016##j.str.2020.11.014]
verified: false
---

# Ball-and-Chain Model for SLC38A9

## Overview
The ball-and-chain model describes a conformational regulation mechanism in SLC38A9 where the N-terminal domain (N-plug) acts as a dynamic plug that inserts into or releases from the substrate-binding pocket in response to luminal arginine levels. At low arginine, the N-plug samples both inserted and released states, with the inserted state blocking transport. At high arginine, arginine occupies the binding site and the N-plug is released, making it available to interact with the Rag GTPase complex. This dual function — transporting arginine while simultaneously serving as a signaling module — provides a direct molecular link between lysosomal amino acid availability and mTORC1 activation.


## Mechanism/Details
The N-plug of SLC38A9 (residues 1-96) folds into a beta hairpin stabilized by hydrogen bonds between Ser80-Glu82, His76, and Tyr85. In the absence of arginine, this beta hairpin inserts deep into the transmembrane domain, occupying the substrate binding pocket where arginine normally binds. The vestibule into which the N-plug inserts measures approximately 20 A in diameter. Structural superposition of the N-plug bound state (PDB: 7KGV) with the arginine-bound state (PDB: 6C08) shows that the same set of backbone atoms are used for binding both molecules, confirming competitive binding between the N-plug and arginine.
When luminal arginine concentration increases, arginine molecules enter the binding site from the luminal side. The N-plug is displaced and released from the binding pocket. In this released state, the N-plug becomes available for two functions: (1) it can interact with the Rag GTPase complex (drRagA and drRagC) at the lysosomal surface through the conserved 85PDH87 motif and Pro 85/Pro 90 residues, triggering mTORC1 activation; and (2) it facilitates the efflux of other essential amino acids such as leucine from the lysosome.
Mutational analysis confirms the N-plug's inhibitory role. Triple site mutants (V77W, H81W, Y87F) that disrupt N-plug binding show 2-fold lower Km for arginine without significant Vmax change. Deleting the N-plug or mutating it to a helical structure (predicted by PEP-FOLD) eliminates the arginine-enhanced leucine transport characteristic of wild-type drSLC38A9.


## Examples in Membrane Protein Work


## Related Concepts


## Cross-References
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Ball-and-chain is a regulatory mechanism layered on top of alternating access
- [Conformational Dynamics in MFS Transporters](/xray-mp-wiki/concepts/conformational-dynamics-mfs/) — N-plug insertion represents a conformational change in the transporter
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/allosteric-regulation/) — Arginine binding allosterically regulates N-plug binding and release
