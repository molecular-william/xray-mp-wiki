---
title: "Human CRTH2 (PGD2 Receptor)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.molcel.2018.08.009, doi/10.1073##pnas.2102813118]
verified: agent
uniprot_id: Q9Y5Y4
---

# Human CRTH2 (PGD2 Receptor)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9Y5Y4">UniProt: Q9Y5Y4</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

CRTH2 (chemoattractant receptor-homologous molecule expressed on Th2 cells, also known as DP2) is a G-protein-coupled receptor (GPCR) for prostaglandin D2 (PGD2). It mediates type 2 inflammation and is a major drug target for asthma and other inflammatory disorders. CRTH2 is the only member of the prostanoid receptor family that is phylogenetically distant from other prostanoid receptors. This paper reports the crystal structure of human CRTH2 bound to the PGD2 derivative [15R Methyl Pgd2](/xray-mp-wiki/reagents/ligands/15r-methyl-pgd2/) (15mPGD2) by serial femtosecond crystallography (SFX) at 2.6-3.2 A resolution, revealing a "polar group in" binding mode that contrasts with the "polar group out" mode of PGE2 in EP3. Previous structures reported CRTH2 bound to antagonists fevipiprant (2.80 A) and CAY10471 (2.74 A).


## Publications

### doi/10.1016##j.molcel.2018.08.009

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6d26">6D26</a></td>
      <td>2.80</td>
      <td>P212121</td>
      <td>Human CRTH2 with mT4L insertion in ICL3, N25A mutation, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a> (R340-S395 removed), N-terminal 8-amino acid linker</td>
      <td>Fevipiprant (QAW039)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6d27">6D27</a></td>
      <td>2.74</td>
      <td>P212121</td>
      <td>Human CRTH2 with mT4L insertion in ICL3, N25A mutation, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a> (R340-S395 removed), N-terminal 8-amino acid linker</td>
      <td>CAY10471</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9)
- **Construct**: Human CRTH2 (UniProt Q9Y5Y4) with N-terminal FLAG tag, mT4L insertion in ICL3 (between R237 and I238), N25A mutation, C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) at R340. Expressed using Bac-to-Bac baculovirus system in Sf9 insect cells.

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
      <td>Expression</td>
      <td>Baculovirus infection</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Sf9 cells infected with baculovirus, harvested 48 h post-infection</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Centrifugation and homogenization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> (pH 7.5), 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a>, 20 mM KCl, protease inhibitors + --</td>
      <td>Cells lysed by repeated homogenization and centrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> (pH 7.5), 500 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a>, 20 mM KCl, 30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a></td>
      <td>Membranes solubilized in 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/); supernatant after 1 h binding with ligand</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> M1 <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> M1 resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> (pH 7.5), 500 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a>, 20 mM KCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> + 0.002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Bound in 2 mM CaCl2; eluted with 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + 200 ug/ml <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> peptide</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> (pH 7.5), 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a>, 20 mM KCl + 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> + 0.002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Final purification after concentrating eluted protein. Final sample buffer for crystallization.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified CRTH2-mT4L in 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> (pH 7.5), 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a>, 20 mM KCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>25% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 3350, 0.1 M bis-tris propane (pH 6.5-7.0), 0.15 M Na-succinate, and 5% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 200</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir solution supplemented with 25% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 2.74-2.80 A. Structures solved by molecular replacement using C5aR (6C1R) and T4L from ETBR (5XPR). Data collected at APS GM/CA beamline. Two PDB depositions: 6D26 (fevipiprant-bound) and 6D27 (CAY10471-bound).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d26">6D26</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GMSAN</span><span class="topo-inside">ATLKPLCPILEQMSRLQSHSATSIRYIDH</span><span class="topo-membrane">AAVLLHGLASLLGLVENGVILFVVGC</span><span class="topo-outside">RMRQTVV</span><span class="topo-membrane">TTWVLHLALSDLLASASLPFFTYFL</span><span class="topo-inside">AVGHSWELGTT</span><span class="topo-membrane">FCKLHSSIFFLNMFASG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FLLSAISLD</span><span class="topo-outside">RCLQVVRPVWAQNHRTVAA</span><span class="topo-membrane">AHKVCLVLWALAVLNTVPYFVFR</span><span class="topo-inside">DTISRLDGRIMCYYNVLLLNPGPDRDATCNSR</span><span class="topo-membrane">QAALAVSKFLLAFLVPLAIIASSHAA</span><span class="topo-outside">VSLRLQHRADL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">GLQHRNIFEMLRIDEGGGSGGDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470</span>
<span class="topo-line"><span class="topo-outside">AYRRRPGRFV</span><span class="topo-membrane">RLVAAVVAAFALCWGPYHVFSLLEA</span><span class="topo-inside">RAHANPGLRPLVWRG</span><span class="topo-membrane">LPFVTSLAFFNSVANPVLYVLTC</span><span class="topo-outside">PDMLRKLRRSLRTVLESVL</span><span class="topo-unknown">VDDSELGGAGSSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>0</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>34</td>
      <td>5</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>60</td>
      <td>34</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>67</td>
      <td>60</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>92</td>
      <td>67</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>103</td>
      <td>92</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>129</td>
      <td>103</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>148</td>
      <td>129</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>171</td>
      <td>148</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>203</td>
      <td>171</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>229</td>
      <td>203</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>237</td>
      <td>229</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>362</td>
      <td>1238</td>
      <td>1362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>370</td>
      <td>2238</td>
      <td>2245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>395</td>
      <td>2246</td>
      <td>2270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>396</td>
      <td>410</td>
      <td>2271</td>
      <td>2285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>433</td>
      <td>2286</td>
      <td>2308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>434</td>
      <td>452</td>
      <td>2309</td>
      <td>2327</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>453</td>
      <td>470</td>
      <td>2328</td>
      <td>2345</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d27">6D27</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GMSAN</span><span class="topo-inside">ATLKPLCPILEQMSRL</span><span class="topo-unknown">QSHS</span><span class="topo-inside">ATSIRYIDHA</span><span class="topo-membrane">AVLLHGLASLLGLVENGVILFVVGC</span><span class="topo-outside">RMRQTVVT</span><span class="topo-membrane">TWVLHLALSDLLASASLPFFTY</span><span class="topo-inside">FLAVGHSWELGTT</span><span class="topo-membrane">FCKLHSSIFFLNMFASG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FLLSAISL</span><span class="topo-outside">DRCLQVVRPVWAQNHRTVAAA</span><span class="topo-membrane">HKVCLVLWALAVLNTVPYFVFR</span><span class="topo-inside">DTISRLDGRIMCYYNVLLLNPGPDRDATCN</span><span class="topo-membrane">SRQAALAVSKFLLAFLVPLAIIASSH</span><span class="topo-outside">AAVSLRLQHRADL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">GLQHRNIFEMLRIDEGGGSGGDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470</span>
<span class="topo-line"><span class="topo-outside">AYRRRPGRFVR</span><span class="topo-membrane">LVAAVVAAFALCWGPYHVFSLLEAR</span><span class="topo-inside">AHANPGLRPLVWR</span><span class="topo-membrane">GLPFVTSLAFFNSVANPVLYVLTC</span><span class="topo-outside">PDMLRKLRRSLRTVLESVL</span><span class="topo-unknown">VDDSELGGAGSSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>0</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>21</td>
      <td>5</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>21</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>35</td>
      <td>25</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>60</td>
      <td>35</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>68</td>
      <td>60</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>90</td>
      <td>68</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>90</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>128</td>
      <td>103</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>149</td>
      <td>128</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>171</td>
      <td>149</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>201</td>
      <td>171</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>227</td>
      <td>201</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>237</td>
      <td>227</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>362</td>
      <td>1238</td>
      <td>1362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>371</td>
      <td>2238</td>
      <td>2246</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>396</td>
      <td>2247</td>
      <td>2271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>409</td>
      <td>2272</td>
      <td>2284</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>433</td>
      <td>2285</td>
      <td>2308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>434</td>
      <td>452</td>
      <td>2309</td>
      <td>2327</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>453</td>
      <td>470</td>
      <td>2328</td>
      <td>2345</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.2102813118

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m8w">7M8W</a></td>
      <td>2.60</td>
      <td>P212121</td>
      <td>Human CRTH2 with mT4L insertion in ICL3, N25A mutation, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a> at R340</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/15r-methyl-pgd2/">15R Methyl Pgd2</a> (15mPGD2)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9)
- **Construct**: Human CRTH2 (UniProt Q9Y5Y4) with N-terminal FLAG tag, mT4L insertion in ICL3 (between R237 and I238), N25A mutation, C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) at R340. Expressed using Bac-to-Bac baculovirus system in Sf9 insect cells.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m8w">7M8W</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GMS</span><span class="topo-inside">ANATLKPLCPILEQMSRLQSHSATSIRYIDHA</span><span class="topo-membrane">AVLLHGLASLLGLVENGVILFVVGCR</span><span class="topo-outside">MRQTV</span><span class="topo-membrane">VTTWVLHLALSDLLASASLPFFTY</span><span class="topo-inside">FLAVGHSWELGTTF</span><span class="topo-membrane">CKLHSSIFFLNMFASG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FLLSAISLDRC</span><span class="topo-outside">LQVVRPVWAQNHRTVA</span><span class="topo-membrane">AAHKVCLVLWALAVLNTVPYFV</span><span class="topo-inside">FRDTISRLDGRIMCYYNVLLLNPGPDRDATCNSRQA</span><span class="topo-membrane">ALAVSKFLLAFLVPLAIIASSHAA</span><span class="topo-outside">VSLRLQHRADL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">GLQHRNIFE</span><span class="topo-unknown">MLRIDEGGGSGGDEA</span><span class="topo-outside">EKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470</span>
<span class="topo-line"><span class="topo-outside">AYRRRPGRF</span><span class="topo-membrane">VRLVAAVVAAFALCWGPYHVFSLL</span><span class="topo-inside">EARAHANPGLRPLVWRG</span><span class="topo-membrane">LPFVTSLAFFNSVANPVLYVLTC</span><span class="topo-outside">PDMLRKLRRSLRTVLESVLVDD</span><span class="topo-unknown">SELGGAGSSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>0</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>35</td>
      <td>3</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>61</td>
      <td>35</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>66</td>
      <td>61</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>90</td>
      <td>66</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>104</td>
      <td>90</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>131</td>
      <td>104</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>147</td>
      <td>131</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>169</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>205</td>
      <td>169</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>229</td>
      <td>205</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>237</td>
      <td>229</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>245</td>
      <td>900</td>
      <td>907</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>249</td>
      <td>1002</td>
      <td>1005</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>264</td>
      <td>1006</td>
      <td>1020</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>265</td>
      <td>362</td>
      <td>1064</td>
      <td>1161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>369</td>
      <td>238</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>393</td>
      <td>245</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>394</td>
      <td>410</td>
      <td>269</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>433</td>
      <td>286</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>434</td>
      <td>455</td>
      <td>309</td>
      <td>330</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>456</td>
      <td>470</td>
      <td>331</td>
      <td>345</td>
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

### Novel N-terminal lid domain covers the ligand-binding pocket

CRTH2 has a well-structured N-terminal region with an N-helix and N-loop that packs tightly against ECL2, covering the ligand-binding pocket. A disulfide bond (C26-C188) connects the N terminus to TM5. This structure creates a semi-occluded pocket with a single open end as a ligand entry port between TM1 and TM7, which is different from other lipid GPCRs ([S1P1](/xray-mp-wiki/proteins/gpcr/s1p1/), [LPA1](/xray-mp-wiki/proteins/gpcr/lpa1/), CB1) where the N-terminal region adopts different conformations.

### Conserved and divergent antagonist binding modes

Both fevipiprant and CAY10471 occupy a similar semi-occluded pocket with conserved polar interactions at the distal end (R170, Y184, K210, Y262) anchoring the carboxylate head group. The central aromatic groups engage in extensive aromatic and hydrophobic interactions with F87, F111, F112, F294, F90, H107, Y183, Y184, Y262, and L286. However, the tail groups show distinct binding modes: fevipiprant's methylsulfonyl phenyl group extends toward ECL2, while CAY10471's fluorophenyl group extends toward TM7, causing W283 and L20 side chain rearrangements.

### Charge attraction-guided binding mechanism for PGD2

A novel multi-step binding mechanism is proposed for PGD2. The carboxylate group of PGD2 first binds to the ligand entry port through interactions with positively charged residues (H95, R175, R179), then follows a positive charge gradient extending deeply into the ligand-binding pocket to reach a highly polar distal end (R170, Y184, K210, Y262, E269). This mechanism differs significantly from [S1P1](/xray-mp-wiki/proteins/gpcr/s1p1/), [LPA1](/xray-mp-wiki/proteins/gpcr/lpa1/), and CB1 where acyl chains enter the binding pocket without orientation change.

### Polar group in lipid-binding mode of CRTH2

The crystal structure of CRTH2 bound to 15mPGD2 (PDB 7M8W) reveals a "polar group in" binding mode where the carboxyl head group of 15mPGD2 is buried deep inside the binding pocket, while the omega-chain points toward the extracellular side. This contrasts with the "polar group out" mode observed in EP3-PGE2, where the carboxyl group is positioned near the extracellular surface and the omega-chain extends deep into the pocket. These two modes are associated with distinct charge distributions in the binding pockets.

### Cationic tetrad captures lipid ligands from the bilayer

MD simulations identified a cationic tetrad (R284, R175, R179, H95) at the ligand entry port of CRTH2 that functions like fishhooks to capture anionic lipid ligands from the lipid bilayer. D32 further funnels ligands toward the entry port. Mutagenesis confirmed these residues are critical for PGD2 binding - mutations at any of these positions abolished detectable specific binding, except R284A which reduced affinity 5-fold.

### Distinct PGD2 activation mechanism compared to PGE2 receptors

Unlike EP3 where PGE2 directly contacts W6.48 (the toggle switch), 15mPGD2 binds superficially without directly contacting the F6.44xxCW6.48 motif. Instead, the carboxyl group forms a hydrogen bond with Y262(6.51), and the omega-chain contacts F111(3.32), both packing against W259(6.48). This implies a distinct activation mechanism involving Y262, F111, and W259.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Primary solubilization and purification detergent (1% for solubilization, 0.01% for SEC)
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — 0.2% CHS added to LMNG for stabilization
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — 20 mM HEPES (pH 7.5) used in purification and crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">Polyethylene Glycol (PEG)</a> — 25% PEG 3350 as crystallization precipitant
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> — CRTH2 expressed in Sf9 insect cells using Bac-to-Bac system
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Anti-FLAG M1 affinity purification
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Crystallization method for CRTH2 antagonist structures
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase</a> — LCP used for crystallization in the SFX structure (PDB 7M8W)
- <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">Serial Femtosecond Crystallography</a> — SFX used to collect diffraction data from CRTH2 microcrystals at LCLS XFEL
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/">Molecular Dynamics Simulation</a> — MD simulations used to study lipid recognition and capture by CRTH2
