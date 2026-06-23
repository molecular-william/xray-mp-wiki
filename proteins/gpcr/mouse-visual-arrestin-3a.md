---
title: Mouse Visual Arrestin (3A)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14656]
verified: false
---

# Mouse Visual Arrestin (3A)

## Overview

Mouse visual arrestin 1 (arrestin-1) is a cytosolic protein that binds to phosphorylated [G Protein](/xray-mp-wiki/concepts/g-protein)-coupled receptors (GPCRs) to terminate [G Protein](/xray-mp-wiki/concepts/g-protein) signaling and redirect signaling to G-protein-independent pathways. The 3A mutant (L374A, V375A, F376A) in the C-terminal tail adopts a pre-activated conformation that binds to activated receptors with high affinity without requiring receptor phosphorylation. The crystal structure of the 3A arrestin bound to constitutively active human rhodopsin (E113Q/M257Y) revealed the molecular basis for arrestin recruitment and biased signaling.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature14656 | not determined | 3.8 A | P212121 | Mouse visual arrestin 1 (residues 12-361, with missing loop 340-342), 3A mutant (L374A/V375A/F376A) | Human rhodopsin (E113Q/M257Y) |

## Expression and Purification

- **Expression system**: HEK293S cells for fusion protein expression. In vitro translation for pull-down assays with 35S labeling.

- **Construct**: 3A arrestin mutant (L374A/V375A/F376A, residues 10-392) fused at C-terminus of rhodopsin-T4L fusion via 15 amino acid linker (AAAGSAGSAGSAGSA)


### Purification Workflow

- **Expression system**: In vitro translation (for pull-down assays)
- **Expression construct**: 3A arrestin (L374A/V375A/F376A, residues 10-392)
- **Tag info**: 35S-labeled for pull-down assays

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| In vitro translation | Cell-free translation | -- | not specified + not specified | Labeled with 35S for bead binding pull-down assays |
| Bead binding pull-down | Amylose bead pull-down | Amylose beads | not specified + not specified | Wild-type arrestin has weak background binding to wild-type rhodopsin; 3A arrestin shows strong binding |

**Final sample**: Complex with rhodopsin purified as fusion protein
**Yield**: not specified
**Purity**: not specified


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Pre-activated arrestin conformation

The 3A arrestin mutant (L374A, V375A, F376A) in the C-terminal tail adopts
a pre-activated conformation that obviates the need for receptor phosphorylation
for high-affinity binding. In the absence of all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal), the 3A arrestin
shows a nearly 30-fold increase in binding to the E113Q/M257Y rhodopsin mutant
compared to wild-type arrestin. Upon binding to activated rhodopsin, arrestin
undergoes a ~20 degree rotation between its amino and carboxy domains, opening
a cleft that accommodates the ICL2 helix of rhodopsin.

### Arrestin interface with rhodopsin

The rhodopsin-arrestin interface involves four distinct patches: (1) the
arrestin finger loop (residues Q70-L78) forming a short alpha helix that
interacts with TM7 and helix 8 of rhodopsin; (2) the arrestin middle loop
(V140 region) and C loop (Y251 region) interacting with rhodopsin ICL2;
(3) the arrestin beta strand (residues 79-86) interacting with rhodopsin
TM5, TM6, and ICL3; (4) the arrestin N-terminal beta strand (residues 11-19)
interacting with the rhodopsin C-terminal tail. The asymmetric binding
arrangement brings the arrestin C domain toward the membrane, with conserved
hydrophobic residues (F197, F198, M199, F339, L343) at the C tip potentially
functioning as a lipid-interacting module.


## Cross-References

- [Human Rhodopsin E113Q/M257Y Mutant](/xray-mp-wiki/proteins/gpcr/human-rhodopsin-e113q-m257y/) — Arrestin binding partner in the rhodopsin-arrestin complex structure
- [Beta-Arrestin Signaling](/xray-mp-wiki/concepts/beta-arrestin-signaling/) — Arrestin-mediated GPCR signaling pathway and biased signaling
- [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) — Bovine rhodopsin is the classical rhodopsin model system studied with arrestin
- [Thermal Shift Assay](/xray-mp-wiki/methods/quality-assessment/thermal-shift-assay/) — Used to assess stability of the T4L rhodopsin-arrestin fusion complex (Tm 59 C)
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal) — Entity mentioned in text
- [G Protein](/xray-mp-wiki/concepts/g-protein) — Entity mentioned in text
