---
title: "ExbD (E. coli)"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19757]
verified: false
---

# ExbD (E. coli)

## Overview

ExbD is an integral polytopic membrane protein from Escherichia coli that, together with [ExbB (E. coli)](/xray-mp-wiki/proteins/exbB) and TonB, forms the Ton complex responsible for energy transduction from the proton motive force at the inner membrane to TonB-dependent transporters at the outer membrane. ExbD contains a single N-terminal transmembrane helix that anchors a large C-terminal periplasmic domain. It assembles as a dimer, with one copy inserting its transmembrane helix into the pore of the ExbB pentamer and the second copy located outside the ExbB pentamer. ExbD forms a pH-sensitive cation-selective channel when complexed with ExbB.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature19757 | 5FQ7 | 2.6 A | P63 | [ExbB (E. coli)](/xray-mp-wiki/proteins/exbB)-ExbD subcomplex; ExbD periplasmic domain (residues 1-45) | calcium ion |
| doi/10.1038##nature19757 | 5FQ6 | 3.5 A | P212121 | [ExbB (E. coli)](/xray-mp-wiki/proteins/exbB)-ExbD Delta peri; ExbD periplasmic domain (residues 22-45) | calcium ion |

## Expression and Purification

- **Expression system**: E. coli K-12 BL21(DE3) cells
- **Construct**: ExbD with N-terminal Strep-tag and C-terminal 10xHis tag (pACYCDUet-1); also subcloned into pCDF-1b with C-terminal TEV site and 10xHis tag; ExbD Delta peri construct with deletion of periplasmic domain (residues 50-141)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex-C3 high-pressure homogenization | -- | 1xPBS or TBS + -- | Cells resuspended with 100 uM AEBSF, 100 uM DNase, 50 ug/ml lysozyme; disrupted at ~15,000 p.s.i. |
| Membrane isolation | Ultracentrifugation | -- | 1xPBS or TBS + -- | Pelleted at 200,000g for 1 h at 4 C; membranes resuspended with dounce homogenizer |
| Solubilization | Membrane solubilization | -- | 1xPBS or TBS + 1% [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100) | Solubilized by addition of [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100) to 1% final concentration for Ton subcomplex |
| Affinity purification | His-tag [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | -- | 1xPBS or TBS + 1% [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100) | Purified using C-terminal 10xHis tag on ExbD |


## Crystallization

### doi/10.1038##nature19757

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | [ExbB (E. coli)](/xray-mp-wiki/proteins/exbB)-ExbD subcomplex at pH 7.0; ExbB-ExbD Delta peri at pH 4.5 |
| Reservoir | Not specified in paper |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Structure at pH 7.0 (2.6 A) solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement). Structure at pH 4.5 (3.5 A) showed clear electron density for the transmembrane helix of ExbD within the ExbB pentamer pore, while at pH 7.0 density was too diffuse to model. This pH-dependent behavior suggests ExbD TMH movement is modulated by pH. |


## Biological / Functional Insights

### ExbD dimer stoichiometry within the Ton complex

ExbD assembles as a dimer within the Ton complex. Crosslinking studies targeting ExbD confirmed a dimer formed within a single complex (intra-complex rather than inter-complex). DEER spectroscopy on MTSL-labeled ExbD at positions 78 and 113 showed distance distributions consistent with the ExbD dimer model (based on PDB 2PFU/TolR dimer, PDB 2JWK). Labeling at position 78 yielded distances of 35 and 43 A (predicted 32-44 A). Labeling at position 113 yielded distances of 23 and 34 A (predicted 15-35 A). The dimer state is maintained in the presence and absence of [TonB (E. coli)](/xray-mp-wiki/proteins/tonB).

### Transmembrane helix of ExbD plugs the ExbB pentamer pore

An extended alpha-helix (residues 22-45) of ExbD was observed within the transmembrane pore of the [ExbB (E. coli)](/xray-mp-wiki/proteins/exbB) pentamer in the pH 4.5 structure. At pH 7.0, sparse electron density suggested the TMH was present but too diffuse to model. The TMH position was offset by approximately 10 A from the predicted transmembrane domain position of ExbB, suggesting pH-dependent movement. Residues from helices alpha 6 and alpha 7 of ExbB line the transmembrane pore and mediate interactions with the ExbD TMH. The D25A mutation in the ExbD TMH affects channel closure at low pH.

### pH-sensitive ion channel conductance

The [ExbB (E. coli)](/xray-mp-wiki/proteins/exbB)-ExbD subcomplex forms a cation-selective channel with 120 +/- 30 pS conductance at neutral pH and a sevenfold greater permeability for K+ than Cl- (Vrev 24.7 +/- 0.9 mV; pK+/pCl- 7.0 +/- 0.9). Conductance decreases from 120 pS at pH 8.0 to 70 pS at pH 4.5. Below pH 4.5, channels close at both positive and negative potentials. This pH sensitivity is likely mediated through movement of the ExbD TMH within the ExbB pore, with the TMH adopting a more closed/fixed conformation at low pH.

### Model of the fully assembled Ton complex

The Ton complex consists of a pentamer of [ExbB (E. coli)](/xray-mp-wiki/proteins/exbB), a dimer of ExbD, and at least one TonB. Since only a single TMH can fit within the ExbB pentamer pore, the second ExbD copy is located outside the ExbB pentamer. TonB association does not notably affect the structure or stoichiometry of ExbB or ExbD. The interaction of TonB with ExbD leads to a functional Ton complex that triggers energy production and transduction.


## Cross-References

- [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/) — ExbD forms a dimer that interacts with the [ExbB (E. coli)](/xray-mp-wiki/proteins/exbB) pentamer to constitute the Ton subcomplex; one ExbD TMH plugs the ExbB pore
- [TonB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/tonB/) — [TonB (E. coli)](/xray-mp-wiki/proteins/tonB) interacts with ExbD in the fully assembled Ton complex; TonB may exchange for one ExbD monomer during energy transduction
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization of the fully assembled Ton complex (0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm) for DEER samples)
- [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100/) — Detergent used for solubilization of the Ton subcomplex (1% final concentration)
- [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — C-terminal 10xHis tag used for ExbD purification
- [Strep Tag](/xray-mp-wiki/reagents/protein-tags/strep-tag/) — N-terminal Strep-tag used on ExbD for purification
- [DEER Spectroscopy](/xray-mp-wiki/methods/quality-assessment/deer-spectroscopy/) — DEER performed on ExbD N78C and E113C mutants labeled with MTSL to confirm dimeric state
- [Ton Complex](/xray-mp-wiki/concepts/miscellaneous/ton-complex/) — ExbD is a core component of the Ton complex; the concept page describes the functional complex
- [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) — Crystallization method used for structure determination
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) — Purification method used in protein preparation
