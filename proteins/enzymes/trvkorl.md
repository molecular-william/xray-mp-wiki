---
title: TrVKORL (Pufferfish Vitamin K Epoxide Reductase-Like)
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.abc5667]
verified: false
---

# TrVKORL (Pufferfish Vitamin K Epoxide Reductase-Like)

## Overview

TrVKORL is a [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide reductase-like protein from the pufferfish Takifugu rubripes. It shares 73% sequence identity with human VKOR-like (HsVKORL) and 52% with [HSVKOR](/xray-mp-wiki/proteins/enzymes/hsvkor/). TrVKORL is catalytically active and inhibitable by [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/), both in cells and after purification. Its higher expression level and better in vitro stability than HsVKORL enabled capture of both ligand-free and warfarin-bound states, providing the structural basis for understanding the conformational changes associated with VKOR catalysis and inhibition. The protein adopts two distinct conformations: an open conformation in the ligand-free state and a closed conformation induced by [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) or substrate binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.abc5667 | 6WVI | 2.9 |  | TrVKORL (6-175) wild-type, ligand-free | None |
| doi/10.1126##science.abc5667 | 6WVB | 2.9 |  | TrVKORL (6-175) with [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) | [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) |
| doi/10.1126##science.abc5667 | 6WV9 | 2.8 |  | TrVKORL (6-175) with [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) quinone (co-crystallized with KO) | [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) quinone (K) |
| doi/10.1126##science.abc5667 | 6WVA | 2.9 |  | TrVKORL (6-175) co-crystallized with [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide (KO) | [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide (KO) |
| doi/10.1126##science.abc5667 | 6WV8 | 2.8 |  | TrVKORL Cys132Ser mutant (6-175) with [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) quinone (K) | [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) quinone (K) |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: TrVKORL (6-175)
- **Notes**: Higher expression level and better in vitro stability than HsVKORL, enabling crystallization without fusion tags

### Purification Workflow

- **Expression system**: Pichia pastoris
- **Expression construct**: TrVKORL (6-175) wild-type or Cys138Ser (Cys132Ser) mutant
- **Tag info**: Native, no purification tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and induction | [Methanol](/xray-mp-wiki/reagents/additives/methanol/) induction in Pichia pastoris |  | BMG media (1.2% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.34% YNB, 1% [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/), 0.4 ug/mL biotin, 100 mM potassium phosphate pH 6.0); BMM media for induction | 1 L culture in BMG at 30C for 20 hr, then switched to BMM with 0.7% [Methanol](/xray-mp-wiki/reagents/additives/methanol/) at 25C for 2 days |
| Cell lysis | Ball mill |  | 225 mM NaCl, 75 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 10 ug/mL DNase I + 2% n-Dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Frozen cells broken by ball mill; membranes solubilized with [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for 3 hr at 4C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) metal-affinity resin (Clontech) | Wash: 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 150 mM NaCl, 0.2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 20 mM Tris pH 8.0; Elution: 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 150 mM NaCl, 0.2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 20 mM Tris pH 8.0
 + 0.2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Protein incubated with [TALON](/xray-mp-wiki/reagents/additives/talon/) resin for 3 hr at 4C |
| Size-exclusion chromatography | Size-exclusion chromatography (SEC) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 150 mM NaCl, 20 mM Tris pH 8.0 + 0.05% Lauryl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol ([LMNG](/xray-mp-wiki/reagents/detergents/lmng/)) | Peak fractions collected; concentrated to 40 mg/mL for crystallization |

**Final sample**: 40 mg/mL in 150 mM NaCl, 20 mM Tris pH 8.0, 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)


## Crystallization

### doi/10.1126##science.abc5667

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | TrVKORL (wild-type or mutant); 40 mg/mL |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | 2:3 (v/v) |
| Temperature | 22 |
| Growth time | Crystals appeared within one week, optimal size after several weeks |
| Notes | For ligand-free TrVKORL, no ligand added during purification. For [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) complex, 1 mM [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) added during cell lysis before [DDM](/xray-mp-wiki/reagents/detergents/ddm/) solubilization and maintained throughout. For substrate complexes (K, KO), ligands mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) for co-crystallization. Data collected at APS NE-CAT beamlines. |


## Biological / Functional Insights

### Open and closed conformations

TrVKORL adopts an open conformation in the ligand-free state, characterized by a luminal helix that converts into loop 1 and beta-hairpin upon [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) or substrate binding. The closed conformation induced by [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) is very similar to that induced by substrate (K) binding, with the cap domain, loop 1, and beta-hairpin adopting essentially the same conformation. This open-to-closed transition is triggered by hydrogen bonding interactions with Asn80 and Tyr139.

### Warfarin-induced conformational changes

[Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) binding induces a global conformational change from open to closed state. In the closed state, Cys43-Cys51 are repositioned to interact with loop 3-4, the cap helix and beta-hairpin are formed, and Asp44 becomes a central residue holding these elements together. In the open conformation, Asp44 is located on the luminal helix and does not participate in stabilizing interactions.

### Substrate-induced reduction and charge-transfer complex

The Cys132Ser mutant of TrVKORL with K bound reveals a charge-transfer complex between Cys135 thiolate and the naphthoquinone ring of K (S to C2 distance ~3 A). This complex stabilizes K within the active site and triggers the open-to-closed conformational change, bringing Cys43-Cys51 close to Cys135-K for thiol-disulfide exchange that resolves the adduct and fully reduces K.

### Similarity between warfarin and substrate-bound states

The closed conformation induced by [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) closely resembles that induced by the Cys135-K charge-transfer adduct. [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) exploits features tailored for substrate binding: hydrogen bonding to Asn80 and Tyr139, and interaction of its side group with the same residues (Phe83, Phe87, Tyr88) that bind the isoprenyl chain of [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/). This explains how VKAs stably occupy the active site.


## Cross-References

- [Human Vitamin K Epoxide Reductase (HsVKOR)](/xray-mp-wiki/proteins/enzymes/hsvkor/) — Mammalian homolog; TrVKORL shares 52% sequence identity and same overall structure
- [VKOR from Synechococcus sp.](/xray-mp-wiki/proteins/enzymes/synechococcus-vkor/) — Bacterial VKOR homolog providing complementary structural information
- [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) — VKA used to capture closed conformation of TrVKORL
- [Vitamin K Catalytic Cycle](/xray-mp-wiki/concepts/enzyme-mechanisms/vitamin-k-catalytic-cycle/) — Catalytic cycle described through TrVKORL structures in different states
- [Termini Restraining](/xray-mp-wiki/concepts/miscellaneous/termini-restraining/) — TrVKORL structure was determined using the termini-restraining approach with split sfGFP
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for TrVKORL membrane solubilization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used for LCP crystallization of TrVKORL
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
