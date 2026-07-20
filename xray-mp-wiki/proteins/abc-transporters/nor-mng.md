---
title: "NorM-NG (Neisseria gonorrhoeae NorM) - MATE Family Na+-Coupled Transporter"
created: 2026-06-05
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11403, doi/10.1038##ncomms8995, doi/10.1073##pnas.1219901110]
verified: agent
uniprot_id: ['E8SM44', 'M1E1G6', 'Q5F9J8']
---

# NorM-NG (Neisseria gonorrhoeae NorM) - MATE Family Na+-Coupled Transporter

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/E8SM44">UniProt: E8SM44</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/M1E1G6">UniProt: M1E1G6</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5F9J8">UniProt: Q5F9J8</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

NorM-NG is a multidrug and toxic compound extrusion (MATE) family transporter from Neisseria gonorrhoeae that functions as a Na+-coupled multidrug efflux pump. It belongs to the NorM subfamily of MATE transporters and exports a broad range of organic cations including ethidium bromide, [Doxorubicin - Anthracycline Anticancer Drug](/xray-mp-wiki/reagents/ligands/doxorubicin), and rhodamine 6G. NorM-NG features the characteristic bilobate 12-transmembrane-helix architecture of the MATE family with pseudo-symmetric N- and C-lobes (TM1-6 and TM7-12), residues 5-230 and 231-459 respectively. In the [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil)-bound structure, NorM-NG undergoes pronounced conformational changes in two extracellular loops (L3-4 and L9-10) that cap the multidrug-binding cavity. Crystal structures of NorM-NG in complexes with three distinct translocation substrates (ethidium, rhodamine 6G, and tetraphenylphosphonium) and Cs+ (a Na+ congener) revealed an extracellular-facing, drug-bound state with a multidrug-binding cavity lined by four negatively charged amino acids and surprisingly limited hydrophobic moieties. An uncommon cation-pi interaction between Na+ and Y294 was identified in the Na+-binding site located outside the drug-binding cavity.


## Publications

### doi/10.1038##nature11403

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4doj">4DOJ</a></td>
      <td>3.0</td>
      <td>P 212121</td>
      <td>NorM-NG wild type, residues 5-459</td>
      <td>Rhodamine 6G (R6G)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with membrane protein expression vectors
- **Construct**: [IPTG](/xray-mp-wiki/reagents/additives/iptg) induction at 37 C for 3 h

### doi/10.1038##ncomms8995

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5c6p">5C6P</a></td>
      <td>3.0</td>
      <td>P 212121</td>
      <td>NorM-NG wild type, residues 5-459</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/verapamil">Verapamil</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with membrane protein expression vectors
- **Construct**: [IPTG](/xray-mp-wiki/reagents/additives/iptg) induction at 37 C for 3 h

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
      <td>Cell growth and induction</td>
      <td>E. coli BL21(DE3) in LB media to OD600 = 0.5; induced with 0.5 mM <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a> at 37 C for 3 h</td>
      <td>--</td>
      <td>LB media + --</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Multiple passages through pre-cooled microfluidizer</td>
      <td>--</td>
      <td>-- + --</td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Ultracentrifugation for membrane collection; extracted with 1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>-NaOH pH 7.5, 100 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> (Anatrace)</td>
      <td></td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin; eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>-NaOH pH 7.5, 100 mM NaCl, 25% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Thrombin cleavage</td>
      <td>Incubated with thrombin protease overnight</td>
      <td>--</td>
      <td>-- + --</td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>-NaOH pH 7.5, 100 mM NaCl, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Co-crystallization with <a href="/xray-mp-wiki/reagents/ligands/verapamil">Verapamil</a>; hanging-drop vapor diffusion at 22 C</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NorM-NG incubated with <a href="/xray-mp-wiki/reagents/ligands/verapamil">Verapamil</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Phasing by molecular replacement and <a href="/xray-mp-wiki/methods/structure-determination/miras">MIRAS</a>; <a href="/xray-mp-wiki/reagents/ligands/verapamil">Verapamil</a>-bound structure differs from R6G-bound by rmsd >2 A over 459 aligned Ca positions; notable conformational changes in L3-4 and L9-10 loops</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5c6p">5C6P</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">LDRFSFSVFLKEIRLLTALAL</span><span class="topo-membrane">PMLLAQVAQVGIGFVDTVM</span><span class="topo-outside">AGGAGKEDLAAVALG</span><span class="topo-membrane">SSAFATVYITFMGIMAA</span><span class="topo-inside">LNPMIAQLYGAGKTGEAGETGRQG</span><span class="topo-membrane">IWFGLILGIFGMILMWAAI</span><span class="topo-outside">TPFRN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WLTLSDYVEGTMAQYMLF</span><span class="topo-membrane">TSLAMPAAMVHRALHAYA</span><span class="topo-inside">SSLNRPR</span><span class="topo-membrane">LIMLVSFAAFVLNVPLNY</span><span class="topo-outside">IFVYGKFGMPALGGAGC</span><span class="topo-membrane">GVATMAVFWFSALALWIY</span><span class="topo-inside">IAKEKFFRPFGLTAKFGKPDWAVF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KQIWKI</span><span class="topo-membrane">GAPIGLSYFLEASAFSFIV</span><span class="topo-outside">FLIAPFGEDYVAAQQ</span><span class="topo-membrane">VGISLSGILYMIPQSVGSAG</span><span class="topo-inside">TVRIGFSLGRREFSRARYISGVSL</span><span class="topo-membrane">VSGWVLAVITVLSLVLFR</span><span class="topo-outside">SPLASMYNDDPAVLSIAS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-outside">TV</span><span class="topo-membrane">LLFAGLFQPADFTQCIASY</span><span class="topo-inside">ALRGYKVTK</span><span class="topo-membrane">VPMFIHAAAFWGCGLLPGYLL</span><span class="topo-outside">AYRFDMGIY</span><span class="topo-membrane">GFWTALIASLTIAAVALV</span><span class="topo-inside">WCLEKYSMELVKSHKAVSSGL</span></span>
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
      <td>21</td>
      <td>5</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>40</td>
      <td>26</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>41</td>
      <td>55</td>
      <td>45</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>72</td>
      <td>60</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>96</td>
      <td>77</td>
      <td>100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>115</td>
      <td>101</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>138</td>
      <td>120</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>156</td>
      <td>143</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>157</td>
      <td>163</td>
      <td>161</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>181</td>
      <td>168</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>186</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>216</td>
      <td>203</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>246</td>
      <td>221</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>265</td>
      <td>251</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>280</td>
      <td>270</td>
      <td>284</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>300</td>
      <td>285</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>301</td>
      <td>324</td>
      <td>305</td>
      <td>328</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>342</td>
      <td>329</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>362</td>
      <td>347</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>381</td>
      <td>367</td>
      <td>385</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>390</td>
      <td>386</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>411</td>
      <td>395</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>420</td>
      <td>416</td>
      <td>424</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>438</td>
      <td>425</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>459</td>
      <td>443</td>
      <td>463</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5c6p">5C6P</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90         </span>
<span class="topo-line"><span class="topo-unknown">ENLYFQGS</span><span class="topo-inside">VSSVPTKLEVVAATPTSLLISWDARGEYVVYYRITYGETGGNSPVQEFTVPGSSSTATISGLSPGVDYTITVYARSYYWGWYSPISINYRT</span></span>
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
      <td>9</td>
      <td>99</td>
      <td>1</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1219901110

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4huk">4HUK</a></td>
      <td>3.5</td>
      <td>--</td>
      <td>NorM-NG (residues 5-459) with C-terminal hexahistidine tag; crystallized with monobody chaperone</td>
      <td>Ethidium</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4huk">4HUK</a></td>
      <td>3.65</td>
      <td>--</td>
      <td>NorM-NG with C-terminal hexahistidine tag; monobody complex</td>
      <td>Rhodamine 6G (R6G)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4huk">4HUK</a></td>
      <td>3.55</td>
      <td>--</td>
      <td>NorM-NG with C-terminal hexahistidine tag; monobody complex</td>
      <td>Tetraphenylphosphonium (TPP)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4huk">4HUK</a></td>
      <td>3.9</td>
      <td>--</td>
      <td>NorM-NG with C-terminal hexahistidine tag; monobody complex</td>
      <td>Cs+ (sodium congener)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with membrane protein expression vectors
- **Construct**: [IPTG](/xray-mp-wiki/reagents/additives/iptg) induction at 37 C for 3 h

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
      <td>Cell growth and induction</td>
      <td>E. coli BL21(DE3) transformed with pET-15b-NorM-NG</td>
      <td>--</td>
      <td>LB media + --</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>--</td>
      <td>--</td>
      <td>-- + --</td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane extraction and purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Thrombin cleavage</td>
      <td>Overnight incubation with thrombin protease</td>
      <td>--</td>
      <td>-- + --</td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>-NaOH pH 7.5, 100 mM NaCl, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Crystallization with monobody chaperone; drug/substrate co-crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NorM-NG-monobody complex incubated with substrate</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structures captured in extracellular-facing, drug-bound states. NorM-NG crystallized in absence of Na+ (1 mM Na+ precluded crystallization). Four substrate-bound structures: ethidium, R6G, TPP (substrate analog), and Cs+ (Na+ congener). Monobody used as crystallization chaperone (engineered binding protein).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4huk">4HUK</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">LDRFSFSVFLKEIRLLTALALP</span><span class="topo-membrane">MLLAQVAQVGIGFVD</span><span class="topo-outside">TVMAGGAGKEDLAAVALGSSAF</span><span class="topo-membrane">ATVYITFMGIMAA</span><span class="topo-inside">LNPMIAQLYGAGKTGEAGETGR</span><span class="topo-membrane">QGIWFGLILGIFGMILM</span><span class="topo-outside">WAAITPFRN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WLTLSDYVEGTMAQYMLFTSLA</span><span class="topo-membrane">MPAAMVHRALHAYASS</span><span class="topo-inside">LNRPR</span><span class="topo-membrane">LIMLVSFAAFVLN</span><span class="topo-outside">VPLNYIFVYGKFGMPALGGAGCGVAT</span><span class="topo-membrane">MAVFWFSALALWIYIA</span><span class="topo-inside">KEKFFRPFGLTAKFGKPDWAVF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KQIWKIG</span><span class="topo-membrane">APIGLSYFLEASAFSFI</span><span class="topo-outside">VFLIAPFGEDYVAAQQVG</span><span class="topo-membrane">ISLSGILYMIPQSVGSA</span><span class="topo-inside">GTVRIGFSLGRREFSRARYISGVSLVSG</span><span class="topo-membrane">WVLAVITVLSLVLF</span><span class="topo-outside">RSPLASMYNDDPAVLSIAS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-outside">TV</span><span class="topo-membrane">LLFAGLFQPADFTQCI</span><span class="topo-inside">ASYALRGYKVTKVPM</span><span class="topo-membrane">FIHAAAFWGCGLLPGYLL</span><span class="topo-outside">AYRFDMGIY</span><span class="topo-membrane">GFWTALIASLTIAA</span><span class="topo-inside">VALVWCLEKYSMELVKSHKAVSSGL</span></span>
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
      <td>22</td>
      <td>5</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>27</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>59</td>
      <td>42</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>72</td>
      <td>64</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>94</td>
      <td>77</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>99</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>142</td>
      <td>116</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>158</td>
      <td>147</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>163</td>
      <td>163</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>176</td>
      <td>168</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>202</td>
      <td>181</td>
      <td>206</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>218</td>
      <td>207</td>
      <td>222</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>247</td>
      <td>223</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>264</td>
      <td>252</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>282</td>
      <td>269</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>299</td>
      <td>287</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>327</td>
      <td>304</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>341</td>
      <td>332</td>
      <td>345</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>342</td>
      <td>362</td>
      <td>346</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>378</td>
      <td>367</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>379</td>
      <td>393</td>
      <td>383</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>411</td>
      <td>398</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>420</td>
      <td>416</td>
      <td>424</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>434</td>
      <td>425</td>
      <td>438</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>459</td>
      <td>439</td>
      <td>463</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4huk">4HUK</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90         </span>
<span class="topo-line"><span class="topo-unknown">ENLYFQGS</span><span class="topo-inside">VSSVPTKLEVVAATPTSLLISWDARGEYVVYYRITYGETGGNSPVQEFTVPGSSSTATISGLSPGVDYTITVYARSYYWGWYSPISINYRT</span></span>
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
      <td>8</td>
      <td>-7</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>99</td>
      <td>1</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hul">4HUL</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">LDRFSFSVFLKEIRLLTALAL</span><span class="topo-membrane">PMLLAQVAQVGIGFVD</span><span class="topo-outside">TVMAGGAGKEDLAAVALGSSAF</span><span class="topo-membrane">ATVYITFMGIMAALN</span><span class="topo-inside">PMIAQLYGAGKTGEAGET</span><span class="topo-membrane">GRQGIWFGLILGIFGMILM</span><span class="topo-outside">WAAITPFRN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WLTLSDYVEGTMAQYMLFTSLA</span><span class="topo-membrane">MPAAMVHRALHAYASSL</span><span class="topo-inside">NRP</span><span class="topo-membrane">RLIMLVSFAAFVLN</span><span class="topo-outside">VPLNYIFVYGKFGMPALGGAGCGVAT</span><span class="topo-membrane">MAVFWFSALALWIYIAK</span><span class="topo-inside">EKFFRPFGLTAKFGKPDWAVF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KQI</span><span class="topo-membrane">WKIGAPIGLSYFLEASAFSFI</span><span class="topo-outside">VFLIAPFGEDYVAAQQVG</span><span class="topo-membrane">ISLSGILYMIPQSVGSAGT</span><span class="topo-inside">VRIGFSLGRREFSRARYISGVSLV</span><span class="topo-membrane">SGWVLAVITVLSLVLFR</span><span class="topo-outside">SPLASMYNDDPAVLSIAS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-outside">TV</span><span class="topo-membrane">LLFAGLFQPADFTQCIASY</span><span class="topo-inside">ALRGYKVTK</span><span class="topo-membrane">VPMFIHAAAFWGCGLLPGYLL</span><span class="topo-outside">AYRFDMGIY</span><span class="topo-membrane">GFWTALIASLTIAAVAL</span><span class="topo-inside">VWCLEKYSMELVKSHKAVSSGL</span></span>
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
      <td>21</td>
      <td>5</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>37</td>
      <td>26</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>59</td>
      <td>42</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>74</td>
      <td>64</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>92</td>
      <td>79</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>111</td>
      <td>97</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>142</td>
      <td>116</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>159</td>
      <td>147</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>162</td>
      <td>164</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>176</td>
      <td>167</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>202</td>
      <td>181</td>
      <td>206</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>219</td>
      <td>207</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>243</td>
      <td>224</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>264</td>
      <td>248</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>282</td>
      <td>269</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>287</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>325</td>
      <td>306</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>342</td>
      <td>330</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>362</td>
      <td>347</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>381</td>
      <td>367</td>
      <td>385</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>390</td>
      <td>386</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>411</td>
      <td>395</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>420</td>
      <td>416</td>
      <td>424</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>437</td>
      <td>425</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>438</td>
      <td>459</td>
      <td>442</td>
      <td>463</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hul">4HUL</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90         </span>
<span class="topo-line"><span class="topo-unknown">ENLYFQGS</span><span class="topo-inside">VSSVPTKLEVVAATPTSLLISWDARGEYVVYYRITYGETGGNSPVQEFTVPGSSSTATISGLSPGVDYTITVYARSYYWGWYSPISINYRT</span></span>
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
      <td>8</td>
      <td>-7</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>99</td>
      <td>1</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hum">4HUM</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">LDRFSFSVFLKEIRLLTALALPML</span><span class="topo-membrane">LAQVAQVGIGFVDTVMAGG</span><span class="topo-outside">AGKEDLAAVA</span><span class="topo-membrane">LGSSAFATVYITFMGIMA</span><span class="topo-inside">ALNPMIAQLYGAGKTGEAGETGRQGIWF</span><span class="topo-membrane">GLILGIFGMILMWAAIT</span><span class="topo-outside">PFRN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WLTLSDYVEGTMAQY</span><span class="topo-membrane">MLFTSLAMPAAMVHRALH</span><span class="topo-inside">AYASSLNRPRLI</span><span class="topo-membrane">MLVSFAAFVLNVPLNYIFV</span><span class="topo-outside">YGKFGMPALGGA</span><span class="topo-membrane">GCGVATMAVFWFSALA</span><span class="topo-inside">LWIYIAKEKFFRPFGLTAKFGKPDWAVF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KQIWKIG</span><span class="topo-membrane">APIGLSYFLEASAFSFIV</span><span class="topo-outside">FLIAPFGEDYVAAQQ</span><span class="topo-membrane">VGISLSGILYMIPQSVGS</span><span class="topo-inside">AGTVRIGFSLGRREFSRARYISGVSLV</span><span class="topo-membrane">SGWVLAVITVLSLVLFR</span><span class="topo-outside">SPLASMYNDDPAVLSIAS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-outside">TV</span><span class="topo-membrane">LLFAGLFQPADFTQCIASY</span><span class="topo-inside">ALRGYKVTKVP</span><span class="topo-membrane">MFIHAAAFWGCGLLPGYL</span><span class="topo-outside">LAYRFDMGIY</span><span class="topo-membrane">GFWTALIASLTIAAVAL</span><span class="topo-inside">VWCLEKYSMELVKSHKAVSSGL</span></span>
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
      <td>24</td>
      <td>5</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>43</td>
      <td>29</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>53</td>
      <td>48</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>71</td>
      <td>58</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>99</td>
      <td>76</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>116</td>
      <td>104</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>135</td>
      <td>121</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>153</td>
      <td>140</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>165</td>
      <td>158</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>184</td>
      <td>170</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>196</td>
      <td>189</td>
      <td>200</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>212</td>
      <td>201</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>247</td>
      <td>217</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>265</td>
      <td>252</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>280</td>
      <td>270</td>
      <td>284</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>298</td>
      <td>285</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>325</td>
      <td>303</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>342</td>
      <td>330</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>362</td>
      <td>347</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>381</td>
      <td>367</td>
      <td>385</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>392</td>
      <td>386</td>
      <td>396</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>410</td>
      <td>397</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>420</td>
      <td>415</td>
      <td>424</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>437</td>
      <td>425</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>438</td>
      <td>459</td>
      <td>442</td>
      <td>463</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hum">4HUM</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90         </span>
<span class="topo-line"><span class="topo-unknown">ENLYFQGS</span><span class="topo-inside">VSSVPTKLEVVAATPTSLLISWDARGEYVVYYRITYGETGGNSPVQEFTVPGSSSTATISGLSPGVDYTITVYARSYYWGWYSPISINYRT</span></span>
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
      <td>8</td>
      <td>-7</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>99</td>
      <td>1</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hun">4HUN</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">LDRFSFSVFLKEIRLLTALA</span><span class="topo-membrane">LPMLLAQVAQVGIGFVDTVMA</span><span class="topo-outside">GGAGKEDLAAVA</span><span class="topo-membrane">LGSSAFATVYITFMGIMAALN</span><span class="topo-inside">PMIAQLYGAGKTGEAGETGRQG</span><span class="topo-membrane">IWFGLILGIFGMILMWAAITP</span><span class="topo-outside">FRN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WLTLSDYVEGTMAQ</span><span class="topo-membrane">YMLFTSLAMPAAMVHRALHAYASS</span><span class="topo-inside">LNRP</span><span class="topo-membrane">RLIMLVSFAAFVLNVPLNYIF</span><span class="topo-outside">VYGKFGMPALGGA</span><span class="topo-membrane">GCGVATMAVFWFSALALWIY</span><span class="topo-inside">IAKEKFFRPFGLTAKFGKPDWAVF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KQIW</span><span class="topo-membrane">KIGAPIGLSYFLEASAFSFIVF</span><span class="topo-outside">LIAPFGEDYVAAQ</span><span class="topo-membrane">QVGISLSGILYMIPQSVGSAGT</span><span class="topo-inside">VRIGFSLGRREFSRARYISG</span><span class="topo-membrane">VSLVSGWVLAVITVLSLVLFR</span><span class="topo-outside">SPLASMYNDDPAVLSIAS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-outside">TV</span><span class="topo-membrane">LLFAGLFQPADFTQCIASYALRG</span><span class="topo-inside">YKVTK</span><span class="topo-membrane">VPMFIHAAAFWGCGLLPGYLL</span><span class="topo-outside">AYRFDMGIY</span><span class="topo-membrane">GFWTALIASLTIAAVALVWC</span><span class="topo-inside">LEKYSMELVKSHKAVSSGL</span></span>
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
      <td>20</td>
      <td>5</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>41</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>53</td>
      <td>46</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>74</td>
      <td>58</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>96</td>
      <td>79</td>
      <td>100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>117</td>
      <td>101</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>134</td>
      <td>122</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>158</td>
      <td>139</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>162</td>
      <td>163</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>183</td>
      <td>167</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>196</td>
      <td>188</td>
      <td>200</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>216</td>
      <td>201</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>244</td>
      <td>221</td>
      <td>248</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>266</td>
      <td>249</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>279</td>
      <td>271</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>301</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>321</td>
      <td>306</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>342</td>
      <td>326</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>362</td>
      <td>347</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>385</td>
      <td>367</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>390</td>
      <td>390</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>411</td>
      <td>395</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>420</td>
      <td>416</td>
      <td>424</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>440</td>
      <td>425</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>441</td>
      <td>459</td>
      <td>445</td>
      <td>463</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hun">4HUN</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90         </span>
<span class="topo-line"><span class="topo-unknown">ENLYFQGS</span><span class="topo-inside">VSSVPTKLEVVAATPTSLLISWDARGEYVVYYRITYGETGGNSPVQEFTVPGSSSTATISGLSPGVDYTITVYARSYYWGWYSPISINYRT</span></span>
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
      <td>8</td>
      <td>-7</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>99</td>
      <td>1</td>
      <td>91</td>
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

### Na+-coupled transport mechanism via transmembrane helix shifting

NorM-NG uses a Na+-coupled mechanism distinct from the H+-coupled [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh). Cation binding triggers substrate unbinding by shifting several transmembrane helices, contrasting with the direct-competition mechanism of [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh) where protonation of D40 triggers release without substantial conformational changes. The D41 residue (equivalent to [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh) D40) is essential for transport but is substituted by asparagine in eukaryotic MATE members.

### Verapamil-binding site and folded ligand conformation

[Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) in NorM-NG adopts a folded conformation with both aromatic rings stacked on top of each other — a double-layered conformation unlike the extended form seen in [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh). Direct contacts involve S61 (TM2), Q284 (TM8) via H-bonding and A57 (TM2), F265, V269 (TM7), P357 (L9-10) via van der Waals. D41 (TM1) and D356 (L9-10) carboxylate groups are ~6 and 3.5 A from [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) N8, implying moderate electrostatic attraction.

### Extracellular loop dynamics upon verapamil binding

Upon [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) binding, NorM-NG undergoes pronounced conformational changes in L3-4 and L9-10 extracellular loops. L3-4 shifts the most, losing ability to insert side chains into the central cavity. L9-10 also shifts away from the multidrug-binding cavity, interacting with [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) only modestly. These changes contrast with [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh) which remains largely unaltered upon ligand exchange.

### Mutational analysis of the verapamil-binding site

Mutations of D41, S61, F265L, V269, Q284, D356 and P357 abolished cellular resistance to [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil), confirming these residues as essential for [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) transport. Unlike [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh), none of the tested NorM-NG mutations enabled drug resistance in the presence of [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil), underscoring mechanistic differences between the NorM and DinF subfamilies.

### Multidrug-binding cavity with four acidic residues

Crystal structures of NorM-NG bound to ethidium, rhodamine 6G, and TPP revealed a multidrug-binding cavity lined by four negatively charged amino acids (D41, D130, D355, D356) and surprisingly limited hydrophobic moieties. This contrasts with the general belief that aromatic amino acids play a prominent role in multidrug recognition. The cavity is capped by extracellular loops L3-4 and L9-10. F265 makes an edge-to-face aromatic stacking interaction with substrates. Mutagenesis confirmed D41, F265, Q284, D355, and D356 as critical for transport function.

### Uncommon Na+-pi interaction in the cation-binding site

A Na+-binding site was identified outside the drug-binding cavity, involving E261 and Y294. Y294 makes an uncommon cation-pi interaction with Na+, the first observation of a Na+-pi interaction in any membrane protein. The cation-binding site is distinct from the substrate-binding residues, supporting an indirect coupling mechanism. D377, while essential for transport, is positioned >7.2 A from the bound Cs+ in the NorM-NG structure, suggesting TM rearrangement is required for D377 to participate in Na+ coordination during transport.

### Unconventional antiport mechanism - indirect coupling

NorM-NG employs an unconventional antiport mechanism where Na+ and substrate bind to distinct amino acids and can bind simultaneously. Na+ binding induces conformational changes in TM7 and TM8 (tilting ~20 degrees relative to membrane normal) that disrupt the drug-binding site, rather than directly competing for shared binding residues. This indirect coupling mechanism is distinct from the canonical antiport mechanism observed in transporters like NhaA and EmrE where counterion and substrate compete for a shared binding site. Na+-induced TM rearrangement pulls F265 (TM7), Q284, and S288 (TM8) away from the central cavity to disrupt drug binding.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/dinf-bh/">DinF-BH (Bacillus halodurans DinF)</a> — Co-reported in same paper; mechanistic comparison between NorM and DinF subfamilies
- <a href="/xray-mp-wiki/proteins/norm-vc/">NorM-VC (Vibrio cholerae NorM)</a> — Earlier NorM subfamily structure; Na+-coupled MATE transporter; comparison of cation-bound states
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Primary detergent used for NorM-NG solubilization and purification
- <a href="/xray-mp-wiki/reagents/ligands/verapamil/">Verapamil</a> — Broad-spectrum MATE inhibitor that co-crystallized with NorM-NG
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/mate-transporter-family/">MATE Transporter Family</a> — NorM-NG is a NorM subfamily member of the MATE family
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — MATE transporters operate via alternating access mechanism
- <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/ligands/doxorubicin">Doxorubicin - Anthracycline Anticancer Drug</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/protein-tags/monobody/">Monobody</a> — Engineered crystallization chaperone used for NorM-NG structure determination
- <a href="/xray-mp-wiki/concepts/cation-pi-interaction/">Cation-pi Interaction</a> — Na+-pi interaction with Y294 is a key mechanistic feature
