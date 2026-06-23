---
title: Transhydrogenase dII Domain (Thermus thermophilus)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [transporter, enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1260451, doi/10.1016##j.str.2017.05.022]
verified: false
---

# Transhydrogenase dII Domain (Thermus thermophilus)

## Overview

The transhydrogenase dII domain from Thermus thermophilus is the transmembrane proton channel component of the nicotinamide nucleotide transhydrogenase (TH), a proton-translocating membrane enzyme that uses the proton-motive force to drive hydride transfer from NADH to NADP+. The first crystal structures of TH from Thermus thermophilus were determined at 2.8 A (membrane domain, PDB 4O93) and 6.9 A (holo-TH, PDB 4O9U) resolution (Leung et al., Science, 2015). The holo-TH is a dimer with each protomer consisting of two hydrophilic nucleotide-binding domains (dI and dIII) and a transmembrane domain (dII). The dII domain serves as the proton channel, and subsequent higher-resolution structures (2.2 A, PDB 5UNI) revealed key residues and water molecules involved in proton translocation across the membrane.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2017.05.022 | 5UNI | 2.2 | C2221 | dII domain, alpha2 chain (residues 1-94) + truncated beta chain (residues 1-261) | [MAG](/xray-mp-wiki/reagents/lipids/mag/) 8.7 |
| doi/10.1126##science.1260451 | 4O93 | 2.77 | C 1 2 1 | dII domain dimer (transmembrane proton channel domain) from Thermus thermophilus transhydrogenase |  |
| doi/10.1126##science.1260451 | 4O9P | 2.89 | P 1 2_1 1 | dII domain dimer (SeMet derivative) from Thermus thermophilus transhydrogenase |  |
| doi/10.1126##science.1260451 | 4O9U | 6.93 | C 1 2 1 | Holo-TH entire enzyme dimer from Thermus thermophilus transhydrogenase |  |
| doi/10.1126##science.1260451 | 4O9T | 3.08 | P 1 2_1 1 | Holo-TH entire enzyme dimer from Thermus thermophilus transhydrogenase, alternative crystal form |  |

## Expression and Purification

- **Expression system**: E. coli BL21DE3 ΔA
- **Construct**: Complete operon of TH from T. thermophilus (alpha2 + beta) with C-terminal His-tag, co-expressed with polypeptide alpha1 in pETDuet-1 vector


### Purification Workflow

- **Expression system**: E. coli BL21DE3 ΔA
- **Expression construct**: C-terminal His-tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Overexpression | Fermentation | -- | LB with appropriate antibiotics + -- | pETDuet-1 vector, co-expression of alpha2+beta and alpha1 |
| Membrane preparation | Cell lysis | -- | -- + -- | Overexpressed bacterial membranes harvested |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | 6xHis affinity resin | -- + -- | 6xHis [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) |
| Gel filtration | Size-exclusion chromatography | Superose 6 | 0.05 M Tris pH 8.0, 0.1 M NaCl, 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Superose 6 gel filtration chromatography |

**Final sample**: 60 mg/ml in 0.05 M Tris pH 8.0, 0.1 M NaCl, 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)


## Crystallization

### doi/10.1016##j.str.2017.05.022

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | 60 mg/ml dII domain in 0.05 M Tris pH 8.0, 0.1 M NaCl, 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Lipid | [MAG](/xray-mp-wiki/reagents/lipids/mag/) 8.7 |
| Protein-to-lipid ratio | 1:1 |
| Temperature | Room temperature |
| Growth time | Not specified |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | dII domain |
| Lipid | [MAG](/xray-mp-wiki/reagents/lipids/mag/) 8.7 |
| Protein-to-lipid ratio | 1:1 |
| Temperature | Room temperature |
| Growth time | Not specified |


## Biological / Functional Insights

### Holo-TH asymmetric dimer with alternating dIII conformations

The 2015 Science paper (Leung et al.) revealed the 2.8 A structure of the transmembrane proton channel domain and the 6.9 A structure of the entire holo-TH enzyme. The holo-TH is a highly asymmetric dimer with the NADP(H)-binding domain (dIII) in two different orientations, suggesting a catalytic mechanism in which the two copies of dIII alternately function in proton translocation and hydride transfer — a division of labor approximately 40 A apart within the complex.

### Internal water molecules in the proton channel

The 2.2-Å structure reveals nine internal water molecules (W1-W9) within cytoplasmic and periplasmic invaginations on either side of His42α2. W2 and W3 are hydrogen bonded to asparagines that are themselves hydrogen bonded to His42α2, forming part of a hydrogen-bond network surrounding this critical residue. W1 is within the cytoplasmic chamber. In MD simulations, W2 can be observed exchanging with bulk water on the cytoplasmic side of the membrane. W4, W5, and W6 are clustered at the periplasmic entrance and hydrogen bonded to Asn227β and Glu103β. W8 and W9 are hydrogen bonded to W4 through main-chain interactions involving Pro228β and Ala229β.

### His42α2 as central protonation gate

His42α2 (chain A, TM3) is a functionally critical residue located in the middle of the membrane. It is postulated to be transiently protonated during proton translocation across the membrane. In MD simulations with His42α2 protonated, a transient water wire forms between Glu221β and His42α2 in the periplasmic region (z = -2 to 5 Å), and a second water wire persists between His42α2 and Ser208β in the cytoplasmic chamber (z = 5 to 15 Å). With His42α2 deprotonated, no water penetrates the dry region between His42α2 and the periplasmic chamber during 300-ns MD runs.

### Thr214β conformational gating

Thr214β (chain B) displays conformational changes that gate channel access. When the transient water wire forms in the dry region, the Thr214β side-chain χ1 dihedral angle transitions from -60° to +60°, rotating its Oγ atom out of the proton pathway. Mutation of Thr214β to Ala deactivated the enzyme to 3-5% of wild-type activity at pH 6.5, 7.0, and 8.0, confirming its critical role in proton translocation.

### pH-dependent conformational changes

Comparison of the dimeric dII structures solved at pH 6.5 (2.2 Å) versus pH 8.5 (2.8 Å) reveals conformational changes in helix positions. The TM helices in each protomer are slightly tilted about a vertical axis near the middle of the TM bundles. These pH-dependent changes may be related to proton translocation or enzymatic activities affected by pH.

### Hydrophobic dry region in the proton channel

The pore profile shows a narrow region (<2 Å radius) that includes both a dry region on the periplasmic side of His42α2 and the region from His42α2 on the cytoplasmic side. The dry region is composed of hydrophobic aliphatic amino acids and acts as a gated barrier between the periplasmic and cytoplasmic chambers. MD simulations show that water wire formation across this dry region is coordinated with Thr214β conformational changes.


## Cross-References

- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method used to solve the 5UNI structure
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Similar monoglyceride lipid used in LCP crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification and crystallization buffers
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — MD simulations used to elucidate proton translocation mechanism
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Used for final purification step with Superose 6 column
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [1,4-Butanediol](/xray-mp-wiki/reagents/additives/1,4-butanediol/) — Additive used in purification or crystallization buffers
- [Ammonium Formate](/xray-mp-wiki/reagents/additives/ammonium-formate/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
