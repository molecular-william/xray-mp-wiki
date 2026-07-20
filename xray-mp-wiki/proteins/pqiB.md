---
title: "E. coli PqiB Syringe-like MCE Protein"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.019]
verified: agent
uniprot_id: P43671
---

# E. coli PqiB Syringe-like MCE Protein

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P43671">UniProt: P43671</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

PqiB is a periplasm-spanning MCE (mammalian cell entry) protein from Escherichia coli that adopts a distinctive needle-and-syringe architecture. PqiB consists of three tandem MCE domains that stack into three hexameric rings, forming a ~360 kDa complex with a hollow six-helix coiled-coil needle projecting from one end. The barrel is approximately 90 A in diameter and the complete assembly extends up to ~230 A from the inner membrane face. PqiB creates a continuous hydrophobic channel running from the tip of the needle through the barrel, potentially facilitating direct lipid transport across the periplasmic space. The structure was determined by single-particle [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em) at 3.96 A resolution.

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5uvn">5UVN</a></td>
      <td>3.96</td>
      <td>C6</td>
      <td>Periplasmic domain of PqiB (three MCE domains plus partial C-terminal helical region), with amphipol A8-35</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli Rosetta2 DE3
- **Construct**: PqiB periplasmic domain (three MCE domains with partial C-terminal region), expressed as soluble protein

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
      <td>Emulsiflex-C3 cell disruptor, centrifugation</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 300 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + --</td>
      <td>Clarified lysate prepared</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Metal Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a> Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) agarose</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 300 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> (wash), 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> (elution) + --</td>
      <td>His-tagged PqiB purified from soluble fraction</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 150 mM NaCl + --</td>
      <td>Hexameric PqiB complex</td>
    </tr>
  </tbody>
</table>


## Biological / Functional Insights

### Needle-and-syringe architecture with continuous hydrophobic channel

Six PqiB polypeptides associate to form a ~360 kDa needle-and-syringe assembly.
The syringe barrel consists of three stacked hexameric rings (MCE1, MCE2, MCE3),
while the needle is formed by a hollow six-helix coiled-coil with an outer diameter
of ~35 A and a hollow lumen of 15-20 A wide. A long tunnel runs from the tip of
the needle to the bottom of the barrel, continuous with the channel through the
barrel. The needle is somewhat flexible at the junction with the barrel, with an
estimated length of ~135 A from barrel base to needle tip.

### Hydrophobic pore lining by beta5-beta6 loops and beta-barrel motifs

The central pore of PqiB is lined by hydrophobic residues from the homologous beta5-beta6
loops of each MCE domain. The MCE3 domain beta5-beta6 loop has a hydrophobic tip
(Leu377, Val378, Thr379) forming a ~13 A constriction at the junction between barrel
and needle. The MCE1 and MCE2 loops form extended beta hairpins that contribute
to two 18-stranded beta-barrel motifs stacked end-to-end, lining the barrel interior
and creating a barrier that could exclude solvent from the hydrophobic central channel.

### Modular MCE domain stacking principle

PqiB has three tandem MCE domains, and its three stacked rings mirror the three
MCE domains in its primary sequence. This confirms the modular assembly principle
where the number of stacked rings equals the number of tandem MCE domains. PqiB
has a C-terminal six-helix coiled-coil needle not present in [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/mlaD), and the needle
lumen is continuous with the barrel channel. PqiB may interact with outer membrane
lipoprotein PqiC and inner membrane protein PqiA to form a complete transport system.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaD/">E. coli MlaD MCE Protein</a> — PqiB shares the same MCE domain fold; MlaD structure docked into PqiB EM density
- <a href="/xray-mp-wiki/proteins/structural-adhesion/yebT/">E. coli YebT Tube-like MCE Protein</a> — YebT shares the same modular stacking principle but with seven MCE domains
- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaC/">E. coli MlaC Lipid-Binding Protein</a> — MlaC shuttles lipids in the Mla system; PqiB may bypass the need for a shuttle by direct spanning
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used for Ni-NTA affinity chromatography
- <a href="/xray-mp-wiki/concepts/protein-families/mce-protein-family/">MCE Protein Family</a> — PqiB is a three-domain MCE protein with unique needle-and-syringe architecture
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — PqiB structure determined by single-particle cryo-EM at 3.96 A resolution
- <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA Agarose Resin</a> — Entity mentioned in text
