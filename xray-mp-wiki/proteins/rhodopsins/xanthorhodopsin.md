---
title: "Xanthorhodopsin"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0807162105]
verified: agent
uniprot_id: Q2S2F8
---

# Xanthorhodopsin

<div class="expr-badges"><span class="expr-badge expr-native-tissue">Native tissue</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q2S2F8">UniProt: Q2S2F8</a>

<span class="expr-badge">Salinibacter ruber</span>

## Overview

Xanthorhodopsin is a light-driven proton pump from the eubacterium Salinibacter ruber that contains a dual chromophore system: a [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore and a noncovalently bound [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) ([Salinixanthin](/xray-mp-wiki/reagents/ligands/salinixanthin/)) antenna. The 1.9 Å crystal structure reveals 7 transmembrane helices similar to [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) and archaerhodopsin, but with considerably different architecture. The structure introduces novel structural motifs for proton transfer during the photocycle, particularly a His-62–Asp-96 complex for regulating the pKa of the primary proton acceptor, and a dramatically different proton release mechanism compared to archaeal pumps. The close approach of the [Salinixanthin](/xray-mp-wiki/reagents/ligands/salinixanthin/) and [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) polyenes (center-to-center distance 11.7 Å, 46° angle) explains the ~45% efficiency of excited-state energy transfer from the [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) antenna to [Retinal](/xray-mp-wiki/reagents/ligands/retinal/). This structure defines the geometry of the dual chromophore system and provides a model for eubacterial proton pump mechanisms.


## Publications

### doi/10.1073##pnas.0807162105

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ddl">3DDL</a></td>
      <td>1.9</td>
      <td>P1</td>
      <td>Full-length xanthorhodopsin from Salinibacter ruber</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> and <a href="/xray-mp-wiki/reagents/ligands/salinixanthin/">Salinixanthin</a> (<a href="/xray-mp-wiki/reagents/ligands/carotenoid/">Carotenoid</a> antenna)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Salinibacter ruber (native source)
- **Construct**: Native xanthorhodopsin

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
      <td>Cell disruption and membrane preparation</td>
      <td>French press</td>
      <td>--</td>
      <td>100 mM NaCl, 5 mM bicine (pH 8.0) + 0.01% dodecyl maltoside</td>
      <td>Cells broken and membranes washed with buffer containing 0.01% dodecyl maltoside</td>
    </tr>
    <tr>
      <td>Membrane resuspension</td>
      <td>Centrifugation</td>
      <td>--</td>
      <td>30 mM phosphate (pH 5.6), 1 mM sodium azide + --</td>
      <td>Membrane fraction resuspended to 5 mg/ml xanthorhodopsin</td>
    </tr>
    <tr>
      <td>Solubilization in bicelle medium</td>
      <td>Bicelle solubilization</td>
      <td>--</td>
      <td>-- + 16.7% (wt/wt) <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a> in 20% nonyl maltoside</td>
      <td>One volume of <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a>/nonyl maltoside bicelle mixture added to 3 volumes of xanthorhodopsin preparation, vortexed, incubated overnight at 4°C</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Solubilized xanthorhodopsin in bicelle medium (5 mg/ml)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>2.5-3 M <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> (pH 5.6)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>4-5 months</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Stepwise equilibration with 5%, 10%, then 15% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in sitting drops containing 10 µL solubilized xanthorhodopsin, 3 µL of 3 M <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> (pH 5.6), and 2 µL of 2.5 mM sodium azide. Crystals approximately 30 × 30 × 150 µm. Data collected at 100 K on SSRL beamline 9.1.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ddl">3DDL</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MLQ</span><span class="topo-inside">ELPTLTPGQYSLV</span><span class="topo-membrane">FNMFSFTVATMTASFVFFVLARNNV</span><span class="topo-outside">APKY</span><span class="topo-membrane">RISMMVSALVVFIAGYHYFRITS</span><span class="topo-inside">SWEAAYALQNGMYQPTGELFND</span><span class="topo-membrane">AYRYVDWLLTVPLLTVELVLVM</span><span class="topo-outside">GLPKNERG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">PLAAKLGFLAALMIVLGYPGEVS</span><span class="topo-inside">ENAAL</span><span class="topo-membrane">FGTRGLWGFLSTIPFVWILYILFTQL</span><span class="topo-outside">GDTIQRQSSRVST</span><span class="topo-membrane">LLGNARLLLLATWGFYPIAYMIPM</span><span class="topo-unknown">AFPEAF</span><span class="topo-inside">PSNTPGTIVA</span><span class="topo-membrane">LQVGYTIADVLAK</span></span>
<span class="topo-ruler">       250       260       270   </span>
<span class="topo-line"><span class="topo-membrane">AGYGVLIYNIAK</span><span class="topo-outside">AKSEEEGFN</span><span class="topo-unknown">VSEMVEPATASA</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>16</td>
      <td>4</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>41</td>
      <td>17</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>45</td>
      <td>42</td>
      <td>45</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>68</td>
      <td>46</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>90</td>
      <td>69</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>112</td>
      <td>91</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>113</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>143</td>
      <td>121</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>144</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>174</td>
      <td>149</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>187</td>
      <td>175</td>
      <td>187</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>211</td>
      <td>188</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>217</td>
      <td>212</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>218</td>
      <td>227</td>
      <td>218</td>
      <td>227</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>252</td>
      <td>228</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>253</td>
      <td>261</td>
      <td>253</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>273</td>
      <td>262</td>
      <td>273</td>
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

### Dual chromophore system with carotenoid antenna

Xanthorhodopsin contains both [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) and the [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) [Salinixanthin](/xray-mp-wiki/reagents/ligands/salinixanthin/) as a light-harvesting antenna. The center-to-center distance between the two chromophores is 11.7 Å, with ring moieties within 5 Å of each other. The 46° angle between chromophore axes represents a compromise between optimal capture of light of all polarization angles and efficient excited-state energy transfer (~45% efficiency). The [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) β-ionone ring forms part of the [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) binding site, explaining the dependence of the [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) spectrum on [Retinal](/xray-mp-wiki/reagents/ligands/retinal/).

### Asp-His counterion complex for pKa regulation

Unlike [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (pKa ~2.5), eubacterial proton pumps have a primary proton acceptor with pKa near 7. In xanthorhodopsin, His-62 ND1 forms a very short hydrogen bond (2.42-2.55 Å) with Asp-96 OD1, creating a shared-proton complex that acts as the Schiff base counterion. This Asp-His complex raises the effective pKa relative to aspartate alone and is conserved in proteorhodopsins, making it a general feature of eubacterial pumps.

### Reversed proton release sequence

Unlike [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/), xanthorhodopsin does not release a proton at the time of Schiff base deprotonation. Instead, proton uptake from the cytoplasm occurs first (via Glu-107 after it reprotonates the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base), and proton release to the extracellular surface is delayed until the final photocycle step. The carboxylate of Asp-96 is severely rotated, and the hydrogen-bonded aqueous network for proton release in BR is replaced by hydrogen-bonded residues more resistant to rearrangement.

### Dramatically different architecture from archaeal rhodopsins

The main chain of xanthorhodopsin differs more from [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) than any other crystallized microbial rhodopsin. Helices A and G are longer (by 4 and 9 residues respectively), and their tilt and rotation differ considerably. The B-C loop reorients dramatically, displacing its tip by 30 Å toward the periphery and creating a large cleft that brings functional residues near the aqueous interface.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/salinixanthin/">Salinixanthin</a> — Carotenoid antenna chromophore bound to xanthorhodopsin
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> — Primary chromophore of xanthorhodopsin
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Archaeal homolog with different proton release mechanism
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/proton-release-complex/">Proton Release Complex</a> — Xanthorhodopsin lacks the canonical proton release complex found in BR
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/evolution-of-rhodopsins/">Evolution of Rhodopsins</a> — Xanthorhodopsin reveals evolutionary divergence between archaeal and eubacterial proton pumps
- <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle Crystallization</a> — Structure was solved from crystals grown in bicelle medium
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/rhodopsins/anabaena-sensory-rhodopsin/">Anabaena Sensory Rhodopsin</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> — Buffer component in purification or crystallization
