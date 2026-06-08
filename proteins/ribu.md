---
title: RibU (ECF-Type Riboflavin Transporter S Component from Staphylococcus aureus)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09488]
verified: true
---

# RibU (ECF-Type Riboflavin Transporter S Component from Staphylococcus aureus)

## Overview

RibU is the S component (substrate-binding protein) of the energy-coupling factor (ECF) type riboflavin transporter from Staphylococcus aureus. ECF transporters are a unique family of membrane transporters responsible for vitamin uptake in prokaryotes. RibU comprises six transmembrane segments, adopts a previously unreported transporter fold, and binds riboflavin on the periplasmic side.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09488 | TBD | 3.6 | P212121 | residues 10-141, 153-188 | riboflavin |

## Expression and Purification

- **Expression system**: E. coli
- **Induction**: 0.5 mM IPTG at A600 0.8, 14 h at 37 C

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press (2 passes at 15-20,000 psi) | N/A | 20 mM Tris-HCl, pH 8.0, 100 mM NaCl | Cell debris removed by centrifugation |
| Membrane isolation | Ultracentrifugation (150,000g, 1 h) | N/A | 20 mM Tris-HCl, pH 8.0, 100 mM NaCl | Membrane fraction collected |
| Solubilization | Detergent solubilization | N/A | 2% beta-NG in 20 mM Tris-HCl, pH 8.0, 100 mM NaCl | 2 h at 4 C, followed by ultracentrifugation (150,000g, 30 min) |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA agarose (Qiagen) | 20 mM Tris, pH 8.0, 500 mM imidazole, 0.4% beta-NG | Elution with 500 mM imidazole |
| Size-exclusion chromatography | Gel filtration | Superdex-200 (GE Healthcare) | 20 mM Tris, pH 8.0, 100 mM NaCl, 0.4% beta-NG | Peak fraction concentrated to 8 mg/ml for crystallization |

**Final sample**: 8 mg/ml in 20 mM Tris, pH 8.0, 100 mM NaCl, 0.4% beta-NG


## Crystallization

### doi/10.1038##nature09488

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Temperature | N/A |


## Biological / Functional Insights

### Riboflavin binding site

Riboflavin is bound on the periplasmic side, approximately 5 A into the predicted membrane surface. The ligand is nestled in a hydrophobic pocket formed by 13 conserved amino acids. Multiple hydrogen bonds stabilize riboflavin binding, including interactions from invariant residues around the substrate-binding pocket. Thr 43 and Lys 167, both from conserved positions, are within hydrogen-bonding distance of riboflavin. The binding affinity is approximately 0.6 nM, consistent with extensive protein-ligand interactions. Flavin mononucleotide binds with moderate affinity (36 nM), while flavin adenine dinucleotide shows no measurable binding.

### Novel transporter fold

RibU comprises six transmembrane segments with a unique fold not previously reported for any membrane transporter. A DALI search of the Protein Data Bank found no structurally homologous entry. The structure resembles a cylinder with rugged ends, positioned roughly perpendicular to the lipid membrane. The outer surface is predominantly hydrophobic, while cytoplasmic and periplasmic faces are enriched with charged amino acids.

### Conserved residues and transport mechanism

Most highly conserved residues cluster in the interior of the cylinder-shaped RibU molecule, with four invariant amino acids located around the substrate-binding pocket. The L1 loop (17 residues between TM1 and TM2, with 9 highly conserved) hovers above the substrate-binding site and is thought to serve as a gate. Upon riboflavin binding, the L1 loop may close down to interact with the substrate. Facilitated by the T-A-A' components through ATP hydrolysis, the TM1-3 module may move away from TM4-6, allowing the protein to adopt a transient inward-open conformation for substrate release into the cytoplasm.

### Structural similarity to particulate methane monooxygenase

While no full transporter structure is homologous to RibU, transmembrane segments 1-5 of RibU can be superimposed with chain F of particulate methane monooxygenase with an RMSD of 3.3 A over 124 aligned C-alpha atoms, suggesting limited structural similarity.

### ECF transporter conservation

Sequence alignment of RibU with representatives from eight bacterial species shows a high degree of pairwise sequence identity. This, combined with alignment with transporters for folate, thiamine precursor, and cobalamin precursor, suggests that S components of at least some ECF transporters contain six transmembrane segments, have a similar structure, and adopt the same membrane topology.


## Cross-References

- [Nonylglucoside (NG)](/xray-mp-wiki/reagents/detergents/nonylglucoside/) — Related nonionic glucoside detergent
- [Nonylmaltoside](/xray-mp-wiki/reagents/detergents/nonylmaltoside/) — Related nonionic maltoside detergent
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Eluent for Ni-NTA affinity chromatography
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component throughout purification
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Size-exclusion chromatography resin
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) — Affinity chromatography resin
- [Multi-Wavelength Anomalous Diffraction](/xray-mp-wiki/methods/structure-determination/multi-wavelength-anomalous-diffraction/) — Phasing method used for structure determination
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method used
