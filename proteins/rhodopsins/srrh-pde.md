---
title: "Rhodopsin Phosphodiesterase (Rh-PDE) from Salpingoeca rosetta"
created: 2026-06-22
updated: 2026-06-22
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-19376-7]
verified: false
---

# Rhodopsin Phosphodiesterase (Rh-PDE) from Salpingoeca rosetta

## Overview

Rhodopsin phosphodiesterase (Rh-PDE) is an enzyme rhodopsin from the
choanoflagellate Salpingoeca rosetta (SrRh-PDE). It consists of an
N-terminal rhodopsin domain and a C-terminal phosphodiesterase (PDE)
domain connected by a 76-residue linker. Rh-PDE hydrolyzes both cAMP
and cGMP in a light-dependent manner, with ~2-fold light-induced
activation. The crystal structure revealed a new 8-TM rhodopsin
topology, including an N-terminal extra transmembrane helix TM0.
Rh-PDE has potential for optogenetic manipulation of cyclic nucleotide
concentrations.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-020-19376-7 | 7CJ3 | 2.6 | — | SrRh-PDE TMD (residues 33-316), C-terminal GFP-His6, TEV cleaved |  |
| doi/10.1038##s41467-020-19376-7 | 7CJ3 | 3.5 | — | SrRh-PDE TMD-Linker (residues 33-378), C-terminal GFP-His6, TEV cleaved |  |
| doi/10.1038##s41467-020-19376-7 | 7CJ3 | 2.1 | — | SrRh-PDE Linker-PDE domain, C-terminal His8, TEV cleaved |  |

## Expression and Purification

- **Expression system**: HEK293S GnTI- cells (TMD/TMD-Linker); Rosetta2 (DE3) E. coli (PDE domain)
- **Construct**: SrRh-PDE TMD (aa 33-316) and TMD-Linker (aa 33-378) in pEG BacMam vector with C-terminal GFP-His6 tag and TEV cleavage site; PDE domain in modified pEG-CGFP-BC vector with C-terminal His8 tag and TEV cleavage site
- **Induction**: 0.2 µg/mL anhydrotetracycline (E. coli); BacMam transduction (HEK)
- **Media**: DMEM with FBS and penicillin-streptomycin (HEK)

### Purification Workflow

- **Expression system**: HEK293S GnTI-
- **Expression construct**: SrRh-PDE TMD (aa 33-316) or TMD-Linker (aa 33-378) with C-terminal GFP-His6, TEV cleaved
- **Tag info**: GFP-His6, removed by TEV cleavage

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Sonication | — | 20 mM Tris pH 8.0, 200 mM NaCl, 20% glycerol, 100 µM all-trans retinal | Supplemented with 100 µM all-trans retinal (Sigma) |
| Membrane isolation | Ultracentrifugation | — | 20 mM Tris pH 8.0, 200 mM NaCl, 20% glycerol | 185,500×g, 1 h, 4°C |
| Solubilization | Detergent extraction | — | 20 mM Tris pH 8.0, 200 mM NaCl, 10 mM MgCl2, 20% glycerol + 1% DDM, 0.2% CHS | 1 h at 4°C |
| Affinity chromatography | TALON metal affinity | TALON Metal Affinity Resin (Clontech) | 20 mM Tris pH 8.0, 500 mM NaCl, 10 mM MgCl2, 15 mM imidazole, 10% glycerol + 0.1% LMNG, 0.01% CHS | 30 min incubation at 4°C |
| TEV cleavage | Protease digestion | — |  | TEV protease treatment to remove GFP-His6 tag |
| Reverse affinity | TALON (flow-through) | — |  | Remove TEV protease and cleaved tag |
| Size-exclusion chromatography | SEC | Superdex 200 Increase column | 20 mM Tris pH 8.0, 150 mM NaCl + 0.1% LMNG, 0.01% CHS |  |

**Final sample**: ~10 mg/mL in SEC buffer

- **Expression system**: Rosetta2 (DE3) E. coli
- **Expression construct**: SrRh-PDE PDE domain with C-terminal His8, TEV cleaved
- **Tag info**: His8, removed by TEV cleavage

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Sonication | — | 50 mM Tris pH 8.0, 100 mM NaCl, 10 mM MgCl2, 20 mM imidazole |  |
| Affinity chromatography | Ni-NTA | Ni-NTA resin (Qiagen) | 50 mM Tris pH 8.0, 100 mM NaCl, 10 mM MgCl2, 200 mM imidazole (elution) | Wash with buffer A, elute with 200 mM imidazole |
| TEV cleavage and dialysis | Protease digestion + dialysis | — | 50 mM Tris pH 8.0, 100 mM NaCl, 10 mM MgCl2 | TEV protease treatment, then dialyzed |
| Reverse affinity | Ni-NTA (flow-through) | — |  | Remove TEV protease and His8 tag |
| Size-exclusion chromatography | SEC | HiLoad 16/600 Superdex 200 pg (GE Healthcare) | 50 mM Tris pH 8.0, 100 mM NaCl, 10 mM MgCl2 |  |

**Final sample**: 10 mg/mL for crystallization


## Crystallization

### doi/10.1038##s41467-020-19376-7

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | SrRh-PDE TMD or TMD-Linker in SEC buffer |
| Lipid | Monoolein |
| Temperature | 20 |
| Growth time | Overnight |
| Notes | Crystals obtained for TMD (2.6 Å) and TMD-Linker (3.5 Å) |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | SrRh-PDE Linker-PDE, 10 mg/mL in 50 mM Tris pH 8.0, 100 mM NaCl, 10 mM MgCl2 |
| Reservoir | 29% (v/v) PEG400, 50 mM calcium acetate pH 5.0, 200 mM NaCl |
| Temperature | 4 |
| Growth time | 1 week |
| Cryoprotection | 15% ethylene glycol |
| Notes | Crystals grown in dark; data collected at SPring-8 BL32XU |


## Biological / Functional Insights

### 8-TM Rhodopsin Topology

The crystal structure revealed a new 8-TM topology for rhodopsins,
including an N-terminal extra transmembrane helix (TM0, residues
50-73) located between TM2 and TM3. TM0 interacts with TM2 and TM3
through hydrophobic interactions and a hydrogen bond between Trp63
and Ser136. TM0 stabilizes the overall folding of the TMD and
facilitates interactions with the retinal chromophore, playing a
crucial role in enzymatic photoactivity. Truncation of TM0 (Δ76)
abolished rhodopsin-related absorption.

### Photoactivation Mechanism

The retinal isomerization displaces TM7, followed by movement of
the linker region, inducing conformational change in the PDE
domain. Bulky hydrophobic residues between TM7 and the retinal
chromophore (Leu299, Met303) are critical for photoactivity.
Mutations of Met301 and Val304 at the dimer interface reduce
dimer stability and photoactivity. The intracellular loop ICL3
contains a Pro-rich PPPPLP sequence forming a right-handed helical
loop that limits TM7 movement. Unlike BR, Rh-PDE lacks pump or
channel activity due to replacement of key proton-transfer
residues (Asp96 replaced by Trp175) and protonated Glu164.

### Full-Length Model and Dimer Architecture

Combining the three crystal structures (TMD, TMD-Linker,
Linker-PDE) with HS-AFM observations and computational modeling,
a full-length model was proposed. The linker region forms a
dimeric, four-helical coiled-coil resembling a HAMP domain. The
TMD and PDE domains do not form direct interactions. Rh-PDE forms
a dimer under physiological conditions.


## Cross-References

- [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) — Rh-PDE belongs to the microbial rhodopsin family with a unique 8-TM topology
- [Enzyme Rhodopsins](/xray-mp-wiki/concepts/enzyme-mechanisms/enzyme-rhodopsins/) — Rh-PDE is a member of the enzyme rhodopsin class, with light-dependent enzymatic activity
- [DDM (n-Dodecyl-β-D-Maltopyranoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Used for membrane protein extraction and solubilization of Rh-PDE
- [LMNG (2,2-Didecylpropane-1,3-bis-β-D-maltopyranoside)](/xray-mp-wiki/reagents/detergents/lmng/) — Used during purification of Rh-PDE after solubilization
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Used as additive during solubilization and purification to stabilize Rh-PDE
- [All-trans Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore bound to Rh-PDE via Schiff base; essential for photoactivity
