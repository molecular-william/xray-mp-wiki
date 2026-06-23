---
title: "WzxE - Lipid III Flippase from Escherichia coli"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1098##rsob.240310]
verified: false
---

# WzxE - Lipid III Flippase from Escherichia coli

## Overview

WzxE is the lipid III flippase from Escherichia coli, responsible for translocating
the enterobacterial common antigen (ECA) lipid-linked repeat unit (lipid III,
und-PP-GlcNAc-ManNAcA-Fuc4NAc) across the inner membrane. WzxE belongs to the
multidrug and toxic compound extrusion (MATE) family of transporters and is part
of the Wzx/Wzy-dependent polysaccharide export pathway. The first X-ray crystal
structures of WzxE, determined in complex with nanobodies Nb7 and Nb10, revealed
both outward-facing (2.31 A) and inward-facing (2.80 A) conformations. Each
structure comprises 12 transmembrane helices arranged as N- and C-terminal
six-helix bundles characteristic of the MATE fold. The conformational switch
between inward- and outward-facing states is mediated by a ~23 degree rotation of
transmembrane helix 7. A conserved arginine triad (R44-R239-D262) and a
C-terminal arginine cluster (R413-R415) are critical for lipid III recognition
and transport. WzxE shows high structural similarity to [NorM-VC (Vibrio cholerae NorM) - MATE Family Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/norM-vc/) (RMSD 1.2 A over
533 residues) and the lipid II flippase [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/).

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1098##rsob.240310 | 9G95 | 2.80 | C2 | Full-length WzxE from E. coli with Nb10 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/), I23 S-SAD phasing | sulfate, zinc |
| doi/10.1098##rsob.240310 | 9G97 | 2.31 | C2 | Full-length WzxE from E. coli with Nb10 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/), I24 native | sulfate, zinc |
| doi/10.1098##rsob.240310 | 9G9M | 2.55 | C2221 | Full-length WzxE from E. coli with Nb10 and Nb7 nanobodies, outward-facing | sulfate, zinc |
| doi/10.1098##rsob.240310 | 9G90 | 2.69 | C2221 | Full-length WzxE from E. coli with Nb10 and Nb7 nanobodies, outward-facing | sulfate, zinc |
| doi/10.1098##rsob.240310 | 9G9N | 2.80 | C2221 | Full-length WzxE from E. coli with Nb10 and Nb7 nanobodies, inward-facing (occluded) | sulfate, zinc |
| doi/10.1098##rsob.240310 | 9G9P | 2.80 | C2221 | Full-length WzxE from E. coli with Nb10 and Nb7 nanobodies, inward-facing (occluded) | sulfate, zinc |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length WzxE from E. coli K-12 genome, cloned into pET-based vector with TEV-cleavable C-terminal His10 tag

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis by Emulsiflex, differential centrifugation | — | 25 mM Tris pH 7.5, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (v/v) + -- |  |
| Solubilization | Overnight detergent extraction at 4 C | — | 25 mM Tris pH 7.5, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (v/v) + 1.5% (w/v) [DM](/xray-mp-wiki/reagents/detergents/dm/) (DM) |  |
| Ni-NTA affinity | Batch binding onto Ni-NTA resin | Ni-NTA resin (ABT) | 25 mM Tris pH 7.5, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (v/v) + 0.058% (w/v) [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) + 0.008% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Washed with 20 mM and 35 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Desalting | CentriPure P100 desalting column | — | 25 mM Tris pH 7.5, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (v/v), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.058% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) + 0.008% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Tag cleavage | Overnight TEV protease digestion | — | 25 mM Tris pH 7.5, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (v/v), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.058% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) + 0.008% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Reverse IMAC | Reverse immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA resin (ABT) | 25 mM Tris pH 7.5, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (v/v) + 0.058% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) + 0.008% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Flow-through collected (TEV-cleaved protein does not bind) |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | HiLoad 16/600 Superose 6 | — | 25 mM Tris pH 7.5, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (v/v) + 0.058% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) + 0.008% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | WzxE-Nb10 complex peak pooled and concentrated using 100 kDa MWCO |

**Final sample**: Concentrated WzxE-Nb10 complex in buffer B (25 mM Tris pH 7.5, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.058% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/), 0.008% [DDM](/xray-mp-wiki/reagents/detergents/ddm/))


## Crystallization

### doi/10.1098##rsob.240310

| Parameter | Value |
|---|---|
| Method | Lipid cubic phase (LCP) crystallization |
| Protein sample | WzxE-Nb10 complex in buffer B, mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/):ECP lipid mixture at 1:1 (v/v) |
| Temperature | 20 C |
| Growth time | 2-3 months for full size (~10 um) |
| Cryoprotection | Crystals harvested from LCP; 15% [E. coli Polar Lipids](/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/) in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Notes | Outward-facing conformation (WzxE-Nb10, PDB 9G97, 2.31 A). Initial hit appeared after 1 week. 15% [E. coli Polar Lipids](/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/) added to [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) improved reproducibility. [Zinc Chloride](/xray-mp-wiki/reagents/additives/zinc-chloride/) added to precipitant for larger crystals. S-SAD phasing at 2.7552 A on I23 beamline. Native data at 0.9688 A on I24 beamline. |

| Parameter | Value |
|---|---|
| Method | LCP crystallization |
| Protein sample | WzxE-Nb10-Nb7 complex (1.2-fold molar excess of Nb7) with 2 mM und-PP-GlcNAc substrate |
| Temperature | 20 C |
| Growth time | 2-3 months |
| Notes | Inward-facing conformation (PDB 9G9N, 2.80 A). Substrate added to protein for 16 h at 4 C with sonication. Outward-facing WzxE-Nb10-Nb7 (PDB 9G9M, 2.55 A) obtained in 0.1 M sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 5, 0.1 M [Lithium Sulfate](/xray-mp-wiki/reagents/additives/lithium-sulfate/), 0.1 M [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 30% (v/v) [PEG300](/xray-mp-wiki/reagents/additives/peg300/) from MemMeso screen. |


## Biological / Functional Insights

### First crystal structure of WzxE reveals MATE family fold

The first X-ray crystal structures of WzxE reveal a 12-transmembrane helix topology with N- and C-terminal six-helix bundles characteristic of the multidrug and toxic compound extrusion (MATE) family. Despite low sequence similarity (as low as 4.6% to MATE consensus), WzxE superimposes closely with [NorM-VC (Vibrio cholerae NorM) - MATE Family Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/norM-vc/) (RMSD 1.2 A over 533 residues, PDB 3MKT). The structure clearly identifies WzxE as a member of the MATE family flippases, structurally similar to the lipid II flippase [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/) (RMSD 2.9 A over 351 residues). TM1 and TM7 extend across both bundles, while TM3 and TM9 contain kinks due to Pro104 and bulky hydrophobic residues (W312, W320, F317) respectively.

### Conformational switch between inward- and outward-facing states

WzxE was captured in both outward-facing (PDB 9G97, 2.31 A) and inward-facing (PDB 9G9N, 2.80 A) conformations. The transition between states is mediated by a ~23 degree rotation of TM7 starting at residue N211, coupled with bending of TM1 at G19. Each helical bundle (N- and C-lobe) remains structurally conserved (max RMSD 0.76 A), with the change occurring in their spatial arrangement (max RMSD 4.56 A over 360 residues). The disordered TM2 region (residues 54-57, 54AGAG57) may play a role in substrate recognition.

### Arg-triad and C-terminal cluster critical for function

The central cavity contains positively charged residues at both cytoplasmic (K64, R143, R282) and periplasmic (R44, R239, K326) surfaces. Mutagenesis showed R44A severely reduces ECA production, establishing R44 as critical for flippase activity. The conserved D262 residue forms a R44-R239-D262 triad analogous to the R24-D25-R255 triad in [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/). The C-terminal arginine cluster (R413-R415) is also essential; alanine mutations progressively reduce ECA production. R143A-R282A double mutant retained partial activity, suggesting the C-terminal cluster provides alternative binding.

### Proposed flipping mechanism for lipid III translocation

Based on the inward- and outward-facing structures, a flipping mechanism is proposed: (1) The C-terminal arginine cluster (R413-R415) initially recruits the pyrophosphate group of lipid III at the cytoplasmic face; (2) The pyrophosphate migrates to the cytoplasmic arginine pair (R143, R282) in the inward-facing conformation; (3) A network of carboxylate residues (D71, D288, E285) interacts with the three sugar moieties of ECA; (4) The pyrophosphate shifts to the periplasmic arginine pair (R44, R239) accompanied by the conformational switch to the outward-facing state; (5) The pyrophosphate moves to the positively charged cluster (R315, R331) at the periplasmic face for handoff to the polymerase WzyE.

### No evidence for proton or chloride antiport mechanism

Despite WzxE being proposed as a proton antiporter, the positively charged central lumen appears unlikely to promote proton transport, and no negatively charged patch spans the membrane. A chloride ion found in one WzxE structure was located on the external surface, unlike the central chloride proposed as a counter-ion in [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/). The data do not support a conserved chloride antiport mechanism for WzxE or MATE family flippases. The voltage difference across the membrane remains a possible source of activation energy, as proposed for [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/).

### Nanobody-based crystallization enabled structure determination

Crystallization of WzxE required complexation with two nanobodies (Nb7 and Nb10) generated by llama immunization. Nb10 binds at the periplasmic face of the N-terminal lobe, while Nb7 binds near the C-terminal lobe. The original structure was solved by sulfur SAD phasing using multi-crystal data at 2.7552 A on Diamond I23 beamline, involving 21 datasets from 4 crystals. The native structure was refined to 2.31 A using data from the I24 beamline. Only ~15% of tested crystals diffracted beyond 3 A, highlighting the challenging nature of this membrane protein.


## Cross-References

- [MurJ (Lipid II Flippase from Escherichia coli)](/xray-mp-wiki/proteins/abc-transporters/murj/) — Structural homolog; both are MATE family flippases with similar mechanism
- [NorM-VC (Vibrio cholerae NorM)](/xray-mp-wiki/proteins/abc-transporters/norM-vc/) — MATE family transporter; WzxE superimposes with RMSD 1.2 A
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used in purification (0.008% DDM and 0.058% OGNG in buffer)
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method for WzxE
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [Lithium Sulfate](/xray-mp-wiki/reagents/additives/lithium-sulfate/) — Additive used in purification or crystallization buffers
