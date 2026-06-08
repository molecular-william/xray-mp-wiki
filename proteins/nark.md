---
title: NarK Nitrate/Nitrite Antiporter from Escherichia coli
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms8097]
verified: false
---

# NarK Nitrate/Nitrite Antiporter from Escherichia coli

## Overview

NarK is a nitrate/nitrite antiporter from the nitrate/nitrite porter (NNP) family in the major facilitator superfamily (MFS). It plays a central role in nitrate uptake and nitrite extrusion in Escherichia coli, functioning as a nitrate/nitrite antiporter that couples substrate recognition to the transport cycle through concomitant movement of transmembrane helices and key residues in the substrate-binding site. NarK comprises 12 transmembrane helices with pseudo twofold symmetry and adopts inward-open, occluded, and outward-open conformations during the alternating access transport cycle.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms8097 | not specified | 2.35 A | P2_12_12_1 | Full-length E. coli NarK (GI: 945783, residues 1-427) from strain K-12 MG1655, N-terminal His8-GFP tag cleaved | none (apo inward-open state) |
| doi/10.1038##ncomms8097 | not specified | 2.4 A | P2_12_12_1 | Full-length E. coli NarK with nitrate bound | nitrate ion (NO3-) |
| doi/10.1038##ncomms8097 | not specified | 2.4 A | P2_12_12_1 | Full-length E. coli NarK with nitrate bound | nitrate ion (NO3-) |

## Expression and Purification

- **Expression system**: Escherichia coli C41(DE3) Delta acrB
- **Construct**: Full-length NarK (GI: 945783) from E. coli K-12 MG1655 genome, cloned in pET-modified vector with N-terminal His8-GFP tag
- **Induction**: 0.5 mM IPTG at 20 C for 24 h

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer processor (Microfluidics) at 15,000 p.s.i., three passages | not applicable | 50 mM Tris-HCl pH 8.0, 300 mM NaCl, 20 mM NaNO3, 0.1 mM PMSF, 4 mM beta-mercaptoethanol | Centrifugation at 12,000g, 30 min, 4 C to remove debris |
| Membrane isolation | Ultracentrifugation | not applicable | Same as lysis buffer | 138,000g, 1 h, 4 C to pellet membranes |
| Solubilization | Detergent solubilization | not applicable | 50 mM Tris-HCl pH 8.0, 300 mM NaCl, 20 mM NaNO3, 0.1 mM PMSF, 4 mM beta-mercaptoethanol + 2% n-dodecyl-beta-D-maltoside (DDM), 0.4% cholesteryl hemisuccinate (CHS) | 30 min at 4 C, ultracentrifugation at 138,000g, 30 min |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA Superflow (Qiagen), 10 ml | 50 mM Tris-HCl pH 8.0, 300 mM NaCl, 25 mM NaNO3, 4 mM beta-mercaptoethanol, 0.05% DDM, 0.01% CHS + 0.05% DDM, 0.01% CHS | Binding 2 h; wash with 20 mM imidazole; elution with 300 mM imidazole at 4 C |
| Tag cleavage | Protease cleavage | Ni-NTA column (10 ml) |  | His-tagged tobacco etch virus protease (produced in-house) cleaved GFP-His8 tag; protease retained on column |
| Size-exclusion chromatography | SEC | HiLoad 16/600 Superdex 200 pg column (GE Healthcare) | 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 25 mM NaNO3, 4 mM beta-mercaptoethanol, 0.05% DDM, 0.01% CHS + 0.05% DDM, 0.01% CHS | Final sample concentrated to 15-20 mg/ml |

**Final sample**: 15-20 mg/ml


## Crystallization

### doi/10.1038##ncomms8097

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified NarK, 15-20 mg/ml |
| Reservoir | not specified in paper |
| Mixing ratio | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Three crystal structures determined (apo inward-open, nitrate-bound inward-open, nitrate-bound occluded); all in P212121 space group; X-ray source: SPring-8 BL32XU |


## Biological / Functional Insights

### NarK is a nitrate/nitrite antiporter

In vitro reconstituted liposome-based nitrite-flux assay demonstrated that NarK functions as a nitrate/nitrite antiporter. Nitrite influx was driven by a nitrate concentration gradient across the membrane at pH 7 with membrane potential present. Substrate specificity showed nitrate and nitrite transport but not chloride, carbonate, formate, acetate, or propionate as counteranions, indicating tight coupling without transport in absence of counteranions.

### Nitrate recognition in the substrate-binding site

The substrate-binding site is formed by F49, R89, F147, N175, Y263, F267, and R305. Nitrate is sandwiched between F147 and F267 forming pi-pi stacking interactions. R89 forms a bidentate salt bridge with nitrate oxygen atoms. Y263 forms a bifurcated hydrogen bond with nitrate oxygen atoms. R305 guanidinium group is oriented perpendicularly to the substrate. These residues are highly conserved among NNP family transporters.

### Alternating access via TM helix bending

The transport cycle involves conformational changes between inward-open, occluded, and outward-open states. TM7, TM10, and TM11 in the C bundle bend at conserved Gly residues (G268 in TM7; G363, G365, G367, G408, G414, G417, G418 in TM10/11) during the transition from occluded to inward-open state. TM10 and TM11 cytosolic halves rotate 31 and 26 degrees away from the transporter center. TM7 rotates 18 degrees toward the periphery. These Gly residues are strictly conserved in NNP family transporters.

### Coupling mechanism between substrate recognition and conformational change

In the nitrate-bound occluded state, the negative charge of nitrate relaxes the electrostatic repulsion between R89 and R305. Transition to inward-open state induces TM bending, enlarging the substrate-binding site volume from 37.6 A^3 to 50.5 A^3, decreasing nitrate affinity and facilitating release. Y263 and R305 are the key coupling residues; Y263F and R305K mutants completely abolish transport activity. The electrostatic repulsion between R89 and R305 prevents premature closure of the transport pathway.

### Structural basis for tight coupling

Acetate and propionate ions do not facilitate nitrate uptake, likely because their bulky methyl and ethyl groups prevent interaction with the narrow substrate binding site. This confirms NarK is a tightly coupled antiporter that does not transport substrates in the absence of counteranions. MD simulations showed the apo occluded state spontaneously transitions toward inward-open conformation within 10 ns when nitrate is absent, confirming the coupling mechanism.


## Cross-References

- [Nitrate/Nitrite Porter (NNP) Family](/xray-mp-wiki/concepts/nnp-family/) — NarK belongs to the NNP family of the major facilitator superfamily
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) — NarK is a member of the MFS superfamily
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — NarK operates via alternating access between inward-open, occluded, and outward-open states
- [NarU Nitrate/Nitrite Antiporter from Escherichia coli](/xray-mp-wiki/proteins/naru/) — Related NNP family member with 75% sequence similarity to NarK
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/n-dodecyl-beta-d-maltopyranoside/) — Primary detergent used for NarK membrane solubilization
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/lipids/cholesteryl-hemisuccinate/) — Lipid stabilizer used with DDM for NarK solubilization
