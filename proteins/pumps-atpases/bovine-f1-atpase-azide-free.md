---
title: Bovine F1-ATPase (azide-free ground state)
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.M700203200]
verified: false
---

# Bovine F1-ATPase (azide-free ground state)

## Overview

Bovine F1-ATPase is the catalytic domain of the mitochondrial F1Fo-ATP synthase. This structure of the azide-free form was determined at 1.9 A resolution from crystals grown in the presence of [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/) and [ADP](/xray-mp-wiki/reagents/ligands/adp/), but without azide. Unlike the azide-inhibited structure where the beta-DP subunit contains [ADP](/xray-mp-wiki/reagents/ligands/adp/) and azide, in this ground state structure the beta-DP and beta-TP subunits both contain [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), and the beta-E subunit is empty. The structure reveals that the beta-DP catalytic site is poised for catalysis, with the nucleophilic water molecule positioned for in-line attack on the gamma-phosphate. The alpha-Arg-373 (arginine finger) residue in the beta-DP subunit moves 1 A toward the gamma-phosphate compared to the beta-TP site, positioning it for optimal catalysis. This structure represents a ground state intermediate in the active catalytic cycle of [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1074##jbc.M700203200 | not stated in raw paper | 1.9 | P2_1_2_1_2_1 | Bovine mitochondrial F1-ATPase (alpha3beta3gamma subcomplex) | [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), [ADP](/xray-mp-wiki/reagents/ligands/adp/), Mg2+ |

## Expression and Purification

- **Expression system**: Bovine heart mitochondria (native source)
- **Construct**: Native F1-ATPase purified from bovine heart mitochondria

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification of F1-ATPase from bovine heart mitochondria | Standard mitochondrial F1-ATPase purification protocol with HiLoad 26/60 Superdex 200pg column | — |  | Sephacryl S-300 column replaced by HiLoad 26/60 Superdex 200pg. 5 mM 2-mercaptoethanol not included in buffer. |


## Crystallization

### doi/10.1074##jbc.M700203200

| Parameter | Value |
|---|---|
| Method | Microdialysis |
| Protein sample | 5 mg/ml F1-ATPase in 100 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.2, 400 mM NaCl, 4 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 2 mM [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), 40 uM [ADP](/xray-mp-wiki/reagents/ligands/adp/), 0.004% [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/), 14% [Peg](/xray-mp-wiki/reagents/additives/peg/) 6000 in D2O |
| Reservoir | 50 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.2, 200 mM NaCl, 20 mM MgSO4, 250 uM [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), 5 uM [ADP](/xray-mp-wiki/reagents/ligands/adp/), 0.004% [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/), 10-12.5% [Peg](/xray-mp-wiki/reagents/additives/peg/) 6000 |
| Temperature | 4 |
| Growth time | 4 weeks |
| Cryoprotection | Crystals dehydrated in humidity gradient 99-94%, coated in perfluoropolyether oil, flash-frozen in liquid nitrogen |
| Notes | Crystals grown in microdialysis buttons (50 ul) with SpectraPor 3500 MWCO membranes. Dehydration using free mounting system improved diffraction. |


## Biological / Functional Insights

### Both beta-DP and beta-TP sites bind AMP-PNP in the azide-free state

In the azide-free structure, the nucleotide binding sites in both beta-DP and beta-TP subunits are occupied by [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), in contrast to the azide-inhibited structure where beta-DP binds [ADP](/xray-mp-wiki/reagents/ligands/adp/) and azide. This indicates that the azide-bound structure represents the ADP-inhibited state, while the azide-free structure represents a ground state intermediate in the active catalytic cycle of [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis.

### alpha-Arg-373 movement in beta-DP positions the nucleophilic water

Superimposition of the P-loop residues shows that the guanidinium group of alpha-Arg-373 moves approximately 1 A toward the gamma-phosphate of [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/) in the beta-DP subunit compared to the beta-TP subunit. This movement positions the nucleophilic water molecule for in-line attack on the gamma-phosphate. The water molecule moves 0.7 A closer to the gamma-phosphate in beta-DP than in beta-TP, consistent with beta-DP being the catalytically active site.

### alpha-E-Arg-373 has dual conformations in the empty catalytic site

The high resolution (1.9 A) electron density map reveals that alpha-Arg-373 in the beta-E (empty) catalytic site has two conformations at approximately 50% occupancy each. One conformation is oriented away from the catalytic site, while the other is oriented toward it. This suggests the side chain alternates between conformations and adopts the inward position when phosphate binds.


## Cross-References

- [Bovine F1-ATPase (azide-inhibited form)](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — Related azide-inhibited structure of the same enzyme; comparison reveals ADP-inhibited vs ground state
- [F1-ATPase Rotary Catalytic Mechanism](/xray-mp-wiki/concepts/f1-atpase-rotary-mechanism/) — This structure provides the ground state intermediate of the catalytic cycle
- [Rotary ATPase Mechanism](/xray-mp-wiki/concepts/rotary-atpase-mechanism/) — Structural basis for the rotary catalytic mechanism of F-type ATPases
- [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/) — Referenced in the context of Amp Pnp
- [ADP](/xray-mp-wiki/reagents/ligands/adp/) — Referenced in the context of ADP
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Referenced in the context of ATP
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in the context of Tris Hcl
- [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Referenced in the context of Mgcl2
- [Peg](/xray-mp-wiki/reagents/additives/peg/) — Referenced in the context of Peg
- [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/) — Referenced in the context of Pmsf
