---
title: Human Rhodopsin E113Q/M257Y Mutant
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14656]
verified: false
---

# Human Rhodopsin E113Q/M257Y Mutant

## Overview

Human rhodopsin is the visual pigment GPCR in vertebrate retinal rod cells, responsible for dim-light vision. The E113Q/M257Y mutant is a constitutively active form that mimics the light-activated state. Glu113 (E(D)RY motif) mutation disrupts the inactive-state salt bridge, while Met257 (H6) mutation further stabilizes the active conformation. This mutant was used in complex with pre-activated mouse visual arrestin (3A mutant) to determine the first high-resolution structure of the rhodopsin-arrestin complex by serial femtosecond crystallography (SFX) at an X-ray free-electron laser.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature14656 | not determined | 3.8 A | P212121 | Human rhodopsin (residues 1-326) with N2C/N282C disulfide mutations, E113Q/M257Y activating mutations, T4 lysozyme fused at ICL3, fused to 3A arrestin (residues 10-392) via 15 aa linker | all-trans retinal (ATR) |

## Expression and Purification

- **Expression system**: HEK293S cells transiently transfected with tetracycline-inducible expression cassette. Cells grown in SFM4TransFx 293, diluted tenfold with CDM4HEK293 medium, induced with 1 ug/ml doxycycline after 24 h.

- **Construct**: Fusion protein: His8-MBP-3C protease site-T4L (residues 2-161, C54T C97A) -rhodopsin (residues 1-326, N2C/N282C/E113Q/M257Y)-15 aa linker (AAAGSAGSAGSAGSA)-3A arrestin (residues 10-392, L374A/V375A/F376A)


### Purification Workflow

- **Expression system**: HEK293S cells
- **Expression construct**: His8-MBP-3C protease site-T4L-rhodopsin(N2C/N282C, E113Q/M257Y)-15aa linker-3A arrestin (residues 10-392)
- **Tag info**: His8-MBP tag at N-terminus, removed by 3C protease cleavage

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and induction | Transient transfection with tetracycline-inducible expression | -- | SFM4TransFx 293, CDM4HEK293 medium + not specified | Induced with 1 ug/ml doxycycline after 24 h |
| Membrane isolation | Hypotonic lysis, Dounce homogenization, ultracentrifugation | -- | 20 mM HEPES pH 7.5, 10 mM NaCl, 10 mM MgCl2 + not specified | 45,000 rpm at 4 C for 1 h |
| Solubilization | Detergent solubilization | -- | 20 mM Tris pH 7.4, 100 mM NaCl, 10% glycerol + 0.5% DDM, 0.1% CHS | Two hours at 4 C with protease inhibitor cocktail |
| Affinity chromatography | Amylose bead affinity | Amylose beads (New England Biolabs) | 20 mM Tris pH 7.4, 100 mM NaCl, 0.005% MNG-3, 0.001% CHS + 0.005% MNG-3, 0.001% CHS | Overnight at 4 C; eluted with 10 mM maltose |
| Tag cleavage | 3C protease cleavage | -- | Washing buffer + 0.005% MNG-3, 0.001% CHS | Overnight at 4 C |
| Tag removal | Ni-NTA affinity chromatography | Ni-NTA beads (Qiagen) | Washing buffer + 0.005% MNG-3, 0.001% CHS | 3 hours at 4 C to remove His8-MBP tag |

**Final sample**: 30 mg/ml in washing buffer
**Yield**: not specified
**Purity**: not specified


## Crystallization

### doi/10.1038##nature14656

| Parameter | Value |
|---|---|
| Method | lipidic-cubic-phase |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Microcrystals 5-15 um; diffracted to 6.8 A at synchrotron; SFX data to 3.8/3.8/3.3 A anisotropic |


## Biological / Functional Insights

### Constitutively active rhodopsin mutant

The E113Q mutation disrupts the salt bridge between Glu113 (E(D)RY motif
in H3) and Arg135 (H3), mimicking the charge redistribution that occurs
upon photoisomerization of 11-cis retinal to all-trans retinal. The M257Y
mutation in H6 further stabilizes the active conformation. Together, these
mutations yield a constitutively active rhodopsin that recruits arrestin
with high affinity without prior phosphorylation by rhodopsin kinase.
The N2C/N282ECL3C disulfide mutation increases thermal stability without
affecting activity.

### Rhodopsin-arrestin complex architecture

The crystal structure of the T4L-rhodopsin-arrestin fusion complex revealed
an asymmetric binding arrangement where rhodopsin uses distinct structural
elements including transmembrane helix 7 (TM7) and helix 8 (H8) to recruit
arrestin. Arrestin adopts a pre-activated conformation with ~20 degree
rotation between its amino and carboxy domains, opening a cleft that
accommodates a short helix formed by the second intracellular loop (ICL2)
of rhodopsin. The complex has four rhodopsins, four arrestins, and three
T4 lysozymes in the asymmetric unit.


## Cross-References

- [Bovine Rhodopsin](/xray-mp-wiki/proteins/bovine-rhodopsin/) — Related rhodopsin structure; bovine rhodopsin dark state (PDB 1GZM) solved at 2.65 A
- [Opsin (Retinal-Free Rhodopsin)](/xray-mp-wiki/proteins/opsin/) — Apoprotein form of rhodopsin; same protein family
- [Squid Rhodopsin](/xray-mp-wiki/proteins/squid-rhodopsin/) — Invertebrate rhodopsin; structural comparison with vertebrate rhodopsin
- [Mouse Visual Arrestin (3A)](/xray-mp-wiki/proteins/mouse-visual-arrestin-3a/) — Arrestin partner in the rhodopsin-arrestin complex structure
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization of rhodopsin-arrestin complex
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/lipids/cholesteryl-hemisuccinate/) — Lipid additive used in solubilization and purification buffers
- [Lauryl Maltose Neopentyl Glycol (MNG-3)](/xray-mp-wiki/reagents/detergents/mng-3/) — Mild detergent used in washing buffer for amylose bead purification
- [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — Primary method for structure determination at LCLS XFEL
