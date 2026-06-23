---
title: "Burkholderia cenocepacia Haem Importer Complex BhuUV"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms13411]
verified: false
---

# Burkholderia cenocepacia Haem Importer Complex BhuUV

## Overview

The BhuUV complex is the transmembrane and nucleotide-binding domain core of the type II ATP-binding cassette (ABC) haem importer from the Gram-negative pathogen Burkholderia cenocepacia. It consists of the transmembrane domain dimer BhuU and the nucleotide-binding domain dimer BhuV. The crystal structure in the nucleotide-free form reveals an inward-facing conformation where the cytoplasmic gate is open and the periplasmic gate is closed. This represents the post-translocation state of the haem transport cycle. BhuUV is a close ortholog of [Hmuuv](/xray-mp-wiki/proteins/abc-transporters/hmuuv/) from Yersinia pestis.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms13411 | unspecified | 2.8 | P2₁2₁2₁ | BhuU (TMD) dimer + BhuV (NBD) dimer (without BhuT) | none (nucleotide-free) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: BhuU and BhuV co-expressed from a single plasmid with N-terminal 8 His-tag and enterokinase cleavage site on BhuU.
- **Induction**: 0.3 mM IPTG at OD600 0.6-0.8, further growth 20 h at 16°C
- **Media**: LB medium with ampicillin (50 µg/mL)

### Purification Workflow

- **Expression system**: E. coli c41 (DE3)
- **Expression construct**: BhuU with N-terminal 8 His-tag + enterokinase site + BhuV

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press | -- | 50 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 2 mM MgCl₂, 10 µg/mL DNase, 0.2 mg/mL lysozyme + -- | Cell debris removed by centrifugation; membrane fraction obtained by ultracentrifugation at 66,000g for 1 h |
| Membrane solubilization | Detergent solubilization | -- | 50 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl + 2% (w/v) n-decyl-β-D-maltopyranoside ([DM](/xray-mp-wiki/reagents/detergents/dm/)) | Solubilized for 1 h at 4°C |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA agarose | 50 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.02% [DM](/xray-mp-wiki/reagents/detergents/dm/) | His-tagged BhuUV captured |
| Size-exclusion chromatography | Size-exclusion chromatography | -- | 50 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 0.02% [DM](/xray-mp-wiki/reagents/detergents/dm/) + 0.02% [DM](/xray-mp-wiki/reagents/detergents/dm/) | BhuUV complex purified |

**Final sample**: BhuUV complex in 50 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.02% DM


## Crystallization

### doi/10.1038##ncomms13411

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | BhuUV complex |
| Reservoir | unspecified |
| Temperature | 4°C or 20°C |
| Growth time | unspecified |
| Notes | Nucleotide-free form; 76 ligands and 22 water molecules resolved in refinement |


## Biological / Functional Insights

### Inward-facing conformation of BhuUV

The BhuUV structure (2.8 Å) reveals an inward-facing conformation in the nucleotide-free form, in sharp contrast to the outward-facing conformation of the orthologous [Hmuuv](/xray-mp-wiki/proteins/abc-transporters/hmuuv/) from Yersinia pestis. The cytoplasmic gate is completely open, with hydrophobic residues L177, L178, and I181 of TM5 separated from the other monomer. The periplasmic gate is sealed by R204-D200 salt bridges and hydrophobic interaction in helix H5a. This structure represents the post-translocation state of the type II ABC haem importer.

### Haem translocation channel architecture

The transmembrane channel extends from below H5a to the cytoplasmic solvent region. The channel wall is formed by TM3, TM5, TM8, and TM10. Per BhuU monomer, 28 hydrophobic residues, 9 polar residues (N108, S119, S120, T127, N184, T195, T207, S210, T319), and only 1 charged residue (D112) are found. D112 is the only charged residue in the BhuU dimer channel and is critical for haem transport activity, as the D112R mutant showed reduced [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis and was unstable during purification.

### Structural comparison with HmuUV

Structural alignment of BhuU and HmuU monomers (r.m.s.d. 0.8 Å for 135 Cα atoms in core TM helices) reveals that while TM1, TM2, TM6, TM7, TM8, and TM9 orientations are similar, TM3-5 and H5a show large deviations. The core TM helices of the dimers can rotate as a unit by 6°. The inward-facing BhuU has an open cytoplasmic gate while HmuU has a sealed cytoplasmic gate, consistent with their respective inward- and outward-facing conformations.


## Cross-References

- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — BhuUV is a type II ABC transporter
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — Inward/outward-facing conformations illustrate alternating access
- [BhuUV-T Complex](/xray-mp-wiki/proteins/abc-transporters/bhuuv-t/) — BhuUV is the core complex of BhuUV-T
- [French Press Cell Lysis](/xray-mp-wiki/methods/cell-lysis/french-press/) — Used for cell lysis in BhuUV purification
- [n-Decyl-β-D-Maltopyranoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used for membrane solubilization
- [Yersinia pestis Heme Transporter HmuUV](/xray-mp-wiki/proteins/abc-transporters/hmuuv/) — Orthologous type II ABC haem importer; HmuUV is outward-facing vs BhuUV inward-facing
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in the context of Tris Hcl
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in the context of DM
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Referenced in the context of ATP
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in the context of Imidazole
