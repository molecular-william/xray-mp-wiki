---
title: V-Type Na+-ATPase Rotor Ring (NtpK10) from Enterococcus hirae
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein]
sources: [doi/10.1126##science.1110064]
verified: false
---

# V-Type Na+-ATPase Rotor Ring (NtpK10) from Enterococcus hirae

## Overview

The membrane rotor ring from the vacuolar-type (V-type) sodium ion-pumping ATPase (Na+-ATPase) from Enterococcus hirae consists of 10 NtpK subunits arranged with 10-fold symmetry. Each NtpK subunit has four transmembrane alpha helices (H0-H4) and is a homolog of both the 16-kDa and 8-kDa proteolipids found in other V-ATPases and F-ATPases, respectively. Sodium ions are bound between helices 2 and 4 at a site buried deeply in the membrane that includes the essential residue Glu-139. The structure supports a two-half-channel ion translocation model in which the binding site is connected to the membrane surface by two half-channels in subunit NtpI against which the ring rotates. Bound phospholipid molecules (DPPG and DPG) are observed on the inner surface of the ring, forming an internal lipid bilayer, while detergent molecules (dodecyl- and ) are associated with the external surface.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1110064 | 2bl2 |  |  | NtpK10 rotor ring (10 NtpK subunits) | Na+ |

## Expression and Purification

- **Expression system**: Enterococcus hirae (native)
- **Construct**: Native NtpK ring
- **Notes**: K rings were isolated from E. hirae membranes as described previously

### Purification Workflow

- **Expression system**: Enterococcus hirae (native)
- **Expression construct**: Native NtpK ring

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane isolation | Cell lysis and membrane fractionation |  |  | E. hirae membranes isolated |
| K ring purification | Chromatography |  | ,  | K rings isolated by chromatography in detergent solution |


## Crystallization

### doi/10.1126##science.1110064

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified NtpK10 ring in detergent solution |
| Reservoir | 100 mM sodium  |
| Notes | Crystallized in presence of dodecyl- and . Both detergent types present in crystallization. |


## Biological / Functional Insights

### Sodium ion binding site

Each NtpK subunit binds a single Na+ ion coordinated by five oxygen atoms 2.2-2.3 A from side chains of Thr-64, Gln-65, Gln-110, and Glu-139, and the main-chain carbonyl of Leu-61. Residues from helices H2, H3, and H4 contribute to the binding pocket. The bound Na+ is occluded by the side chain of Glu-139, whose gamma-carboxylate is stabilized by hydrogen bonds with Gln-110, Tyr-68, and Thr-64. Access to the bound ion requires changing torsion angles of the Glu-139 side chain.

### Two-half-channel translocation mechanism

The Na+ binding site is located near the middle of the lipid bilayer. No intrinsic K-ring channel leads to the site. The structure supports a two-half-channel model where clockwise rotation (viewed from cytoplasm) brings an occupied Na+ binding site into the K-ring-subunit-I interface. Proximity to NtpI-Arg-573 (essential for ion transport) creates electrostatic interaction with Glu-139, disrupting the hydrogen-bond network and releasing Na+ into the periplasm via a half-channel in NtpI. Further rotation brings the site to a second half-channel for binding a cytoplasmic Na+ ion.

### Symmetry mismatch

The 10-fold symmetry of the K ring differs from the 6-fold symmetry previously assumed for V-type rings based on electron microscopy and chemical analysis. This is reminiscent of the history of F-ATPase c-ring stoichiometries, where 12-fold was assumed until structural data revealed 10-, 11-, and 14-fold symmetries. The range of stoichiometries suggests different energetic costs for  synthesis or ion pumping across species.


## Cross-References

- [V1-ATPase from Enterococcus hirae (EhV1)](/xray-mp-wiki/proteins/pumps-atpases/enterococcus-hirae-v1-atpase/) — V0 domain counterpart; the K ring is part of the V0 membrane domain
- [F-Type Na+-ATPase c11 Rotor Ring from Ilyobacter tartaricus](/xray-mp-wiki/proteins/pumps-atpases/ilyobacter-tartaricus-c-subunit/) — F-ATPase rotor ring from related Na+-translocating ATP synthase
- [F1-ATPase Rotary Catalytic Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/) — Rotary mechanism shared between V- and F-ATPases
- [UDM](/xray-mp-wiki/reagents/undecylmaltoside/) — Referenced in ehirae-v-atpase-k-ring text
- [Acetate](/xray-mp-wiki/reagents/buffers/acetate/) — Referenced in ehirae-v-atpase-k-ring text
- [DDM](/xray-mp-wiki/reagents/dodecylmaltoside/) — Referenced in ehirae-v-atpase-k-ring text
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Referenced in ehirae-v-atpase-k-ring text
