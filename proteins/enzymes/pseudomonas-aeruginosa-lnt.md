---
title: "Pseudomonas aeruginosa Apolipoprotein N-Acyl Transferase (LntPae)"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.adf5799]
verified: false
---

# Pseudomonas aeruginosa Apolipoprotein N-Acyl Transferase (LntPae)

## Overview

Pseudomonas aeruginosa apolipoprotein N-acyltransferase (LntPae) is a 57 kDa integral membrane enzyme that catalyzes the final step of lipoprotein maturation in Gram-negative bacteria, transferring an acyl chain from a glycerophospholipid (GPL) donor to the N-terminal cysteine of diacylated lipoproteins. LntPae shares 39% sequence identity with E. coli Lnt. The structure was determined by x-ray crystallography (PDB 8AQ2) as a TITC-modified variant in complex with monoolein, capturing a mimic of the second Michaelis complex (M2 state) in the ping-pong reaction mechanism.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##sciadv.adf5799 | 8AQ2 | Not specified (~2.7 A range) | Not specified | Full-length P. aeruginosa Lnt with TITC modification at catalytic Cys | TITC (tetradecyl-1-isothiocyanate), monoolein |

## Expression and Purification

- **Expression system**: E. coli C43(DE3)
- **Construct**: Full-length P. aeruginosa Lnt (514 residues) with N-terminal His6-tag

### Purification Workflow

- **Expression system**: E. coli C43(DE3)
- **Expression construct**: Full-length P. aeruginosa Lnt with N-terminal His6-tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization | — |  | Membranes isolated by centrifugation at 120,000g for 45 min |
| Membrane solubilization | Detergent solubilization | — | Lauryl maltose neopentyl glycol (LMNG) or n-dodecyl-beta-D-maltopyranoside (DDM) | Solubilized for 45 min at room temperature |
| Affinity chromatography | Ni-NTA affinity | Ni-NTA Superflow |  | Washed with buffer containing 40 mM imidazole; eluted with 400 mM imidazole |
| Size-exclusion chromatography | SEC | HiLoad 16/60 Superdex 200 |  | Purified in buffer containing 0.05% (w/v) LMNG or 0.02% (w/v) DDM |


## Crystallization

### doi/10.1126##sciadv.adf5799

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (in meso) |
| Protein sample | TITC-modified LntPae in detergent |
| Lipid | Monoolein |
| Temperature | 20°C |
| Growth time | Varies |
| Notes | Crystallized by in meso method. Data collected at Swiss Light Source. |


## Biological / Functional Insights

### M2 state mimic reveals acyl chain binding sites

The TITC-modified LntPae structure with two monoolein molecules (PDB 8AQ2) represents a mimic of the second Michaelis complex (M2 state). The TITC alkyl chain aligns with the amide-linked acyl chain of the final product, while the two monoolein molecules align with the sn-1 and sn-2 chains of the diacylglyceryl moiety in the TA-BLP product. This structure, together with the other eight structures solved in the study, defines three distinct acyl chain binding sites in Lnt that are occupied to varying degrees throughout the N-acylation reaction.

### Structural conservation across Lnt orthologs

Despite only 39% sequence identity, LntPae and LntEco share highly similar overall architecture with the same nitrilase-like domain (ND) and membrane domain (MD) organization. The active site catalytic triad (Glu267-Lys335-Cys387 in E. coli numbering) is conserved. The structures solved at multiple states along the reaction coordinate validate the ping-pong mechanism and explain substrate promiscuity.


## Cross-References

- [Escherichia coli Apolipoprotein N-Acyl Transferase (Lnt)](/xray-mp-wiki/proteins/enzymes/e-coli-lnt/) — Orthologous Lnt from E. coli with 39% sequence identity; both characterized in the same structural study
- [Ping-Pong Catalytic Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/ping-pong-mechanism/) — Lnt uses ping-pong mechanism for N-acyl transfer; structural snapshots of all states
- [Nitrilase Superfamily](/xray-mp-wiki/concepts/protein-families/nitrilase-superfamily/) — Lnt belongs to the nitrilase superfamily (ninth branch)
