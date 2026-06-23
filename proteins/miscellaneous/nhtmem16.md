---
title: nhTMEM16 (TMEM16 Lipid Scramblase from Nectria haematococca)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13984]
verified: false
---

# nhTMEM16 (TMEM16 Lipid Scramblase from Nectria haematococca)

## Overview

nhTMEM16 is a calcium-activated lipid scramblase from the fungus Nectria haematococca. It is a member of the TMEM16 (anoctamin) protein family, which includes both Ca2+-activated chloride channels and lipid scramblases. nhTMEM16 functions as a homodimer, with each subunit containing ten transmembrane helices and a hydrophilic membrane-traversing cavity exposed to the lipid bilayer. The structure provides the first insight into the architecture of lipid scramblases and their mode of Ca2+ activation. The Ca2+-binding site is located within the hydrophobic core of the membrane and coordinates two Ca2+ ions. Mutations of residues involved in Ca2+ coordination affect both lipid scrambling in nhTMEM16 and ion conduction in the chloride channel TMEM16A.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13984 | 4Q6R | 3.3 A | P212121 | Full-length nhTMEM16 (772 residues) from Nectria haematococca, homodimer, expressed in S. cerevisiae with His10-EGFP tag and HRV 3C cleavage site | Two Ca2+ ions per subunit, [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| doi/10.1038##nature13984 | 4Q6S | 3.4 A | P212121 | Full-length nhTMEM16 (772 residues) from Nectria haematococca, homodimer, expressed in S. cerevisiae with His10-EGFP tag and HRV 3C cleavage site | Two Ca2+ ions per subunit, [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| doi/10.1038##nature13984 | TBD | 4.0 A | P212121 | Full-length nhTMEM16 (772 residues) from Nectria haematococca, [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-labeled, homodimer | [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| doi/10.1038##nature13984 | TBD | 3.5 A | P212121 | Full-length nhTMEM16 (772 residues), Ca2+ binding site structure determined by anomalous scattering | Two Ca2+ ions per subunit, [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| doi/10.1038##nature13984 | TBD | 4.2 A | P212121 | Full-length nhTMEM16 (772 residues), purified in presence of [EDTA](/xray-mp-wiki/reagents/additives/edta), crystallized without Ca2+ | [DDM](/xray-mp-wiki/reagents/detergents/ddm) |

## Expression and Purification

- **Expression system**: S. cerevisiae (Saccharomyces cerevisiae) FGY217 strain (URA deletion mutant)
- **Construct**: Full-length nhTMEM16 (772 residues) from Nectria haematococca, C-terminal fusion to His10-EGFP cassette with HRV 3C cleavage site (crystallization construct); N-terminal fusion to streptavidin-binding peptide (SBP) with Myc tag and HRV 3C cleavage site (scrambling assay construct)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and induction | Fermentation culture in S. cerevisiae FGY217 | -- | Yeast nitrogen base with Synthetic Complete drop-out medium without [URACIL](/xray-mp-wiki/reagents/ligands/uracil), 0.1% [Glucose](/xray-mp-wiki/reagents/additives/glucose) + -- | Protein expression induced with 2% galactose for 40 h at 25 C |
| Membrane extraction | Cell lysis and membrane fractionation | -- | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.6, 150 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm) (n-dodecyl-beta-D-maltopyranoside) | Membranes extracted from S. cerevisiae expressing nhTMEM16 |
| Affinity purification | Ni-NTA affinity chromatography (His-tag) | Ni-NTA resin | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.6, 150 mM NaCl, [DDM](/xray-mp-wiki/reagents/detergents/ddm) + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | His10-tag purification of nhTMEM16 |
| Tag cleavage | HRV 3C protease cleavage | -- | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.6, 150 mM NaCl, [DDM](/xray-mp-wiki/reagents/detergents/ddm) + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | HRV 3C protease cleavage of His10-EGFP tag |
| Second affinity purification | Ni-NTA affinity chromatography (remove cleaved tag and uncleaved protein) | Ni-NTA resin | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.6, 150 mM NaCl, [DDM](/xray-mp-wiki/reagents/detergents/ddm) + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Flow-through contains cleaved nhTMEM16 |
| Size-exclusion chromatography | SEC on Superdex 200 | Superdex 200 | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.6, 150 mM NaCl, [DDM](/xray-mp-wiki/reagents/detergents/ddm) + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Final sample is a homogeneous homodimer |


## Crystallization

### doi/10.1038##nature13984

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | nhTMEM16 at 10 mg/mL in [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| Reservoir | 20% [PEG](/xray-mp-wiki/reagents/additives/peg) 4000, 100 mM magnesium chloride, 100 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.8 |
| Temperature | 4 C |
| Growth time | Crystals appeared after several days |
| Cryoprotection | Cryocooled at 100 K |
| Notes | Crystal form 1 (CF1), space group P212121, unit cell a=96.5, b=113.7, c=235.7 A. Resolution 3.3 A. R_work=0.23, R_free=0.27. Dimer in asymmetric unit. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | nhTMEM16 at 10 mg/mL in [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| Reservoir | 20% [PEG](/xray-mp-wiki/reagents/additives/peg) 5000 MME, 100 mM lithium sulfate, 100 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 6.0 |
| Temperature | 4 C |
| Growth time | Crystals appeared after several days |
| Cryoprotection | Cryocooled at 100 K |
| Notes | Crystal form 2 (CF2), space group P212121, unit cell a=115.9, b=127.2, c=180.1 A. Resolution 3.4 A. R_work=0.24, R_free=0.28. Dimer in asymmetric unit. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-labeled nhTMEM16 |
| Reservoir | Not explicitly reported |
| Temperature | 100 K (cryocooled) |
| Growth time | Not reported |
| Cryoprotection | Cryocooled |
| Notes | Se-Met derivative for SAD phrasing. Space group P212121, unit cell a=113.7, b=124.8, c=177.4 A. Resolution 4.0 A. |


## Biological / Functional Insights

### Homodimeric architecture with 10 transmembrane helices per subunit

nhTMEM16 forms a homodimer with each subunit containing ten transmembrane helices (alpha0a, alpha0b, alpha1-alpha10). The dimer has a rhombus-like shape with about 130 A in the long dimension and 40 A in the short dimension. Both termini are structured and located on the cytoplasmic side. The N-terminal domain has a ferredoxin-like fold, and the C-terminal alpha-helices wrap around the N-terminal domain of the adjacent subunit, constituting a large part of the subunit interface.

### Dimer cavity at the subunit interface

The dimer interface buries 9,650 A2 of combined molecular surface. The largest contribution comes from N- and C-terminal domain interactions; the transmembrane contact area is only 1,520 A2. The interface generates a large pore-like structure (dimer cavity) across the transmembrane region with two 15 A wide entrances at the extracellular side merging to one 30 A wide vestibule at the intracellular half. The cavity is predominantly hydrophobic and aromatic, and is proposed to be packed with lipids. Access to the outer leaflet is via V-shaped gaps between alpha-helices 3 and 10 from adjacent subunits.

### Subunit cavity as the catalytic site

Each subunit contains a narrow crevice (subunit cavity) spanning the entire membrane, formed by alpha-helices 3-7. This cavity is 8-11 A wide, twisted like a spiral staircase, and exposed to the membrane. Despite membrane exposure, the surface is strongly hydrophilic. The cavity harbors residues with equivalent positions involved in ion conduction in TMEM16A and influencing ion selectivity in TMEM16A and F. It is proposed as the translocation path for lipid scrambling.

### Intramembrane Ca2+-binding site

Within the hydrophobic core of the membrane, at about one third of membrane thickness from the intracellular side, the subunit cavity is lined by residues of alpha-helices 6 and 7 forming a conserved Ca2+-binding site. Two Ca2+ ions were detected by anomalous scattering, separated by 4.2 A. The binding site is coordinated by three glutamates, two aspartates, and one asparagine on alpha-helices 6, 7, and 8. This intramembrane location explains the voltage-dependence of Ca2+ activation observed in TMEM16A, TMEM16B, and TMEM16F.

### Ca2+ activation mechanism

nhTMEM16 catalyzes Ca2+-dependent scrambling of phospholipids at submicromolar concentrations. Sr2+ also activates but Mg2+ does not. The EC50 for Ca2+ is in the submicromolar range. Ca2+ binding may either induce a conformational change in the protein or modify electrostatics in the nearby subunit cavity. The intramembrane location of the binding site provides an explanation for the voltage-dependence of Ca2+ activation.

### Functional dichotomy between scramblases and ion channels in TMEM16 family

While nhTMEM16 functions as a lipid scramblase, TMEM16A and TMEM16B function as Ca2+-activated chloride channels. The paper speculates that in channel-forming TMEM16 proteins, monomers might be rotated by 180 degrees and interact via their subunit cavities to form an enclosed pore, whereas scramblase-like dimers (like nhTMEM16) contain two potentially independent pores similar to the CIC family. This different dimer assembly could explain the functional dichotomy.


## Cross-References

- [afTMEM16 (TMEM16 Lipid Scramblase from Aspergillus fumigatus)](/xray-mp-wiki/proteins/miscellaneous/af-tmem16/) — Homologous fungal TMEM16 scramblase; compared in sequence alignment
- [mTMEM16A (Murine TMEM16A Calcium-Activated Chloride Channel)](/xray-mp-wiki/proteins/miscellaneous/mtmem16a/) — Murine homolog; Ca2+ binding site mutations affect ion conduction
- [TMEM16 Family](/xray-mp-wiki/concepts/protein-families/tmem16-family/) — nhTMEM16 is the structural prototype of the TMEM16 lipid scramblase subfamily
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for nhTMEM16 solubilization and purification
- [HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid)](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in nhTMEM16 purification (50 mM HEPES pH 7.6)
- [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) — NBD-labeled PE used as substrate in nhTMEM16 scrambling assay
- [Phosphatidylserine](/xray-mp-wiki/reagents/lipids/phosphatidylserine/) — NBD-labeled PS used as substrate in nhTMEM16 scrambling assay
- [Intramembrane Ion Coordination](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/intramembrane-ion-coordination/) — nhTMEM16 Ca2+ binding site is an example of intramembrane ion coordination
- [EDTA](/xray-mp-wiki/reagents/additives/edta) — Entity mentioned in text
- [Glucose](/xray-mp-wiki/reagents/additives/glucose) — Entity mentioned in text
