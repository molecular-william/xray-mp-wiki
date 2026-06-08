---
title: Interleukin-17 Receptor A (IL-17RA)
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.immuni.2020.02.004]
verified: false
---

# Interleukin-17 Receptor A (IL-17RA)

## Overview

IL-17RA is the founding and best-known member of the interleukin-17 receptor (IL-17R) family. It is a single-pass type I transmembrane glycoprotein that serves as the shared receptor for several members of the IL-17 cytokine family, including IL-17A, IL-17F, and IL-17A/F. IL-17RA was traditionally believed to operate in concert with IL-17RC to mediate IL-17 signaling. However, structural analysis revealed that IL-17RC and IL-17RA compete for the same binding surface on IL-17F. IL-17RA has a shorter extracellular domain compared to IL-17RC and is classified as a "short receptor." It contains a cytoplasmic SEFIR domain for intracellular signaling.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.immuni.2020.02.004 | 3JVF | not specified | not specified | Human IL-17RA extracellular domain (referenced structure from Ely et al., 2009; the numbering in the PDB differs from UniProt Q96F46 by +31)
 | IL-17F |

## Expression and Purification

- **Expression system**: HEK293S cells (human embryonic kidney cells deficient in N-acetylglucosaminyl-transferase I)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Transient expression in HEK293S cells | -- | V3 medium (Novartis medium, patent WO 2011/134920 A1) + -- | Full-length IL-17RA ECD (residues 33-320 of UniProt entry Q96F46) fused to CD33 signal peptide and C-terminal APP4-tag, cloned into pRS5-derived vector
 |
| SEC purification | Size-exclusion chromatography | -- | -- + -- | IL-17RA purified by SEC; used for ITC and SEC-MALS experiments
 |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### IL-17RA competes with IL-17RC for IL-17F binding

IL-17RA forms an asymmetric 1:1 complex with IL-17F (one IL-17RA chain per IL-17F homodimer), while IL-17RC binds symmetrically on both sides forming a 2:1 complex. The footprints of IL-17RC and IL-17RA on IL-17F overlap extensively, with both receptors interacting with the same three binding sub-sites (S1-S3). IL-17RC blocks the IL-17RA binding site, paradoxically competing with its co-receptor for cytokine binding.

### IL-17RA induces conformational changes in IL-17F

Upon binding IL-17RA, the cytokine undergoes large conformational changes that break the two-fold symmetry of the IL-17F homodimer. The first beta-hairpin shifts outward by approximately 3 A, and the second beta-hairpin of the same IL-17F subunit is pushed up to approximately 13 A outward by the IL-17RA R1 motif. In contrast, IL-17RC binding preserves the symmetry of the cytokine.

### IL-17RA is a short receptor

IL-17RA has a short extracellular domain compared to IL-17RC. The last 17 amino acid residues of the IL-17RA ECD before the predicted transmembrane segment (304-PEMPDTPEPIPDYMPPLW-320) were disordered in all published X-ray analyses. In contrast, IL-17RC is classified as a tall receptor with extended D3-D4 stalk domains.

### IL-17A drives heteromeric complex formation more efficiently than IL-17F

In the presence of both IL-17RA and IL-17RC, IL-17A readily drives formation of the heteromeric IL-17RC:IL-17RA:IL-17A complex. IL-17F preferentially forms a symmetrical complex with IL-17RC, requiring approximately 250-fold higher concentrations than IL-17A in TR-FRET assays to achieve a similar signal.


## Cross-References

- [Interleukin-17 Receptor C (IL-17RC)](/xray-mp-wiki/proteins/il-17rc/) — Co-receptor that competes with IL-17RA for cytokine binding
- [Interleukin-17F (IL-17F)](/xray-mp-wiki/proteins/il-17f/) — Cytokine that forms asymmetric 1:1 complex with IL-17RA
- [Interleukin-17A (IL-17A)](/xray-mp-wiki/proteins/il-17a/) — Cytokine that efficiently drives heteromeric IL-17RC:IL-17RA:IL-17A complex
- [Tall Receptor](/xray-mp-wiki/concepts/tall-receptor/) — IL-17RA classified as a short receptor, contrasting with tall IL-17RC
- [Competitive Receptor Binding](/xray-mp-wiki/concepts/competitive-receptor-binding/) — IL-17RA and IL-17RC compete for the same binding surface on IL-17F
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Related precipitant used in crystallization
