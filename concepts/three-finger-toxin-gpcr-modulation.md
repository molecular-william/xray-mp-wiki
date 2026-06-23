---
title: Three-Finger Toxin Scaffold for GPCR Modulation
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-structural, concept-functional, xray-crystallography]
sources: [doi/10.1126##science.aax2517]
verified: false
---

# Three-Finger Toxin Scaffold for GPCR Modulation

## Overview
Three-finger toxins (3FTs) are a superfamily of small protein toxins (65-80 amino acids) found in the venom of elapid snakes (cobras, mambas, kraits). They are characterized by a conserved structural fold consisting of three beta-stranded loops (fingers) emanating from a central hydrophobic core stabilized by four conserved disulfide bonds. Despite high sequence and structural similarity, 3FTs exhibit diverse biological activities by targeting different receptors and ion channels. Among these, muscarinic toxins (MTs) are a subclass that bind allosterically to muscarinic acetylcholine receptors (mAChRs) with remarkable subtype selectivity. The three-finger fold is emerging as a promising scaffold for developing protein-based GPCR modulators, as demonstrated by the successful re-engineering of [MT7](/xray-mp-wiki/reagents/ligands/mt7/) to [Tx24](/xray-mp-wiki/reagents/ligands/tx24/) with redirected selectivity from [M1](/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/) to [M2](/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/) muscarinic receptors.


## Mechanism/Details
Three-finger toxins (3FTs) are characterized by a flat, leaf-like structure with three protruding loops (fingers I, II, III) that form the binding interface with target proteins. The conserved structural core consists of four invariant disulfide bonds (C1-C4, C2-C4, C3-C2, C3-C4 in the numbering scheme) that stabilize the fold. The finger loops exhibit high sequence variability, which underlies the diverse functional specificity across the 3FT family.
In the context of GPCR modulation, muscarinic toxins (MTs) from mamba venom bind to the extracellular vestibule of mAChRs, interacting primarily via finger loop 2, which inserts deep into the receptor's extracellular binding pocket. The structure of the [M1 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/)-[MT7](/xray-mp-wiki/reagents/ligands/mt7/) complex (PDB 6WJC) revealed that finger loop 2 stabilizes an outward movement of TM6, ECL3, and TM7, preventing receptor activation. The same scaffold can be re-engineered through directed evolution by mutating residues in the finger loops to redirect receptor subtype selectivity, as demonstrated by the creation of [Tx24](/xray-mp-wiki/reagents/ligands/tx24/), which targets [M2 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/) instead of M1.
Key advantages of the 3FT scaffold for GPCR modulation include: (1) high stability due to the conserved disulfide framework; (2) modular binding interfaces where individual finger loops can be independently evolved; (3) the ability to achieve extreme subtype selectivity (>5 orders of magnitude); (4) the capacity for both positive and negative allosteric modulation; and (5) amenability to yeast surface display and in vitro evolution for affinity maturation and specificity retargeting.


## Examples in Membrane Protein Work
- [M1 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/) — [MT7](/xray-mp-wiki/reagents/ligands/mt7/) — natural 3FT with subnanomolar M1 affinity and >100,000-fold selectivity; PDB 6WJC
- [M2 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/) — [Tx24](/xray-mp-wiki/reagents/ligands/tx24/) — engineered 3FT with redirected M2 selectivity via 5 consensus mutations + affinity maturation

## Related Concepts
- [Allosteric Regulation](/xray-mp-wiki/concepts/allosteric-regulation/) — 3FTs bind allosterically to GPCR extracellular vestibules
- [Negative Allosteric Modulation](/xray-mp-wiki/concepts/negative-allosteric-modulation/) — MT7 acts as a NAM for M1AChR agonist activation
- [Positive Allosteric Modulation](/xray-mp-wiki/concepts/positive-allosteric-modulation/) — MT7/Tx24 act as PAMs for orthosteric antagonist binding
- [Extracellular Domain GPCR Allostery](/xray-mp-wiki/concepts/extracellular-domain-gpcr-allostery/) — 3FT binding occurs at the extracellular vestibule allosteric site

## Cross-References
- [MT7](/xray-mp-wiki/reagents/ligands/mt7/) — Prototypical 3FT GPCR modulator; target M1AChR
- [Tx24](/xray-mp-wiki/reagents/ligands/tx24/) — Engineered 3FT demonstrating scaffold retargetability
- [M1 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/) — Target of MT7; structural basis for 3FT-GPCR interaction (PDB 6WJC)
- [Human M2 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/) — Target of engineered Tx24 toxin
- [Atropine](/xray-mp-wiki/reagents/ligands/atropine/) — Orthosteric antagonist co-crystallized in M1AChR-MT7 complex
