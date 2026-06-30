---
title: "MBP (Escherichia coli Maltose-Binding Protein)"
created: 2026-06-02
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature06264]
verified: false
---

# MBP (Escherichia coli Maltose-Binding Protein)

## Overview

MBP (maltose-binding protein) is the periplasmic binding protein component of
the Escherichia coli maltose uptake system, an ATP-binding cassette (ABC)
importer. MBP binds maltose and malto-oligosaccharides (up to 7 glucose units)
with high affinity in a cleft between two lobes that completely engulf the
substrate upon lobe rotation. MBP docks onto the transmembrane subunits
[MalF](/xray-mp-wiki/proteins/abc-transporters/malF/) and [MalG](/xray-mp-wiki/proteins/abc-transporters/malG/),
delivering the substrate and stimulating ATP hydrolysis. In the maltose
transporter complex, MBP remains in its open, ligand-free conformation,
stabilized by interactions with the TM subunits, which promotes sugar release
and ensures unidirectional translocation. Crystal structures of MBP bound to
maltoheptaose show the first four glucosyl units from the reducing end (g1-g4)
bound in the MBP binding groove through 14 direct hydrogen bonds and 118 van
der Waals interactions with a continuous surface of four stacking aromatic
residues.


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
      <td>—</td>
      <td>Open apo conformation of MBP from E. coli maltose transporter</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1omp">1OMP</a></td>
      <td></td>
      <td>—</td>
      <td>Open apo MBP (search model for molecular replacement)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1jw5">1JW5</a></td>
      <td></td>
      <td>—</td>
      <td></td>
      <td>maltose</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BAR1000
- **Construct**: MBP under mal promoter; increased expression strain
- **Notes**: Cells cultured overnight with maltose induction

**Purification:**

- **Expression system**: E. coli BAR1000
- **Expression construct**: MBP under mal promoter

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
      <td>—</td>
      <td>Luria-Bertani medium supplemented with 4 g/L maltose</td>
      <td>Cells cultured overnight with maltose induction</td>
    </tr>
    <tr>
      <td>Osmotic shock</td>
      <td>Osmotic shock</td>
      <td>—</td>
      <td>30 mM Tris-HCl pH 8, 20% sucrose; then ice-cold 5 mM MgSO4</td>
      <td>Cells resuspended in sucrose buffer, centrifuged, then resuspended in MgSO4 to release periplasmic MBP</td>
    </tr>
    <tr>
      <td>Ion-exchange chromatography</td>
      <td>Ion-exchange chromatography</td>
      <td>Source 15Q (GE Healthcare)</td>
      <td>20 mM Tris-HCl pH 8</td>
      <td>FPLC (AKTA) at 4 C</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>Superdex 200 (GE Healthcare)</td>
      <td>20 mM Tris-HCl pH 8</td>
      <td>FPLC (AKTA) at 4 C</td>
    </tr>
  </tbody>
</table>
**Final sample**: 1 mg/mL in 20 mM Tris-HCl pH 8

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

### Open apo conformation in the transporter complex

MBP docks onto MalF and MalG in an open, ligand-free conformation at the periplasmic surface. The open form has lower affinity for maltose because it makes fewer contacts than the closed form. Interactions with the TM subunits stabilize MBP in the open state, presumably to promote sugar release. The absence of maltose electron density in the MBP binding site demonstrates that maltose has been translocated to the TM subunits. This is a key feature of the catalytic intermediate state.

### MBP as a cap for unidirectional transport

MBP serves as a cap at the periplasmic entrance of the translocation cavity, ensuring unidirectional translocation of the sugar molecule. Two notable interactions include the insertion of the MalG periplasmic loop (P3) into the MBP sugar-binding cleft and contacts by mostly the N-lobe of MBP with a large periplasmic loop (P2) of MalF that folds into an Ig-like domain and extends about 30 A away from the membrane surface. MBP also stimulates ATP hydrolysis, ensuring that substrate is transported during each cycle.

### Maltose scoop mechanism by MalG P3 loop

Insertion of the MalG P3 loop into the MBP sugar-binding site physically dislodges the sugar from the binding protein. Modeling a sugar molecule into the binding site based on the open maltose-bound MBP structure (1JW5) shows that even the smallest substrate, maltose, clashes with the P3 loop. This scoop mechanism ensures efficient transfer of substrate from MBP to the transmembrane subunits.

### MBP binding of maltoheptaose and interaction with MalG

In the pretranslocation state bound with maltoheptaose, the first four glucosyl units from the reducing end (g1-g4) are bound in the MBP binding groove. The maltoheptaose forms 14 direct hydrogen bonds with polar residues and 118 van der Waals interactions with MBP. Four stacking aromatic residues form a continuous surface matching the curvature of the left-handed helix of the malto-oligosaccharide. The MalG scoop loop reaches to the reducing end via conserved Q256, which hydrogen bonds to OH6 and ring oxygen of the g1 unit.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/">Maltose Transporter MalFGK2 (E. coli)</a> — MBP delivers substrate to the MalFGK2 ABC transporter complex
- <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> — Physiological substrate; binds in MBP cleft
- <a href="/xray-mp-wiki/reagents/ligands/atp/">Adenosine Triphosphate (ATP)</a> — MBP stimulates ATP hydrolysis upon delivering substrate to TM subunits
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer used for MBP purification and storage
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — ABC transporter transport mechanism
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — MBP structure (1OMP) used as search model for phasing
