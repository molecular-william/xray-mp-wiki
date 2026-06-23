---
title: "Sarcolipin (SLN)"
created: 2026-06-03
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, pump]
sources: [doi/10.1038##nature11900, doi/10.1038##nature11899]
verified: false
---

# Sarcolipin (SLN)

## Overview

Sarcolipin (SLN) is a small (~30 amino acid) membrane protein that regulates the sarcoplasmic reticulum Ca2+-ATPase (SERCA) by binding to it and lowering its apparent Ca2+ affinity. SLN is primarily expressed in skeletal muscle in humans and is involved in non-shivering thermogenesis. It traps SERCA in an E1 intermediate state with exposed Ca2+ binding sites, preventing productive Ca2+ transport. SLN and [PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) ([PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/)) are homologous regulators that bind SERCA in a similar fashion.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11900 | 4K5T | 3.1 A | P21212 | Rabbit SLN (30 residues) in complex with rabbit [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) | Mg2+, [AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/), [PEG6000](/xray-mp-wiki/reagents/additives/peg6000/), [MPD](/xray-mp-wiki/reagents/additives/mpd/), [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |

## Expression and Purification

- **Expression system**: Rabbit (Oryctolagus cuniculus) skeletal muscle, native extraction
- **Construct**: Native SLN co-purified with [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) from rabbit sarcoplasmic reticulum

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane isolation | Isolation of sarcoplasmic reticulum vesicles from rabbit skeletal muscle | -- | 100 mM MOPS-Tris pH 6.8, 80 mM KCl | Membranes extracted and purified with low concentration of [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/) |
| Solubilization | Solubilization with octaethylene glycol dodecylether ([C12E8](/xray-mp-wiki/reagents/detergents/c12e8/)) | -- | 100 mM MOPS-KOH pH 6.8, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 80 mM KCl, 3 mM MgCl2, 3.9 mM [EGTA](/xray-mp-wiki/reagents/additives/egta/), 1% DMSO + [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) (octaethylene glycol dodecylether) at 35 mM | SERCA and SLN solubilized together for 10 min; [AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/) added at 1 mM |
| Centrifugation | Ultracentrifugation to remove insoluble material | -- | Same as solubilization buffer | 50,000g for 35 min at 4 C; protein concentration of final supernatant was 12 mg/ml |


## Crystallization

### doi/10.1038##nature11900

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | SERCA1a-SLN complex at 12 mg/ml with 1 mM [AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/) in [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) |
| Reservoir | 19.5% [PEG6000](/xray-mp-wiki/reagents/additives/peg6000/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 150 mM MgSO4, 6% [MPD](/xray-mp-wiki/reagents/additives/mpd/) |
| Mixing ratio | 1:1 |
| Temperature | 23 C |
| Growth time | Single crystals appeared after a few days, grew within 1 week to 250 x 250 x 50 um |
| Cryoprotection | 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 19.5% [PEG6000](/xray-mp-wiki/reagents/additives/peg6000/), 150 mM MgSO4, 6% [MPD](/xray-mp-wiki/reagents/additives/mpd/) |
| Notes | Crystals belong to space group P21212 with unit cell parameters a=71.7, b=74.8, c=125.9 A. Resolution 3.1 A. R factor 19.1%, R free 24.6%. Phases determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using individual domains of SERCA (PDB 2AGV and 3N5K) as search models. SLN was traced as a polyalanine model; Phe 12 served as hallmark residue for sequence assignment.
 |


## Biological / Functional Insights

### SLN traps SERCA in a unique E1 intermediate state

The SLN-bound SERCA structure reveals a previously undescribed E1 intermediate state (E1-SLN) with exposed Ca2+ binding sites through an open cytoplasmic pathway stabilized by Mg2+. The regulatory SLN helix binds in a groove between transmembrane helices M2, M6, and M9 of SERCA. This state allows cytoplasmic ion exchange in transition from the proton-occluded [Hn]E2 to the calcium-occluded [Ca2]E1P state.

### SLN binding groove is compatible with E2 state but not E1P state

Superposition of SLN on the [Hn]E2 state of SERCA reveals a wider SLN-binding groove compatible with extensive contact to M4, including a close contact to SERCA Leu 321 which when mutated reduces both SLN and [PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) binding. In contrast, the occluded [Ca2]E1P conformation has M1, M2, M3, and M4 moved, narrowing the SLN-binding site. Residues Leu 96, Trp 107, and Glu 108 constrict the groove for the N-terminal region of SLN, suggesting SLN is either dislodged or undergoes positional rearrangement during the shift to [Ca2]E1P conformation.

### Phosphorylation of SLN at Thr 5 abolishes inhibition

SLN is phosphorylated by CaMKII at Thr 5, and a phosphorylation mimic (Thr5Glu mutation) abolishes the inhibitory function of SLN in adult rat ventricular myocytes. Thr 5 interacts with SERCA Trp 932, and phosphorylation at this site would cause a steric clash that destabilizes SLN binding to SERCA.

### PLB mutations segregate on opposite sides of the helix

Plotting gain-of-function and loss-of-function mutations of [PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) onto the SLN structure, the mutations clearly segregate on opposite sides of the helix: loss-of-function mutations at the SERCA interface, and gain-of-function mutations (presumably impaired [PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) pentamerization leading to more active monomer) on the outside. This supports the notion that SERCA can interact with [PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) pentamers, as the pentamerization-interface residues and SERCA-binding residues are on opposite sides.

### SLN exists in monomeric and multimeric forms

Both SLN and [PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) have been proposed to exist in biological membranes in monomeric and multimeric free forms and as monomers and dimers in SERCA-bound forms. The pentamer interface of [PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) is on the outside of the helix, opposite the SERCA-binding interface, allowing simultaneous formation of both PLB-[PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) and SERCA-[PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) interactions.


## Cross-References

- [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase 1a)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) — Primary target of SLN regulation; SLN co-crystallized with SERCA1a
- [Phospholamban (PLB)](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) — Homologous regulator of SERCA; similar binding mechanism
- [AMPPCP (Adenosine 5'-[beta,gamma-methylene]triphosphate)](/xray-mp-wiki/reagents/ligands/amppcp/) — Non-hydrolyzable ATP analog used in crystallization
- [Octaethylene Glycol Dodecylether (C12E8)](/xray-mp-wiki/reagents/detergents/c12e8/) — Detergent used for SERCA-SLN solubilization
- [Magnesium Sulfate (MgSO4)](/xray-mp-wiki/reagents/additives/magnesium-sulfate/) — Source of Mg2+ ions in crystallization at 150 mM
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/) — Additive used in purification or crystallization buffers
- [EGTA](/xray-mp-wiki/reagents/additives/egta/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [MPD](/xray-mp-wiki/reagents/additives/mpd/) — Additive used in purification or crystallization buffers
