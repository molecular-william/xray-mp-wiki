---
title: GLIC (Gloeobacter violaceus Ion Channel)
created: 2026-06-10
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2012.08.009, doi/10.1016##j.str.2016.02.014, doi/10.1038##nature07461, doi/10.1038##nature07462, doi/10.1038##NSMB.1933, doi/10.1038##emboj.2013.17, doi/10.1085##jgp.201711803, doi/10.1073##pnas.1314997111, doi/10.1073##pnas.1813378116, doi/10.1074##jbc.M116.766964, doi/10.7554##eLife.23886, doi/10.1038##nature09647]
verified: false
---

# GLIC (Gloeobacter violaceus Ion Channel)

## Overview

GLIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from the cyanobacterium Gloeobacter violaceus. It is a proton-gated ion channel that serves as a bacterial homolog of eukaryotic Cys-loop receptors including nicotinic acetylcholine receptors, GABA-A receptors, and 5-HT3 receptors. GLIC is activated by low pH and inhibited by general anesthetics including ketamine, propofol, and volatile anesthetics. It has been widely used as a model system for understanding pLGIC gating, ion permeation, and anesthetic action. FD/DH electrostatics and FTIR spectroscopy identified E35 as the key proton sensor, with gating mediated by two distinct water-mediated and hydrophobic networks connecting E35 through the ECD-TMD interface to the M2 helix and M2-M3 loop region, bypassing the canonical orthosteric site.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature07461 | 3GHG | 3.1 | C2 | Full-length GLIC wild-type | -- |
| doi/10.1038##nature07462 | 3EHZ | 2.9 | C2 | Full-length GLIC residues 6-315 (MBP fusion cleaved) | -- |
| doi/10.1016##j.str.2012.08.009 | 3EAM | 3.25 | P21212 | Full-length GLIC residues 1-355 | -- |
| doi/10.1016##j.str.2012.08.009 | not specified (Ketamine-bound) | 2.99 | — | Full-length GLIC co-crystallized with ketamine | Ketamine (1 mM, 5 sites per pentamer) |
| doi/10.1016##j.str.2016.02.014 | 5HCJ | 2.95 | C2 | Full-length GLIC, MBP fusion cleaved | Bromoform (pore site, locally closed) |
| doi/10.1016##j.str.2016.02.014 | 5HCM | 3.15 | C2 | Full-length GLIC, MBP fusion cleaved | Bromoform (open conformation, intra-subunit sites) |
| doi/10.1085##jgp.201711803 | 5V6N | 3.12 | — | Full-length GLIC C27S + K33C + I9'A + N21'C quadruple mutant | -- |
| doi/10.1038##emboj.2013.17 | not specified (GLIC_2.4) | 2.4 | C2 | Full-length GLIC residues 1-355 | Br-, Cs+, acetate, sulfate |
| doi/10.1073##pnas.1314997111 | not specified (GLIC pH 7) | 4.35 | P21 | Full-length GLIC from G. violaceus, wild-type | -- |
| doi/10.1073##pnas.1314997111 | not specified (GLIC_His10 pH 4) | not specified | P212121 | Full-length GLIC with C-terminal His10 tag, expressed in insect cells | -- |
| doi/10.1073##pnas.1813378116 | not specified (Q193M pH 4) | 2.95 | — | GLIC Q193M mutant | -- |
| doi/10.1073##pnas.1813378116 | not specified (Q193L pH 4) | 3.39 | — | GLIC Q193L mutant | -- |
| doi/10.1073##pnas.1813378116 | not specified (Q193C pH 4) | 2.58 | — | GLIC Q193C mutant | -- |
| doi/10.1073##pnas.1813378116 | not specified (Y197F pH 4) | not specified | — | GLIC Y197F mutant | -- |
| doi/10.1073##pnas.1813378116 | not specified (K248C pH 4) | not specified | — | GLIC K248C mutant | -- |
| doi/10.1073##pnas.1813378116 | not specified (K248A pH 4) | not specified | — | GLIC K248A mutant | -- |
| doi/10.1073##pnas.1813378116 | not specified (E243C pH 4) | not specified | — | GLIC E243C mutant | -- |
| doi/10.1074##jbc.M116.766964 | 5L4H | 3.3 | C2 | GLIC K33C-L246C locally-closed (LC) mutant | [Bromobarbital](/xray-mp-wiki/reagents/ligands/bromobarbital) (pore site) |
| doi/10.1074##jbc.M116.766964 | 5L47 | 2.99 | C2 | GLIC K33C-L246C locally-closed (LC) mutant | [Selenocyanobarbital](/xray-mp-wiki/reagents/ligands/selenocyanobarbital) (pore site) |
| doi/10.1074##jbc.M116.766964 | 5L4E | 3.5 | C2 | GLIC K33C-L246C locally-closed (LC) mutant | [Thiopental](/xray-mp-wiki/reagents/ligands/thiopental) (pore site) |
| doi/10.7554##eLife.23886 | 5J0Z | 3.25 | C121 | Full-length GLIC wild-type, co-crystallized with DHA | Docosahexaenoic acid (DHA); phospholipid (PLC) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

### Purification Workflow

*Source: doi/10.1038##nature07462*

- **Expression system**: E. coli
- **Expression construct**: Full-length GLIC with MBP fusion and thrombin cleavage site
- **Tag info**: MBP fusion tag cleaved by thrombin

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression | — |  |  |
| Membrane extraction and solubilization | Detergent solubilization | — | DDM (2%/0.02%) |  |
| Amylose affinity chromatography | Affinity chromatography | Amylose resin | DDM (0.02%) |  |
| Size-exclusion chromatography (first) | SEC | — | DDM (0.02%) |  |
| Thrombin cleavage | Protease cleavage | — | DDM (0.02%) |  |
| Size-exclusion chromatography (second) | SEC | — | DDM (0.02%) |  |

**Final sample**: GLIC pentamer in 0.02% DDM buffer

### Purification Workflow

*Source: doi/10.1038##NSMB.1933*

- **Expression system**: E. coli
- **Expression construct**: Full-length GLIC with MBP-His10 fusion and E. coli pELB signal sequence
- **Tag info**: MBP-His10, cleaved by HRV 3C protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression | — |  |  |
| Membrane extraction | Detergent solubilization | — | DDM |  |
| Affinity purification | Ni-NTA affinity chromatography | Ni-NTA | DDM |  |
| Tag cleavage | HRV 3C protease cleavage | — | DDM | MBP cleaved off, removed by rebinding to Ni-NTA |
| Size-exclusion chromatography | SEC | Superdex 200 | 10 mM Tris pH 7.5, 150 mM NaCl + 0.5 mM DDM |  |

**Final sample**: 10 mg/ml in 10 mM Tris pH 7.5, 150 mM NaCl, 0.5 mM DDM

### Purification Workflow

*Source: doi/10.7554##eLife.23886*

- **Expression system**: E. coli (C43)
- **Expression construct**: Full-length GLIC with N-terminal MBP fusion and HRV 3C protease cleavage site, in modified pET26b vector
- **Tag info**: MBP tag cleaved by HRV 3C protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli (C43) expression in terrific broth with 50 ug/ml kanamycin, induced with 0.2 mM IPTG at 18 C overnight | — |  |  |
| Membrane preparation | Homogenization and centrifugation at 100,000 x g | — |  |  |
| Membrane solubilization | Detergent solubilization | — | 100 mM NaCl, 20 mM Tris-HCl pH 7.4, protease inhibitors + DDM (40 mM) |  |
| Amylose affinity chromatography | Affinity chromatography | Amylose resin | DDM (0.5 mM) | Eluted with 20 mM maltose |
| Tag cleavage | HRV 3C protease cleavage | — | DDM (0.5 mM) |  |
| Size-exclusion chromatography | SEC | Superdex 200 | 100 mM NaCl, 20 mM Tris-HCl pH 7.4 + DDM (0.5 mM) |  |

**Final sample**: GLIC pentamer in 100 mM NaCl, 20 mM Tris-HCl pH 7.4, 0.5 mM DDM

### Purification Workflow

*Source: doi/10.1073##pnas.1314997111*

- **Expression system**: E. coli / Insect cells (Sf9)
- **Expression construct**: Full-length GLIC (untagged) for pH 7 structure; GLIC_His10 (C-terminal His10) for pH 4 structure
- **Tag info**: His10 for GLIC_His10 expressed in insect cells

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli expression for pH 7 GLIC | — |  | GLIC expressed and purified as described in Bocquet et al., 2009 |
| Expression (alternative) | Insect cell (Sf9) expression for GLIC_His10 | — |  | GLIC fused to C-terminal His10 tag produced in insect cells |
| Purification | Standard GLIC purification protocol | — |  | Purified as per ref. 8 (Bocquet et al., 2007) |


## Crystallization

### doi/10.1016##j.str.2012.08.009

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | GLIC (~10 mg/ml) pre-equilibrated with 0.5 mg/ml E. coli polar lipids |
| Reservoir | 10%-12% PEG 4000, 225 mM ammonium sulfate, 50 mM sodium acetate buffer pH 3.9-4.1 |
| Mixing ratio | 1:1 |
| Temperature | 4 C |
| Growth time | 1 week |
| Cryoprotection | Reservoir supplemented with 20% glycerol |

### doi/10.1073##pnas.1314997111

| Parameter | Value |
|---|---|
| Method | Vapor diffusion with dehydrating cryoprotection |
| Protein sample | Purified GLIC at neutral pH |
| Notes | Initial diffraction to 8.5 A. Elaborate dehydrating cryoprotection protocol and extensive screening improved diffraction to 4.35 A. Space group P21 with four pentamers per asymmetric unit (~6200 residues). NCS averaging over 20 chains and B-factor sharpening improved map quality. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | GLIC_His10 at pH 4 |
| Notes | GLIC_His10 produced in insect cells, crystallized at pH 4. Space group P212121. Shows coexistence of locally closed and open conformations. |

### doi/10.7554##eLife.23886

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | GLIC (9-10 mg/ml) pre-incubated with 50 uM DHA and 0.5 mg/ml E. coli polar extract for 1 hr on ice |
| Reservoir | 225 mM ammonium sulfate, 50 mM sodium acetate pH 3.9-4.2, 9-12% PEG4000 |
| Mixing ratio | 1:1 |
| Temperature | 4 C |
| Growth time | 1-3 weeks |
| Cryoprotection | Reservoir supplemented with 30% ethyleneglycol |


## Biological / Functional Insights

### Open conformation of GLIC reveals gating mechanism of pLGICs

The 2.9 A GLIC structure at pH 4.6 reveals open conformation. Key rearrangements: quaternary twist of pentamer, rotation of each extracellular beta-sandwich domain, tilt of M2 and M3 away from pore axis.

### Ketamine binding to an intersubunit cavity

Ketamine binds to a pre-existing cavity between adjacent subunits in the extracellular domain. Five molecules per pentamer. Site near homologous orthosteric agonist-binding site.

### Resting state structure of GLIC at neutral pH

The pH 7 (neutral) structure of GLIC reveals the resting state at 4.35 A resolution. The ECD displays large intrinsic structural flexibility with significant deviations from C5 symmetry (rmsd 1.2 A in ECD vs 0.2 A in TMD). The pore is closed by an upper bend of helix M2 (as in locally closed form) and a kink of helix M1. A marked quaternary change is observed involving both a twist and a blooming motion. Detachment of inner and outer beta sheets reshapes the ligand-binding cavity and a cavity near a known divalent cation binding site.

### Open and LC forms coexist at pH 4

GLIC_His10 crystallized at pH 4 in space group P212121 shows both locally closed and open conformations coexisting as discrete states. The M2 helix and M2-M3 loop show dual conformations, with the energy landscape made of two wells in the presence of the ligand (protons).

### Critical residues at the ECD-TMD interface

Phe195 (F195A shows loss of function), Leu246 (L246A shows loss of function, interacts with ECD via hydrophobic cleft), and Asp32-Arg192 salt bridge (D32N shifts pH50, D32N-R192Q double mutant shows loss of function) play key roles in gating.

### Barbiturate binding in the ion channel pore

The first X-ray structures of barbiturates bound to a pLGIC were determined using GLIC K33C-L246C (locally-closed mutant). Bromobarbital (3.3 A, PDB 5L4H), selenocyanobarbital (2.99 A, PDB 5L47), and thiopental (3.5 A, PDB 5L4E) all bind within the central ion channel pore between residues 2' and 9' of the M2 helix. Hydrogen bonds between barbiturate carbonyl groups and 6' serines are the primary interactions, with van der Waals interactions involving 9' isoleucines. Thiopental adopts an inverted orientation due to its branched C5 tail. Docking calculations across closed, open, and desensitized states predict barbiturates preferentially stabilize the closed conformation, explaining their inhibitory mechanism on cationic pLGICs. The same pore site also binds xenon and bromoform.

### Structural fluctuations prefigure the gating transition

Principal component analysis of the 20 monomers in the pH 7 asymmetric unit reveals that the first PC of fluctuations has an overlap of 0.88 with the quaternary transition and 0.75 with the tertiary transition between pH 7 and pH 4 forms. This demonstrates that intrinsic fluctuations of the unperturbed system prefigure the response to ligand binding, consistent with linear response theory.

### Sequential model for pLGIC activation

The gating pathway starts at the extracellular tip with orthosteric site contraction and beta sheet movements, propagates through the ECD-TMD interface involving the beta1-beta2 loop and M2-M3 loop, and results in M2 helix tilting and pore opening. This is consistent with experimental data from nicotinic receptor studies.

### E35 is the key proton sensor for GLIC gating

Using finite difference Poisson-Boltzmann/Debye-Huckel (FD/DH) electrostatics calculations and FTIR spectroscopy combined with site-directed mutagenesis, E35 was identified as the key proton sensor with a measured individual pKa of 5.8, close to the electrophysiological pH50 of 5.1. E35 is located in front of loop F, far from the canonical orthosteric site. It establishes a polar interaction with T158 from loop F, connecting to a water-mediated hydrogen bond network reaching Q193 in the pre-M1 region and further to the ECD-TMD interface.

### Two networks connect E35 to the transmembrane domain

The gating signal from E35 propagates through two distinct networks. Network 1 (hydrophilic): E35 → water network → Q193 (pre-M1) → R192-D122-D32 electrostatic triad → Y197 → K248 → E243 → N239 → H235, reaching the middle of the M2 helix in the adjacent subunit. Network 2 (hydrophobic): Y197-P120-Y119 interactions → L246 (M2-M3 loop) → P247 and T251, encircling the ECD-TMD interface. Q193M/L mutations trap the channel in a nonconductive LC1 conformation. The two networks converge at H235 and the pre-M1 region, showing loop F acts as an allosteric site instead of the classic orthosteric site for gating in GLIC.

### DHA binding site and desensitized state of GLIC

Docosahexaenoic acid (DHA), an omega-3 polyunsaturated fatty acid abundant in synaptic membranes, enhances agonist-induced desensitization in GLIC. The 3.25 A crystal structure (PDB: 5J0Z) reveals DHA bound at the channel periphery near the M4 helix, interacting with Arg118 in the Cys-loop (beta6-beta7 loop). Mutation R118A reduces the DHA effect, validating the binding site. The GLIC-DHA complex adopts a potentially desensitized conformation distinct from previously observed pLGIC states: the extracellular half of M2 is splayed open (reminiscent of open state), while the intracellular half is constricted at Ile9' with loss of both water and permeant ions. DEER spectroscopy in nanodiscs shows M4 undergoes an outward tilt (up to 4 A) during desensitization, with increased lipid exposure of the TMD-facing side. CW-EPR reveals Pro300 acts as a hinge for M4 motion. The DHA effect is absent in the non-desensitizing I9'A/H11'F mutant, confirming the state is agonist-induced and not an uncoupled conformation.

### General anesthetic binding site in GLIC revealed by propofol and desflurane structures

X-ray structures of GLIC complexed with propofol (3.3 A) and desflurane (3.2 A) reveal a common general-anesthetic binding site pre-existing in the apo-structure in the upper part of the transmembrane domain of each protomer. Both molecules bind within an intra-subunit cavity and establish van der Waals interactions with residues from M1 (I201, I202, M205, L206), M2 (V242), M3 (Y254, T255, I258, I259), M4 (N307, F303), and the beta6-beta7 loop (Y119). Propofol binds at the entrance of the cavity while the smaller desflurane binds deeper inside. Mutation of residues within this site (I202Y, V242M, T255A) alters both the intrinsic ionic response of GLIC and its general-anesthetic pharmacology. The binding site is located on the backside of the pore-lining M2 helices at the level of the gate, close to the TMD-ECD interface, suggesting the mechanism involves reorganization of the binding site during gating through M2 and M3 helix tilting. Nearby ordered lipids are displaced upon propofol binding, suggesting general anaesthetics may compete with endogenous lipid modulators.


## Cross-References

- [Pentameric Ligand-Gated Ion Channel (pLGIC)](/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/) — GLIC is a prokaryotic member of the pLGIC superfamily
- [Ketamine](/xray-mp-wiki/reagents/ligands/ketamine/) — Ketamine binds to intersubunit cavity in ECD, inhibits GLIC
- [ELIC (Erwinia ligand-gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Direct structural comparison between closed (ELIC) and open (GLIC) states
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary purification and crystallization detergent
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in SEC buffer (10 mM Tris pH 7.5)
- [Xenopus Oocytes Expression System](/xray-mp-wiki/methods/expression-systems/xenopus-oocytes/) — GLIC and mutants expressed in Xenopus oocytes for electrophysiology
- [PEG 4000](/xray-mp-wiki/reagents/additives/peg-4000/) — Crystallization precipitant
- [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate/) — Crystallization buffer at pH 4
- [sTeLIC (Tevnia jerichonana Endosymbiont pLGIC)](/xray-mp-wiki/proteins/cys-loop-receptors/stelic/) — Homologous prokaryotic pLGIC; sTeLIC shows an even more open pore conformation than GLIC
- [Barbiturate Binding Mechanism in pLGICs](/xray-mp-wiki/concepts/transport-mechanisms/barbiturate-binding-mechanism/) — First X-ray structures of barbiturates bound to GLIC revealed the pore binding site
- [Bromobarbital](/xray-mp-wiki/reagents/ligands/bromobarbital/) — Barbiturate co-crystallized with GLIC-LC (PDB 5L4H)
- [Thiopental](/xray-mp-wiki/reagents/ligands/thiopental/) — Clinically used barbiturate co-crystallized with GLIC-LC (PDB 5L4E)
- [Selenocyanobarbital](/xray-mp-wiki/reagents/ligands/selenocyanobarbital/) — Synthetic barbiturate co-crystallized with GLIC-LC (PDB 5L47)
