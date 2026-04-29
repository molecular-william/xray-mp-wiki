---

title: Drug-Proton Antiporters (DHA)
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [transporter, membrane-protein]
sources: [doi/10.1016##j.bbrc.2020.11.096]

category: concepts
---
layout: default


# Drug-Proton Antiporters (DHA)

## Overview

Drug-proton antiporters (DHA) are a subfamily of the Major Facilitator Superfamily (MFS) that expel toxic compounds from cells using the proton-motive force. They are a major contributor to multi-drug resistance (MDR) in bacteria, pumping out antibiotics, detergents, dyes, and organic solvents.

## Classification

- **TCDB**: 2.A.1 (Drug:H⁺ Antiporter family)
- **Subfamilies**: DHA1, DHA2, etc.
- **SotB**: DHA1 family member from *E. coli*

## Mechanism

DHA transporters utilize the proton gradient across the membrane to drive the extrusion of toxic compounds:
1. **Proton binds** to the transporter (protonated state)
2. **Substrate binds** to the protonated transporter
3. **Conformational change** to outward-open state
4. **Substrate released** to the extracellular space
5. **Proton released** to the extracellular space
6. **Return to inward-open** state

Key feature: **Substrate binding and protonation compete** with each other. Substrate binding-induced deprotonation triggers the conformational change.

## Clinical Significance

- **Multi-drug resistance**: DHA transporters pump out multiple classes of antibiotics
- **Target for resistance reversal**: Inhibiting DHA transporters could restore antibiotic sensitivity
- **Broad substrate specificity**: Each DHA can transport multiple structurally unrelated compounds

## Known Members

| Organism | Transporter | Substrate Specificity |
|----------|------------|----------------------|
| *E. coli* | SotB (DHA1) | Multiple drugs, antibiotics |
| *E. coli* | EmrD (DHA2) | Ethidium, doxorubicin, detergents |
| *E. coli* | MdfA (DHA3) | Wide range of weak organic acids |
| *S. aureus* | NorA (DHA4) | Quaternary ammonium compounds |

## Related Transporters

- [sotb](//xray-mp-wiki/proteins/sotb/) — DHA1 family member, 4 conformations captured
- [nTMATE2-transporter](//xray-mp-wiki/proteins/nTMATE2-transporter/) — MATE family, different mechanism
- [acrB](//xray-mp-wiki/proteins/acrB/) — RND efflux pump, different superfamily
- [mfs-transporter](//xray-mp-wiki/concepts/mfs-transporter/) — Major Facilitator Superfamily overview