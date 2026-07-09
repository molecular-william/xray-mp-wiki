---
title: "Drosophila melanogaster Dopamine Transporter"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3029, doi/10.1038##s41467-021-22385-9]
verified: regex
uniprot_id: ['P0A334', 'Q7K4Y6']
---

# Drosophila melanogaster Dopamine Transporter

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0A334">UniProt: P0A334</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q7K4Y6">UniProt: Q7K4Y6</a>

<span class="expr-badge">Streptomyces lividans</span>

## Overview

The Drosophila melanogaster [DOPAMINE](/xray-mp-wiki/reagents/ligands/dopamine) transporter (dDAT) is a Na+/Cl--coupled biogenic amine transporter that clears [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine), norepinephrine, and tyramine from synaptic spaces. dDAT is widely used as a model system for mammalian biogenic amine transporters because it lacks a dedicated norepinephrine transporter (NET) in Drosophila, making dDAT the primary catecholamine reuptake mechanism. Despite preferring [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine) over norepinephrine, dDAT exhibits pharmacological properties closest to mammalian NETs, making it an excellent model for structure-based studies of NET-specific antidepressant inhibitors.

## Publications

### doi/10.1038##nsmb.3029

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4xnu">4XNU</a></td>
      <td>3.0</td>
      <td></td>
      <td>dDAT_cryst</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/nisoxetine">NISOXETINE</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4xnx">4XNX</a></td>
      <td>3.0</td>
      <td></td>
      <td>dDAT_mfc</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/reboxetine">REBOXETINE</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK-293S GnTI- cells (baculovirus-mediated transduction)
- **Construct**: C-terminal GFP-His8 fusion; thermostabilized variants with EL2 [TRUNCATION](/xray-mp-wiki/concepts/methods-techniques/truncation) and thrombin cleavage site

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
      <td>1</td>
      <td>membrane solubilization</td>
      <td></td>
      <td>1x TBS (20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 150 mM NaCl) + 20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Membranes homogenized in TBS and solubilized with 20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>2</td>
      <td>cobalt-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>cobalt-charged metal-affinity resin</td>
      <td>1x TBS with 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 0.2 mM CHS, 100 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">IMIDAZOLE</a>, pH 8.0 + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>GFP-His8 tag captured on cobalt resin and eluted with <a href="/xray-mp-wiki/reagents/additives/imidazole">IMIDAZOLE</a></td>
    </tr>
    <tr>
      <td>3</td>
      <td>thrombin cleavage</td>
      <td></td>
      <td>1x TBS with 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 0.2 mM CHS + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>GFP-His8 tag removed by overnight thrombin digestion at 4 C</td>
    </tr>
    <tr>
      <td>4</td>
      <td>size-exclusion chromatography</td>
      <td>Superdex 200 10/300 column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 300 mM NaCl, 4 mM decyl-beta-D-maltoside, 0.2 mM CHS, 0.001% <a href="/xray-mp-wiki/reagents/lipids/pope">POPE</a> + 4 mM decyl-beta-D-maltoside</td>
      <td>Peak fractions pooled; all procedures at 4 C</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Fab-DAT complex at 3-4 mg/ml with 1 mM <a href="/xray-mp-wiki/reagents/ligands/nisoxetine">Nisoxetine</a> or (R,R)-<a href="/xray-mp-wiki/reagents/ligands/reboxetine">REBOXETINE</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/glycine">GLYCINE</a> pH 9, 38% <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> 350 monomethyl ether</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of dDAT_mfc obtained by streak seeding 7 d after drop setup</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4xnu">4XNU</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">DERETWSGKVDFL</span><span class="topo-membrane">LSVIGFAVDLANVWRFP</span><span class="topo-inside">YLCYKNGGG</span><span class="topo-membrane">AFLVPYGIMLAVGGIPLF</span><span class="topo-outside">YMELALGQHNRKGAITCWGRLVPLFKGIGYA</span><span class="topo-membrane">VVLIAFYVDFYYNVIIAWSL</span><span class="topo-inside">RFFFASFTNSLP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WTSCNNIWNTPNCRPFESQGFQSAASEYFNRYILELNRSEGIHDLGAIKWDM</span><span class="topo-membrane">ALCLLIVYLICYFSLW</span><span class="topo-outside">KGIST</span><span class="topo-membrane">SGKVVWFTALFPYAALLI</span><span class="topo-inside">LLIRGLTLPGSFLGIQYYLTPNF</span><span class="topo-membrane">SAIYKA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EVWADAATQVFFSLGPGFGVL</span><span class="topo-outside">LAYASYNKYHNNVYKDA</span><span class="topo-membrane">LLTSFINSATSFIAGF</span><span class="topo-inside">VIFSVLGYMAHTLGVRIEDVATEGPGLVFVVYPAAIATMPASTFWALI</span><span class="topo-membrane">FFMMLATLGLDSSFGGSE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">AI</span><span class="topo-outside">ITALSDEFPKIKRNRELF</span><span class="topo-membrane">VAGLFSLYFVVGLASC</span><span class="topo-inside">TQGGFYF</span><span class="topo-membrane">FHLLDRYAAGYSILVAVF</span><span class="topo-outside">FEAIAVSWIYGTNRFSEDIRDMIGFPPG</span><span class="topo-unknown">RYWQVCWR</span><span class="topo-outside">FV</span><span class="topo-membrane">APIFLLFITVYLLIGYEPL</span><span class="topo-inside">TY</span></span>
<span class="topo-ruler">       490       500       510       520       530  </span>
<span class="topo-line"><span class="topo-inside">ADYVYPS</span><span class="topo-membrane">WANALGWCIAGSSVVM</span><span class="topo-outside">IPAVAIFKLLSTPGSLRQRFTILTTPWRD</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>13</td>
      <td>25</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>30</td>
      <td>38</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>39</td>
      <td>55</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>57</td>
      <td>64</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>88</td>
      <td>82</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>108</td>
      <td>113</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>172</td>
      <td>133</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>188</td>
      <td>240</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>193</td>
      <td>256</td>
      <td>260</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>211</td>
      <td>261</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>234</td>
      <td>279</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>261</td>
      <td>302</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>329</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>294</td>
      <td>346</td>
      <td>361</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>342</td>
      <td>362</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>362</td>
      <td>410</td>
      <td>429</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>380</td>
      <td>430</td>
      <td>447</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>396</td>
      <td>448</td>
      <td>463</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>403</td>
      <td>464</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>421</td>
      <td>471</td>
      <td>488</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>449</td>
      <td>489</td>
      <td>516</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>457</td>
      <td>517</td>
      <td>524</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>458</td>
      <td>459</td>
      <td>525</td>
      <td>526</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>460</td>
      <td>478</td>
      <td>527</td>
      <td>545</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>479</td>
      <td>487</td>
      <td>546</td>
      <td>554</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>488</td>
      <td>503</td>
      <td>555</td>
      <td>570</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>504</td>
      <td>532</td>
      <td>571</td>
      <td>599</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4xnx">4XNX</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">DERETWSGKV</span><span class="topo-membrane">DFLLSVIGFAVDLANVWRFPYLC</span><span class="topo-inside">YKNGG</span><span class="topo-membrane">GAFLVPYGIMLAVGGIPLFYMEL</span><span class="topo-outside">ALGQHNRKGAITCWGRLVPLFKG</span><span class="topo-membrane">IGYAVVLIAFYVDFYYNVIIAWSLRFFF</span><span class="topo-inside">ASFTNSLP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WTSCNNIWNTPNCRPFEGHVEGFQSAASEYFNRYILELNRSEGIHDLGAIKW</span><span class="topo-membrane">DMALCLLIVYLICYFSLW</span><span class="topo-outside">KGIST</span><span class="topo-membrane">SGKVVWFTALFPYAVLLILLIRGL</span><span class="topo-inside">TLPGSFLGIQYYLTPNFSAI</span><span class="topo-membrane">Y</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">KAEVWVDAATQVFFSLGPGFGVLLAY</span><span class="topo-outside">ASYNKYHNNVYKD</span><span class="topo-membrane">ALLTSFINSATSFIAGFVI</span><span class="topo-inside">FSVLGYMAHTLGVRIEDVATEGPGLVFVVYPAAIATMPASTF</span><span class="topo-membrane">WALIFFMMLATLGLDSSFGG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">SEAIITAL</span><span class="topo-outside">SDEFPKIKRNRE</span><span class="topo-membrane">LFVAGLFSLYFVVGLASC</span><span class="topo-inside">TQGGFYF</span><span class="topo-membrane">FHLLDRYAAGYSILVAVFFEAIA</span><span class="topo-outside">VSWIYGTNRFSEDIRDMIGFPPGRYWQV</span><span class="topo-membrane">CWRFVAPIFLLFITVYGLIGY</span><span class="topo-inside">EPL</span></span>
<span class="topo-ruler">       490       500       510       520       530      </span>
<span class="topo-line"><span class="topo-inside">TYADYVYPSWA</span><span class="topo-membrane">NALGWCIAGSSVVMIPAVAIF</span><span class="topo-outside">KLLSTPGSLRQRFTILTTPWRDQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>25</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>33</td>
      <td>35</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>38</td>
      <td>58</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>61</td>
      <td>63</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>86</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>112</td>
      <td>109</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>137</td>
      <td>137</td>
      <td>161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>172</td>
      <td>203</td>
      <td>237</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>190</td>
      <td>238</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>195</td>
      <td>256</td>
      <td>260</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>219</td>
      <td>261</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>239</td>
      <td>285</td>
      <td>304</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>266</td>
      <td>305</td>
      <td>331</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>279</td>
      <td>332</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>298</td>
      <td>345</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>340</td>
      <td>364</td>
      <td>405</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>368</td>
      <td>406</td>
      <td>433</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>380</td>
      <td>434</td>
      <td>445</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>398</td>
      <td>446</td>
      <td>463</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>399</td>
      <td>405</td>
      <td>464</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>428</td>
      <td>471</td>
      <td>493</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>429</td>
      <td>456</td>
      <td>494</td>
      <td>521</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>457</td>
      <td>477</td>
      <td>522</td>
      <td>542</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>478</td>
      <td>491</td>
      <td>543</td>
      <td>556</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>492</td>
      <td>512</td>
      <td>557</td>
      <td>577</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>513</td>
      <td>536</td>
      <td>578</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41467-021-22385-9

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m2e">7M2E</a></td>
      <td>3.3</td>
      <td></td>
      <td>dDAT_subB (hNET-like mutations D121G/S426M in subsite B), substrate-free</td>
      <td>None (Na+ and Cl- bound at respective sites)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m2f">7M2F</a></td>
      <td>2.8</td>
      <td></td>
      <td>dDAT_mfc with norepinephrine bound</td>
      <td>Norepinephrine</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m2g">7M2G</a></td>
      <td>3.3</td>
      <td></td>
      <td>dDAT_subB (hNET-like mutations D121G/S426M) with <a href="/xray-mp-wiki/reagents/ligands/duloxetine">DULOXETINE</a> bound</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/duloxetine">DULOXETINE</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m2h">7M2H</a></td>
      <td>3.0</td>
      <td></td>
      <td>dDAT_NET with milnacipran bound</td>
      <td>Milnacipran</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m2i">7M2I</a></td>
      <td>2.8</td>
      <td></td>
      <td>dDAT_NET with tramadol bound</td>
      <td>Tramadol</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK-293S GnTI- cells (baculovirus-mediated transduction)
- **Construct**: C-terminal GFP-His8 fusion; thermostabilized variants with EL2 [TRUNCATION](/xray-mp-wiki/concepts/methods-techniques/truncation) and thrombin cleavage site

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2h">7M2H</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGHF</span></span>
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
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>125</td>
      <td>112</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2h">7M2H</a> — Chain I (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGHF</span></span>
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
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>125</td>
      <td>112</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2h">7M2H</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGHF</span></span>
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
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>125</td>
      <td>112</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2h">7M2H</a> — Chain O (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGHF</span></span>
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
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>125</td>
      <td>112</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2i">7M2I</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WR</span><span class="topo-membrane">CAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWFV</span><span class="topo-outside">GQCQQQ</span></span>
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
      <td>1</td>
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>25</td>
      <td>28</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>90</td>
      <td>87</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>96</td>
      <td>116</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2i">7M2I</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WR</span><span class="topo-membrane">CAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWFV</span><span class="topo-outside">GQCQQQ</span></span>
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
      <td>1</td>
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>25</td>
      <td>28</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>90</td>
      <td>87</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>96</td>
      <td>116</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2i">7M2I</a> — Chain I (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WR</span><span class="topo-membrane">CAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWFV</span><span class="topo-outside">GQCQQQ</span></span>
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
      <td>1</td>
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>25</td>
      <td>28</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>90</td>
      <td>87</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>96</td>
      <td>116</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2i">7M2I</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WR</span><span class="topo-membrane">CAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWFV</span><span class="topo-outside">GQCQQQ</span></span>
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
      <td>1</td>
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>25</td>
      <td>28</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>90</td>
      <td>87</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>96</td>
      <td>116</td>
      <td>121</td>
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

### Norepinephrine binds in a different pose than dopamine

Norepinephrine binds in subsite C of the primary binding site, oriented more towards subsite C relative to [DOPAMINE](/xray-mp-wiki/reagents/ligands/dopamine) which binds closer to subsite B. The beta-OH group in NE restricts catechol rotation with an energy barrier of 9-12 kcal/mol, compared to 0.3-0.6 kcal/mol for DA. This difference translates to DAT and NET having greater propensity to interact with DA compared to NE, consistent with higher Ki values for NE competition (19 uM vs 2.0 uM for DA).

### Subsite C determines NET-specific inhibitor selectivity

SNRIs [DULOXETINE](/xray-mp-wiki/reagents/ligands/duloxetine), milnacipran, and tramadol all interact with subsite C through aromatic groups. hDAT-like mutations in subsite C (A117S, A428S) in dDAT cause maximal loss of affinity for these inhibitors, demonstrating that subsite C residues are key determinants of NET specificity. Non-specific inhibitors like [Cocaine](/xray-mp-wiki/reagents/ligands/cocaine) primarily interact with subsite B, while NET-specific inhibitors engage subsite C.

### Tramadol binds primarily at subsite C

Tramadol's methoxyphenyl ring interacts with Y124 by aromatic edge-to-face interactions and fits into the hydrophobic pocket lined by A117, V120, A428, and F325 of subsite C. Unlike [COCAINE](/xray-mp-wiki/reagents/ligands/cocaine) which wedges its benzoyl group into subsite B, tramadol's lack of interaction at subsite B compromises affinity but retains NET specificity over DAT.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-Beta-D-Maltoside (DDM)</a> — Primary solubilization detergent used throughout purification
- <a href="/xray-mp-wiki/reagents/additives/peg/">Polyethylene Glycol (PEG)</a> — PEG 350 monomethyl ether used as crystallization precipitant
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 SEC Resin</a> — Size-exclusion chromatography resin used for final purification
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine Buffer</a> — Crystallization reservoir buffer (0.1 M, pH 9)
- <a href="/xray-mp-wiki/reagents/ligands/nisoxetine/">Nisoxetine</a> — NET-specific inhibitor co-crystallized with dDAT_cryst (PDB 4XNU)
- <a href="/xray-mp-wiki/reagents/ligands/reboxetine/">Reboxetine</a> — NET-specific inhibitor co-crystallized with dDAT_mfc (PDB 4XNX)
- <a href="/xray-mp-wiki/reagents/antibodies/fab-9d5/">Fab 9D5</a> — Antibody fragment used to complex with dDAT for crystallization
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Crystallization method used to grow dDAT-Fab complexes
- <a href="/xray-mp-wiki/reagents/ligands/duloxetine/">Duloxetine</a> — SNRI inhibitor co-crystallized with dDAT_subB (PDB 7M2G)
- <a href="/xray-mp-wiki/reagents/additives/milnacipran/">Milnacipran</a> — SNRI inhibitor co-crystallized with dDAT_NET (PDB 7M2H)
- <a href="/xray-mp-wiki/reagents/additives/tramadol/">Tramadol</a> — Synthetic opioid co-crystallized with dDAT_NET (PDB 7M2I)
- <a href="/xray-mp-wiki/reagents/buffers/mops/">MOPS Buffer</a> — Buffer (0.1 M, pH 6.5-7.0) used in crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/peg-600/">Polyethylene glycol 600 (PEG 600)</a> — Precipitant (30-32%) used in crystallization reservoir
