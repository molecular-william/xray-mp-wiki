---
title: Methanosarcina acetivorans ModBC Molybdate/Tungstate ABC Transporter (MaModBC)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1156213]
verified: false
---

# Methanosarcina acetivorans ModBC Molybdate/Tungstate ABC Transporter (MaModBC)

## Overview

The crystal structure of Methanosarcina acetivorans ModBC (MaModBC),
a binding protein-dependent ABC transporter specific for molybdate and
[Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/), reveals the structural basis of trans-inhibition. The transporter
consists of two transmembrane domains (TMDs, ModB subunits) forming the
translocation pathway, and two cytoplasmic nucleotide-binding domains (NBDs,
ModC subunits) with C-terminal regulatory domains (~120 amino acids each).
In the trans-inhibited state, molybdate or [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) binds to oxyanion
binding pockets at the interface of the regulatory domains, locking the
transporter in an inward-facing conformation with the NBDs separated and
ATP hydrolysis inhibited. This represents a feedback mechanism where
intracellular substrate accumulation downregulates further uptake.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1156213 | not specified | 3.0 | not specified | Full-length MaModBC with bound [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) | [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) (WO4^2-) |
| doi/10.1126##science.1156213 | not specified | 3.5 | not specified | Full-length MaModBC with bound [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) | [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) (WO4^2-) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Full-length MaModBC (ModB + ModC with regulatory domains)

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Full-length MaModBC

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) and SEC | — |  | Purified in detergent solution; detailed purification protocol in supporting online material |

**Final sample**: Purified MaModBC in detergent solution with bound [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) for crystallization


## Crystallization

### doi/10.1126##science.1156213

| Parameter | Value |
|---|---|
| Method | Co-crystallization with [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) |
| Temperature | 20 |
| Notes | Crystals obtained by co-crystallization with [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/). Structure determined by three-wavelength MAD around tungsten edge. Diffraction data anisotropic, truncated to 3.0, 3.3, and 3.5 Å in three directions. Phases improved by solvent flattening and [NCS](/xray-mp-wiki/concepts/non-crystallographic-symmetry/) averaging. |


## Biological / Functional Insights

### Trans-Inhibition by Substrate Binding to Regulatory Domains

The regulatory domains appended to the C-terminus of the NBDs form two oxyanion binding pockets at their shared interface. Each pocket is contributed by residues from both regulatory domains. Key residues Ser286, Thr320, Ser323, and Lys340 serve as hydrogen bond donors. Binding of molybdate or [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) to these pockets allosterically inhibits ATPase activity (Ki ~5 µM), locking the transporter in an inward-facing conformation with the catalytic RecA-like and helical subdomains of the NBDs separated by ~23 Å (compared to ~10 Å in the uninhibited AfModBC). This trans-inhibition provides feedback regulation where intracellular molybdate accumulation downregulates further import.

### Comparison with Other ABC Transporter Conformations

The structure reveals a more pronounced inward-facing conformation compared to the nucleotide-free AfModBC, with increased angles between the two TMDs and a larger distance between coupling helices. Cross-linking experiments using engineered cysteines at position 153 in AfModB demonstrated that ATP binding induces closure of the NBDs, forcing the cytoplasmic ends of TM helices together and converting the translocation pathway to an outward-facing conformation similar to MalFGK2. This provides biochemical support for the [Alternating Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) in ABC transporters.


## Cross-References

- [Trans-Inhibition in ABC Transporters](/xray-mp-wiki/concepts/trans-inhibition-in-abc-transporters/) — MaModBC is the structural prototype for trans-inhibition in ABC transporters
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Related biological concept
- [NCS](/xray-mp-wiki/concepts/non-crystallographic-symmetry/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) — Related ligand or cofactor
