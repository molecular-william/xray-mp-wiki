---
title: "KirBac Potassium Channels"
created: 2026-05-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1085028, doi/10.1016##J.CELL.2010.05.003, doi/10.1038##NSMB.2208, doi/10.3390##ijms23010335, doi/10.1038##s41467-020-16842-0, doi/10.1074##jbc.M113.501833]
verified: regex
uniprot_id: ['D9N164', 'P83698', 'Q2W6R1']
---

# KirBac Potassium Channels

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/D9N164">UniProt: D9N164</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P83698">UniProt: P83698</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q2W6R1">UniProt: Q2W6R1</a>

<span class="expr-badge">Magnetospirillum magnetotacticum</span>

## Overview

KirBac1.1 and KirBac3.1 are prokaryotic inward-rectifier potassium channels from Magnetospirillum magnetotactium that serve as structural models for eukaryotic Kir channels. A comparative analysis of 11 KirBac crystal structures (KirBac1.1 at 3.7 A and multiple KirBac3.1 structures at 2.6-4.2 A resolution) revealed interdependent gates in the conduction pathway and the mechanism of polyamine block, including interdomain conformational changes coupled to ion configuration in the selectivity filter, identification of two polyamine-binding sites, and a staged activation pathway via two-fold symmetric intermediates. The first open-state structure of a KirBac channel was obtained using the S129R gating mutant of KirBac3.1 (3.05 A resolution), which traps the helix bundle crossing in an open conformation. This structure demonstrates that TM2 bends at a conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) hinge (Gly120) and rotates approximately 25 degrees to open both the bundle-crossing gate (Tyr132) and a secondary constriction at Leu124. Contrary to prior models, this open structure adopts a twist conformation yet maintains a conductive selectivity filter with all four K+ binding sites occupied. A network of interactions between the TMD and CTD — involving the C-linker, slide helix, G-loop, and CD loop — couples rotational movement of the cytoplasmic domain to opening of the bundle-crossing gate. Crosslinking experiments on KirBac3.1 (PDB 6O9T, 6O9U, 6O9V) challenged the canonical gating model by showing that covalently constraining the Tyr132 intracellular collar to prevent widening does not impair K+ conduction. MD simulations reveal that K+ ions transiently lose 3-4 water molecules from their hydration shell to pass through the constriction, with a low free-energy barrier to partial dehydration. These findings demonstrate that Kir channels do not require the canonical pore-dilation gating mechanism and suggest the selectivity filter or lipid-mediated changes may be the primary gate.

## Publications

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.1085028 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1p7b">1P7B</a></td>
      <td>3.65 A</td>
      <td>I222</td>
      <td>Full-length KirBac1.1</td>
      <td>Mg2+ ions</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 (DE3) star
- **Construct**: Full-length histidine-tagged recombinant KirBac3.1 from Magnetospirillum magnetotactium. Q170A mutant expressed separately for comparison.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1p7b">1P7B</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNVDPFSPHSSDSFAQAASPARKPPRGGRRIWSGT</span><span class="topo-outside">REVIAYGMPAS</span><span class="topo-unknown">VWRDLYYWALK</span><span class="topo-outside">VSW</span><span class="topo-membrane">PVFFASLAALFVVNNTLFALLYQLG</span><span class="topo-inside">DAPIANQSPPGF</span><span class="topo-unknown">VGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YAHAIATLEIFVGMSGIALSTGLV</span><span class="topo-outside">FARFARPRAKIMFARHAIVRPFNGRMTLMVRAANARQNVIAEARAKMRLM</span><span class="topo-unknown">RREHSSEGYS</span><span class="topo-outside">LMKIHDLKLVRNEHPIFLLGWNMMHVIDESSPLFG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-outside">ETPESLAEGRAMLLVMIEGSDETTAQVMQARHAWEHDDIRWHHRYVDLM</span><span class="topo-unknown">SDVDGM</span><span class="topo-outside">THIDYTRFNDTEPV</span><span class="topo-unknown">EPPGAAPDAQAFAAKPGEGDARPV</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>35</td>
      <td>1</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>57</td>
      <td>47</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>85</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>97</td>
      <td>86</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>114</td>
      <td>98</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>122</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>195</td>
      <td>146</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>205</td>
      <td>196</td>
      <td>205</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>206</td>
      <td>289</td>
      <td>206</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>295</td>
      <td>290</td>
      <td>295</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>296</td>
      <td>309</td>
      <td>296</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>333</td>
      <td>310</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1p7b">1P7B</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNVDPFSPHSSDSFAQAASPARKPPRGGRRIWSGT</span><span class="topo-outside">REVIAYGMPAS</span><span class="topo-unknown">VWRDLYYWALK</span><span class="topo-outside">VSW</span><span class="topo-membrane">PVFFASLAALFVVNNTLFALLYQLG</span><span class="topo-inside">DAPIANQSPPGF</span><span class="topo-unknown">VGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YAHAIATLEIFVGMSGIALSTGLV</span><span class="topo-outside">FARFARPRAKIMFARHAIVRPFNGRMTLMVRAANARQNVIAEARAKMRLM</span><span class="topo-unknown">RREHSSEGYS</span><span class="topo-outside">LMKIHDLKLVRNEHPIFLLGWNMMHVIDESSPLFG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-outside">ETPESLAEGRAMLLVMIEGSDETTAQVMQARHAWEHDDIRWHHRYVDLM</span><span class="topo-unknown">SDVDGM</span><span class="topo-outside">THIDYTRFNDTEPV</span><span class="topo-unknown">EPPGAAPDAQAFAAKPGEGDARPV</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>35</td>
      <td>1</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>57</td>
      <td>47</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>85</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>97</td>
      <td>86</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>114</td>
      <td>98</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>122</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>195</td>
      <td>146</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>205</td>
      <td>196</td>
      <td>205</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>206</td>
      <td>289</td>
      <td>206</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>295</td>
      <td>290</td>
      <td>295</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>296</td>
      <td>309</td>
      <td>296</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>333</td>
      <td>310</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1p7b">1P7B</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNVDPFSPHSSDSFAQAASPARKPPRGGRRIWSGT</span><span class="topo-outside">REVIAYGMPAS</span><span class="topo-unknown">VWRDLYYWALK</span><span class="topo-outside">VSW</span><span class="topo-membrane">PVFFASLAALFVVNNTLFALLYQLG</span><span class="topo-inside">DAPIANQSPPGF</span><span class="topo-unknown">VGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YAHAIATLEIFVGMSGIALSTGLV</span><span class="topo-outside">FARFARPRAKIMFARHAIVRPFNGRMTLMVRAANARQNVIAEARAKMRLM</span><span class="topo-unknown">RREHSSEGYS</span><span class="topo-outside">LMKIHDLKLVRNEHPIFLLGWNMMHVIDESSPLFG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-outside">ETPESLAEGRAMLLVMIEGSDETTAQVMQARHAWEHDDIRWHHRYVDLM</span><span class="topo-unknown">SDVDGM</span><span class="topo-outside">THIDYTRFNDTEPV</span><span class="topo-unknown">EPPGAAPDAQAFAAKPGEGDARPV</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>35</td>
      <td>1</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>57</td>
      <td>47</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>85</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>97</td>
      <td>86</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>114</td>
      <td>98</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>122</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>195</td>
      <td>146</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>205</td>
      <td>196</td>
      <td>205</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>206</td>
      <td>289</td>
      <td>206</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>295</td>
      <td>290</td>
      <td>295</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>296</td>
      <td>309</td>
      <td>296</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>333</td>
      <td>310</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1p7b">1P7B</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNVDPFSPHSSDSFAQAASPARKPPRGGRRIWSGT</span><span class="topo-outside">REVIAYGMPAS</span><span class="topo-unknown">VWRDLYYWALK</span><span class="topo-outside">VSW</span><span class="topo-membrane">PVFFASLAALFVVNNTLFALLYQLG</span><span class="topo-inside">DAPIANQSPPGF</span><span class="topo-unknown">VGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YAHAIATLEIFVGMSGIALSTGLV</span><span class="topo-outside">FARFARPRAKIMFARHAIVRPFNGRMTLMVRAANARQNVIAEARAKMRLM</span><span class="topo-unknown">RREHSSEGYS</span><span class="topo-outside">LMKIHDLKLVRNEHPIFLLGWNMMHVIDESSPLFG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-outside">ETPESLAEGRAMLLVMIEGSDETTAQVMQARHAWEHDDIRWHHRYVDLM</span><span class="topo-unknown">SDVDGM</span><span class="topo-outside">THIDYTRFNDTEPV</span><span class="topo-unknown">EPPGAAPDAQAFAAKPGEGDARPV</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>35</td>
      <td>1</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>57</td>
      <td>47</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>85</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>97</td>
      <td>86</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>114</td>
      <td>98</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>122</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>195</td>
      <td>146</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>205</td>
      <td>196</td>
      <td>205</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>206</td>
      <td>289</td>
      <td>206</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>295</td>
      <td>290</td>
      <td>295</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>296</td>
      <td>309</td>
      <td>296</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>333</td>
      <td>310</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1016##J.CELL.2010.05.003 (11 structures, 12 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1p7b">1P7B</a></td>
      <td>3.7 A</td>
      <td>I222</td>
      <td>Full-length KirBac1.1 with His-tag</td>
      <td>Mg2+ (blocked configuration)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1xl4">1XL4</a></td>
      <td>2.6 A</td>
      <td>P21212</td>
      <td>Full-length KirBac3.1 with His-tag</td>
      <td>Ca2+ (blocked), <a href="/xray-mp-wiki/reagents/additives/spermine/">Spermine</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1xl6">1XL6</a></td>
      <td>2.8 A</td>
      <td>C2221</td>
      <td>Full-length KirBac3.1 with His-tag</td>
      <td><a href="/xray-mp-wiki/reagents/additives/spermine/">Spermine</a> (conduction-compromised)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/structure iii">STRUCTURE III</a></td>
      <td>3.1 A</td>
      <td>P21212</td>
      <td>Full-length KirBac3.1 with His-tag</td>
      <td>none (stalled twist conformation)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/structure iv">STRUCTURE IV</a></td>
      <td>3.3 A</td>
      <td>I222</td>
      <td>Full-length KirBac3.1 with His-tag</td>
      <td>none (stalled twist conformation)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/structure v">STRUCTURE V</a></td>
      <td>3.5 A</td>
      <td>C2221</td>
      <td>Full-length KirBac3.1 with His-tag</td>
      <td>none (stalled twist conformation)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/structure vi">STRUCTURE VI</a></td>
      <td>3.8 A</td>
      <td>P1</td>
      <td>Full-length KirBac3.1 with His-tag</td>
      <td>none (unlatched, conducting twist conformation)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/structure vii">STRUCTURE VII</a></td>
      <td>4.2 A</td>
      <td>P212121</td>
      <td>Full-length KirBac3.1 with His-tag</td>
      <td>none (stalled twist conformation)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/structure ix">STRUCTURE IX</a></td>
      <td>3.2 A</td>
      <td>P21212</td>
      <td>Full-length KirBac3.1 with His-tag</td>
      <td>none (twist conformation)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/structure x">STRUCTURE X</a></td>
      <td>3.0 A</td>
      <td>P21212</td>
      <td>Full-length KirBac3.1 with His-tag</td>
      <td>Ba2+ (blocked configuration)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/structure xi">STRUCTURE XI</a></td>
      <td>2.9 A</td>
      <td>P21212</td>
      <td>Full-length KirBac3.1 with His-tag</td>
      <td>Sm3+ (nontwist, conducting conformation)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 (DE3) star
- **Construct**: Full-length histidine-tagged recombinant KirBac3.1 from Magnetospirillum magnetotactium. Q170A mutant expressed separately for comparison.

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
      <td>High-pressure homogenization</td>
      <td>--</td>
      <td>Not specified + --</td>
      <td>Cells lysed at 20,000 psi in a high-pressure homogenizer</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>-- + 1% <a href="/xray-mp-wiki/reagents/detergents/anzergent-3-12/">Anzergent 3,12</a> at room temperature for 1 hr</td>
      <td>Cellular debris removed by centrifugation after solubilization</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni2+-loaded IMAC resin</td>
      <td>Ni2+-IMAC</td>
      <td>-- + 1% <a href="/xray-mp-wiki/reagents/detergents/anzergent-3-12/">Anzergent 3,12</a></td>
      <td>His-tagged KirBac3.1 purified by <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>--</td>
      <td>-- + 1% <a href="/xray-mp-wiki/reagents/detergents/anzergent-3-12/">Anzergent 3,12</a></td>
      <td>Peak fractions pooled after SEC</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Ultrafiltration</td>
      <td>Amicon</td>
      <td>-- + --</td>
      <td>Concentrated to ~8 mg/ml for crystallization</td>
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
      <td>Purified KirBac3.1 at ~8 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350 + 0.2 M calcium chloride + 0.1 M HEPES buffer pH 7.5 (III); 15% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350 + 0.1 M <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a> + 0.1 M <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> buffer pH 5.6 (VI); 20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350 + 0.2 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> + 0.1 M HEPES buffer pH 7.5 (VIII); 20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350 + 0.2 M <a href="/xray-mp-wiki/reagents/additives/spermine/">Spermine</a> + 0.1 M HEPES buffer pH 8.0 (XI)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>19-20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals soaked in 50 mM <a href="/xray-mp-wiki/reagents/additives/spermine/">Spermine</a> prior to data collection (structures II and VIII)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized at Bio21 C3 facility. Structures III-VII phased by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using 1XL4/1XL6. Q170A mutant crystallized separately. Structure XI soaked with Sm3+ to capture nontwist form.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1p7b">1P7B</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNVDPFSPHSSDSFAQAASPARKPPRGGRRIWSGT</span><span class="topo-outside">REVIAYGMPAS</span><span class="topo-unknown">VWRDLYYWALK</span><span class="topo-outside">VSW</span><span class="topo-membrane">PVFFASLAALFVVNNTLFALLYQLG</span><span class="topo-inside">DAPIANQSPPGF</span><span class="topo-unknown">VGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YAHAIATLEIFVGMSGIALSTGLV</span><span class="topo-outside">FARFARPRAKIMFARHAIVRPFNGRMTLMVRAANARQNVIAEARAKMRLM</span><span class="topo-unknown">RREHSSEGYS</span><span class="topo-outside">LMKIHDLKLVRNEHPIFLLGWNMMHVIDESSPLFG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-outside">ETPESLAEGRAMLLVMIEGSDETTAQVMQARHAWEHDDIRWHHRYVDLM</span><span class="topo-unknown">SDVDGM</span><span class="topo-outside">THIDYTRFNDTEPV</span><span class="topo-unknown">EPPGAAPDAQAFAAKPGEGDARPV</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>35</td>
      <td>1</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>57</td>
      <td>47</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>85</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>97</td>
      <td>86</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>114</td>
      <td>98</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>122</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>195</td>
      <td>146</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>205</td>
      <td>196</td>
      <td>205</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>206</td>
      <td>289</td>
      <td>206</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>295</td>
      <td>290</td>
      <td>295</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>296</td>
      <td>309</td>
      <td>296</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>333</td>
      <td>310</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1p7b">1P7B</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNVDPFSPHSSDSFAQAASPARKPPRGGRRIWSGT</span><span class="topo-outside">REVIAYGMPAS</span><span class="topo-unknown">VWRDLYYWALK</span><span class="topo-outside">VSW</span><span class="topo-membrane">PVFFASLAALFVVNNTLFALLYQLG</span><span class="topo-inside">DAPIANQSPPGF</span><span class="topo-unknown">VGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YAHAIATLEIFVGMSGIALSTGLV</span><span class="topo-outside">FARFARPRAKIMFARHAIVRPFNGRMTLMVRAANARQNVIAEARAKMRLM</span><span class="topo-unknown">RREHSSEGYS</span><span class="topo-outside">LMKIHDLKLVRNEHPIFLLGWNMMHVIDESSPLFG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-outside">ETPESLAEGRAMLLVMIEGSDETTAQVMQARHAWEHDDIRWHHRYVDLM</span><span class="topo-unknown">SDVDGM</span><span class="topo-outside">THIDYTRFNDTEPV</span><span class="topo-unknown">EPPGAAPDAQAFAAKPGEGDARPV</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>35</td>
      <td>1</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>57</td>
      <td>47</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>85</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>97</td>
      <td>86</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>114</td>
      <td>98</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>122</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>195</td>
      <td>146</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>205</td>
      <td>196</td>
      <td>205</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>206</td>
      <td>289</td>
      <td>206</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>295</td>
      <td>290</td>
      <td>295</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>296</td>
      <td>309</td>
      <td>296</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>333</td>
      <td>310</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1p7b">1P7B</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNVDPFSPHSSDSFAQAASPARKPPRGGRRIWSGT</span><span class="topo-outside">REVIAYGMPAS</span><span class="topo-unknown">VWRDLYYWALK</span><span class="topo-outside">VSW</span><span class="topo-membrane">PVFFASLAALFVVNNTLFALLYQLG</span><span class="topo-inside">DAPIANQSPPGF</span><span class="topo-unknown">VGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YAHAIATLEIFVGMSGIALSTGLV</span><span class="topo-outside">FARFARPRAKIMFARHAIVRPFNGRMTLMVRAANARQNVIAEARAKMRLM</span><span class="topo-unknown">RREHSSEGYS</span><span class="topo-outside">LMKIHDLKLVRNEHPIFLLGWNMMHVIDESSPLFG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-outside">ETPESLAEGRAMLLVMIEGSDETTAQVMQARHAWEHDDIRWHHRYVDLM</span><span class="topo-unknown">SDVDGM</span><span class="topo-outside">THIDYTRFNDTEPV</span><span class="topo-unknown">EPPGAAPDAQAFAAKPGEGDARPV</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>35</td>
      <td>1</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>57</td>
      <td>47</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>85</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>97</td>
      <td>86</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>114</td>
      <td>98</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>122</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>195</td>
      <td>146</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>205</td>
      <td>196</td>
      <td>205</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>206</td>
      <td>289</td>
      <td>206</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>295</td>
      <td>290</td>
      <td>295</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>296</td>
      <td>309</td>
      <td>296</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>333</td>
      <td>310</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1p7b">1P7B</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNVDPFSPHSSDSFAQAASPARKPPRGGRRIWSGT</span><span class="topo-outside">REVIAYGMPAS</span><span class="topo-unknown">VWRDLYYWALK</span><span class="topo-outside">VSW</span><span class="topo-membrane">PVFFASLAALFVVNNTLFALLYQLG</span><span class="topo-inside">DAPIANQSPPGF</span><span class="topo-unknown">VGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YAHAIATLEIFVGMSGIALSTGLV</span><span class="topo-outside">FARFARPRAKIMFARHAIVRPFNGRMTLMVRAANARQNVIAEARAKMRLM</span><span class="topo-unknown">RREHSSEGYS</span><span class="topo-outside">LMKIHDLKLVRNEHPIFLLGWNMMHVIDESSPLFG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-outside">ETPESLAEGRAMLLVMIEGSDETTAQVMQARHAWEHDDIRWHHRYVDLM</span><span class="topo-unknown">SDVDGM</span><span class="topo-outside">THIDYTRFNDTEPV</span><span class="topo-unknown">EPPGAAPDAQAFAAKPGEGDARPV</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>35</td>
      <td>1</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>57</td>
      <td>47</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>85</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>97</td>
      <td>86</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>114</td>
      <td>98</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>122</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>195</td>
      <td>146</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>205</td>
      <td>196</td>
      <td>205</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>206</td>
      <td>289</td>
      <td>206</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>295</td>
      <td>290</td>
      <td>295</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>296</td>
      <td>309</td>
      <td>296</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>333</td>
      <td>310</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1xl4">1XL4</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPAR</span><span class="topo-outside">KPRILNSDGSSNITRLGLEKRGWLDDHYHDLLTV</span><span class="topo-membrane">SWPVFITLITGLYLVTNALFALAYLAC</span><span class="topo-inside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGY</span><span class="topo-inside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAASLIYARF</span><span class="topo-outside">TRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHH</span><span class="topo-unknown">HH</span></span>
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
      <td>1</td>
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>44</td>
      <td>11</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>71</td>
      <td>45</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>99</td>
      <td>84</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>135</td>
      <td>108</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>299</td>
      <td>136</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1xl4">1XL4</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARKPRILNSDGSSN</span><span class="topo-outside">ITRLGLEKRGWLDDH</span><span class="topo-unknown">YHDLLT</span><span class="topo-outside">V</span><span class="topo-membrane">SWPVFITLITGLYLVTNALFALAYLAC</span><span class="topo-inside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGY</span><span class="topo-inside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAASLIYAR</span><span class="topo-outside">FTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHH</span><span class="topo-unknown">HH</span></span>
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
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>23</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>43</td>
      <td>38</td>
      <td>43</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>71</td>
      <td>45</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>99</td>
      <td>84</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>134</td>
      <td>108</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>299</td>
      <td>135</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1xl4">1XL4</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPAR</span><span class="topo-outside">KPRILNSDGSSNITRLGLEKRGWLDDHYHDLLTV</span><span class="topo-membrane">SWPVFITLITGLYLVTNALFALAYLAC</span><span class="topo-inside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGY</span><span class="topo-inside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAASLIYAR</span><span class="topo-outside">FTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHH</span><span class="topo-unknown">HH</span></span>
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
      <td>1</td>
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>44</td>
      <td>11</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>71</td>
      <td>45</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>99</td>
      <td>84</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>134</td>
      <td>108</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>299</td>
      <td>135</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1xl4">1XL4</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARKPRILNSDGSSN</span><span class="topo-outside">ITRLGLEKRGWLDDH</span><span class="topo-unknown">YHDLLT</span><span class="topo-outside">V</span><span class="topo-membrane">SWPVFITLITGLYLVTNALFALAYLAC</span><span class="topo-inside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGY</span><span class="topo-inside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAASLIYARF</span><span class="topo-outside">TRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHH</span><span class="topo-unknown">HH</span></span>
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
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>23</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>43</td>
      <td>38</td>
      <td>43</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>71</td>
      <td>45</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>99</td>
      <td>84</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>135</td>
      <td>108</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>299</td>
      <td>136</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1xl6">1XL6</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPAR</span><span class="topo-outside">KPRILNSDGSSNITRLGLEKRG</span><span class="topo-unknown">WLDDHYH</span><span class="topo-outside">DLLTV</span><span class="topo-membrane">SWPVFITLITGLYLVTNALFALAYLAC</span><span class="topo-inside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGYG</span><span class="topo-inside">KLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAASLIYARF</span><span class="topo-outside">TRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHHHH</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>32</td>
      <td>11</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>39</td>
      <td>33</td>
      <td>39</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>40</td>
      <td>44</td>
      <td>40</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>71</td>
      <td>45</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>100</td>
      <td>84</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>101</td>
      <td>107</td>
      <td>101</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>135</td>
      <td>108</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>301</td>
      <td>136</td>
      <td>301</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1xl6">1XL6</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPAR</span><span class="topo-outside">KPRILNSDGSSNITRLGLEKRG</span><span class="topo-unknown">WLDDHYH</span><span class="topo-outside">DLLTV</span><span class="topo-membrane">SWPVFITLITGLYLVTNALFALAYLAC</span><span class="topo-inside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGYG</span><span class="topo-inside">KLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAASLIYARF</span><span class="topo-outside">TRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHHHH</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>32</td>
      <td>11</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>39</td>
      <td>33</td>
      <td>39</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>40</td>
      <td>44</td>
      <td>40</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>71</td>
      <td>45</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>100</td>
      <td>84</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>101</td>
      <td>107</td>
      <td>101</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>135</td>
      <td>108</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>301</td>
      <td>136</td>
      <td>301</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1xl6">1XL6</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPAR</span><span class="topo-outside">KPRILNSDGSSNITRLGLEKRG</span><span class="topo-unknown">WLDDHYH</span><span class="topo-outside">DLLTV</span><span class="topo-membrane">SWPVFITLITGLYLVTNALFALAYLAC</span><span class="topo-inside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGYG</span><span class="topo-inside">KLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAASLIYARF</span><span class="topo-outside">TRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHHHH</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>32</td>
      <td>11</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>39</td>
      <td>33</td>
      <td>39</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>40</td>
      <td>44</td>
      <td>40</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>71</td>
      <td>45</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>100</td>
      <td>84</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>101</td>
      <td>107</td>
      <td>101</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>135</td>
      <td>108</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>301</td>
      <td>136</td>
      <td>301</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1xl6">1XL6</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPAR</span><span class="topo-outside">KPRILNSDGSSNITRLGLEKRG</span><span class="topo-unknown">WLDDHYH</span><span class="topo-outside">DLLTV</span><span class="topo-membrane">SWPVFITLITGLYLVTNALFALAYLAC</span><span class="topo-inside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGYG</span><span class="topo-inside">KLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAASLIYARF</span><span class="topo-outside">TRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHHHH</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>32</td>
      <td>11</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>39</td>
      <td>33</td>
      <td>39</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>40</td>
      <td>44</td>
      <td>40</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>71</td>
      <td>45</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>100</td>
      <td>84</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>101</td>
      <td>107</td>
      <td>101</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>135</td>
      <td>108</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>301</td>
      <td>136</td>
      <td>301</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##NSMB.2208 (1 structure)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/s129r mutant (open state)">S129R MUTANT (OPEN STATE)</a></td>
      <td>3.05 A</td>
      <td>P42_12</td>
      <td>KirBac3.1 S129R gating mutant, codon-optimized for E. coli expression in pET30a vector</td>
      <td>K+ ions in selectivity filter (S1-S4 occupied, conductive conformation)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 (DE3) star
- **Construct**: Full-length histidine-tagged recombinant KirBac3.1 from Magnetospirillum magnetotactium. Q170A mutant expressed separately for comparison.

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
      <td>Cell lysis and membrane preparation</td>
      <td>Not specified</td>
      <td>--</td>
      <td>Not specified + --</td>
      <td>Expression and purification identical to previously described wild-type KirBac3.1 protocol</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td>--</td>
      <td>Not specified + triDM</td>
      <td>Detergent exchanged from triDM into 14 mM <a href="/xray-mp-wiki/reagents/detergents/hega-10/">HEGA-10</a> using Vivaspin concentrators (100 kDa cutoff) after gel filtration</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Vivaspin concentrators (100 kDa cutoff)</td>
      <td>--</td>
      <td>Not specified + 14 mM <a href="/xray-mp-wiki/reagents/detergents/hega-10/">HEGA-10</a></td>
      <td>Concentrated to 6 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KirBac3.1 S129R at 6 mg/ml in 14 mM <a href="/xray-mp-wiki/reagents/detergents/hega-10/">HEGA-10</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 90 mM HEPES pH 7.2, 20% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 5% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000, 2.5% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 8000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-4 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals cryocooled under liquid nitrogen before analysis</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown using 1:1 protein:reservoir ratio. Data collected at Diamond Light Source I-24 beamline (lambda = 0.9778 A) at 100 K using Pilatus 6M detector.</td>
    </tr>
  </tbody>
</table>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.3390##ijms23010335 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7adi">7ADI</a></td>
      <td>2.80 A</td>
      <td>P2_1_2_1_2</td>
      <td>KirBac3.1 W46R mutant, full-length with His-tag, expressed in E. coli in pET30a vector</td>
      <td>K+ and Mg2+ ions</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 (DE3) star
- **Construct**: Full-length histidine-tagged recombinant KirBac3.1 from Magnetospirillum magnetotactium. Q170A mutant expressed separately for comparison.

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
      <td>French press</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cell disruption by French press</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>-- + 45 mM DM (Decyl beta-D-maltopyranoside)</td>
      <td>Directly solubilized with 45 mM DM, then centrifuged</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Co2+ affinity column</td>
      <td>Co2+ affinity resin</td>
      <td>-- + --</td>
      <td>Supernatant loaded onto Co2+ affinity column</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300</td>
      <td>2 mM TriDM + 2 mM TriDM</td>
      <td>Purified on <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column pre-equilibrated with 2 mM TriDM buffer</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Ultrafiltration</td>
      <td>--</td>
      <td>20 mM Tris pH 7.4, 150 mM KCl, 0.2 mM TriDM + 0.2 mM TriDM</td>
      <td>Concentrated to 1-2.5 mg/mL, stored at -80 C</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop and hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KirBac3.1 W46R at 10 mg/mL in 20 mM Tris pH 7.4, 150 mM KCl, 0.2 mM TriDM</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>15% (w/v) PEG-MME 5k, 15% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 M LiCl, 100 mM MES pH 6.5</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir solution used as cryo-protectant</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial screening with Mosquito nanoliter-dispensing system (672 conditions). Best crystals obtained by hanging-drop vapor diffusion. 400 nL drops (1:1 protein:reservoir) for screening, 4 uL drops for optimization. Crystals in P2_1_2_1_2 space group. Data collected at SOLEIL PROXIMA-1 beamline at 100 K with PILATUS 6M detector at 1.07114 A wavelength.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7adi">7ADI</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-inside">PRILNSDGSSNITRLGL</span><span class="topo-unknown">EKRGWLD</span><span class="topo-inside">DHYHDLLTVSRP</span><span class="topo-membrane">VFITLITGLYLVTNALFALAYLAC</span><span class="topo-outside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGY</span><span class="topo-outside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTT</span><span class="topo-unknown">LPDG</span><span class="topo-inside">RRALDLGKFHEIAQHHH</span><span class="topo-unknown">HHH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>28</td>
      <td>12</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>35</td>
      <td>29</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>47</td>
      <td>36</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>71</td>
      <td>48</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>99</td>
      <td>84</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>128</td>
      <td>108</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>277</td>
      <td>129</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>281</td>
      <td>278</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>282</td>
      <td>298</td>
      <td>282</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>301</td>
      <td>299</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7adi">7ADI</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARKPRILNSDGSSN</span><span class="topo-inside">ITRLGL</span><span class="topo-unknown">EKRGWLDDH</span><span class="topo-inside">YHDLLTVSRP</span><span class="topo-membrane">VFITLITGLYLVTNALFALAYLAC</span><span class="topo-outside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGY</span><span class="topo-outside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTT</span><span class="topo-unknown">LPDG</span><span class="topo-inside">RRALDLGKFHEIAQHHHHH</span><span class="topo-unknown">H</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>28</td>
      <td>23</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>37</td>
      <td>29</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>38</td>
      <td>47</td>
      <td>38</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>71</td>
      <td>48</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>99</td>
      <td>84</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>128</td>
      <td>108</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>277</td>
      <td>129</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>281</td>
      <td>278</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>282</td>
      <td>300</td>
      <td>282</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>301</td>
      <td>301</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7adi">7ADI</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-inside">PRILNSDGSSNITRLGL</span><span class="topo-unknown">EKRGWLD</span><span class="topo-inside">DHYHDLLTVSRP</span><span class="topo-membrane">VFITLITGLYLVTNALFALAYLAC</span><span class="topo-outside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGY</span><span class="topo-outside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTT</span><span class="topo-unknown">LPDG</span><span class="topo-inside">RRALDLGKFHEIAQHHH</span><span class="topo-unknown">HHH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>28</td>
      <td>12</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>35</td>
      <td>29</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>47</td>
      <td>36</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>71</td>
      <td>48</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>99</td>
      <td>84</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>128</td>
      <td>108</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>277</td>
      <td>129</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>281</td>
      <td>278</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>282</td>
      <td>298</td>
      <td>282</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>301</td>
      <td>299</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7adi">7ADI</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARKPRILNSDGSSN</span><span class="topo-inside">ITRLGL</span><span class="topo-unknown">EKRGWLDDH</span><span class="topo-inside">YHDLLTVSRP</span><span class="topo-membrane">VFITLITGLYLVTNALFALAYLAC</span><span class="topo-outside">GDVIENARPGSF</span><span class="topo-unknown">TDAFFFSVQTMATIGY</span><span class="topo-outside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTT</span><span class="topo-unknown">LPDG</span><span class="topo-inside">RRALDLGKFHEIAQHHHHH</span><span class="topo-unknown">H</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>28</td>
      <td>23</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>37</td>
      <td>29</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>38</td>
      <td>47</td>
      <td>38</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>71</td>
      <td>48</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>72</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>99</td>
      <td>84</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>128</td>
      <td>108</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>277</td>
      <td>129</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>281</td>
      <td>278</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>282</td>
      <td>300</td>
      <td>282</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>301</td>
      <td>301</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##s41467-020-16842-0 (3 structures, 12 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6o9t">6O9T</a></td>
      <td>3.1 A</td>
      <td>P4(3)2(1)2</td>
      <td>KirBac3.1 S129C-F135C with MTS-1-MTS crosslinker, C262S/C71V/C119V background</td>
      <td>K+ ions</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6o9u">6O9U</a></td>
      <td>2.0 A</td>
      <td>P4(3)2(1)2</td>
      <td>Full-length wild-type KirBac3.1 (C262S/C71V/C119V background)</td>
      <td>K+ ions</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6o9v">6O9V</a></td>
      <td>4.1 A</td>
      <td>P4(3)2(1)2</td>
      <td>KirBac3.1 A133C-T136C with dibromobimane crosslinker, C262S/C71V/C119V background</td>
      <td>K+ ions</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 (DE3) star
- **Construct**: Full-length histidine-tagged recombinant KirBac3.1 from Magnetospirillum magnetotactium. Q170A mutant expressed separately for comparison.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9t">6O9T</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-inside">PRILNSDGSSNITRL</span><span class="topo-unknown">GLEKRGWL</span><span class="topo-inside">DDHYHDLLTVSWP</span><span class="topo-membrane">VFITLITGLYLVTNALFALAY</span><span class="topo-outside">LAVGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-outside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYCRFCRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSSDEIIWGGHFVDVFTTLPDGRRALDLGKFHEI</span><span class="topo-unknown">AQHHHHHH</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>34</td>
      <td>27</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>47</td>
      <td>35</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>68</td>
      <td>48</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>293</td>
      <td>129</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>301</td>
      <td>294</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9t">6O9T</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-inside">PRILNSDGSSNITRL</span><span class="topo-unknown">GLEKRGWL</span><span class="topo-inside">DDHYHDLLTVSWP</span><span class="topo-membrane">VFITLITGLYLVTNALFALAY</span><span class="topo-outside">LAVGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-outside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYCRFCRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSSDEIIWGGHFVDVFTTLPDGRRALDLGKFHEI</span><span class="topo-unknown">AQHHHHHH</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>34</td>
      <td>27</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>47</td>
      <td>35</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>68</td>
      <td>48</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>293</td>
      <td>129</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>301</td>
      <td>294</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9t">6O9T</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-inside">PRILNSDGSSNITRL</span><span class="topo-unknown">GLEKRGWL</span><span class="topo-inside">DDHYHDLLTVSWP</span><span class="topo-membrane">VFITLITGLYLVTNALFALAY</span><span class="topo-outside">LAVGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-outside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYCRFCRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSSDEIIWGGHFVDVFTTLPDGRRALDLGKFHEI</span><span class="topo-unknown">AQHHHHHH</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>34</td>
      <td>27</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>47</td>
      <td>35</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>68</td>
      <td>48</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>293</td>
      <td>129</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>301</td>
      <td>294</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9t">6O9T</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-inside">PRILNSDGSSNITRL</span><span class="topo-unknown">GLEKRGWL</span><span class="topo-inside">DDHYHDLLTVSWP</span><span class="topo-membrane">VFITLITGLYLVTNALFALAY</span><span class="topo-outside">LAVGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-outside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYCRFCRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSSDEIIWGGHFVDVFTTLPDGRRALDLGKFHEI</span><span class="topo-unknown">AQHHHHHH</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>34</td>
      <td>27</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>47</td>
      <td>35</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>68</td>
      <td>48</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>293</td>
      <td>129</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>301</td>
      <td>294</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9u">6O9U</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-inside">PRILNSDGSSNITRLGL</span><span class="topo-unknown">EKRG</span><span class="topo-inside">WLDDHYHDLLTVSWPVFI</span><span class="topo-membrane">TLITGLYLVTNALFALAY</span><span class="topo-outside">LACGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-outside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHH</span><span class="topo-unknown">HHH</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>28</td>
      <td>12</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>32</td>
      <td>29</td>
      <td>32</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>33</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>68</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>298</td>
      <td>129</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>301</td>
      <td>299</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9u">6O9U</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-inside">PRILNSDGSSNITRLGL</span><span class="topo-unknown">EKRG</span><span class="topo-inside">WLDDHYHDLLTVSWPVFI</span><span class="topo-membrane">TLITGLYLVTNALFALAY</span><span class="topo-outside">LACGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-outside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHH</span><span class="topo-unknown">HHH</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>28</td>
      <td>12</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>32</td>
      <td>29</td>
      <td>32</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>33</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>68</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>298</td>
      <td>129</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>301</td>
      <td>299</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9u">6O9U</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-inside">PRILNSDGSSNITRLGL</span><span class="topo-unknown">EKRG</span><span class="topo-inside">WLDDHYHDLLTVSWPVFI</span><span class="topo-membrane">TLITGLYLVTNALFALAY</span><span class="topo-outside">LACGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-outside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHH</span><span class="topo-unknown">HHH</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>28</td>
      <td>12</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>32</td>
      <td>29</td>
      <td>32</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>33</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>68</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>298</td>
      <td>129</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>301</td>
      <td>299</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9u">6O9U</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-inside">PRILNSDGSSNITRLGL</span><span class="topo-unknown">EKRG</span><span class="topo-inside">WLDDHYHDLLTVSWPVFI</span><span class="topo-membrane">TLITGLYLVTNALFALAY</span><span class="topo-outside">LACGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-outside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-inside">SLIYARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHH</span><span class="topo-unknown">HHH</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>28</td>
      <td>12</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>32</td>
      <td>29</td>
      <td>32</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>33</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>68</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>298</td>
      <td>129</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>301</td>
      <td>299</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9v">6O9V</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-outside">PRILNSDGSSNITRL</span><span class="topo-unknown">GLEKRGWL</span><span class="topo-outside">DDHYHDLLTVSWPVFI</span><span class="topo-membrane">TLITGLYLVTNALFALAY</span><span class="topo-inside">LAVGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-inside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-outside">CLIYARCTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSSDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHH</span><span class="topo-unknown">HHH</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>34</td>
      <td>27</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>50</td>
      <td>35</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>68</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>298</td>
      <td>129</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>301</td>
      <td>299</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9v">6O9V</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPAR</span><span class="topo-outside">KPRILNSDGSSNITRLGLE</span><span class="topo-unknown">KRGW</span><span class="topo-outside">LDDHYHDLLTVSWPVFI</span><span class="topo-membrane">TLITGLYLVTNALFALAY</span><span class="topo-inside">LAVGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-inside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-outside">CLIYARCTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSSDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQH</span><span class="topo-unknown">HHHHH</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>29</td>
      <td>11</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>33</td>
      <td>30</td>
      <td>33</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>34</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>68</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>296</td>
      <td>129</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>301</td>
      <td>297</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9v">6O9V</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARK</span><span class="topo-outside">PRILNSDGSSNITRL</span><span class="topo-unknown">GLEKRGWL</span><span class="topo-outside">DDHYHDLLTVSWPVFI</span><span class="topo-membrane">TLITGLYLVTNALFALAY</span><span class="topo-inside">LAVGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-inside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-outside">CLIYARCTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSSDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHH</span><span class="topo-unknown">HHH</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>34</td>
      <td>27</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>50</td>
      <td>35</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>68</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>298</td>
      <td>129</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>301</td>
      <td>299</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o9v">6O9V</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPAR</span><span class="topo-outside">KPRILNSDGSSNITRLGLE</span><span class="topo-unknown">KRGW</span><span class="topo-outside">LDDHYHDLLTVSWPVFI</span><span class="topo-membrane">TLITGLYLVTNALFALAY</span><span class="topo-inside">LAVGDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIG</span><span class="topo-inside">YGKLIPIGPL</span><span class="topo-membrane">ANTLVTLEALVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAA</span><span class="topo-outside">CLIYARCTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRSPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">VLFTGHHEAFAQNVHARHAYSSDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQH</span><span class="topo-unknown">HHHHH</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>29</td>
      <td>11</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>33</td>
      <td>30</td>
      <td>33</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>34</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>68</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>86</td>
      <td>69</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>87</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>99</td>
      <td>108</td>
      <td>99</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>128</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>296</td>
      <td>129</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>301</td>
      <td>297</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1074##jbc.M113.501833 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4lp8">4LP8</a></td>
      <td>2.46 A</td>
      <td>P4_2_1_2</td>
      <td>KirBac3.1 S129R/S205L double mutant, full-length, expressed in E. coli</td>
      <td>K+ ions in selectivity filter, K+ ion in CTD pore coordinated by Glu173 and Asp175</td>
    </tr>
  </tbody>
</table>
 - R-work 0.183%, R-free 0.248%; Data collection: Diamond Light Source I-24 beamline (lambda=0.978 A), 100 K, Pilatus 6M detector

**Expression:**

- **Expression system**: E. coli BL21 (DE3) star
- **Construct**: Full-length histidine-tagged recombinant KirBac3.1 from Magnetospirillum magnetotactium. Q170A mutant expressed separately for comparison.

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
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>Not specified</td>
      <td>Not specified + tridecyl-beta-maltoside</td>
      <td>After elution from SEC, detergent exchanged to 14 mM <a href="/xray-mp-wiki/reagents/detergents/hega-10/">HEGA-10</a> using Amicon 100-kDa cutoff filtration device</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Amicon 100-kDa cutoff filtration</td>
      <td>Amicon</td>
      <td>Not specified + 14 mM <a href="/xray-mp-wiki/reagents/detergents/hega-10/">HEGA-10</a></td>
      <td>Concentrated to 6 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified (hanging/sitting drop vapor diffusion)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KirBac3.1 S129R/S205L at 6 mg/ml in 14 mM <a href="/xray-mp-wiki/reagents/detergents/hega-10/">HEGA-10</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 90 mM HEPES pH 7, 20% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg-400/">Polyethylene Glycol 400 (PEG 400)</a>, 5% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg-4000/">PEG 4000 (Polyethylene Glycol 4000)</a>, 2.5% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg-8000/">Polyethylene Glycol 8000 (PEG 8000)</a>, 10 mM spermidine</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-4 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested using LithoLoops (Molecular Dimensions) and immediately cryo-cooled in liquid N2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared after 2-4 days at room temperature. Data collected at Diamond Light Source I-24 beamline (lambda=0.978 A) at 100 K using Pilatus 6M detector to 2.46 A resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4lp8">4LP8</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARKP</span><span class="topo-inside">RILNSDGSSNITRLG</span><span class="topo-unknown">LEKR</span><span class="topo-inside">GWLDD</span><span class="topo-unknown">HYHDLLT</span><span class="topo-inside">VSW</span><span class="topo-membrane">PVFITLITGLYLVTNALFALAYLAC</span><span class="topo-outside">GDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIGY</span><span class="topo-outside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAARLIY</span><span class="topo-inside">ARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRLPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHH</span><span class="topo-unknown">HH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>27</td>
      <td>13</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>31</td>
      <td>28</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>43</td>
      <td>37</td>
      <td>43</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>44</td>
      <td>46</td>
      <td>44</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>71</td>
      <td>47</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>86</td>
      <td>72</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>99</td>
      <td>87</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>132</td>
      <td>108</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>299</td>
      <td>133</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4lp8">4LP8</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARKP</span><span class="topo-inside">RILNSDGSSNITRLG</span><span class="topo-unknown">LEKR</span><span class="topo-inside">GWLDD</span><span class="topo-unknown">HYHDLLT</span><span class="topo-inside">VSW</span><span class="topo-membrane">PVFITLITGLYLVTNALFALAYLAC</span><span class="topo-outside">GDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIGY</span><span class="topo-outside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAARLIY</span><span class="topo-inside">ARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRLPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHH</span><span class="topo-unknown">HH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>27</td>
      <td>13</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>31</td>
      <td>28</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>43</td>
      <td>37</td>
      <td>43</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>44</td>
      <td>46</td>
      <td>44</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>71</td>
      <td>47</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>86</td>
      <td>72</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>99</td>
      <td>87</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>132</td>
      <td>108</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>299</td>
      <td>133</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4lp8">4LP8</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARKP</span><span class="topo-inside">RILNSDGSSNITRLG</span><span class="topo-unknown">LEKR</span><span class="topo-inside">GWLDD</span><span class="topo-unknown">HYHDLLT</span><span class="topo-inside">VSW</span><span class="topo-membrane">PVFITLITGLYLVTNALFALAYLAC</span><span class="topo-outside">GDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIGY</span><span class="topo-outside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAARLIY</span><span class="topo-inside">ARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRLPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHH</span><span class="topo-unknown">HH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>27</td>
      <td>13</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>31</td>
      <td>28</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>43</td>
      <td>37</td>
      <td>43</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>44</td>
      <td>46</td>
      <td>44</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>71</td>
      <td>47</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>86</td>
      <td>72</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>99</td>
      <td>87</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>132</td>
      <td>108</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>299</td>
      <td>133</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4lp8">4LP8</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTGGMKPPARKP</span><span class="topo-inside">RILNSDGSSNITRLG</span><span class="topo-unknown">LEKR</span><span class="topo-inside">GWLDD</span><span class="topo-unknown">HYHDLLT</span><span class="topo-inside">VSW</span><span class="topo-membrane">PVFITLITGLYLVTNALFALAYLAC</span><span class="topo-outside">GDVIENARPGSFTDA</span><span class="topo-unknown">FFFSVQTMATIGY</span><span class="topo-outside">GKLIPIGP</span><span class="topo-membrane">LANTLVTLEALCG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLGLAVAARLIY</span><span class="topo-inside">ARFTRPTAGVLFSSRMVISDFEGKPTLMMRLANLRIEQIIEADVHLVLVRSEISQEGMVFRRFHDLTLTRSRLPIFSLSWTVMHPIDHHSPIYGETDETLRNSHSEFL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-inside">VLFTGHHEAFAQNVHARHAYSCDEIIWGGHFVDVFTTLPDGRRALDLGKFHEIAQHHHH</span><span class="topo-unknown">HH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>27</td>
      <td>13</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>31</td>
      <td>28</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>43</td>
      <td>37</td>
      <td>43</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>44</td>
      <td>46</td>
      <td>44</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>71</td>
      <td>47</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>86</td>
      <td>72</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>99</td>
      <td>87</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>107</td>
      <td>100</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>132</td>
      <td>108</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>299</td>
      <td>133</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>


## Biological / Functional Insights

### Interdependent gates in the conduction pathway

Crystallographic evidence reveals interdependent gates in the Kir channel conduction pathway. Reorientation of the intracellular domains, concomitant with activation, instigates polyamine release from intracellular binding sites to block the permeation pathway. Conformational adjustments of the slide helices, achieved by rotation of the cytoplasmic assembly relative to the pore, are directly correlated to the ion configuration in the selectivity filter. Ion redistribution occurs irrespective of the bundle crossing constriction, suggesting a more expansive role of the selectivity filter in gating than previously appreciated.

### Selectivity filter gating and ion configuration

The ion distribution in the selectivity filter is systematically correlated to global conformational changes. Twist structures (III-VII, IX) have a three-ion configuration (S1, S3, S4) representing stalled conduction. Nontwist structures (II, VIII, X) have four occupied sites (S1, S2, S3, S4) corresponding to conducting or blocked states. Divalent ions (Mg2+, Ca2+, Ba2+) produce cation-specific blocked configurations. The selectivity filter can switch between nonconducting and conducting configurations without significant displacement of the inner helices, suggesting a more prominent role for the selectivity filter in gating than previously appreciated.

### Polyamine binding and rectification mechanism

Two distinct polyamine-binding sites identified at latched intracellular interfaces. [Spermine](/xray-mp-wiki/reagents/additives/spermine/) binds within closed pockets at latched interfaces but not at unlatched interfaces. Unlatching causes the intracellular vestibule to connect with the pore, simultaneously disrupting binding sites and facilitating polyamine release into the conduction path. His177 in KirBac3.1 (counterpart of His216 in Kir6.2) interacts with Asp197 to enclose the binding pocket. Protonation of His177 at low pH offsets the negative charge of Asp197, reducing electrostatic attraction of polyamines and providing a mechanism for pH-titratable rectification.

### Staged activation pathway via symmetric intermediates

Conformational interchange mediated at intracellular subunit interfaces follows a staged path to activation via two-fold symmetric intermediates. In intermediate states, every other subunit is unlatched, distorting symmetry along a cross-sectional diagonal. Only when all four interfaces have eschewed the latched arrangement can the selectivity filter acquire a conducting conformation. Unlatching is concomitant with activation. The Q170A mutant is effectively unlatched at all four interfaces but has fewer molecular constraints, resulting in a 1-2 degree difference in cytoplasmic domain orientation and higher open probability.

### Molecular pulleys link unlatching to domain reorientation

Structural interdependency links rearrangement at subunit interfaces to systematic reorientation of intracellular domains, where latched and unlatched states differ by approximately 5 degrees. Coupling is facilitated by the N and C termini acting as a pulley system. The intracellular domain of each subunit is an immunoglobulin-like beta sandwich overlaid by N and C termini, with the C terminus tethered to both the N terminus and the underlying beta sandwich. Parallel beta sheet interactions formed between betaC_N on one subunit and betaM on another interweave neighboring subunits into a circle, coupling the motion of each subunit to that of its neighbor.

### Open-state gating via TM2 bending and rotation

The first open-state structure of a KirBac channel (S129R mutant) reveals that TM2 bends at Gly120 by up to 20 degrees and rotates approximately 25 degrees along its helical axis to open the bundle-crossing gate. This rotation moves the secondary constriction at Leu124 away from the pore, increasing effective pore diameter from less than 2 A to greater than 8 A. Contrary to a previously proposed gating model, the structure adopts a twist configuration of the CTD yet maintains a fully conductive selectivity filter with all four K+ binding sites (S1-S4) occupied. A network of inter- and intrasubunit interactions involving the C-linker, slide helix, G-loop, and CD loop couples rotational movement of the CTD to opening of the bundle-crossing gate.

### W46R mutation disrupts TM1-TM2 hydrophobic cluster in KirBac3.1

The W46R mutation replaces the highly conserved tryptophan at the cytosolic end of TM1 (equivalent to W68 in Kir6.2) with arginine. In wild-type KirBac3.1, W46 adopts a 'flipped-in' conformation tightly packed against the C-terminal end of TM2, interacting with I131, R134, and F135. In the W46R mutant crystal structure (PDB 7ADI, 2.80 A), R46 points away from the channel pore in a 'flipped-out' conformation (98.68% occupancy in MDeNM), disrupting these hydrophobic contacts and forming new electrostatic interactions with Y38 and D36 on the slide helix of the adjacent subunit.

### Differential flexibility revealed by HDX-MS

[HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/) experiments show that the W46R mutant has reduced flexibility at the mutation site (aa 43-56: 37.9% vs 65.1% normalized HDX rate) due to a stable interaction network around R46. However, this is accompanied by increased flexibility in the slide helix (aa 36-42: 41.57% vs 26.92%), selectivity filter region (aa 93-112: 50.04% vs 30.08%), and CD-loop (aa 162-174: 94.61% vs 83.1%), illustrating long-range conformational effects propagating from the mutation site to the pore and cytoplasmic domains.

### W46R gating mechanism involves synchronized chain movements

MDeNM simulations reveal a multi-step gating mechanism: (1) R46 interacts with D36 on the slide helix of the neighboring subunit; (2) this interaction promotes upward movement of the slide helices; (3) slide helix movement induces tilting of TM1 and TM2; (4) this causes increased opening at the L124 constriction (33% vs 29% WT) but decreased opening at Y132 (11% vs 14% WT). The fully open state population is similar (7.4% vs 6.8% WT). Correlations between chains are more pronounced in the mutant, suggesting synchronized gating steps - a key difference from the uncorrelated chain movements in WT.

### W46R functional characterization and relevance to neonatal diabetes

Single-channel recordings of purified W46R reconstituted in DPhPC lipid bilayers show a single-channel conductance of 36 pS at +100 mV and open probability of 0.071, similar to the WT (0.099). The mutation does not significantly alter the intrinsic open probability of the bacterial KirBac channel. By analogy, the homologous W68R mutation in human Kir6.2 (which causes neonatal diabetes) is hypothesized to reduce ATP sensitivity by disrupting the hydrophobic cluster that couples ATP binding to pore closure, rather than directly increasing open probability.

### Constricted Tyr132 opening does not impede K+ conduction

Crosslinking experiments using disulfide bonds and chemical crosslinkers (MTS-1-MTS, dibromobimane) to covalently link the four inner helices of KirBac3.1 at the Tyr132 collar demonstrate that K+ conduction continues unimpaired even when the intracellular opening is locked in a constricted conformation. Crystal structures of crosslinked mutants S129C-F135C-MTS-1-MTS (PDB 6O9T, 3.1 A) and A133C-T136C-bimane (PDB 6O9V, 4.1 A) confirm the crosslinks encircle the conduction pathway at Tyr132. [Native Mass Spectrometry](/xray-mp-wiki/methods/quality-assessment/native-mass-spectrometry/) and SDS-PAGE verified complete tetrameric crosslinking. Liposomal flux assays using the ACMA fluorimetric assay show that all six crosslinked variants conduct K+ at levels comparable to wild-type channels.

### K+ permeates the narrow collar by partial dehydration

All-atom MD simulations using [Umbrella Sampling](/xray-mp-wiki/methods/structure-determination/umbrella-sampling/) to calculate the potential of mean force (PMF) reveal that K+ passes through the Tyr132 collar in a partially dehydrated state, transiently shedding 3-4 water molecules from its hydration shell. The coordination number drops from approximately six in the cavity to three or four at the constriction. Transient interactions with Tyr132 hydroxyl groups partially compensate for lost waters. The free energy barrier to permeation at the constriction is not prohibitive (low kJ/mol), demonstrating that the narrow opening does not represent a significant energetic barrier to K+ flux.

### Spermine block is prevented by crosslinking but K+ flux is unaffected

[Spermine](/xray-mp-wiki/reagents/additives/spermine/), a narrow polyamine blocker of Kir channels, is able to block wild-type KirBac3.1 but fails to block disulfide-linked A133C-T136C mutants. MD simulations show the disulfide-linked constriction presents a significantly higher PMF barrier to [Spermine](/xray-mp-wiki/reagents/additives/spermine/) penetration (25 kJ/mol vs 15 kJ/mol at site 2, and 45 kJ/mol vs 15 kJ/mol at site 4) compared to wild-type. The cross-sectional width of hydrated K+ (~6.6 A) and [Spermine](/xray-mp-wiki/reagents/additives/spermine/) (~5.6 A) explains this differential effect: K+ can partially dehydrate to pass through the ~4.0-6.0 A opening, while [Spermine](/xray-mp-wiki/reagents/additives/spermine/) as a rigid polyamine cannot. This provides direct experimental verification that the covalent disulfide linkages effectively constrain the pore without preventing K+ conduction.

### Canonical pore-gating model challenged for Kir channels

The finding that Kir channels conduct K+ through a constricted opening challenges the canonical gating model, which posits that a conformational change must widen the intracellular helix bundle crossing to accommodate fully hydrated K+ ions. Instead, these results suggest that the primary gate in Kir channels may be at the selectivity filter, or that gating involves changes in lipid accessibility at the pore entrance rather than pore dilation. The ability of K+ to shed water molecules from its coordination shell, combined with a short bottleneck distance that allows simultaneous access to water on both sides, enables conduction without significant structural rearrangement.

### Closed state architecture of KirBac1.1

The KirBac1.1 closed state structure at 3.65 A resolution reveals four mechanisms preventing ion conduction: (i) occlusion of the ion-conduction pathway by hydrophobic phenylalanine (Phe146) side chains acting as the activation gate, (ii) misalignment of pore helices away from the central cavity, (iii) decreased volume of the central cavity accommodating fewer water molecules (20 vs 27 in [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/)), and (iv) altered conformation of the selectivity filter with a stable K+ ion at the S2 position preventing filter collapse. The total ion conduction path is 88 A from the extracellular turret to the C-terminal domain.

### Slide helix as a gating coupling element

An amphipathic slide helix running parallel to the membrane-cytoplasmic interface serves as a central coupling mechanism between the intracellular domains and the blocking residue. The slide helix interacts with conserved Arg148 via its negative C-terminal end, using helix dipole interactions. Conserved Asp50 on the slide helix hydrogen bonds to the backbone nitrogen of Ser46, stabilizing the connection between the N-terminal strand and the slide helix. When the C-terminal assembly receives a gating signal, outer helices move with the slide helix, creating room for inner helix bending and displacement of Phe146 from the conduction pathway.

### Inner-helix bending at glycine hinges

Gating involves bending of the inner helix at conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues. KirBac1.1 has three [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues on the inner helix at positions 134, 137, and 143. Gly143 is the most highly conserved among Kir channels and is proposed as the primary hinge for helix bending during gating. As the channel opens, the slide helix moves laterally, exerting strain on the bottom of the inner helix and causing distortion at Gly143. This moves the blocking residue Phe146 away from the center of the ion-conduction pathway. Gly134 likely plays a minor role in gating and a more important role in protein packing.

### Dimer-of-dimers architecture and rectification

The KirBac1.1 channel shows a dimer-of-dimers arrangement where the transmembrane section displays four-fold symmetry but the intracellular domains adopt a two-fold arrangement, hinged at the cytosolic face of the membrane. Rectification involves three key residues: Ile138, Glu187, and Glu258. Glu187 and Glu258 form a double ring of negatively charged glutamate side chains in the C-terminal vestibule. These outstretched negatively charged rings, with ~8 A spacing between adjacent glutamate side chains, favor coordination of linear polyamines over compact Mg2+ ions, explaining the slower component of rectification by endogenous polyamines.

### S205L mutation stabilizes a novel open conformation at CTD interface

The S205L activatory mutation in the CTD of KirBac3.1, crystallized in the S129R/S205L double mutant (PDB 4LP8, 2.46 A), stabilizes a novel high-energy open conformation. S205L disrupts the Glu173-His177-Asp175 intersubunit triad, causing His177 to switch rotamer and form a new triad with Asp197 and Arg202. This releases Glu173 and Asp175 into the cytoplasmic pore, where they coordinate a potassium ion and alter the electrostatic potential of the CTD cavity, reducing the energetic barrier to K+ permeation. The S205L mutation increases channel activity in liposomal Rb+ flux assays (p=0.03) and complements growth in K+- auxotrophic E. coli.

### His177 as a pH-sensitive switch at the CTD interface

KirBac3.1 is a pH-sensitive channel with maximal activity at pH 8.0, decreasing at more alkaline pH. His177, equivalent to His216 in Kir6.2, acts as a pH-titratable switch at the CTD intersubunit interface. The H177A mutation mimics aspects of the S205L mutation by preventing formation of the Glu173-His177-Asp175 triad, releasing Glu173 and Asp175 to line the cytoplasmic vestibule. Both S205L and H177A increase activity at pH 7.5 but neither abolishes pH sensitivity, suggesting the pH sensor involves multiple titratable interactions.

### CTD interface dynamics control Kir channel gating

Molecular dynamics simulations (100 ns) of the S129R/S205L double mutant structure (with R129S/L205S reversion) show that the His177 side chain reverts from interacting with Asp197/Arg202 back to interacting with Glu173/Asp175 in three of four subunit interfaces. The G-loop gate closes (radius reduced from 5 to <2.2 A) in the double-mutant simulation but not the single-mutant, indicating the S205L mutant structure represents a higher energy open conformation. No untwisting of the CTD was observed, suggesting the CTD twist is stabilized in this conformation. Glu173 is conserved in strongly rectifying Kir channels (Glu225 in Kir2.2) and serves as a K+ coordination site that influences unitary conductance and polyamine block.

### Lipid acyl tails gate Kir channels by competing with Leu124 collar

Crystal structures of KirBac3.1 show the conduction pathway is occluded by a cluster of four Leu124 branched aliphatic side chains. Unbiased MD simulations revealed that fatty acyl chains of lipids occupying conserved fenestrations in the pore walls naturally interact with Leu124, drawing the leucine side chains away from the conduction pathway and creating an opening of ~5 A diameter. Each K+ permeation event occurred in response to lipid-Leu124 interaction. Umbrella sampling showed the energetic barrier at the Leu124 collar is 13 kJ/mol with native lipid interaction vs 41 kJ/mol when fenestrations are blocked (by Tyr57 gauche rotamer). The L124M mutant (labile methionine side chains) conducts K+ even when fenestrations are blocked, confirming the leucine collar is the primary gate.

### Minimal barrier to K+ permeation is at Leu124, not Tyr132

The canonical gating model posits the inner helix bundle (Tyr132 in KirBac3.1) is the permeation gate. However, Leu124 forms a steric cluster physically occluding the conduction pathway. ACMA fluorimetric population assays comparing Leu124M (exhibits similar activity to wild-type) and Tyr132I (also non-impairing) mutants demonstrate the Leu124 collar - not the Tyr132 bundle crossing - provides the limiting barrier. PMF calculations showed the energetic barrier at the Tyr132 collar is dissipative, confirming it is not a functional gate.

### Alkyl chain length determines gating efficacy

Alkyl-MTS reagents of varying chain lengths (hexyl, octyl, decyl) were covalently attached to Cys119 (adjacent to the fenestrations) to mimic lipid tails. ACMA assays showed decyl chains (C119-decyl) increased activity, while hexyl chains (C119-hexyl) reduced it by blocking fenestrations without reaching Leu124. Single channel recordings revealed C119-decyl has higher open probability (Po=0.69) and more fully open events, while C119-hexyl predominantly operates at lower conductance substrate levels. This demonstrates ion permeation is contingent on lipid tails being of sufficient length to reach the Leu124 occlusion.

### Anionic lipids bind specifically to KirBac3.1 and gate the pore

Coarse-grained MD simulations showed pores preferentially concentrate anionic lipids (PS, PG) around the pore, while zwitterionic PC accumulates at the tetramer interfaces. Native mass spectrometry of purified KirBac3.1 revealed adduct masses of +765, +1513, and +2270 Da, corresponding to 1-3 phospholipids (PE and PG). Lipidomics analysis confirmed PG enrichment and preferential binding of long-chain lipids (>34 total carbons). 95.5% of fenestration-occupying lipids had head groups within 5 A of the Arg137/Trp46/His37 canonical lipid-binding pocket. The nexus of electrostatic contacts between anionic lipid head groups and both pore and intracellular elements couples interdomain motions to the movement of lipid tails engaging Leu124.


## Cross-References

- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Ni2+-loaded IMAC used for His-tagged KirBac purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — SEC used after affinity chromatography for KirBac purification
- <a href="/xray-mp-wiki/reagents/detergents/anzergent-3-12/">Anzergent 3,12</a> — Primary solubilization detergent at 1% for KirBac3.1 extraction
- <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">Calcium Chloride</a> — Crystallization additive (0.2 M) in structure III
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a> — Crystallization additive (0.1 M) in structure VI
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — Crystallization precipitant (PEG 3350) used in all conditions
- <a href="/xray-mp-wiki/reagents/additives/spermine/">Spermine</a> — Crystallization additive (0.2 M) and polyamine channel blocker
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer</a> — Crystallization buffer (0.1 M sodium citrate pH 5.6) in structure VI
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Crystallization buffer (0.1 M HEPES pH 7.5/8.0) in multiple structures
- <a href="/xray-mp-wiki/reagents/detergents/hega-10/">HEGA-10</a> — Detergent for S129R mutant crystallization (14 mM)
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Crystallization additive (10% v/v) for S129R structure
