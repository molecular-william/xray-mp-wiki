---
title: Human KDEL Receptor
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2012.05.064]
verified: false
---

# Human KDEL Receptor

## Overview

The human KDEL receptor is a seven-pass transmembrane receptor that retrieves escaped endoplasmic reticulum (ER) resident proteins from the Golgi apparatus by recognizing the C-terminal KDEL (Lys-Asp-Glu-Leu) retrieval signal. This paper presents the first crystal structure of the human KDEL receptor in complex with a KDEL peptide, solved at 3.0 A resolution using the [lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) method. The structure reveals the molecular basis for KDEL peptide recognition and provides insights into the receptor's role in retrograde transport and pH-dependent ligand binding.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2012.05.064 | 3JMD | 3.0 A | P212121 | Human KDEL receptor (seven transmembrane domain construct with truncated N- and C-terminal extensions, expressed in Sf9 insect cells) | KDEL peptide |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: Human KDEL receptor with truncated N- and C-terminal cytoplasmic tails, containing only the seven transmembrane domain and extracellular loops

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Cell lysis and membrane fractionation | -- | -- + -- | Sf9 insect cells infected with baculovirus expressing the human KDEL receptor construct were harvested and homogenized. Crude membrane fraction was isolated by differential ultracentrifugation. |
| Solubilization | Detergent solubilization | -- | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (N-Dodecyl-beta-D-maltoside) at 1% (w/w) | Membranes solubilized in buffer containing 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm) to extract the seven-pass transmembrane KDEL receptor into detergent micelles. |
| Affinity purification | [Affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) resin | Buffer containing [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) for elution + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | His-tag affinity purification of the KDEL receptor from the solubilized membrane fraction. The receptor was eluted with [Imidazole](/xray-mp-wiki/reagents/additives/imidazole)-containing buffer while maintaining [DDM](/xray-mp-wiki/reagents/detergents/ddm) to keep the protein soluble. |
| Size-exclusion chromatography | [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Superdex 200 column | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) (pH 7.5), 150 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Final purification and buffer exchange. The KDEL receptor was concentrated to approximately 10 mg/ml for crystallization. The protein eluted as a monodisperse peak indicating proper folding and detergent micelle stability. |


## Crystallization

### doi/10.1016##j.jmb.2012.05.064

| Parameter | Value |
|---|---|
| Method | [Lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) |
| Protein sample | KDEL receptor at 10 mg/ml in 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes) (pH 7.5), 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm), mixed with [monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) lipid at a 1:1.5 protein-to-lipid ratio |
| Temperature | 20 C |
| Growth time | Crystals appeared within 1-2 weeks |
| Cryoprotection | Crystals were flash-cooled in liquid nitrogen without additional cryoprotectant (LCP matrix provides inherent cryoprotection) |
| Notes | Crystals grew as thin plates and diffracted to 3.0 A resolution. The structure was solved by molecular replacement. The acidic pH of the reservoir (pH 4.6) mimics the acidic pH of the Golgi apparatus where the KDEL receptor binds its ligand. Space group P212121, one molecule in the asymmetric unit. |


## Biological / Functional Insights

### Molecular basis for KDEL peptide recognition

The crystal structure reveals a deep binding pocket formed by the extracellular loops and the upper portion of the transmembrane helices of the KDEL receptor. The KDEL peptide binds in an extended conformation within this pocket, with key hydrogen bonds formed between the receptor and the conserved Asp and Glu side chains of the KDEL motif. The Lys residue at the N-terminus of the KDEL peptide makes ionic interactions with a cluster of acidic residues on the receptor surface. This binding mode explains the high specificity of the KDEL receptor for the KDEL retrieval signal and its ability to discriminate against other C-terminal tetrapeptides.

### pH-dependent ligand binding mechanism

The structure was solved at acidic pH (4.6), which corresponds to the pH of the cis-Golgi network where the KDEL receptor retrieves escaped ER proteins. The acidic environment promotes protonation of key histidine and glutamate residues in the binding pocket, strengthening the interaction with the KDEL peptide. Upon delivery of the cargo to the ER at neutral pH (approximately 7.2), deprotonation of these residues triggers ligand release, completing the retrieval cycle. This pH-dependent binding mechanism is essential for the receptor''s function in retrograde transport.

### Seven-pass transmembrane topology and comparison to other receptors

The KDEL receptor adopts a seven-pass transmembrane topology, which is distinct from the canonical seven-transmembrane G protein-coupled receptor (GPCR) fold. The transmembrane helices are arranged in a bundle with the ligand-binding pocket oriented toward the extracellular side, consistent with its role in retrieving luminal ER proteins. Despite the topological differences from class A GPCRs, the KDEL receptor shares a similar overall architecture with other seven-pass membrane proteins, suggesting convergent evolution of ligand-binding mechanisms in membrane receptors. The structure provides a structural framework for understanding the [ER retrieval mechanism](/xray-mp-wiki/concepts/signaling-receptors/er-retrieval-mechanism/) that maintains ER protein localization.


## Cross-References

- [ER Retrieval Mechanism](/xray-mp-wiki/concepts/signaling-receptors/er-retrieval-mechanism/) — The KDEL receptor is the central receptor in the ER retrieval mechanism that maintains ER resident protein localization
- [Membrane Mimetics and Structural Biology](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/) — The KDEL receptor was solubilized and crystallized using detergent micelles and lipidic cubic phase, key membrane mimetic techniques
- [DDM (N-Dodecyl-beta-D-maltoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent (1%) used for KDEL receptor membrane extraction and purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used as the cubic phase matrix for LCP crystallization of the KDEL receptor
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant (20-30% PEG 400) used in the LCP crystallization reservoir
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Primary buffer (20 mM, pH 7.5) used in KDEL receptor purification
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) — Used for His-tag affinity purification of the KDEL receptor
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for the KDEL receptor; LCP is particularly well-suited for seven-pass transmembrane proteins
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Used for final purification and buffer exchange of the KDEL receptor
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA affinity chromatography used for initial purification of the His-tagged KDEL receptor
