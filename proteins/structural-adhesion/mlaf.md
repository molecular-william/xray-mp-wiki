---
title: E. coli MlaF ABC ATPase
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.60030]
verified: false
---

# E. coli MlaF ABC ATPase

## Overview

MlaF is the cytoplasmic ABC ATPase (nucleotide binding domain, NBD) component of the MlaFEDB ABC transporter complex from Escherichia coli. Together with the transmembrane domain protein MlaE, the periplasmic MCE domain protein [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaD/), and the STAS domain regulatory protein [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/), MlaF drives phospholipid trafficking across the bacterial envelope to maintain outer membrane integrity. MlaF exhibits a canonical ABC ATPase fold with catalytic and helical subdomains, and possesses a unique ~25 amino acid C-terminal extension (CTE) that forms a domain-swapped reciprocal 'handshake' with the adjacent MlaF subunit, stabilizing the MlaF dimer. The signature motif of MlaF (LSGGM) contains a rare methionine instead of the consensus glutamine at its final position, a feature conserved in Mla and TGD-like MCE transport systems.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.60030 | 6XGY | 2.9 A | P3_2 21 | Full-length E. coli MlaF (269 residues), residues 5-267 resolved, co-expressed with [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) with N-terminal His-TEV tag | ADP, Mg²⁺ |
| doi/10.7554##eLife.60030 | 6XGZ | 2.6 A | P2_1 2_1 2_1 | Full-length E. coli MlaF (269 residues), residues 5-267 resolved, co-expressed with [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/), apo form (no nucleotide) | None (apo) |

## Expression and Purification

- **Expression system**: E. coli Rosetta 2 (DE3), T7-based expression
- **Construct**: Full-length MlaF (269 residues) co-expressed with [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) from a bicistronic operon. MlaF with N-terminal Strep tag (optional), [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) with N-terminal His6-TEV tag. For MlaFEDB complex purification, constructs encoded the entire mlaFEDCB operon with N-terminal His-TEV tag on [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaD/).


### Purification Workflow

- **Expression system**: E. coli Rosetta 2 (DE3)
- **Tag info**: His6-TEV tag on [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) (for MlaFB complex), His-TEV tag on [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaD/) (for MlaFEDB complex)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Freeze-thaw / Emulsiflex | -- | 50 mM Tris pH 8.0, 300 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 1 mg/ml lysozyme, 0.5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 25U benzonase + -- | Freeze-thaw lysis for small-scale. Emulsiflex-C3 for large-scale. Clarified by centrifugation at 15,000g. |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (IMAC) | Ni-NTA agarose (GE Healthcare) | Ni Wash Buffer (50 mM Tris pH 8.0, 300 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/)); Ni Elution Buffer (50 mM Tris pH 8.0, 300 mM NaCl, 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/)) + -- | Batch binding at 4°C, followed by wash and elution |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 16/60 (GE Healthcare) | 20 mM Tris pH 8.0, 150 mM NaCl, 2 mM TCEP + -- | MlaFB complex elutes at ~40 kDa (1:1 heterodimer) |


## Crystallization

### doi/10.7554##eLife.60030

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | MlaFB complex at 24 mg/ml in 20 mM Tris pH 8.0, 150 mM NaCl, 2 mM TCEP |
| Reservoir | 0.7 M ammonium dihydrogen phosphate, 0.07 M sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 5.6, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Temperature | 18 |
| Growth time | Not specified |
| Cryoprotection | Reservoir solution supplemented with 5% [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) |
| Notes | Crystals of apo MlaFB (MlaF_1B_1, PDB 6XGZ). 100 nL + 100 nL drop. |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | MlaFB complex at 24 mg/ml supplemented with 2 mM ADP and 2 mM magnesium acetate in 20 mM Tris pH 8.0, 150 mM NaCl, 2 mM TCEP |
| Reservoir | 0.2 M magnesium formate |
| Temperature | 4 |
| Growth time | Not specified |
| Cryoprotection | Reservoir solution supplemented with 35% [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) |
| Notes | Crystals of ADP-bound MlaFB (MlaF_2B_2, PDB 6XGY). 100 nL + 100 nL drop. Phased using BALBES with search models 2OUK (MlaF) and 3F43 ([MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/)). |


## Biological / Functional Insights

### Unique C-terminal extension handshake

MlaF possesses a unique ~25 amino acid C-terminal extension (CTE, residues
247-269) that wraps around the neighboring MlaF subunit in a domain-swapped
reciprocal 'handshake'. Three hydrophobic residues (Tyr261, Leu265, Leu266)
at the tip of the CTE dock into a pocket at the MlaF-[MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) interface of the
adjacent subunit. Deletion of the CTE completely abolishes MlaF function in
cellular assays and prevents MlaF from stably associating with MlaE in the
MlaFEDB complex, despite having no effect on MlaF-[MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) binding. Artificial
dimerization via GCN4 leucine zipper partially rescues ΔCTE function,
suggesting the CTE promotes NBD dimerization.

### MlaF signature motif variation

MlaF contains a rare substitution in its ABC signature motif: 145-LSGGM-149
instead of the consensus LSGGQ. The methionine at the final position cannot
hydrogen bond to the 2' and 3' hydroxyls of the ATP ribose as glutamine does.
This substitution may impair MlaF's ability to discriminate between ATP and
deoxyATP or decrease its affinity for NTPs. Methionine at this position is
conserved in Mla and TGD-like MCE systems, as well as O-antigen and teichoic
acid transporters, suggesting functional similarity.

### MlaF-MlaB interaction defines a novel regulatory site

[MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) binds to the helical subdomain of MlaF at a site that is distant from
the ATP-binding pocket (~30 Å from nearest ADP). The binding interface
involves contributions from both MlaF subunits in the dimer, with the helical
subdomain making extensive contacts with all three [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) helices, and the CTE
of the opposite MlaF subunit providing additional contacts. This binding site
is distinct from all previously characterized ABC transporter regulatory
interactions, defining a potentially novel mechanism of ABC transporter
regulation through STAS domain proteins.


## Cross-References

- [E. coli MlaB STAS Domain Protein](/xray-mp-wiki/proteins/mlaB/) — Binding partner that stabilizes MlaF and promotes MlaFEDB complex assembly
- [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaD/) — Transmembrane/periplasmic component of the MlaFEDB complex
- [E. coli MlaC Periplasmic Lipid-Binding Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaC/) — Periplasmic shuttle protein in the Mla lipid transport pathway
- [E. coli MlaA Outer Membrane Lipoprotein](/xray-mp-wiki/proteins/miscellaneous/mlaA/) — Outer membrane component of the Mla lipid transport system
- [ADP](/xray-mp-wiki/reagents/ligands/adp/) — Bound nucleotide in the MlaF_2B_2 dimeric structure (post-hydrolysis state)
- [ABC Transporter](/xray-mp-wiki/concepts/abc-transporter-family/) — MlaF is the NBD of the MlaFEDB ABC transporter complex
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) — Related protein structure
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
