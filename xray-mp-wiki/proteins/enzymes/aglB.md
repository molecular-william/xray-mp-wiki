---
title: "A. fulgidus AglB-L Oligosaccharyltransferase"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1309777110]
verified: regex
uniprot_id: O29867
---

# A. fulgidus AglB-L Oligosaccharyltransferase

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O29867">UniProt: O29867</a>

<span class="expr-badge">Archaeoglobus fulgidus</span>

## Overview

AglB-L (archaeal glycosylation B, Long form) from Archaeoglobus fulgidus is a single-subunit membrane oligosaccharyltransferase (OST) that transfers oligosaccharide chains to asparagine residues in proteins (N-linked glycosylation). The full-length crystal structures were determined at 2.5 A and 3.41 A resolutions in two crystal forms. The structures reveal 13 transmembrane helices with a characteristic long plastic loop (EL5) in the transmembrane region. The catalytic center consists of conserved acidic residues (Asp47, Glu360) coordinating a divalent metal ion (Zn2+ or Mg2+). AglB-L shares high structural similarity with the eubacterial PglB from Campylobacter lari, despite less than 20% sequence identity, indicating a conserved catalytic mechanism across archaeal, eubacterial, and eukaryotic (STT3) OSTs.


## Publications

### doi/10.1073##pnas.1309777110

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3waj">3WAJ</a></td>
      <td>2.50 A</td>
      <td>C2</td>
      <td>A. fulgidus AglB-L full-length; C-terminal His10-tag after thrombin cleavage site; crystal form 1 in n-octyl-beta-D-glucopyranoside (OG); Zn2+ and sulfate ion bound; EL5 loop disordered</td>
      <td>Zn2+ (catalytic site, six-coordinated, distorted octahedral), sulfate ion (mimics dolichol-phosphate phosphate group)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3waj">3WAJ</a></td>
      <td>3.41 A</td>
      <td>P4_3_2_1_2</td>
      <td>A. fulgidus AglB-L full-length; crystal form 2 in <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>; resting state with well-ordered EL5 plastic loop</td>
      <td>unknown metal ion; no sulfate ion bound</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C43 (DE3)
- **Construct**: A. fulgidus AglB-L (O29867_ARCFU) cloned into pET-52b(+) between NcoI and XhoI sites; C-terminal His10-tag after thrombin cleavage site; cultured in Terrific Broth with [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) (100 mg/L) at 310 K overnight

**Purification:**

- **Expression system**: E. coli C43 (DE3)
- **Expression construct**: C-terminal His10-tag
- **Tag info**: C-terminal His10-tag, removable by thrombin cleavage

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
      <td>Overnight expression</td>
      <td>not applicable</td>
      <td>Terrific Broth with 100 mg/L <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> + not applicable</td>
      <td>Overnight culture at 310 K</td>
    </tr>
    <tr>
      <td>Protein extraction and purification</td>
      <td>Detergent solubilization and <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity purification</a></td>
      <td>not specified</td>
      <td>not specified + not specified (monodisperse in various detergents by gel filtration)</td>
      <td>Monodisperse and monomeric in various detergents by gel filtration chromatography</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified in n-dodecyl-beta-D-maltopyranoside (DDM) for activity assays
**Yield**: Highest yield among three A. fulgidus AglB paralogs

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>A. fulgidus AglB-L in <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M zinc sulfate, 0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a> buffer pH 4.6, 15% (vol/vol) polyethylene glycol 4000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>0.2 M zinc sulfate, 0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a> pH 4.6, 15% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> 4000, 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>, 15% ethylene glycol</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal form 1; space group C2; contains 0.06% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> added; Zn2+ and sulfate bound; EL5 disordered</td>
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
      <td>A. fulgidus AglB-L in <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.02 M <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> HCl pH 8.0, 22% (wt/vol) polyethylene glycol 550MME</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>0.02 M <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> HCl pH 8.0, 28% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> 550MME, 0.06% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal form 2; space group P4_3_2_1_2; resting state with well-ordered EL5 plastic loop; no sulfate bound</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3waj">3WAJ</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQNAESWFKKYWHL</span><span class="topo-outside">S</span><span class="topo-membrane">VLVIAALISV</span><span class="topo-inside">KLRILNPWNSVFTWTVRLGGNDPWYYYRLIENTIHNFPHRIWFDPFTYYPYGSYTHFG</span><span class="topo-unknown">PFLVYLGSIAGII</span><span class="topo-inside">FSATSGESLRAVLAFIPAI</span><span class="topo-membrane">GGVLA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ILPVYLLTREVFDK</span><span class="topo-outside">R</span><span class="topo-membrane">AAVIAAFLIAIV</span><span class="topo-inside">PGQFLQRSILGFNDHHI</span><span class="topo-membrane">WEAFWQVSALGTFLLAYNRW</span><span class="topo-outside">KGHD</span><span class="topo-unknown">LSHN</span><span class="topo-outside">LT</span><span class="topo-membrane">ARQMAYPVIAGITIGLYVLS</span><span class="topo-inside">WGA</span><span class="topo-membrane">GFIIAPIILAFMFFAFVL</span><span class="topo-outside">AGFVN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ADRKN</span><span class="topo-membrane">LSLVAVVTFAVSALIYLP</span><span class="topo-inside">FAFNYPGFSTIFYSP</span><span class="topo-membrane">FQLLVLLGSAVIAAAFYQI</span><span class="topo-outside">EKWNDVGFFERVGLGRKGMP</span><span class="topo-membrane">LAVIVLTALIMGLFFV</span><span class="topo-unknown">ISPDFARNLLSVVRVVQPKGGALTIAE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">VYPFFFTHNGEFT</span><span class="topo-inside">LT</span><span class="topo-unknown">NAVLHF</span><span class="topo-membrane">GALFFFGMAGILYSAYRFL</span><span class="topo-outside">KRRS</span><span class="topo-membrane">FPEMALLIWAIAMFIALW</span><span class="topo-inside">GQNRFAY</span><span class="topo-membrane">YFAAVSAVYSALALSVVFDKLH</span><span class="topo-unknown">LYRALENAIGARNKLSY</span><span class="topo-outside">F</span><span class="topo-membrane">RVAFALLIALA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">AIYPTY</span><span class="topo-inside">ILADAQSSYAGGPNKQWYDALTWMRENTPDGEKYDEYYLQLYPTPQSNKEPFSYPFETYGVISWWDYGHWIEAVAHRMPIANPFQAGIGNKYNNVPGASSFFTAENESYAEFVA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">EKLNVKYVVSDIEMETGKYYAMAVWAEGDLPLAEKYYGGYFYYSPTGTFGYANSQWDIPLNSIIIPLRIPSELYYSTMEAKLHLFDGSGLSHYRMIYESDYPAEWKSYSSQVNLNNESQV</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">LQTALYEAVMRARYGVSPTMGTQEVLYKYAYTQLYEKKMGIPVKIAPSGYVKIFERVKGAVVTGKVSANVTEVSVNATIKTNQNRTFEYWQTVEVKNGTYTVVLPYSHNSDYPVKPITPY</span></span>
<span class="topo-ruler">       850       860       870     </span>
<span class="topo-line"><span class="topo-inside">HIKAGNVVKEITIYESQVQNGEIIQLDL</span><span class="topo-unknown">ELALVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (36 regions)</summary>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>25</td>
      <td>16</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>83</td>
      <td>26</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>96</td>
      <td>84</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>115</td>
      <td>97</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>134</td>
      <td>116</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>135</td>
      <td>135</td>
      <td>135</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>147</td>
      <td>136</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>164</td>
      <td>148</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>184</td>
      <td>165</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>188</td>
      <td>185</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>192</td>
      <td>189</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>193</td>
      <td>194</td>
      <td>193</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>214</td>
      <td>195</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>217</td>
      <td>215</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>235</td>
      <td>218</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>245</td>
      <td>236</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>263</td>
      <td>246</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>278</td>
      <td>264</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>297</td>
      <td>279</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>317</td>
      <td>298</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>333</td>
      <td>318</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>373</td>
      <td>334</td>
      <td>373</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>374</td>
      <td>375</td>
      <td>374</td>
      <td>375</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>376</td>
      <td>381</td>
      <td>376</td>
      <td>381</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>382</td>
      <td>400</td>
      <td>382</td>
      <td>400</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>401</td>
      <td>404</td>
      <td>401</td>
      <td>404</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>405</td>
      <td>422</td>
      <td>405</td>
      <td>422</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>429</td>
      <td>423</td>
      <td>429</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>451</td>
      <td>430</td>
      <td>451</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>452</td>
      <td>468</td>
      <td>452</td>
      <td>468</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>469</td>
      <td>469</td>
      <td>469</td>
      <td>469</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>486</td>
      <td>470</td>
      <td>486</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>487</td>
      <td>868</td>
      <td>487</td>
      <td>868</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>869</td>
      <td>875</td>
      <td>869</td>
      <td>875</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3waj">3WAJ</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQNAESWFKKYWHL</span><span class="topo-outside">S</span><span class="topo-membrane">VLVIAALISV</span><span class="topo-inside">KLRILNPWNSVFTWTVRLGGNDPWYYYRLIENTIHNFPHRIWFDPFTYYPYGSYTHFG</span><span class="topo-unknown">PFLVYLGSIAGII</span><span class="topo-inside">FSATSGESLRAVLAFIPAI</span><span class="topo-membrane">GGVLA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ILPVYLLTREVFDK</span><span class="topo-outside">R</span><span class="topo-membrane">AAVIAAFLIAIV</span><span class="topo-inside">PGQFLQRSILGFNDHHI</span><span class="topo-membrane">WEAFWQVSALGTFLLAYNRW</span><span class="topo-outside">KGHD</span><span class="topo-unknown">LSHN</span><span class="topo-outside">LT</span><span class="topo-membrane">ARQMAYPVIAGITIGLYVLS</span><span class="topo-inside">WGA</span><span class="topo-membrane">GFIIAPIILAFMFFAFVL</span><span class="topo-outside">AGFVN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ADRKN</span><span class="topo-membrane">LSLVAVVTFAVSALIYLP</span><span class="topo-inside">FAFNYPGFSTIFYSP</span><span class="topo-membrane">FQLLVLLGSAVIAAAFYQI</span><span class="topo-outside">EKWNDVGFFERVGLGRKGMP</span><span class="topo-membrane">LAVIVLTALIMGLFFV</span><span class="topo-unknown">ISPDFARNLLSVVRVVQPKGGALTIAE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">VYPFFFTHNGEFT</span><span class="topo-inside">LT</span><span class="topo-unknown">NAVLHF</span><span class="topo-membrane">GALFFFGMAGILYSAYRFL</span><span class="topo-outside">KRRS</span><span class="topo-membrane">FPEMALLIWAIAMFIALW</span><span class="topo-inside">GQNRFAY</span><span class="topo-membrane">YFAAVSAVYSALALSVVFDKLH</span><span class="topo-unknown">LYRALENAIGARNKLSY</span><span class="topo-outside">F</span><span class="topo-membrane">RVAFALLIALA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">AIYPTY</span><span class="topo-inside">ILADAQSSYAGGPNKQWYDALTWMRENTPDGEKYDEYYLQLYPTPQSNKEPFSYPFETYGVISWWDYGHWIEAVAHRMPIANPFQAGIGNKYNNVPGASSFFTAENESYAEFVA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">EKLNVKYVVSDIEMETGKYYAMAVWAEGDLPLAEKYYGGYFYYSPTGTFGYANSQWDIPLNSIIIPLRIPSELYYSTMEAKLHLFDGSGLSHYRMIYESDYPAEWKSYSSQVNLNNESQV</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">LQTALYEAVMRARYGVSPTMGTQEVLYKYAYTQLYEKKMGIPVKIAPSGYVKIFERVKGAVVTGKVSANVTEVSVNATIKTNQNRTFEYWQTVEVKNGTYTVVLPYSHNSDYPVKPITPY</span></span>
<span class="topo-ruler">       850       860       870     </span>
<span class="topo-line"><span class="topo-inside">HIKAGNVVKEITIYESQVQNGEIIQLDL</span><span class="topo-unknown">ELALVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (36 regions)</summary>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>25</td>
      <td>16</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>83</td>
      <td>26</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>96</td>
      <td>84</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>115</td>
      <td>97</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>134</td>
      <td>116</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>135</td>
      <td>135</td>
      <td>135</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>147</td>
      <td>136</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>164</td>
      <td>148</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>184</td>
      <td>165</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>188</td>
      <td>185</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>192</td>
      <td>189</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>193</td>
      <td>194</td>
      <td>193</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>214</td>
      <td>195</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>217</td>
      <td>215</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>235</td>
      <td>218</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>245</td>
      <td>236</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>263</td>
      <td>246</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>278</td>
      <td>264</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>297</td>
      <td>279</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>317</td>
      <td>298</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>333</td>
      <td>318</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>373</td>
      <td>334</td>
      <td>373</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>374</td>
      <td>375</td>
      <td>374</td>
      <td>375</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>376</td>
      <td>381</td>
      <td>376</td>
      <td>381</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>382</td>
      <td>400</td>
      <td>382</td>
      <td>400</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>401</td>
      <td>404</td>
      <td>401</td>
      <td>404</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>405</td>
      <td>422</td>
      <td>405</td>
      <td>422</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>429</td>
      <td>423</td>
      <td>429</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>451</td>
      <td>430</td>
      <td>451</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>452</td>
      <td>468</td>
      <td>452</td>
      <td>468</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>469</td>
      <td>469</td>
      <td>469</td>
      <td>469</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>486</td>
      <td>470</td>
      <td>486</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>487</td>
      <td>868</td>
      <td>487</td>
      <td>868</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>869</td>
      <td>875</td>
      <td>869</td>
      <td>875</td>
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

### Conserved 13-TM architecture across archaeal and eubacterial OSTs

The A. fulgidus AglB-L structure reveals 13 transmembrane helices with a topology nearly identical to C. lari PglB, despite <20% sequence identity. The TM domain comprises ca. 400-500 residues, and the characteristic long EL1 (extracellular loop 1) and EL5 loops are conserved. This striking similarity indicates that eukaryotic STT3 catalytic subunits share the same 13-TM + CC (central core) architecture.

### Plastic EL5 loop dynamics in catalytic cycle

The EL5 loop is completely disordered in crystal form 1 (sulfate-bound, representing the lipid-phosphate bound state) but well-ordered in crystal form 2 (resting state). This conformational flexibility suggests that EL5 becomes unstructured upon ligand binding, disrupting the porthole structure to facilitate release of the glycosylated product. The conserved Glu360 in the TIXE motif on EL5 serves as a coordination switch responding to ligand binding.

### Metal coordination by conserved DXD/DXH motifs

The catalytic site contains a divalent metal ion (Zn2+ in crystal form 1, substituting for the natural cofactor Mg2+) coordinated by Asp47 (first DXD motif on EL1), Asp161 and His163 (second DXH motif on EL2), and three water molecules in a distorted octahedral geometry. Glu360 on the EL5 loop completes the carboxylate dyad. Mutagenesis confirms Asp47 and Glu360 are critical for activity; charge-preserving mutations (Asp47Glu, Glu360Asp) retain partial activity.

### Ser/Thr-binding pocket in sequon recognition

The C-terminal globular domain contains a Ser/Thr-binding pocket formed by the WWD motif (part of the WWDYG motif) and a second signature residue (Lys or Ile) of the DK/MI motif. In crystal form 2, the pocket adopts a Lys-type conformation with W550, W551, D552, and K618 forming the binding site (compared to W463, W464, D465, I572 in C. lari PglB). The Lys-type pocket is proposed to be more dynamic on millisecond timescales, enabling efficient scanning of nascent polypeptide chains during co-translational glycosylation in eukaryotes.

### Sulfate ion mimics dolichol-phosphate binding

In crystal form 1, a sulfate ion is bound 5.0 A from the Zn2+ ion, interacting with His81, His162, Trp215, and Arg426. Mutagenesis of these residues (particularly His81Ala, His162Ala, Arg426Ala) severely impairs activity. The sulfate is proposed to mimic the phosphate group of the dolichol-phosphate carrier. A docking model shows the isoprene units of dolichol phosphate fitting within a hydrophobic groove on the protein surface.


## Cross-References

- <a href="/xray-mp-wiki/concepts/membrane-mimetics/n-glycosylation-sequon/">N-Glycosylation Sequon</a> — AglB-L recognizes the N-glycosylation sequon (Asn-X-Ser/Thr) via the Ser/Thr-binding pocket in its C-terminal domain
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/ost-catalytic-cycle/">Catalytic Cycle of Oligosaccharyltransferase</a> — The AglB-L crystal structures in two forms provide structural snapshots of different states in the OST catalytic cycle
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for AglB-L purification and activity assays
- <a href="/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/">n-Octyl-beta-D-glucopyranoside (OG)</a> — Detergent used in crystal form 1 crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO (Lauryldimethylamine-N-oxide)</a> — Detergent used in crystal form 2 crystallization
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/n-glycosylation-sequon/">N-Glycosylation Sequon</a> — Key concept related to this protein
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/ost-catalytic-cycle/">Catalytic Cycle of Oligosaccharyltransferase</a> — Key concept related to this protein
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)</a> — Related protein mentioned in the study
