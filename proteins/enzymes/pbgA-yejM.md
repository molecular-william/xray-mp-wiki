---
title: PbgA (YejM) Inner Membrane LPS Sensor
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##srep30815, doi/10.1038##s41586-020-2597-x]
verified: false
---

# PbgA (YejM) Inner Membrane LPS Sensor

## Overview

[PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) (also known as YejM) is an essential inner membrane protein in Gram-negative bacteria that functions as a sensor of lipopolysaccharide (LPS) levels on the periplasmic leaflet of the inner membrane, coordinating LPS biogenesis by regulating the stability of LpxC, the committed enzyme in [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) biosynthesis. [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) contains five N-terminal transmembrane helices upon which a C-terminal periplasmic globular domain (residues 191-586) sits, connected by a three-helix bundle interfacial domain (IFD). Earlier crystal structures of the isolated periplasmic domain from Salmonella typhimurium and Escherichia coli (Lu et al., 2016, Sci Rep) revealed a fold resembling arylsulfatases and lipoteichoic acid synthases, but lacking their enzymatic activities, and were interpreted as supporting a [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) transport function. However, the full-length crystal structure of [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) determined at 2.0 A resolution (Clairfeuille et al., 2020, Nature) — together with physiological, proteomic, and pharmacological studies — definitively refuted the cardiolipin-transporter model. The full-length structure shows that the periplasmic domain remains anchored onto the TMD (total interdomain contacts ~2,550 A2) and protrudes only ~60 A above the inner membrane, inconsistent with a domain that shuttles across the ~200 A periplasm. Crucially, the structure revealed a lipid A-binding (LAB) motif along the periplasmic leaflet of the inner membrane, formed by the IFD and TMD. [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) binds LPS with remarkable selectivity — recognizing a single phospho-GlcNAc unit of [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) through a backbone-mediated coordination scheme — and does not require divalent cations or basic residues, distinguishing it from known LPS receptors. [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) constitutively associates with LapB, and together they antagonize FtsH-mediated degradation of LpxC when LPS demand is high; when periplasmic LPS accumulates, LPS binding to [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) alters the PbgA-LapB complex and promotes FtsH-dependent LpxC degradation, forming a rheostat that controls LPS synthesis. Synthetic peptides derived from the [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) LAB motif (LAB peptides) selectively bind LPS and exhibit broad-spectrum Gram-negative antibacterial activity, including against polymyxin-resistant strains. [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) is essential for E. coli pathogenesis, outer membrane integrity, and growth.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##srep30815 | unknown | 1.67 | P 31 2 1 | EcPbgA245-586 (E. coli [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) periplasmic domain, residues 245-586) | none |
| doi/10.1038##srep30815 | unknown | 2.19 | P 21 | StPbgA191-586 (S. typhimurium [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) periplasmic domain, residues 191-586) | none |
| doi/10.1038##srep30815 | unknown | 1.64 | P 21 | StPbgA245-586 (S. typhimurium [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) periplasmic domain, residues 245-586) | none |
| doi/10.1038##s41586-020-2597-x | 6XLP | 2.0 | C 2 | Full-length E. coli [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) (residues 1-586) with C-terminal TEV-2xFlag-hexahistidine tag | LPS ([Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/)), [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/), [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| doi/10.1038##s41586-020-2597-x | unknown | 4.6 | P 31 | Full-length E. coli [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) (residues 1-586) with C-terminal TEV-2xFlag-hexahistidine tag | none |

## Expression and Purification

- **Expression system**: Escherichia coli BL21-Gold(DE3)
- **Construct**: Full-length [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) (residues 1-586) with C-terminal TEV-2xFlag-hexahistidine tag

### Purification Workflow

*Source: doi/10.1038##srep30815*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli BL21(DE3) expression | — | LB medium with 50 ug/mL [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) + -- | Induced with 0.1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 12 h at 20 C. |
| Cell lysis | Cell disruption at 30,000 psi | — | 20 mM Tris-Cl pH 7.8, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 500 mM NaCl, cOmplete protease inhibitor, 1 mM DNase, 1 mM PMSF + -- | Debris removed by centrifugation at 120,000 g for 25 min at 4 C. |
| Affinity purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — | 20 mM Tris-Cl pH 7.8, 500 mM NaCl, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + -- | Eluted with 20 mM Tris-Cl pH 7.8, 500 mM NaCl, 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/). Buffer exchanged for further processing. |

### Purification Workflow

*Source: doi/10.1038##s41586-020-2597-x*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli BL21-Gold(DE3) expression | — | TB autoinduction medium + -- | Expression for 48 h at 17 C in autoinduction medium. |
| Cell lysis | Sonication | — | 50 mM Tris pH 8, 300 mM NaCl, 1 ug/mL benzonase, 1 mM PMSF, Roche protease inhibitor tablets + -- | 50 g cell pellet resuspended in 250 mL buffer. |
| Solubilization | Detergent solubilization | — | 50 mM Tris pH 8, 300 mM NaCl + 1% (w/v) [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) or 1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Solubilization for 2 h at 4 C under gentle agitation. Insoluble debris pelleted at 18,000 rpm for 1 h. |
| Affinity purification | M2-agarose Flag resin batch binding | — | 50 mM Tris pH 8, 300 mM NaCl + 0.01% (w/v) [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) or 0.1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Batch binding to 20 mL M2-agarose Flag resin for 2 h at 4 C. Unbound washed with 10 CV of purification buffer. |


## Crystallization

### doi/10.1038##srep30815

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Temperature | 20 |
| Notes | PbgA245-586 from S. typhimurium and E. coli crystallized by [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/). StPbgA191-586 showed degradation and crystallized from the degradation product. |

### doi/10.1038##s41586-020-2597-x

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Temperature | 20 |
| Notes | Full-length [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) crystallized in LCP using [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) as the host lipid. [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) was added to allow high-resolution diffraction. Two crystal forms: C2 at 2.0 A (synchrotron) and P31 at 4.6 A (XFEL, with 7.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/) as viscosity enhancer for injection). |


## Biological / Functional Insights

### PbgA is an LPS sensor, not a cardiolipin transporter

The full-length [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) structure at 2.0 A definitively refutes the earlier model that [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) functions as a [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) transporter. The periplasmic domain remains firmly anchored onto the TMD (~2,550 A2 interdomain contacts) and protrudes only ~60 A above the inner membrane — far short of the ~200 A periplasmic width. The IFD is a compact three-helix bundle, not a simple linker. [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) shows no structural homology to any known transporter. No [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) density was observed in the structure; instead, LPS ([Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/)) was bound.

### Lipid A-binding (LAB) motif on the periplasmic leaflet

[PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) binds LPS selectively through a backbone-mediated coordination scheme at the periplasmic leaflet of the inner membrane. A single phospho-GlcNAc unit of [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) is recognized, distinguishing [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) from other LPS receptors that bind the [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) disaccharide. The binding does not require divalent cations or basic residues. Key residues include R215 which stabilizes the IFD-TMD interface.

### PbgA-LapB complex regulates LpxC stability via FtsH

[PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) constitutively associates with LapB at its TMD. Together they antagonize FtsH-mediated degradation of LpxC when LPS demand is high (e.g., during cell growth). When periplasmic LPS accumulates, LPS binds to [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/), altering the PbgA-LapB interaction and promoting FtsH-dependent degradation of LpxC. This rheostat mechanism coordinates LPS synthesis with demand, maintaining outer membrane integrity. Deletion of [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) leads to growth inhibition, loss of cell shape, membrane bursting, and attenuation of virulence.

### PbgA-derived LAB peptides as broad-spectrum antibiotics

Synthetic peptides derived from the [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) lipid A-binding motif (LAB peptides) selectively bind LPS over phospholipids. Structure-guided optimization produced LABv2.1 with MICs of 12.5-200 uM against clinically relevant Gram-negative pathogens including E. coli, K. pneumoniae, A. baumannii, and P. aeruginosa, including polymyxin-resistant strains. These peptides represent a novel class of LPS-targeting antibiotics.

### PbgA structure resembles hydrolase superfamily

The [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) periplasmic domain is structurally related to a superfamily of cell envelope-modifying enzymes including LtaS (S. aureus lipoteichoic acid synthase) and EptA/MCR-1 (phosphoethanolamine transferases). [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) retains the fold but lacks catalytic residues (pseudo-hydrolase). The IFD aligns with the EptA linker but is reoriented ~180 degrees.

### PbgA co-purifies with LPS but not cardiolipin

Purified full-length [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) specifically co-purifies with various [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) species (tetra-, hexa-acylated, and arabinose-modified forms) as shown by MALDI-TOF mass spectrometry and limulus amebocyte lysate assays. No [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) was detected bound to [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/). In contrast, [LNT](/xray-mp-wiki/proteins/enzymes/lnt/) (a control inner membrane protein) did not co-purify with LPS. PbgA-LPS binding was observed in two crystal forms and supported by molecular dynamics simulations.


## Cross-References

- [Selective Lipid Binding](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/selective-lipid-binding/) — PbgA selectively binds lipid A (LPS) through a backbone-mediated scheme recognizing a single phospho-GlcNAc unit
- [Membrane Mimetics](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/) — PbgA structure was determined in LCP (lipidic cubic phase), a membrane-mimetic system
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Method used in structure determination or purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — Method used in structure determination or purification
- [LNT](/xray-mp-wiki/proteins/enzymes/lnt/) — Related protein structure
- [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA/) — Related protein structure
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
