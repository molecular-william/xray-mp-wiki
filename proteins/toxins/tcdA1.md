---
title: "TcdA1 Toxin Complex A Subunit from Photorhabdus luminescens"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein]
sources: [doi/10.1038##nature13015]
verified: false
---

# TcdA1 Toxin Complex A Subunit from Photorhabdus luminescens

## Overview

TcdA1 is the TcA subunit of the toxin complex from Photorhabdus luminescens subsp. akhurstii. It forms a large bell-shaped pentameric structure that perforates host membranes and translocates toxic enzymes into host cells. The prepore structure was solved at 4.0 A resolution by X-ray crystallography, and the pore structure at 9 A by [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em). The structure reveals a translocation channel, four receptor-binding sites, and a neuraminidase-like region important for host specificity. The transition from prepore to pore state involves pH-induced shell opening driven by an entropic spring mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13015 | 4O9Y | 4.0 A | not specified | TcdA1 full-length from P. luminescens subsp. akhurstii (12500 residues in pentamer, 1.41 MDa) | None |
| doi/10.1038##nature13015 | 4O9Y | 9 A | C5 (cryo-EM) | TcdA1 pore state from P. luminescens subsp. akhurstii | None |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: TcdA1 full-length from P. luminescens subsp. akhurstii, overexpressed and purified as previously described

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and expression | Overexpression in E. coli BL21(DE3) | -- | not specified + -- | TcdA1 overexpressed and purified as previously described |
| Dialysis | Dialysis | -- | 50 mM [MES](/xray-mp-wiki/reagents/buffers/mes) pH 5.0, 100 mM NaCl, 0.05% [Tween-20 Polysorbate 20 Nonionic Detergent](/xray-mp-wiki/reagents/detergents/tween-20), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + [Tween-20 Polysorbate 20 Nonionic Detergent](/xray-mp-wiki/reagents/detergents/tween-20) | Dialysis of TcdA1 against purification buffer |
| Size-exclusion chromatography | Size-exclusion chromatography | Superose 6 10/300 GL column (GE Healthcare Life Sciences) | 50 mM [MES](/xray-mp-wiki/reagents/buffers/mes) pH 5.0, 100 mM NaCl, 0.05% [Tween-20 Polysorbate 20 Nonionic Detergent](/xray-mp-wiki/reagents/detergents/tween-20), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + [Tween-20 Polysorbate 20 Nonionic Detergent](/xray-mp-wiki/reagents/detergents/tween-20) | Final purification step, concentrated to 15-20 mg/mL using Amicon filter devices |


## Crystallization

### doi/10.1038##nature13015

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 15-20 mg/mL TcdA1 in 50 mM [MES](/xray-mp-wiki/reagents/buffers/mes) pH 5.0, 100 mM NaCl, 0.05% [Tween-20 Polysorbate 20 Nonionic Detergent](/xray-mp-wiki/reagents/detergents/tween-20), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) |
| Reservoir | 0.1 M [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.0, Jeffamine ED-2001, 1.1 M sodium malonate |
| Temperature | 4 C |
| Growth time | 5-7 days |
| Cryoprotection | Reservoir solution with 5-25% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), flash frozen in liquid nitrogen |
| Notes | Crystals reached approximately 300 x 200 x 200 micrometers. Data collected at PXII-X10SA beamline at Swiss Light Source. Structure solved at 4.0 A by molecular replacement using previous 6.3 A [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em) search model with PHENIX. |


## Biological / Functional Insights

### Domain organization and receptor-binding sites

The TcdA1 protomer is composed of eight domains. Six domains form the alpha-helical shell and are connected by a ~42 amino acid linker to two domains forming the inner channel. The pentamer assembles through tight protomer-protomer interactions. TcA forms four receptor-binding domains (A-D) with structural homology to host cytokine receptors (IFNAR2, IL17-R, IL2-R, IL15-R, IL12-R families), suggesting adaptation to eukaryotic cell surface receptors. The receptor-binding domains are positioned approximately 125 A from the membrane, consistent with binding to elongated cell surface proteins such as integrins.

### Entropic spring mechanism drives membrane injection

The linker connecting the shell and channel in the prepore state has a stretched-out conformation (113 A for 48 residues). In the pore state, the linker contracts, indicating it acts as an entropic spring. Steered molecular dynamics simulations show a free energy gain of 20-66 kcal/mol with strong entropic contribution, suggesting the process is exergonic. The stretched linker in the prepore state can only achieve its preferred condensed conformation once the shell opens, pulling on the central channel and driving the syringe-like injection mechanism.

### Translocation channel properties

The luminal surface of the channel is mainly negatively charged with conserved charged residues protruding into the lumen, supporting cation selectivity. The channel diameter varies, narrowing from top to bottom with the narrowest position at tyrosine 2163 (minimal diameter 3.9 A). A ring of 15 arginines marks the upper end of the transmembrane region, providing a positively charged ring that likely interacts with the negatively charged membrane surface. The outer surface of the putative transmembrane region (residues 2107-2158) is predominantly hydrophobic.

### Transition from prepore to pore state

Pore formation involves marked conformational changes including shell opening and a 12 nm shift of the central channel. Three major hinge regions drive the opening: two involve receptor-binding domains and one between the two lobes of the alpha-helical shell domain. The shell subunits from adjacent protomers overlap like an iris diaphragm, with electrostatic interactions mediating the interface. pH-induced changes at the neuraminidase-like domains create strong repulsions that act as an electrostatic lock responsible for pH-induced shell opening.

### pH-independent translocation of cationic substrates

The TcdA1 channel is cation selective, similar to the anthrax translocation pore. However, the translocated domains in Tc complexes from P. luminescens (hypervariable regions of TccC3 and TccC5) are both cationic substrates with isoelectric points of 9.68 and 8.65, respectively. This contrasts with the anionic anthrax lethal factor and suggests a pH-independent translocation mechanism for Tc toxins, as cationic substrates would not require protonation-driven Brownian ratchet movement.


## Cross-References

- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — 0.1 M HEPES pH 7.0 component of TcdA1 crystallization reservoir
- [Sodium Malonate](/xray-mp-wiki/reagents/additives/sodium-malonate/) — 1.1 M sodium malonate precipitant in TcdA1 crystallization
- [Jeffamine ED-2001](/xray-mp-wiki/reagents/additives/jeffamine-ed-2001/) — Polyalkylene glycol precipitant in TcdA1 crystallization
- [Tween-20](/xray-mp-wiki/reagents/detergents/tween-20/) — 0.05% Tween-20 in TcdA1 purification and crystallization buffers
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — 50 mM MES pH 5.0 in TcdA1 dialysis and storage buffer
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method used for TcdA1
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Structure solution method for TcdA1 at 4.0 A using previous cryo-EM search model
- [Cryo-EM](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Used to determine TcdA1 pore state structure at 9 A resolution
- [Tween-20 Polysorbate 20 Nonionic Detergent](/xray-mp-wiki/reagents/detergents/tween-20) — Entity mentioned in text
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em) — Entity mentioned in text
