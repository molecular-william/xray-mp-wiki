---
title: "Mechanosensitive Channel of Large Conductance MscL (Mycobacterium tuberculosis)"
created: 2026-06-03
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13419]
verified: agent
---

# Mechanosensitive Channel of Large Conductance MscL (Mycobacterium tuberculosis)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

MscL (mechanosensitive channel of large conductance) from Mycobacterium tuberculosis is a pentameric mechanosensitive ion channel with two transmembrane helices per subunit. MscL was found to bind lipids non-selectively, with all tested phospholipids imparting comparable stabilization. However, [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) bound with higher avidity, conferring a large linear increase in stability. This is consistent with PI's proposed functional role in MscL mechanosensitivity. MscL demonstrates a broad lipid binding profile without regard to particular headgroup or chain length.


## Publications

### doi/10.1038##nature13419

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/not solved in this paper (pdb 2oar referenced from chang et al. 1998)">NOT SOLVED IN THIS PAPER (PDB 2OAR REFERENCED FROM CHANG ET AL. 1998)</a></td>
      <td>not solved in this paper</td>
      <td>not solved in this paper</td>
      <td>MscL-GFP fusion</td>
      <td>Various phospholipids studied by IM-MS</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) Delta mscL::KanR (homologous recombination disrupted endogenous mscL)
- **Construct**: MscL-GFP fusion

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
      <td>Membrane preparation</td>
      <td>Microfluidizer cell lysis</td>
      <td>--</td>
      <td>300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">TRIS</a> (pH 7.4), protease inhibitor, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">2-Mercaptoethanol</a> + --</td>
      <td>Cells lysed at 19,000 psi; membranes pelleted at 100,000g for 2 h; <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> omitted for MscL</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization</td>
      <td>--</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">2-Mercaptoethanol</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">TRIS</a> (pH 7.4) + 1% <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">n-Nonyl-beta-D-Glucopyranoside (NGNG)</a></td>
      <td>Extracted overnight at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>5 mL HisTrap-HP column</td>
      <td>200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">TRIS</a> (pH 7.4) + 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 1% [n-nonyl-beta-D-glucopyranoside (NGNG)]; eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
  </tbody>
</table>


## Biological / Functional Insights

### Non-selective lipid binding with PI as the most stabilizing lipid

IM-MS analysis revealed that MscL binds lipids non-selectively; all seven tested phospholipids and synthetic PCs with chain lengths C14-C22 imparted comparable stabilization. MscL avidly bound [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol) (PI), greater than all other lipids, conferring a large linear increase in stability upon binding multiple PI molecules. This is consistent with PI's proposed functional role in Mycobacterium mechanosensitivity. MscL responds promiscuously to lipid composition.

### Gas-phase unfolding reveals cumulative lipid stabilization

Collision-induced unfolding experiments showed that apo MscL and lipid-bound forms (1-5 lipids) maintain pentameric state throughout unfolding. All lipid-bound states showed less unfolding as a function of lipid binding. Cumulative stabilization was observed for 1-2 bound lipid molecules. The equilibrium unfolding model identified four distinct intermediate states in the unfolding trajectories.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/mechanosensitive-gating/">Mechanosensitive Gating in Ion Channels</a> — MscL is a mechanosensitive ion channel; lipid binding modulates its mechanosensitivity
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/force-from-lipid-principle/">Force-from-Lipid Principle in Mechanosensation</a> — PI proposed as functional lipid in MscL mechanosensitivity via force-from-lipid mechanism
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol/">Phosphatidylinositol (PI)</a> — PI is the most stabilizing lipid for MscL; confers large linear increase in stability
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylcholine/">Phosphatidylcholine (PC)</a> — Various PC species (DNPC, DEPC, DIPC, DOPC, DPPC, DMPC) tested with MscL
- <a href="/xray-mp-wiki/reagents/detergents/c8e4/">Octyltetraoxyethylene (C8E4)</a> — Optimal detergent for maintaining intact MscL complexes in native MS
- <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">n-Nonyl-beta-D-Glucopyranoside (NGNG)</a> — Detergent used for MscL solubilization (1%)
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> — Buffer used in purification (20-50 mM, pH 7.4)
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mscs/">E. coli MscS (Mechanosensitive Channel of Small Conductance)</a> — Related mechanosensitive channel; different lipid selectivity profile
- <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> — Entity mentioned in text
