---
title: "CIR Chloride-Pumping Rhodopsin from Nonlabens marinus"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NCOMMS12677, doi/10.1073##pnas.2020486118, doi/10.1073##pnas.2117433119, doi/10.1126##science.abj6663, doi/10.1126##sciadv.aay2042]
verified: agent
uniprot_id: W8VZW3
---

# CIR Chloride-Pumping Rhodopsin from Nonlabens marinus

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/W8VZW3">UniProt: W8VZW3</a>

<span class="expr-badge">Nonlabens marinus S1-08</span>

## Overview

CIR (Chloride-pumping Rhodopsin/rhodopsin 3, also called NmHR) from the
flavobacterium Nonlabens marinus S1-08 is a light-driven inward chloride
pump containing an NTQ motif (Asn98, Thr102, Gln109) in its putative ion
conduction pathway, distinct from the TSA motif of archaeal
[Halorhodopsin](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/). The crystal structures were determined under multiple
conditions using [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization, revealing
chloride-binding sites around the protonated Schiff base (PSB) of the
[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore. Time-resolved serial femtosecond crystallography
(TR-SFX) combined with time-resolved spectroscopy and multiscale
simulations elucidated the complete molecular mechanism of chloride
transport from picosecond to millisecond timescales. Key features include
an anion-&#x3C0; interaction between chloride and the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) &#x3C0;-system,
a steric molecular gate (Asn98) preventing backflow, and an electrostatic
gate (Arg95-Asp231 salt bridge) ensuring unidirectional transport.

## Publications

### doi/10.1038##NCOMMS12677

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5g28">5G28</a></td>
      <td>2.0</td>
      <td>P 3 2 1</td>
      <td>CIR from Nonlabens marinus S1-08, type A crystal at pH 6.0</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, chloride ion</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5g54">5G54</a></td>
      <td>1.56</td>
      <td>P 3 2 1</td>
      <td>CIR from Nonlabens marinus S1-08, type B crystal at pH 4.5</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, chloride ion</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5g2a">5G2A</a></td>
      <td></td>
      <td>—</td>
      <td>CIR from Nonlabens marinus S1-08, bromide-soaked</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, bromide ion</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5g2d">5G2D</a></td>
      <td></td>
      <td>—</td>
      <td>CIR T102N mutant</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, chloride ion</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5g2c">5G2C</a></td>
      <td>2.0</td>
      <td>P1 (T102D mutant crystal)</td>
      <td>ClR T102D mutant</td>
      <td>All-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (chloride binding prevented)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-CodonPlus
- **Construct**: CIR from Nonlabens marinus S1-08 with C-terminal 6xHis tag (residues 1-272)
- **Induction**: 0.5 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) + 50 uM all-trans-retinal for 6-8 h at 30 C

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
      <td>Cell harvest and lysis</td>
      <td>Centrifugation and mechanical disruption</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization and <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 150 mM NaCl + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (in meso) crystallization</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> in reservoir solution</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Type A crystals at pH 6.0 diffracted to 2.0 A; type B crystals at pH 4.5 diffracted to 1.56 A. Data at Pohang Accelerator Laboratory. Structures solved by molecular replacement using <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> (PDB 1C3W).</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5g28">5G28</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">PNSM</span><span class="topo-outside">KNIESLFDYSAGQFEF</span><span class="topo-membrane">IDHLLTMGVGVHFAALIFFLVVSQ</span><span class="topo-inside">FVAPKYR</span><span class="topo-membrane">IATALSCIVMVSAGLILNSQAV</span><span class="topo-outside">MWTDAYAYVDGSYQLQDLTFS</span><span class="topo-membrane">NGYRYVNWMATIPCLLLQLLIV</span><span class="topo-inside">LNLK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">GKEL</span><span class="topo-membrane">FSTATWLILAAWGMIITGYVGQLYE</span><span class="topo-outside">VDDI</span><span class="topo-membrane">AQLMIWGAVSTAFFVVMNWIVGTKI</span><span class="topo-inside">FKNRATMLGGTDST</span><span class="topo-membrane">ITKVFWLMMFAWTLYPIAYLVPAF</span><span class="topo-outside">MNNADGVV</span><span class="topo-membrane">LRQLLFTIADISSKVI</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-membrane">YGLMITYIA</span><span class="topo-inside">IQQSAAAGYVPAQQALGRI</span><span class="topo-unknown">GMDSKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>4</td>
      <td>-2</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>20</td>
      <td>2</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>44</td>
      <td>18</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>51</td>
      <td>42</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>73</td>
      <td>49</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>94</td>
      <td>71</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>116</td>
      <td>92</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>124</td>
      <td>114</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>149</td>
      <td>122</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>153</td>
      <td>147</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>178</td>
      <td>151</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>192</td>
      <td>176</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>216</td>
      <td>190</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>224</td>
      <td>214</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>249</td>
      <td>222</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>268</td>
      <td>247</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>275</td>
      <td>266</td>
      <td>272</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5g54">5G54</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">PNSMKNIESLFDYSAGQFEF</span><span class="topo-membrane">IDHLLTMGVGVHFAALIFFLVVSQ</span><span class="topo-inside">FVAPKYR</span><span class="topo-membrane">IATALSCIVMVSAGLILNSQAV</span><span class="topo-outside">MWTDAYAYVDGSYQLQDLTFS</span><span class="topo-membrane">NGYRYVNWMATIPCLLLQLLIV</span><span class="topo-inside">LNLK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">GKEL</span><span class="topo-membrane">FSTATWLILAAWGMIITGYVGQLYE</span><span class="topo-outside">VDDI</span><span class="topo-membrane">AQLMIWGAVSTAFFVVMNWIVGTKI</span><span class="topo-inside">FKNRATMLGGTDSTI</span><span class="topo-membrane">TKVFWLMMFAWTLYPIAYLVPAFM</span><span class="topo-outside">NNAD</span><span class="topo-membrane">GVVLRQLLFTIADISSKVI</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-membrane">YGLMITY</span><span class="topo-inside">IAIQQSAAAGYVPAQQALGRIG</span><span class="topo-unknown">MDSKAA</span></span>
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
      <td>20</td>
      <td>-2</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>44</td>
      <td>18</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>51</td>
      <td>42</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>73</td>
      <td>49</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>94</td>
      <td>71</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>116</td>
      <td>92</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>124</td>
      <td>114</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>149</td>
      <td>122</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>153</td>
      <td>147</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>178</td>
      <td>151</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>193</td>
      <td>176</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>217</td>
      <td>191</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>221</td>
      <td>215</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>247</td>
      <td>219</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>248</td>
      <td>269</td>
      <td>245</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>275</td>
      <td>267</td>
      <td>272</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5g2a">5G2A</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">PNSM</span><span class="topo-outside">KNIESLFDYSAGQF</span><span class="topo-membrane">EFIDHLLTMGVGVHFAALIFFLV</span><span class="topo-inside">VSQFVAPKYRIA</span><span class="topo-membrane">TALSCIVMVSAGLILNSQAVMWTD</span><span class="topo-outside">AYAYVDGSYQLQDLTF</span><span class="topo-membrane">SNGYRYVNWMATIPCLLLQLL</span><span class="topo-inside">IVLNLK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">GKELF</span><span class="topo-membrane">STATWLILAAWGMIITGYVGQLYE</span><span class="topo-outside">VDDIAQ</span><span class="topo-membrane">LMIWGAVSTAFFVVMNWIVGTKIF</span><span class="topo-inside">KNRATMLGGTDST</span><span class="topo-membrane">ITKVFWLMMFAWTLYPIAYLVPAF</span><span class="topo-outside">MNNADG</span><span class="topo-membrane">VVLRQLLFTIADISSKVI</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-membrane">YGLMIT</span><span class="topo-inside">YIAIQQSAAAGYVPAQQALGRI</span><span class="topo-unknown">GMDSKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>5</td>
      <td>18</td>
      <td>2</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>41</td>
      <td>16</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>53</td>
      <td>39</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>77</td>
      <td>51</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>93</td>
      <td>75</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>114</td>
      <td>91</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>125</td>
      <td>112</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>149</td>
      <td>123</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>155</td>
      <td>147</td>
      <td>152</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>179</td>
      <td>153</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>192</td>
      <td>177</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>216</td>
      <td>190</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>222</td>
      <td>214</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>246</td>
      <td>220</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>268</td>
      <td>244</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5g2d">5G2D</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">P</span><span class="topo-inside">NSMKNIESLFDYSAGQFE</span><span class="topo-membrane">FIDHLLTMGVGVHFAALIFFLVV</span><span class="topo-outside">SQFVAPKYRI</span><span class="topo-membrane">ATALSCIVMVSAGLILNSQAVMWT</span><span class="topo-inside">DAYAYVDGSYQLQDLTF</span><span class="topo-membrane">SNGYRYVNWMANIPCLLLQLLIVL</span><span class="topo-outside">NLK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GK</span><span class="topo-membrane">ELFSTATWLILAAWGMIITGYVGQ</span><span class="topo-inside">LYEVDDIAQL</span><span class="topo-membrane">MIWGAVSTAFFVVMNWIVGTKIFK</span><span class="topo-outside">NRATMLGGTDST</span><span class="topo-membrane">ITKVFWLMMFAWTLYPIAYLV</span><span class="topo-inside">PAFMNNADGV</span><span class="topo-membrane">VLRQLLFTIADISSKVI</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-membrane">YGLMITY</span><span class="topo-outside">IAIQQSAAAGYVPAQQALGRI</span><span class="topo-unknown">GMDSKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>19</td>
      <td>-1</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>42</td>
      <td>17</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>52</td>
      <td>40</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>76</td>
      <td>50</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>74</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>117</td>
      <td>91</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>122</td>
      <td>115</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>123</td>
      <td>146</td>
      <td>120</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>156</td>
      <td>144</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>180</td>
      <td>154</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>192</td>
      <td>178</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>213</td>
      <td>190</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>223</td>
      <td>211</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>247</td>
      <td>221</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>248</td>
      <td>268</td>
      <td>245</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5g2c">5G2C</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PNSMKNIESLFDYSAGQFE</span><span class="topo-membrane">FIDHLLTMGVGVHFAALIFFLVVS</span><span class="topo-outside">QFVAPKYRI</span><span class="topo-membrane">ATALSCIVMVSAGLILNSQAVMWT</span><span class="topo-inside">DAYAYVDGSYQLQDLTF</span><span class="topo-membrane">SNGYRYVNWMADIPCLLLQLLIVL</span><span class="topo-outside">NLK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GKE</span><span class="topo-membrane">LFSTATWLILAAWGMIITGYVGQ</span><span class="topo-inside">LYEVDDIAQLM</span><span class="topo-membrane">IWGAVSTAFFVVMNWIVGTKIFKN</span><span class="topo-outside">RATMLGGTDS</span><span class="topo-membrane">TITKVFWLMMFAWTLYPIAYLV</span><span class="topo-inside">PAFMNNADGVV</span><span class="topo-membrane">LRQLLFTIADISSKVI</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-membrane">YGLMITYI</span><span class="topo-outside">AIQQSAAAGY</span><span class="topo-unknown">VPAQQALG</span><span class="topo-outside">RI</span><span class="topo-unknown">GMDSKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>19</td>
      <td>-2</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>43</td>
      <td>17</td>
      <td>40</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>52</td>
      <td>41</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>76</td>
      <td>50</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>74</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>117</td>
      <td>91</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>123</td>
      <td>115</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>146</td>
      <td>121</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>157</td>
      <td>144</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>181</td>
      <td>155</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>191</td>
      <td>179</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>213</td>
      <td>189</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>224</td>
      <td>211</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>248</td>
      <td>222</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>258</td>
      <td>246</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>266</td>
      <td>256</td>
      <td>263</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>267</td>
      <td>268</td>
      <td>264</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.2020486118

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7crj">7CRJ</a></td>
      <td>1.65</td>
      <td>C 1 2 1</td>
      <td>CIR dark state (TR-SFX reference structure)</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, chloride ion</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7crj">7CRJ</a></td>
      <td>1.85</td>
      <td>C 1 2 1</td>
      <td>CIR 1 ps after photoactivation (TR-SFX)</td>
      <td>13-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, chloride ion (dissociating)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7crj">7CRJ</a></td>
      <td>1.85</td>
      <td>C 1 2 1</td>
      <td>CIR 2 ps after photoactivation (TR-SFX)</td>
      <td>13-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, chloride ion (moving toward Thr102)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7crj">7CRJ</a></td>
      <td>1.85</td>
      <td>C 1 2 1</td>
      <td>CIR 50 ps after photoactivation (TR-SFX)</td>
      <td>13-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, chloride ion (near Thr102)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7crj">7CRJ</a></td>
      <td>1.85</td>
      <td>C 1 2 1</td>
      <td>CIR 100 ps after photoactivation (TR-SFX, 0.90 mJ/mm2)</td>
      <td>13-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, chloride ion (relaxed at Thr102)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-CodonPlus
- **Construct**: CIR from Nonlabens marinus S1-08 with C-terminal 6xHis tag (residues 1-272)
- **Induction**: 0.5 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) + 50 uM all-trans-retinal for 6-8 h at 30 C

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
      <td>Cell culture and expression</td>
      <td>E. coli expression with <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> induction</td>
      <td>—</td>
      <td></td>
      <td>Cells grown in high-salt LB medium at 37 C; induced at OD600 > 1.0</td>
    </tr>
    <tr>
      <td>Cell lysis and membrane isolation</td>
      <td>Sonication and <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a></td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> HCl pH 7.0, 150 mM NaCl</td>
      <td>Membrane fraction isolated by ultracentrifugation at 370,000 x g for 40 min at 4 C</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> HCl pH 7.0, 150 mM NaCl + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Solubilization for 2 h at 4 C</td>
    </tr>
    <tr>
      <td>Affinity purification and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> followed by <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> affinity resin; <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluate applied to <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column for final purification</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) crystallization for TR-SFX</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Microcrystals grown in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> for TR-SFX at LCLS. Dark state at 1.65 A; time delays: 1 ps to 100 ps after 550 <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> fs-pumping laser.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7crj">7CRJ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">KNIESLFDYSAG</span><span class="topo-membrane">QFEFIDHLLTMGVGVHFAALIFFLV</span><span class="topo-inside">VSQFVAPKYRI</span><span class="topo-membrane">ATALSCIVMVSAGLILNSQAVMWT</span><span class="topo-outside">DAYAYVDGSYQLQDLTF</span><span class="topo-membrane">SNGYRYVNWMATIPCLLLQLL</span><span class="topo-inside">IVLNLKGKEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">F</span><span class="topo-membrane">STATWLILAAWGMIITGYVGQL</span><span class="topo-outside">YEVDDIA</span><span class="topo-membrane">QLMIWGAVSTAFFVVMNWIVGTKI</span><span class="topo-inside">FKNRATMLGGTDSTIT</span><span class="topo-membrane">KVFWLMMFAWTLYPIAYLVPAFM</span><span class="topo-outside">NNAD</span><span class="topo-membrane">GVVLRQLLFTIADISSKVIYGLM</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">IT</span><span class="topo-inside">YIAIQQSAAAGYVPAQQALGRI</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>2</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>37</td>
      <td>14</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>48</td>
      <td>39</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>72</td>
      <td>50</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>89</td>
      <td>74</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>110</td>
      <td>91</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>121</td>
      <td>112</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>143</td>
      <td>123</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>150</td>
      <td>145</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>174</td>
      <td>152</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>190</td>
      <td>176</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>213</td>
      <td>192</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>217</td>
      <td>215</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>242</td>
      <td>219</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>264</td>
      <td>244</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cri">7CRI</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">KNIESLFDYSAG</span><span class="topo-membrane">QFEFIDHLLTMGVGVHFAALIFFLV</span><span class="topo-inside">VSQFVAPKYRI</span><span class="topo-membrane">ATALSCIVMVSAGLILNSQAVMWT</span><span class="topo-outside">DAYAYVDGSYQLQDLTF</span><span class="topo-membrane">SNGYRYVNWMATIPCLLLQLL</span><span class="topo-inside">IVLNLKGKEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">F</span><span class="topo-membrane">STATWLILAAWGMIITGYVGQLYE</span><span class="topo-outside">VDDIA</span><span class="topo-membrane">QLMIWGAVSTAFFVVMNWIVGTKI</span><span class="topo-inside">FKNRATMLGGTDSTIT</span><span class="topo-membrane">KVFWLMMFAWTLYPIAYLVPAFM</span><span class="topo-outside">NNAD</span><span class="topo-membrane">GVVLRQLLFTIADISSKVIYGLM</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">IT</span><span class="topo-inside">YIAIQQSAAAGYVPAQQALGRI</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>2</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>37</td>
      <td>14</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>48</td>
      <td>39</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>72</td>
      <td>50</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>89</td>
      <td>74</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>110</td>
      <td>91</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>121</td>
      <td>112</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>123</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>150</td>
      <td>147</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>174</td>
      <td>152</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>190</td>
      <td>176</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>213</td>
      <td>192</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>217</td>
      <td>215</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>242</td>
      <td>219</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>264</td>
      <td>244</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7crk">7CRK</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">KNIESLFDYSAGQFE</span><span class="topo-membrane">FIDHLLTMGVGVHFAALIFFLV</span><span class="topo-inside">VSQFVAPKYRIA</span><span class="topo-membrane">TALSCIVMVSAGLILNSQAVMWTD</span><span class="topo-outside">AYAYVDGSYQLQDLTF</span><span class="topo-membrane">SNGYRYVNWMATIPCLLLQLL</span><span class="topo-inside">IVLNLKGKEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">F</span><span class="topo-membrane">STATWLILAAWGMIITGYVGQL</span><span class="topo-outside">YEVDDIAQ</span><span class="topo-membrane">LMIWGAVSTAFFVVMNWIVGTKIF</span><span class="topo-inside">KNRATMLGGTDS</span><span class="topo-membrane">TITKVFWLMMFAWTLYPIAYLV</span><span class="topo-outside">PAFMNNADGV</span><span class="topo-membrane">VLRQLLFTIADISSKVIYGLM</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">ITY</span><span class="topo-inside">IAIQQSAAAGY</span><span class="topo-unknown">VPAQQALGR</span><span class="topo-inside">I</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>2</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>37</td>
      <td>17</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>49</td>
      <td>39</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>73</td>
      <td>51</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>89</td>
      <td>75</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>110</td>
      <td>91</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>121</td>
      <td>112</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>143</td>
      <td>123</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>151</td>
      <td>145</td>
      <td>152</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>175</td>
      <td>153</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>187</td>
      <td>177</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>209</td>
      <td>189</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>210</td>
      <td>219</td>
      <td>211</td>
      <td>220</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>243</td>
      <td>221</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>254</td>
      <td>245</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>263</td>
      <td>256</td>
      <td>264</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>264</td>
      <td>264</td>
      <td>265</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7crl">7CRL</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">KNIESLFDYSAGQF</span><span class="topo-membrane">EFIDHLLTMGVGVHFAALIFFLV</span><span class="topo-inside">VSQFVAPKYRIA</span><span class="topo-membrane">TALSCIVMVSAGLILNSQAVMWTD</span><span class="topo-outside">AYAYVDGSYQLQDLTF</span><span class="topo-membrane">SNGYRYVNWMATIPCLLLQLL</span><span class="topo-inside">IVLNLKGKEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">F</span><span class="topo-membrane">STATWLILAAWGMIITGYVGQLYE</span><span class="topo-outside">VDDIA</span><span class="topo-membrane">QLMIWGAVSTAFFVVMNWIVGTKI</span><span class="topo-inside">FKNRATMLGGTDSTI</span><span class="topo-membrane">TKVFWLMMFAWTLYPIAYLVPAF</span><span class="topo-outside">MNNADG</span><span class="topo-membrane">VVLRQLLFTIADISSKVIYGLM</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">IT</span><span class="topo-inside">YIAIQQSAAAGYVPAQQALGRI</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>14</td>
      <td>2</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>37</td>
      <td>16</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>49</td>
      <td>39</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>73</td>
      <td>51</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>89</td>
      <td>75</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>110</td>
      <td>91</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>121</td>
      <td>112</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>123</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>150</td>
      <td>147</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>174</td>
      <td>152</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>189</td>
      <td>176</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>212</td>
      <td>191</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>218</td>
      <td>214</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>242</td>
      <td>220</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>264</td>
      <td>244</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7crs">7CRS</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">KNIESLFDYSAGQFE</span><span class="topo-membrane">FIDHLLTMGVGVHFAALIFFLVVS</span><span class="topo-inside">QFVAPKYR</span><span class="topo-membrane">IATALSCIVMVSAGLILNSQAVMW</span><span class="topo-outside">TDAYAYVDGSYQLQDLTFS</span><span class="topo-membrane">NGYRYVNWMATIPCLLLQLLI</span><span class="topo-inside">VLNLKGK</span><span class="topo-membrane">EL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FSTATWLILAAWGMIITGYVGQL</span><span class="topo-outside">YEVDDIA</span><span class="topo-membrane">QLMIWGAVSTAFFVVMNWIVGTKI</span><span class="topo-inside">FKNRATMLGGTDSTI</span><span class="topo-membrane">TKVFWLMMFAWTLYPIAYLVPAFM</span><span class="topo-outside">NNAD</span><span class="topo-membrane">GVVLRQLLFTIADISSKVIYGLM</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">ITY</span><span class="topo-inside">IAIQQSAAAGY</span><span class="topo-unknown">VPAQQALG</span><span class="topo-inside">RI</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>2</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>39</td>
      <td>17</td>
      <td>40</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>47</td>
      <td>41</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>71</td>
      <td>49</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>90</td>
      <td>73</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>111</td>
      <td>92</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>118</td>
      <td>113</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>143</td>
      <td>120</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>150</td>
      <td>145</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>174</td>
      <td>152</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>189</td>
      <td>176</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>213</td>
      <td>191</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>217</td>
      <td>215</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>243</td>
      <td>219</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>254</td>
      <td>245</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>262</td>
      <td>256</td>
      <td>263</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>263</td>
      <td>264</td>
      <td>264</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.2117433119

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7vgt">7VGT</a></td>
      <td>2.1</td>
      <td>—</td>
      <td>NM-R3 resting state (XFEL structure, bromide-bound)</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, bromide ion</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7vgu">7VGU</a></td>
      <td>2.1</td>
      <td>—</td>
      <td>NM-R3 1 ms after photoactivation (TR-SFX, O1 intermediate)</td>
      <td>13-cis/15-syn <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, bromide ion (released)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7gvg">7GVG</a></td>
      <td></td>
      <td>—</td>
      <td>NM-R3 anion-depleted form (P2(1)2(1)2(1) crystal form)</td>
      <td>13-cis/15-syn <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, no halide bound (Asn98 occupies anion site)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-CodonPlus
- **Construct**: CIR from Nonlabens marinus S1-08 with C-terminal 6xHis tag (residues 1-272)
- **Induction**: 0.5 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) + 50 uM all-trans-retinal for 6-8 h at 30 C

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
      <td>Protein expression and purification</td>
      <td>E. coli expression with <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> induction, <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) affinity, <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/); <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>NM-R3 purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization. Crystals grown in 1500 mM NaBr or NaI for halide replacement.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) crystallization for TR-SFX at SACLA</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Microcrystals grown in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> for TR-SFX at SACLA BL3. Time delays: 10 us and 1 ms after 540 <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> or 532 <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> pump laser.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7vgt">7VGT</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSSGSSG</span><span class="topo-inside">MKNIESLFDYSAGQFE</span><span class="topo-membrane">FIDHLLTMGVGVHFAALIFFLV</span><span class="topo-outside">VSQFVAPKYRI</span><span class="topo-membrane">ATALSCIVMVSAGLILNSQAVMWTD</span><span class="topo-inside">AYAYVDGSYQLQDLTF</span><span class="topo-membrane">SNGYRYVNWMATIPCLLLQLLI</span><span class="topo-outside">V</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LNLKGKE</span><span class="topo-membrane">LFSTATWLILAAWGMIITGYVGQL</span><span class="topo-inside">YEVDDIAQL</span><span class="topo-membrane">MIWGAVSTAFFVVMNWIVGTKIFK</span><span class="topo-outside">NRATMLGGTDS</span><span class="topo-membrane">TITKVFWLMMFAWTLYPIAYLV</span><span class="topo-inside">PAFMNNADGVV</span><span class="topo-membrane">LRQLLFTIADIS</span></span>
<span class="topo-ruler">       250       260       270         </span>
<span class="topo-line"><span class="topo-membrane">SKVIYGLMITY</span><span class="topo-outside">IAIQQSAAAGYVPAQQALGRI</span><span class="topo-unknown">GMDSKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>-6</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>23</td>
      <td>1</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>45</td>
      <td>17</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>56</td>
      <td>39</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>81</td>
      <td>50</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>97</td>
      <td>75</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>119</td>
      <td>91</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>127</td>
      <td>113</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>151</td>
      <td>121</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>160</td>
      <td>145</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>184</td>
      <td>154</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>178</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>217</td>
      <td>189</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>228</td>
      <td>211</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>251</td>
      <td>222</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>272</td>
      <td>245</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>279</td>
      <td>266</td>
      <td>272</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7vgu">7VGU</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSSGSSG</span><span class="topo-inside">MKNIESLFDYSAGQFE</span><span class="topo-membrane">FIDHLLTMGVGVHFAALIFFLV</span><span class="topo-outside">VSQFVAPKYRI</span><span class="topo-membrane">ATALSCIVMVSAGLILNSQAVMWTD</span><span class="topo-inside">AYAYVDGSYQLQDLTF</span><span class="topo-membrane">SNGYRYVNWMATIPCLLLQLLI</span><span class="topo-outside">V</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LNLKGKE</span><span class="topo-membrane">LFSTATWLILAAWGMIITGYVGQL</span><span class="topo-inside">YEVDDIAQL</span><span class="topo-membrane">MIWGAVSTAFFVVMNWIVGTKIFK</span><span class="topo-outside">NRATMLGGTDS</span><span class="topo-membrane">TITKVFWLMMFAWTLYPIAYLV</span><span class="topo-inside">PAFMNNADGVV</span><span class="topo-membrane">LRQLLFTIADIS</span></span>
<span class="topo-ruler">       250       260       270         </span>
<span class="topo-line"><span class="topo-membrane">SKVIYGLMITY</span><span class="topo-outside">IAIQQSAAAGYVPAQQALGRI</span><span class="topo-unknown">GMDSKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>-6</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>23</td>
      <td>1</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>45</td>
      <td>17</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>56</td>
      <td>39</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>81</td>
      <td>50</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>97</td>
      <td>75</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>119</td>
      <td>91</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>127</td>
      <td>113</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>151</td>
      <td>121</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>160</td>
      <td>145</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>184</td>
      <td>154</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>178</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>217</td>
      <td>189</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>228</td>
      <td>211</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>251</td>
      <td>222</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>272</td>
      <td>245</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>279</td>
      <td>266</td>
      <td>272</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1126##science.abj6663

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7o8f">7O8F</a></td>
      <td></td>
      <td>—</td>
      <td>NmHR dark state and time-resolved structures at 10 ps, 1 us, 20 us, 300 us, 12.5 ms, 22.5-45 ms (TR-SFX at SwissFEL and SLS)</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, chloride/bromide ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-CodonPlus
- **Construct**: CIR from Nonlabens marinus S1-08 with C-terminal 6xHis tag (residues 1-272)
- **Induction**: 0.5 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) + 50 uM all-trans-retinal for 6-8 h at 30 C

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
      <td>Protein expression and purification</td>
      <td>E. coli expression and purification for TR-SFX</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purified NmHR used for <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization and TR-SFX experiments at SwissFEL and SLS</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) crystallization for TR-SFX</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>NmHR crystallized in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> for time-resolved serial crystallography at SwissFEL XFEL and Swiss Light Source synchrotron. Bromide-soaked crystals continuously illuminated with 520-nm laser diode during delivery for photostationary state data. Time delays from picoseconds to milliseconds. Crystals in space group with chloride/bromide concentration affecting kinetics.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7o8f">7O8F</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MASMTGGQQMGRDPNS</span><span class="topo-inside">MKNIESLFDYSAG</span><span class="topo-membrane">QFEFIDHLLTMGVGVHFAALIFFLV</span><span class="topo-outside">VSQFVAPKYRI</span><span class="topo-membrane">ATALSCIVMVSAGLILNSQAVMWTD</span><span class="topo-inside">AYAYVDGSYQLQDLT</span><span class="topo-membrane">FSNGYRYVNWMATIP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">CLLLQLLI</span><span class="topo-outside">VLNLKGKEL</span><span class="topo-membrane">FSTATWLILAAWGMIITGYVGQL</span><span class="topo-inside">YEVDDIAQ</span><span class="topo-membrane">LMIWGAVSTAFFVVMNWIVGTKIF</span><span class="topo-outside">KNRATMLGGTDSTI</span><span class="topo-membrane">TKVFWLMMFAWTLYPIAYLVPAF</span><span class="topo-inside">MNNAD</span><span class="topo-membrane">GVVLRQ</span></span>
<span class="topo-ruler">       250       260       270       280       290      </span>
<span class="topo-line"><span class="topo-membrane">LLFTIADISSKVIYGLMIT</span><span class="topo-outside">YIAIQQSAAAGYVPAQQAL</span><span class="topo-unknown">GRIGMDSKAALEHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>16</td>
      <td>-15</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>29</td>
      <td>1</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>54</td>
      <td>14</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>65</td>
      <td>39</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>50</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>105</td>
      <td>75</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>128</td>
      <td>90</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>137</td>
      <td>113</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>160</td>
      <td>122</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>168</td>
      <td>145</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>192</td>
      <td>153</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>206</td>
      <td>177</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>229</td>
      <td>191</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>234</td>
      <td>214</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>259</td>
      <td>219</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>278</td>
      <td>244</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>296</td>
      <td>263</td>
      <td>280</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1126##sciadv.aay2042

**Expression:**

- **Expression system**: Escherichia coli BL21-CodonPlus
- **Construct**: CIR from Nonlabens marinus S1-08 with C-terminal 6xHis tag (residues 1-272)
- **Induction**: 0.5 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) + 50 uM all-trans-retinal for 6-8 h at 30 C

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Single-crystal microspectrophotometry and cryo-crystallography</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>95 K and 140 K</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled under cold nitrogen gas stream</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Single crystals subjected to CW laser (532 <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a>) or pulsed laser (532 <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a>, 10 kHz). Data at Pohang Accelerator Laboratory.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Temperature (structured)</td>
      <td>95 K</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### NTQ motif and chloride binding at the Schiff base

The CIR structure reveals a chloride ion (Cl-I) bound at the protonated Schiff base (PSB), positioned 3.1 A from the Schiff base nitrogen. Cl-I directly interacts with the conserved Asn98 and Thr102 of the NTQ motif, as well as PSB. This is distinct from archaeal [Halorhodopsin](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) where chloride is coordinated by the TSA motif. Mutation of Asn98 or Thr102 eliminates or substantially reduces chloride-pumping activity, demonstrating the essential role of these residues in chloride binding and transport.

### Anion-&#x3C0; interaction with the retinal chromophore

Time-resolved crystallography and QM/MM simulations revealed that the transient Cl352-binding site at 1 us is stabilized by an anion-&#x3C0; interaction between the chloride ion and the conjugated &#x3C0;-electron system of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore. The stabilization is dominated by the electrostatic component between chloride and the protonated Schiff base (PSB), with additional contribution from the C14-C15=N fragment of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/). The polarization of the &#x3C0;-electron density by the negative charge of the chloride resembles common interactions between anions and &#x3C0; electrons of aromatic rings. This interaction supports transient chloride ion binding across a major bottleneck in the transport pathway, enabling the anion to pass over the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore.

### PSB flip drives the first step of chloride transport

At 10 ps after photoactivation, the protonated Schiff base of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) flips from pointing toward the extracellular side to pointing toward the cytoplasm. The chloride ion Cl351 shifts away from the PSB (distance increases from 3.1 A to 4.1 A), breaking the hydrogen bond. QM/MM simulations indicate 28.2 kcal/mol of energy is stored upon charge separation between the PSB and Cl351 at 10 ps, corresponding to more than half of a green light photon (530 [NM](/xray-mp-wiki/reagents/detergents/nm/), 53.9 kcal/mol). At 1 us, the chloride is dragged through the Cl352-binding site over the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore via the anion-&#x3C0; interaction.

### Steric molecular gate prevents chloride backflow

At 20 us, the relaxation of a kink in helix C moves the side chain of Asn98 into the chloride-free Cl351 site, acting as a sterically closing molecular gate that prevents reverse flow of chloride. Asn98 replaces Cl351 and interacts with water molecules Wat484 and Wat407. Additional stabilization is achieved by a new hydrogen bond between Thr102 and the carbonyl group of the Asn98 backbone, sealing the gate. Thr102 plays multiple roles: coordinating Cl351 in the resting state, assisting chloride transfer to Cl352 by rotamericization, and sealing the molecular gate to prevent backflow.

### Cl- release through Gln109 of the NTQ motif

At 20 us, the Cl353-binding site emerges above the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), 14 A from Cl352 toward the cytoplasm. The site is accessed through water molecules Wat401 and Wat402 and formed by Gln109 of the conserved NTQ motif, Ser54, and Thr243. Gln109 is at a strategic position for ion pumps: the equivalent residue in [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) is Asp96 (internal proton donor), and in [Kr2](/xray-mp-wiki/proteins/rhodopsins/kr2/) is Gln123 (involved in sodium transport). This suggests that pumping rhodopsins share sections of the transport pathway despite different substrate charge and size.

### Electrostatic gate at Arg95-Asp231 ensures unidirectional transport

An electrostatic gate formed by a salt bridge between Arg95 and Asp231 controls chloride uptake from the extracellular side. QM/MM simulations confirmed Asp231 is in anionic form, supporting the presence of this salt bridge. When chloride diffuses to the Wat409 position, it interferes with the Arg95-Asp231 electrostatic attraction, causing Asp231 to rotate and interact with His29 instead. This opens the electrostatic gate, creating a pathway for the anion to the Cl355-binding site (4 A from Cl351). After recharging the resting state, the electrostatic gate closes again, preventing anion leakage back into bulk solvent and ensuring vectorial transport.

### Complete chloride transport pathway

The combined time-resolved experiments enabled tracing of five transient anion-binding sites (Cl351-Cl355) and elucidation of the complete chloride transport pathway in NmHR. The pathway involves: (1) PSB flip at 10 ps, storing photon energy as charge separation; (2) chloride passage over the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) via anion-&#x3C0; interaction at 1 us; (3) steric gate closure by Asn98 at 20 us preventing backflow; (4) release through Gln109 to Cl353 site; (5) ordering of surface residues for Cl- release at 300 us; (6) electrostatic gate opening at Arg95-Asp231 for chloride uptake from extracellular side; (7) recharging of Cl351 site and gate closure. The mechanism combines steric and electrostatic gating with anion-&#x3C0; interactions to achieve light-driven unidirectional chloride transport.

### NM-R3 chloride pathway mapping by cryo-crystallography

Single-crystal cryo-crystallography with difference Fourier maps (light-minus-dark) at multiple laser intensities revealed the chloride ion conduction pathway of NM-R3. On photoexcitation, the Schiff base chloride (Cl-1) moves slightly to Cl-1B, then to Cl-5 (between Ser60 and Cys105) and Cl-6 (near Cys105, Ala125, Ile129) toward the cytoplasmic face. An additional chloride ion (Cl-3) enters near Phe90 from the extracellular side, and Cl-4 arrives near the PSB region from the extracellular face via Cl-3. These five discrete chloride positions map the complete anion conduction pathway in a light-driven chloride pump.

### TR-SFX reveals picosecond chloride dissociation dynamics

Time-resolved serial femtosecond crystallography (TR-SFX) captured the dynamics of Cl- ion transport upon photoactivation. [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomerization from all-trans to 13-cis occurs in 1 ps, flipping the C12-C13=C14-C15 torsion angle from 179 degrees to 4 degrees. The Cl- ion dissociates from the PSB within 1 ps, moving 1.3 A toward the extracellular side as the electrostatic interaction with the protonated Schiff base is abruptly lost. By 50-100 ps, the Cl- ion moves toward Thr102, revealing a dissociation-diffusion mechanism rather than the dipole switching model.

### TR-SFX reveals millisecond-scale gating dynamics during chloride pumping

TR-SFX data at 10 us and 1 ms after photoactivation of NM-R3 revealed the conformational alterations during ion transfer and after ion release. At 10 us (L/N intermediate), the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomerizes and moves toward helix C, the iodide ion bound to the PSB displaces toward Thr102, and Trp201 shifts toward the cytoplasmic side. Asn98 moves toward the anion binding site, distorting helix C. At 1 ms (O1 intermediate), the halide ion is released from the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) binding pocket. The [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) adopts a 13-cis/15-syn configuration. Inward movements of helix C and helix G and lateral displacements of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) block access from the extracellular side, preventing backflow of anions.

### Comparison with KR2 and archaeal halorhodopsins

NM-R3 and [Kr2](/xray-mp-wiki/proteins/rhodopsins/kr2/) share identical key ion transfer residues except Thr102 versus Asp116, yet pump oppositely charged ions. In [Kr2](/xray-mp-wiki/proteins/rhodopsins/kr2/), the O1 state at 1 ms shows Na+ near Asn112 and Asp251; in NM-R3, the O1 state shows larger inward movements of helix C and helix G, and [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) adopts 13-cis/15-syn configuration (versus 13-cis/15-anti in [Kr2](/xray-mp-wiki/proteins/rhodopsins/kr2/)). NM-R3 shares structural similarities with NpHR despite low sequence identity and different key motifs (NTQ vs TSA). The chloride-binding site coordinated by Gln105 in HsHR does not align with the anion uptake pathway in NmHR, whereas the NpHR N-state site is near Cl352 in NmHR. Large conformational changes in helix C of NpHR and the existence of a salt bridge next to the resting-state chloride-binding site in HsHR and NpHR suggest that molecular gates may be a general feature of [Halorhodopsin](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) ion pumps.

### Hydrophobic gate opening at Leu106

Leu106 on TM-C is a major hydrophobic residue on the chloride pathway to the cavity near Gln109. In the dark state, the channel between Cl-1 and the cavity near Gln109 is blocked. At 100 ps after activation, the Leu106 side chain moves away from TM-G by about 0.6 A, suggesting the initial stages of hydrophobic gate opening that may facilitate Cl- migration to the cytoplasmic side in later stages of the photocycle.


## Cross-References

- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/">Microbial Rhodopsins</a> — CIR/NmHR is a member of the microbial rhodopsin family of light-driven ion pumps
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/ntq-motif/">NTQ Motif in Chloride Pumping Rhodopsins</a> — The NTQ motif (Asn98, Thr102, Gln109) defines the chloride-pumping rhodopsin family and plays multiple roles in chloride binding, transport, and gating
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Archetypal microbial rhodopsin; comparison reveals mechanistic equivalence and differences in ion transport
- <a href="/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/">Halorhodopsin (HR) from Halobacterium salinarum</a> — Archaeal halorhodopsin with TSA motif; convergent evolution for chloride pumping
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (In Meso) Crystallization</a> — Crystallization method used for all CIR/NmHR structures including TR-SFX experiments
- <a href="/xray-mp-wiki/methods/structure-determination/time-resolved-serial-femtosecond-crystallography/">Time-Resolved Serial Femtosecond Crystallography (TR-SFX)</a> — Primary method used to capture picosecond to millisecond dynamics of chloride transport
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> — Referenced in the context of Retinal
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> — Referenced in the context of Iptg
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in the context of DDM
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> — Referenced in the context of Hepes
- <a href="/xray-mp-wiki/proteins/rhodopsins/pharaonis-halorhodopsin/">pharaonis Halorhodopsin (phR)</a> — Archaeal inward chloride pump with TSA motif; convergent evolution comparison
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/retinal-chromophore-conformation/">Retinal Chromophore Conformation</a> — All-trans retinal is the chromophore in ClR
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> — Related protein structure
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — CIR functions through a rhodopsin photocycle
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> — Used in cell wash buffers
- <a href="/xray-mp-wiki/reagents/lipids/oleic-acid/">Oleic Acid</a> — Binds to CIR C-terminal helix on TM A
