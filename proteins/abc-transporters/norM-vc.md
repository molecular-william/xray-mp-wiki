---
title: NorM-VC (Vibrio cholerae NorM) - MATE Family Multidrug Efflux Transporter
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09408]
verified: false
---

# NorM-VC (Vibrio cholerae NorM) - MATE Family Multidrug Efflux Transporter

## Overview

NorM-VC is a multidrug and toxic compound extrusion (MATE) family transporter from Vibrio cholerae that functions as a drug efflux pump. It is a secondary transporter with 12 transmembrane helices that exports a broad range of organic cations including [Ethidium - Fluorescent Intercalating Dye](/xray-mp-wiki/reagents/ligands/ethidium/) bromide, [Doxorubicin - Anthracycline Anticancer Drug](/xray-mp-wiki/reagents/ligands/doxorubicin/), and rhodamine 6G. NorM-VC represents the first crystal structure of a prokaryotic MATE family member and revealed the bilobate architecture characteristic of the MATE family with pseudo-symmetric N- and C-lobes (TM1-6 and TM7-12). The structure was solved in two crystal forms: a native crystal and a rubidium-bound crystal, revealing a cation-binding site centered on D371.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09408 | 2VBQ | 3.65 | P 212121 | Full-length NorM from Vibrio cholerae (V. cholerae), residues 1-458 | Rb+ in Crystal 2; no ligand in Crystal 1 (native) |

## Expression and Purification

- **Expression system**: E. coli BL21 DE3 transformed with pET19b-norM-VC expression vector
- **Construct**: pET19b-norM-VC fusion expression in E. coli BL21 DE3

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Recombinant NorM-VC production and native NorM-VC purification | Expression in E. coli BL21 DE3 / pET19b-norM-VC; native NorM-VC purified from V. cholerae membrane fraction | -- | -- + -- | Details not available in supplementary information; main paper required for full purification protocol |


## Crystallization

### doi/10.1038##nature09408

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization; two crystal forms obtained |
| Protein sample | Native NorM-VC for Crystal 1; NorM-VC soaked with Rb+ for Crystal 2 |
| Reservoir | -- |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | -- |
| Notes | Crystal 1 (native): P 212121, a=142.8, b=240.8, c=45.7 A; Crystal 2 (Rb+-bound): P 212121, a=159.6, b=241.7, c=46.2 A. Phasing by [NCS](/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/) averaging using PHASER. Data collection at CLS (08ID-1), ALS (BL 8.2.2), and SSRL (BL 11-1). |


## Biological / Functional Insights

### Bilobate 12-TM architecture with pseudo-symmetry

NorM-VC adopts the characteristic bilobate MATE family architecture with two pseudo-symmetric domains: an N-lobe (TM1-6) and a C-lobe (TM7-12) related by a pseudo-2-fold rotation axis. The structure contains two monomers (NorM1 and NorM2) in the asymmetric unit, each with 12 transmembrane helices. The internal cavity between the two lobes forms the substrate-binding pocket, which is accessible from the extracellular side in the outward-facing conformation.

### Cation-binding site centered on D371

A cation-binding site was identified in the internal cavity of NorM-VC, centered on residue D371 in TM10. Soaking crystals with Rb+ and Cs+ revealed distinct anomalous peaks at 5.5 sigma and 5.0 sigma respectively. Mutational analysis (D371N and D371A) abolished cation binding, confirming D371 as essential for cation coordination. This site is located near the proposed substrate-binding region and may play a role in the transport mechanism.

### Substrate binding profile

NorM-VC binds multiple drug substrates with measurable affinity. Fluorescence polarization assays revealed a Kd of 1.00 +/- 0.08 uM for [Doxorubicin - Anthracycline Anticancer Drug](/xray-mp-wiki/reagents/ligands/doxorubicin/) and a Kd of 2.09 +/- 0.0115 uM for rhodamine 6G. Functional assays showed that recombinant NorM-VC expressed in E. coli BL21 DE3 delta acrAB significantly reduces [Ethidium - Fluorescent Intercalating Dye](/xray-mp-wiki/reagents/ligands/ethidium/) bromide accumulation compared to vector-only controls, confirming its role as a multidrug efflux pump.

### Topology and membrane orientation

Topology was verified using single-cysteine mutagenesis combined with [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) labeling. Sixteen cysteine mutants (K10C, S26C, V76C, E91C, L101C, S103C, A149C, M164C, V182C, V216C, A260C, A296C, M323C, Y367C, S397C, F429C) were generated and analyzed by [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) difference Fourier maps. All 16 mutants showed [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) peaks consistent with the predicted topology: extracellular loops at positions 10, 76, 149, 216, 296, 397, and 429; cytoplasmic loops at positions 26, 91, 103, 164, 182, 260, 323, and 367.


## Cross-References

- [Doxorubicin](/xray-mp-wiki/reagents/ligands/doxorubicin/) — NorM-VC binds doxorubicin with Kd = 1.00 +/- 0.08 uM (Table S1)
- [Rhodamine 6G](/xray-mp-wiki/reagents/ligands/rhodamine-6g/) — NorM-VC binds rhodamine 6G with Kd = 2.09 +/- 0.0115 uM (Table S1)
- [MATE Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/mate-transporter-family/) — NorM-VC is the first prokaryotic MATE family member with a crystal structure
- [Major Facilitator Superfamily](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — MATE transporters are secondary transporters related to MFS family
- [NtMATE2 (Nicotiana tabacum MATE2)](/xray-mp-wiki/proteins/abc-transporters/ntmate2/) — Another MATE family member with crystal structure for comparison
- [CasMATE (Camelina sativa MATE Transporter)](/xray-mp-wiki/proteins/abc-transporters/casmate/) — Eukaryotic MATE transporter for structural comparisons
- [NCS](/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/) — Related biological concept
- [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) — Additive used in purification or crystallization buffers
- [Ethidium - Fluorescent Intercalating Dye](/xray-mp-wiki/reagents/ligands/ethidium/) — Related ligand or cofactor
