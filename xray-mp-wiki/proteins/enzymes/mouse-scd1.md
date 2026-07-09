---
title: "Mouse Stearoyl-CoA Desaturase 1 (mSCD1)"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2020.05.017, doi/10.1038##nature14549]
verified: regex
uniprot_id: P13516
---

# Mouse Stearoyl-CoA Desaturase 1 (mSCD1)

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P13516">UniProt: P13516</a>

<span class="expr-badge">Mus musculus</span>

## Overview

Mouse [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) desaturase 1 (SCD1) is a membrane-embedded diiron enzyme embedded in the endoplasmic reticulum membrane that catalyzes the formation of a cis-double bond at the Delta9 position of saturated acyl-CoAs, converting them to monounsaturated acyl-CoAs. This paper reports the first crystal structure of iron-containing mouse SCD1 (PDB 6WF2) solved at 3.5 A resolution by X-ray crystallography, revealing a unique all-histidine-coordinated diiron center and a tightly bound [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) ligand. The structure was expressed in HEK293 cells using a novel [IRON](/xray-mp-wiki/reagents/additives/iron/) incorporation protocol, overcoming the zinc misincorporation problem that plagued previous SCD1 structures.


## Publications

### doi/10.1016##j.jmb.2020.05.017

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6wf2">6WF2</a></td>
      <td>3.5 A</td>
      <td>P212121</td>
      <td>mDeltaSCD1 (residues 41-361), N-terminal 2-23 deletion, iron-containing diiron center</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/oleoyl-coa/">Oleoyl-CoA</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnTI- suspension cells (BacMam expression)
- **Construct**: Mouse SCD1 gene with deletion of residues 2-23 at N-terminus (mDeltaSCD1), codon-optimized for human cell expression, C-terminally tagged with GFP and TEV protease site

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
      <td>Cell culture and membrane preparation</td>
      <td>HEK293S GnTI- suspension cell expression with BacMam vector</td>
      <td>--</td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl, 1 mM PMSF, 5 mM MgCl2, DNase I + --</td>
      <td>Cells infected with 10% P3 virus, supplemented with 5 mg/L iron-saturated transferrin and 5 uM FeCl3. Induced with 10 mM <a href="/xray-mp-wiki/reagents/additives/sodium-butyrate/">Sodium Butyrate</a>, 30 C for 48 h</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl + 40 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (DM)</td>
      <td>40 mM DM added to membranes, 4 C for 2 h under gentle agitation. Centrifuged at 55,000g for 45 min at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (GFP <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a>)</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>CNBR-activated Sepharose coupled to GFP <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> (GFPnb)</td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl, 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a> + 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
      <td>1 h incubation at 4 C, washed with 20 column volumes of buffer B</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease">TEV</a> protease cleavage</td>
      <td>GFP <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> resin</td>
      <td>Room temperature + 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease">TEV</a> protease cleaved GFP tag at room temperature for 1 h</td>
    </tr>
    <tr>
      <td>Secondary affinity cleanup</td>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt-based affinity resin</td>
      <td>-- + --</td>
      <td>Removed His-tagged <a href="/xray-mp-wiki/reagents/enzymes/tev-protease">TEV</a> protease</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL</td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl, 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a> + 4 mM DM</td>
      <td>Peak fractions collected and analyzed by SDS-PAGE</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>30-50 mg/ml mDeltaSCD1 in <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> + 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>None; crystals flash frozen in liquid nitrogen directly</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein mixed with molten <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> doped with 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> at 1:1.5 (v/w) ratio using coupled syringe device. 50 nl deposited over 800 nl precipitant using Gryphon LCP robot. Data collected at 24-ID (NE-CAT), APS, Argonne. Wavelength 0.9791 A, resolution 3.51 A. R/Rfree 21.9%/27.6%. Model includes residues 41-361, two <a href="/xray-mp-wiki/reagents/additives/iron/">IRON</a> ions, and one <a href="/xray-mp-wiki/reagents/ligands/oleoyl-coa/">Oleoyl-CoA</a></td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6wf2">6WF2</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSGNEREKVKTVPLHLEE</span><span class="topo-inside">DIRPEMKEDIHDPTYQDEEGPPPKLEY</span><span class="topo-membrane">VWRNIILMVLLHLGGLYGIILVP</span><span class="topo-outside">SCKL</span><span class="topo-membrane">YTCLFGIFYYMTSALG</span><span class="topo-inside">ITAGAHRLWSHRTYKARLPLRIFLIIANTMAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QNDVYEWARDHRAHHKFSETHADPHNSRRGFFFSHVGWLLVRKHPAVKEKGGKLDMSDLKAEKLVMF</span><span class="topo-membrane">QRRYYKPGLLLMCFILPT</span><span class="topo-outside">LVPWYCWGETFVNS</span><span class="topo-membrane">LFVSTFLRYTLVLNA</span><span class="topo-inside">TWLVNS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330         </span>
<span class="topo-line"><span class="topo-inside">AAHLYGYRPYDKNIQSRENILVSLGAVGEGFHNYHHTFPFDYSASEYRWHINFTTFFIDCMAALGLAYDRKKVSKATVLARIKRTGDGSHKSSENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>18</td>
      <td>23</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>45</td>
      <td>41</td>
      <td>67</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>68</td>
      <td>68</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>72</td>
      <td>91</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>88</td>
      <td>95</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>187</td>
      <td>111</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>205</td>
      <td>210</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>219</td>
      <td>228</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>234</td>
      <td>242</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>339</td>
      <td>257</td>
      <td>361</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature14549

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ymk">4YMK</a></td>
      <td>2.6 A</td>
      <td>P212121</td>
      <td>Mouse SCD1 Delta2-23 (residues 24-355), N-terminal 2-23 <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, zinc-containing dimetal center</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/stearoyl-coa/">Stearoyl-CoA</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnTI- suspension cells (BacMam expression)
- **Construct**: Mouse SCD1 gene with deletion of residues 2-23 at N-terminus (mDeltaSCD1), codon-optimized for human cell expression, C-terminally tagged with GFP and TEV protease site

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ymk">4YMK</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSGNEREKVKTVPLHLE</span><span class="topo-inside">EDIRPEMKEDIHDPTYQDEEGPPPKLE</span><span class="topo-membrane">YVWRNIILMVLLHLGGLYGII</span><span class="topo-outside">LVPSCKL</span><span class="topo-membrane">YTCLFGIFYYMTSALGI</span><span class="topo-inside">TAGAHRLWSHRTYKARLPLRIFLIIANTMAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QNDVYEWARDHRAHHKFSETHADPHNSRRGFFFSHVGWLLVRKHPAVKEKGGKLDMSDLKAEKL</span><span class="topo-membrane">VMFQRRYYKPGLLLMCFILPT</span><span class="topo-outside">LVPWYCWGETFVNSL</span><span class="topo-membrane">FVSTFLRYTLVLNATW</span><span class="topo-inside">LVNS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330         </span>
<span class="topo-line"><span class="topo-inside">AAHLYGYRPYDKNIQSRENILVSLGAVGEGFHNYHHTFPFDYSASEYRWHINFTTFFIDCMAALGLAYDRKKVSKATVLARIKRTGDGSHKSSENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>18</td>
      <td>44</td>
      <td>40</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>65</td>
      <td>67</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>72</td>
      <td>88</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>89</td>
      <td>95</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>184</td>
      <td>112</td>
      <td>206</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>205</td>
      <td>207</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>220</td>
      <td>228</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>236</td>
      <td>243</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>339</td>
      <td>259</td>
      <td>361</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ymk">4YMK</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSGNEREKVKTVPLHLEE</span><span class="topo-inside">DIRPEMKEDIHDPTYQDEEGPPPKLEYVW</span><span class="topo-membrane">RNIILMVLLHLGGLYGIILVPSC</span><span class="topo-outside">K</span><span class="topo-membrane">LYTCLFGIFYYMTS</span><span class="topo-inside">ALGITAGAHRLWSHRTYKAR</span><span class="topo-unknown">LPLRIFLIIANTMA</span><span class="topo-inside">F</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QNDVYEWARDHRAHHKFSETHADPHNSRRGFFFSHVGWLLVRKHPAVKEKGGKLDMSDLKAEKLVMFQRRY</span><span class="topo-membrane">YKPGLLLMCFILPTLVPW</span><span class="topo-outside">YCWGETF</span><span class="topo-membrane">VNSLFVSTFLRYTLV</span><span class="topo-inside">LNATWLVNS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330         </span>
<span class="topo-line"><span class="topo-inside">AAHLYGYRPYDKNIQSRENILVSLGAVGEGFHNYHHTFPFDYSASEYRWHIN</span><span class="topo-unknown">FTTFFIDCMAA</span><span class="topo-inside">LGLAYDRKKVSKATVLARIKRTGDGSH</span><span class="topo-unknown">KSSENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>47</td>
      <td>41</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>70</td>
      <td>70</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>71</td>
      <td>93</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>85</td>
      <td>94</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>105</td>
      <td>108</td>
      <td>127</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>119</td>
      <td>128</td>
      <td>141</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>120</td>
      <td>191</td>
      <td>142</td>
      <td>213</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>209</td>
      <td>214</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>210</td>
      <td>216</td>
      <td>232</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>231</td>
      <td>239</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>292</td>
      <td>254</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>303</td>
      <td>315</td>
      <td>325</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>304</td>
      <td>330</td>
      <td>326</td>
      <td>352</td>
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

### Unique all-histidine-coordinated diiron center

The diiron center in SCD1 is coordinated by nine highly conserved histidine
residues that segregate into four histidine-rich motifs distant in the primary
sequence. Fe1 is coordinated by five histidine residues, while Fe2 is coordinated
by four histidines and a putative water molecule. The two [IRON](/xray-mp-wiki/reagents/additives/iron/) ions are separated
by approximately 6.4 A. Unlike other diiron enzymes, there is no oxo-bridge
between the [IRON](/xray-mp-wiki/reagents/additives/iron/) ions, and the coordination geometry and inter-ionic distance
exceed the range for known reaction intermediates such as cis-mu-1,2-peroxo or
diferryl species. This suggests a novel oxygen activation mechanism in SCD1.

### Tightly bound endogenous oleoyl-CoA ligand

A single [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) molecule is tightly bound to SCD1 even in the non-functional
zinc-containing structure (PDB 4YMK). The CoA moiety is recognized by the protein
surface while the 18:1 acyl chain accommodates a V-shaped tunnel. The Delta9 and
Delta10 carbons are positioned at the inflection point of the V-shape, close to
the diiron center. The Delta9 carbon on [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) is approximately 3 A from the
water bound to Fe2. The double bond in [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) causes a different zigzag
conformation of the acyl chain compared to [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/), which may contribute
to product inhibition.

### Diiron center structure and iron incorporation protocol

Previous SCD1 structures (PDB 4YMK and 5J45) contained zinc ions instead of [IRON](/xray-mp-wiki/reagents/additives/iron/),
an artifact of heterologous expression in insect cells. Zinc served as a structural
surrogate (0.88 A vs 0.92 A ionic radius) but rendered the enzyme inactive. This
paper developed a protocol for [IRON](/xray-mp-wiki/reagents/additives/iron/) incorporation using HEK293 cells supplemented
with iron-saturated transferrin and FeCl3, achieving >90% [IRON](/xray-mp-wiki/reagents/additives/iron/) occupancy by ICP-MS.
The iron-containing structure is nearly identical to the zinc-containing form
(RMSD 0.3 A for backbone atoms), confirming zinc's suitability as a structural
surrogate.

### In vitro reconstituted electron transfer chain

The complete electron transfer chain was assembled in vitro using purified mouse
SCD1, soluble domains of [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/) and [Cytochrome b5 Reductase](/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/), and
[Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) as substrate. NADH served as the electron donor. Michaelis-Menten
kinetics yielded a Km of 6.3 +/- 1.2 uM and kcat of 2.78 +/- 0.59 min-1 for
[Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/). The rate-limiting step is the interaction between [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/)
and SCD1 (k1 = 1.86 min-1), comparable to the steady-state rate. Product
inhibition was observed after approximately 10 minutes, with a turnover number
of 7.52 +/- 0.047, likely due to limited detergent micelle capacity.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/cytochrome-b5/">Cytochrome b5</a> — Direct electron transfer partner; forms electron transport pair with SCD1
- <a href="/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/">Cytochrome b5 Reductase</a> — Electron donor to cytochrome b5 in the SCD1 electron transport chain
- <a href="/xray-mp-wiki/reagents/ligands/oleoyl-coa/">Oleoyl-CoA</a> — Endogenous bound ligand in crystal structure and product of SCD1 reaction
- <a href="/xray-mp-wiki/reagents/ligands/stearoyl-coa/">Stearoyl-CoA</a> — Substrate of SCD1 desaturation reaction
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used to crystallize iron-containing mSCD1 (PDB 6WF2)
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Primary lipid component of LCP crystallization matrix
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — Precipitant (PEG400) used in LCP crystallization of mSCD1
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Buffer used in purification (20 mM, pH 7.5)
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
