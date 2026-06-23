---
title: "E. coli PqiB Syringe-like MCE Protein"
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.019]
verified: false
---

# E. coli PqiB Syringe-like MCE Protein

## Overview

PqiB is a periplasm-spanning MCE (mammalian cell entry) protein from Escherichia coli that adopts a distinctive needle-and-syringe architecture. PqiB consists of three tandem MCE domains that stack into three hexameric rings, forming a ~360 kDa complex with a hollow six-helix coiled-coil needle projecting from one end. The barrel is approximately 90 A in diameter and the complete assembly extends up to ~230 A from the inner membrane face. PqiB creates a continuous hydrophobic channel running from the tip of the needle through the barrel, potentially facilitating direct lipid transport across the periplasmic space. The structure was determined by single-particle [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em) at 3.96 A resolution.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2017.03.019 | 5UVN | 3.96 A | C6 | Periplasmic domain of PqiB (three MCE domains plus partial C-terminal helical region), with amphipol A8-35 | none |

## Expression and Purification

- **Expression system**: E. coli Rosetta2 DE3
- **Construct**: PqiB periplasmic domain (three MCE domains with partial C-terminal region), expressed as soluble protein

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex-C3 cell disruptor, centrifugation | -- | 50 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 300 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) + -- | Clarified lysate prepared |
| Ni-NTA affinity chromatography | Metal affinity chromatography | [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) agarose | 50 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 300 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) (wash), 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) (elution) + -- | His-tagged PqiB purified from soluble fraction |
| Gel filtration | Size-exclusion chromatography | Superdex 200 | 20 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 150 mM NaCl + -- | Hexameric PqiB complex |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Needle-and-syringe architecture with continuous hydrophobic channel

Six PqiB polypeptides associate to form a ~360 kDa needle-and-syringe assembly.
The syringe barrel consists of three stacked hexameric rings (MCE1, MCE2, MCE3),
while the needle is formed by a hollow six-helix coiled-coil with an outer diameter
of ~35 A and a hollow lumen of 15-20 A wide. A long tunnel runs from the tip of
the needle to the bottom of the barrel, continuous with the channel through the
barrel. The needle is somewhat flexible at the junction with the barrel, with an
estimated length of ~135 A from barrel base to needle tip.

### Hydrophobic pore lining by beta5-beta6 loops and beta-barrel motifs

The central pore of PqiB is lined by hydrophobic residues from the homologous beta5-beta6
loops of each MCE domain. The MCE3 domain beta5-beta6 loop has a hydrophobic tip
(Leu377, Val378, Thr379) forming a ~13 A constriction at the junction between barrel
and needle. The MCE1 and MCE2 loops form extended beta hairpins that contribute
to two 18-stranded beta-barrel motifs stacked end-to-end, lining the barrel interior
and creating a barrier that could exclude solvent from the hydrophobic central channel.

### Modular MCE domain stacking principle

PqiB has three tandem MCE domains, and its three stacked rings mirror the three
MCE domains in its primary sequence. This confirms the modular assembly principle
where the number of stacked rings equals the number of tandem MCE domains. PqiB
has a C-terminal six-helix coiled-coil needle not present in [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/mlaD), and the needle
lumen is continuous with the barrel channel. PqiB may interact with outer membrane
lipoprotein PqiC and inner membrane protein PqiA to form a complete transport system.


## Cross-References

- [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaD/) — PqiB shares the same MCE domain fold; MlaD structure docked into PqiB EM density
- [E. coli YebT Tube-like MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/yebT/) — YebT shares the same modular stacking principle but with seven MCE domains
- [E. coli MlaC Lipid-Binding Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaC/) — MlaC shuttles lipids in the Mla system; PqiB may bypass the need for a shuttle by direct spanning
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used for Ni-NTA affinity chromatography
- [MCE Protein Family](/xray-mp-wiki/concepts/protein-families/mce-protein-family/) — PqiB is a three-domain MCE protein with unique needle-and-syringe architecture
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — PqiB structure determined by single-particle cryo-EM at 3.96 A resolution
- [TRIS](/xray-mp-wiki/reagents/buffers/tris) — Entity mentioned in text
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) — Entity mentioned in text
