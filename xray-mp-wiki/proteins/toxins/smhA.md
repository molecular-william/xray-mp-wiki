---
title: "SmhA from Serratia marcescens"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41598-021-85726-0]
verified: regex
uniprot_id: A0A1Q4NVM5
---

# SmhA from Serratia marcescens

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A1Q4NVM5">UniProt: A0A1Q4NVM5</a>

<span class="expr-badge">Serratia marcescens</span>

## Overview

SmhA is the A component of the SmhABC tripartite alpha-pore-forming toxin (alpha-PFT) from Serratia marcescens MSU-97. SmhA shares structural similarity with the A components of other tripartite ClyA family alpha-PFTs such as NheA and AhlB. SmhA adopts a compact soluble structure with a beta-tongue motif that shields hydrophobic residues. Upon membrane binding, SmhA is proposed to undergo a conformational change from the soluble form to an extended helical pore form, providing the hydrophilic lining of the tripartite pore lumen. SmhA interacts with the SmhB component during pore assembly after formation of the SmhBC pro-pore complex.


## Publications

### doi/10.1038##s41598-021-85726-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7a26">7A26</a></td>
      <td>2.98 A</td>
      <td>P42</td>
      <td>Full-length SmhA with C-terminal 6xHis tag (SeMet)</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7a27">7A27</a></td>
      <td>2.57 A</td>
      <td>P212121</td>
      <td>Full-length SmhA with C-terminal 6xHis tag</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 DE3
- **Construct**: Full-length SmhA with C-terminal 6xHis tag, cloned into pET21a
- **Induction**: 1 mM IPTG at 16 C overnight
- **Media**: LB medium

**Purification:**

- **Expression system**: E. coli BL21 DE3
- **Expression construct**: SmhA with C-terminal 6xHis tag
- **Tag info**: C-terminal 6xHis tag

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
      <td>Sonication</td>
      <td>—</td>
      <td>50 mM Tris pH 8</td>
      <td>3 x 20 s burst at 16000 nm lambda</td>
    </tr>
    <tr>
      <td>Clarification</td>
      <td>Centrifugation</td>
      <td>—</td>
      <td></td>
      <td>40,000 g for 15 min</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Ni-NTA</td>
      <td>5 ml Nickel Hi-trap column (GE Healthcare)</td>
      <td>50 mM Tris pH 8, 0.5 M NaCl</td>
      <td>Elution with 0-1 M imidazole gradient</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td>SEC</td>
      <td>Superdex 200 pg (GE Healthcare)</td>
      <td>50 mM Tris pH 8, 0.5 M NaCl</td>
      <td>Pre-equilibrated with running buffer</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting drop vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SmhA at 7 mg/ml in 50 mM Tris pH8, 10 mM NaCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>SeMet: 0.1 M MES pH 6.5, 0.16 M CaCl2, 20% PEG 6000; S-Met: 0.2 M potassium nitrate, 20% PEG 3350</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>200 nl:200 nl</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>7 C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Mother liquor with additional 20% (v/v) ethylene glycol</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in 96-well plates. SeMet structure solved by SAD at 2.98 A using CRANK2 pipeline. S-Met structure solved by molecular replacement at 2.57 A. Data collected at Diamond Light Source beamlines I03 and I04-1.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Structural similarity to tripartite ClyA family components

SmhA shares strong structural similarity with SmhB (PDB 6ZZ5, RMSD 2.9 A), NheA (PDB 4K1P, RMSD 3.2 A), AhlB (PDB 6GRJ, RMSD 3.3 A), Hbl-B (PDB 2NRJ, RMSD 2.8 A), and MakA (PDB 6DFP, RMSD 3.5 A). All share the same compact helical bundle tail domain and beta-tongue domain. The C-terminus shields hydrophobic residues of the beta-tongue, with differences in shielding mechanism across species.

### Predicted pore conformation

SmhA is predicted to undergo a conformational change from soluble beta-tongue to extended helical pore form, with two amphipathic helices 36 A in length formed from the head domain. These helices would cross the membrane and provide the hydrophilic lining of the tripartite pore, with hydrophobic and hydrophilic surfaces on opposite faces of the monomer.

### Intracellular loop in Gram-negative tripartite toxins

An intracellular loop between the two amphipathic helices (residues G208-A229) is present in all Gram-negative tripartite toxin A components but absent in Gram-positive Nhe/Hbl toxins, single-component ClyA, and bipartite YaxAB/XaxAB toxins. This loop may interact with intracellular components of the target cell.


## Cross-References

- <a href="/xray-mp-wiki/proteins/toxins/smhB/">SmhB</a> — SmhB is the B component of the SmhABC tripartite alpha-PFT, interacting with SmhA during pore assembly
- <a href="/xray-mp-wiki/proteins/toxins/clyA/">ClyA Cytotoxin</a> — Prototypical single-component alpha-PFT in the same ClyA family
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/pore-forming-toxins/">Pore-Forming Toxins</a> — SmhA is a component of a tripartite alpha-pore-forming toxin in the ClyA family
