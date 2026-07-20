---
title: "LPCAT3 (Lysophosphatidylcholine Acyltransferase 3)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##s41467-021-27244-1]
verified: pdb
uniprot_id: A0A1L1RNG8
---

# LPCAT3 (Lysophosphatidylcholine Acyltransferase 3)

<div class="expr-badges"><span class="expr-badge expr-mammalian">Mammalian</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A1L1RNG8">UniProt: A0A1L1RNG8</a>

<span class="expr-badge">Gallus gallus</span>

## Overview

LPCAT3 ([LPC](/xray-mp-wiki/reagents/lipids/lysophosphatidylcholine) Acyltransferase 3), also known as MBOAT5, is a multi-pass membrane protein belonging to the membrane-bound O-acyltransferase (MBOAT) family. It catalyzes the re-acylation step of Lands' cycle, preferentially introducing polyunsaturated acyl chains (particularly arachidonoyl, 20:4) onto the sn-2 position of [LPC](/xray-mp-wiki/reagents/lipids/lysophosphatidylcholine) (LPC). LPCAT3 is the main isoform expressed in major metabolic tissues including liver, small intestine, skeletal muscle, macrophage, and adipocyte. It plays critical roles in lipoprotein production, membrane fluidity regulation, and has been implicated in metabolic disorders such as hyperlipidemia and atherosclerosis.


## Publications

### doi/10.1038##s41467-021-27244-1

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7ewt">7EWT</a></td>
      <td>1.9</td>
      <td>not specified</td>
      <td>Trypsin-digested chicken LPCAT3 core</td>
      <td>apo</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7f3x">7F3X</a></td>
      <td>3.49</td>
      <td>C2</td>
      <td>Chicken LPCAT3 dimer with arachidonoyl-CoA</td>
      <td>arachidonoyl-CoA</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7f40">7F40</a></td>
      <td>3.57</td>
      <td>C2</td>
      <td>Chicken LPCAT3 dimer with 12:0-LPC</td>
      <td>1-dodecanoyl-sn-glycero-3-phosphocholine</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Expi293 mammalian cells
- **Construct**: Chicken LPCAT3 (cLPCAT3), trypsin-digested core for crystallization
- **Notes**: Human and chicken LPCAT3 share 69% protein sequence identity. [Trypsin](/xray-mp-wiki/reagents/additives/trypsin) digestion used to generate crystallizable core construct.

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
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>not specified</td>
      <td>not specified + <a href="/xray-mp-wiki/reagents/detergents/lmng">LMNG</a> (Lauryl <a href="/xray-mp-wiki/reagents/additives/maltose">Maltose</a> Neopentyl Glycol)</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/lmng">LMNG</a> used for solubilization; enables dimer formation unlike <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>not specified</td>
      <td>GDN supplemented with 0.2 mM arachidonoyl-CoA + GDN (<a href="/xray-mp-wiki/reagents/detergents/glyco-diosgenin">GDN</a>)</td>
      <td>Separates oligomeric LPCAT3 from monomers; 0.2 mM arachidonoyl-CoA added to stabilize substrate-bound state</td>
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
      <td><a href="/xray-mp-wiki/reagents/additives/trypsin">Trypsin</a>-digested cLPCAT3 core, 14-28 days</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM Magnesium <a href="/xray-mp-wiki/reagents/buffers/acetate">Acetate Buffer (Sodium Acetate)</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> pH 6.0, 25% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg">PEG (Polyethylene Glycol)</a> 400, 1% (v/v) Formamide</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>16</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals harvested by flash freezing in liquid nitrogen. Cryoprotectant: 32% <a href="/xray-mp-wiki/reagents/additives/peg">PEG (Polyethylene Glycol)</a> 400, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> pH 6.0, 50 mM magnesium <a href="/xray-mp-wiki/reagents/buffers/acetate">Acetate Buffer (Sodium Acetate)</a></td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7ewt">7EWT</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-membrane">ARVAEALGSSEQALRLIVSILMGYPF</span><span class="topo-outside">ALFQRYFLFQKETYLIHLYNV</span><span class="topo-membrane">FTGLSIAYFNFG</span><span class="topo-inside">M</span><span class="topo-membrane">QFFHSLLCVLIQFLI</span><span class="topo-outside">LRLMGRTVTAVF</span><span class="topo-membrane">TTFVFQMTYLMAGYYF</span><span class="topo-unknown">TATEHY</span><span class="topo-inside">D</span><span class="topo-membrane">IKWTMPHCV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LTLKLI</span><span class="topo-outside">GLAIDYY</span><span class="topo-unknown">DGGKDPEL</span><span class="topo-outside">LTPEQRRFAVRG</span><span class="topo-unknown">VPT</span><span class="topo-outside">LLEVSGFSYFYGAFMVGPQFSMTDYQKLAKGEM</span><span class="topo-unknown">TDVPGQ</span><span class="topo-outside">RPNSFVPALKRL</span><span class="topo-membrane">SLGLLFLVTYTLSSPYISE</span><span class="topo-inside">EYLISDDYMEKPFW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">FRC</span><span class="topo-membrane">GYILVWGKIILYKYVTCWLVT</span><span class="topo-outside">EGVCILVGLGYNGNDQNGKPVWDACANMKVWLYETTPLFTGTIASFNINTNAWVARYVFKRL</span><span class="topo-unknown">KFLG</span><span class="topo-outside">NKLL</span><span class="topo-membrane">SQALALFFLAIWHGLHS</span><span class="topo-inside">G</span><span class="topo-membrane">YLVCFQME</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440        </span>
<span class="topo-line"><span class="topo-membrane">LLIVIVE</span><span class="topo-outside">RQVINLVRDSPTLSTLASITAL</span><span class="topo-unknown">QPIF</span><span class="topo-outside">Y</span><span class="topo-membrane">VLQQTNHWMFMGYSLVPFCLF</span><span class="topo-inside">TWDKWMKVYKSIYF</span><span class="topo-membrane">LGHVLFFTLLLVLPYIRKL</span></span>
<details class="topo-details"><summary>Topology coordinates (33 regions)</summary>
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
      <td>42</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>27</td>
      <td>43</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>48</td>
      <td>69</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>60</td>
      <td>90</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>61</td>
      <td>102</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>76</td>
      <td>103</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>88</td>
      <td>118</td>
      <td>129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>104</td>
      <td>130</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>146</td>
      <td>151</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>111</td>
      <td>111</td>
      <td>152</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>126</td>
      <td>153</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>133</td>
      <td>168</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>141</td>
      <td>175</td>
      <td>182</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>142</td>
      <td>153</td>
      <td>183</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>156</td>
      <td>195</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>157</td>
      <td>189</td>
      <td>198</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>195</td>
      <td>231</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>207</td>
      <td>237</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>226</td>
      <td>249</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>243</td>
      <td>268</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>264</td>
      <td>285</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>326</td>
      <td>306</td>
      <td>367</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>330</td>
      <td>368</td>
      <td>371</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>331</td>
      <td>334</td>
      <td>372</td>
      <td>375</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>351</td>
      <td>376</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>352</td>
      <td>393</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>367</td>
      <td>394</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>389</td>
      <td>409</td>
      <td>430</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>393</td>
      <td>431</td>
      <td>434</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>394</td>
      <td>394</td>
      <td>435</td>
      <td>435</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>415</td>
      <td>436</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>416</td>
      <td>429</td>
      <td>457</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>448</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f3x">7F3X</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGAERDESGAGAAVLVPLLGFGSNRPAGPAEKMAVAGSGWS</span><span class="topo-outside">LARVAEALGSSEQALRL</span><span class="topo-membrane">IVSILMGYPFALFQRYFL</span><span class="topo-inside">FQKETY</span><span class="topo-membrane">LIHLYNVFTGLSIAYFNF</span><span class="topo-outside">GMQ</span><span class="topo-membrane">FFHSLLCVLIQFL</span><span class="topo-inside">ILRL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MGRTVTAVFTT</span><span class="topo-membrane">FVFQMTYLMAGYYFT</span><span class="topo-outside">ATEHYDI</span><span class="topo-membrane">KWTMPHCVLTLKLI</span><span class="topo-inside">GLAIDYYDGGKDPELLTPEQRRFAVRGVPTLLEV</span><span class="topo-unknown">SGFSYFYGAFMVGPQF</span><span class="topo-inside">SMTDYQKLAKGEMTDVPGQRPNS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">FVPALKRLSLGLLFL</span><span class="topo-outside">VTYTLSSPYISEEYLISDDYMEKPFWFRCGYILVWG</span><span class="topo-membrane">KIILYKYVTCWLVTEGVCILVG</span><span class="topo-inside">LGYNGNDQNGKPVWDACANMKVWLYETTPLFTGTIASFNINTNAWVA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">RYVFKRLKFLGNKLLSQA</span><span class="topo-membrane">LALFFLAIWHGLHS</span><span class="topo-outside">G</span><span class="topo-membrane">YLVCFQMELLIVIVE</span><span class="topo-inside">RQVINLVRDSPTLSTLASITA</span><span class="topo-membrane">LQPIFYVLQQTNHWMFMGYSLVPFC</span><span class="topo-outside">LFTWDKWMKVYKSIYF</span><span class="topo-membrane">LGHVLFFTLL</span></span>
<span class="topo-ruler">       490       500 </span>
<span class="topo-line"><span class="topo-membrane">LVL</span><span class="topo-inside">PYIRKLL</span><span class="topo-unknown">VPRKEKLKKAE</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>41</td>
      <td>1</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>42</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>76</td>
      <td>59</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>82</td>
      <td>77</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>103</td>
      <td>101</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>116</td>
      <td>104</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>117</td>
      <td>131</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>146</td>
      <td>132</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>153</td>
      <td>147</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>167</td>
      <td>154</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>201</td>
      <td>168</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>217</td>
      <td>202</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>218</td>
      <td>240</td>
      <td>218</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>291</td>
      <td>256</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>378</td>
      <td>314</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>392</td>
      <td>379</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>393</td>
      <td>393</td>
      <td>393</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>408</td>
      <td>394</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>429</td>
      <td>409</td>
      <td>429</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>454</td>
      <td>430</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>470</td>
      <td>455</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>483</td>
      <td>471</td>
      <td>483</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>484</td>
      <td>490</td>
      <td>484</td>
      <td>490</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>491</td>
      <td>501</td>
      <td>491</td>
      <td>501</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f3x">7F3X</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGAERDESGAGAAVLVPLLGFGSNRPAGPAEKMAVAGSGWS</span><span class="topo-outside">LARVAEALGSSEQALRL</span><span class="topo-membrane">IVSILMGYPFALFQRYFL</span><span class="topo-inside">FQKETY</span><span class="topo-membrane">LIHLYNVFTGLSIAYFNF</span><span class="topo-outside">GMQ</span><span class="topo-membrane">FFHSLLCVLIQFL</span><span class="topo-inside">ILRL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MGRTVTAVFTT</span><span class="topo-membrane">FVFQMTYLMAGYYFTA</span><span class="topo-outside">TEHYDI</span><span class="topo-membrane">KWTMPHCVLTLKLI</span><span class="topo-inside">GLAIDYYDGGKDPELLTPEQRRFAVRGVPTLLEV</span><span class="topo-unknown">SGFSYFYGAFMVGPQF</span><span class="topo-inside">SMTDYQKLAKGEMTDVPGQRPNS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">FVPALKRLSLGLLFL</span><span class="topo-outside">VTYTLSSPYISEEYLISDDYMEKPFWFRCGYILVWG</span><span class="topo-membrane">KIILYKYVTCWLVTEGVCILV</span><span class="topo-inside">GLGYNGNDQNGKPVWDACANMKVWLYETTPLFTGTIASFNINTNAWVA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">RYVFKRLKFLGNKLLSQA</span><span class="topo-membrane">LALFFLAIWHGLHS</span><span class="topo-outside">G</span><span class="topo-membrane">YLVCFQMELLIVIVE</span><span class="topo-inside">RQVINLVRDSPTLSTLASITA</span><span class="topo-membrane">LQPIFYVLQQTNHWMFMGYSLVPFC</span><span class="topo-outside">LFTWDKWMKVYKSIYF</span><span class="topo-membrane">LGHVLFFTLL</span></span>
<span class="topo-ruler">       490       500 </span>
<span class="topo-line"><span class="topo-membrane">LVL</span><span class="topo-inside">PYIRKLL</span><span class="topo-unknown">VPRKEKLKKAE</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>41</td>
      <td>1</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>42</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>76</td>
      <td>59</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>82</td>
      <td>77</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>103</td>
      <td>101</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>116</td>
      <td>104</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>117</td>
      <td>131</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>147</td>
      <td>132</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>153</td>
      <td>148</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>167</td>
      <td>154</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>201</td>
      <td>168</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>217</td>
      <td>202</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>218</td>
      <td>240</td>
      <td>218</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>291</td>
      <td>256</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>312</td>
      <td>292</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>378</td>
      <td>313</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>392</td>
      <td>379</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>393</td>
      <td>393</td>
      <td>393</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>408</td>
      <td>394</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>429</td>
      <td>409</td>
      <td>429</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>454</td>
      <td>430</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>470</td>
      <td>455</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>483</td>
      <td>471</td>
      <td>483</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>484</td>
      <td>490</td>
      <td>484</td>
      <td>490</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>491</td>
      <td>501</td>
      <td>491</td>
      <td>501</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f40">7F40</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGAERDESGAGAAVLVPLLGFGSNRPAGPAEKMAVAGSGWS</span><span class="topo-inside">LARVAEALGSSEQALRL</span><span class="topo-membrane">IVSILMGYPFALFQRYFLFQ</span><span class="topo-outside">KETY</span><span class="topo-membrane">LIHLYNVFTGLSIAYFN</span><span class="topo-inside">FGMQ</span><span class="topo-membrane">FFHSLLCVLIQFLIL</span><span class="topo-outside">RL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">MGRTVTAVF</span><span class="topo-membrane">TTFVFQMTYLMAGYY</span><span class="topo-inside">FTATEHYDIK</span><span class="topo-membrane">WTMPHCVLTLKLIGLA</span><span class="topo-outside">IDYYDGGKDPELLTPEQRRFAVRGVPTL</span><span class="topo-unknown">LEVSGFSYFYGAFMVGPQFS</span><span class="topo-outside">MTDYQKLAKGEMTDVPGQR</span><span class="topo-membrane">PNS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">FVPALKRLSLGLLFL</span><span class="topo-inside">VTYTLSSPYISEEYLISDDYMEKPFWFRCGYILVWG</span><span class="topo-membrane">KIILYKYVTCWLVTEGVCILVGLG</span><span class="topo-outside">YNGNDQNGKPVWDACANMKVWLYETTPLFTGTIASFNINTNAWVA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">RYVFKRLKFLGNKL</span><span class="topo-membrane">LSQALALFFLAIWHGLHS</span><span class="topo-inside">G</span><span class="topo-membrane">YLVCFQMELLIVIVERQVI</span><span class="topo-outside">NLVRDSPTLSTLASITA</span><span class="topo-membrane">LQPIFYVLQQTNHWMFMGYSLVPF</span><span class="topo-inside">CLFTWDKWMKVYKSIYF</span><span class="topo-membrane">LGHVLFFTLL</span></span>
<span class="topo-ruler">       490       500 </span>
<span class="topo-line"><span class="topo-membrane">LVLPYI</span><span class="topo-outside">RKLL</span><span class="topo-unknown">VPRKEKLKKAE</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>41</td>
      <td>1</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>42</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>78</td>
      <td>59</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>82</td>
      <td>79</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>99</td>
      <td>83</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>103</td>
      <td>100</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>118</td>
      <td>104</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>129</td>
      <td>119</td>
      <td>129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>144</td>
      <td>130</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>154</td>
      <td>145</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>170</td>
      <td>155</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>198</td>
      <td>171</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>219</td>
      <td>237</td>
      <td>219</td>
      <td>237</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>255</td>
      <td>238</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>291</td>
      <td>256</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>315</td>
      <td>292</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>374</td>
      <td>316</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>392</td>
      <td>375</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>393</td>
      <td>393</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>412</td>
      <td>394</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>429</td>
      <td>413</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>453</td>
      <td>430</td>
      <td>453</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>470</td>
      <td>454</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>486</td>
      <td>471</td>
      <td>486</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>487</td>
      <td>490</td>
      <td>487</td>
      <td>490</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>491</td>
      <td>501</td>
      <td>491</td>
      <td>501</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f40">7F40</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGAERDESGAGAAVLVPLLGFGSNRPAGPAEKMAVAGSGWS</span><span class="topo-inside">LARVAEALGSSEQALRL</span><span class="topo-membrane">IVSILMGYPFALFQRYFLFQ</span><span class="topo-outside">KETY</span><span class="topo-membrane">LIHLYNVFTGLSIAYFN</span><span class="topo-inside">FGMQ</span><span class="topo-membrane">FFHSLLCVLIQFLIL</span><span class="topo-outside">RL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">MGRTVTAVF</span><span class="topo-membrane">TTFVFQMTYLMAGYY</span><span class="topo-inside">FTATEHYDIK</span><span class="topo-membrane">WTMPHCVLTLKLIGL</span><span class="topo-outside">AIDYYDGGKDPELLTPEQRRFAVRGVPTL</span><span class="topo-unknown">LEVSGFSYFYGAFMVGPQFS</span><span class="topo-outside">MTDYQKLAKGEMTDVPGQR</span><span class="topo-membrane">PNS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">FVPALKRLSLGLLFL</span><span class="topo-inside">VTYTLSSPYISEEYLISDDYMEKPFWFRCGYILVWG</span><span class="topo-membrane">KIILYKYVTCWLVTEGVCILVGLG</span><span class="topo-outside">YNGNDQNGKPVWDACANMKVWLYETTPLFTGTIASFNINTNAWVA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">RYVFKRLKFLGNKL</span><span class="topo-membrane">LSQALALFFLAIWHGLHS</span><span class="topo-inside">G</span><span class="topo-membrane">YLVCFQMELLIVIVERQVI</span><span class="topo-outside">NLVRDSPTLSTLASITA</span><span class="topo-membrane">LQPIFYVLQQTNHWMFMGYSLVPF</span><span class="topo-inside">CLFTWDKWMKVYKSIYF</span><span class="topo-membrane">LGHVLFFTLL</span></span>
<span class="topo-ruler">       490       500 </span>
<span class="topo-line"><span class="topo-membrane">LVLPYI</span><span class="topo-outside">RKLL</span><span class="topo-unknown">VPRKEKLKKAE</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>41</td>
      <td>1</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>42</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>78</td>
      <td>59</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>82</td>
      <td>79</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>99</td>
      <td>83</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>103</td>
      <td>100</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>118</td>
      <td>104</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>129</td>
      <td>119</td>
      <td>129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>144</td>
      <td>130</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>154</td>
      <td>145</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>169</td>
      <td>155</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>198</td>
      <td>170</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>219</td>
      <td>237</td>
      <td>219</td>
      <td>237</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>255</td>
      <td>238</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>291</td>
      <td>256</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>315</td>
      <td>292</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>374</td>
      <td>316</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>392</td>
      <td>375</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>393</td>
      <td>393</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>412</td>
      <td>394</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>429</td>
      <td>413</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>453</td>
      <td>430</td>
      <td>453</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>470</td>
      <td>454</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>486</td>
      <td>471</td>
      <td>486</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>487</td>
      <td>490</td>
      <td>487</td>
      <td>490</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>491</td>
      <td>501</td>
      <td>491</td>
      <td>501</td>
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

### T-shaped reaction chamber with lateral gate

LPCAT3 features a T-shaped reaction chamber with a lateral gate formed by TM1 and TM6 helices. The chamber comprises a horizontal tunnel for the acyl acceptor (LPC) and a vertical tunnel for the acyl donor (acyl-CoA), connected near the catalytic center. A side pocket extends from the vertical tunnel to accommodate the bulky polyunsaturated acyl chain of arachidonoyl-CoA.

### Substrate preference mechanism

The side pocket's near-to-90 degree bending routine from the vertical tunnel favors polyunsaturated acyl chains (e.g., 20:4) which adopt a ring-shape structure fitting the pocket well. Saturated acyl chains in all-trans configuration suffer from steric hindrance, explaining LPCAT3's preference for polyunsaturated over saturated fatty acids.

### Catalytic mechanism

The catalytic residues H388 and N352 are positioned near the junction of the horizontal and vertical tunnels. N352 is implied to act as a protonation reagent for the thioester bond. The catalytic chamber allows both substrates (LPC and arachidonoyl-CoA) to bind simultaneously, with the acyl chain positioned for transfer.


## Cross-References

- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — Peg used in purification or crystallization buffer
- <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a> — Buffer component used in purification
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification and crystallization
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Detergent used in purification and crystallization
- <a href="/xray-mp-wiki/reagents/detergents/glyco-diosgenin/">GDN</a> — Detergent used in purification and crystallization
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> — Buffer component used in purification
- <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> — Maltose used in purification or crystallization buffer
- <a href="/xray-mp-wiki/reagents/lipids/lysophosphatidylcholine/">LPC</a> — Lipid component used in crystallization or solubilization
- <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> — Trypsin used in purification or crystallization buffer
