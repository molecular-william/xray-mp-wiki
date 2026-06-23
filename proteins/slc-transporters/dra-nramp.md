---
title: "Deinococcus radiodurans Nramp (DraNramp)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2016.09.017, doi/10.7554##eLife.84006]
verified: false
---

# Deinococcus radiodurans Nramp (DraNramp)

## Overview

DraNramp is a divalent metal transporter from Deinococcus radiodurans belonging to the Natural resistance-associated macrophage protein (Nramp) family. It is a homologue of human DMT1 (SLC11A2) and enables manganese and [Iron](/xray-mp-wiki/reagents/additives/iron/) import in bacteria. The protein adopts a LeuT-fold architecture with 11 transmembrane segments. The first crystal structure (PDB 5KTE, 2016) was determined at 3.94 A resolution in an inward-facing, substrate-free conformation with a complete TM1a helix. Subsequent high-resolution structures across three conformations (outward-open, occluded, and inward-open) in both Mn2+-bound and metal-free states provided the first complete molecular map of the Mn2+ transport cycle (Ray et al., 2023). These structures revealed that Nramps achieve alternating access by distinct Mn2+-coordination geometries in different conformations, supported by conserved polar residue networks that gate the outer and inner vestibules. A high-resolution Cd2+-bound structure revealed differences in how Cd2+ and Mn2+ are coordinated, explaining functional differences in their transport.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2016.09.017 | 5KTE | 3.94 A | I222 | Full-length DraNramp from Deinococcus radiodurans with surface patch mutations (QK169-170HH, EEK251-3YYY, RR398-9HH) and N-terminal 25-residue [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/), co-crystallized with Fab fragment | none (apo, inward-facing state) |
| doi/10.7554##eLife.84006 | 8E5V | 2.36 A | P 2 21 21 | WT DraNramp metal-free occluded | none (apo, occluded state) |
| doi/10.7554##eLife.84006 | 8E60 | 2.38 A | P 2 21 21 | WT DraNramp Mn2+-bound occluded | Mn2+ (orthosteric and external sites) |
| doi/10.7554##eLife.84006 | 8E6I | 2.52 A | P 2 21 21 | M230A DraNramp Mn2+-bound inward-open | Mn2+ (orthosteric and external sites) |
| doi/10.7554##eLife.84006 | 8E6M | 2.48 A | P 2 21 21 | WT DraNramp Cd2+-bound inward-open | Cd2+ (orthosteric and external sites) |

## Expression and Purification

- **Expression system**: Escherichia coli C41(DE3)
- **Construct**: DraNramp with N-terminal 25-residue [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) and surface patch mutations, cloned into pET21-N8H

### Purification Workflow

#### Source: doi/10.1016##j.str.2016.09.017


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | -- | 20 mM NaPO4 pH 7.0, 75 mM imidazole-HCl pH 7.0, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + -- | Lysis buffer supplemented with 1 mM [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/), 1 mM [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine/), 0.3 mg/mL DNase I and lysozyme |
| Membrane isolation | Differential centrifugation | -- | 20 mM NaPO4 pH 7.0, 75 mM imidazole-HCl pH 7.0, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + -- | Membranes pelleted at 230,000 x g for 70 min after debris removal at 27,000 x g for 20 min |
| Membrane solubilization | Detergent extraction | -- | 20 mM NaPO4 pH 7.0, 75 mM imidazole-HCl pH 7.0, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% (w/v) beta-dodecylmaltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Solubilization for 1 hr at 4C, clarified at 140,000 x g for 35 min, filtered through 0.45 micron filter |
| IMAC | Immobilized metal affinity chromatography | Ni-Sepharose (GE Healthcare) | 20 mM NaPO4 pH 7.0, 75 mM imidazole-HCl pH 7.0, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.03% beta-DDM + 0.03% beta-DDM | Pre-equilibrated with lysis buffer + 0.03% beta-DDM. Washed thrice with 50 mL. Eluted with [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient to 450 mM. |
| SEC | Size-exclusion chromatography | Superdex S200 (GE Healthcare) | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl, 0.1% (w/v) beta-decylmaltoside ([DM](/xray-mp-wiki/reagents/detergents/dm/)) + 0.1% beta-DM | Protein concentrated to ~1 mL in 50 kDa cutoff centrifugal concentrator before SEC. Pooled fractions concentrated to ~5 mg/mL. |

#### Source: doi/10.7554##eLife.84006


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent extraction | -- | 100 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membranes homogenized and solubilized in 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for 1 hr at 4C |
| IMAC | Immobilized metal affinity chromatography | Ni-Sepharose | 100 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 25 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Washed with 10 CV of wash buffer, eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in same buffer |
| Detergent exchange (LCP prep) | On-column exchange | -- | 10 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl, 0.003% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) | Eluted protein concentrated, exchanged into [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) buffer, and purified by SEC on Superdex S200 in 10 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl, 0.003% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/). Peak fractions concentrated to ~25-40 mg/mL. |


## Crystallization

### doi/10.1016##j.str.2016.09.017

| Parameter | Value |
|---|---|
| Method | Co-crystallization with Fab fragment, vapor diffusion |
| Protein sample | DraNramp-Fab complex at ~5 mg/mL in 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl, 0.1% beta-DM |
| Reservoir | Not specified in detail |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | DraNramp was co-crystallized with a monoclonal Fab fragment isolated from BALB/c mice immunized with DraNramp proteoliposomes. The crystallization construct included three surface patch mutations (QK169-170HH, EEK251-3YYY, RR398-9HH). Data collected at NE-CAT beamline at APS. Structure refined to R = 0.239, R_free = 0.274. Unit cell: 113.13, 132.08, 221.0 A. |

### doi/10.7554##eLife.84006

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | DraNramp at ~25-40 mg/mL in 10 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl, 0.003% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) |
| Temperature | 20 C |
| Growth time | 7-10 days |
| Cryoprotection | Mesh loops, flash-frozen in liquid nitrogen |
| Notes | Protein mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) in 1:1.5 volume ratio using syringe reconstitution method. 60 nL protein bolus + 720 nL precipitant dispensed onto 96-well glass sandwich plates. Metal-free and metal-soaked (5 mM MnCl2 or Cd2+) crystals grown in various precipitant conditions. Crystals grown as 30-40 um rods. Soaking experiments performed by adding 2 uL soak solution to wells for 16-18 hr. Data collected at APS beamlines 24-ID-C and 23-ID-B. |


## Biological / Functional Insights

### Inward-open conformation with complete TM1a

The DraNramp structure at 3.94 A reveals the complete TM segment 1a (absent in previous ScaNramp structure), bent outward at a 103-degree angle between TM1a and TM1b, lying nearly parallel to the membrane. This creates a large aqueous vestibule on the cytoplasmic side. The structure represents a substrate-free inward-facing conformation with the metal-binding site unoccupied.

### TM4 G153R alters metal selectivity

The G153R mutation on TM4 perturbs the closing of the outward metal-permeation pathway and alters the selectivity of the conserved metal-binding site. G153R transports more Ca2+ than wild-type while Cd2+ transport is reduced. The mutation shows additive effects with the M230A selectivity filter mutation, suggesting it distorts the binding site in favor of Ca2+ while maintaining use of the canonical metal-binding site.

### TM1a G45R locks the inward-open state

The G45R mutation on TM1a prevents conformational change by sterically blocking the essential movement of TM1a, locking the transporter in an inward-facing state. G45R drastically decreases accessibility of the outward-open conformational reporter A61C, indicating a strong preference for the inward-open conformation. The mutation does not cause steric clash in the inward-facing state but would clash in the outward-open state.

### TM1a movement is essential for transport

NEM modification of single-cysteine mutants along TM1a severely impaired metal transport for 6 of 7 positions tested, demonstrating that TM1a movement into a congested environment is an integral part of the Nramp conformational change. Tryptophan substitutions at these positions similarly impaired transport and locked the protein in the inward-facing state, confirming that unencumbered TM1a movement is essential for the conformational change and transport cycle.

### High-resolution structures map the complete Mn2+ transport cycle

High-resolution structures of DraNramp in three conformations (outward-open, occluded, inward-open) in both Mn2+-bound and metal-free states provide the first complete molecular map of the Mn2+ transport cycle. The Mn2+-coordination geometry differs across conformations: six-coordinate distorted octahedral in outward-open and occluded states, and seven-coordinate in the inward-open state. The pseudosymmetrically related alanines A53 (TM1a) and A227 (TM6b) alternately coordinate Mn2+ as the gates open and close.

### Polar residue networks gate the outer and inner vestibules

Two conserved polar networks seal the outer gate: the Q378 network (Q378-D56-T130 via conserved waters) and the T228 network (T228-N275-N82). These networks persist in the occluded and inward-open states but are disrupted in the outward-open state. The inner vestibule is gated by the R244 network (R244-E176-D263) and the Q89 network (Q89-Y54-H237). Y54 in TM1a acts as a conserved aromatic gate, progressively swinging downward to open the inner vestibule, with Y54A nearly abolishing transport while Y54F retains near-wildtype activity.

### Cd2+ and Mn2+ differ in coordination and thermodynamics

The Cd2+-bound structure (PDB 8E6M, 2.48 A) reveals inward-open conformation with differences in metal coordination. D56 adopts a different rotamer and does not directly coordinate Cd2+, while M230 (soft sulfur ligand) still coordinates. Cd2+ has six coordinating ligands (vs seven for Mn2+), with longer bond distances. ITC shows Mn2+ binding is endothermic while Cd2+ binding is exothermic. Cd2+ binding favors the inward-open state, whereas Mn2+ favors the occluded state, creating different thermodynamic landscapes for physiological vs toxic metal transport.


## Cross-References

- [SLC11 (NRAMP) Family](/xray-mp-wiki/concepts/protein-families/slc11-nramp-family/) — DraNramp is a member of the Nramp/SLC11 family of divalent metal transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — DraNramp operates via alternating access between inward-open and outward-open states
- [LeuT Return State Mechanism](/xray-mp-wiki/concepts/miscellaneous/leut-return-state-mechanism/) — DraNramp adopts the LeuT-fold architecture common to this transporter superfamily
- [ScaDMT](/xray-mp-wiki/proteins/slc-transporters/sca-dmt/) — Related Nramp family divalent metal transporter from Staphylococcus capitis
- [N-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane protein solubilization
- [Decylmaltoside](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used in SEC buffer and crystallization
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final purification step
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — IMAC used for initial purification via His-tag
- [Lipidic Cubic Phase (LCP)](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method used for high-resolution structures
- [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used in final purification and crystallization buffer
