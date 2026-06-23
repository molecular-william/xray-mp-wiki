---
title: "PcManGT Mannosyltransferase"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2020.06.016]
verified: false
---

# PcManGT Mannosyltransferase

## Overview

PcManGT is a crenarchaeal membrane glycosyltransferase from Pyrobaculum calidifontis involved in N-glycan biosynthesis. It belongs to the GT2 family of inverting glycosyltransferases and is the first glycosyltransferase of TACK superphylum origin to be characterized structurally and biochemically. PcManGT is a GDP-, dolichylphosphate-, and manganese-dependent mannosyltransferase. Its membrane domain includes three transmembrane helices (TMH1-TMH3) that topologically coincide with half of the six-transmembrane helix cellulose-binding tunnel in Rhodobacter spheroides cellulose synthase [BCSA](/xray-mp-wiki/proteins/enzymes/bcsa/). The enzyme is specifically stabilized by anionic dolichylphosphates and phospholipids, and shows a remarkable increase in catalytic activity when incorporated into bicelle membranes in the presence of Dol55-P. The crystal structures were determined in the unliganded state (2.6 A), in complex with GDP·Mn2+ (2.7 A), and with GDP-alpha-Man·Mn2+ (2.7 A).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2020.06.016 | 6YV7 | 2.6 | P212121 | Full-length PcManGT (UniProt A3MTD6, residues 1-351) from Pyrobaculum calidifontis, TEV-cleaved from GFP-His8 tag | Unliganded (apo) |
| doi/10.1016##j.jmb.2020.06.016 | 6YV8 | 2.7 | P212121 | Full-length PcManGT, TEV-cleaved from GFP-His8 tag, soaked with GDP and MnCl2 | GDP, Mn2+ |
| doi/10.1016##j.jmb.2020.06.016 | 6YV9 | 2.7 | P212121 | Full-length PcManGT, TEV-cleaved from GFP-His8 tag, soaked with GDP-alpha-Man and MnCl2 | GDP-alpha-Mannose, Mn2+ |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: PcManGT-TEV-GFP-His8 (codon-optimized Pcal_0472 gene) in pWaldo-GFPd vector, expressed in E. coli BL21(DE3)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction | -- | Terrific Broth + -- | Expression induced with 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600=1.0, 15-17 h at 18 C |
| Cell lysis | Homogenization | -- | PBS with protease inhibitor cocktail + -- | Cells lysed using Avestin EmulsiFlex C3 homogenizer, followed by sonication |
| Membrane collection | Centrifugation | -- | 25 mM K2HPO4 (pH 7.2), 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + -- | Low-speed spin at 10,000 rpm, then membrane pellet at 35,000 rpm (125,749 g) |
| Solubilization | Detergent solubilization | -- | 25 mM K2HPO4 (pH 7.2), 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1.5% DM (or [LAPAO](/xray-mp-wiki/reagents/detergents/lapao/), [LDAO](/xray-mp-wiki/reagents/detergents/ldao/)) | Membranes resuspended and solubilized in detergent |
| Affinity purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | 25 mM K2HPO4 (pH 7.2), 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient (30-500 mM) + 0.2% DM (or 0.3% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), 0.08% [LAPAO](/xray-mp-wiki/reagents/detergents/lapao/)) | Wash with 30 mM and 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), elution with 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| TEV cleavage | Enzymatic cleavage | -- | 25 mM K2HPO4 (pH 7.2), 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 0.5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/) + 0.2% DM | TEV protease at 1:10 molar ratio, overnight at 4 C. Cleaved PcManGT recovered as flow-through from reverse IMAC. |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 16/60 | 50 mM HEPES (pH 7.5), 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.1% DM (or 0.05% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), 0.07% [LAPAO](/xray-mp-wiki/reagents/detergents/lapao/)) | Final buffer: 50 mM HEPES pH 7.5, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% DM |


## Crystallization

### doi/10.1016##j.jmb.2020.06.016

| Parameter | Value |
|---|---|
| Method | [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) (in meso) |
| Protein sample | Purified PcManGT at 5.5 mg/ml in 50 mM HEPES (pH 7.5), 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% DM, mixed with 8% bicelles ([DMPC](/xray-mp-wiki/reagents/lipids/dmpc/):[CHAPSO](/xray-mp-wiki/reagents/detergents/chapso/), 2.8:1) |
| Reservoir | 0.1 mM HEPES (pH 7.5), 20% [PEG](/xray-mp-wiki/reagents/additives/peg/) 4000, 10% isopropanol, 10 mM MnCl2, 2% 1,2,3-heptanetriol |
| Temperature | 22 |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Crystals grew in space group P212121 with two molecules per asymmetric unit and ~50% solvent content. Experimental phases determined by SIRAS using Na2WO4 derivative. Data collected at Diamond Light Source (I24, I02), SOLEIL (PROXIMA1), ESRF (ID23-1), and Swiss Light Source (PXI X06SA). |


## Biological / Functional Insights

### First crystal structure of a crenarchaeal membrane glycosyltransferase

PcManGT is the first glycosyltransferase from the TACK superphylum of archaea to be structurally characterized. The overall fold features a catalytic GT-A extramembrane domain connected to two membrane-interface helices (IFH1, IFH2) and a transmembrane domain of three antiparallel TM helices. TMH3 is kinked 90 degrees midway across the membrane, forming a substratum interface helix (sub-IFH3). The three-TMH domain represents half of the six-helix cellulose-binding tunnel in [BCSA](/xray-mp-wiki/proteins/enzymes/bcsa/).

### Dolichylphosphate-dependent stabilization and activity

PcManGT is specifically stabilized by anionic dolichylphosphates (Dol55-P and Dol95-P) with DeltaTm values of 30 C and 22 C, respectively. Anionic phospholipids (PS, PG) also provide substantial stabilization. The dolichylphosphate-dependent behavior parallels that of PfDPMS. When incorporated into bicelles with Dol55-P, PcManGT shows five-fold increased donor hydrolysis activity, indicating that the natural acceptor is a Dol-PP-linked sugar intermediate of the N-glycan biosynthesis pathway.

### Donor specificity and catalytic mechanism

PcManGT uses GDP-alpha-Man as the natural donor substrate, with Mn2+ as the preferred divalent metal cofactor. [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) binding studies show Kd values in the low micromolar range for GDP and GDP-alpha-Man. The DXD motif (Asp135-Asp137) coordinates the diphosphate group via Mn2+. Despite classification as a GT2 inverting glycosyltransferase, PcManGT catalyzes hydrolytic side-reaction in the absence of acceptor, a feature associated with retaining mechanism.


## Cross-References

- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Primary solubilization and purification detergent
- [LAPAO](/xray-mp-wiki/reagents/detergents/lapao/) — Alternative detergent for solubilization and crystallization
- [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) — Alternative detergent for solubilization
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — 50 mM HEPES (pH 7.5) in SEC buffer and crystallization
- [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) — Crystallization performed in bicelles (in meso method)
- [Ni-NTA Affinity Chromatography](/xray-mp-wiki/methods/purification/ninta-affinity-chromatography/) — His8-tag purification
- [Size-Exclusion Chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final polishing step using Superdex 200
- [Protein N-Glycosylation](/xray-mp-wiki/concepts/protein-glycosylation/) — PcManGT involved in N-glycan biosynthesis in Pyrobaculum calidifontis
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) — Method used in structure determination or purification
