---
title: "TcdA1 Toxin Complex A Subunit from Photorhabdus luminescens"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein]
sources: [doi/10.1038##nature13015]
verified: regex
uniprot_id: Q9RN43
---

# TcdA1 Toxin Complex A Subunit from Photorhabdus luminescens

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9RN43">UniProt: Q9RN43</a>

<span class="expr-badge">Photorhabdus luminescens</span>

## Overview

TcdA1 is the TcA subunit of the toxin complex from Photorhabdus luminescens subsp. akhurstii. It forms a large bell-shaped pentameric structure that perforates host membranes and translocates toxic enzymes into host cells. The prepore structure was solved at 4.0 A resolution by X-ray crystallography, and the pore structure at 9 A by [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em). The structure reveals a translocation channel, four receptor-binding sites, and a neuraminidase-like region important for host specificity. The transition from prepore to pore state involves pH-induced shell opening driven by an entropic spring mechanism.


## Publications

### doi/10.1038##nature13015

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4o9y">4O9Y</a></td>
      <td>4.0 A</td>
      <td>not specified</td>
      <td>TcdA1 full-length from P. luminescens subsp. akhurstii (12500 residues in pentamer, 1.41 MDa)</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4o9y">4O9Y</a></td>
      <td>9 A</td>
      <td>C5 (cryo-EM)</td>
      <td>TcdA1 pore state from P. luminescens subsp. akhurstii</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: TcdA1 full-length from P. luminescens subsp. akhurstii, overexpressed and purified as previously described

**Purification:**

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
      <td>Cell lysis and expression</td>
      <td>Overexpression in E. coli BL21(DE3)</td>
      <td>--</td>
      <td>not specified + --</td>
      <td>TcdA1 overexpressed and purified as previously described</td>
    </tr>
    <tr>
      <td>Dialysis</td>
      <td>Dialysis</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> pH 5.0, 100 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/tween-20">Tween-20 Polysorbate 20 Nonionic Detergent</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + <a href="/xray-mp-wiki/reagents/detergents/tween-20">Tween-20 Polysorbate 20 Nonionic Detergent</a></td>
      <td>Dialysis of TcdA1 against purification buffer</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Superose 6 10/300 GL column (GE Healthcare Life Sciences)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> pH 5.0, 100 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/tween-20">Tween-20 Polysorbate 20 Nonionic Detergent</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + <a href="/xray-mp-wiki/reagents/detergents/tween-20">Tween-20 Polysorbate 20 Nonionic Detergent</a></td>
      <td>Final purification step, concentrated to 15-20 mg/mL using Amicon filter devices</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>15-20 mg/mL TcdA1 in 50 mM <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> pH 5.0, 100 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/tween-20">Tween-20 Polysorbate 20 Nonionic Detergent</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.0, Jeffamine ED-2001, 1.1 M sodium malonate</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>5-7 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir solution with 5-25% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, flash frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals reached approximately 300 x 200 x 200 micrometers. Data collected at PXII-X10SA beamline at Swiss Light Source. Structure solved at 4.0 A by molecular replacement using previous 6.3 A <a href="/xray-mp-wiki/methods/structure-determination/cryo-em">Cryo-Electron Microscopy</a> search model with PHENIX.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Domain organization and receptor-binding sites

The TcdA1 protomer is composed of eight domains. Six domains form the alpha-helical shell and are connected by a ~42 amino acid linker to two domains forming the inner channel. The pentamer assembles through tight protomer-protomer interactions. TcA forms four receptor-binding domains (A-D) with structural homology to host cytokine receptors (IFNAR2, IL17-R, IL2-R, IL15-R, IL12-R families), suggesting adaptation to eukaryotic cell surface receptors. The receptor-binding domains are positioned approximately 125 A from the membrane, consistent with binding to elongated cell surface proteins such as integrins.

### Entropic spring mechanism drives membrane injection

The linker connecting the shell and channel in the prepore state has a stretched-out conformation (113 A for 48 residues). In the pore state, the linker contracts, indicating it acts as an entropic spring. Steered molecular dynamics simulations show a free energy gain of 20-66 kcal/mol with strong entropic contribution, suggesting the process is exergonic. The stretched linker in the prepore state can only achieve its preferred condensed conformation once the shell opens, pulling on the central channel and driving the syringe-like injection mechanism.

### Translocation channel properties

The luminal surface of the channel is mainly negatively charged with conserved charged residues protruding into the lumen, supporting cation selectivity. The channel diameter varies, narrowing from top to bottom with the narrowest position at tyrosine 2163 (minimal diameter 3.9 A). A ring of 15 arginines marks the upper end of the transmembrane region, providing a positively charged ring that likely interacts with the negatively charged membrane surface. The outer surface of the putative transmembrane region (residues 2107-2158) is predominantly hydrophobic.

### Transition from prepore to pore state

Pore formation involves marked conformational changes including shell opening and a 12 nm shift of the central channel. Three major hinge regions drive the opening: two involve receptor-binding domains and one between the two lobes of the alpha-helical shell domain. The shell subunits from adjacent protomers overlap like an iris diaphragm, with electrostatic interactions mediating the interface. pH-induced changes at the neuraminidase-like domains create strong repulsions that act as an electrostatic lock responsible for pH-induced shell opening.

### pH-independent translocation of cationic substrates

The TcdA1 channel is cation selective, similar to the anthrax translocation pore. However, the translocated domains in Tc complexes from P. luminescens (hypervariable regions of TccC3 and TccC5) are both cationic substrates with isoelectric points of 9.68 and 8.65, respectively. This contrasts with the anionic anthrax lethal factor and suggests a pH-independent translocation mechanism for Tc toxins, as cationic substrates would not require protonation-driven Brownian ratchet movement.


## Cross-References

- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — 0.1 M HEPES pH 7.0 component of TcdA1 crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/sodium-malonate/">Sodium Malonate</a> — 1.1 M sodium malonate precipitant in TcdA1 crystallization
- <a href="/xray-mp-wiki/reagents/additives/jeffamine-ed-2001/">Jeffamine ED-2001</a> — Polyalkylene glycol precipitant in TcdA1 crystallization
- <a href="/xray-mp-wiki/reagents/detergents/tween-20/">Tween-20</a> — 0.05% Tween-20 in TcdA1 purification and crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> — 50 mM MES pH 5.0 in TcdA1 dialysis and storage buffer
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Crystallization method used for TcdA1
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Structure solution method for TcdA1 at 4.0 A using previous cryo-EM search model
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-EM</a> — Used to determine TcdA1 pore state structure at 9 A resolution
- <a href="/xray-mp-wiki/reagents/detergents/tween-20">Tween-20 Polysorbate 20 Nonionic Detergent</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em">Cryo-Electron Microscopy</a> — Entity mentioned in text
