---
title: "Escherichia coli DtpB Peptide Transporter"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2023.112831]
verified: false
---

# Escherichia coli DtpB Peptide Transporter

## Overview

DtpB is a proton-dependent oligopeptide transporter (POT) from the Major Facilitator Superfamily (MFS) in Escherichia coli. It mediates the uptake of di- and tripeptides across the inner membrane using the proton motive force. DtpB adopts the canonical MFS fold with N- and C-terminal six-transmembrane helix bundles related by pseudo-two-fold symmetry, connected by HA-HB linker helices. 14 X-ray crystal structures of DtpB in complex with chemically diverse di- and tripeptides and the [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) 132 (Nb132) crystallization chaperone revealed the plasticity of the conserved central binding cavity. Together with structures of [Dtpa](/xray-mp-wiki/proteins/slc-transporters/dtpa/), DtpC, and DtpD, this completes the entire family of experimental POT structures from E. coli. The binding affinities for over 80 peptides were measured via thermal shift assays, showing that high-affinity peptides are poorly transported and act as inhibitors, while medium-affinity peptides display the highest transport rates.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.celrep.2023.112831 | 8B1C | 2.45 | Not specified | E. coli DtpB with Nb132 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | Ala-Leu-Ala (tripeptide) |
| doi/10.1016##j.celrep.2023.112831 | 8B1D | 2.80 | Not specified | E. coli DtpB with Nb132 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | Ala-Phe (dipeptide) |
| doi/10.1016##j.celrep.2023.112831 | 8B1E | 2.56 | Not specified | E. coli DtpB with Nb132 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | Ala-Leu (dipeptide) |
| doi/10.1016##j.celrep.2023.112831 | 8B1F | 2.47 | Not specified | E. coli DtpB with Nb132 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | Ala-Gln (dipeptide) |
| doi/10.1016##j.celrep.2023.112831 | 8B1G | 2.35 | Not specified | E. coli DtpB with Nb132 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | Ala-Glu (dipeptide) |
| doi/10.1016##j.celrep.2023.112831 | 8B17 | 2.50 | Not specified | E. coli DtpB with Nb132 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | Phe-Ala (dipeptide) |
| doi/10.1016##j.celrep.2023.112831 | 8B1H | 2.80 | Not specified | E. coli DtpB with Nb132 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | Lys-Ser, Ser-Lys, Asn-Val (multiple dipeptides) |
| doi/10.1016##j.celrep.2023.112831 | 8B1I | 2.47 | Not specified | E. coli DtpB with Nb132 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | Met-Ala (dipeptide) |
| doi/10.1016##j.celrep.2023.112831 | 8B1J | 2.47 | Not specified | E. coli DtpB with Nb132 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | Leu-Leu (dipeptide) |
| doi/10.1016##j.celrep.2023.112831 | 8B1K | 2.50 | Not specified | E. coli DtpB with Nb132 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | Phe-Ala-Gln (tripeptide) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: E. coli DtpB (full-length) with Nb132 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) as crystallization chaperone

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent extraction | — | Standard purification buffer + Not specified | DtpB purified in detergent for crystallization with [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) 132 |
| Affinity chromatography | Affinity chromatography | Not specified | Not specified | Purified prior to [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) complex formation |
| Size-exclusion chromatography | Size-exclusion chromatography | Not specified | Not specified | DtpB-Nb132 complex purified by SEC |


## Crystallization

### doi/10.1016##j.celrep.2023.112831

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | DtpB-Nb132 complex incubated with di-/tripeptide |
| Reservoir | Not specified |
| Temperature | 20 |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | 14 structures in total with various di- and tripeptide substrates; DtpB crystallized in inward-facing (IF) open state; molecular replacement using [Dtpa](/xray-mp-wiki/proteins/slc-transporters/dtpa/) (PDB 6GS4) as search model |


## Biological / Functional Insights

### Binding pocket plasticity enables promiscuous substrate recognition

14 X-ray structures of DtpB complexed with chemically diverse di- and tripeptides revealed the molecular basis of the broad substrate specificity. Peptides bind in the central cavity with their N-terminus coordinated by the conserved N153, N318, E393 triad and C-terminus by R33, R149, Y154 residues. The P1 pocket, comprising Y31, Q34, S156, L160, M288, and P319 together with the conserved triad, accommodates the N-terminal residue side chain. Structural comparisons show that the binding site adapts to different peptide side chains through local rearrangements, particularly in the P1 pocket region, explaining how DtpB can recognize a vast diversity of substrates.

### High-affinity peptides act as transport inhibitors

Binding affinity measurements for over 80 di- and tripeptides combined with a fluorescence-based transport assay revealed an inverse correlation between binding affinity and transport rate. High-affinity peptides (Kd < 100 uM) are poorly transported and act as competitive inhibitors, while medium-affinity peptides (Kd 100 uM - 2.5 mM) display the highest transport rates. This suggests that tight-binding substrates remain trapped in the binding pocket and are not efficiently released during the transport cycle, while moderate-binding substrates dissociate more readily for productive transport.

### Machine learning predicts transportable substrates

Molecular docking of all 8,400 possible di- and tripeptides composed of proteinogenic amino acids into DtpB, combined with machine learning (logistic regression classifier), predicted that peptides with compact hydrophobic residues are the best DtpB binders. The study concluded that a specific subset of peptides with compact hydrophobic residues are the best DtpB binders and potential transport substrates, providing a framework for predicting transport selectivity in POT family transporters.


## Cross-References

- [RND Efflux Pumps](/xray-mp-wiki/concepts/transport-mechanisms/rnd-efflux-pumps/) — POT transporters are MFS family members; DtpB complements the E. coli POT structural coverage alongside DtpA, DtpC, and DtpD
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Used for purification of DtpB prior to crystallization
- [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) — Crystallization method used for DtpB-peptide complexes
- [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) — Referenced in context related to Nanobody
- [Dtpa](/xray-mp-wiki/proteins/slc-transporters/dtpa/) — Referenced in context related to Dtpa
