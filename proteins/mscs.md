---
title: E. coli MscS (Mechanosensitive Channel of Small Conductance)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3120]
verified: false
---

# E. coli MscS (Mechanosensitive Channel of Small Conductance)

## Overview

MscS (mechanosensitive channel of small conductance) is a mechanosensitive ion channel from Escherichia coli that gates in response to increased tension in the cytoplasmic membrane. It forms a heptameric assembly that opens in response to osmotic downshock, releasing cytoplasmic solutes to prevent cell lysis. MscS consists of four transmembrane helices (TM1, TM2, TM3a, TM3b) per subunit, with the TM3a helices lining the central pore. The channel features hydrophobic pockets between transmembrane helices that are filled by lipid acyl chains, and the extent of lipid interdigitation in these pockets is proposed to control channel gating.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.3120 | 5AJI | 3.0 A | C2 | MscS D67R1 single-cysteine MTSSL spin-labeled mutant, heptameric assembly | Phospholipid acyl chains in transmembrane pockets |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: MscS from Escherichia coli, D67R1 single-cysteine MTSSL spin-labeled mutant

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Concentration | Vivaspin concentrators (100 kDa cutoff) | -- | 50 mM sodium phosphate pH 7.5, 300 mM NaCl + 0.05% DDM | Concentrated to 9-13 mg/mL |


## Crystallization

### doi/10.1038##nsmb.3120

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | MscS D67R1, 9-13 mg/mL in 0.05% DDM, 50 mM sodium phosphate pH 7.5, 300 mM NaCl |
| Reservoir | 0.07 M sodium citrate pH 4.5, 0.07 M NaCl, 23% v/v PEG 400 |
| Temperature | 100 K (data collection) |
| Notes | Crystals grew to 0.3 x 0.1 x 0.1 mm in 2 d. Data collected at ID14-4, ESRF. Resolution determined by Diederichs-Karplus method as implemented in PDB REDO. |


## Biological / Functional Insights

### Lipid-filled pockets between transmembrane helices

Several phospholipid acyl chains were experimentally located in pockets formed between TM1, TM2, and TM3b helices in the heptameric MscS structure. Two alkyl chains penetrate into the pocket while a third packs against TM3b. Native mass spectrometry of purified MscS resolved lipid adducts of 620-790 Da, consistent with E. coli phosphatidylethanolamine (PE) and phosphatidylglycerol (PG) species. PE was the predominant phospholipid, with PG 30:1, PE 14:0/14:0, and PE 16:1/14:0 enriched relative to natural abundance in E. coli.

### Lipid exchange between pockets and bilayer

Molecular dynamics simulations (1 microsecond coarse-grained and 100 nanosecond atomistic) showed that lipids migrate to fill TM pockets in both closed and open states, with more lipids in the lower than upper half of the pocket. Fluorescence quenching with single-tryptophan mutants (A119W, A103W, V107W) demonstrated that phospholipid acyl chains exchange between the bilayer and TM pockets. Brominated lipids (BrPC) were used to confirm that pockets are accessible from the cytosolic leaflet. Lipids in pockets are mobile and in continuous contact with the bulk membrane bilayer.

### Mechanosensitive gating via lipid interdigitation

As MscS opens, the volume of the interhelical pockets decreases by approximately 1200 cubic angstroms per pocket, and the lipid content decreases by approximately one lipid per pocket. The loss occurs between TM2 and TM3a. Phospholipids with one acyl chain per head group (lysolipids, e.g. LPC 18:1) displace normal phospholipids (with two acyl chains) from MscS pockets and trigger channel opening, creating a subconducting state. The model proposes that the extent of acyl-chain interdigitation in these pockets determines the conformation of MscS, and that this lipid partitioning between pockets and bilayer is the missing component of tension-sensing models.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for MscS purification and crystallization
- [Phosphatidylethanolamine (PE)](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) — Predominant phospholipid bound in MscS transmembrane pockets
- [Phosphatidylglycerol (PG)](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) — Major E. coli phospholipid co-purifying with MscS
- [Polyethylene Glycol 400 (PEG 400)](/xray-mp-wiki/reagents/additives/peg-400/) — Crystallization precipitant
- [Sodium Phosphate Buffer](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) — 50 mM sodium phosphate pH 7.5 in purification buffer
- [Mechanosensitive Gating in Ion Channels](/xray-mp-wiki/concepts/mechanosensitive-gating/) — MscS is a canonical mechanosensitive channel
- [Lysophosphatidylcholine (LPC)](/xray-mp-wiki/reagents/lipids/lysophosphatidylcholine/) — Lysolipids displace normal phospholipids from MscS pockets and trigger channel opening
