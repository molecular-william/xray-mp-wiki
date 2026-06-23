---
title: NarGHI Quinol Binding Site
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-enzyme-mechanism, membrane-protein]
sources: [doi/10.1074##jbc.M410457200]
verified: false
---

# NarGHI Quinol Binding Site

## Overview
The quinol binding site (Q-site) of Escherichia coli nitrate reductase A (NarGHI) is located in the membrane anchor subunit NarI, within a narrow hydrophobic cleft (cleft B) between transmembrane helices II, III, and IV'. The site was structurally characterized at 2.0 A resolution using the inhibitor pentachlorophenol (PCP), which binds with high affinity (Kic = 57 nM) in close proximity to heme bD (edge-to-edge distance 2.8 A). The Q-site is multifunctional, capable of binding both physiological electron donors ubiquinol and menaquinol. Critical residues include His-66, which coordinates heme bD and positions within hydrogen-bonding distance of the PCP hydroxyl group, and Lys-86, whose mutation to alanine significantly impairs quinol oxidation activity and inhibitor binding. A chain of water molecules connecting heme bD propionates to bulk solvent suggests a proton wire for proton release into the periplasm during quinol oxidation.


## Mechanism/Details
**Structural characterization of the Q-site:**

The NarI subunit (225 amino acids) consists of five tilted transmembrane helices (I-V) with two additional short helices IV' and IV'' in a hairpin arrangement on the periplasmic side. Two hydrophobic clefts are present:

- **Cleft A (elongated cavity)** — Located between helices I, II, and IV', exposing the edges of both hemes bP and bD to the membrane. This may represent a secondary quinone reactive site, possibly involved in structural integrity or electron transfer without proton translocation.

- **Cleft B (PCP binding pocket)** — Located between helices II, III, and IV', leading to heme bD. This narrow pocket provides the spatial constriction for correct quinol orientation. PCP binds here with full occupancy, with thermal parameters similar to surrounding NarI residues.

**Inhibitor binding and kinetics:**

Pentachlorophenol (PCP) is a potent inhibitor of quinol:nitrate oxidoreductase activity (I50 ~0.4 uM). Steady-state kinetic analysis shows mixed inhibition with a competitive inhibitor binding constant Kic = 57 ± 14 nM and an uncompetitive constant of 490 ± 9 nM, indicating primarily competitive behavior. The fluorescence quencher HOQNO also inhibits with I50 ~1.5 uM and binds at the same site (Kd ~250 nM).

**Functional significance of key residues:**

- **His-66** — Axial ligand of heme bD; positioned within hydrogen-bonding distance of the PCP hydroxyl group. This dual role as both heme ligand and quinone ligand is a common theme in quinol/quinone binding sites (also observed in E. coli FdnGHI).

- **Lys-86** — Lines the Q-site pocket. The K86A mutation reduces plumbagin:nitrate oxidoreductase activity from 68 s-1 to 10 s-1 and abolishes high-affinity HOQNO binding. Similar lysine residues near quinone molecules play a potential role in proton shuttling in other respiratory complexes (e.g., E. coli fumarate reductase QP-site).

**Proton conduction pathway:**

A chain of water molecules located between the propionates of heme bD and the bulk solvent forms a "proton wire," analogous to those proposed in E. coli FdnGHI and the yeast cytochrome bc1 complex. The proposed quinol oxidation mechanism involves: (i) ubiquinol binds with its hydroxyl group forming hydrogen bonds to a heme bD propionate and His-66; (ii) one electron transfers to heme bD and one proton shuttles toward the periplasm via the water chain; (iii) the second electron transfers through the remaining redox chain (bP -> FS4 -> FS3 -> FS2 -> FS1 -> FS0) to the Mo-bisMGD cofactor in NarG, where nitrate is reduced.

**Multifunctional Q-site:**

The site accommodates both physiological electron donors. Molecular modeling shows that both ubiquinol and menaquinol can occupy the PCP binding pocket. The primarily competitive inhibition mode of PCP (a ubiquinol analog) against plumbagin (a menaquinol analog) supports this multifunctional role. This is similar to the QP-site in E. coli fumarate reductase, where DNP-19 and HOQNO bind at different locations within the same pocket.


## Examples in Membrane Protein Work
- narghi — The quinol binding site was characterized in NarGHI using the PCP-bound structure. The heterotrimeric enzyme (NarG, NarH, NarI) catalyzes electron transfer from quinol to nitrate, with the Q-site in NarI accepting electrons from ubiquinol or menaquinol and transferring them through an eight-center redox chain to the Mo-bisMGD cofactor in NarG.

## Related Concepts
- [Proton Wire](/xray-mp-wiki/concepts/proton-wire/) — A chain of water molecules between heme bD propionates and bulk solvent serves as a proton wire for shuttling protons during quinol oxidation
- [Quinol-Fumarate Reductase](/xray-mp-wiki/concepts/quinol-fumarate-reductase/) — E. coli fumarate reductase (Frd) has a similar multifunctional QP-site that accommodates multiple quinone analogs

## Cross-References
- [Nitrate Reductase A (NarGHI)](/xray-mp-wiki/proteins/enzymes/narghi/) — Primary enzyme in which this Q-site was characterized
- [Proton Wire](/xray-mp-wiki/concepts/proton-wire/) — The water-mediated proton conduction pathway from heme bD to the periplasm
