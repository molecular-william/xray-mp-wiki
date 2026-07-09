---
title: "Fluoride Channel from B. pertussis (Bpe)"
created: 2026-05-29
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2018.02.004, doi/10.1038##NATURE14981]
verified: regex
uniprot_id: Q7VYU0
---

# Fluoride Channel from B. pertussis (Bpe)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q7VYU0">UniProt: Q7VYU0</a>

<span class="expr-badge">Bordetella PERTUSSIS</span>

## Overview

The fluoride channel from [Bordetella pertussis](/xray-mp-wiki/organisms/bordetella-pertussis) (Bpe) is a member of the Fluc family of fluoride-specific ion channels. Bpe assembles as a symmetrical homodimer with antiparallel transmembrane topology, such that the channel's intracellular and extracellular ion entryways are structurally identical. Each subunit contributes residues to both of the channel's two F- permeation pathways. Bpe crystallization requires engineered monobody chaperones (S7, L2, S8, etc.) that bind to both ends of the channel dimer. The channel forms a dual-topology homodimer where each subunit spans the membrane in opposite orientation, a defining feature of the Fluc family. High-resolution structures (PDB 5A40 at 3.6 A, 5A41 at 2.1 A) reveal a double-barrelled architecture with two F- permeation pathways, a centrally coordinated Na+ ion in the channel plug, and F- ion binding sites at conserved positions involving phenylalanine quadrupole interactions.


## Publications

### doi/10.1016##j.str.2018.02.004

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bqo">6BQO</a></td>
      <td>2.8</td>
      <td>C 1 2 1</td>
      <td>Bpe fluoride channel homodimer from B. pertussis with monobody S8 bound to one end</td>
      <td>Monobody S8 (~950 A^2 hydrophobic interface, peripheral hydrogen bonds and salt bridges)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli. Bpe from B. pertussis was expressed from pET21c vector with C-terminal hexahistidine tag, as described in Stockbridge et al. 2013.

- **Construct**: Bpe fluoride channel homodimer from B. pertussis, full-length with C-terminal hexahistidine tag.


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
      <td><a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a> expression</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Bpe expressed from pET21c with C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">hexahistidine tag</a> in <a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a>, as described in Stockbridge et al. 2013</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> (via <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">hexahistidine tag</a>)</td>
      <td>-- + --</td>
      <td>Purification as described in Stockbridge et al. 2013</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">In meso</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Bpe-Fluc homodimer in detergent, co-complexed with <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s8/">monobody S8</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared in 2-3 days in several low molecular weight <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a>s including 30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a>, <a href="/xray-mp-wiki/reagents/additives/peg-550mme/">PEG 550MME</a>, and <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a>. Final optimized crystals grown in 26% <a href="/xray-mp-wiki/reagents/additives/peg-550mme/">PEG 550MME</a>, 0.1M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> pH 5.0. Data collected at beam-line I04 Diamond Light Source, UK. Space group C 1 2 1.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bqo">6BQO</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ML</span><span class="topo-outside">TYAP</span><span class="topo-membrane">LNFIAIGIGATLGAWLRWVLGLKLNG</span><span class="topo-inside">AGW</span><span class="topo-membrane">PWGTLTANLVGGYLIGVMV</span><span class="topo-outside">ALIASHPEWPAWIR</span><span class="topo-membrane">LAAVTGFLGGLTTFSTFSAETV</span><span class="topo-inside">DMLCRGVYAT</span><span class="topo-membrane">AAAYAGASLAGSLAMTGLGL</span></span>
<span class="topo-ruler">        </span>
<span class="topo-line"><span class="topo-membrane">AT</span><span class="topo-outside">VRLLLR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>3</td>
      <td>6</td>
      <td>3</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>32</td>
      <td>7</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>35</td>
      <td>33</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>54</td>
      <td>36</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>68</td>
      <td>55</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>90</td>
      <td>69</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>100</td>
      <td>91</td>
      <td>100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>122</td>
      <td>101</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>128</td>
      <td>123</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bqo">6BQO</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90     </span>
<span class="topo-line"><span class="topo-inside">SSVPTKLEVVAATPTSLLISWDAPAVTVDHYVITYGETGAYWSYQEFTVPGSKSTATISGLKPGVDYTITVYANPYSDAPIYYSYHSPISINYRT</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>95</td>
      <td>3</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##NATURE14981

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5a40">5A40</a></td>
      <td>3.6</td>
      <td>P 21 21 2</td>
      <td>Bpe fluoride channel homodimer from B. pertussis with monobody S7 bound to both ends</td>
      <td>Monobody S7, Na+ (centrally coordinated), Hg (labelling site)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5a41">5A41</a></td>
      <td>2.1</td>
      <td>P 1</td>
      <td>Bpe fluoride channel homodimer from B. pertussis with monobody L2 bound to both ends</td>
      <td>Monobody L2, Na+ (centrally coordinated), F- (putative, F1 and F2 sites)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli. Bpe from B. pertussis was expressed from pET21c vector with C-terminal hexahistidine tag, as described in Stockbridge et al. 2013.

- **Construct**: Bpe fluoride channel homodimer from B. pertussis, full-length with C-terminal hexahistidine tag.


**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a> (<a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting drop</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Bpe-Fluc homodimer in detergent, co-complexed with <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s7/">monobody S7</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in detail</td>
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
      <td>Notes</td>
      <td>Crystals grown from detergent micelles. <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s7/">Monobody S7</a> was required for crystallization; crystals could not be grown without monobody. <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">SAD phasing</a> with Hg-labelled Bpe at unique cysteine residue (E94C). Space group P21212. Resolution 3.6 Angstrom.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a> (<a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting drop</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Bpe-Fluc homodimer in detergent, co-complexed with <a href="/xray-mp-wiki/reagents/protein-tags/monobody-l2/">monobody L2</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in detail</td>
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
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">In meso</a> crystallization attempt. Crystals diffracting to 2.1 Angstrom obtained in presence of 20 mM F-. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a>. Space group P1. <a href="/xray-mp-wiki/reagents/protein-tags/monobody-l2/">Monobody L2</a> binds in different orientation than S7 but also extends long loop into vestibule.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5a40">5A40</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">LTY</span><span class="topo-membrane">APLNFIAIGIGATLGAWLRWVLGLKLNG</span><span class="topo-inside">AGW</span><span class="topo-membrane">PWGTLTANLVGGYLIGVMV</span><span class="topo-outside">ALIASHPEWPAWIR</span><span class="topo-membrane">LAAVTGFLGGLTTFSTFSAET</span><span class="topo-inside">VDMLCRGVYATAA</span><span class="topo-membrane">AYAGASLAGSLAMTGLGL</span></span>
<span class="topo-ruler">        </span>
<span class="topo-line"><span class="topo-membrane">AT</span><span class="topo-outside">VRLLLR</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>32</td>
      <td>5</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>35</td>
      <td>33</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>54</td>
      <td>36</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>68</td>
      <td>55</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>89</td>
      <td>69</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>102</td>
      <td>90</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>122</td>
      <td>103</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>128</td>
      <td>123</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Double-barrelled channel architecture

The 2.1 A Bpe-L2 structure reveals a surprising double-barrelled channel architecture in which two F- ion pathways span the membrane. The channel is hourglass-shaped, with wide vestibules symmetrically opening to two aqueous solutions separated by a solid plug of protein 10-15 A thick. Each F- permeation pathway is lined with H-bond donors along TM4, creating a polar track through which largely dehydrated F- ions move across the membrane. The narrow pores and unusual anion coordination exploiting quadrupolar edges of conserved phenylalanine rings provide the basis for F- selectivity over Cl- by >10^4.

### Centrally coordinated Na+ ion in the channel plug

A prominent electron density resides in the centre of the plug separating the vestibules, precisely on the homodimer's two-fold non-crystallographic axis. This density is identified as a Na+ ion coordinated by four backbone carbonyl groups from residues in each subunit associated with the conserved TM3 break (G77 and T80). This coordination is inconsistent with F-, water, a divalent metal, or K+. The deeply buried cation could not exchange with aqueous solution if the plug remained intact, and it is proposed to be an important structural component incorporated irreversibly upon dimer assembly.

### F- ion binding sites at F1 and F2 positions

Four electron densities in the Bpe-L2 structure are identified as F- ions at F1 and F2 sites in non-crystallographic symmetry-related pairs. These sites are located in crevices between TM2, TM3b, and TM4 near the periphery of the channel. The crevice-facing surface of TM4 is lined with H-donating side chains (Y104, S108, S112, T116 in Bpe), creating a polar track along which F- ions move. The conserved phenylalanine residues (F82, F85) provide unusual edge-on coordination exploiting their quadrupolar edges for F- recognition. Mutations F85I and F82I reduce F- efflux by two and three orders of magnitude, respectively.

### Channsporter mechanism for F- permeation

The conduction mechanism for F- transport through Fluc channels is proposed to be distinct from classic diffusion through a fixed, water-filled channel. Instead, F- moves along the pore concomitant with a rotameric switch of the conserved N43 side chain, such that the amide nitrogen remains H-bonded as the anion moves along the pore. This mechanism incorporates a central feature of membrane transporters: substrate transport coupled to concerted movement of the protein. The four F- ions observed probably occupy the channel simultaneously, suggesting multi-ion conduction phenomena akin to those in K+ channels.

### Cork-in-bottle occlusion mechanism

The Bpe-S8 structure provides direct structural evidence that monobody binding does not induce local structural changes in the fluoride channel. Only one end of the channel binds a monobody, yet both ends are structurally identical and identical to all previously solved doubly complexed structures. The monobody's diversified loop physically occludes the aqueous vestibule through which fluoride ions enter and leave the transport pathway, acting as a "cork" in a bottle. This mechanism of physical occlusion rather than allosteric closure explains why the channel structure represents the functional, F- conducting conformation.

### Dual-topology homodimer structure

Bpe assembles as a symmetrical homodimer with antiparallel transmembrane topology. The two subunits are arranged such that intracellular and extracellular ion entryways are structurally identical. The channel dimer contains two F- permeation pathways, with each subunit contributing residues to both pathways. This dual-topology arrangement is a defining feature of the Fluc family of fluoride channels.

### Monobody-channel interface

The Bpe-S8 monobody interface is ~950 A^2 and mainly hydrophobic. Hydrogen bonds and salt bridges between S8 and the channel are rare and peripheral. The only polar monobody/channel interactions within H-bonding distance are between D80 (S8) and T3 (channel) at the periphery, the carbonyl oxygen of Y43 (S8) and the backbone amide of Y98 (channel) at the opposite periphery, and a salt bridge between E48 (S8) and the channel at the periphery.


## Cross-References

- <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s7/">Monobody S7</a> — Engineered protein inhibitor used to crystallize Bpe-S7 complex (PDB 5A40, 3.6 A)
- <a href="/xray-mp-wiki/reagents/protein-tags/monobody-l2/">Monobody L2</a> — Engineered protein inhibitor used to crystallize Bpe-L2 complex (PDB 5A41, 2.1 A)
- <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s9/">Monobody S9</a> — Engineered protein inhibitor used to crystallize Ec2-S9 complex (PDB 5A43); homologous monobody family
- <a href="/xray-mp-wiki/proteins/other-ion-channels/fluc-ec2/">Fluoride Channel from E. coli (Ec2)</a> — Ec2 is the E. coli Fluc homologue; identical fold with 33% sequence identity; Ec2-S9 structure confirms conserved F- binding sites
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for Bpe purification and crystallization (5 mM)
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Buffer used in Bpe purification and crystallization (10 mM, pH 7.0)
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — NaF used in Bpe purification buffer (100 mM) for fluoride channel activity
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/dual-topology-channels/">Dual-Topology Channels</a> — Bpe is a dual-topology homodimer; 2.1 A structure confirms double-barrelled architecture
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a> — Crystallization method used for structure determination
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> — Structure determination method used
