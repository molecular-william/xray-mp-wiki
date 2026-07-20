---
title: "Rice silicon channel Lsi1 crystallization construct"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-26535-x]
verified: agent
uniprot_id: Q6Z2T3
---

# Rice silicon channel Lsi1 crystallization construct

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q6Z2T3">UniProt: Q6Z2T3</a>

<span class="expr-badge">Oryza sativa subsp. japonica</span>

## Overview

Lsi1 is the Low silicon rice 1 channel, a silicon (Si) uptake transporter from rice (*Oryza sativa*) that belongs to the Nodulin 26-like intrinsic protein (NIP) subfamily of aquaporins. Silicon is the most abundant mineral element in the earth's crust and is especially essential for high and stable rice production, helping plants overcome biotic and abiotic stresses. Lsi1 shows remarkably high selectivity for silicic acid Si(OH)4 over smaller molecules like [Glycerol](/xray-mp-wiki/reagents/additives/glycerol). The crystal structure at 1.8 Angstrom resolution reveals unique transmembrane helical orientations, a widely opened hydrophilic selectivity filter composed of five residues (Thr65_TM1/Gly88_TM2/Ser207_TM5/Gly216_LE1/Arg222_LE2), and two Thr residues (Thr65_TM1 and Thr181) that create two polar faces in the channel. Molecular dynamics simulations of silicic acid permeation showed that water molecules Wat3 and Wat9 act as part of the channel lumen, narrowing the channel and strictly selecting the orientation of silicic acid during transport. The structure provides a blueprint for rational design of transgenic crops that specifically take up silicic acid but not carcinogenic arsenite.


## Publications

### doi/10.1038##s41467-021-26535-x

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7cjs">7CJS</a></td>
      <td>1.80</td>
      <td>P 21 21 21</td>
      <td>Lsi1 crystallization construct (residues 47-264) with mutations K50R, C66A, T93V, C139A, K232R, T253V, K264R</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells
- **Construct**: Lsi1 crystallization construct (residues 47-264) with TEV protease cleavage site and octa-His tag, cloned into pFastBac1 vector
- **Notes**: Baculovirus expression system. Functionally active construct discovered by screening N- and C-terminal deletion constructs, point mutations, and Si-permeable AQPs from other organisms.

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
      <td>1</td>
      <td>Cell lysis by sonication</td>
      <td>—</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Sf9 insect cell membranes solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>2</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (<a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Octa-His tag purification</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Size-exclusion chromatography</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES Buffer</a> pH 7.5, 150 mM NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Final polishing step for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, sitting drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Lsi1_cryst at ~10 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES Buffer</a> pH 7.5, 150 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> pH 5.5, 0.1 M Li2SO4, 0.1 M NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride">Magnesium Chloride (MgCl₂)</a>, 34% <a href="/xray-mp-wiki/reagents/additives/peg-400">PEG400</a>, 5 mM <a href="/xray-mp-wiki/reagents/ligands/atp">ATP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 1.6 Angstrom but suffered from lattice-translocation defects. X-ray intensities corrected using Wang et al. approach. Structure solved at 1.8 Angstrom resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cjs">7CJS</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ALLKRV</span><span class="topo-membrane">VSEVVATFLLVFMTAGA</span><span class="topo-inside">AGISGSDLSRISQLG</span><span class="topo-membrane">QSIAGGLIVVVMIYAVG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHMNPAVTLAF</span><span class="topo-outside">AVFRHFPWIQV</span><span class="topo-membrane">PFYWAAQFTGAIAASFVL</span><span class="topo-inside">KAVIHPVDVIGTTTPVGPHW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">HSL</span><span class="topo-membrane">VVEVIVTFNMMFVTLAV</span><span class="topo-outside">ATDTRAVGEL</span><span class="topo-membrane">AGLAVGSAVCITSIFA</span><span class="topo-inside">GAISGG</span><span class="topo-unknown">SMNPARTLGP</span><span class="topo-inside">ALASNRFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWVY</span><span class="topo-outside">TFIR</span><span class="topo-unknown">FEDTPREGSSQKLSSFKLRRLRSQQS</span></span>
<span class="topo-ruler">       250    </span>
<span class="topo-line"><span class="topo-unknown">IAADDVDEMENIQV</span></span>
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
      <td>2</td>
      <td>7</td>
      <td>46</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>24</td>
      <td>52</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>39</td>
      <td>69</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>56</td>
      <td>84</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>60</td>
      <td>101</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>71</td>
      <td>105</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>72</td>
      <td>82</td>
      <td>116</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>123</td>
      <td>145</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>140</td>
      <td>168</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>150</td>
      <td>185</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>166</td>
      <td>195</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>172</td>
      <td>211</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>182</td>
      <td>217</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>183</td>
      <td>192</td>
      <td>227</td>
      <td>236</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>210</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>214</td>
      <td>255</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cjs">7CJS</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ALLKRV</span><span class="topo-membrane">VSEVVATFLLVFMTAGA</span><span class="topo-inside">AGISGSDLSRISQLG</span><span class="topo-membrane">QSIAGGLIVVVMIYAVG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHMNPAVTLAF</span><span class="topo-outside">AVFRHFPWIQV</span><span class="topo-membrane">PFYWAAQFTGAIAASFVL</span><span class="topo-inside">KAVIHPVDVIGTTTPVGPHW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">HSL</span><span class="topo-membrane">VVEVIVTFNMMFVTLAV</span><span class="topo-outside">ATDTRAVGEL</span><span class="topo-membrane">AGLAVGSAVCITSIFA</span><span class="topo-inside">GAISGG</span><span class="topo-unknown">SMNPARTLGP</span><span class="topo-inside">ALASNRFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWVY</span><span class="topo-outside">TFIRFEDTPR</span><span class="topo-unknown">EGSSQKLSSFKLRRLRSQQS</span></span>
<span class="topo-ruler">       250    </span>
<span class="topo-line"><span class="topo-unknown">IAADDVDEMENIQV</span></span>
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
      <td>2</td>
      <td>7</td>
      <td>46</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>24</td>
      <td>52</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>39</td>
      <td>69</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>56</td>
      <td>84</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>60</td>
      <td>101</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>71</td>
      <td>105</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>72</td>
      <td>82</td>
      <td>116</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>123</td>
      <td>145</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>140</td>
      <td>168</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>150</td>
      <td>185</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>166</td>
      <td>195</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>172</td>
      <td>211</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>182</td>
      <td>217</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>183</td>
      <td>192</td>
      <td>227</td>
      <td>236</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>210</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>220</td>
      <td>255</td>
      <td>264</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cjs">7CJS</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ALLKRV</span><span class="topo-membrane">VSEVVATFLLVFMTAGA</span><span class="topo-inside">AGISGSDLSRISQLG</span><span class="topo-membrane">QSIAGGLIVVVMIYAVG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHMNPAVTLAF</span><span class="topo-outside">AVFRHFPWIQV</span><span class="topo-membrane">PFYWAAQFTGAIAASFVL</span><span class="topo-inside">KAVIHPVDVIGTTTPVGPHW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">HSL</span><span class="topo-membrane">VVEVIVTFNMMFVTL</span><span class="topo-outside">AVATDTRAVGEL</span><span class="topo-membrane">AGLAVGSAVCITSIFA</span><span class="topo-inside">GAISGG</span><span class="topo-unknown">SMNPARTLGP</span><span class="topo-inside">ALASNRFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWVY</span><span class="topo-outside">TFIRF</span><span class="topo-unknown">EDTPREGSSQKLSSFKLRRLRSQQS</span></span>
<span class="topo-ruler">       250    </span>
<span class="topo-line"><span class="topo-unknown">IAADDVDEMENIQV</span></span>
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
      <td>2</td>
      <td>7</td>
      <td>46</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>24</td>
      <td>52</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>39</td>
      <td>69</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>56</td>
      <td>84</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>60</td>
      <td>101</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>71</td>
      <td>105</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>72</td>
      <td>82</td>
      <td>116</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>123</td>
      <td>145</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>138</td>
      <td>168</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>150</td>
      <td>183</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>166</td>
      <td>195</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>172</td>
      <td>211</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>182</td>
      <td>217</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>183</td>
      <td>192</td>
      <td>227</td>
      <td>236</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>210</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>255</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cjs">7CJS</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ALLKRV</span><span class="topo-membrane">VSEVVATFLLVFMTAGA</span><span class="topo-inside">AGISGSDLSRISQLG</span><span class="topo-membrane">QSIAGGLIVVVMIYAVG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHMNPAVTLAF</span><span class="topo-outside">AVFRHFPWIQV</span><span class="topo-membrane">PFYWAAQFTGAIAASFVL</span><span class="topo-inside">KAVIHPVDVIGTTTPVGPHW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">HSL</span><span class="topo-membrane">VVEVIVTFNMMFVTLAV</span><span class="topo-outside">ATDTRAVGEL</span><span class="topo-membrane">AGLAVGSAVCITSIFA</span><span class="topo-inside">GAISGG</span><span class="topo-unknown">SMNPARTLGP</span><span class="topo-inside">ALASNRFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWVY</span><span class="topo-outside">TFIRFEDTPR</span><span class="topo-unknown">EGSSQKLSSFKLRRLRSQQS</span></span>
<span class="topo-ruler">       250    </span>
<span class="topo-line"><span class="topo-unknown">IAADDVDEMENIQV</span></span>
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
      <td>2</td>
      <td>7</td>
      <td>46</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>24</td>
      <td>52</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>39</td>
      <td>69</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>56</td>
      <td>84</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>60</td>
      <td>101</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>71</td>
      <td>105</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>72</td>
      <td>82</td>
      <td>116</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>123</td>
      <td>145</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>140</td>
      <td>168</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>150</td>
      <td>185</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>166</td>
      <td>195</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>172</td>
      <td>211</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>182</td>
      <td>217</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>183</td>
      <td>192</td>
      <td>227</td>
      <td>236</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>210</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>220</td>
      <td>255</td>
      <td>264</td>
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

### Unique selectivity filter for silicic acid

The Lsi1 selectivity filter (SF) is the widest and most hydrophilic among characterized aquaporins, composed of five residues including a unique fifth residue Thr65_TM1. In canonical aquaporins, a bulky hydrophobic residue in TM2 (Phe in [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1), Trp in GlpF) shields the equivalent position. In Lsi1, Gly88_TM2 exposes Thr65_TM1 to the channel, creating a wide hydrophilic SF. The two polar faces formed by water molecules Wat3 and Wat9 hydrogen-bonded to Thr65_TM1 provide an energetically preferable environment for the tetrahedral silicic acid molecule. Mutagenesis studies showed that Thr65_TM1 substitutions to Ala, Gly, or Ser were unaffected, but substitutions to Val, Ile, or Cys substantially decreased or abolished transport activity.

### Silicic acid transport mechanism and MD simulations

Molecular dynamics simulations of silicic acid permeation through Lsi1 revealed three structural bottlenecks in the channel, two in the SF region and one near Thr181. Water molecules Wat3, Wat9, and Wat17 stably exist within cavities at these bottlenecks. During silicic acid permeation, Wat3 and Wat9 act as part of the channel lumen, narrowing the channel and strictly selecting the orientation of silicic acid. Wat9 remained bound to its site independently of Si(OH)4 movement (94% occupancy, average exchange time tau = 1.5 ns), while Wat3 (60% occupancy, tau ~ 0.3 ns) and Wat17 (44% occupancy, tau ~ 0.3 ns) were displaced during permeation. The modeled Si2 position in the SF showed all four hydroxyl groups forming hydrogen bonds with channel carbonyls, waters, Ser207_TM5, and Arg222_LE2, compensating for the energetic cost of dehydration.


## Cross-References

- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Buffer component used in purification
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification and crystallization
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component used in purification
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride (MgCl₂)</a> — Mgcl2 used in purification or crystallization buffer
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Imidazole used in purification or crystallization buffer
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Glycerol used in purification or crystallization buffer
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> — Peg400 used in purification or crystallization buffer
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component used in purification
- <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> — Atp as ligand or binding partner
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp1/">AQP1</a> — Related protein: Aqp1
