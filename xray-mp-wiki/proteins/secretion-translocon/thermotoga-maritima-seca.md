---
title: "Thermotoga maritima SecA ATPase"
created: 2026-06-09
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature07335]
verified: regex
uniprot_id: ['B1L914', 'P35874', 'Q9X1I9', 'Q9X1R4']
---

# Thermotoga maritima SecA ATPase

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/B1L914">UniProt: B1L914</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P35874">UniProt: P35874</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9X1I9">UniProt: Q9X1I9</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9X1R4">UniProt: Q9X1R4</a>

<span class="expr-badge">Thermotoga maritima MSB8</span>

## Overview

SecA is the cytoplasmic ATPase motor of the bacterial Sec protein translocation machinery that drives post-translational secretion of proteins across the plasma membrane and membrane protein integration. The crystal structure of Thermotoga maritima SecA bound to the [SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) translocon complex (PDB 3DIN, 4.5 A resolution) revealed the conformational changes that occur upon [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) binding and provided mechanistic insights into how ATP hydrolysis drives polypeptide movement. SecA comprises two RecA-like nucleotide-binding domains (NBD1 and NBD2), a polypeptide-cross-linking domain (PPXD), a helical scaffold domain (HSD) with a two-helix finger, and a helical wing domain (HWD). Upon binding to the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) channel, the PPXD undergoes an ~80 degree rigid-body rotation to form a clamp over the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) pore, and the two-helix finger inserts into the cytoplasmic funnel of [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) to push polypeptides through the channel.

## Publications

### doi/10.1038##nature07335

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3din">3DIN</a></td>
      <td>4.5 A</td>
      <td>not specified</td>
      <td>Thermotoga maritima SecA (residues 1-816) with C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a>, bound to T. maritima <a href="/xray-mp-wiki/proteins/secretion-translocon/secyeg/">SECYEG</a> complex; ADP-<a href="/xray-mp-wiki/reagents/ligands/bef3/">BeF3 (Beryllium Fluoride)</a> bound</td>
      <td>ADP-<a href="/xray-mp-wiki/reagents/ligands/bef3/">BeF3 (Beryllium Fluoride)</a> (transition state analog); beta-D-Octylglucoside (OG)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: T. maritima SecA (residues 1-816) with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) under IPTG-inducible promoter

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
      <td>Microfluidizer</td>
      <td>--</td>
      <td>20 mM Tris pH 7.5, 1 M NaCl, 1 mM TCEP (HS buffer) + --</td>
      <td>Centrifuged 30 min at 205,000g at 4 C</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (His-tag)</td>
      <td>Ni-NTA Sepharose (Qiagen)</td>
      <td>HS buffer with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + --</td>
      <td>Washed with 200 ml HS buffer + 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, then 200 ml HS buffer + 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 6 M guanidine-HCl</td>
    </tr>
    <tr>
      <td>Elution and refolding</td>
      <td>Affinity elution with dialysis refolding</td>
      <td>--</td>
      <td>D buffer (20 mM Tris pH 7.5, 0.5 M NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>) + --</td>
      <td>Eluted in 50 ml HS buffer + 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 6 M guanidine-HCl; refolded by dialysis against D buffer overnight at 4 C</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td>Superdex S200 (GE Healthcare)</td>
      <td>D buffer + --</td>
      <td>Fractions lacking 30 kDa proteolytic fragment pooled and concentrated to 100 uM</td>
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
      <td>SecA-<a href="/xray-mp-wiki/proteins/secretion-translocon/secyeg/">SECYEG</a> complex formed at 1:1.2 molar ratio, dialyzed against buffer containing 20 mM MES pH 6.5, 0.1 M NaCl, 10 mM MgCl2, 1 mM ADP, 2 mM BeCl2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in presence of ADP-BeFx corresponding to intermediate state during ATP hydrolysis. Data collected at synchrotron beamlines ID-19 and 24ID at Argonne National Laboratory and X29 at Brookhaven National Laboratory. <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> used B. subtilis SecA as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3din">3DIN</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MILFDKNKRILKKYAKMVSKINQIESDLRSKKNSELIRLSMVLKEKVNSFEDADEHLFEAFALVREAARRTLGMRPFDVQVMGGIALHEGKVAEMKTGEGKTLAATMPIYLNALIGKGVH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LVTVNDYLARRDALWMGPVYLFLGLRVGVINSLGKSYEVVWKNPDLARKAIEENWSVWPDGFNGEVLKEESMNKEAVEAFQVELKEITRKEAYLCDVTYGTNNEFGFDYLRDNLVLDYND</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KVQRGHFYAIVDEADSVLIDEARTPLIISGPSKESPSVYRRFAQIAKKFVKDKDFTVDEKARTIILTEEGVAKAEKIIGVENLYDPGNVSLLYHLINALKALHLFKKDVDYVVMNGEVII</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VDEFTGRLLPGRRYSGGLHQAIEAKEGVPIKEESITYATITFQNYFRMYEKLAGMTGTAKTEESEFVQVYGMEVVVIPTHKPMIRKDHDDLVFRTQKEKYEKIVEEIEKRYKKGQPVLVG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">TTSIEKSELLSSMLKKKGIPHQVLNAKYHEKEAEIVAKAGQKGMVTIATNMAGRGTDIKLGPGVAELGGLCIIGTERHESRRIDNQLRGRAGRQGDPGESIFFLSLEDDLLRIFGSEQIG</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">KVMNILKIEEGQPIQHPMLSKLIENIQKKVEGINFSIRKTLMEMDDVLDKQRRAVYSLRDQILLEKDYDEYLKDIFEDVVSTRVEEFCSGKNWDIESLKNSLSFFPAGLFDLDEKQFSSS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">EELHDYLFNRLWEEYQRKKQEIGEDYRKVIRFLMLRIIDDHWRRYLEEVEHVKEAVQLRSYGQKDPIVEFKKETYYMFDEMMRRINDTIANYVLRV</span><span class="topo-unknown">VKVSEKDEKEAKEELGKIRLVHEE</span></span>
<span class="topo-ruler">       850       860       870 </span>
<span class="topo-line"><span class="topo-unknown">FNLVNRAMRRATEKKKKKDGLHSFGRIRVKR</span></span>
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
      <td>816</td>
      <td>1</td>
      <td>816</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>817</td>
      <td>871</td>
      <td>817</td>
      <td>871</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3din">3DIN</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MWQAFKN</span><span class="topo-inside">AFKIPELRDR</span><span class="topo-membrane">IIFTFLALIVFRMGI</span><span class="topo-outside">YIPVPGLNL</span><span class="topo-unknown">EAWGEIFRRIAETAGVAGIL</span><span class="topo-outside">SFYDVFTGGALS</span><span class="topo-membrane">RFSVFTMSVTPYITASIILQLL</span><span class="topo-inside">ASVMPSLKEMLREGEEGRKKFAKYT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RRLTLLIGGFQAF</span><span class="topo-outside">FVSFSLARSNPDMVAPGVNVLQFTVLST</span><span class="topo-membrane">MSMLAGTMFLLWLGERI</span><span class="topo-inside">TEKG</span><span class="topo-membrane">IGNGISILIFAGIVAR</span><span class="topo-outside">YPSYIRQAYLGGLNL</span><span class="topo-membrane">LEWIFLIAVALIT</span><span class="topo-inside">IFGIILVQQAERRI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">TIQYARRVTGRRVYGGASTYLPIKVNQGGV</span><span class="topo-membrane">IPIIFASAIVSIP</span><span class="topo-outside">SAIASITNNETLKNLFRAG</span><span class="topo-membrane">GFLYLLIYGLLVF</span><span class="topo-inside">FFTYFYSVVIFDPREISENIRKYGGYIPGLRPGRSTEQYLHRVLN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430 </span>
<span class="topo-line"><span class="topo-inside">RVTFIGA</span><span class="topo-membrane">VFLVVIALLPYLVQG</span><span class="topo-outside">AIKVNVW</span><span class="topo-membrane">IGGTSALIAVGVAL</span><span class="topo-inside">DIIQQMETHMVMRHYEGFIK</span><span class="topo-unknown">KGKIRGRR</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>17</td>
      <td>8</td>
      <td>17</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>32</td>
      <td>18</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>61</td>
      <td>42</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>62</td>
      <td>73</td>
      <td>62</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>95</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>120</td>
      <td>96</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>133</td>
      <td>121</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>161</td>
      <td>134</td>
      <td>161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>178</td>
      <td>162</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>182</td>
      <td>179</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>198</td>
      <td>183</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>213</td>
      <td>199</td>
      <td>213</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>226</td>
      <td>214</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>270</td>
      <td>227</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>283</td>
      <td>271</td>
      <td>283</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>284</td>
      <td>302</td>
      <td>284</td>
      <td>302</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>303</td>
      <td>315</td>
      <td>303</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>367</td>
      <td>316</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>382</td>
      <td>368</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>389</td>
      <td>383</td>
      <td>389</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>403</td>
      <td>390</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>404</td>
      <td>423</td>
      <td>404</td>
      <td>423</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>424</td>
      <td>431</td>
      <td>424</td>
      <td>431</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3din">3DIN</a> — Chain D (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MEKLRKFFR</span><span class="topo-inside">E</span><span class="topo-unknown">VIAEAKKISWPS</span><span class="topo-inside">RKELLTSFGVVL</span><span class="topo-membrane">VILAVTSVYFFVLDFIF</span><span class="topo-outside">SGVVSAIFKALGIG</span></span>
<details class="topo-details"><summary>Topology coordinates (6 regions)</summary>
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
      <td>9</td>
      <td>1</td>
      <td>9</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>22</td>
      <td>11</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>34</td>
      <td>23</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>51</td>
      <td>35</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>65</td>
      <td>52</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3din">3DIN</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70      </span>
<span class="topo-line"><span class="topo-unknown">MKTFFLIV</span><span class="topo-outside">HTIISV</span><span class="topo-membrane">ALIYMVQVQMSKFSE</span><span class="topo-inside">LGGAFGSGGLHTVFGRRKGLDTGG</span><span class="topo-membrane">KITLVLSVLFFVS</span><span class="topo-outside">CVVTAFV</span><span class="topo-unknown">LTR</span></span>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>14</td>
      <td>9</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>29</td>
      <td>15</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>53</td>
      <td>30</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>66</td>
      <td>54</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>73</td>
      <td>67</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>76</td>
      <td>74</td>
      <td>76</td>
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

### SecA undergoes large conformational changes upon SecY binding

When SecA binds to the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) complex, the PPXD rotates by ~80 degrees towards NBD2 as a rigid body with a ~10 degree tilt towards the membrane, with the hinge formed by two short beta-strands connecting PPXD and NBD1. The closed clamp formed by PPXD, NBD2, and HSD positions the polypeptide chain right above the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) pore. An evolutionarily conserved loop in PPXD (residues 360-370) contacts both NBD1 and NBD2 near the nucleotide-binding site.

### Two-helix finger mechanism for polypeptide translocation

A two-helix finger of the HSD inserts into the cytoplasmic funnel of [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/), with the loop connecting the two helices located right above the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) pore entrance. The finger has an ~45 degree angle relative to the membrane plane and rests in a cleft between the 6-7 loop and C-terminal tail of [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/). The two-helix finger is proposed to move up and down during the ATP hydrolysis cycle, pushing the polypeptide chain into the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) pore.

### SecA binding induces SecY lateral gate opening

SecA binding generates a window at the lateral gate of [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) formed by TM2b, TM3, TM7, and TM8. The displacement of TM7 opens a ~5 A gap between TM7 and TM2b towards the centre of the lipid bilayer. The plug helix (TM2a) moves away from the centre of the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) channel towards the external side, preparing the channel for signal sequence binding and opening.


## Cross-References

- <a href="/xray-mp-wiki/proteins/secretion-translocon/secyeg/">Thermus thermophilus SecYEG Translocon Complex</a> — SecA binding partner; translocon complex that forms the protein-conducting channel
- <a href="/xray-mp-wiki/proteins/secretion-translocon/secy/">Thermus thermophilus SecY Core Channel Subunit</a> — SecA interacts with the SecY pore ring and lateral gate during translocation
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/ligands/bef3/">BeF3 (Beryllium Fluoride)</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a> — Fusion tag for crystallization or purification
