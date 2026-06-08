---
title: FlaK (Preflagellin Peptidase from Methanococcus maripaludis)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10218]
verified: false
---

# FlaK (Preflagellin Peptidase from Methanococcus maripaludis)

## Overview

FlaK is a preflagellin peptidase (PFP) from the archaeon Methanococcus maripaludis. It belongs to the GXGD family of polytopic membrane proteases that cleave type-II (N_in-C_out) membrane protein substrates using a pair of essential aspartyl residues. FlaK processes preflagellin leader peptides before flagellin incorporation into the archaeal flagellum. The crystal structure reveals six transmembrane helices with the GXGD motif positioned at the center of the transmembrane bundle.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10218 | Not specified in this paper | 3.6 A | Not specified | Full-length FlaK (MmarC6_0338) from M. maripaludis strain C6 | None |

## Expression and Purification

- **Expression system**: E. coli Rosetta 2 (DE3) cells
- **Construct**: MmarC6_0338 encoding FlaK with N-terminal His6-tag and Gly-Ser-Gly-Ser linker between thrombin site and FlaK sequence, cloned into pET-28a
- **Notes**: Se-Met substituted version expressed in M9 minimum media supplemented with Se-Met, induced by 1 mM IPTG at A600 of 0.6, grown at 20 deg.C for 16 h

### Purification Workflow

- **Expression system**: E. coli Rosetta 2 (DE3)
- **Expression construct**: His6-tagged FlaK with Gly-Ser-Gly-Ser linker for thrombin cleavage
- **Tag info**: His6-tag, removed by thrombin cleavage overnight at 22 deg.C

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Spheroplast method | -- | 50 mM sodium phosphate pH 7.2, 500 mM NaCl, 5 mM beta-mercaptoethanol, complete protease inhibitor cocktail (Roche, without EDTA) + -- | Cytoplasmic membranes prepared from M. maripaludis strain C6 genomic DNA expression |
| Solubilization | Detergent solubilization | -- | 50 mM sodium phosphate pH 7.2, 500 mM NaCl, 5 mM beta-mercaptoethanol + 1% (w/v) foscholine-12 (Anatrace) | Membrane suspension solubilized by adding foscholine-12 powder |
| Affinity chromatography | TALON metal-affinity chromatography | TALON (Clontech) | 50 mM sodium phosphate pH 7.2, 500 mM NaCl, 200 mM imidazole, 5 mM beta-mercaptoethanol, 0.1% foscholine-12 + 0.1% foscholine-12 | His-tagged protein eluted from TALON column |
| Desalting | Desalting column | Sephadex G-25 | -- + -- | Sample passed through Sephadex G-25 desalting column before thrombin cleavage |
| Tag cleavage | Proteolytic cleavage | -- | -- + -- | Thrombin cleavage overnight at 22 deg.C to remove N-terminal His tag |
| Size-exclusion chromatography | SEC | Superdex-200 (GE Healthcare) | 20 mM HEPES pH 7.3, 100 mM NaCl, 1 mM TCEP, 0.1% foscholine-12 + 0.1% foscholine-12 | Final purification step |

**Final sample**: Concentrated to approximately 10 mg/ml for crystallization


## Crystallization

### doi/10.1038##nature10218

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Se-Met substituted FlaK at 4 mg/ml (lower concentration due to precipitation during dialysis) |
| Reservoir | 30% PEG 300, 50 mM glycine pH 9.5, 100 mM NaCl |
| Mixing ratio | 1:1 (1 ul protein + 1 ul well solution) |
| Temperature | 22 deg.C |
| Growth time | Needle-shaped crystals appeared in 2 days, full size in 1 week |
| Cryoprotection | Dehydrated by equilibrating 24 h against well solution with 40% PEG 300, then flash-frozen in liquid nitrogen |
| Notes | Data collected at NSLS (X25, X29) and APS (24-ID-C, E). Structure determined by Se-Met SAD phasing. |


## Biological / Functional Insights

### GXGD protease active site architecture

The two aspartyl residues essential for catalysis (Asp 18 and Asp 79) are located at the ends of TM helices alpha1 and alpha4, respectively. The GXGD motif (containing Asp 79) and helix 4 are positioned at the center of the transmembrane bundle, surrounded by other TM helices. The conserved asparagine on alpha5 (Asn 120) forms a hydrogen bond with the carbonyl oxygen of Gly 220 from the extended segment between alpha6 and alpha6a, which would be unfavorably exposed to lipid if the carboxy-terminus were positioned elsewhere.

### Conformational switching mechanism

The 12 A gap between Asp 18 and Asp 79 in the crystal structure suggests FlaK can adopt an inactive conformation where the two catalytic aspartyl residues are structurally uncoupled. Crosslinking experiments with M2M between Cys 25 (alpha2) and Cys 206 (alpha6) bridged this gap and maintained activity, while crosslinking that prevented movement of Asp 18 and Asp 79 toward each other completely eliminated activity. This conformational switching behavior parallels that of presenilin, where the two catalytic aspartates also do not closely oppose each other in all conformations.

### Membrane tilting and constriction

The tilted arrangement of TM helices accommodates unusual peripheral structures (alpha4a and alpha6a) and prevents charged groups (Asp 26, Asp 49, Asp 225) from entering the hydrophobic membrane region. Tyrosine and tryptophan residues cluster at the water-lipid interface, marking the membrane boundaries. The tilted model requires the membrane to constrict around the protease, a feature previously thought unique to intramembrane proteases.

### Evolutionary relationship to presenilin

Comparison of FlaK with presenilin models reveals that TM1, TM4, and TM6 of FlaK are equivalent to presenilin TM6, TM7, and TM9, respectively. Both proteases house their active sites in open hydrophilic cavities surrounded by TM segments carrying catalytic aspartates and a C-terminal TM segment with conserved motifs. This structural similarity reinforces the evolutionary relationship between prokaryotic GXGD proteases and the human presenilin-gamma-secretase complex.


## Cross-References

- [GXGD Proteases](/xray-mp-wiki/concepts/gxgd-proteases/) — FlaK is the prototypic GXGD family member whose structure was solved
- [Signal Peptide Peptidase A from Escherichia coli](/xray-mp-wiki/proteins/sppa-ec/) — Related signal peptidase family member
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Se-Met SAD phasing used for structure determination
- [Single-Wavelength Anomalous Diffraction](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — SAD phasing method used for structure solution
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Crystallization method used for FlaK
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC on Superdex-200 used for final purification
