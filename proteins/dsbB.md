---
title: DsbB
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.febslet.2008.07.063]
verified: false
---

# DsbB

## Overview

DsbB is an inner membrane quinone reductase from Escherichia coli that reoxidizes the periplasmic dithiol oxidase DsbA, enabling disulfide bond formation in folding secretory proteins. DsbB consists of four transmembrane helices arranged in a four-helix bundle and two periplasmic loops, each containing a pair of essential cysteines. The catalytic cycle involves a charge-transfer interaction between the unpaired Cys44 thiolate of DsbB and the quinone ring of ubiquinone Q8, followed by nucleophilic attack of Cys44 on the quinone ring to generate the Cys41-Cys44 disulfide bond in DsbB and ubiquinol.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.febslet.2008.07.063 | Not available in raw paper (crystallographic details in supplementary data) | Not explicitly stated in raw paper | Not available | Wild-type E. coli DsbB in complex with DsbA(Cys33Ala) and ubiquinone Q8. The complex contains the intermolecular disulfide bond between Cys30 of DsbA and Cys104 of DsbB, the intramolecular disulfide bond Cys41-Cys130 in DsbB, and the unpaired Cys44 thiolate. | Ubiquinone Q8 bound in the active site, forming a charge-transfer interaction with Cys44 thiolate |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Wild-type E. coli DsbB (full-length, 4 transmembrane helices). Membrane-enriched fractions prepared from E. coli cells expressing DsbB.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane preparation | -- | -- + -- | Membrane fractions enriched for DsbB-Q8 prepared from E. coli cells |
| Complex formation | In vitro complex formation | -- | -- + -- | wtDsbB-Q8-enriched membrane suspension mixed with purified DsbA(Cys33Ala) to form the mixed disulfide complex |
| Solubilization | Detergent solubilization | -- | -- + Nonylmaltoside | Complex solubilized with nonylmaltoside detergent |
| Affinity purification | Affinity chromatography | Ni-NTA (metal chelate affinity) | -- + Nonylmaltoside | Metal chelate affinity enrichment using Ni2+-NTA chromatography |
| Size exclusion | Size exclusion chromatography | Preparative gel filtration | -- + Nonylmaltoside | Gel filtration yielded homogeneous complex, monitored by absorbance at 280 nm and 580 nm (pink color of charge-transfer complex) |


## Crystallization

### doi/10.1016##j.febslet.2008.07.063

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | wtDsbB-DsbA(Cys33Ala)-Q8 complex in nonylmaltoside |
| Reservoir | Not explicitly stated |
| Temperature | Not explicitly stated |
| Growth time | Not explicitly stated |
| Cryoprotection | None; crystals mounted in cryoloops and cryocooled by immersion into liquid nitrogen without additional cryoprotectant |
| Notes | Crystals grown and cryocooled without cryoprotectant. Crystallographic data collection, structure solution and refinement described in supplementary data. |


## Biological / Functional Insights

### Charge-transfer interaction between Cys44 thiolate and ubiquinone Q8

The crystal structure reveals a non-covalent charge-transfer interaction between the unpaired Cys44 thiolate of DsbB and the quinone ring of ubiquinone Q8. This interaction is responsible for the characteristic pink color of the complex (absorbance maximum at 500 nm). The invariant Arg48 side chain stabilizes the negative charge of the charge-transfer state. The location of Cys44 at the N-terminus of an alpha-helix suggests that the helix dipole may provide additional stabilization to the Cys44 thiolate.

### Mechanism of de novo disulfide bond formation by DsbB

The structure provides strong experimental support for the proposed mechanism of de novo disulfide bond formation by DsbB. The mechanism involves: (1) charge-transfer interaction between Cys44 thiolate and Q8 quinone ring, (2) nucleophilic attack of Cys44 on the C2 atom of the quinone ring, and (3) attack of Cys41 on Cys44, generating the Cys41-Cys44 disulfide bond and ubiquinol (reduced quinone). The second step requires the presence of reduced Cys41, which is formed when wtDsbB reacts with wild-type DsbA, producing semi-reduced DsbB with an inter-loop disulfide exchange creating the reduced Cys41/Cys44 pair.

### Unexpected stability of the mixed disulfide complex

The wtDsbB-DsbA(Cys33Ala)-Q8 complex with all essential cysteines in DsbB proved to be surprisingly stable under physiological conditions, despite being expected to be kinetically unstable. The stability is attributed to the strong charge-transfer interaction between the unpaired Cys44 thiolate of DsbB and ubiquinone Q8, which prevents the nucleophilic attack of Cys44 onto the inter-loop disulfide bond Cys41-Cys130 of DsbB. This stability enabled crystallization and structural characterization.

### Comparison with glutathione reductase mechanism

An analogous charge-transfer mechanism is found in glutathione reductase, where a cysteine thiolate forms a charge-transfer interaction with flavin adenine dinucleotide (FAD). The crystal structure of glutathione reductase charge-transfer intermediate revealed the flavin ring of FAD at a 0.2 A larger distance from the neighboring alpha-helix, similar to the shift observed in DsbB. This mechanistic resemblance extends to eukaryotic functional homologs of DsbB (Ero1p and Erv2p), which use FAD instead of quinones.

### Disorder in the second periplasmic loop

The second periplasmic DsbB loop (between TM3 and TM4) exhibits very weak electron density, in agreement with a high degree of disorder. DsbB residues 127-141 are absent from the model, precluding structural analysis of the region around the interloop disulfide bond Cys41-Cys130. This disorder is conserved between the wtDsbB and the DsbB(Cys130Ser) variant structures.


## Cross-References

- [DsbA](/xray-mp-wiki/proteins/dsbA/) — DsbA is the periplasmic dithiol oxidase that transfers its disulfide bond to folding polypeptides and is reoxidized by DsbB
- [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) — Quinone redox cofactor that accepts electrons from DsbB and forms a charge-transfer interaction with Cys44 thiolate
- [Menaquinone](/xray-mp-wiki/reagents/ligands/menaquinone/) — Anaerobic electron acceptor that can replace ubiquinone Q8 in DsbB, forming a purple complex
- [Nonylmaltoside](/xray-mp-wiki/reagents/detergents/nonylmaltoside/) — Nonionic detergent used for solubilization of the wtDsbB-DsbA-Q8 complex
- [Charge-Transfer Interaction](/xray-mp-wiki/concepts/charge-transfer-interaction/) — Key mechanistic concept describing the interaction between Cys44 thiolate and ubiquinone Q8
