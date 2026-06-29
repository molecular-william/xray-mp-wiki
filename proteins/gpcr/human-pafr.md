---
title: "Human Platelet-Activating Factor Receptor (PAFR)"
created: 2018-05-28
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-018-0068-y]
verified: false
---

# Human Platelet-Activating Factor Receptor (PAFR)

## Overview

The human platelet-activating factor receptor (PAFR) is a class A [G Protein](/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-coupling/)-coupled receptor that responds to platelet-activating factor (PAF), a phospholipid mediator of cell-to-cell communication involved in inflammation, immune responses, and cardiovascular regulation. The first crystal structures of PAFR were determined in complex with the antagonist SR 27417 at 2.8 A resolution (PDB 5ZKP) and the inverse agonist ABT-491 at 2.9 A resolution (PDB 5ZKQ) (Cao et al., 2018). The structures reveal an unusual conformation in the SR 27417-bound state, with the intracellular tips of helices II and IV shifting outward by 13 A and 4 A, respectively, and helix VIII adopting an inward conformation across the helical bundle. Combined with smFRET and functional assays, the structures suggest that the conformational change in the helical bundle is ligand dependent and plays a critical role in PAFR activation.

## Publications

### doi/10.1038##s41594-018-0068-y

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5zkp">5ZKP</a></td>
      <td>2.8 A</td>
      <td>P 21 21 21</td>
      <td>Human PAFR with ICL3 replaced by residues 2-148 of modified flavodoxin (P2A Y98W), C-terminal truncation (C317-N342 removed), five point mutations (F116Y, N169D, A230D, V234A, D289N), N-terminal HA signal peptide, C-terminal PreScission site and decahistidine/FLAG tag</td>
      <td>SR 27417 (antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5zkq">5ZKQ</a></td>
      <td>2.9 A</td>
      <td>P 21 21 21</td>
      <td>Human PAFR with ICL3 replaced by mT4L fusion, C-terminal truncation (C317-N342 removed), five point mutations (F116Y, N169D, A230D, V234A, D289N), N-terminal HA signal peptide, C-terminal PreScission site and decahistidine/FLAG tag</td>
      <td>ABT-491 (inverse agonist)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Sf9](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) insect cells ([Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: Human PAFR with ICL3 replaced by flavodoxin or mT4L fusion, C-terminal truncation (C317-N342), five point mutations (F116Y, N169D, A230D, V234A, D289N), N-terminal HA signal peptide, C-terminal PreScission site and decahistidine/FLAG tag

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
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus</a> infection of <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9</a> cells at MOI 5 for 48 h; 1 uM SR 27417 or ABT-491 added during expression</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 10 mM MgCl2, 20 mM KCl, EDTA-free <a href="/xray-mp-wiki/reagents/additives/protease-inhibitor-cocktail/">protease inhibitor cocktail</a> + --</td>
      <td>Cells disrupted by hypotonic buffer and Dounce homogenization; extensive washing of membranes by repeated centrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>30 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 5 mM MgCl2, 10 mM KCl, 7.5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 25 uM ligand (SR 27417 or ABT-491), 1 mg/ml <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">iodoacetamide</a>, EDTA-free <a href="/xray-mp-wiki/reagents/additives/protease-inhibitor-cocktail/">protease inhibitor cocktail</a> + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">cholesterol hemisuccinate (CHS)</a></td>
      <td>Membranes solubilized at 0.5% DDM + 0.1% CHS</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin (Clontech)</td>
      <td>Same as solubilization buffer with ligand + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Imidazole removed via PD MiniTrap G-25 column after elution</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission protease</a> cleavage (overnight)</td>
      <td>--</td>
      <td>Same as solubilization buffer + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Histidine-tagged PreScission protease (30 ul) treated overnight to remove C-terminal His tag</td>
    </tr>
    <tr>
      <td>Negative purification</td>
      <td>Negative <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> superflow resin (Qiagen)</td>
      <td>Same as solubilization buffer + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Cleaved His tag and PreScission protease removed by passage through Ni-NTA resin</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Concentration by ultrafiltration</td>
      <td>--</td>
      <td>Same as solubilization buffer + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>PAFR-flavodoxin concentrated to 30-40 mg/ml; PAFR-mT4L concentrated to 40-45 mg/ml; Vivaspin concentrator with 100 kDa MWCO</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PAFR-flavodoxin (for SR 27417 complex) or PAFR-mT4L (for ABT-491 complex), concentrated to 30-45 mg/ml in purification buffer</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoirs with 32-40% PEG 400; crystals flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein reconstituted into LCP with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>.
PAFR-SR 27417 (flavodoxin fusion): 30-40 mg/ml, 28-30% PEG 400, 100 mM Na <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate</a>
pH 5.0, 100 mM Na malonate pH 7.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, no sarcosine. PAFR-ABT-491
(mT4L fusion): 40-45 mg/ml, 30-32% PEG 400, 100 mM Na <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate</a> pH 5.0, 100 mM
Na malonate pH 7.0, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 3% sarcosine. Data merged from 36 crystals
(SR 27417) and 52 crystals (ABT-491) due to radiation damage.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zkp">5ZKP</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GAPEPHD</span><span class="topo-outside">SSHMDSEFRYTL</span><span class="topo-membrane">FPIVYSIIFVLGVIANGYVLWVFAR</span><span class="topo-inside">LYPCKKFN</span><span class="topo-membrane">EIKIFMVN</span></span>
<span class="topo-line"><span class="topo-membrane">LTMADMLFLITLPLWI</span><span class="topo-outside">VYYQNQGNWILPKFLCN</span><span class="topo-membrane">VAGCLFFINTYCSVAFLGVITYNRY</span><span class="topo-inside">QA</span></span>
<span class="topo-line"><span class="topo-inside">VTRPI</span><span class="topo-unknown">KTAQANTRKRGISL</span><span class="topo-inside">S</span><span class="topo-membrane">LVIWVAIVGAASYFL</span><span class="topo-outside">ILDSTNTVPDSAGSGDVTRCFEHYE</span></span>
<span class="topo-line"><span class="topo-outside">KGSVPV</span><span class="topo-membrane">LIIHIFIVFSFFLVFLIILFCNLVII</span><span class="topo-inside">RTLLMQAKALIVYGSTTGNTEYTAETIA</span></span>
<span class="topo-line"><span class="topo-inside">RELADAGYEVDSRDAASVEAGGLFEGFDLVLLGCSTWGDDSIELQDDFIPLFDSLEETGA</span></span>
<span class="topo-line"><span class="topo-inside">QGRKVACFGCGDSSWEYFCGAVDAIEEKLKNLGAEIVQDGLRIDGDPRAARDDIVGWAHD</span></span>
<span class="topo-line"><span class="topo-inside">VRGAIAEVKRRDL</span><span class="topo-membrane">WMACTVLAVFIICFVPHHVVQLPW</span><span class="topo-outside">TLAELGFQDSKFHQAINDA</span><span class="topo-membrane">HQVT</span></span>
<span class="topo-line"><span class="topo-membrane">LCLLSTNCVLNPVIYCFLTK</span><span class="topo-inside">KFRKHLTEKFYSMRSSR</span><span class="topo-unknown">KEFLEVLFQ</span></span>
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
      <td>-1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>19</td>
      <td>6</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>44</td>
      <td>18</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>52</td>
      <td>43</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>76</td>
      <td>51</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>75</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>118</td>
      <td>92</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>125</td>
      <td>117</td>
      <td>123</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>139</td>
      <td>124</td>
      <td>137</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>140</td>
      <td>140</td>
      <td>138</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>155</td>
      <td>139</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>186</td>
      <td>154</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>212</td>
      <td>185</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>218</td>
      <td>211</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>365</td>
      <td>1001</td>
      <td>1147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>373</td>
      <td>224</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>397</td>
      <td>232</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>416</td>
      <td>256</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>440</td>
      <td>275</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>441</td>
      <td>457</td>
      <td>299</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>466</td>
      <td>316</td>
      <td>324</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zkq">5ZKQ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GAPEP</span><span class="topo-outside">HDSSHMDSEFRYT</span><span class="topo-membrane">LFPIVYSIIFVLGVIANGYVLWVFA</span><span class="topo-inside">RL</span><span class="topo-unknown">YPCKK</span><span class="topo-inside">FNEIK</span><span class="topo-membrane">IFMVN</span></span>
<span class="topo-line"><span class="topo-membrane">LTMADMLFLITLPLWIVYY</span><span class="topo-outside">QNQGNWIL</span><span class="topo-membrane">PKFLCNVAGCLFFINTYCSVAFLGVITY</span><span class="topo-inside">NRYQA</span></span>
<span class="topo-line"><span class="topo-inside">VTRP</span><span class="topo-unknown">IKTA</span><span class="topo-inside">QANTRKRG</span><span class="topo-membrane">ISLSLVIWVAIVGAASYFLIL</span><span class="topo-outside">DSTNTVPDSAGSGDVTRCFEHYE</span></span>
<span class="topo-line"><span class="topo-outside">KGSV</span><span class="topo-membrane">PVLIIHIFIVFSFFLVFLIILFCNL</span><span class="topo-inside">VIIRTLLMQP</span><span class="topo-unknown">VNIFEMLRIDEGGGSGGDEAE</span></span>
<span class="topo-line"><span class="topo-unknown">KLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQK</span></span>
<span class="topo-line"><span class="topo-unknown">RWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAY</span><span class="topo-inside">AEVKRRDLW</span><span class="topo-membrane">MACTVLAVFIICFV</span></span>
<span class="topo-line"><span class="topo-membrane">PHHVVQLPWTL</span><span class="topo-outside">AELGFQDSKFHQA</span><span class="topo-membrane">INDAHQVTLCLLSTNCVLNPVIYCF</span><span class="topo-inside">LT</span><span class="topo-unknown">KKFRKHLTE</span></span>
<span class="topo-line"><span class="topo-unknown">KFYSMRSSRKEFLEVLFQ</span></span>
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
      <td>-1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>18</td>
      <td>4</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>43</td>
      <td>17</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>45</td>
      <td>42</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>50</td>
      <td>44</td>
      <td>48</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>55</td>
      <td>49</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>79</td>
      <td>54</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>87</td>
      <td>78</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>115</td>
      <td>86</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>124</td>
      <td>114</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>128</td>
      <td>123</td>
      <td>126</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>129</td>
      <td>136</td>
      <td>127</td>
      <td>134</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>157</td>
      <td>135</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>184</td>
      <td>156</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>209</td>
      <td>183</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>210</td>
      <td>219</td>
      <td>208</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>346</td>
      <td>224</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>371</td>
      <td>233</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>384</td>
      <td>258</td>
      <td>270</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>409</td>
      <td>271</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>411</td>
      <td>296</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>438</td>
      <td>298</td>
      <td>324</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### First crystal structures of PAFR reveal ligand-dependent conformational changes

The crystal structures of PAFR bound to antagonist SR 27417 (2.8 A) and inverse agonist ABT-491 (2.9 A) are the first reported structures of this receptor. The SR 27417-bound structure shows an unusual conformation where the intracellular tips of helices II and IV shift outward by 13 A and 4 A, respectively, compared to the ABT-491-bound structure, while helix VIII adopts an inward conformation across the helical bundle.

### Unique helix VIII conformation in the SR 27417-bound state

PAFR helix VIII in the SR 27417 complex adopts a conformation not seen in other known GPCR structures. It extends across the helical bundle flanked by ICL1 and ICL2, with its C terminus wedged into a gap between helices II and IV. Residue F300 on the N terminus of helix VIII, together with L304, forms a hydrophobic-packing core with F295(7.55) and L296(7.56) in helix VII. This unique conformation may facilitate G-protein coupling.

### Helices II and IV as key regulators of PAFR activation

smFRET assays confirmed the conformational difference between SR 27417- and ABT-491-bound states. The FRET efficiency for PAFR-SR 27417 was 0.75 vs 0.90 for PAFR-ABT-491, consistent with a longer distance between intracellular tips of helices II and IV in the SR 27417 complex. The agonist PAF-bound receptor showed an FRET efficiency of 0.70, suggesting helices II and IV in the agonist-bound receptor adopt an outward conformation similar to the SR 27417 complex. Mutations F66(2.53)A, F97(3.32)A, and F152(4.60)A decreased PAFR-mediated IP production.

### Lipid receptor structural features

Similarly to other lipid receptors (S1P1, FFAR1, LPA1, CB1), the PAFR ligand-binding pocket is capped by the N terminus and extracellular loops (mainly ECL2). The roof-like structure over the binding pocket may be a general structural feature shared by lipid GPCRs. Unlike most class A GPCRs, PAFR has a valine at position 5.50 (instead of the conserved proline), resulting in a straight helix V without the canonical helical bend.

### PAF binding mode revealed by molecular docking

Molecular docking of PAF into the PAFR-SR 27417 structure revealed that the sn-1 alkyl chain extends into a tunnel formed by aromatic and hydrophobic residues of helices III-VI and ECL2, with its tail squeezing into the lipid bilayer between helices IV and V. The sn-2 and sn-3 groups occupy a subpocket bordered by helices I, II, VI, VII and ECL2. Mutagenesis of residues in the subpocket (W73(2.60)A, Y77(2.64)A, H248(6.51)W, W255(6.58)A, H275(7.35)A, H275(7.35)W) substantially decreased PAF binding.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent (0.5%) used for membrane solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Stabilizing additive (0.1%) used with DDM in purification buffers
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — Buffer (30 mM, pH 7.5) used in purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — Salt (150 mM) included in purification buffer
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Cryoprotectant/stabilizer (7.5%) in purification buffer
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used for LCP crystallization matrix
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — LCP method used for both PAFR complexes
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> — Protein expressed in Sf9 cells using baculovirus system
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9 Insect Cells</a> — Expression host for recombinant PAFR production
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON IMAC Resin</a> — Used for affinity purification of PAFR
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Resin</a> — Used for negative purification after tag cleavage
- <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> — Added (1 mg/ml) during solubilization
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/">GPCR Active Conformation</a> — PAFR structures reveal ligand-dependent conformational changes in helical bundle
- <a href="/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/">Bovine Rhodopsin</a> — Prototypical class A GPCR for structural comparison
