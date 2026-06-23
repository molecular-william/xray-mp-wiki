---
title: Glucose/H+ Symport Mechanism
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-functional, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1311485110]
verified: false
---

# Glucose/H+ Symport Mechanism

## Overview
The glucose/H+ symport mechanism describes how members of the
[Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/major-facilitator-superfamily/)
couple the translocation of glucose to the electrochemical proton gradient.
This mechanism is distinct from the facilitated diffusion used by most human
GLUT glucose transporters. The crystal structure of GlcP_Se from
[Staphylococcus epidermidis](/xray-mp-wiki/proteins/mfs-transporters/glcp-se/) provided a
detailed structural basis for this process.


## Mechanism/Details
The mechanism involves a six-step cycle adapted from the LacY model, with the key difference being the location of the H+-binding site:

1. **Resting state (no H+, no glucose):** D22 (helix 1) and R102 (helix 4) form a salt bridge that juxtaposes helices 1 and 4, holding the substrate cavity wide open toward the cytoplasm (inward-facing).

2. **H+ binding:** At low pH, H+ binds to D22, disrupting the salt bridge with R102. Helices 1 and 4 rearrange to decrease the cavity size, lowering the energetic barrier for conformational transitions. This primes the transporter for substrate binding.

3. **Glucose binding:** Glucose binds through residues on helices 5 (Q137), 7 (Q250, Q251, N256), and 10 (W357). Substrate binding brings the N- and C-terminal domains closer together, facilitating the transition to the outward-facing state.

4. **Conformational transition:** The structure undergoes a 24-degree relative rotation of the N and C domains around an axis through the substrate-binding site, transitioning from inward- to outward-facing. In the outward-facing state, Q137 and W357 reposition to coordinate glucose in the binding pocket.

5. **Glucose release:** In the inward-facing conformation, helices 5 and 10 move away from the center, dislocating Q137 and W357 from the glucose-binding site and opening the cavity toward the cytoplasm for glucose release.

6. **H+ release:** After glucose exits, H+ is released from D22, allowing D22 to re-form the salt bridge with R102 and return the transporter to its wide-open resting conformation.

**Structural basis for symport vs. uniport:** The presence of an acidic residue at the position corresponding to D22 (helix 1, cytoplasmic end) is necessary but not sufficient for H+ symport. Human GLUTs with Asn at this position (GLUT1, -3, -4, -5, -7, -9, -11) are uniporters. GLUT12 (Glu) and GLUT13 (Asp) are H+ symporters. GLUT2 has Asp but is a uniporter because an adjacent Ser (S161) hydrogen bonds to the carboxylate, altering the H+-binding environment — this was confirmed by the I105S mutation in GlcP_Se that converted it to a uniporter.

## Examples in Membrane Protein Work
- [GlcP_Se (Staphylococcus epidermidis Glucose/H+ Symporter)](/xray-mp-wiki/proteins/mfs-transporters/glcp-se/) — Inward-facing structure at 3.2 A revealing the H+-binding site (D22-R102 salt bridge)
- [LacY (Lactose Permease)](/xray-mp-wiki/proteins/mfs-transporters/lac-y/) — Most intensively studied MFS H+ symporter; model for the GlcP_Se mechanism

## Related Concepts
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/major-facilitator-superfamily/) — GlcP_Se is a member of the MFS; the symport mechanism is an MFS transport paradigm
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — The general transport mechanism adapted for H+ coupled symport

## Cross-References
- [GlcP_Se (Staphylococcus epidermidis Glucose/H+ Symporter)](/xray-mp-wiki/proteins/mfs-transporters/glcp-se/) — Protein whose structure revealed the symport mechanism
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/major-facilitator-superfamily/) — GlcP_Se is a member of the MFS; the symport mechanism is an MFS transport paradigm
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Physiological substrate of GlcP_Se and all GLUT transporters
