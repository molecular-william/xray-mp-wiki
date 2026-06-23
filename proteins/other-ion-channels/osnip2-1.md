---
title: OsNIP2;1 (Silicon Transporter Lsi1 from Oryza sativa)
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2021.167226]
verified: false
---

# OsNIP2;1 (Silicon Transporter Lsi1 from Oryza sativa)

## Overview

OsNIP2;1 (Nodulin26-like Intrinsic Protein 2;1) is a silicon transporter from the rice plant Oryza sativa, also known as Lsi1 (low silicon rice 1). It belongs to the NIP (Nodulin26-like Intrinsic Protein) subfamily of aquaporins, also termed metalloid porins. OsNIP2;1 mediates the uptake of silicic acid across root cell plasma membranes, a critical step for silicon accumulation in rice and other grasses. The protein forms a tetrameric assembly with each protomer containing six transmembrane helices and two half-helices forming NPA motifs. The structure reveals a novel five-residue selectivity filter (TGSGR) and a channel gating mechanism involving cytoplasmic loop D.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2021.167226 | 7NL4 | 2.6 A | P1 | Truncated OsNIP2;1, residues 38-264, N4Q/N13Q/N26Q glycosylation mutants, C-terminal 6xHis-tag | None (apo) |
| doi/10.1016##j.jmb.2021.167226 | 7NL4 | 3.8 A | C2 | Full-length OsNIP2;1, N4Q/N13Q/N26Q glycosylation mutants, C-terminal 6xHis-tag | None (apo) |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae W303 delta pep4 strain
- **Construct**: Synthetic gene optimized for yeast expression; hexa-histidine tag at C terminus; N-terminal glycosylation sites removed (N4Q/N13Q/N26Q); cloned via BamHI and XhoI into 83v vector; expressed by galactose induction (YP medium with 1.5% galactose) at 30 C for 16-20 hours

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Cell disruption (cell disrupter at 35-37 kpsi) | -- | TSB buffer (20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris), 300 mM NaCl, pH 8) with 5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta) + -- | Cells resuspended in TSB buffer with [EDTA](/xray-mp-wiki/reagents/additives/edta); lysed by 1-2 passes through cell disrupter; membranes collected by centrifugation at 200,000g for 90 min |
| Solubilization | Membrane solubilization | -- | TSB buffer (20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris), 300 mM NaCl, pH 8) with Complete [EDTA](/xray-mp-wiki/reagents/additives/edta)-free protease inhibitor + 1:1 (w/w) mixture of [dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm))] and [[DM](/xray-mp-wiki/reagents/detergents/decylmaltoside)] (total 1% w/v detergent) | Homogenization in TSB with DDM/DM mixture; stirred at 4 C for 1 hr or overnight; 1 g total detergent per 2 liters of cells |
| Affinity chromatography | Ni-NTA affinity chromatography | -- | TSB buffer with [[DM](/xray-mp-wiki/reagents/detergents/decylmaltoside)] + ['[DM](/xray-mp-wiki/reagents/detergents/decylmaltoside)'] | Centrifuged membrane extract loaded onto Ni-NTA resin |


## Crystallization

### doi/10.1016##j.jmb.2021.167226

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | Truncated OsNIP2;1 (residues 38-264) at ~5 mg/ml in [[DM](/xray-mp-wiki/reagents/detergents/decylmaltoside)] |
| Reservoir | MemGold H11 hit condition: 1 mM cadmium chloride, 30 mM magnesium chloride, 0.1 M [MES](/xray-mp-wiki/reagents/buffers/mes) (pH 6.5), 30% [PEG](/xray-mp-wiki/reagents/additives/peg) 400 |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Block-shaped crystals in space group P1. Data collected at beamline I24 at Diamond Light Source. Solved by molecular replacement using AqpM from Methanothermobacter marburgensis (PDB 2EVU) as search model. Two tetramers per asymmetric unit. Cadmium ions bridge tetramers via cytoplasmic faces. |


## Biological / Functional Insights

### Novel five-residue selectivity filter (TGSGR)

The extracellular mouth of OsNIP2;1 contains a five-residue selectivity filter TGSGR, which is wider than the canonical four-residue SF of conventional aquaporins. The fifth residue, Thr65, is located at the extracellular end and is occluded in most other AQP/AQGP structures by an aromatic residue. The SF contains four oxygen atoms lining the channel, providing multiple hydrogen bond donor and acceptor groups for the four hydroxyl groups of translocating silicic acid. The Arg residue in the SF forms a hydrogen bond with Gly155 in extracellular loop C, constraining the Arg sidechain in a substrate-permissive position. A precise spacing of 108 residues between the NPA motifs is crucial for Si selectivity, as it positions Gly155 to maintain this critical Arg-loop C interaction.

### Channel gating by cytoplasmic loop D

The OsNIP2;1 channel is closed in the crystal structure by cytoplasmic loop D (residues 185-ATDTRA-191). Equilibrium MD simulations in a [POPC](/xray-mp-wiki/reagents/lipids/popc) bilayer show that the channel opens in solution: three independent 0.5 microsecond simulations show a pronounced shift of up to 15 A for the Arg189 side chain, opening the channel. 10 out of 12 monomers showed partial or complete channel opening, suggesting the closed conformation was selected by crystallization. The closed channels in MD simulations are still more open than the crystal structure per HOLE analysis. Channel opening may require phosphorylation of residues such as Thr186 or Thr188 in loop D, though no phosphorylation was detected by mass spectrometry.

### Silicic acid translocation mechanism

MD simulations reveal spontaneous silicic acid uptake and export through OsNIP2;1. Translocating silicic acid molecules form hydrogen bonds with all SF residues including Thr65, with Ser207 appearing especially important. The SF region combined with NPA1 motif provides the largest permeation barrier. Residence times in SF, NPA1, and NPA2 regions were 16.0 ns, 9.9 ns, and 8.4 ns from steered MD, respectively. Silicic acid (diameter 6 +/- 0.5 A) is larger than most of the channel per HOLE analysis, but non-spherical geometry allows permeation without hydration waters. The molecule rotates during passage, with hydroxyl hydrogens pointing away from NPA asparagine side chains at the NPA region. Transport appears bidirectional in the absence of a gradient.


## Cross-References

- [Aquaporin Family](/xray-mp-wiki/concepts/aquaporin/) — OsNIP2;1 is a member of the NIP subfamily of aquaporins (metalloid porins)
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used for membrane solubilization and purification
- [n-Dodecyl-beta-D-Maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in solubilization mixture with DM (1:1 w/w)
- [Decyl Maltose Neopentyl Glycol (DMng)](/xray-mp-wiki/reagents/detergents/dmng/) — Detergent in which OsNIP2;1 behaves well for crystallization
- [Cadmium Chloride](/xray-mp-wiki/reagents/additives/cadmium-chloride/) — Used in crystallization reservoir; bridges tetramers via cytoplasmic faces
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — Buffer in crystallization reservoir (0.1 M, pH 6.5)
- [PEG (Polyethylene Glycol) 400](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant (30% w/v)
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Crystallization additive (30 mM)
- [EDTA](/xray-mp-wiki/reagents/additives/edta) — Additive used in purification or crystallization buffers
- [Tris](/xray-mp-wiki/reagents/buffers/tris) — Buffer component in purification or crystallization
