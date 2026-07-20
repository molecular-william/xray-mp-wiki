---
title: "Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)"
created: 2026-06-02
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08156]
verified: agent
---

# Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

Syntaxin-1A is a neuronal Qa-SNARE protein from rat that plays a central role in neurotransmitter release at synaptic terminals. It is a single-pass transmembrane protein containing an N-terminal Habc domain, a SNARE motif, a linker region, and a C-terminal transmembrane domain. In the synaptic terminal, syntaxin-1A assembles with SNAP-25 and [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) into a four-helix bundle [SNARE Complex](/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/) that drives synaptic vesicle fusion with the plasma membrane. The X-ray structure of the syntaxin-1A SNARE motif with linkers and transmembrane region revealed continuous helical extension from the SNARE core through the linker into the membrane.


## Publications

### doi/10.1038##nature08156

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/tba">TBA</a></td>
      <td>3.4 A</td>
      <td>C2</td>
      <td>Rat syntaxin-1A residues 183-288 (SNARE motif, linker, transmembrane region)</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/tba">TBA</a></td>
      <td>4.3 A</td>
      <td>TBA</td>
      <td>Selenomethionine-labelled rat syntaxin-1A residues 183-288 (for SAD phasing)</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BI21 (DE3)
- **Construct**: Rat syntaxin-1A (residues 180-262 and 183-288) with N-terminal His-tag, expressed from pET28a

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
      <td>Protein expression</td>
      <td>Expression in E. coli BI21 (DE3) from pET28a</td>
      <td>--</td>
      <td>-- + --</td>
      <td>His-tagged syntaxin-1A expressed separately</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose</td>
      <td>-- + --</td>
      <td>Initial purification of His-tagged syntaxin-1A</td>
    </tr>
    <tr>
      <td>Tag cleavage and desalting</td>
      <td>Tag removal and desalting</td>
      <td>HiPrep 26/10 Desalting column</td>
      <td>20 mM Tris pH 8.8, 500 mM NaCl, 50 mM n-octyl beta-D-glucopyranoside, 1 mM TCEP + n-octyl beta-D-glucopyranoside</td>
      <td>Tags removed, desalted after <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
    </tr>
    <tr>
      <td>Ion-exchange chromatography</td>
      <td>Ion-exchange chromatography</td>
      <td>Not specified</td>
      <td>20 mM Tris pH 8.8, 500 mM NaCl, 50 mM n-octyl beta-D-glucopyranoside + n-octyl beta-D-glucopyranoside</td>
      <td>Further purification by ion exchange</td>
    </tr>
    <tr>
      <td>Complex assembly</td>
      <td>In vitro complex assembly</td>
      <td>--</td>
      <td>Assembled by overnight incubation of monomers at 4 C + --</td>
      <td>Syntaxin-1A used as limiting component in complex assembly with <a href="/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/">Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)</a> and <a href="/xray-mp-wiki/proteins/structural-adhesion/snap-25a/">SNAP-25A (Rat Neuronal Qbc-SNARE Protein)</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Syntaxin-1A/SNAP-25/synaptobrevin-2 complex with linkers and TMRs in n-nonyl beta-D-glucopyranoside</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in main text</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>C2 space group, diffracted to 3.4 A. Also solved SAD structure with SeMet-syntaxin-1A at 4.3 A resolution. Data collected at X10SA beamline, Swiss Light Source. Phases obtained by single-wavelength anomalous dispersion (SAD).</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Continuous helical extension into the membrane

Syntaxin-1A forms a continuous alpha-helix throughout its SNARE motif, linker region, and transmembrane region. This helical continuity extends the known four-helix core [SNARE Complex](/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/) into the membrane, suggesting that the final phase of SNARE assembly is directly coupled to membrane merger.

### Aromatic layer stabilizes linker region

The linker region contains a collar of aromatic residues surrounded predominantly by basic residues. Tyr 257 is deeply buried in a pocket formed by three flanking lysine residues of syntaxin-1A (Lys 253, Lys 256, Lys 260) and four residues of [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) (Lys 85, Arg 86, Trp 89, Asn 92). Mutation of Tyr 257 to alanine reduced thermal stability, demonstrating that intermolecular side-chain contacts in the aromatic layer are crucial for complex stability.

### Transmembrane region interactions drive complex association

In the crystal, hydrophobic contacts between the transmembrane regions of [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) and syntaxin-1A mediate the association of four complexes through their TMRs, forming an X-shaped assembly. Four [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) TMRs build the core, surrounded by four syntaxin-1A TMRs. Residues Ile 268, Cys 271, Ile 274, and Leu 275 in syntaxin-1A contribute largely to the interaction surface with [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) TMRs.

### Linkers and TMRs add thermal stability

The complex including linkers and TMRs of syntaxin-1A and [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) was significantly more resistant to thermal and chemical denaturation than the core complex alone. The crystallization complex unfolded at approximately 97 C in CD spectroscopy thermal unfolding experiments. Presence of syntaxin-1A TMR alone provided stability comparable to the core complex.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/">Synaptobrevin-2 (Rat Neuronal Qb-SNARE Protein)</a> — Core SNARE complex partner; forms continuous helical bundle with syntaxin-1A through SNARE motif, linker, and TMR
- <a href="/xray-mp-wiki/proteins/structural-adhesion/snap-25a/">SNAP-25A (Rat Neuronal Qbc-SNARE Protein)</a> — Third component of the neuronal SNARE complex; anchors to plasma membrane via palmitoyl chains
- <a href="/xray-mp-wiki/proteins/structural-adhesion/tlg2/">Tlg2 (Cryptococcus thermophilum Qa-SNARE Protein)</a> — Homologous Qa-SNARE protein from endosomal system; also has Habc domain and SNARE motif
- <a href="/xray-mp-wiki/reagents/detergents/nonylglucoside/">Nonylglucoside (NG)</a> — n-nonyl beta-D-glucopyranoside used as detergent for crystallization of SNARE complex
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl beta-D-glucopyranoside (OG)</a> — n-octyl beta-D-glucopyranoside used in purification buffer (50 mM) for syntaxin-1A
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — 20 mM Tris pH 8.8 used in desalting and ion exchange purification buffer
- <a href="/xray-mp-wiki/reagents/additives/tcep/">Tris-(2-carboxyethyl)phosphine (TCEP)</a> — 1 mM TCEP used in desalting buffer for syntaxin-1A purification
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/">SNARE Complex</a> — Syntaxin-1A is the Qa-SNARE component of the four-helix bundle SNARE complex
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
