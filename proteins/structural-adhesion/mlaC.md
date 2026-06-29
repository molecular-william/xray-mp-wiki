---
title: "E. coli MlaC Periplasmic Lipid-Binding Protein"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.019]
verified: false
---

# E. coli MlaC Periplasmic Lipid-Binding Protein

## Overview

MlaC is a soluble [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) lipid-binding protein from Escherichia coli that functions as a shuttle carrier for phospholipids in the Mla lipid transport system. MlaC binds lipid tails in a deep [hydrophobic pocket](/xray-mp-wiki/concepts/hydrophobic-pocket/) with little head group specificity, allowing it to ferry a wide range of diacyl lipids between the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/) MlaFEDB transporter complex and the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) [MLAA](/xray-mp-wiki/proteins/mlaA)-OmpC/OmpF complex. MlaC adopts a mixed alpha/beta fold with four beta strands and seven alpha helices. Its structure reveals a deep [hydrophobic pocket](/xray-mp-wiki/concepts/hydrophobic-pocket/) that binds the two tails of a lipid molecule without interacting with the lipid head group.

## Publications

### doi/10.1016##j.cell.2017.03.019

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5uwa">5UWA</a></td>
      <td>2.5 A</td>
      <td>P212121</td>
      <td>Mature MlaC, signal peptide-cleaved, residues 22-211, with <a href="/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/">N-terminal</a> <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">6xHis</a> tag and <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a> cleavage site</td>
      <td>Phosphatidic acid</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli Rosetta2 DE3
- **Construct**: Mature MlaC (residues 22-211), signal peptide-cleaved, cloned into custom pET vector (pBE1092) with [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) [6xHis](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag and [TEV protease](/xray-mp-wiki/reagents/additives/tev-protease/) cleavage site

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
      <td>Cell lysis</td>
      <td>Emulsiflex-C3 cell disruptor, centrifugation at 38,000g</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> + --</td>
      <td>Clarified lysate from <a href="/xray-mp-wiki/concepts/miscellaneous/periplasm/">periplasmic</a> fraction</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA Agarose Resin</a> agarose</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (wash), 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (elution) + --</td>
      <td>His-tagged MlaC purified from soluble <a href="/xray-mp-wiki/concepts/miscellaneous/periplasm/">periplasmic</a> fraction</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> on <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + --</td>
      <td>Monomeric MlaC eluted as single peak</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting-drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>MlaC (residues 22-211), concentrated to 10-60 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/additives/citric-acid/">citric acid</a> pH 3.5, 1.6 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">ammonium sulfate</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir solution supplemented with 37.5% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">ethylene glycol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Phased by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using MR-Rosetta homology model based on PDB 2QGU template. Two <a href="/xray-mp-wiki/reagents/lipids/phosphatidic-acid/">Phosphatidic Acid</a> molecules built into electron density in the core of each MlaC monomer in the asymmetric unit.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Lipid tail binding pocket with head group independence

MlaC contains a deep [hydrophobic pocket](/xray-mp-wiki/concepts/hydrophobic-pocket/) that binds the two acyl tails of a lipid
molecule without interacting with the lipid head group. This structural feature
allows MlaC to bind a wide range of diacyl lipids including [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol)
(PG), [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine) (PE), and [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin)-like species. Mass spectrometry
analysis of co-purified lipids confirmed that [MLAD](/xray-mp-wiki/proteins/mlaD), [PQIB](/xray-mp-wiki/proteins/pqiB), and [YEBT](/xray-mp-wiki/proteins/yebT) each bind PG
and PE species. The lack of head group specificity supports a model where MlaC
functions as a general lipid shuttle.

### Periplasmic lipid shuttle between inner and outer membrane complexes

MlaC interacts directly with both the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/) MlaFEDB transporter complex
and the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) [MLAA](/xray-mp-wiki/proteins/mlaA)-OmpC/OmpF complex, as demonstrated by [biolayer interferometry](/xray-mp-wiki/methods/quality-assessment/biolayer-interferometry/)
(Octet RED384). MlaC makes no significant interactions with lipid head groups,
suggesting it binds the hydrophobic tails of phospholipids extracted from the inner
membrane and delivers them to the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/). This shuttle mechanism bridges
the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) space between the IM and OM lipid transport complexes.

### MlaC homologs and structural conservation

Two MlaC homologs were previously deposited by the Northeast Structural Genomics
Consortium (NESG): PDB 2QGU from Ralstonia solanacearum (27% sequence identity)
and PDB 4FCZ (22% sequence identity). The 2QGU structure was crystallized with
a ligand modeled as [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine). Re-refinement of 4FCZ coordinates
revealed additional electron density in the [hydrophobic pocket](/xray-mp-wiki/concepts/hydrophobic-pocket/) suggestive of a
tetra-acyl [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin)-like lipid. These homologs support the conservation of
MlaC as a lipid-binding protein across bacterial species.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaD/">E. coli MlaD MCE Protein</a> — MlaC ferries lipids between MlaD at the inner membrane and outer membrane complexes
- <a href="/xray-mp-wiki/proteins/mlaa/">E. coli MlaA Outer Membrane Lipoprotein</a> — MlaC interacts directly with the MlaA-OmpC/OmpF outer membrane complex
- <a href="/xray-mp-wiki/proteins/structural-adhesion/yebT/">E. coli YebT Tube-like MCE Protein</a> — YebT binds the same phospholipids (PG, PE) that MlaC shuttles
- <a href="/xray-mp-wiki/proteins/structural-adhesion/pqiB/">E. coli PqiB Syringe-like MCE Protein</a> — PqiB binds the same phospholipids (PG, PE) that MlaC shuttles
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/">Phosphatidylglycerol</a> — MlaC binds PG lipids as part of its lipid shuttle function
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/">Phosphatidylethanolamine</a> — MlaC binds PE lipids as part of its lipid shuttle function
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used for Ni-NTA affinity chromatography wash (10 mM) and elution (250 mM)
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer</a> — 0.1 M citric acid pH 3.5 used in crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/citric-acid/">citric acid</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a> — Entity mentioned in text
