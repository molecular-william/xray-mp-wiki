---
title: GlcP_Se (Staphylococcus epidermidis Glucose/H+ Symporter)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1311485110]
verified: false
---

# GlcP_Se (Staphylococcus epidermidis Glucose/H+ Symporter)

## Overview

GlcP_Se is a glucose/H+ symporter from Staphylococcus epidermidis and a
member of the [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/major-facilitator-superfamily/).
It is homologous to human GLUT glucose transporters (27-34% sequence
identity) and is highly specific for glucose with a Km of 29 +/- 4 uM and
high avidity. GlcP_Se is inhibited by the human GLUT inhibitors cytochalasin
B, phloretin, and forskolin. The inward-facing, unliganded crystal structure
at 3.2 A resolution revealed 12 transmembrane helices arranged as two
twofold pseudosymmetrical N- and C-terminal domains, with a central
amphipathic cavity ~20 A deep formed by helices 1, 4, 7, and 10. The
structure provides a basis for understanding glucose/H+ symport and how it
differs from the facilitated diffusion mechanism of most human GLUTs.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1311485110 | not specified | 3.2 | — | Full-length GlcP_Se | unliganded (inward-facing conformation) |

## Expression and Purification

- **Expression system**: E. coli
- **Notes**: Expressed for crystallographic studies

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### H+/glucose symport mechanism in GlcP_Se

The proposed symport mechanism involves six steps: (A) In the absence of H+, D22 and R102 form a salt bridge to juxtapose helices 1 and 4, opening the substrate cavity wide. (B) When H+ binds to D22, the salt bridge is disrupted and helices 1 and 4 rearrange to decrease cavity size, lowering the energetic barrier for conformational transitions. (C) Glucose binds through residues of helices 5 (Q137), 7 (Q250, Q251, N256), and 10 (W357), bringing the N and C domains closer together. (D) In the inward-facing conformation, helices 5 and 10 move away from the center, dislocating Q137 and W357 from the glucose-binding site and opening the cavity toward the cytoplasm. (E) Glucose is released. (F) H+ is released, returning D22 and R102 to their salt bridge form, reopening the cavity.

### Structural basis for H+ symport versus uniport

The presence of an acidic residue at position 22 (D22 in GlcP_Se) is indicative of H+ symport. Human GLUTs that function as uniporters (GLUT1, -3, -4, -5, -7, -9, -11) have Asn at this position. GLUT12 (Glu) and GLUT13 (Asp) have acidic residues and function as H+ symporters. However, GLUT2 has Asp but is a uniporter due to an adjacent Ser residue (S161) that hydrogen bonds to the carboxylate, altering the H+-binding environment. The I105S mutation in GlcP_Se (mimicking GLUT2's H+-binding site) converts the symporter to a uniporter.

### Structural comparison between inward- and outward-facing conformations

The transition between inward-facing and outward-facing conformations involves a 24-degree relative rotation of the N and C domains around an axis passing through the substrate-binding site. Comparison with the XylE outward-facing structure shows that residues Q250, Q251, and N256 remain in approximately the same location in both conformations, while Q137 and W357 are removed from the glucose-binding site in the inward-facing structure, contributing to substrate release.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/major-facilitator-superfamily/) — GlcP_Se is a member of the MFS transporter family
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Glucose is the physiological substrate of GlcP_Se
