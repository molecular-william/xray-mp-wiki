---
title: Ammonium Transporter AmtB (E. coli)
created: 2026-06-03
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1101952, doi/10.1038##nature13419, doi/10.1073##pnas.0609796104, doi/10.1073##pnas.0610348104, doi/10.1073##pnas.1719813115, doi/10.1074##jbc.M608325200]
verified: false
---

# Ammonium Transporter AmtB (E. coli)

## Overview

AmtB (ammonium transporter B) is a trimeric ammonium channel from
Escherichia coli that mediates ammonium uptake across the cytoplasmic
membrane. Each subunit contains 11 transmembrane helices (TMH). The
first atomic-resolution structure of AmtB at 1.35 Å revealed it as a
channel rather than a transporter, conducting uncharged NH3 through a
20 Å hydrophobic channel. AmtB was shown to be highly selective for
[Phosphatidylglycerol](/xray-mp-wiki/reagents/phosphatidylglycerol/) (PG) among phospholipids, with PG binding inducing
distinct conformational changes that reposition key residues to interact
with the lipid bilayer. The twin-His motif (His-168 and His-318) within
the channel pore was demonstrated by comprehensive mutagenesis to 14
polar and non-polar residues to be absolutely essential for optimum
substrate conductance. Crystal structures of variants confirmed that
substitutions do not affect overall structure. Pore hydration analysis
revealed a correlation between transport activity and the presence of
ordered water/ammonia molecules in the central pore.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1101952 | 1U7G | 1.35 | — | AmtB_Ecoli (residues 23-428, signal peptide removed) |  |
| doi/10.1126##science.1101952 | 1U7I | 1.35 | — | AmtB_Ecoli with ammonia bound |  |
| doi/10.1073##pnas.0609796104 | 2NS1 | 1.96 | P6(3)22 | AmtB (full-length) in complex with [GlnK PII Signal Transduction Protein (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glnk/) Y51F mutant |  |
| doi/10.1073##pnas.1719813115 | 6B21 | 2.45 | H32 | AmtB E. coli (residues 1-428) |  |
| doi/10.1038##nature13419 | 4NH2 | 2.3 | C2221 | AmtB (residues 26-428), MBP fusion construct |  |
| doi/10.1074##jbc.M608325200 | not stated | 2.0 (best) | — | AmtB variants: H168A, H168E, H168F, H318A, H318F, H168A/H318A |  |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) Gold (Agilent) transformed with MBP-AmtB plasmid
- **Construct**: MBP-AmtB fusion (residues 26-428); secreted with pelB signal peptide and 10x His-tag

### Purification Workflow

*Source: doi/10.1038##nature13419*

- **Expression system**: E. coli BL21(DE3) Gold
- **Expression construct**: MBP-AmtB fusion (residues 26-428) with pelB signal peptide and 10x His-tag
- **Tag info**: MBP fusion + 10x His-tag, TEV cleaved

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Membrane solubilization | — | 100 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM 2-mercaptoethanol, 20 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4 + 200 mM n-octyl beta-D-glucopyranoside (OG) | Extracted from purified membranes overnight at 4 C |
| Affinity chromatography | Ni-NTA affinity chromatography | 5 mL HisTrap-HP column (GE Healthcare) | 200 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 50 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4 + 0.025% n-dodecyl-beta-D-maltopyranoside (DDM) | Washed with [DDM](/xray-mp-wiki/reagents/detergents/ddm/)-free buffer + 1% [OG](/xray-mp-wiki/reagents/detergents/og/); eluted with 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag cleavage | TEV protease cleavage | — | 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 50 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4 + 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Tag-removed protein collected as flow-through after second HisTrap-HP pass |
| Concentration | Concentration | — | 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 50 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4 + 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | 100 kDa MWCO concentrator; stored at -80 C |

### Purification Workflow

*Source: doi/10.1126##science.1101952*

- **Expression system**: E. coli
- **Expression construct**: AmtB_Ecoli (native, signal peptide removed)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Recombinant expression in E. coli | — |  | 20 amino acids excised from N terminus; signal sequence identified by MALDI-MS and neural network prediction |


## Crystallization

### doi/10.1126##science.1101952

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Reservoir | 25 mM AmSO4, pH 6.5 |
| Temperature | Not specified |
| Notes | Crystals of AmtB_Ecoli grown in presence of 25 mM AmSO4 at pH 6.5 diffract to 1.35 A. Also crystallized with 100 mM MASO4 at pH 6.5 for methylammonium complex. |

### doi/10.1038##nature13419

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | AmtB at 15 mg/mL in 0.5% [C8E4](/xray-mp-wiki/reagents/c8e4/), 130 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 50 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4 |
| Reservoir | 15% [PEG 4000 (Polyethylene Glycol 4000)](/xray-mp-wiki/reagents/peg-4000/), 0.8 M Potassium Formate, 0.1 M Sodium [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate/) pH 4.6 |
| Temperature | 20 C |
| Growth time | One month |
| Cryoprotection | Crystals flash-frozen with CrystalCap HT Cryoloops |
| Notes | Ten-fold molar excess of PG added prior to crystallization. Solved by molecular replacement using PHASER with PDB 1U7G. |

### doi/10.1073##pnas.0609796104

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | AmtB-[GlnK PII Signal Transduction Protein (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glnk/) Y51F complex at 10 mg/ml in 40 mM [OG](/xray-mp-wiki/reagents/detergents/og/), 25 mM AmSO4, 2 mM [ATP](/xray-mp-wiki/reagents/ligands/atp/) |
| Reservoir | 100 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 200 mM NaCl, 20% [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) 4000 |
| Temperature | 20 C |
| Notes | Solved by molecular replacement using AmtB structure (1U7G) as search model. |

### doi/10.1073##pnas.1719813115

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | AmtB at 10 mg/mL (79 uM) mixed with 1:1.5:3 molar excess of [POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine)](/xray-mp-wiki/reagents/lipids/pope/) and TFCDL |
| Reservoir | 0.1 M [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 0.3 M magnesium nitrate, 22% (wt/vol) [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) 8000 |
| Temperature | Not specified (room temperature) |
| Growth time | 2-3 days |
| Cryoprotection | No cryoprotection needed; mounted with CrystalCap HT Cryoloops and flash-frozen |
| Notes | Best diffracting crystals grew at 1:1 sample to reservoir ratio. Diffraction data collected at APS beamline 24-ID-E at 2.45 A resolution. Solved by molecular replacement using apo AmtB structure (PDB 1U76). Space group H32. |

### doi/10.1074##jbc.M608325200

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hexagonal form) |
| Protein sample | Purified AmtB variants |
| Notes | Five variants (H168A, H168E, H168F, H318A, H318F) and double mutant H168A/H318A crystallized in hexagonal form. Data collected at Swiss Light Source. Structures refined to 2.0-2.2 A resolution. |


## Biological / Functional Insights

### First structure of an ammonia channel from Amt/MEP/Rh superfamily

The 1.35 A structure of AmtB revealed it as an 11-transmembrane helix channel with a quasi-twofold axis in the plane of the membrane. The structure shows a vestibule that recruits NH4+/NH3, a binding site for NH4+ using pi-cation interactions with Trp148 and Phe107, and a 20 A hydrophobic channel that lowers the NH4+ pKa to below 6 and conducts NH3. Two conserved histidines (His168 and His318) at the center of the channel provide C-H hydrogen bond donors for NH3 passage. Reconstitution into vesicles confirmed AmtB conducts uncharged NH3.

### Mechanism of NH3 conductance

The mechanism involves vestibular recruitment of total Am (NH3 + NH4+), a site that can bind NH4+ via pi-cation interactions, and a hydrophobic channel for NH3 that lowers its pKa to <6. NH4+ becomes deprotonated at the Am2/Am3 site, and uncharged NH3 passes through. This mechanism reconciles seemingly inconsistent proposals about Amt/MEP family function, showing bidirectional NH3 conductance. The narrow hydrophobic channel excludes water and ions while selectively conducting NH3.

### GlnK-mediated channel blockade by R47 insertion

The 1.96 A structure of the AmtB-[GlnK PII Signal Transduction Protein (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glnk/) complex reveals that the T-loop of [GlnK PII Signal Transduction Protein (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glnk/) becomes highly ordered upon complex formation, inserting R47 deeply into the cytoplasmic vestibule of AmtB. The guanidinium cation of R47 makes five donor hydrogen bonds inside the channel, completely occluding any NH3 or water from passage through the cytosolic portal.

### Specific phosphatidylglycerol binding site

Eight PG molecules resolved on the periplasmic side of AmtB. A distinct conformational change in residues 70-81 forms a specific lipid-binding site. PG forms hydrogen bonds to N72 and E70. Mutation of N72 and N79 to alanine abolishes PG-induced gas-phase stability.

### Allosteric modulation of lipid binding to AmtB

Native MS analysis of AmtB binding to heterogeneous lipid pairs revealed that different lipid combinations display a range of allosteric modulation. The TFCDL (TopFluor cardiolipin) and [POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine)](/xray-mp-wiki/reagents/lipids/pope/) pair exhibited the strongest positive allosteric modulation, where binding of [POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine)](/xray-mp-wiki/reagents/lipids/pope/) enhanced TFCDL binding. Principal component analysis of coupling factors grouped six lipid pairs into four distinct allosteric patterns. The H156A mutation in AmtB completely abolished this positive allostery. Crystal structure of AmtB bound to TFCDL (PDB 6B21, 2.45 A) revealed H156 forms a hydrogen bond with the TFCDL headgroup, and E357 rotates ~150 degrees relative to the PG-bound state to interact with H156. This H156-E357 interaction is unique among all 21 previously determined AmtB structures and provides a mechanism for allosteric communication between lipid binding sites.

### Twin-His motif is essential for optimum substrate conductance

Mutagenesis of His-168 and His-318 to 14 different polar and non-polar residues demonstrated both are absolutely required for optimum methylammonium transport activity in E. coli AmtB. Crystal structures of six variants (H168A, H168E, H168F, H318A, H318F, H168A/H318A) confirmed no structural perturbation beyond the mutated residue. The H168E variant retains partial activity (~30% of WT), and its structure suggests the glutamate side chain can make similar hydrogen-bonding interactions to histidine, explaining the natural Glu substitution found in some fungal Amt proteins. Pore hydration analysis revealed that inactive variants show no electron density at the central pore site S4, while wild-type and H168E show strong peaks, correlating pore hydration with transport activity. Rh30 proteins (RhD, RhCE) lack the twin-His motif entirely and likely do not function as ammonium channels.


## Cross-References

- [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) — AmtB comparison with other structurally characterized membrane channels
- [Glycerol Facilitator (GlpF)](/xray-mp-wiki/proteins/other-ion-channels/glycerol-facilitator/) — GlpF and aquaporins share similar internal duplication fold with AmtB
- [Rh/Amt/MEP Protein Family](/xray-mp-wiki/concepts/protein-families/rh-amt-mep-protein-family/) — The twin-His motif is a conserved and essential feature of functional ammonium channels in this family
- [E. coli AmtB (ammonia channel)](/xray-mp-wiki/proteins/other-ion-channels/e-coli-amtb/) — Alternative protein entry for the same protein; twin-His mutagenesis study
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [Rh/Amt/MEP Protein Family](/xray-mp-wiki/concepts/protein-families/rh-amt-mep-protein-family/) — Key concept related to this protein
- [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) — Key concept related to this protein
- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — Key concept related to this protein
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein mentioned in the study
- [Glycerol Facilitator (GlpF)](/xray-mp-wiki/proteins/other-ion-channels/glycerol-facilitator/) — Related protein mentioned in the study
