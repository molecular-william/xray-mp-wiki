---
title: "E. coli Signal Peptide Peptidase (SppA, Protease IV)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2007.11.080]
verified: false
---

# E. coli Signal Peptide Peptidase (SppA, Protease IV)

## Overview

SppA (signal peptide peptidase, also known as protease IV) from Escherichia coli
is the enzyme responsible for cleaving remnant signal peptides left behind in the
membrane following Sec-dependent protein secretion. SppA is a 618-residue protein
(67 kDa) anchored to the cytoplasmic membrane via an N-terminal transmembrane
segment (residues 29-45). The crystal structure of a soluble, catalytically active
construct (SppAΔ2-46) revealed a tetrameric assembly with a novel bowl-shaped
architecture. The bowl has a dramatically hydrophobic interior and contains four
separate active sites that utilize a Ser/Lys catalytic dyad mechanism (Ser409 and
Lys209). The N-terminal (residues 56-316) and C-terminal (residues 326-549) halves
are tandem repeats of an alpha/beta fold with only 18% sequence identity but
superimposing with 2.5 A RMSD. SppA shares a similar protein fold with the
cytoplasmic Ser/His/Asp protease , suggesting a possible role in quality
assurance of periplasmic and membrane-bound proteins.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2007.11.080 | 3BF0 | 2.6 A | P2_1 | SppAΔ2-46 (residues 56-549) with N-terminal 6xHis tag and thrombin cleavage site, expressed in E. coli BL21(DE3); native and SeMet-incorporated | None (apo structure) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: SppAΔ2-46 with N-terminal MGSS-HHHHHH-SSGLVPR-GSH tag (6xHis + thrombin cleavage site) followed by Met and SppA starting at Gly47; cloned into pET-28a via NdeI and XhoI sites

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and induction | Cells grown in LB + 25 ug/mL  at 37C, induced with 0.75 mM  at 27.5C for 3.5 h | -- | -- + -- | Overnight culture diluted 2:100 into LB media |
| Cell lysis | French press in 50 mM  Hcl]] pH 7.5, 100 mM NaCl, 5 mM  | -- | 50 mM  Hcl]] pH 7.5, 100 mM NaCl, 5 mM  + -- | Lysate centrifuged at 37,000g for 20 min |
| Nickel [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA column (5 mL column volume, Qiagen) | Ni-NTA agarose (Qiagen) | 50 mM  Hcl]] pH 7.5, 100 mM NaCl; wash with 50 mM ; elution with 100-500 mM  step gradient + -- | Protein eluted between 200-400 mM  |
| Size exclusion chromatography | Sephacryl S-100 HiPrep 26/60 SEC on AKTA Prime | Sephacryl S-100 HiPrep 26/60 (GE Healthcare) | 50 mM  Hcl]] pH 7.5, 100 mM NaCl, 1 mM  + -- | Run at 1 mL/min; fractions analyzed by SDS-PAGE; concentrated to 8 mg/mL |


## Crystallization

### doi/10.1016##j.jmb.2007.11.080

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | 8 mg/mL SppAΔ2-46 (native or SeMet-incorporated) |
| Reservoir | 100 mM  Hcl]] pH 7.5, 18%  3350, 200 mM K2HPO4 |
| Temperature | 18 C |
| Growth time | Not specified |
| Cryoprotection | 20%  (replacing water in reservoir solution); crystals incubated ~5 min before flash-cooling in liquid N2 |
| Notes | Crystals in space group P2_1 with 4 molecules per asymmetric unit. SeMet data collected at NSLS beamline X4A; native data at ALS beamline 8.2.1. Matthews coefficient 2.7 A3/Da (54.6% solvent). |


## Biological / Functional Insights

### Bowl-shaped tetrameric architecture with hydrophobic interior

SppA forms a unique tetramer with a bowl-shaped architecture. The bowl has
an opening of approximately 96 A in diameter at its base (predicted membrane
association surface) with a ridge restricting the opening to approximately 40 A.
The concave surface between the arched roof and the ridge creates substrate-binding
pockets for signal peptide hydrolysis. The interior of the bowl is dramatically
hydrophobic, contrasting with the more polar interior of . The four active
sites (Ser/Lys dyads) are located within this hydrophobic chamber and are
positioned near the membrane interface.

### Ser/Lys catalytic dyad mechanism

SppA utilizes a Ser/Lys catalytic dyad mechanism (Ser409 as nucleophile,
Lys209 as general base) rather than the classical Ser/His/Asp triad found in
most serine proteases. The catalytic residues are provided by different halves
of the tandem repeat: Ser409 from the C-terminal half and Lys209 from the
N-terminal half. They form the active site at the interface between the repeated
domains. The oxyanion hole is formed by the main-chain NH groups of Gly377 and
Gly410. In Gram-positive and archaeal organisms, which encode half-size SppA
variants, the catalytic residues would be provided by neighboring monomers in
an octameric assembly.

### Structural similarity to ClpP protease

Despite limited sequence identity, the N-terminal and C-terminal halves of
SppA monomers share a similar protein fold with the cytoplasmic  protease
monomers. The N-terminal half superimposes with  at 3.0 A RMSD (15.6%
identity, 147 residues), and the C-terminal half at 1.8 A RMSD (25% identity,
155 residues). When  is superimposed onto the C-terminal half of SppA,
the catalytic triad residues of  overlay with the Ser/Lys dyad atoms of
SppA. This structural homology suggests SppA may have a role in quality assurance
of periplasmic and membrane-bound proteins, analogous to 's role for
cytoplasmic proteins.

### Substrate binding and specificity

The S1 substrate-binding pocket is lined by hydrophobic residues (Val379,
Ile434), consistent with a preference for substrates with aliphatic residues
at the P1 position. The S3 pocket is relatively large and negatively charged,
suggesting it may interact with the positively charged N-region of signal
peptides. The two aliphatic side chains of Val379 and Ile434 form a ridge
dividing the S1 and S3 binding pockets, similar to the arrangement in E. coli
type I signal peptidase. The binding site model was constructed based on the
structure of  with a bound peptide-based inhibitor.


## Cross-References

- [Signal Peptide Processing](/xray-mp-wiki/concepts/signal-peptide-processing/) — SppA cleaves remnant signal peptides after Sec-dependent protein secretion
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA affinity chromatography used for initial purification
- [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Sephacryl S-100 SEC used for final purification step
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method used for SppAΔ2-46
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Tris-HCl pH 7.5 used in all purification buffers and crystallization reservoir
- [PEG 3350 (Polyethylene Glycol 3350)](/xray-mp-wiki/reagents/additives/peg-3350/) — 18% PEG 3350 used as precipitant in crystallization
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used for elution in Ni-NTA affinity chromatography
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — SeMet-incorporated SppA used for SAD phasing
- [Clpp](/xray-mp-wiki/proteins/enzymes/clpp/) — Referenced in escherichia-coli-sppa text
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in escherichia-coli-sppa text
