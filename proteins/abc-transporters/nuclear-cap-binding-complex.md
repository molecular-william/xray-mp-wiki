---
title: "Nuclear Cap-Binding Complex (CBC)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [receptor, xray-crystallography]
sources: [doi/10.1038##s41467-017-01402-w]
verified: false
---

# Nuclear Cap-Binding Complex (CBC)

## Overview

The nuclear cap-binding complex (CBC) is a heterodimer of CBP20 (NCBP2, 20 kDa) and CBP80 (NCBP1, 80 kDa) that binds tightly to the 5′-cap structure (m⁷GpppN) added co-transcriptionally to all nascent Pol II transcripts. CBC protects capped transcripts from decapping and 5′-3′ degradation, and acts as a platform for interaction with nuclear factors that determine transcript fate. Crystal structures of human CBC bound to C-terminal peptides of ARS2 or NELF-E have been determined at 2.8 Å resolution, revealing that both partners bind identically to the same site at the CBP20-CBP80 interface. The homologous C-terminal peptides of NELF-E and ARS2 share 7 identical residues out of 21, including key interacting residues that form a bipartite binding site. These structures define two mutually exclusive CBC-containing complexes: CBC-NELF-E (associated with early transcription pausing) and CBC-ARS2-PHAX (associated with later events such as 3′-end processing and nuclear export).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-017-01402-w | 5OO6 | 2.79 | P2₁ | CBC-ΔNLS (CBP80 with residues 1-19 deleted) + CBP20, reconstituted heterodimer; crystallized with m⁷GTP and NELF-E³⁶⁰⁻³⁸⁰ synthetic peptide | m⁷GTP, NELF-E³⁶⁰⁻³⁸⁰ peptide |
| doi/10.1038##s41467-017-01402-w | 5OO6 | 2.80 | P1 | CBC-ΔNLS (CBP80 with residues 1-19 deleted) + CBP20, reconstituted heterodimer; crystallized with m⁷GTP and ARS2⁸²⁷⁻⁸⁷¹ peptide | m⁷GTP, ARS2⁸²⁷⁻⁸⁷¹ peptide |

 - R-work 20.2%, R-free 22.9%; Data collection: ESRF ID30A1, 0.966 Å wavelength; 117,089 reflections (6345 free); redundancy 2.71
 - R-work 23.1%, R-free 26.8%; Data collection: ESRF ID23-1, 0.97917 Å wavelength; 190,778 reflections (10,059 free); redundancy 2.08

## Expression and Purification

- **Expression system**: E. coli Rosetta 2 for CBP20 and ARS2/NELF-E/PHAX constructs; High Five insect cells for CBP80ΔNLS and full-length NELF-E

- **Construct**: CBP20 with N-terminal GST tag (pETM30). CBP80ΔNLS (residues 1-19 deleted) expressed in insect cells. Reconstituted CBC heterodimer by co-purification: His-tagged CBP20 lysate immobilized on Ni-sepharose, then CBP80 lysate applied to the column.


### Purification Workflow

- **Expression system**: E. coli Rosetta 2 / High Five insect cells
- **Expression construct**: CBP20 (GST-tag), CBP80ΔNLS (insect cells), ARS2 constructs (pETM11), NELF-E constructs (pETM11), PHAX constructs (pETM11)
- **Tag info**: N-terminal 6xHis-tag (TEV-cleavable) for CBP20, ARS2, NELF-E, PHAX constructs

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | — | 50 mM HEPES pH 7.8, 300 mM NaCl, 10% v/v [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM β-mercaptoethanol | Lysates clarified by centrifugation |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Nickel [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — | 50 mM HEPES pH 7.8, 300 mM NaCl, 10% v/v [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM β-mercaptoethanol | Washed with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in lysis buffer |
| TEV protease cleavage | Proteolytic cleavage | — |  | Overnight dialysis into 20 mM HEPES pH 7.8, 120 mM NaCl, 10% v/v [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM β-mercaptoethanol with His-tagged TEV protease at 1:100 ratio |
| Reverse Ni-NTA | Nickel [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (flow-through) | — |  | Post-cleavage sample passed over Ni-sepharose to remove TEV and uncleaved protein |
| Anion exchange chromatography | [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) | — | 20 mM HEPES pH 7.8, 50-800 mM NaCl gradient, 0.5 mM TCEP | HitTrap Q column; optional HiTrap Heparin column used for some constructs |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### ARS2 and NELF-E Bind Identically to CBC

The C-terminal peptides of ARS2 (residues 845-871) and NELF-E (residues 360-380) bind to exactly the same site on m⁷GTP-bound CBC, at the interface of CBP20 and CBP80, with a total buried surface area of ~2500 Å² shared equally between the two subunits. Key interactions include: (i) Arg854 (ARS2) / Arg362 (NELF-E) interacting with CBP80 Tyr461 and CBP20 Gln55/Asp107; (ii) Tyr859 (ARS2) / Tyr367 (NELF-E) buried in a pocket with CBP20 Glu53; (iii) Phe871 (ARS2) / Phe380 (NELF-E) interacting with CBP80 His651. A sequence alignment reveals 7 identical residues out of 21, explaining the identical binding mode. NELF-E has an additional tyrosine (Tyr372) that makes van der Waals contacts with CBP20 Ile70.

### Cap-Dependent Enhancement of Partner Binding

Both ARS2 and NELF-E binding to CBC is enhanced in the presence of the cap analogue m⁷GTP. ARS2 binding affinity increases 12-fold (K_D ~12 μM without cap vs ~1 μM with cap). NELF-E binding affinity increases 8-fold (K_D ~0.4 μM without cap vs ~0.05 μM with cap). PHAX binding is less cap-dependent (K_D ~0.3 μM without cap vs ~0.125 μM with cap). This cap-dependent enhancement suggests a mechanism where CBC recruitment to the capped transcript precedes high-affinity binding of these partners.

### Two Mutually Exclusive CBC Complexes

Competition assays demonstrate that CBC-NELF-E and CBC-ARS2-PHAX form mutually exclusive complexes. NELF-E binding to CBC is incompatible with PHAX binding, while ARS2 and PHAX can simultaneously bind CBC. This defines two distinct complexes: (i) CBC-NELF-E, associated with early Pol II pausing, and (ii) CBC-ARS2-PHAX, involved in later snRNA/snoRNA export. PHAX binding to CBC is not cap-dependent and PHAX cannot bind simultaneously with NELF-E, suggesting a sequential remodeling of CBC complexes during transcription.

### Peptide Binding Determinants by ITC

The C-terminal 27 residues of ARS2 (845-871) are sufficient for CBC binding. The C-terminal 21 residues of NELF-E (360-380) bind CBC with K_D ~3.3 μM (with cap), but the longer NELF-E²⁴⁴⁻³⁸⁰ construct (including the RRM domain) binds more strongly (K_D ~0.05 μM), suggesting additional stabilizing interactions. CBC with CBP20 mutations Y50A/Y89A (CBCmut) abolishes binding to both NELF-E and ARS2, confirming the shared binding interface.


## Cross-References

- [Human Delta-Opioid Receptor (DOP)](/xray-mp-wiki/proteins/gpcr/delta-opioid-receptor/) — Reference for crossover topic; both illustrate X-ray crystallography of protein-ligand complexes
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
