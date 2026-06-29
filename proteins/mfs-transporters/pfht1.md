---
title: "PfHT1 (Plasmodium falciparum Hexose Transporter 1)"
created: 2026-06-11
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.2017749118, doi/10.1038##s41586-020-1963-z]
verified: false
---

# PfHT1 (Plasmodium falciparum Hexose Transporter 1)

## Overview

PfHT1 (PF3D7_0204700) is the sole hexose transporter in Plasmodium falciparum,
the deadliest species of malaria parasite. It is a member of the major facilitator
superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)) and is essential for the survival of the blood-stage parasite by
importing D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) as the primary energy source. The crystal structure of PfHT1
in complex with D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) was determined at 3.6 A resolution (Qureshi et al., Nature
2020, PDB 6RW3), revealing a fully occluded conformation with TM7b positioned as an
extracellular substrate-gating helix. Unlike human GLUT transporters which rely on
conserved tyrosine residues for gating, PfHT1 has evolved polar residues (Ser315,
Asn316) at these positions that form allosteric contacts with TM1 residues (Lys51,
Asn48) — located approximately 15 A from the D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) binding site. These TM1-TM7b
interactions are equally critical for transport as the sugar-coordinating residues
themselves, demonstrating strong allosteric coupling between sugar binding and gating.
PfHT1 achieves broad substrate promiscuity not through modifications to its sugar-binding
site (which is remarkably similar to [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) and [GLUT5 Fructose Transporter](/xray-mp-wiki/proteins/mfs-transporters/glut5/)), but through evolved substrate-gating
dynamics. The protein was also crystallized in complex with D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) at 2.6 A resolution
(PDB 6M20) and with the inhibitor [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) at 3.7 A resolution (PDB 6M2L). Structural
comparison with human [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) revealed a unique allosteric pocket adjacent to the
glucose-binding site that is more hydrophobic than the corresponding region in [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/),
exploited to design orthosteric-allosteric dual inhibitors (TH-PF series) with potent
antiplasmodial activity. PfHT1 has been genetically validated as a drug target and is
the subject of a selective starvation antimalarial strategy.


## Publications

### doi/10.1073##pnas.2017749118

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6m20">6M20</a></td>
      <td>2.6</td>
      <td></td>
      <td>Full-length PfHT1</td>
      <td>D-<a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6m2l">6M2L</a></td>
      <td>3.7</td>
      <td></td>
      <td>Full-length PfHT1</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/c3361/">C3361 (PfHT1 Inhibitor)</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Notes</td>
      <td>Structures reported previously in Jiang et al., Cell 2020 (ref 20). PfHT1 was crystallized in complex with D-<a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> (2.6 A) and <a href="/xray-mp-wiki/reagents/ligands/c3361/">C3361 (PfHT1 Inhibitor)</a> (3.7 A).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m20">6M20</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSSKDICSENEGKKNGKSGF</span><span class="topo-outside">FSTSFKYV</span><span class="topo-membrane">LSACIASFIFGYQVSVLNT</span><span class="topo-inside">IKNFIVVEFEW</span></span>
<span class="topo-line"><span class="topo-inside">CKGEKDRLNCSNNTIQSS</span><span class="topo-membrane">FLLASVFIGAVLGCGFSG</span><span class="topo-outside">YLVQFGRRLS</span><span class="topo-membrane">LLIIYNFFFLVSIL</span></span>
<span class="topo-line"><span class="topo-membrane">TSIT</span><span class="topo-inside">HHFH</span><span class="topo-membrane">TILFARLLSGFGIGLVTVSVP</span><span class="topo-outside">MYISEMTHKDKKGAYG</span><span class="topo-membrane">VMHQLFITFGIFVAV</span></span>
<span class="topo-line"><span class="topo-membrane">MLG</span><span class="topo-inside">LAMGEGPKADSTEPLTSFAKLWWR</span><span class="topo-membrane">LMFLFPSVISLIGILALV</span><span class="topo-outside">VFFKEETPYFLFEKG</span></span>
<span class="topo-line"><span class="topo-outside">RIEESKNILKKIYETDNVDEPLNAIKEAVEQNESAKKNSLSLLSALKIPSYRYVII</span><span class="topo-membrane">LGCL</span></span>
<span class="topo-line"><span class="topo-membrane">LSGLQQFTGINVLVSNS</span><span class="topo-inside">NELYKEFLDSHLITIL</span><span class="topo-membrane">SVVMTAVNFLMTFPAIYIV</span><span class="topo-outside">EKLGRK</span><span class="topo-membrane">TL</span></span>
<span class="topo-line"><span class="topo-membrane">LLWGCVGVLVAYLPTAI</span><span class="topo-inside">ANEINRNSNFVKIL</span><span class="topo-membrane">SIVATFVMIISFAVSYGPVLWI</span><span class="topo-outside">YLHEMFP</span></span>
<span class="topo-line"><span class="topo-outside">SEIKDSAAS</span><span class="topo-membrane">LASLVNWVCAIIVVFPSD</span><span class="topo-inside">IIIKKSPS</span><span class="topo-membrane">ILFIVFSVMSILTFFFIF</span><span class="topo-outside">FFIKETK</span></span>
<span class="topo-line"><span class="topo-outside">GGEIGTSPYITMEERQKH</span><span class="topo-unknown">MTKSVV</span></span>
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
      <td>23</td>
      <td>30</td>
      <td>23</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>49</td>
      <td>31</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>78</td>
      <td>50</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>96</td>
      <td>79</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>106</td>
      <td>97</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>124</td>
      <td>107</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>128</td>
      <td>125</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>149</td>
      <td>129</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>165</td>
      <td>150</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>183</td>
      <td>166</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>207</td>
      <td>184</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>208</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>296</td>
      <td>226</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>317</td>
      <td>297</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>333</td>
      <td>318</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>352</td>
      <td>334</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>358</td>
      <td>353</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>377</td>
      <td>359</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>391</td>
      <td>378</td>
      <td>391</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>413</td>
      <td>392</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>429</td>
      <td>414</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>447</td>
      <td>430</td>
      <td>447</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>448</td>
      <td>455</td>
      <td>448</td>
      <td>455</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>456</td>
      <td>473</td>
      <td>456</td>
      <td>473</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>474</td>
      <td>498</td>
      <td>474</td>
      <td>498</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m20">6M20</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSSKDICSENEGKKNGKSG</span><span class="topo-outside">FFSTSFKYV</span><span class="topo-membrane">LSACIASFIFGYQVSVLNT</span><span class="topo-inside">IKNFIVVEFEW</span></span>
<span class="topo-line"><span class="topo-inside">CKGEKDRLNCSNNTIQSS</span><span class="topo-membrane">FLLASVFIGAVLGCGFSG</span><span class="topo-outside">YLVQFGRRLS</span><span class="topo-membrane">LLIIYNFFFLVSIL</span></span>
<span class="topo-line"><span class="topo-membrane">TSIT</span><span class="topo-inside">HHFH</span><span class="topo-membrane">TILFARLLSGFGIGLVTVSVP</span><span class="topo-outside">MYISEMTHKDKKGAYG</span><span class="topo-membrane">VMHQLFITFGIFVAV</span></span>
<span class="topo-line"><span class="topo-membrane">MLG</span><span class="topo-inside">LAMGEGPKADSTEPLTSFAKLWWR</span><span class="topo-membrane">LMFLFPSVISLIGILALV</span><span class="topo-outside">VFFKEETPYFLFEKG</span></span>
<span class="topo-line"><span class="topo-outside">RIEESKNILKKIYETDNVDEPLNAIKEAVEQNESAKKNSLSLLSALKIPSYRYVII</span><span class="topo-membrane">LGCL</span></span>
<span class="topo-line"><span class="topo-membrane">LSGLQQFTGINVLVSNS</span><span class="topo-inside">NELYKEFLDSHLITIL</span><span class="topo-membrane">SVVMTAVNFLMTFPAIYIV</span><span class="topo-outside">EKLGR</span><span class="topo-membrane">KTL</span></span>
<span class="topo-line"><span class="topo-membrane">LLWGCVGVLVAYLPTAI</span><span class="topo-inside">ANEINRNSNFVKIL</span><span class="topo-membrane">SIVATFVMIISFAVSYGPVLWI</span><span class="topo-outside">YLHEMFP</span></span>
<span class="topo-line"><span class="topo-outside">SEIKDSAAS</span><span class="topo-membrane">LASLVNWVCAIIVVFPSD</span><span class="topo-inside">IIIKKSPS</span><span class="topo-membrane">ILFIVFSVMSILTFFFIF</span><span class="topo-outside">FFIKETK</span></span>
<span class="topo-line"><span class="topo-outside">GGEIGTSPYITMEERQKHM</span><span class="topo-unknown">TKSVV</span></span>
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
      <td>22</td>
      <td>30</td>
      <td>22</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>49</td>
      <td>31</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>78</td>
      <td>50</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>96</td>
      <td>79</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>106</td>
      <td>97</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>124</td>
      <td>107</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>128</td>
      <td>125</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>149</td>
      <td>129</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>165</td>
      <td>150</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>183</td>
      <td>166</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>207</td>
      <td>184</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>208</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>296</td>
      <td>226</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>317</td>
      <td>297</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>333</td>
      <td>318</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>352</td>
      <td>334</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>357</td>
      <td>353</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>377</td>
      <td>358</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>391</td>
      <td>378</td>
      <td>391</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>413</td>
      <td>392</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>429</td>
      <td>414</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>447</td>
      <td>430</td>
      <td>447</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>448</td>
      <td>455</td>
      <td>448</td>
      <td>455</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>456</td>
      <td>473</td>
      <td>456</td>
      <td>473</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>474</td>
      <td>499</td>
      <td>474</td>
      <td>499</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m2l">6M2L</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSSKDICSENEGKKNGKSGFF</span><span class="topo-inside">STSFKYVL</span><span class="topo-membrane">SACIASFIFGYQVSVLN</span><span class="topo-outside">TIKNFIVVEFEW</span></span>
<span class="topo-line"><span class="topo-outside">C</span><span class="topo-unknown">KGEKDRLN</span><span class="topo-outside">CSNNTIQSSFL</span><span class="topo-membrane">LASVFIGAVLGCGFSGYL</span><span class="topo-inside">VQFGRRLS</span><span class="topo-membrane">LLIIYNFFFLVSIL</span></span>
<span class="topo-line"><span class="topo-membrane">TSIT</span><span class="topo-outside">HHFH</span><span class="topo-membrane">TILFARLLSGFGIGLVTVSVP</span><span class="topo-inside">MYISEMTHKDKKGAYG</span><span class="topo-membrane">VMHQLFITFGIFVAV</span></span>
<span class="topo-line"><span class="topo-membrane">MLG</span><span class="topo-outside">L</span><span class="topo-unknown">AMGEGPKADSTEPLT</span><span class="topo-outside">SFAKLWWR</span><span class="topo-membrane">LMFLFPSVISLIGILA</span><span class="topo-inside">LVVFFKEETPYFLFEKG</span></span>
<span class="topo-line"><span class="topo-inside">RIEESKNILKKIYETDNVDEPLNAIKEAVEQNESAKKNSLSLLSALKIPSYRYVI</span><span class="topo-membrane">ILGCL</span></span>
<span class="topo-line"><span class="topo-membrane">LSGLQQFTGINVLV</span><span class="topo-outside">SNSNELYKEFLDSHLITILS</span><span class="topo-membrane">VVMTAVNFLMTFPAIYIV</span><span class="topo-inside">EKLGR</span><span class="topo-membrane">KTL</span></span>
<span class="topo-line"><span class="topo-membrane">LLWGCVGVLVAYLP</span><span class="topo-outside">TAIANEINRNSNFVKILSIV</span><span class="topo-membrane">ATFVMIISFAVSYGPVLWIYL</span><span class="topo-inside">HEMFP</span></span>
<span class="topo-line"><span class="topo-inside">SEIKDS</span><span class="topo-membrane">AASLASLVNWVCAIIVV</span><span class="topo-outside">FPSDIIIKKSPSILFI</span><span class="topo-membrane">VFSVMSILTFFFIFFFI</span><span class="topo-inside">KETK</span></span>
<span class="topo-line"><span class="topo-inside">GGEIGTSPYITME</span><span class="topo-unknown">ERQKHMTKSVV</span></span>
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
      <td>24</td>
      <td>31</td>
      <td>24</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>48</td>
      <td>32</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>61</td>
      <td>49</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>80</td>
      <td>70</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>98</td>
      <td>81</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>106</td>
      <td>99</td>
      <td>106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>124</td>
      <td>107</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>128</td>
      <td>125</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>149</td>
      <td>129</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>165</td>
      <td>150</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>183</td>
      <td>166</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>184</td>
      <td>184</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>207</td>
      <td>200</td>
      <td>207</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>223</td>
      <td>208</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>295</td>
      <td>224</td>
      <td>295</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>314</td>
      <td>296</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>334</td>
      <td>315</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>352</td>
      <td>335</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>357</td>
      <td>353</td>
      <td>357</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>374</td>
      <td>358</td>
      <td>374</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>375</td>
      <td>394</td>
      <td>375</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>415</td>
      <td>395</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>416</td>
      <td>426</td>
      <td>416</td>
      <td>426</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>443</td>
      <td>427</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>459</td>
      <td>444</td>
      <td>459</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>460</td>
      <td>476</td>
      <td>460</td>
      <td>476</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>477</td>
      <td>493</td>
      <td>477</td>
      <td>493</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##s41586-020-1963-z

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6rw3">6RW3</a></td>
      <td>3.6</td>
      <td></td>
      <td>Full-length PfHT1 crystallized in D-glucose-bound occluded conformation</td>
      <td>D-<a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a></td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rw3">6RW3</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MEKEDSG</span><span class="topo-outside">FFSTSFKYV</span><span class="topo-membrane">LSACIASFIFGYQVSVLNT</span><span class="topo-inside">I</span><span class="topo-unknown">KNFIVVEF</span><span class="topo-inside">E</span><span class="topo-unknown">WCKGEKDRLN</span><span class="topo-inside">CSNNT</span></span>
<span class="topo-line"><span class="topo-inside">IQSS</span><span class="topo-membrane">FLLASVFIGAVLGCGFSGYL</span><span class="topo-outside">VQFGRRL</span><span class="topo-membrane">SLLIIYNFFFLVSILTSI</span><span class="topo-inside">THHFH</span><span class="topo-membrane">TILFAR</span></span>
<span class="topo-line"><span class="topo-membrane">LLSGFGIGLVTVSVP</span><span class="topo-outside">MYISEMTHKDKKGA</span><span class="topo-membrane">YGVMHQLFITFGIFVAVMLG</span><span class="topo-inside">LAMGE</span><span class="topo-unknown">GPKADS</span></span>
<span class="topo-line"><span class="topo-unknown">TEPL</span><span class="topo-inside">TSFAKLWWR</span><span class="topo-membrane">LMFLFPSVISLIGILALVV</span><span class="topo-outside">FFKEETPYFLFEKGRIEESKNILKKIYE</span></span>
<span class="topo-line"><span class="topo-outside">TDNVDEPLNAIKEAVEQNESAKKNSLSLLSALKIPSYRYVII</span><span class="topo-membrane">LGCLLSGLQQFTGINVLV</span></span>
<span class="topo-line"><span class="topo-membrane">SNS</span><span class="topo-inside">NELYKEFLDSHLITIL</span><span class="topo-membrane">SVVMTAVNFLMTFPAIYIV</span><span class="topo-outside">EKLGR</span><span class="topo-membrane">KTLLLWGCVGVLVAYLP</span></span>
<span class="topo-line"><span class="topo-membrane">TAI</span><span class="topo-inside">ANE</span><span class="topo-unknown">INRNS</span><span class="topo-inside">NFVKIL</span><span class="topo-membrane">SIVATFVMIISFAVSYGPVLWIYL</span><span class="topo-outside">HEMFPSEIKDSAA</span><span class="topo-membrane">SLASLV</span></span>
<span class="topo-line"><span class="topo-membrane">NWVCAIIVVFPSD</span><span class="topo-inside">IIIKKSPS</span><span class="topo-membrane">ILFIVFSVMSILTFFFIFF</span><span class="topo-outside">FIKETKGGE</span><span class="topo-unknown">IGTSPYITMEE</span></span>
<span class="topo-line"><span class="topo-unknown">RQKHMTKSVVENLYFQ</span></span>
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
      <td>8</td>
      <td>16</td>
      <td>22</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>35</td>
      <td>31</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>36</td>
      <td>50</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>44</td>
      <td>51</td>
      <td>58</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>45</td>
      <td>45</td>
      <td>59</td>
      <td>59</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>70</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>84</td>
      <td>79</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>91</td>
      <td>99</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>109</td>
      <td>106</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>124</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>135</td>
      <td>129</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>149</td>
      <td>150</td>
      <td>163</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>169</td>
      <td>164</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>174</td>
      <td>184</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>193</td>
      <td>199</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>212</td>
      <td>208</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>282</td>
      <td>227</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>303</td>
      <td>297</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>319</td>
      <td>318</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>338</td>
      <td>334</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>343</td>
      <td>353</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>363</td>
      <td>358</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>366</td>
      <td>378</td>
      <td>380</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>377</td>
      <td>386</td>
      <td>391</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>378</td>
      <td>401</td>
      <td>392</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>402</td>
      <td>414</td>
      <td>416</td>
      <td>428</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>415</td>
      <td>433</td>
      <td>429</td>
      <td>447</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>434</td>
      <td>441</td>
      <td>448</td>
      <td>455</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>460</td>
      <td>456</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>461</td>
      <td>469</td>
      <td>475</td>
      <td>483</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rw3">6RW3</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MEKEDSG</span><span class="topo-outside">FFSTSFKYV</span><span class="topo-membrane">LSACIASFIFGYQVSVLNT</span><span class="topo-inside">I</span><span class="topo-unknown">KNFIVVEF</span><span class="topo-inside">E</span><span class="topo-unknown">WCKGEKDRLN</span><span class="topo-inside">CSNNT</span></span>
<span class="topo-line"><span class="topo-inside">IQSS</span><span class="topo-membrane">FLLASVFIGAVLGCGFSGYL</span><span class="topo-outside">VQFGRRL</span><span class="topo-membrane">SLLIIYNFFFLVSILTSIT</span><span class="topo-inside">HHFH</span><span class="topo-membrane">TILFAR</span></span>
<span class="topo-line"><span class="topo-membrane">LLSGFGIGLVTVSVP</span><span class="topo-outside">MYISEMTHKDKKGA</span><span class="topo-membrane">YGVMHQLFITFGIFVAVMLG</span><span class="topo-inside">LAMGEGPK</span><span class="topo-unknown">ADS</span></span>
<span class="topo-line"><span class="topo-unknown">TEPL</span><span class="topo-inside">TSFAKLWWR</span><span class="topo-membrane">LMFLFPSVISLIGILALVV</span><span class="topo-outside">FFKEETPYFLFEKGRIEESKNILKKIYE</span></span>
<span class="topo-line"><span class="topo-outside">TDNVDEPLNAIKEAVEQNESAKKNSLSLLSALKIPSYRYVII</span><span class="topo-membrane">LGCLLSGLQQFTGINVLV</span></span>
<span class="topo-line"><span class="topo-membrane">SNS</span><span class="topo-inside">NELYKEFLDSHLITIL</span><span class="topo-membrane">SVVMTAVNFLMTFPAIYIV</span><span class="topo-outside">EKLGR</span><span class="topo-membrane">KTLLLWGCVGVLVAYLP</span></span>
<span class="topo-line"><span class="topo-membrane">TAI</span><span class="topo-inside">ANEIN</span><span class="topo-unknown">RNS</span><span class="topo-inside">NFVKIL</span><span class="topo-membrane">SIVATFVMIISFAVSYGPVLWIYL</span><span class="topo-outside">HEMFPSEIKDSAA</span><span class="topo-membrane">SLASLV</span></span>
<span class="topo-line"><span class="topo-membrane">NWVCAIIVVFPSD</span><span class="topo-inside">IIIKKSPS</span><span class="topo-membrane">ILFIVFSVMSILTFFFIFF</span><span class="topo-outside">FIKETK</span><span class="topo-unknown">GGEIGTSPYITMEE</span></span>
<span class="topo-line"><span class="topo-unknown">RQKHMTKSVVENLYFQ</span></span>
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
      <td>8</td>
      <td>16</td>
      <td>22</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>35</td>
      <td>31</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>36</td>
      <td>50</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>44</td>
      <td>51</td>
      <td>58</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>45</td>
      <td>45</td>
      <td>59</td>
      <td>59</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>70</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>84</td>
      <td>79</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>91</td>
      <td>99</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>110</td>
      <td>106</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>114</td>
      <td>125</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>135</td>
      <td>129</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>149</td>
      <td>150</td>
      <td>163</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>169</td>
      <td>164</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>177</td>
      <td>184</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>193</td>
      <td>199</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>212</td>
      <td>208</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>282</td>
      <td>227</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>303</td>
      <td>297</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>319</td>
      <td>318</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>338</td>
      <td>334</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>343</td>
      <td>353</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>363</td>
      <td>358</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>368</td>
      <td>378</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>377</td>
      <td>386</td>
      <td>391</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>378</td>
      <td>401</td>
      <td>392</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>402</td>
      <td>414</td>
      <td>416</td>
      <td>428</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>415</td>
      <td>433</td>
      <td>429</td>
      <td>447</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>434</td>
      <td>441</td>
      <td>448</td>
      <td>455</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>460</td>
      <td>456</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>461</td>
      <td>466</td>
      <td>475</td>
      <td>480</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Allosteric coupling between TM1 and TM7b drives sugar transport in PfHT1

The 3.6 A crystal structure of PfHT1 (PDB 6RW3) revealed that polar contacts
between the extracellular gating helix TM7b (residues Asn311, Asn316, Ser317, Asn318)
and TM1 (residues Lys51, Asn48) — located approximately 15 A from the D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) binding
site — are just as critical for transport as residues that directly coordinate D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/).
In human GLUT transporters, two conserved tyrosine residues on TM7b form occlusion
contacts, but in PfHT1 these are replaced by Ser315 and Asn316. Substitution of either
with tyrosine abolished transport. Asn316 interacts with Lys51 on TM1, and mutations
of Lys51 (to Ala or Gln) also rendered PfHT1 non-functional. Molecular dynamics
simulations (1 microsecond) showed that TM7b in human [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) is highly mobile and moves
apart from TM1 to release D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/), whereas TM7b in PfHT1 maintains an occluded
conformation. This demonstrates strong allosteric coupling between sugar binding and
gating, suggesting that TM1-TM7b interactions should be considered more closely in
establishing transport mechanisms in general.

### Sugar promiscuity in PfHT1 is achieved through gating dynamics, not binding-site modification

Unlike human GLUT transporters which show narrow substrate specificity, PfHT1
transports both D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) and [D-Fructose](/xray-mp-wiki/reagents/ligands/d-fructose/) with kinetics similar to dedicated [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/)
and [GLUT5 Fructose Transporter](/xray-mp-wiki/proteins/mfs-transporters/glut5/). The sugar-binding site in PfHT1 is remarkably similar to those of
distantly related [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) and [GLUT5 Fructose Transporter](/xray-mp-wiki/proteins/mfs-transporters/glut5/), and engineered PfHT1 mutations to match GLUT
sugar-binding sites did not shift sugar preferences. The C3-hydroxyl group orientation
was determined as the most critical for D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) recognition. PfHT1 achieves substrate
promiscuity by evolving substrate-gating dynamics rather than modifying its binding site.
The C3- and C4-hydroxyl groups hydrogen bond to Asn311 and Gln306, while C1- and C2-
hydroxyl groups bond to Gln169, Gln305 and Trp412. Asn311 in TM7b is the only binding-site
residue that moves substantially during the transport cycle, forming hydrogen bonds with
the critically important C3- and C4-hydroxyl groups during transition to the occluded state.

### PfHT1 is the sole hexose transporter in P. falciparum

PfHT1 is transcribed from a single-copy gene with no close paralogue and is
essential for the survival of the blood-stage parasite. [Glucose](/xray-mp-wiki/reagents/additives/glucose/) is the primary
energy source for blood-stage P. falciparum, making PfHT1 a validated antimalarial
target. The blood-stage parasites depend on constant [Glucose](/xray-mp-wiki/reagents/additives/glucose/) supply, and PfHT1
inhibition leads to glycolysis shutdown and parasite death.

### Unique allosteric pocket in PfHT1 enables selective inhibitor design

Structural comparison between PfHT1 and [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) revealed an additional pocket
adjacent to the substrate-binding site, linked by a narrow hydrophobic channel.
This allosteric site is highly hydrophobic in PfHT1 but more hydrophilic in [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/),
providing a structural basis for designing selective PfHT1 inhibitors. The allosteric
pocket was exploited to design dual orthosteric–allosteric inhibitors (TH-PF series)
that simultaneously block both the glucose-binding site and the adjacent allosteric
pocket, achieving high selectivity over human GLUT transporters.

### Selectivity over human GLUT transporters

The TH-PF series of compounds showed selective inhibition of PfHT1 over [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/).
Key residues in the connecting channel (F85, V44 in PfHT1) are responsible for the
hydrophobic nature of the allosteric pocket. Mutating these residues to their human
[SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) counterparts (F85S, V44T) decreased inhibitor potency, confirming that the
hydrophobicity of the allosteric channel is critical for selectivity.


## Cross-References

- <a href="/xray-mp-wiki/proteins/mfs-transporters/hglut1/">hGLUT1 (Human Glucose Transporter 1)</a> — Human ortholog used for selectivity comparison in drug design
- <a href="/xray-mp-wiki/proteins/mfs-transporters/hglut3/">hGLUT3 (Human Glucose Transporter 3)</a> — Crystal structure of hGLUT3-C3361 complex (2.3 A) used to confirm PfHT1-specific allosteric pocket
- <a href="/xray-mp-wiki/concepts/miscellaneous/selective-starvation/">Selective Starvation of Malaria Parasites</a> — PfHT1 inhibition is the basis of the selective starvation antimalarial strategy
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/orthosteric-allosteric-dual-inhibition/">Orthosteric–Allosteric Dual Inhibition</a> — TH-PF series compounds simultaneously target orthosteric and allosteric sites of PfHT1
- <a href="/xray-mp-wiki/reagents/ligands/c3361/">C3361 (PfHT1 Inhibitor)</a> — Reference compound used to identify the allosteric pocket in PfHT1
- <a href="/xray-mp-wiki/reagents/ligands/th-pf01/">TH-PF01</a> — Lead dual inhibitor targeting PfHT1 orthosteric and allosteric pockets
- <a href="/xray-mp-wiki/reagents/ligands/th-pf02/">TH-PF02</a> — Lead dual inhibitor targeting PfHT1 orthosteric and allosteric pockets
- <a href="/xray-mp-wiki/reagents/ligands/th-pf03/">TH-PF03</a> — Lead dual inhibitor targeting PfHT1 orthosteric and allosteric pockets
- <a href="/xray-mp-wiki/concepts/mfs-transporter-mechanism/">Major Facilitator Superfamily Transport Mechanism</a> — PfHT1 exhibits rocker-switch alternating-access mechanism typical of MFS transporters
- <a href="/xray-mp-wiki/concepts/alternating-access/">Alternating Access Mechanism</a> — The occluded PfHT1 structure combined with previous sugar-porter structures reconstructs the MFS transport cycle
- <a href="/xray-mp-wiki/concepts/allosteric-coupling/">Allosteric Coupling in Transporters</a> — TM1-TM7b interactions 15 A from the sugar site demonstrate long-range allosteric coupling between sugar binding and gating
- <a href="/xray-mp-wiki/reagents/ligands/mmv009085/">MMV009085 (PfHT1 Inhibitor)</a> — MMV009085 binds in the sugar-binding pocket and its inhibition depends on Trp412
- <a href="/xray-mp-wiki/reagents/ligands/cytochalasin-b/">Cytochalasin B</a> — Cytochalasin B inhibits PfHT1 by binding to the hydrophobic-side vestibule adjacent to the sugar-binding site
