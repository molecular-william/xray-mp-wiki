---
title: A. thaliana STP10
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##s41467-018-08176-9, doi/10.1038##s41477-021-00992-0]
verified: false
---

# A. thaliana STP10

## Overview

A. thaliana STP10 is a high-affinity [Glucose](/xray-mp-wiki/reagents/additives/glucose/)/H+ symporter from the Sugar Transport Protein (STP) family in Arabidopsis thaliana. It belongs to the major facilitator superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/)) and is responsible for proton-coupled uptake of monosaccharides from the apoplast into plant cells. STP10 is expressed in pollen tubes and plays crucial roles in plant organ development, stress responses, and defense against fungal pathogens. Two X-ray crystal structures were determined: an outward-occluded conformation at 1.8 A resolution (PDB: 7AAQ) and an inward-open conformation at 2.6 A resolution (PDB: 7AAR), both with [Glucose](/xray-mp-wiki/reagents/additives/glucose/) and protons bound.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41477-021-00992-0 | 7AAQ | 1.8 | C2 | Full-length STP10 (wild type) | [Glucose](/xray-mp-wiki/reagents/additives/glucose/) |
| doi/10.1038##s41477-021-00992-0 | 7AAR | 2.6 | — | STP10 E162Q D344N double mutant (inward-open conformation) | [Glucose](/xray-mp-wiki/reagents/additives/glucose/) |
| doi/10.1038##s41467-018-08176-9 | 6H7D | 2.4 | C2 | Full-length STP10 (residues 21-507 of 514) with C-terminal deca-His tag | [Glucose](/xray-mp-wiki/reagents/additives/glucose/) |

 - R-work 24.3%, R-free 26.8%

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae EBY.VW4000
- **Construct**: Full-length STP10 with C-terminal His6 tag in pDR196 vector
- **Notes**: Expressed in hexose-transport-defective yeast strain EBY.VW4000

### Purification Workflow

- **Expression system**: Saccharomyces cerevisiae EBY.VW4000

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Differential centrifugation | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl | Cells harvested and lysed; membranes collected by ultracentrifugation |
| Solubilization | Detergent extraction | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl + 1% n-decyl-β-D-maltopyranoside (DM) | Membranes solubilized for 1 h at 4°C |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA agarose | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl + 0.05% DM | Wash with 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), elute with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | SEC | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl + 0.05% DM | Detergent exchanged to NG/OG for crystallization |

**Final sample**: STP10 in 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl, NG/OG


## Crystallization

### doi/10.1038##s41477-021-00992-0

| Parameter | Value |
|---|---|
| Method | LCP |
| Protein sample | Purified STP10 in NG/OG |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (9.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/)) |
| Protein-to-lipid ratio | 2:3 |
| Temperature | 293 |
| Growth time | 2-4 weeks |
| Notes | Crystals appeared using the sitting-drop LCP method |


## Biological / Functional Insights

### Proton-coupled transport mechanism

Glu162 was identified as the proton donor/acceptor residue essential for proton-coupled [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transport in STP10. In the outward-occluded state, Glu162 is protonated, while in the inward-open state it is deprotonated. This protonation switch is coupled to conformational changes in the transport cycle, providing a detailed molecular basis for proton-to-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) coupling in the STP family.

### Sugar binding site

[Glucose](/xray-mp-wiki/reagents/additives/glucose/) is bound in a central cavity between the N- and C-domains of STP10. Key residues involved in [Glucose](/xray-mp-wiki/reagents/additives/glucose/) coordination include Asp42, Asn46, Glu170, Arg264, Trp388, Asn392 and Trp488. The 1.8 A outward-occluded structure reveals detailed hydrogen bonding networks between [Glucose](/xray-mp-wiki/reagents/additives/glucose/) and these conserved residues.

### Intracellular gate regulation

The intracellular gate is formed by a network of salt bridges involving Glu162, Arg169, Asp344, Arg422 and Glu415. These interactions maintain the structural integrity of the ICH domain and regulate the opening and closing of the intracellular gate during the transport cycle. The double mutant E162Q/D344N was used to capture the inward-open state.

### Conserved structural elements

STP10 has 12 transmembrane helices organized into N-domain (TM1-TM6) and C-domain (TM7-TM12), with a Lid domain and intracellular helical (ICH) domain characteristic of the STP subfamily. A conserved disulfide bridge between the Lid domain and C-domain is present in all STPs. Structural elements and key residues are perfectly conserved across plant STPs.

### Lid domain and disulfide bridge regulation

The Lid domain is a unique extracellular domain in STPs that locks the mobile transmembrane domains through a conserved disulfide bridge (Cys77-Cys449). A cluster of aromatic residues (Phe55, Phe59, Phe60, Phe79, Phe87, Trp202) isolates the proton donor/acceptor pair from the extracellular space, maintaining Asp42 protonation during transport. Breaking the disulfide bridge (C77A, C449A mutants) makes the protein sensitive to alkaline pH, functioning only at pH < 5. The equivalent mutation in wheat Lr67 reintroduces pathogen susceptibility, highlighting the physiological importance of the Lid domain in plant defense.

### Proton donor/acceptor pair and high affinity glucose binding

Asp42 and Arg142 form the proton donor/acceptor pair essential for proton-coupled glucose transport. Asp42 is located on the flexible M1b helix flanked by 6 glycine residues, giving it high flexibility. At low pH (crystallization at pH 4.5), Asp42 is protonated. The μM affinity of STP10 for glucose is achieved through tight hydrophobic interactions with Phe39 and Leu43 in the N-domain, a feature not found in bacterial or human sugar transporters. The L43A mutation reduces affinity from μM to mM range (Km 391 μM), demonstrating that hydrophobic interaction is a key contributor to high affinity.

### Substrate specificity

STP10 transports D-glucose with high affinity and can also transport the non-metabolized glucose analog 2-deoxyglucose. It shows sensitivity to only some inhibitors known from bacterial and human sugar transport. The C-domain polar interactions (Q295, N301, N332) recognize specific hydroxyl groups of glucose, mediating substrate specificity.


## Cross-References

- [A. thaliana SWEET1](/xray-mp-wiki/proteins/miscellaneous/a-thaliana-sweet1/) — Both are plant sugar transporters from Arabidopsis thaliana, solved by X-ray crystallography
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) — STP10 belongs to the MFS family of secondary active transporters
- [Lid Domain in Sugar Transport Proteins (STPs)](/xray-mp-wiki/concepts/transport-mechanisms/lid-domain/) — STP10 structure revealed the Lid domain, a conserved feature of all STPs
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in purification or crystallization
- [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) — Buffer component in purification or crystallization
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [MAG](/xray-mp-wiki/reagents/lipids/mag/) — Additive used in purification or crystallization buffers
