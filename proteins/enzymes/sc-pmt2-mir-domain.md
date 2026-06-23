---
title: "Pmt2-MIR Domain (S. cerevisiae Protein O-Mannosyltransferase MIR Domain)"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.61189]
verified: false
---

# Pmt2-MIR Domain (S. cerevisiae Protein O-Mannosyltransferase MIR Domain)

## Overview

The Pmt2-MIR domain is the luminal MIR (mannosyltransferase, IP3R, and RyR) domain of Pmt2, a member of the PMT2 subfamily of protein O-mannosyltransferases (PMTs) from Saccharomyces cerevisiae. PMTs are multispanning ER membrane glycosyltransferases that catalyze transfer of mannose from Dol-P-Man to serine/threonine residues of proteins. Pmt2 functions as a heterodimer with Pmt1 (Pmt1-Pmt2 complex), which accounts for the major O-mannosylation activity in yeast. The MIR domain adopts a canonical beta-trefoil fold (12 beta-strands) consisting of three MIR-motif repeats (MIRm1-3) spanning residues 339-532. The structure was solved at 1.6 A resolution by molecular replacement using SDF2 from Arabidopsis thaliana as a search model. The domain contains conserved carbohydrate-binding sites (sites alpha and beta) that bind mannose and O-mannosylated peptides, as well as a PMT2-subfamily-specific FKR motif at site delta. Site alpha is critical for processive O-mannosylation of S/T-rich protein substrates.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.61189 | 6ZQP | 1.6 | P 41 3 2 | Pmt2-MIR domain (residues 339-532) | Glycerol (site alpha); sulfate (site beta); glycerol (site delta) |
| doi/10.7554##eLife.61189 | 6ZQP | 2.3 | I 21 21 21 | Pmt2-MIR domain | Glycerol bound to site delta |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Pmt2-MIR domain (residues 339-532, UniProt P46983) with N-terminal His6 tag, expressed in BL21(DE3) or SHuffle T7 Express
- **Notes**: MIR domain of PMT1 family members (Pmt1, Pmt5) proved unstable; PMT2 family MIR domains (Pmt2, Pmt3) were thermostable and readily crystallized

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Pmt2-MIR with N-terminal His6 tag and 3C protease cleavage site, in pETHis vector
- **Tag info**: His6 tag cleaved by 3C protease for crystallization; retained for nanoDSF and MST analyses

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer | — | 20 mM Tris-HCl pH 7.0, 200 mM NaCl, 1 mM MgCl2, 20 mM imidazole, protease inhibitor cocktail |  |
| Centrifugation | Centrifugation at 48,000 x g, 25 min | — |  |  |
| HisTrap affinity chromatography | Affinity chromatography | HisTrap (GE Healthcare) | 20 mM Tris-HCl pH 7.0, 200 mM NaCl, 20 mM imidazole |  |
| Tag cleavage (optional) | 3C protease cleavage on column | — |  |  |
| Size-exclusion chromatography | SEC | Superdex 75 26/600 | 20 mM Tris-HCl pH 7.0, 150 mM NaCl |  |

**Final sample**: 13 mg/ml Pmt2-MIR in 20 mM Tris-HCl pH 7.0, 150 mM NaCl


## Crystallization

### doi/10.7554##eLife.61189

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 13 mg/ml Pmt2-MIR |
| Reservoir | 85 mM HEPES pH 7.5, 1.7 M ammonium sulfate, 0.2 M magnesium acetate, 5.45 mM sodium acetate, 1.7% (v/v) PEG 400, 15% (v/v) glycerol |
| Mixing ratio | 2:1 (200 nL protein + 100 nL reservoir) |
| Temperature | 18 C |
| Growth time | Not specified |
| Cryoprotection | Directly harvested and plunged into liquid nitrogen (cryoprotected by reservoir conditions) |


## Biological / Functional Insights

### MIR domain as a carbohydrate-binding module

The Pmt2-MIR domain functions as a carbohydrate-binding module (CBM) with beta-trefoil fold. Two conserved mannose-binding sites were identified: site alpha (in MIRm1/MIRm3 interface, with conserved histidines H362 and H364) and site beta (in MIRm2/MIRm1 interface, with H428 and H430). NMR chemical shift perturbations show mannose binds weakly to site beta (preferentially), while O-Man peptides bind with higher affinity primarily to site alpha. These sites are structurally homologous to CBM family 13 carbohydrate-binding sites.

### PMT2-subfamily-specific FKR motif at site delta

Site delta (MIRm3) contains a unique FKR motif (F516, K517, R518) specific to the PMT2 subfamily. This positively charged patch forms a trident that coordinates a glycerol ligand via hydrogen bonding. K517A partially compromises complementation of thermosensitive pmt2pmt4 phenotype, indicating a functional role. The FKR motif may mediate interactions with the Pmt1-TMD via a complementary site delta-prime.

### Site alpha is critical for processive O-mannosylation of S/T-rich substrates

Alanine substitution of conserved histidines at site alpha (H362A, H364A) reduces O-mannosylation of S/T-rich substrates (Hsp150, Scw4) but does not affect O-mannosylation of unfolded protein targets (UPOM) like ER-GFP. This suggests the MIR domain acts as a processivity factor: site alpha binds the O-Man product to keep it away from the active center or to increase local concentration of nearby unmodified serine/threonine residues for efficient catalysis on multi-acceptor substrates.

### Analogy to GalNAc-T2 lectin domain

The Pmt2-MIR domain is structurally and functionally analogous to the lectin domain of GalNAc-transferase 2 (GalNAc-T2). Superposition of Pmt2-MIRm1 site alpha with the GalNAc-T2 lectin domain (PDB: 5ajo) shows the glycerol in site alpha overlaps with the GalNAc moiety bound to the lectin domain. The distance between the active center and site alpha in the Pmt1-Pmt2 complex (PDB: 6p25) is similar to that in GalNAc-T2, consistent with a role in organizing multi-acceptor substrates.


## Cross-References

- [MIR Domain (Mannosyltransferase, IP3R, RyR)](/xray-mp-wiki/concepts/structural-mechanisms/mir-domain/) — Pmt2-MIR is the defining MIR domain characterized in this study
- [Pmt3-MIR Domain](/xray-mp-wiki/proteins/enzymes/sc-pmt3-mir-domain/) — Pmt3-MIR is a close homolog (PMT2 subfamily) with nearly identical structure
- [OST Catalytic Cycle](/xray-mp-wiki/concepts/enzyme-mechanisms/ost-catalytic-cycle/) — PMTs and OSTs share GT-C fold and similar ER luminal glycosylation mechanisms
