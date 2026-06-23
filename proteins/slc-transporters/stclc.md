---
title: StClC CIC Chloride Channel
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##415287a]
verified: false
---

# StClC CIC Chloride Channel

## Overview

StClC is a prokaryotic CIC chloride channel from Salmonella enterica serovar typhimurium whose X-ray crystal structure at 3.0 Å resolution, together with the related EcClC channel from Escherichia coli at 3.5 Å, revealed the molecular basis of anion selectivity in CIC chloride channels. The structure showed that CIC channels form homodimers with two independent pores, each pore formed by a separate subunit with an antiparallel transmembrane architecture. Each subunit is composed of two roughly repeated halves that span the membrane with opposite orientations, and the Cl- selectivity filter is defined by electrostatic interactions with alpha-helix dipoles and chemical coordination with main-chain amide nitrogen atoms and side-chain hydroxyl groups from Ser 107 and Tyr 445. The pore features a narrow selectivity filter near the membrane center with wider vestibules on both sides. A conserved glutamate residue (Glu 148) projects into the pore above the Cl- binding site and is proposed to act as a gate that must be displaced for Cl- conduction to occur. This landmark study established the physical and chemical principles underlying anion selectivity in the CIC channel family.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##415287a | 1KPL | 3.0 A | P2(1) | Full-length StClC from Salmonella enterica serovar typhimurium with C-terminal His tag | Cl- ion bound in selectivity filter |

## Expression and Purification

- **Expression system**: E. coli BL21 DE3
- **Construct**: StClC cloned into pET28b+ vector using NcoI and XhoI restriction sites with C-terminal His tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression | -- | -- + -- | StClC expressed in E. coli BL21 DE3 with C-terminal His tag |


## Crystallization

### doi/10.1038##415287a

| Parameter | Value |
|---|---|
| Method | Vapor diffusion / heavy atom derivatization |
| Protein sample | Purified StClC in detergent |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Native data collected at BNL X25 beamline. Initial phases estimated from platinum derivatives. Four-fold [NCS](/xray-mp-wiki/concepts/non-crystallographic-symmetry/) averaging and phase extension to 3.0 Å using RAVE and DM. Solvent-flattened, averaged electron density maps used for model building. Crystal form: P2(1) space group. |


## Biological / Functional Insights

### Antiparallel architecture defines the CIC channel fold

Each CIC subunit is composed of two roughly repeated halves (helices A-I and J-R) that span the membrane with opposite orientations. This antiparallel architecture brings the N-termini of alpha-helices D, F, and N together near the membrane center to form an electrostatically favorable environment for anion binding. This architecture is distinct from the parallel barrel-stave architecture of K+ channels and represents a novel membrane protein fold that satisfies the constraints of placing helix dipoles at the selectivity filter while burying the opposite ends in the membrane.

### Cl- selectivity filter uses partial charges, not full charges

The Cl- ion is coordinated by main-chain amide nitrogen atoms from Ile 356 and Phe 357, and side-chain oxygen atoms from Ser 107 and Tyr 445. The favorable electrostatic environment arises from partial positive charges contributed by helix dipole interactions and contacts with main-chain and side-chain nitrogen and oxygen atoms. Unlike cation channels that use full positive charges, CIC channels use partial charges to stabilize Cl- while still permitting rapid ionic diffusion rates. A full positive charge would create too deep an energy well.

### Glutamate gate mechanism for Cl- conduction

A conserved glutamate residue (Glu 148) projects into the pore above the Cl- binding site, sandwiched between the positive ends of alpha-helices F and N. The selectivity filter effectively contains two anions: a Cl- ion at the inner site (closer to the intracellular vestibule) and a carboxylate anion (Glu 148) at the outer site (closer to the extracellular vestibule). For Cl- conduction to occur, the glutamate side chain must swing out of the way, allowing a Cl- ion to enter in its place. This provides a structural basis for the Cl- activation and gating properties observed in CIC channels.

### Double-barreled channel architecture

The CIC channel forms a homodimer with two identical pores, each formed by a separate subunit. The contact surface between subunits is extensive (~2,300 Å² within the membrane), consistent with CIC channels existing and functioning only as dimers. The two pores are separated by a large distance and by an electronegative (Cl--repulsive) region on the extracellular surface, consistent with the functional independence of the two pores observed in ClC-0 channels by single-channel analysis.

### Electrostatic funneling of Cl- ions

The vestibules leading to the selectivity filter on both sides of the membrane contain basic (positively charged) amino acids (e.g., Arg 147, Arg 451). The distribution of charges on the entire channel surface creates an electrostatic potential that funnels Cl- ions into the pore entryways. Poisson-Boltzmann calculations in 150 mM electrolyte confirm that the electrostatic surface potential around the pore openings attracts anions.


## Cross-References

- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Comparison of antiparallel (CIC) vs barrel-stave (KcsA) ion channel architectures
- [NCS](/xray-mp-wiki/concepts/non-crystallographic-symmetry/) — Related biological concept
