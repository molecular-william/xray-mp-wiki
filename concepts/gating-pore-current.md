---
title: Gating Pore Current (Omega Current)
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-concepts]
sources: [doi/10.1038##s41586-018-0120-4, doi/10.1038##nature05598, doi/10.1085##jgp.200709755]
verified: false
---

# Gating Pore Current (Omega Current)

## Overview
The gating pore current (also called omega current) is a pathological ionic current that flows through the voltage-sensor domain (VSD) of voltage-gated ion channels when mutations create an aqueous pathway through the membrane via the gating charge pore. In voltage-gated sodium channels, single mutations of positively charged gating charges (arginine residues) in the S4 transmembrane segment can create a cation leak pathway that bypasses the central pore, leading to periodic paralysis disorders.


## Mechanism/Details
The voltage-sensor domain of voltage-gated sodium channels contains highly
conserved positively charged arginine residues (designated R1-R4) in the S4
helix that serve as gating charges. Under normal conditions, these charges
move through a narrow hydrophobic constriction site (HCS) in the VSD during
voltage sensing, without creating a continuous aqueous pore across the
membrane.

Mutations of the outermost gating charges create pathogenic gating pores:
- R1 and R2 mutations (outermost): cause hypokalaemic periodic paralysis by
  creating a gating pore permeable to cations in the resting (hyperpolarized)
  state of the VSD
- R3 mutations: cause normokalaemic periodic paralysis by creating a gating
  pore conducting cations in both activated and inactivated states

High-resolution crystal structures of NavAb bacterial sodium channels with
analogous R2G and R3G mutations reveal the structural basis:
- R2G and R3G mutations do not alter the backbone structure of the VSD
- Both mutations create an aqueous cavity near the hydrophobic constriction
  site that controls gating charge movement
- R3G extends the extracellular aqueous cleft through the entire activated
  VSD, creating a continuous aqueous path through the membrane
- R2G creates a continuous aqueous path only in the resting state, as
  revealed by molecular modeling

Crystal structures of NavAb(R2G) in complex with guanidinium define a
potential drug target site within the gating pore. Molecular dynamics
simulations show that Na+ permeation through the mutant gating pore occurs
in concert with conformational fluctuations of the remaining gating charge
R4, which acts as a dynamic barrier.

## Examples in Membrane Protein Work
- [NavAb R2G Mutant](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — The R2G mutation in the bacterial NavAb channel, analogous to the hypokalaemic periodic paralysis mutation in human Nav1.4 R2, creates an aqueous cavity near the HCS. Crystal structures at high resolution reveal the structural changes and guanidinium binding defines a potential drug target site within the gating pore.

- [NavAb R3G Mutant](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — The R3G mutation in NavAb, analogous to the normokalaemic periodic paralysis mutation, extends the extracellular aqueous cleft through the entire activated VSD, creating a continuous aqueous path for cation leak.


## Related Concepts
- [Gated-Pore Mechanism]() — Distinct from gated-pore mechanism in transporters; gating pore current is a pathological leak through the voltage sensor domain, not the central pore of the channel

- [Voltage-Sensor Paddle]() — The S4 segment and its associated paddle motif contain the gating charges whose mutation creates the gating pore

- [Sodium Channel Gating and Selectivity]() — Gating pore currents represent a pathological disruption of normal sodium channel gating and voltage sensing


## Cross-References
- [NavAb Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — NavAb R2G and R3G mutants reveal structural basis of gating pore currents
- [Sodium Channel Gating and Selectivity](/xray-mp-wiki/concepts/sodium-channel-gating/) — Context for how gating pore currents disrupt normal gating function
- [Hydrophobic Gating (Vapor Lock Mechanism)](/xray-mp-wiki/concepts/hydrophobic-gating/) — The hydrophobic constriction site whose disruption creates the gating pore
- [Sliding Helix Mechanism](/xray-mp-wiki/concepts/sliding-helix-mechanism/) — The voltage-sensing mechanism that is altered by gating charge mutations
- [Voltage-Sensor Paddle](/xray-mp-wiki/concepts/voltage-sensor-paddle/) — Structural motif containing the gating charges whose mutation creates gating pores
