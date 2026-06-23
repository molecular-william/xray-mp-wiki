---
title: CmTMEM175 — Prokaryotic TMEM175 Lysosomal Potassium Channel
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature23269]
verified: false
---

# CmTMEM175 — Prokaryotic TMEM175 Lysosomal Potassium Channel

## Overview

CmTMEM175 is a prokaryotic homologue of the lysosomal potassium channel TMEM175 from Chamaesiphon minutus. TMEM175 is a lysosomal K+ channel important for maintaining membrane potential and pH stability in lysosomes. Unlike canonical 6-TM tetrameric K+ channels, TMEM175 has no TVGYG selectivity filter motif and adopts a completely novel fold. The structure reveals that all six transmembrane helices are tightly packed within each subunit without domain swapping, with TM1 acting as the pore-lining inner helix. Three layers of hydrophobic residues (Ile23, Leu27, Leu30) form an hourglass-shaped ion permeation pathway, with the first isoleucine layer primarily responsible for K+ selectivity. The structure represents a novel architecture of a tetrameric cation channel with a distinct ion selectivity mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature23269 | 5VRE | 3.3 | C2 | Full-length CmTMEM175 with N-terminal hexahistidine tag (removed by thrombin cleavage) | none (apo) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21 (DE3)
- **Construct**: Full-length CmTMEM175 (NCBI WP_015160509.1) in pET15b vector with N-terminal hexahistidine tag and thrombin cleavage site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent extraction | — | 50 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 200 mM KCl, 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), protease inhibitors (leupeptin, pepstatin A, DNaseI, aprotinin, [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/)) + n-Dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | 3 h incubation at room temperature for protein extraction |
| Immobilized metal affinity chromatography | Co2+ affinity column | [Talon](/xray-mp-wiki/reagents/additives/talon/) Co2+ affinity resin (Clontech) | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 200 mM KCl, 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 5-300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + n-Dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); His-tag removed by overnight thrombin digestion at 4 C |
| Size exclusion chromatography | Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (10/30 GL) | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 200 mM KCl, 3 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) + [DM](/xray-mp-wiki/reagents/detergents/dm/) ([DM](/xray-mp-wiki/reagents/detergents/dm/)) | Purified in [Dmng](/xray-mp-wiki/reagents/detergents/dmng/) for crystallization; CmTMEM175 elutes as monodispersed tetramer |


## Crystallization

### doi/10.1038##nature23269

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 6 mg/mL CmTMEM175 in [Dmng](/xray-mp-wiki/reagents/detergents/dmng/) detergent |
| Reservoir | 16-22% [Peg](/xray-mp-wiki/reagents/additives/peg/) 1000, 50 mM CaCl2, 50 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 100 mM NaAc pH 4.6 |
| Temperature | 20 |
| Growth time | 3 days to 2-4 weeks |
| Notes | Cryoprotected with 25% [Peg](/xray-mp-wiki/reagents/additives/peg/) 1000, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 50 mM CaCl2, 50 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 0.5 mM [Dmng](/xray-mp-wiki/reagents/detergents/dmng/), 100 mM NaAc pH 4.6. Heavy atom derivatization with methyl [Mercury](/xray-mp-wiki/reagents/additives/mercury/) chloride (CH3HgCl) for experimental phasing. |


## Biological / Functional Insights

### Novel tetrameric potassium channel architecture

CmTMEM175 represents a completely new fold for tetrameric K+ channels. Unlike canonical 6-TM K+ channels (e.g., Kv channels), all six TM helices are tightly packed within each subunit without domain swapping. TM1 (not TM6) forms the pore-lining inner helix, and there is no separate pore helix or TVGYG selectivity filter motif. DALI structure search yielded no similar structures, confirming the novel architecture.

### Hydrophobic bottleneck as selectivity filter

Three layers of conserved hydrophobic residues (Ile23, Leu27, Leu30) on the C-terminal half of TM1 helices create a ~10 A-long bottleneck with ~3 A diameter at each constriction point. This narrow hydrophobic pathway serves as the ion selectivity filter. Mutagenesis shows that the first isoleucine layer (Ile23) is primarily responsible for K+ selectivity — replacement with asparagine abolishes K+/Cs+ selectivity.

### Hourglass-shaped ion conduction pathway

The four TM1 helices and their extended C-terminal tails create an hourglass-shaped ion permeation pathway. The N-terminal half of TM1 lines the cytosolic entrance with a negatively charged surface potential. No specifically bound ions were observed in the pathway even in crystals soaked with heavy monovalent or divalent cations.

### Conserved RxxxFSD motif for inter-subunit interactions

A conserved RxxxFSD motif (Arg18, Phe22, Ser26, Asp18) mediates key intra- and inter-subunit interactions important for tetramer assembly. Arg18 forms a salt bridge with Asp18 of the same subunit; Asp18 forms a hydrogen bond with Trp70; Phe22 participates in pi-pi stacking with Phe16 of the neighboring subunit.


## Cross-References

- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in the context of Hepes
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in the context of DDM
- [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/) — Referenced in the context of Pmsf
- [Talon](/xray-mp-wiki/reagents/additives/talon/) — Referenced in the context of Talon
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in the context of Imidazole
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Referenced in the context of Superdex 200
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in the context of DM
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in the context of DM
- [Dmng](/xray-mp-wiki/reagents/detergents/dmng/) — Referenced in the context of Dmng
- [Peg](/xray-mp-wiki/reagents/additives/peg/) — Referenced in the context of Peg
