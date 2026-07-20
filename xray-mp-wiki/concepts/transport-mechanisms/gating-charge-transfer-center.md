---
title: "Gating Charge Transfer Center in Voltage Sensors"
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-functional, membrane-protein, subdirectory-transport-mechanisms]
sources: [doi/10.1126##science.1185954]
verified: regex
---

# Gating Charge Transfer Center in Voltage Sensors

## Overview
The gating charge transfer center is a conserved structural feature in voltage-sensor domains (VSDs) of voltage-dependent ion channels. It consists of an occluded binding site formed by a highly conserved phenylalanine residue (Phe233 in Kv2.1 paddle chimera) on the S2 helix, together with negatively charged glutamate and aspartate residues, that catalyzes the transfer of positively charged amino acids on the S4 helix (gating charges) across the membrane electric field. By providing an energetically favorable environment for gating charges as they cross the low-dielectric membrane interior, this center lowers the energy barrier for voltage-dependent conformational changes.


## Mechanism/Details
The gating charge transfer center was identified and characterized in the Shaker K+ channel and the paddle-chimera Kv channel (Kv1.2-Kv2.1 chimera) through combined crystallographic and electrophysiological studies (Tao et al., Science 2010).

**Structural organization.** In the crystal structure of the open (depolarized) voltage sensor, the transfer center is located between the extracellular negative cluster and the intracellular negative cluster. It is formed by:

1. **Phe233 (S2 helix):** A highly conserved phenylalanine that forms the extracellular lid of the occluded binding site. This residue is conserved in Kv, Nav, Cav, Hv channels, and voltage-sensitive phosphatases (VSP).

2. **Glu and Asp (S2/S3):** Negatively charged residues below Phe233 that form ionized hydrogen bonds with the positively charged side chain at position 5 (K5 or R5) on S4.

**Distinct binding for different S4 positions.** The occluded site interacts with different positively charged residues on the S4 helix depending on the voltage sensor conformation:

- In the **open (depolarized) conformation**, the positively charged residue at position 5 (K5/R5) on S4 binds in the occluded site, stabilized by interactions with the conserved Glu and Asp below and the Phe lid above.

- In the **closed (hyperpolarized) conformation**, evidence suggests that the positively charged residue at position 1 (R1/K1) on S4 binds in the same occluded site. The alpha-carbon distance between positions 1 and 5 along S4 is approximately 21 A (18 A perpendicular to the membrane), consistent with the 15-20 A gating charge movement inferred from biotin-avidin accessibility studies.

This means the occluded site serves as a central waypoint that sequentially accommodates each gating charge as it crosses the membrane.

**Lys vs. Arg discrimination.** Mutagenesis of Phe233 revealed that the site's selectivity between lysine and arginine can be altered:

- Mutation of Phe233 to Trp (F233W) slows channel closing when Lys is at position 5 (R1K5(W)), indicating Lys stabilizes the open conformation.
- The F233W mutation slows channel opening when Lys is at position 1 (K1R5(W)), indicating Lys stabilizes the closed conformation.
- Arg at position 5 in the presence of Trp produces faster closure and separates ~25% of gating charge movement as a distinct component associated with pore opening.

These observations support a model in which the occluded site binds the S4 charge at position 1 in the closed state and at position 5 in the open state, acting as a catalytic center that lowers the energy barrier for charge transfer across the membrane.

**Implications for gating.** A five-state model was proposed in which each of the S4 positive charges (positions 1-5) sequentially occupies the occluded site as the voltage sensor transitions from fully closed (state 1) to fully open (state 5). Each transition carries ~25% of the total gating charge. The final transition (state 4 to 5), in which position 5 binds the occluded site, is closely associated with pore opening. This explains why ~25% of the gating charge movement is separable as a late component that correlates with pore opening.


## Examples in Membrane Protein Work
- [Shaker Kv1.2](/xray-mp-wiki/proteins/voltage-gated-channels/shaker-kv1-2/) — Mutagenesis of Phe233 in Shaker channel established the functional role of the occluded site in gating charge transfer
- [Paddle-Chimaera Channel](/xray-mp-wiki/proteins/voltage-gated-channels/paddle-chimaera-channel/) — Crystal structure of the open conformation at 2.4 A revealed the occluded site with Phe233, Glu, and Asp forming the gating charge transfer center. Crystal structure of F233W mutant at 2.9 A confirmed the site remains intact

## Related Concepts
- []() — The voltage-sensor paddle (S3b-S4) carries the gating charges that pass through the transfer center during voltage-dependent conformational changes
- []() — The gating charge transfer center is a potential target for state-dependent inhibitors that stabilize specific voltage sensor conformations

## Cross-References
- [Shaker Kv1.2 Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/shaker-kv1-2/) — Primary model system for functional characterization of the gating charge transfer center via Phe233 mutagenesis
- [Paddle-Chimaera Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/paddle-chimaera-channel/) — Crystal structure revealed the atomic architecture of the occluded binding site
- [Voltage-Sensor Paddle](/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/) — The S3b-S4 paddle carries the gating charges that translocate through the transfer center
