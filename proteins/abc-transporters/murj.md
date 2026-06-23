---
title: MurJ (Lipid II Flippase from E. coli and T. africanus)
created: 2026-06-08
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2022.05.008, doi/10.1038##s41467-019-09658-0, doi/10.1038##nsmb.3346, doi/10.1073##pnas.1802192115]
verified: false
---

# MurJ (Lipid II Flippase from E. coli and T. africanus)

## Overview

MurJ is an essential integral membrane protein in Gram-negative bacteria that flips the cell wall building block Lipid II across the cytoplasmic membrane for peptidoglycan biosynthesis. MurJ is a member of the MOP (Multidrug/Oligosaccharidyl-lipid/Polysaccharide) flippase superfamily. Crystal structures have revealed V-shaped inward- and outward-facing forms with a central cavity for substrate binding. A novel "squeezed" form of E. coli MurJ (EcMurJ) was discovered, representing an intermediate conformation after substrate release that lacks an internal cavity. Structures from Arsenophonus endosymbiont MurJ (AeMurJ) show inward closed and occluded conformations. The MurJ from Thermosiphon africanus (MurJ_TA) was captured in multiple conformations — inward-closed, inward-open, inward-occluded, and outward-facing — revealing the complete conformational landscape of the Lipid II flipping cycle, including a sodium binding site and a conserved Arg24-Asp25-Arg255 substrate-binding triad.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-019-09658-0 | 5T77 | 2.0 | Not specified | MurJ_TA (Thermosiphon africanus) |  |
| doi/10.1038##s41467-019-09658-0 | 6NBL | 3.2 | Not specified | MurJ_TA inward-closed |  |
| doi/10.1038##s41467-019-09658-0 | 6NBM | 3.0 | Not specified | MurJ_TA inward-open |  |
| doi/10.1038##s41467-019-09658-0 | 6NBN | 2.6 | Not specified | MurJ_TA inward-occluded |  |
| doi/10.1038##s41467-019-09658-0 | 6NBO | 1.8 | Not specified | MurJ_TA outward-facing |  |
| doi/10.1016##j.str.2022.05.008 | 7WAG | 2.6 | Not specified | EcMurJ, residues 12-511 |  |
| doi/10.1016##j.str.2022.05.008 | 7WAW | 2.8 | Not specified | AeMurJ, inward closed form (AeMurJ-N) |  |
| doi/10.1016##j.str.2022.05.008 | 7WAX | 2.4 | Not specified | AeMurJ, inward occluded form (AeMurJ-L) |  |
| doi/10.1073##pnas.1802192115 | 6CC4 | 3.5 | Not specified | E. coli MurJ (residues 5-507) with N-terminal BRIL fusion |  |

## Expression and Purification

- **Expression system**: Escherichia coli C41(DE3)
- **Construct**: MurJ_TA (T. africanus): His10-MBP-PPX-MurJ_TA-PPX-His10; EcMurJ (E. coli) residues 12-511; AeMurJ (Arsenophonus) full-length with TEV-cleavable C-terminal GFP-His8
- **Notes**: Sources: doi/10.1038##s41467-019-09658-0 (MurJ_TA); doi/10.1016##j.str.2022.05.008 (EcMurJ, AeMurJ)

### Purification Workflow

*Source: doi/10.1038##s41467-019-09658-0*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Microfluidizer disruption | — | 50 mM HEPES-NaOH pH 8.0, 150 mM Na acetate, 10 mM beta-ME, protease inhibitors | Chloride-free buffers used throughout |
| Membrane protein extraction | Detergent solubilization | — | 50 mM HEPES-NaOH pH 8.0, 150 mM Na acetate + 30 mM n-dodecyl-beta-D-maltopyranoside (DDM) | 60 min at 4 C |
| Immobilized metal-affinity chromatography | TALON cobalt affinity | TALON Cobalt resin | 50 mM HEPES-NaOH pH 8.0, 150 mM Na acetate, 15 mM imidazole, 1 mM DDM | Eluted with 200 mM imidazole. PreScission protease cleavage overnight at 4 C to remove tags. |
| Buffer exchange and size-exclusion chromatography | Gel filtration | Superdex 200 10/300 | 20 mM HEPES-NaOH pH 8.0, 150 mM Na acetate, 2 mM DTT, 0.3 mM decyl maltose neopentyl glycol (DMNG) | Exchanged into DMNG by 15-fold dilution prior to SEC |

### Purification Workflow

*Source: doi/10.1016##j.str.2022.05.008*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Microfluidizer lysis, ultracentrifugation | — | 50 mM Tris-HCl pH 8.0, 300 mM NaCl, 1 mM beta-ME, 0.1 mM PMSF |  |
| Solubilization | Detergent extraction | — | 50 mM Tris-HCl pH 8.0, 300 mM NaCl, 1 mM beta-ME, 0.1 mM PMSF + 1% (w/v) n-dodecyl-beta-D-maltopyranoside (DDM) | 60 min at 4 C |
| Ni-NTA affinity chromatography | Immobilized metal-affinity chromatography | Ni-NTA agarose | 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 5% glycerol, 0.1% DDM, 5 mM beta-ME | Eluted with 100-300 mM imidazole gradient. GFP-His8 tag cleaved by TEV protease at 4 C for 16 h. |
| Size-exclusion chromatography | Gel filtration | Superdex 200 Increase 10/30 GL | 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 0.05% DDM, 5 mM beta-ME |  |


## Crystallization

### doi/10.1038##s41467-019-09658-0

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | 20-25 mg/mL MurJ_TA in DMNG buffer mixed with Lipid II-doped monoolein (2:3 w/w water:lipid ratio) |
| Temperature | 20 C |
| Notes | Crystals grown in 96-well glass sandwich plates. Salt composition of precipitant determined crystal form. Inward-closed: 1 M NaCl, 50 mM Na acetate pH 4.6, 40% PEG400. Inward-open: 200 mM (NH4)2SO4, 50 mM Tris-HCl pH 8.5 or 100 mM Na citrate pH 5.5, 20-40% PEG400. Inward-occluded: 100 mM Na citrate pH 5.0, 40% PEG200. Outward: 1 M NaCl, 50 mM HEPES-NaOH pH 7.5, 20% PEG400, or MgCl2/NaCl conditions. Crystals grew to full size in 4 weeks. |

### doi/10.1016##j.str.2022.05.008

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Approximately 20 mg/ml EcMurJ or AeMurJ in DDM |
| Temperature | 20 C |
| Notes | EcMurJ crystallized in long thin plate-like crystals. AeMurJ produced two crystal forms (AeMurJ-N and AeMurJ-L). Structures determined by Se-Met SAD (AeMurJ) and molecular replacement using EcMurJ (PDB 6CC4) as search model. |


## Biological / Functional Insights

### Complete conformational landscape of MurJ

The paper captured MurJ_TA in four conformations (inward-closed, inward-open, inward-occluded, outward-facing), revealing the complete transport cycle. The ordered trajectory proceeds through lateral gating at the membrane portal, asymmetric thin gate formation, and outward transition driven by TM7 straightening.

### Lateral membrane portal controls substrate entry

The lateral membrane portal between TM1 and TM8 dilates from 8.0 A to 17.4 A during the inward-closed to inward-open transition, controlled by TM4-5 loop rearrangement and TM1 bending. The conserved TM4-5 loop (Leu145, Asn146, Phe151, Pro158) distinguishes MurJ from MATE drug pumps and is a specific adaptation for flippase function.

### Thin gate occludes Lipid II headgroup

An asymmetric inward-occluded state features a thin gate formed by Glu57 (TM2) and Arg352 (TM10) that likely occludes the Lipid II headgroup in the cavity above the gate. The conserved (G/A)-E-G-A motif on TM2 enables S-shaped bending for thin gate formation.

### Arg352 as a multifunctional switch

Arg352 participates in both the thin gate (with Glu57 in inward-occluded) and the cytoplasmic gate (with Ser61, Ser62, Gly58 backbone in outward-facing), suggesting it plays a key role in conformational transitions during the transport cycle.

### Sodium binding site in the C-lobe

A sodium ion was identified in the C-lobe (TMs 7, 11, 12) coordinated by Asp235, Asn374, Asp378, Val390 (CO), and Thr394 in trigonal bipyramidal geometry. The DNDXT motif and coordination geometry are conserved with MATE transporters. Sodium binding at Asp235 may propagate conformational changes down TM7.

### Arg24-Asp25-Arg255 substrate-binding triad

Three conserved residues (Arg24, Asp25, Arg255) undergo coordinated rearrangement across conformational states. In the inward-occluded state, Arg24 and Arg255 are brought to 2.9 A proximity, stabilized by electrostatic interactions with Asp25 and the Lipid II diphosphate moiety. Mutations at these positions cause Lipid II accumulation and loss of complementation.

### Squeezed form represents post-release intermediate

The EcMurJ squeezed form lacks an internal cavity. The distance between TM2 and TM8 at the middle and periplasmic pairs is less than 9 A, considerably closer than in inward or outward forms. This conformation is proposed to occur after Lipid II release to the periplasm, preventing substrate re-binding and reverse flip.

### TM7 acts as conformational switch

TM7 is the most structurally variable helix, connecting N- and C-lobes. The bend angle at G239 in the squeezed form (76 deg) is larger than in the outward form. C-lobe rotates about 35 deg in conjunction with TM7 bend angle changes, leading to cavity closure.

### Coevolution supports squeezed form existence

EVcouplings server predicted coevolution of residues R53 and E273, whose side chains are adjacent only in the squeezed form. The cluster of residues R52, R53, E57, R270, and E273 appears to stabilize the squeezed form.

### Rocker switch transport model

MurJ transports Lipid II via alternating access. Inward closed/open form captures Lipid II. Inward occluded form holds substrate with a narrow gate between E57(TM2) and V281(TM8). Outward form releases Lipid II to periplasm. After release, MurJ adopts the squeezed form before transitioning back to inward forms.

### High-throughput mutagenesis (mut-seq) mapping of E. coli MurJ

High-throughput mutagenesis with next-generation sequencing (mut-seq) was performed on E. coli MurJ, scoring complementation of more than 1,500 individual point mutants covering all 521 codons. A total of 61 severely deleterious missense mutations were identified and mapped into four functional groups: (i) buried hydrophobic residues affecting folding; (ii) extracellular gate residues (D39, S263) at the interface between N-lobe and C-lobe; (iii) intracellular gate residues (V65, P66, A69 interacting with L288, P289, S292) that stabilize the outward-open conformation; and (iv) solvent-exposed residues in the central cavity and extended groove involved in substrate binding. Mutations altering the central cavity charge were particularly common, highlighting the importance of electrostatic interactions for substrate recognition and transport.

### Rocker-switch alternating-access model supported by evolutionary coupling

Evolutionary coupling analysis using 15,972 MurJ sequences identified 470 significant coevolving pairs. A subset of coevolved residue pairs are distant in the inward-open structure but become close in an outward-open homology model (based on MATE transporter PDB 3VVN). These pairs are located on opposite lobes at the cytosolic face, demonstrating that both inward-open and outward-open states are under evolutionary selection and supporting a rocker-switch alternating-access model for lipid II flipping.


## Cross-References

- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — MurJ uses alternating access to flip Lipid II across the membrane
- [N-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for purification and crystallization
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used in Ni-NTA affinity chromatography buffers
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer component throughout purification
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) — Reducing agent in purification buffers
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA IMAC and TALON cobalt affinity used for initial purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC used as final polishing step
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — EcMurJ and AeMurJ-L and MurJ_TA structures solved by MR
- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — AeMurJ-N structure solved by Se-Met SAD phasing
- [Lipidic Cubic Phase (LCP)](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — MurJ_TA was crystallized by LCP method
- [Decyl Maltose Neopentyl Glycol (DMNG)](/xray-mp-wiki/reagents/detergents/dmng/) — Used in final purification buffer for MurJ_TA
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Used as LCP host lipid for MurJ_TA crystallization
