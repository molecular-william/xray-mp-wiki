---
title: NTSR1-ELF Mutant
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms8895]
verified: false
---

# NTSR1-ELF Mutant

## Overview

NTSR1-ELF is a thermostabilized mutant of the neurotensin receptor 1 (NTSR1) containing three point mutations: E166A (3.49), L310A (6.37) was replaced by wild-type L310, and F358A (7.42) was replaced by wild-type F358. The construct retains the wild-type sequence at positions 3.49, 6.37, and 7.42, making it capable of activating Gq protein to near wild-type levels. The structure was determined at 2.9 A resolution (PDB to be assigned, space group P212121). NTSR1-ELF is able to stimulate nucleotide exchange at Galphaq in response to the agonist neurotensin peptide NTS(8-13), and contains a T4 lysozyme (T4L) fusion replacing most of the third intracellular loop (ICL3) for crystallization. The key structural findings include the conserved W321(6.48) adopting a rotamer orientation parallel to the lipid bilayer, sealing the collapsed Na+ ion-binding pocket, and the R167(3.50) side chain adopting an orientation similar to active GPCR-G protein complexes. The E166(3.49) residue provides critical determinants for G-protein activation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms8895 | Not specified (see main paper) | 2.9 A | P212121 | NTSR1-ELF-T4L: Wild-type residues at positions E166(3.49), L310(6.37), F358(7.42); T4 lysozyme replacing most of ICL3 (residues H269-R299); expressed in Sf9 insect cells via baculovirus
 | NTS(8-13) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: NTSR1-ELF-T4L construct with wild-type residues at positions 3.49, 6.37, 7.42; T4 lysozyme replacing most of ICL3 (residues H269-R299)


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 insect cells | — | Not specified | NTSR1-ELF construct produced in insect cells |
| Membrane preparation | Urea-washed P2 insect cell membranes | — | Not specified | Membranes washed with urea to reduce background binding |
| Solubilization | LMNG/CHS detergent | — | 1% LMNG, 0.1% CHS | Solubilized in LMNG/CHS with neurotensin peptide |
| Purification | Ni-NTA affinity (Talon resin) | — | 50 mM TrisHCl pH 7.4, 200 mM NaCl, 0.05% LMNG, 0.005% CHS | Batch incubation with Talon resin; eluted with 250 mM imidazole |
| Desalting | PD10 column | — | 50 mM TrisHCl pH 7.4, 200 mM NaCl, 0.003% LMNG, 0.0003% CHS | Desalted and NTS(8-13) added to 20 uM |


## Crystallization

### doi/10.1038##ncomms8895

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Notes | NTSR1-ELF-T4L crystallized in lipidic cubic phase (LCP) with cholesteryl hemisuccinate (CHS) additive. Crystals in space group P212121. Resolution 2.9 A. The LCP method with LMNG/CHS mixed micelles enabled crystallization of the active-like conformation.
 |


## Biological / Functional Insights

### E166(3.49) critical for G-protein activation

The glutamic acid at position 3.49 of the D/ERY motif is critical for G-protein coupling. NTSR1-ELF retains wild-type E166 and shows near wild-type ability to stimulate nucleotide exchange at Galphaq. In contrast, NTSR1-LF (which lacks E166) shows only moderate G-protein activation ability.

### W321(6.48) rotamer sealing collapsed Na+ pocket

The conserved W321(6.48) adopts a side chain rotamer orientation parallel to the lipid bilayer, sealing the top of the collapsed Na+ ion-binding pocket. This rotamer conformation has not been observed in any other GPCR structures to date and is enabled by the presence of F358(7.42).

### R167(3.50) positioning by L310(6.37)

The bulkier L310(6.37) side chain sterically prevents R167(3.50) from adopting the conformation seen in NTSR1-GW5. Instead, R167(3.50) adopts an orientation similar to that found in the beta2AR-Gs complex, the active M2 receptor, and opsin in its G-protein-interacting conformation.


## Cross-References

- [Rat Neurotensin Receptor 1 (NTSR1)](/xray-mp-wiki/proteins/neurotensin-receptor-1/) — NTSR1-ELF is a mutant derivative of NTSR1 with wild-type residues at positions 3.49, 6.37, 7.42
- [NTSR1-LF Mutant](/xray-mp-wiki/proteins/ntsr1-lf/) — Related mutant lacking E166(3.49); used for comparative structural analysis
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion replacing ICL3 in NTSR1-ELF-T4L crystallization construct
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for solubilization and purification of NTSR1-ELF-T4L
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/additives/cholesteryl-hemisuccinate/) — CHS used in combination with LMNG for solubilization and in LCP crystallization
