---
title: GadC Glutamate/GABA Antiporter
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10917]
verified: false
---

# GadC Glutamate/GABA Antiporter

## Overview

GadC is a glutamate/GABA antiporter from the APC (amino acid-polyamine-organocation) superfamily of membrane transporters. It functions in the acid resistance system 2 (AR2) of Escherichia coli, exchanging extracellular L-glutamate for intracellular GABA to facilitate net proton efflux under acidic conditions. GadC comprises 12 transmembrane segments (TMs) and adopts an inward-open conformation with a C-terminal plug (C-plug) that blocks the substrate-binding cleft. The transport is strictly pH-dependent, with robust activity at pH 5.5 or below and no detectable transport above pH 6.5.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10917 | not specified | 2.95 A | P2_12_12_1 | Full-length E. coli GadC (residues 1-511) from strain O157:H7 | none (ligand-free, inward-open state with C-plug) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Full-length GadC (residues 1-511) with N-terminal His-tag, cloned in pET15b

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press | not applicable | 25 mM Tris-HCl pH 8.0, 150 mM NaCl + not specified | Homogenization of collected cells after ultracentrifugation of lysate |
| Membrane isolation | Ultracentrifugation | not applicable | 25 mM Tris-HCl pH 8.0, 150 mM NaCl + not specified | 1 h at 150,000g to collect membrane fraction |
| Solubilization | Detergent solubilization | not applicable | 25 mM Tris-HCl pH 8.0, 150 mM NaCl + 2% n-octyl-beta-D-glucopyranoside (beta-OG) | 2 h incubation at 4 C |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA (Qiagen) | 25 mM Tris-HCl pH 8.0, 500 mM NaCl, 20 mM imidazole, 0.4% n-nonyl-beta-D-maltopyranoside (NM) + 0.4% NM | His-tag removed on column |
| Size-exclusion chromatography | SEC | Superdex-200 10/30 (GE Healthcare) | 25 mM Tris-HCl pH 8.0, 150 mM NaCl, various detergents + 0.2% beta-NG or 0.023% LDAO (for crystallization) | Peak fractions collected |

**Final sample**: 10-15 mg/ml


## Crystallization

### doi/10.1038##nature10917

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | GadC, 10-15 mg/ml in 0.2% beta-NG, 0.023% LDAO |
| Reservoir | 21% PEG400, 100 mM Tris-HCl pH 8.0, 100 mM NaCl, 325 mM sodium acetate |
| Mixing ratio | not specified |
| Temperature | 18 C |
| Growth time | overnight to 1 week |
| Cryoprotection | flash-frozen in cold nitrogen stream at 100 K; platinum derivatives by 48 h soak in mother liquor containing 10 mg/ml K2Pt(NO2)4 |
| Notes | Rod-shaped crystals; best diffraction 2.95 A at SSRF beamline BL17U. SeMet and Pt-SAD derivatives also obtained. |


## Biological / Functional Insights

### C-terminal plug (C-plug) blocks inward-open conformation

GadC exists in a closed state where its extended C-terminal fragment (residues 477-511) forms a folded domain that completely blocks the path to the putative substrate-binding site. This C-plug is stabilized by hydrogen bonds including His491, Arg499, Arg497, His502, and Tyr503. Deletion of the C-plug (GadC 1-470) or missense mutations (H491A, R497A, R499A, H502A, Y503A) restored substrate transport at pH 6.5, where WT GadC showed no activity. The C-plug displacement is a prerequisite for transport activity, providing a gating mechanism unique among APC superfamily members.

### pH-dependent transport activity

GadC transports GABA/Glu only under acidic conditions. Transport is robust at pH 4.5, decreasing to 67% at pH 5.0, 32% at pH 5.5, and 8% at pH 6.0, with no detectable activity at pH 6.5 or above. This stringent pH dependence contrasts with AdiC, which retains moderate transport activity at basic pH values (up to pH 8). The pH dependence is shifted toward higher pH when the C-plug is deleted, indicating the C-plug contributes to pH sensitivity.

### Substrate specificity of GadC

GadC mediates transport of GABA, glutamate (Glu), glutamine (Gln), and to a smaller extent methionine (Met) and leucine (Leu). The substrate specificity was determined using a proteoliposome-based transport assay with 3H-labelled substrates at pH 5.5.

### Gating residues and transport path

Six potential gating residues were identified: Tyr96, Tyr214, Glu218, Trp308, Tyr378, and Tyr382. Mutations of these residues (Y30A, E218A, E304A, W308A, Y378A, Y382A) caused at least 90% decrease in substrate transport. W308A retained only 2% of WT activity. The transport path is sandwiched axially between the C-plug and the L7 loop, and surrounded laterally by TM1, TM3, TM6, TM8, and TM10.

### Rigid-body rotation mechanism

Structural alignment between outward-open AdiC and inward-open GadC reveals a clockwise rotation of the gate domain (TM1, TM2, TM6, TM7) by approximately 35 degrees relative to the core domain. This rigid-body movement between gate and core domains supports the alternating access mechanism. The gate domain undergoes the most drastic conformational changes among all 12 TMs, while core domain TMs (especially TM3, TM8, TM9) show minimal rearrangement. This mechanism is conserved with other transporters including Mhp1 and vSGLT.

### L7 loop gating at periplasmic side

The L7 loop at the periplasmic side, together with the C-plug at the cytoplasmic side, closes the GadC conformation. The L7 loop interacts with surrounding elements through hydrogen bonds and van der Waals contacts. A disulfide bond between L267C and N364C could be formed (Ca-Ca distance ~5.6 A), and oxidation with o-phenanthroline copper complex eliminated transport activity, which was restored by dithiothreitol reduction.


## Cross-References

- [AdiC Arginine/Agmatine Antiporter](/xray-mp-wiki/proteins/adic/) — Homologous APC superfamily member; used as structural comparison for transport mechanism
- [APC Superfamily (Amino Acid-Polyamine-Organocation Transporter Family)](/xray-mp-wiki/concepts/apc-superfamily/) — GadC belongs to the APC superfamily of membrane transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — GadC operates via alternating access between outward-closed/inward-open states
- [n-Octyl-beta-D-glucopyranoside (beta-OG)](/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/) — Primary detergent used for GadC membrane solubilization
- [n-Nonyl-beta-D-maltopyranoside (NM)](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-maltopyranoside/) — Detergent used in Ni-NTA wash and elution buffers during GadC purification
- [n-Nonyl-beta-D-glucopyranoside (beta-NG)](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) — Detergent used in GadC crystallization
