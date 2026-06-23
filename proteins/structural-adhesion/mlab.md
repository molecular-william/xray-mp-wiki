---
title: E. coli MlaB STAS Domain Protein
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.60030]
verified: false
---

# E. coli MlaB STAS Domain Protein

## Overview

MlaB is a small STAS (Sulfate Transporter and Anti-Sigma factor Antagonist) domain protein from Escherichia coli that binds to the ABC ATPase subunit [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) of the MlaFEDB phospholipid transport complex. MlaB consists of a minimalist STAS domain with a four-stranded beta-sheet packed against three alpha-helices, lacking the fifth beta-strand and additional C-terminal helix found in canonical STAS domain proteins. MlaB stabilizes [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) by binding to its helical subdomain and C-terminal extension, promoting the assembly of active MlaFEDB transporter complexes. The MlaB binding site on [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) defines a previously undescribed interaction surface on ABC transporters, suggesting a novel mechanism for post-translational regulation of ABC transporter activity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.60030 | 6XGY | 2.9 A | P3_2 21 | Full-length E. coli MlaB (97 residues), residues 2-97 resolved, co-expressed with [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/), N-terminal His6-TEV tag | None (ADP bound to [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/)) |
| doi/10.7554##eLife.60030 | 6XGZ | 2.6 A | P2_1 2_1 2_1 | Full-length E. coli MlaB (97 residues), residues 2-97 resolved, co-expressed with [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/), apo state | None |

## Expression and Purification

- **Expression system**: E. coli Rosetta 2 (DE3), T7-based co-expression with [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/)
- **Construct**: Full-length MlaB (97 residues) with N-terminal His6-TEV tag, co-expressed from a bicistronic operon with [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/). MlaB is not stable when expressed alone and is prone to precipitation; co-expression with [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) is required for purification in good yield.


### Purification Workflow

- **Expression system**: E. coli Rosetta 2 (DE3)
- **Tag info**: N-terminal His6-TEV tag on MlaB

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Freeze-thaw / Emulsiflex | -- | 50 mM Tris pH 8.0, 300 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 1 mg/ml lysozyme, 0.5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 25U benzonase + -- | Clarified lysate by centrifugation |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | IMAC | Ni-NTA agarose | 50 mM Tris pH 8.0, 300 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash); 50 mM Tris pH 8.0, 300 mM NaCl, 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) + -- | MlaB co-purifies with [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) as a stable complex |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 16/60 | 20 mM Tris pH 8.0, 150 mM NaCl, 2 mM TCEP + -- | MlaFB complex elutes at ~40 kDa |


## Crystallization

### doi/10.7554##eLife.60030

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | MlaFB complex at 24 mg/ml |
| Reservoir | 0.7 M ammonium dihydrogen phosphate, 0.07 M sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 5.6, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Temperature | 18 |
| Growth time | Not specified |
| Cryoprotection | Reservoir + 5% [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) |
| Notes | Co-crystallized with [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) as MlaFB complex. Apo structure (MlaF_1B_1, PDB 6XGZ). |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | MlaFB complex at 24 mg/ml + 2 mM ADP + 2 mM magnesium acetate |
| Reservoir | 0.2 M magnesium formate |
| Temperature | 4 |
| Growth time | Not specified |
| Cryoprotection | Reservoir + 35% [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) |
| Notes | ADP-bound structure (MlaF_2B_2, PDB 6XGY). Phased using BALBES. |


## Biological / Functional Insights

### Minimalist STAS domain architecture

MlaB is a minimalist member of the STAS domain family, consisting of a
four-stranded beta-sheet packed against three alpha-helices. Unlike canonical
STAS domains such as SpoIIAA which have a fifth beta-strand and an additional
C-terminal helix, MlaB's C-terminus is too short to form these elements.
MlaB is more structurally similar to the smaller STAS domains associated with
SLC26/SulP transporters. The conserved Ser/Thr residue (Thr52) implicated in
phosphoregulation of STAS domains is present in MlaB.

### MlaB stabilizes MlaF for complex assembly

MlaB is required for [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) stability and productive assembly of the MlaFEDB
transporter complex. [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) cannot be expressed and purified alone in significant
quantities, but co-expression with MlaB yields stable MlaFB complex. In cells,
deletion of mlaFEDCB operon components lacking MlaB (MlaFEDC) results in loss
of both [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) and MlaB from purified complexes. Overexpression of [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) fully
suppresses the mlaB knockout phenotype, indicating that MlaB has no essential
function in Mla transport beyond promoting [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) stability and association with
MlaED.

### STAS domain as an ABC transporter regulator

MlaB binds to the helical subdomain of [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) at a site distant from the ATP
binding pocket, defining a previously undescribed interaction surface on ABC
transporters. This binding mode is distinct from all other characterized ABC
transporter regulatory interactions. MlaB may regulate Mla transport activity
indirectly by modulating [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) stability and availability for complex assembly
with MlaED. This raises the possibility that STAS domain proteins may regulate
other ABC transporters through analogous mechanisms.


## Cross-References

- [E. coli MlaF ABC ATPase](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) — Binding partner; MlaF stabilization and complex assembly require MlaB
- [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaD/) — Transmembrane/periplasmic component of the MlaFEDB complex
- [E. coli MlaC Periplasmic Lipid-Binding Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaC/) — Periplasmic shuttle protein in the Mla pathway
- [E. coli MlaA Outer Membrane Lipoprotein](/xray-mp-wiki/proteins/miscellaneous/mlaA/) — Outer membrane component of the Mla system
- [ABC Transporter](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — MlaB regulates the MlaFEDB ABC transporter complex
- [ADP](/xray-mp-wiki/reagents/ligands/adp/) — ADP-bound state of the MlaF_2B_2 structure
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) — Additive used in purification or crystallization buffers
