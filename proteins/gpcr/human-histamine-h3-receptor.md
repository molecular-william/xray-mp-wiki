---
title: Human Histamine H3 Receptor (H3R)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-022-33880-y]
verified: false
---

# Human Histamine H3 Receptor (H3R)

## Overview

The human histamine H3 receptor (H3R) is a [G Protein](/xray-mp-wiki/concepts/signaling-receptors/g-protein/)-coupled receptor ([GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/)) belonging to the aminergic [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) subfamily. It is expressed mainly in the central nervous system, where it acts as an auto- or hetero-receptor to regulate histamine release and modulate the release of various neurotransmitters including [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/), GABA, and [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/). H3R is associated with physiological processes such as sleep-wake cycles, learning, memory, feeding, and cerebral ischemia, making it a potential drug target for neurological and psychiatric disorders including sleep disorders, Parkinson's disease, schizophrenia, and Alzheimer's disease. The crystal structure of H3R in complex with the non-[Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) antagonist PF-03654746 reveals the molecular basis for ligand recognition and allosteric [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-022-33880-y | not specified | 2.6 | not specified | Human H3R (residues 27-432), with N-terminal truncation (1-26), ICL3 truncation (242-346), C-terminal truncation (433-445), S121K mutation, and N-terminal BRIL fusion (M7W, H102I, R106L) | PF-03654746 |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda ([Sf9](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)) insect cells
- **Construct**: Codon-optimized human H3R gene cloned into modified pFastBacI vector with N-terminal HA signal sequence, FLAG tag, 10x His tag, and TEV protease cleavage site
- **Notes**: [Bac-to-Bac](/xray-mp-wiki/methods/expression-systems/bac-to-bac/) [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) Expression System; infected at 2-3 x 10^6 cells/ml, harvested 48h post-infection

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane fractionation | not specified | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 10 mM [MgCl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl (hypotonic); 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 1.0 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10 mM [MgCl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl (high-osmotic) + not specified | Cells washed with hypotonic buffer then high-osmotic buffer; purified membranes resuspended with 2 mg/mL [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) |
| Solubilization | Detergent solubilization | not specified | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 800 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Solubilized for 3h at 4 C; centrifuged at 58,000xg for 1h |
| [IMAC](/xray-mp-wiki/methods/purification/affinity-chromatography/) purification | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) [IMAC](/xray-mp-wiki/methods/purification/affinity-chromatography/) resin (TaKaRa) | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 800 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash I); 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 500 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash II); 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 500 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) + [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Incubated overnight at 4 C; eluted in 3 column volumes |


## Crystallization

### doi/10.1038##s41467-022-33880-y

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) |
| Protein sample | H3R-PF-03654746 complex in 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |
| Temperature | not specified |
| Notes | Crystals formed within 1 week; collected with 50 um micro-loops and flash-frozen in liquid nitrogen |


## Biological / Functional Insights

### Extended binding pocket (EBP) in H3R

The H3R structure reveals an extended binding pocket (EBP) around TMs2/7 and ECL2 compared to other aminergic receptors. This EBP accommodates the aromatic moieties of H3R antagonists through pi-pi stacking and OH/pi hydrogen bonds with aromatic residues including Y91 and Y189. Functional assays showed Y91A and Y189A mutations significantly decreased inhibition of several antagonists, confirming the EBP's importance for ligand binding and efficacy.

### Allosteric cholesterol binding

A [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) molecule was observed binding at the extrahelical pocket between TM1 and TM7 of H3R, forming extensive hydrophobic interactions with F29, L37, M41, L40, L44, T396, Y393, and W399. The beta-3-hydroxy head group of [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) forms a hydrogen bond with E395, which also participates in polar interactions with PF-03654746. Molecular dynamics simulations showed [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) stabilizes the TM1-TM7-N-term contacts, potentially affecting antagonist binding through an allosteric mechanism.

### Inactive state conformation

Compared to inactive H1R, H3R shows inward movement of TM6 and TM7 extracellular tips by 2.3 and 3.5 A, respectively, and an outward movement of TM6 by 2.8 A at the intracellular side (vs 12 A in active H1R). The D131-R132 salt bridge (instead of D-R-Y motif) is a key feature of the inactive state. ECL2 shifts 11 A toward TM3, creating space for the antagonist.


## Cross-References

- [G Protein](/xray-mp-wiki/concepts/signaling-receptors/g-protein/) — Related entity
- [Gpcr](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) — Related entity
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Related entity
- [Bac To Bac](/xray-mp-wiki/methods/expression-systems/bac-to-bac/) — Related entity
- [Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Related entity
- [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Related entity
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Related entity
- [Immobilized Metal Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Related entity
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Related entity
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Related entity
