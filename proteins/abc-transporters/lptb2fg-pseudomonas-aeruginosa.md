---
title: Pseudomonas aeruginosa LptB2FG LPS Extraction Complex
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3399]
verified: false
---

# Pseudomonas aeruginosa LptB2FG LPS Extraction Complex

## Overview

LptB2FG is an ATP-binding cassette (ABC) transporter complex responsible for extracting lipopolysaccharide (LPS) molecules from the outer leaflet of the inner membrane and transporting them to the periplasmic chaperone LptC in Gram-negative bacteria. The complex consists of two copies of the cytoplasmic ATPase LptB and two transmembrane proteins, LptF and LptG, each containing six transmembrane helices and a periplasmic beta-jellyroll-like domain. The crystal structure of nucleotide-free LptB2FG from Pseudomonas aeruginosa reveals a large outward-facing V-shaped cavity formed by the LptF and LptG transmembrane domains, which is proposed to accommodate the [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) moiety of LPS. The structure represents a resting state distinct from classical ABC transporters that transport substrates across the membrane.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.3399 | 5X5Y | 3.46 | P2(1)2(1)2(1) | Pseudomonas aeruginosa LptB with C-terminal hexahistidine tag, LptF, and LptG co-expressed |  |

## Expression and Purification

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: C-terminal hexahistidine-tagged LptB co-expressed with untagged LptF and LptG using pQLink vectors
- **Induction**: 0.1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 20 degC overnight
- **Media**: LB medium

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press |  | 20 mM Tris, pH 8.0, 150 mM NaCl | Single passage at 16,000 psi; debris removed by centrifugation at 18,000 rpm for 1 hour; total membranes collected |
| Membrane solubilization | Detergent solubilization |  | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), pH 8.0, 300 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Solubilized for 1 hour at 4 degC; supernatant collected by centrifugation at 18,000 rpm for 1 hour |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), pH 8.0, 150 mM NaCl, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted from Ni-NTA agarose beads |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 (GE Healthcare) | 20 mM Tris, pH 7.5, 150 mM NaCl + 0.06% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Used for ATPase activity assays; protein concentrations determined by Bradford assay |


## Crystallization

### doi/10.1038##nsmb.3399

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | LptB2FG complex |
| Reservoir | 0.1 M HEPES, pH 7.0 |
| Temperature | 4 degC |
| Notes | 1 ul protein mixed with 1 ul reservoir solution. Best crystals obtained in solution containing 0.1 M HEPES pH 7.0. |


## Biological / Functional Insights

### LPS extraction mechanism by LptB2FG

The nucleotide-free LptB2FG structure reveals a large V-shaped cavity (approximately 25 A x 45 A at the membrane-periplasm interface, 10 A deep) formed by the 12 TM helices of LptF and LptG, which are all bent outward. The inner surface of the IM cavity is hydrophobic, while the IM-periplasm interface is positively charged, suggesting the cavity accommodates the hydrophobic fatty acyl chains and negatively charged phosphate groups of [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/). Limited van der Waals contacts between LptF TM1-LptG TM5 and LptF TM5-LptG TM1 suggest these interfaces may open further upon ATP binding to allow LPS lateral entry from the IM outer leaflet. Mutational analysis of conserved hydrophobic residues lining the cavity caused growth defects in E. coli, supporting the cavity's role in LPS binding.

### Coupling helices and LptB interactions

The coupling helices connecting TM2 and TM3 of LptF and LptG each interact with one LptB subunit on the cytoplasmic side. Residues LptF(S83, E84, V87) and LptG(N82, E84) contribute hydrogen bonds to LptB, supported by van der Waals contacts (V87 of LptF, I87 of LptG with F90 of LptB). Complementation assays showed that E84K mutation in LptF_Ec and E88K in LptG_Ec were lethal. The LptB dimer in the nucleotide-free structure resembles the inward-facing state of canonical ABC exporters; ATP binding is predicted to induce dimerization and closure similar to that seen in E. coli AMP-PNP-bound LptB, potentially enlarging the cavity for LPS loading.


## Cross-References

- [LptB2FGC LPS Transport Complex](/xray-mp-wiki/proteins/abc-transporters/lptb2fgc-complex/) — Related LPS transport complex from Enterobacter cloacae and Vibrio cholerae that includes the accessory protein LptC
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Used in crystallization reservoir at 0.1 M, pH 7.0
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used at 1% for membrane solubilization and 0.06-0.1% in purification buffers
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) — Additive used in purification or crystallization buffers
