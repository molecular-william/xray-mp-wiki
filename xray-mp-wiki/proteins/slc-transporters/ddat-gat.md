---
title: "dDAT_GAT (GAT1-Engineered Drosophila Dopamine Transporter)"
created: 2026-06-11
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography, transporter]
sources: [doi/10.15252##embj.2022110735]
verified: agent
uniprot_id: Q7K4Y6
---

# dDAT_GAT (GAT1-Engineered Drosophila Dopamine Transporter)


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q7K4Y6">UniProt: Q7K4Y6</a>

<span class="expr-badge">Drosophila melanogaster</span>

## Overview

dDAT_GAT is an engineered construct of the Drosophila melanogaster dopamine transporter (dDAT) in which 11 residues in the primary binding site were substituted to mimic the binding pocket of the human GABA transporter 1 (hGAT1, SLC6A1). The construct was built on a thermostabilized dDAT scaffold (ts2-L415A, V74A) and includes mutations F43Y, D46G, V120A, D121N, F325L, S422Q, G425T, S426V, Y124F (TM3), I113V (TM3), and E384S (EL4). Although dDAT_GAT lacks GABA transport activity, it binds GAT1-specific inhibitors including NO711 (KD ~10 µM) and SKF89976a (KD ~34 µM) as measured by microscale thermophoresis, enabling the first X-ray structures of GAT1 inhibitors bound to an NSS family member. The substrate-free structure (3.2 Å, PDB 7WGD) reveals an outward-open conformation with altered subsite architecture compared to wild-type dDAT.


## Publications

### doi/10.15252##embj.2022110735

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wgd">7WGD</a></td>
      <td>3.2</td>
      <td>not specified</td>
      <td>dDAT_GAT — ts2-L415A, V74A with 11 GAT1-like substitutions (F43Y, D46G, V120A, D121N, F325L, S422Q, G425T, S426V, Y124F, I113V, E384S)</td>
      <td>substrate-free (water molecules modeled in binding site)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wgd">7WGD</a></td>
      <td>not specified</td>
      <td>not specified</td>
      <td>dDAT_GAT — as above</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/no711">NO711</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wgd">7WGD</a></td>
      <td>not specified</td>
      <td>not specified</td>
      <td>dDAT_GAT — as above</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/skf89976a">SKF89976a</a> (primary site + allosteric site)</td>
    </tr>
  </tbody>
</table>

**Purification:**

- **Expression system**: HEK293S GnTI- cells
- **Expression construct**: dDAT_GAT with C-terminal [GFP](/xray-mp-wiki/reagents/protein-tags/gfp/)-His8 fusion
- **Tag info**: [GFP](/xray-mp-wiki/reagents/protein-tags/gfp/)-His8

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
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus</a>-mediated transduction (BacMam)</td>
      <td>—</td>
      <td></td>
      <td>HEK293S GnTI- cells transduced with P2 virus</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 4 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> in TBS (20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 100 mM NaCl)</td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td>Cobalt-charged metal affinity resin</td>
      <td>—</td>
      <td></td>
      <td>Batch binding with cobalt resin</td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>Thrombin digestion</td>
      <td>—</td>
      <td></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/gfp/">GFP</a>-His8 tag removed</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">[Superdex 200</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) Increase 10/300</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 300 mM NaCl, 4 mM decyl-β-D-maltoside, 0.2 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 0.001% POPE</td>
      <td></td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wgd">7WGD</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">DERETWSGKV</span><span class="topo-membrane">DFLLSVIGYAVGLANVWRFP</span><span class="topo-inside">YLCYKNGGG</span><span class="topo-membrane">AFLVPYGIMLAVGGIPLF</span><span class="topo-outside">YMELALGQHNRKGAITCWGRLVPLFKGIGYA</span><span class="topo-membrane">VVLISFYLNFYYNVIIAWSLR</span><span class="topo-inside">FFFASFTNSLP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WTSCNNIWNTPNCRPFEGHVEGFQSAASEYFNRYILELNRSEGIHDLGAIKW</span><span class="topo-membrane">DMALCLLIVYLICYFSLW</span><span class="topo-outside">KGIST</span><span class="topo-membrane">SGKVVWFTALFPYAALLI</span><span class="topo-inside">LLIRGLTLPGSFLGIQYYLTPNFSA</span><span class="topo-membrane">IY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">KAEVWADAATQVFFSLGPGLGSL</span><span class="topo-outside">LAYASYNKYHNNVYKDA</span><span class="topo-membrane">LLTSFINSATSFIAG</span><span class="topo-inside">FVIFSVLGYMAHTLGVRIEDVATSGPGLVFVVYPAAIATMPASTFWALI</span><span class="topo-membrane">FFMMLATLGLDSQFGT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VEAI</span><span class="topo-outside">ITALSDEFPKIKRNRELFV</span><span class="topo-membrane">AGLFSLYFVVGLASCT</span><span class="topo-inside">QGG</span><span class="topo-membrane">FYFFHLLDRYAAGYSILVAVF</span><span class="topo-outside">FEAIAVSWIYGTNRFSEDIRDMIGFPPGRYWQVCWRFV</span><span class="topo-membrane">APIFLLFITVYLLIGYEPL</span></span>
<span class="topo-ruler">       490       500       510       520       530      </span>
<span class="topo-line"><span class="topo-inside">TYADYVYP</span><span class="topo-membrane">SWANALGWCIAGSSVV</span><span class="topo-outside">MIPAVAIFKLLSTPGSLRQRFTILTTPWRDQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>30</td>
      <td>35</td>
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
      <td>109</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>172</td>
      <td>134</td>
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
      <td>213</td>
      <td>261</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>238</td>
      <td>279</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>263</td>
      <td>304</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>280</td>
      <td>329</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>295</td>
      <td>346</td>
      <td>360</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>344</td>
      <td>361</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>364</td>
      <td>410</td>
      <td>429</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>383</td>
      <td>430</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>399</td>
      <td>449</td>
      <td>464</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>400</td>
      <td>402</td>
      <td>465</td>
      <td>467</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>403</td>
      <td>423</td>
      <td>468</td>
      <td>488</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>461</td>
      <td>489</td>
      <td>526</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>462</td>
      <td>480</td>
      <td>527</td>
      <td>545</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>481</td>
      <td>488</td>
      <td>546</td>
      <td>553</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>504</td>
      <td>554</td>
      <td>569</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>505</td>
      <td>536</td>
      <td>570</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wgd">7WGD</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">DERETWSGKV</span><span class="topo-membrane">DFLLSVIGYAVGLANVWRFP</span><span class="topo-inside">YLCYKNGGG</span><span class="topo-membrane">AFLVPYGIMLAVGGIPLF</span><span class="topo-outside">YMELALGQHNRKGAITCWGRLVPLFKGIGYA</span><span class="topo-membrane">VVLISFYLNFYYNVIIAWSLR</span><span class="topo-inside">FFFASFTNSLP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WTSCNNIWNTPNCRPFEGHVEGFQSAASEYFNRYILELNRSEGIHDLGAIKW</span><span class="topo-membrane">DMALCLLIVYLICYFSLW</span><span class="topo-outside">KGIST</span><span class="topo-membrane">SGKVVWFTALFPYAALLI</span><span class="topo-inside">LLIRGLTLPGSFLGIQYYLTPNFSA</span><span class="topo-membrane">IY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">KAEVWADAATQVFFSLGPGLGSL</span><span class="topo-outside">LAYASYNKYHNNVYKDA</span><span class="topo-membrane">LLTSFINSATSFIAG</span><span class="topo-inside">FVIFSVLGYMAHTLGVRIEDVATSGPGLVFVVYPAAIATMPASTFWALI</span><span class="topo-membrane">FFMMLATLGLDSQFGT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VEAI</span><span class="topo-outside">ITALSDEFPKIKRNRELFV</span><span class="topo-membrane">AGLFSLYFVVGLASCT</span><span class="topo-inside">QGG</span><span class="topo-membrane">FYFFHLLDRYAAGYSILVAVF</span><span class="topo-outside">FEAIAVSWIYGTNRFSEDIRDMIGFPPGRYWQVCWRFV</span><span class="topo-membrane">APIFLLFITVYLLIGYEPL</span></span>
<span class="topo-ruler">       490       500       510       520       530      </span>
<span class="topo-line"><span class="topo-inside">TYADYVYP</span><span class="topo-membrane">SWANALGWCIAGSSVV</span><span class="topo-outside">MIPAVAIFKLLSTPGSLRQRFTILTTPWRDQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>30</td>
      <td>35</td>
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
      <td>109</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>172</td>
      <td>134</td>
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
      <td>213</td>
      <td>261</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>238</td>
      <td>279</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>263</td>
      <td>304</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>280</td>
      <td>329</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>295</td>
      <td>346</td>
      <td>360</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>344</td>
      <td>361</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>364</td>
      <td>410</td>
      <td>429</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>383</td>
      <td>430</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>399</td>
      <td>449</td>
      <td>464</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>400</td>
      <td>402</td>
      <td>465</td>
      <td>467</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>403</td>
      <td>423</td>
      <td>468</td>
      <td>488</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>461</td>
      <td>489</td>
      <td>526</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>462</td>
      <td>480</td>
      <td>527</td>
      <td>545</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>481</td>
      <td>488</td>
      <td>546</td>
      <td>553</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>504</td>
      <td>554</td>
      <td>569</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>505</td>
      <td>536</td>
      <td>570</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wgd">7WGD</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">DERETWSGKV</span><span class="topo-membrane">DFLLSVIGYAVGLANVWRFP</span><span class="topo-inside">YLCYKNGGG</span><span class="topo-membrane">AFLVPYGIMLAVGGIPLF</span><span class="topo-outside">YMELALGQHNRKGAITCWGRLVPLFKGIGYA</span><span class="topo-membrane">VVLISFYLNFYYNVIIAWSLR</span><span class="topo-inside">FFFASFTNSLP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WTSCNNIWNTPNCRPFEGHVEGFQSAASEYFNRYILELNRSEGIHDLGAIKW</span><span class="topo-membrane">DMALCLLIVYLICYFSLW</span><span class="topo-outside">KGIST</span><span class="topo-membrane">SGKVVWFTALFPYAALLI</span><span class="topo-inside">LLIRGLTLPGSFLGIQYYLTPNFSA</span><span class="topo-membrane">IY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">KAEVWADAATQVFFSLGPGLGSL</span><span class="topo-outside">LAYASYNKYHNNVYKDA</span><span class="topo-membrane">LLTSFINSATSFIAG</span><span class="topo-inside">FVIFSVLGYMAHTLGVRIEDVATSGPGLVFVVYPAAIATMPASTFWALI</span><span class="topo-membrane">FFMMLATLGLDSQFGT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VEAI</span><span class="topo-outside">ITALSDEFPKIKRNRELFV</span><span class="topo-membrane">AGLFSLYFVVGLASCT</span><span class="topo-inside">QGG</span><span class="topo-membrane">FYFFHLLDRYAAGYSILVAVF</span><span class="topo-outside">FEAIAVSWIYGTNRFSEDIRDMIGFPPGRYWQVCWRFV</span><span class="topo-membrane">APIFLLFITVYLLIGYEPL</span></span>
<span class="topo-ruler">       490       500       510       520       530      </span>
<span class="topo-line"><span class="topo-inside">TYADYVYP</span><span class="topo-membrane">SWANALGWCIAGSSVV</span><span class="topo-outside">MIPAVAIFKLLSTPGSLRQRFTILTTPWRDQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>30</td>
      <td>35</td>
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
      <td>109</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>172</td>
      <td>134</td>
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
      <td>213</td>
      <td>261</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>238</td>
      <td>279</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>263</td>
      <td>304</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>280</td>
      <td>329</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>295</td>
      <td>346</td>
      <td>360</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>344</td>
      <td>361</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>364</td>
      <td>410</td>
      <td>429</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>383</td>
      <td>430</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>399</td>
      <td>449</td>
      <td>464</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>400</td>
      <td>402</td>
      <td>465</td>
      <td>467</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>403</td>
      <td>423</td>
      <td>468</td>
      <td>488</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>461</td>
      <td>489</td>
      <td>526</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>462</td>
      <td>480</td>
      <td>527</td>
      <td>545</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>481</td>
      <td>488</td>
      <td>546</td>
      <td>553</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>504</td>
      <td>554</td>
      <td>569</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>505</td>
      <td>536</td>
      <td>570</td>
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

## Biological / Functional Insights

### Altered subsite architecture for GAT1 inhibitor recognition

The GAT1-like substitutions in subsites A and B reorganize the binding pocket. Subsite A loses the conserved Asp46 (substituted to Gly63-like) to accommodate the carboxylate group of GAT1 inhibitors, which coordinates Na+ at site 1. Subsite B is occluded by a hydrogen bond network (Asn121-Gln422, Gln422-Thr425, Asn121-Thr425, Asn121-Asn125) that minimizes the accessible cavity. A new subsite C' is created, replacing the conventional trilobed subsite architecture of biogenic amine transporters.

### TM6 linker as a selectivity determinant

The F325L substitution (Leu300 in GAT1) at the TM6 linker is critical for GAT1 inhibitor binding. In biogenic amine transporters the larger phenylalanine side chain restricts access, whereas the leucine in GATs allows accommodation of the diaryl groups of tiagabine analogs by widening the TM6 linker. Mutation of L300W in GAT1 nearly abolishes GABA transport, confirming the gatekeeper role of this residue.

### Allosteric binding site for SKF89976a

SKF89976a binds not only at the primary S1 site but also at an allosteric site in the extracellular vestibule, near EL4 (E384S substitution, Ser359 in GAT1). This dual binding mode provides a structural rationale for SKF89976a's ability to display both competitive and noncompetitive inhibition characteristics in GAT1. The allosteric site involves interactions with residues in TM10 and EL4, analogous to the (S)-citalopram secondary binding site in SERT.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/d-dopamine-transporter/">Drosophila Dopamine Transporter (dDAT)</a> — Parent construct; dDAT_GAT is derived from dDAT with 11 GAT1-like substitutions
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/nss-family/">Neurotransmitter/Sodium Symporter (NSS) Family</a> — dDAT_GAT is an engineered NSS family member
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/gaba-transporters-gats/">GABA Transporters (GATs)</a> — dDAT_GAT was engineered to mimic the GAT1 binding site
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/allosteric-site-in-nss-transporters/">Allosteric Site in NSS Transporters</a> — SKF89976a binds the allosteric site in the extracellular vestibule of dDAT_GAT
- <a href="/xray-mp-wiki/reagents/ligands/no711/">NO711</a> — GAT1 inhibitor co-crystallized with dDAT_GAT at primary binding site
- <a href="/xray-mp-wiki/reagents/ligands/skf89976a/">SKF89976a</a> — GAT1 inhibitor bound at both primary and allosteric sites
