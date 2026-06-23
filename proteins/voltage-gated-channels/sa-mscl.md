---
title: "Staphylococcus aureus MscL (Mechanosensitive Channel of Large Conductance)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08277]
verified: false
---

# Staphylococcus aureus MscL (Mechanosensitive Channel of Large Conductance)

## Overview

SaMscL is the mechanosensitive channel of large conductance from Staphylococcus aureus, a bacterial ion channel that protects cells from lysis upon acute osmotic down-shock. The crystal structure of a C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) mutant (CΔ26, residues 1-94) was determined at 3.8 A resolution, revealing a tetrameric channel with both transmembrane helices (TM1 and TM2) tilted away from the membrane normal at angles close to those inferred for the open state. TM1 and TM2 are tilted 49 degrees and 59 degrees with respect to the pore axis, significantly larger than the 36-38 degrees in the closed-state pentameric [MSCL](/xray-mp-wiki/proteins/other-ion-channels/mscl/) from M. tuberculosis. The pore constriction at Val21 is widened to ~6 A diameter compared to ~3 A in the closed state, but remains hydrophobic and likely non-conducting, representing an expanded intermediate state between the closed and open conformations.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature08277 | (deposited; referenced PDB 2OAR for MtMscL comparison) | 3.8 A | Tetragonal (four-fold crystallographic axis coincides with molecular symmetry) | SaMscL C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) mutant (CΔ26, residues 1-94); one subunit per asymmetric unit | None |

## Expression and Purification

- **Expression system**: E. coli BL21-Gold (DE3)
- **Construct**: SaMscL(CA26) with stop codon at Glu95, cloned into pET15b vector with NdeI and BamHI sites

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), 200 mM NaCl, 44 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), pH 8.0 | Cells resuspended in lysis buffer and sonicated for 4 min |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA gravity column | 2 ml Ni-NTA (Qiagen) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), 300 mM NaCl, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), pH 7.5 (high salt wash); 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), 20 mM NaCl, 75 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), pH 7.5 (low [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) wash); 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), 20 mM NaCl, 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), pH 7.5 (elution) | Protein concentrated to ~15 mg/ml |
| Size-exclusion chromatography | Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/30 HR column | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), 150 mM NaCl, 2 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), pH 7.5 | Major peak eluting at ~14.3 ml; concentrated to 15-20 mg/ml |


## Crystallization

### doi/10.1038##nature08277

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Purified SaMscL(CA26) at 15-20 mg/ml with 3.0 mM decyl-beta-D-maltoside (DM) added |
| Reservoir | 24-30% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.0, 150 mM Na2SO4 |
| Temperature | 4 degrees C (crystal crosslinking) |
| Growth time | ~1 month |
| Cryoprotection | Not specified |
| Notes | Initial hits from MemGold screen. Crystals crosslinked with 25% glutaraldehyde through vapor diffusion at 4 C for 1-2 h. Crystals soaked overnight in 10 mM Na2WO4 or Na2MoO4 for phasing. Structure solved by [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) using S32C mutant soaked in Na4P2O7 for phasing at 3.8 A resolution. |


## Biological / Functional Insights

### Tetrameric MscL represents an expanded intermediate state

SaMscL(CΔ26) forms a tetramer in the crystal, in contrast to the pentameric MtMscL closed-state structure. The channel is expanded within the membrane plane and compressed along the pore axis compared to the closed state. TM1 and TM2 are tilted 49 degrees and 59 degrees with respect to the pore axis, close to the ~51 degrees predicted for the open state. However, the pore constriction at Val21 remains narrow (~6 A diameter) and hydrophobic, suggesting the structure is non-conducting and represents an expanded intermediate state.

### Two-step helix-pivoting gating mechanism

The structure supports a two-step gating mechanism: (1) TM1-TM2 pairs tilt outward as rigid bodies, expanding the periplasmic surface area while the pore remains essentially closed at the constriction; (2) a second anticlockwise pivoting of the TM1-TM2 pair around a hinge at Gly48 expands the pore diameter to ~22 A, compatible with the 3 nS conductance. The periplasmic loop acts as a spring limiting the extent of channel expansion. This glycine-pivoting mechanism is analogous to that observed in [MSCS](/xray-mp-wiki/proteins/voltage-gated-channels/mscs/).

### C-terminal truncation traps the intermediate state

Removal of 26 C-terminal residues (residues 95-120) lowers the energy barrier for transition from the closed to expanded state. The C-terminal helical bundle in the full-length protein likely stabilizes the closed conformation and may act as a plug or pre-filter to the permeation pathway. Both full-length and truncated SaMscL rescue an [MSCL](/xray-mp-wiki/proteins/other-ion-channels/mscl/)/MscS/MscK knockout strain from osmotic down-shock, confirming the mutant is functional in vivo.


## Cross-References

- [MscL (Mycobacterium tuberculosis)](/xray-mp-wiki/proteins/other-ion-channels/mscl/) — Related mechanosensitive channel from M. tuberculosis; closed-state pentameric structure (PDB 2OAR) compared to the SaMscL expanded intermediate
- [Mechanosensitive Gating](/xray-mp-wiki/concepts/transport-mechanisms/mechanosensitive-gating/) — SaMscL is a mechanosensitive ion channel; the structure reveals the expanded intermediate in the gating pathway
- [Force-from-Lipid Principle](/xray-mp-wiki/concepts/membrane-mimetics/force-from-lipid-principle/) — MscL is directly gated by membrane tension via the force-from-lipid principle
- [LDAO (Lauryldimethylamine Oxide)](/xray-mp-wiki/reagents/detergents/ldao/) — Detergent used for SaMscL purification and crystallization
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in purification (10-50 mM Tris-HCl, pH 7.0-8.0)
- [PEG 400](/xray-mp-wiki/reagents/additives/peg-400/) — Precipitant used in crystallization (24-30% PEG400)
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) — Method used in structure determination or purification
- [MSCS](/xray-mp-wiki/proteins/voltage-gated-channels/mscs/) — Related protein structure
