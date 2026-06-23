---
title: Human P2Y1 Receptor
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14287]
verified: false
---

# Human P2Y1 Receptor

## Overview

The human P2Y1 receptor (P2Y1R) is a class A [G Protein](/xray-mp-wiki/concepts/g-protein/)-coupled receptor ([GPCR](/xray-mp-wiki/concepts/gpcr/)) that serves as a critical target for antithrombotic therapy. It is activated by adenosine 5'-diphosphate ([ADP](/xray-mp-wiki/reagents/ligands/adp/)) and facilitates platelet aggregation, playing a pivotal role in thrombosis formation. Unlike the Gi-coupled P2Y12 receptor, P2Y1R is Gq-coupled and has been suggested to offer a safety advantage over P2Y12R inhibitors with reduced bleeding liabilities. The receptor is also involved in vascular inflammation and calcium wave propagation in astrocytes. Two distinct ligand-binding sites were revealed: an orthosteric site within the transmembrane bundle and an allosteric site on the external receptor interface with the lipid bilayer.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature14287 | 4M48 | 2.70 A | P1 | Human P2Y1R construct 1: residues 1-341 with N-terminal HA signal sequence, Flag tag, and C-terminal PreScission protease site plus 10x His tag. ICL3 (residues K247-P253) replaced by rubredoxin (M1-E54). D320(7.49)N mutation for improved yield and stability.
 | MRS2500 |
| doi/10.1038##nature14287 | 4M49 | 2.20 A | R3H | Human P2Y1R construct 2: residues 1-341 with N-terminal HA signal sequence, Flag tag, and C-terminal PreScission protease site plus 10x His tag. A23-L128 of thermostabilized BRIL (PDB 1M6T) fused before residue A8. D320(7.49)N mutation for improved yield and stability.
 | BPTU |

## Expression and Purification

- **Expression system**: [Sf9](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) insect cells ([Bac-to-Bac](/xray-mp-wiki/methods/expression-systems/bac-to-bac/) [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) Expression System)
- **Construct**: Two engineered constructs: Construct 1 with rubredoxin (M1-E54) fused into ICL3 at K247-P253 and D320N mutation. Construct 2 with A23-L128 of thermostabilized BRIL fused before residue A8 and D320N mutation. High-titre recombinant baculovirus (>10^8 viral particles per ml) used to infect Sf9 cells at 2x10^6 to 3x10^6 cells/ml at MOI of 5.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and differential centrifugation | -- | Hypotonic: 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 10 mM [MgCl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl, [EDTA](/xray-mp-wiki/reagents/additives/edta/)-free protease inhibitor. High osmotic: 1 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 10 mM [MgCl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl. Storage: 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 10 mM [MgCl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl.
 + -- | [Sf9](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) cell membranes disrupted by dounce homogenization. Extensive washing by centrifugation in hypotonic buffer, then high osmotic buffer (3x), then hypotonic buffer again. Purified membranes flash-frozen in liquid nitrogen and stored at -80C.
 |
| Solubilization | Detergent solubilization | -- | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 300 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/) + 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Purified membranes solubilized in 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) and 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) for 3h at 4C in presence of 1 mM [ATP](/xray-mp-wiki/reagents/ligands/atp/) and 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/). Supernatant isolated by centrifugation at 160,000g for 30 min.
 |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) [IMAC](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Wash: 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 300 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 1 mM [ATP](/xray-mp-wiki/reagents/ligands/atp/). Elution: 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 300 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/).
 | [TALON](/xray-mp-wiki/reagents/additives/talon/) resin incubated overnight at 4C. Resin washed with 10 column volumes of wash buffer, then eluted with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/).
 |


## Crystallization

### doi/10.1038##nature14287

| Parameter | Value |
|---|---|
| Method | X-ray crystallography |
| Protein sample | P2Y1R construct 1 ([Rubredoxin](/xray-mp-wiki/reagents/protein-tags/rubredoxin/) fusion) in complex with [MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/) |
| Notes | Data collection statistics from Extended Data Table 1. 50.0-2.70 A resolution (2.80-2.70 A shell). Rmerge 16.1% (83.2% in shell).
 |

| Parameter | Value |
|---|---|
| Method | X-ray crystallography |
| Protein sample | P2Y1R construct 2 ([BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion) in complex with [BPTU](/xray-mp-wiki/reagents/ligands/bptu/) |
| Notes | Data collection statistics from Extended Data Table 1. 50.0-2.20 A resolution (2.30-2.20 A shell). Rmerge 10.1% (97.9% in shell).
 |


## Biological / Functional Insights

### Two distinct ligand-binding sites

The P2Y1R structures reveal two distinct ligand-binding sites. [MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/) recognizes an orthosteric binding site within the seven transmembrane bundle, located closer to the extracellular surface than typical [GPCR](/xray-mp-wiki/concepts/gpcr/) antagonist binding sites. [BPTU](/xray-mp-wiki/reagents/ligands/bptu/) binds to an allosteric pocket on the external receptor interface with the lipid bilayer, making it the first structurally characterized selective [GPCR](/xray-mp-wiki/concepts/gpcr/) ligand located entirely outside of the helical bundle.

### MRS2500 orthosteric binding mode

[MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/) occupies a pocket defined by residues from the N terminus, ECL2, and helices VI and VII. The adenine ring inserts into a binding crevice with R287(6.62) and L44 on either side, and its N6H and N7 are coordinated by hydrogen bonds with N283(6.58). The 2-iodo group fits into a small sub-pocket shaped by the N terminus, interacting with the main chain carbonyl of C42. The N6-methyl group extends into a sub-pocket between helices VI and VII, forming hydrophobic interactions with A286(6.61) and N299(7.28). A salt bridge forms between [MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/) and R195. Key residues K46, R195, Y303(7.32), and Y306(7.35) surround the 3'-phosphate binding region.

### Distinct nucleotide binding between P2Y1R and P2Y12R

Despite recognizing the same endogenous ligand [ADP](/xray-mp-wiki/reagents/ligands/adp/), P2Y1R and P2Y12R reveal very different nucleotide-binding features. The [MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/) binding site in P2Y1R and the 2MeSADP binding site in P2Y12R are spatially distinct, with only minor overlap of phosphate binding regions near position 7.35. In P2Y1R, the adenine ring is adjacent to helices VI and VII, whereas in P2Y12R the adenine group reaches deep into the binding pocket for hydrophobic interactions with helices III and IV. The adenine groups adopt different orientations in the two receptors.

### BPTU allosteric binding at the lipid bilayer interface

[BPTU](/xray-mp-wiki/reagents/ligands/bptu/) binds to a shallow pocket on the external receptor interface with the lipid bilayer, not within the transmembrane bundle. The [Urea](/xray-mp-wiki/reagents/substrates/urea/) group forms two hydrogen bonds with the mainchain carbonyl of L102(2.55), which is available for bidentate coordination because P105(2.58) precludes intrahelical hydrogen bonding. The pyridyl group forms hydrophobic interactions with A106(2.59) and F119. The phenoxy benzene ring wedges into a cavity between helices II and III, interacting with T103(2.56), M123(3.24), L126(3.27), and Q127(3.28). The ligand likely enters the binding pocket via the lipid bilayer due to its high lipophilicity (HPLC logP = 5.7).

### P2Y1R selectivity determinant A106(2.59)

A106(2.59) is unique to P2Y1 among P2Y receptors; other subtypes have larger side chains at this position that would sterically hinder [BPTU](/xray-mp-wiki/reagents/ligands/bptu/) binding. Mutants A106(2.59)W/F/L lost [BPTU](/xray-mp-wiki/reagents/ligands/bptu/) binding ability while retaining recognition of nucleotide agonist 2MeSADP and antagonist [MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/). This explains the P2Y1R selectivity of diarylurea antagonists like [BPTU](/xray-mp-wiki/reagents/ligands/bptu/).

### GPCR structural comparison

The P2Y1R structures share a canonical seven-transmembrane helical bundle architecture with other class A GPCRs. Two disulfide bonds stabilize the extracellular loops: one connecting the N terminus to helix VII, and another connecting helix III to ECL2. The extracellular end of helix V is displaced by over 4 A compared to P2Y12R due to a helical kink, and helix III shifts away from the bundle axis by over 5 A. The intracellular halves of P2Y1R and P2Y12R are very similar.


## Cross-References

- [Human P2Y12 Receptor](/xray-mp-wiki/proteins/gpcr/p2y12-receptor/) — Direct structural comparison; related Gq-coupled vs Gi-coupled P2YR subfamilies
- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — BRIL fused to N-terminus of P2Y1R construct 2 for crystallization
- [MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/) — Co-crystallized nucleotide antagonist (PDB 4M48)
- [BPTU](/xray-mp-wiki/reagents/ligands/bptu/) — Co-crystallized non-nucleotide allosteric antagonist (PDB 4M49)
- [2-Methylthio-ADP (2MeSADP)](/xray-mp-wiki/reagents/ligands/2me-sadp/) — Radiolabeled agonist analog used in binding assays for mutagenesis
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for membrane protein solubilization
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Lipid additive used in combination with DDM for protein stabilization
- [P2Y Receptor Family](/xray-mp-wiki/concepts/p2y-receptor-family/) — P2Y1R is a Gq-coupled member of the P2Y purinergic GPCR family
- [G Protein](/xray-mp-wiki/concepts/g-protein/) — Related protein
- [Gpcr](/xray-mp-wiki/concepts/gpcr/) — Related protein
