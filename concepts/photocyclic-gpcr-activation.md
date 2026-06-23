---
title: Photocyclic GPCR Activation
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-concepts]
sources: [doi/10.1073##pnas.1617446114]
verified: false
---

# Photocyclic GPCR Activation

## Overview
Photocyclic GPCR activation refers to the ability of a G protein-coupled receptor to repeatedly activate G proteins in response to successive light stimuli without chromophore release, functioning in a cyclical manner analogous to [Microbial Rhodopsins](/xray-mp-wiki/concepts/microbial-rhodopsins/). In contrast, native vertebrate rhodopsin undergoes a one-way photobleaching reaction: [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) isomerizes to all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/), activates transducin (Gt), and then releases the chromophore. Photocyclic behavior has been demonstrated in [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) regenerated with a synthetic six-carbon-ring [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore (6mr), which undergoes an atypical 11-cis to 11,13-dicis isomerization upon light absorption. The 11,13-dicis isomer thermally reisomerizes to the 11-cis configuration on a slow timescale (hours), enabling repeated cycles of Gt activation. This makes photocyclic GPCRs candidates for optogenetic applications requiring reversible control over effector ligands.


## Mechanism/Details
In native vertebrate rhodopsin, absorption of a photon triggers cis-trans isomerization
of [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) to all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/), causing a conformational change in the [OPSIN](/xray-mp-wiki/proteins/gpcr/opsin/)
moiety to form the active Meta-II state. Meta-II formation involves deprotonation of
the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base, disruption of the intramolecular hydrogen-bonding network,
and opening of the cytoplasmic side to enable Gt binding. After activation, all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/)
is released and must be replaced by fresh [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) for another activation cycle.

In Rh6mr (rhodopsin bound to a six-carbon-ring [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) analog with a locked C11=C12
cis double bond), light absorption drives an atypical 11-cis to 11,13-dicis isomerization
of the chromophore. This isomerization occurs at the C13=C14 double bond rather than
C11=C12, which is locked in the cis conformation by the six-membered ring. The 11,13-dicis
photoproduct induces a Meta-II-like conformational change that activates Gt with an
activation energy (Ea = 11.1 kcal/mol) similar to native Rh (Ea = 9.6 kcal/mol).

Unlike native Rh, Rh6mr retains its chromophore after activation, with the Schiff base
remaining protonated and stabilized by interaction with Glu181. The 11,13-dicis isomer
slowly thermally reisomerizes to 11-cis over 24-48 hours, restoring the inactive state.
During this period, Rh6mr's cytoplasmic side remains more open than native Rh, allowing
bulk solvent access. The reisomerization enables multiple rounds of Gt activation upon
successive light stimuli after dark recovery periods.

## Examples in Membrane Protein Work
- [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) (Rh6mr) — Rh6mr exhibits photocyclic Gt activation with a photosensitivity approximately
0.043 relative to native Rh. The 11,13-dicis photoproduct reisomerizes to 11-cis
over 24-48 hours at 20 C, and Rh6mr can repeatedly activate Gt upon subsequent
illuminations after dark recovery. The chromophore remains bound and the Schiff
base stays protonated throughout the cycle.

## Related Concepts
- [](/xray-mp-wiki/concepts/bacteriorhodopsin-photocycle/) — 
- [](/xray-mp-wiki/concepts/channelrhodopsin-photocycle/) — 
- [](/xray-mp-wiki/concepts/microbial-rhodopsins/) — 

## Cross-References
- [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) — Bovine rhodopsin is the protein in which photocyclic GPCR activation was demonstrated
- [Microbial Rhodopsins](/xray-mp-wiki/concepts/microbial-rhodopsins/) — Related biological concept
- [OPSIN](/xray-mp-wiki/proteins/gpcr/opsin/) — Related protein structure
- [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Related ligand or cofactor
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Related ligand or cofactor
