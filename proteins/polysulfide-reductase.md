---
title: Polysulfide Reductase (PsrABC) from Thermus thermophilus
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NSMB.1434]
verified: false
---

# Polysulfide Reductase (PsrABC) from Thermus thermophilus

## Overview

Polysulfide reductase (PsrABC) from Thermus thermophilus is an integral membrane protein complex responsible for quinone-coupled reduction of polysulfide (Sn2-). It is a molybdenum/tungsten-containing bis-molybdopterin guanine dinucleotide (bis-MGD) oxidoreductase that uses menaquinone-7 as the endogenous electron donor and polysulfide as the terminal electron acceptor. The enzyme is expressed under aerobic conditions in this thermophilic bacterium and is proposed to function as a key energy-conserving enzyme in the respiratory chain, potentially coupling electron transfer to proton pumping across the membrane.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NSMB.1434 | unknown (not explicitly stated in paper) | 2.4 A | P212121 | Native PsrABC heterotrimeric complex from Thermus thermophilus. The dimeric (ABC)2 configuration has a total molecular weight of approximately 260 kDa. PsrA subunit (733 residues), PsrB subunit (194 residues), and PsrC subunit (integral membrane, 8 transmembrane helices). Each monomer contains two Mo-bis-MGD cofactors, five [4Fe-4S] clusters on PsrB, one [4Fe-4S] cluster on PsrA, and 1,306 resolved water molecules. | menaquinone-7, pentachlorophenol, ubiquinone-1 |

## Expression and Purification

- **Expression system**: Thermus thermophilus (HB27)
- **Construct**: His-tagged PsrABC complex from Thermus thermophilus HB27. The PsrA subunit N-terminus contains a twin-arginine translocase (TAT) motif, suggesting periplasmic localization. N-terminal sequencing confirmed absence of first 28 amino acids including the TAT signal peptide.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press | -- | -- + -- | Cells lysed by French press |
| Membrane isolation | Differential centrifugation | -- | -- + -- | Membranes isolated by centrifugation |
| Membrane solubilization | Detergent solubilization | -- | -- + n-dodecyl-beta-D-maltopyranoside (DDM) | Membranes solubilized in DDM |
| Affinity purification | Ni-NTA affinity chromatography | TALON | 20 mM Tris-HCl pH 8.0, 300 mM NaCl + DDM | Eluted with linear gradient from 100-280 mM NaCl |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex-200 | 30 mM Tris-HCl pH 8.0, 100 mM NaCl, 0.05% DDM + n-dodecyl-beta-D-maltopyranoside (DDM) | Column pre-equilibrated and run at 0.5 mL/min. Flow rate 0.5 mL/min |
| Concentration | Ultrafiltration | -- | 20 mM Tris-HCl pH 8.0, 0.05% DDM + n-dodecyl-beta-D-maltopyranoside (DDM) | Concentrated to approximately 15 mg/mL using Amicon Ultra-15 with 10 kDa MWCO filter. Purity approximately 95% by SDS-PAGE |


## Crystallization

### doi/10.1038##NSMB.1434

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | PsrABC complex at 15 mg/mL in 20 mM Tris-HCl pH 8.0, 0.05% DDM |
| Reservoir | 0.1 M MES pH 6.5, 30-34% PEG400, 200 mM CaCl2 |
| Temperature | 20 C |
| Growth time | 48 h for initial appearance; full size in approximately 2 weeks |
| Cryoprotection | not specified |
| Notes | Native crystals and quinone/inhibitor-bound complexes obtained from cocrystallization. MK-7, PCP, and UQ1 added to reservoir at 0.5-1 mM. |


## Biological / Functional Insights

### Dimeric architecture and physiological oligomerization

The crystal packing reveals an (ABC)2 dimer configuration with an extensive interface of 2,614 A2 between the two heterotrimeric monomers and an intricate hydrogen-bond network between PsrB subunits. The dimer is likely physiological, similar to the dimeric configuration found in nitrate reductase (NarGHI), another membrane-bound bis-MGD oxidoreductase. The overall molecular organization of PsrABC resembles those of formate dehydrogenase-N (FdnGHI) and NarGHI, with two membrane-associated subunits (PsrA and PsrB) and one integral membrane subunit (PsrC).

### Active site architecture and polysulfide reduction mechanism

The PsrA subunit contains two molybdopterin guanine dinucleotide cofactors (bis-MGD), designated P and Q following DMSO reductase nomenclature, and a cubane-type [4Fe-4S] cluster. The subunit folds into four distinct domains with internal pseudo two-fold symmetry. ArgA332 is key to polysulfide substrate coordination at the active site. During catalysis, molybdenum is proposed to become hexa-coordinated by sulfur atoms, with ArgA332 acting as a direct ligand. Substrate binding cleaves polysulfide, releasing Sn-1 2- and leaving a Mo[S]6 core. Electrons and protons are delivered via five [4Fe-4S] clusters on PsrB to the Mo center, generating H2S and leaving a Mo[S]5 core. HisA145 is proposed to act as a general acid-base catalyst.

### Electron transfer chain through iron-sulfur clusters

Four [4Fe-4S] clusters in PsrB and FeS-0 on PsrA are aligned in a single chain. Distances between adjacent redox centers are within the 14-A limit for physiological electron transfer. Two electrons and two protons are released from MK-7 (the bound substrate) and transferred via the iron-sulfur cluster chain to the bis-MGD cofactor to reduce polysulfide. The enzyme catalyzes: MKH2 → MK + 2H+ + 2e- (in the membrane) and Sn2- + 2e- + 2H+ → S + H2S.

### Menaquinone-7 binding pocket in PsrC

The quinone binding site is situated on the periplasmic side of the membrane in the N-terminal four-helix bundle of PsrC, in close proximity to FeS-4. It is composed of residues from TMII, TMIII, and the horizontal helix hII-III of PsrC, plus a short loop region (residues B91-B95) of the PsrB subunit. The pocket is mainly hydrophobic, with the quinone sandwiched between LeuC64 and IleC89. In the MK-7-bound structure, TyrC130 is a direct ligand of the O1 carbonyl group. HisC21, AspC60, and GluC67 are implicated in quinone coordination and proton removal. The equivalent of HisC21 is a tyrosine in all homologous enzymes.

### Proposed proton-pumping mechanism

PsrC accommodates a possible proton-relay network centered on a hydrophilic cavity partially occupied by water molecules. The relay network starts from GluC224 and ArgC177 on the cytoplasmic surface of the second helix bundle (hb2) and leads through hb2 to ArgC239 via ThrC220, SerC183, a water molecule, and ThrC155. The pathway may cross over to hb1 and connect to AspC60 and HisC21 via three water molecules. This suggests Psr could incorporate proton-translocation machinery energized by redox reactions in the quinone site, analogous to Complex I. Such a mechanism would provide efficient energy conservation in T. thermophilus.


## Cross-References

- [Menaquinone-7 (MK-7)](/xray-mp-wiki/reagents/cofactors/menaquinone-7/) — Endogenous quinone substrate and electron donor
- [Ubiquinone (Coenzyme Q10)](/xray-mp-wiki/reagents/cofactors/ubiquinone/) — Similar quinone electron carrier; UQ1 used as crystallization analog
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization and purification
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification and crystallization
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Related redox enzyme mechanism principle
- [Menaquinone](/xray-mp-wiki/reagents/ligands/menaquinone/) — General menaquinone family; MK-7 is specific isoform used by Psr
