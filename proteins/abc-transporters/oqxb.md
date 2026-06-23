---
title: OqxB efflux pump from Klebsiella pneumoniae
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-25679-0]
verified: false
---

# OqxB efflux pump from Klebsiella pneumoniae

## Overview

OqxB is a Resistance-Nodulation-Division (RND) efflux pump from *Klebsiella pneumoniae* that contributes to multidrug antibiotic resistance. OqxB underwent horizontal gene transfer and is now found in other Gram-negative bacterial pathogens including *Escherichia coli*, *Enterobacter cloacae*, and *Salmonella* spp. It confers resistance against fluoroquinolones, nitrofurantoin, quinoxalines, tigecycline, and [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol). The crystal structure at 1.85 Angstrom resolution reveals a symmetric trimer wherein all three protomers adopt a binding/tight conformation, unlike the asymmetric trimers observed in other RND pumps ([ACRB](/xray-mp-wiki/proteins/acrB), [MEXB](/xray-mp-wiki/proteins/mexB)). Each protomer contains two bound [DDM](/xray-mp-wiki/reagents/detergents/ddm) molecules in the substrate-binding pocket. A unique charged arginine residue R157 in the substrate-binding pocket, absent in [ACRB](/xray-mp-wiki/proteins/acrB) and [MEXB](/xray-mp-wiki/proteins/mexB), forms hydrogen bonds with substrates and is critical for fluoroquinolone binding and efflux. The longer gate loop (g-loop) with two proline residues and a unique phenylalanine cage architecture distinguish OqxB from related pumps. Functional complementation assays demonstrated 8- to 16-fold increased MIC for fluoroquinolones upon OqxB expression, and the R157A mutant showed 4- to 8-fold improved MIC, validating the structural predictions.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-021-25679-0 | 7L0Q | 1.85 | P 65 2 2 | OqxB (residues 1-977) symmetric trimer | [DDM](/xray-mp-wiki/reagents/detergents/ddm) (2 molecules per protomer) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: OqxB (residues 1-977) with C-terminal hexa-histidine tag, cloned into modified pET-22b vector
- **Notes**: Expressed in E. coli C43(DE3) at 25 C for 8 hours with 0.1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) induction at A600nm of 0.6

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1 | Cell lysis by Microfluidizer | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.0, 0.5 mM Na-[EDTA](/xray-mp-wiki/reagents/additives/edta), 1 mM [MGCL2](/xray-mp-wiki/reagents/additives/mgcl2) | 3 passes at 15,000 psi. Membrane fraction collected by ultracentrifugation |
| 2 | Solubilization | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.0, 300 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Solubilized from membrane fraction |
| 3 | Affinity chromatography (Ni-NTA) | Ni-NTA Superflow (Qiagen) | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.0, 300 mM NaCl, 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) purification |
| 4 | Size-exclusion chromatography | — | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Final polishing step for crystallization |


## Crystallization

### doi/10.1038##s41467-021-25679-0

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | OqxB purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm) at ~10 mg/mL |
| Reservoir | 0.1 M sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate) pH 5.5, 0.1 M Li2SO4, 0.1 M NaCl, 20 mM [MGCL2](/xray-mp-wiki/reagents/additives/mgcl2), 34% [PEG400](/xray-mp-wiki/reagents/additives/peg400), 5 mM [ATP](/xray-mp-wiki/reagents/ligands/atp) |
| Temperature | 293 |
| Notes | Symmetric trimer structure with [DDM](/xray-mp-wiki/reagents/detergents/ddm) molecules bound in substrate pocket |


## Biological / Functional Insights

### Unique charged residue R157 in substrate-binding pocket

R157 is a unique positively charged arginine residue in the OqxB substrate-binding pocket that is absent in related pumps [ACRB](/xray-mp-wiki/proteins/acrB) and [MEXB](/xray-mp-wiki/proteins/mexB) (which have a small hydrophilic serine at the equivalent position). R157 forms hydrogen bond interactions with the [DDM](/xray-mp-wiki/reagents/detergents/ddm) molecule and is proposed to interact with zwitterionic fluoroquinolone antibiotics through its guanidino side chain. Molecular docking and MD simulations showed that ciprofloxacin interacts with R157, forming stable hydrogen bonds (>80% occupancy) between the fluoroquinolone carboxyl and carbonyl groups. The R157A mutation reduced efflux liability for fluoroquinolones by 4- to 8-fold, confirming its critical role in drug binding and efflux.

### Extended gate loop and phenylalanine cage

The OqxB gate loop (g-loop) is longer by two residues (16 vs. 14) than [ACRB](/xray-mp-wiki/proteins/acrB) and [MEXB](/xray-mp-wiki/proteins/mexB), containing two proline residues (P619 and P630) on either side of the loop. The conserved phenylalanine residues (F615 and F617) in [ACRB](/xray-mp-wiki/proteins/acrB) and [MEXB](/xray-mp-wiki/proteins/mexB) g-loops are replaced with L621 and A623 in OqxB. This is compensated by F626, which swings back toward the substrate-binding pocket, contributing to the unique phenylalanine cage architecture. These structural differences are responsible for the distinct binding mode of [DDM](/xray-mp-wiki/reagents/detergents/ddm) molecules in OqxB compared to [MEXB](/xray-mp-wiki/proteins/mexB).


## Cross-References

- [EDTA](/xray-mp-wiki/reagents/additives/edta) — Entity mentioned in text
- [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol) — Entity mentioned in text
- [IPTG](/xray-mp-wiki/reagents/additives/iptg) — Entity mentioned in text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm) — Entity mentioned in text
- [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) — Entity mentioned in text
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) — Entity mentioned in text
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes) — Entity mentioned in text
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) — Entity mentioned in text
- [ATP](/xray-mp-wiki/reagents/ligands/atp) — Entity mentioned in text
- [PEG400](/xray-mp-wiki/reagents/additives/peg400) — Entity mentioned in text
