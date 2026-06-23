---
title: Escherichia coli YidC
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.bbrc.2018.09.043, doi/10.1038##srep07299]
verified: false
---

# Escherichia coli YidC

## Overview

YidC is an essential bacterial membrane protein insertase and chaperone that mediates the insertion and assembly of membrane proteins. It is a member of the conserved YidC/Alb3/Oxa1 family. The crystal structure of full-length E. coli YidC was first determined at 3.2 Å resolution, revealing five transmembrane helices (TM2-6) forming a hydrophilic groove open toward both the cytoplasmic and membrane sides, along with the periplasmic P1 domain and the C1 region. A later higher-resolution structure at 2.8 Å revealed the complete core region including the previously disordered C2 cytoplasmic loop. YidC cooperates with the  translocon complex during membrane protein biogenesis and can also function independently as an insertase.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.bbrc.2018.09.043 | unknown | 2.8 | P1 | Full-length E. coli YidC core region (residues 325-532) | none |
| doi/10.1038##srep07299 | 3WVF | 3.2 | P1 | Full-length E. coli YidC (residues 2-540) with C-terminal His8 tag, TEV-cleavable | none |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length E. coli YidC (residues 2-540) with LE接头SGENLYFQGQFTS-H8 tag

### Purification Workflow

*Source: doi/10.1016##j.bbrc.2018.09.043*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli expression | — | -- + -- | Protein expressed in E. coli cells. |
| Crystallization | Helical Data Collection Method | — | -- + -- | Over 100 crystals used for data collection. 97 datasets merged for final structure determination. Data collected at SPring-8 beamline BL32XU, wavelength 1.00 A, 100 K. |

### Purification Workflow

*Source: doi/10.1038##srep07299*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli expression in BL21(DE3) | — | LB medium with 50 ug/mL  + -- | Cells induced with 1 mM  for 18 h at 37 C. Harvested by centrifugation at 4,500 g for 10 min at 4 C. |
| Membrane preparation | Ultracentrifugation | — | 20 mM -NaOH pH 5.6, 300 mM NaCl, 2%  (), 0.1 mM  + 2%  () | Total membranes prepared as described. YidC solubilized for 1 h at 4 C. Ultracentrifugation at 138,000 g for 30 min at 4 C. |
| Affinity purification | Ni Sepharose excel (IMAC) | — | 20 mM -NaOH pH 5.6, 300 mM NaCl, 0.25%  + 0.25%  () | Batch binding for 30 min at 4 C. Wash with 50 mM . Elution with 100-500 mM  gradient. |
| TEV cleavage | His-tagged [TEV Protease (Tobacco Etch Virus Protease)](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) | — | 20 mM -NaOH pH 5.6, 300 mM NaCl, 0.25% , 10 mM  + 0.25%  | C-terminal His8 tag cleaved by [TEV Protease (Tobacco Etch Virus Protease)](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) for 12 h at 4 C. Flow-through collected from Ni-NTA after cleavage. |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | HiLoad 16/600 Superdex 200 | — | 20 mM -NaOH pH 5.6, 300 mM NaCl, 0.25%  + 0.25%  | Final polishing step. N-terminal sequencing confirmed intact YidC in purified sample. |


## Crystallization

### doi/10.1038##srep07299

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Temperature | 20 |
| Notes | Crystallized by sitting drop vapor diffusion at 20 C. Crystals appeared within 3-7 days. Data collected at BL32XU of SPring-8 at 100 K. Helical data collection method used for small crystals. |


## Biological / Functional Insights

### Structure determination at 2.8 A

The 2.8 A crystal structure of E. coli YidC revealed the complete core region including the previously disordered C2 loop (residues 480-492). The overall structure is nearly identical to the 3.2 A structure (RMSD 0.49 A for Calpha atoms), but additionally reveals previously disordered regions 49-55 and 204-215 in the P1 region.

### C2 loop covers the positively charged cavity

The C2 loop is located at the cytoplasmic entrance of the positively charged cavity and appears to restrict excessive exposure of the cavity. The conserved Arg366 is positioned in the cavity. The C2 loop is highly flexible (B-factor 133 A² vs overall 57.5 A²) and may become dislocated when YidC is in an active form.

### MD simulations show C2 loop dynamics

100-ns MD simulation of YidC embedded in a  bilayer showed high RMSD values for the C2 loop, correlating with high B-factors in the crystal structure. TM5 showed the highest mobility, attributed to its outermost position and fewer intramolecular interactions.

### Functional role of TM5

TM5 lacks a hydrogen bond due to Pro499 positioned in the middle, causing high mobility of the cytoplasmic side (residues 486-498). In contrast, conserved Pro371 and Pro431 in TM2 and TM3 do not show similar fluctuations in MD simulations.

### Hydrophilic groove is a conserved YidC feature

The 3.2 A structure revealed a hydrophilic groove formed by five TM helices (TM2-6), open toward both the cytoplasmic and membrane sides through a gap between TM3 and TM5. The groove contains conserved hydrophilic residues including Thr362, Arg366, Thr373, Gln429, Thr474, Ser520, Asn521 and Gln527. Arg366 generates a positively charged surface in the groove. This groove is a conserved structural feature of YidC, as also observed in BhYidC.

### P1 domain orientation

The P1 domain consists of two antiparallel beta-sheets forming a beta-supersandwich fold, connected to the TM region by the amphipathic PH1 helix. The P1 domain forms hydrogen bonds with the P2 region and TM3 helix, stabilizing its orientation. The cleft in the P1 domain is oriented away from the membrane, suggesting it may bind periplasmic molecules rather than substrate proteins.

### Substrate-contacting sites mapped to groove

Substrate-contacting residues identified by crosslinking map to the exterior surface of the TM region and the interior surface of the hydrophilic groove, particularly near the groove opening at TM3 and TM5. Both Sec-independent substrates (Pf3 coat protein, Foc, MifM) and Sec-dependent substrates (FtsQ) share overlapping contact regions, supporting the groove as a central functional element for both insertase and chaperone activities.

### Structural organization of holo-translocon

The holo-translocon is composed of single copies of YidC,  and SecDFYajC. SecF interacts with part of the P1 domain (residues 215-265), where Lys249 was crosslinked to , SecD and . The highly conserved TM3 surface may provide interaction sites for TM regions of Sec proteins. The lateral gate of  likely faces the hydrophilic groove of YidC in Sec-dependent membrane protein integration.


## Cross-References

- [YidC/Oxa1/Alb3 Insertase Family](/xray-mp-wiki/concepts/yidc-oxa1-alb3-insertase-family/) — YidC is the founding bacterial member of the YidC/Alb3/Oxa1 insertase family
- [Secyeg](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) — Referenced in ec-yidc text
- [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) — Referenced in ec-yidc text
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in ec-yidc text
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in ec-yidc text
- [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/) — Referenced in ec-yidc text
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in ec-yidc text
- [Ada](/xray-mp-wiki/reagents/ada/) — Referenced in ec-yidc text
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in ec-yidc text
- [Popc](/xray-mp-wiki/reagents/lipids/popc/) — Referenced in ec-yidc text
