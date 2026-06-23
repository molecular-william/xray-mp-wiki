---
title: "Human TASK-1 (K2P 3.1) Potassium Channel"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-020-2250-8]
verified: false
---

# Human TASK-1 (K2P 3.1) Potassium Channel

## Overview

TWIK-related acid-sensitive potassium (TASK) channels (K2P 3.1/KCNK3) are
members of the two-pore domain potassium (K2P) channel family, found in
neurons, cardiomyocytes, and vascular smooth muscle cells, where they regulate
the resting membrane potential and are involved in heart rate, pulmonary artery
tone, sleep/wake cycles, and responses to volatile anaesthetics. Unlike other
K2P channels, TASK channels bind inhibitors with high affinity, exceptional
selectivity, and very slow washout rates, making them attractive drug targets
for obstructive sleep apnoea and atrial fibrillation. The X-ray crystal
structure of human TASK-1 (construct Met1-Glu259) was determined at 3.0 A
resolution, revealing a domain-swapped homodimer with a pseudo-tetrameric
selectivity filter, four transmembrane helices (M1-M4), and an extracellular
cap. Notably, TASK-1 contains a novel lower gate termed the 'X-gate', formed by
the crossed C-terminal M4 transmembrane helices at the vestibule entrance. This
structure is created by six residues (243VLRFMT248) that are essential for
responses to volatile anaesthetics, neurotransmitters, and GPCRs. Structures
of TASK-1 bound to two high-affinity inhibitors (BAY1000493 and BAY2341237)
show both compounds bind below the selectivity filter and are trapped in the
vestibule by the X-gate, explaining their exceptionally low washout rates.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-020-2250-8 | 6RV2 | 3.0 | Not specified | Human TASK-1 Met1-Glu259 (C-terminally truncated), C-terminal TEV cleavage site, decahistidine and Flag tags | K+ ions at selectivity filter sites |
| doi/10.1038##s41586-020-2250-8 | 6RV3 | 3.0 | Not specified | Human TASK-1 Met1-Glu259 plus BAY1000493 (inhibitor) | BAY1000493 (4-[[2-(4-bromophenyl)imidazo[1,2-a]pyridin-3-yl]methyl]piperazin-1-yl)(2-fluorophenyl)methanone), K+ ions |
| doi/10.1038##s41586-020-2250-8 | 6RV4 | 3.0 | Not specified | Human TASK-1 Met1-Glu259 plus BAY2341237 (inhibitor) | BAY2341237 (4-[[2-(4-chlorophenyl)imidazo[1,2-a]pyridin-3-yl]methyl]piperazin-1-yl]6-(trifluoromethoxy)pyridin-2-yl]methanone), K+ ions |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) cells, Bac-to-Bac baculovirus system
- **Construct**: Human KCNK3 (GenBank ID 4504849), residues Met1-Glu259, subcloned in pFB-CT10HF-LIC with C-terminal TEV protease site, decahistidine and Flag tags

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex-C3/C5 high-pressure homogenizer | -- | 50 mM HEPES pH 7.5, 200 mM KCl, 5% v/v [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + -- | 40 ml breaking buffer per litre of culture |
| Solubilization | Detergent solubilization | -- | 50 mM HEPES pH 7.5, 200 mM KCl, 5% v/v [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% w/v [DM](/xray-mp-wiki/reagents/detergents/dm/) (DM), 0.1% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) Tris salt | Rotated at 4 C for 1 h |
| Affinity purification | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) resin (0.5 ml resin per litre culture) | Wash buffer (50 mM HEPES pH 7.5, 200 mM KCl, 5% v/v [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) pH 8.0, 0.24% w/v DM, 0.024% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)); Elution buffer (same + 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/)) + 0.24% w/v DM, 0.024% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | 30 column volumes wash; 5 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) added before loading |
| Tag cleavage and deglycosylation | TEV protease + PNGaseF digestion | -- | Desalting buffer (50 mM HEPES pH 7.5, 200 mM KCl, 5% v/v [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.24% w/v DM, 0.024% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)) + 0.24% w/v DM, 0.024% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | 1:3 w/w TEV protease, 1:10 w/w PNGaseF, 12-16 h at 4 C |
| Size-exclusion chromatography | SEC | Superose 6 Increase 10/300 GL | 20 mM HEPES pH 7.5, 200 mM KCl, 0.12% w/v DM, 0.012% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.12% w/v DM, 0.012% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Concentrated to 12-30 mg/ml with 50 kDa MWCO spin concentrator |


## Crystallization

### doi/10.1038##s41586-020-2250-8

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified TASK-1 at 8-12 mg/ml in gel filtration buffer |
| Reservoir | Not specified in raw paper |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Crystals flash-frozen in liquid nitrogen |
| Notes | Crystals obtained with CHOL-[PEG](/xray-mp-wiki/reagents/additives/peg/) mix and trigalactoside additives; data processed with STARANISO for anisotropic [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/). Three structures: apo TASK-1 (6RV2), TASK-1-BAY1000493 complex (6RV3, 50% occupancy in two orientations), and TASK-1-BAY2341237 complex (6RV4, 100% occupancy, single orientation). Ramachandran statistics: 97.56% allowed, 2.44% preferred (6RV3); 97.54% allowed, 2.46% preferred (6RV4). BAY1000493 was synthesized in-house; BAY2341237 was synthesized as described in ref 31. |


## Biological / Functional Insights

### Discovery of the X-gate in TASK channels

TASK-1 contains a novel lower gate (the 'X-gate') formed by the crossed
C-terminal M4 transmembrane helices. This is created by six residues
(243VLRFMT248) that adopt an extended two-turn-helical structure lacking
standard alpha/3-10 hydrogen bonding. The gate narrows the vestibule
entrance to only 0.8 A radius (measured by CHAP), compared to 7.5 A in
[KCNK10](/xray-mp-wiki/proteins/voltage-gated-channels/trek-2/) (PDB 4XDJ). TASK-3 and TASK-5 likely form similar X-gates based on
sequence conservation. This is the first example of a lower gate in K2P
channels, breaking the paradigm that K2P channels lack lower gates.

### X-gate mutations increase channel activity

Alanine scanning mutagenesis across the distal M4 helix (Thr230-Thr248)
showed that disruption of the X-gate increases the low basal activity of
TASK-1. Mutation of any X-gate residue except Val243 led to increased
currents without increased surface expression. Leu244Ala showed the largest
effect, with a sixfold increase in channel-open probability (from 0.7% to
4.0%) and increased open times. The X-gate is also essential for activation
by volatile anaesthetics (sevoflurane, halothane) - mutations in the X-gate
reduce anaesthetic activation.

### Latch region stabilizes the X-gate

A latch region involving Arg7 on the N terminus and Arg131 on the M2-M3
loop stabilizes the X-gate by electrostatic interactions with the distal
M4 region. Mutations to acidic residues (Arg7Asp, Arg131Asp) result in
5-10 fold increases in currents without increased surface expression,
confirming the latch's role in stabilizing the closed X-gate. X-gate
opening and pH sensing (via His98) appear not to be strictly coupled.

### High-affinity inhibitors are trapped by the X-gate

BAY1000493 and BAY2341237 bind to the closed TASK-1 conformation below
the selectivity filter without perturbing the X-gate structure. Both
compounds fit precisely on the vestibule surface, with Leu122 projecting
below the compounds. The binding site is created by the closed X-gate,
which traps inhibitors within the vestibule, explaining their exceptionally
slow washout rates. Mutation of binding-site residues (Thr93Cys, Ile118Ala,
Leu122Ala, Thr199Cys, Leu239Ala, Asn240Ala) substantially reduced
inhibition. Once trapped, the inhibitor remains bound for extended periods,
with important implications for drug development and clinical trials.


## Cross-References

- [Human TRAAK Potassium Channel (K2P 4.1)](/xray-mp-wiki/proteins/voltage-gated-channels/traak/) — K2P channel family comparison; TREK-2 (4XDJ) used as comparison for vestibule size measurements
- [Human K2P2.1 (TREK-1) I110D Mutant](/xray-mp-wiki/proteins/voltage-gated-channels/k2p2-1/) — Fellow K2P channel member; both are two-pore domain potassium channels
- [C-type Inactivation](/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/) — K2P channels use C-type gate as principal gating site; X-gate is an additional lower gate unique to TASK
- [Ion Channel Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — TASK-1 has a pseudo-tetrameric selectivity filter with K+ binding sites S1-S4
- [KirBac Potassium Channels](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) — Inward rectifier potassium channels discussed as comparison for lower gate architecture
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [KCNK10](/xray-mp-wiki/proteins/voltage-gated-channels/trek-2/) — Related protein structure
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
