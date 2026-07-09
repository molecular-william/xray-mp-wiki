---
title: Cork-in-Bottle Occlusion
created: 2026-05-29
updated: 2026-05-29
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-concepts]
sources: [doi/10.1016##j.str.2018.02.004, doi/10.1038##NATURE14981]
verified: false
---

# Cork-in-Bottle Occlusion

## Overview
Cork-in-bottle occlusion is a mechanism of ion channel block in which a bound protein or ligand physically plugs the wide aqueous vestibule through which ions enter and leave the selective permeation pathway, without inducing allosteric conformational changes in the channel protein. The bound molecule acts like a cork in a bottle, physically occluding ion entry while leaving the channel's conductive pore structure unchanged. This mechanism was demonstrated for fluoride channel (Fluc) block by monobody chaperones.


## Mechanism/Details
In dual-topology Fluc channels, each subunit contributes to a wide aqueous vestibule at both membrane interfaces. Engineered monobody chaperones bind to these vestibules with their diversified loop inserting into the vestibule entrance, creating a ~950 A^2 mainly hydrophobic interface. The block is purely physical: the monobody's diversified loop sterically occludes the vestibule entrance, preventing fluoride ions from entering or leaving the selective permeation pathway. Electrophysiological recordings show that partial blockers (S8, S7) reduce current to ~10-15% of open rate (~900,000 F- ions/s), while complete blockers (L2, L3) reduce current to zero. The key structural evidence comes from the Bpe-S8 asymmetric structure (PDB 6BQO), where only one end of the channel binds a monobody, yet both ends are structurally identical to each other and to all previously solved doubly-bound structures. This proves that monobody binding does not induce local or global allosteric changes in the channel pore.


## Examples in Membrane Protein Work
- [Fluoride Channel from B. pertussis (Bpe)](/xray-mp-wiki/proteins/other-ion-channels/bpe-fluoride-channel/) — [Monobody S8](/xray-mp-wiki/reagents/protein-tags/monobody-s8/) binds to one end of the Bpe homodimer (PDB 6BQO), physically occluding the aqueous vestibule. The ~950 A^2 interface is mainly hydrophobic with rare peripheral hydrogen bonds. S8 causes partial block (~10% residual conductance at 2 uM concentration, 20 ms block events). Both channel ends are structurally identical despite only one being bound, proving no allosteric mechanism.
- [Fluoride Channel from B. pertussis (Bpe)](/xray-mp-wiki/proteins/other-ion-channels/bpe-fluoride-channel/) — [Monobody L3](/xray-mp-wiki/reagents/protein-tags/monobody-l3/) causes complete block of fluoride current (tens of seconds block events) upon binding. Despite complete functional block, the underlying channel structure remains identical to the partially blocked S8-bound state, supporting the physical occlusion model rather than allosteric closure.
- [Fluoride Channel from B. pertussis (Bpe)](/xray-mp-wiki/proteins/other-ion-channels/bpe-fluoride-channel/) — [Monobody S7](/xray-mp-wiki/reagents/protein-tags/monobody-s7/) binds to both ends of the Bpe homodimer (PDB 5A40, 3.6 A). S7 extends a long loop deep into each vestibule, occluding much of the channel's water-exposed surface. The Bpe-S7 structure demonstrates that monobody binding does not induce local structural changes in the channel.
- [Fluoride Channel from B. pertussis (Bpe)](/xray-mp-wiki/proteins/other-ion-channels/bpe-fluoride-channel/) — [Monobody L2](/xray-mp-wiki/reagents/protein-tags/monobody-l2/) binds to both ends of the Bpe homodimer (PDB 5A41, 2.1 A). L2 binds in a different orientation than S7 but also extends a long loop into each vestibule. The backbone conformation of the channel is identical to Bpe-S7 (C-alpha r.m.s.d. 0.4 A), confirming the physical occlusion model without allosteric changes.

## Related Concepts


## Cross-References
- [Fluoride Channel from B. pertussis (Bpe)](/xray-mp-wiki/proteins/other-ion-channels/bpe-fluoride-channel/) — Cork-in-bottle occlusion demonstrated by Bpe-S8 asymmetric structure (PDB 6BQO)
- [Monobody S7](/xray-mp-wiki/reagents/protein-tags/monobody-s7/) — Engineered inhibitor used in Bpe-S7 crystallization (PDB 5A40)
- [Monobody L2](/xray-mp-wiki/reagents/protein-tags/monobody-l2/) — Engineered inhibitor used in Bpe-L2 crystallization (PDB 5A41)
- [Monobody S9](/xray-mp-wiki/reagents/protein-tags/monobody-s9/) — Homologous monobody used to crystallize Ec2-S9 (PDB 5A43)
- [Fluoride Channel from E. coli (Ec2)](/xray-mp-wiki/proteins/other-ion-channels/fluc-ec2/) — Ec2-S9 complex also demonstrates monobody-mediated physical occlusion
- [Dual-Topology Channels](/xray-mp-wiki/concepts/transport-mechanisms/dual-topology-channels/) — Cork-in-bottle mechanism applies specifically to dual-topology Fluc channels with symmetric vestibules
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — Cork-in-bottle occlusion is the alternative to allosteric closure as a channel block mechanism
- [Monobody L3](/xray-mp-wiki/reagents/protein-tags/monobody-l3/) — Fusion tag for crystallization or purification
- [Monobody S8](/xray-mp-wiki/reagents/protein-tags/monobody-s8/) — Fusion tag for crystallization or purification
