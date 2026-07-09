---
title: "FtsH from Aquifex aeolicus (A. aeolicus AAA Protease)"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [membrane-protein, enzyme, xray-crystallography]
sources: [doi/10.1107##s1399004715005945]
verified: regex
uniprot_id: O67077
---

# FtsH from Aquifex aeolicus (A. aeolicus AAA Protease)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O67077">UniProt: O67077</a>

<span class="expr-badge">Aquifex aeolicus</span>

## Overview

FtsH is a universally conserved [ATP](/xray-mp-wiki/reagents/ligands/atp/)-dependent zinc metalloprotease found in eubacteria,
mitochondria and chloroplasts. It belongs to the AAA+ (ATPases associated with various cellular
activities) family and degrades both membrane-bound and soluble protein substrates. FtsH is a
membrane-anchored hexameric protease where each polypeptide chain contains two N-terminal
transmembrane helices, followed by cytosolic AAA and protease domains. The crystal structure
of a truncated soluble quadruple mutant (Delta-AaFtsH, residues 142-634) from Aquifex aeolicus
was determined in the [ADP](/xray-mp-wiki/reagents/ligands/adp/)-bound state at 2.96 A resolution (PDB 4ww0), revealing a C2-symmetric
AAA ring arrangement distinct from the Thermotoga maritima FtsH structure. The protease ring
exhibits sixfold symmetry and is identical to other FtsH structures. The AAA domains in a
related crystal form are highly disordered (PDB 4z8x at 3.25 A), highlighting their flexibility.
The active-site switch beta-strand in the protease domain was found to be critical for
proteolytic activity, and a conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) in the linker between [AAA](/xray-mp-wiki/reagents/ligands/aaa/) and protease domains
(Gly399) is essential for FtsH function.

## Publications

### doi/10.1107##s1399004715005945

**Structures:**

<table class="wiki-table">
  <thead><tr>
    <th>PDB ID</th>
    <th>Resolution</th>
    <th>Space Group</th>
    <th>Construct</th>
    <th>Ligand/Co-factor</th>
  </tr></thead>
  <tbody>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ww0">4WW0</a></td>
      <td>2.96</td>
      <td>I222</td>
      <td>Delta-AaFtsH (residues 142-634 with mutations I250M, F360L, K552R, E627G; N-terminal His tag cleaved</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4z8x">4Z8X</a></td>
      <td>3.25</td>
      <td>I222</td>
      <td>Delta-AaFtsH (residues 142-634 with mutations I250M, F360L, K552R, E627G</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21 (DE3 CodonPlus
- **Construct**: Truncated A. aeolicus FtsH (residues 142-634 with N-terminal thrombin-cleavable hexahistidine tag. Contains four mutations: I250M, F360L, K552R, E627G
- **Notes**: P Glycoprotein Induced Fit Bindingduced Tight Junction Disassemblyduced Domain Rearrangement P Type Atpases with 1 mM IptgG at OD600 0.8-1.0, grown overnight at 22 C. Purified by Ni-NTA, Resource Q [Gtacr1](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) Familylus Plusn Pi Interactionn Channel Gatingn Mediated Ligand Bindingn Ae1 Anion Exchanger-Hdx MsSp Sepharoseton Transport Mechanism, and [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) S200 Size Exclusion Chromatographyy-mp-wiki/concepts/[Inducer Exclusion](/xray-mp-wiki/concepts/miscellaneous/inducer-exclusion/)/ Affinity Chromatographyay-mp-wiki/methods/quality-assessment/[Sec Mals](/xray-mp-wiki/methods/quality-assessment/sec-mals/)/e ChromatographyChromatographyp-wiki/methods/quality-assessment/[FSEC](/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)/. His tag cleaved with [Thrombin Protease](/xray-mp-wiki/reagents/protein-tags/thrombin-protease/) before SEC.

**Purification:**

- **Expression system**: E. coli BL21 (DE3 CodonPlus
- **Expression construct**: Delta-AaFtsH (142-634 with N-terminal thrombin-cleavable His tag
- **Tag info**: N-terminal hexahistidine tag, cleaved by thrombin

<table class="wiki-table">
  <thead><tr>
    <th>Step</th>
    <th>Method</th>
    <th>Resin / Column</th>
    <th>Buffer + Detergent</th>
    <th>Notes</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>Cell lysis</td>
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French press</a> (3 passages at 6.9 MPa</td>
      <td>—</td>
      <td>20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> Propane-HCl pH 8.0, 300 mM NaCl, 0.02% NaN3</td>
      <td><a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>-Opsin40e Energy Perturbationl Free Protein Synthesiskey Beta1 Ar Ligand Free Basalch Crystallization Free Interface Diffusion cOmplete ClppPn ProteaseProteased Proteaseoteasession Proteaseubstratetease MechanismCytochia Coli SppaProtease Family Mechanismd Protease Substrate Specificity C3361noline Msba Inhibitor Pyridylpiperazine Epitial Quinoline Msba Inhibitorimized Quinoline <a href="/xray-mp-wiki/proteins/abc-transporters/msba/">Msba</a> Inhibitor cocktail added</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> (Qiagen</td>
      <td>20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> Propane-HCl pH 8.0, 300 mM NaCl, 0.02% NaN3</td>
      <td></td>
    </tr>
    <tr>
      <td>Anion-exchange chromatography</td>
      <td>Ion-exchange</td>
      <td>Resource Q (GE Healthcare</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>His tag cleavage</td>
      <td>Thrombin digestion overnight at 4 C</td>
      <td>—</td>
      <td></td>
      <td>Followed by another <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> step to remove uncleaved Mladoxinstabilizationtiona5Ama3hapin 1A3 Familyotein Family Family 1obrevin 2 4Protein FamilyntamerProtein Family Yidcov 2 Ctd Agonismotein FamilyKir3 2dral Twinning Mep Protein Familyrome B561 Family Protein Couplinge Binding Proteincholine Binding Proteinopology Architecturetein Nitrosomonas EuropaeaeCytoplasmic Poreree Protein Synthesischromatium Tepidum Hipipaeodactylum TricornutumGas Anaesthetic MechanismNetworks Membrane Protein Oligomerizationne Protein Crystals For Neutron Diffractionirected Spin Labeling Membrane ProteinAtom Derivative Detergents And Lipids and tag</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>Superdex S200 16/600 (GE Healthcare</td>
      <td>20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> Propane-HCl pH 8.0, 100 mM NaCl, 0.02% NaN3</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a> (<a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting drop</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Masr1rb Ac-AaFtsH at 10 mg/mL in 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis Tris Propane-HCl pH 8.0, 100 mM NaCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M CaCl2, 0.1 M MES pH 6.0, 20% Pegg 6000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified (Single Crystal Microspectrophotometry Mscs A106V X1</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of form X1 appeared initially. After several months, smaller Diffractive Imaging Imperfect Crystalse Protein Crystals For Neutron Diffraction of form X2 (shrunken c-axis appeared alongside. <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mscs/">Mscs</a>s A106V](/xray-mp-wiki/proteins/voltage-gated-channels/mscs-a106v/) X2 has ordered <a href="/xray-mp-wiki/reagents/ligands/aaa/">AAA</a> <a href="/xray-mp-wiki/concepts/transport-mechanisms/autoinhibitory-domains/">Autoinhibitory Domains</a>.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### C2-symmetric AAA ring with ADP-bound state

The AAA domains assemble into a ring with C2 symmetry, in contrast to the sixfold symmetry
of the protease ring. The breakdown of NCSy Mismatch Rotary Motor arises from different interdomain angles
[Conformational Coupling Gating](/xray-mp-wiki/concepts/transport-mechanisms/conformational-coupling-gating/) the protease and AAA domains in the [Trex1](/xray-mp-wiki/proteins/gpcr/trex1/) crystallographically independent monomers.
The [Autoinhibitory Domains](/xray-mp-wiki/concepts/transport-mechanisms/autoinhibitory-domains/) move as rigid bodies by ~30 degrees rotation, with the [Glycine](/xray-mp-wiki/reagents/buffers/glycine/)e Gating Hinge](/xray-mp-wiki/concepts/transport-mechanisms/glycine-gating-hinge/) around residues
400-410 in the M4M Linker Interaction Motif. Unlike the T. maritima FtsH [Structure Based Antipsychotic Design](/xray-mp-wiki/concepts/construct-design/structure-based-antipsychotic-design/) where Mlabd1pry1epeat12 LbdDomainDomain6r An Swappingphorin AtbEcdel GatingCov 2 CtdC Luminal Domain Receptor4 Cterm CamB Glun2B Atdal Core Diseasehydrogenase Dii Domainomain Activation Mechanism Ae1 Anion Exchanger Domain Motion In P Type Atpasesnduced Domain Rearrangement P Type Atpases rotations are
mainly perpendicular to the ClppPn ProteaseProteased Proteaseoteasession Proteaseubstratetease MechanismCytochia Coli SppaProtease Family Mechanismd Protease Substrate Specificity ring (closure, the A. aeolicus FtsH shows more lateral
(twisting movements, resulting in a qualitatively different [AAA](/xray-mp-wiki/reagents/ligands/aaa/) 6Mr Six Carbon Ring Retinalrulina Platensis C15 Ringrae V Atpase K Ringst Atp Synthase C10 Ringoroplast Atp Synthase C Ringobacter Tartaricus C Subunitillus Pseudofirmus Of4 C12 Ringnach Chloroplast C14 Rotor Ringillus Pseudofirmus Of4 C13 Ringst Mitochondrial Atp Synthase C10 Ringmon Drug Binding Site Atp Synthase C Ring arrangement.

### Closed pore and contiguous phenylalanine path

The [Central Core Disease](/xray-mp-wiki/concepts/signaling-receptors/central-core-disease/) pore in the A. aeolicus FtsH structure is completely closed. The pore
L Phenylalaninel Gating residues (Phe228, part of the [Conserved Core Triad](/xray-mp-wiki/concepts/signaling-receptors/conserved-core-triad/) 228FGV Gxxxg Motifega MotifMotif5 Linker Interaction Motif Substrate Recognition Gmg Motif are partially disordered
but line a contiguous funnel-shaped path. Compared to the T. maritima FtsH [Structure Based Antipsychotic Design](/xray-mp-wiki/concepts/construct-design/structure-based-antipsychotic-design/), the
aromatic Apolar Side Chain Packinge Entry Ion Conduction Pathway chains are more buried inside the cleft, and Cry6Aaabce Forming Toxinsed Pore Mechanisming Pore Currentae1P Sodium Channelm Pore Modulek1 Cytoplasmic Poreha Helical Pore Forming Toxin Family contacts are tighter.

### Active-site switch beta-strand is critical for proteolytic activity

A [Conserved Core Triad](/xray-mp-wiki/concepts/signaling-receptors/conserved-core-triad/) Gs Betaar B3an Beta1 Ara Arrestin Signalingkey Beta1 Ar M23a1 Adrenergic Receptora2 Adrenergic Receptoran Beta 2 Adrenergic Receptorkey Beta1 Ar M23 2Vt4key Beta1 Ar Ligand Free Basal-strand (the active-site [Rocker](/xray-mp-wiki/proteins/miscellaneous/rocker/) Switch Mechanismor Switch Gatingh Loop Gating Rnd Transporters covering the Ntsr1 ElActive Conformation041 Active Enantiomeritutive Active Gpcr Mutationscillus Thermodenitrificans SecyeActive State High Affinity Agonist Binding-Kkrsepsep2Pra Helical Binding Sitee 2 Protease Family Mechanismosteric Site In Nss Transportersiplasmic Drug Binding Site Rndmon Drug Binding Site Atp Synthase C Ringe Directed Spin Labeling Membrane Protein Gs Alphabc Alpha3ine Receptor Alpha3n Alpha4Beta2 Nicotinic Receptora 1B Adrenergic Receptora Helical Pore Forming Toxin Family-helix is
disordered in all Trex1in Swapping copies of the A. aeolicus FtsH structure. This segment functions as
an edge strand for Tat A SubstrateBinding Pockete Binding In Asbt Yfe Protonation Coupling Protease Substrate Specificitysporter Substrate Specificitystrate Recognition Gmg Motifly Substrate Specificitye Polyspecificity Smr Transporters Protein Insertase Substrate Exit Gate [S1I8](/xray-mp-wiki/reagents/ligands/s1i8/) Fsce 5hte Binding Modeichia Coli SppaGly 3M3Sh Malodour Precursor [Molecular Docking](/xray-mp-wiki/methods/structure-determination/molecular-docking/). The T450P mutation in this segment within the
[Sri 9829](/xray-mp-wiki/reagents/ligands/sri-9829/)-[Glun1 Glun2B Nmda Receptor](/xray-mp-wiki/proteins/other-ion-channels/gluN1-gluN2b-nmda-receptor/) FtsH severely impaired proteolytic activity while retaining ATPase [Trex1](/xray-mp-wiki/proteins/gpcr/trex1/) Rnase Activitynstitutive Activity,
confirming its functional importance. The lid-Gxxxg Motifing Helix Mechanismx Shift Mechanismzontal Helix Spring Mechanism interpretation in the T. thermophilus
FtsH [Structure Based Antipsychotic Design](/xray-mp-wiki/concepts/construct-design/structure-based-antipsychotic-design/) is problematic due to Ball And Chain Modelcal Recoil Desensitization bias and flawed NCSy Refinement data.

### Conserved glycine in AAA-protease linker is essential

An absolutely [Conserved Core Triad](/xray-mp-wiki/concepts/signaling-receptors/conserved-core-triad/) [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residue (Gly399 in A. aeolicus and T. thermophilus FtsH
in the M4M Linker Interaction Motif [Bovine F1 Atpase](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/)e Stator Complex](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase-stator-complex/) [Conformational Coupling Gating](/xray-mp-wiki/concepts/transport-mechanisms/conformational-coupling-gating/) the [AAA](/xray-mp-wiki/reagents/ligands/aaa/) and ClppPn ProteaseProteased Proteaseoteasession Proteaseubstratetease MechanismCytochia Coli SppaProtease Family Mechanismd Protease Substrate Specificity [Autoinhibitory Domains](/xray-mp-wiki/concepts/transport-mechanisms/autoinhibitory-domains/) is crucial for FtsH activity.
The G399L mutation in T. thermophilus FtsH causes the Mladoxinstabilizationtiona5Ama3hapin 1A3 Familyotein Family Family 1obrevin 2 4Protein FamilyntamerProtein Family Yidcov 2 Ctd Agonismotein FamilyKir3 2dral Twinning Mep Protein Familyrome B561 Family Protein Couplinge Binding Proteincholine Binding Proteinopology Architecturetein Nitrosomonas EuropaeaeCytoplasmic Poreree Protein Synthesischromatium Tepidum Hipipaeodactylum TricornutumGas Anaesthetic MechanismNetworks Membrane Protein Oligomerizationne Protein Crystals For Neutron Diffractionirected Spin Labeling Membrane ProteinAtom Derivative Detergents And Lipids to elute exclusively as a
monomer and eliminates both ATPase and proteolytic [Trex1](/xray-mp-wiki/proteins/gpcr/trex1/) Rnase Activitynstitutive Activity. This Glycinee Betaine GlycineGlyt1lpha3e Gating Hingee Receptor Alpha3 provides
necessary flexibility for interdomain communication.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/">Bovine F1-ATPase (azide-inhibited form)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase-stator-complex/">Bovine Mitochondrial F1-ATPase-Stator Complex (Membrane Extrinsic Region)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/other-ion-channels/gluN1-gluN2b-nmda-receptor/">GluN1-GluN2B NMDA Receptor (Xenopus laevis, Full-Length)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/rhodopsins/gtacr1/">GtACR1 Anion Channelrhodopsin from Guillardia theta</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mscs/">E. coli MscS (Mechanosensitive Channel of Small Conductance)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/abc-transporters/msba/">MsbA Lipid A Flippase</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mscs-a106v/">E. coli MscS Mechanosensitive Channel (A106V Open Form)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/gpcr/trex1/">Mouse TREX1 (Three Prime Repair Exonuclease 1)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/miscellaneous/rocker/">Rocker — De Novo Designed Zn²⁺ Transporter</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/concepts/miscellaneous/inducer-exclusion/">Inducer Exclusion</a> — Related concept; referenced in text
