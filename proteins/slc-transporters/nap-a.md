---
title: Na+/H+ Antiporter NapA from Thermus thermophilus
created: 2026-06-03
updated: 2026-06-22
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12484, doi/10.1038##nsmb.3164]
verified: false
---

# Na+/H+ Antiporter NapA from Thermus thermophilus

## Overview

NapA from Thermus thermophilus is a Na+/H+ antiporter belonging to the CPA2 clade of the monovalent cation proton antiporter (CPA) superfamily. It catalyzes the electrogenic exchange of Na+ (or Li+) for H+ across the membrane, playing a critical role in intracellular pH homeostasis and sodium concentration regulation. The protein consists of 13 transmembrane helices organized into a core domain (helices 1-6) and a dimerization domain (helices -1 and 7-12), forming a homodimer in the membrane. NapA was initially crystallized in an outward-facing conformation at 3.0 A resolution, revealing a negatively charged extracellular cavity with the strictly conserved aspartate residue (Asp 157) positioned for ion binding. Later structures trapped NapA in an inward-facing conformation via disulfide crosslinking (PDB 5BZ2, 3.7 A) and refined the outward-facing conformation in lipidic cubic phase (PDB 5BZ3, 2.3 A), confirming an elevator-like alternating-access mechanism for ion translocation with the core domain moving ~8 A relative to the fixed dimer domain.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12484 | not specified | 3.0 A | C222_1 | Full-length NapA from Thermus thermophilus (Uniprot Q72IM4), GFP-His8 fusion with TEV cleavage site | zinc (2 ions per monomer) |
| doi/10.1038##nsmb.3164 | 5BZ2 | 3.7 A | C222_1 | Full-length NapA V31C I130C mutant (Uniprot Q72IM4), TEV-cleaved | none |
| doi/10.1038##nsmb.3164 | 5BZ3 | 2.3 A | C222_1 | Full-length NapA wild-type (Uniprot Q72IM4), TEV-cleaved | LCP lipid MAG7.7 modeled at core-dimer interface |

 - R-work not specified%, R-free not specified%; Data collection: X-ray diffraction at 3.0 A resolution, solved by multiple isomorphous replacement with anomalous scattering (MIRAS) with Mercury (HgCl2) and Selenomethionine (SeMet) derivatization, multi-crystal averaging
 - R-work 0.292%, R-free 0.325%; Data collection: X-ray diffraction at 3.7 A resolution; molecular replacement with dimer and core domains of PDB 4BWZ as separate search models; refined in autoBUSTER/Phenix
 - R-work 0.206%, R-free 0.218%; Data collection: X-ray diffraction at 2.3 A resolution; LCP crystallization; data collected at Diamond Light Source; refined in autoBUSTER/Phenix

## Expression and Purification

- **Expression system**: Escherichia coli Lemo21(DE3)
- **Construct**: Full-length NapA from Thermus thermophilus (Uniprot Q72IM4) cloned into pWaldoGFPe vector as GFP-His8 fusion; expressed with IPTG induction at 25 C overnight

### Purification Workflow

*Source: doi/10.1038##nature12484*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane fractionation | not specified | 1x PBS, 150 mM NaCl + not specified | Membranes isolated from 5 L E. coli cultures |
| Solubilization | Detergent solubilization | not specified | 1x PBS, 150 mM NaCl, 10 mM Imidazole + 1% DDM | Solubilized in 1% DDM for 2 h |
| Ni-NTA affinity capture | Ni-NTA affinity chromatography | Ni-NTA Superflow resin | 1x PBS, 150 mM NaCl, 20 mM Imidazole, 0.1% DDM + 0.1% DDM | Washed with 20 mM and 50 mM Imidazole |
| Elution | Ni-NTA affinity elution | Ni-NTA Superflow resin | 1x PBS, 150 mM NaCl, 250 mM Imidazole, 0.6% NM + 0.6% NM | Eluted in NM-containing buffer |
| Tag cleavage | TEV protease cleavage | not specified | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.5% NM + 0.5% NM | Dialyzed overnight with His6-tagged TEV protease |
| Second Ni-NTA purification | Ni-NTA affinity chromatography | Ni-NTA His-Trap column | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.5% NM + 0.5% NM | Cleaved NapA collected in flow-through |

### Purification Workflow

*Source: doi/10.1038##nsmb.3164*

- **Expression system**: Escherichia coli Lemo21(DE3)
- **Expression construct**: Full-length NapA (wild-type and mutants V31C, I130C, V31C/I130C, I55C) in pWaldoGFPe vector, GFP-His8 fusion with TEV cleavage site
- **Tag info**: C-terminal GFP-His8 tag, removed by TEV protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | MemStar overexpression | not specified | not specified + not specified | Transformed into E. coli Lemo21(DE3), overexpressed with MemStar protocol |
| Membrane preparation | Ultracentrifugation | not specified | 1x PBS, 150 mM NaCl + not specified | Membranes isolated from 6 L E. coli cultures |
| Solubilization | Detergent solubilization | not specified | 1x PBS, 150 mM NaCl, 10 mM Imidazole + 1% DDM | Solubilized in 1% DDM for 1 h at 4 C |
| Ni-NTA affinity capture | Ni-NTA affinity chromatography | Ni-NTA Superflow resin | 1x PBS, 150 mM NaCl, 0.1% DDM + 0.1% DDM | Washed with 10, 20, 45 mM Imidazole (3 x 10 CV each) |
| Elution | Ni-NTA affinity elution | Ni-NTA Superflow resin | 1x PBS, 150 mM NaCl, 250 mM Imidazole, 0.6% NM + 0.6% NM | Eluted in NM-containing buffer |
| Tag cleavage | TEV protease cleavage | not specified | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.5% NM + 0.5% NM | Dialyzed overnight with His6-tagged TEV protease and 5 mM DTT |
| Second Ni-NTA purification | Ni-NTA affinity chromatography | Ni-NTA His-Trap column (GE Healthcare) | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.5% NM + 0.5% NM | Cleaved NapA collected in flow-through |
| Oxidation and gel filtration (functional studies) | Size-exclusion chromatography | Superdex 200 10/300 | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.03% DDM + 0.03% DDM | Pre-incubated with 1 mM CuSO4 for 30 min for reoxidation; SEC in DDM |
| Gel filtration (structural studies) | Size-exclusion chromatography | Superdex 200 10/300 | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.6% NM + 0.6% NM | No CuSO4 treatment; SEC in NM |

**Final sample**: Purified NapA in 20 mM Tris-HCl pH 7.5, 150 mM NaCl with either 0.03% DDM or 0.6% NM


## Crystallization

### doi/10.1038##nature12484

| Parameter | Value |
|---|---|
| Method | Vapour diffusion |
| Protein sample | Cleaved NapA in NM detergent |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystals grown at pH 7.8 or 9.0; data collected at Diamond Light Source I02, I03 and ESRF ID 23-1, 23-2; protein derivatized with 2.5 mM Mercury (HgCl2) in Acetate Buffer; structure solved by MIRAS with multi-crystal averaging at 3.0 A resolution in space group C222_1; crystals contain 4 molecules in asymmetric unit; 2 zinc ions bound per monomer on periplasmic surface |

### doi/10.1038##nsmb.3164

| Parameter | Value |
|---|---|
| Method | Vapour diffusion |
| Protein sample | NapA V31C I130C mutant, TEV-cleaved |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Inward-facing disulfide-trapped structure (PDB 5BZ2); data collected at Diamond Light Source; molecular replacement with PDB 4BWZ dimer and core domains; refined to 3.7 A resolution in space group C222_1; disulfide bond between C31 and C130 |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Cleaved wild-type NapA |
| Lipid | MAG7.7 (monoacylglycerol) |
| Protein-to-lipid ratio | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Outward-facing LCP structure (PDB 5BZ3); data collected at Diamond Light Source; refined to 2.3 A resolution in space group C222_1; bilayer-type crystal packing; LCP lipid MAG7.7 modeled at core-dimer interface; half helices TM4a and TM11b more open than detergent structure |


## Biological / Functional Insights

### Two-domain elevator mechanism for alternating access

The NapA structure reveals a two-domain architecture with a core domain (helices 1-6) and a dimerization domain (helices -1 and 7-12). The core and dimerization domains are in different positions compared to the inward-facing NhaA structure, with a 20-degree rotation of the core domain relative to the dimerization domain. This rotation opens a negatively charged cavity to the extracellular side, allowing access to the strictly conserved aspartate (Asp 157) that coordinates ion binding. The elevator movement carries the substrate-binding domain across the membrane, resembling the mechanism seen in the glutamate transporter GltPh and the bile acid sodium symporter ASBT_NM.

### Dimer assembly and dimerization interface

NapA purifies as a homodimer with an extensive interface burying 1,800 A^2 of surface area. The dimer has a crystallographic two-fold operator approximately parallel to the transmembrane helices, formed by tight hydrophobic helix-helix packing between TM-1 on one monomer and TM7 on the other, with additional contacts between the ends of TM2 and TM9. NapA lacks the beta-hairpin domain present in NhaA that mediates extracellular dimer contacts; instead, the dimer interface resembles that modeled in the NhaP1 electron crystallography structure.

### Ion-binding site and conserved residues

The substrate-binding cavity is open to the extracellular side and is negatively charged, lined with glutamate residues. Near the base of the cavity are two highly conserved aspartates, Asp 156 and Asp 157, located on TM5. Asp 157 is strictly conserved and ideally positioned for binding both protons and sodium ions. Lys 305 (TM10) forms a salt bridge with Asp 156 in the outward-facing state. Mutation of Glu 333 (TM11b) decreased Na+ affinity (>15-fold) and Lys 305 mutation decreased both Na+ and Li+ affinity (>20-fold), confirming their functional importance.

### Disulfide trapping of inward-facing conformation confirms elevator mechanism

An engineered disulfide bond between V31C (dimer domain) and I130C (core domain) traps NapA in an inward-facing conformation (PDB 5BZ2), abolishing ~90% of transport activity. The disulfide bond can form spontaneously in a membrane environment. ITC measurements of the trapped mutant give Kd values for Na+ (1.6 mM) and Li+ (0.25 mM) at pH 8.0, similar to apparent Km values, confirming the trapped state is functionally competent for binding. The C-alpha atom of D157 is relocated ~8 A vertically between outward and inward states, with the side chain rotating ~55 degrees.

### LCP structure reveals physiological outward-facing conformation

The 2.3 A LCP structure (PDB 5BZ3) shows bilayer-type crystal packing, unlike the detergent-grown crystal. The core domain adopts the same overall conformation, but half helices TM11b and TM4a are tilted ~6 A further from the cavity, making it more open. MD simulations show these half helices fluctuate between positions seen in both structures, indicating high mobility. The open vestibule provides an open path for Na+ ions to bind D157 from extracellular solvent.

### MD simulations confirm core domain movement against fixed dimer

Molecular dynamics simulations of outward- and inward-facing NapA in a POPE/POPG (4:1) bilayer show the dimer domain vertical position differs by only ~2 A between states, while the core domain moves ~6 A relative to the membrane and ~7 A relative to the dimer domain. Morph analysis shows the core domain undergoes a large rotation and translation, with D157 relocated ~11 A between the two states. Flexible hinge regions between TM9-10 (extracellular) and TM6-7 (intracellular) containing glycine residues (G193, G213, G277, G294) facilitate the movement.

### Alternating salt bridges and half-helix gating

Positively charged residues K344 (TM11b) and R133 (TM4b) form alternating ionic interactions with negatively charged residues in the dimer domain to stabilize alternate conformations. K344A and R133E mutations negatively affect transport; a charge-swapped double mutant (E35R/R133E) rescues activity. Acyl chains (modeled as LCP lipids) located between TM4b/TM11b half helices and the dimer domain in the outward-facing LCP structure suggest in vivo lipids may facilitate the elevator-like structural transitions.


## Cross-References

- [Na+/H+ Antiporter NhaA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/nhaa/) — Structural homologue and comparison protein; inward-facing NhaA structure used for alternating access model
- [Elevator Mechanism](/xray-mp-wiki/concepts/elevator-mechanism/) — NapA provides structural evidence for the elevator transport mechanism
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — NapA operates by alternating access between outward-facing and inward-facing states
- [Rocking-Bundle Mechanism](/xray-mp-wiki/concepts/rocking-bundle-mechanism/) — Contrasted with elevator mechanism as alternative transport model for Na+/H+ antiporters
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for NapA membrane solubilization at 1%
- [n-Nonyl-beta-D-maltopyranoside (NM)](/xray-mp-wiki/reagents/detergents/nm/) — Used for NapA elution and purification at 0.6% and 0.5%
- [Dithiothreitol (DTT)](/xray-mp-wiki/reagents/additives/dtt/) — Used as reducing agent in TEV cleavage and functional assays
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to obtain outward-facing NapA structure at 2.3 A (PDB 5BZ3)
- [Isothermal Titration Calorimetry (ITC)](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) — ITC used to measure Na+, Li+, and K+ binding affinities of trapped inward-facing NapA
- [Molecular Dynamics Simulations](/xray-mp-wiki/methods/molecular-dynamics-simulations/) — MD simulations confirmed core domain movement against fixed dimer domain
