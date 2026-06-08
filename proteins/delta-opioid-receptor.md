---
title: Human Delta-Opioid Receptor (OPRD1)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12944, doi/10.1038##nature08282]
verified: false
---

# Human Delta-Opioid Receptor (OPRD1)

## Overview

The human delta-opioid receptor (δ-OR, OPRD1, UniProt P41143) is a class A G-protein-coupled receptor (GPCR) that mediates analgesia, mood regulation, and neuroendocrine effects. It is one of three classical opioid receptors alongside the mu (μ-OR) and kappa (κ-OR) receptors. The δ-OR is activated by endogenous enkephalins and exogenous ligands including naltrindole (selective antagonist), DADLE (selective agonist), and BW373U86 (selective agonist). The receptor exhibits a conserved allosteric sodium ion binding site within its seven-transmembrane bundle that modulates ligand binding and functional selectivity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12944 | TBD | 1.8 | C21 | BRIL-δOR(ΔN/ΔC) (residues 36-338, N-term BRIL fusion, C-term 34 aa truncation, Pro37Ser mutation) | naltrindole |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: BRIL-δOR(ΔN/ΔC) with N-terminal HA tag, Flag tag, 10xHis tag, TEV protease site; 35 N-terminal residues replaced with BRIL; 34 C-terminal residues deleted; Pro37Ser mutation

### Purification Workflow

- **Expression system**: Sf9 insect cells
- **Expression construct**: BRIL-δOR(ΔN/ΔC) with HA/Flag/10xHis tags, TEV site

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Baculovirus infection | -- | 50 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 1.0 M NaCl + -- | Infected Sf9 cells at 27 deg.C for 48 h |
| Membrane solubilization | Detergent solubilization | -- | 50 mM HEPES pH 7.5, 500 mM NaCl + 0.75% DDM, 0.15% CHS | 25 μM naltrindole present; 3 h at 4 deg.C |
| Affinity chromatography | TALON IMAC | TALON IMAC resin (Clontech) | 20 mM imidazole pH 7.5, 0.7 M NaCl, 0.1% DDM, 0.02% CHS + 0.1% DDM, 0.02% CHS | Overnight incubation at 4 deg.C; wash with 15 column volumes |
| Elution | Imidazole elution | TALON IMAC resin | 200 mM imidazole pH 7.5 + 0.1% DDM, 0.02% CHS | Elution with imidazole |


## Crystallization

### doi/10.1038##nature12944

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | BRIL-δOR(ΔN/ΔC)-naltrindole complex at 10-15 mg/ml |
| Temperature | 20 deg.C |
| Growth time | 2-4 weeks |
| Cryoprotection | Mother liquor supplemented with 25% glycerol |
| Notes | 47 crystals used for data collection; beamline GM/CA CAT 23ID-D, APS |


## Biological / Functional Insights

### Allosteric Sodium Ion Modulation

The δ-OR contains a highly conserved allosteric sodium ion binding site within the seven-transmembrane bundle core. The sodium ion is coordinated by five oxygen atoms from Asp95 (2.50), Ser135 (3.39), Asn131 (3.35) side chains, and two structurally conserved water molecules in the first coordination shell. A second coordination shell includes Trp274 (6.48), Asn310 (7.45), and Asn314 (7.49). The sodium ion stabilizes a reduced agonist affinity state and modulates signal transduction. At physiological sodium concentrations (140 mM), the sodium site is likely saturated (K_B = 13.3 mM). The non-conserved Asn131 (3.35) side chain is unique to opioid receptors and positions its OD1 and ND2 atoms between the ion and orthosteric pocket.

### Efficacy Switches and Beta-Arrestin Bias

Sodium-coordinating residues act as efficacy switches that regulate biased signaling. Mutating Asn131 (3.35) to alanine or valine augments constitutive β-arrestin-mediated signaling, exceeding wild-type activation levels. Asp95 (2.50), Asn310 (7.45), and Asn314 (7.49) mutations transform classical δ-OR antagonists (naltrindole, naltriben, BNTX) into potent β-arrestin-biased agonists. The Asn131 (3.35)Ala mutation abolishes sodium binding, while Asn131 (3.35)Val retains sodium binding with lower affinity. These mutations demonstrate that sodium-coordinating residues serve as molecular efficacy switches controlling the balance between G-protein and β-arrestin signaling pathways.

### Intracellular Loop 3 (ICL3) Conformation

The high-resolution structure reveals a fully resolved ICL3 adopting a closed inactive state conformation, unlike lower-resolution constructs fused to T4 lysozyme where ICL3 is replaced. The wild-type ICL3 contains Arg257 (6.31) that forms polar and ionic interactions. The ICL3 hydrophobic cluster includes residues that interact with water molecules and lipids. This intact ICL3 conformation closely resembles a near-native state.

### Orthosteric Ligand Binding Site

The orthosteric site features water-mediated ligand-receptor interactions. Naltrindole binds through hydrogen bonds and hydrophobic interactions. Asp128 (3.32) occupies a central position deep in the orthosteric site and establishes a salt bridge with the nitrogen group of naltrindole. The extracellular loop 3 (ECL3) contains Arg291 (ECL3) that constrains loop conformation through hydrogen-bonding networks with Val287 (ECL3) and Trp284 (6.58), positioning the latter for π-π interaction with naltrindole.


## Cross-References

- [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) — Subtype-selective δ-OR antagonist used in crystal structure
- [DADLE](/xray-mp-wiki/reagents/ligands/dadle/) — Selective δ-OR peptide agonist used in functional assays
- [Bremazocine](/xray-mp-wiki/reagents/ligands/bremazocine/) — Opioid ligand characterized in radioligand binding assays
- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — BRIL fusion replaces ICL3 for crystallization
- [Sodium Ion Allosteric Modulation in GPCRs](/xray-mp-wiki/concepts/sodium-allosteric-modulation/) — δ-OR sodium site provides molecular basis for allosteric regulation
- [Biased Agonism in GPCRs](/xray-mp-wiki/concepts/biased-agonism/) — Efficacy switches modulate β-arrestin-biased signaling
- [Kappa Opioid Receptor](/xray-mp-wiki/proteins/kappa-opioid-receptor/) — Related classical opioid GPCR
- [Beta-Arrestin Signaling](/xray-mp-wiki/concepts/beta-arrestin-signaling/) — β-arrestin recruitment assays used for functional characterization
