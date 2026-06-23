---
title: "B800-850 Light-Harvesting Complex II (LH2) from Rhodospirillum molischianum"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##S0969-2126(96)00063-9]
verified: false
---

# B800-850 Light-Harvesting Complex II (LH2) from Rhodospirillum molischianum

## Overview

The B800-850 light-harvesting complex II (LH2) from Rhodospirillum molischianum is an octameric integral membrane protein that functions as a peripheral antenna complex in photosynthetic purple bacteria. The crystal structure was determined at 2.4 Å resolution by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using a homology model based on the Rhodopseudomonas acidophila LH2 structure. The complex displays two concentric cylinders of sixteen membrane-spanning helical subunits, containing two rings of bacteriochlorophyll-a molecules — one ring of sixteen B850 BChl-as perpendicular to the membrane plane and one ring of eight B800 BChl-as nearly parallel to the membrane plane — plus eight membrane-spanning lycopenes. The B800 BChl-a is ligated by an aspartate residue (α-Asp6), in contrast to the formyl-methionine ligand found in Rps. acidophila.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##S0969-2126(96)00063-9 | 1LGH | 2.4 | P42₁2 | Native LH2 complex from Rhodospirillum molischianum. Octameric (α₈β₈) ring of α- and β-apoproteins with [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) a (B800 and B850) and lycopene [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) pigments. Asymmetric unit contains two αβ-heterodimers with 8-fold [NCS](/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/). | [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) a (B800, B850), lycopene |

## Expression and Purification

- **Expression system**: Rhodospirillum molischianum (native expression)
- **Construct**: Native LH2 complex, no affinity tags or modifications

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| LH2 complex purification | Ion exchange and detergent exchange | Mono-Q FPLC (Pharmacia), Q-Sepharose fast flow | 10 mM phosphate buffer (pH 8.7) + [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) (initially), then UDAO after exchange | The material eluted from Mono-Q FPLC was dialysed against 10 mM phosphate buffer pH 8.7 containing 0.1% (w/v) [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) and 0.1% sodium azide. Detergent was exchanged by absorbing onto Q-Sepharose, washing with buffer containing 0.2% UDAO instead of [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), and eluting with 150 mM potassium phosphate buffer pH 6.5 containing 0.2% UDAO and 0.1% sodium azide. |


## Crystallization

### doi/10.1016##S0969-2126(96)00063-9

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | Purified LH2 complex at OD850 ~200 (20 mg/mL) in 150 mM potassium phosphate pH 6.5, 0.2% UDAO, with 3.2% (w/v) HPTO added |
| Reservoir | 3.0-3.3 M [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) |
| Temperature | Room temperature |
| Growth time | Not specified |
| Cryoprotection | Flash frozen; no explicit cryoprotection specified |
| Notes | Crystals in space group P42₁2 with two crystallographically independent octameric complexes per asymmetric unit. Data collected from selenomethionine-incorporated protein. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using a homology model. Rwork/Rfree = 21.1/23.2%. The α-apoprotein is 56 residues, the β-apoprotein 45 residues (first two residues not observed). 16 water molecules, 3 UDAO and 6 HPTO molecules per αβ-heterodimer. |


## Biological / Functional Insights

### Octameric ring architecture differs from nonameric LH2

LH-2 from Rs. molischianum forms an octamer (α₈β₈) instead of the nonamer found in Rps. acidophila. The complex is shaped as a hollow cylinder of 90 Å diameter, with the α-apoprotein (inside) and β-apoprotein (outside), forming inner and outer helical rings of 31 Å and 62 Å diameter respectively. The cylinder height is 50 Å.

### B850 and B800 bacteriochlorophyll ring organization

Sixteen B850 BChl-a molecules form a ring perpendicular to the membrane plane, with Mg-Mg distances of 9.2 Å within the αβ-heterodimer and 8.9 Å between heterodimers. Eight B800 BChl-as form a second ring nearly parallel to the membrane plane, with Mg-Mg separation of 22.0 Å between neighboring BChl-as. The B800 BChl-as are tilted 38° from the membrane plane.

### Aspartate ligation of B800 BChl-a

The B800 BChl-a in Rs. molischianum is ligated by α-Asp6 (Oδ1 to Mg distance 2.45 Å), unlike the formyl-methionine ligand found in Rps. acidophila. The other carboxyl oxygen (Oδ2) is 2.75 Å from the amide Nδ of α-Asn2, forming a strong hydrogen bond. A water molecule also contacts the methyl-ester carbonyl oxygen near the B800 ring.

### Optimal Förster energy transfer between B800 and B850

The Qy transition dipole moments of neighboring B850 and B800 BChl-as are nearly parallel, optimally aligned for Förster exciton transfer. The Qy of B800 forms angles of 13.1° and 151.5° with those of B850b and B850a' respectively. The B800 Qy transition dipoles are parallel to the membrane plane to within 10°.

### Lycopene-mediated Dexter energy transfer and photoprotection

Lycopene (the major [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/)) is in van der Waals contact with both B850 and B800 BChl-as, enabling singlet and triplet energy transfer by the Dexter mechanism. Four aromatic residues (α-Trp23, β-Phe20, β-Phe24, β-Phe27) cluster around the lycopene. Lycopene runs parallel within 5 Å of the B850a' porphyrin plane and makes van der Waals contact with B800 BChl-a via neighboring heterodimer lycopene.

### High sequence conservation and structural homology with Rps. acidophila

The α- and β-apoproteins have marginal sequence homology (26% and 31% identity) with those from Rps. acidophila, but the overall fold in the transmembrane region is very similar. Major differences are found at the N- and C-terminal ends: the α-apoprotein of Rs. molischianum has a much longer C-terminal helix at a 140° angle (vs. 100° in Rps. acidophila), and the B800 BChl-a orientation differs by ~20°.


## Cross-References

- [B800-850 LH2 Light-Harvesting Complex from Rhodopseudomonas acidophila](/xray-mp-wiki/proteins/photosynthesis/lh2-rps-acidophila/) — Related LH2 from a different purple bacterium; structural homolog
- [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) — B800 and B850 bacteriochlorophyll a are the primary chromophores
- [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) — Lycopene is the major carotenoid in this complex
- [Lycopene](/xray-mp-wiki/reagents/ligands/lycopene/) — Major carotenoid in the LH2 complex; functions in energy transfer and photoprotection
- [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) — Initial solubilization detergent used during purification
- [UDAO](/xray-mp-wiki/reagents/detergents/udao/) — Detergent used after exchange for crystallization
- [Rps. viridis Photosynthetic Reaction Centre](/xray-mp-wiki/proteins/photosynthesis/rps-viridis-reaction-centre/) — Related photosynthetic membrane protein from purple bacteria
- [Rhodobacter sphaeroides Reaction Centre with Zn-BChl](/xray-mp-wiki/proteins/photosynthesis/rhodobacter-sphaeroides-reaction-center/) — Related photosynthetic complex from purple bacteria
- [NCS](/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/) — Related biological concept
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
