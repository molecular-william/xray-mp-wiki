---
title: Human Neurokinin 1 Receptor (NK1R)
created: 2026-06-08
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-018-07939-8, doi/10.1073##pnas.1812717115]
verified: false
---

# Human Neurokinin 1 Receptor (NK1R)

## Overview

The human neurokinin 1 receptor (NK1R, TACR1) is a class A G protein-coupled receptor that binds the neuropeptide Substance P (SP) as its preferred endogenous agonist. NK1R is expressed in the central and peripheral nervous system, smooth muscle, endothelial cells, and immune cells. It is implicated in nausea, analgesia, inflammation, pruritus, and depression, making it a key therapeutic target for chemotherapy-induced nausea and vomiting (CINV). The receptor was crystallized as a thermostabilized NK1R-PGS fusion construct (with Pyrococcus abyssi glycogen synthase replacing intracellular loop 3), and high-resolution structures were determined in complex with the antagonists CP-99,994 (3.27 A), [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/) (2.40 A), [Netupitant](/xray-mp-wiki/reagents/ligands/netupitant/) (2.20 A), and L760735 (3.4 A).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-018-07939-8 | 6HLL | 3.27 A | C2221 | Human NK1R-PGS fusion: Pyrococcus abyssi glycogen synthase (PGS) replacing ICL3; expressed in Sf9 insect cells via baculovirus
 | CP-99,994 |
| doi/10.1038##s41467-018-07939-8 | 6HLO | 2.40 A | P212121 | Human NK1R-PGS fusion: Pyrococcus abyssi glycogen synthase (PGS) replacing ICL3; expressed in Sf9 insect cells via baculovirus
 | [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/) |
| doi/10.1038##s41467-018-07939-8 | 6HLP | 2.20 A | P212121 | Human NK1R-PGS fusion: Pyrococcus abyssi glycogen synthase (PGS) replacing ICL3; expressed in Sf9 insect cells via baculovirus
 | [Netupitant](/xray-mp-wiki/reagents/ligands/netupitant/) |
| doi/10.1073##pnas.1812717115 | not specified | 3.4 A | not specified | Human NK1R-PGS fusion: Pyrococcus abyssi glycogen synthase (PGS) replacing ICL3; expressed in Sf9 insect cells via baculovirus
 | L760735 |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: Human NK1R with [PGS (Pyrococcus abyssi Glycogen Synthase) Fusion](/xray-mp-wiki/reagents/protein-tags/pgs-fusion/) replacing ICL3; N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) and His10 tag; 3C protease cleavage site for tag removal

- **Notes**: Receptor expressed in Sf9 insect cells using baculovirus system. Thermostabilized construct based on directed evolution studies (Schutz et al. 2016).


### Purification Workflow

*Source: doi/10.1038##s41467-018-07939-8*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Homogenization and ultracentrifugation | — | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + None | Sf9 cell pellet resuspended and membranes collected |
| Solubilization | Detergent extraction | — | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% (w/v) [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Membranes solubilized for 1 h at 4 C with [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/CHS |
| Ni-NTA affinity | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA resin | 50 mM HEPES pH 7.5, 500 mM NaCl, 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/)
 + 0.05% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.01% (w/v) [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | His-tagged receptor bound to Ni-NTA resin, eluted with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Buffer exchange and tag cleavage | Desalting (PD MiniTrap G-25) | — | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.03% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.006% (w/v) [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) removed; His-tagged 3C protease and PNGaseF added for 6 h at 4 C |
| Reverse Ni-NTA | Flow-through collection | Ni-NTA resin | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% (w/v) [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)
 + 0.03% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.006% (w/v) [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Cleaved receptor collected as flow-through; uncleaved and 3C protease bind resin |
| Concentration | Vivaspin 2 concentrator (100 kDa MWCO) | — | as above + as above | Concentrated to ~50-60 mg/ml for crystallization |

### Purification Workflow

*Source: doi/10.1073##pnas.1812717115*

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: Human NK1R-PGS fusion with N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) and His10 tag
- **Tag info**: N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) + His10 tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Homogenization and ultracentrifugation | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Sf9 cell pellet homogenized |
| Solubilization | Detergent extraction | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 500 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% Na Cholate, 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mg/mL [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/), 5 uM L760735 + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.2% Na Cholate, 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Solubilization for 1 h at 4 C, ultracentrifugation at 100,000 x g |
| Ni-NTA batch binding | Batch binding with Ni-NTA agarose | Ni-NTA agarose | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 500 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% Na Cholate, 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 5 uM L760735 | 20 GE [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) added before binding, batch mode for 4 h at 4 C |
| Ni-NTA elution | Column elution | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 500 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% Na Cholate, 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 5 uM L760735 | Eluted with 5 volumes of elution buffer |
| M1 anti-FLAG affinity | M1 FLAG [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) with detergent exchange | M1 anti-FLAG agarose | 200 ug/mL FLAG peptide, 5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) + Detergent exchanged from [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/Na Cholate/CHS to 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) on M1 beads | 2 mM CaCl2 added before loading; eluted with FLAG peptide + [EDTA](/xray-mp-wiki/reagents/additives/edta/) |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) |  | Single monomeric peak collected, purity checked by SDS/PAGE |


## Crystallization

### doi/10.1038##s41467-018-07939-8

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | ~50-60 mg/ml NK1R-PGS in 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) + 10% (w/v) [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) |
| Temperature | 20 C |
| Notes | CP-99,994 complex crystals appeared in <1 h in broad conditions. [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/) complex: 100 mM sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 6.0, 31% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 50-70 mM MgCl2, 50 uM [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/). [Netupitant](/xray-mp-wiki/reagents/ligands/netupitant/) complex: 100 mM sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 6.0, 31% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 40-50 mM Mg(HCO3)2, 50 uM [Netupitant](/xray-mp-wiki/reagents/ligands/netupitant/). All crystals cryo-cooled in liquid nitrogen without additional cryoprotectant.
 |

### doi/10.1073##pnas.1812717115

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | 30-50 mg/ml NK1R-PGS |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) + 10% (w/w) [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) (2:3 protein:lipid mass ratio) |
| Temperature | 20 C |
| Notes | Crystals observed in 1 day, full size in 1 week. Cryoprotected in crystallization mother liquid. Data from 36 merged crystals. Diffraction data collected at APS 23ID-D beamline (12 keV, Pilatus3 6M detector). Resolution limit 3.4 A. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with Phaser.
 |


## Biological / Functional Insights

### Antagonist binding modes reveal induced-fit mechanism

The three structures reveal distinct binding poses for the progenitor
antagonist CP-99,994 and the clinically approved antagonists [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/)
and [Netupitant](/xray-mp-wiki/reagents/ligands/netupitant/). CP-99,994 binds with its core (piperidine ring) between
F268(6.55) and Q165(4.60), with two arms targeting distinct lipophilic
subpockets. [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/), with an additional arm 3 (triazolinone) substituent,
creates an extended binding pocket ([EBP](/xray-mp-wiki/proteins/enzymes/human-ebp/)) at the interface of helices IV,
V and ECL2, inducing an induced-fit conformational change. [Netupitant](/xray-mp-wiki/reagents/ligands/netupitant/),
with its distinct chemical scaffold (substituted pyridine core), binds in
a more upright position with its arm 3 targeting a hydrophobic groove
between F268(6.55), P271(6.58) and Y272(6.59) at the extracellular tip
of helix VI.

### Histidine lock — interhelical H-bond network for insurmountable antagonism

Both [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/) and [Netupitant](/xray-mp-wiki/reagents/ligands/netupitant/) induce a distinct receptor conformation
characterized by a reorientation of H197(5.39) and Y272(6.59), forming
an extended interhelical hydrogen bond network that cross-links the
extracellular ends of helices V and VI. The network involves residues
Y272(6.59), H197(5.39), T201(5.43) and H265(6.52). This "histidine lock"
reduces conformational flexibility and provides a structural rationale
for the insurmountable antagonism observed for these clinically approved
antagonists. CP-99,994 does not induce this network.

### E78(2.50) replaces sodium ion for lack of basal activity

NK1R has a glutamate (E78) at position 2.50 instead of the more common
aspartate found in most class A GPCRs. This larger glutamate side chain
forms a direct bidentate interaction with the amide group of N301(7.49)
and hydrogen bonds to S119(3.39), replacing the structural role of the
allosteric sodium ion observed in other inactive class A GPCRs. This
tighter helical bundle cross-linking provides a structural basis for
the observed lack of basal signaling in NK1R.

### L760735 antagonist binding and MD simulation analysis

The 3.4 A crystal structure of hNK1R bound to L760735 (a close [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/)
analog with amine-substituted triazole instead of 3-oxo-substituted triazole)
reveals a three-layered antagonist architecture spanning 14 A in a narrow
orthosteric pocket. The fluorophenyl and 3,5-trifluoromethyl-benzylether
moieties form an intramolecular pi-pi stacking interaction. Glide docking
and MD simulations in explicit lipid bilayers show that L760735 and
[Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/) prefer to bind in their neutral forms, with the neutral form
adopting a conformation more consistent with the crystal structure.
W261(6.48) at the pocket base contributes to ligand stability. The
antagonist does not make strong contacts with TM2 and TM7, allowing
binding without orthosteric pocket contraction.


## Cross-References

- [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/) — L760735 is a close analog of the clinically approved drug aprepitant
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent exchanged on M1 anti-FLAG beads during purification
- [Tachykinin Receptor Family](/xray-mp-wiki/concepts/tachykinin-receptor-family/) — NK1R is the founding member of the tachykinin receptor family
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [EBP](/xray-mp-wiki/proteins/enzymes/human-ebp/) — Related protein structure
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
