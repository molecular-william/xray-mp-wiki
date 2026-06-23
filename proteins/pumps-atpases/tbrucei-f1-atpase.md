---
title: F1-ATPase from Trypanosoma brucei
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1720940115]
verified: false
---

# F1-ATPase from Trypanosoma brucei

## Overview

The F1-ATPase from Trypanosoma brucei is the catalytic domain of its
mitochondrial ATP synthase, a multisubunit rotary enzyme complex that
generates ATP from ADP and phosphate using proton-motive force. The
crystal structure at 3.2 A resolution revealed that, contrary to a
previous proposal based on electron cryotomography at 32.5 A resolution,
the T. brucei F1-domain has a conventional alpha3-beta3 spherical
structure with the arginine finger provided by the alpha-subunit (alphaArg-386)
in the canonical manner. The complex consists of alpha3-beta3-gamma-delta-
epsilon subunits plus three copies of the euglenozoa-specific p18 subunit
bound to the external surface of each alpha-subunit. The p18 subunit is
a pentatricopeptide repeat (PPR) protein with three PPRs and appears to
have no role in the catalytic mechanism, though it is essential for
complex assembly.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1720940115 | not stated in raw paper text | 3.2 | P2(1) | T. brucei F1-ATPase (alpha3-beta3-gamma-delta-epsilon + 3x p18) |  |

## Expression and Purification

- **Expression system**: Trypanosoma brucei (native source)
- **Construct**: Endogenous F1-ATPase purified from T. brucei mitochondria

### Purification Workflow

- **Expression system**: T. brucei (native)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Crystallization | Vapor diffusion | — | 50 mM MES pH 6.0, 0.5 mM ADP, 5% [PEG](/xray-mp-wiki/reagents/additives/peg/) 12000, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1 M MgSO4 | Cryoprotected by adding 0.1 M MgSO4, 0.5 mM ADP, 50 mM MES pH 6.0, 5% [PEG](/xray-mp-wiki/reagents/additives/peg/) 12000, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/). Harvested with MicroLoop (MiTeGen) and flash-frozen. |


## Crystallization

### doi/10.1073##pnas.1720940115

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified T. brucei F1-ATPase |
| Temperature | Not specified |
| Cryoprotection | 0.1 M MgSO4, 0.5 mM ADP, 50 mM MES pH 6.0, 5% [PEG](/xray-mp-wiki/reagents/additives/peg/) 12000, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Notes | Unit cell a=124.2 A, b=206.4 A, c=130.2 A, alpha=gamma=90 degrees, beta=104.9 degrees. Space group P2(1). Data collected at ESRF, Grenoble at 100 K with PILATUS3 2M detector at 0.966 A wavelength. |


## Biological / Functional Insights

### Conventional catalytic mechanism in T. brucei ATP synthase

The 3.2 A crystal structure of T. brucei F1-ATPase demonstrates that
the catalytic domain has a conventional alpha3-beta3 spherical structure
with the arginine finger (alphaArg-386) provided by the alpha-subunit,
refuting the proposal from 32.5 A ECT data that p18 provides this
essential catalytic residue. The structure confirms the conservation
of ATP synthase catalytic mechanism across divergent eukaryotes.

### p18 subunit as a PPR protein

The p18 subunit is a pentatricopeptide repeat (PPR) protein with three
PPRs, folded into seven alpha-helices (H1-H7). It binds to the external
surface of each alpha-subunit with buried surface areas of 2,500-2,600 A2.
p18 does not bind RNA and has no catalytic function, but is essential for
enzyme assembly. The p18 sequence is highly conserved across euglenozoa.

### Elaborated F1-domain features

The T. brucei F1-domain has additional surface features compared to
bovine F1-ATPase: (1) In vivo proteolytic cleavage of alpha-subunits
removing residues 128-135; (2) Extended C-terminal regions in alpha-
(residues 483-498 and 536-560), beta- (485-499), delta- (1-17), and
epsilon- (39-50) subunits; (3) Extended gamma-subunit C-terminus
(residues 286-304, not resolved). The delta-subunit interaction with
gamma increases from 1,000 to 1,700 A2.


## Cross-References

- [F1-ATPase Rotary Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/) — T. brucei F1-ATPase has conventional rotary catalytic mechanism
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
