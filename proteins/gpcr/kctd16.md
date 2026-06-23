---
title: "KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1903024116]
verified: false
---

# KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16)

## Overview

KCTD16 is a potassium channel tetramerization domain-containing protein that functions
as an auxiliary subunit of metabotropic GABA_B receptors. It belongs to the KCTD family
(group D) along with KCTD8, KCTD12, and KCTD12b, which modulate GABA_B receptor
signaling. KCTD16 contains an N-terminal T1 oligomerization domain (broad-complex,
tramtrack, and bric a brac fold) and two C-terminal homology domains (H1 and H2).
The T1 domain forms an open pentamer that binds to the C-terminal tail of the GABA_B2
subunit. The crystal structure of the KCTD16 T1 domain in complex with a GABA_B2-derived
peptide (residues 895-909) was solved at 2.4 A resolution, revealing that a single
GABA_B2 peptide binds to the interior of the open pentamer formed by five KCTD16
subunits. Key interfacial residues include F80 (conserved across all four KCTD subunits)
and E102, which form hydrophobic and hydrogen bonding interactions with the GABA_B2
peptide.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1903024116 | 6OCP | 2.4 | P1 | KCTD16 T1 domain (residues 22-134) in complex with GABA_B2(895-909) peptide | GABA_B2 peptide |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: KCTD16 T1 domain (residues 22-134), L89M mutant for SeMet

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Homogenization | — | 50 mM Tris pH 8.0, 500 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) | Lysate clarified by centrifugation |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA affinity | Ni-NTA | 50 mM Tris pH 8.0, 500 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) | Eluted with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag removal | TEV protease cleavage | — |  | His6-SUMO tag removed overnight at 4 C |
| Gel filtration | Size-exclusion chromatography | Superdex 75 | 10 mM HEPES pH 7.5, 150 mM NaCl |  |


## Crystallization

### doi/10.1073##pnas.1903024116

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | KCTD16 T1 domain with GABA_B2(895-909) peptide at 1.5:5 molar ratio |
| Reservoir | 2% [PEG](/xray-mp-wiki/reagents/additives/peg/) 6000, 2% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 8% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 0.1 M [Sodium Cacodylate](/xray-mp-wiki/reagents/buffers/sodium-cacodylate/) trihydrate pH 5.6 |
| Notes | Crystals belong to P1 space group with 15 molecules per asymmetric unit. Data collected at APS 24ID-C beamline. |


## Biological / Functional Insights

### KCTD16 T1 forms an open pentamer

KCTD16 T1 assembles into an open pentameric ring structure (inner diameter ~25 A)
with a gap of ~16 A between subunits I and V. The pentamer is stabilized by extensive
salt bridge interactions mediated by the alpha-3 helix of each subunit. A D76R mutation
disrupts pentamer formation, converting KCTD16 T1 to a monomer in solution and
abolishing its ability to accelerate GIRK channel activation.

### Single GABA_B2 peptide binds to four KCTD16 subunits

The GABA_B2 C-terminal peptide (residues 895-909) forms a loop inside the KCTD16
pentamer ring, contacting four of the five subunits (I-IV). The binding involves
three regions: (1) N-terminal anchor via Q34/L896/L899 interactions with F80 from
subunits I-II; (2) a 3_10 helix (H900-Y903) sandwiched between F80 of subunits II-III
with key hydrogen bonds involving E102-Y903 and Q34-H901; (3) C-terminal contacts
with F80 of subunits III-IV. The interfacial residue F80 is conserved across all
GABA_B-associated KCTDs.

### Conserved binding mode across KCTD family

The GABA_B2-binding residues in KCTD16 (particularly F80, Q34, and E102) are
highly conserved in KCTD8, KCTD12, and KCTD12b, suggesting a universal binding
mode for all GABA_B-associated KCTD proteins. Co-immunoprecipitation experiments
confirmed that mutations at the interface (F80A, E102A in KCTD16; I898A, Y903A,
L904A in GABA_B2) disrupt both biochemical association and functional modulation
of GABA_B receptors.


## Cross-References

- [Human GABA_B Receptor](/xray-mp-wiki/proteins/gpcr/human-gabab-receptor/) — KCTD16 binds to the C-terminal tail of the GABA_B2 subunit as an auxiliary regulatory subunit
- [GPCR-G Protein Coupling Mechanism](/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-coupling/) — KCTD16 modulates GABA_B receptor coupling to GIRK channels
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Sodium Cacodylate](/xray-mp-wiki/reagents/buffers/sodium-cacodylate/) — Buffer component in purification or crystallization
