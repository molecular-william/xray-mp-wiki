---
title: "Kir3.1-KirBac1.3 Chimeric GIRK Channel"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##sj.emboj.7601828]
verified: pdb-pass
uniprot_id: Q146M9
---

# Kir3.1-KirBac1.3 Chimeric GIRK Channel

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q146M9">UniProt: Q146M9</a>

<span class="expr-badge">Paraburkholderia xenovorans (strain LB400)</span>

## Overview

The Kir3.1 (GIRK1) K+ channel is a G-protein-gated inward rectifier that participates in heart rate control and neuronal excitability. A chimeric channel was constructed by replacing three-fourths of the transmembrane pore of mouse Kir3.1 with the pore of the prokaryotic KirBac1.3 channel from Burkholderia xenovorans, leaving the cytoplasmic pore and membrane interfacial regions of Kir3.1 origin. Two crystal structures were determined at 2.2 Å resolution, revealing a closed inner helix bundle gate and two conformations of the cytoplasmic pore (dilated and constricted), mediated by rigid-body movements of the G-loop. The selectivity filter is nearly identical to [KcsA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) (r.m.s.d. < 0.2 Å), demonstrating extreme structural conservation of the K+ selectivity mechanism.


## Publications

### doi/10.1038##sj.emboj.7601828

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2qks">2QKS</a></td>
      <td>2.2</td>
      <td>P4</td>
      <td>Chimeric channel — N-terminal KirBac1.3 sequence (aa 1-23 + LV insertion) fused to mouse Kir3.1 (aa 41-82, 178-371) with M180A mutation; C-terminal His6-tag (VPRGSGGLEHHHHHH); thrombin-cleavable N-terminus; expressed in pET-28b(+)</td>
      <td>Rb+ ions (7 sites from RbCl soak), nonylglucoside (detergent molecule at PIP2-binding site)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: Kir3.1-KirBac1.3 chimera in pET-28b(+); aa 1-23 KirBac1.3 + LV insertion + aa 41-82 and 178-371 of mouse Kir3.1 (M180A); C-terminal His6-tag; thrombin site for N-terminus removal
- **Notes**: N-terminus of KirBac1.3 retained for correct membrane insertion in E. coli, then removed by thrombin cleavage before crystallization
- **Induction**: 300 µM IPTG at OD600 = 2.0; temperature lowered to 23°C; 12-15 h induction
- **Media**: LB medium

**Purification:**

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: Full-length chimera with C-terminal His6-tag in pET-28b(+)
- **Tag info**: C-terminal His6-tag (VPRGSGGLEHHHHHH); N-terminal KirBac1.3 sequence removed by thrombin cleavage

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
      <td>Shaker flask fermentation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>16 L LB medium; cells grown at 37°C to OD600 = 2.0, then induced at 23°C for 12-15 h</td>
    </tr>
    <tr>
      <td>Cell harvesting and resuspension</td>
      <td>Centrifugation</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 7.5, 150 mM KCl + --</td>
      <td>Protease inhibitors: 100 µM PMSF, 1 µg/ml leupeptin, 1 µg/ml pepstatin, 1000× aprotinin</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>French press</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 7.5, 150 mM KCl + --</td>
      <td>French pressure cell press at 15,000 psi, 4°C</td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 7.5, 150 mM KCl + 20 mM dodecylmaltopyranoside (DDM)</td>
      <td>Gentle shaking for 2 h at room temperature; debris removed by centrifugation at 40,000 g for 20 min</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>--</td>
      <td>--</td>
      <td>-- + --</td>
      <td>His6-tag purification (details not specified in text); N-terminal KirBac1.3 tag removed by thrombin cleavage before crystallization</td>
    </tr>
    <tr>
      <td>Final purification and detergent exchange</td>
      <td>Size exclusion chromatography (inferred)</td>
      <td>--</td>
      <td>-- + Nonylglucoside</td>
      <td>Purified as stable tetramer in nonylglucoside for crystallization; final sample contained channel in nonylglucoside</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified chimera tetramer in nonylglucoside detergent

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified Kir3.1-KirBac1.3 chimera in nonylglucoside</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>120 mM KCl, 200 mM potassium phosphate, PEG 4000, pH 6.2</td>
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
      <td>Crystals in space group P4 (a = b = 98.42 Å, c = 92.62 Å); two unique subunits per asymmetric unit, producing two distinct four-fold symmetric channels (dilated and constricted cytoplasmic pore conformations). RbCl soak used to identify permeant ions at 2.4 Å. Data collected at Brookhaven X29 beamline. Resolution: 100-2.2 Å.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qks">2QKS</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GS</span><span class="topo-outside">KKRQRFVDKNGRCNVQHGN</span><span class="topo-unknown">LGSETSR</span><span class="topo-outside">YL</span><span class="topo-unknown">SDLFTTLVD</span><span class="topo-outside">LK</span><span class="topo-membrane">WRWFFVSLAVLFLLLNTAFATLYMLG</span><span class="topo-inside">SAPIANQFPAGF</span><span class="topo-unknown">GGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQTV</span><span class="topo-membrane">YAHWIATLEIFVGMSSI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ALATGCAF</span><span class="topo-outside">IKMSQPKKRAETLMFSEHAVISMRDGKLTLMFRVGNLRNSHMVSAQIRCKLLKSRQTPEGEFLPLDQLELDVGFSTGADQLFLVSPLTICHVIDAKSPFYDLSQRSMQTEQF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320 </span>
<span class="topo-line"><span class="topo-outside">EVVVILEGIVETTGMTCQARTSYTEDEVLWGHRFFPVISLEEGFFKVDYSQFHATFEVPTPPYSVKEQEEM</span><span class="topo-unknown">LLMSSPLVPR</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>21</td>
      <td>3</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>28</td>
      <td>22</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>30</td>
      <td>29</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>39</td>
      <td>31</td>
      <td>39</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>40</td>
      <td>41</td>
      <td>40</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>67</td>
      <td>42</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>79</td>
      <td>68</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>96</td>
      <td>80</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>103</td>
      <td>97</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>128</td>
      <td>104</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>311</td>
      <td>129</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>321</td>
      <td>312</td>
      <td>321</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qks">2QKS</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GS</span><span class="topo-outside">KKRQRFVDKNGRCNVQHGN</span><span class="topo-unknown">LGSETSR</span><span class="topo-outside">YL</span><span class="topo-unknown">SDLFTTLVD</span><span class="topo-outside">LK</span><span class="topo-membrane">WRWFFVSLAVLFLLLNTAFATLYMLG</span><span class="topo-inside">SAPIANQFPAGF</span><span class="topo-unknown">GGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQTV</span><span class="topo-membrane">YAHWIATLEIFVGMSSI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ALATGCAF</span><span class="topo-outside">IKMSQPKKRAETLMFSEHAVISMRDGKLTLMFRVGNLRNSHMVSAQIRCKLLKSRQTPEGEFLPLDQLELDVGFSTGADQLFLVSPLTICHVIDAKSPFYDLSQRSMQTEQF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320 </span>
<span class="topo-line"><span class="topo-outside">EVVVILEGIVETTGMTCQARTSYTEDEVLWGHRFFPVISLEEGFFKVDYSQFHATFEVPTPPYSVKEQEEM</span><span class="topo-unknown">LLMSSPLVPR</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>21</td>
      <td>3</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>28</td>
      <td>22</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>30</td>
      <td>29</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>39</td>
      <td>31</td>
      <td>39</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>40</td>
      <td>41</td>
      <td>40</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>67</td>
      <td>42</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>79</td>
      <td>68</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>96</td>
      <td>80</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>103</td>
      <td>97</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>128</td>
      <td>104</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>311</td>
      <td>129</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>321</td>
      <td>312</td>
      <td>321</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qks">2QKS</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GS</span><span class="topo-outside">KKRQRFVDKNGRCNVQHGN</span><span class="topo-unknown">LGSETSR</span><span class="topo-outside">YL</span><span class="topo-unknown">SDLFTTLVD</span><span class="topo-outside">LK</span><span class="topo-membrane">WRWFFVSLAVLFLLLNTAFATLYMLG</span><span class="topo-inside">SAPIANQFPAGF</span><span class="topo-unknown">GGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQTV</span><span class="topo-membrane">YAHWIATLEIFVGMSSI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ALATGCAF</span><span class="topo-outside">IKMSQPKKRAETLMFSEHAVISMRDGKLTLMFRVGNLRNSHMVSAQIRCKLLKSRQTPEGEFLPLDQLELDVGFSTGADQLFLVSPLTICHVIDAKSPFYDLSQRSMQTEQF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320 </span>
<span class="topo-line"><span class="topo-outside">EVVVILEGIVETTGMTCQARTSYTEDEVLWGHRFFPVISLEEGFFKVDYSQFHATFEVPTPPYSVKEQEEM</span><span class="topo-unknown">LLMSSPLVPR</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>21</td>
      <td>3</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>28</td>
      <td>22</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>30</td>
      <td>29</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>39</td>
      <td>31</td>
      <td>39</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>40</td>
      <td>41</td>
      <td>40</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>67</td>
      <td>42</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>79</td>
      <td>68</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>96</td>
      <td>80</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>103</td>
      <td>97</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>128</td>
      <td>104</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>311</td>
      <td>129</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>321</td>
      <td>312</td>
      <td>321</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qks">2QKS</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GS</span><span class="topo-outside">KKRQRFVDKNGRCNVQHGN</span><span class="topo-unknown">LGSETSR</span><span class="topo-outside">YL</span><span class="topo-unknown">SDLFTTLVD</span><span class="topo-outside">LK</span><span class="topo-membrane">WRWFFVSLAVLFLLLNTAFATLYMLG</span><span class="topo-inside">SAPIANQFPAGF</span><span class="topo-unknown">GGAFFFSVETLATVGYG</span><span class="topo-inside">DMHPQTV</span><span class="topo-membrane">YAHWIATLEIFVGMSSI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ALATGCAF</span><span class="topo-outside">IKMSQPKKRAETLMFSEHAVISMRDGKLTLMFRVGNLRNSHMVSAQIRCKLLKSRQTPEGEFLPLDQLELDVGFSTGADQLFLVSPLTICHVIDAKSPFYDLSQRSMQTEQF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320 </span>
<span class="topo-line"><span class="topo-outside">EVVVILEGIVETTGMTCQARTSYTEDEVLWGHRFFPVISLEEGFFKVDYSQFHATFEVPTPPYSVKEQEEM</span><span class="topo-unknown">LLMSSPLVPR</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>21</td>
      <td>3</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>28</td>
      <td>22</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>30</td>
      <td>29</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>39</td>
      <td>31</td>
      <td>39</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>40</td>
      <td>41</td>
      <td>40</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>67</td>
      <td>42</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>79</td>
      <td>68</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>96</td>
      <td>80</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>103</td>
      <td>97</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>128</td>
      <td>104</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>311</td>
      <td>129</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>321</td>
      <td>312</td>
      <td>321</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Extreme conservation of K+ selectivity filter structure

The selectivity filter of the Kir3.1-KirBac1.3 chimera and KcsA are nearly identical (r.m.s.d. < 0.2 Å for main chain atoms), within the error of measurement between independent refinements of KcsA structures. This demonstrates that the K+ selectivity filter requires extreme conservation of three-dimensional structure for its catalytic function. The deviations are smaller than the difference in ionic radius between K+ and Na+ (0.38 Å).

### Seven ion binding sites in the conduction pore

Four Rb+ ion positions in the selectivity filter (positions 1-4, corresponding to KcsA ions), a fifth in the central cavity, and a sixth and seventh between the transmembrane and cytoplasmic pores. The ion positions at the TMD-cytoplasmic interface are unique to this Kir channel structure and were identified by RbCl soaking experiments.

### Dual gates — inner helix bundle and G-loop

Two constrictions along the pore: (1) the inner helix bundle gate formed by Phe181 side chains that completely occlude the pore (closed conformation, similar to KirBac1.1), and (2) the G-loop (residues 301-309) at the apex of the cytoplasmic pore. Two structures in one crystal show the G-loop in dilated and constricted conformations. The dilated conformation is wide enough for a hydrated K+ to pass; the constricted conformation is lined by Met308 and too narrow for even a dehydrated K+ ion.

### G-loop gating by rigid-body domain movements

Gating of the cytoplasmic pore apex is mediated by rigid-body movements of the cytoplasmic pore subunits. In the dilated conformation, the G-loop exposes oxygen atoms (Thr306 and Gly307) on its surface; in the constricted conformation, Met308 sulfur atoms line a narrow constriction. This finding supports numerous studies identifying the G-loop as a potential gate in Kir channels.

### PIP2-interacting residues mapped onto the chimera

Several known PIP2-sensitive mutations from eukaryotic Kir channels (Kir1.1, Kir2.1, Kir3.x, Kir6.2) map to cationic clusters on the membrane-facing surface of the cytoplasmic pore (Lys188, Lys189, Arg219) and to buried positions (Arg190, Glu304, Arg313). A nonylglucoside detergent molecule was observed bound at the putative PIP2-binding site in the dilated conformation, adjacent to the G-loop and interfacial helix, suggesting competition between detergent and PIP2 for the binding pocket.

### Disease mutations in the G-loop

In Kir2.1, mutations within the G-loop (G300V, V302M, E303K) cause Andersen's syndrome. The equivalent positions in the chimera map to the G-loop region (residues 301-309). In Kir6.2, mutation I296L (equivalent to M308 in Kir3.1) causes a severe form of DEND syndrome characterized by neonatal diabetes and developmental abnormalities. These mutations cluster at the cytoplasmic pore apex, supporting its role in Kir channel gating.

### No channel activity in planar lipid bilayers

The chimera showed no detectable channel activity in planar lipid membranes (POPE:POPG 3:1). Possible reasons include: unmet lipid requirement, Kir3.1 normally functions as a heteromultimer (chimera is homomultimeric), lack of proper coupling between cytoplasmic and transmembrane pores, and that no prokaryotic Kir channel has demonstrated single-channel activity.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/girk1-cytoplasmic-pore/">GIRK1 Cytoplasmic Pore</a> — Kir3.1 cytoplasmic domain structure; the chimera incorporates Kir3.1 cytoplasmic pore residues 41-82 and 178-371
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/">KirBac Potassium Channels</a> — Related prokaryotic Kir channels; the chimera transmembrane pore derives from KirBac1.3
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — High-resolution K+ channel structure used for selectivity filter comparison (r.m.s.d. < 0.2 Å)
- <a href="/xray-mp-wiki/reagents/detergents/nonylglucoside/">Nonylglucoside (NG)</a> — Primary detergent for purification and crystallization; observed bound at PIP2-binding site
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Used at 20 mM for membrane extraction during purification
- <a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French Press</a> — Cell lysis method at 15,000 psi
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/">Selectivity Filter</a> — The chimera structure demonstrates extreme structural conservation of the K+ selectivity filter
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/">Channel Gating</a> — Dual-gate mechanism (inner helix bundle and G-loop) elucidated by two conformations in the same crystal
