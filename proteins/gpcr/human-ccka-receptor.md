---
title: "Human Cholecystokinin A Receptor (CCKₐR)"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein]
sources: [doi/10.1038##s41589-021-00866-8]
verified: false
---

# Human Cholecystokinin A Receptor (CCKₐR)

## Overview

The human cholecystokinin A receptor (CCKₐR) is a class A G-protein-coupled receptor (GPCR) that preferentially binds sulfated cholecystokinin (CCK) peptides. CCKₐR plays vital roles in food intake regulation, pancreatic enzyme secretion, and gall bladder contraction. Crystal structures of human CCKₐR have been determined in complex with two small-molecule antagonists (devazepide at 2.5 Å, PDB 7F8W; lintitript at 2.8 Å, PDB 7F8V) and one peptide agonist analog (NN9056 at 3.0 Å, PDB 7F8W — the same PDB code covers multiple structures). The structures revealed an ECL3 forming a two-turn α-helical conformation (never before observed in class A GPCRs) and a β-hairpin in ECL2 typical of peptide receptors. The agonist-bound structure showed an inward shift of helix VI in the ligand-binding region as an early step toward activation.

## Publications

### doi/10.1038##s41589-021-00866-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a></td>
      <td>2.50</td>
      <td>P2₁2₁2</td>
      <td>Human CCKₐR with T4L fusion in ICL3 (between I240 and A302), C-terminal truncation (G407-Q428), mutation D87²·⁵⁰N for inactive state stabilization</td>
      <td>Devazepide (antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7f8v">7F8V</a></td>
      <td>2.80</td>
      <td>P2₁2₁2</td>
      <td>Human CCKₐR with T4L fusion in ICL3, C-terminal truncation, D87²·⁵⁰N mutation</td>
      <td>Lintitript (antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a></td>
      <td>3.00</td>
      <td>P2₁2₁2</td>
      <td>Human CCKₐR with T4L fusion in ICL3, C-terminal truncation, F130³·⁴⁰W mutation</td>
      <td>NN9056 (peptide agonist analog)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells (Bac-to-Bac baculovirus expression system)
- **Construct**: Human CCKₐR with HA signal sequence, Flag tag, N-terminal tag, PreScission protease site, 10× His tag at C-terminus; T4L inserted at ICL3 (I240-A302) with C-terminal truncation (G407-Q428)

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
      <td>1. Membrane preparation and solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 10 μM ligand</td>
      <td>Sf9 cell membranes solubilized for 2 h at 4°C</td>
    </tr>
    <tr>
      <td>2. Ni-NTA affinity chromatography</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM imidazole</td>
      <td>Protein eluted with 200 mM imidazole</td>
    </tr>
    <tr>
      <td>3. PreScission protease cleavage</td>
      <td>Protease treatment</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Overnight cleavage at 4°C to remove N-terminal tag</td>
    </tr>
    <tr>
      <td>4. Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL</td>
      <td>—</td>
      <td>25 mM HEPES pH 7.5, 150 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 10 μM ligand</td>
      <td>Peak fractions concentrated to 20 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<<<<<<< HEAD
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CCKₐR-T4L at ~20 mg/ml in 25 mM HEPES pH 7.5, 150 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-7 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at SPring-8 beamline BL41XU. Structures solved by molecular replacement using T4L and a GPCR template. Diffraction data from <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>-grown crystals with space group P2₁2₁2.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**
=======
| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Membrane preparation and solubilization | Detergent extraction | — | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 μM ligand | Sf9 cell membranes solubilized for 2 h at 4°C |
| 2. Ni-NTA affinity chromatography | Immobilized metal [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM imidazole | Protein eluted with 200 mM imidazole |
| 3. PreScission protease cleavage | Protease treatment | — | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Overnight cleavage at 4°C to remove N-terminal tag |
| 4. Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL | — | 25 mM HEPES pH 7.5, 150 mM NaCl, 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 μM ligand | Peak fractions concentrated to 20 mg/ml for crystallization |
>>>>>>> d0e2c437136bdf2885afc6a99e0a9d4117821696

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGCTLS</span><span class="topo-outside">AEDKAAVERSKMIDRNLRRDKRDARRELKLLLLGTGESGKSTFIKQMRIIHG</span><span class="topo-unknown">SG</span></span>
<span class="topo-line"><span class="topo-unknown">YSDEDKRGFTKLVYQNIFTAMQAMIRAMDTLKIPYKYEHNKAHAQLVREVDVEKVSAFEN</span></span>
<span class="topo-line"><span class="topo-unknown">PYVDAIKSLWNDPGIQECYDRRREYQLSDSTKYYLNDLDRVADPAYLPTQQDVLRVRVPT</span></span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-outside">GIIEYPFDLQSVIFRMVDVGGQRSERRKWIHCFENVTSIMFLVALSEYDQVLVESDNEN</span></span>
<span class="topo-line"><span class="topo-outside">RMEESKALFRTIITYPWFQNSSVILFLNKKDLLEEKIMYSHLVDYFPEYDGPQRDAQAAR</span></span>
<span class="topo-line"><span class="topo-outside">EFILKMFVDLNPDSDKIIYSHFTCATDTENIRFVFAAVKDTILQLNLKEYNLV</span></span>
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
      <td>7</td>
      <td>58</td>
      <td>7</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>353</td>
      <td>182</td>
      <td>353</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain B (0 TMs, non_tm)**

<<<<<<< HEAD
<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MHHHHHHGSLLQSELDQLRQEAEQLKNQIRDARKACADATLSQIT</span><span class="topo-outside">NNIDPVGRIQMRTRR</span></span>
<span class="topo-line"><span class="topo-outside">TLRGHLAKIYAMHWGTDSRLLVSASQDGKLIIWDSYTTNKVHAIPLRSSWVMTCAYAPSG</span></span>
<span class="topo-line"><span class="topo-outside">NYVACGGLDNICSIYNLKTREGNVRVSRELAGHTGYLSCCRFLDDNQIVTSSGDTTCALW</span></span>
<span class="topo-line"><span class="topo-outside">DIETGQQTTTFTGHTGDVMSLSLAPDTRLFVSGACDASAKLWDVREGMCRQTFTGHESDI</span></span>
<span class="topo-line"><span class="topo-outside">NAICFFPNGNAFATGSDDATCRLFDLRADQELMTYSHDNIICGITSVSFSKSGRLLLAGY</span></span>
<span class="topo-line"><span class="topo-outside">DDFNCNVWDALKADRAGVLAGHDNRVSCLGVTDDGMAVATGSWDSFLKIWN</span></span>
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
      <td>46</td>
      <td>351</td>
      <td>35</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>
=======
| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) |
| Protein sample | CCKₐR-T4L at ~20 mg/ml in 25 mM HEPES pH 7.5, 150 mM NaCl, 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |
| Temperature | 20°C |
| Growth time | 3-7 days |
| Notes | Data collected at SPring-8 beamline BL41XU. Structures solved by molecular replacement using T4L and a GPCR template. Diffraction data from [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)-grown crystals with space group P2₁2₁2. |
>>>>>>> d0e2c437136bdf2885afc6a99e0a9d4117821696

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MASNNTASIAQARKLVEQLKMEANIDRI</span><span class="topo-outside">KVSKAAADLMAYCEAHAKEDPLLTPVPASENP</span></span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-unknown">REKKFFCAIL</span></span>
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
      <td>29</td>
      <td>61</td>
      <td>29</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MVRTAVLILLLVRFSEPD</span><span class="topo-outside">VQLVESGGGLVQPGGSRKLSCSASGFAFSSFGMHWVRQAPEK</span></span>
<span class="topo-line"><span class="topo-outside">GLEWVAYISSGSGTIYYADTVKGRFTISRDDPKNTLFLQMTSLRSEDTAMYYCVRSIYYY</span></span>
<span class="topo-line"><span class="topo-outside">GSSPFDFWGQGTTLTVSS</span><span class="topo-unknown">GGGGSGGGGSGGGG</span><span class="topo-outside">SDIVMTQATSSVPVTPGESVSISCRSSK</span></span>
<span class="topo-line"><span class="topo-outside">SLLHSNGNTYLYWFLQRPGQSPQLLIYRMSNLASGVPDRFSGSGSGTAFTLTISRLEAED</span></span>
<span class="topo-line"><span class="topo-outside">VGVYYCMQHLEYPLTFGAGTKLEL</span><span class="topo-unknown">KAAA</span></span>
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
      <td>19</td>
      <td>138</td>
      <td>19</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>264</td>
      <td>153</td>
      <td>264</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">?GPWLEEEEEAYGWM</span><span class="topo-unknown">D?</span></span>
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
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>17</td>
      <td>16</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain R (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDGAPELLKLNRSVQGTGPGPGASLCRPGAPLLNSSSVGNLSCEPPRIRGAGTRE</span></span>
<span class="topo-line"><span class="topo-unknown">LEL</span><span class="topo-inside">AI</span><span class="topo-membrane">RITLYAVIFLMSVGGNMLIIV</span><span class="topo-outside">VLGLSRRLRTVTNAFLL</span><span class="topo-membrane">SLAVSDLLLAVACMPF</span><span class="topo-inside">T</span></span>
<span class="topo-line"><span class="topo-inside">LLPNLMGTFIFGTVICKA</span><span class="topo-membrane">VSYLMGVSVSVSTLSLV</span><span class="topo-outside">AIALERYSAICRPLQARVWQTRSHA</span></span>
<span class="topo-line"><span class="topo-outside">ARVI</span><span class="topo-membrane">VATWLLSGLLMVPYP</span><span class="topo-inside">VYTVVQPVGPRVLQCVHRWPSARVRQ</span><span class="topo-membrane">TWSVLLLLLLFFIPG</span></span>
<span class="topo-line"><span class="topo-membrane">VVMA</span><span class="topo-outside">VAYGLISRELYLGL</span><span class="topo-unknown">RFDGDSDSDSQSRVRNQGGLPGAVHQNGRCRPETGAVGEDSD</span></span>
<span class="topo-line"><span class="topo-unknown">GCYVQLPRSRPALELTALTAPGPGSGSRPTQAKL</span><span class="topo-outside">LAKKRVVRMLLV</span><span class="topo-membrane">IVVLFFLCWLPVYS</span></span>
<span class="topo-line"><span class="topo-membrane">ANT</span><span class="topo-inside">WRAFDGPGAHRALSGAPIS</span><span class="topo-membrane">FIHLLSYASACVNPLV</span><span class="topo-outside">YCFMH</span><span class="topo-unknown">RRFRQACLET</span><span class="topo-outside">C</span><span class="topo-unknown">ARCCPR</span></span>
<span class="topo-line"><span class="topo-unknown">PPRARPREFLEVLFQGPWSHPQFEKGGGSGGGSGGSAWSHPQFEK</span></span>
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
      <td>64</td>
      <td>65</td>
      <td>55</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>57</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>78</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>119</td>
      <td>95</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>138</td>
      <td>111</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>155</td>
      <td>130</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>184</td>
      <td>147</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>199</td>
      <td>176</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>225</td>
      <td>191</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>244</td>
      <td>217</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>258</td>
      <td>236</td>
      <td>249</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>346</td>
      <td>326</td>
      <td>337</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>363</td>
      <td>338</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>382</td>
      <td>355</td>
      <td>373</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>398</td>
      <td>374</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>399</td>
      <td>403</td>
      <td>390</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>413</td>
      <td>395</td>
      <td>404</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>414</td>
      <td>414</td>
      <td>405</td>
      <td>405</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8v">7F8V</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGCTVSAED</span><span class="topo-outside">KAAAERSKMIDKNLREDGEKAAREVKLLLLGAGESGKNTIVKQM</span><span class="topo-unknown">KIIHEDG</span></span>
<span class="topo-line"><span class="topo-unknown">YSEEECRQYRAVVYSNTIQSIMAIVKAMGNLQIDFADPSRADDARQLFALSCTAEEQGVL</span></span>
<span class="topo-line"><span class="topo-unknown">PDDLSGVIRRLWADHGVQACFGRSREYQLNDSAAYYLNDLERIAQSDYIPTQQDVLRTRV</span></span>
<span class="topo-line"><span class="topo-unknown">KT</span><span class="topo-outside">TGIVETHFTFKDLHFKMFDVGAQRSERKKWIHCFEGVTAIIFCVALSAYDLVLAEDEE</span></span>
<span class="topo-line"><span class="topo-outside">MNRMHASMKLFDSICNNKWFTDTSIILFLNKKDLFEEKITHSPLTICFPEYTGANKYDEA</span></span>
<span class="topo-line"><span class="topo-outside">ASYIQSKFEDLNKRKDTKEIYTHFTCSTDTKNVQFVFDAVTDVIIKNNLKDCGLF</span></span>
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
      <td>10</td>
      <td>53</td>
      <td>10</td>
      <td>53</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>355</td>
      <td>183</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8v">7F8V</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MHHHHHHGSLLQSELDQLRQEAEQLKNQIRDARKACADATLSQIT</span><span class="topo-outside">NNIDPVGRIQMRTRR</span></span>
<span class="topo-line"><span class="topo-outside">TLRGHLAKIYAMHWGTDSRLLVSASQDGKLIIWDSYTTNKVHAIPLRSSWVMTCAYAPSG</span></span>
<span class="topo-line"><span class="topo-outside">NYVACGGLDNICSIYNLKTREGNVRVSRELAGHTGYLSCCRFLDDNQIVTSSGDTTCALW</span></span>
<span class="topo-line"><span class="topo-outside">DIETGQQTTTFTGHTGDVMSLSLAPDTRLFVSGACDASAKLWDVREGMCRQTFTGHESDI</span></span>
<span class="topo-line"><span class="topo-outside">NAICFFPNGNAFATGSDDATCRLFDLRADQELMTYSHDNIICGITSVSFSKSGRLLLAGY</span></span>
<span class="topo-line"><span class="topo-outside">DDFNCNVWDALKADRAGVLAGHDNRVSCLGVTDDGMAVATGSWDSFLKIWN</span></span>
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
      <td>46</td>
      <td>351</td>
      <td>35</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8v">7F8V</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MASNNTASIAQARKLVEQLKMEANIDRI</span><span class="topo-outside">KVSKAAADLMAYCEAHAKEDPLLTPVPASENP</span></span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-unknown">REKKFFCAIL</span></span>
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
      <td>29</td>
      <td>61</td>
      <td>29</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8v">7F8V</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">?GPWLEEEEEAYGWM</span><span class="topo-unknown">D?</span></span>
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
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>17</td>
      <td>16</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8v">7F8V</a> — Chain R (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDGAPELLKLNRSVQGTGPGPGASLCRPGAPLLNSSSVGNLSCEPPRIRGAGTRE</span></span>
<span class="topo-line"><span class="topo-unknown">LEL</span><span class="topo-inside">AI</span><span class="topo-membrane">RITLYAVIFLMSVGGNMLIIVVLG</span><span class="topo-outside">LSRRLRTVTNA</span><span class="topo-membrane">FLLSLAVSDLLLAVACMPF</span><span class="topo-inside">T</span></span>
<span class="topo-line"><span class="topo-inside">LLPNLMGTFIFGTVICKA</span><span class="topo-membrane">VSYLMGVSVSVSTLSLVAIAL</span><span class="topo-outside">ERYSAICRPLQARVWQTRSHA</span></span>
<span class="topo-line"><span class="topo-outside">A</span><span class="topo-membrane">RVIVATWLLSGLLMVPYP</span><span class="topo-inside">VYTVVQPVGPRVLQCVHRWPSARVRQT</span><span class="topo-membrane">WSVLLLLLLFFIPG</span></span>
<span class="topo-line"><span class="topo-membrane">VVMAVAY</span><span class="topo-outside">GLISRELYLGL</span><span class="topo-unknown">RFDGDSDSDSQSRVRNQGGLPGAVHQNGRCRPETGAVGEDSD</span></span>
<span class="topo-line"><span class="topo-unknown">GCYVQLPRSRPALELTALTAPGPGSGSRPTQAKL</span><span class="topo-outside">LAKKRVVR</span><span class="topo-membrane">MLLVIVVLFFLCWLPVYS</span></span>
<span class="topo-line"><span class="topo-membrane">ANT</span><span class="topo-inside">WRAFDGPGAHRALSGAPISF</span><span class="topo-membrane">IHLLSYASACVNPLVYCFM</span><span class="topo-outside">H</span><span class="topo-unknown">RRFRQACLET</span><span class="topo-outside">C</span><span class="topo-unknown">ARCCPR</span></span>
<span class="topo-line"><span class="topo-unknown">PPRARPREFLEVLFQGPWSHPQFEKGGGSGGGSGGSAWSHPQFEK</span></span>
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
      <td>64</td>
      <td>65</td>
      <td>55</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>89</td>
      <td>57</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>100</td>
      <td>81</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>119</td>
      <td>92</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>138</td>
      <td>111</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>159</td>
      <td>130</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>181</td>
      <td>151</td>
      <td>172</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>199</td>
      <td>173</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>226</td>
      <td>191</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>247</td>
      <td>218</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>248</td>
      <td>258</td>
      <td>239</td>
      <td>249</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>342</td>
      <td>326</td>
      <td>333</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>363</td>
      <td>334</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>383</td>
      <td>355</td>
      <td>374</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>402</td>
      <td>375</td>
      <td>393</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>403</td>
      <td>403</td>
      <td>394</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>413</td>
      <td>395</td>
      <td>404</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>414</td>
      <td>414</td>
      <td>405</td>
      <td>405</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGCTLS</span><span class="topo-outside">AEDKAAVERSKMIDRNLRRDKRDARRELKLLLLGTGESGKSTFIKQMRIIHG</span><span class="topo-unknown">SG</span></span>
<span class="topo-line"><span class="topo-unknown">YSDEDKRGFTKLVYQNIFTAMQAMIRAMDTLKIPYKYEHNKAHAQLVREVDVEKVSAFEN</span></span>
<span class="topo-line"><span class="topo-unknown">PYVDAIKSLWNDPGIQECYDRRREYQLSDSTKYYLNDLDRVADPAYLPTQQDVLRVRVPT</span></span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-outside">GIIEYPFDLQSVIFRMVDVGGQRSERRKWIHCFENVTSIMFLVALSEYDQVLVESDNEN</span></span>
<span class="topo-line"><span class="topo-outside">RMEESKALFRTIITYPWFQNSSVILFLNKKDLLEEKIMYSHLVDYFPEYDGPQRDAQAAR</span></span>
<span class="topo-line"><span class="topo-outside">EFILKMFVDLNPDSDKIIYSHFTCATDTENIRFVFAAVKDTILQLNLKEYNLV</span></span>
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
      <td>7</td>
      <td>58</td>
      <td>7</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>353</td>
      <td>182</td>
      <td>353</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MHHHHHHGSLLQSELDQLRQEAEQLKNQIRDARKACADATLSQIT</span><span class="topo-outside">NNIDPVGRIQMRTRR</span></span>
<span class="topo-line"><span class="topo-outside">TLRGHLAKIYAMHWGTDSRLLVSASQDGKLIIWDSYTTNKVHAIPLRSSWVMTCAYAPSG</span></span>
<span class="topo-line"><span class="topo-outside">NYVACGGLDNICSIYNLKTREGNVRVSRELAGHTGYLSCCRFLDDNQIVTSSGDTTCALW</span></span>
<span class="topo-line"><span class="topo-outside">DIETGQQTTTFTGHTGDVMSLSLAPDTRLFVSGACDASAKLWDVREGMCRQTFTGHESDI</span></span>
<span class="topo-line"><span class="topo-outside">NAICFFPNGNAFATGSDDATCRLFDLRADQELMTYSHDNIICGITSVSFSKSGRLLLAGY</span></span>
<span class="topo-line"><span class="topo-outside">DDFNCNVWDALKADRAGVLAGHDNRVSCLGVTDDGMAVATGSWDSFLKIWN</span></span>
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
      <td>46</td>
      <td>351</td>
      <td>35</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MASNNTASIAQARKLVEQLKMEANIDRI</span><span class="topo-outside">KVSKAAADLMAYCEAHAKEDPLLTPVPASENP</span></span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-unknown">REKKFFCAIL</span></span>
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
      <td>29</td>
      <td>61</td>
      <td>29</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MVRTAVLILLLVRFSEPD</span><span class="topo-outside">VQLVESGGGLVQPGGSRKLSCSASGFAFSSFGMHWVRQAPEK</span></span>
<span class="topo-line"><span class="topo-outside">GLEWVAYISSGSGTIYYADTVKGRFTISRDDPKNTLFLQMTSLRSEDTAMYYCVRSIYYY</span></span>
<span class="topo-line"><span class="topo-outside">GSSPFDFWGQGTTLTVSS</span><span class="topo-unknown">GGGGSGGGGSGGGG</span><span class="topo-outside">SDIVMTQATSSVPVTPGESVSISCRSSK</span></span>
<span class="topo-line"><span class="topo-outside">SLLHSNGNTYLYWFLQRPGQSPQLLIYRMSNLASGVPDRFSGSGSGTAFTLTISRLEAED</span></span>
<span class="topo-line"><span class="topo-outside">VGVYYCMQHLEYPLTFGAGTKLEL</span><span class="topo-unknown">KAAA</span></span>
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
      <td>19</td>
      <td>138</td>
      <td>19</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>264</td>
      <td>153</td>
      <td>264</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">?GPWLEEEEEAYGWM</span><span class="topo-unknown">D?</span></span>
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
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>17</td>
      <td>16</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8w">7F8W</a> — Chain R (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDGAPELLKLNRSVQGTGPGPGASLCRPGAPLLNSSSVGNLSCEPPRIRGAGTRE</span></span>
<span class="topo-line"><span class="topo-unknown">LEL</span><span class="topo-inside">AI</span><span class="topo-membrane">RITLYAVIFLMSVGGNMLIIV</span><span class="topo-outside">VLGLSRRLRTVTNAFLL</span><span class="topo-membrane">SLAVSDLLLAVACMPF</span><span class="topo-inside">T</span></span>
<span class="topo-line"><span class="topo-inside">LLPNLMGTFIFGTVICKA</span><span class="topo-membrane">VSYLMGVSVSVSTLSLV</span><span class="topo-outside">AIALERYSAICRPLQARVWQTRSHA</span></span>
<span class="topo-line"><span class="topo-outside">ARVI</span><span class="topo-membrane">VATWLLSGLLMVPYP</span><span class="topo-inside">VYTVVQPVGPRVLQCVHRWPSARVRQ</span><span class="topo-membrane">TWSVLLLLLLFFIPG</span></span>
<span class="topo-line"><span class="topo-membrane">VVMA</span><span class="topo-outside">VAYGLISRELYLGL</span><span class="topo-unknown">RFDGDSDSDSQSRVRNQGGLPGAVHQNGRCRPETGAVGEDSD</span></span>
<span class="topo-line"><span class="topo-unknown">GCYVQLPRSRPALELTALTAPGPGSGSRPTQAKL</span><span class="topo-outside">LAKKRVVRMLLV</span><span class="topo-membrane">IVVLFFLCWLPVYS</span></span>
<span class="topo-line"><span class="topo-membrane">ANT</span><span class="topo-inside">WRAFDGPGAHRALSGAPIS</span><span class="topo-membrane">FIHLLSYASACVNPLV</span><span class="topo-outside">YCFMH</span><span class="topo-unknown">RRFRQACLET</span><span class="topo-outside">C</span><span class="topo-unknown">ARCCPR</span></span>
<span class="topo-line"><span class="topo-unknown">PPRARPREFLEVLFQGPWSHPQFEKGGGSGGGSGGSAWSHPQFEK</span></span>
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
      <td>64</td>
      <td>65</td>
      <td>55</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>57</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>78</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>119</td>
      <td>95</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>138</td>
      <td>111</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>155</td>
      <td>130</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>184</td>
      <td>147</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>199</td>
      <td>176</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>225</td>
      <td>191</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>244</td>
      <td>217</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>258</td>
      <td>236</td>
      <td>249</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>346</td>
      <td>326</td>
      <td>337</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>363</td>
      <td>338</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>382</td>
      <td>355</td>
      <td>373</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>398</td>
      <td>374</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>399</td>
      <td>403</td>
      <td>390</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>413</td>
      <td>395</td>
      <td>404</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>414</td>
      <td>414</td>
      <td>405</td>
      <td>405</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Unique ECL3 α-helical conformation in CCKₐR

The third extracellular loop (ECL3) of CCKₐR adopts a two-turn α-helical conformation that has never been observed before in other class A GPCR structures. This unusual ECL3 architecture may play a role in ligand recognition and receptor activation.

### ECL2 β-hairpin and peptide recognition

ECL2 of CCKₐR forms a β-hairpin structure similar to other peptide-activated GPCRs. Key residue R197 in ECL2 forms a salt bridge with the sulfated tyrosine of CCK peptides, which is critical for high-affinity binding. Mutation R197A greatly diminishes CCK-8 binding.

### Helix VI movement in partial activation

Upon binding the agonist NN9056, an approximately 1 Å inward shift of helix VI in the ligand-binding region was observed compared to antagonist-bound structures. This represents an early conformational change toward receptor activation, though the full active state requires G protein coupling.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/human-cckb-receptor/">Human Cholecystokinin B Receptor (CCKᴅR)</a> — Sister receptor with distinct peptide selectivity; complementary structures from same study
- <a href="/xray-mp-wiki/concepts/signaling-receptors/cck-receptor-peptide-selectivity/">Peptide Selectivity in Cholecystokinin Receptors</a> — Structural basis for CCKₐR preference for sulfated CCK over gastrin
- <a href="/xray-mp-wiki/concepts/signaling-receptors/cck-receptor-stepwise-activation/">Stepwise Activation of Cholecystokinin Receptors</a> — The CCKₐR structures in antagonist, agonist, and G protein-bound states reveal a stepwise activation mechanism
