---
title: LspA from Staphylococcus aureus (Lipoprotein Signal Peptidase II)
created: 2026-06-08
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-13724-y, doi/10.1126##science.aad3747]
verified: false
---

# LspA from Staphylococcus aureus (Lipoprotein Signal Peptidase II)

## Overview

LspA (lipoprotein signal peptidase II) is an integral membrane aspartyl protease responsible for processing bacterial lipoproteins by cleaving the signal peptide after diacylglyceryl modification. The enzyme is essential in Gram-negative bacteria and required for full virulence in Gram-positive bacteria, making it an attractive drug target. The first crystal structure of LspA from Pseudomonas aeruginosa (strain PAO1) was solved at 2.8 A resolution in complex with the natural antibiotic [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) using in meso crystallization and Se-Met SAD phasing, identifying LspA as an aspartyl peptidase with catalytic dyad Asp124 and Asp143 (Science 2016). Subsequently, crystal structures of LspA from methicillin-resistant Staphylococcus aureus (MRSA) in complex with [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) and myxovirescin revealed both antibiotics inhibit the enzyme as non-cleavable tetrahedral intermediate analogs, sharing a common 19-atom spine motif (Nature Communications 2019).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-019-13724-y | 6RYO | 1.92 A | P3_2 21 | LspA from S. aureus MRSA (LspMrs) in complex with [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/), residues approximately 1-163, crystallized using lipidic cubic phase (LCP) | [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) |
| doi/10.1038##s41467-019-13724-y | 6RYP | 2.30 A | P6_1 22 | LspA from S. aureus MRSA (LspMrs) in complex with myxovirescin A1, residues approximately 1-162, crystallized using lipidic cubic phase (LCP) | myxovirescin A1 |
| doi/10.1126##science.aad3747 |  | 2.8 A |  | LspA from P. aeruginosa PAO1 in complex with [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/), 169 amino acids | [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length LspMrs with N-terminal MGSS-hexahistidine tag, TEV protease cleavage site, expressed in E. coli

### Purification Workflow

*Source: doi/10.1038##s41467-019-13724-y*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Cell disruption and ultracentrifugation |  | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM TCEP | Cells resuspended and lysed; membranes collected by ultracentrifugation |
| Membrane solubilization | Detergent solubilization |  | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM TCEP + n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membranes solubilized with [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (IMAC) | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM TCEP, [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Histidine-tagged LspMrs purified on Ni-NTA column |
| TEV protease cleavage | Tag removal by TEV protease |  | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM TCEP + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | N-terminal His-tag cleaved by TEV protease; cleaved protein used for crystallization |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) (SEC) | Size exclusion column | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM TCEP + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final purification step; protein concentrated to 14-16 mg/mL for crystallization |

**Final sample**: 14-16 mg/ml in 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM TCEP
**Purity**: High purity by SDS-PAGE

### Purification Workflow

*Source: doi/10.1126##science.aad3747*

- **Expression system**: Escherichia coli (P. aeruginosa PAO1 LspA)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — |  | Provided material of high purity (fig. S2) |
| Size-exclusion chromatography | SEC | — |  | Provided material of high purity (fig. S2) |

**Final sample**: Purified LspA-[Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) complex for in meso crystallization
**Purity**: High purity by SDS-PAGE (fig. S2)


## Crystallization

### doi/10.1038##s41467-019-13724-y

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | LspMrs in buffer D (50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM TCEP) at 14-16 mg/mL, with 5-fold molar excess of [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) or myxovirescin in DMSO |
| Temperature | 20 C |
| Growth time | [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) complex: 15-20 days; Myxovirescin complex: 21 days |
| Notes | Crystallization was performed using the in meso method. Protein solution mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) in a 2:3 ratio (v/v) to form the lipidic cubic phase. Boluses of protein-laden mesophase (50 nL) were covered with 800 nL precipitant solution. LspMrs-[Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) crystals: bipyramid-shaped, 50x50x50 um, appeared after 4 days. LspMrs-myxovirescin crystals: thin hexagon-shaped, 80 um longest dimension, appeared after 2-3 days. Data collected at SLS beamline X06SA-PXI. |

### doi/10.1126##science.aad3747

| Parameter | Value |
|---|---|
| Method | In meso (lipid cubic phase) crystallization |
| Protein sample | LspA from P. aeruginosa PAO1 in complex with [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) |
| Temperature | Not specified |
| Notes | LspA from P. aeruginosa was crystallized using the in meso (lipid cubic phase) method in the presence of [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/). The structure of the complex was obtained at 2.8 A resolution by using seleno-methionine, single-wavelength anomalous diffraction (SAD) phasing. |


## Biological / Functional Insights

### Convergent evolution of two natural antibiotics targeting LspA

[Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) (a cyclic depsipeptide) and myxovirescin (a macrolactam) have completely different molecular structures and biosynthetic origins. Yet both inhibit LspA by the same mechanism: they position a hydroxyl group between the catalytic aspartate dyad (Asp118 and Asp136) as non-cleavable tetrahedral intermediate analogs. The two antibiotics superpose along 19 contiguous atoms (the "spine") that interact similarly with LspA, demonstrating a remarkable instance of convergent evolution towards the same molecular target.

### Structural basis for antibiotic binding

[Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) approaches the substrate-binding pocket from one side while myxovirescin approaches from the other, yet both block the catalytic dyad. The 19-atom spine motif recapitulates a part of the natural lipoprotein substrate in its proposed binding mode. All 14 highly conserved residues in LspA are similarly poised in both complex structures. The extracellular loop (EL) between the beta-cradle and H2 exhibits flexibility that is key to effective binding of both antibiotics, enabled by Gly54 as a flexible hinge.

### LspA as a therapeutic target

LspA is essential in Gram-negative bacteria and required for full virulence in Gram-positive bacteria, including MRSA. The lspA mutant showed reduced ability to survive in whole human blood, confirming LspA is important for MRSA survival under physiologically relevant conditions. Both antibiotics interact with highly conserved residues, making resistance development difficult - mutations that weaken antibiotic binding would also compromise LspA function, providing no competitive advantage.

### Mechanism of globomycin and myxovirescin inhibition

Both antibiotics act as non-cleavable tetrahedral intermediate analogs of the aspartyl protease reaction. The beta-hydroxyl of [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/)'s Ser residue and the 6-OH of myxovirescin lodge between the catalytic aspartates (Asp118, Asp136). The blocking hydroxyl oxygens superpose to within 0.8 A in the two complex structures. The 19-atom spine of overlapping atoms provides a natural pharmacophore framework for drug design.

### Substrate specificity and EL flexibility

The extracellular loop (EL, residues Asn53-Lys63) shows remarkable flexibility between the two complex structures. In the [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) complex, the loop includes a half-turn helix with Trp57 reaching over the antibiotic. In the myxovirescin complex, the loop unfolds fully, allowing Trp57 to contact the macrocycle from the opposite side. This EL flexibility likely reflects substrate promiscuity, as LspA must process many different lipoprotein substrates (67 in S. aureus, 175 in P. aeruginosa).

### LspA is an aspartyl peptidase with catalytic dyad Asp124 and Asp143

Mutagenesis studies confirmed LspA is an aspartyl peptidase. The catalytic dyad consists of Asp124 and Asp143, both strictly conserved in 485 organisms. Asp124Asn and Asp143Asn mutants were devoid of activity, while Asp115Ala retained partial activity, confirming Asp115 is functionally important but not catalytic.

### Globomycin inhibits via non-cleavable transition-state mimicry

[Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) acts as a competitive inhibitor of LspA by molecular mimicry. The beta-hydroxyl of g-Ser nests between the two catalytic aspartates (Asp124, Asp143), acting as a non-cleavable tetrahedral intermediate analog. [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) also mimics the P-3, P-2, P-1 residues of the lipobox consensus sequence (LAGC). The hydroxyethylamide of g-Ser incorporates elements of a noncleavable transition-state isostere, similar to inhibitors designed for other aspartyl proteases (renin, HIV protease).

### Substrate recognition via shape complementarity

LspA processes 175 different lipoproteins in P. aeruginosa. The structure has grooves and clefts radiating about the active site with remarkable shape complementarity to the trigonal feature of the prolipoprotein substrate (signal peptide, lipoprotein, and [DAG](/xray-mp-wiki/reagents/lipids/dag/) modification converging at the lipobox cysteine). The scissile Gly-Cys* bond is positioned between the catalytic aspartates. This shape complementarity explains how LspA can accommodate diverse lipoprotein substrates while maintaining specificity for the lipobox.


## Cross-References

- [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) — Natural cyclic depsipeptide antibiotic that inhibits LspA
- [Myxovirescin A1](/xray-mp-wiki/reagents/ligands/myxovirescin/) — Natural macrolactam antibiotic that inhibits LspA
- [n-Dodecyl-beta-D-Maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization and purification of LspMrs
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lcp/) — Crystallization method used to obtain LspMrs-antibiotic complex structures
- [Intramembrane Proteolysis](/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-proteolysis/) — LspA catalyzes signal peptide cleavage at the membrane interface
- [SeMet SAD Phasing](/xray-mp-wiki/methods/structure-determination/semet-sad-phasing/) — Phasing method used for the 2.8 A P. aeruginosa LspA structure
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
