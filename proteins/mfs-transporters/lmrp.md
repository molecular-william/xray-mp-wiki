---
title: LmrP Multidrug Transporter from Lactococcus lactis
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-020-0464-y]
verified: false
---

# LmrP Multidrug Transporter from Lactococcus lactis

## Overview

LmrP is a prototypical multidrug efflux pump from Lactococcus lactis belonging
to the Major Facilitator Superfamily (MFS). It exports structurally diverse
lipophilic cationic compounds ranging from antibiotics to DNA dyes, including
Hoechst 33342, ethidium bromide, roxithromycin, tetraphenyl phosphonium (TPP+),
verapamil, and tetracycline. LmrP uses a proton-motive force for drug efflux
and alternates between inward-open and outward-open conformations depending on
protonation states of key acidic residues (Asp68 and Glu327). The 2.9 A crystal
structure of LmrP bound to Hoechst 33342 in an outward-open state revealed an
embedded lipid (phosphatidylglycerol, PG) within the substrate-binding cavity,
suggesting a mechanism for polyspecificity where the lipid provides a malleable
hydrophobic component to accommodate diverse substrates.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41594-020-0464-y | 6T1Z | 2.9 | C2221 | LmrP delta199-202 (loop deletion mutant), expressed in Lactococcus lactis NZ9000 | Hoechst 33342 |

## Expression and Purification

- **Expression system**: Lactococcus lactis NZ9000
- **Construct**: Full-length LmrP with delta199-202 deletion; pHLP5-3C expression plasmid; nisin-inducible

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Cell lysis and membrane vesicle preparation | High-pressure homogenizer (6 passes at 15,000 psi) | — | 100 mM HEPES pH 7, 300 mM NaCl, 20% (v/v) glycerol | Cells treated with lysozyme (5 mg/mL), MgSO4 (10 mM), and DNase I (10 ug/mL) before lysis; membranes collected by ultracentrifugation at 125,000g |
| 2. Solubilization | Detergent solubilization | — | n-Dodecyl-beta-D-maltoside (beta-DDM) | Membranes solubilized with 2.4% (w/v) beta-DDM in water for 1 h at 4 C; insoluble fragments removed at 100,000g |
| 3. Affinity chromatography | Ni-NTA affinity | Ni-NTA (Qiagen) | 50 mM HEPES pH 7, 150 mM NaCl, 10% (v/v) glycerol, 0.05% beta-DDM | 10 mM imidazole for binding; 20 mM imidazole wash; 250 mM imidazole elution |
| 4. Desalting | PD10 desalting column | — | 50 mM HEPES pH 7, 150 mM NaCl, 10% (v/v) glycerol, 0.05% beta-DDM | Imidazole removal |
| 5. Size-exclusion chromatography | Gel filtration | SDX 200 10/300 GL increase (GE Lifescience) | 20 mM HEPES pH 7, 100 mM NaCl, 10% (v/v) glycerol, 0.02% beta-DDM | Concentrated using spin-concentrators (VWR) |


## Crystallization

### doi/10.1038##s41594-020-0464-y

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | Purified LmrP in 20 mM HEPES pH 7, 100 mM NaCl, 10% glycerol, 0.02% beta-DDM, co-crystallized with Hoechst 33342 |
| Reservoir | Not explicitly specified in paper (see Methods for detailed crystallization screening) |
| Temperature | Not specified |
| Notes | Crystallization required extensive screening; precise control of lipidation state essential; highest-resolution crystals required delta199-202 loop deletion; co-crystallization with Hoechst 33342; SeMet derivative crystals used for phasing |


## Biological / Functional Insights

### Embedded lipid in the binding cavity

The crystal structure reveals a phosphatidylglycerol (PG) lipid embedded within the substrate-binding cavity of LmrP, in close proximity to bound Hoechst 33342. The lipid likely originates from the native L. lactis membrane and remains bound through purification. Molecular dynamics simulations show that the anionic lipid (POPG) stabilizes the observed ligand-bound conformation by maintaining the Arg14-Asp142 salt bridge in the N-lobe.

### Limited conformational adaptation to substrates

DEER spectroscopy with six structurally diverse substrates (Hoechst 33342, ethidium bromide, roxithromycin, TPP+, verapamil, tetracycline) shows that LmrP adopts a common outward-open conformation for high-affinity binding without requiring large conformational changes of the protein scaffold.

### Substrate-dependent role of embedded lipid

Mutations that disrupt lipid binding (S52Y, T56Y, N116Y) reduce transport of Hoechst 33342, tetracycline, and erythromycin, but do not affect clindamycin transport, demonstrating substrate-specific dependence on the embedded lipid. This suggests the lipid contributes to polyspecificity by providing a malleable hydrophobic environment.

### Native MS confirms tightly bound PG

Native mass spectrometry of LmrP reconstituted in DOPE/DOPG nanodiscs shows a tightly bound DOPG molecule that is lost in the N116Y mutant, confirming the specificity of PG binding in the cavity.


## Cross-References

- [Major Facilitator Superfamily](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) — LmrP is a prototypical MFS multidrug transporter
- [Antibiotic Efflux Pump](/xray-mp-wiki/concepts/transport-mechanisms/antibiotic-efflux-pump/) — LmrP is a multidrug efflux pump; the paper discusses mechanism of polyspecific drug export
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — LmrP alternates between inward-open and outward-open states depending on protonation
- [Substrate Polyspecificity in SMR Transporters](/xray-mp-wiki/concepts/transport-mechanisms/substrate-polyspecificity-smr-transporters/) — The embedded lipid mechanism proposed may relate to polyspecificity mechanisms across transporter families
- [POPG](/xray-mp-wiki/reagents/lipids/popg/) — POPG (DOPG analog) is the embedded lipid in LmrP binding cavity
- [Hoechst 33342](/xray-mp-wiki/reagents/additives/hoechst-33342/) — Hoechst 33342 is the substrate in the crystal structure
- [MdfA (E. coli Multidrug Transporter)](/xray-mp-wiki/proteins/mfs-transporters/mdfa/) — MdfA is another MFS multidrug transporter with known outward-open structure, used for comparison
- [n-Dodecyl-beta-D-Maltoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/n-dodecyl-beta-d-maltoside/) — Primary detergent used for LmrP solubilization and purification
