---
title: FtsH from Aquifex aeolicus (A. aeolicus AAA Protease)
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [membrane-protein, enzyme, xray-crystallography]
sources: [doi/10.1107##s1399004715005945]
verified: false
---

# FtsH from Aquifex aeolicus (A. aeolicus AAA Protease)

## Overview

FtsH is a universally conserved [ATP]-dependent zinc metalloprotease found in eubacteria,
mitochondria and chloroplasts. It belongs to the AAA+ (ATPases associated with various cellular
activities) family and degrades both membrane-bound and soluble protein substrates. FtsH is a
membrane-anchored hexameric protease where each polypeptide chain contains two N-terminal
transmembrane helices, followed by cytosolic AAA and protease domains. The crystal structure
of a truncated soluble quadruple mutant (Delta-AaFtsH, residues 142-634) from Aquifex aeolicus
was determined in the [ADP]-bound state at 2.96 A resolution (PDB 4ww0), revealing a C2-symmetric
AAA ring arrangement distinct from the Thermotoga maritima FtsH structure. The protease ring
exhibits sixfold symmetry and is identical to other FtsH structures. The AAA domains in a
related crystal form are highly disordered (PDB 4z8x at 3.25 A), highlighting their flexibility.
The active-site switch beta-strand in the protease domain was found to be critical for
proteolytic activity, and a conserved [Glycine] in the linker between [AAA] and protease domains
(Gly399) is essential for FtsH function.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1107##s1399004715005945 | 4WW0 | 2.96 | I222 | Delta-AaFtsH (residues 142-634 with mutations I250M, F360L, K552R, E627G; N-terminal His tag cleaved | [ADP] |
| doi/10.1107##s1399004715005945 | 4Z8X | 3.25 | I222 | Delta-AaFtsH (residues 142-634 with mutations I250M, F360L, K552R, E627G | -- |

## Expression and Purification

- **Expression system**: Escherichia coli BL21 (DE3 CodonPlus
- **Construct**: Truncated A. aeolicus FtsH (residues 142-634 with N-terminal thrombin-cleavable hexahistidine tag. Contains four mutations: I250M, F360L, K552R, E627G
- **Notes**: with 1 mM IptgG at OD600 0.8-1.0, grown overnight at 22 C. Purified by Ni-NTA, Resource Q [Gtacr1] Familylus Plusn Pi Interactionn Channel Gatingn Mediated Ligand Bindingn Ae1 Anion Exchanger-Hdx MsSp Sepharoseton Transport Mechanism, and [Superdex 200] S200 Size Exclusion Chromatographyy-mp-wiki/concepts/[Inducer Exclusion]/ Affinity Chromatographyay-mp-wiki/methods/quality-assessment/[Sec Mals](/xray-mp-wiki/methods/quality-assessment/sec-mals/)/e ChromatographyChromatographyp-wiki/methods/quality-assessment/[FSEC](/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/)y]/. His tag cleaved with [Thrombin Protease](/xray-mp-wiki/reagents/protein-tags/thrombin-protease/) before SEC.

### Purification Workflow

- **Expression system**: E. coli BL21 (DE3 CodonPlus
- **Expression construct**: Delta-AaFtsH (142-634 with N-terminal thrombin-cleavable His tag
- **Tag info**: N-terminal hexahistidine tag, cleaved by thrombin

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press (3 passages at 6.9 MPa | — | 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis [Tris] Propane-HCl pH 8.0, 300 mM NaCl, 0.02% NaN3 | [EDTA]- complete Family Mechanismd Protease Substrate Specificity Quinoline [Msba](/xray-mp-wiki/proteins/abc-transporters/msba/) Inhibitor cocktail added |
| Ni-NTA affinity chromatography | Affinity chromatography | Ni-NTA (Qiagen | 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis [Tris] Propane-HCl pH 8.0, 300 mM NaCl, 0.02% NaN3 | |
| Anion-exchange chromatography | Ion-exchange | Resource Q (GE Healthcare | | |
| His tag cleavage | Thrombin digestion overnight at 4 C | — | | Followed by another Ni-NTA step to remove uncleaved Mladoxinstabilizationtiona5Ama3hapin 1A3 Familyotein Family Family 1obrevin 2 4Protein FamilyntamerProtein Family Yidcov 2 Ctd Agonismotein FamilyKir3 2dral Twinning Mep Protein Familyrome B561 Family Protein Couplinge Binding Proteincholine Binding Proteinopology Architecturetein Nitrosomonas EuropaeaeCytoplasmic Poreree Protein Synthesischromatium Tepidum Hipipaeodactylum TricornutumGas Anaesthetic MechanismNetworks Membrane Protein Oligomerizationne Protein Crystals For Neutron Diffractionirected Spin Labeling Membrane ProteinAtom Derivative Detergents And Lipids and tag |
| Size-exclusion chromatography | SEC | Superdex S200 16/600 (GE Healthcare | 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis [Tris] Propane-HCl pH 8.0, 100 mM NaCl, 0.02% NaN3 | |

## Crystallization

### doi/10.1107##s1399004715005945

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop |
| Protein sample | -AaFtsH at 10 mg/mL in 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis Tris Propane-HCl pH 8.0, 100 mM NaCl |
| Reservoir | 0.2 M CaCl2, 0.1 M MES pH 6.0, 20% Pegg 6000 |
| Temperature | 20 C |
| Growth time | Not specified (|
| Notes | Crystals of form X1 appeared initially. After several months, smaller of form X2 (shrunken c-axis appeared alongside. MscS X2 has ordered [AAA] [Autoinhibitory Domains](/xray-mp-wiki/concepts/transport-mechanisms/autoinhibitory-domains/). |

## Biological / Functional Insights

### C2-symmetric AAA ring with ADP-bound state

The AAA domains assemble into a ring with C2 symmetry, in contrast to the sixfold symmetry
of the protease ring. The breakdown of arises from different interdomain angles
 the protease and AAA domains in the [Trex1] crystallographically independent monomers.
The [Autoinhibitory Domains](/xray-mp-wiki/concepts/transport-mechanisms/autoinhibitory-domains/) move as rigid bodies by ~30 degrees rotation, with the [Glycine]e Gating Hinge](/xray-mp-wiki/concepts/transport-mechanisms/glycine-gating-hinge/) around residues
400-410 in the M4M Linker Interaction Motif. Unlike the T. maritima FtsH structure where 6r An Swappingphorin AtbEcdel GatingCov 2 CtdC Luminal Domain Receptor4 Glun2B Atdal Core Diseasehydrogenase Dii Domainomain Activation Mechanism Ae1 Anion Exchanger Domain Motion In P Type Atpasesnduced Domain Rearrangement P Type Atpases rotations are
mainly perpendicular to the Family Mechanismd Protease Substrate Specificity ring (closure, the A. aeolicus FtsH shows more lateral
(twisting movements, resulting in a qualitatively different [AAA] 6Mr Six Carbon Ring Retinalrulina Platensis C15 Ringrae V Atpase K Ringst Atp Synthase C10 Ringoroplast Atp Synthase C Ringobacter Tartaricus C Subunitillus Pseudofirmus Of4 C12 Ringnach Chloroplast C14 Rotor Ringillus Pseudofirmus Of4 C13 Ringst Mitochondrial Atp Synthase C10 Ringmon Drug Binding Site Atp Synthase C Ring arrangement.

### Closed pore and contiguous phenylalanine path

The [Central Core Disease](/xray-mp-wiki/concepts/signaling-receptors/central-core-disease/) pore in the A. aeolicus FtsH structure is completely closed. The pore
L Phenylalaninel Gating residues (Phe228, part of the [Conserved Core Triad](/xray-mp-wiki/concepts/signaling-receptors/conserved-core-triad/) 228FGV Gxxxg motifMotif5 Linker Interaction Motif Substrate Recognition Gmg Motif are partially disordered
but line a contiguous funnel-shaped path. Compared to the T. maritima FtsH structure, the
aromatic Entry Ion Conduction Pathway chains are more buried inside the cleft, and Cry6Aaabce Forming Toxinsed Pore Mechanisming Pore Currentae1P Sodium Channelm Pore Modulek1 Cytoplasmic Poreha Helical Pore Forming Toxin Family contacts are tighter.

### Active-site switch beta-strand is critical for proteolytic activity

A [Conserved Core Triad](/xray-mp-wiki/concepts/signaling-receptors/conserved-core-triad/) Gs Betaar B3an Beta1 Ara Arrestin Signalingkey Beta1 Ar M23a1 Adrenergic Receptora2 Adrenergic Receptoran Beta 2 Adrenergic Receptorkey Beta1 Ar M23 2Vt4key Beta1 Ar Ligand Free Basal-strand (the active-site Loop Gating Rnd Transporters covering the Ntsr1 ElActive Conformation041 Active Enantiomeritutive Active Gpcr Mutationscillus Thermodenitrificans SecyeActive State High Affinity Agonist Binding-Kkrsepsep2Pra Helical Binding Sitee 2 Protease Family Mechanismosteric Site In Nss Transportersiplasmic Drug Binding Site Rndmon Drug Binding Site Atp Synthase C Ringe Directed Spin Labeling Membrane Protein Gs Alphabc Alpha3ine Receptor Alpha3n Alpha4Beta2 Nicotinic Receptora 1B Adrenergic Receptora Helical Pore Forming Toxin Family-helix is
disordered in all Trex1in Swapping copies of the A. aeolicus FtsH structure. This segment functions as
an edge strand for Tat A SubstrateBinding Pockete Binding In Asbt Yfe Protonation Coupling Protease Substrate Specificitysporter Substrate Specificitystrate Recognition Gmg Motifly Substrate Specificitye Polyspecificity Smr Transporters Protein Insertase Substrate Exit Gate [S1I8] Fsce 5hte Binding Modeichia Coli SppaGly 3M3Sh Malodour Precursor [Molecular Docking](/xray-mp-wiki/methods/structure-determination/molecular-docking/). The T450P mutation in this segment within the []-[Glu](/xray-mp-wiki/proteins/other-ion-channels/gluN1-gluN2b-nmda-receptor/) FtsH severely impaired proteolytic activity while retaining ATPase [Trex1] Rnase Activitynstitutive Activity,
confirming its functional importance. The lid-Gxxxg motif Helix Mechanism interpretation in the T. thermophilus
FtsH structure is problematic due to Recoil Desensitization bias and flawed Refinement data.

### Conserved glycine in AAA-protease linker is essential

An absolutely [Conserved Core Triad](/xray-mp-wiki/concepts/signaling-receptors/conserved-core-triad/) [Glycine] residue (Gly399 in A. aeolicus and T. thermophilus FtsH
in the M4M Linker Interaction Motif the [AAA] and Family Mechanismd Protease Substrate Specificity [Autoinhibitory Domains](/xray-mp-wiki/concepts/transport-mechanisms/autoinhibitory-domains/) is crucial for FtsH activity.
The G399L mutation in T. thermophilus FtsH causes the Mladoxinstabilizationtiona5Ama3hapin 1A3 Familyotein Family Family 1obrevin 2 4Protein FamilyntamerProtein Family Yidcov 2 Ctd Agonismotein FamilyKir3 2dral Twinning Mep Protein Familyrome B561 Family Protein Couplinge Binding Proteincholine Binding Proteinopology Architecturetein Nitrosomonas EuropaeaeCytoplasmic Poreree Protein Synthesischromatium Tepidum Hipipaeodactylum TricornutumGas Anaesthetic MechanismNetworks Membrane Protein Oligomerizationne Protein Crystals For Neutron Diffractionirected Spin Labeling Membrane ProteinAtom Derivative Detergents And Lipids to elute exclusively as a
monomer and eliminates both ATPase and proteolytic [Trex1] Rnase Activitynstitutive Activity. This Glycinee Betaine GlycineGlyt1lpha3e Gating Hingee Receptor Alpha3 provides
necessary flexibility for interdomain communication.

## Cross-References

- [Bovine F1-ATPase (azide-inhibited form)](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — Related protein structure; referenced in text
- [Bovine Mitochondrial F1-ATPase-Stator Complex (Membrane Extrinsic Region)](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase-stator-complex/) — Related protein structure; referenced in text
- [GluN1-GluN2B NMDA Receptor (Xenopus laevis, Full-Length)](/xray-mp-wiki/proteins/other-ion-channels/gluN1-gluN2b-nmda-receptor/) — Related protein structure; referenced in text
- [GtACR1 Anion Channelrhodopsin from Guillardia theta] — Related protein structure; referenced in text
- [E. coli MscS (Mechanosensitive Channel of Small Conductance)](/xray-mp-wiki/proteins/voltage-gated-channels/mscs/) — Related protein structure; referenced in text
- [MsbA Lipid A Flippase](/xray-mp-wiki/proteins/abc-transporters/msba/) — Related protein structure; referenced in text
- [E. coli MscS Mechanosensitive Channel (A106V Open Form)](/xray-mp-wiki/proteins/voltage-gated-channels/mscs-a106v/) — Related protein structure; referenced in text
- [Mouse TREX1 (Three Prime Repair Exonuclease 1)] — Related protein structure; referenced in text
- [Rocker — De Novo Designed Zn²⁺ Transporter] — Related protein structure; referenced in text
- [Inducer Exclusion] — Related concept; referenced in text
