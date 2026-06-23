---
title: Opsin (Retinal-Free Rhodopsin Apoprotein)
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature07063, doi/10.1038##nature07330, doi/10.1002##anie.201302374, doi/10.1016##j.str.2015.09.015, doi/10.1038##ncomms5801]
verified: false
---

# Opsin (Retinal-Free Rhodopsin Apoprotein)

## Overview

Opsin is the apoprotein form of rhodopsin, the G-protein-coupled receptor responsible for vision in vertebrate retinal rod cells. The first crystal structure of ligand-free native opsin (PDB 3CAP, 2.9 A resolution, 2008) revealed the conformational changes associated with GPCR activation in the absence of an inactivating ligand. Compared to the dark-state rhodopsin structure, opsin shows prominent structural changes in the conserved E(D)RY and NPxxY(x)5,6F regions and in TM5-TM7, including a 6-7 A outward tilt of cytoplasmic TM6, breakage of the ionic lock between Arg135 and Glu247, and reorganization of the empty retinal-binding pocket with two openings that may serve retinal entry and exit. Later higher-resolution structures (PDB 4GZM at 2.65 A, PDB 4X1H at 2.3 A) resolved the active Ops* conformation in complex with synthetic G-protein peptides, revealing an extensive solvent-mediated hydrogen-bonding network connecting the chromophore binding site to the G protein binding site through conserved GPCR activation motifs (CWxP, NPxxY, and (D/E)RY). The opsin structure serves as the best available structural template for homology modeling of olfactory receptors (ORs), which comprise over half of all GPCRs.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature07063 | 3CAP | 2.9 A | H3 | Native opsin apoprotein from bovine retinal rod cells (retinal-free rhodopsin, residues 1-348) | None (retinal-free; empty binding pocket) |
| doi/10.1038##nature07330 | 3DQB | 3.2 A | H32 | Ops* (bovine rhodopsin apoprotein, residues 1-326) in complex with synthetic GalphaCT peptide (Galpha_t(340-350)K341L; ILENLKDCGLF) | beta-D-Octylglucoside (OG); Palmitoyl chains; N-Acetyl-D-Glucosamine; GalphaCT peptide |
| doi/10.1002##anie.201302374 | 4GZM | 2.65 A | not specified | Ops* conformation (retinal-free rhodopsin apoprotein) in complex with synthetic G protein peptide GalphaCT2 | Octyl glucoside (OG) in retinal-binding pocket; synthetic G protein peptide GalphaCT2 |
| doi/10.1016##j.str.2015.09.015 | 4X1H | 2.3 A | not specified | Activated opsin (bovine rhodopsin, residues 1-326) stabilized with nonyl-glucoside in chromophore binding site, in complex with Galpha-CT peptide (VLEDLKSCGLF) | nonyl-glucoside (C9G) in chromophore binding pocket; Galpha-CT peptide (G alpha C-terminus mimetic) |
| doi/10.1038##ncomms5801 | 4PXF | 2.75 A | H32 | Ops* (bovine rhodopsin apoprotein, residues 1-326) in complex with ArrFL-1 peptide (residues 71-77 of rod photoreceptor arrestin: DVMGLLL) | beta-D-Octylglucopyranoside (OG) in retinal-binding pocket; ArrFL-1 peptide (arrestin finger loop mimic); Palmitoyl chains; N-Acetyl-D-Glucosamine (oligosaccharides) |

## Expression and Purification

- **Expression system**: Vertebrate retinal rod cells (disc membrane)
- **Construct**: Native opsin apoprotein (retinal-free rhodopsin)

### Purification Workflow

*Source: doi/10.1038##nature07063*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Disc membrane preparation | Opsin solubilization from rod outer-segment disc membranes | -- | 20 mM BTP (pH 7.5), 130 mM NaCl, 1 mM MgCl2, 10% sucrose + [OG](/xray-mp-wiki/reagents/detergents/og/) (beta-D-octylglucopyranoside, 1% w/v) | Rod outer-segment disc membranes prepared from bovine eyes. Opsin solubilized using 1% beta-D-octylglucopyranoside. Solubilized opsin with A280/A362 ratios greater than 4 used without further purification. |

### Purification Workflow

*Source: doi/10.1002##anie.201302374*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Disc membrane solubilization | Solubilization in OG detergent | -- | not specified + [OG](/xray-mp-wiki/reagents/detergents/og/) | Opsin was solubilized from disc membranes of vertebrate retinal rod cells using OG, which favors the active Ops* conformation |


## Crystallization

### doi/10.1038##nature07063

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Opsin apoprotein (5 mg/ml, epsilon280 = 81,200 M-1 cm-1) solubilized in OG detergent |
| Reservoir | 2.8-3.2 M ammonium sulphate in 0.1 M MES or 0.1 M sodium acetate buffer, pH 5.6 |
| Temperature | 277 K (4 C) |
| Growth time | 7 days (crystals appeared within 2-3 days, grew further for 5 days) |
| Cryoprotection | 10% (w/v) trehalose in reservoir solution; crystals flash-frozen in liquid nitrogen |
| Notes | Crystals grown using hanging-drop vapor diffusion at 277 K in 24-well Linbro plates. Each drop contained 2 ul protein + 2 ul reservoir. Colourless opsin crystals had dimensions of 0.1 x 0.1 x 0.2 mm3. On addition of 11-cis-retinal to the crystal, a colour change to red was observed, indicating rhodopsin could be regenerated. Data collected at 100 K at synchrotron beamline BL 14.2, BESSY (Berlin) with MAR-165CCD detector at 210 mm distance. Space group H3 (a = 242.92 A, b = 242.92 A, c = 110.42 A, alpha = beta = 90 degrees, gamma = 120 degrees). Two monomers in asymmetric unit arranged as a dimer with TM1 and H8 as interface. |

### doi/10.1002##anie.201302374

| Parameter | Value |
|---|---|
| Method | X-ray crystallography |
| Protein sample | Ops* in complex with synthetic G protein peptide GalphaCT2 and OG in [OG](/xray-mp-wiki/reagents/detergents/og/) detergent |
| Reservoir | pH 5.6 crystallization conditions |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Crystallization at low pH (5.6) in OG detergent promotes formation of the active Ops* conformation. The well-defined hydrogen-bond network holds OG in the retinal-binding pocket. Active Ops* conformation stabilized by OG in the ligand-binding pocket. |

### doi/10.1016##j.str.2015.09.015

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | Photoactivated rhodopsin (opsin) with 12-fold molar excess of Galpha-CT peptide (VLEDLKSCGLF), in nonyl-glucoside (C9G) detergent |
| Reservoir | 3-3.4 M ammonium sulfate, 100 mM citrate (pH 5-6.5) |
| Temperature | 4 C |
| Growth time | 3-12 months |
| Cryoprotection | Crystals harvested from mother liquor, blotted, and flash frozen in liquid nitrogen |
| Notes | Crystals grown in complete darkness at 4 C. Crystals appeared after 3-4 months and reached maximum dimensions of 300 x 300 x 600 um at 6-12 months. Data collected from a crystal over 16 months old at NE-CAT 23-ID-C using shutterless mode. Nonyl-glucoside (C9G) detergent was found occupying the chromophore binding site instead of retinal. |

### doi/10.1038##ncomms5801

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Ops* (150 uM in 20 mM BTP pH 7.5, 130 mM NaCl, 1 mM MgCl2, 1.25% n-octyl-beta-D-glucopyranoside) mixed with ArrFL-1 peptide (12:1 molar ratio, peptide:protein), light-activated (530 nm for 60 s) |
| Reservoir | 3.2-3.5 M (NH4)2SO4 in 0.1 M MES or sodium acetate, pH 6.0 |
| Temperature | 277 K (4 C) |
| Growth time | 12 days (crystals appeared within 7 days, grew further for 5 days) |
| Cryoprotection | 10-15% trehalose in crystallization buffer; crystals flash-frozen in liquid nitrogen |
| Notes | Best results obtained with ArrFL-1 peptide derived from rod photoreceptor arrestin (residues 67-77: YGQEDIDVMGLLL). Space group H32 with cell dimensions a=b=242.62 A, c=110.22 A, alpha=beta=90 degrees, gamma=120 degrees. One monomer per asymmetric unit. Data collected at ESRF ID29. Resolution 2.75 A with Rwork/Rfree = 21.7/25.1%. Over 500 crystals screened. Phases obtained by molecular replacement using Ops*-GalphaCT structure (3DQB) as search model. |


## Biological / Functional Insights

### Crystal structure of Ops*–GalphaCT complex reveals G protein binding surface

The 3.2 A crystal structure of the Ops*–GalphaCT complex (PDB 3DQB) revealed how the C-terminal alpha5 helix of Galpha_t (transducin) binds to the cytoplasmic pocket of active opsin. The GalphaCT peptide (residues 340-350, sequence ILENLKDCGLF) forms an alpha_L-type C-cap motif upon receptor binding. Key interactions include hydrogen bonds between main-chain atoms of the peptide and residues in TM3, TM5, TM6, and Helix 8 of Ops*, as well as van der Waals contacts with Val230, Ala233, Thr242, Thr243, Ala246, Val138, Val139, Ala246, Val250, Leu72, Asn310, and other residues. Arg135 of the conserved E(D)RY motif interacts with the C-terminal region of the peptide. The structure shows that GalphaCT binding stabilizes the active Ops* conformation, with the nucleotide-free G protein coupled receptor state providing a crevice for Galpha binding that is absent in dark-state rhodopsin.

### First crystal structure of ligand-free opsin reveals GPCR activation mechanism

The 2.9 A structure of native opsin (PDB 3CAP) was the first crystal structure of a ligand-free GPCR, revealing the conformational changes that occur upon release of the inactivating ligand 11-cis-retinal. Key changes include: (1) breakage of the ionic lock (Arg135-Glu247 salt bridge), (2) 6-7 A outward tilt of the cytoplasmic end of TM6 with Trp265 as a pivot point, (3) elongation of TM5 by 1.5-2.5 helical turns at the cytoplasmic side, (4) rotation of Tyr306 (NPxxY motif) to face into the helix bundle, blocking TM6 from returning to the rhodopsin conformation, and (5) formation of two openings in the retinal-binding pocket between TM5-TM6 and TM1-TM7, proposed as entry and exit routes for retinal.

### Ionic lock breakage and new stabilizing interactions in opsin

In rhodopsin, a salt bridge between Arg135 (TM3, part of the E(D)RY motif) and Glu247 (TM6) together with Glu134 and Thr251 forms the ionic lock that stabilizes TM6 within the helical bundle. In opsin, this ionic lock is broken: Arg135 is released from Glu134 and Glu247 and instead engages with Tyr223 to tether TM5. Glu247 flips over to interact with Lys231 (TM5) and Thr251 (TM6) in an extended hydrogen-bonded network, stabilizing the TM5-TM6 pair at the cytoplasmic side. Glu134 repositions toward TM2 and TM4 without specific interactions.

### Retinal-binding pocket openings for ligand exchange

The ligand-free opsin structure reveals two openings in the retinal-binding pocket that are absent in rhodopsin. The first opening between TM5 and TM6 is formed by Ile205, Phe208 (TM5) and Phe273, Phe276 (TM6), resulting from small backbone movements and side-chain reorientations. This hydrophobic hole is proposed as the entry route for 11-cis-retinal during rhodopsin regeneration. The second opening between TM1 and TM7 arises from backbone alteration in TM7 and a 120-degree clockwise rotation of Phe293, with a small hole that can be sealed by rotamers of the Lys296 side chain. This opening is proposed as the exit route for all-trans-retinal after photobleaching.

### Conserved Trp265 as pivot for TM6 movement

The highly conserved Trp265 (Trp6.48) acts as a pivot point for the outward tilt of the cytoplasmic end of TM6. In the ligand-free opsin structure, Trp265 is in van der Waals contact with the space previously occupied by the beta-ionone ring of retinal, with Phe261 moving toward TM5. The indole side chain of Trp265 fills part of the space vacated by retinal. Coupled changes in the rotamer states of Trp6.48 and Phe6.52 were predicted to enable the activating outward movement of TM6. In opsin, the empty retinal-binding pocket means no rotamer change is observed for Trp265 relative to rhodopsin, but the cytoplasmic end of TM6 is already displaced outward.

### Ops* conformation stabilized by OG in ligand-binding pocket

A molecule of [OG](/xray-mp-wiki/reagents/detergents/og/) was identified in the retinal-binding pocket of the active Ops* conformation, replacing retinal and stabilizing the G-protein-interacting state. This was confirmed by the crystal structure of Ops* in complex with the synthetic G protein peptide GalphaCT2, derived from the key GPCR binding site on the C-terminal region of the G-alpha subunit.

### Structural homology between opsin and olfactory receptors

Opsin shares key features expected for olfactory receptors (ORs): a deep hydrophobic ligand-binding pocket accessible from the lipid bilayer, a hydrogen-bond network for ligand recognition, and conformational flexibility between active and inactive states. The hydrogen-bond pattern holding OG in the pocket is reminiscent of the dynamic hydrogen-bond pattern proposed for OR-odorant interactions, in which the receptor offers changing side chains for bonding.

### Detergent chain-length-dependent pocket occupancy

Various detergents ([DM](/xray-mp-wiki/reagents/detergents/dm/), OG, [NG](/xray-mp-wiki/reagents/detergents/nonylglucoside/), and [HpG](/xray-mp-wiki/reagents/detergents/heptylglucoside/)) can occupy the binding pocket in a chain-length-dependent manner, providing a model for how hydrophobic odorants enter ORs. The neopentyl glycol detergents ([LMNG](/xray-mp-wiki/reagents/detergents/lmng/), octyl glucose neopentyl glycol) showed only small inhibitory effects, suggesting they block the openings rather than entering the pocket.

### Opsin as structural template for OR homology modeling

Opsin can host various artificial hydrophobic retinal analogues, naturally occurring hydroxy analogues, and chemically distinct molecules like detergents containing multiple hydroxy groups. The Ops* structure illustrates how hydrophobic odorants, after partitioning into the membrane, can enter from the lipid bilayer into the 7TM scaffold. Ops* may serve as the best currently available structural template for homology modeling of ORs.

### Conserved solvent network in activated opsin links GPCR activation motifs

The 2.3-A resolution structure of activated opsin (PDB 4X1H) revealed an extensive water-mediated hydrogen-bonding network connecting the chromophore binding site to the G protein binding site over 35 A away. This continuous solvent network links three conserved GPCR activation motifs: the CWxP motif at the base of the chromophore binding site, the NPxxY motif at the end of Helix VII, and the (D/E)RY ionic lock motif. Three subsets of ordered solvent molecules were identified: (1) waters present in both active and ground states (structural role), (2) remodeled solvent retaining hydrogen bonding despite protein rearrangement, and (3) activation-state-specific solvent. Nonyl-glucoside (C9G) detergent molecules occupied the chromophore binding site in place of retinal, stabilizing an activated-state-like conformation.

### Ops*-ArrFL-1 structure reveals arrestin finger loop binding to active GPCR

The 2.75 A crystal structure of Ops* in complex with the ArrFL-1 peptide (PDB 4PXF, doi/10.1038##ncomms5801) reveals the structural basis for arrestin recognition of active GPCRs. The ArrFL-1 peptide (derived from residues 71-77 of rod photoreceptor arrestin finger loop, sequence DVMGLLL) binds in the same cytoplasmic crevice of the active receptor as the Gα C-terminus (GαCT), using the conserved consensus motif (E/D)x(I/L)xxxGL. The peptide adopts a reverse turn-like structure (C-cap) similar to GαCT upon binding. However, structural differences at the rim of the binding crevice reflect their divergent biological functions: G protein undergoes GDP/GTP exchange while arrestin blocks G protein access and scaffolds signaling proteins. Arg135 (E(D)RY motif) and Lys311 (NPxxY motif) form key interactions with the ArrFL-1 peptide.


## Cross-References

- [Bovine Rhodopsin (Dark State)](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) — Same protein in dark state with 11-cis-retinal bound (PDB 1GZM); structural basis for comparison to active Ops* state
- [Metarhodopsin II (Active Photointermediate)](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) — Active photointermediate of rhodopsin; opsin represents the decay product after all-trans-retinal is released
- [Octyl Glucoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent found bound in orthosteric ligand-binding pocket of Ops*, stabilizing active conformation
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent tested for reconstitution compatibility with opsin
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Neopentyl glycol detergent family, tested for pocket access in reconstitution experiments
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Shows strong concentration-dependent inhibition of rhodopsin reconstitution, fitting best into retinal-binding pocket
- [Nonylglucoside (NG)](/xray-mp-wiki/reagents/detergents/nonylglucoside/) — Tested for reconstitution inhibition, shows chain-length-dependent pocket occupancy; C9G occupied chromophore site in 4X1H structure
- [Heptylglucoside (HpG)](/xray-mp-wiki/reagents/detergents/heptylglucoside/) — Tested for reconstitution inhibition, shows chain-length-dependent pocket occupancy
- [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Natural chromophore ligand of rhodopsin; replaced by OG in the Ops* crystal structure
- [GPCR G Protein-Arrestin Common Interface](/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-arrestin-common-interface/) — Ops*-ArrFL-1 structure (PDB 4PXF) reveals the common GPCR-binding interface shared by G proteins and arrestins
