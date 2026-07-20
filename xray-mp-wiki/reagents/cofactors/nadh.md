---
title: "NADH"
created: 2026-05-27
updated: 2026-06-03
type: reagent
category: reagents
layout: default
tags: [cofactor, subdirectory-cofactors]
sources: [doi/10.1016##j.jmb.2020.05.017, doi/10.1038##nature12056]
verified: agent
---

# NADH

## Overview

Nicotinamide adenine dinucleotide (reduced form, NADH) is a universal electron carrier cofactor that serves as the primary electron donor in the SCD1 in vitro electron transfer chain. NADH donates electrons to [Cytochrome b5 Reductase](/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/) (b5R), which then transfers them through [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/) to [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) desaturase 1 (SCD1), ultimately driving the desaturation of [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) to [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/). NADPH can also serve as an electron donor but NADH is the preferred substrate in the described system.


## Properties

- **Chemical name**: Beta-Nicotinamide adenine dinucleotide (reduced)
- **Chemical formula**: C21H29N7O17P3
- **Molecular weight**: 663.4 g/mol
- **Class**: Dinucleotide cofactor

## Use in Membrane Protein Work

### Electron donor in SCD1 electron transfer chain

NADH serves as the initial electron donor in the reconstituted SCD1 electron transfer chain. It reduces the [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/) cofactor of [Cytochrome b5 Reductase](/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/) (b5R), which in turn reduces the [HEME](/xray-mp-wiki/reagents/ligands/heme/) of [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/). Reduced [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/) then donates electrons to SCD1 to drive the desaturation reaction. The reaction was initiated by adding 1 mM NADH to the in vitro system containing SCD1 (2 uM), cyt b5 (10 uM), b5R (20 uM), and [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) (300 uM).


### In vitro electron transfer kinetics

NADH-dependent reduction of [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/) was confirmed by a shift in the Soret peak from 413 nm to 423 nm, indicating that b5R and cyt b5 function properly. Kinetic measurements were conducted anaerobically using a stopped-flow apparatus inside an anaerobic chamber. NADH was prepared in anaerobic buffer and added to reduce cyt b5 before mixing with SCD1.


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| [Cytochrome b5 Reductase](/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/) | 1 mM (initiating in vitro reaction) | Electron donor for b5R in reconstituted SCD1 electron transfer chain | Reduces b5R [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/), driving electron flow to cyt b5 and SCD1 |
| [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/) | 3.1 uM with 3.1 uM NADH | Anaerobic reduction of cyt b5 [HEME](/xray-mp-wiki/reagents/ligands/heme/) by b5R + NADH; monitored by Soret peak shift from 413 nm to 423 nm | Confirmed proper function of b5R and cyt b5 in electron transfer chain |
| [TRKA](/xray-mp-wiki/proteins/pumps-atpases/trka/) (ATP-binding Regulatory Subunit from Klebsiella pneumoniae) | Not specified | NADH binding to [TRKA](/xray-mp-wiki/proteins/pumps-atpases/trka/) in the TrkH-[TRKA](/xray-mp-wiki/proteins/pumps-atpases/trka/) complex; four binding sites identified in [TRKA](/xray-mp-wiki/proteins/pumps-atpases/trka/) tetramer | 3.8 A structure of TrkH-[TRKA](/xray-mp-wiki/proteins/pumps-atpases/trka/) complex with NADH bound; conserved GXGXXG motif forms NADH binding site; likelihood-weighted Fo-Fc maps at 3 sigma |

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [Cytochrome b5 Reductase](/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/) — Primary electron acceptor from NADH; catalyzes electron transfer to cyt b5
- [Mouse Stearoyl-CoA Desaturase 1 (mSCD1)](/xray-mp-wiki/proteins/enzymes/mouse-scd1/) — Terminal electron acceptor; NADH drives entire electron transfer chain to SCD1
- [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/) — Intermediate electron carrier; reduced by b5R using NADH electrons
- [TrkH (Potassium Channel from Klebsiella pneumoniae)](/xray-mp-wiki/proteins/pumps-atpases/trkh/) — NADH binds to the TrkH-TrkA complex; used for anomalous phasing in 3.8 A structure
- [TrkA (ATP-binding Regulatory Subunit from Klebsiella pneumoniae)](/xray-mp-wiki/proteins/pumps-atpases/trka/) — NADH binds to TrkA in the TrkH-TrkA complex; four binding sites identified in TrkA tetramer
- [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/) — Additive used in purification or crystallization buffers
- [HEME](/xray-mp-wiki/reagents/ligands/heme/) — Related ligand or cofactor
- [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) — Related ligand or cofactor
- [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) — Related ligand or cofactor
