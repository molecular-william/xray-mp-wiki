---
title: T4 Lysozyme (T4L)
created: 2026-06-05
updated: 2026-06-05
type: reagent
category: reagents
layout: default
tags: [protein-tag, subdirectory-protein-tags]
sources: [doi/10.1021##acs.jmedchem.5b00892, doi/10.1021##acs.jmedchem.7b01722, doi/10.1038##nature10867, doi/10.1038##nature11558, doi/10.1038##nature11701, doi/10.1038##nature12357, doi/10.1038##nature14656, doi/10.1038##nature22309, doi/10.1038##nchembio.2547, doi/10.1038##ncomms8895]
verified: false
---

# T4 Lysozyme (T4L)

## Overview

T4 lysozyme (T4L) is a fusion partner protein used to replace flexible intracellular loops (ICLs) of GPCRs to facilitate crystallization. Unlike BRIL which replaces ICL3, T4L has been inserted into ICL2 of certain GPCRs. The T4L fusion provides a rigid, well-folded helical bundle that replaces the disordered intracellular loop, improving construct stability and enabling crystallization. T4L was originally developed by Palczewski et al. for rhodopsin crystallization and has since been used for several other GPCR targets.


## Properties

- **Chemical name**: T4 lysozyme
- **Class**: fusion partner protein
- **Source organism**: Bacteriophage T4
- **Fusion strategy**: T4 lysozyme is inserted into an intracellular loop of the GPCR, replacing the flexible loop with a rigid helical bundle. In the mGlu5-StaR construct, T4L was inserted into ICL2 between Lys678 and Lys679. In PAR1, T4L was inserted between A301 and A303 in ICL3. The fusion is connected via linker sequences on both sides. T4L provides a crystallization handle with a well-defined surface for crystal contacts.

- **Size**: ~16.5 kDa

## Use in Membrane Protein Work

### GPCR crystallization construct stabilization

T4L replaces ICL2 in mGlu5-StaR construct, providing a rigid scaffold that enables crystallization of the mGlu5 transmembrane domain. The T4L insertion was combined with ECD (residues 2-568) and C-terminus (residues 833-1153) truncation, six thermostabilizing mutations, and TMD-only construct to enable LCP crystallization.


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| Metabotropic Glutamate Receptor 5 (mGlu5) | not specified | T4L inserted into ICL2 between Lys678 and Lys679 in mGlu5-StaR TMD construct (residues 569-832). Enabled LCP crystallization of mGlu5 in complex with NAMs.
 | Enabled LCP crystallization of mGlu5 in complex with NAMs (PDB 5CGC, 5CGD)
 |
| M3 Muscarinic Acetylcholine Receptor | not specified | T4L inserted into ICL3 replacing M3 residues 259-482 in rat M3 receptor crystallization construct (M3-crys). Multiple T4L variants tested: wtT4L (PDB 4DAJ, 3.4 A), dsT4L (PDB 4U14, 3.6 A), mT4L (PDB 4U15, 2.8 A). mT4L variant eliminated epitaxial twinning.
 | T4L fusion enabled first crystal structures of M3 muscarinic receptor at resolutions 2.8-3.4 A
 |
| Rat Neurotensin Receptor 1 (NTSR1) | not specified | T4L inserted into ICL3 replacing NTSR1 residues H269-R299 in NTSR1-GW5-T4L construct. The thermostabilized GW5 mutant contains six point mutations (A86L, E166A, G215A, L310A, F358A, V360A). T4L provided crystallographic contacts enabling structure determination at 2.80 A resolution.
 | Enabled crystal structure of neurotensin receptor in complex with agonist NTS(8-13)
 |
| [Human Protease-Activated Receptor 1 (PAR1)](/xray-mp-wiki/proteins/par1/) | not specified | T4L inserted between A301 and A303 in ICL3 of human PAR1 construct. The PAR1 construct also included N-terminal FLAG epitope, TEV cleavage site between P85 and A86 (N-terminus before P85 removed by TEV protease), 10xHis tag after S395, and glycosylation mutations N250G and N259S in ECL2. T4L provided a rigid crystallization handle. Lattice packing showed T4L packed against extracellular loops, but molecular dynamics simulations confirmed that ECL loop structures did not change when T4L was removed.
 | Enabled crystal structure of human PAR1 in complex with vorapaxar at 2.20 A resolution (PDB 4MB0). The T4L fusion was critical for obtaining well-ordered crystals in space group P212121.
 |
| Human Protease-Activated Receptor 2 (PAR2) - Stabilized T4L Fusion | not specified | T4L inserted between F58 and F59 in N terminus of PAR2-StaR, replacing residues 1-54 (NDelta57). The PAR2-StaR T4L fusion construct also included nine thermostabilizing mutations, ICL3 cytochrome b562RIL insertion, N222Q mutation, and C-terminal truncation after K377. T4L provided crystal contacts in the triclinic P1 crystal lattice.
 | Enabled crystal structures of PAR2 with AZ8838 (2.80 A, PDB 5IRV), AZ3451 (3.59 A, PDB 5IRW), and MAB3949 Fab (4.00 A, PDB 5IRX).
 |
| Guinea Pig Leukotriene B4 Receptor 1 (BLT1) | not specified | T4L was fused at intracellular loop 3 (ICL3) of a thermostabilized guinea pig BLT1 mutant (lacking residues 1-14, with H83G/K88G/V212A/S309A mutations). The construct (ICL3-10) was expressed in Pichia pastoris. T4L insertion was essential for crystal appearance, although it decreased thermostability to some extent. The BLT1-T4L fusion was crystallized in complex with BIIL260 by the lipidic cubic phase method at 3.7 A resolution (PDB 5X33).
 | Enabled first BLT1 crystal structure at 3.7 A resolution (PDB 5X33)
 |

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [Metabotropic Glutamate Receptor 5 (mGlu5)](/xray-mp-wiki/proteins/metabotropic-glutamate-receptor-5/) — T4L inserted into ICL2 for mGlu5 crystallization
- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — Alternative fusion partner; replaces ICL3 instead of ICL2
- [Rat Neurotensin Receptor 1 (NTSR1)](/xray-mp-wiki/proteins/neurotensin-receptor-1/) — T4L fusion replacing ICL3 in NTSR1-GW5-T4L crystallization construct
- [Human Protease-Activated Receptor 1 (PAR1)](/xray-mp-wiki/proteins/par1/) — T4L inserted into ICL3 (A301-A303) for PAR1 vorapaxar complex crystallization
- [Human Protease-Activated Receptor 2 (PAR2) - Stabilized T4L Fusion](/xray-mp-wiki/proteins/par2/) — T4L inserted between F58 and F59 in N terminus (replacing residues 1-54) for PAR2 crystallization
