---
title: Thermotoga maritima SecA ATPase
created: 2026-06-09
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature07335]
verified: false
---

# Thermotoga maritima SecA ATPase

## Overview

SecA is the cytoplasmic ATPase motor of the bacterial Sec protein translocation machinery that drives post-translational secretion of proteins across the plasma membrane and membrane protein integration. The crystal structure of Thermotoga maritima SecA bound to the [SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) translocon complex (PDB 3DIN, 4.5 A resolution) revealed the conformational changes that occur upon [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) binding and provided mechanistic insights into how ATP hydrolysis drives polypeptide movement. SecA comprises two RecA-like nucleotide-binding domains (NBD1 and NBD2), a polypeptide-cross-linking domain (PPXD), a helical scaffold domain (HSD) with a two-helix finger, and a helical wing domain (HWD). Upon binding to the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) channel, the PPXD undergoes an ~80 degree rigid-body rotation to form a clamp over the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) pore, and the two-helix finger inserts into the cytoplasmic funnel of [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) to push polypeptides through the channel.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature07335 | 3DIN | 4.5 A | not specified | Thermotoga maritima SecA (residues 1-816) with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/), bound to T. maritima [SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) complex; ADP-[BeF3 (Beryllium Fluoride)](/xray-mp-wiki/reagents/ligands/bef3/) bound | ADP-[BeF3 (Beryllium Fluoride)](/xray-mp-wiki/reagents/ligands/bef3/) (transition state analog); beta-D-Octylglucoside (OG) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: T. maritima SecA (residues 1-816) with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) under IPTG-inducible promoter

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer | -- | 20 mM Tris pH 7.5, 1 M NaCl, 1 mM TCEP (HS buffer) + -- | Centrifuged 30 min at 205,000g at 4 C |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (His-tag) | Ni-NTA Sepharose (Qiagen) | HS buffer with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + -- | Washed with 200 ml HS buffer + 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), then 200 ml HS buffer + 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 6 M guanidine-HCl |
| Elution and refolding | Affinity elution with dialysis refolding | -- | D buffer (20 mM Tris pH 7.5, 0.5 M NaCl, 5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/)) + -- | Eluted in 50 ml HS buffer + 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 6 M guanidine-HCl; refolded by dialysis against D buffer overnight at 4 C |
| Size-exclusion chromatography | Gel filtration | Superdex S200 (GE Healthcare) | D buffer + -- | Fractions lacking 30 kDa proteolytic fragment pooled and concentrated to 100 uM |


## Crystallization

### doi/10.1038##nature07335

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | SecA-[SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) complex formed at 1:1.2 molar ratio, dialyzed against buffer containing 20 mM MES pH 6.5, 0.1 M NaCl, 10 mM MgCl2, 1 mM ADP, 2 mM BeCl2 |
| Notes | Crystals grown in presence of ADP-BeFx corresponding to intermediate state during ATP hydrolysis. Data collected at synchrotron beamlines ID-19 and 24ID at Argonne National Laboratory and X29 at Brookhaven National Laboratory. [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) used B. subtilis SecA as search model. |


## Biological / Functional Insights

### SecA undergoes large conformational changes upon SecY binding

When SecA binds to the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) complex, the PPXD rotates by ~80 degrees towards NBD2 as a rigid body with a ~10 degree tilt towards the membrane, with the hinge formed by two short beta-strands connecting PPXD and NBD1. The closed clamp formed by PPXD, NBD2, and HSD positions the polypeptide chain right above the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) pore. An evolutionarily conserved loop in PPXD (residues 360-370) contacts both NBD1 and NBD2 near the nucleotide-binding site.

### Two-helix finger mechanism for polypeptide translocation

A two-helix finger of the HSD inserts into the cytoplasmic funnel of [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/), with the loop connecting the two helices located right above the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) pore entrance. The finger has an ~45 degree angle relative to the membrane plane and rests in a cleft between the 6-7 loop and C-terminal tail of [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/). The two-helix finger is proposed to move up and down during the ATP hydrolysis cycle, pushing the polypeptide chain into the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) pore.

### SecA binding induces SecY lateral gate opening

SecA binding generates a window at the lateral gate of [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) formed by TM2b, TM3, TM7, and TM8. The displacement of TM7 opens a ~5 A gap between TM7 and TM2b towards the centre of the lipid bilayer. The plug helix (TM2a) moves away from the centre of the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) channel towards the external side, preparing the channel for signal sequence binding and opening.


## Cross-References

- [Thermus thermophilus SecYEG Translocon Complex](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) — SecA binding partner; translocon complex that forms the protein-conducting channel
- [Thermus thermophilus SecY Core Channel Subunit](/xray-mp-wiki/proteins/secretion-translocon/secy/) — SecA interacts with the SecY pore ring and lateral gate during translocation
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [BeF3 (Beryllium Fluoride)](/xray-mp-wiki/reagents/ligands/bef3/) — Related ligand or cofactor
- [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — Fusion tag for crystallization or purification
