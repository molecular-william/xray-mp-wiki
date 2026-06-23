---
title: "VrH+PPase (Vigna radiata H+-Pumping Inorganic Pyrophosphatase)"
created: 2026-05-29
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, enzyme, membrane-protein]
sources: [doi/10.1038##NATURE10963, doi/10.1016##j.jmb.2019.03.009]
verified: false
---

# VrH+PPase (Vigna radiata H+-Pumping Inorganic Pyrophosphatase)

## Overview

VrH+-PPase (H+-pumping inorganic pyrophosphatase from Vigna radiata, also known as [VrPPase (Vibrio rotiferans H+-Pumping Pyrophosphatase)](/xray-mp-wiki/proteins/pumps-atpases/vrppase/) or AVP1 homolog) is a membrane-bound enzyme that catalyzes the hydrolysis of inorganic pyrophosphate (PPi) and couples the released energy to proton translocation across the vacuolar membrane. This enzyme belongs to the family of P-type ATPases and is found in the tonoplast of plant cells. It plays a critical role in establishing proton gradients that drive secondary transport processes and regulate cellular pH and turgor pressure. The crystal structure reveals a dimeric arrangement with 16 transmembrane helices per monomer and an intrinsically disordered region ([IDP](/xray-mp-wiki/reagents/ligands/idp/)) involved in Mg2+ coordination.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NATURE10963 | 4A01 | 2.35 | C2 |  | [IDP](/xray-mp-wiki/reagents/ligands/idp/) (imidodiphosphate), Mg2+, K+ |
| doi/10.1016##j.jmb.2019.03.009 | 6AFS | 2.3 | C2 |  | 2Pi (two inorganic phosphates), Mg2+, K+ |
| doi/10.1016##j.jmb.2019.03.009 | 6AFT | 2.5 | C2 | E301Q mutant (ion gate residue) | Pi |
| doi/10.1016##j.jmb.2019.03.009 | 6AFU | 2.8 | C2 | L555M mutant (hydrophobic gate residue) | Pi |
| doi/10.1016##j.jmb.2019.03.009 | 6AFV | 2.7 | C2 | L555K mutant (hydrophobic gate residue) | Pi |
| doi/10.1016##j.jmb.2019.03.009 | 6AFW | 2.2 | C2 | T228D mutant (exit channel residue) | Pi |
| doi/10.1016##j.jmb.2019.03.009 | 6AFX | 2.3 | C2 | E225A mutant (exit channel latch residue) | Pi |
| doi/10.1016##j.jmb.2019.03.009 | 6AFY | 2.4 | C2 | E225S mutant (exit channel latch residue) | Pi |
| doi/10.1016##j.jmb.2019.03.009 | 6AFZ | 2.48 | C2 | E225H mutant (exit channel latch residue) | Pi |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### Dimer Interface Structure

The VrH+-PPase crystal structure reveals a dimeric arrangement where the two monomers
interact through a combination of hydrophobic interactions in the transmembrane region
and salt bridges/hydrogen bonds near the cytosolic and vacuolar lumen regions. Key
dimer interface interactions include:

- Salt bridge: R441 (helix alpha2, subunit A) to E606 (helix M13, subunit B) with
  distance of 2.3 Å
- Hydrogen bonds: R441-O to R609-NH1/NH2 (3.0 Å), V568-O to V570-N (3.1 Å),
  V570-N to V568-O (3.2 Å), Y587-OH to Y587-OH (2.2 Å), R609-NH2 to R441-O (2.9 Å)
- Extensive hydrophobic interactions between helices M5-M16 of the two subunits,
  primarily in the membrane portion of the dimer interface
- Salt bridge network at the cytosolic surface involving seven charged residues
  (K261, R523, D269, E268, D527, K695, E698) forming a core salt bridge network

### Hydrophobic gate checkpoint mechanism

The hydrophobic gate of VrH+-PPase (L232, A305, L555, V746) acts as a
checkpoint in the ion translocation pathway. Pore diameter analysis using
PoreWalker reveals a wave-like profile with diameters varying from ~1 A
(narrow, at D294/E301/T228) to ~4 A (wide, at R242/K742/L555). The
2Pi-bound state shows the largest pore diameter at the hydrophobic gate
(3.7 A), indicating an open-gate conformation, while the IDP- and
Pi-bound states show narrower diameters (2.1 and 2.0 A respectively),
corresponding to a closed gate after proton transfer.

### E225-R562 salt bridge acts as exit channel latch

A salt bridge between E225 (TM5) and R562 (TM12) at the exit channel
regulates proton release into the vacuolar lumen. The E225A mutation
eliminates this interaction, creating a cavity with continuous water
wire (Wat5-Wat10) that mimics an open exit channel. The E225S and
E225H mutants partially compensate through hydrogen bonds (4.5 A and
4.0 A respectively). The sequential movement of E225-R562 suggests a
dynamic latch mechanism controlling proton release.

### Continuous water wire from ion gate to exit channel

A continuous water wire from the ion gate (Wat_nu, Wat1, Wat2) through
the hydrophobic gate (Wat3, Wat4) and into the exit channel (Wat5-Wat10)
is observed across multiple mutant structures. Wat3 and Wat4 at the
hydrophobic gate in the E301Q, L555K, and T228D mutants suggest
solvation of the gate during proton translocation. This water wire
reflects the path of proton transfer via the Grotthuss-chain mechanism.

### L555 mutations uncouple PPi hydrolysis from proton pumping

Mutation of the highly conserved L555 (TM12) at the hydrophobic gate
differentially affects PPi hydrolysis and proton pumping. L555M retains
75% hydrolysis but only 29% pumping; L555K retains 44% hydrolysis but
0% pumping. In L555K, water (Wat3) is recruited near the hydrophobic
gate, coordinated by T228, E301, and K555. The L555A mutation similarly
abolishes pumping while retaining 39% hydrolysis, demonstrating that
L555 acts as a hydrophobic seal whose size and properties are critical
for coupling hydrolysis to ion translocation.

### Mg2+ Ion Coordination and IDP Binding

The intrinsically disordered region ([IDP](/xray-mp-wiki/reagents/ligands/idp/)) of VrH+-PPase coordinates three Mg2+ ions
(Mg1, Mg2, Mg3) through water-mediated interactions and direct coordination with
aspartate residues. Each Mg2+ ion is coordinated by 3-4 water molecules and one or
two aspartate side chains (D253, D257, D507). The Mg2+ coordination sites are
conserved between subunits A and B, with nearly symmetric coordination geometries.
This Mg2+ coordination is essential for catalytic activity, as Mg2+ is a required
cofactor for PPi hydrolysis.

### Proton Translocation Pathway

The structure identifies key residues along the proton translocation pathway, including
conserved arginine (R242 in VrH+-PPase, corresponding to R246 in A. thaliana AVP1) and
aspartate (D294) residues critical for proton pumping activity. Mutagenesis studies
show that R242A reduces both PPi hydrolysis (7% of WT) and proton pumping (7% of WT),
while D294N, D294E, D294T, and D294A mutations abolish proton pumping activity while
retaining partial PPi hydrolysis. These findings support a mechanism where proton
translocation is coupled to PPi hydrolysis through conformational changes in the
transmembrane helices.


## Cross-References

- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — SAD phasing with OsO4 and Orange-Pt derivatives used to solve the structure
- [Multi-Wavelength Anomalous Diffraction (MAD)](/xray-mp-wiki/methods/structure-determination/multi-wavelength-anomalous-diffraction/) — MAD phasing with Ta6Br12 derivative used to solve the structure
- [Platinum(II) Chloride](/xray-mp-wiki/reagents/additives/platinum-ii-chloride/) — Related heavy atom compound used in SAD phasing
- [VrPPase (Vibrio rotiferans H+-Pumping Pyrophosphatase)](/xray-mp-wiki/proteins/pumps-atpases/vrppase/) — Related protein structure
- [IDP](/xray-mp-wiki/reagents/ligands/idp/) — Related ligand or cofactor
