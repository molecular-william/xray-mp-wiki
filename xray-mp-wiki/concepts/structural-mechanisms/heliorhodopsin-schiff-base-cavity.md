---
title: "Heliorhodopsin Schiff Base Cavity"
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-structural, concept-functional, membrane-protein, subdirectory-structural-mechanisms]
sources: [doi/10.1073##pnas.1915888117]
verified: regex
---

# Heliorhodopsin Schiff Base Cavity

## Overview
The Schiff base cavity (SBC) is a large hydrophilic cavity located in the cytoplasmic part of heliorhodopsins (HeRs), adjacent to the retinal Schiff base (RSB). It is a defining structural feature that distinguishes HeRs from all other known microbial rhodopsins. The SBC is filled with a cluster of water molecules and surrounded by highly conserved charged and polar residues that create an extensive hydrogen bonding network. Unlike bacteriorhodopsin and other type-1 rhodopsins where specific aspartate or glutamate residues serve as proton acceptors, the SBC water cluster in HeRs is proposed to function as the primary proton reservoir, temporarily storing the proton released from the RSB during the photocycle.


## Mechanism/Details
Structure and Composition

In HeR-48C12 at pH 8.8, the SBC is located between residues Glu107 and Arg104, separated from the cytoplasmic bulk by only the side chain of Asn101. The cavity is surrounded by:
- Charged residues: Glu107 (RSB counterion), His23, His80, Arg104, Glu230
- Polar residues: Asn16, Tyr92, Asn101, Tyr108, Ser237
- Additional interacting residues: Glu149, Tyr226, Trp105, Gln213, Gln216

The cavity contains six well-ordered water molecules creating a dense hydrogen bonding network extending from the RSB to Arg104. The RSB is directly hydrogen bonded to Glu107 and Ser237. Glu107 (analogous to Asp85 in bacteriorhodopsin) serves as the RSB counterion but is not the proton acceptor.

Comparison with Other Rhodopsins

In bacteriorhodopsin, Asp85 serves as both the RSB counterion and primary proton acceptor. In HeR-48C12, Glu107 is the RSB counterion, but mutational studies showed that neither Glu107, His23, His80, nor any single charged residue acts as the proton acceptor. The hydrophobic extracellular interior prevents proton transfer to the extracellular side. This led to the proposal that the water cluster itself functions as the proton reservoir.

Anion Binding at Low pH

At pH 4.3, a planar triangular molecule (acetate from the crystallization buffer, or potentially nitrate/bicarbonate) binds in the SBC. The acetate is hydrogen bonded to Glu107 (protonated/neutralized at low pH) and the water network. This explains why HeRs can bind exogenous anions under acidic conditions or when the counterion is mutated. Similar anion binding has been demonstrated in the archaeal HeR TaHeR at low pH.

Functional Significance

The SBC is proposed to function as an "active site" for substrate binding in HeR-48C12. The proton released from RSB during the photocycle might interact with a substrate in the reaction H+ + substrate- -> reduced substrate, analogous to carbon fixation processes. The SBC is connected to the cytoplasmic bulk via two pathways: (1) past the Asn101 residue at the hydrophobic/hydrophilic interface, and (2) through the Arg104 gate. These pathways could allow substrate access and product release.

Conservation Across HeRs

The SBC residues (His23, His80, Asn101, Tyr108, Asn16, Glu230, Arg104, Tyr92) and the hydrophobic barrier residues (Leu12, Leu96, Leu227) are almost completely conserved across all HeR subfamilies. This conservation, together with the hydrophobic extracellular organization, supports the functional importance of the SBC as a defining feature of the heliorhodopsin family.


## Examples in Membrane Protein Work
- [HeR-48C12](/xray-mp-wiki/proteins/rhodopsins/heliorhodopsin-48c12/) — SBC contains six water molecules at pH 8.8; acetate binds at pH 4.3. Water cluster proposed as proton acceptor.
- [Heliorhodopsin TaHeR](/xray-mp-wiki/proteins/rhodopsins/heliorhodopsin-taher/) — SBC with water molecules at pH 8.0; chloride ion binds at pH 4.5. Analogous anion-binding behavior confirmed.

## Related Concepts
- [Retinal Chromophore Conformation](/xray-mp-wiki/concepts/structural-mechanisms/retinal-chromophore-conformation/) — The RSB is part of the retinal chromophore; the SBC directly interacts with the RSB
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — The SBC water cluster mediates proton transfer during the HeR photocycle
- [Proton Wire](/xray-mp-wiki/concepts/transport-mechanisms/proton-wire/) — The hydrogen bonding network in the SBC functions as a proton wire connecting RSB to Arg104 and protein surface

## Cross-References
- [Heliorhodopsin 48C12](/xray-mp-wiki/proteins/rhodopsins/heliorhodopsin-48c12/) — HeR-48C12 is the model system in which the SBC was structurally characterized at 1.5 A
- [Heliorhodopsin TaHeR](/xray-mp-wiki/proteins/rhodopsins/heliorhodopsin-taher/) — Archaeal HeR shows analogous SBC with chloride binding at low pH
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Comparison reveals that HeR SBC replaces the Asp85 proton acceptor with a water cluster
