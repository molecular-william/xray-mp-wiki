---
title: "MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)"
created: 2026-06-02
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature06264]
verified: regex
uniprot_id: ['P02916', 'P0AEX9', 'P68183', 'Q1R3Q1']
---

# MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P02916">UniProt: P02916</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AEX9">UniProt: P0AEX9</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P68183">UniProt: P68183</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1R3Q1">UniProt: Q1R3Q1</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

MalG is a transmembrane subunit of the Escherichia coli [Maltose](/xray-mp-wiki/reagents/additives/maltose/) uptake system, an ATP-binding cassette (ABC) importer. MalG contains 6 transmembrane helices and 296 residues. Together with [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malF/), it forms the transmembrane domain of the transporter. MalG features a periplasmic loop (P3) that inserts into the maltose-binding protein cleft to dislodge bound [Maltose](/xray-mp-wiki/reagents/additives/maltose/), acting as a scoop mechanism. Its C-terminal tail (residues 290-296) packs along the Q loop of [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/), contributing to Q loop ordering and catalytic intermediate formation.


## Publications

### doi/10.1038##nature06264

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2r6g">2R6G</a></td>
      <td>2.8</td>
      <td>not specified</td>
      <td>Full-length MalG (296 residues) from E. coli <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> transporter</td>
      <td><a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> (transmembrane binding site)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli HN741
- **Construct**: Full-length MalG with [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malF/) and [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/)(E159Q); engineered C-terminal His6 tag on [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/)

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>--</td>
      <td>Terrific Broth + --</td>
      <td>Cells grown at 37 C, induced with 50 uM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> at 22 C for 24 h</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>High-pressure homogenization and centrifugation</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8, 100 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 5 mM MgCl2 + --</td>
      <td>100,000g for 30 min at 4 C</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8, 100 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 5 mM MgCl2 + 0.35% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Solubilized for 4 h at room temperature; 100,000g for 20 min at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt-affinity resin (Clontech)</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8, 100 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Wash with 5 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elute with 100 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Dialysis</td>
      <td>Dialysis</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8, 200 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>--</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8, 200 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>--</td>
    </tr>
  </tbody>
</table>
**Final sample**: Not specified
**Yield**: Not specified

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2r6g">2R6G</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">ASVQLQNVTKAWGEVVVSKDINLDIHEGEFVVFVGPSGCGKSTLLRMIAGLETITSGDLFIGEKRMNDTPPAERGVGMVFQSYALYPHLSVAENMSFGLKLAGAKKEVINQRVNQVAEV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LQLAHLLDRKPKALSGGQRQRVAIGRTLVAEPSVFLLDQPLSNLDAALRVQMRIEISRLHKRLGRTMIYVTHDQVEAMTLADKIVVLDAGRVAQVGKPLELYHYPADRFVAGFIGSPKMN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">FLPVKVTATAIDQVQVELPMPNRQQVWLPVESRDVQVGANMSLGIRPEHLLPSDIADVILEGEVQVVEQLGNETQIHIQIPSIRQNLVYRQNDVVLVEEGATFAIGLPPERCHLFREDGT</span></span>
<span class="topo-ruler">       370       380 </span>
<span class="topo-line"><span class="topo-inside">ACRRLHKEPGVA</span><span class="topo-unknown">SASHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>2</td>
      <td>372</td>
      <td>2</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>373</td>
      <td>381</td>
      <td>373</td>
      <td>381</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2r6g">2R6G</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">ASVQLQNVTKAWGEVVVSKDINLDIHEGEFVVFVGPSGCGKSTLLRMIAGLETITSGDLFIGEKRMNDTPPAERGVGMVFQSYALYPHLSVAENMSFGLKLAGAKKEVINQRVNQVAEV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LQLAHLLDRKPKALSGGQRQRVAIGRTLVAEPSVFLLDQPLSNLDAALRVQMRIEISRLHKRLGRTMIYVTHDQVEAMTLADKIVVLDAGRVAQVGKPLELYHYPADRFVAGFIGSPKMN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">FLPVKVTATAIDQVQVELPMPNRQQVWLPVESRDVQVGANMSLGIRPEHLLPSDIADVILEGEVQVVEQLGNETQIHIQIPSIRQNLVYRQNDVVLVEEGATFAIGLPPERCHLFREDGT</span></span>
<span class="topo-ruler">       370       380 </span>
<span class="topo-line"><span class="topo-inside">ACRRLHKEPGVAS</span><span class="topo-unknown">ASHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>2</td>
      <td>373</td>
      <td>2</td>
      <td>373</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>381</td>
      <td>374</td>
      <td>381</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2r6g">2R6G</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">KIEEGKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWAHDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LLPNPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADGGYAFKYENGKYDIKDVGVDNAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NYGVTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVALKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEA</span></span>
<span class="topo-ruler">       370</span>
<span class="topo-line"><span class="topo-outside">LKDAQTRITK</span></span>
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
      <td>1</td>
      <td>370</td>
      <td>1</td>
      <td>370</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2r6g">2R6G</a> — Chain F (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDVIKKKHWWQS</span><span class="topo-inside">DALK</span><span class="topo-membrane">WSVLGLLGLLVGYLVV</span><span class="topo-outside">LMYAQGEYLFA</span><span class="topo-membrane">ITTLILSSAGLYIFANR</span><span class="topo-inside">KAYAW</span><span class="topo-membrane">RYVYPGMAGMGLFVLFPLV</span><span class="topo-outside">CTIAIAFTNYSSTNQLTFERAQEVLLDRSWQAGKTY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">NFGLYPAGDEWQLALSDGETGKNYLSDAFKFGGEQKLQLKETTAQPEGERANLRVITQNRQALSDITAILPDGNKVMMSSLRQFSGTQPLYTLDGDGTLTNNQSGVKYRPNNQIGFYQSI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TA</span><span class="topo-unknown">DG</span><span class="topo-outside">NWGDEKLSPGYTVTTGWKNFTRVFTDEGIQKPFLAIF</span><span class="topo-membrane">VWTVVFSLITVFLTVAVGMVLACLV</span><span class="topo-inside">QWEALRG</span><span class="topo-membrane">KAVYRVLLILPYAVPS</span><span class="topo-outside">FISILIFKGLFNQSFGEINMMLSALFGVKPA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">WFSDPTTAR</span><span class="topo-membrane">TMLIIVNTWLGYPYMMILCMGL</span><span class="topo-inside">LKAIPDDLYEASAMDGAGPFQNFFKITLPLLIKP</span><span class="topo-membrane">LTPLMIASFAFNFNN</span><span class="topo-outside">FVLIQLLTNGGPDRLGTTTPAGYTDLLVNYTYRIAFEGGG</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-outside">GQDFGLAAAIAT</span><span class="topo-membrane">LIFLLVGALAIV</span><span class="topo-unknown">NLKATRMKFD</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>16</td>
      <td>13</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>32</td>
      <td>17</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>43</td>
      <td>33</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>60</td>
      <td>44</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>65</td>
      <td>61</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>84</td>
      <td>66</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>242</td>
      <td>85</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>244</td>
      <td>243</td>
      <td>244</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>245</td>
      <td>281</td>
      <td>245</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>306</td>
      <td>282</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>313</td>
      <td>307</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>329</td>
      <td>314</td>
      <td>329</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>330</td>
      <td>369</td>
      <td>330</td>
      <td>369</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>391</td>
      <td>370</td>
      <td>391</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>392</td>
      <td>425</td>
      <td>392</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>440</td>
      <td>426</td>
      <td>440</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>441</td>
      <td>492</td>
      <td>441</td>
      <td>492</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>504</td>
      <td>493</td>
      <td>504</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>505</td>
      <td>514</td>
      <td>505</td>
      <td>514</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2r6g">2R6G</a> — Chain G (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAMVQP</span><span class="topo-inside">KSQKARLF</span><span class="topo-membrane">ITHLLLLLFIAAIMFPLL</span><span class="topo-outside">MVVAISLRQGNFATGSLIPEQISWDHWKLALGFSV</span><span class="topo-unknown">EQADGR</span><span class="topo-outside">ITPPPFPVLLWL</span><span class="topo-membrane">WNSVKVAGISAIGIVALSTTCA</span><span class="topo-inside">YAFARMRFP</span><span class="topo-membrane">GKAT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LLKGMLIFQMFPA</span><span class="topo-outside">VLSLVALYALFDRLGEYIPFIGLNTH</span><span class="topo-membrane">GGVIFAYLGGIALHVWTIK</span><span class="topo-inside">GYFETIDSSLEEAAALDGATPWQAFRLVLLPLSVP</span><span class="topo-membrane">ILAVVFILSFIAAITE</span><span class="topo-outside">VPVASLLLRDV</span></span>
<span class="topo-ruler">       250       260       270       280       290      </span>
<span class="topo-line"><span class="topo-outside">NSYTLAVGMQQYLNPQNYLWGDFAAAAV</span><span class="topo-membrane">MSALPITIVFLLAQRWL</span><span class="topo-inside">VNGLTAGGVKG</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>14</td>
      <td>7</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>15</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>67</td>
      <td>33</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>73</td>
      <td>68</td>
      <td>73</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>74</td>
      <td>85</td>
      <td>74</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>116</td>
      <td>108</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>159</td>
      <td>134</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>178</td>
      <td>160</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>213</td>
      <td>179</td>
      <td>213</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>229</td>
      <td>214</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>268</td>
      <td>230</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>285</td>
      <td>269</td>
      <td>285</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>296</td>
      <td>286</td>
      <td>296</td>
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

### P3 loop scoop mechanism

The periplasmic loop P3 of MalG inserts into the MBP sugar-binding cleft, physically dislodging the [Maltose](/xray-mp-wiki/reagents/additives/maltose/) molecule from the binding protein. This scoop mechanism ensures efficient transfer of sugar from MBP to the transmembrane subunits. A mutant with a 31-residue insertion in this loop was defective in transport but retained the ability to assemble a MalFGK2 complex. This insertion mechanism was also observed in the BtuCD-F structure.

### C-terminal tail interaction with MalK

Residues 290-296 of MalG pack along the Q loop (residues 83-89) of one [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) monomer, with the terminal carboxyl group of MalG making three hydrogen bonds with backbone atoms of the Q loop in the other monomer (residues S83, A85 and L86). Although not required for closure of the isolated [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) dimer, the coupling between [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) monomers by MalG contributes to Q loop ordering and may be important in forming the catalytic intermediate conformation.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/">Maltose Transporter (MalFGK2)</a> — Full transporter complex; EIIA^Glc binding structure solved in this paper
- <a href="/xray-mp-wiki/proteins/abc-transporters/malF/">MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)</a> — Partner transmembrane subunit; forms the TM cavity with MalG
- <a href="/xray-mp-wiki/proteins/abc-transporters/malK/">MalK (Escherichia coli Maltose Transporter ATPase Subunit)</a> — Cytoplasmic ATP-binding subunit; C-terminal tail of MalG inserts into MalK dimer
- <a href="/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/">MBP (Escherichia coli Maltose-Binding Protein)</a> — Periplasmic binding protein; MalG P3 loop inserts into MBP cleft
- <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> — Substrate transferred from MBP to MalG via scoop mechanism
- <a href="/xray-mp-wiki/reagents/ligands/atp/">Adenosine Triphosphate (ATP)</a> — Energy source; binds to MalK dimer interface
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for membrane solubilization and purification
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — ABC transporter transport mechanism described in this paper
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Phasing method used to solve the structure
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
