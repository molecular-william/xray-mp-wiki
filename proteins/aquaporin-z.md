---
title: Aquaporin Z (AqpZ) - Escherichia coli
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [aquaporin, water-channel, membrane-protein, tm-helices, homotetramer]
sources: [doi/10.1016##j.jmb.2007.02.070]
---

# Aquaporin Z (AqpZ) - Escherichia coli

## Overview

X-ray crystal structures of Escherichia coli Aquaporin Z (AqpZ) mutants in complex with mercury, revealing the structural basis of aquaporin inhibition. AqpZ is the bacterial homolog of human AQP1, sharing the canonical aquaporin fold: six transmembrane helices (M1-M8, with M1-M2 and M5-M6 as half-helices) and two NPA motifs. AqpZ is water-selective with a conserved histidine at the selectivity filter. Structures determined for T183C and L170C mutants (apo and mercury-bound forms) reveal a steric blockage mechanism for mercury inhibition.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2007.02.070 | 2O9D | 2.3 A | not specified | AqpZ T183C mutant (C9S/C20S background) | Apo form |
| doi/10.1016##j.jmb.2007.02.070 | 2O9E | 2.2 A | not specified | AqpZ T183C mutant + HgCl2 | [Mercury](/xray-mp-wiki/reagents/mercury/) (Hg2+) at two sites: pore and interstitial |
| doi/10.1016##j.jmb.2007.02.070 | 2O9F | 2.55 A | not specified | AqpZ L170C mutant (C9S/C20S background) | Apo form |
| doi/10.1016##j.jmb.2007.02.070 | 2O9G | 1.9 A | not specified | AqpZ L170C mutant + HgCl2 | [Mercury](/xray-mp-wiki/reagents/mercury/) (Hg2+) at four pore sites |

## Expression and Purification

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: AqpZ with 6xHis tag (C9S/C20S background for T183C and L170C)

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer lysis | -- | 20 mM Tris (pH 7.4), 100 mM NaCl, 0.5 mM PMSF, 5 mM BME | 6 L culture, 100,000g centrifugation for 2 h to recover membranes |
| Solubilization | 10-16 h agitation at 4 C | -- | 20 mM Tris (pH 7.4), 100 mM NaCl, 5 mM BME, 10% glycerol, 270 mM OG | OG = n-octyl beta-D-glucopyranoside |
| Affinity chromatography | Ni-NTA batch binding | Ni-NTA (Qiagen) | 20 mM Tris (pH 7.4), 100 mM NaCl, 5 mM BME, 10% glycerol, 40 mM OG, 20 mM imidazole (wash) | Eluted with 250 mM imidazole |
| Tag removal | Trypsin digestion | -- | -- | 5 ug trypsin for 12 h; imidazole removed by Biorad Econo-Pac 10DG column |


## Crystallization

### doi/10.1016##j.jmb.2007.02.070

| Parameter | Value |
|---|---|
| Method | Standard crystallization (details from parent study) |
| Protein sample | Purified AqpZ mutants |
| Reservoir | -- |
| Temperature | -- |
| Notes | Crystallized with and without HgCl2; structures solved by molecular replacement |


## Biological / Functional Insights

### Steric blockage mechanism of mercury inhibition

[Mercury](/xray-mp-wiki/reagents/mercury/) blocks the AqpZ pore through steric occlusion without conformational change (RMSD 0.27 A between apo and Hg-bound forms). In T183C, two Hg2+ sites were found: one directly in the pore (T183C-Hg1) ~5.6 A from Cys183, and one interstitially bound to Cys183 (T183C-Hg2) in a hydrophilic pocket with Glu138 and Ser177. In L170C, four mercury atoms clustered at the pore site, with Hg2 covalently bound to Cys170 at 2.6 A (ideal S-Hg bond length). Hg atoms form dinuclear complexes with distances of 2.3-2.5 A between atoms.

### [Mercury](/xray-mp-wiki/reagents/mercury/) dynamics and radiation damage

[Mercury](/xray-mp-wiki/reagents/mercury/) atoms show significant disorder and radiation sensitivity. Occupancies refined to 0.24 (T183C-Hg1), 0.32 (T183C-Hg2), and 0.40/0.23/0.20/0.18 for L170C-Hg1/2/3/4. F_o-F_c difference maps show noisy positive peaks after refinement, attributed to radiation-induced cleavage of thiol-mercury bonds. The more deeply buried L170C-Hg1 showed little radiation-induced motion compared to solvent-accessible sites.

### [Mercury](/xray-mp-wiki/reagents/mercury/) sensitivity of mutants

IC50 values for HgCl2 inhibition: WT AqpZ 345 uM, T183C 84 uM, L170C 18 uM. L170C is 20 times more sensitive than WT and 4 times more sensitive than T183C. Water conduction rates: WT 73.9 s-1, T183C 57.3 s-1, L170C 39.0 s-1. Inhibition is reversible with 5 mM 2-mercaptoethanol (BME).

### NPA motifs and selectivity filter

AqpZ has the canonical aquaporin architecture with two NPA (Asn-Pro-Ala) motifs at the ends of half-helices M3 and M7. The selectivity filter contains a conserved histidine (characteristic of water-selective AQPs) and is smaller and more polar than aquaglyceroporins. The pore is ~20 A long, resembling WT structure.


## Cross-References

- [Mercury (HgCl2)](/xray-mp-wiki/reagents/mercury/) — Inhibitor used to block AqpZ water channel
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Primary detergent for solubilization at 270 mM
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component (20 mM, pH 7.4) for purification
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer (20 mM, pH 7.5) for liposome reconstitution and running buffer
