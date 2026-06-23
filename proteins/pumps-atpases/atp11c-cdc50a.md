---
title: ATP11C-CDC50A (Human Plasma Membrane Phospholipid Flippase)
created: 2020-06-03
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.RA120.014144]
verified: false
---

# ATP11C-CDC50A (Human Plasma Membrane Phospholipid Flippase)

## Overview

ATP11C is a member of the P4-ATPase family that functions as an aminophospholipid-specific
flippase at the plasma membrane, translocating [Phosphatidylserine](/xray-mp-wiki/reagents/lipids/phosphatidylserine/) (PtdSer) and
[Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) (PtdEtn) from the outer to the inner leaflet. ATP11C forms a
functional complex with the accessory subunit CDC50A, which is required for correct
localization and functional expression. The crystal structure of the human ATP11C-CDC50A
complex was determined in a stabilized outward-open E2P conformation at 3.9 A resolution
(PDB 6LKN), using beryllium fluoride (BeFx) as a phosphate analog to trap the E2P state.
The structure reveals a deep longitudinal crevice along transmembrane helices continuous
from the exoplasmic surface to a PtdSer occlusion site at the unwound part of TM4
(PVSM motif). Two extra electron densities, most likely bound PtdSer molecules, were
identified: one at the canonical occlusion site near the PVSM motif and another in an
exoplasmic cavity formed by the TM3-4 loop of ATP11C and the CDC50A exoplasmic domain.
The crevice is the conduit along which PtdSer traverses from the outer leaflet to its
occlusion site, resolving the "giant substrate problem" of how large phospholipid head
groups are translocated across the membrane. The structure also reveals three caspase
recognition sites on the N domain that mediate inactivation during apoptosis.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1074##jbc.RA120.014144 | 6LKN | 3.9 | P 21 21 21 | Human ATP11C (DeltaN7, DeltaC38 with N-terminal Flag-His6-EGFP-TEV tag; CDC50A (N190Q, S292W double mutant, deglycosylated | BeFx (beryllium Alf42milyay-mp-wiki/reagents/additives/[KF](/xray-mp-wiki/reagents/additives/potassium-fluoride/)/oride Channeloride Channel, [ADP](/xray-mp-wiki/reagents/ligands/adp/), PtdSer (2 molecules modeled, [DOPC](/xray-mp-wiki/reagents/lipids/dopc/) |

## Expression and Purification

- **Expression system**: BacMam system in Expi293 cells (mammalian
- **Construct**: Human ATP11C (DeltaN7, DeltaC38 with N-terminal Flag-His6-EGFP-TEV tag; human CDC50A with N190Q/S292W mutations
- **Notes**: Both [Glun1B Glun2B Atd](/xray-mp-wiki/proteins/other-ion-channels/gluN1b-gluN2b-atd/) Atpase Subunits D F Scdf co-expressed; CDC50A [Deer Spectroscopy](/xray-mp-wiki/methods/quality-assessment/deer-spectroscopy/) [Ntsr1 Lf](/xray-mp-wiki/proteins/gpcr/ntsr1-lf/) N64A K294A1A E309Q1A E340A El Delta Ic3A195 Glt Phpsin N2C D282C Mutant Rhodopsin E113Q M257Yenza A M2 Proton Channel S31Ny Beta1 Ar M23 2Vt4 regulates [N Glycosylation Sequon](/xray-mp-wiki/concepts/n-glycosylation-sequon/) for improved [Single Crystal Microspectrophotometry](/xray-mp-wiki/methods/structure-determination/single-crystal-microspectrophotometry/) quality
- **Induction**: [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)-Anion Mediated Ligand Bindingdulation Gabab Receptor Paracellular Ion Selectivity [Glnk](/xray-mp-wiki/proteins/other-ion-channels/glnk/) Family, 48 h at 31.5C

### Purification Workflow

- **Expression system**: Expi293 cells (BacMam system
- **Expression construct**: ATP11C (DeltaN7, DeltaC38 with N-terminal Flag-His6-EGFP-TEV; CDC50A with N190Q/S292W
- **Tag info**: N-terminal Flag-His6-EGFP-TEV tag on ATP11C; removed by TEV protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and solubilization | Direct detergent solubilization | — | 40 mM [MES](/xray-mp-wiki/reagents/buffers/mes/)/TrisPs Hclfer Trisfer Bis [Tris](/xray-mp-wiki/reagents/buffers/tris/) Propane pH 6.5, 200 mM NaCl, 2 mM Mg(CH3COO2, 1 mM [ATP](/xray-mp-wiki/reagents/ligands/atp/), 1 mM DTTT, 0.1 mM [Egta](/xray-mp-wiki/reagents/additives/egta/), ClppPn ProteaseProteased Proteaseoteasession Proteaseubstratetease MechanismCyto Aeolicus Ftshchia Coli SppaProtease Family Mechanismd Protease Substrate Specificity C3361noline Msba Inhibitor Pyridylpiperazine Epitial Quinoline Msba Inhibitorimized Quinoline [Msba](/xray-mp-wiki/proteins/abc-transporters/msba/) Inhibitor cocktail + 1.5% (w/v n-decyl-beta-D-maltoside (DM | Harvested [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) solubilized on ice for 20 min; insoluble material removed at 200,000g for 1 h |
| Affinity chromatography | Anti-Flag M2 affinity chromatography | Anti-Flag M2 affinity resin (Sigma-Aldrich | 20 mM [MES](/xray-mp-wiki/reagents/buffers/mes/)/TrisPs Hclfer Trisfer Bis [Tris](/xray-mp-wiki/reagents/buffers/tris/) Propane pH 6.5, 200 mM NaCl, 2 mM Mg(CH3COO2, 1 mM [ATP](/xray-mp-wiki/reagents/ligands/atp/), 1 mM DTTT, 0.1% DMMMM + 0.1% DM | Wash with 20 CV HepeseteteHclr Chesr Hepesr Glyciner Acetater Succinater Mesm Citrater Bis [Tris](/xray-mp-wiki/reagents/buffers/tris/) Propane; elute with Flag [S1I8](/xray-mp-wiki/reagents/ligands/s1i8/) Fsce 5hte Binding Modeichia Coli SppaGly 3M3Sh Malodour Precursor |
| TEV protease cleavage | Tag removal | — |  | Flag-His6-EGFP tag removed by TEV ClppPn ProteaseProteased Proteaseoteasession Proteaseubstratetease MechanismCyto Aeolicus Ftshchia Coli SppaProtease Family Mechanismd Protease Substrate Specificity |
| Size-exclusion chromatography | SEC | Not specified | 20 mM [MES](/xray-mp-wiki/reagents/buffers/mes/)/TrisPs Hclfer Trisfer Bis [Tris](/xray-mp-wiki/reagents/buffers/tris/) Propane pH 6.5, 50 mM NaCl, 5 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 1 mM DTTT, 0.1% C12E88 + 0.1% C12E8 | Final polishing step; Mladoxinstabilizationa5Ama3hapin 1A3 Familyotein Family Family 1obrevin 2 4Protein FamilyntamerProtein Family Yidcov 2 Ctd Agonismotein FamilyKir3 2dral Twinning Mep Protein Familyrome B561 Family Protein Couplinge Binding Proteincholine Binding Proteinopology Architecturetein Nitrosomonas EuropaeaeCytoplasmic Poreree Protein Synthesischromatium Tepidum Hipipaeodactylum TricornutumGas Anaesthetic MechanismNetworks Membrane Protein Oligomerizationne Protein Crystals For Neutron Diffractionirected Spin Labeling Membrane ProteinAtom Derivative Detergents And Lipids concentrated for TruncationllizationlizationPhasellizationimerizationPhase Crystallizationstallization Under OilLysozyme Fusionization Free Interface Diffusion |
| Deglycosylation | Endoglycosidase treatment | — |  | Treated with [Endoh](/xray-mp-wiki/reagents/additives/endoh/) to remove excess glycans; Secyserved Core Triadtral Core Diseasere Core Complex Assembly GlcNAc moieties retained for [Single Crystal Microspectrophotometry](/xray-mp-wiki/methods/structure-determination/single-crystal-microspectrophotometry/) [Gxxxg Motif](/xray-mp-wiki/concepts/gxxxg-motif/) Side Chain Packing |
| Lipidation | HiLiDe method | — |  | Protein mixed with [DOPC](/xray-mp-wiki/reagents/lipids/dopc/) and DOPS at Msbad Aem16oc 17 4mem16ptactive Lipid Binding3 Lipid Transport Mechanisme From Lipid Principle Ta Thermosiphon Africanus-to-protein ratio of 0.2; C12E88 added at 0.5-2.0 Mladoxinstabilizationtiona5Ama3hapin 1A3 Familyotein Family Family 1obrevin 2 4Protein FamilyntamerProtein Family Yidcov 2 Ctd Agonismotein FamilyKir3 2dral Twinning Mep Protein Familyrome B561 Family Protein Couplinge Binding Proteincholine Binding Proteinopology Architecturetein Nitrosomonas EuropaeaeCytoplasmic Poreree Protein Synthesischromatium Tepidum Hipipaeodactylum TricornutumGas Anaesthetic MechanismNetworks Membrane Protein Oligomerizationne Protein Crystals For Neutron Diffractionirected Spin Labeling Membrane ProteinAtom Derivative Detergents And Lipids:[Tween 20](/xray-mp-wiki/reagents/detergents/tween-20/) ratio; incubated overnight at 4C |

**Final sample**: 10 mg/ml in 20 mM MES/Tris pH 6.5, 50 mM NaCl, 5 mM MgCl2, 1 mM ADP, 0.5 mM BeSO4, 1.5 mM NaF, 0.1 mg/ml DOPS


## Crystallization

### doi/10.1074##jbc.RA120.014144

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop |
| Protein sample | 10 mg/ml lipidated ATP11C-CDC50A in 20 mM MES/TrisPs Hclfer Trisfer Bis Tris Propane pH 6.5, 50 mM NaCl, 5 mM Mgcl2, 1 mM ADP, 0.5 mM BeSO4, 1.5 mM NaF, 0.1 mg/ml DOPS |
| Reservoir | 10% (v/v GlycerolColil 3 Phosphatel Facilitator, 14-17% Pegg 4000, 0.4 M MgSO4, 2-5 mM Gs Betaar B3a Mercaptoethanolay-mp-wiki/proteins/human-beta1-ar/a Arrestin Signalingkey Beta1 Ar M23a1 Adrenergic Receptora2 Adrenergic Receptoran Alpha4Beta2 Nicotinic Receptoran Beta 2 Adrenergic Receptorkey Beta1 Ar M23 2Vt4key Beta1 Ar Ligand Free Basal-mercaptoethanol |
| Temperature | 20C |
| Growth time | 2 weeks (thin plate-Glp1Rbkorlinge Injection Mechanism Like Displacement Mechanism Diffractive Imaging Imperfect Crystalse Protein Crystals For Neutron Diffraction, 800 x 500 x 50 um |
| Cryoprotection | 10% glycerol, 14-17% PEG 4000, 0.4 M MgSO4, 4 mg/ml DOPS, 20 mM MES/Tris pH 6.5, 50 mM NaCl, 5 mM MgCl2, 5 mM BME, 2% C12E8, 1 mM ADP, 0.5 mM BeSO4, 1.5 mM NaF |
| Notes | DOPS (4 mg/ml in harvest solution was critical for preserving [Single Crystal Microspectrophotometry](/xray-mp-wiki/methods/structure-determination/single-crystal-microspectrophotometry/) quality; data from 1,588 crystals merged; collected at Horizontal Helix Spring Mechanismpic Spring Mechanism-8 beamlines BL32XU, BL41XU, BL45XU; Helical Recoil DesensitizationHelical Pore Forming Toxin Familyne Protein Insertase Substrate Exit Gateirected Spin Labeling Membrane Protein scan method used for Msclsclscl Gating Mechanisme Domain Motion In P Type Atpases Diffractive Imaging Imperfect Crystalse Protein Crystals For Neutron Diffraction |


## Biological / Functional Insights

### Outward-open E2P conformation with phospholipid conduit

The ATP11C [Structure Based Antipsychotic Design](/xray-mp-wiki/concepts/structure-based-antipsychotic-design/) reveals a deep longitudinal crevice formed by TM2, TM4, and
TM6 helices, continuous from the exoplasmic [Surface Hydroxyl Acidity](/xray-mp-wiki/concepts/surface-hydroxyl-acidity/) to the PtdSer [Cork In Bottle Occlusion](/xray-mp-wiki/concepts/cork-in-bottle-occlusion/) Kkrsepsep2P Site Binding Modera Helical Binding Sitee 2 Protease Family Mechanismosteric Site In Nss Transportersiplasmic Drug Binding Site Rndmon Drug Binding Site Atp Synthase C Ring
in the middle of the Cuscjmray-mp-wiki/proteins/wza/ 1ocessing4Yidce Mimeticsric Regulation Like Mechanismve Lipid BindingCenter Mechanismpology ArchitectureSide Chain PackingCoupling Mechanismee Protein Synthesise1 Anion Exchangerponent Signaling Systemas Anaesthetic Mechanismupported Membrane ElectrophysiologyF1 Atpase Stator Complexetworks Membrane Protein Oligomerizatione Protein Crystals For Neutron Diffractionrected Spin Labeling Membrane Proteintom Derivative Detergents And Lipids. TM2 is kinked at Pro94 ([Conserved Core Triad](/xray-mp-wiki/concepts/conserved-core-triad/) in all mammalian
P4-ATPases, enabling a wide and [Continuous Diffraction](/xray-mp-wiki/concepts/continuous-diffraction/) crevice. The P94A mutation significantly
reduces apparent Talony Chromatographytive State High Affinity Agonist Binding for both PtdSer and PtdEtn, confirming the TM2 kink is key
for [Nbd Phospholipid Scrambling Assay](/xray-mp-wiki/methods/quality-assessment/nbd-phospholipid-scrambling-assay/) passage.

### Two PtdSer binding sites on the transport pathway

Two extra Cryo Emectroscopy densities, most likely DltbhhReceptor Bosentann 5 Ht2B Receptort Atp Synthase C10 Ringn Endothelin Etb Receptor Et1rnating Ion Bound Configurations PtdSer, were identified: one at the
canonical occlusion site near the unwound part of TM4 (PVSM Gxxxg Motifega MotifMotif5 Linker Interaction Motif Substrate Recognition Gmg Motif, residues 356-359
and another in an exoplasmic cavity formed by the TM3-4 [Pq Loop Family](/xray-mp-wiki/concepts/pq-loop-family/) Loop Receptor Familypetitive Antagonism Cys Loopensitization In Cys Loop Receptorstch Loop Gating Rnd Transporters of ATP11C and the CDC50A
exoplasmic Mlabd1pry1epeat12 LbdDomainDomain6r An Swappingphorin AtbEcdel GatingCov 2 CtdC Luminal Domaing Cyto Receptor4 Cterm CamB Glun2B Atdal Core Diseasehydrogenase Dii Domainomain Activation Mechanism Ae1 Anion Exchanger Domain Motion In P Type Atpasesnduced Domain Rearrangement P Type Atpases. The exoplasmic cavity is highly hydrophilic with basic residues from
both ATP11C and CDC50A, suggesting it serves as the [G592 Initial Quinoline Msba Inhibitor](/xray-mp-wiki/reagents/ligands/g592-initial-quinoline-msba-inhibitor/)p-wiki/proteins/msba/) Inhibitor PtdSer recruitment site
from the outer leaflet. The cavity site is connected to the longitudinal crevice,
providing a complete Channel 4thwaylease Pathwayry Malodour Production Pathwayntry Ion Conduction Pathway for PtdSer from the [Cusc](/xray-mp-wiki/proteins/abc-transporters/cusC/) leaflet to the [Cork In Bottle Occlusion](/xray-mp-wiki/concepts/cork-in-bottle-occlusion/) Kkrsepsep2P Site Binding Modera Helical Binding Sitee 2 Protease Family Mechanismosteric Site In Nss Transportersiplasmic Drug Binding Site Rndmon Drug Binding Site Atp Synthase C Ringe Directed Spin Labeling Membrane Protein.

### E2P state trapped by beryllium fluoride

BeFx forms a covalent [Dsbb](/xray-mp-wiki/proteins/enzymes/dsbB/) Barrier Hydrogen Bond with the invariant L Aspartateatellosteric Mechanism (Asp409 in the DKTG signature
sequence, which is covered by the DGES/T Gxxxg Motifega MotifMotif5 Linker Interaction Motif Substrate Recognition Gmg Motif on the A domain to prevent spontaneous
dephosphorylation. The N domain is segregated from the P Mlabd1pry1epeat12DomainDomain6r An Swappingphorin AtbEcdel GatingCov 2 CtdC Luminal Domaing Cyto ReceptorB Glun2B Atdal Core Diseasehydrogenase Dii Domainomain Activation Mechanism Ae1 Anion Exchanger Domain Motion In P Type Atpasesnduced Domain Rearrangement P Type Atpases and relatively flexible.
The overall [Nb N00](/xray-mp-wiki/reagents/antibodies/nb-n00/) Conformationve Conformationed Conformationomophore Conformationng Conformationing Conformation of the A and P [Autoinhibitory Domains](/xray-mp-wiki/concepts/autoinhibitory-domains/) is close to those in Drs2p and ATP8A1
E2P [Squid Rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) Conformational States Clc. The [Thermal Shift Assay](/xray-mp-wiki/methods/quality-assessment/thermal-shift-assay/) stability of the BeFx-PtdSer DltbhhReceptor Bosentann 5 Ht2B Receptort Atp Synthase C10 Ringn Endothelin Etb Receptor Et1rnating Ion Bound Configurations Ton ComplexcComplexpdc ComplexTSecretase Complexb1 BrilTccc3pinachBtuf ComplexB Complex Cterm Camgc Complex Release Complexs Acidophila Molischianum Spoiiah ComplexCore Complex Assemblyg Pseudomonas Aeruginosaght Harvesting Complex Ii F1 Atpase Efrapeptin Complexh Light Harvesting Complex IiEndothelin Etb Receptor [Irl2500](/xray-mp-wiki/reagents/ligands/irl2500/) F1 Atpase Stator Complex (Tm = 53.5C is
markedly higher than in the absence of either [Tc114](/xray-mp-wiki/reagents/ligands/tc114/) Lbdccd Efficiencyite Binding Mode Mediated Ligand Binding Network In Ligand Bindingturate Binding Mechanismy Beta1 Ar Ligand Free Basal.

### Caspase inactivation sites mapped on the N domain

Trex1 caspase-Slc6 Substrate Recognition Gmg Motifrecursor Recognition Pot sites (sites I-[Gold Iii Chloride](/xray-mp-wiki/reagents/additives/gold-iii-chloride/)balt Hexamine](/xray-mp-wiki/reagents/additives/cobalt-hexamine/) on the N domain of ATP11C mediate
irreversible C Type Inactivationnel Inactivation Gating during apoptosis. Sites I and Zneaercury Ii Chloridelatinum Ii Chlorideotassium Tetrakis Hydroxido Platinate Ii are clustered at the
N-terminal side of an Gs Alphabc Alpha3ine Receptor Alpha3n Alpha4Beta2 Nicotinic Receptora 1B Adrenergic Receptora Helical Pore Forming Toxin Family-helix, while Kkrsepsep2Pe 2 Protease Family Mechanismosteric Site In Nss Transporters Gold Iii Chloridebalt Hexamine is at the C-[N Terminal T4 Lysozyme Fusion](/xray-mp-wiki/concepts/n-terminal-t4-lysozyme-fusion/)i/reagents/protein-tags/t4-lysozyme/) Fusion Apolar Side Chain Packinge Entry Ion Conduction Pathway. This
helix acts as a [Membrane Mimetics](/xray-mp-wiki/concepts/membrane-mimetics/) bolt for N domain folding. [Si Face Cleavage](/xray-mp-wiki/concepts/si-face-cleavage/) at both ends of this
Gxxxg Motifing Helix Mechanismx Shift Mechanismzontal Helix Spring Mechanism by caspase-3 dimers (distance ~35-40 A [Conformational Coupling Gating](/xray-mp-wiki/concepts/conformational-coupling-gating/) [Site Directed Spin Labeling Membrane Protein](/xray-mp-wiki/concepts/site-directed-spin-labeling-membrane-protein/) leads to N Mlabd1pry1epeat12Domain6r An Swappingphorin AtbEcdel GatingCov 2 CtdC Luminal Domaing Cyto Receptor4 Cterm CamB Glun2B Atdal Core Diseasehydrogenase Dii Domainomain Activation Mechanism Ae1 Anion Exchanger Domain Motion In P Type Atpasesnduced Domain Rearrangement P Type Atpases
[Gas Phase Unfolding](/xray-mp-wiki/methods/quality-assessment/gas-phase-unfolding/), preventing [ATP](/xray-mp-wiki/reagents/ligands/atp/) Fkbp12Lbdomaing Change Mechanismte Binding Modee Binding PocketHelical Binding Sitee Binding Proteinate Binding In Asbt Yfive Lipid Bindingcholine Binding Proteinc Glycoside Binding MechanismMediated Ligand Bindingxtended Binding Pocket Modifier Toxin Bindingoprotein Induced Fit BindingNetwork In Ligand Bindingasmic Drug Binding Site Rndurate Binding Mechanismaeodactylum TricornutumGas Anaesthetic Mechanism Drug Binding Site Atp Synthase C Ringctive State High Affinity Agonist Bindingendent Quinone Binding Reaction Center and [Pglk](/xray-mp-wiki/proteins/abc-transporters/pglk/) Thermosiphon Africanus [Trex1](/xray-mp-wiki/proteins/gpcr/trex1/) Rnase Activitynstitutive Activity.

### Cytoplasmic gate formed by Val357 and Val98

The transport conduit ends at Val357 in the PVSM Gxxxg Motifega MotifMotif5 Linker Interaction Motif Substrate Recognition Gmg Motif, which forms a [Cpe Induced Tight Junction Disassembly](/xray-mp-wiki/concepts/cpe-induced-tight-junction-disassembly/) seal
with Val98 on its Ec Cor Aoplasmic Pore side, preventing PtdSer head group penetration to the
cytoplasm in the [Abc Transporter Outward Occluded Mechanism](/xray-mp-wiki/concepts/abc-transporter-outward-occluded-mechanism/)-Inward Facing Conformationrd Facing Conformation E2P [Phosphoenzyme E2P State](/xray-mp-wiki/concepts/phosphoenzyme-e2p-state/) Adapted Statet Adapted State Return State Mechanismey Beta1 Ar Ligand Free Basal. The Val357Ile [Ntsr1 Lf](/xray-mp-wiki/proteins/gpcr/ntsr1-lf/) N64A K294A1A E309Q1A E340A El Delta Ic3A195 Glt Phpsin N2C D282C Mutant Rhodopsin E113Q M257Yenza A M2 Proton Channel S31Ny Beta1 Ar M23 2Vt4 (isoleucine is more
[Common Drug Binding Site Atp Synthase C Ring](/xray-mp-wiki/concepts/common-drug-binding-site-atp-synthase-c-ring/) in other P4-ATPases shows reduced apparent Talony Chromatographytive State High Affinity Agonist Binding for PtdSer and PtdEtn but
near-[Normal Mode Xray Refinement](/xray-mp-wiki/methods/structure-determination/normal-mode-xray-refinement/) transport [Trex1](/xray-mp-wiki/proteins/gpcr/trex1/) Rnase Activitynstitutive Activity, while Val357Ala and Val357Phe significantly impair
both ATPase and Pbga4 Interaction Complexpin TransportLike Mechanismermus Thermophilusift Mechanismpid Transport Mechanismon Transport Mechanismnformational States Clc activities, demonstrating the importance of specific [Side Entry Ion Conduction Pathway](/xray-mp-wiki/concepts/side-entry-ion-conduction-pathway/)
[Proton Wire](/xray-mp-wiki/concepts/proton-wire/) And Chain Modelar Side Chain Packing Sec Malse Exclusion ChromatographyC at the Ag Sf Couplingckering Gate Mechanismon Channel Gatingformational Coupling Gatingbrane Protein Insertase Substrate Exit Gate position.

### Distinct crevice conformation compared to Drs2p and ATP8A1

The crevice in ATP11C is [Continuous Diffraction](/xray-mp-wiki/concepts/continuous-diffraction/) and wider than in the Aqy1t Atm1t V1 Atpaset Adp Atp Carriert F1 Atpaset V Atpase Subunits D F Scdft F1C10 Atp Synthase Subcomplext Mitochondrial Atp Synthase C10 Ring Drs2p E2P PAR1ray-mp-wiki/proteins/[Par2](/xray-mp-wiki/proteins/gpcr/par2/)/
[Mscs](/xray-mp-wiki/proteins/voltage-gated-channels/mscs/)s A106V](/xray-mp-wiki/proteins/voltage-gated-channels/mscs-a106v/), and contrasts with the ATP8A1 E2P [Phosphoenzyme E2P State](/xray-mp-wiki/concepts/phosphoenzyme-e2p-state/) Adapted Statet Adapted State Return State Mechanismey Beta1 Ar Ligand Free Basal Active State High Affinity Agonist Binding where no Cuscjmray-mp-wiki/proteins/wza/ 1ocessing4Yidcric Regulation Like Mechanismve Lipid BindingCenter Mechanismpology ArchitectureSide Chain PackingCoupling Mechanismee Protein Synthesisponent Signaling Systemas Anaesthetic Mechanismupported Membrane ElectrophysiologyF1 Atpase Stator Complexetworks Membrane Protein Oligomerizatione Protein Crystals For Neutron Diffractionrected Spin Labeling Membrane Proteintom Derivative Detergents And Lipids crevice is formed
(exoplasmic Ag Sf Couplingckering Gate Mechanismon Channel Gatingformational Coupling Gatingbrane Protein Insertase Substrate Exit Gate substantially closed. This difference is attributed to the longer
C-[N Terminal T4 Lysozyme Fusion](/xray-mp-wiki/concepts/n-terminal-t4-lysozyme-fusion/)i/reagents/protein-tags/t4-lysozyme/) Fusion Trkaay-mp-wiki/proteins/[Ktra](/xray-mp-wiki/proteins/pumps-atpases/ktra/)/ay-mp-wiki/proteins/[Sbtb](/xray-mp-wiki/proteins/slc-transporters/sbtb/)/ Mlabd1pry1epeat12 LbdDomainDomain6r An Swappingphorin AtbEcdel GatingCov 2 CtdC Luminal Domaing Cyto Receptor4 Cterm Camal Core Diseasehydrogenase Dii Domainomain Activation Mechanism Ae1 Anion Exchanger Domain Motion In P Type Atpasesnduced Domain Rearrangement P Type Atpases in ATP8A1 (~38 Leutct1Qn21B Glun2B Atdo Methoxy IsocoumarinSuperfamily acids compared to ATP11C. The
PtdSer-bound ATP11C E2P structure provides direct [Membrane Mimetics](/xray-mp-wiki/concepts/membrane-mimetics/) evidence for the proposed
phospholipid conduit that was only inferred from the Drs2p [Structure Based Antipsychotic Design](/xray-mp-wiki/concepts/structure-based-antipsychotic-design/) (without DltbhhReceptor Bosentann 5 Ht2B Receptort Atp Synthase C10 Ringn Endothelin Etb Receptor Et1rnating Ion Bound Configurations
[Nbd Phospholipid Scrambling Assay](/xray-mp-wiki/methods/quality-assessment/nbd-phospholipid-scrambling-assay/).

### Substrate specificity determinants at the occlusion site

Phe354 in ATP11C (replaced by Asn in ATP8A1, ATP8A2, and Drs2p contributes to
PtdSer/PtdEtn [Rhomboid Protease](/xray-mp-wiki/concepts/rhomboid-protease/) Substrate Specificityorter Substrate Specificity Substrate Specificity. The Phe354Asn [Ntsr1 Lf](/xray-mp-wiki/proteins/gpcr/ntsr1-lf/) N64A K294A1A E309Q1A E340A El Delta Ic3A195 Glt Phpsin N2C D282C Mutant Rhodopsin E113Q M257Yenza A M2 Proton Channel S31Ny Beta1 Ar M23 2Vt4 shows significantly higher affinity
for both PtdSer and PtdEtn, suggesting a hydrophilic [Side Entry Ion Conduction Pathway](/xray-mp-wiki/concepts/side-entry-ion-conduction-pathway/) [Proton Wire](/xray-mp-wiki/concepts/proton-wire/) And Chain Modelar Side Chain Packing at this position
is favorable for aminophospholipid head group accommodation. Residues Val98, Phe72,
Asn881, and Asn912 discriminate [Conformational Coupling Gating](/xray-mp-wiki/concepts/conformational-coupling-gating/) PtdSer and PtdEtn, with D Alanineine mutants
showing increased apparent affinity for PtdSer but decreased Talony Chromatographytive State High Affinity Agonist Binding for PtdEtn.


## Cross-References

- [Squid Rhodopsin (Primary Photochemical Reaction States)](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) — Related protein structure; referenced in text
- [PglK ABC Flippase](/xray-mp-wiki/proteins/abc-transporters/pglk/) — Related protein structure; referenced in text
- [NTSR1-LF Mutant](/xray-mp-wiki/proteins/gpcr/ntsr1-lf/) — Related protein structure; referenced in text
- [CusC Outer Membrane Channel](/xray-mp-wiki/proteins/abc-transporters/cusC/) — Related protein structure; referenced in text
- [GlnK PII Signal Transduction Protein (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glnk/) — Related protein structure; referenced in text
- [MsbA Lipid A Flippase](/xray-mp-wiki/proteins/abc-transporters/msba/) — Related protein structure; referenced in text
- [E. coli MscS (Mechanosensitive Channel of Small Conductance)](/xray-mp-wiki/proteins/voltage-gated-channels/mscs/) — Related protein structure; referenced in text
- [Human Protease-Activated Receptor 2 (PAR2) - Stabilized T4L Fusion](/xray-mp-wiki/proteins/gpcr/par2/) — Related protein structure; referenced in text
- [KtrA (Cytosolic Regulatory Protein from Bacillus subtilis)](/xray-mp-wiki/proteins/pumps-atpases/ktra/) — Related protein structure; referenced in text
- [SbtB (PII-Like Regulatory Protein, Synechocystis sp. PCC 6803)](/xray-mp-wiki/proteins/slc-transporters/sbtb/) — Related protein structure; referenced in text
