---
title: Human TRPML1 (Mucolipin-1) - Luminal Domain
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3362]
verified: false
---

# Human TRPML1 (Mucolipin-1) - Luminal Domain

## Overview

Human TRPML1 is a Ca2+-release channel primarily located in lysosomes, belonging to the transient receptor potential mucolipin (TRPML) subfamily of ion channels. It plays crucial roles in lysosome-dependent cellular events including exocytosis, membrane trafficking, and autophagy. Mutations in TRPML1 cause mucolipidosis type IV (MLIV), a severe lysosomal storage disorder characterized by neurodegeneration, mental retardation, and blindness. Crystal structures of the luminal I-II linker domain (residues 84-296) at pH 4.5, 6.0, and 7.5 revealed a tetrameric assembly with a novel highly electronegative central pore (the luminal pore) formed by a luminal pore loop, which is critical for the dual regulation of TRPML1 by luminal Ca2+ and pH.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.3362 | 5TJA | 2.3 | I422 | Human TRPML1 residues 84-296 (luminal I-II linker domain) with N-terminal MBP tag and C-terminal hexahistidine tag, thrombin-cleaved |  |
| doi/10.1038##nsmb.3362 | 5TJB | 2.4 | P42(1)2 | Human TRPML1 residues 84-296 (luminal I-II linker domain), residues 200-213 removed, with N-terminal MBP tag and C-terminal hexahistidine tag, thrombin-cleaved |  |
| doi/10.1038##nsmb.3362 | 5TJC | 2.4 | F432 | Human TRPML1 residues 84-296 (luminal I-II linker domain), residues 200-213 removed, with N-terminal MBP tag and C-terminal hexahistidine tag, thrombin-cleaved |  |

## Expression and Purification

- **Expression system**: Escherichia coli Rosetta-gami 2(DE3)
- **Construct**: Human TRPML1 luminal linker (residues 84-296) with N-terminal MBP tag (maltose-binding protein), thrombin recognition site between MBP and linker, and C-terminal hexahistidine tag
- **Induction**: 0.1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 22 degC for 12 hours
- **Media**: LB medium containing 50 ug/ml [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) and 34 ug/ml [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication |  | 50 mM [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/), pH 8.0, 300 mM NaCl, 2.5% (w/w) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Cells resuspended with 5 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.5 mg/ml lysozyme, 25 ug/ml DNase, 2 mM PMSF; debris removed by centrifugation at 17,000g for 30 min |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA His-Bind resin (Novagen) | 50 mM [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/), pH 8.0, 300 mM NaCl, 2.5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Eluted with 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in solution A |
| Amylose [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Amylose resin (NEB) | 50 mM [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/), pH 8.0, 300 mM NaCl, 2.5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Eluted with 20 mM [Maltose](/xray-mp-wiki/reagents/additives/maltose/) in solution A |
| MBP tag cleavage | Proteolytic cleavage |  | Same as gel filtration buffer | Thrombin added at 4 U per mg protein, incubated at 16 degC overnight |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (GE Healthcare) | 10 mM HEPES, 150 mM NaCl, pH 7.5 | Removed MBP tag; peak fractions of tetrameric I-II linker collected and concentrated to 4 mg/ml |


## Crystallization

### doi/10.1038##nsmb.3362

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | TRPML1 luminal linker at 4 mg/ml in 10 mM HEPES, 150 mM NaCl, pH 7.5 |
| Reservoir | 1.38 M [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) monobasic monohydrate, 0.42 M potassium phosphate dibasic, pH 6.0, 5% pentaerythritol ethoxylate |
| Temperature | 16 degC |
| Notes | Crystal form for pH 6.0 (PDB 5TJA). For pH 4.5 (PDB 5TJB), crystallized at 20 degC; for pH 7.5 (PDB 5TJC), crystallized at 20 degC. |


## Biological / Functional Insights

### Dual Ca2+/pH regulation via the luminal pore

TRPML1 activity is regulated by both luminal Ca2+ and H+. Ca2+ inhibits the channel in a dose-dependent manner, and this inhibition is attenuated at acidic pH (lysosomal pH 4.6). The luminal pore contains 12 aspartate residues (D111, D114, D115 per subunit) that create a highly electronegative environment. Mutating all 12 aspartates to glutamine (3DQ mutant) greatly decreased Ca2+ inhibition. Crystal structures at pH 4.5, 6.0, and 7.5 show the luminal pore is virtually unchanged across pH conditions, indicating that Ca2+ inhibition is attenuated at low pH by protonation of the luminal-pore aspartates rather than by conformational changes. This mechanism allows high TRPML1 conductance in acidic lysosomes and low conductance at the neutral extracellular pH.

### MLIV-causing missense mutations disrupt luminal domain structure

Three MLIV-causing missense mutations (L106P, C166F, T232P) are located in the luminal linker domain. L106P is at the junction of the anchoring alpha-helix and luminal pore loop; C166F disrupts an intrasubunit disulfide bond (C166-C192); T232P is on beta5 of a core beta-sheet. All three mutations cause marked changes in secondary structure, disrupt tetrameric assembly, cause protein aggregation, and prevent proper lysosomal localization. The mutant channels produce little or no current.


## Cross-References

- [Maltose-Binding Protein (MBP)](/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/) — Used as N-terminal fusion tag for expression and purification of the TRPML1 luminal linker
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Used in gel filtration buffer at 10 mM, pH 7.5
- [Sodium Phosphate Buffer](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) — Used in purification buffer at 50 mM, pH 8.0 and in crystallization reservoir at 1.38 M
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used for solubilization of full-length TRPML1 for biochemical analyses
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) — Additive used in purification or crystallization buffers
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) — Additive used in purification or crystallization buffers
