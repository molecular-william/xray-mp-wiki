---
title: "MastR (Mastigocladopsis repens Rhodopsin)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.RA120.014118]
verified: false
---

# MastR (Mastigocladopsis repens Rhodopsin)

## Overview

MastR (Mastigocladopsis repens rhodopsin, also known as MrHR) is a cyanobacterial chloride-pumping microbial rhodopsin representing the third group of known anion pumps with a characteristic Thr-Ser-Asp (TSD) motif in the ion transport pathway. The crystal structure was determined at 2.33 A resolution using the [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) method, revealing a trimeric arrangement reminiscent of [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (BR)-like proton pumps. The structure shows two chloride ion-binding sites: a primary site adjacent the protonated [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base (PRSB) coordinated by Thr-74 and Ser-78 of the TSD motif, and a secondary crystal-contact site. The MastR-T74D mutant structure (2.50 A) converts the chloride pump into an efficient proton pump by replacing the chloride ion with the carboxylate side chain of Asp-74, maintaining the extended hydrogen-bonding network required for outward proton transport. The strong structural similarity between MastR and BR explains why functional conversion from Cl- to H+ pump is possible for MastR but not for archaeal halorhodopsins.


## Publications

### doi/10.1074##jbc.RA120.014118

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6x13">6X13</a></td>
      <td>2.33 A</td>
      <td>not specified</td>
      <td>Full-length MastR with C-terminal hexahistidine tag (wild-type, chloride pump)</td>
      <td>all-trans-<a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, chloride ion</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6wp8">6WP8</a></td>
      <td>2.50 A</td>
      <td>not specified</td>
      <td>MastR T74D mutant with C-terminal hexahistidine tag (proton pump)</td>
      <td>all-trans-<a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: Full-length MastR with C-terminal His6 tag in pET21a(+)

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
      <td>Cell lysis</td>
      <td>Emulsiflex C3 homogenizer</td>
      <td>—</td>
      <td>50 mM MES pH 6.5, 300 mM NaCl, protease inhibitor cocktail</td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td></td>
      <td>Crude membranes pelleted at 125,000 x g for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM MES pH 6.5, 300 mM NaCl + 2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>HisTrap 1 mL Ni-NTA</td>
      <td>0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 50 mM MES pH 6.5, 300 mM NaCl</td>
      <td>Detergent exchanged to 2% OG during wash before elution</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>—</td>
      <td>10 mM MES pH 6.5, 300 mM NaCl, 0.8% OG</td>
      <td>Purity >95% by SDS-PAGE (A537nm/A280nm > 0.6)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle Crystallization</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>24% <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a> MME, 100 mM sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 5.0, 200 mM <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Bicelles composed of DMPC-<a href="/xray-mp-wiki/reagents/detergents/chapso/">CHAPSO</a> (2.8:1 ratio, 24% w/v). Crystals grown in hanging drops</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6x13">6X13</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">?</span><span class="topo-outside">G</span><span class="topo-unknown">LYRKYI</span><span class="topo-outside">EYPV</span><span class="topo-membrane">LQKILIGLILGAIVGLIL</span><span class="topo-inside">GHYGYA</span><span class="topo-unknown">HAVHTY</span><span class="topo-membrane">VKPFGDLFVRLLCMLVMP</span></span>
<span class="topo-line"><span class="topo-membrane">IVFASLV</span><span class="topo-outside">VGAASISPARLGRVGVKIVVYYL</span><span class="topo-membrane">LTSAFAVTLGIIMARLFNPGAGI</span><span class="topo-inside">HLAVGGQ</span></span>
<span class="topo-line"><span class="topo-inside">QFQPHQAPP</span><span class="topo-membrane">LVHILLDIVPTNPFGALANGQVLPTIFFAIILG</span><span class="topo-outside">IAITYLMNSENE</span><span class="topo-unknown">KVRKSA</span></span>
<span class="topo-line"><span class="topo-unknown">ETLLDAINGLAEA</span><span class="topo-membrane">MYKIVNGVMQYAPIGVFALIAYVM</span><span class="topo-inside">AEQGV</span><span class="topo-membrane">HVVGELAKVTAAVYVGLT</span></span>
<span class="topo-line"><span class="topo-membrane">LQ</span><span class="topo-outside">ILLVYFVLLKIYGIDPISFIKHAKDAMLTAFVTRSSSGTLPVTMRVAKEMGISEGIYS</span></span>
<span class="topo-line"><span class="topo-outside">FTLPLGATINMD</span><span class="topo-membrane">GTALYQGVATFFIANA</span><span class="topo-inside">LGSHL</span><span class="topo-membrane">TVGQQLTIVLTAVLASIGT</span><span class="topo-outside">AGVP</span><span class="topo-membrane">GAGA</span></span>
<span class="topo-line"><span class="topo-membrane">IMLCMVLHSVGLPLTDP</span><span class="topo-inside">N</span><span class="topo-membrane">VAAAYAMILGIDAILD</span><span class="topo-outside">MGRTMVNVTGDLTGTAIVAKTEGT</span><span class="topo-unknown">LV</span></span>
<span class="topo-line"><span class="topo-unknown">PR</span></span>
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
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>8</td>
      <td>3</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>12</td>
      <td>9</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>30</td>
      <td>13</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>36</td>
      <td>31</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>42</td>
      <td>37</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>43</td>
      <td>67</td>
      <td>43</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>90</td>
      <td>68</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>113</td>
      <td>91</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>129</td>
      <td>114</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>162</td>
      <td>130</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>174</td>
      <td>163</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>193</td>
      <td>175</td>
      <td>193</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>194</td>
      <td>217</td>
      <td>194</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>242</td>
      <td>223</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>312</td>
      <td>243</td>
      <td>312</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>313</td>
      <td>328</td>
      <td>313</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>333</td>
      <td>329</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>352</td>
      <td>334</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>356</td>
      <td>353</td>
      <td>356</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>377</td>
      <td>357</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>378</td>
      <td>378</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>394</td>
      <td>379</td>
      <td>394</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>395</td>
      <td>418</td>
      <td>395</td>
      <td>418</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6wp8">6WP8</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MTQAW</span><span class="topo-membrane">LWIGVISMALGSVFFGFGAHN</span><span class="topo-outside">AKNERWQ</span><span class="topo-membrane">ILYTLNFFICLIAAGLYLAM</span><span class="topo-inside">ALGLGVN</span></span>
<span class="topo-line"><span class="topo-inside">VINGRPTYW</span><span class="topo-membrane">VRFVDWFCSTPLLLLDLTFL</span><span class="topo-outside">GRTSL</span><span class="topo-membrane">PLTGSLLGANAYMLVTGFVA</span><span class="topo-inside">TVTPKP</span></span>
<span class="topo-line"><span class="topo-inside">MSYI</span><span class="topo-membrane">WYIVSCAAYLAIVYLLAQPYR</span><span class="topo-outside">IAAERKHPRSKQAF</span><span class="topo-membrane">RTLVTVHLVLWTLYPIVWIL</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-inside">PEGFSTFTQGSE</span><span class="topo-membrane">TMFYTLLDIASKVGFGFLSLNT</span><span class="topo-outside">LHTLEQAT</span><span class="topo-unknown">EPARETHLSYLEHHHHHH</span></span>
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
      <td>1</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>6</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>27</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>34</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>69</td>
      <td>54</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>89</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>90</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>114</td>
      <td>95</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>124</td>
      <td>115</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>159</td>
      <td>146</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>179</td>
      <td>160</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>192</td>
      <td>180</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>214</td>
      <td>193</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>222</td>
      <td>215</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6wp8">6WP8</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MTQAW</span><span class="topo-membrane">LWIGVISMALGSVFFGFGAHN</span><span class="topo-outside">AKNERWQ</span><span class="topo-membrane">ILYTLNFFICLIAAGLYLAM</span><span class="topo-inside">ALGLGVN</span></span>
<span class="topo-line"><span class="topo-inside">VINGRPTYW</span><span class="topo-membrane">VRFVDWFCSTPLLLLDLTFL</span><span class="topo-outside">GRTSL</span><span class="topo-membrane">PLTGSLLGANAYMLVTGFVA</span><span class="topo-inside">TVTPKP</span></span>
<span class="topo-line"><span class="topo-inside">MSYI</span><span class="topo-membrane">WYIVSCAAYLAIVYLLAQPYR</span><span class="topo-outside">IAAERKHPRSKQAF</span><span class="topo-membrane">RTLVTVHLVLWTLYPIVWIL</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-inside">PEGFSTFTQGSE</span><span class="topo-membrane">TMFYTLLDIASKVGFGFLSLNT</span><span class="topo-outside">LHTLEQAT</span><span class="topo-unknown">EPARETHLSYLEHHHHHH</span></span>
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
      <td>1</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>6</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>27</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>34</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>69</td>
      <td>54</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>89</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>90</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>114</td>
      <td>95</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>124</td>
      <td>115</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>159</td>
      <td>146</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>179</td>
      <td>160</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>192</td>
      <td>180</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>214</td>
      <td>193</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>222</td>
      <td>215</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6wp8">6WP8</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MTQAW</span><span class="topo-membrane">LWIGVISMALGSVFFGFGAHN</span><span class="topo-outside">AKNERWQ</span><span class="topo-membrane">ILYTLNFFICLIAAGLYLAM</span><span class="topo-inside">ALGLGVN</span></span>
<span class="topo-line"><span class="topo-inside">VINGRPTYW</span><span class="topo-membrane">VRFVDWFCSTPLLLLDLTFL</span><span class="topo-outside">GRTSL</span><span class="topo-membrane">PLTGSLLGANAYMLVTGFVA</span><span class="topo-inside">TVTPKP</span></span>
<span class="topo-line"><span class="topo-inside">MSYI</span><span class="topo-membrane">WYIVSCAAYLAIVYLLAQPYR</span><span class="topo-outside">IAAERKHPRSKQAF</span><span class="topo-membrane">RTLVTVHLVLWTLYPIVWIL</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-inside">PEGFSTFTQGSE</span><span class="topo-membrane">TMFYTLLDIASKVGFGFLSLNT</span><span class="topo-outside">LHTLEQAT</span><span class="topo-unknown">EPARETHLSYLEHHHHHH</span></span>
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
      <td>1</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>6</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>27</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>34</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>69</td>
      <td>54</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>89</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>90</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>114</td>
      <td>95</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>124</td>
      <td>115</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>159</td>
      <td>146</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>179</td>
      <td>160</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>192</td>
      <td>180</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>214</td>
      <td>193</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>222</td>
      <td>215</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### TSD motif and chloride binding

The primary chloride ion is coordinated by Thr-74 and Ser-78 of the TSD motif (d(Cl-O) = 3.1 A and 3.0 A, respectively) and connected via a bridging water molecule (d(Cl-O) = 3.1 A) to the PRSB (d = 2.8 A) and the carboxyl group of Asp-200. The T74A mutation reduced chloride affinity from KD 2 mM to 85 mM, while S78T decreased affinity ~200-fold.

### BR-like trimeric assembly

MastR forms trimers in the crystal and in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) micelles (as shown by CD spectroscopy with bilobed spectra showing a positive peak at ~510 nm and negative at ~560 nm relative to 540 nm lambda-max). The trimer interface involves helix B interacting with helices D' and E' of adjacent protomers. Unlike eubacterial pumps, MastR lacks pentamer-inducing structural features (extended helix B and 3-omega motif).

### Functional conversion via T74D mutation

The MastR-T74D mutation converts the chloride pump into an efficient proton pump. The carboxylate side chain of Asp-74 fills the space occupied by Cl- in wild-type, maintaining the extended hydrogen-bonding network. The BR-like structure of MastR, including proper positioning of the Schiff base water and Ala-53 equivalent, enables this conversion, unlike archaeal halorhodopsins where similar mutations fail.

### Chloride transport pathway

The putative chloride entrance is between the B-C and F-G loops, gated by Glu-192 and Glu-182 (homologous to BR's proton-release pathway Glu-204/Glu-194). After photoisomerization, the chloride ion moves toward the cytoplasmic side, with His-166 identified as part of the chloride release pathway (H166A mutation slows photocycle >10-fold). Asp-85 deprotonation accompanies chloride translocation, with reprotonation preventing backflow.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/pharaonis-halorhodopsin/">Pharaonis Halorhodopsin (NpHR)</a> — Both are chloride-pumping microbial rhodopsins with similar chloride-binding motif
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — MastR shows closest structural homology to BR, with BR-like trimeric assembly and overall fold
- <a href="/xray-mp-wiki/proteins/rhodopsins/cir-nonlabens-marinus/">CIR (Nonlabens marinus)</a> — CIR represents the eubacterial group of chloride-pumping rhodopsins, distinct from MastR's cyanobacterial group
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/dtg-dts-rhodopsin/">DTG/DTS Rhodopsin Motif</a> — MastR contains a TSD motif, related to the function-determining motifs in ion-pumping rhodopsins
- <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle Crystallization</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a> — Additive used in purification or crystallization buffers
