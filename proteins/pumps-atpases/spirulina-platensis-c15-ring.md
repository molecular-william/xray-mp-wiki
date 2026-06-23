---
title: Spirulina platensis ATP Synthase c15 Ring
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NSMB.1678]
verified: false
---

# Spirulina platensis ATP Synthase c15 Ring

## Overview

The c15 ring from the proton-coupled F1Fo ATP synthase of Spirulina platensis is a membrane-embedded rotor ring composed of 15 c subunits forming an hourglass-shaped assembly. Determined at 2.1-A resolution, the structure reveals the proton-locked conformation of a conserved glutamate (Glu62) that serves as the H+ binding site. The ring differs from Na+-dependent c-rings in its coordination chemistry and selectivity for protons over other cations.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NSMB.1678 | 2WIE | 2.13 | P6322 | Isolated c15 ring from Spirulina platensis thylakoid membranes; 15 c subunits (residues 5-82) | [Cymal-4](/xray-mp-wiki/reagents/detergents/cymal-4/) detergent (15 molecules, one per subunit) |

## Expression and Purification

No purification described.

## Crystallization

### doi/10.1038##NSMB.1678

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | S. platensis c15 ring at 1.8 mg/mL in 2.5% [Cymal-4](/xray-mp-wiki/reagents/detergents/cymal-4/) solution in water |
| Reservoir | 10% [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/), 350 mM [Lithium Sulfate](/xray-mp-wiki/reagents/additives/lithium-sulfate/), 0.1 M [Sodium Acetate Buffer](/xray-mp-wiki/reagents/buffers/acetate/) (pH 4.3) |
| Temperature | 4 C (implied by typical crystallization conditions) |
| Cryoprotection | Same buffer with 35% [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/); crystal flash-frozen in liquid nitrogen |
| Notes | Bipyramidal crystals grew within 3-5 days; data collected at 0.9202 A wavelength at Swiss Light Source (SLS) PX-II beamline; structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using I. tartaricus c11 ring (PDB 1YCE) as search model |


## Biological / Functional Insights

### Proton-locked conformation of Glu62

The H+-binding site is formed by the conserved glutamate (Glu62) in the proton-locked conformation. Glu62 is located in the center of the outer helix, 5 A above the middle of the membrane toward the cytoplasm. The carboxyl oxygens of Glu62 engage in a hydrogen bonding network: Oepsilon2 accepts a hydrogen from Gln29 (same subunit), Oepsilon1 accepts from Tyr67 (adjacent subunit), and Oepsilon2 donates to the backbone carbonyl of Phe60 (neighboring subunit), breaking the alpha-helical hydrogen bonding pattern. This conformation prevents the carboxyl group from being exposed to the hydrophobic lipid environment.

### 15-subunit ring architecture

The c15 ring comprises 15 c subunits forming an hourglass-shaped assembly. Each c subunit binds one [Cymal-4](/xray-mp-wiki/reagents/detergents/cymal-4/) detergent molecule mimicking the outer membrane leaflet. The detergent molecules replace membrane lipids and form a belt around the outer perimeter of the ring. The outer membrane leaflet position is shifted by 10 A toward the periplasmic side relative to the membrane surrounding the ring.

### Proton selectivity against Na+ and H3O+

The structure demonstrates high selectivity for H+ binding over Na+ and H3O+. The proton-binding site lacks the buried structural water molecule characteristic of Na+-dependent rings. Ser66 (in I. tartaricus) is replaced by Ala63, and Thr67 is replaced by the bulkier Leu64, which excludes the bound water. The reduced size of the binding site and these substitutions confer pronounced selectivity for protons. The structure does not support hydronium ion (H3O+) binding to H+-coupled c-rings.

### Proposed proton translocation mechanism

The c subunits remain in the proton-locked state when facing the membrane lipid. Proton exchange occurs only at the interface with the a subunit, where a more hydrophilic and electrostatically distinct environment facilitates the interconversion between proton-locked and open orientations. A conserved positively charged arginine in the a subunit is crucial for proton release. The model proposes four intermediate states (0-3) for coupled rotation and ion translocation.


## Cross-References

- [Ilyobacter tartaricus C Subunit](/xray-mp-wiki/proteins/pumps-atpases/ilyobacter-tartaricus-c-subunit/) — Na+-dependent c11 ring compared throughout; structure comparison shows ~12 degree outer-helix bend angle difference and distinct ion coordination
- [Bovine Mitochondrial F1-ATPase](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — Related F-type ATPase; bovine F1 domain (alpha3beta3gamma delta epsilon) powers rotation of the c-ring rotor
- [Rotary ATPase Mechanism](/xray-mp-wiki/concepts/rotary-atpase-mechanism/) — The c-ring rotation driven by proton translocation is the core of the rotary ATPase mechanism
- [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) — Related Cymal detergent family member used in membrane protein crystallization
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Structure solved by molecular replacement using I. tartaricus c11 ring (PDB 1YCE) as search model
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method used to obtain bipyramidal crystals of the c15 ring
- [Lithium Sulfate](/xray-mp-wiki/reagents/additives/lithium-sulfate/) — Additive used in purification or crystallization buffers
- [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/) — Additive used in purification or crystallization buffers
- [Sodium Acetate Buffer](/xray-mp-wiki/reagents/buffers/acetate/) — Buffer component in purification or crystallization
- [Cymal-4](/xray-mp-wiki/reagents/detergents/cymal-4/) — Detergent used in purification or crystallization
