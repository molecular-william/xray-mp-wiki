---
title: Channel Gating via Plug Domain Displacement
created: 2026-05-28
updated: 2026-05-28
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, membrane-protein]
sources: [doi/10.1016##j.molcel.2007.05.002]
verified: false
---

# Channel Gating via Plug Domain Displacement

## Overview
Channel gating in the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) translocation channel is mediated by the displacement of the plug helix (TM2a), a short alpha helix that seals the periplasmic side of the channel in its closed state. The plug acts as both a seal preventing ion flux and a lock stabilizing the closed conformation through contacts with the lateral gate (TM2b/TM7) and the pore ring. During protein translocation, signal sequence intercalation at the lateral gate pulls on the plug, displacing it and allowing the lateral gate helices to separate and the pore ring to widen for polypeptide passage.


## Mechanism/Details
In the resting state, the plug helix sits in the periplasmic funnel abutting the pore ring. It makes extensive contacts with TM2b and TM7 (the lateral gate helices) as well as with the six hydrophobic residues forming the pore ring. This network of interactions locks the channel in a closed conformation, preventing uncontrolled membrane permeability.
During translocation, the hydrophobic core of a signal sequence inserts as a loop between TM2b and TM7 at the cytoplasmic lateral gate. This intercalation requires spontaneous separation of the lateral gate helices, which may be facilitated by [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) dimerization or binding of channel partners such as the ribosome or SecA. As the signal sequence inserts, TM2b moves and pulls on the terminal residues of the adjacent plug domain. This reduces the number of plug residues available to interact within the extra-cytoplasmic funnel, destabilizing the plug-lateral gate and plug-pore ring contacts. The major consequence is that the plug no longer stabilizes the closed state, allowing the pore ring to widen and the channel to open for the translocating polypeptide chain.
The plug domain is poorly conserved in sequence among different species, suggesting that the only sequence requirements are hydrophobic and alpha-helix-forming residues, along with flexible linkers (PPhiXG at the N terminus and GPhiXP at the C terminus, where Phi is a hydrophobic residue) on either side to allow plug movement during translocation.


## Examples in Membrane Protein Work
- **Methanococcus jannaschii [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/)**: Crystal structures of plug deletion mutants
  (Delta60-65 and Delta57-67) show that new helical plugs form from adjacent sequences
  but lack the stabilizing contacts of the wild-type plug, explaining why deletion
  mutants are functional but have destabilized closed states. The new plugs interact
  weakly with the lateral gate, allowing easier channel opening.
- **E. coli [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/)**: Plug deletion mutants are functional in vivo and in vitro, and
  act as strong suppressors of defective or missing signal sequences (prl phenotype).
  The destabilized closed state allows translocation of proteins even without proper
  signal sequence recognition.
- **Saccharomyces cerevisiae Sec61p**: Plug deletion mutants in the eukaryotic
  homolog are also functional, indicating that plug-mediated gating is a conserved
  mechanism across all domains of life.


## Related Concepts
- Signal sequence recognition and lateral gate opening
- Pore ring dynamics during translocation
- Ribosome-channel coupling during cotranslational translocation


## Cross-References
- [Thermus thermophilus SecY Core Channel Subunit](/xray-mp-wiki/proteins/secretion-translocon/secy/) — Structural basis for plug-mediated gating of the SecY channel
- [Thermus thermophilus SecYEG Translocon Complex](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) — Full heterotrimeric complex with lateral gate architecture involved in gating
- [Scissor-Switch Gating](/xray-mp-wiki/concepts/scissor-switch-gating/) — Alternative channel gating mechanism in GPCR families
