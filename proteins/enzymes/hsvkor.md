---
title: Human Vitamin K Epoxide Reductase (HsVKOR)
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.abc5667]
verified: false
---

# Human Vitamin K Epoxide Reductase (HsVKOR)

## Overview

Human [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide reductase (HsVKOR) is an integral membrane enzyme of the endoplasmic reticulum that catalyzes the reduction of [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide to [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) hydroquinone, a critical step in the [Vitamin K Cycle](/xray-mp-wiki/concepts/enzyme-mechanisms/vitamin-k-cycle/) that sustains blood coagulation. HsVKOR is the target of [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) and related [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) antagonists, which are widely used oral anticoagulants. The structure reveals a four-transmembrane-helix bundle (TM1-4) that creates a central pocket housing the active site cysteines Cys132 and Cys135. A large ER-luminal region connecting TM1 and TM2 contains a beta-hairpin, cap domain, and anchor domain that together cover the active site pocket. The enzyme undergoes open-to-closed conformational changes during its catalytic cycle, and [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) antagonists inhibit by mimicking the binding interactions of the natural substrates.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.abc5667 | 6WV3 | 3.2 | C2221 | HsVKOR (3-155) with sfGFP fusion at termini; N- and C-termini restrained by split sfGFP | [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) |
| doi/10.1126##science.abc5667 | 6WV6 | 3.1 | P212121 | HsVKOR (3-155) with sfGFP fusion at termini | [Phenindione](/xray-mp-wiki/reagents/ligands/phenindione/) |
| doi/10.1126##science.abc5667 | 6WVH | 3.2 | C2221 | HsVKOR (3-155) with sfGFP fusion at termini | [Brodifacoum](/xray-mp-wiki/reagents/ligands/brodifacoum/) |
| doi/10.1126##science.abc5667 | 6WV7 | 3.1 | I222 | HsVKOR (3-155) with sfGFP fusion at termini | [Chlorophacinone](/xray-mp-wiki/reagents/ligands/chlorophacinone/) |
| doi/10.1126##science.abc5667 | 6WV4 | 3.2 | C2221 | HsVKOR Cys43Ser mutant (3-155) with sfGFP fusion at termini | [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) |
| doi/10.1126##science.abc5667 | 6WV5 | 3.0 | C2221 | HsVKOR Cys43Ser mutant (3-155) with sfGFP fusion at termini | [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide (KO) adduct |

## Expression and Purification

- **Expression system**: Pichia pastoris (split sfGFP fusion)
- **Construct**: HsVKOR (3-155) with N- and C-terminal halves of superfolder GFP (sfGFP); codon-optimized
- **Notes**: Termini-restrained construct catalytically active and inhibitable by [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) both in cells and after purification

### Purification Workflow

- **Expression system**: Pichia pastoris
- **Expression construct**: HsVKOR (3-155) with sfGFP fusion at N- and C-termini
- **Tag info**: Split superfolder GFP (sfGFP) fused to N- and C-termini

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and induction | [Methanol](/xray-mp-wiki/reagents/additives/methanol/) induction in Pichia pastoris |  | BMG media (1.2% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.34% YNB, 1% [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/), 0.4 ug/mL biotin, 100 mM potassium phosphate pH 6.0); BMM media for induction | 1 L culture in BMG at 30C for 20 hr, then switched to BMM with 0.7% [Methanol](/xray-mp-wiki/reagents/additives/methanol/) at 25C for 2 days |
| Cell lysis | Ball mill |  | 225 mM NaCl, 75 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 10 ug/mL DNase I + 2% n-Dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Frozen cells broken by ball mill; membranes solubilized with [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for 3 hr at 4C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) metal-affinity resin (Clontech) | Wash: 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 150 mM NaCl, 0.2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 20 mM Tris pH 8.0; Elution: 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 150 mM NaCl, 0.2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 20 mM Tris pH 8.0
 + 0.2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Protein incubated with [TALON](/xray-mp-wiki/reagents/additives/talon/) resin for 3 hr at 4C; washed and eluted |
| Size-exclusion chromatography | Size-exclusion chromatography (SEC) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 150 mM NaCl, 20 mM Tris pH 8.0 + 0.05% Lauryl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol ([LMNG](/xray-mp-wiki/reagents/detergents/lmng/)) | Peak fractions collected; concentrated to 40 mg/mL for crystallization |

**Final sample**: 40 mg/mL in 150 mM NaCl, 20 mM Tris pH 8.0, 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)


## Crystallization

### doi/10.1126##science.abc5667

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | HsVKOR (sfGFP fusion) with pre-bound VKA ligands; 40 mg/mL |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | 2:3 (v/v) |
| Temperature | 22 |
| Growth time | Crystals appeared within one week, optimal size after several weeks |
| Notes | Ligands added during purification (HsVKOR unstable without ligand). Crystals harvested from lipid bolus and flash-frozen in liquid nitrogen. Data collected at APS NE-CAT beamlines 24ID-C and 24ID-E. |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | HsVKOR Cys43Ser mutant (sfGFP fusion); 40 mg/mL |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | 2:3 (v/v) |
| Temperature | 22 |
| Growth time | Several weeks |
| Notes | Co-crystallized with KO ([Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide) mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |


## Biological / Functional Insights

### Overall structure of HsVKOR with bound VKAs

HsVKOR contains four transmembrane helices (TM1-4) forming a four-helix bundle with a central pocket occupied by VKAs. The catalytic cysteines Cys132 and Cys135 are located in this pocket. TM1 and TM2 are connected by a large ER-luminal region comprising a helical extension (TM1e), loop 1, a beta-hairpin stapled by Cys43-Cys51 disulfide, and a cap domain covering the central pocket. An amphipathic anchor domain attaches the cap to the membrane.

### VKA binding interactions

All VKAs ([Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/), [Phenindione](/xray-mp-wiki/reagents/ligands/phenindione/), [Brodifacoum](/xray-mp-wiki/reagents/ligands/brodifacoum/), [Chlorophacinone](/xray-mp-wiki/reagents/ligands/chlorophacinone/)) are hydrogen-bonded to Asn80 on TM2 and Tyr139 on TM4. The 4-hydroxyl group of coumarin-based VKAs forms a hydrogen bond with Tyr139 hydroxyl. The 2-ketone group hydrogen bonds with Asn80 amide. Mutations disrupting these interactions (Asn80Ala, Tyr139Phe) cause strong [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) resistance.

### Warfarin resistance mechanisms

[Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) resistance arises from two distinct mechanisms: direct disruption of [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) binding (Asn80Ala, Tyr139Phe) or destabilization of the cap domain (Tyr25Ala, His28Ala, Asp44Ala). The cap domain is stabilized by interactions with TM1/TM1e and loop 3-4; mutations that disrupt these interactions cause resistance even though the mutated residues do not directly contact [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/).

### Capturing the catalytic intermediate

A Cys43Ser mutant of HsVKOR co-crystallized with [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide (KO) revealed a covalent Cys135-KOH adduct (C-S bond distance ~2 A). The 3-hydroxy [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) (3-OH K) product was identified by NMR spectroscopy, confirming that Cys135 attacks the C2 atom of the naphthoquinone ring.

### Distinct warfarin and product-bound states

The warfarin-bound structure differs from the 3-OH K-bound structure. In the 3-OH K state, Arg58 interacts with Glu67 differently than when [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) is bound. The polar 3-hydroxyl of 3-OH K prevents Phe55 from interacting with the naphthoquinone ring, whereas Phe55 forms pi-pi stacking with the coumarin ring of [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/). This shows [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) mimics a later step of VKOR catalysis rather than being a true transition-state analog.


## Cross-References

- [VKOR from Synechococcus sp.](/xray-mp-wiki/proteins/enzymes/synechococcus-vkor/) — Bacterial homolog of HsVKOR providing earlier structural information
- [TrVKORL](/xray-mp-wiki/proteins/enzymes/trvkorl/) — Pufferfish VKOR-like protein used for ligand-free structural comparison
- [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) — Primary VKA inhibitor bound in HsVKOR structures
- [Brodifacoum](/xray-mp-wiki/reagents/ligands/brodifacoum/) — Superwarfarin bound in HsVKOR structure 6WVH
- [Termini Restraining](/xray-mp-wiki/concepts/miscellaneous/termini-restraining/) — HsVKOR structure was determined using the termini-restraining approach with split sfGFP
- [Vitamin K Catalytic Cycle](/xray-mp-wiki/concepts/enzyme-mechanisms/vitamin-k-catalytic-cycle/) — Central enzymatic cycle catalyzed by HsVKOR
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for HsVKOR purification
- [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for SEC and final sample of HsVKOR
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used for LCP crystallization of HsVKOR
- [Vitamin K Cycle](/xray-mp-wiki/concepts/enzyme-mechanisms/vitamin-k-cycle/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
