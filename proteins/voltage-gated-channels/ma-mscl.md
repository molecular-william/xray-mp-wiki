---
title: "MaMscL (Methanosarcina acetivorans Mechanosensitive Channel of Large Conductance)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1503202112]
verified: false
---

# MaMscL (Methanosarcina acetivorans Mechanosensitive Channel of Large Conductance)

## Overview

[MSCL](/xray-mp-wiki/proteins/other-ion-channels/mscl/) (mechanosensitive channel of large conductance) from Methanosarcina acetivorans (MaMscL) is a prokaryotic pressure-relief valve that protects cells from lysis during acute osmotic downshock. MaMscL forms a homo-pentameric channel that responds to membrane tension by opening a non-selective pore of ~30 Å width with a unitary conductance of ~3 nS. Structures of MaMscL were solved in closed and expanded intermediate states using a fusion protein strategy with [Riboflavin (Vitamin B2)](/xray-mp-wiki/reagents/cofactors/riboflavin/) synthase (MjRS) from Methanocaldococcus jannaschii to enhance crystallizability.


## Publications

### doi/10.1073##pnas.1503202112

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a></td>
      <td></td>
      <td></td>
      <td>MaMscL-MjRS fusion (full-length MaMscL with C-terminal MjRS fusion)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a></td>
      <td></td>
      <td></td>
      <td>MaMscL-MjRS fusion (full-length MaMscL with C-terminal MjRS fusion)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: MaMscL-MjRS fusion (C-terminal fusion with Methanocaldococcus jannaschii [Riboflavin (Vitamin B2)](/xray-mp-wiki/reagents/cofactors/riboflavin/) synthase)
- **Notes**: Fusion protein enhances crystallizability by providing a large hydrophilic scaffold

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: MaMscL-MjRS fusion

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
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td></td>
      <td></td>
      <td>Purified in two different detergent types for distinct crystal forms</td>
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
      <td>MaMscL-MjRS fusion in detergent type 1</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Form 1 crystals - closed state, different space group</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>MaMscL-MjRS fusion in detergent type 2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Form 2 crystals - expanded intermediate state, different space group</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMG</span><span class="topo-outside">LFSEFKEFLYEYKVIPLAIAF</span><span class="topo-membrane">IMGIASTALIKSFVDNIIMPIIT</span><span class="topo-inside">PFVPGGGWETATVELGPIVI</span><span class="topo-membrane">SWGAFLGELVNFIIIAFAV</span><span class="topo-outside">FIIAKKVLQEEKVEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TKKVGIVDTTFARVDMASIAIKKLKELSPNIKIIRKTVPGIKDLPVACKKLLEEEGCDIVMALGMPGKAEKDKVCAHEASLGLMLAQLMTNKHIIEVFVHEDEAKDDKELDWLAKRRAEE</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-outside">HAENVYYLLFKPEYLTRMAGKGLRQGFEDAGP</span><span class="topo-unknown">ARE</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>43</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>24</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>47</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>105</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>272</td>
      <td>86</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMG</span><span class="topo-outside">LFSEFKEFLYEYKVIPLAIAF</span><span class="topo-membrane">IMGIASTALIKSFVDNIIMPIIT</span><span class="topo-inside">PFVPGGGWETATVELGPIVI</span><span class="topo-membrane">SWGAFLGELVNFIIIAFAV</span><span class="topo-outside">FIIAKKVLQEEKVEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TKKVGIVDTTFARVDMASIAIKKLKELSPNIKIIRKTVPGIKDLPVACKKLLEEEGCDIVMALGMPGKAEKDKVCAHEASLGLMLAQLMTNKHIIEVFVHEDEAKDDKELDWLAKRRAEE</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-outside">HAENVYYLLFKPEYLTRMAGKGL</span><span class="topo-unknown">RQGFEDAGPARE</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>43</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>24</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>47</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>105</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>263</td>
      <td>86</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMG</span><span class="topo-outside">LFSEFKEFLYEYKVIPLAIAF</span><span class="topo-membrane">IMGIASTALIKSFVDNIIMPIIT</span><span class="topo-inside">PFVPGGGWETATVELGPIVI</span><span class="topo-membrane">SWGAFLGELVNFIIIAFA</span><span class="topo-outside">VFIIAKKVLQEEKVEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TKKVGIVDTTFARVDMASIAIKKLKELSPNIKIIRKTVPGIKDLPVACKKLLEEEGCDIVMALGMPGKAEKDKVCAHEASLGLMLAQLMTNKHIIEVFVHEDEAKDDKELDWLAKRRAEE</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-outside">HAENVYYLLFKPEYLTRMA</span><span class="topo-unknown">G</span><span class="topo-outside">KGLR</span><span class="topo-unknown">QGFEDAGPARE</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>43</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>24</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>47</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>67</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>259</td>
      <td>85</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>260</td>
      <td>240</td>
      <td>240</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>261</td>
      <td>264</td>
      <td>241</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMG</span><span class="topo-outside">LFSEFKEFLYEYKVIPLAIAF</span><span class="topo-membrane">IMGIASTALIKSFVDNIIMPIIT</span><span class="topo-inside">PFVPGGGWETATVELGPIVI</span><span class="topo-membrane">SWGAFLGELVNFIIIAFAV</span><span class="topo-outside">FIIAKKVLQEEKVEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TKKVGIVDTTFARVDMASIAIKKLKELSPNIKIIRKTVPGIKDLPVACKKLLEEEGCDIVMALGMPGKAEKDKVCAHEASLGLMLAQLMTNKHIIEVFVHEDEAKDDKELDWLAKRRAEE</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-outside">HAENVYYLLFKPEYLTRMAGKGLR</span><span class="topo-unknown">QGFEDAGPARE</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>43</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>24</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>47</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>105</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>264</td>
      <td>86</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMG</span><span class="topo-outside">LFSEFKEFLYEYKVIPLAIAF</span><span class="topo-membrane">IMGIASTALIKSFVDNIIMPIIT</span><span class="topo-inside">PFVPGGGWETATVELGPIVI</span><span class="topo-membrane">SWGAFLGELVNFIIIAFAV</span><span class="topo-outside">FIIAKKVLQEEKVEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TKKVGIVDTTFARVDMASIAIKKLKELSPNIKIIRKTVPGIKDLPVACKKLLEEEGCDIVMALGMPGKAEKDKVCAHEASLGLMLAQLMTNKHIIEVFVHEDEAKDDKELDWLAKRRAEE</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-outside">HAENVYYLLFKPEYLTRMAGKGLR</span><span class="topo-unknown">QGFEDAGPARE</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>43</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>24</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>47</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>105</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>264</td>
      <td>86</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMG</span><span class="topo-outside">LFSEFKEFLYEYKVIPLAIAF</span><span class="topo-membrane">IMGIASTALIKSFVDNIIMPIIT</span><span class="topo-inside">PFVPGGGWETATVELGPIVI</span><span class="topo-membrane">SWGAFLGELVNFIIIAFAV</span><span class="topo-outside">FIIAKKVLQEEKVEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TKKVGIVDTTFARVDMASIAIKKLKELSPNIKIIRKTVPGIKDLPVACKKLLEEEGCDIVMALGMPGKAEKDKVCAHEASLGLMLAQLMTNKHIIEVFVHEDEAKDDKELDWLAKRRAEE</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-outside">HAENVYYLLFKPEYLTRMAGKGLRQGFEDAGP</span><span class="topo-unknown">ARE</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>43</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>24</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>47</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>105</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>272</td>
      <td>86</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMG</span><span class="topo-outside">LFSEFKEFLYEYKVIPLAIAF</span><span class="topo-membrane">IMGIASTALIKSFVDNIIMPIIT</span><span class="topo-inside">PFVPGGGWETATVELGPIVI</span><span class="topo-membrane">SWGAFLGELVNFIIIAFAV</span><span class="topo-outside">FIIAKKVLQEEKVEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TKKVGIVDTTFARVDMASIAIKKLKELSPNIKIIRKTVPGIKDLPVACKKLLEEEGCDIVMALGMPGKAEKDKVCAHEASLGLMLAQLMTNKHIIEVFVHEDEAKDDKELDWLAKRRAEE</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-outside">HAENVYYLLFKPEYLTRMAGKGL</span><span class="topo-unknown">RQGFEDAGPARE</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>43</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>24</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>47</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>105</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>263</td>
      <td>86</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMG</span><span class="topo-outside">LFSEFKEFLYEYKVIPLAIAF</span><span class="topo-membrane">IMGIASTALIKSFVDNIIMPIIT</span><span class="topo-inside">PFVPGGGWETATVELGPIVI</span><span class="topo-membrane">SWGAFLGELVNFIIIAFA</span><span class="topo-outside">VFIIAKKVLQEEKVEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TKKVGIVDTTFARVDMASIAIKKLKELSPNIKIIRKTVPGIKDLPVACKKLLEEEGCDIVMALGMPGKAEKDKVCAHEASLGLMLAQLMTNKHIIEVFVHEDEAKDDKELDWLAKRRAEE</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-outside">HAENVYYLLFKPEYLTRMA</span><span class="topo-unknown">G</span><span class="topo-outside">KGLR</span><span class="topo-unknown">QGFEDAGPARE</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>43</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>24</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>47</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>67</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>259</td>
      <td>85</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>260</td>
      <td>240</td>
      <td>240</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>261</td>
      <td>264</td>
      <td>241</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMG</span><span class="topo-outside">LFSEFKEFLYEYKVIPLAIAF</span><span class="topo-membrane">IMGIASTALIKSFVDNIIMPIIT</span><span class="topo-inside">PFVPGGGWETATVELGPIVI</span><span class="topo-membrane">SWGAFLGELVNFIIIAFAV</span><span class="topo-outside">FIIAKKVLQEEKVEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TKKVGIVDTTFARVDMASIAIKKLKELSPNIKIIRKTVPGIKDLPVACKKLLEEEGCDIVMALGMPGKAEKDKVCAHEASLGLMLAQLMTNKHIIEVFVHEDEAKDDKELDWLAKRRAEE</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-outside">HAENVYYLLFKPEYLTRMAGKGLR</span><span class="topo-unknown">QGFEDAGPARE</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>43</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>24</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>47</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>105</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>264</td>
      <td>86</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y7k">4Y7K</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMG</span><span class="topo-outside">LFSEFKEFLYEYKVIPLAIAF</span><span class="topo-membrane">IMGIASTALIKSFVDNIIMPIIT</span><span class="topo-inside">PFVPGGGWETATVELGPIVI</span><span class="topo-membrane">SWGAFLGELVNFIIIAFAV</span><span class="topo-outside">FIIAKKVLQEEKVEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TKKVGIVDTTFARVDMASIAIKKLKELSPNIKIIRKTVPGIKDLPVACKKLLEEEGCDIVMALGMPGKAEKDKVCAHEASLGLMLAQLMTNKHIIEVFVHEDEAKDDKELDWLAKRRAEE</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-outside">HAENVYYLLFKPEYLTRMAGKGLR</span><span class="topo-unknown">QGFEDAGPARE</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>43</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>24</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>47</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>105</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>264</td>
      <td>86</td>
      <td>244</td>
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

### Helix-Pivoting Gating Mechanism

During the transition from closed to expanded state, TM1 and TM2 helices undergo large tilting movements (TM1: 37°→58°, TM2: 24°→42°), consistent with the helix-pivoting model. The transmembrane domain thins from 44Å to 30Å as the periplasmic surface expands from 50Å to 66Å width (ΔA ~1,457 Å²).

### N-Helix as Membrane-Anchored Stopper

The N-terminal helix undergoes significant rotation and horizontal sliding coupled to TM1/TM2 tilting. The N-helix serves as a membrane-anchored stopper that limits TM1/TM2 tilt during gating. The relationship follows: r(cosη₁ - cosη₂) = Δh = n(cosψ₁ - cosψ₂), where η and ψ are TM1 and N-helix tilt angles.

### Periplasmic Loop Reorganization

The periplasmic loop transforms from a folded structure containing an ω-shaped loop (residues Pro50-Ala57, motif PGGGWETA) and a short β-hairpin to an extended and partly disordered conformation. The ω-loop motif is involved in regulating the mechanosensitivity of [MSCL](/xray-mp-wiki/proteins/other-ion-channels/mscl/), with deletion of Gly51-Thr56 abolishing channel function.

### Mechanical Coupling of Channel Domains

The intersubunit coupling between the N-helix and TM1-TM2 pairs drives coordinated movement during channel expansion. The TM2 behaves like an umbrella stretcher and the N-helix like a rib that is pushed open. This provides a mechanism for force transmission across the pentameric channel.


## Cross-References

- <a href="/xray-mp-wiki/proteins/other-ion-channels/mscl/">Mechanosensitive Channel of Large Conductance MscL (Mycobacterium tuberculosis)</a> — MaMscL structure compared with closed-state MtMscL
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/sa-mscl/">Staphylococcus aureus MscL</a> — MaMscL expanded state compared with SaMscL-CΔ26 expanded intermediate
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/cofactors/riboflavin/">Riboflavin (Vitamin B2)</a> — Related ligand or cofactor
