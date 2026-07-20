---
title: "Human Cholecystokinin B Receptor (CCKᴅR)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein]
sources: [doi/10.1038##s41589-021-00866-8]
verified: agent
uniprot_id: P32238
---

# Human Cholecystokinin B Receptor (CCKᴅR)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P32238">UniProt: P32238</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The human cholecystokinin B receptor (CCKᴅR) is a class A G-protein-coupled receptor (GPCR) that recognizes both sulfated cholecystokinin (CCK) and gastrin peptides with similar affinities. CCKᴅR is involved in satiety regulation, anxiety, memory, and drug addiction, and can activate both Gᵢ and G₉ signaling pathways. Cryo-electron microscopy structures of human CCKᴅR in complex with the endogenous peptide gastrin-17 and two different G proteins — Gᵢ₂ (3.1 Å resolution) and G₉ (3.3 Å resolution) — revealed the fully active receptor conformation and provided insights into G protein coupling selectivity.

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7f8x">7F8X</a></td>
      <td>3.10</td>
      <td></td>
      <td>Human CCKᴅR with N-terminal HA signal and <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>, C-terminal PreScission-Strep tag, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> (419-447)</td>
      <td>Gastrin-17 (endogenous peptide agonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7f8y">7F8Y</a></td>
      <td>3.30</td>
      <td></td>
      <td>Human CCKᴅR with N-terminal HA signal and <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>, C-terminal PreScission-Strep tag, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> (419-447)</td>
      <td>Gastrin-17 (endogenous peptide agonist)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: High Five insect cells (Bac-to-Bac baculovirus expression system)
- **Construct**: Human CCKᴅR with N-terminal HA signal sequence and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), C-terminal [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) site followed by 2× Strep-tag; C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) of residues 419-447

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
      <td>20 mM HEPES pH 7.5, 200 mM NaCl, 5 mM CaCl₂, 10 µM gastrin-17, 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Co-expression with G proteins; solubilization for 2 h at 4°C</td>
    </tr>
    <tr>
      <td>2. G protein complex assembly</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> 35 (<a href="/xray-mp-wiki/reagents/antibodies/nb35/">Nb35 Nanobody</a>) addition</td>
      <td>—</td>
      <td>20 mM HEPES pH 7.5, 200 mM NaCl, 5 mM CaCl₂, 10 µM gastrin-17, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td><a href="/xray-mp-wiki/reagents/antibodies/nb35/">Nb35 Nanobody</a> added to stabilize G protein-receptor complex</td>
    </tr>
    <tr>
      <td>3. M1 anti-Flag <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> affinity purification</td>
      <td>—</td>
      <td>20 mM HEPES pH 7.5, 200 mM NaCl, 5 mM CaCl₂, 10 µM gastrin-17, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Elution with <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> peptide</td>
    </tr>
    <tr>
      <td>4. Size-exclusion chromatography</td>
      <td>Superose 6 10/300 GL</td>
      <td>—</td>
      <td>20 mM HEPES pH 7.5, 200 mM NaCl, 5 mM CaCl₂, 10 µM gastrin-17, 0.00075% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.00025% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 0.00025% <a href="/xray-mp-wiki/reagents/detergents/glyco-diosgenin/">GDN</a></td>
      <td>Peak fractions collected for <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> grid preparation</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Cryo-electron microscopy (single particle)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CCKᴅR-gastrin-17-G protein-<a href="/xray-mp-wiki/reagents/antibodies/nb35/">Nb35 Nanobody</a> complex</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected on Titan Krios with K3 detector. Processing in RELION3.1. Resolution: 3.1 Å (Gᵢ₂ complex) and 3.3 Å (G₉ complex). Local resolution estimation by ResMap.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8x">7F8X</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDGAPDVVDSLLVNGSNITPPCELGLENETLFCLDQPRPS</span><span class="topo-inside">KEW</span><span class="topo-membrane">QPAVQILLYSLIFLLSVLGNTLVITV</span><span class="topo-outside">LIRNKRMRTVTNI</span><span class="topo-membrane">FLLSLAVSDLMLCLFCMPFNLIPNL</span><span class="topo-inside">LKDFIF</span><span class="topo-membrane">GS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AVCKTTTYFMGTSVSVSTWNLVAIS</span><span class="topo-outside">LERYGAICKPLQSRVWQTKSHAL</span><span class="topo-membrane">KVIAATWCLSFTIMTPYPIYSN</span><span class="topo-inside">LVPFTKNNNQTANMCRFLLPND</span><span class="topo-membrane">VMQQSWHTFLLLILFLIPGIVMMVAYG</span><span class="topo-outside">L</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ISLELYQGINIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYAANLMAKKRVIR</span><span class="topo-membrane">MLIVIVVLFFLCWMPIFSANAWRAY</span><span class="topo-inside">DTASAERRLSGT</span><span class="topo-membrane">PISFILLLSYTSSCVNPIIYCF</span></span>
<span class="topo-ruler">       490       500       510       520       530    </span>
<span class="topo-line"><span class="topo-membrane">M</span><span class="topo-outside">NKRFRLG</span><span class="topo-unknown">FMATFPCCPNPGPPGARGEVGEEEEGEFLEVLFQGPHHHHHHHHHH</span></span>
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
      <td>45</td>
      <td>-8</td>
      <td>36</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>46</td>
      <td>48</td>
      <td>37</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>74</td>
      <td>40</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>87</td>
      <td>66</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>112</td>
      <td>79</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>118</td>
      <td>104</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>145</td>
      <td>110</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>168</td>
      <td>137</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>190</td>
      <td>160</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>212</td>
      <td>182</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>239</td>
      <td>204</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>290</td>
      <td>231</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>291</td>
      <td>355</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>292</td>
      <td>387</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>293</td>
      <td>407</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>421</td>
      <td>420</td>
      <td>547</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>446</td>
      <td>548</td>
      <td>572</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>447</td>
      <td>458</td>
      <td>573</td>
      <td>584</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>459</td>
      <td>481</td>
      <td>585</td>
      <td>607</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>482</td>
      <td>488</td>
      <td>608</td>
      <td>614</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>534</td>
      <td>615</td>
      <td>660</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f8y">7F8Y</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDGAPDVVDSLLVNGSNITPPCELGLENETLFCLDQPRPS</span><span class="topo-outside">KEW</span><span class="topo-membrane">QPAVQILLYSLIFLLSVLGNTLVITVLI</span><span class="topo-inside">RNKRMRTVT</span><span class="topo-membrane">NIFLLSLAVSNLMLCLFCMPFNLI</span><span class="topo-outside">PNLLKDFIFGS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">A</span><span class="topo-membrane">VCKTTTYFMGTSVSVSTWNLVAISL</span><span class="topo-inside">ERYGAICKPLQSRVWQTKSH</span><span class="topo-membrane">ALKVIAATWCLSFTIMTPYPIYS</span><span class="topo-outside">NLVPFTKNNNQTANMCRFLLPNDVM</span><span class="topo-membrane">QQSWHTFLLLILFLIPGIVMMVAYG</span><span class="topo-inside">L</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ISLELYQGINIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">GFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYAANLMAKKRVI</span><span class="topo-membrane">RMLIVIVVLFFLCWMPIFSANAW</span><span class="topo-outside">RAYDTASAERRLSGT</span><span class="topo-membrane">PISFILLLSYTSSCVNPIIYCF</span></span>
<span class="topo-ruler">       490       500       510       520       530    </span>
<span class="topo-line"><span class="topo-membrane">M</span><span class="topo-inside">NK</span><span class="topo-unknown">RFRLGFMATFPCCPNPGPPGARGEVGEEEEGEFLEVLFQGPHHHHHHHHHH</span></span>
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
      <td>45</td>
      <td>-8</td>
      <td>36</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>46</td>
      <td>48</td>
      <td>37</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>76</td>
      <td>40</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>85</td>
      <td>68</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>109</td>
      <td>77</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>121</td>
      <td>101</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>146</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>166</td>
      <td>138</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>189</td>
      <td>158</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>214</td>
      <td>181</td>
      <td>205</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>239</td>
      <td>206</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>249</td>
      <td>231</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>409</td>
      <td>1241</td>
      <td>1400</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>420</td>
      <td>302</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>443</td>
      <td>313</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>458</td>
      <td>336</td>
      <td>350</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>459</td>
      <td>481</td>
      <td>351</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>482</td>
      <td>483</td>
      <td>374</td>
      <td>375</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>534</td>
      <td>376</td>
      <td>426</td>
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

### G protein coupling promiscuity

CCKᴅR can activate both Gᵢ and G₉ signaling pathways. The [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structures with Gᵢ₂ and G₉ showed that both G proteins insert into the same binding pocket formed by helices II, III, VI, VII and the intracellular loops, but with an approximately 8° rotation of the G protein heterotrimer between the two complexes. Differences in ICL2 interactions with the G protein αN helix were observed: residues R163 and V164 in CCKᴅR form hydrophobic interactions with G₉ αN, while only V164 interacts with Gᵢ₂.

### ECL2 dynamics in peptide discrimination

Unlike CCKₐR (which has R197 in ECL2 forming a salt bridge with sulfated tyrosine), CCKᴅR has a valine at the equivalent position, removing the spatial hindrance that prevents gastrin binding to CCKₐR. Instead, W209 in CCKᴅR ECL2 pushes H207 toward gastrin for a hydrogen bond with the peptide backbone, enabling gastrin recognition.

### Active state conformation

The active CCKᴅR structures show an approximately 6 Å outward movement of helix VI, smaller than typical class A GPCR-G protein complexes (∼8-14 Å). An approximately 8° rotation between Gᵢ₂ and G₉ heterotrimers was observed, reflecting different binding modes of the two G proteins.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/human-ccka-receptor/">Human Cholecystokinin A Receptor (CCKₐR)</a> — Sister receptor with distinct peptide selectivity; structures from same study showing antagonist and agonist-bound states
- <a href="/xray-mp-wiki/concepts/signaling-receptors/cck-receptor-peptide-selectivity/">Peptide Selectivity in Cholecystokinin Receptors</a> — Structural comparison reveals basis for differential peptide recognition between CCKₐR and CCKᴅR
- <a href="/xray-mp-wiki/concepts/signaling-receptors/cck-receptor-stepwise-activation/">Stepwise Activation of Cholecystokinin Receptors</a> — Active CCKᴅR-G protein structures represent the fully active state in the stepwise activation model
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/antibodies/nb35/">Nb35 Nanobody</a> — Antibody used in crystallization or binding studies
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/glyco-diosgenin/">GDN</a> — Detergent used in purification or crystallization
