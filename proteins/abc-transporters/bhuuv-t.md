---
title: "Burkholderia cenocepacia Haem Importer Complex BhuUV-T"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms13411]
verified: false
---

# Burkholderia cenocepacia Haem Importer Complex BhuUV-T

## Overview

The BhuUV-T complex is a type II ATP-binding cassette (ABC) haem importer from the Gram-negative pathogen Burkholderia cenocepacia. It consists of the transmembrane domain dimer BhuU, the nucleotide-binding domain dimer BhuV, and the periplasmic haem-binding protein BhuT. The crystal structure reveals an inward-facing conformation in the nucleotide-free form, representing the post-translocation state of the haem transport cycle. The periplasmic gate is closed and the cytoplasmic gate is open. This structure provides mechanistic insights into the conformational transitions of type II ABC haem importers.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms13411 | unspecified | 3.2 | P2₁2₁2₁ | BhuU (TMD) dimer + BhuV (NBD) dimer + BhuT (PBP) | none (haem- and nucleotide-free) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: BhuU and BhuV co-expressed from a single plasmid with N-terminal 8 His-tag and enterokinase cleavage site on BhuU. BhuT (residues 40-311, signal sequence removed) expressed separately with N-terminal GST tag and PreScission protease cleavage site.
- **Induction**: 0.3 mM IPTG at OD600 0.6-0.8, further growth 20 h at 16°C
- **Media**: LB medium with ampicillin (50 µg/mL) and chloramphenicol (34 µg/mL)

### Purification Workflow

- **Expression system**: E. coli c41 (DE3) for BhuUV, E. coli Rosetta2 (DE3) for BhuT
- **Expression construct**: BhuU with N-terminal 8 His-tag + enterokinase site; BhuV; BhuT residues 40-311 with N-terminal GST tag + PreScission site

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press | -- | 50 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 2 mM MgCl₂, 10 µg/mL DNase, 0.2 mg/mL lysozyme + -- | Cell debris removed by centrifugation; membrane fraction obtained by ultracentrifugation at 66,000g for 1 h |
| Membrane solubilization | Detergent solubilization | -- | 50 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl + 2% (w/v) n-decyl-β-D-maltopyranoside ([DM](/xray-mp-wiki/reagents/detergents/dm/)) | Solubilized for 1 h at 4°C |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA agarose | 50 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.02% [DM](/xray-mp-wiki/reagents/detergents/dm/) | His-tagged [Bhuuv](/xray-mp-wiki/proteins/abc-transporters/bhuuv/) captured; GST-BhuT co-purified |
| Size-exclusion chromatography | Size-exclusion chromatography | -- | 50 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 0.02% [DM](/xray-mp-wiki/reagents/detergents/dm/) + 0.02% [DM](/xray-mp-wiki/reagents/detergents/dm/) | BhuUV-T complex co-purified |

**Final sample**: BhuUV-T complex in 50 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.02% DM


## Crystallization

### doi/10.1038##ncomms13411

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | BhuUV-T complex |
| Reservoir | unspecified |
| Temperature | 4°C or 20°C |
| Growth time | unspecified |
| Notes | Nucleotide-free form; BhuT exhibits poor electron density with high temperature factors, possibly due to alternative orientation |


## Biological / Functional Insights

### Inward-facing conformation of BhuUV-T

The BhuUV-T crystal structure reveals an inward-facing conformation in the nucleotide-free, haem-free form. The cytoplasmic gate is completely open, formed by separation of hydrophobic residues (L177, L178, I181) of TM5 from the other monomer. The periplasmic gate is tightly sealed by R204-D200 salt bridges and hydrophobic interaction (L203-L203') in helix H5a. This represents the post-translocation state of the haem transport cycle, previously uncharacterized for type II ABC transporters.

### BhuT-BhuU interaction interface

BhuT interacts with the periplasmic surface of BhuU. The α3-α4 helices of the N-terminal domain and α9-α10 helices and β-strands of the C-terminal domain of BhuT are bound into a shallow pocket on the BhuU dimer periplasmic surface. Binding is mediated by van der Waals contacts and salt bridges between E94 or E231 of BhuT with R84 of BhuU. These residues are highly conserved in type II ABC haem importers.

### Haem translocation channel

The haem translocation channel extends from below H5a to the cytoplasmic solvent region via the BhuU-BhuU and BhuV-BhuV dimerization interface. The channel wall is formed by TM3, TM5, TM8, and TM10. Per BhuU monomer, 28 hydrophobic residues, 9 polar residues (N108, S119, S120, T127, N184, T195, T207, S210, T319), and only 1 charged residue (D112) are found. No stable ligand binding site for haem [Iron](/xray-mp-wiki/reagents/additives/iron/) is present, suggesting hydrophobic residues transiently interact with haem during translocation.

### ATP-binding triggers BhuT dissociation

Pull-down assays demonstrate that [ATP](/xray-mp-wiki/reagents/ligands/atp/) or non-hydrolysable [ATP](/xray-mp-wiki/reagents/ligands/atp/) analogue ([Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/)) causes dissociation of GFP-BhuT from [Bhuuv](/xray-mp-wiki/proteins/abc-transporters/bhuuv/), while [ADP](/xray-mp-wiki/reagents/ligands/adp/) does not. This indicates that ATP-binding (not hydrolysis) is sufficient to reduce [Bhuuv](/xray-mp-wiki/proteins/abc-transporters/bhuuv/) affinity for BhuT, facilitating the conformational reset from inward- to outward-facing state after haem translocation.


## Cross-References

- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — BhuUV-T is a type II ABC transporter
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — Inward/outward-facing conformations illustrate alternating access
- [French Press Cell Lysis](/xray-mp-wiki/methods/cell-lysis/french-press/) — Used for cell lysis in BhuUV-T purification
- [n-Decyl-β-D-Maltopyranoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used for membrane solubilization
- [AMP-PNP](/xray-mp-wiki/reagents/ligands/amp-pnp/) — ATP analog used in pull-down assays
- [BhuUV Complex](/xray-mp-wiki/proteins/abc-transporters/bhuuv/) — BhuUV-T contains BhuUV as core complex
- [Yersinia pestis Heme Transporter HmuUV](/xray-mp-wiki/proteins/abc-transporters/hmuuv/) — Orthologous type II ABC haem importer; HmuUV outward-facing vs BhuUV-T inward-facing
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in the context of Tris Hcl
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in the context of DM
- [Iron](/xray-mp-wiki/reagents/additives/iron/) — Referenced in the context of Iron
