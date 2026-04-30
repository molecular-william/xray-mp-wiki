---
title: KirBac Potassium Channel
created: 2026-04-27
updated: 2026-04-28
type: protein
tags: [ion-channel, channel, membrane-protein]
sources: [doi/10.1016##J.CELL.2010.05.003]

category: proteins
layout: default
---



# KirBac Potassium Channel

## Overview

KirBac is a family of prokaryotic inwardly rectifying potassium (Kir) channels that serve as structural and functional models for eukaryotic Kir channels. Inward rectifiers control the resting membrane potential by allowing K⁺ influx but not efflux — a property conferred by intracellular polyamine block. KirBac channels are encoded by bacteria such as *Magnetospirillum magnetotactium* (KirBac1.1, KirBac3.1) and have been extensively crystallized to reveal gating mechanisms.

## Structure

### KirBac1.1 (PDB: 1P7B)

- **Resolution**: 3.7 Å (re-refined from original)
- **Space group**: I222
- **Architecture**: Homotetramer, each subunit has two transmembrane helices (inner and outer), a pore helix, and an extended cytoplasmic domain
- **Ion configuration**: Blocked (Mg²⁺ at S3/S4 site)
- **Intracellular state**: Latched (all 4 interfaces compact)
- **Selectivity filter**: Blocked configuration

### KirBac3.1 (Multiple Structures)

- **Structure I (1XL4)**: 2.6 Å, P2₁2₁2₁, Ca²⁺-blocked
- **Structure II (1XL6)**: 2.8 Å, P2₁2₁2₁, nontwist, conducting
- **Structures III–VII**: 3.1–4.2 Å, various space groups, twist (stalled)
- **Structure VIII**: 60% nontwist, 40% twist, axial spermine in pore
- **Structure XI**: 100% nontwist, conducting, anisotropic mobility

### Architecture (All KirBac)

- **Selectivity filter**: Conserved TVGYG motif with ion binding sites S1–S4
- **Oligomerization**: Homotetramer
- **Subunit topology**: Each subunit has two transmembrane helices (inner and outer), a pore helix, and an extended cytoplasmic domain

## Gating Mechanism

This study revealed interdependent gates in the Kir conduction pathway:

1. **Selectivity filter gating**: Ion configuration in the filter (S1–S4 sites) is coupled to global conformational changes. The "twist" conformation (S1, S3, S4 occupied) is stalled/non-conducting. The "nontwist" conformation (S1, S2, S3, S4 occupied or Mg²⁺/Ca²⁺/Ba²⁺ blocked) represents conducting or blocked states.

2. **Intracellular domain reorientation**: The cytoplasmic assembly rotates relative to the pore by ~23° between open and closed states. This rotation is mediated by a "molecular pulley" system involving N and C termini interweaving between subunits.

3. **Latched/unlatched interfaces**: Subunit interfaces alternate between "latched" (compact, closed vestibule) and "unlatched" (dilated iris-like opening) arrangements. Full unlatching of all four interfaces is concomitant with activation.

4. **Slide helix coupling**: Conformational adjustments of slide helices, achieved by rotation of the cytoplasmic assembly, are directly correlated to ion configuration in the selectivity filter.

## Polyamine Block Mechanism

- **Intracellular binding sites**: Two [spermine](/xray-mp-wiki/reagents/ligands/spermine/)-binding pockets identified at latched subunit interfaces. These pockets are preformed and superimpose closely with unliganded structures.
- **Rectification**: At resting potential, latched interfaces concentrate polyamines. Upon unlatching (activation), the intracellular vestibule dilates by ~4.5 Å, disrupting binding sites and releasing polyamines into the conduction path.
- **Deep pore block**: Extended [spermine](/xray-mp-wiki/reagents/ligands/spermine/) molecules protrude from intracellular sites into the permeation pathway, forming cation-π interactions with Tyr132 at the bundle crossing.

## Ion Configurations

| Structure | Status | Ion Sites | Block Ion |
|