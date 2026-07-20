---
title: "EIIA^Glc (Escherichia coli Enzyme IIA^Glc)"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12232]
verified: agent
uniprot_id: ['P02916', 'P68183', 'P68187', 'P69783']
---

# EIIA^Glc (Escherichia coli Enzyme IIA^Glc)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P02916">UniProt: P02916</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P68183">UniProt: P68183</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P68187">UniProt: P68187</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P69783">UniProt: P69783</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

EIIA^Glc (Enzyme IIA^Glc) is a central signaling protein in the Escherichia coli phosphotransferase system (PTS) that mediates carbon catabolite repression. It is a 168-residue protein that exists in a phosphorylated and unphosphorylated form depending on cellular carbon source availability. Unphosphorylated EIIA^Glc directly binds to and inhibits several non-PTS sugar transporters including the maltose transporter (MalFGK2), lactose permease (LacY), [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose) permease (MelB), and raffinose permease (RafB). The N-terminal 18 residues are disordered in the crystal structure but function as a membrane anchor. The phosphorylation site His90 lies at a canonical surface that also interacts with glycerol kinase, HPr, and EIIB^Glc.


## Publications

### doi/10.1038##nature12232

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4jbw">4JBW</a></td>
      <td>3.9</td>
      <td>not specified</td>
      <td>EIIA^Glc residues 19-168 (N-terminal 18 residues disordered) in complex with MalFGK2</td>
      <td>MalFGK2 (<a href="/xray-mp-wiki/reagents/additives/maltose">Maltose</a> transporter, ABC transporter)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1f3g">1F3G</a></td>
      <td>not specified</td>
      <td>not specified</td>
      <td>Free EIIA^Glc (used as search model for <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a>)</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 (DE3) Star
- **Construct**: Full-length EIIA^Glc or Delta(1-18) truncation mutant; N-terminal 10x-His tag with [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease) cleavage site

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
      <td>Luria-Bertani medium + --</td>
      <td>Grown at 37 C until D600nm = 0.6-0.8, induced with 100 uM <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG (Isopropyl-beta-D-thiogalactopyranoside)</a> at 16 C for 20 h</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>Cobalt-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>Cobalt-affinity resin (Clontech)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + --</td>
      <td>Ni2+-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography">IMAC</a> for His-tagged EIIA^Glc</td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV Protease</a> cleavage</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + --</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV Protease</a> removes N-terminal 10x-His tag</td>
    </tr>
    <tr>
      <td>Ion-exchange chromatography</td>
      <td>Ion-exchange chromatography</td>
      <td>Source 15Q (GE Healthcare)</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8.0, 200 mM NaCl + --</td>
      <td>FPLC purification</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) (SEC)</td>
      <td>Superdex 75 (GE Healthcare)</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8.0, 200 mM NaCl + --</td>
      <td>Final polishing step</td>
    </tr>
  </tbody>
</table>
**Final sample**: Not specified
**Yield**: Not specified

**Crystallization:**


<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4jbw">4JBW</a> — Chain F (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDVIKKKHWWQSDALKW</span><span class="topo-outside">S</span><span class="topo-membrane">VLGLLGLLVGYLVVLMY</span><span class="topo-inside">AQGEY</span><span class="topo-membrane">LFAITTLILSSAGLYIFA</span><span class="topo-outside">NRKAYAWRYV</span><span class="topo-membrane">YPGMAGMGLFVLFPLVCTIA</span><span class="topo-inside">IAFTNYSSTNQLTFERAQEVLLDRSWQAGKTY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NFGLYPAGDEWQLALSDGETGKNYLSDAFKFGGEQKLQLKETTAQPEGERANLRVITQNRQALSDITAILPDGNKVMMSSLRQFSGTQPLYTLDGDGTLTNNQSGVKYRPNNQIGFYQSI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">TADGNWGDEKLSPGYTVTTGW</span><span class="topo-unknown">KNFTRVF</span><span class="topo-inside">TDEGIQKPFLAI</span><span class="topo-membrane">FVWTVVFSLITVFLTVAVGMVLA</span><span class="topo-outside">CLVQWEALRGKAV</span><span class="topo-membrane">YRVLLILPYAVPSFISILIF</span><span class="topo-inside">KGLFNQSFGE</span><span class="topo-unknown">INMMLSA</span><span class="topo-inside">LFGVKPA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">WFSDPTTAR</span><span class="topo-membrane">TMLIIVNTWLGYPYMMILC</span><span class="topo-outside">MGLLKAIPDDLYEASAMDGAG</span><span class="topo-unknown">PFQNFFK</span><span class="topo-outside">I</span><span class="topo-unknown">TLPLLIKPLT</span><span class="topo-membrane">PLMIASFAFNFNNFVLI</span><span class="topo-inside">QLLTNGGPDRLGTTTPAGYTDLLVNYTYRIAFEGGG</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-inside">GQDFGLAA</span><span class="topo-membrane">AIATLIFLLVGALAIVNL</span><span class="topo-outside">KAT</span><span class="topo-unknown">RMKFD</span></span>
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
      <td>17</td>
      <td>1</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>18</td>
      <td>18</td>
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
      <td>40</td>
      <td>36</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>58</td>
      <td>41</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>68</td>
      <td>59</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>88</td>
      <td>69</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>261</td>
      <td>89</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>268</td>
      <td>262</td>
      <td>268</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>269</td>
      <td>280</td>
      <td>269</td>
      <td>280</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>303</td>
      <td>281</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>316</td>
      <td>304</td>
      <td>316</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>336</td>
      <td>317</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>346</td>
      <td>337</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>353</td>
      <td>347</td>
      <td>353</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>354</td>
      <td>369</td>
      <td>354</td>
      <td>369</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>388</td>
      <td>370</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>409</td>
      <td>389</td>
      <td>409</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>416</td>
      <td>410</td>
      <td>416</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>417</td>
      <td>417</td>
      <td>417</td>
      <td>417</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>418</td>
      <td>427</td>
      <td>418</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>444</td>
      <td>428</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>488</td>
      <td>445</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>506</td>
      <td>489</td>
      <td>506</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>507</td>
      <td>509</td>
      <td>507</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>514</td>
      <td>510</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4jbw">4JBW</a> — Chain G (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AMVQPKSQKARLFI</span><span class="topo-membrane">THLLLLLFIAAIMFPLLMVVA</span><span class="topo-inside">ISLRQGNFATGSLIPEQISW</span><span class="topo-unknown">DHWKLAL</span><span class="topo-inside">GFSVEQADGRITPPPFPVLLWL</span><span class="topo-membrane">WNSVKVAGISAIGIVALSTTC</span><span class="topo-outside">AYAFARMRFPGKAT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">L</span><span class="topo-membrane">LKGMLIFQMFPAVLSL</span><span class="topo-unknown">VALYALFDRLGEY</span><span class="topo-inside">IPFIGLNTH</span><span class="topo-membrane">GGVIFAYLGGIALHVWT</span><span class="topo-outside">IKGYFETIDSSLEEAAALDGAT</span><span class="topo-unknown">PWQAFRL</span><span class="topo-outside">VLLPLSVPIL</span><span class="topo-membrane">AVVFILSFIAAITEVPVA</span><span class="topo-inside">SLLLRDV</span></span>
<span class="topo-ruler">       250       260       270       280       290      </span>
<span class="topo-line"><span class="topo-inside">NSYTLAVGMQQYLNPQNYLWGDFAA</span><span class="topo-membrane">AAVMSALPITIVFLLAQRW</span><span class="topo-outside">LVN</span><span class="topo-unknown">GLTAGGVKG</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>15</td>
      <td>2</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>36</td>
      <td>16</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>56</td>
      <td>37</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>63</td>
      <td>57</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>64</td>
      <td>85</td>
      <td>64</td>
      <td>85</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>106</td>
      <td>86</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>121</td>
      <td>107</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>137</td>
      <td>122</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>150</td>
      <td>138</td>
      <td>150</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>151</td>
      <td>159</td>
      <td>151</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>176</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>198</td>
      <td>177</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>205</td>
      <td>199</td>
      <td>205</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>206</td>
      <td>215</td>
      <td>206</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>233</td>
      <td>216</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>265</td>
      <td>234</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>284</td>
      <td>266</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>287</td>
      <td>285</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>296</td>
      <td>288</td>
      <td>296</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4jbw">4JBW</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ASVQLQNVTKAWGEVVVSKDINLDIHEGEFVVFVGPSGCGKSTLLRMIAGLETITSGDLFIGEKRMNDTPPAERGVGMVFQSYALYPHLSVAENMSFGLKLAGAKKEVINQRVNQVAEV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LQLAHLLDRKPKALSGGQRQRVAIGRTLVAEPSVFLLDEPLSNLDAALRVQMRIEISRLHKRLGRTMIYVTHDQVEAMTLADKIVVLDAGRVAQVGKPLELYHYPADRFVAGFIGSPKMN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">FLPVKVTATAIDQVQVELPMPNRQQVWLPVESRDVQVGANMSLGIRPEHLLPSDIADVILEGEVQVVEQLGNETQIHIQIPSIRQNLVYRQNDVVLVEEGATFAIGLPPERCHLFREDGT</span></span>
<span class="topo-ruler">       370       380 </span>
<span class="topo-line"><span class="topo-outside">ACRRLHKEPGV</span><span class="topo-unknown">ASASHHHHHH</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>371</td>
      <td>2</td>
      <td>371</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>381</td>
      <td>372</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4jbw">4JBW</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ASVQLQNVTKAWGEVVVSKDINLDIHEGEFVVFVGPSGCGKSTLLRMIAGLETITSGDLFIGEKRMNDTPPAERGVGMVFQSYALYPHLSVAENMSFGLKLAGAKKEVINQRVNQVAEV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LQLAHLLDRKPKALSGGQRQRVAIGRTLVAEPSVFLLDEPLSNLDAALRVQMRIEISRLHKRLGRTMIYVTHDQVEAMTLADKIVVLDAGRVAQVGKPLELYHYPADRFVAGFIGSPKMN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">FLPVKVTATAIDQVQVELPMPNRQQVWLPVESRDVQVGANMSLGIRPEHLLPSDIADVILEGEVQVVEQLGNETQIHIQIPSIRQNLVYRQNDVVLVEEGATFAIGLPPERCHLFREDGT</span></span>
<span class="topo-ruler">       370       380 </span>
<span class="topo-line"><span class="topo-outside">ACRRLHKEPGV</span><span class="topo-unknown">ASASHHHHHH</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>371</td>
      <td>2</td>
      <td>371</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>381</td>
      <td>372</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4jbw">4JBW</a> — Chain M (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SNAMGLFDKLKSLVSDDKKDTG</span><span class="topo-outside">TIEIIAPLSGEIVNIEDVPDVVFAEKIVGDGIAIKPTGNKMVAPVDGTIGKIFETNHAFSIESDSGVELFVHFGIDTVELKGEGFKRIAEEGQRVKVG</span></span>
<span class="topo-ruler">       130       140       150       160       170  </span>
<span class="topo-line"><span class="topo-outside">DTVIEFDLPLLEEKAKSTLTPVVISNMDEIKELIKLSGSVTVGETPVIRIKK</span></span>
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
      <td>1</td>
      <td>22</td>
      <td>-3</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>172</td>
      <td>19</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4jbw">4JBW</a> — Chain N (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SNAMGLFDKLKSLVSDDKKDTG</span><span class="topo-outside">TIEIIAPLSGEIVNIEDVPDVVFAEKIVGDGIAIKPTGNKMVAPVDGTIGKIFETNHAFSIESDSGVELFVHFGIDTVELKGEGFKRIAEEGQRVKVG</span></span>
<span class="topo-ruler">       130       140       150       160       170  </span>
<span class="topo-line"><span class="topo-outside">DTVIEFDLPLLEEKAKSTLTPVVISNMDEIKELIKLSGSVTVGETPVIRIKK</span></span>
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
      <td>1</td>
      <td>22</td>
      <td>-3</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>172</td>
      <td>19</td>
      <td>168</td>
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

### Allosteric inhibition of maltose transporter

Two EIIA^Glc molecules bind to the cytoplasmic ATPase subunits (MalK) of the [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter, stabilizing it in an inward-facing conformation and preventing the structural rearrangements necessary for ATP hydrolysis. Each EIIA^Glc is wedged between the NBD of one MalK and the regulatory domain of the opposite MalK, linking these two domains together. Of the 1,500 A^2 buried surface area on EIIA^Glc, approximately 55% is buried at the NBD interface and 45% at the regulatory domain interface. EIIA^Glc is a classical Monod-Wyman-Changeux allosteric inhibitor of the maltose transporter.

### Canonical binding surface with promiscuous interactions

The NBD of MalK binds to a canonical surface of EIIA^Glc that also interacts with [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) kinase, EIIB^Glc, and histidine protein (HPr). Of the 17 residues making contacts with the NBD, 11 are shared with these other partners (Val 39, Val 40, Phe 41, Ile 45, Val 46, Lys 69, Phe 71, Glu 72, Phe 88, His 90, and Val 96). Most interface residues are hydrophobic, consistent with the promiscuous interactions this surface makes with different proteins.

### Phosphorylation prevents transporter binding

The phosphorylation site His90 is located at the EIIA^Glc-MalK interface and is in its unphosphorylated form, hydrogen bonded with Gln122 of MalK. Adding a negatively charged phosphate group to the side chain of His90 would disrupt the interface, thus relieving the [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter from inducer exclusion.

### N-terminal membrane anchor function

The N-terminal 18 residues are disordered in the crystal structure. Studies of synthetic peptides showed that residues 3-10 form an amphipathic helix in the presence of detergent micelles or lipid vesicles, functioning as a membrane anchor. The first ordered residue Thr19 is approximately 20 A outside the lipid bilayer. The IC50 of full-length EIIA^Glc (1.61 uM) differs by 60-fold from the Delta(1-18) [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation) mutant (91 uM), consistent with the N-terminal region increasing the effective EIIA^Glc concentration at the membrane.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/">Maltose Transporter (MalFGK2)</a> — Primary target of EIIA^Glc inhibition; complex structure solved in this paper
- <a href="/xray-mp-wiki/proteins/abc-transporters/malK/">MalK (Escherichia coli Maltose Transporter ATPase Subunit)</a> — EIIA^Glc binds to [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK) NBD and regulatory domain interfaces
- <a href="/xray-mp-wiki/proteins/abc-transporters/malF/">MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)</a> — TM subunit of the [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter complex
- <a href="/xray-mp-wiki/proteins/abc-transporters/malG/">MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)</a> — TM subunit of the [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter complex
- <a href="/xray-mp-wiki/concepts/miscellaneous/carbon-catabolite-repression/">Carbon Catabolite Repression</a> — EIIA^Glc is the key regulatory protein in CCR in E. coli
- <a href="/xray-mp-wiki/concepts/miscellaneous/inducer-exclusion/">Inducer Exclusion</a> — Mechanism by which EIIA^Glc inhibits sugar transporters
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used in MalFGK2 purification for complex formation
- <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC (1,2-Dimyristoyl-sn-glycero-3-phosphocholine)</a> — Lipid component of bicelles used for complex crystallization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Immobilized Metal Affinity Chromatography (IMAC)</a> — Purification method used in protein preparation
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography (SEC)</a> — Purification method used in protein preparation
