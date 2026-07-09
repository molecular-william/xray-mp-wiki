---
title: "KdpFABC Potassium-Importing Complex"
created: 2017-06-21
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature22970]
verified: regex
uniprot_id: ['P03959', 'P03960', 'P03961', 'P36937']
---

# KdpFABC Potassium-Importing Complex


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P03959">UniProt: P03959</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P03960">UniProt: P03960</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P03961">UniProt: P03961</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P36937">UniProt: P36937</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

The KdpFABC complex is a four-subunit potassium pump from Escherichia coli that maintains intracellular K+ homeostasis under conditions in which potassium is limiting. The complex consists of a channel-like subunit (KdpA) belonging to the superfamily of potassium transporters (SKT) and a pump-like subunit (KdpB) belonging to the superfamily of P-type ATPases, together with two auxiliary subunits KdpC and KdpF, each having a single transmembrane helix. The 2.9 A X-ray crystal structure (Huang et al., 2017, PDB 5MRW) of the complete complex revealed a potassium ion within the selectivity filter of KdpA and a water molecule at a canonical cation site in the transmembrane domain of KdpB. The structure identified two structural elements mediating coupling between these subunits: a protein-embedded tunnel running between the K+ and water sites, and a helix controlling the cytoplasmic gate of KdpA linked to the phosphorylation domain of KdpB. A mechanism was proposed that repurposes protein channel architecture for active transport by using charge transfer through the intramembrane tunnel to trigger ATP hydrolysis and gating.


## Publications

### doi/10.1038##nature22970

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5mrw">5MRW</a></td>
      <td>2.9 A</td>
      <td>I222</td>
      <td>Full-length E. coli KdpFABC complex (KdpA Q116R mutant), with 8xHis tag on KdpC C-terminus; selenomethionine-substituted</td>
      <td>K+ ion in S3 site of KdpA selectivity filter</td>
    </tr>
  </tbody>
</table>

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
      <td>Membrane preparation</td>
      <td>Ultracentrifugation (90,140g, 2 h)</td>
      <td>—</td>
      <td>50 mM Tris pH 7.5, 1.2 M NaCl, 10 mM MgCl2, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a></td>
      <td>Cells lysed by Emulsiflex C3 homogenizer</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM Tris pH 7.5, 600 mM NaCl, 10 mM MgCl2, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> + 1.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-maltoside</a> (DM)</td>
      <td>Incubated at 4C for at least 2 h</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Gradient elution (20-500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>)</td>
      <td>Ni2+-charged HiTrap chelating column (GE Healthcare)</td>
      <td>50 mM Tris pH 7.5, 600 mM NaCl, 10 mM MgCl2, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.15% DM, 20-500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL</td>
      <td>50 mM Tris pH 7.5, 600 mM NaCl, 10 mM MgCl2, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.15% DM</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, sitting drop</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> (pH 5.0), 50 mM NaCl, 20 mM CaCl2, 30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 550 MME</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Plate-like morphology with birefringence; crystals appeared within 1-2 weeks</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5mrw">5MRW</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MAA</span><span class="topo-membrane">QGFLLIATFLLVLMVLA</span><span class="topo-inside">RPLGSGLARLINDIPLPGTTGVERVLFRALGVSDREMNWKQYLCAILGL</span><span class="topo-membrane">NMLGLAVLFFMLLGQ</span><span class="topo-outside">HYLPLNPQQLPGLSWDLA</span><span class="topo-unknown">LNTAVSFVTNTNW</span><span class="topo-outside">RSYSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ETTLSY</span><span class="topo-membrane">FSQMAGLTVQNFLSAASG</span><span class="topo-inside">IAVIFALIRAFTRQSMSTLGNAWVDLLRITLWV</span><span class="topo-membrane">LVPVALLIALFFIQ</span><span class="topo-outside">QGALQNFLPYQAVNTVEGAQQLLPMGP</span><span class="topo-unknown">VASQEAIKMLGTNGGG</span><span class="topo-outside">FFNANS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SHPFENPTAL</span><span class="topo-membrane">TNFVQMLAIFLIPTA</span><span class="topo-inside">LCFAFGEVMGDRRQGRMLL</span><span class="topo-membrane">WAMSVIFVICVGVV</span><span class="topo-outside">MWAEVQGNPHLLALGTDSSINMEGKESRFGVLVSSL</span><span class="topo-unknown">FAVVTTAASCGA</span><span class="topo-outside">VIAMHDSFTALGGM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VPMWLMQIGEVVFGGVGSGL</span><span class="topo-inside">YGMMLFVLLAVFIAGLMIGRTPEYLGKKIDVREMKLTALA</span><span class="topo-membrane">ILVTPTLVLMGAAL</span><span class="topo-outside">AMMTDAGRSAMLNPGPHGFSEVL</span><span class="topo-unknown">YAVSSAANNNGS</span><span class="topo-outside">AFAGLSANSPF</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       </span>
<span class="topo-line"><span class="topo-outside">WN</span><span class="topo-membrane">CLLAFCMFVGRFGV</span><span class="topo-inside">IIPVMAIAGSLVSKKSQAASSGTLPTHGPLFVGLL</span><span class="topo-membrane">IGTVLLVGALTFIPAL</span><span class="topo-outside">ALGPVAEYLS</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>20</td>
      <td>4</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>69</td>
      <td>21</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>84</td>
      <td>70</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>102</td>
      <td>85</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>115</td>
      <td>103</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>116</td>
      <td>126</td>
      <td>116</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>144</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>177</td>
      <td>145</td>
      <td>177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>191</td>
      <td>178</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>218</td>
      <td>192</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>234</td>
      <td>219</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>235</td>
      <td>250</td>
      <td>235</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>265</td>
      <td>251</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>284</td>
      <td>266</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>298</td>
      <td>285</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>334</td>
      <td>299</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>346</td>
      <td>335</td>
      <td>346</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>347</td>
      <td>360</td>
      <td>347</td>
      <td>360</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>380</td>
      <td>361</td>
      <td>380</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>381</td>
      <td>420</td>
      <td>381</td>
      <td>420</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>434</td>
      <td>421</td>
      <td>434</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>457</td>
      <td>435</td>
      <td>457</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>469</td>
      <td>458</td>
      <td>469</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>470</td>
      <td>482</td>
      <td>470</td>
      <td>482</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>483</td>
      <td>496</td>
      <td>483</td>
      <td>496</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>497</td>
      <td>531</td>
      <td>497</td>
      <td>531</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>532</td>
      <td>547</td>
      <td>532</td>
      <td>547</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>548</td>
      <td>557</td>
      <td>548</td>
      <td>557</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5mrw">5MRW</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">FEPTLVVQALKEAVKKLNPQAQWRNPV</span><span class="topo-membrane">MFIVWIGSLLTTCISIA</span><span class="topo-outside">MASGAMPGNALF</span><span class="topo-membrane">SAAISGWLWITVLF</span><span class="topo-inside">ANFAEALAEGRSKAQANSLKGVKKTAFARKLREPKYGAAADKVPADQLRK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">GDIVLVEAGDIIPCDGEVIEGGASVDESAITGESAPVIRESGGDFASVTGGTRILSDWLVIECSVNPGETFLDRMIAMVEGAQRRKTPNEIALTILLI</span><span class="topo-membrane">ALTIVFLLATATL</span><span class="topo-outside">WPFSAWGGN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AVSV</span><span class="topo-membrane">TVLVALLVCLIPTT</span><span class="topo-inside">IGGLLSAIGVAGMSRMLGANVIATSGRAVEAAGDVDVLLLDKTGTITLGNRQASEFIPAQGVDEKTLADAAQLASLADETPEGRSIVILAKQRFNLRERDVQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">SLHATFVPFTAQSRMSGINIDNRMIRKGSVDAIRRHVEANGGHFPTDVDQKVDQVARQGATPLVVVEGSRVLGVIALKDIVKGGIKERFAQLRKMGIKTVMITGDNRLTAAAIAAEAGVD</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">DFLAEATPEAKLALIRQYQAEGRLVAMTGDGTNDAPALAQADVAVAMNSGTQAAKEAGNMVDLDSNPTKLIEVVHIGKQMLMTRGSLTTF</span><span class="topo-membrane">SIANDVAKYFAII</span><span class="topo-outside">PAAFAATYPQLNALNIM</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670    </span>
<span class="topo-line"><span class="topo-outside">CLHSPDS</span><span class="topo-membrane">AILSAVIFNALIIVF</span><span class="topo-inside">LIPLALKGVSYKPLTASAMLRRNLWIYG</span><span class="topo-membrane">LGGLLVPFIGIKVIDLLL</span><span class="topo-outside">TVCGLV</span></span>
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
      <td>27</td>
      <td>9</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>44</td>
      <td>36</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>56</td>
      <td>53</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>65</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>218</td>
      <td>79</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>231</td>
      <td>227</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>244</td>
      <td>240</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>258</td>
      <td>253</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>259</td>
      <td>570</td>
      <td>267</td>
      <td>578</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>571</td>
      <td>583</td>
      <td>579</td>
      <td>591</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>584</td>
      <td>607</td>
      <td>592</td>
      <td>615</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>608</td>
      <td>622</td>
      <td>616</td>
      <td>630</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>623</td>
      <td>650</td>
      <td>631</td>
      <td>658</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>651</td>
      <td>668</td>
      <td>659</td>
      <td>676</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>669</td>
      <td>674</td>
      <td>677</td>
      <td>682</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5mrw">5MRW</a> — Chain C (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">LRPALSTF</span><span class="topo-membrane">IFLLLITGGVYPLLTTVLGQWWF</span><span class="topo-outside">PWQANGSLIREGDTVRGSALIGQNFTGNGYFHGRPSATAEMPYNPQASGGSNLAVSNPELDKLIAARVAALRAANPDASASVPVELVTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       </span>
<span class="topo-line"><span class="topo-outside">SASGLDNNITPQAAAWQIPRVAKARNLSVEQLTQLIAKYSQQPLVKYIGQPVVNIVELNLALDKLDE</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>8</td>
      <td>4</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>31</td>
      <td>12</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>187</td>
      <td>35</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5mrw">5MRW</a> — Chain D (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20       </span>
<span class="topo-line"><span class="topo-outside">MSAGV</span><span class="topo-membrane">ITGVLLVFLLLGYLV</span><span class="topo-inside">YALINAE</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>20</td>
      <td>6</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>27</td>
      <td>21</td>
      <td>27</td>
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

### Coupling mechanism between KdpA and KdpB

The structure reveals a 1.4 A radius intramembrane tunnel connecting the K+ binding site in KdpA to a water molecule bound at the canonical cation site in KdpB. This tunnel likely facilitates proton charge transfer that triggers ATP hydrolysis in KdpB in response to K+ binding in KdpA. Key residues include Asp583 and Lys586 in KdpB, and Glu370 and Arg493 in KdpA.

### KdpA as a repurposed K+ channel

KdpA uses a selectivity filter architecture descended from the [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) K+ channel, but repurposes it for active transport rather than passive diffusion. Unlike [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), KdpA has a gating loop at the cytoplasmic end derived from the D3M2 helix, and the S1 site of the selectivity filter is occupied by Arg116 (Q116R in this construct).

### E1 state of KdpB

KdpB adopts an E1 conformational state with the A domain decoupled from the P domain, the N and P domains juxtaposed, Asp307 unphosphorylated, and the bM4 helix unwound at the conserved Pro264 motif. A phosphoserine (Ser162) in the A domain forms a salt bridge with Lys357 and Arg363 of the N domain, suggesting an autoinhibited state.

### KdpC as a periplasmic gate

The soluble domain of KdpC is held by two loops from D2 and D3 repeats of KdpA via a robust hydrogen bond network. This interaction suggests that relative movements between KdpA repeats could move KdpC into an occluding position in response to conformational changes in KdpB, acting as a periplasmic gate.


## Cross-References

- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KCSA</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-maltoside</a> — Detergent used in purification or crystallization
