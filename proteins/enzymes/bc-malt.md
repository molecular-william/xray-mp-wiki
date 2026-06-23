---
title: "bcMalT (Bacillus cereus Maltose Transporter)"
created: 2026-05-28
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2016.04.003, doi/10.1073##pnas.1800647115]
verified: false
---

# bcMalT (Bacillus cereus Maltose Transporter)

## Overview

bcMalT is a [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter from Bacillus cereus, belonging to the Glucose superfamily of enzyme IIC (EIIC) components of the phosphoenolpyruvate:carbohydrate phosphotransferase system (PTS). It is the first crystal structure of a Glucose superfamily EIIC transporter in an outward-facing occluded conformation. The protein undergoes a large rigid-body motion of its substrate-binding domain, moving the substrate-binding cavity by approximately 20 A between inward-facing and outward-facing states, consistent with an elevator-car transport mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2016.04.003 | 5IWS | 2.55 | I222 | Trypsinized EIIC domain (residues 8-450) | [Maltose](/xray-mp-wiki/reagents/additives/maltose) |
| doi/10.1073##pnas.1800647115 | 6BVG | 3.2 | I222 | bcMalT T280C/E54C double-cysteine mutant, Hg2+-crosslinked, inward-facing conformation | [Maltose](/xray-mp-wiki/reagents/additives/maltose) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: His6-tagged EIIC domain from Bacillus cereus (Uniprot Q63GK8), cloned into pMCSG28 vector, [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-derivatized
- **Notes**: Gene cloned from Bacillus cereus E33L chromosome. Cells grown in SeMet-containing minimal media, induced with 0.5 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg) at 20 C overnight.

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) on full-length protein, trypsinized to yield EIIC domain only

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | — | 20 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol, 2 mM [Beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol), 25 ug/mL DNase I, 5 mM MgCl2, 1 mM PMSF | Cells resuspended and sonicated until fully lysed |
| Membrane extraction | Detergent solubilization | — | 20 mM HEPES pH 7.5, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 30 mM [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm) (Anatrace) | Gentle shaking for 2 hours at room temperature, centrifuged 45 min at 55,000g |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) affinity (TALON, Clontech) | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon) cobalt affinity resin | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM NaCl + 30 mM [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm) | Washed with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), eluted with 300 mM imidazole |
| Limited proteolysis | [Trypsin](/xray-mp-wiki/reagents/additives/trypsin) digestion | — |  | 1:20 wt ratio bcMalT to [Trypsin](/xray-mp-wiki/reagents/additives/trypsin), 30 min at room temperature, yielded EIIC domain (~50.84 kDa) |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | SEC ([Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200) 10/300 GL) | — | 20 mM HEPES pH 7.5, 150 mM NaCl, 10 mM trehalose, 4 mM DM, 4 mM [Beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) | Full-length EIICB protein unstable at high concentrations in detergent; trypsinized EIIC domain used for crystallization |


## Crystallization

### doi/10.1016##j.str.2016.04.003

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) (in meso) |
| Protein sample | 50-55 mg/mL trypsinized EIIC domain in 20 mM HEPES pH 7.5, 150 mM NaCl, 10 mM trehalose, 4 mM DM, 4 mM [Beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Protein-to-lipid ratio | 2:3 (protein solution:molten [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein), w:w) |
| Temperature | Room temperature |
| Growth time | Approximately 3 weeks |
| Cryoprotection | Flash frozen in liquid nitrogen |


## Biological / Functional Insights

### Maltose-specific binding and transport

bcMalT selectively binds and transports maltose. Scintillation proximity assay (SPA) with radiolabeled maltose showed an IC50 of 4.5 +/- 1.1 uM for competitive binding by unlabeled maltose. Reconstitution into proteoliposomes demonstrated maltose uptake via facilitated diffusion, reaching steady state after 10 minutes at 5-fold higher accumulation than control liposomes. No significant binding was observed for glucose, [Trehalose](/xray-mp-wiki/reagents/additives/trehalose), sucrose (except weak sucrose binding), or other tested sugars, indicating strict requirement for both sugar moieties and sensitivity to the alpha-1,4 glycosidic linkage.

### Elevator-car transport mechanism

Comparison of bcMalT (outward-facing occluded) with bcChbC (inward-facing occluded, PDB 3G5R) reveals a rigid-body displacement of the C-terminal substrate-binding domain by 44 degrees rotation and 9 A translation toward the periplasm, moving the substrate-binding cavity by approximately 20 A. Molecular dynamics simulations showed that TM7 rotation can open the cavity to the periplasm, suggesting an outward-facing open state. This supports an elevator-car mechanism where the substrate-binding domain carrying the intact ligand moves between inward-facing and outward-facing states.

### Active site architecture and substrate recognition

Each protomer contains a large cavity in the substrate-binding domain where [Maltose](/xray-mp-wiki/reagents/additives/maltose) is bound. Conserved residues forming hydrogen bonds include Glu355 (HP1) and His240 (TM7) interacting with C6 hydroxyl of the non-reducing sugar, Thr354 (HP1), Arg232 and Glu231 (TM6) with the non-reducing sugar, Lys307 (TM8) and His241 (TM7) stabilizing the reducing sugar, and Phe393 (HP2) contributing stacking interactions. These residues are strongly conserved within the Glc subfamily of EIIC transporters.

### Direct structural evidence for elevator mechanism from inward-facing bcMalT-X

The crystal structure of bcMalT cross-linked in an inward-facing conformation (bcMalT-X, 3.2 A) provides direct visualization of both outward- and inward-facing states on the same transporter. The substrate-binding domain undergoes a rigid-body 9 A vertical translation and 45 degree rotation relative to the dimerization domain. The amphipathic helix AH2 bends at a conserved Pro199 hinge, changing angle from 137.5 to 117.0 degrees to accommodate the domain motion. The structure was validated by all-atom MD simulations showing stability of the inward-facing state with or without Hg2+ cross-linking, and by smFRET experiments confirming a two-state equilibrium with a ~5:1 preference for the outward-facing conformation (free energy difference ~2-4 kJ/mol). The structure confirms the elevator-type mechanism for the glucose superfamily of EIIC transporters. 


## Cross-References

- [bcChbC (Bacillus cereus Chitobiose Transporter)](/xray-mp-wiki/proteins/bc-chbc) — Comparison structure; inward-facing occluded conformation of [Glucose](/xray-mp-wiki/reagents/additives/glucose) superfamily EIIC
- [Elevator Mechanism](/xray-mp-wiki/concepts/elevator-mechanism) — bcMalT provides structural evidence for elevator-car transport in EIIC transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism) — bcMalT and bcChbC represent outward- and inward-facing states of the alternating-access cycle
- [Maltose](/xray-mp-wiki/reagents/additives/maltose) — bcMalT selectively binds and transports [Maltose](/xray-mp-wiki/reagents/additives/maltose); IC50 4.5 uM
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) — bcMalT crystallized using LCP method with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein)
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm) — [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm) used for membrane protein solubilization during bcMalT purification
- [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/lDAO) — [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/lDAO) used for functional assays and proteoliposome reconstitution
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) — [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) used as lipid matrix in LCP crystallization of bcMalT
- [Size-Exclusion Chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) — Purification method used in protein preparation
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) — Purification method used in protein preparation
