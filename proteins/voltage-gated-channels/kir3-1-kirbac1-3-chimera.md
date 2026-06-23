---
title: "Kir3.1-KirBac1.3 Chimeric GIRK Channel"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##sj.emboj.7601828]
verified: false
---

# Kir3.1-KirBac1.3 Chimeric GIRK Channel

## Overview

The Kir3.1 (GIRK1) K+ channel is a G-protein-gated inward rectifier that participates in heart rate control and neuronal excitability. A chimeric channel was constructed by replacing three-fourths of the transmembrane pore of mouse Kir3.1 with the pore of the prokaryotic KirBac1.3 channel from Burkholderia xenovorans, leaving the cytoplasmic pore and membrane interfacial regions of Kir3.1 origin. Two crystal structures were determined at 2.2 Å resolution, revealing a closed inner helix bundle gate and two conformations of the cytoplasmic pore (dilated and constricted), mediated by rigid-body movements of the G-loop. The selectivity filter is nearly identical to [KcsA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) (r.m.s.d. < 0.2 Å), demonstrating extreme structural conservation of the K+ selectivity mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##sj.emboj.7601828 | 2QKS | 2.2 | P4 | Chimeric channel — N-terminal KirBac1.3 sequence (aa 1-23 + LV insertion) fused to mouse Kir3.1 (aa 41-82, 178-371) with M180A mutation; C-terminal His6-tag (VPRGSGGLEHHHHHH); thrombin-cleavable N-terminus; expressed in pET-28b(+) | Rb+ ions (7 sites from RbCl soak), nonylglucoside (detergent molecule at PIP2-binding site) |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: Kir3.1-KirBac1.3 chimera in pET-28b(+); aa 1-23 KirBac1.3 + LV insertion + aa 41-82 and 178-371 of mouse Kir3.1 (M180A); C-terminal His6-tag; thrombin site for N-terminus removal
- **Notes**: N-terminus of KirBac1.3 retained for correct membrane insertion in E. coli, then removed by thrombin cleavage before crystallization
- **Induction**: 300 µM IPTG at OD600 = 2.0; temperature lowered to 23°C; 12-15 h induction
- **Media**: LB medium

### Purification Workflow

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: Full-length chimera with C-terminal His6-tag in pET-28b(+)
- **Tag info**: C-terminal His6-tag (VPRGSGGLEHHHHHH); N-terminal KirBac1.3 sequence removed by thrombin cleavage

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Shaker flask fermentation | -- | -- + -- | 16 L LB medium; cells grown at 37°C to OD600 = 2.0, then induced at 23°C for 12-15 h |
| Cell harvesting and resuspension | Centrifugation | -- | 50 mM Tris-HCl pH 7.5, 150 mM KCl + -- | Protease inhibitors: 100 µM PMSF, 1 µg/ml leupeptin, 1 µg/ml pepstatin, 1000× aprotinin |
| Cell lysis | French press | -- | 50 mM Tris-HCl pH 7.5, 150 mM KCl + -- | French pressure cell press at 15,000 psi, 4°C |
| Membrane extraction | Detergent solubilization | -- | 50 mM Tris-HCl pH 7.5, 150 mM KCl + 20 mM dodecylmaltopyranoside (DDM) | Gentle shaking for 2 h at room temperature; debris removed by centrifugation at 40,000 g for 20 min |
| Affinity purification | -- | -- | -- + -- | His6-tag purification (details not specified in text); N-terminal KirBac1.3 tag removed by thrombin cleavage before crystallization |
| Final purification and detergent exchange | Size exclusion chromatography (inferred) | -- | -- + Nonylglucoside | Purified as stable tetramer in nonylglucoside for crystallization; final sample contained channel in nonylglucoside |

**Final sample**: Purified chimera tetramer in nonylglucoside detergent


## Crystallization

### doi/10.1038##sj.emboj.7601828

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified Kir3.1-KirBac1.3 chimera in nonylglucoside |
| Reservoir | 120 mM KCl, 200 mM potassium phosphate, PEG 4000, pH 6.2 |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals in space group P4 (a = b = 98.42 Å, c = 92.62 Å); two unique subunits per asymmetric unit, producing two distinct four-fold symmetric channels (dilated and constricted cytoplasmic pore conformations). RbCl soak used to identify permeant ions at 2.4 Å. Data collected at Brookhaven X29 beamline. Resolution: 100-2.2 Å. |


## Biological / Functional Insights

### Extreme conservation of K+ selectivity filter structure

The selectivity filter of the Kir3.1-KirBac1.3 chimera and KcsA are nearly identical (r.m.s.d. < 0.2 Å for main chain atoms), within the error of measurement between independent refinements of KcsA structures. This demonstrates that the K+ selectivity filter requires extreme conservation of three-dimensional structure for its catalytic function. The deviations are smaller than the difference in ionic radius between K+ and Na+ (0.38 Å).

### Seven ion binding sites in the conduction pore

Four Rb+ ion positions in the selectivity filter (positions 1-4, corresponding to KcsA ions), a fifth in the central cavity, and a sixth and seventh between the transmembrane and cytoplasmic pores. The ion positions at the TMD-cytoplasmic interface are unique to this Kir channel structure and were identified by RbCl soaking experiments.

### Dual gates — inner helix bundle and G-loop

Two constrictions along the pore: (1) the inner helix bundle gate formed by Phe181 side chains that completely occlude the pore (closed conformation, similar to KirBac1.1), and (2) the G-loop (residues 301-309) at the apex of the cytoplasmic pore. Two structures in one crystal show the G-loop in dilated and constricted conformations. The dilated conformation is wide enough for a hydrated K+ to pass; the constricted conformation is lined by Met308 and too narrow for even a dehydrated K+ ion.

### G-loop gating by rigid-body domain movements

Gating of the cytoplasmic pore apex is mediated by rigid-body movements of the cytoplasmic pore subunits. In the dilated conformation, the G-loop exposes oxygen atoms (Thr306 and Gly307) on its surface; in the constricted conformation, Met308 sulfur atoms line a narrow constriction. This finding supports numerous studies identifying the G-loop as a potential gate in Kir channels.

### PIP2-interacting residues mapped onto the chimera

Several known PIP2-sensitive mutations from eukaryotic Kir channels (Kir1.1, Kir2.1, Kir3.x, Kir6.2) map to cationic clusters on the membrane-facing surface of the cytoplasmic pore (Lys188, Lys189, Arg219) and to buried positions (Arg190, Glu304, Arg313). A nonylglucoside detergent molecule was observed bound at the putative PIP2-binding site in the dilated conformation, adjacent to the G-loop and interfacial helix, suggesting competition between detergent and PIP2 for the binding pocket.

### Disease mutations in the G-loop

In Kir2.1, mutations within the G-loop (G300V, V302M, E303K) cause Andersen's syndrome. The equivalent positions in the chimera map to the G-loop region (residues 301-309). In Kir6.2, mutation I296L (equivalent to M308 in Kir3.1) causes a severe form of DEND syndrome characterized by neonatal diabetes and developmental abnormalities. These mutations cluster at the cytoplasmic pore apex, supporting its role in Kir channel gating.

### No channel activity in planar lipid bilayers

The chimera showed no detectable channel activity in planar lipid membranes (POPE:POPG 3:1). Possible reasons include: unmet lipid requirement, Kir3.1 normally functions as a heteromultimer (chimera is homomultimeric), lack of proper coupling between cytoplasmic and transmembrane pores, and that no prokaryotic Kir channel has demonstrated single-channel activity.


## Cross-References

- [GIRK1 Cytoplasmic Pore](/xray-mp-wiki/proteins/voltage-gated-channels/girk1-cytoplasmic-pore/) — Kir3.1 cytoplasmic domain structure; the chimera incorporates Kir3.1 cytoplasmic pore residues 41-82 and 178-371
- [KirBac Potassium Channels](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) — Related prokaryotic Kir channels; the chimera transmembrane pore derives from KirBac1.3
- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — High-resolution K+ channel structure used for selectivity filter comparison (r.m.s.d. < 0.2 Å)
- [Nonylglucoside (NG)](/xray-mp-wiki/reagents/detergents/nonylglucoside/) — Primary detergent for purification and crystallization; observed bound at PIP2-binding site
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used at 20 mM for membrane extraction during purification
- [French Press](/xray-mp-wiki/methods/cell-lysis/french-press/) — Cell lysis method at 15,000 psi
- [Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — The chimera structure demonstrates extreme structural conservation of the K+ selectivity filter
- [Channel Gating](/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/) — Dual-gate mechanism (inner helix bundle and G-loop) elucidated by two conformations in the same crystal
