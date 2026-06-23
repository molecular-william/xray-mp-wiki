---
title: "Pmt3-MIR Domain (S. cerevisiae Protein O-Mannosyltransferase MIR Domain)"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.61189]
verified: false
---

# Pmt3-MIR Domain (S. cerevisiae Protein O-Mannosyltransferase MIR Domain)

## Overview

The Pmt3-MIR domain is the luminal MIR domain of Pmt3, a member of the PMT2 subfamily of protein O-mannosyltransferases (PMTs) from Saccharomyces cerevisiae. Pmt3 is highly homologous to Pmt2 (both PMT2 subfamily members) and its MIR domain adopts the same canonical beta-trefoil fold. The structure was solved at 1.9 A resolution by molecular replacement using Pmt2-MIR as a search model. Pmt3-MIR is almost identical to Pmt2-MIR in overall fold, differing primarily in MIRm3 loop regions. Pmt3-MIR contains the same conserved carbohydrate-binding sites (sites alpha and beta) and the PMT2-subfamily-specific FKR motif.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.61189 | 6ZQQ | 1.9 | P 1 | Pmt3-MIR domain | -- |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Pmt3-MIR domain with N-terminal His6 tag and TEV protease cleavage site, expressed in BL21(DE3) or SHuffle T7 Express
- **Notes**: MIR domain was thermostable and readily formed crystals

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Pmt3-MIR with N-terminal His6 tag and TEV protease cleavage site
- **Tag info**: His6 tag cleaved by TEV protease

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer | — | 20 mM Tris-HCl pH 7.0, 200 mM NaCl, 1 mM MgCl2, 20 mM imidazole, protease inhibitor cocktail |  |
| Centrifugation | Centrifugation at 48,000 x g, 25 min | — |  |  |
| HisTrap affinity chromatography | Affinity chromatography | HisTrap (GE Healthcare) | 20 mM Tris-HCl pH 7.0, 200 mM NaCl, 20 mM imidazole |  |
| TEV protease cleavage | TEV protease cleavage overnight at 4 C | — |  |  |
| HisTrap reverse purification | Affinity chromatography (flow-through) | HisTrap |  | TEV protease and cleaved His-tag bind to column, Pmt3-MIR flows through |
| Size-exclusion chromatography | SEC | Superdex 75 26/600 | 20 mM Tris-HCl pH 7.0, 200 mM NaCl |  |

**Final sample**: 15 mg/ml Pmt3-MIR in 20 mM Tris-HCl pH 7.0, 200 mM NaCl


## Crystallization

### doi/10.7554##eLife.61189

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 15 mg/ml Pmt3-MIR |
| Reservoir | 0.1 M MES pH 6.0, 0.26 M calcium acetate, 15% (w/v) PEG 8000 |
| Mixing ratio | 2:1 (200 nL protein + 100 nL reservoir) |
| Temperature | 18 C |
| Cryoprotection | Quick soak in reservoir supplemented with 20% (v/v) glycerol before plunging into liquid nitrogen |


## Biological / Functional Insights

### Structural conservation within PMT2 subfamily MIR domains

Pmt3-MIR is structurally almost identical to Pmt2-MIR (rmsd below detection limits for core beta-trefoil fold). Both domains contain conserved carbohydrate-binding sites alpha and beta with identical key residues (histidine pairs H362/H364 in site alpha, H428/H430 in site beta), and the PMT2-specific FKR motif at site delta. The high structural conservation suggests all PMT2 subfamily MIR domains share the same carbohydrate-binding function.


## Cross-References

- [Pmt2-MIR Domain](/xray-mp-wiki/proteins/enzymes/sc-pmt2-mir-domain/) — Pmt2-MIR is the close homolog with nearly identical structure, solved in the same study
- [MIR Domain (Mannosyltransferase, IP3R, RyR)](/xray-mp-wiki/concepts/structural-mechanisms/mir-domain/) — Pmt3-MIR is a member of the MIR domain family
