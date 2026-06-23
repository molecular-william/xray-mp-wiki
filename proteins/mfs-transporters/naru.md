---
title: NarU Nitrate/Nitrite Transporter from Escherichia coli
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2013.03.007]
verified: false
---

# NarU Nitrate/Nitrite Transporter from Escherichia coli

## Overview

NarU is a nitrate/nitrite transporter from Escherichia coli belonging to the
nitrate/nitrite porter (NNP) family of the major facilitator superfamily (MFS).
NarU shares 76% sequence identity with NarK and transports both nitrate (NO3-)
and nitrite (NO2-), playing a key role during severe nutrient starvation in
bacteria. The crystal structure of NarU was determined at 3.1 A resolution by
selenomethionine single-wavelength anomalous dispersion (SeMet SAD) phasing.
The asymmetric unit contains two NarU molecules in distinct conformational
states: occluded (Mol A) and partially inward-open (Mol B and Mol B'),
providing insights into the transport mechanism. The substrate-binding site
is defined by four highly conserved residues (Arg87, Arg303, Asn173, Tyr261)
that coordinate nitrate through hydrogen bonds. The transport path features a
thin cytoplasmic gate (Phe145 and Phe367) and a thick periplasmic gate composed
of hydrophobic and polar layers. Unlike the canonical rocker-switch model for
MFS transporters, NarU appears to employ a mechanism involving bending of
transmembrane helices TM10 and TM11 around conserved glycine residues, rather
than rigid-body domain rotation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.celrep.2013.03.007 | (not deposited in PDB per paper) | 3.1 | P212121 | Native full-length NarU from E. coli K-12, selenomethionine-substituted for phasing |  |

## Expression and Purification

- **Expression system**: Escherichia coli (heterologous overexpression)
- **Construct**: Full-length NarU (E. coli K-12)
- **Notes**: Overexpressed in E. coli. Selenomethionine-substituted NarU produced in minimal medium for SAD phasing.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression and membrane preparation | Standard membrane protein preparation | — |  | Overexpressed NarU in E. coli, membrane purification. |
| Purification | Standard purification (details in paper) | — |  | Purified to homogeneity for crystallization. |


## Crystallization

### doi/10.1016##j.celrep.2013.03.007

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop or hanging drop) |
| Protein sample | Purified NarU (native or SeMet-substituted) |
| Reservoir | -- (not specified in detail) |
| Temperature | -- (not specified) |
| Growth time | -- (not specified) |
| Cryoprotection | -- (not specified) |
| Notes | Crystallized in space group P212121 with two molecules per asymmetric unit. SeMet-NarU crystallized in presence of 5 mM nitrate for phasing. Native NarU crystallized in absence of substrate. |


## Biological / Functional Insights

### Substrate-binding site defined by four conserved residues

Nitrate is coordinated by four highly conserved amino acids: Arg87 (TM2),
Arg303 (TM8), Asn173 (TM5), and Tyr261 (TM7). Arg87 and Arg303 are essential
for transport activity. Mutagenesis of any of these four residues to Ala
reduces transport by 40-60%. The bound nitrate forms six hydrogen bonds with
these surrounding residues, positioning the substrate at the center of the
transporter.

### Two distinct conformational states reveal transport mechanism

Two NarU molecules in the asymmetric unit exhibit different conformations.
Mol A adopts an occluded conformation with the substrate-binding site isolated
from both sides. Mol B and Mol B' are partially open to the cytoplasmic side.
The main structural difference is the bending of TM10 and TM11: the C-terminal
half of TM10 and N-terminal half of TM11 rotate approximately 16 degrees and
23 degrees, respectively, around Gly364 and Gly405.

### Thin gate and thick gate architecture

The transport path is gated by two distinct barriers. A thin gate on the
cytoplasmic side consists of only two residues: Phe145 and Phe367, which must
separate for substrate release. A thick gate on the periplasmic side comprises
two hydrophobic layers (Phe47/Trp50/Phe265 and Met51/Phe268/Ile269) and a
polar layer (Ser54/Gln180/Ser272). The hydrophobic layers maintain the
outward-closed conformation through extensive van der Waals contacts.

### Proposed deviation from the rocker-switch model

Unlike the canonical rocker-switch mechanism of MFS transporters (involving
rigid-body rotation of N-terminal and C-terminal domains), NarU appears to
undergo conformational changes primarily through bending of transmembrane
helices, particularly TM10 and TM11, facilitated by conserved glycine-rich
nitrate signature motifs in TM5 and TM11, and additional glycine residues in
TM4, TM7, TM8, and TM10. This model may be favored by the small size of
nitrate (ionic radius ~1.96 A).

### Functional characterization by stopped-flow and ITC

NarU transports nitrate and nitrite at similar rates, with binding affinities
of ~33 uM for nitrate and ~373 uM for nitrite. Transport specificity was
demonstrated by much reduced rates for phosphate and ammonium. A liposome-based
stopped-flow assay showed that NarU-mediated nitrate transport reduces osmotic
pressure, favoring a symporter mechanism rather than a nitrate-nitrite
antiporter. No detectable pH change was observed, suggesting NarU is not
proton-coupled.


## Cross-References

- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — SeMet SAD method used for experimental phasing of NarU structure
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — MR used to determine native NarU structure
- [Isothermal Titration Calorimetry](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) — ITC used to measure nitrate and nitrite binding affinities to NarU
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Primary method used for structure determination
