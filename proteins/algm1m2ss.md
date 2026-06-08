---
title: AlgM1M2SS Alginate ABC Transporter
created: 2026-05-28
updated: 2026-05-28
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2015.06.021]
verified: false
---

# AlgM1M2SS Alginate ABC Transporter

## Overview

AlgM1M2SS is an ATP-binding cassette (ABC) importer from the alginate-assimilating bacterium Sphingomonas sp. A1, responsible for the import of the acidic polysaccharide alginate across the cytoplasmic membrane. The transporter comprises two transmembrane subunits (AlgM1 and AlgM2) forming a heterodimer and two nucleotide-binding domains (homodimer of AlgS). It belongs to the type I ABC importer family. The crystal structure of the AlgM1M2SS/AlgQ2 complex reveals an inward-facing conformation with a tunnel-like structure at the interface between the periplasmic binding protein AlgQ2 and the transmembrane domains, facilitating alginate translocation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2015.06.021 | -- | 3.2 | P212121 | AlgM1(d24)M2(H10)SS(E160Q) in complex with AlgQ2; 24-residue deletion in AlgM1, 10-His tag at C-terminus of AlgM2, E160Q mutation in AlgS | AlgQ2 (periplasmic binding protein), Delta-MMM (unsaturated alginate trisaccharide) |

## Expression and Purification

- **Expression system**: E. coli BL21-Gold(DE3)/pLysS
- **Construct**: AlgM1M2SS with 10-His tag at C-terminus of AlgM2, expressed from pET21b vector; AlgM1(d24) variant with 24-residue N-terminal deletion; AlgS(E160Q) mutant for trapping inward-facing conformation

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Overexpression | E. coli BL21-Gold(DE3)/pLysS transformed with pET21b vector; C-terminal His-tag on AlgM2 produced protein, N-terminal His-tag on AlgM1 did not | -- | LB medium + -- | pET21b vector most suitable for AlgM1M2SS overexpression; C-terminal His-tag on AlgM2 successful, N-terminal His-tag on AlgM1 failed |
| Solubilization and purification | Membrane protein solubilized in mixture of DM, CHAPSO, and Cymal-6; purified by affinity chromatography and functional reconstitution in liposomes | -- | 20 mM Tris-HCl (pH 8.0) + DM, CHAPSO, Cymal-6 | Purified to homogeneity and functionally reconstituted in liposomes for ATPase and transport assays |


## Crystallization

### doi/10.1016##j.str.2015.06.021

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 7 mg/ml AlgM1(d24)M2(H10)SS(E160Q), 3 mg/ml AlgQ2, 1 mM Delta-MMM, 3.6 mM DM, 16 mM CHAPSO |
| Reservoir | 18% PEG3000, 0.15 M NaCl, 0.1 M N-(2-acetamido)iminodiacetic acid (pH 6.6) |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | SeMet derivative crystallized separately with Cymal-6 instead of DM; binding-protein-free form also crystallized at 4.5 A resolution (P1 space group) |

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion (SeMet derivative) |
| Protein sample | 7 mg/ml SeMet-AlgM1(d24)M2(H10)SS(WT), 3 mg/ml AlgQ2, 1 mM Delta-MMM, 1.2 mM Cymal-6, 16 mM CHAPSO |
| Reservoir | 18% PEG4000, 0.15 M sodium potassium tartrate, 0.1 M N-(2-acetamido)iminodiacetic acid (pH 6.6) |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | SeMet derivative used for phasing; structure solved by molecular replacement using MalF, MalG, MalK subunits from PDB 2R6G |


## Biological / Functional Insights

### Inward-facing conformation of AlgM1M2SS

The crystal structure of AlgM1M2SS in complex with AlgQ2 adopts an inward-facing conformation, with AlgM1 and AlgM2 open to the cytoplasm and the ATP-binding sites of the AlgS dimer widely separated. This conformation is similar to the resting state of the maltose transporter MalFGK2 without its binding protein MalE. Unlike the maltose transporter which undergoes conformational changes upon solute-binding protein interaction, AlgM1M2SS binds AlgQ2 without conformational change, suggesting the ABC transporter in the resting state conformation can bind solute-binding protein directly.

### Tunnel-like alginate translocation route

The interaction between AlgQ2 and AlgM1M2SS induces the formation of an alginate-binding tunnel-like structure accessible to the solvent. The uncovered part of the alginate-binding cleft of AlgQ2 resembles the entrance of a tunnel that continues inside AlgQ2. AlgQ2 accommodates oligoalginate at the back of the tunnel, with a length of approximately 30 A corresponding to alginate heptasaccharides. The tunnel accommodates the non-reducing terminal residue of alginate while other residues extend outward.

### Charged inner cavity for acidic saccharide import

The translocation route inside the transmembrane domains contains charged residues suitable for the import of acidic saccharides. Charged residues in the cavity include AlgM1 Lys195, Glu196, Asp200, Arg249, Glu259, and AlgM2 Arg209. Histidine residues AlgM1 His141 and His252 are also present. Mutagenesis of H141A and E196A decreased both ATPase and transport activities to less than 50%, while E259A, R209A, and E196A/E259A mutants showed transport activities below 40%. This contrasts with the maltose transporter, which lacks charged residues in its inner cavity.

### Substrate specificity and transport range

AlgM1M2SS specifically transports oligoalginate trisaccharides to heptasaccharides. ATPase activity is enhanced by poly- and oligoalginate, with the strongest response to tetrasaccharides and longer chains. Transport assays show that oligoalginate up to heptasaccharides can be transported, but polysaccharides longer than heptasaccharides (8-20M and 8-20G) are not transported in the in vitro system. This suggests additional factors such as the alginate concentrator pit on the cell surface may be required for macromolecular transport.


## Cross-References

- [AcrB Multidrug Efflux Pump](/xray-mp-wiki/proteins/acrB/) — AcrB is a related ABC transporter from E. coli, providing comparative framework for ABC transporter structure-function analysis
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM tested for AlgM1M2SS solubilization in ATPase activity assays
- [3-[(3-Cholamidopropyl)dimethylammonio]-1-propanesulfonate (CHAPSO)](/xray-mp-wiki/reagents/chapso/) — CHAPSO used in crystallization sample solution for AlgM1M2SS/AlgQ2 complex
- [Tris (Tris-Hydroxymethyl-Aminomethane)](/xray-mp-wiki/reagents/buffers/tris/) — Tris-HCl buffer (pH 8.0) used in purification and functional assays
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — ABC transporters operate via alternating-access mechanism between inward and outward facing conformations
