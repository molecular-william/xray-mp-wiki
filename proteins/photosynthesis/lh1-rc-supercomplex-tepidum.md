---
title: "LH1-RC Supercomplex from Thermochromatium tepidum"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-018-0002-9, doi/10.1038##s41467-021-21397-9]
verified: false
---

# LH1-RC Supercomplex from Thermochromatium tepidum

## Overview

The light-harvesting complex 1 (LH1) and reaction centre (RC) form a membrane-protein supercomplex that performs the primary reactions of photosynthesis in purple photosynthetic bacteria. The crystal structure of the calcium-ion-bound LH1-RC supercomplex from the thermophilic purple sulfur bacterium Thermochromatium tepidum was determined at 1.9 A resolution (Yu et al., Nature 2018, PDB 5Y5S), representing a significant improvement over the previous 3.0 A structure. The RC is surrounded by 16 heterodimers of LH1 alpha-beta-subunits containing 32 [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) a and 16 spirilloxanthin molecules, forming a completely closed elliptical ring. The high-resolution structure revealed unique features including: intact loop regions of the RC cytochrome (Cyt) and H subunits in their native conformations stabilized by interactions with LH1; the detailed Ca2+-binding environment with all 16 Ca2+-binding sites identified; a quinone exchange channel between the LH1 alpha- and beta-subunits; and extensive water-mediated hydrogen-bonding networks for proton transfer to QB. A subsequent co-crystal structure of HiPIP-bound LH1-RC at 2.9 A resolution revealed the molecular basis for interprotein electron transfer from the high-potential iron-sulfur protein (HiPIP) to the RC via the tetraheme cytochrome subunit.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-018-0002-9 | 5Y5S | 1.9 | C121 | LH1-RC supercomplex from Thermochromatium tepidum comprising 36 protein subunits: RC subunits (C-cytochrome, H, M, L) and 16 LH1 alpha-beta heterodimers (32 subunits) | [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) a (36 total: 4 in RC, 32 in LH1), [Bacteriopheophytin](/xray-mp-wiki/reagents/cofactors/bacteriopheophytin/) a (2), heme-Fe (4 in Cyt subunit), spirilloxanthin (17: 1 in RC, 16 in LH1), non-[HEME](/xray-mp-wiki/reagents/ligands/heme/) Fe (1), Mg2+ (1 in Cyt), Ca2+ (16 in LH1), MQ8 (1, QA), UQ8 (5: QB + 3 in gap + 1 near channel), [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) (9), [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) (10), [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) (2) |
| doi/10.1038##s41467-021-21397-9 | 7C52 | 2.9 | Not specified | HiPIP:LH1-RC co-complex from Thermochromatium tepidum: LH1-RC supercomplex (RC subunits C, H, M, L + 16 LH1 alpha-beta heterodimers) bound with one HiPIP molecule at the Cyt subunit surface | HiPIP (4Fe-4S cluster), [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) a, [Bacteriopheophytin](/xray-mp-wiki/reagents/cofactors/bacteriopheophytin/) a, heme-Fe (4 in Cyt subunit), spirilloxanthin, non-[HEME](/xray-mp-wiki/reagents/ligands/heme/) Fe, Ca2+, [Menaquinone](/xray-mp-wiki/reagents/ligands/menaquinone/), [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) |

## Expression and Purification

- **Expression system**: Thermochromatium tepidum (thermophilic purple sulfur bacterium)
- **Construct**: Native LH1-RC supercomplex from Tch. tepidum cells grown at 49 C for 7 days

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth | Tch. tepidum cells grown in BiOTRON LH-410PFP-SP chamber at 49 C for 7 days with LED illumination (450 nm and 645 nm, 30 microE m-2 s-1) | -- | -- + -- | Bacterial cells grown under these conditions appeared to have a larger ratio of LH1-RC/LH2 according to absorption spectra |
| Purification | Purified as described previously (Niwa et al., Nature 2014) with slight modifications | -- | 20 mM MES pH 6.2 + 3.4% n-octyl-phosphocholine (OPC) | Final LH1-RC samples with A915/A280 ratio > 2.20 collected and precipitated by addition of 13% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 1450, then suspended in 20 mM MES pH 6.2 containing 3.4% OPC to 20 mg/mL |


## Crystallization

### doi/10.1038##s41586-018-0002-9

| Parameter | Value |
|---|---|
| Method | Microbatch-under-oil crystallization |
| Protein sample | LH1-RC at 20 mg/mL in 20 mM MES pH 6.2, 3.4% OPC |
| Reservoir | 50 mM MES pH 6.2, 50 mM CaCl2, 10 mM MgCl2, 3.4% OPC, 26% [PEG](/xray-mp-wiki/reagents/additives/peg/) 1450 |
| Temperature | 20 C |
| Growth time | 10 days (crystals grew to 0.3-0.4 x 0.4-0.8 x 0.05-0.2 mm3) |
| Cryoprotection | 50 mM MES pH 6.2, 3.4% OPC, 30% [PEG](/xray-mp-wiki/reagents/additives/peg/) 1450, 50 mM CaCl2, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/); flash-frozen in nitrogen stream |
| Notes | 2 uL protein solution mixed with equal volume of precipitant solution. Space group C121 with unit cell a=145.23 A, b=143.81 A, c=210.28 A, beta=90.74 deg. Data collected at BL41XU of SPring-8 (wavelength 1.0 A, Pilatus 6M detector). 5400 images collected over 540 deg rotation. Refined to Rwork/Rfree = 0.1815/0.2152. |

### doi/10.1038##s41467-021-21397-9

| Parameter | Value |
|---|---|
| Method | Microbatch-under-oil crystallization |
| Protein sample | LH1-RC at 0.0694 mM mixed with HiPIP at 15:1 molar ratio in 30 mM sodium [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/) pH 5.0, 20 mM CaCl2, 3.4% OPC, 30% [PEG](/xray-mp-wiki/reagents/additives/peg/) 1500 |
| Reservoir | 30 mM sodium [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/) pH 5.0, 20 mM CaCl2, 3.4% OPC, 30% [PEG](/xray-mp-wiki/reagents/additives/peg/) 1500 |
| Temperature | 20 C |
| Growth time | 5 days (crystals ~0.4 x 0.7 x 0.3 mm) |
| Cryoprotection | Post-crystallization treatment similar to free LH1-RC protocol |
| Notes | HiPIP purified in reduced state. High molar ratio (15:1 HiPIP:LH1-RC) and acidic pH (5.0) required for co-crystal formation. MALDI/TOF-MS used to confirm HiPIP binding. [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) analysis confirmed endothermic (entropically driven) binding. |


## Biological / Functional Insights

### Complete closed elliptical LH1 ring with 16 alpha-beta heterodimers

The LH1 ring comprises 16 alpha-beta heterodimers forming a completely closed elliptical ring surrounding the RC. This differs from Rhodobacter sphaeroides (dimeric with PufX, 8.0 A structure) and Rhodopseudomonas palustris (monomeric with transmembrane helix protein W, 4.8 A structure), both of which show incomplete ring structures. The closed ring in Tch. tepidum is stabilized by extensive inter-subunit interactions, particularly in the Ca2+-binding C-terminal domain on the periplasmic side.

### Triacylated cytochrome subunit N-terminus

The cytochrome (Cyt) subunit N-terminal cysteine (Cys23) is triacylated with N-acyl and S-diacylglycerol in a manner similar to outer membrane proteins. The previous 3.0 A structure assigned this region incorrectly. Three partial acyl chains were resolved, with one single chain and one branched chain. These fatty acids anchor the Cyt subunit in the membrane and beyond the seventh carbon, the aliphatic tails are disordered and may interact with UQ8.

### Intact RC loop regions stabilized by LH1 interactions

Three RC loop regions show major differences from isolated RC structures: (1) the Cyt N-terminal region; (2) the Cyt loop (residues 172-196) which interacts with LH1 alpha-Asp48 and alpha-Ser41, and is stabilized by a bound Mg2+; (3) the H subunit loop (residues 44-58) which interacts with the neighboring LH1 beta-polypeptide at the cytoplasmic side. These interactions with LH1 maintain the intact-state conformations and are absent in isolated RC structures.

### Quinone exchange channel between LH1 alpha and beta subunits

Direct structural evidence for quinone transport through a channel between neighboring LH1 alpha- and beta-subunits. A UQ8 molecule has its isoprenoid tail inserted into the inter-subunit space, suggesting it is being transported between the inside and outside of the LH1 ring. The channel is hydrophobic, surrounded by Val20, Ser23, Ile24, Phe27 (alpha-subunit) and Leu21, Val22, Val25, Ile29 (adjacent alpha-subunit). The spirilloxanthin and BChl phytol tail contribute to the hydrophobic channel exit.

### Comprehensive Ca2+-binding environment in LH1

All 16 Ca2+-binding sites in the LH1 C-terminal loops are identified unambiguously at 1.9 A resolution. The calcium ions are coordinated by residues from both the alpha and beta subunits, and their binding reduces conformational flexibility of the LH1 ring. This Ca2+-binding is responsible for the unusual redshift and enhanced thermal stability of the thermophilic Tch. tepidum LH1, and is related to the deletion of residue alpha-43 in this organism (insertion of alanine disrupts Ca2+ binding and causes blueshift).

### Water-mediated proton transfer networks

Extensive hydrogen-bonding networks in the H subunit connect QB to the cytoplasmic surface via a large number of water molecules. One major hydrogen-bonding network runs approximately perpendicular to the membrane surface, serving as a proton-transfer channel connecting QB to the aqueous phase. A water cluster parallel to the membrane plane was also found, similar to that in Rba. sphaeroides RC, supporting multi-entry proton uptake networks for QB protonation.

### Lipid distribution and positively charged layer

21 lipid molecules identified: 9 cardiolipins (CDL), 10 phosphatidylglycerols (PG), and 2 phosphatidylethanolamines (PEF). Two arginine residues (Arg18 and Arg19) at the beginning of LH1 alpha-subunit helices, together with other arginines and lysines from RC and LH1, form a positively charged layer at the membrane surface that may interact with phosphate groups of lipids, strengthening the association of LH1 with RC.

### BChl arrangement and ring planarity changes

Compared to the 3.0 A structure, the [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) ring of beta-His36 (direct ligand for beta-BChl) is rotated by ~45 degrees, and the porphyrin plane of the beta-BChl is rotated by ~10 degrees along its Qy axis. These changes result in a more parallel orientation of neighboring BChls, giving rise to stronger coupling between adjacent BChls and explaining the improved spectral properties of the high-resolution structure.

### HiPIP binding site on the tetraheme cytochrome subunit

The co-crystal structure of the HiPIP:LH1-RC complex at 2.9 A resolution reveals that HiPIP binds at the surface of the tetraheme cytochrome (Cyt) subunit, covering a range from Glu60 to Asp120 and in close proximity to the low-potential heme-1. The contact surface area between the two proteins is 667 A2. A hydrogen bond between Trp116 (Cyt subunit) and Thr79 (HiPIP) stabilizes the complex. The binding is hydrophobic and entropically driven, requiring high molar ratios (15:1) and acidic pH (5.0) for co-crystallization. HiPIP binding induces a significant bend in the heme-1 macrocycle, which likely modulates its reduction potential to make electron transfer more favorable.

### Five-step electron transfer pathway from HiPIP to the RC special pair

The co-crystal structure reveals a five-step trans-protein electron tunneling chain spanning more than 70 A: from the 4Fe-4S cluster of HiPIP to heme-1, then through heme-2, heme-3, and heme-4 of the Cyt subunit, and finally to the special pair [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) dimer in the RC. Center-to-center distances between redox pairs range from 12.2-20.6 A. The first step from 4Fe-4S to heme-1 is mediated by Leu63 of HiPIP, located 3.5 A from both the sulfur S1 of the cluster and the 2-methyl carbon of heme-1. The rate-limiting step is the interprotein electron transfer from HiPIP to heme-1 (calculated rate ~1.5 x 10^5 s^-1), which is thermodynamically unfavorable but enabled by [HEME](/xray-mp-wiki/reagents/ligands/heme/) distortion upon HiPIP binding. The final step to the special pair is mediated by Tyr171 of the RC L-subunit.


## Cross-References

- [Photosystem II core dimer from Thermosynechococcus elongatus](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii-core-dimer/) — Another photosynthetic membrane protein supercomplex solved by X-ray crystallography; comparison of light-harvesting and electron transfer mechanisms
- [Photosystem II from red alga Cyanidioschyzon merolae](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii-red-alga/) — Photosynthetic supercomplex from a different organism; comparison of reaction center architecture
- [PSI-LHCI supercomplex from Pisum sativum](/xray-mp-wiki/proteins/photosynthesis/psi-lhci-pea/) — Another photosynthetic supercomplex with light-harvesting antenna solved at high resolution
- [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) — Related ligand or cofactor
- [Bacteriopheophytin](/xray-mp-wiki/reagents/cofactors/bacteriopheophytin/) — Related ligand or cofactor
- [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) — Related ligand or cofactor
