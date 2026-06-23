---
title: Schizorhodopsin SzR4 (AM_5_00977)
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.2016328118]
verified: false
---

# Schizorhodopsin SzR4 (AM_5_00977)

## Overview

Schizorhodopsins (SzRs) are a family of light-driven inward H+ pumps identified
in Asgard archaea, phylogenetically located at an intermediate position between
type-1 [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) and heliorhodopsins. SzR4 (AM_5_00977, GenBank
TFG21677.1) is a full-length schizorhodopsin whose structure was determined at
2.1 A resolution by X-ray crystallography using [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with
[Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) as the search model. The structure reveals that SzRs belong
to the type-1 rhodopsin family, with a seven-transmembrane helix architecture
forming a trimer in the crystal. Key structural features include a single
counterion (D184) to the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base, absence of the strongly
hydrogen-bonded water molecule (water402) characteristic of other H+ pumping
rhodopsins, and uniquely short cytoplasmic ends of TM2, TM6, and TM7 that
position E81 near the cytosol. This close proximity of E81 to the solvent
enables an "untrapped inward H+ release" mechanism: H+ is released from the
[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base through a water-mediated transport network to the cytosol
without being metastably trapped at E81, unlike other proton pumps.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.2016328118 |  | 2.1 |  | Full-length SzR4 (AM_5_00977) | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) |

## Expression and Purification

- **Expression system**: Escherichia coli C41(Rosetta)
- **Construct**: SzR4 with C-terminal TEV cleavage site followed by GFP-His10 tag in pET21a(+)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and membrane preparation | E. coli C41(Rosetta) transformed with pET21a(+)-SzR4, grown at 25 C for 20 h with 1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction and 10 uM all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) supplementation. Cells disrupted by sonication in 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/). Crude membrane fraction collected by ultracentrifugation at 180,000g for 1 h. | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + -- | Cells harvested and disrupted by sonication |
| Solubilization | Membrane fraction solubilized for 1 h at 4 C in buffer containing detergent | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Solubilized for 1 h at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Eluate from affinity step treated with TEV protease and dialyzed overnight. Cleaved GFP and protease removed with Co2+-NTA resin. | Co2+-NTA | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | TEV cleavage removed GFP-His10 tag |
| Size-exclusion chromatography | Flow-through concentrated and loaded onto Superdex200 10/300 Increase column | Superdex200 10/300 Increase | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Peak fractions pooled and concentrated to 30 mg/mL |


## Crystallization

### doi/10.1073##pnas.2016328118

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | 30 mg/mL SzR4 in 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (protein:lipid ratio 1:1.5) |
| Temperature | 20 C |
| Cryoprotection | Crystals harvested directly from LCP and frozen in liquid nitrogen without added cryoprotectant |
| Notes | Crystals grown in LCP using Gryphon robot. 30 nL protein-laden mesophase drops overlaid with 800 nL precipitant solution in 96-well glass plates. Data collected at SPring-8 BL32XU with EIGER X 9M detector at 1.0 A wavelength. 148 small-wedge datasets (10 deg/crystal) processed with KAMO, XDS, and XSCALE. Structure determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with PHASER using BR structure (PDB 1M0K). |


## Biological / Functional Insights

### SzR4 structure establishes schizorhodopsins as type-1 rhodopsins

The SzR4 structure superimposes well on [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (BR, RMSD 1.27 A for
C-alpha atoms) rather than heliorhodopsin (TaHeR, RMSD 1.96 A). SzR4 and BR
similarly form trimers in the crystal, with TM1 and TM2 of one monomer creating
a binding interface with TM4' and TM5' of the adjacent monomer, in contrast to
heliorhodopsins which form dimers. The membrane orientation is the same as type-1
rhodopsins (N terminus extracellular, C terminus cytoplasmic), opposite to HeRs.
This classifies SzRs within the type-1 rhodopsin family despite their intermediate
phylogenetic position.

### Single counterion D184 and absence of strongly hydrogen-bonded water

Unlike BR which has a double counterion system (D85, D212) bridged by a strongly
hydrogen-bonded water molecule (water402), SzR4 employs D184 as a single counterion
forming a direct salt bridge with the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base (RSB). No electron
density corresponds to water402. Three water molecules exist in the space opened
by F70 side-chain flipping, but the RSB complex does not form hydrogen bonds with
them. This absence of the strongly hydrogen-bonded water molecule is a unique
structural feature of SzR4 among H+ pumping rhodopsins and may be associated
with its inward pumping function.

### Short cytoplasmic helices position E81 near the cytosol

The cytoplasmic parts of TM2, TM6, and TM7 in SzR4 are shorter than in other
[Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/). TM6 of SzR4 has only 13 residues between the conserved
Pro and the cytoplasmic end, compared to ~21 residues in other type-1 rhodopsins,
making it the shortest among [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/). This places E81 (the putative
H+ acceptor, homologous to BR D96) very close to the cytoplasmic surface,
separated from the solvent by only two leucine residues (L30, L85). This
structural feature enables the "untrapped inward H+ release" mechanism.

### Color-tuning mechanism via residues around the beta-ionone ring

SzR4 shows lambda_max at 557 nm, identical to SzR1. SzR2 and SzR3 show
blue-shifted absorptions at 542 and 540 nm, respectively. Residues N100 and
V103 around the beta-ionone ring were identified as primary determinants of
color tuning. The N100M mutation (SzR4 to SzR2 type) and N100T mutation (SzR4
to SzR3 type) each produced 11 nm blue shifts. In BR, the homologous position
(D115) also affects absorption wavelength, suggesting a conserved color-tuning
mechanism at this position across rhodopsins.

### L78 hydrophobic gate regulates solvent access to E81

L78 in SzR4 (homologous to L93 in BR) forms a hydrophobic barrier between the
RSB and E81. The L78A mutant completely abolished H+ transport activity. The
RSB in SzR4 L78A was accessible to hydroxylamine even in the dark, indicating
that L78 normally gates solvent access to the cytoplasmic side. Light-induced
rotation of L78 likely opens a water-mediated transport network from the RSB to
the cytosol, enabling H+ release attracted by the negative charge of E81.

### Untrapped inward H+ release mechanism

SzR4 employs a unique "untrapped inward H+ release" mechanism distinct from
other proton pumps. During the M-intermediate rise, light-induced structural
changes (including TM3 movement) disrupt the hydrogen-bonding network around
E81 and the two hydrophobic barriers above and below it. A water-mediated
transport network forms between the RSB and the cytosol. The RSB deprotonates,
and the H+ is released to the solvent through this network, attracted by the
negative charge of E81. Unlike BR where H+ is metastably trapped at D96, the
H+ in SzR is not trapped at E81 because the rate of H+ release to the bulk
is faster than H+ transfer from RSB to E81. This model explains the different
kinetic behaviors of SzR compared to xenorhodopsins and [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/).


## Cross-References

- [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) — SzR is a newly identified family of microbial rhodopsins from Asgard archaea
- [Evolution of Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/evolution-of-rhodopsins/) — SzRs are phylogenetically intermediate between type-1 rhodopsins and heliorhodopsins
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — SzR4 structure was solved by molecular replacement using BR model and shows structural similarity to BR
- [BcXeR (Xenorhodopsin from Bacillus coahuilensis)](/xray-mp-wiki/proteins/rhodopsins/bcxer/) — SzR and XeR both function as inward H+ pumps but with different mechanisms
- [Proton Wire](/xray-mp-wiki/concepts/transport-mechanisms/proton-wire/) — SzR uses a water-mediated transport network (proton wire) for inward H+ release
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — SzR4 was crystallized using LCP with monoolein
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Monoolein was the lipid used for LCP crystallization
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — All-trans retinal is covalently bound to K188 via Schiff base
- [Retinal Chromophore Conformation](/xray-mp-wiki/concepts/structural-mechanisms/retinal-chromophore-conformation/) — All-trans to 13-cis isomerization drives the photocycle
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — SzR exhibits a photocycle with M-intermediate formation
