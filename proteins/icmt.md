---
title: ICMT (Isoprenylcysteine Carboxyl Methyltransferase)
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [methyltransferase, membrane-protein, posttranslational-modification, xray-crystallography]
sources: [doi/10.1016##J.MOLCEL.2011.10.020]
category: proteins
layout: default
---


# ICMT — Isoprenylcysteine Carboxyl Methyltransferase

## Overview

ICMT (Isoprenylcysteine Carboxyl Methyltransferase) is an integral membrane methyltransferase that catalyzes the final step of CAAX motif processing in proteins such as Ras, Rho GTPases, and G protein γ subunits. It methylates the carboxyl group of the prenylated cysteine residue using S-adenosyl-L-methionine (SAM) as a methyl donor, augmenting the hydrophobicity of the prenyl membrane anchor for efficient membrane association.

## Structure

- **Protein**: *Methanosarcina acetivorans* ICMT (Ma-ICMT, MA2698) — prokaryotic ortholog of eukaryotic ICMT
- **Resolution**: 3.4 Å
- **PDB ID**: 4A2N
- **Architecture**: 5 transmembrane α helices (H1-H5) + short C-terminal cytosolic α helix (H6)
- **Topology**: Matches eukaryotic ICMT predictions
- **Cofactor**: S-adenosyl-L-homocysteine (SAH, reaction product of SAM) — required for crystallization

### Catalytic Mechanism

- **SAM binding pocket**: Enclosed within conserved C-terminal catalytic subdomain
- **Substrate access tunnel**: Links SAM methyl group to inner membrane
  - Upper hydrophobic region: accommodates prenyl lipid from membrane
  - Lower polar region: accommodates polar C terminus of prenylated protein
- **Key residue**: Arg163 (M2 motif) — positions substrate carboxylate for nucleophilic attack on SAM methyl group
- **Conserved motifs**: M1 (125RHPxY), M2 (163R[x]3EE)

### Lipid Binding

- **Endogenous lipid**: C9 alkyl chain observed in electron density
- **Location**: Tunnel between H1 and H2 helices
- **Function**: Mimics prenyl lipid substrate (e.g., farnesyl group)

## Expression and Purification

- **Expression**: *E. coli* C41(DE3) strain
- **Construct**: Ma-ICMT-GFP-His7 (TEV-cleavable C-terminal GFP His7 tag)
- **Expression conditions**: 20°C overnight
- **Purification**:
  - Ni-NTA affinity chromatography (His7 tag)
  - Ion exchange chromatography
  - Size-exclusion chromatography
- **Detergent**: 0.024% DDM maintained throughout purification

## Crystallization

- **Protein concentration**: 8 mg/ml
- **Buffer**: 20 mM MES pH 6.5, 200 mM NaCl, 10% glycerol, 0.024% DDM
- **Cofactor**: 5 mM SAH (S-adenosyl-L-homocysteine)
- **Additive**: 0.5 mg/ml polar lipids (Avanti Polar Lipids) — required for crystallization
- **Phasing**: Single-wavelength anomalous diffraction (SAD)
  - KAu(CN)2 or EMTS (ethylmercurithiosalicylate) derivatives
  - Multi-crystal averaging
- **Data collection**: Diamond Light Source beamlines I02 and I03
- **Refinement**: PHENIX with iterative manual building (COOT)

## Biological Function

- **CAAX processing**: Final step in posttranslational modification of CAAX motifs
- **Substrates**: Ras, Rho GTPases, G protein γ subunits, protein phosphatases, phosphodiesterases, nuclear lamins
- **Function**: Augments hydrophobicity of prenyl membrane anchor for efficient membrane association
- **Therapeutic target**: ICMT inhibition disrupts Rho-mediated cell migration and adhesion; potential anticancer target

## Related Enzymes

- **RCE1**: Ras converting enzyme 1 — endoprotease that cleaves -AAX tripeptide before ICMT action
- **Farnesyl transferase**: Attaches farnesyl lipid to cysteine of CAAX motif
- **Geranylgeranyl transferase**: Attaches geranylgeranyl lipid to cysteine of CAAX motif

## Cross-References

- [ddm](/xray-mp-wiki/reagents/detergents/ddm/) — DDM used for solubilization (0.024% throughout purification)
- [mes-buffer](/xray-mp-wiki/reagents/buffers/mes-buffer/) — MES buffer pH 6.5 used in crystallization
- [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — 10% glycerol in crystallization buffer
- [affinity-chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA affinity purification via His7 tag
- [size-exclusion-chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final SEC polishing step
- [tev-protease](/xray-mp-wiki/reagents/protein-tags/tev-protease/) — TEV-cleavable tag strategy

### Paper Details

- Yang et al. (2011) Molecular Cell 44: [DOI: 10.1016/j.molcel.2011.10.020] — Crystal structure of Ma-ICMT