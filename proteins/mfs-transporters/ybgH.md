---
title: "E. coli YbgH Peptide Transporter"
created: 2026-05-28
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1016##j.str.2014.06.008]
verified: false
---

# E. coli YbgH Peptide Transporter

## Overview

YbgH (also known as DtpD) is a proton-dependent oligopeptide transporter (POT) from
Escherichia coli. It belongs to the POT family, a subfamily of the major facilitator
superfamily (MFS) of secondary active transporters. YbgH specifically transports
di- and tripeptides with a preference for substrates bearing a C-terminal basic
residue. It couples peptide uptake to proton symport across the inner membrane.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2014.06.008 | 4Q65 | 3.4 | P21212 | YbgH residues 6-482, His6-tag at C terminus | None |

## Expression and Purification

- **Expression system**: E. coli C43 (DE3)
- **Construct**: YbgH coding sequence fused to His6 tag at C terminus, cloned in pET-28a vector
- **Notes**: Gene amplified from E. coli BL21 genomic DNA, ligated into ligation-independent
cloning-compatible pET-28a vector. Transformed into E. coli C43 (DE3) cells.
Induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at 16C for 20 hr.


### Purification Workflow

- **Expression system**: E. coli C43 (DE3)
- **Expression construct**: YbgH residues 6-482, [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) C-terminal

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | Terrific broth + 25 ug/ml [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin) | Grown at 37C to OD600 0.6, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg), shifted to 16C for 20 hr |
| Cell harvest | Centrifugation | -- | Lysis buffer | 4000 x g for 30 min |
| Cell lysis | Sonication | -- | Lysis buffer | -- |
| Solubilization | Detergent extraction | -- | [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Membrane fraction solubilized with detergent |
| Affinity chromatography | Ni-NTA affinity | Ni-NTA | 50 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8, 300 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) affinity purification |
| Final sample | Buffer exchange | -- | Crystallization buffer + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | -- |


## Crystallization

### doi/10.1016##j.str.2014.06.008

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Notes | Structure determined by single-wavelength anomalous dispersion (SAD) phasing.
Se-Met labeled protein used for phasing. Also tested [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury) derivative
(C9H9O2HgNaS). Type I membrane crystals with TM helices parallel to crystallographic a axis.
 |


## Biological / Functional Insights

### Glu21 is the essential protonation site

Glu21 (first residue of motif 1) is the only conserved proton-titratable residue
located in the central cavity among POTs. Mutations E21Q and E21A abolished
transport activity, confirming its critical role. Glu21 is proposed to be the
site of protonation induced by substrate binding, driving the COut-to-CIn
conformational change via the negative-inside membrane potential.

### Motif 2 functions as a conformational switch

Motif 2 (motif A of MFS), with consensus sequence GGxxaDRxxG, is located between
TMs 2 and 3 of the N-terminal domain. The Asp70 residue within motif 2 is proposed
to form a charge-dipole interaction with the N-terminal end of TM 11, stabilizing
the COut state. Motif 2 acts as a conformational switch that senses and responds
to protonation inside the central cavity.

### HA-HB insertion regulates transport activity

Two TM helices HA and HB are inserted between the two MFS domains of YbgH. They
form a V-shaped structure in the Cin state with the opening end facing the cytosol.
Insertion of Gly residues at the closed end completely abolished activity, indicating
that rigidity of the V-shaped helix pair is essential. Mutations at positively
charged residues N-terminal to HA also lost transport activity, supporting a
regulatory role for the HA-HB insert.

### Stability balance between Cin and COut states

The balance between stabilities of the two major conformations is critical for
efficient transport. Charge-dipole interaction between Glu163 and TM8, and salt
bridge between Asp44 and Arg297, both on the periplasmic side, stabilize the
Cin state. Mutations E163A and R297A disrupted these interactions and reduced
activity, while the double mutant E163A/R297A was inactive.


## Cross-References

- [POT Family](/xray-mp-wiki/concepts/transport-mechanisms/pot-family/) — YbgH is a member of the POT family of proton-dependent oligopeptide transporters
- [Major Facilitator Superfamily](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — POT family is a subfamily of MFS transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — YbgH alternates between inward-facing and outward-facing conformations
- [Scissor-Switch Gating](/xray-mp-wiki/concepts/transport-mechanisms/scissor-switch-gating/) — POT-specific gating mechanism involving motif 2
- [PepT_So Oligopeptide Transporter](/xray-mp-wiki/proteins/mfs-transporters/pept-so/) — Another POT family member with reported crystal structure
- [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury) — Entity mentioned in text
- [TRIS](/xray-mp-wiki/reagents/buffers/tris) — Entity mentioned in text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm) — Entity mentioned in text
- [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin) — Entity mentioned in text
- [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) — Entity mentioned in text
