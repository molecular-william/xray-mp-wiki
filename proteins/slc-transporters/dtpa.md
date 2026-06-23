---
title: "E. coli DtpA Peptide Transporter"
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1021##jacs.8b11343]
verified: false
---

# E. coli DtpA Peptide Transporter

## Overview

DtpA is a proton-dependent oligopeptide transporter (POT) from Escherichia coli and a member of the solute carrier 15 family (SLC15). It belongs to the major facilitator superfamily (MFS) of secondary active transporters. DtpA is notable for its high similarity to human PepT1 (SLC15A1) in ligand selectivity, transporting di- and tripeptides as well as peptidomimetic drugs including antiviral prodrugs such as [VALGANCICLOVIR](/xray-mp-wiki/reagents/antibiotics/valganciclovir) and valacyclovir. Unlike most characterized bacterial POTs which prefer dipeptides, DtpA prefers tripeptides, a property attributed to a characteristic intra-helical loop in transmembrane helix 10 that enlarges its binding cavity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##jacs.8b11343 | 6GS7 | 3.30 | P212121 | Full-length DtpA from E. coli (Uniprot P77304), N- and C-terminal His6-tag, co-crystallized with conformation-selective [NANOBODY](/xray-mp-wiki/reagents/protein-tags/nanobody) N00 | None (ligand-free, [GLYCINE](/xray-mp-wiki/reagents/buffers/glycine) buffer) |
| doi/10.1021##jacs.8b11343 | 6GS4 | 2.65 | P212121 | Full-length DtpA from E. coli (Uniprot P77304), N- and C-terminal His6-tag, co-crystallized with conformation-selective [NANOBODY](/xray-mp-wiki/reagents/protein-tags/nanobody) N00 | [VALGANCICLOVIR](/xray-mp-wiki/reagents/antibiotics/valganciclovir) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Full-length dtpA gene (Uniprot P77304) amplified from E. coli genome, cloned into pH27 vector with N- and C-terminal His6 tags
- **Notes**: Gene amplified from E. coli genome and cloned into pH27 vector. Expressed in E. coli cells. Purified using Ni-NTA affinity chromatography followed by size-exclusion chromatography.


### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Full-length DtpA, N- and C-terminal [HIS6-TAG](/xray-mp-wiki/reagents/protein-tags/his6-tag), pH27 vector

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | Terrific broth (TB) | DtpA expressed in E. coli |
| Cell lysis | Sonication | -- | Lysis buffer with protease inhibitor | Membranes collected |
| Solubilization | Detergent extraction | -- | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Membrane fraction solubilized with n-Dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm)) |
| Affinity chromatography | Ni-NTA affinity | Ni-NTA | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | [HIS6-TAG](/xray-mp-wiki/reagents/protein-tags/his6-tag) affinity purification |
| Size-exclusion chromatography | SEC | HiLoad 16/600 Superdex 75 pg | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM NaCl, 0.03% DDM + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | DtpA-N00 complex formation evaluated by analytical gel filtration on Superdex 200 5/150 GL |
| Final sample | Concentration | -- | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM NaCl, 0.03% DDM + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Concentrated to 13 mg/ml using 5 kDa cut-off concentrator, flash-frozen and stored at -80C |


## Crystallization

### doi/10.1021##jacs.8b11343

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Notes | Ligand-free DtpA-N00 in [GLYCINE](/xray-mp-wiki/reagents/buffers/glycine) buffer. Crystals grew in 0.1 M glycine pH 9.0, 35% PEG 400, 0.15 M CaCl2. Data collected at beamline P14, PETRA III at 100 K wavelength 0.976 A. Solved by molecular replacement using ligand-free structure as search model.
 |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Notes | DtpA-N00 complex with [VALGANCICLOVIR](/xray-mp-wiki/reagents/antibiotics/valganciclovir). Drug added to DtpA solution in powder form (20 mM estimated concentration) and N00 added. Best diffracting crystals grew in 0.1 M glycine pH 9.0, 35% PEG 400, 0.15 M CaCl2, 0.02% Anapoe-C12E10. Data collected at beamline P13, PETRA III at 100 K wavelength 0.966 A. Solved by molecular replacement using ligand-free structure as search model.
 |


## Biological / Functional Insights

### Tripeptide preference over dipeptides

DtpA preferentially binds and transports tripeptides over dipeptides, in contrast to most other POTs with known structures which show dipeptide preference. Tripeptide binding increased thermal stability by a median of 7.1 C compared to 2.4 C for dipeptides. The highest binding affinity by MST was for tripeptide LLA (Kd = 58 +/- 10 uM). This preference relates to the presence of an intra-helical loop in TM10, also found in PepTSo2.

### Valganciclovir binding mode

[VALGANCICLOVIR](/xray-mp-wiki/reagents/antibiotics/valganciclovir) binds in the ligand-binding site with its guanine base mimicking the N-terminal residue of a canonical peptide substrate, and its valine residue inserting into a pocket equivalent to the P2 peptide side chain binding pocket of PepTSo2. This binding mode was also modeled to apply to human PepT1 based on homology modeling. The binding cavity in DtpA is the largest among POTs with known structures, accommodating the guanine base of valganciclovir.

### TM10 intra-helical loop enlarges binding cavity

DtpA has a characteristic intra-helical loop in TM10 that shifts TM11 by 6.8 A (F424 Calpha in TM11) relative to POTs without this feature. This creates a significantly enlarged binding cavity, which appears to be an adaptation for binding and transport of larger substrates like tripeptides and drug prodrugs.

### Functional validation by mutagenesis

Five residues in the binding site (Y38, Y71, K130, N160, I399) were mutated to alanine. Binding affinities for di/tripeptides and drugs were strongly reduced and AK-AMCA uptake was abolished, confirming the location of the ligand-binding site by functional assays. Two additional mutants Y156A and F289L also abrogated uptake.


## Cross-References

- [E. coli YbgH Peptide Transporter](/xray-mp-wiki/proteins/mfs-transporters/ybgH/) — Another E. coli POT family member (DtpD) with reported crystal structure
- [PepT_So Oligopeptide Transporter](/xray-mp-wiki/proteins/mfs-transporters/pept-so/) — POT family member with intra-helical loop in TM10, similar substrate preference
- [PepT_St Proton-Dependent Oligopeptide Transporter](/xray-mp-wiki/proteins/mfs-transporters/pept-st/) — POT family member with reported crystal structure
- [POT Family](/xray-mp-wiki/concepts/transport-mechanisms/pot-family/) — DtpA is a member of the POT (proton-dependent oligopeptide transporter) family
- [Major Facilitator Superfamily](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — POT family is a subfamily of MFS transporters
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for DtpA solubilization, purification, and crystallization
- [Valganciclovir](/xray-mp-wiki/reagents/antibiotics/valganciclovir/) — Antiviral prodrug that binds to DtpA and is transported by it
- [Nb.AT110i1 Synthetic Nanobody](/xray-mp-wiki/reagents/antibodies/nb-at110i1/) — Conformation-selective nanobody technology used for DtpA crystallization (N00)
- [NANOBODY](/xray-mp-wiki/reagents/protein-tags/nanobody) — Reagent used in this study
- [VALGANCICLOVIR](/xray-mp-wiki/reagents/antibiotics/valganciclovir) — Reagent used in this study
