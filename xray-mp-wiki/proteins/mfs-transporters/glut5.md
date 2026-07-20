---
title: "GLUT5 Fructose Transporter"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14909]
verified: agent
---

# GLUT5 Fructose Transporter

<div class="expr-badges"><span class="expr-badge expr-s-cerevisiae">S. cerevisiae</span></div>


## Overview

GLUT5 is a fructose-specific facilitated-diffusion transporter belonging to the solute carrier 2 (SLC2) family and the major facilitator superfamily (MFS). It is primarily expressed in the small intestine but also found in brain, adipose tissue, kidney, testes, and skeletal muscle. GLUT5 is the only member of the GLUT family specific to fructose, and its altered activity has been linked to metabolic disorders such as type 2 diabetes and obesity. GLUT5 is also overexpressed in certain tumour cells, making it a potential drug target. This paper describes the crystal structures of Rattus norvegicus GLUT5 (rGLUT5) in an open outward-facing conformation at 3.27 A resolution and Bos taurus GLUT5 (bGLUT5) in an open inward-facing conformation at 3.0 A resolution, providing mechanistic insights into fructose transport via a gated-pore mechanism.


## Publications

### doi/10.1038##nature14909

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/--">--</a></td>
      <td>3.27</td>
      <td>P2_1</td>
      <td>Rat GLUT5 (full-length, N50Y deglycosylation mutant) in complex with 4D111Fv fragment (VL and VH chains)</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/--">--</a></td>
      <td>3.0</td>
      <td>P2_12_12_1</td>
      <td>Bovine GLUT5 (residues 1-473, N51A deglycosylation mutant)</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae FGY217
- **Construct**: Full-length GLUT5 with C-terminal His6 tag and TEV cleavage site (pDDGFP2 vector, GAL1 inducible)
- **Notes**: GLUT5 homologues screened using fluorescence-based methods. Rat GLUT5 N50Y and bovine GLUT5 N51A mutants were used for deglycosylation.

**Purification:**

- **Expression system**: S. cerevisiae FGY217
- **Expression construct**: Full-length GLUT5 with C-terminal His6 tag, TEV cleavable

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
      <td>Cell culture</td>
      <td>Yeast fermentation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>10 ml S. cerevisiae culture; overexpression as described previously</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Cell lysis and ultracentrifugation</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 150 mM NaCl + --</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Solubilization and purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 150 mM NaCl + 0.03% n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>; monodisperse peak assessed by gel filtration</td>
    </tr>
  </tbody>
</table>
**Final sample**: 0.06 mg/ml in purification buffer (20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 0.03% DDM)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>rGLUT5-Fv complex in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>33-35% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 400, 0.12 M CaCl2</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Rat GLUT5 crystallized in complex with 4D111Fv fragment in the open outward-facing conformation</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>bGLUT5 in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Bovine GLUT5 crystallized in the open inward-facing conformation; data showed severe anisotropy (resolutions along a*/b*/c* of 4.0/3.0/4.0 A)</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Gated-pore transport mechanism in GLUT5

Comparison of the open outward-facing (rGLUT5) and open inward-facing (bGLUT5) structures reveals that in addition to a global [Rocker](/xray-mp-wiki/proteins/miscellaneous/rocker/)-switch-like reorientation of the N- and C-terminal 6-TM bundles (~15 degree rotation), local asymmetric rearrangements of C-terminal bundle helices TM7 and TM10 form substrate-induced gates. TM7 gates the extracellular side while TM10 gates the intracellular side, supporting a gated-pore transport mechanism for MFS monosaccharide transporters.

### Substrate specificity switch via single point mutation

Substitution of Gln166 (TM5) with glutamate (the equivalent residue in GLUT7) switches substrate preference from fructose to [Glucose](/xray-mp-wiki/reagents/additives/glucose/). The Q166E mutant shows robust D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) binding with a Kd of ~4 mM, whereas wild-type GLUT5 binds only [D Fructose](/xray-mp-wiki/reagents/ligands/d-fructose/) (Kd ~6-9 mM). This demonstrates that a single residue can determine substrate specificity among GLUT isoforms.

### Inter-bundle salt bridge network in conformational states

In the outward-facing conformation, conserved salt bridges form between the N- and C-terminal bundles (Glu400-Arg158 and Glu151-Arg407), which break apart in the inward-facing state (~7 A and 13 A separation, respectively). An additional salt bridge linking Glu336 (TM8) to Arg340 connects to this inter-bundle network. Substitution of Glu151 or Glu400 to alanine significantly reduces [D Fructose](/xray-mp-wiki/reagents/ligands/d-fructose/) binding, showing coupling between salt bridge integrity and substrate binding. The intracellular helical domain (ICH1-ICH5) provides additional stabilization of the outward-facing conformation.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">MFS Transporter</a> — GLUT5 belongs to the Major Facilitator Superfamily
- <a href="/xray-mp-wiki/concepts/protein-families/sugar-porter-family/">Sugar Porter Family</a> — GLUT5 is a member of the sugar porter subfamily of MFS transporters
- <a href="/xray-mp-wiki/proteins/mfs-transporters/glut1/">GLUT1</a> — Comparison with hGLUT1 inward-facing structure shows conservation of substrate-binding residues
- <a href="/xray-mp-wiki/reagents/ligands/d-fructose/">D-Fructose</a> — Primary substrate of GLUT5
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Referenced in glut5 text
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in glut5 text
- <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> — Referenced in glut5 text
- <a href="/xray-mp-wiki/proteins/miscellaneous/rocker/">Rocker</a> — Referenced in glut5 text
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Referenced in glut5 text
- <a href="/xray-mp-wiki/reagents/ligands/d-fructose/">D Fructose</a> — Referenced in glut5 text
