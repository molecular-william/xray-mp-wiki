---
title: Sodium-dependent Phosphate Transporter TmPiT from Thermotoga maritima
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.abb4024]
verified: false
---

# Sodium-dependent Phosphate Transporter TmPiT from Thermotoga maritima

## Overview

TmPiT (locus Tm0261) is a sodium-dependent phosphate transporter from the hyperthermophilic bacterium Thermotoga maritima, belonging to the inorganic phosphate transporter (PiT/SLC20) family. The structure of the TmPiT-Na/Pi complex was determined at 2.3 A resolution, revealing a dimeric architecture with each protomer containing 12 transmembrane helices organized into a transport domain (5+5 inverted repeat fold with two PD001131 repeats) and a scaffold domain. The structure captured one phosphate and three sodium ions (Pi-2Na bound at the core and Na_fore near the inner membrane boundary) in an inward occluded conformation. TmPiT exhibits high-affinity phosphate binding (Kd = 57.0 uM) and strictly sodium-dependent transport, with an elevator-like mechanism proposed for substrate translocation. The structure provides a framework for understanding disease-associated mutations in human PiT homologues (hPiT1/hPiT2/SLC20A1/SLC20A2), which are linked to primary familial brain calcification and neuropsychiatric disorders.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##sciadv.abb4024 |  | 2.3 |  | Full-length TmPiT (locus Tm0261, residues 1-420?) from T. maritima MSB8 | One phosphate ion, three sodium ions |

## Expression and Purification

- **Expression system**: Escherichia coli (inferred)
- **Construct**: Full-length TmPiT amplified from T. maritima MSB8 genomic DNA
- **Notes**: Protein expressed and purified for crystallization and functional studies

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Microsome preparation | Cell lysis and membrane fractionation | -- | Not specified + -- | Microsomes prepared from expression culture |
| Solubilization and purification | Affinity chromatography | Nickel affinity resin | 25 mM MES (pH 6.5), 3% glycerol, 120 mM NaCl + 0.03% DDM | Purified in the presence of DDM detergent; final buffer for crystallization contained 10 mM KH2PO4 |


## Crystallization

### doi/10.1126##sciadv.abb4024

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Purified TmPiT in 0.03% DDM, 10 mM KH2PO4, 25 mM MES (pH 6.5), 120 mM NaCl, 3% glycerol |
| Reservoir | 50 mM sodium citrate (pH 5.5), 10% PEG 3000 (approximate) |
| Temperature | 20 |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Data collected at 2.3 A resolution. Structure solved by molecular replacement or SAD. TmPiT forms a dimer in the asymmetric unit with subunits A and B showing different conformations at the inner gate (inward occluded for subunit A, inward open-like for subunit B). |


## Biological / Functional Insights

### Sodium-dependent phosphate binding and coordination

The TmPiT-Na/Pi complex reveals one phosphate and three sodium ions bound at distinct sites. The Pi-2Na site at the core of the transporter comprises phosphate associated with two sodium ions (Na1-Pi-Na2) through conserved aspartates D22 and D258. The phosphate is coordinated via 12 interactions with eight conserved residues: D22/TM1, D258/TM6, and six polar residues from the reentrant helical hairpins — S105/T106/T107 (HP1b) and S345/T346/T347 (HP2b). Na1 is pentacoordinated by N21, D22, V104, T347, and K314; Na2 by N257, D258, T107, I344, and a water molecule. A third sodium (Na_fore) is located near the inner membrane boundary, coordinated by T29, Q243, S247, and D327. Mutation of D22A or D258A maintains Pi binding but abolishes uptake, while D22/258A double mutant fails to bind Pi.

### Elevator-like transport mechanism

TmPiT is proposed to use a two-gated elevator-like mechanism for phosphate and sodium transport, analogous to the GltPh glutamate transporter and VcINDY dicarboxylate transporter. The transport cycle involves at least four sequential states: outward open, outward occluded, inward occluded, and inward open. The structure captures the inward occluded state. The two inverted PD001131 repeats (N-PD001131: TM1-TM2-HP1-TM3; C-PD001131: TM6-TM7-HP2-TM8) form reentrant helical hairpins HP1 and HP2 that control the inner and outer gates. Subunits A and B of the dimer reveal different inner gate conformations (closed vs. open), suggesting asymmetric functional states and possible cooperative behavior.

### Structural basis for human PiT disease mutations

The TmPiT structure informs disease-associated mutations in human PiT (hPiT1/SLC20A1 and hPiT2/SLC20A2), which cause primary familial brain calcification (PFBC) and neuropsychiatric disorders. Key correspondences include: D22 (TmPiT) → D28N (hPiT2, PFBC-linked); D258 → D506N; D327 → E575K (PFBC-linked); W378 → W626 duplication (PFBC-linked). Mutations cluster in Pi/Na-binding residues, the N- and C-PD001131 repeats, dimer interface, and scaffold domain. The D22A/D258A double mutant fails to bind Pi, and the D327Q mutant (corresponding to hPiT2 E575K) loses Pi binding entirely, explaining the disease mechanism.


## Cross-References

- [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) — TmPiT uses an elevator-like mechanism for phosphate/sodium transport
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — TmPiT operates via alternating access between outward and inward conformations
