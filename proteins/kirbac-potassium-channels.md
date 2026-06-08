---
title: 
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2010.05.003]
verified: false
---

# 

## Overview

KirBac1.1 and KirBac3.1 are prokaryotic inward-rectifier potassium channels from Magnetospirillum magnetotactium that serve as structural models for eukaryotic Kir channels. This paper presents comparative analysis of 11 KirBac structures (KirBac1.1 at 3.7 A and multiple KirBac3.1 structures at 2.6-4.2 A resolution), revealing interdependent gates in the conduction pathway and the mechanism of polyamine block. Key findings include: (1) interdomain conformational changes coupled to ion configuration in the selectivity filter, (2) identification of two polyamine-binding sites in intracellular interfaces, and (3) a staged path to activation via two-fold symmetric intermediates where unlatching of subunit interfaces is concomitant with channel activation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2010.05.003 | 1P7B | 3.7 A | I222 | Full-length KirBac1.1 with His-tag | Mg2+ (blocked configuration) |
| doi/10.1016##j.cell.2010.05.003 | 1XL4 | 2.6 A | P21212 | Full-length KirBac3.1 with His-tag | Ca2+ (blocked), [Spermine](/xray-mp-wiki/reagents/additives/spermine/) |
| doi/10.1016##j.cell.2010.05.003 | 1XL6 | 2.8 A | C2221 | Full-length KirBac3.1 with His-tag | [Spermine](/xray-mp-wiki/reagents/additives/spermine/) (conduction-compromised) |

## Expression and Purification

- **Expression system**: E. coli BL21 (DE3) star
- **Construct**: Full-length histidine-tagged recombinant KirBac3.1

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenizer | — | not specified | 20,000 psi |
| Solubilization | Detergent solubilization | — | 1% [Anzergent 3,12](/xray-mp-wiki/reagents/detergents/anzergent-3-12/), room temp, 1 hr |  |
| [Affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni2+-loaded IMAC resin | Ni2+-IMAC |  |  |
| [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | — |  |  |
| Concentration | Ultrafiltration | Amicon | ~8 mg/ml |  |


## Crystallization

### doi/10.1016##j.cell.2010.05.003

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified KirBac3.1 at ~8 mg/ml |
| Reservoir | Varies by structure: 20%  3350 + 0.2 M CaCl2 + 0.1 M [HEPES(/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5 (III); 15%  3350 + 0.1 M [MgCl2(/xray-mp-wiki/reagents/additives/mgcl2/) + 0.1 M sodium  pH 5.6 (VI); 20% [PEG(/xray-mp-wiki/reagents/additives/peg/) 3350 + 0.2 M  + 0.1 M [HEPES(/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5 (VIII); 20%  3350 + 0.2 M [spermine(/xray-mp-wiki/reagents/additives/spermine/) + 0.1 M [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 8.0 (XI) |
| Temperature | 19-20 C |
| Notes | Crystallized at Bio21 C3 facility. Structures III-VII phased by molecular replacement using 1XL4/1XL6. Structures VIII and XI soaked in 50 mM [spermine](/xray-mp-wiki/reagents/additives/spermine/) prior to data collection. Q170A mutant crystallized separately. |


## Biological / Functional Insights

### Selectivity filter gating

The ion distribution in the selectivity filter is systematically correlated to global conformational changes. Twist structures have three-ion configuration (S1, S3, S4) representing stalled conduction. Nontwist structures have four occupied sites indicating conducting state. Divalent ions (Mg2+, Ca2+, Ba2+) produce blocked configurations. Selectivity filter can switch between nonconducting and conducting configurations without significant displacement of inner helices.

### Polyamine binding and rectification

Two distinct polyamine-binding sites identified at latched intracellular interfaces. [Spermine](/xray-mp-wiki/reagents/additives/spermine/) binds within closed pockets at latched interfaces but not at unlatched interfaces. Unlatching causes intracellular vestibule to connect with pore, simultaneously disrupting binding sites and facilitating polyamine release into conduction path. His177 (KirBac3.1) counterpart of His216 in Kir6.2 implicated in pH-titratable rectification.

### Staged activation pathway

Conformational interchange mediated at intracellular subunit interfaces follows a staged path to activation via two-fold symmetric intermediates. Latched/unlatched interfaces alternate, distorting symmetry. Only when all four interfaces eschew latched arrangement can selectivity filter acquire conducting conformation. Unlatching is concomitant with activation.


## Cross-References

- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni2+-loaded IMAC used for His-tagged KirBac purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC used after affinity chromatography for KirBac purification
- [Anzergent 3,12](/xray-mp-wiki/reagents/detergents/anzergent-3-12/) — Primary solubilization detergent at 1% for KirBac3.1 extraction
- [Calcium Chloride](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Crystallization additive (0.2 M) in structure III
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Crystallization additive (0.1 M) in structure VI
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant (PEG 3350)
- [Spermine](/xray-mp-wiki/reagents/additives/spermine/) — Crystallization additive (0.2 M) and channel blocker
- [Citrate Buffer](/xray-mp-wiki/reagents/buffers/citrate/) — Crystallization buffer (0.1 M sodium citrate pH 5.6) in structure VI
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Crystallization buffer (0.1 M HEPES pH 7.5/8.0)
