---
title: "McjD - Antibacterial Peptide ABC Exporter from Escherichia coli"
created: 2026-06-08
updated: 2026-06-17
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1320506111, doi/10.15252##embj.201797278, doi/10.1107##S2052252520012312]
verified: false
---

# McjD - Antibacterial Peptide ABC Exporter from Escherichia coli

## Overview

McjD is an ATP-binding cassette (ABC) exporter from Escherichia coli that
confers self-immunity to the producing strain by exporting the antimicrobial
lasso peptide microcin J25 (MccJ25). It is, to the authors' knowledge, the
first crystal structure of an antibacterial peptide ABC transporter. McjD
adopts a homodimeric architecture similar to multidrug ABC exporters such as
[Sav1866](/xray-mp-wiki/proteins/abc-transporters/sav1866/) and
[MsbA](/xray-mp-wiki/proteins/abc-transporters/msba/), but crystallizes in a novel
nucleotide-bound outward-occluded conformation that represents an intermediate
state between the outward-open and inward-open states of ABC exporters.
Each monomer comprises an N-terminal transmembrane domain (TMD) with six
transmembrane helices and a C-terminal nucleotide-binding domain (NBD).
The structure was determined at 2.7-A resolution in complex with the ATP
analog AMP-PNP and Mg2+. Subsequent work captured the McjD-ADP-VO4
(nucleotide-bound, 2.7 A) and McjD-apo (nucleotide-free, 2.5 A) states,
revealing NBD disengagement in the absence of nucleotides. EPR spectroscopy
and MD simulations showed the NBDs separate by up to 16 A in the apo state,
while substrate binding (MccJ25) enhances conformational sampling of the
inward-open conformation. Vanadium SAD (V-SAD) phasing using the anomalous
signal from the vanadate ion in McjD-ADP-VO4 crystals successfully provided
experimental phases at 3.4 A resolution, enabling structure solution despite
severe anisotropy.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1320506111 | 4PL0 | 2.7 | — | Full-length McjD with C-terminal GFP-His6 tag (cleaved) | AMP-PNP |
| doi/10.15252##embj.201797278 | 5OFR | 2.7 | — | Full-length McjD | ADP-VO4 |
| doi/10.15252##embj.201797278 | 5OFR | 2.5 | — | Full-length McjD | none (apo) |
| doi/10.1107##S2052252520012312 | 6YSO | 3.4 (V-SAD), 2.7 (phase extension) | — | Full-length McjD with ADP-VO4 | ADP-VO4 |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: McjD with C-terminal GFP-His6 tag and TEV protease cleavage site
- **Notes**: Drug-hypersensitive E. coli strain lacking AcrAB-TolC used for functional studies; non-GFP-tagged for cellular assays

### Purification Workflow

#### Source: doi/10.1073##pnas.1320506111

- **Expression system**: E. coli
- **Expression construct**: McjD-GFP-His6

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity chromatography | Ni Sepharose affinity chromatography | — | 0.03% n-Dodecyl-beta-D-maltopyranoside (DDM) | GFP-tag removed by TEV protease before crystallization |
| Exchange into crystallization detergent | Detergent exchange | — |  | Exchanged into nonyl-glucopyranoside for crystallization |

**Final sample**: McjD in nonyl-glucopyranoside with 10 mM AMP-PNP and 2.5 mM MgCl2

#### Source: doi/10.1107##S2052252520012312

- **Expression system**: E. coli
- **Expression construct**: McjD

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | As described previously (Bountra et al., 2017; Choudhury et al., 2014) | — | 20 mM Tris pH 7.8, 150 mM NaCl, 0.03% dodecyl maltopyranoside |  |

**Final sample**: McjD at 15 mg/ml in 20 mM Tris pH 7.8, 150 mM NaCl, 0.03% DDM


## Crystallization

### doi/10.1073##pnas.1320506111

| Parameter | Value |
|---|---|
| Method | Not specified in main text |
| Protein sample | McjD in nonyl-glucopyranoside with 10 mM AMP-PNP, 2.5 mM MgCl2 |
| Notes | Crystals grown in presence of nonyl-glucopyranoside; structure solved by molecular replacement using MsbA and Sav1866 as search models |

### doi/10.15252##embj.201797278

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | McjD with ADP-VO4 |
| Notes | McjD-ADP-VO4 and McjD-apo crystals grown by vapor diffusion; data collected at Diamond Light Source beamlines |

### doi/10.1107##S2052252520012312

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | 15 mg/ml McjD incubated with 2 mM ATP, 2 mM sodium orthovanadate, 5 mM MgCl2 for 1 h at room temperature |
| Reservoir | 10% PEG 4000, 100 mM ammonium sulfate, 100 mM HEPES pH 7.5, 22% glycerol |
| Temperature | 293 K |
| Growth time | 4 days |
| Cryoprotection | Directly flash-cooled in liquid nitrogen |
| Notes | McjD-ADP-VO4 complex crystals; space group C2; data collected on beamline I23 at Diamond Light Source using PILATUS 12M detector |


## Biological / Functional Insights

### Novel outward-occluded conformation

McjD represents a new conformation for ABC exporters, termed nucleotide-bound
outward occluded. Unlike the outward-open Sav1866 and MsbA structures, both
the cytoplasmic and periplasmic sides of the McjD dimer are occluded. The
occluded state is formed by rotation of TMs 1 and 2 toward the equivalent
TMs of the opposite monomer, without the intertwining of TM helices seen in
Sav1866. Salt bridges (Lys80-Glu301, Arg141-Glu309, Arg195-Asp135) stabilize
the occluded packing.

### Substrate-binding cavity

McjD defines a clear internal cavity of approximately 1,784 A3 that can
accommodate one MccJ25 molecule. Mutagenesis identified Phe86, Asn134, and
Asn302 as important for MccJ25 recognition. The cavity is wider and more
charged at the cytoplasmic side and more narrow and hydrophobic at the
periplasmic face, consistent with binding the lariat ring and loop regions
of MccJ25 respectively.

### MccJ25 binding and ATPase stimulation

McjD binds MccJ25 with a KD of 104 +- 52 uM as measured by microscale
thermophoresis. The ATPase activity of McjD (Km 169.3 uM, Vmax 44.4 nmol
min-1 mg-1) is stimulated by MccJ25 in both detergent solution and
proteoliposomes. McjD also transports the multidrug substrate Hoechst 33342,
underscoring structural similarities with multidrug ABC exporters.

### Nucleotide-dependent NBD dynamics

Comparison of McjD-ADP-VO4 (nucleotide-bound) and McjD-apo (nucleotide-free)
structures reveals that the NBDs disengage in the absence of nucleotides.
In the ADP-VO4-bound state, the NBDs form a firmly closed dimer, while in
the apo state they separate by up to 16 A (measured at residue C547).
EPR spectroscopy and MD simulations confirm these large-scale NBD motions.
The TMDs show only minor rearrangements between the two states, indicating
that nucleotide binding primarily affects NBD dimerization.

### Substrate-induced conformational sampling

Cysteine cross-linking and PEGylation studies demonstrate that the presence
of substrate MccJ25 enhances conformational sampling of the inward-open
conformation. The L53C construct shows increased cross-linking efficiency
in the presence of MccJ25, suggesting substrate binding promotes transition
to the inward-open state. The A122C and S509C constructs show similar
substrate-enhanced accessibility, consistent with an induced-fit mechanism
where MccJ25 binding stabilizes the inward-facing conformation.

### McjD structure solved by vanadium SAD phasing

McjD-ADP-VO4 was used as a test case for vanadium-based experimental phasing
(V-SAD). Data collected at lambda = 2.2604 A on beamline I23 at Diamond Light
Source exploited the vanadium K-edge anomalous signal (f'' ~4 e-). Despite
severe anisotropy and low resolution (3.4 A), the two vanadium sites (one per
monomer) were located by SHELXD with strong anomalous peaks (19.5 and 13.7
sigma). After anisotropy correction with STARANISO, initial electron-density
maps from the CRANK2 pipeline clearly showed transmembrane and nucleotide-binding
domains. Phase extension using a higher-resolution (2.7 A) dataset at
lambda = 0.9791 A enabled complete model building. This demonstrated that V-SAD
can succeed at low resolution and with a low scatterer-to-residue ratio (1:580).


## Cross-References

- [Sav1866 Multidrug ABC Exporter](/xray-mp-wiki/proteins/abc-transporters/sav1866/) — Structural comparison; McjD shares similar overall architecture but adopts distinct occluded conformation
- [MsbA Lipid Flippase](/xray-mp-wiki/proteins/abc-transporters/msba/) — Structural comparison; used as search model for molecular replacement
- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — McjD is a member of the ABC exporter family
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — McjD's outward-occluded state represents an intermediate in the alternating access cycle
- [ABC Transporter Outward-Occluded Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-outward-occluded-mechanism/) — McjD defines the outward-occluded conformation in ABC exporters
- [Vanadate Inhibition](/xray-mp-wiki/concepts/enzyme-mechanisms/vanadate-inhibition/) — Vanadate binding used for V-SAD phasing of McjD structure
