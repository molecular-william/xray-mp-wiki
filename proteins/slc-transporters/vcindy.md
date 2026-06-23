---
title: VcINDY Sodium-Dependent Dicarboxylate Transporter
created: 2026-06-08
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11542, doi/10.1038##ncomms15009]
verified: false
---

# VcINDY Sodium-Dependent Dicarboxylate Transporter

## Overview

VcINDY is a sodium-dependent dicarboxylate transporter from Vibrio cholerae, belonging to the [Divalent Anion/Na+ Symporter (DASS) Family](/xray-mp-wiki/concepts/dass-family/). It is a homologue of the mammalian SLC13 transporters (NaCT, NaDC1, NaDC3) and the Drosophila INDY (I'm Not Dead Yet) protein. VcINDY catalyzes the Na+-coupled uptake of di- and tricarboxylates such as [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) and [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/). The 3.2 A crystal structure of VcINDY revealed an inward-facing conformation with one [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) molecule and one sodium ion bound per protomer. Higher resolution 2.8 A structures of succinate- and citrate-bound VcINDY later identified a second Na+-binding site (Na2) and elucidated how DASS proteins recognize and distinguish between C4-dicarboxylate and C6-tricarboxylate substrates.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11542 | not specified in paper | 3.2 A | C2 | N-terminal 10X His-tagged VcINDY | [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) |
| doi/10.1038##ncomms15009 | not specified in paper | 2.8 A | not specified | Full-length VcINDY (462 residues), N-terminal deca-histidine tag cleaved | [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/) |
| doi/10.1038##ncomms15009 | not specified in paper | 2.8 A | not specified | Full-length VcINDY (462 residues), N-terminal deca-histidine tag cleaved | [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) |
| doi/10.1038##ncomms15009 | not specified in paper | 2.8 A | not specified | MT5 (humanized VcINDY octuple mutant) | [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/) |
| doi/10.1038##ncomms15009 | not specified in paper | 2.8 A | not specified | MT5 (humanized VcINDY octuple mutant) | [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21-AI
- **Construct**: N-terminal 10X His-tagged VcINDY in modified pET vector
- **Notes**: Seleno-[L-Methionine](/xray-mp-wiki/reagents/ligands/l-methionine/) (SeMet) protein produced in E. coli B834DE3 cells grown in minimal media containing SeMet. For ncomms15009, proteins expressed with N-terminal cleavable deca-histidine tag in modified pET28b vector; site-directed mutagenesis by QuikChange method.

### Purification Workflow

- **Expression system**: E. coli BL21-AI
- **Expression construct**: N-terminal 10X His-tagged VcINDY

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization | — | 1.2% [n-Decyl-β-D-maltoside](/xray-mp-wiki/reagents/detergents/dm/) (DM) | Membranes solubilized in 1.2% DM |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt affinity (IMAC) | [TALON](/xray-mp-wiki/reagents/additives/talon/) (Clontech) | 50 mM Tris pH 7.5, 100 mM NaCl, 50 mM [Lithium Citrate](/xray-mp-wiki/reagents/additives/lithium-citrate/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.15% DM |  |
| Size-exclusion chromatography | Gel filtration | Shodex KW804 (HPLC) | 50 mM Tris pH 7.5, 100 mM NaCl, 50 mM [Lithium Citrate](/xray-mp-wiki/reagents/additives/lithium-citrate/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.15% DM | Preparative SEC in same buffer |


## Crystallization

### doi/10.1038##nature11542

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | Size-exclusion purified VcINDY in 50 mM Tris pH 7.5, 100 mM NaCl, 50 mM [Lithium Citrate](/xray-mp-wiki/reagents/additives/lithium-citrate/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.15% DM |
| Reservoir | 29% (v/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 1000, 50 mM [Lithium Citrate](/xray-mp-wiki/reagents/additives/lithium-citrate/), 50 mM MOPS pH 6.5 |
| Temperature | 18 |
| Growth time | Not specified |
| Notes | Crystals grown at 18 C. SeMet crystals used for structure determination by multi-crystal SAD at 0.9792 A wavelength. |

### doi/10.1038##ncomms15009

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified VcINDY or MT5 in crystallization buffer |
| Reservoir | Not specified in paper body |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Structures determined by combining [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) and multiple isomorphous replacement and anomalous scattering ([MIRAS](/xray-mp-wiki/methods/structure-determination/miras/)) phasing. [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) phases allowed modelling of 445 out of 462 residues. |


## Biological / Functional Insights

### Inward-facing conformation and inverted two-fold symmetry

VcINDY consists of 11 transmembrane helices (TM1-TM11) arranged in two
inverted symmetry-related halves. The N-terminal half (TM2-TM6) and
C-terminal half (TM7-TM11) each form a hand-shaped structure related by
an inverted two-fold symmetry axis parallel to the membrane plane. The
N-terminal hand adopts a V-shape while the C-terminal hand adopts a
U-shape. Each hand contains a helical hairpin (HP_in and HP_out,
respectively) that inserts into the membrane from opposite sides.

### Two sodium-binding sites (Na1 and Na2)

Two Na+ binding sites were identified in 2.8 A structures. Na1 is coordinated by
Ser146 (side chain and backbone carbonyl), Ser150 (backbone carbonyl), Asn151
(side chain carbonyl), and Gly199 (backbone carbonyl). Na2 is coordinated by
Thr373 (side chain hydroxyl and backbone carbonyl), Asn378 (side chain carbonyl),
Ala376 (backbone carbonyl), and Ala420 (backbone carbonyl). Both Na+ ions are
penta-coordinated and separated by >13 A. Na2 is functionally more important
than Na1; T373A mutation caused more severe transport defects than S146A.

### Succinate recognition without positively charged residues

Unlike many anion transporters that use Arg or Lys residues, VcINDY binds
[Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/) without any positively charged amino acids in the binding site.
Instead, the two negative charges of [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/) are stabilized by positive
helix dipoles from four short helices (HP_in, HP_out, TM5b, TM10b) and by
the two bound Na+ ions. This suggests a general mechanism for achieving
anion selectivity within the lipid bilayer by membrane proteins.

### Substrate discrimination between C4 and C6 carboxylates

VcINDY discriminates between [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/) (C4) and [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) (C6) through
steric and electrostatic mechanisms. Pro201 and Thr379 pack against [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/)'s
pro-S carboxylate, steering it away from the transporter. In the MT5
humanized variant (P201G, T379V), the pro-S carboxylate forms additional
hydrogen bonds with the protein, explaining why MT5/NaCT transport [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/)
more effectively.

### Relationship to mammalian SLC13 transporters

VcINDY shares 26-33% sequence identity with human SLC13 transporters
(NaCT/SLC13A5, NaDC1/SLC13A2, NaDC3/SLC13A3). The SNT motifs identified
in VcINDY are conserved across the DASS family and serve as signature
sequences for Na+-dependent tri- and dicarboxylate transporters. The
structural framework provides direct insight into the transport mechanism
of human NaCT, a potential drug target for obesity, diabetes, and
cardiovascular diseases.

### Structural similarity to AbgT transporters

VcINDY exhibits striking structural resemblance to dimeric AbgT transporters
(r.m.s.d. 3.1-3.5 A for ~300 C-alpha atoms), despite only 13-18% sequence
identity. A Na+-binding site similar to Na2 in VcINDY was found in an AbgT
transporter, suggesting that at least one functionally important Na+-binding
site is conserved between the DASS and AbgT protein families.


## Cross-References

- [Divalent Anion/Na+ Symporter (DASS) Family](/xray-mp-wiki/concepts/dass-family/) — VcINDY is a member of the DASS family of transporters
- [Inward-Facing Conformation](/xray-mp-wiki/concepts/inward-facing-conformation/) — The VcINDY structure represents an inward-facing conformation
- [N-Decyl-beta-D-maltopyranoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Primary detergent used for VcINDY purification
- [MOPS Buffer](/xray-mp-wiki/reagents/buffers/mops/) — Used in crystallization reservoir (50 mM, pH 6.5)
- [Lithium Citrate](/xray-mp-wiki/reagents/additives/lithium-citrate/) — Used in purification buffer and crystallization reservoir
- [Citrate](/xray-mp-wiki/reagents/ligands/citrate/) — Primary substrate and bound ligand in the crystal structure
- [Succinate](/xray-mp-wiki/reagents/ligands/succinate/) — Alternative dicarboxylate substrate of VcINDY
- [Selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/) — Used for SeMet SAD phasing
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Method used in structure determination or purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
