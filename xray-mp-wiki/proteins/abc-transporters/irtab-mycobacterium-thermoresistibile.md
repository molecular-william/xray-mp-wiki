---
title: "IrtAB ABC Exporter from Mycobacterium thermoresistibile"
created: 2026-06-21
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-020-2136-9]
verified: agent
uniprot_id: ['A0A100XE85', 'A0A100XEC2']
---

# IrtAB ABC Exporter from Mycobacterium thermoresistibile

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A100XE85">UniProt: A0A100XE85</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A100XEC2">UniProt: A0A100XEC2</a>

<span class="expr-badge">Mycolicibacterium thermoresistibile</span>

## Overview

IrtAB is a heterodimeric ATP-binding cassette (ABC) transporter from
Mycobacterium thermoresistibile that imports iron-bound mycobactin and
carboxymycobactin siderophores across the inner mycobacterial membrane. Despite
having an ABC exporter fold, IrtAB functions as an importer — an unusual feature
for this structural class. The protein comprises IrtA and IrtB subunits, each
containing a transmembrane domain (TMD) and a nucleotide-binding domain (NBD).
IrtA additionally features an N-terminal siderophore interaction domain (SID)
that binds flavin adenine dinucleotide (FAD) and reduces Fe(III)-mycobactin to
Fe(II), facilitating iron release. The structure reveals a collapsed inward-facing
cavity with a lateral opening to the inner membrane leaflet, positioning the SID
to capture membrane-embedded mycobactin.


## Publications

### doi/10.1038##s41586-020-2136-9

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tej">6TEJ</a></td>
      <td>2.7</td>
      <td>P2₁</td>
      <td>IrtAB lacking SID domain (IrtAB(ΔSID)) with sybody Syb_NL5</td>
      <td>None (apo, inward-facing)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tej">6TEJ</a></td>
      <td>1.8</td>
      <td>P2₁</td>
      <td>Isolated SID domain (residues 1-...)</td>
      <td>FAD</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tej">6TEJ</a></td>
      <td>6.9</td>
      <td></td>
      <td>Full-length IrtAB (including SID)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli MC1061
- **Construct**: Full-length IrtAB with C-terminal GFP-His10 on IrtB; SID constructs with N-terminal His10-3C tag
- **Notes**: IrtAB expressed in E. coli; membrane vesicles prepared by ultracentrifugation

**Purification:**

- **Expression system**: E. coli MC1061
- **Expression construct**: Full-length IrtAB with C-terminal GFP-His10 tag on IrtB
- **Tag info**: C-terminal His10 tag on IrtB (cleavable by 3C protease)

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
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>TBS (50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>)</td>
      <td>Cells broken, debris removed at 8,000g, membranes pelleted at 170,000g</td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Solubilization</td>
      <td>—</td>
      <td>TBS + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Extracted for 2 h at 4°C, followed by ultracentrifugation at 170,000g</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> gravity flow column</td>
      <td>TBS with 20-250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient + 0.03% β-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Imidazole added to 20 mM before loading; elution with 250 mM imidazole</td>
    </tr>
    <tr>
      <td>Ion exchange chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Anion Exchange</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/resource-q/">Resource Q</a> (GE Healthcare)</td>
      <td>15 mM Tris pH 8.0, 20-350 mM NaCl gradient + 0.03% β-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Protein eluted at ~150 mM NaCl</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superose-6/">Superose 6 Increase</a> 10/300 GL</td>
      <td>TBS + Various (0.3% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 0.03% β-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>)</td>
      <td>Final polishing step; buffer exchanged to desired detergent during <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified IrtAB in 0.03% β-DDM for nanodisc reconstitution or crystallization

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>IrtAB(ΔSID) with sybody Syb_NL5 in 0.03% β-DDM</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>IrtAB(ΔSID) was crystallized with the aid of sybody Syb_NL5; SID domain was crystallized separately</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>sitting-drop</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tej">6TEJ</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGFQGVMLRGLGARDHQATVVDKEYIAPHFVRVRLVSPTLFDEVIVEPTSWLRFWFPDPDGSDTEFQRAYTITESDPETGRFAVDMVLHEPAGPASTWARTVEPGATIAVMSMGSRGF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">SVPEDPEDRPVGYLLIGDSASTPAINGIIEVVPHDIPIELYLEQHHDDDVLIPLAEHPRLRVHRVSRDDASSLAAALELRDWSNWYCWAGPEAGALKQVRTRLRDEFGFPKREVYAQAYW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">TEGRAMGSSRGETSTPAKPAAKTAPAKAAAKPAAASGAGTPEHAAAPAAATTGAPQAAPAPGAAQPRTPVRGRWR</span><span class="topo-outside">AEAGSRLLAPLKKPLIVSG</span><span class="topo-membrane">VLQALITLIELAPFV</span><span class="topo-inside">LLVELARLLLG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">GAEAERLWTLGLT</span><span class="topo-membrane">AVSLIGLGAVLAAA</span><span class="topo-outside">MTLWLHRVDARFAHELRGRLLTKLSRLPLGWFTRRGSASTKQLVQDDTLALHYLITHAIPDA</span><span class="topo-membrane">VAAVVAPVAVLVYLFV</span><span class="topo-inside">AD</span><span class="topo-membrane">WRVALVLFIPVLV</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">YL</span><span class="topo-outside">VLMSVMTIQSGSKIAQAPRWAERMGGEAGAFLEGQPVIRIFGGAAASRFRRRLDDYIDFLVSWQRPFVGKKT</span><span class="topo-membrane">LMDLVTRPATFLWII</span><span class="topo-inside">LVAGVPLVVTGRMDPVNLL</span><span class="topo-membrane">PFLLLGTTFGAR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LL</span><span class="topo-outside">GIGYGLSGIQTGMLAARRIQTVLDEPELVVRDRT</span><span class="topo-unknown">GQAGTDHASGDQAR</span><span class="topo-outside">PGTVELDRVSFEYRPGVPVIRDVTLTLRPGTVTALVGPSGSGKSTLAALVARFHDVTQGAIRVDGRDIRT</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LTADELYRRVGFVLQDAQLVHGSVAENIALAEPDAGLERIRTAARDAQIHDRITRMPDGYDSVLGAGSALSGGERQRVTIARAILADTPVLVLDEATAFADPESEYLVQQAINRLTRDRT</span></span>
<span class="topo-ruler">       850       860       870       880       890       900        </span>
<span class="topo-line"><span class="topo-outside">VLVIAHRLHTITHADQIVVLDDGRIVEVGTHDELLAAGGRYRGLWDSGRY</span><span class="topo-unknown">SSPDAGRPVSADAVEVGR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>315</td>
      <td>1</td>
      <td>315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>316</td>
      <td>334</td>
      <td>316</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>349</td>
      <td>335</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>373</td>
      <td>350</td>
      <td>373</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>387</td>
      <td>374</td>
      <td>387</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>449</td>
      <td>388</td>
      <td>449</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>465</td>
      <td>450</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>467</td>
      <td>466</td>
      <td>467</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>482</td>
      <td>468</td>
      <td>482</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>483</td>
      <td>554</td>
      <td>483</td>
      <td>554</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>555</td>
      <td>569</td>
      <td>555</td>
      <td>569</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>570</td>
      <td>588</td>
      <td>570</td>
      <td>588</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>589</td>
      <td>602</td>
      <td>589</td>
      <td>602</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>603</td>
      <td>636</td>
      <td>603</td>
      <td>636</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>637</td>
      <td>650</td>
      <td>637</td>
      <td>650</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>651</td>
      <td>890</td>
      <td>651</td>
      <td>890</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>891</td>
      <td>908</td>
      <td>891</td>
      <td>908</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tej">6TEJ</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">IRTLLRLVPAEKRGAVA</span><span class="topo-membrane">GYAVLTLLSVLLRAVGA</span><span class="topo-inside">VLLIPLLAALFSDTPSDAWLWLGWL</span><span class="topo-membrane">TAVTLAGWVTDTNT</span><span class="topo-outside">ARLGFDLGFAVLSRTQHDMADRLPNVAMSWFTPDNTATARQAIAAT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GPELAGLVVNLL</span><span class="topo-membrane">TPLIGAALLPAAIGVA</span><span class="topo-inside">LLFVSVPLG</span><span class="topo-membrane">LAALAGVAVLFGALALS</span><span class="topo-outside">GRLSRAADKVAGETNSAFTERIIEFARTQQALRAARRVEPARSQVGSALAAQHGAGLRLLTMQI</span><span class="topo-membrane">PG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">QVLFSLAGQVALIG</span><span class="topo-inside">FAGMAVWLTVRGQLGVPEAI</span><span class="topo-membrane">ALIVVLVRYLEPFA</span><span class="topo-outside">AIADLAPALETTRATLNRIQAVLDAPTLPAGRRRLDRTGAAPSIEFDDVRFSYGDEVVLDGVSFTLRPGNTT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AIVGPSGSGKTTILSLIAGLQQPASGRVLLDGVDVTTLDPEARRAAVSVVFQHPYLFDGTLRDNVLVGDPEADPDDVTAAMRLARVDELLDRLPDGDATVVGEGGTALSGGERQRVSIAR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580      </span>
<span class="topo-line"><span class="topo-outside">ALLKPAPVLLVDEATSALDNANEAAVVDALTADPRPRTRVIVAHRLASIRHADRVLFVEAGRVVEDGAIDELLAAGGRFAQFWAQQQAASEWAIGSTARALEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>18</td>
      <td>2</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>19</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>60</td>
      <td>36</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>74</td>
      <td>61</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>132</td>
      <td>75</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>148</td>
      <td>133</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>157</td>
      <td>149</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>174</td>
      <td>158</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>238</td>
      <td>175</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>254</td>
      <td>239</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>274</td>
      <td>255</td>
      <td>274</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>288</td>
      <td>275</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>586</td>
      <td>289</td>
      <td>586</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tej">6TEJ</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGFQGVMLRGLGARDHQATVVDKEYIAPHFVRVRLVSPTLFDEVIVEPTSWLRFWFPDPDGSDTEFQRAYTITESDPETGRFAVDMVLHEPAGPASTWARTVEPGATIAVMSMGSRGF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">SVPEDPEDRPVGYLLIGDSASTPAINGIIEVVPHDIPIELYLEQHHDDDVLIPLAEHPRLRVHRVSRDDASSLAAALELRDWSNWYCWAGPEAGALKQVRTRLRDEFGFPKREVYAQAYW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">TEGRAMGSSRGETSTPAKPAAKTAPAKAAAKPAAASGAGTPEHAAAPAAATTGAPQAAPAPGAAQPRTPVRGRWR</span><span class="topo-outside">AEAGSRLLAPLKKPLIVSG</span><span class="topo-membrane">VLQALITLIELAPFV</span><span class="topo-inside">LLVELARLLLG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">GAEAERLWTLGLT</span><span class="topo-membrane">AVSLIGLGAVLAAA</span><span class="topo-outside">MTLWLHRVDARFAHELRGRLLTKLSRLPLGWFTRRGSASTKQLVQDDTLALHYLITHAIPDA</span><span class="topo-membrane">VAAVVAPVAVLVYLFV</span><span class="topo-inside">AD</span><span class="topo-membrane">WRVALVLFIPVLV</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">YL</span><span class="topo-outside">VLMSVMTIQSGSKIAQAPRWAERMGGEAGAFLEGQPVIRIFGGAAASRFRRRLDDYIDFLVSWQRPFVGKKT</span><span class="topo-membrane">LMDLVTRPATFLWII</span><span class="topo-inside">LVAGVPLVVTGRMDPVNLL</span><span class="topo-membrane">PFLLLGTTFGAR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LL</span><span class="topo-outside">GIGYGLSGIQTGMLAARRIQTVLDEPELVVRDRT</span><span class="topo-unknown">GQAGTDHASGDQAR</span><span class="topo-outside">PGTVELDRVSFEYRPGVPVIRDVTLTLRPGTVTALVGPSGSGKSTLAALVARFHDVTQGAIRVDGRDIRT</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LTADELYRRVGFVLQDAQLVHGSVAENIALAEPDAGLERIRTAARDAQIHDRITRMPDGYDSVLGAGSALSGGERQRVTIARAILADTPVLVLDEATAFADPESEYLVQQAINRLTRDRT</span></span>
<span class="topo-ruler">       850       860       870       880       890       900        </span>
<span class="topo-line"><span class="topo-outside">VLVIAHRLHTITHADQIVVLDDGRIVEVGTHDELLAAGGRYRGLWDSGRY</span><span class="topo-unknown">SSPDAGRPVSADAVEVGR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>315</td>
      <td>1</td>
      <td>315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>316</td>
      <td>334</td>
      <td>316</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>349</td>
      <td>335</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>373</td>
      <td>350</td>
      <td>373</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>387</td>
      <td>374</td>
      <td>387</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>449</td>
      <td>388</td>
      <td>449</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>465</td>
      <td>450</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>467</td>
      <td>466</td>
      <td>467</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>482</td>
      <td>468</td>
      <td>482</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>483</td>
      <td>554</td>
      <td>483</td>
      <td>554</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>555</td>
      <td>569</td>
      <td>555</td>
      <td>569</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>570</td>
      <td>588</td>
      <td>570</td>
      <td>588</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>589</td>
      <td>602</td>
      <td>589</td>
      <td>602</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>603</td>
      <td>636</td>
      <td>603</td>
      <td>636</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>637</td>
      <td>650</td>
      <td>637</td>
      <td>650</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>651</td>
      <td>890</td>
      <td>651</td>
      <td>890</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>891</td>
      <td>908</td>
      <td>891</td>
      <td>908</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tej">6TEJ</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">IRTLLRLVPAEKRGAVA</span><span class="topo-membrane">GYAVLTLLSVLLRAVGA</span><span class="topo-inside">VLLIPLLAALFSDTPSDAWLWLGWL</span><span class="topo-membrane">TAVTLAGWVTDTNT</span><span class="topo-outside">ARLGFDLGFAVLSRTQHDMADRLPNVAMSWFTPDNTATARQAIAAT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GPELAGLVVNLL</span><span class="topo-membrane">TPLIGAALLPAAIGVA</span><span class="topo-inside">LLFVSVPLG</span><span class="topo-membrane">LAALAGVAVLFGALALS</span><span class="topo-outside">GRLSRAADKVAGETNSAFTERIIEFARTQQALRAARRVEPARSQVGSALAAQHGAGLRLLTMQI</span><span class="topo-membrane">PG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">QVLFSLAGQVALIG</span><span class="topo-inside">FAGMAVWLTVRGQLGVPEAI</span><span class="topo-membrane">ALIVVLVRYLEPFA</span><span class="topo-outside">AIADLAPALETTRATLNRIQAVLDAPTLPAGRRRLDRTGAAPSIEFDDVRFSYGDEVVLDGVSFTLRPGNTT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AIVGPSGSGKTTILSLIAGLQQPASGRVLLDGVDVTTLDPEARRAAVSVVFQHPYLFDGTLRDNVLVGDPEADPDDVTAAMRLARVDELLDRLPDGDATVVGEGGTALSGGERQRVSIAR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580      </span>
<span class="topo-line"><span class="topo-outside">ALLKPAPVLLVDEATSALDNANEAAVVDALTADPRPRTRVIVAHRLASIRHADRVLFVEAGRVVEDGAIDELLAAGGRFAQFWAQQQAASEWAIGSTARALEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>18</td>
      <td>2</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>19</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>60</td>
      <td>36</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>74</td>
      <td>61</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>132</td>
      <td>75</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>148</td>
      <td>133</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>157</td>
      <td>149</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>174</td>
      <td>158</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>238</td>
      <td>175</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>254</td>
      <td>239</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>274</td>
      <td>255</td>
      <td>274</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>288</td>
      <td>275</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>586</td>
      <td>289</td>
      <td>586</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tej">6TEJ</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGFQGVMLRGLGARDHQATVVDKEYIAPHFVRVRLVSPTLFDEVIVEPTSWLRFWFPDPDGSDTEFQRAYTITESDPETGRFAVDMVLHEPAGPASTWARTVEPGATIAVMSMGSRGF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">SVPEDPEDRPVGYLLIGDSASTPAINGIIEVVPHDIPIELYLEQHHDDDVLIPLAEHPRLRVHRVSRDDASSLAAALELRDWSNWYCWAGPEAGALKQVRTRLRDEFGFPKREVYAQAYW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">TEGRAMGSSRGETSTPAKPAAKTAPAKAAAKPAAASGAGTPEHAAAPAAATTGAPQAAPAPGAAQPRTPVRGRWR</span><span class="topo-outside">AEAGSRLLAPLKKPLIVSG</span><span class="topo-membrane">VLQALITLIELAPFV</span><span class="topo-inside">LLVELARLLLG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">GAEAERLWTLGLT</span><span class="topo-membrane">AVSLIGLGAVLAAA</span><span class="topo-outside">MTLWLHRVDARFAHELRGRLLTKLSRLPLGWFTRRGSASTKQLVQDDTLALHYLITHAIPDA</span><span class="topo-membrane">VAAVVAPVAVLVYLFV</span><span class="topo-inside">AD</span><span class="topo-membrane">WRVALVLFIPVLV</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">YL</span><span class="topo-outside">VLMSVMTIQSGSKIAQAPRWAERMGGEAGAFLEGQPVIRIFGGAAASRFRRRLDDYIDFLVSWQRPFVGKKT</span><span class="topo-membrane">LMDLVTRPATFLWII</span><span class="topo-inside">LVAGVPLVVTGRMDPVNLL</span><span class="topo-membrane">PFLLLGTTFGAR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LL</span><span class="topo-outside">GIGYGLSGIQTGMLAARRIQTVLDEPELVVRDRT</span><span class="topo-unknown">GQAGTDHASGDQAR</span><span class="topo-outside">PGTVELDRVSFEYRPGVPVIRDVTLTLRPGTVTALVGPSGSGKSTLAALVARFHDVTQGAIRVDGRDIRT</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LTADELYRRVGFVLQDAQLVHGSVAENIALAEPDAGLERIRTAARDAQIHDRITRMPDGYDSVLGAGSALSGGERQRVTIARAILADTPVLVLDEATAFADPESEYLVQQAINRLTRDRT</span></span>
<span class="topo-ruler">       850       860       870       880       890       900        </span>
<span class="topo-line"><span class="topo-outside">VLVIAHRLHTITHADQIVVLDDGRIVEVGTHDELLAAGGRYRGLWDSGRY</span><span class="topo-unknown">SSPDAGRPVSADAVEVGR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>315</td>
      <td>1</td>
      <td>315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>316</td>
      <td>334</td>
      <td>316</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>349</td>
      <td>335</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>373</td>
      <td>350</td>
      <td>373</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>387</td>
      <td>374</td>
      <td>387</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>449</td>
      <td>388</td>
      <td>449</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>465</td>
      <td>450</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>467</td>
      <td>466</td>
      <td>467</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>482</td>
      <td>468</td>
      <td>482</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>483</td>
      <td>554</td>
      <td>483</td>
      <td>554</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>555</td>
      <td>569</td>
      <td>555</td>
      <td>569</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>570</td>
      <td>588</td>
      <td>570</td>
      <td>588</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>589</td>
      <td>602</td>
      <td>589</td>
      <td>602</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>603</td>
      <td>636</td>
      <td>603</td>
      <td>636</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>637</td>
      <td>650</td>
      <td>637</td>
      <td>650</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>651</td>
      <td>890</td>
      <td>651</td>
      <td>890</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>891</td>
      <td>908</td>
      <td>891</td>
      <td>908</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tej">6TEJ</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">IRTLLRLVPAEKRGAVA</span><span class="topo-membrane">GYAVLTLLSVLLRAVGA</span><span class="topo-inside">VLLIPLLAALFSDTPSDAWLWLGWL</span><span class="topo-membrane">TAVTLAGWVTDTNT</span><span class="topo-outside">ARLGFDLGFAVLSRTQHDMADRLPNVAMSWFTPDNTATARQAIAAT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GPELAGLVVNLL</span><span class="topo-membrane">TPLIGAALLPAAIGVA</span><span class="topo-inside">LLFVSVPLG</span><span class="topo-membrane">LAALAGVAVLFGALALS</span><span class="topo-outside">GRLSRAADKVAGETNSAFTERIIEFARTQQALRAARRVEPARSQVGSALAAQHGAGLRLLTMQI</span><span class="topo-membrane">PG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">QVLFSLAGQVALIG</span><span class="topo-inside">FAGMAVWLTVRGQLGVPEAI</span><span class="topo-membrane">ALIVVLVRYLEPFA</span><span class="topo-outside">AIADLAPALETTRATLNRIQAVLDAPTLPAGRRRLDRTGAAPSIEFDDVRFSYGDEVVLDGVSFTLRPGNTT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AIVGPSGSGKTTILSLIAGLQQPASGRVLLDGVDVTTLDPEARRAAVSVVFQHPYLFDGTLRDNVLVGDPEADPDDVTAAMRLARVDELLDRLPDGDATVVGEGGTALSGGERQRVSIAR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580      </span>
<span class="topo-line"><span class="topo-outside">ALLKPAPVLLVDEATSALDNANEAAVVDALTADPRPRTRVIVAHRLASIRHADRVLFVEAGRVVEDGAIDELLAAGGRFAQFWAQQQAASEWAIGSTARALEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>18</td>
      <td>2</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>19</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>60</td>
      <td>36</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>74</td>
      <td>61</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>132</td>
      <td>75</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>148</td>
      <td>133</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>157</td>
      <td>149</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>174</td>
      <td>158</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>238</td>
      <td>175</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>254</td>
      <td>239</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>274</td>
      <td>255</td>
      <td>274</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>288</td>
      <td>275</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>586</td>
      <td>289</td>
      <td>586</td>
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

### ABC exporter fold with import function

IrtAB adopts an ABC exporter fold despite functioning as an importer. The inward-facing cavity is collapsed at the upper region compared to canonical ABC exporters like TM287/288. TMH6 of IrtB protrudes into the cavity, TMH3 is strongly kinked, and the domain-swap helices (TMH4 and TMH5) of IrtA are bulged out, forming a lateral opening to the inner membrane leaflet where the SID is located.

### Siderophore Interaction Domain (SID) function

The SID is an N-terminal domain of IrtA with a flavoreductase fold and bound FAD. It reduces Fe(III)-mycobactin to Fe(II) using NADPH as electron donor, facilitating iron release. The SID is essential for iron utilization via Fe-MBT (membrane-bound mycobactin) but dispensable for Fe-cMBT (soluble carboxymycobactin), which can diffuse into the cytoplasm and be reduced by other ferric reductases.

### Transport and reduction mechanism

IrtAB imports both Fe-MBT and Fe-cMBT across the inner mycobacterial membrane. Fe-MBT, being lipid-bound, remains anchored to the inner membrane leaflet after import and is positioned for reduction by the SID. Fe-cMBT, being water-soluble, can diffuse freely into the cytoplasm. The transport mechanism likely involves a credit-card-swipe mechanism similar to the glycolipid ABC transporter PglK, with the lipid tail of Fe-MBT remaining embedded in the bilayer during import.


## Cross-References

- <a href="/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/">Flavin Adenine Dinucleotide (FAD)</a> — FAD is the redox cofactor bound by the SID domain of IrtA
- <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-beta-D-Maltoside (DM)</a> — Detergent used in purification and crystallization of IrtAB
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-d-maltopyranoside (DDM)</a> — Detergent used for membrane extraction and purification of IrtAB
- <a href="/xray-mp-wiki/methods/solubilization/nanodisc-reconstitution/">Nanodisc Reconstitution</a> — IrtAB was reconstituted into nanodiscs for ATPase activity measurements
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — IrtAB belongs to the ABC transporter superfamily with an exporter fold
