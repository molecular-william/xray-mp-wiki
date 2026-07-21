---
title: "Escherichia coli CorA Mg2+ Channel (Cytoplasmic Domain)"
created: 2026-05-29
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.05.024]
verified: agent
uniprot_id: P31224
---

# Escherichia coli CorA Mg2+ Channel (Cytoplasmic Domain)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P31224">UniProt: P31224</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

CorA from Escherichia coli is the family prototype of the CorA Mg2+ transporter channel, the major Mg2+ uptake system in prokaryotes. This entry documents the first crystal structures of the cytoplasmic domain from E. coli CorA (EcCorA), revealing a pentameric arrangement with novel Mg2+ binding sites at subunit interfaces and within the pore. The structures provide structural evidence for cooperative gating and demonstrate that the cytoplasmic domain alone contains all components necessary for the gating motion.


## Publications

### doi/10.1016##j.str.2017.05.024

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5n77">5N77</a></td>
      <td>2.90 A</td>
      <td>C 222_1</td>
      <td>241EcCorA (residues 1-241 of EcCorA, cytoplasmic domain only, TEV-GFP-His8 tag)</td>
      <td>Apo (no Mg2+)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5n77">5N77</a></td>
      <td>2.80 A</td>
      <td>P 2_1</td>
      <td>257EcCorA (residues 1-257 of EcCorA, cytoplasmic domain only, TEV-GFP-His8 tag)</td>
      <td>Mg2+ (bound at interfacial and pore sites)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5n77">5N77</a></td>
      <td>2.85 A</td>
      <td>P 2_1</td>
      <td>257EcCorA-Mg2+/CoHex (residues 1-257 of EcCorA, cytoplasmic domain, TEV-GFP-His8 tag, with cobalt hexamine)</td>
      <td>Mg2+ and cobalt hexamine (hexaamminecobalt(III))</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: Cytoplasmic domains of EcCorA (residues 1-241, 1-247, and 1-257) cloned into pGFPe vector with N-terminal TEV-GFP-His8 tag, controlled by T7 promoter. Cells grown in Terrific broth at 37 C, induced with 0.4 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg), grown overnight at 20 C.


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
      <td>Sonication</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 7.9, 300 mM NaCl, EDTA-free Complete Protease Inhibitor Cocktail, Benzonase Nuclease, Lysozyme + --</td>
      <td>Cells resuspended in lysis buffer, sonicated, unbroken cells removed by centrifugation at 9300 g for 20 min</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">IMAC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) Agarose (Invitrogen)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 7.9, 300 mM NaCl + --</td>
      <td>Supernatant applied to 2 ml <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> Agarose, incubated 30 min. Washed with 2 column volumes of buffer containing 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>. Eluted with buffer containing 350 mM imidazole.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8, 100 mM NaCl + --</td>
      <td>Final purification step. <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) performed in presence or absence of Mg2+ depending on construct and experimental condition.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>241EcCorA monomeric construct</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td><a href="/xray-mp-wiki/reagents/additives/peg-400">PEG 400</a>0</td>
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
      <td>Monomeric 241EcCorA crystallized in space group C222_1 at 2.90 A resolution. Solved by SAD phasing with <a href="/xray-mp-wiki/reagents/additives/selenomethionine">Selenomethionine (SeMet)</a>-labeled protein.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5jmn">5JMN</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDTVTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGSQYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANALDTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVMAEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYR</span><span class="topo-membrane">QFSITIVSAMAL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGRYL</span><span class="topo-membrane">VLYLIIVVGMAYLFVRL</span><span class="topo-outside">PSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAIT</span><span class="topo-unknown">M</span><span class="topo-outside">RATRAFSQIKDAMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYRMLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIPFSV</span><span class="topo-membrane">MLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050       </span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQ</span><span class="topo-membrane">NAVGTGVMGGMVTATVLA</span><span class="topo-unknown">IFFVPVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>468</td>
      <td>459</td>
      <td>468</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>489</td>
      <td>469</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>537</td>
      <td>512</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>542</td>
      <td>538</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>559</td>
      <td>543</td>
      <td>559</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>560</td>
      <td>648</td>
      <td>560</td>
      <td>648</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>649</td>
      <td>649</td>
      <td>649</td>
      <td>649</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>650</td>
      <td>873</td>
      <td>650</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>890</td>
      <td>874</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>901</td>
      <td>891</td>
      <td>901</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>902</td>
      <td>919</td>
      <td>902</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>992</td>
      <td>976</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1000</td>
      <td>993</td>
      <td>1000</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1001</td>
      <td>1018</td>
      <td>1001</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1032</td>
      <td>1019</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5jmn">5JMN</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDTVTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGSQYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANALDTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVMAEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STGR</span><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKDAMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYRMLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFSVMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050       </span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIFFV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>384</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>412</td>
      <td>397</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>441</td>
      <td>413</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>456</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>536</td>
      <td>511</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>540</td>
      <td>537</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>556</td>
      <td>541</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>918</td>
      <td>896</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>944</td>
      <td>928</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>974</td>
      <td>945</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5jmn">5JMN</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPIFA</span><span class="topo-membrane">WVIAIIIMLAGGLAIL</span><span class="topo-outside">KLPVAQYPTIAPPAVTISASYPGADAKTVQDTVTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGSQYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANALDTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVMAEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIY</span><span class="topo-membrane">RQFSITIVSAMAL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">SVLVA</span><span class="topo-inside">LILTPALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STGRY</span><span class="topo-membrane">LVLYLIIVVGMAYLFVR</span><span class="topo-outside">LPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKDAMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYRMLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FSVMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050       </span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLA</span><span class="topo-unknown">IFFVPVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>8</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>28</td>
      <td>13</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>340</td>
      <td>29</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>467</td>
      <td>459</td>
      <td>467</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>485</td>
      <td>468</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>536</td>
      <td>512</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>558</td>
      <td>542</td>
      <td>558</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>559</td>
      <td>873</td>
      <td>559</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>891</td>
      <td>874</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>992</td>
      <td>976</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1018</td>
      <td>1004</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1032</td>
      <td>1019</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5jmn">5JMN</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHLEIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-ruler">       130       140       150       160         </span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQKL</span><span class="topo-unknown">N</span></span>
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
      <td>11</td>
      <td>168</td>
      <td>11</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5jmn">5JMN</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHLEIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-ruler">       130       140       150       160         </span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>13</td>
      <td>166</td>
      <td>13</td>
      <td>166</td>
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

### Novel Mg2+ ligand binding site at subunit interfaces

The 257EcCorA-Mg2+ structure reveals a novel putative Mg2+ ligand binding site located at the interface between each of the five subunits. A single Mg2+ ion is coordinated by D58 and E60 from the clutch motif of one subunit and D146 and E149 from helix 4 on the adjacent subunit. This represents a new variant of the regulatory Mg2+ ligand binding site in the CorA family, structurally distinct from the M1/M2 sites identified in TmCorA and MjCorA. ConSurf analysis shows all four Mg2+ binding residues, plus S62 and D222, are highly conserved in the CorA family. The pore helix residue D222 forms a hydrogen bond with S62 of the clutch motif, potentially mediating a subunit contact that stabilizes the pore helix indirectly.

### Mg2+ binding sites within the pore

Two Mg2+ ions are trapped inside the pore at each subunit. At the top site near the membrane interface, a putative substrate-Mg2+ is sandwiched between two polar rings: Q252 (5-fold, ~4.3 A pore diameter) and N249 (5-fold, ~7 A pore diameter). The bound Mg2+ coordinates with multiple amide oxygens from both rings. Below, a 5-fold ring of Q242 residues coordinates another Mg2+ ion in the ion-conduction pathway. The Q242 site has no direct contacts with protein side chains and appears functionally dispensable based on alanine scanning mutagenesis.

### Cobalt hexamine competes with Mg2+ at the pore site

Soaking experiments with cobalt hexamine (hexaamminecobalt(III)) show it outcompetes substrate-Mg2+ at the N249/Q252 site closest to the membrane, while the Q242 site and the five interfacial ligand binding sites retain their Mg2+. Cobalt hexamine binds at the N249/Q252 site and 13 peripheral sites. This provides the first structural evidence that a hexa-hydrated Mg2+ analog can fit inside the cytoplasmic portion of the CorA pore, suggesting Mg2+ is or becomes hexa-hydrated as it enters the pore.

### Cooperative gating by pentamer assembly/disassembly

[SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) shows the 257EcCorA cytoplasmic domain assembles into a pentamer in response to Mg2+ (100 mM) and dissociates to monomer in low Mg2+ (10 mM). The dissociation curve is sigmoidal, occurring between 10-20 mM Mg2+, indicating a cooperative process. Shorter constructs (241EcCorA, 247EcCorA) with truncated pore helices remain monomeric even at 100 mM Mg2+, showing pore helix length is critical for pentamer stabilization. Mutations of the interfacial ligand binding site (D58A/E60A/D146A/E149A) or N249A/Q252A prevent pentamer assembly, confirming both sites are essential for the gating mechanism.

### Full-length protein has 10-fold higher Mg2+ affinity

Protease protection assays comparing the isolated cytoplasmic domain (257EcCorA) with full-length 316EcCorA in native membranes reveal a 10-fold increase in Mg2+ affinity in the full-length protein. The cytoplasmic domain shows Mg2+-dependent protection between 10-20 mM, while full-length EcCorA requires only 0-10 mM Mg2+. This is attributed to structural stabilization of the interfacial ligand binding sites provided by intra- and inter-subunit interactions in the membrane domain. The isolated cytoplasmic domain thus contains all molecular components for gating but with non-physiological Mg2+ affinity.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/cora-mg-transporter/">CorA Mg2+ Transporter</a> — CorA is the prototype family; this paper provides first EcCorA cytoplasmic domain structures
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/mit-superfamily/">Metal Ion Transporter Superfamily</a> — CorA is the founding member of the MIT superfamily of metal ion transporters
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Used for final purification and [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) analysis of pentamer assembly/disassembly
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Used to solve 257EcCorA-Mg2+ and 257EcCorA-Mg2+/CoHex structures
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> — Used for [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag) affinity purification of TEV-GFP-His8 tagged constructs
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride (MgCl2)</a> — Mg2+ is the physiological ligand that drives pentamer assembly and channel gating
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/">Channel Gating via Plug Domain Displacement</a> — CorA gating mechanism involves rigid-body motion of cytoplasmic domain subunits
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a> — Crystallization method used for structure determination
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Immobilized Metal Affinity Chromatography (IMAC)</a> — Purification method used in protein preparation
- <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a> — Additive used in purification or crystallization buffers
