---
title: "Phosphatidylinositol-Phosphate Synthase (RsPIPS) from Renibacterium salmoninarum"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##ncomms9505]
verified: false
---

# Phosphatidylinositol-Phosphate Synthase (RsPIPS) from Renibacterium salmoninarum

## Overview

Phosphatidylinositol-phosphate (PIP) synthase catalyses the first step of phosphatidylinositol biosynthesis in prokaryotes, using L-myo-inositol-1-phosphate as the acceptor alcohol and CDP-diacylglycerol (CDP-DAG) as the donor substrate. The crystal structures of PIP synthase from Renibacterium salmoninarum (RsPIPS) were determined in apo form (2.5 Å, construct RsPIPS-Δ6N with N-terminal deletion) and in complex with CDP-DAG (3.6 Å, full-length RsPIPS-FL), revealing a homodimeric six-transmembrane-helix architecture characteristic of class I CDP-alcohol phosphotransferases (CDP-APs). The structures identify the inositol phosphate acceptor pocket (defined by conserved arginines R155 and R195), the nucleotide-binding pocket containing the signature CDP-AP sequence, and a hydrophobic groove between TM2 and JM1 that accommodates the acyl chains of CDP-DAG. A chimeric fusion strategy using the Af2299 cytidylyltransferase-like domain as a crystallization chaperone was essential for obtaining diffracting crystals. Functional characterization of the 40%-identical ortholog from Mycobacterium tuberculosis (MtPIPS, a potential anti-tuberculosis drug target) supports the proposed mechanism and reveals a sequential ordered bi-bi reaction in which CDP-DAG binds first, followed by inositol phosphate, with D93 acting as the catalytic base.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms9505 | 5D91 | 2.50 | P 2₁ 2₁ 2 | RsPIPS-Δ6N: chimeric construct with N-terminal Af2299 cytidylyltransferase-like domain, first six residues of RsPIPS omitted, with six interface mutations (L75, F77, etc.) | Apo (SO₄²⁻ bound at the active site mimicking the phosphate of inositol phosphate) |
| doi/10.1038##ncomms9505 | 5D91 | 3.61 | P 2₁ | RsPIPS-FL: full-length RsPIPS (absent initiating methionine) with N-terminal Af2299 cytidylyltransferase-like domain and six interface mutations | CDP-diacylglycerol (CDP-DAG), Mg²⁺ |

## Expression and Purification

- **Expression system**: Escherichia coli (expression of synthetic gene; chimeric construct with N-terminal Af2299 cytidylyltransferase-like domain)
- **Construct**: Chimeric RsPIPS with N-terminal Af2299 extramembrane domain (residues 1-242) fused to RsPIPS sequence. Six interface mutations (L75F, F77Y, etc.) introduced to mimic the Af2299 soluble-TM domain interface. RsPIPS-Δ6N omits first 6 residues; RsPIPS-FL includes full sequence minus initiating Met.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Affinity purification | Ni²⁺ affinity chromatography | — |  | His-tagged chimeric protein purified by Ni-NTA |
| 2. Size-exclusion chromatography | Gel filtration | — |  | Final polishing step in detergent-containing buffer |

**Final sample**: Purified RsPIPS chimera in detergent solution for LCP crystallization


## Crystallization

### doi/10.1038##ncomms9505

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified RsPIPS chimera in detergent solution, reconstituted into monoolein lipidic cubic phase |
| Temperature | 20 °C |
| Notes | RsPIPS-Δ6N diffracted to 2.5 Å. RsPIPS-FL diffracted to 3.6 Å. Crystals grown in LCP using monoolein as host lipid. Heavy-atom derivatives for SeMet SAD phasing. Data collected at APS NE-CAT beamline 24ID-C. |


## Biological / Functional Insights

### Dimeric six-TM architecture of PIP synthase

RsPIPS adopts a homodimeric architecture with each protomer possessing six transmembrane helices surrounding a large polar cavity located at the cytosolic boundary of the membrane. This architecture is conserved among class I CDP-APs that utilize soluble acceptor substrates.

### Active site architecture with three subregions

The central polar cavity contains three distinct regions that form the active site: (1) the inositol phosphate acceptor-binding pocket defined by conserved arginines R155 and R195 that coordinate the phosphate group; (2) the nucleotide-binding pocket between TM2 and TM3 characterized by the conserved CDP-AP signature sequence D₁xxD₂G₁xxAR...G₂xxxD₃xxxD₄; and (3) a hydrophobic groove between TM2 and JM1 that accommodates the acyl chains of CDP-DAG.

### CDP-DAG binding and lipid substrate pathway

The structure of RsPIPS-FL with bound CDP-DAG reveals a hydrophobic crevice between JM1, TM2, and TM5 that is directly exposed to the bulk lipid, providing a pathway for lateral diffusion of CDP-DAG into the active site. The CDP moiety is wedged between TM2 and TM3, interacting with residues from the signature sequence. D31 and T34 (conserved P(D/N)xx(T/S) motif on TM1) form hydrogen bonds with the pyrimidine ring.

### Sequential ordered bi-bi reaction mechanism

Functional characterization of MtPIPS (40% identical to RsPIPS) demonstrates that inositol phosphate binding is strictly CDP-DAG dependent, supporting a sequential ordered bi-bi mechanism in which CDP-DAG binds first, followed by inositol phosphate. D93 (the fourth aspartate in the signature sequence 'D₄') acts as the catalytic base. Mutation D93N nearly completely abrogates activity without substantially affecting substrate binding.

### Inositol phosphate recognition by conserved arginine pair

Two conserved arginine residues, R155 and R195, coordinate the phosphate group of inositol phosphate. Mutation of either residue to alanine or glutamine severely impairs enzymatic activity. R195Q mutation increases K_M for inositol phosphate 10-fold (from 122 µM to 1,208 µM) while only mildly affecting CDP-DAG K_M, confirming these residues are specific inositol phosphate binding determinants.

### M. tuberculosis PIP synthase as anti-tuberculosis drug target

Genetic ablation of PIP synthase in Mycobacterium smegmatis is lethal. The unique prokaryotic PI biosynthesis pathway and the absence of inositol phosphate recognition by eukaryotic CDP-APs position MtPIPS as a plausible target for novel anti-tuberculosis drugs. The inositol phosphate binding pocket, with its relatively low affinity (K_M = 122 µM), provides a potentially druggable site that could be targeted by competitive inhibitors.


## Cross-References
