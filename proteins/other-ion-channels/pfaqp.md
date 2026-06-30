---
title: "Aquaglyceroporin PfAQP from Plasmodium falciparum"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein]
sources: [doi/10.1038##nsmb.1431]
verified: false
---

# Aquaglyceroporin PfAQP from Plasmodium falciparum

## Overview

PfAQP is the sole [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) member in the malarial parasite Plasmodium falciparum. It has the unusual property of conducting both [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) and water at high rates, making it a benchmark for understanding the determinants of water vs. [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) selectivity in the [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/). The crystal structure of PfAQP was determined at 2.05 Å resolution, revealing a tetrameric assembly with each monomer containing eight transmembrane helices. The structure shows [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) and water molecules alternating in single file along the conduction channel, providing a detailed atomic view of the transport mechanism. Unlike its closest structural homolog [GLPF](/xray-mp-wiki/proteins/other-ion-channels/glpf/) (an E. coli aquaglyceroporin with poor water conductance), the selectivity filter arginine (Arg196) in PfAQP donates three hydrogen bonds to protein moieties, matching the hydrogen-bonding pattern of water-selective aquaporins. This decreased desolvation energy of the guanidinium cation may provide the basis for high water conductance. The two NPA regions bear rare substitutions to NLA (Asn-Leu-Ala) and NPS (Asn-Pro-Ser), yet preserve the essential interactions that orient the signature asparagine residues into the channel center. PfAQP is important in malarial biology, facilitating [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) uptake from host serum and ensuring survival during osmotic stress. The PfAQP knockout in the rodent parasite P. berghei impedes growth and decreases parasitemia.

## Publications

### doi/10.1038##nsmb.1431

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3c02">3C02</a></td>
      <td>2.05</td>
      <td>I422</td>
      <td>Synthetic gene optimized for E. coli codon usage; full-length PfAQP</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> and water molecules in the conduction channel</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (synthetic gene optimized for codon usage; GeMS software used for gene design)
- **Construct**: Synthetic PfAQP gene designed to match E. coli codon usage and moderate 5′ transcript secondary structure (native A-T content >70%). Full-length protein with no affinity tag.

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
      <td>1. Membrane preparation</td>
      <td>High-pressure homogenization and ultracentrifugation</td>
      <td>—</td>
      <td>20 mM Tris pH 7.5, 500 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 4 mM β-mercaptoethanol, 1 mM PMSF</td>
      <td>Cells lysed by Emulsiflex-C5 at 10,000-15,000 psi; membranes pelleted at 160,000g for 1 h</td>
    </tr>
    <tr>
      <td>2. Membrane solubilization and purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a>? (detergent extraction)</td>
      <td>—</td>
      <td></td>
      <td>Purified to homogeneity; ~1 mg of purified tetrameric protein from 6 L culture</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified tetrameric PfAQP in detergent solution

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (presumed; crystallization details not fully specified)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified PfAQP</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in I422 space group with cell dimensions a=b=92.4 Å, c=193.2 Å. Data collected to 2.05 Å. Two crystals used for complete data collection.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3c02">3C02</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHMLFYK</span><span class="topo-outside">SYVREF</span><span class="topo-membrane">IGEFLGTFVLMFLGEGAT</span><span class="topo-inside">ANFHTTGLSGDWY</span><span class="topo-membrane">KLCLGWGLAVFFGILVSA</span><span class="topo-outside">KLSGA</span><span class="topo-unknown">HLNLAVSIGLSS</span><span class="topo-outside">INKFDLKK</span><span class="topo-membrane">IPVYFFAQLLGAFVGTSTV</span><span class="topo-inside">YGLYHGFISNSKIP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QFAWETSRNPSISLTGA</span><span class="topo-membrane">FFNELILTGILLLVILVV</span><span class="topo-outside">VDENICGKFHIL</span><span class="topo-membrane">KLSSVVGLIILCIGITFG</span><span class="topo-inside">GNTG</span><span class="topo-unknown">FALNPSRDLGSRFL</span><span class="topo-inside">SLIAYGKDTFTKDNFYF</span><span class="topo-membrane">WVPLVAPCVGSVVFCQFY</span><span class="topo-outside">DK</span></span>
<span class="topo-ruler">       250        </span>
<span class="topo-line"><span class="topo-outside">VICPLVDLA</span><span class="topo-unknown">NNEKDGVDL</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>13</td>
      <td>8</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>31</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>44</td>
      <td>32</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>62</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>63</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>79</td>
      <td>68</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>87</td>
      <td>80</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>106</td>
      <td>88</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>137</td>
      <td>107</td>
      <td>137</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>155</td>
      <td>138</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>167</td>
      <td>156</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>185</td>
      <td>168</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>189</td>
      <td>186</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>203</td>
      <td>190</td>
      <td>203</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>204</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>249</td>
      <td>239</td>
      <td>249</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>258</td>
      <td>250</td>
      <td>258</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3c02">3C02</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHMLFYK</span><span class="topo-outside">SYVREF</span><span class="topo-membrane">IGEFLGTFVLMFLGEGAT</span><span class="topo-inside">ANFHTTGLSGDWY</span><span class="topo-membrane">KLCLGWGLAVFFGILVSA</span><span class="topo-outside">KLSGA</span><span class="topo-unknown">HLNLAVSIGLSS</span><span class="topo-outside">INKFDLKK</span><span class="topo-membrane">IPVYFFAQLLGAFVGTSTV</span><span class="topo-inside">YGLYHGFISNSKIP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QFAWETSRNPSISLTGA</span><span class="topo-membrane">FFNELILTGILLLVILVV</span><span class="topo-outside">VDENICGKFHIL</span><span class="topo-membrane">KLSSVVGLIILCIGITFG</span><span class="topo-inside">GNTG</span><span class="topo-unknown">FALNPSRDLGSRFL</span><span class="topo-inside">SLIAYGKDTFTKDNFYF</span><span class="topo-membrane">WVPLVAPCVGSVVFCQFY</span><span class="topo-outside">DK</span></span>
<span class="topo-ruler">       250        </span>
<span class="topo-line"><span class="topo-outside">VICPLVDLA</span><span class="topo-unknown">NNEKDGVDL</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>13</td>
      <td>8</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>31</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>44</td>
      <td>32</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>62</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>63</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>79</td>
      <td>68</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>87</td>
      <td>80</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>106</td>
      <td>88</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>137</td>
      <td>107</td>
      <td>137</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>155</td>
      <td>138</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>167</td>
      <td>156</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>185</td>
      <td>168</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>189</td>
      <td>186</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>203</td>
      <td>190</td>
      <td>203</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>204</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>249</td>
      <td>239</td>
      <td>249</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>258</td>
      <td>250</td>
      <td>258</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3c02">3C02</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHMLFYK</span><span class="topo-outside">SYVREF</span><span class="topo-membrane">IGEFLGTFVLMFLGEGAT</span><span class="topo-inside">ANFHTTGLSGDWY</span><span class="topo-membrane">KLCLGWGLAVFFGILVSA</span><span class="topo-outside">KLSGA</span><span class="topo-unknown">HLNLAVSIGLSS</span><span class="topo-outside">INKFDLKK</span><span class="topo-membrane">IPVYFFAQLLGAFVGTSTV</span><span class="topo-inside">YGLYHGFISNSKIP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QFAWETSRNPSISLTGA</span><span class="topo-membrane">FFNELILTGILLLVILVV</span><span class="topo-outside">VDENICGKFHIL</span><span class="topo-membrane">KLSSVVGLIILCIGITFG</span><span class="topo-inside">GNTG</span><span class="topo-unknown">FALNPSRDLGSRFL</span><span class="topo-inside">SLIAYGKDTFTKDNFYF</span><span class="topo-membrane">WVPLVAPCVGSVVFCQFY</span><span class="topo-outside">DK</span></span>
<span class="topo-ruler">       250        </span>
<span class="topo-line"><span class="topo-outside">VICPLVDLA</span><span class="topo-unknown">NNEKDGVDL</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>13</td>
      <td>8</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>31</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>44</td>
      <td>32</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>62</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>63</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>79</td>
      <td>68</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>87</td>
      <td>80</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>106</td>
      <td>88</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>137</td>
      <td>107</td>
      <td>137</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>155</td>
      <td>138</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>167</td>
      <td>156</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>185</td>
      <td>168</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>189</td>
      <td>186</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>203</td>
      <td>190</td>
      <td>203</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>204</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>249</td>
      <td>239</td>
      <td>249</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>258</td>
      <td>250</td>
      <td>258</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3c02">3C02</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHMLFYK</span><span class="topo-outside">SYVREF</span><span class="topo-membrane">IGEFLGTFVLMFLGEGAT</span><span class="topo-inside">ANFHTTGLSGDWY</span><span class="topo-membrane">KLCLGWGLAVFFGILVSA</span><span class="topo-outside">KLSGA</span><span class="topo-unknown">HLNLAVSIGLSS</span><span class="topo-outside">INKFDLKK</span><span class="topo-membrane">IPVYFFAQLLGAFVGTSTV</span><span class="topo-inside">YGLYHGFISNSKIP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QFAWETSRNPSISLTGA</span><span class="topo-membrane">FFNELILTGILLLVILVV</span><span class="topo-outside">VDENICGKFHIL</span><span class="topo-membrane">KLSSVVGLIILCIGITFG</span><span class="topo-inside">GNTG</span><span class="topo-unknown">FALNPSRDLGSRFL</span><span class="topo-inside">SLIAYGKDTFTKDNFYF</span><span class="topo-membrane">WVPLVAPCVGSVVFCQFY</span><span class="topo-outside">DK</span></span>
<span class="topo-ruler">       250        </span>
<span class="topo-line"><span class="topo-outside">VICPLVDLA</span><span class="topo-unknown">NNEKDGVDL</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>13</td>
      <td>8</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>31</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>44</td>
      <td>32</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>62</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>63</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>79</td>
      <td>68</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>87</td>
      <td>80</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>106</td>
      <td>88</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>137</td>
      <td>107</td>
      <td>137</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>155</td>
      <td>138</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>167</td>
      <td>156</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>185</td>
      <td>168</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>189</td>
      <td>186</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>203</td>
      <td>190</td>
      <td>203</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>204</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>249</td>
      <td>239</td>
      <td>249</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>258</td>
      <td>250</td>
      <td>258</td>
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

### Triply-satisfied arginine selectivity filter determines high water conductance

PfAQP conducts water as efficiently as water-specific channels, yet also passes [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) well. A key structural difference from the homologous [GLPF](/xray-mp-wiki/proteins/other-ion-channels/glpf/) (which conducts water poorly) is the hydrogen-bonding network around the conserved selectivity filter arginine (Arg196). In low-water-conductance [GLPF](/xray-mp-wiki/proteins/other-ion-channels/glpf/), only one of the two guanidinium NH donors (NH₁) is satisfied by protein hydrogen bonds. In PfAQP and all water-specific aquaporins, both NH₁ and NH₂ donate three hydrogen bonds to protein moieties. This triply-satisfied arginine has a decreased desolvation energy cost, allowing more rapid water passage through the channel.

### Compensatory mutations in NPA motifs preserve channel function

All Plasmodium aquaporins bear rare substitutions in the otherwise universally conserved NPA (Asn-Pro-Ala) motifs: NLA (Asn70-Leu71-Ala72) in the M3 half-helix and NPS (Asn193-Pro194-Ser195) in the M7 half-helix. Despite these changes, the essential interactions are preserved: the carbonyl of Asn70 accepts a hydrogen bond from Ala72's backbone amide, and Asn193's carbonyl accepts from Ser195's backbone amide. This maintains the proper orientation of the two signature asparagine N-H donors into the center of the conduction channel, which is essential for proton exclusion and substrate specificity.

### Glycerol and water conduction in proteoliposomes

Reconstituted PfAQP proteoliposomes show high rates of both [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) and water conductance. Light-scattering assays measure [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) conductance at 15.8 ± 0.2 (vs. 0.066 ± 0.003 for empty liposomes) and water conductance at 21.5 ± 0.8 (vs. 4.5 ± 0.1 for liposomes). These relative rates confirm that the heterologously expressed eukaryotic protein is fully functional and demonstrate PfAQP's dual high-efficiency conductance.

### Malarial aquaglyceroporin as a virulence factor

PfAQP is expressed on the parasite surface and is maximal during the later blood-stage when parasite growth is greatest. Knocking out the ortholog in P. berghei (PbAQP) impedes parasite growth, decreases parasitemia, and increases survival time of infected mice. The mutant parasites have greatly diminished [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) uptake. Host AQP9 (the major [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) uptake pathway in murine erythrocytes) knockout also increases mouse resistance to P. berghei infection, highlighting the importance of [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) acquisition for malarial virulence.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glpf/">GLPF</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
