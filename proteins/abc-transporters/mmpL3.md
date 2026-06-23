---
title: MmpL3 from Mycobacterium smegmatis
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1901346116, doi/10.1016##j.cell.2019.01.003, doi/10.1016##j.jmb.2020.05.019]
verified: true
---

# MmpL3 from Mycobacterium smegmatis

## Overview

MmpL3 (Mycobacterial membrane protein Large 3) is an inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/) transporter essential for mycolic acid biosynthesis in mycobacteria. It transports [Trehalose](/xray-mp-wiki/reagents/additives/trehalose) monomycolate (TMM) from the cytoplasm to the cell envelope, a pivotal step in cell wall synthesis. MmpL3 belongs to the Resistance Nodulation Division ([RND](/xray-mp-wiki/concepts/protein-families/rnd-superfamily/)) protein superfamily and is a validated target for anti-tuberculosis drug discovery. The protein from Mycobacterium smegmatis serves as an excellent model for the Mycobacterium tuberculosis ortholog.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2019.01.003 | 6AJF | 3.0 | not reported | M. smegmatis MmpL3 (residues 1-748) fused to T4 lysozyme (160 aa) + 10x [His tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) | none |
| doi/10.1016##j.cell.2019.01.003 | 6AJG | 2.6 | not reported | M. smegmatis MmpL3 (residues 1-748) fused to T4 lysozyme (160 aa) + 10x [His tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) | [SQ109](/xray-mp-wiki/reagents/ligands/sq109) |
| doi/10.1016##j.cell.2019.01.003 | 6AJH | 2.7 | not reported | M. smegmatis MmpL3 (residues 1-748) fused to T4 lysozyme (160 aa) + 10x [His tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) | [AU1235](/xray-mp-wiki/reagents/ligands/au1235) |
| doi/10.1016##j.cell.2019.01.003 | 6AJI | 2.9 | not reported | M. smegmatis MmpL3 (residues 1-748) fused to T4 lysozyme (160 aa) + 10x [His tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) | [Rimonabant](/xray-mp-wiki/reagents/ligands/rimonabant) |
| doi/10.1016##j.cell.2019.01.003 | 6AJJ | 2.8 | not reported | M. smegmatis MmpL3 (residues 1-748) fused to T4 lysozyme (160 aa) + 10x [His tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) | [ICA38](/xray-mp-wiki/reagents/ligands/ica38) |
| doi/10.1016##j.jmb.2020.05.019 | 7C2M | 3.1 | P2_12_12_1 | M. smegmatis MmpL3 (residues 1-748) fused to T4 lysozyme (160 aa) + 10x [His tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) | [NITD-349](/xray-mp-wiki/reagents/ligands/nitd-349) |
| doi/10.1016##j.jmb.2020.05.019 | 7C2N | 2.8 | P2_12_12_1 | M. smegmatis MmpL3 (residues 1-748) fused to T4 lysozyme (160 aa) + 10x [His tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) | [SPIRO](/xray-mp-wiki/reagents/ligands/spiro) |
| doi/10.1073##pnas.1901346116 |  | 2.59 |  | M. smegmatis MmpL3_773 (residues 1-773) with C-terminal 6xHis tag, expressed in E. coli BL21(DE3)ΔacrB | phosphatidylethanolamine (PE), DDM |

## Expression and Purification

- **Expression system**: Mycobacterium smegmatis mc2155
- **Construct**: [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) 748 residues of M. smegmatis MmpL3 (MSMEG_0250) fused to T4 lysozyme (160 aa) at C-terminus with 10x [His tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/)
- **Induction**: 0.2% acetamide at 16 C for four days
- **Media**: Luria broth with 50 ug/mL [kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) and 20 ug/mL [carbenicillin](/xray-mp-wiki/reagents/additives/carbenicillin/)

### Purification Workflow

*Source: doi/10.1016##j.cell.2019.01.003*

- **Expression system**: Mycobacterium smegmatis mc2155

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | [French press](/xray-mp-wiki/methods/cell-lysis/french-press/) at 1,200 bar | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Cell debris removed by centrifugation at 8,000 rpm for 15 min at 4 C |
| Membrane fractionation | Ultra-centrifugation at 150,000 g for 1 h | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |  |
| Solubilization | Detergent extraction at 4 C for 1.5 h | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Affinity capture | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose incubation for 2 h at 4 C | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 10 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Wash | Column wash | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 50 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Elution | [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) elution | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 300 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Size exclusion chromatography | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) on Superose-6 increase | Superose-6 increase (GE Healthcare) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Concentrated to ~15 mg/mL for crystallization |

### Purification Workflow

*Source: doi/10.1016##j.jmb.2020.05.019*

- **Expression system**: Mycobacterium smegmatis mc2155

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | [French press](/xray-mp-wiki/methods/cell-lysis/french-press/) at 1,200 bar | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Cell debris removed by centrifugation at 8,000 rpm for 15 min at 4 C |
| Membrane fractionation | Ultra-centrifugation at 150,000 g for 1 h | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |  |
| Solubilization | Detergent extraction at 4 C for 1.5 h | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Affinity capture | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose incubation for 2 h at 4 C | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 10 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Wash | Column wash | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 50 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Elution | [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) elution | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 300 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Size exclusion chromatography | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) on Superose-6 increase | Superose-6 increase (GE Healthcare) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 6-n-dodecyl-alpha,alpha-[Trehalose](/xray-mp-wiki/reagents/additives/trehalose) ([6-n-Dodecyl-alpha,alpha-trehalose](/xray-mp-wiki/reagents/lipids/6-ddtre)) | Peak fractions pooled and concentrated to 15 mg/mL for crystallization |


## Crystallization

### doi/10.1016##j.cell.2019.01.003

| Parameter | Value |
|---|---|
| Method | [sitting-drop vapor diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), ~15 mg/mL |
| Temperature | 293 K |
| Growth time | not reported |

| Parameter | Value |
|---|---|
| Method | [sitting-drop vapor diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | M. smegmatis MmpL3-T4L complex with [SQ109](/xray-mp-wiki/reagents/ligands/sq109) |
| Temperature | not reported |
| Growth time | not reported |

| Parameter | Value |
|---|---|
| Method | [sitting-drop vapor diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | M. smegmatis MmpL3-T4L complex with [AU1235](/xray-mp-wiki/reagents/ligands/au1235) |
| Temperature | not reported |
| Growth time | not reported |

| Parameter | Value |
|---|---|
| Method | [sitting-drop vapor diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | M. smegmatis MmpL3-T4L complex with [ICA38](/xray-mp-wiki/reagents/ligands/ica38) |
| Temperature | not reported |
| Growth time | not reported |

| Parameter | Value |
|---|---|
| Method | [sitting-drop vapor diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | M. smegmatis MmpL3-T4L complex with [Rimonabant](/xray-mp-wiki/reagents/ligands/rimonabant) |
| Temperature | not reported |
| Growth time | not reported |

### doi/10.1016##j.jmb.2020.05.019

| Parameter | Value |
|---|---|
| Method | [hanging-drop vapor diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | M. smegmatis MmpL3-T4L complex with [NITD-349](/xray-mp-wiki/reagents/ligands/nitd-349), 6-8 mg/mL protein, 0.5 mM ligand, 10%-20% PEGMME 350, 50 mM ADA pH 6.0-7.0, 7.5%-17.5% [PEG200](/xray-mp-wiki/reagents/additives/peg200)0 |
| Temperature | 16 C |
| Growth time | 3 days |

| Parameter | Value |
|---|---|
| Method | [hanging-drop vapor diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | M. smegmatis MmpL3-T4L complex with [SPIRO](/xray-mp-wiki/reagents/ligands/spiro), 6-8 mg/mL protein, 0.5 mM ligand, 10%-20% PEGMME 350, 50 mM ADA pH 6.0-7.0, 7.5%-17.5% [PEG200](/xray-mp-wiki/reagents/additives/peg200)0 |
| Temperature | 16 C |
| Growth time | 3 days |


## Biological / Functional Insights

### Periplasmic pore domain structure

The [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) pore domain consists of two subdomains, PN and PC, both adopting a beta-alpha-beta-alpha-beta fold. The subdomains intertwine to create a central cavity connecting to three openings: a funnel at the top (GT), an opening in the front (GF), and an opening at the back (GB). Two 6-n-dodecyl-alpha,alpha-[Trehalose](/xray-mp-wiki/reagents/additives/trehalose) ([6-n-Dodecyl-alpha,alpha-trehalose](/xray-mp-wiki/reagents/lipids/6-ddtre)) detergent molecules, mimics of the substrate TMM, are bound in the cavity and GT opening, suggesting potential roles in substrate transportation.

### Transmembrane helix bundle and proton-translocation mechanism

The transmembrane region contains 12 transmembrane helices with a pseudo-two-fold symmetry axis relating the six [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) and six [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) helices. Two conserved Asp-Tyr pairs (Asp256-Tyr646 and Asp645-Tyr257) are located centrally in TM helices IV and X, linked by [hydrogen bonds](/xray-mp-wiki/concepts/hydrogen-bonding/). These pairs are a conserved feature of MmpL family transporters and appear to facilitate proton-translocation, generating the [proton motive force](/xray-mp-wiki/concepts/proton-motive-force/) for substrate transport.

### Inhibitor binding disrupts proton-translocation channel

Six drug candidates ([SQ109](/xray-mp-wiki/reagents/ligands/sq109), [AU1235](/xray-mp-wiki/reagents/ligands/au1235), [ICA38](/xray-mp-wiki/reagents/ligands/ica38), [Rimonabant](/xray-mp-wiki/reagents/ligands/rimonabant), [NITD-349](/xray-mp-wiki/reagents/ligands/nitd-349), and [SPIRO](/xray-mp-wiki/reagents/ligands/spiro)) bind inside the transmembrane region, disrupting both Asp-Tyr pairs implicated in proton relay. Upon inhibitor binding, [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) transmembrane helices undergo [conformational changes](/xray-mp-wiki/concepts/structural-mechanisms/conformational-change/), moving away from the center and expanding the narrow proton-translocating channel to accommodate the inhibitors. The binding pocket can be divided into five subsites (S1-S5), with S1-S3 and S5 being hydrophobic and S4 containing the two Asp-Tyr pairs.

### Chimeric MmpL3 for drug screening

A chimeric MmpL3 construct with M. tuberculosis-equivalent residues in the binding pocket (S301A/I319T/V638L/L686V) was created to study interactions with the Mtb ortholog. This chimeric protein binds all four inhibitors with similar affinity to wild-type M. smegmatis MmpL3, making it suitable for future drug screening applications.

### Drug resistance mutations map to binding pocket

Approximately 80% of known drug resistance mutations lie inside or within 10 Angstroms of the combined inhibitor binding pocket. Key resistance mutations include Y257C (affects [SQ109](/xray-mp-wiki/reagents/ligands/sq109) and [AU1235](/xray-mp-wiki/reagents/ligands/au1235) binding) and S293A (disrupts binding through [hydrogen bond](/xray-mp-wiki/concepts/hydrogen-bonding/) disruption). These findings confirm the proton-translocating channel as the common target for all six compound classes.

### NITD-349 binding mode and inhibitory mechanism

[NITD-349](/xray-mp-wiki/reagents/ligands/nitd-349) binds deep in the central channel of the transmembrane domain. The indole group inserts into the upper hydrophobic region (Ile249, Ile253, Ile297, Val638, Gly641, Leu642, Leu686, Leu708). The amide nitrogen and indole nitrogen interact with Asp645, while the amide oxygen bonds with Asp256. The dimethylcyclohexane group presses down Phe260 and Phe649. The binding pocket volume is ~206 A^3. [conformational changes](/xray-mp-wiki/concepts/structural-mechanisms/conformational-change/) include TMH I, IV, V, VI, VII, VIII, IX, X, and XI rotating away from the center.

### SPIRO binding mode and inhibitory mechanism

[SPIRO](/xray-mp-wiki/reagents/ligands/spiro) binds to the same pocket with a slightly larger volume (~214 A^3). The benzodioxane head interacts with hydrophobic residues in the upper pocket. The thiophene of the spirocyclic thienopyran inserts between Tyr257 and Phe649, forming pi-pi stacking. The piperidine nitrogen interacts with Asp645 and Tyr646. Phe260 and Phe649 undergo downward [conformational changes](/xray-mp-wiki/concepts/structural-mechanisms/conformational-change/). The same [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) helices move outward as with [NITD-349](/xray-mp-wiki/reagents/ligands/nitd-349), but to a greater degree.

### Inhibitor binding pocket plasticity

Overlay of all six complex structures reveals the plasticity of the MmpL3 binding pocket. All inhibitors share a hydrophobic head and tail with nitrogen atoms in the center that form a [hydrogen bond](/xray-mp-wiki/concepts/hydrogen-bonding/) with Asp645. [SPIRO](/xray-mp-wiki/reagents/ligands/spiro) and [NITD-349](/xray-mp-wiki/reagents/ligands/nitd-349) both span subsites S3, S4, and S5, with S4 fully occupied to block proton relay. Other subsites have space for optimization. The Phe260-Phe649 pair adopts different conformations across ligand-bound structures.

### PE and TMM binding specificity of MmpL3

Native mass spectrometry revealed that MmpL3 specifically binds both trehalose monomycolate (TMM, Kd = 3.7 uM) and phosphatidylethanolamine (PE, Kd = 19.5 uM), but not trehalose dimycolate (TDM). MmpL3 also binds PG, PI, DAG, and CDL, indicating it is a promiscuous lipid-binding protein. The PE molecule was unexpectedly discovered inside the crystal structure, bound in a pocket created by TMs 7-10 and the periplasmic domain, involving 21 residues including the conserved Q40. These observations suggest MmpL3 functions by shuttling a variety of lipids across the membrane for cell-wall biogenesis.


## Cross-References

- [AcrB](/xray-mp-wiki/proteins/abc-transporters/acrb/) — RND superfamily member with similar proton-translocation mechanism
- [MexB](/xray-mp-wiki/proteins/abc-transporters/mexb/) — RND family efflux transporter
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization and purification
- [6-n-Dodecyl-alpha,alpha-trehalose](/xray-mp-wiki/reagents/lipids/6-ddtre/) — TMM substrate mimic used in purification and binds in periplasmic cavity
- [NITD-349](/xray-mp-wiki/reagents/ligands/nitd-349/) — Indole-2-carboxamide inhibitor with crystal structure at 3.1 A resolution
- [SPIRO](/xray-mp-wiki/reagents/ligands/spiro/) — Spiropiperidine inhibitor with crystal structure at 2.8 A resolution
- [SQ109](/xray-mp-wiki/reagents/ligands/sq109/) — Diamine inhibitor with similar binding mode to MmpL3
- [Rimonabant](/xray-mp-wiki/reagents/ligands/rimonabant/) — Cannabinoid receptor antagonist repurposed as MmpL3 inhibitor
- [proton motive force](/xray-mp-wiki/concepts/proton-motive-force/) — Entity mentioned in text
- [Trehalose](/xray-mp-wiki/reagents/additives/trehalose) — Entity mentioned in text
