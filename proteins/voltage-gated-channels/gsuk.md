---
title: GsuK Multi-Ligand Gated K+ Channel
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.7554##eLife.00184]
verified: false
---

# GsuK Multi-Ligand Gated K+ Channel

## Overview

GsuK is a two-transmembrane, RCK-regulated K+ channel from *Geobacter sulfurreducens*. Each subunit contains two tandem RCK domains, reminiscent of Slo K+ channels. The channel is activated by [ADP](/xray-mp-wiki/reagents/ligands/adp/) and NAD+, while Ca2+ serves as an allosteric inhibitor. GsuK features a segmented inner helix pore with a unique opening mechanism distinct from other K+ channels. The channel exhibits weak K+ selectivity due to a Phe residue in the selectivity filter, and its intracellular gate is located at the end of the inner helix, coupled to the RCK gating ring via extended linkers.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.00184 | 4GVL | 3.0 | I222 | Intracellular subunit (residues 110-564) |  |
| doi/10.7554##eLife.00184 | 4GX5 | 3.7 | C2 | Wild-type full-length (E52A/Q77E mutants) | Ca2+ |
| doi/10.7554##eLife.00184 | 4GX0 | 2.6 | C2 | L97D mutant full-length | Ca2+ |
| doi/10.7554##eLife.00184 | 4GX1 | 2.8 | C2 | L97D mutant with [ADP](/xray-mp-wiki/reagents/ligands/adp/) | [ADP](/xray-mp-wiki/reagents/ligands/adp/) |
| doi/10.7554##eLife.00184 | 4GX2 | 3.2 | C2 | L97D mutant with NAD+ | NAD+ |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: Full-length GsuK (Ala9 with N-terminal MQRGS) in pQE70 vector with C-terminal His-tag and thrombin cleavage site
- **Notes**: Intracellular subunit construct starts at Tyr10 with N-terminal MQ
- **Induction**: 0.4 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) at A600 ~0.8, 37°C for 3-4 hr

### Purification Workflow

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: GsuK in pQE70 with C-terminal His-tag
- **Tag info**: C-terminal His6, removed by in-gel thrombin digestion

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest and lysis | Lysis | — | 50 mM [[Tris](/xray-mp-wiki/reagents/buffers/tris/) Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 250 mM KCl, protease inhibitors |  |
| Membrane protein extraction | Detergent extraction | — | 50 mM [[Tris](/xray-mp-wiki/reagents/buffers/tris/) Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 250 mM KCl + 40 mM [N Decyl Beta D Maltoside](/xray-mp-wiki/reagents/detergents/dm/) (DM) | 3 hr at room temperature |
| Affinity chromatography | IMAC (Co2+) | [Talon](/xray-mp-wiki/reagents/additives/talon/) Co2+ affinity resin (Clontech) | 50 mM [[Tris](/xray-mp-wiki/reagents/buffers/tris/) Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 250 mM KCl + 4 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) |  |
| Tag removal | Thrombin cleavage | — |  | In-gel digestion, 1 U thrombin per L culture, 4°C overnight |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (10/30) | 20 mM CHES pH 9.0, 150 mM KSCN, 2 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/) + 4 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) | For full-length channel; also contains 0.1 mg/ml E. coli polar lipid |

**Final sample**: ~6-8 mg/ml in SEC buffer
**Purity**: Tetrameric on SEC


## Crystallization

### doi/10.7554##eLife.00184

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | Purified GsuK intracellular subunit (~8 mg/ml) |
| Reservoir | 20-23% [Peg](/xray-mp-wiki/reagents/additives/peg/) 3350, 120 mM KCl, 80 mM NaNO3, 1% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 100 mM Bis-Tris propane pH 8.5 |
| Temperature | 20 |
| Cryoprotection | 20% [Peg](/xray-mp-wiki/reagents/additives/peg/) 400 |
| Notes | Intracellular subunit crystals |

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | Full-length GsuK in [DM](/xray-mp-wiki/reagents/detergents/dm/) with E. coli polar lipids (~6 mg/ml) |
| Reservoir | 20-23% [Peg](/xray-mp-wiki/reagents/additives/peg/) 3350, 120 mM KCl, 80 mM NaNO3, 1% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 100 mM Bis-Tris propane pH 8.5 |
| Temperature | 20 |
| Cryoprotection | 20% [Peg](/xray-mp-wiki/reagents/additives/peg/) 400 |
| Notes | Full-length channel crystals; various constructs used (wild-type, L97D, L97D+[ADP](/xray-mp-wiki/reagents/ligands/adp/), L97D+NAD+) |


## Biological / Functional Insights

### Multi-ligand gating mechanism

GsuK is activated by [ADP](/xray-mp-wiki/reagents/ligands/adp/) and NAD+ and inhibited by Ca2+. Ca2+ binds at the inter-subunit assembly interface of the gating ring, stabilizing the closed conformation. [ADP](/xray-mp-wiki/reagents/ligands/adp/) binds at the Rossmann-fold nucleotide binding site on RCK2; the cis configuration of [ADP](/xray-mp-wiki/reagents/ligands/adp/) inserts the beta-phosphate into a pocket at the flexible interface, promoting gating ring conformational change. NAD+ binds with the nicotinamide group inserted beneath the alphaF helix of RCK1, acting as a lever to promote hinged motion.

### Distinct pore opening mechanics

GsuK has a segmented inner helix (TM2A, TM2B, TM2C) with two hinge points (Gly92 and between TM2B/2C). The intracellular gate is at Leu117, at the end of the inner helix, coupled directly to the gating ring via extended linkers. Pore opening involves bending at Gly92 (hinge 1) with TM2B and TM2C moving as a rigid body, rotating Leu117 away from the permeation pathway — a mechanism distinct from [Mthk](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) and Kv channels.

### Structural resemblance to Slo channels

GsuK shares several features with eukaryotic Slo K+ channels: dual RCK domains per subunit, TVGFG selectivity filter sequence, segmented inner helix with a proline break equivalent, and NAD+ modulation at the conserved nucleotide binding site in RCK2. The relative orientation between the pore and gating ring in GsuK may more closely resemble Slo channels than [Mthk](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/).


## Cross-References

- [RCK Domain Activation Mechanism](/xray-mp-wiki/concepts/structural-mechanisms/rck-domain-activation-mechanism/) — GsuK gating is regulated by its RCK domains binding ADP, NAD+, and Ca2+
- [ADP](/xray-mp-wiki/reagents/ligands/adp/) — Referenced in gsuk text
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in gsuk text
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in gsuk text
- [N Decyl Beta D Maltoside](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in gsuk text
- [Talon](/xray-mp-wiki/reagents/additives/talon/) — Referenced in gsuk text
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in gsuk text
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Referenced in gsuk text
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Referenced in gsuk text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in gsuk text
