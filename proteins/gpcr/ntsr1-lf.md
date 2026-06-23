---
title: "NTSR1-LF Mutant"
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms8895]
verified: false
---

# NTSR1-LF Mutant

## Overview

NTSR1-LF is a thermostabilized mutant of the [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) receptor 1 ([NTSR1](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/)) containing two point mutations: wild-type L310(6.37) and wild-type F358(7.42), but lacking the E166(3.49) residue (replaced by the thermostabilizing mutation E166A found in the parent NTSR1-GW5 construct). The construct retains wild-type residues at positions 6.37 and 7.42, enabling moderate G-protein activation ability. The structure was determined at 2.6 A resolution (space group P212121), slightly higher resolution than NTSR1-ELF. NTSR1-LF is able to catalyze nucleotide exchange at Galphaq at a moderate level, likely because of the absence of the E166(3.49) side chain which is critical for full G-protein activation. The structure was obtained with T4 lysozyme ([T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)) fusion replacing most of ICL3 for crystallization.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms8895 | 4XEE | 2.6 A | P212121 | NTSR1-LF-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/): Wild-type residues at positions L310(6.37), F358(7.42); E166A mutation at position 3.49; T4 lysozyme replacing most of ICL3 (residues H269-R299); expressed in Sf9 insect cells via baculovirus
 | NTS(8-13) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: NTSR1-LF-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) construct with wild-type residues at positions 6.37, 7.42; E166A mutation at 3.49; T4 lysozyme replacing most of ICL3 (residues H269-R299)


### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 insect cells | — | Not specified | NTSR1-LF construct produced in insect cells |
| Membrane preparation | Urea-washed P2 insect cell membranes | — | Not specified | Membranes washed with [UREA](/xray-mp-wiki/reagents/substrates/urea/) to reduce background binding |
| Solubilization | [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/CHS detergent | — | 1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Solubilized in [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/CHS with [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) peptide |
| Purification | Ni-NTA affinity ([TALON](/xray-mp-wiki/reagents/additives/talon/) resin) | — | 50 mM TrisHCl pH 7.4, 200 mM NaCl, 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Batch incubation with [TALON](/xray-mp-wiki/reagents/additives/talon/) resin; eluted with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Desalting | PD10 column | — | 50 mM TrisHCl pH 7.4, 200 mM NaCl, 0.003% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0003% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Desalted and NTS(8-13) added to 20 uM |


## Crystallization

### doi/10.1038##ncomms8895

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Notes | NTSR1-LF-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) crystallized in lipidic cubic phase (LCP) with cholesteryl hemisuccinate ([CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)) additive. Crystals in space group P212121. Resolution 2.6 A. The LCP method with [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/CHS mixed micelles enabled crystallization of the active-like conformation.
 |


## Biological / Functional Insights

### Moderate G-protein activation without E166(3.49)

NTSR1-LF has moderate ability to activate Gq protein compared to NTSR1-ELF which shows near wild-type activity. The absence of E166(3.49) in NTSR1-LF is the primary reason for reduced G-protein activation ability, as E166(3.49) is critical for governing receptor conformation and G-protein recognition.

### W321(6.48) rotamer sealing collapsed Na+ pocket

Like NTSR1-ELF, NTSR1-LF shows the conserved W321(6.48) adopting a side chain rotamer orientation parallel to the lipid bilayer, sealing the top of the collapsed Na+ ion-binding pocket. This conformation is enabled by the presence of F358(7.42) and has not been observed in other GPCR structures to date.

### R167(3.50) positioning by L310(6.37)

The bulkier L310(6.37) side chain sterically prevents R167(3.50) from adopting the conformation seen in NTSR1-GW5. Instead, R167(3.50) adopts an orientation similar to that found in the beta2AR-Gs complex, the active M2 receptor, and [OPSIN](/xray-mp-wiki/proteins/gpcr/opsin/) in its G-protein-interacting conformation.


## Cross-References

- [Rat Neurotensin Receptor 1 (NTSR1)](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/) — NTSR1-LF is a mutant derivative of NTSR1 with wild-type residues at positions 6.37, 7.42
- [NTSR1-EL Constitutively Active Mutant](/xray-mp-wiki/proteins/gpcr/ntsr1-el/) — Related constitutively active mutant with F358A; used for comparative structural analysis of constitutive activity
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion replacing ICL3 in NTSR1-LF-T4L crystallization construct
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for solubilization and purification of NTSR1-LF-T4L
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — CHS used in combination with LMNG for solubilization and in LCP crystallization
- [OPSIN](/xray-mp-wiki/proteins/gpcr/opsin/) — Related protein structure
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [TALON](/xray-mp-wiki/reagents/additives/talon/) — Additive used in purification or crystallization buffers
- [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) — Related ligand or cofactor
- [UREA](/xray-mp-wiki/reagents/substrates/urea/) — Entity mentioned in text
