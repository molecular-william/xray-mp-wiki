---
title: "E. coli MlaD MCE Protein"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.019]
verified: agent
uniprot_id: P64605
---

# E. coli MlaD MCE Protein

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P64605">UniProt: P64605</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

MlaD is an [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/)-associated MCE (mammalian cell entry) protein from Escherichia coli that forms a homo-hexameric ring with a central hydrophobic pore. MlaD is a key component of the Mla lipid transport system, which maintains [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) [lipid asymmetry](/xray-mp-wiki/concepts/structural-mechanisms/lipid-asymmetry/) in [Gram-negative](/xray-mp-wiki/concepts/miscellaneous/gram-negative/) bacteria. The protein associates with the MlaFEDB [ABC transporter](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) complex in the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/) and interacts with the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) lipid-binding protein [MLAC](/xray-mp-wiki/proteins/mlaC), which shuttles phospholipids between the inner and outer membranes. MlaD adopts a seven-stranded beta-barrel MCE domain fold and its hexameric assembly creates a continuous hydrophobic channel from the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/) into the [periplasm](/xray-mp-wiki/concepts/miscellaneous/periplasm/).

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5uw8">5UW8</a></td>
      <td>2.0 A</td>
      <td>C2</td>
      <td>Core MCE domain, residues 32-140</td>
      <td>none</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5uw2">5UW2</a></td>
      <td>2.5 A</td>
      <td>P212121</td>
      <td><a href="/xray-mp-wiki/concepts/miscellaneous/periplasm/">periplasmic</a> domain, residues 32-183</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli Rosetta2 DE3
- **Construct**: Core MCE domain (residues 32-140) or [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) domain (residues 32-183) with [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) signal peptide cleavage, cloned into pET22b(+) with [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) [6xHis](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag

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
      <td>Cell lysis and membrane fractionation</td>
      <td>Emulsiflex-C3 cell disruptor, <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 35,000g and 200,000g</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> + --</td>
      <td>Membrane fraction pelleted at 200,000g</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Solubilized membrane fraction</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a> Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) agarose</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (wash), 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (elution) + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His-tagged MlaD purified from solubilized membranes</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography on <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Hexameric MlaD ring eluted as a single peak</td>
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
      <td>Core MCE domain (residues 32-140), concentrated to 10-60 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M <a href="/xray-mp-wiki/reagents/additives/lithium-sulfate/">lithium sulfate</a>, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 15% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a></td>
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
      <td>Reservoir solution supplemented with 20% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">ethylene glycol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/additives/selenomethionine/">selenomethionine</a>-derivatized crystals for <a href="/xray-mp-wiki/methods/crystallography/mad-phasing/">MAD phasing</a> at ALS 8.3.1. Indexed to C2 space group. Phased by MAD using SHELX C/D/E pipeline. Final model: 7 copies of MCE domain forming hexameric ring.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting-drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/concepts/miscellaneous/periplasm/">periplasmic</a> domain (residues 32-183), concentrated to 10-60 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M <a href="/xray-mp-wiki/reagents/additives/zinc-acetate/">zinc acetate</a>, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.0, 15% ethanol</td>
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
      <td>Reservoir solution supplemented with 20% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">ethylene glycol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Native data collected at ALS 8.3.1, indexed to P212121. Phased by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using Phaser with core MCE domain as search model. Final model: 3 copies of <a href="/xray-mp-wiki/concepts/miscellaneous/periplasm/">periplasmic</a> domain; 2-fold symmetry generates hexameric ring.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Hexameric ring architecture with central hydrophobic pore

MlaD forms a homo-hexameric ring where each subunit contributes a seven-stranded
beta-barrel MCE domain. The hexameric assembly creates a central channel lined
with hydrophobic residues including Leu106, Leu107 at the tip of the beta5-beta6
loop, and Phe150 from the [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) helical bundle. Additional pore-lining residues
include Met141, Leu143, Leu146, Ile147, and Leu149. The hydrophobic pore is oriented
toward the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/), poised to facilitate trafficking of small hydrophobic
molecules to or from the membrane.

### Functional role in lipid transport at the inner membrane

MlaD associates with the MlaFEDB [ABC transporter](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) complex (MlaF ATPase, MlaE permease,
MlaB STAS domain) in the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/). The hexameric MlaD ring sits at the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/)
face of the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/), with its [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) [transmembrane helix](/xray-mp-wiki/concepts/structural-mechanisms/transmembrane-helix/) anchoring one
face of the ring near the membrane. Mutagenesis of pore-lining residues (L106N/L107N,
Phe150Asn, [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) deletions) disrupts complementation of a delta mlaD mutant,
demonstrating that the hydrophobic pore is essential for MlaD function in maintaining
[outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) [lipid asymmetry](/xray-mp-wiki/concepts/structural-mechanisms/lipid-asymmetry/).

### MCE domain fold and conservation

The core MCE domain of MlaD adopts a seven-stranded beta-barrel fold with no similarity
to other known protein structures. MCE proteins are ubiquitous among double-membraned
bacteria and eukaryotic chloroplasts. The MlaD MCE domain serves as a structural
template for understanding the entire MCE protein superfamily, including [YEBT](/xray-mp-wiki/proteins/yebT) and
[PQIB](/xray-mp-wiki/proteins/pqiB) which form elongated tube- and syringe-like architectures by stacking multiple
MCE domains.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/mce-protein-family/">MCE Protein Family</a> — MlaD is the prototypical characterized member of the MCE protein superfamily
- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaC/">E. coli MlaC Lipid-Binding Protein</a> — MlaC ferries lipids between MlaD at the inner membrane and MlaA at the outer membrane
- <a href="/xray-mp-wiki/proteins/structural-adhesion/yebT/">E. coli YebT Tube-like MCE Protein</a> — YebT shares the same MCE domain fold as MlaD but forms an elongated tube of seven stacked rings
- <a href="/xray-mp-wiki/proteins/structural-adhesion/pqiB/">E. coli PqiB Syringe-like MCE Protein</a> — PqiB shares the same MCE domain fold as MlaD but forms a needle-and-syringe architecture
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for MlaD solubilization from membranes
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used for Ni-NTA affinity chromatography wash (10 mM) and elution (250 mM)
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — 0.1 M HEPES pH 7.5 used in crystallization reservoir for core MCE domain
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> — 0.1 M MES pH 6.0 used in crystallization reservoir for periplasmic domain
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> — Entity mentioned in text
