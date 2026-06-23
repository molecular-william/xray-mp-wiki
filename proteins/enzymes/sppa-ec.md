---
title: Signal Peptide Peptidase A from Escherichia coli
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2007.11.080]
verified: false
---

# Signal Peptide Peptidase A from Escherichia coli

## Overview

Signal peptide peptidase (SppA) from *Escherichia coli* is the first crystal structure of a bacterial signal peptide peptidase reported. SppA_EC forms a tetrameric assembly with a novel bowl-shaped architecture featuring a dramatically hydrophobic interior and four separate active sites that utilize a Ser/Lys catalytic dyad mechanism. The structure reveals that the previously predicted transmembrane segments are actually buried within the globular domain, and shows a surprising fold similarity to the cytoplasmic [ClpP](/xray-mp-wiki/proteins/enzymes/clpp/) protease despite a different catalytic mechanism.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2007.11.080 | 3BF0 | 2.6 A | P2_1 | SppA_EC delta 2-46 (residues 47-549, lacking predicted N-terminal TM segment), with 6xHis tag and thrombin cleavage site (MGSSHHHHHHSSGLVPRGSH) | -- |
| doi/10.1016##j.jmb.2007.11.080 | 3BF1 | 2.5 A | P2_1 | SppA_EC delta 2-46 (native), with 6xHis tag and thrombin cleavage site | -- |

## Expression and Purification

- **Expression system**: *E. coli* BL21 (DE3) cells transformed with plasmid pET28-sppA_delta2-46
- **Construct**: SppA_EC delta 2-46 (residues 47-549) with N-terminal 6xHis affinity tag and thrombin cleavage site (MGSSHHHHHHSSGLVPRGSH), cloned into pET-28a using NdeI and XhoI restriction sites. The expressed protein is 593 residues in length (including the 6xHis tag and thrombin site) with a molecular mass of 63,849 Da and a theoretical isoelectric point of 5.9.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and induction | Overnight small-scale cultures diluted 1:50 into LB media with [kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) (25 ug/mL), grown at 37 C for 3.5 h, then induced with 0.75 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at 27.5 C for 3.5 h. Cells pelleted by centrifugation at 37,000 x g for 20 min. | -- | LB media with [kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) (25 ug/mL) + -- | For [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-incorporated protein, BL21 (DE3) cells grown in M9 minimal media supplemented with amino acids including 60 mg Se-Met, with 15 min pre- induction before 0.75 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) addition. |
| Cell lysis | Cell pellet resuspended in buffer A and lysed by sonication (three 15-s pulses at 30% amplitude with 30-s rest) and homogenization (20,000-25,000 psi, 3 min, Avestin Emulsiflex-3C). Lysate centrifuged at 30,000 x g for 35 min; supernatant used for purification. | -- | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris)-HCl (pH 7.5), 100 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) + -- | -- |
| Ni-NTA affinity chromatography | Supernatant applied three times to Ni2+-NTA affinity column (5 mL column volume, Qiagen) pre-equilibrated with 5 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris)-HCl (pH 7.5), 100 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/). Column washed with 50 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in buffer (10 column volumes), then eluted with step gradient (100 to 500 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in 100 mM increments). Protein eluted between 200 and 400 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/). | [nickel-nta](/xray-mp-wiki/reagents/additives/nickel-nta/) (Qiagen, 5 mL column volume) | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris)-HCl (pH 7.5), 100 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 100-400 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) + -- | Fractions containing SppA_EC pooled for next step. |
| Concentration | Protein concentrated via Amicon ultracentrifuge filter (Millipore). | -- | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris)-HCl (pH 7.5), 100 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) + -- | Concentrated to 8 mg/mL. |
| Size-exclusion chromatography | Applied to Sephacryl S-100 HiPrep 26/60 SEC column on AKTA Prime system (Pharmacia Biotech) at 1 mL/min. Fractions containing pure SppA analyzed by SDS-PAGE and concentrated to 8 mg/mL. Analytical SEC with multiangle light scattering consistent with monodispersed tetramer in solution. | Sephacryl S-100 HiPrep 26/60 column (Pharmacia Biotech) | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris)-HCl (pH 7.5), 100 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 1 mM [ethylenediaminetetraacetic acid](/xray-mp-wiki/reagents/additives/) ([EDTA](/xray-mp-wiki/reagents/additives/edta)) + -- | Cleavage assays confirmed SppA_EC_delta2-46 is catalytically active. |


## Crystallization

### doi/10.1016##j.jmb.2007.11.080

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | SppA_EC delta 2-46 at 8 mg/mL in 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris)-HCl (pH 7.5), 100 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta). Drop prepared by mixing 1 uL protein with 1 uL reservoir solution. |
| Reservoir | 100 mM [Tris](/xray-mp-wiki/reagents/buffers/tris)-HCl (pH 7.5), 18% [polyethylene glycol 3350](/xray-mp-wiki/reagents/), 200 mM [sodium-phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) (K2HPO4) |
| Temperature | 18 C |
| Growth time | -- |
| Cryoprotection | Reservoir solution with 20% water replaced by [glycerol](/xray-mp-wiki/reagents/additives/glycerol/). Crystals incubated in cryosolvent for ~5 min before flash-cooling in liquid nitrogen. |
| Notes | Crystals in space group P2_1 with unit cell dimensions 93.0 x 153.0 x 100.2 A, beta = 104.2 deg (Se-Met) and 94.2 x 153.5 x 100.7 A, beta = 104.3 deg (native). Four molecules in the asymmetric unit, Matthews coefficient 2.7 A^3/Da (54.6% solvent). Se-Met crystals used for SAD phasing at NSLS beamline X4A. Native crystals collected at ALS beamline 8.2.1. Data processed with HKL2000. |


## Biological / Functional Insights

### Tetrameric bowl-shaped architecture with four active sites

SppA_EC forms a tetrameric assembly with a novel bowl-shaped architecture. The
tetramer has an opening at its base of approximately 96 A in diameter (predicted
membrane association surface). A ridge on the inside restricts the opening to
approximately 40 A in diameter. A concave surface between the arched roof and the
ridge creates the substrate-binding pockets for the four active sites. The
protein/protein interface between monomers buries approximately 1450 A^2 of
surface on each monomer (~60% nonpolar) and is predominantly alpha-helical with
one long antiparallel two-stranded beta-sheet.

### Ser/Lys catalytic dyad formed at domain interface

The catalytic dyad consists of nucleophile Ser409 from the C-terminal half and
general base Lys209 from the N-terminal half, which are within hydrogen-bonding
distance (2.8 A) only when the two halves of the tandem repeat come together.
The Ser409 O-gamma and Lys209 N-epsilon are 2.8 A apart (average for the four
molecules in the asymmetric unit). No other titratable functional groups are
within the vicinity of Ser409, confirming Lys209 as the general base. The
nucleophile and general base are actually quite far apart (29 A) within a single
protomer, requiring the tandem repeat fold to bring them into proximity.

### Previously predicted transmembrane segments are buried

The previously predicted second and third transmembrane segments (residues 398-414
and 421-441, respectively) are actually buried segments within the major globular
domain of SppA_EC. This finding explains why earlier attempts to create soluble
constructs by deleting these regions failed — they spanned crucial folding elements
of the enzyme. The construct used for crystallization (delta 2-46) removes only
the predicted N-terminal transmembrane segment (residues 29-45).

### Hydrophobic substrate-binding pockets

The substrate-binding pocket has a hydrophobic S1 pocket consistent with preference
for aliphatic residues at the P1 position. The S3 pocket is relatively large and
negatively charged, possibly interacting with the positively charged N-region of
signal peptides. Val379 and Ile434 aliphatic side chains form a ridge corresponding
to the dividing point between the S1 and S3 binding pockets, similar to the
analogous residues in *E. coli* type I signal peptidase.

### Unique oxyanion hole among serine proteases

The NH of Gly377 and Gly410 form the SppA_EC oxyanion hole by contributing hydrogen
bond donors to the developing oxyanion during the hydrolytic transition state. These
two [Glycine](/xray-mp-wiki/reagents/buffers/glycine) residues are completely conserved. The oxyanion holes in SppA and [CLPP](/xray-mp-wiki/proteins/clpp)
are unique among serine proteases in that they use a main-chain amide NH from the
residue following the nucleophile rather than the main-chain NH of the nucleophile
itself along with the penultimate residue to the nucleophile.

### Structural similarity to ClpP protease

Despite limited sequence identity, the N- and C-terminal regions of SppA_EC monomers
are similar in protein fold to monomers seen in the cytoplasmic Ser/His/Asp [CLPP](/xray-mp-wiki/proteins/clpp)
protease. The C-terminal half superimposes on a [CLPP](/xray-mp-wiki/proteins/clpp) monomer with an rmsd of 1.8 A
(25% identity for 155 aligned residues). Remarkably, when a [CLPP](/xray-mp-wiki/proteins/clpp) monomer is
superimposed onto the C-terminal half of SppA_EC, the chemically important atoms
within the Ser/His/Asp catalytic triad of [CLPP](/xray-mp-wiki/proteins/clpp) superimpose with the catalytic atoms
within the Ser/Lys catalytic dyad of SppA_EC. This suggests SppA may have a role in
protein quality control at the membrane surface, similar to [CLPP](/xray-mp-wiki/proteins/clpp) in the cytoplasm.

### Membrane orientation and substrate presentation model

SppA_EC contains a proposed N-terminal transmembrane segment (residues 29-45) that
likely tethers it to the cytoplasmic membrane. The structure is oriented such that
its axial hole points away from the inner membrane and the large opening of the bowl
associates with the membrane surface. Surface analysis reveals that the largest
depression on the SppA_EC molecular surface corresponds to the association interface
between individual monomers, which leads up to the substrate-binding sites. This
depression may help guide signal peptide substrate towards the active site.


## Cross-References

- [Signal Peptide Peptidase A from Bacillus subtilis (SppA_BS)](/xray-mp-wiki/proteins/enzymes/sppa-bs/) — Gram-positive homolog compared throughout the paper; half-size unduplicated SppA variant discussed in structural context; octameric assembly compared to tetrameric SppA_EC
- [ClpP Protease](/xray-mp-wiki/proteins/enzymes/clpp/) — Major structural comparison; ClpP shows surprising fold similarity to SppA despite different catalytic mechanisms (Ser/His/Asp vs Ser/Lys); both share unique oxyanion hole architecture using main-chain amide NH from residue following nucleophile
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine) — Entity mentioned in text
- [IPTG](/xray-mp-wiki/reagents/additives/iptg) — Entity mentioned in text
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine) — Entity mentioned in text
- [EDTA](/xray-mp-wiki/reagents/additives/edta) — Entity mentioned in text
