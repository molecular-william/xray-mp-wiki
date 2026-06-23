---
title: "Human Neuropeptide Y Y1 Receptor (Y1R, NPY1R)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-018-0046-x]
verified: false
---

# Human Neuropeptide Y Y1 Receptor (Y1R, NPY1R)

## Overview

The neuropeptide Y (NPY) Y1 receptor (Y1R, NPY1R) is a class A
G-protein-coupled receptor that mediates the effects of NPY, the most
powerful stimulant of food intake. Y1R is widely expressed in the central
nervous system and peripheral tissues, and is involved in the regulation of
food intake, anxiety, cancer biology, and bone metabolism. Crystal structures
of the human Y1R bound to two selective antagonists - UR-MK299 (argininamide)
at 2.7 A resolution and BMS-193885 (urea-based) at 3.0 A resolution - reveal
the structural basis of antagonist binding and ligand selectivity at NPY
receptors. The structures combined with mutagenesis, NMR, photo-crosslinking,
and functional studies provide insights into the binding mode of the
endogenous agonist NPY and demonstrate how the C-terminal pentapeptide of NPY
penetrates the binding pocket while the N terminus contacts the second
extracellular loop (ECL2). These findings enable structure-based drug
discovery targeting NPY receptors for the treatment of obesity, cancer, and
bone disorders.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-018-0046-x | 5ZBQ | 2.7 | P21 | Human Y1R with [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion inserted at ICL3 between R241 and D250, F129(3.41)W mutation, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (V359-I384), N-terminal HA signal sequence, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), C-terminal PreScission site and 10xHis tag | UR-MK299 (argininamide-type antagonist) |
| doi/10.1038##s41586-018-0046-x | 5ZBH | 3.0 | C2221 | Human Y1R with [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion at ICL3, F129(3.41)W mutation, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), N-terminal HA signal sequence, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), C-terminal 10xHis tag | BMS-193885 (urea-based antagonist) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) cells, Bac-to-Bac baculovirus system
- **Construct**: Engineered human Y1R with N-terminal HA signal sequence, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/); [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion at ICL3 (between R241 and D250); F129(3.41)W mutation; C-terminal PreScission site and 10xHis tag; C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) after H384 (TCap). Ligand (UR-MK299 or BMS-193885) added at 1 uM.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Dounce homogenization and ultracentrifugation | -- | Hypotonic buffer (10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitor cocktail); High-osmotic buffer (10 mM HEPES pH 7.5, 1 M NaCl, 10 mM MgCl2, 20 mM KCl) + -- | Membranes washed 2-3 times with high-osmotic buffer, then hypotonic buffer. Final membranes resuspended in hypotonic buffer + 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), stored at -80 C. |
| Solubilization | Detergent solubilization | -- | 50 mM HEPES pH 7.5, 500 mM NaCl, 0.5% w/v [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.5% w/v [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Incubated at 4 C for 3 h with 100 uM ligand, 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/), and protease inhibitor cocktail |
| Affinity purification | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) resin | Wash buffer (25 mM HEPES pH 7.5, 500 mM NaCl, 0.05% w/v [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 50 uM ligand) + 0.05% w/v [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Resin incubated with solubilized material overnight at 4 C with 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/). Washed with 10 column volumes of wash buffer. |
| Elution | IMAC elution | [TALON](/xray-mp-wiki/reagents/additives/talon/) resin | 25 mM HEPES pH 7.5, 500 mM NaCl, 0.05% w/v [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 50 uM ligand + 0.05% w/v [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Eluted Y1R-ligand complex concentrated and used directly for crystallization trials. |


## Crystallization

### doi/10.1038##s41586-018-0046-x

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified Y1R-ligand complex in 25 mM HEPES pH 7.5, 500 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 50 uM ligand |
| Reservoir | -- |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | UR-MK299 complex (5ZBQ, 2.7 A) crystallized in space group P21 with unit cell 37.8, 100.7, 83.2 A, beta=98.8 deg. BMS-193885 complex (5ZBH, 3.0 A) crystallized in space group C2221 with unit cell 76.9, 126.8, 170.3 A. Data from 47 crystals (UR-MK299) and 33 crystals (BMS-193885) merged for completeness. Protein residues 3-361 modeled; [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) residues 2-161 visible. Ramachandran: 97.56% allowed, 2.44% preferred (5ZBQ); 97.54% allowed, 2.46% preferred (5ZBH). |


## Biological / Functional Insights

### Antagonist binding modes at Y1R

UR-MK299 binds in a pocket formed by helices III, V, VI, and VII, ECL2,
and ECL3. The argininamide group of UR-MK299 forms a bidentate salt bridge
with Asp287(6.59) and hydrogen bonds with Asn283(6.55) and Gln219(5.46).
The diphenylmethyl group of UR-MK299 makes extensive hydrophobic contacts
with Phe282(6.54), Phe286(6.58), and Phe302(7.35). The hydroxyphenyl group
contacts Gln120(3.32), Cys121(3.33), Ile124(3.36), Trp276(6.48), and
Leu279(6.51). Trp276(6.48) (the 'toggle switch') adopts an inactive-state
conformation, stabilized by the antagonist. BMS-193885 binds similarly but
uses a [UREA](/xray-mp-wiki/reagents/substrates/urea/) group for hydrogen bonding with Asp287(6.59) rather than a
guanidine group. The piperidine and methoxyphenyl rings of BMS-193885 form
hydrophobic contacts with Phe282, Phe286, and Phe302.

### Structural basis of ligand selectivity among NPY receptors

Ligand selectivity between Y1R and Y2R is determined by differences in the
ECL2 region and the binding pocket. Phe173(4.60) and Ile124(3.36) in Y1R
create a deeper, more hydrophobic pocket compared to Y2R. The residues at
positions 6.55 (Asn283 in Y1R vs His in Y2R) and 6.59 (Asp287 in Y1R vs
Glu in Y2R) contribute to differential ligand recognition. The
F129(3.41)W mutation introduced for crystallogenesis did not affect ligand
selectivity patterns.

### NPY agonist binding model

The NPY agonist binds Y1R with its C-terminal pentapeptide (residues 32-36)
penetrating the binding pocket. R35 of NPY mimics the guanidine group of
UR-MK299 by interacting with Asp287(6.59). Y36 of NPY points toward
Gln120(3.32) on helix III, forming a hydrogen bond, in contrast to the
hydroxyphenyl group of UR-MK299 which orients toward helix V. The
unstructured N terminus (Y1-P13) of NPY contacts ECL2 of Y1R, as
confirmed by photo-crosslinking experiments. The middle alpha-helix of NPY
is positioned above the receptor. Solid-state NMR chemical shift
measurements revealed residue-specific secondary structure changes in NPY
upon binding.

### Y1R-T4L fusion construct design

To facilitate structure determination, an engineered Y1R construct was
designed with [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) inserted at the third intracellular loop (ICL3) between
R241 and D250, the F129(3.41)W mutation for improved expression and
stability, and a 25-residue C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (V359-I384). The
T4L-fusion strategy at ICL3 has been validated across multiple class A
GPCR structures and was effective here for enabling diffraction-quality
crystals of both Y1R-antagonist complexes.


## Cross-References

- [Neurotensin Receptor 1 (NTS1)](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/) — Class A GPCR of the same beta-branch; comparison of ligand binding modes
- [Orexin 1 Receptor (OX1)](/xray-mp-wiki/proteins/enzymes/orexin-1-receptor/) — Class A GPCR of the same beta-branch; comparison of ligand binding modes
- [Orexin 2 Receptor (OX2)](/xray-mp-wiki/proteins/gpcr/orexin-2-receptor/) — Class A GPCR of the same beta-branch; comparison of ligand binding modes
- [GPCR Inactive Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-inactive-conformation/) — Y1R-UR-MK299 structure reveals antagonist-stabilized inactive state with Trp276(6.48) toggle switch in inactive conformation
- [GPCR G-protein Coupling](/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-coupling/) — Y1R is a Gi/Go-coupled receptor; agonist NPY activates through G-protein signaling cascade
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Y1R expressed in Sf9 cells using Bac-to-Bac baculovirus system
- [n-Dodecyl-beta-D-Maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for Y1R purification and crystallization
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — CHS used as additive during Y1R purification at 0.1% w/v
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Human NPY Y2 Receptor (Y2R, NPY2R)](/xray-mp-wiki/proteins/gpcr/human-y2-receptor-npy2r/) — Related NPY receptor subtype; comparison of antagonist-bound structures reveals ligand selectivity determinants
