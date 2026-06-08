---
title: Acid-Sensing Ion Channel 1a
created: 2026-05-27
updated: 2026-06-04
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2014.01.011, doi/10.1038##nature06163, doi/10.1038##nature11375, doi/10.1038##ncomms1917]
verified: false
---

# Acid-Sensing Ion Channel 1a

## Overview

Acid-sensing ion channel 1a (ASIC1a) is a proton-gated, sodium-selective ion channel from the degenerin/epithelial sodium channel (Deg/ENaC) superfamily. Expressed in vertebrate central and peripheral nervous systems, ASIC1a detects extracellular protons produced during inflammation or ischemic injury and initiates pain signals. The first high-resolution structure of the open state was solved by Se-Met SAD phasing at 1.9 A resolution (Kawate & Gouaux, Nature 2009). A later structure captured the open state in complex with the snake toxin MitTx (Cell 2014). The first structure of a gating modifier toxin bound to an ion channel was solved for the PcTx1-ASIC1 complex at 3.0 A resolution (Dawson et al., Nat Commun 2012).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature06163 | 3HV4 | 1.9 A | P21 | Chicken delta ASIC1 (residues 147-526) | Na+ |
| doi/10.1016##j.cell.2014.01.011 | 4NTW | 2.1 A | R3 | Chicken delta13 ASIC1a | Na+ |
| doi/10.1016##j.cell.2014.01.011 | 4NTX | 2.3 A | R3 | Chicken delta13 ASIC1a | amiloride |
| doi/10.1016##j.cell.2014.01.011 | 4NTY | 2.6 A | R3 | Chicken delta13 ASIC1a | Cs+ |
| doi/10.1038##nature11375 | 4H2N | 3.35 A | R3 | Chicken delta13 ASIC1a | PcTx1 |
| doi/10.1038##nature11375 | 4H2O | 2.80 A | C2 | Chicken delta13 ASIC1a | PcTx1 |
| doi/10.1038##ncomms1917 | 3S3W | 1.9 A | C2 | Chicken ASIC1 (residues 26-463, apo) | none |
| doi/10.1038##ncomms1917 | 3S3X | 3.0 A | C2 | Chicken ASIC1 (residues 26-463) + Psalmotoxin 1 | Psalmotoxin 1 |

## Expression and Purification

- **Expression system**: HEK293T cells (electrophysiology), E. coli (crystallography)
- **Construct**: Chicken ASIC1a (full-length for electrophysiology), Chicken delta ASIC1 (residues 147-526, truncated extracellular N-terminus for crystallography), Chicken ASIC1 (residues 26-463, for PcTx1 complex)

### Purification Workflow

*Source: doi/10.1038##nature06163*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| FSEC screening | Fluorescence size-exclusion chromatography | Superose 6 10/300 | 20 mM Tris pH 8.0, 150 mM NaCl + 1 mM DDM | N- and C-terminally EGFP-tagged chicken ASIC1 and delta ASIC1 constructs screened by FSEC. Solubilized in PBS with 20 mM DDM and protease inhibitors for 1 h. Monodisperse peak identified for delta ASIC1-EGFP fusion. |
| SEC purification | Size-exclusion chromatography | Superose 6 10/300 | 20 mM Tris pH 8.0, 150 mM NaCl, 1 mM DDM + 1 mM DDM | Monodisperse fractions of delta ASIC1 collected for crystallization. Molecular mass determined by light scattering: 165.9 +/- 1.4 kDa, consistent with a trimer. |

### Purification Workflow

*Source: doi/10.1038##ncomms1917*

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: Chicken ASIC1 (residues 26-463), His6-tagged
- **Tag info**: His6-tag, removed with PreScission protease at 4 C or thrombin at room temperature

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | Baculovirus expression in Sf9 cells | -- | 50 mM Tris(HCl) pH 8.0, 150 mM NaCl + -- | Sf9 cells infected with baculovirus expressing chicken ASIC1(26-463). Cell debris removed by centrifugation at 488 g for 15 min, supernatant centrifuged at 95,700 g for 35 min at 4 C. Membranes resuspended in 50 mM Tris(HCl) pH 8.0, 150 mM NaCl and stored at -80 C. |
| Solubilization | Detergent solubilization | -- | 50 mM Tris(HCl) pH 8.0, 150 mM NaCl + 2% (w/v) n-dodecyl-beta-D-maltopyranoside (DDM) | Purified membranes (corresponding to 100 g cells) solubilized in 200 ml buffer with 2% DDM under stirring for 60 min at 4 C. Supernatant isolated by centrifugation at 150,000 g for 20 min. |
| IMAC purification | Nickel-affinity chromatography | Talon Superflow IMAC resin | 50 mM Tris(HCl) pH 8.0, 150 mM NaCl, 0.05% DDM + 0.05% DDM | Washed and eluted with 45 mM or 300 mM imidazole, respectively, at 4 C. Tag removed with PreScission protease at 4 C or thrombin at room temperature for 1 h. |
| Complex formation | In-solution mixing | -- | 20 mM Tris(HCl) pH 8.0, 150 mM NaCl, 0.05% DDM + 0.05% DDM | 0.36 mg of synthetic, lyophilized PcTx1 (Peptanova) dissolved directly in protein solution after tag removal. |
| Size exclusion chromatography | Size-exclusion chromatography | Superose 10/300 GL | 20 mM Tris(HCl) pH 8.0, 150 mM NaCl, 0.05% DDM + 0.05% DDM | Excess PcTx1, protease and other buffer components removed. Isolated, monodisperse protein preparation concentrated to 2.7 mg/ml using Amicon Ultra Ultracel centrifugal filter (100 kDa MWCO). |


## Crystallization

### doi/10.1038##nature06163

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Chicken delta ASIC1 (residues 147-526) at ~10 mg/mL in 20 mM Tris pH 8.0, 150 mM NaCl, 1 mM DDM |
| Reservoir | Not specified in supplementary information |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Open state structure solved at 1.9 A resolution, space group P21. Se-Met SAD phasing used. Crystals also derivatized with platinum and bromine for additional phasing. Resolution: 50-1.9 A (outer shell 1.97-1.90 A). R_merge 6.6% (42.1% in outer shell). Completeness 93.6% (69.3% outer shell). |

### doi/10.1038##ncomms1917

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Chicken ASIC1 (residues 26-463) in complex with Psalmotoxin 1 at 2.7 mg/ml in 20 mM Tris(HCl) pH 8.0, 150 mM NaCl, 0.05% DDM |
| Reservoir | Not specified in supplementary information |
| Temperature | 4 C |
| Growth time | matured within 1 week |
| Cryoprotection | 15% glycerol |
| Notes | Crystals in monoclinic space group C2 with one trimer per asymmetric unit. Collected directly from crystal well with 15% glycerol for cryoprotection, flash frozen in liquid nitrogen. Diffraction data collected to 3.0 A resolution at wavelength 1.0000 A using PILATUS 6M detector at beamline X10SA, Swiss Light Source. Structure determined by molecular replacement with PHASER using apo chicken delta ASIC1 as start model. Refinement with PHENIX using NCS restraints for extracellular domains. Three Ramachandran outliers (6.5% allowed), 6 rotamer outliers. |


## Biological / Functional Insights

### pH-dependent gating mechanism

At high pH, the finger and thumb domains of ASIC1 are separated, possibly with calcium ions bound in the interdomain cleft. Upon exposure to low pH, calcium ions are released, key acidic residues become protonated, and the thumb and finger domains move together, pivoting around the beta-ball domain. The ion channel then opens and desensitizes, coupled to the thumb domain through a ball-and-socket joint at Trp 288. This mechanism links extracellular proton sensing to transmembrane pore opening.

### Trimer stoichiometry confirmed by crosslinking and light scattering

Glutaraldehyde crosslinking of delta ASIC1 revealed trimeric (250 kDa), dimeric (150 kDa), and monomeric (100 kDa) species. Molecular mass determination by light scattering of the monodisperse peak indicated 165.9 +/- 1.4 kDa, consistent with a trimeric assembly.

### TM2 contains a degenerin (d) position analog

Gly 432 corresponds to the degenerin (d) position found in other Deg/ENaC family members. Maltoside groups from DDM detergent molecules are located near this position in the transmembrane domain, viewed parallel to the membrane bilayer plane.

### Chloride binding site in the pore

An anomalous difference Fourier map from crystals soaked in NaBr revealed a chloride binding site coordinated by Lys 212 (subunit C), Arg 310, and Glu 314. This represents a specific ion coordination site within the transmembrane pore.

### MitTx acts as a bottle opener to stabilize the open state

MitTx binds to the wrist, palm, and thumb domains of ASIC1a like a churchkey bottle opener. The alpha subunit's Phe 14 inserts as a hook into the subunit interface, splaying subunits apart. The binding site overlaps with psalmotoxin binding, explaining why these toxins are mutually exclusive.

### TM2 is a discontinuous helix with a belt-like GAS selectivity filter

TM2 is not a continuous alpha helix but has a break approximately two-thirds of the way across the membrane, dividing it into TM2a (extracellular) and TM2b (cytoplasmic) segments. The GAS (Gly-Ala-Ser) selectivity filter motif adopts an extended, belt-like conformation aligned parallel to the membrane plane.

### TM2b swaps between subunits

The cytoplasmic one-third of TM2 (TM2b) undergoes a swap between adjacent subunits. The TM2b element of one subunit interacts with TM1a of an adjacent subunit, effectively generating a continuous TM2 helical segment.

### Ion selectivity by hydrated ion size barrier

The GAS selectivity filter positions the carbonyl oxygen of Gly 443 directly into the pore, forming a triangular ring with a radius of approximately 3.6 A that matches the radius of a hydrated Na+ ion. The channel is selective for Li+ and Na+ over K+ (~4:1) and nearly impermeable to larger cations Rb+ and Cs+.

### PcTx1 binding site at subunit interfaces

PcTx1 (pilidium toxin 1) binds at the subunit interfaces of the ASIC1a trimer, contacting residues across the wrist, palm, and thumb domains. The arginine residues of the toxin form key interactions at the subunit interface, and the aromatic residues engage in an 'aromatic embrace' with the channel. This binding site overlaps with the acidic pocket region, stabilizing the desensitized conformation of the channel.

### pH-dependent vestibule expansion

The vestibule region undergoes conformational changes between high pH and low pH structures. Flexing of beta1 and beta12 helices expands the vestibule at low pH. Residues Glu 80, Leu 414, and Asn 415 are key players in this conformational change. The E80A mutant shows altered activation kinetics (time constant ~10 ms vs ~400 ms for wild-type) and can be activated by PcTx1 at pH 7.25.

### Transmembrane pore constriction and hydrophobic gating

The high pH structure has a large pore (~10 A diameter at residue 433) while the low pH structure has an elliptical hydrophobic pore constriction lined by Leu 440 from all three subunits. Asp 433 is positioned above the hydrophobic constriction. The L440A and L440S mutants show altered channel function with steady-state currents of ~30% and ~20% of peak current, respectively.

### Cs+ binding site in the wrist region

Anomalous difference electron density maps from Cs+ soaks reveal a cesium binding site in the wrist region of the high pH complex. The Cs+ ion is coordinated by backbone carbonyl oxygens arranged in a specific geometry that can be compared between high pH, low pH, and desensitized state structures using Pro 287 and Pro 288 as reference.

### Correlated structural movements between extracellular and transmembrane domains

Structural rearrangements in the wrist region (Tyr 72 and Trp 288) couple extracellular and transmembrane domain movements. These residues are implicated in channel gating, and their side chains show rotational movements in opposite directions between the desensitized and pH-bound states. Five disulfide bonds in the thumb region (connecting residues 324-336, 322-344, 313-360, 309-362, and 291-366) provide structural stability to this coupling region.

### Peptide plane flip and main chain swap in linkers

A peptide plane flip occurs in the beta1-beta2 linker between residues Thr 84 and Arg 85, which is observed in the desensitized state but not in the toxin-bound high and low pH structures. Additionally, a main chain swap occurs in the beta11-beta12 linker involving residues 412-416, where Leu 414 mediates hydrophobic interactions that differ between the high pH and desensitized structures.

### Transmembrane domain intersubunit contacts

The high pH structure shows intersubunit hydrophobic contacts between Val 46 (TM1) of one subunit and Ile 446 (TM2) of an adjacent subunit. The low pH structure shows a leucine zipper-like motif in the TM domain with leucines at positions i and i+7 (L440 and L447). The TM domains do not participate in direct lattice contacts, suggesting crystal packing does not influence TM domain conformation.

### Hydrophobic seal enhances electrostatic interactions in PcTx1-ASIC1 complex

The hydrophobic patch of PcTx1 wraps around helix 5 of ASIC1 and shields the basic cluster (arginine residues) from bulk solvent. This hydrophobic seal enhances the electrostatic contribution of charge-charge interactions between the arginine guanidinium groups and ASIC1 carboxylates in the acidic pocket, similar to hydrophobic O-rings at protein-protein binding hot spots. The extensive hydrophobic surface (860 A^2 total, with ASIC1-specific residues providing 350 A^2) surrounds the positively charged guanidinium groups. Phe351 and Phe174 of ASIC1 account for 155 A^2 of the binding surface and are critical for PcTx1 selectivity.

### Cation-binding site in the central vestibule

Extra electron density was observed in the occluded central vestibule, approximately 20 A above the ion-selective pore. The vestibule is lined by acidic residues (Glu80, Glu374, Glu412, Gln277, Gln279, Glu417) and the density is located near Glu80 and Glu417. Carboxylate groups of Glu417 coordinate a putative cation right above Leu78, which separates the central from the extracellular vestibule. Arg370 is the only positively charged residue in the central vestibule, located about 7.5 A above the putative cation. This supports the model that the central vestibule functions as a cation reservoir.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and SEC purification of ASIC1a
- [Fluorescence Size-Exclusion Chromatography (FSEC)](/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/) — FSEC used to identify optimal detergent conditions for ASIC1a
- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Se-Met SAD phasing used to solve the open state structure (3HV4)
- [GAS Selectivity Filter](/xray-mp-wiki/concepts/gas-selectivity-filter/) — Central mechanism of ion selectivity in ASIC1a
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Used for Se-SAD phasing of ASIC1a crystals
- [Pilidium Toxin 1 (PcTx1)](/xray-mp-wiki/reagents/ligands/pc-tx1/) — Toxin bound in ASIC1a complex structures (PDB 3S3X, 4H2N, 4H2O) at subunit interfaces
- [MitTx (Texas coral snake toxin)](/xray-mp-wiki/reagents/ligands/mittx/) — Heteromeric toxin that binds to overlapping site on ASIC1a, stabilizing the open state
