---
title: "Human Alpha4Beta2 Nicotinic Receptor"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19785]
verified: false
---

# Human Alpha4Beta2 Nicotinic Receptor

## Overview

The human alpha4beta2 nicotinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptor (nAChR) is a pentameric ligand-gated ion channel and the most abundant nicotinic receptor subtype in the brain. It mediates fast chemical neurotransmission and is a key therapeutic target for neuromuscular disease, addiction, and epilepsy. The receptor assembles in two functional subunit stoichiometries (3α:2β and 2α:3β), with the latter showing approximately 100-fold higher affinity for [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/) and [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/). The alpha4 and beta2 subunits share 59% amino acid sequence identity and adopt similar backbone conformations. This structure provides insights into ligand recognition, heteromer assembly, ion permeation, and desensitization in Cys-loop receptors.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature19785 | 5HUW | 3.9 A | P212121 | Human alpha4 (residues 1-338, 556-601) and beta2 (residues 1-330, 417-477) with M3-M4 loop deletion and Glu-Arg linker at MX-M4 junction. Strep-tag at C terminus of beta2 subunit. | Nicotine (bound at two alpha-beta interfaces) |

## Expression and Purification

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Transfection and expression | [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) transduction with MOIs 0.25:0.5 for alpha4:beta2 subunits | Not specified | Not specified | [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/) (0.1 mM) and sodium butyrate (3 mM) added at transduction; cells at 30 C and 8% CO2 |
| Cell lysis and solubilization | Cell harvest after 72 h; detergent solubilization | Not specified | Not specified | Not specified in detail |
| Affinity purification | Strep-tag affinity purification on beta2 C-terminus | Strep-Tactin | Not specified | Strep-tag preceded by Ser-Ala linker |
| Size-exclusion chromatography | Fluorescence-detection size-exclusion chromatography (FSEC) for monodispersity screening | SRT [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)-500 column | Not specified | Monitored by tryptophan fluorescence; time-dependent oligomerization/aggregation observed |


## Crystallization

### doi/10.1038##nature19785

| Parameter | Value |
|---|---|
| Method | Co-crystallization with [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/) and [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) analogue |


## Biological / Functional Insights

### Neurotransmitter-binding site architecture at alpha-beta interfaces

[Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/) binds at the alpha-beta interfaces in the classical neurotransmitter site, almost fully buried from solvent. The alpha4 subunit forms the (+) side and beta2 forms the (-) side. Three loops from each side contribute: A, B, C from the (+) side and D, E, F from the (-) side. Residues from loops A-E form a tightly packed aromatic box surrounding [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/), with the floor formed by Y100 on loop A and W57 on the beta2 strand in loop D. The back walls are defined by W156 in loop B and L121 on the beta6 strand in loop E. [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/) forms hydrophobic interactions with Y100, W57, W156, V111, F119, and L121, and is poised to form a hydrogen bond between its pyrrolidine nitrogen and the backbone carbonyl oxygen of W156, as well as a cation-pi interaction with the indole ring of W156. No electron density was observed at beta-beta or beta-alpha interfaces, explaining binding selectivity.

### Heteromeric assembly and subunit ordering

The receptor assembles as a pseudo-symmetrical pentamer with subunit ordering of alpha-beta-beta-alpha-beta around the ring. The alpha-beta interface buries 2820 A2 (+ subunit) and 2806 A2 (- subunit), significantly larger than the beta-beta (2501/2575 A2) and beta-alpha (2544/2561 A2) interfaces. The conserved aromatic residues at non-alpha-beta interfaces are reorganized, precluding [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/) binding. In the beta2 subunit contributing to the (+) side, R149 replaces the [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) found before loop B tryptophan in alpha4. This arginine orients longitudinally into the binding pocket base and is sandwiched between two tyrosine aromatic rings, mimicking the cation-pi interaction of [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/). W151 in loop B must rotate out of the binding pocket completely.

### Ion permeation and desensitized conformation

The receptor pore is formed by M2 alpha-helices from each subunit. A strong electron density peak in the pore was modelled as a Na+ ion and water. The pore conformation most closely resembles the desensitized GABA_A receptor, with the gate at the cytosolic end. The extracellular vestibule is strongly electronegative, probably serving to increase local cation concentration. The 20' position is the only site where alpha4 and beta2 subunits contribute opposing charges (20' glutamate from alpha4 and 20' lysine from beta2). The selectivity filter at the pore base is dominated by five glutamate side chains folded toward the pore axis. The receptor is locked in a non-conducting, desensitized conformation by [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/).

### Conformational changes underlying desensitization

Comparison of the alpha4beta2 receptor with reference structures (GlyR-open, GABA_A desensitized) reveals extensive conformational rearrangements at the ECD-TMD interface. The extracellular and transmembrane subdomains behave largely as rigid bodies during state transitions. The alpha4beta2 receptor conformation is distinct from the desensitized GABA_A receptor, providing important structural insight into allosteric gating in Cys-loop receptors. The N-terminal helix is important in pentameric assembly, and the M2-M3 loop is critical for allosteric signal transduction.


## Cross-References

- [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/) — Co-crystallization ligand bound at alpha-beta interfaces; functional agonist
- [Epibatidine](/xray-mp-wiki/reagents/additives/epibatidine/) — Used in competition binding assays to determine ligand affinities
- [Acetylcholine-Binding Protein (AChBP)](/xray-mp-wiki/proteins/cys-loop-receptors/acetylcholine-binding-protein/) — Soluble surrogate of Cys-loop receptor extracellular domain; used for structural comparison of nicotine binding
- [Human GABA_A Receptor Beta-3 Subunit](/xray-mp-wiki/proteins/cys-loop-receptors/gabar-b3/) — Cys-loop receptor homologue; desensitized state used for pore conformation comparison
- [Mouse 5-HT3A Receptor](/xray-mp-wiki/proteins/cys-loop-receptors/mouse-5ht3a-receptor/) — Homopentameric Cys-loop receptor; MX helix conformation comparison
- [GLIC](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Prokaryotic Cys-loop receptor; structural superposition and conformational comparison
- [Cys-Loop Receptor Family](/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/) — Alpha4beta2 nAChR is a member of the Cys-loop receptor superfamily
- [Desensitization in Cys-Loop Receptors](/xray-mp-wiki/concepts/signaling-receptors/desensitization-in-cys-loop-receptors/) — Alpha4beta2 receptor locked in desensitized conformation by nicotine
- [Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Related protein
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Related protein
