---
title: CusA Heavy-Metal Efflux RND Transporter (E. coli)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, pump, membrane-protein]
sources: [doi/10.1038##nature09395]
verified: false
---

# CusA Heavy-Metal Efflux RND Transporter (E. coli)

## Overview

CusA is the inner-membrane transporter component of the CusCBA tripartite efflux complex in Escherichia coli, responsible for extruding biocidal Cu(I) and Ag(I) ions. It belongs to the heavy-metal efflux (HME) subfamily of the resistance-nodulation-cell division (RND) superfamily. The crystal structures of CusA in apo, Cu(I)-bound, and Ag(I)-bound forms were determined, providing the first structural information for any HME-RND efflux pump. The structures reveal a homotrimeric architecture with distinct periplasmic (PN1, PN2, PC1, PC2) and transmembrane (DN, DC) subdomains. Metal binding occurs via a three-methionine cluster (M573, M623, M672) within a cleft of the periplasmic domain that is closed in the apo form and opens upon metal binding. Five methionine pairs/clusters (M410/M501, M403/M486, M391/M1009, M271/M755, and the M573/M623/M672 three-methionine site) form a relay network for stepwise metal transport from the cytoplasm through the transmembrane region to the central funnel for extrusion via CusC.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09395 | Not specified in publication | Not specified | R32 | Full-length CusA with N-terminal His6 tag | Apo (no metal bound) |
| doi/10.1038##nature09395 | Not specified in publication | Not specified | R32 | Full-length CusA with N-terminal His6 tag | Cu(I) |
| doi/10.1038##nature09395 | Not specified in publication | Not specified | R32 | Full-length CusA with N-terminal His6 tag | Ag(I) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)ΔacrB cells
- **Construct**: Full-length CusA with N-terminal His6 tag in pET15bΩcusA vector, ampicillin selection, IPTG induction

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Affinity purification | Ni2+ affinity chromatography | — |  | His6-tagged CusA purified by Ni-NTA affinity |
| 2. Size-exclusion chromatography | Gel filtration | — |  | Final polishing step |

**Final sample**: Purified CusA in detergent-containing buffer


## Crystallization

### doi/10.1038##nature09395

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified CusA |
| Reservoir | 10% PEG 3350, 0.1 M Na-MES pH 6.5, 0.4 M (NH4)2SO4, 1% Jeffamine M600, 0.05% (w/v) Cymal-6 |
| Temperature | 25 °C |
| Notes | Apo-CusA, SeMet-CusA crystallized under same conditions. Heavy-atom derivatives: KAuCl4 (1 mM) or Ta6Br12 (5 mM) soaked 1.5 h. CusA-Cu(I): 2 mM [Cu(CH3CN)4]PF6, 2 mM TCEP soaked 1 h. CusA-Ag(I): 1 mM AgNO3 soaked 1 h. Data collected at APS beamline 24ID-C. Rhombohedral R32 space group, one monomer per asymmetric unit. |


## Biological / Functional Insights

### Metal binding via three-methionine cluster in periplasmic cleft

The primary metal-binding site is formed by M573, M623, and M672, located in the cleft region between the PC1 and PC2 subdomains of the periplasmic domain. In the apo state, the cleft is closed. Upon Cu(I) or Ag(I) binding, the PC2 subdomain swings ~30° (hinge at G721/P810) to open the cleft. The horizontal helix (residues 665-675) tilts upward by 21°, allowing M672 to move closer to M573 and M623 to form a transient three-sulfur coordination site. TM8 also shifts vertically by ~10 Å at its N-terminal end.

### Methionine relay network for stepwise metal transport

CusA contains five methionine pairs/clusters that form a relay network: the primary three-methionine site (M573/M623/M672), and four methionine pairs - M271/M755 (periplasmic domain), M391/M1009, M403/M486, and M410/M501 (transmembrane region). CAVER analysis shows these sites form a continuous channel spanning the transmembrane region to the periplasmic funnel. Transport assay mutants (M573I, M623I, M672I, M391I, M486I, M755I) lost Ag+ transport activity, confirming their essential roles. This suggests a stepwise shuttle mechanism where metal ions pass sequentially between methionine pairs.

### Proton-relay network for energy coupling

Conserved charged residues D405 (TM4), E939, and K984 form a potential proton-relay network. Mutants D405A, E939A, and K984A lost Ag+ transport activity in reconstituted liposome assays, confirming their essential role in proton translocation and energy coupling for active metal export.

### Alternating-access mechanism

Dynamics simulations using an elastic network model suggest CusA operates through three coupled motions in which the periplasmic clefts formed by PC1 and PC2 subdomains alternately open and close. This alternating-access mechanism, similar to AcrB, allows coordinated metal ion uptake from both cytoplasm and periplasm and extrusion through the CusC outer-membrane channel.

### Substrate uptake from both cytoplasm and periplasm

The structures suggest CusA can pick up metal ions from both the cytoplasm (via methionine pairs in the transmembrane region that line a channel) and the periplasm (via the open periplasmic cleft). Metal ions bind to the three-methionine site directly through the periplasmic cleft or via the methionine pairs within the transmembrane region, then are transferred stepwise to the M271/M755 pair and released into the central funnel for extrusion through CusC.


## Cross-References
