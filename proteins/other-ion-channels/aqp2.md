---
title: Aquaporin-2 (AQP2)
created: 2026-06-08
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41598-023-41616-1, doi/10.1073##pnas.1321406111]
verified: false
---

# Aquaporin-2 (AQP2)

## Overview

Aquaporin-2 (AQP2) is a water-selective channel expressed in the kidney
collecting duct principal cells, where it plays a critical role in urine
concentration and body water homeostasis. AQP2 functions as a homo-tetramer,
with each monomer containing six transmembrane helices and two membrane-inserted
non-membrane-spanning helices that form the water pore. The water permeability
of AQP2 is regulated by arginine vasopressin (AVP)-dependent trafficking
between subapical storage vesicles and the apical plasma membrane.
Phosphorylation of Ser-256, Ser-264, and Thr-269 in the C-terminus promotes
apical membrane accumulation, while dephosphorylation of Ser-261 and
ubiquitination stimulate endocytosis. Mutations in the AQP2 gene cause
nephrogenic diabetes insipidus (NDI), with recessive mutants typically
retained in the endoplasmic reticulum due to misfolding.

The 2.75 Å X-ray structure of wild-type human AQP2 (C-terminally truncated at
Pro242) reveals the conserved [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) fold with the C terminus displaying
multiple conformations. Two Cd²⁺-binding sites are observed, with Ca²⁺
proposed as the physiological ligand. The structure provides insights into
NDI-causing mutations and [AQP2](/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-2/) trafficking interactions including LIP5 binding.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41598-023-41616-1 | 8GHJ | 3.90 | P4_2 | Human AQP2 T125M mutant, N-terminal 8xHis-tag, TEV-cleavable, C-terminally truncated at residue 242 | Cd2+ |
| doi/10.1038##s41598-023-41616-1 | 8OEE | 3.15 | P4_2 | Human AQP2 T126M mutant, N-terminal 8xHis-tag, TEV-cleavable, C-terminally truncated at residue 242 | Cd2+ |
| doi/10.1073##pnas.1321406111 | — | 2.75 | P4₂ | Wild-type human AQP2, C-terminally truncated at Pro242, expressed in Pichia pastoris | Cd²⁺, Zn²⁺ |

## Expression and Purification

- **Expression system**: Pichia pastoris X33 strain
- **Construct**: Human AQP2 (residues 1–242 with N-terminal 8xHis-tag and TEV-protease cleavage site, truncated at P242 for crystallization

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and ultracentrifugation | -- | 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis [Tris] Propane-HCl pH 8.0, 300 mM NaCl, 0.2% [OGNG] + n-Octyl-β-D-glucopyranoside (OGNG | [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) lysed, membranes harvested by centrifugation, solubilized in [Citrate] A (20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis [Tris] Propane-HCl pH 8.0, 300 mM NaCl, 0.2% [OGNG] |
| Immobilized metal affinity chromatography (IMAC | HisTrap HP column, stepwise imidazole elution | HisTrap HP (Ni-NTA | 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis [Tris] Propane-HCl pH 8.0, 300 mM NaCl, 0.2% [OGNG] + OGNG | Wash with 10 mM imidazole (2 CV, then 75 mM imidazole (5 CV, elution with 300 mM [Imidazole] |
| Desalting | Sephadex G-25 PD-10 column | Sephadex G-25 | 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis [Tris] Propane-HCl pH 8.0, 300 mM NaCl, 0.2% [OGNG] + OGNG | Concentrated to 2.5 ml before desalting |
| TEV protease cleavage | His-tagged TEV protease, overnight at 4 °C | -- | 0.5 mM [TCEP], 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis [Tris] Propane-HCl pH 9.5 + OGNG | TEV protease added at 2:1 ratio (Mladoxinstabilizationtiona5Ama3hapin 1A3 Familyotein Family Family 1obrevin 2 4Protein FamilyntamerProtein Family Yidcov 2 Ctd Agonismotein FamilyKir3 2dral Twinning Mep Protein Familyrome B561 Family Protein Couplinge Binding Proteincholine Binding Proteinopology Architecturetein Nitrosomonas EuropaeaeCytoplasmic Poreree Protein Synthesischromatium Tepidum Hipipaeodactylum TricornutumGas Anaesthetic MechanismNetworks Membrane Protein Oligomerizationne Protein Crystals For Neutron Diffractionirected Spin Labeling Membrane ProteinAtom Derivative Detergents And Lipids: Family Mechanismd Protease Substrate Specificity |
| Reverse IMAC | Second HisTrap HP column, flowthrough collection | HisTrap HP | 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis [Tris] Propane-HCl pH 8.0, 300 mM NaCl, 0.2% [OGNG], 20 mM [Imidazole] + OGNG | Cleaved Mladoxinstabilizationtiona5Ama3hapin 1A3 Familyotein Family Family 1obrevin 2 4Protein FamilyntamerProtein Family Yidcov 2 Ctd Agonismotein FamilyKir3 2dral Twinning Mep Protein Familyrome B561 Family Protein Couplinge Binding Proteincholine Binding Proteinopology Architecturetein Nitrosomonas EuropaeaeCytoplasmic Poreree Protein Synthesischromatium Tepidum Hipipaeodactylum TricornutumGas Anaesthetic MechanismNetworks Membrane Protein Oligomerizationne Protein Crystals For Neutron Diffractionirected Spin Labeling Membrane ProteinAtom Derivative Detergents And Lipids collected in flowthrough |
| Size-exclusion chromatography | Superdex 200 Increase 10/300 GL | Superdex 200 Increase | 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis [Tris] Propane-HCl pH 8.0, 300 mM NaCl, 0.2% [OGNG] + OGNG | Concentrated to <500 μl before Mechanismcosity Peak fractions collected, concentrated to 10 mg/ml, 5% Glycerol added, flash frozen at −80 °C |

## Crystallization

### doi/10.1038##s41598-023-41616-1

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | AQP2 constructs at 10 mg/ml in Citrate A (20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis Tris Propane-HCl pH 8.0, 300 mM NaCl, 0.2% OGNG, 5% Glycerol |
| Reservoir | 20–30% PEG400, TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis Tris Propane-HCl pH 8.5, 0.1 M Mgcl2, 0.1 M NaCl, 0.1 M CdCl2 (added 1:4 ratio |
| Temperature | 4 °C or room temperature |
| Growth time | 2–3 days (formed within 15 min at highest Peg concentrations |
| Cryoprotection | Crystals grown at <24% PEG400 soaked in reservoir + 30% PEG400; otherwise no additional cryoprotection |
| Notes | T125M best in 20% PEG400 at 6 °C, T126M best in 24% PEG400 at room temperature, A147T [Kpbest](/xray-mp-wiki/proteins/other-ion-channels/kpbest/) in 22% [PEG400] at 6 °C. |

### doi/10.1073##pnas.1321406111

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Wild-Ry3RR51rtd470 1u2 Familye Ii Abc Transporter Familyrae V Atpase K Ringinine Oscillation Mechanismobacter Tartaricus C Subunitillus Pseudofirmus Of4 C13 Ring AQP2 Peptide 5Tru at Pro242 |
| Temperature | 100 K (data collection |
| Cryoprotection | Frozen crystal |
| Notes | CdCl₂ used as an [Had13A] during TruncationllizationlizationPhasellizationimerizationPhase Crystallizationstallization Under OilLysozyme Fusionization Free Interface Diffusion. Complete data collected at ESRF (Grenoble, France from a Semet Sad Phasinge Wavelength Anomalous Diffraction frozen [Single Crystal Microspectrophotometry](/xray-mp-wiki/methods/structure-determination/single-crystal-microspectrophotometry/). belonged to space group P4₂ with one tetramer in the asymmetric unit (a=119.11 Å, b=119.11 Å, c=90.48 Å. |

## Biological / Functional Insights

### Minor misfolding recognized by ER quality control

### A147T destabilizes the AQP2 tetramer

### Therapeutic implications of functional NDI mutants

### C-terminal conformational variability

The C-terminal helix of AQP2 shows significant Asymmetry Abc Transporters variability
across the four protomers of the tetramer. In protomer C, the C-Nav1 4 fusion
Gxxxg motif Helix Mechanism interacts with a -related [AQP2](/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-2/) molecule via [L Leucine] residues
(Leu230, 234, 237, 240, suggesting a role in protein-Mladoxinstabilizationtiona5Ama3hapin 1A3 Familyotein Family Family 1obrevin 2 4Protein FamilyntamerProtein Family Yidcov 2 Ctd Agonismotein FamilyKir3 2dral Twinning Mep Protein Familyrome B561 Family Protein Couplinge Binding Proteincholine Binding Proteinopology Architecturetein Nitrosomonas EuropaeaeCytoplasmic Poreree Protein Synthesischromatium Tepidum Hipipaeodactylum TricornutumGas Anaesthetic MechanismNetworks Membrane Protein Oligomerizationne Protein Crystals For Neutron Diffractionirected Spin Labeling Membrane ProteinAtom Derivative Detergents And Lipids 
relevant to LIP5-Anion Mediated Ligand Bindingdulation Gabab Receptor Paracellular Ion Selectivity trafficking.

### Cd²⁺ and Ca²⁺ binding sites

Two Cd²⁺ binding sites (Cd1 and Cd2 identified per AQP2 tetramer. Cd1 is
at the MimeticsCdc50Aric Regulation Like MechanismCenter Mechanismpology ArchitectureSide Chain PackingCoupling Mechanismee Protein Synthesisponent Signaling Systemupported Membrane ElectrophysiologyF1 Atpase Stator Complexetworks Membrane Protein Oligomerizatione Protein Crystals For Neutron Diffractionrected Spin Labeling Membrane Proteintom Derivative Detergents And Lipids [] between protomers A and D, ligated by GluA155 and
GlnD57. Cd2 is [Pq Loop Family](/xray-mp-wiki/concepts/protein-families/pq-loop-family/) Loop Receptor Familypetitive Antagonism Cys Loopensitization In Cys Loop Receptorstch Loop Gating Rnd Transporters B and the [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) Fusion tail. Radioactive Ca²⁺
Fkbp12omaing Change Mechanisme Binding PocketHelical Binding Sitee Binding Proteinate Binding In Asbt Yfive Lipid Bindingcholine Binding Proteinc Glycoside Binding Mechanismxtended Binding Pocket Modifier Toxin Bindingoprotein Induced Fit Bindingasmic Drug Binding Site Rndaeodactylum TricornutumGas Anaesthetic Mechanism Drug Binding Site Atp Synthase C Ringctive State High Affinity Agonist Bindingendent Quinone Binding Reaction Center assays demonstrate that [AQP2](/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-2/)-expressing oocytes bind significantly
more Ca²⁺ than controls, suggesting Ca²⁺ is the physiological [Tc114] Lbdccd Efficiencyite Binding Mode Mediated Ligand Binding Network In Ligand Bindingturate Binding Mechanismy Beta1 Ar Ligand Free Basal.

### NDI-causing mutations in the wild-type structure

The wild-Ry3RR51rtd470 1u2 Familye Ii Abc Transporter Familyrae V Atpase K Ringinine Oscillation Mechanismobacter Tartaricus C Subunitillus Pseudofirmus Of4 C13 Ring [AQP2](/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-2/) structure reveals locations of mutations causing NDI.
Key sites include: Gln57 (Cd1 [Tc114] Lbdccd Efficiency Mediated Ligand Binding Network In Ligand Bindingturate Binding Mechanismy Beta1 Ar Ligand Free Basal, Ser148 (casein Dgkalglycerol Kinase Zneaercury Ii Chloridelatinum Ii Chlorideotassium Tetrakis Hydroxido Platinate Ii site,
Thr125/Thr126 in loop C near the N-[N Glycosylation Sequon](/xray-mp-wiki/concepts/membrane-mimetics/n-glycosylation-sequon/) Kkrsepsep2P Site Binding Modera Helical Binding Sitee 2 Protease Family Mechanismosteric Site In Nss Transportersiplasmic Drug Binding Site Rndmon Drug Binding Site Atp Synthase C Ringe Directed Spin Labeling Membrane Protein Asn123, and Asp150
in loop D which mediates [Pq Loop Family](/xray-mp-wiki/concepts/protein-families/pq-loop-family/) Loop Receptor Familypetitive Antagonism Cys Loopensitization In Cys Loop Receptorstch Loop Gating Rnd Transporters D-C CamT4L fusion tail via Arg152.
Most NDI-causing Malignant Hyperthermiative Active Gpcr Mutations are in [Autoinhibitory Domains](/xray-mp-wiki/concepts/transport-mechanisms/autoinhibitory-domains/) and cause
misfolding and ER retention.

## Cross-References

- [Human Aquaporin 7 (AQP7)](/xray-mp-wiki/proteins/other-ion-channels/human-aqp7/) — Related protein structure; referenced in text
- [Human Aquaporin 5 (AQP5)](/xray-mp-wiki/proteins/other-ion-channels/human-aqp5/) — Related protein structure; referenced in text
- [MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malG/) — Related protein structure; referenced in text
- [KpBest Bestrophin Ion Channel](/xray-mp-wiki/proteins/other-ion-channels/kpbest/) — Related protein structure; referenced in text
- [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malF/) — Related protein structure; referenced in text
- [Human Aquaporin 2 (AQP2)](/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-2/) — Related protein structure; referenced in text
- [N-Glycosylation Sequon](/xray-mp-wiki/concepts/membrane-mimetics/n-glycosylation-sequon/) — Related concept; referenced in text
- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — Related concept; referenced in text
- [PQ-Loop Family](/xray-mp-wiki/concepts/protein-families/pq-loop-family/) — Related concept; referenced in text
- [Steered Molecular Dynamics (SMD)](/xray-mp-wiki/concepts/methods-techniques/steered-molecular-dynamics/) — Related concept; referenced in text
