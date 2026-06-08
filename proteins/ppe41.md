---
title: PPE41
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jsb.2015.06.003]
verified: false
---

# PPE41

## Overview

PPE41 is the conserved N-terminal domain of the PPE (Pro-Pro-Glu) protein family from Mycobacterium tuberculosis. PPE41 forms a heterodimer with PE25 through a four-helix bundle interface, creating an elongated all-helical structure characteristic of ESX-secreted substrates. The PPE41 protein contains a characteristic hh motif (residues D121-T129) that serves as the binding site for EspG chaperones. PPE41 is secreted by the ESX-1 type VII secretion system as part of the PE25-PPE41 heterodimer and is essential for mycobacterial virulence.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jsb.2015.06.003 | 2G38 | 2.0 A | Not specified | PE25-PPE41 heterodimer (N-terminal domains only, lacking C-terminal regions) | None |
| doi/10.1016##j.jsb.2015.06.003 | 4KXR | Not specified | Not specified | PE25-PPE41-EspG5 complex | EspG5 chaperone |
| doi/10.1016##j.jsb.2015.06.003 | 4W4L | Not specified | Not specified | PE25-PPE41-EspG5 complex | EspG5 chaperone |

## Expression and Purification

- **Expression system**: Not specified in this paper
- **Construct**: PPE41 N-terminal domain as part of PE25-PPE41 heterodimer

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Not specified | Not specified | -- | -- + -- | Purification details not described in this paper; original structure determined by Strong et al. (2006) PNAS 103:8060-8065 |


## Crystallization

### doi/10.1016##j.jsb.2015.06.003

| Parameter | Value |
|---|---|
| Method | Not specified in this paper |
| Protein sample | PE25-PPE41 heterodimer |
| Reservoir | -- |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Original crystallization described in Strong et al. (2006) PNAS 103:8060-8065 |


## Biological / Functional Insights

### PPE41 contains the EspG chaperone-binding site

PPE41 contains a characteristic hh motif (residues D121-T129) that mediates binding to EspG chaperones. The EspG chaperone binds specifically to this conserved motif on PPE41, protecting the hydrophobic regions of the PE-PPE heterodimer from self-polymerization. EspG chaperones are essential for PE-PPE heterodimer folding, stability, and targeting to the cognate ESX secretion machinery. The alpha4-alpha5 loop of PPE proteins, which contains the hh motif, is highly conserved in length and sequence among PPE family members.

### PPE41 contributes helices to the PE-PPE heterodimer bundle

In the PE25-PPE41 heterodimer, PPE41 contributes two alpha-helices to the four-helix bundle interface. Helix alpha1 of PPE41 corresponds to helix alpha3 of the related EspB protein. The conserved Trp56 (W56) of PPE41 makes van der Waals contacts with Y87 of PE25 in the heterodimer interface. The length and sequence of the alpha4-alpha5 loop of PPE proteins are highly conserved, distinguishing them from the variable corresponding region in EspB homologs.

### YxxxD/E secretion motif in PE25-PPE41 complex

The YxxxD/E secretion motif is present in PE25 (part of the PE-PPE heterodimer). In the isolated heterodimer structures (PDB 2G38, 4W4K), the motif is partially disordered. However, in the PE25-PPE41-EspG5 complex structures (PDB 4KXR, 4W4L), the motif adopts a helical conformation, suggesting that chaperone binding stabilizes the secretion-competent conformation.


## Cross-References

- [PE25](/xray-mp-wiki/proteins/pe25/) — PPE41 forms the heterodimer partner of PE25 in the canonical PE-PPE complex
- [EspB](/xray-mp-wiki/proteins/espB/) — EspB structure structurally resembles the PE25-PPE41 heterodimer despite being a single-chain fusion
- [PE-PPE Fusion Proteins](/xray-mp-wiki/concepts/pe-ppe-fusion-proteins/) — PPE41 is the PPE domain component of the canonical PE-PPE heterodimer architecture
- [ESX-1 Secretion System](/xray-mp-wiki/concepts/esx-1-secretion-system/) — PPE41 is a secreted substrate of the ESX-1 type VII secretion system as part of PE25-PPE41
- [EspG1](/xray-mp-wiki/proteins/espg1/) — EspG chaperones bind the hh motif on PPE41 for heterodimer folding and secretion
