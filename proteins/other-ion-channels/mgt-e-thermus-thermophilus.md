---
title: "MgtE (Magnesium Transport Channel)"
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature06093, doi/10.1038##s41467-017-00082-w, doi/10.1038##emboj.2009.288, doi/10.1038##ncomms6374]
verified: false
---

# MgtE (Magnesium Transport Channel)

## Overview

MgtE is a magnesium-selective ion channel from Thermus thermophilus that mediates
Mg2+ uptake across the cytoplasmic membrane. It functions as a homodimer, with
each subunit containing an N-terminal cytosolic domain followed by five
transmembrane helices. The cytosolic domain acts as a Mg2+ sensor that regulates
channel gating in response to intracellular Mg2+ concentration, enabling Mg2+
homeostasis. The N-terminal cytosolic domain comprises an N domain and two
tandem CBS (cystathionine beta-synthase) domains. The closed-state structure
shows the ion-conducting pore occluded on both the periplasmic side (by a
hydrophobic gate at Pro321) and the cytosolic side (by plug helices from the
CBS domains). Seven Mg2+-binding sites in the cytosolic domain cooperatively
stabilize the closed conformation at high intracellular Mg2+ concentrations.
A high-resolution (2.2 A) crystal structure of the MgtE transmembrane domain
revealed that the selectivity filter (M1 site) recognizes fully hydrated Mg2+
ions via carboxylate groups of Asp432, in contrast to dehydrated K+ recognition
by KcsA. Periplasmic M2 and M3 sites bind transition metal cations such as Mn2+
and regulate channel gating.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##emboj.2009.288 | 2ZY9 | 2.94 | Not specified | Full-length Thermus thermophilus MgtE | Mg2+ ions (7 binding sites: Mg1-Mg7) |
| doi/10.1038##ncomms6374 | 4U9L | 2.2 | P 2(1) 2(1) 2(1) | MgtE transmembrane domain (MgtE-TMD) from Thermus thermophilus | Mg2+, Mn2+, Ca2+ ions at M1 site; Mn2+ at M2, M2', M3 sites |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length Thermus thermophilus MgtE with His6 tag in pET vector

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: His6 tag
- **Tag info**: His6 tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization and extraction | Detergent solubilization | -- | 50 mM HEPES pH 7.0, 150 mM NaCl + 0.1% (w/v) n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Protein expressed and solubilized in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) as described in Hattori et al., 2007 |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA (Qiagen) | 50 mM HEPES pH 7.0, 150 mM NaCl + 0.25% (w/v) n-nonyl-beta-D-thiomaltoside (NTM) | Detergent exchanged from [DDM](/xray-mp-wiki/reagents/detergents/ddm/) to NTM during purification. Wash with 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), elute with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | SEC | HiLoad 16/60 [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM HEPES pH 7.0, 150 mM NaCl + 0.25% (w/v) NTM | Final purification step |


## Crystallization

### doi/10.1038##emboj.2009.288

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified full-length MgtE in NTM at ~10 mg/ml |
| Reservoir | 7-9% [PEG](/xray-mp-wiki/reagents/additives/peg/) 4000, 0.2 M MgCl2, 0.1 M MES pH 6.5 |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | 9% [PEG](/xray-mp-wiki/reagents/additives/peg/) 4000, 0.2 M MgCl2, 0.1 M MES pH 6.5, 30% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Notes | New crystal form obtained by extensive detergent screening. Co2+-soaked crystals used for anomalous signal to confirm Mg2+-binding sites. Structure determined at 2.94 A resolution, improved from earlier 3.5 A structure. |

### doi/10.1038##ncomms6374

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified MgtE-TMD after TEV cleavage, in 0.1% DDM |
| Reservoir | Not specified in detail |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | MgtE-TMD crystals obtained after TEV protease cleavage of the loop connecting cytosolic and TM domains. Three data sets collected: Mg2+-bound (2.2 A), Mn2+-bound (2.2 A native, 2.84 A anomalous), and Ca2+-bound (3.2 A). |


## Biological / Functional Insights

### MgtE is a highly Mg2+-selective channel gated by intracellular Mg2+ concentration

Patch-clamp electrophysiology of MgtE expressed in giant E. coli spheroplasts demonstrated single-channel currents with a conductance of 96 pS for Mg2+. The channel is highly selective for Mg2+ over Ca2+, Ni2+, and Mn2+. Increasing intracellular Mg2+ from 0.2 to 10 mM progressively decreased channel open probability, directly demonstrating Mg2+-dependent gating. Co(III) hexamine, a hydrated Mg2+ analog, completely blocked Mg2+ influx.

### Seven cooperative Mg2+-binding sites in the cytosolic domain control gating

The higher-resolution 2.94 A structure identified seven Mg2+-binding sites (Mg1-Mg7) in the cytosolic domain. Mg5 at the CBS domain dimer interface and Mg2/Mg3 on the plug helices are particularly important. Mutations at these sites (D226N/D250A for Mg5, E258Q for Mg2, D259N for Mg3) largely abolished Mg2+-dependent suppression of channel opening. The Mg7 site at the N domain-CBS interface contributes a weaker regulatory function. All sites function cooperatively to stabilize the closed state at high Mg2+.

### Dual occlusion of the MgtE pore in the closed state

The updated structure revealed that the MgtE pore is occluded on both sides: a hydrophobic gate at Pro321 (kinked TM2 helix with F318, P321, L324) on the periplasmic side, and plug helices from the CBS domains on the cytosolic side. This dual-gate architecture ensures complete channel closure at high intracellular Mg2+ concentrations. For channel opening, both the TM2 helices must move apart at Pro321 and the plug helices must disengage.

### Cooperativity model for Mg2+ sensing and channel gating

A three-state model is proposed: open state (low Mg2+), transiently closed state (intermediate Mg2+), and stable closed state (high Mg2+). Mg2+ binding to any temporary binding site stabilizes the closed conformation, facilitating further Mg2+ binding to other sites. All seven binding sites cooperatively regulate the structural transition, providing a sensitive homeostatic mechanism for maintaining intracellular Mg2+ concentration.

### Ion selectivity via hydrated Mg2+ recognition

The 2.2 A crystal structure of the MgtE-TMD revealed that the M1 site (selectivity filter) recognizes Mg2+ in a fully hydrated state. Asp432 carboxylate groups form hydrogen bonds with water molecules in the first hydration shell of Mg2+, while the ion itself remains hydrated with 6 water molecules in octahedral coordination (average Mg2+-O distance 2.11 A). This is fundamentally different from K+ channels like KcsA, which recognize dehydrated K+. The geometry of the hydration shell is critical: Mg2+ and Mn2+ (which form stable octahedral hydration) bind tightly, while Ca2+ (with flexible 6-8 coordination) binds more weakly. Na+ and K+ (monovalent, weaker electrostatic interaction with Asp432) also cannot compete effectively. This mechanism explains the high Mg2+ selectivity with minimal dehydration energy cost.

### Periplasmic gating sites for transition metal selectivity

Three periplasmic metal-binding sites (M2, M2', M3) were identified in the Mn2+-bound structure. The M2 site involves Gln304, Glu307, and His383 from adjacent protomers. The M3 site involves Glu307 and Glu311. Mn2+ binding at these sites decreases channel open probability (shown by patch-clamp), acting as a gating mechanism to prevent toxic transition metal uptake. The M2M3A mutant (disrupting these sites) loses Mn2+-dependent inhibition but retains Mg2+ selectivity at the M1 site, confirming the distinct roles of the selectivity filter and periplasmic gating sites.


## Cross-References

- [CorA Mg2+ Channel](/xray-mp-wiki/proteins/corA/) — Functional homolog also involved in bacterial Mg2+ transport
- [Magnesium Homeostasis](/xray-mp-wiki/concepts/magnesium-homeostasis/) — MgtE directly participates in cellular Mg2+ homeostasis
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for protein extraction
- [NTM (n-Nonyl-beta-D-Thiomaltoside)](/xray-mp-wiki/reagents/detergents/ntm/) — Detergent used for crystallization
- [Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) — Crystallization method used for MgtE
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
