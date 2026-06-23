---
title: Yeast Mitochondrial ABC Transporter Atm1
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, pump, membrane-protein]
sources: [doi/10.1126##science.1246729]
verified: false
---

# Yeast Mitochondrial ABC Transporter Atm1

## Overview

Yeast Atm1 (ABC transporter of mitochondria 1) is a mitochondrial inner membrane ABC exporter from *Saccharomyces cerevisiae* that functions in the export of a sulfur-containing molecule required for cytosolic-nuclear iron-sulfur (Fe/S) protein biogenesis and cellular [IRON](/xray-mp-wiki/reagents/additives/iron/) regulation. Crystal structures were determined in nucleotide-free and glutathione-bound forms at 3.06 and 3.38 Å resolution, respectively, both in inward-facing, open conformations. The structures reveal that Atm1 forms a domain-swapped dimer with 12 transmembrane helices enclosing a 6900 Å³ positively charged cavity. A defining feature is the complete resolution of two C-terminal α-helices that interact in a crossover fashion to stabilize the dimer in the inward-facing open conformation, a structural element not observed previously in any other ABC transporter crystal structure. Mutations in the human ortholog ABCB7 cause X-linked sideroblastic anemia with cerebellar ataxia (XLSA/A).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1246729 | 4MYC | 3.06 | — | S. cerevisiae Atm1Δ98 (residues 99-678), C-terminal Strep-tag | None (nucleotide-free) |
| doi/10.1126##science.1246729 | 4MYH | 3.38 | — | S. cerevisiae Atm1Δ98 (residues 99-678), C-terminal Strep-tag | [GSH](/xray-mp-wiki/reagents/additives/glutathione/) ([GSH](/xray-mp-wiki/reagents/additives/glutathione/)) |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae
- **Construct**: Atm1Δ98 lacking the first 98 residues (mitochondrial presequence), with C-terminal Strep-tag; residues 99-678
- **Notes**: Expressed in S. cerevisiae; the processed mature form (residues 99-678) was used for crystallization

### Purification Workflow

- **Expression system**: Saccharomyces cerevisiae
- **Expression construct**: Atm1Δ98 (residues 99-678) with C-terminal Strep-tag
- **Tag info**: C-terminal Strep-tag; five residues of the Strep-tag visible in the C-terminal helix structure

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Strep-tag affinity purification | — |  | Purified via C-terminal Strep-tag; [GSH](/xray-mp-wiki/reagents/additives/glutathione/) co-purified with protein throughout purification at low temperature |
| Size-exclusion chromatography | Size-exclusion chromatography | — |  | Final purification step in detergent solution |

**Final sample**: Purified Atm1Δ98 in detergent solution; contained bound [GSH](/xray-mp-wiki/reagents/additives/glutathione/) (Kd = 23 μM) as verified by mass spectrometry
**Yield**: —
**Purity**: —


## Crystallization

### doi/10.1126##science.1246729

| Parameter | Value |
|---|---|
| Method | — |
| Notes | Crystallization details in Supporting Online Material. Data collected at X06SA beamline, Swiss Light Source, Paul Scherrer Institute. ATPase activity of Atm1 was almost fully recovered after detergent solubilization of crystals. |


## Biological / Functional Insights

### Glutathione Binding Site

[GSH](/xray-mp-wiki/reagents/additives/glutathione/) binds in the large positively charged cavity formed by the Atm1 dimer, interacting with residues R280 and R284 (TM4), N343 (TM5), and N390, S394, R397, and D398 (TM6). The binding site is located close to the inner membrane surface on the matrix side. All GSH-coordinating residues are conserved in Atm1-like proteins, including human ABCB7 and bacterial homologs. One residue, D398 (corresponding to human E433), is mutated to lysine in patients with XLSA/A, demonstrating the physiological relevance of [GSH](/xray-mp-wiki/reagents/additives/glutathione/) ligand binding. [GSH](/xray-mp-wiki/reagents/additives/glutathione/) binds with an apparent Kd of 23 μM as measured by microscale thermophoresis.

### Role in Iron-Sulfur Cluster Biogenesis

Atm1, together with [GSH](/xray-mp-wiki/reagents/additives/glutathione/) ([GSH](/xray-mp-wiki/reagents/additives/glutathione/)) and the sulfhydryl oxidase Erv1, is essential for the export of a sulfur-containing molecule from mitochondria that is used by the cytosolic Fe/S protein assembly (CIA) system. This exported molecule is required for maturation of cytosolic-nuclear Fe/S proteins including DNA polymerases, primases, and helicases. The substrate may be [GSH](/xray-mp-wiki/reagents/additives/glutathione/) persulfide (GSSH) or a GSH-coordinated [2Fe-2S] cluster, both of which are consistent with the structural and biochemical data.

### C-Terminal α-Helices Stabilize the Dimer

A unique structural feature of Atm1 is the complete resolution of the C terminus, consisting of a 24-amino-acid α-helix. Two such helices from each monomer interact tightly in a crossover fashion (2.65-4.0 Å distances), stabilizing the inward-facing, open conformation. This feature has not been observed in any other ABC transporter crystal structure and likely represents a common structural element of ABC exporters that keeps the NBDs in close vicinity despite being nucleotide-free.

### Domain-Swapped Architecture

The Atm1 dimer adopts a domain-swapped arrangement where the long TM4 and TM5 helices from each monomer reach out to the other monomer, creating an intertwined, V-shaped molecule. This configuration encloses a 6900 Å³ positively charged cavity on the matrix side of the inner membrane. The two TM6 helices bend out of the membrane, forming a kink at residue S394, providing flexibility to accommodate the [GSH](/xray-mp-wiki/reagents/additives/glutathione/) ligand.

### XLSA/A Disease Mutations

Three XLSA/A patient mutations map to the Atm1 structure: E208D (long TM2 helix), I400M (between TM5 and TM6), and V411L (TM6). All mutations are conservative, indicating that even subtle changes in ABCB7 function lead to disease. The V376 (yeast) / V411L (human) mutation lies at the dimer interface, where the valine side chain undergoes hydrophobic interactions with its counterpart, tightly closing the transmembrane channel toward the intermembrane space.


## Cross-References

- [NaAtm1 ABC Exporter from Novosphingobium aromaticivorans](/xray-mp-wiki/proteins/abc-transporters/naatm1/) — Bacterial homolog of Atm1; companion paper in same Science issue; GSH bound at similar location
- [Human ABCB10 Mitochondrial ATP-Binding Cassette Transporter](/xray-mp-wiki/proteins/abc-transporters/abcb10/) — Related mitochondrial ABC transporter for structural comparison
- [Glutathione (GSH)](/xray-mp-wiki/reagents/additives/glutathione/) — GSH is the bound ligand in the structure and likely a component of the exported substrate
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/) — Representative transporter for comparative transport mechanism studies
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [IRON](/xray-mp-wiki/reagents/additives/iron/) — Additive used in purification or crystallization buffers
