---
title: Influenza A M2 Proton Channel
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein]
sources: [doi/10.1038##nature06528, doi/10.1021##jacs.8b06741, doi/10.1021##jacs.9b02196, doi/10.1073##pnas.1007071107, doi/10.1073##pnas.1518493112, doi/10.1073##pnas.1705624114, doi/10.1021##acs.biochem.9b00971]
verified: false
---

# Influenza A M2 Proton Channel

## Overview

The M2 proton channel of influenza A virus is a homotetrameric ion channel that transports protons from the low-pH environment of the endosome into the viral interior during viral entry. The transmembrane (TM) domain (residues 23-46 in full-length M2, residues 22-46 in crystallized constructs) is sufficient for selective proton transport and forms the target of the adamantyl-amine class of antiviral drugs including [Amantadine](/xray-mp-wiki/reagents/ligands/amantadine/) and [Rimantadine](/xray-mp-wiki/reagents/ligands/rimantadine/). The channel adopts Inward_closed and Inward_open conformational states that cycle during proton transport, with His37 serving as a selectivity filter and proton shuttle.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature06528 | 3C9J | 3.50 | P 21 21 2 | M2TM G34A mutant (residues 22-46) with amantadine at pH 5.3 | amantadine |
| doi/10.1038##nature06528 | 3BKD | 2.00 | P21 | M2TM I33-SeMet (residues 22-46) at pH 7.3 |  |
| doi/10.1021##jacs.8b06741 | 6BKK | 2.00 | P21 | M2 TM domain (residues 22-46), Inward_closed conformation | amantadine |
| doi/10.1021##jacs.8b06741 | 6BKL | 2.00 | P21 | M2 TM domain (residues 22-46), Inward_closed conformation | rimantadine |
| doi/10.1021##jacs.8b06741 | 6BMZ | 2.63 | P21 | M2 TM domain (residues 22-46), Inward_closed conformation | spiro-adamantyl amine |
| doi/10.1021##jacs.8b06741 | 5BOC | 2.25 | P21 | M2 TM domain (residues 22-46), Inward_open conformation | rimantadine |
| doi/10.1021##jacs.9b02196 | 6MJH | 2.20 | P21 | M2 TM domain (residues 22-46), S31N mutant, Inward_open conformation |  |
| doi/10.1021##jacs.9b02196 | 6MJH | 2.20 | P21 | M2 TM domain (residues 22-46), S31N mutant, Inward_closed conformation |  |
| doi/10.1073##pnas.1007071107 | 3LBW | 1.65 | — | M2TM' (residues 22-46), crystallized at pH 6.5 (intermediate protonation state) |  |
| doi/10.1073##pnas.1518493112 | 4QK7 | 1.10 | I4 | M2TM (residues 22-46) from influenza A/Udorn/307/1972, pH 8.0, cryogenic (100 K) |  |
| doi/10.1073##pnas.1518493112 | 4QKC | 1.10 | I4 | M2TM (residues 22-46) from influenza A/Udorn/307/1972, pH 5.5, cryogenic (100 K) |  |
| doi/10.1073##pnas.1518493112 | 4QKL | 1.71 | I4 | M2TM (residues 22-46) from influenza A/Udorn/307/1972, pH 8.0, room temperature (273 K) |  |
| doi/10.1073##pnas.1518493112 | 4QKM | 1.44 | I4 | M2TM (residues 22-46) from influenza A/Udorn/307/1972, pH 5.5, room temperature (273 K) |  |
| doi/10.1073##pnas.1705624114 | 5JOO | 1.40 | I4 | M2TM (residues 22-46) from influenza A/Udorn/307/1972, pH 5.5, room temperature XFEL |  |
| doi/10.1073##pnas.1705624114 | 5UM1 | 1.40 | I4 | M2TM (residues 22-46) from influenza A/Udorn/307/1972, pH 6.5, room temperature XFEL |  |
| doi/10.1073##pnas.1705624114 | 5TTC | 1.40 | I4 | M2TM (residues 22-46) from influenza A/Udorn/307/1972, pH 8.0, room temperature XFEL |  |
| doi/10.1021##acs.biochem.9b00971 | 6NV1 | 2.50 | P21 | M2(22-46) V27A mutant in complex with spiro-adamantyl amine, Inward_closed conformation | spiro-adamantyl amine |
| doi/10.1021##acs.biochem.9b00971 | 6OUG | 3.00 | P21 | M2(21-61) V27A mutant in complex with spiro-adamantyl amine, Inward_closed conformation | spiro-adamantyl amine |

## Expression and Purification

- **Expression system**: Chemically synthesized peptide (M2TM' residues 22-46); also recombinant A/M2-G34A and A/M2-G34V expressed in Xenopus oocytes for electrophysiology


### Purification Workflow

*Source: doi/10.1073##pnas.1007071107*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Peptide synthesis | Chemical synthesis | — |  | M2TM' (residues 22-46) and M2TM were chemically synthesized |

### Purification Workflow

*Source: doi/10.1073##pnas.1518493112*

- **Expression system**: Chemically synthesized
- **Expression construct**: M2(22-46) SSDPLVVAASIGILHLILWILDRL-NH3 from influenza A/Udorn/307/1972 (MW 2682.268 Da)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Peptide synthesis | Fmoc chemistry, manually at high temperature | — |  | Peptide sequence from influenza A/Udorn/307/1972 |
| Purification | Reverse-phase HPLC | — |  | Purity confirmed by analytical HPLC and mass spectrometry |
| Storage | Dissolved in ethanol | — |  | Stored at -80 C |


## Crystallization

### doi/10.1073##pnas.1007071107

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | M2TM' (residues 22-46) with bromobenzoyl group |
| Reservoir | pH 6.5 buffer |
| Temperature | not specified |
| Cryoprotection | not specified |
| Notes | 1.65 A resolution structure of M2TM' crystallized at pH 6.5; bromobenzoyl group used for Br-SAD phasing; structure represents intermediate protonation state between pH 7.5 NMR and pH 5.3 X-ray structures |

### doi/10.1073##pnas.1518493112

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | M2TM (residues 22-46) in ethanol |
| Lipid | Monoolein |
| Protein-to-lipid ratio | not specified |
| Temperature | 10 C (cryo crystals), 20 C (room temp crystals) |
| Growth time | 2-4 weeks |
| Notes | LCP prepared with modifications to Caffrey and Cherezov protocol; crystals grown in 96-well plastic sandwich plates; cryo crystals grown at 10 C and harvested into LN2; RT crystals grown at 20 C and transported to beamline at ambient temp; crystals 20-120 um; data collected at ALS beamline 8.3.1 with ADSC Q315r CCD detector |

### doi/10.1021##acs.biochem.9b00971

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | M2(22-46) V27A or M2(21-61) V27A dissolved in ethanol with spiro-adamantyl amine, mixed with MNG-3-C8 detergent |
| Lipid | Monoolein |
| Temperature | 20 C |
| Notes | Peptides synthesized by Fmoc chemistry, purified by reverse-phase HPLC. Peptides dissolved in ethanol and added to dry monoolein powder with spiro-adamantyl amine. Lyophilized overnight, then cubic phase formed by melting at 40 C with MNG-3-C8 detergent. Data collected at ALS beamline 8.3.1. |


## Biological / Functional Insights

### Proton conduction mechanism through His-box and water clusters

The 1.65 A X-ray structure of M2TM' at pH 6.5 reveals a pore lined by five layers of sidechains (Val27, Ala30, Ser31, His37, Trp41, Asp44/Arg45) and three intercalated water clusters (entry cluster of 6 waters, His37/Trp41 bridging cluster of 2 waters, and exit cluster of 4 waters). The His37 residues form a box-like structure (His-box) with imidazoles connected via structured water networks rather than direct H-bonds. Protons conducted through the channel need not be localized to a single His37 imidazole, but may be delocalized over the entire His-box and associated water clusters, unifying discrete site versus continuum conduction models.

### pH-dependent conformational transitions and gating

Comparison of the pH 6.5 structure (intermediate form) with the pH 7.5-8 NMR structure (neutral form) and pH 5.3 X-ray structure (low pH form) reveals pH-dependent conformational changes. The structure at pH 6.5 shows hybrid features: the C-terminal portion matches the NMR structure angle, while the N-terminal portion resembles the low pH X-ray structure, with a 12 degree bend at Ala34. As pH decreases, the Val27 valve constricts and the Trp-basket opens. A conserved Gly (Ala34 in M2TM', Gly34 in WT) acts as a hinge, similar to gating transitions in K+ and NaK channels.

### G34A mutation and water density disruption

MD simulations comparing WT M2, G34A (M2TM'), and nonfunctional G34V show correlation between water density in the channel leading to the His-box and proton conduction. G34V introduces a 5 A gap in water density that blocks conduction, while G34A shows intermediate behavior with reduced but detectable activity (2.5-fold lower than WT). Both WT and G34A are equivalently selective for protons. This demonstrates that efficient proton conduction requires continuous water density throughout the pore.

### Ordered water wires spanning the M2 pore at cryogenic temperatures

Cryogenic structures at 1.10 A resolution at pH 8.0 (4QK7) and pH 5.5 (4QKC) reveal multiple continuous paths of water molecules stretching ~17 A from Val27 to His37. The water wires form highly degenerate hydrogen-bonded networks with multiple branching points, providing multiple pathways for proton conduction via the Grotthuss mechanism. Some water molecules occupy full occupancy sites, while others alternate between two closely adjoining positions summing to full occupancy. These structures are among the highest-resolution membrane protein structures determined (<1.2 A).

### Fluid water wires at room temperature

Room temperature structures at 273 K (4QKL at pH 8.0, 1.71 A; 4QKM at pH 5.5, 1.44 A) show fewer ordered water molecules compared to cryogenic structures and no longer form continuous water wires. At low pH, the waters appear fluid-like and do not form ordered networks at all, indicating that water becomes increasingly fluid with increasing temperature and decreasing pH, despite the higher electrostatic field.

### XFEL structures reveal room temperature water networks and avoid cryo/radiation artifacts

XFEL structures collected at room temperature at SACLA at three pH conditions (5.5, 6.5, 8.0) to 1.4 A resolution avoid artifacts from both cryocooling and radiation damage. At pH 5.5, a continuous hydrogen-bonded water network spans from Ser31 to the gating His37 residues, consistent with a Grotthuss proton transport mechanism. Two alternate-occupancy water networks (A and B) were identified; only network A provides a continuous proton wire. Graph theory analysis identified 11 unique hydrogen-bonding networks, with only 2 forming continuous water wires. At pH 6.5, the water network spans roughly half the channel. At pH 8.0, no vertical hydrogen bonds connect the three water layers. Solvent ordering decreases at higher pH, correlating with decreased proton conduction.

### Directional H-bond switching as basis for asymmetric proton conduction

MD simulations reveal that the polarity of H-bonds between water molecules becomes increasingly aligned with the channel axis as the His37 tetrad becomes more protonated. At low pH (3+ and 4+ charge states), H-bonds are highly directional: oriented outward in the extraviral half of the pore and inward in the intraviral half, with polarity switching at His37 acting as a "rectifier." At high pH (0 and 1+ states), water molecules form "loopback circuits" with no preferred orientation. The switch between configurations occurs at the 2+ charge state (most populated at neutral pH). This collective switch of hydrogen bond orientations contributes to the directionality of proton flux, explaining M2's asymmetric conductance (conducts protons inward when outside pH is low, but not outward when pH gradient is reversed).

### Mechanism of V27A adamantane resistance

The Val27 to Ala mutation at the N-terminus of M2 widens the channel pore at the adamantane binding site from 0.7 A (Val27 in WT) to 3.0 A (Ala27 in V27A mutant). This removes hydrophobic interactions between Val27 side chains and the adamantyl group of amantadine/rimantadine, rendering these drugs ineffective. The widened pore also increases water and hydronium access, explaining the increased proton conductance rate of the V27A mutant channel.

### Spiro-adamantyl amine shifts binding position to accommodate V27A mutation

The spiro-adamantyl amine inhibitor adapts to the wider V27A pore by shifting its adamantyl group upward (toward the N-terminus) by approximately 2 A relative to its position in the WT channel. The ammonium group remains at the same position as amantadine's ammonium in WT (6BKK). Two ordered water layers (Ala30 carbonyl layer and Gly34 carbonyl layer) form between the inhibitor ammonium and the gating His37 residues, compared to one water layer in the WT-spiro-adamantyl amine complex. This dual water layer arrangement interrupts proton-conducting water networks while accommodating the wider pore. Spiro-adamantyl amine inhibits both WT (IC50 18.7 uM) and V27A (IC50 0.3 uM) channels.

### Cytosolic helix packing and potential proton exit site

The 3.0 A structure of M2(21-61) V27A (6OUG) reveals that residues Asp44, Arg45, and Phe48 face the center of the channel pore at the C-terminus. Arg45 side chains are well-positioned to interact with protons exiting the M2 channel after passing through the His37 gate. Phe48 stabilizes Arg45 via cation-pi interactions. The C-terminal channel packing is tighter in the longer construct (minimum pore diameter 1.0 A at Arg45) compared to the TM-only construct (2.8 A at Arg45).


## Cross-References

- [Amantadine](/xray-mp-wiki/reagents/ligands/amantadine/) — Adamantyl-amine inhibitor targeting M2 proton channel
- [Rimantadine](/xray-mp-wiki/reagents/ligands/rimantadine/) — Adamantyl-amine inhibitor targeting M2 proton channel
- [M2 Proton Channel Conformational Equilibrium](/xray-mp-wiki/concepts/transport-mechanisms/m2-conformational-equilibrium/) — Conformational dynamics between Inward_open and Inward_closed states
- [Influenza A M2 Proton Channel S31N Mutant](/xray-mp-wiki/proteins/other-ion-channels/influenza-a-m2-proton-channel-s31n/) — Drug resistance mutant of M2
- [Spiro-Adamantyl Amine](/xray-mp-wiki/reagents/ligands/spiro-adamantyl-amine/) — Inhibitor that binds both WT and V27A mutant M2 channels
- [Proton Wire](/xray-mp-wiki/concepts/transport-mechanisms/proton-wire/) — Water networks in the M2 pore mediate proton conduction via Grotthuss mechanism
