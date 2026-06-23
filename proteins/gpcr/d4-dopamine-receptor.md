---
title: "D4 Dopamine Receptor (DRD4)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aan5468]
verified: false
---

# D4 Dopamine Receptor (DRD4)

## Overview

The human D4 [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor (DRD4) is a class A G protein-coupled receptor
(GPCR) belonging to the D2-like [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor subfamily (D2, D3, D4). DRD4
is implicated in attention deficit disorder, metastatic progression, and penile
erection, making DRD4-selective drugs therapeutically promising. The crystal
structures of DRD4 in its inactive state bound to the antipsychotic drug
[Nemonapride](/xray-mp-wiki/reagents/ligands/nemonapride/) were determined at resolutions up to 1.95 Å using a [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion
strategy. The structures reveal a full network of water molecules and ions,
including the first direct structural evidence for a sodium ion in its allosteric
binding site in a [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor. The extended binding pocket (EBP) defined
by non-conserved residues V87^2.57, L90^2.60, F91^2.61, and L111^3.28
provides an atomic-resolution model for DRD4 ligand selectivity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aan5468 | 5WIU | 1.95 | — | DRD4-BRIL fusion (residues 228-336 of ICL3 replaced with thermostabilized apocytochrome b562RIL), bound to [Nemonapride](/xray-mp-wiki/reagents/ligands/nemonapride/), 200 mM Na+ added | [Nemonapride](/xray-mp-wiki/reagents/ligands/nemonapride/), Na+ |
| doi/10.1126##science.aan5468 | 5WIV | 2.15 | — | DRD4-BRIL fusion (residues 228-336 of ICL3 replaced with [Bril](/xray-mp-wiki/reagents/protein-tags/bril/)), bound to [Nemonapride](/xray-mp-wiki/reagents/ligands/nemonapride/), no added Na+ | [Nemonapride](/xray-mp-wiki/reagents/ligands/nemonapride/) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells via baculovirus
- **Construct**: DRD4-BRIL — residues 228-336 of ICL3 replaced with thermostabilized apocytochrome b562RIL ([Bril](/xray-mp-wiki/reagents/protein-tags/bril/))
- **Notes**: DRD4-BRIL has binding affinity for 3H-N-methylspiperone similar to native DRD4. [Nemonapride](/xray-mp-wiki/reagents/ligands/nemonapride/) added during purification to form complex.

### Purification Workflow

- **Expression system**: Sf9 insect cells, baculovirus
- **Expression construct**: DRD4-BRIL (ICL3 replaced with BRIL)
- **Tag info**: BRIL fusion (no affinity tag mentioned for DRD4 portion)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus infection | — |  | Sf9 cells infected with recombinant baculovirus encoding DRD4-BRIL construct |
| Complex formation | Ligand addition | — |  | [Nemonapride](/xray-mp-wiki/reagents/ligands/nemonapride/) added during purification to stabilize the receptor-ligand complex |
| Purification | Affinity chromatography | — |  | Purification details in supplementary materials; DRD4/nemonapride complex purified to homogeneity |

**Final sample**: DRD4/nemonapride complex in crystallization buffer


## Crystallization

### doi/10.1126##science.aan5468

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Notes | Crystals grown in presence and absence of 200 mM added sodium. DRD4/nemonapride complex crystals diffracted to 1.95 Å resolution. Data collected at GM/CA@APS, Advanced Photon Source. |


## Biological / Functional Insights

### First dopamine receptor structures at atomic resolution

The D4 [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor structures at 1.95 Å and 2.15 Å resolution are the highest-resolution [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor structures reported. The unusually high resolution enabled visualization of a full network of water molecules and ions, providing unprecedented detail of [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor architecture.

### Sodium ion allosteric modulation

The structures provide the first direct structural evidence for a sodium ion in its allosteric binding site in a [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor. Sodium forms a salt bridge with D80^2.50 and polar interactions with S122^3.39 and two water molecules. DRD4 has lower sodium affinity than δ-OR, μ-OR or A2AAR. Lowering [Na+] potentiates DRD4 constitutive activity in a nemonapride-sensitive fashion. MD simulations show the sodium-free pocket fills with water and does not collapse.

### Mechanism of constitutive signaling control

In DRD4, the absence of a hydrogen bond between position 7.35 and 6.55 (V430^7.35 cannot hydrogen bond with H414^6.55) leads to closer proximity of TM V and TM VI, explaining the more inactive DRD4/nemonapride structure compared to DRD3. A V430^7.35Y mutation in DRD4 recapitulates the DRD3 inter-helical hydrogen bond and increases constitutive activity. The reverse mutation in DRD3 (Y365^7.35V) diminishes constitutive activity. Thus, the 7.35-6.55 hydrogen bond potentiates DRD3 constitutive activity while its absence in DRD4 suppresses it.

### Extended binding pocket (EBP) for DRD4 selectivity

The high-resolution structure revealed an extended binding pocket (EBP) bordered by non-conserved residues V87^2.57, L90^2.60, F91^2.61, and L111^3.28. In DRD3, the corresponding residues are V86^2.61 and F106^3.28, which create steric clashes with DRD4-selective ligands. A F^2.61V/L^3.28F double substitution in DRD4 attenuates affinities of DRD4-selective compounds, while the reverse double mutant in [DRD2](/xray-mp-wiki/proteins/gpcr/drd2/) (V^2.61F/F^3.28L) increases affinity for DRD4-selective ligands, providing an atomic resolution model of DRD4 ligand selectivity.

### Structure-based discovery of DRD4-selective agonists

Using the 1.95 Å DRD4 structure, a virtual screen of over 600,000 cationic lead-like molecules from ZINC was performed. Hit compound 9 was optimized through 75 docked analogs to yield 9-6 and 9-11, which were DRD4-selective partial agonists. Further optimization produced 9-6-23 and 9-6-24 with Ki of 30 [NM](/xray-mp-wiki/reagents/detergents/nm/) and 3 [NM](/xray-mp-wiki/reagents/detergents/nm/) at DRD4, respectively, with >3,300-fold selectivity over [DRD2](/xray-mp-wiki/proteins/gpcr/drd2/) and DRD3. 9-6-24 (UCSF924) is a DRD4 partial agonist with 7.4-fold bias toward arrestin over Gαi/o signaling and no substantial agonist activity against 320 non-olfactory GPCRs.


## Cross-References

- [Human Dopamine D3 Receptor (D3R)](/xray-mp-wiki/proteins/gpcr/human-dopamine-d3-receptor/) — DRD3 is the closest structural homolog; comparison of EBP and constitutive activity mechanisms
- [Sodium Ion Allosteric Modulation in GPCRs](/xray-mp-wiki/concepts/signaling-receptors/sodium-allosteric-modulation/) — First direct structural evidence for sodium allosteric site in a dopamine receptor
- [Biased Agonism in G Protein-Coupled Receptors](/xray-mp-wiki/concepts/signaling-receptors/biased-agonism/) — Compound 9-6-24 shows 7.4-fold arrestin bias over Gαi/o signaling
- [DRD2 Extended Binding Pocket (DRD2-EBP)](/xray-mp-wiki/concepts/structural-mechanisms/drd2-extended-binding-pocket/) — Closely related concept — DRD4 EBP is the DRD4-specific analog driving subtype selectivity
- [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) — Referenced in context related to Dopamine
- [Nemonapride](/xray-mp-wiki/reagents/ligands/nemonapride/) — Referenced in context related to Nemonapride
- [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) — Referenced in context related to Bril
- [DRD2](/xray-mp-wiki/proteins/gpcr/drd2/) — Referenced in context related to DRD2
- [NM](/xray-mp-wiki/reagents/detergents/nm/) — Referenced in context related to NM
