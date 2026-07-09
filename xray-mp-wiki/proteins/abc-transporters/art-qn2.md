---
title: "Art(QN)2 ABC Amino Acid Importer from Thermoanaerobacter tengcongensis"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1415037112]
verified: regex
uniprot_id: ['Q8RCC2', 'Q8RCC3']
---

# Art(QN)2 ABC Amino Acid Importer from Thermoanaerobacter tengcongensis

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8RCC2">UniProt: Q8RCC2</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8RCC3">UniProt: Q8RCC3</a>

<span class="expr-badge">Caldanaerobacter subterraneus subsp. tengcongensis MB4</span>

## Overview

Art(QN)2 is a homodimeric type I ABC importer from the thermophilic bacterium Thermoanaerobacter tengcongensis that transports positively charged amino acids (Arg, His). The complex consists of two transmembrane domains (ArtQ) and two nucleotide-binding domains (ArtN). Crystal structures were determined in the apo form, in complex with Arg, His, and/or [ATP](/xray-mp-wiki/reagents/ligands/atp/) at resolutions ranging from 2.5 to 3.0 A. The structures reveal that the transmembrane domains straddle around the twofold axis to form a substrate translocation pathway across the membrane. Each ArtQ subunit contains a highly negatively charged pocket, and together they create a negatively charged internal tunnel that allows amino acids carrying positively charged side chains to pass through. This represents the first structural characterization, to our knowledge, of an amino acid-binding site within the transmembrane domains of an ABC importer. The cognate solute-binding protein ArtI was also crystallized in complex with Arg at 1.48 A resolution.

## Publications

### doi/10.1073##pnas.1415037112

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a></td>
      <td>2.8</td>
      <td>—</td>
      <td>Full-length Art(QN2 complex from T. tengcongensis, apo form</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a></td>
      <td>2.6</td>
      <td>—</td>
      <td>Full-length Art(QN2 complex with Arg bound</td>
      <td>Arg</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a></td>
      <td>2.8</td>
      <td>—</td>
      <td>Full-length Art(QN2 complex with His bound</td>
      <td>His</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a></td>
      <td>3.0</td>
      <td>—</td>
      <td>Full-length Art(QN2 complex with ATP bound</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a></td>
      <td>2.5</td>
      <td>—</td>
      <td>Full-length Art(QN2 complex with Arg and ATP bound</td>
      <td>Arg, <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a></td>
      <td>1.48</td>
      <td>—</td>
      <td>Cognate solute-binding protein ArtI complexed with Arg</td>
      <td>Arg</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43 (for Art(QN2; E. coli BL21 (for ArtI
- **Construct**: Full-length ArtQ (C-terminal 6x His tag and ArtN coexpressed from pACYCDuet vector; full-length ArtI (C-terminal 6x His tag expressed from pet21b vector

**Purification:**

- **Expression system**: E. coli C43
- **Expression construct**: Art(QN2 with ArtQ C-terminal 6x His tag
- **Tag info**: 6x His tag on ArtQ

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
      <td>Fermentation</td>
      <td>—</td>
      <td></td>
      <td>E. coli C43 expressing Art(QN2 from pACYCDuet vector</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td></td>
      <td>Purification via 6x His tag on ArtQ</td>
    </tr>
  </tbody>
</table>

- **Expression system**: E. coli BL21
- **Expression construct**: ArtI with C-terminal 6x His tag
- **Tag info**: 6x His tag on ArtI

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
      <td>Fermentation</td>
      <td>—</td>
      <td></td>
      <td>E. coli BL21 expressing ArtI from pet21b vector</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td></td>
      <td>ArtI purification, followed by denaturation/renaturation to remove prebound substrate</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified Art(QN)₂ complex</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at Shanghai Synchrotron Radiation Facility Beamline BL17U. Structure solved by molecular replacement.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified ArtI with Arg</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>ArtI-Arg complex solved at 1.48 Å resolution</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain J (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain D (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRLR</span><span class="topo-unknown">AGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>215</td>
      <td>208</td>
      <td>215</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRL</span><span class="topo-unknown">RAGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>214</td>
      <td>208</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain J (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain D (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRLR</span><span class="topo-unknown">AGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>215</td>
      <td>208</td>
      <td>215</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRL</span><span class="topo-unknown">RAGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>214</td>
      <td>208</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain J (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain D (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRLR</span><span class="topo-unknown">AGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>215</td>
      <td>208</td>
      <td>215</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRL</span><span class="topo-unknown">RAGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>214</td>
      <td>208</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain J (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain D (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRLR</span><span class="topo-unknown">AGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>215</td>
      <td>208</td>
      <td>215</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRL</span><span class="topo-unknown">RAGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>214</td>
      <td>208</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain J (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain D (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRLR</span><span class="topo-unknown">AGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>215</td>
      <td>208</td>
      <td>215</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRL</span><span class="topo-unknown">RAGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>214</td>
      <td>208</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain J (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIFVNDVYKNFGSLEVLKGVTLKVNKGEVVVIIGPSGSGKSTLLRCINLLEEPTKGEVFIDGVKINNGKVNINKVRQKVGMVFQHFNLFPHLTAIENITLAPVKVKKMNKKEAEELAVDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LAKVGLLDKKDQYPIKLSGGQKQRLAIARALAMQPEVMLFDEPTSALDPEMVKEVLNVMKQLANEGMTMVVVTHEMGFAREVGDRVIFMDDGVIVEEGTPEEIFYRAKNERTREFLSKIL</span></span>
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
      <td>240</td>
      <td>1</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain D (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRLR</span><span class="topo-unknown">AGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>215</td>
      <td>208</td>
      <td>215</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yms">4YMS</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTV</span><span class="topo-membrane">DFLSMVKYTPLFISGLIMTLKLTFLAVTIGVLMGLFIALMK</span><span class="topo-inside">MSSI</span><span class="topo-membrane">KPIKLVASSYIEVIRGTPLLVQLLLIYNGL</span><span class="topo-outside">MQFGMNI</span><span class="topo-membrane">PAFTAGVSALAINSSAYVAEII</span><span class="topo-inside">RAGIQAVDPGQNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220</span>
<span class="topo-line"><span class="topo-inside">AARSLGMTHAMAMRYVIIPQAIKNIL</span><span class="topo-membrane">PALGNEFIVMLKESAIVSVIGF</span><span class="topo-outside">ADLTRQADIIQSVTYRY</span><span class="topo-membrane">FEPYIIIAAIYFVMTLTFSKLL</span><span class="topo-inside">SLFERRL</span><span class="topo-unknown">RAGDIR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>44</td>
      <td>4</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>146</td>
      <td>108</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>207</td>
      <td>186</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>214</td>
      <td>208</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### First structural basis of substrate specificity in an amino acid ABC importer TMD

The Art(QN)₂ complex contains two substrate-binding sites, one per ArtQ subunit, located at the interface between the two ArtQ subunits, reaching halfway across the predicted membrane bilayer from the periplasmic surface. Each binding pocket is highly negatively charged, creating an electrostatic tunnel that allows positively charged amino acids (Arg, His) to pass through. Key residues involved in substrate binding include ArtQ-Pro66, ArtQ-Leu67, ArtQ-Asn98, ArtQ-Tyr102, ArtQ-Glu152, ArtQ-Glu159, ArtQ-Val155, and ArtQ-Met156. These residues are highly conserved across species.

### Inward-facing conformation with semi-open NBD dimer

The ArtQ dimer adopts an inward-facing conformation open to the cytoplasm, while the ArtN dimer exists in a semi-open state. Two ATP molecules are bound at the Walker A and Walker B motifs. No obvious conformational changes were observed between apo, Arg-bound, ATP-bound, and Arg/ATP-bound forms (RMSD < 0.2 Å), indicating that the transition to the outward-facing state requires the cognate solute-binding protein ArtI.

### Functional coupling requires ArtI SBP

Art(QN)₂ exhibits low spontaneous ATPase activity that is stimulated approximately fourfold by Arg- or His-loaded ArtI. The ATPase activity is sensitive to ortho-vanadate. A mutation at the key binding residue ArtQ-E152A resulted in substantially increased basal and stimulated ATPase activity, suggesting the mutation uncouples ATP hydrolysis from transport regulation.

### Homodimeric type I ABC importer architecture

ArtQ contains five transmembrane segments (TM1-TM5), with TM1 wrapping around the outer membrane-facing surface and TM2-TM5 adopting an up-down topology lining the translocation pathway. This fold is similar to MetI of the E. coli methionine uptake system (RMSD ~2.6 Å). The EAA-X(3)-G motif mediates interactions between ArtQ and ArtN subunits.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kir2-2-channel/">Chicken Kir2.2 Inward Rectifier K+ Channel</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mscs/">E. coli MscS (Mechanosensitive Channel of Small Conductance)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/gpcr/turkey-beta1-ar-ligand-free-basal/">Turkey Beta1-Adrenergic Receptor Ligand-Free Basal State</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/abc-transporters/malG/">MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/pumps-atpases/yeast-v-atpase-subunits-d-f-scdf/">Yeast V-ATPase Subunits D and F (ScDF Assembly)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/gpcr/rhodopsin-2-2a/">Bovine Rhodopsin (2.2 A Resolution, PDB 1U19)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/abc-transporters/malF/">MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mscs-a106v/">E. coli MscS Mechanosensitive Channel (A106V Open Form)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/gpcr/trex1/">Mouse TREX1 (Three Prime Repair Exonuclease 1)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/abc-transporters/aaprtd/">Aquifex aeolicus PrtD (AaPrtD) Type-1 Secretion System ABC Transporter</a> — Related protein structure; referenced in text
