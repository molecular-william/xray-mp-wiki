---
title: PSI-LHCI supercomplex from pea (Pisum sativum) at 2.4 A resolution
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1111##jipb.13095]
verified: false
---

# PSI-LHCI supercomplex from pea (Pisum sativum) at 2.4 A resolution

## Overview

Photosystem I (PSI) is one of the two photosystems in oxygenic photosynthesis, performing light-driven electron transfer from plastocyanin to ferredoxin. In higher plants, PSI is surrounded by four light-harvesting complex I (LHCI) subunits (Lhca1-Lhca4) arranged in a semi-ring that harvests and transfers excitation energy to the PSI core. The highest-resolution X-ray crystal structure of the plant PSI-LHCI supercomplex was determined at 2.4 A resolution from pea (Pisum sativum) using data collected from a single crystal (Wang et al., 2021, J Integr Plant Biol). The structure was obtained by optimizing crystallization pH (from 6.9 to 9.0) and using a [PEG](/xray-mp-wiki/reagents/additives/peg/) 400/PEG 3000 cryoprotectant mixture, yielding a new crystal form in space group C12_1. Compared to previous structures (PDB 4XK8 at 2.8 A and 5L8R at 2.6 A), the Lhca4 subunit is shifted outward from the PSI core by up to 4.5 A, suggesting intrinsic flexibility in the LHCI belt. Five new lipid molecules were identified in the gap region between the PSI core and LHCI subunits, including DGDG, PG, and [MGDG](/xray-mp-wiki/reagents/lipids/monogalactosyl-diacylglycerol/) species that may facilitate attachment of Lhcas to the core and assembly of the supercomplex. The structure contains 16 protein subunits, 186 pigments (140 Chl a, 12 Chl b, 34 carotenoids), 93 water molecules, and 14 lipid molecules.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1111##jipb.13095 | 7DKZ | 2.4 | C 1 2 1 | PSI-LHCI supercomplex purified from Pisum sativum thylakoid membranes. 16 protein subunits, 186 pigments, 14 lipids resolved. | Chlorophyll a (140), chlorophyll b (12), carotenoids (34: [LUTEIN](/xray-mp-wiki/reagents/ligands/lutein/), [Violaxanthin](/xray-mp-wiki/reagents/ligands/violaxanthin/), beta-carotene), [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) (PG, 7), monogalactosyldiacylglycerol ([MGDG](/xray-mp-wiki/reagents/lipids/monogalactosyl-diacylglycerol/), 5), digalactosyldiacylglycerol (DGDG, 2) |

## Expression and Purification

- **Expression system**: Pisum sativum (pea, var. Alaska)
- **Construct**: Native PSI-LHCI supercomplex purified from thylakoid membranes

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Thylakoid isolation | Mechanical disruption and differential centrifugation | — | 0.3 M [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/), 20 mM Tricine (pH 8.0) + -- | Peas cultivated and thylakoid membranes prepared as described in Qin et al. (2015). |
| Initial solubilization | beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) solubilization | — | 0.3 M [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/), 20 mM Tricine (pH 8.0) + 0.55% (w/v) beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Thylakoids at 2.6 mg Chl/mL solubilized with 0.55% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) on ice for 12 min. Diluted 3x with cold water. Centrifuged at 20,000xg for 10 min, then supernatant at 150,000xg for 30 min. Pellet contains PSI-LHCI and LHCII. |
| Re-solubilization and DEAE chromatography | Re-solubilization + DEAE-650M ion exchange | — | Buffer A: 20 mM Tricine-Tris (pH 7.5), 50 mM NaCl, 0.075% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 1.8% (w/v) beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) for solubilization; 0.075% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) in column buffers | Pellet resuspended to 3 mg Chl/mL and re-solubilized with 1.8% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) for 15 min on ice. Centrifuged at 150,000xg for 15 min. Supernatant applied to DEAE-650M column. Elution with 50-250 mM NaCl linear gradient. PSI-LHCI eluted at 180-230 mM NaCl. |
| [PEG](/xray-mp-wiki/reagents/additives/peg/) precipitation | [PEG](/xray-mp-wiki/reagents/additives/peg/) 6000 precipitation | — | 20 mM Tricine-Tris (pH 7.5), 0.05% beta-DDTM + 0.05% beta-DDTM (n-dodecyl-beta-D-thiomaltopyranoside) | PSI-LHCI peak precipitated with 10% [PEG](/xray-mp-wiki/reagents/additives/peg/) 6000. Resuspended in 20 mM Tricine-Tris (pH 7.5) + 0.05% beta-DDTM at 1 mg Chl/mL. |
| [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) density gradient | [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) density gradient ultracentrifugation | — | 20 mM Tricine-Tris (pH 7.5), 0.05% beta-DDTM + 0.05% beta-DDTM | 0.3-0.9 M [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) gradient, centrifuged at 230,000xg for 18 h (P40ST rotor). Darkest green band collected. Precipitated with 50 mM [Ammonium Acetate](/xray-mp-wiki/reagents/buffers/ammonium-acetate/) + 10% [PEG](/xray-mp-wiki/reagents/additives/peg/) 6000. Final pellet solubilized in 20 mM Tricine-Tris (pH 7.5) for crystallization. |


## Crystallization

### doi/10.1111##jipb.13095

| Parameter | Value |
|---|---|
| Method | [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | PSI-LHCI at 4 mg Chl/mL in 20 mM Tricine-Tris (pH 7.5) |
| Reservoir | 50 mM NaCl, 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) (pH 8.0-9.0), 70 mM MgCl2, 17-18% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 1.7% (w/v) n-heptyl-beta-D-thioglucoside |
| Temperature | 285 |
| Growth time | 12-15 days at 285 K; max crystal size 0.3 x 0.2 x 0.2 mm |
| Cryoprotection | Stepwise increase of [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 (16% to 35% w/v) and [PEG 3000](/xray-mp-wiki/reagents/additives/peg3000/) (0% to 15% w/v) in 10 steps, 5 min intervals at 285 K. Flash-frozen in liquid nitrogen. |
| Notes | Higher pH (9.0) compared to previous structures (pH 6.9 for 4XK8, pH 8.0 for 5L8R) was critical for resolution improvement. The pH change and [PEG](/xray-mp-wiki/reagents/additives/peg/) mixture cryoprotection were the two main factors enabling 2.4 A resolution from a single crystal. |


## Biological / Functional Insights

### Highest-resolution structure of plant PSI-LHCI at 2.4 A

The structure of pea PSI-LHCI was determined at 2.4 A resolution from a single crystal, representing the highest-resolution plant PSI-LHCI structure to date. Key improvements came from changing crystallization pH to 9.0 (from 6.9/8.0 used previously) and a [PEG](/xray-mp-wiki/reagents/additives/peg/) 400/PEG 3000 cryoprotectant cocktail. The new crystal form (C12_1, beta=121.4 deg) differs from the previous P21 (4XK8, beta=91.4 deg) and P212121 (5L8R, beta=90 deg) forms, enabling better diffraction.

### Lhca4 shifts outward from the PSI core by up to 4.5 A

Lhca4 shows significant outward and downward translocation from the PSI core: ~3.0 A compared to 4XK8 and ~4.5 A compared to 5L8R. Lhca2 also shifts but to a lesser extent, while Lhca1 and Lhca3 remain in place. The shift correlates with loss of the bridging [LUTEIN](/xray-mp-wiki/reagents/ligands/lutein/) 320/Lhca1 molecule (also absent in moss PSI-LHCI where Lhca5 substitutes Lhca4), suggesting this [LUTEIN](/xray-mp-wiki/reagents/ligands/lutein/) normally stabilizes the Lhca1-Lhca4 dimer-core interaction. The increased Lhca4-core distance (up to 15.5 A) implies inefficient direct energy transfer from Lhca4 to the PSI core, consistent with the lack of direct pigment connections between Lhca4 and core subunits.

### Five new lipids identified in the core-LHCI gap region

Compared to the 4XK8 structure, five new lipid molecules were identified: DGDG 624/Lhca4, PG 625/Lhca4, and [MGDG](/xray-mp-wiki/reagents/lipids/monogalactosyl-diacylglycerol/) 305/PsaF in the PsaF-Lhca4 interface; PG 321/Lhca1 between Lhca1 and PsaB/PsaG; and [MGDG](/xray-mp-wiki/reagents/lipids/monogalactosyl-diacylglycerol/) 105/PsaG (previously assigned as beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) in 4XK8). These lipids are positioned to act as molecular linkers between the PSI core and LHCI antennas, facilitating supercomplex assembly. DGDG 624/Lhca4 occupies the position of the missing [LUTEIN](/xray-mp-wiki/reagents/ligands/lutein/) 320, with one tail bridging Lhca4 to PsaF via interactions with Tyr217/PsaF and Trp90/Lhca4.

### Chlorophyll a loss and lutein loss at alkaline pH

The structure contains 2-3 fewer Chl a molecules than 4XK8: Chls a301, a310, and a315 of Lhca3 are absent (a315 also absent in 5L8R). [LUTEIN](/xray-mp-wiki/reagents/ligands/lutein/) 320/Lhca1 is also missing. These losses are attributed to the alkaline pH (9.0) crystallization conditions, which affect the highly flexible, peripheral region of Lhca3 near PsaK. The room-temperature absorption spectra at pH 7.0 vs 9.0 confirm reduced Chl a content at pH 9.0, while fluorescence emission at 736 nm (77 K) remains unchanged, indicating functional integrity.

### Lipid distribution differs from 5L8R but core lipids are conserved

Comparison with the 5L8R structure (2.6 A, merged multi-crystal dataset) reveals major differences in lipid distribution, particularly around Lhca1-4. 5L8R assigned many more truncated lipids in the antenna gap region, while the present structure finds fewer but fully modeled lipids. PSI core lipids are more conserved across structures. All PG and DGDG molecules are on the stromal side, while MGDGs are predominantly on the lumenal side, reflecting the asymmetric thylakoid membrane environment.


## Cross-References

- [PSI-LHCI supercomplex from Chlamydomonas reinhardtii](/xray-mp-wiki/proteins/photosynthesis/psi-lhci-chlamydomonas/) — Both are PSI-LHCI supercomplexes from different organisms, with distinct LHCI composition and structural features
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent (beta-DDM) used throughout purification and crystallization
- [Tris (Tris-HCl buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Crystallization buffer component (50 mM Tris-HCl, pH 8.0-9.0)
- [Membrane Protein Structural Biology Concepts](/xray-mp-wiki/concepts/membrane-mimetics/) — PSI-LHCI is a large multisubunit membrane protein supercomplex embedded in the thylakoid membrane
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [PEG 3000](/xray-mp-wiki/reagents/additives/peg3000/) — Additive used in purification or crystallization buffers
- [Ammonium Acetate](/xray-mp-wiki/reagents/buffers/ammonium-acetate/) — Buffer component in purification or crystallization
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
