---
title: "PaNhaP Sodium/Proton Antiporter from Pyrococcus abyssi"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##ELIFE.03579]
verified: false
---

# PaNhaP Sodium/Proton Antiporter from Pyrococcus abyssi

## Overview

PaNhaP is an electroneutral Na+/H+ antiporter from the hyperthermophilic archaeon *Pyrococcus abyssi*, belonging to the CPA1 (cation-proton antiporter 1) family. It exchanges one Na+ for one H+ with 1:1 stoichiometry, playing roles in intracellular pH and sodium homeostasis. PaNhaP is a functional homologue of the medically important human Na+/H+ exchanger NHE1 and serves as a structural model for understanding CPA1 transport mechanisms. It functions as a homodimer, with each protomer containing 13 transmembrane helices (H1-H13) arranged in an inverted 6-helix repeat. The structure was determined in two conformations (pH 8 and pH 4) by X-ray crystallography, with the substrate ion (Tl+ as Na+ surrogate) bound at pH 8. The ion-binding site at the deepest point of a negatively charged cytoplasmic funnel is coordinated by three acidic sidechains (Glu73, Asp130, Asp159), a water molecule, Ser155, and the main-chain carbonyl of Thr129. Transport activity is pH-dependent and cooperative at pH 6, mediated by allosteric coupling through His292 at the dimer interface.


## Publications

### doi/10.7554##ELIFE.03579

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4cz8">4CZ8</a></td>
      <td>3.15</td>
      <td>P21</td>
      <td>SeMet-labeled PaNhaP, CPD fusion cleaved</td>
      <td>Na+ (substrate ion)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4cz9">4CZ9</a></td>
      <td>3.5</td>
      <td>P64</td>
      <td>Native PaNhaP, CPD fusion cleaved</td>
      <td>none (no bound Na+)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4cza">4CZA</a></td>
      <td>3.2</td>
      <td>P21</td>
      <td>Native PaNhaP, thallium-soaked at pH 8</td>
      <td>Tl+ (Na+ surrogate)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41-(DE3)
- **Construct**: Codon-optimized PaNhaP (WP_010868413.1) with C-terminal CPD (cysteine protease domain) fusion
- **Notes**: CPD fusion allows tag-free elution by inositol-hexaphosphate cleavage. SeMet-labeled protein expressed in PASM-5052 medium with 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/).
- **Induction**: ZYM-5052 autoinduction medium, 10 hr at 37°C

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
      <td>Membrane isolation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>20 mM Tris pH 7.4, 250 mM <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a>, 140 mM <a href="/xray-mp-wiki/reagents/ligands/choline/">Choline</a> chloride</td>
      <td>Membranes resuspended at 15 mg/ml protein</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>20 mM Tris pH 7.4, 150 mM NaCl, 30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1.5% Cymal-5</td>
      <td>Overnight solubilization at 4°C, clarified at 100,000xg for 1 hr</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin (Co2+ affinity)</td>
      <td>—</td>
      <td>Wash buffer - 20 mM Tris pH 7.4, 300 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.15% Cymal-5</td>
      <td>Supernatant with 5 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> incubated 2 hr with <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin at 4°C. Elution with 20 uM inositol-hexaphosphate cleaves CPD tag</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>10 mM Na-<a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 4.0, 300 mM NaCl, 0.15% Cymal-5</td>
      <td>Concentrated to 5 mg/ml. Pooled fractions diluted 1:4 with buffer containing 100 mM NaCl and re-concentrated</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PaNhaP at 5 mg/ml in SEC buffer</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM Tris/HCl pH 8.0, 100 mM CaCl2/MgCl2, 35-40% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3 months</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Direct vitrification in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Long needle-like crystals at pH 8. Used for SeMet SAD phasing and thallium soaks</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PaNhaP at 5 mg/ml in SEC buffer</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM Na-<a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 4.0, 100 mM CaCl2/MgCl2, 35-40% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>7 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Direct vitrification in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Trapezoidal crystals at pH 4, up to 200 um. Different space group and cell dimensions from pH 8 crystals</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4cz8">4CZ8</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MIELSL</span><span class="topo-membrane">AEALFLILFTGVISMLIS</span><span class="topo-outside">RRTGI</span><span class="topo-membrane">SYVPIFILTGLVIG</span><span class="topo-inside">PLLKLIPRDLAHEI</span><span class="topo-membrane">FDF</span></span>
<span class="topo-line"><span class="topo-membrane">VRVFGLVIILFTEG</span><span class="topo-outside">HNLS</span><span class="topo-unknown">WRLLKK</span><span class="topo-outside">NMPTI</span><span class="topo-membrane">VTLDTIGLILTALIAGFIF</span><span class="topo-inside">KVVFNSSFLLGF</span></span>
<span class="topo-line"><span class="topo-membrane">LFGAIIGATDPAT</span><span class="topo-outside">LIPLFRQYRVKQDIETVIVTE</span><span class="topo-membrane">SIFNDPLGIVLTLI</span><span class="topo-inside">AISMLVPGYGGG</span></span>
<span class="topo-line"><span class="topo-unknown">IFSTLSEKL</span><span class="topo-inside">GIY</span><span class="topo-membrane">AGGVIYFLYNVSVSISLGIFLG</span><span class="topo-outside">ILGYKFIKRTGIFDFPEIE</span><span class="topo-membrane">AFSLSLA</span></span>
<span class="topo-line"><span class="topo-membrane">FLGFFIGERL</span><span class="topo-inside">D</span><span class="topo-membrane">ASGYLVATVTG</span><span class="topo-outside">IVLGNYKLLKPRENIRILKRLQRAIEKEVHF</span><span class="topo-membrane">NDTLAAL</span></span>
<span class="topo-line"><span class="topo-membrane">ATIFIFVLLGAE</span><span class="topo-inside">MN</span><span class="topo-unknown">LEVIWS</span><span class="topo-inside">NL</span><span class="topo-membrane">GKGLLVALGVMILARPLATLPL</span><span class="topo-outside">LKWWNFREYLFI</span><span class="topo-membrane">ALEG</span></span>
<span class="topo-line"><span class="topo-membrane">PRGVVPSALAS</span><span class="topo-inside">LPLSLALKYKSPLLTVHWGEIIM</span><span class="topo-membrane">ATVVITVLTSVIVETLW</span><span class="topo-unknown">IPILKDKL</span><span class="topo-outside">D</span></span>
<span class="topo-line"><span class="topo-outside">VG</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>7</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>43</td>
      <td>30</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>57</td>
      <td>44</td>
      <td>57</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>74</td>
      <td>58</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>78</td>
      <td>75</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>79</td>
      <td>84</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>89</td>
      <td>85</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>108</td>
      <td>90</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>120</td>
      <td>109</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>133</td>
      <td>121</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>168</td>
      <td>155</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>180</td>
      <td>169</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>189</td>
      <td>181</td>
      <td>189</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>192</td>
      <td>190</td>
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
      <td>233</td>
      <td>215</td>
      <td>233</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>250</td>
      <td>234</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>262</td>
      <td>252</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>293</td>
      <td>263</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>312</td>
      <td>294</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>314</td>
      <td>313</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>315</td>
      <td>320</td>
      <td>315</td>
      <td>320</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>321</td>
      <td>322</td>
      <td>321</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>371</td>
      <td>357</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>394</td>
      <td>372</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>411</td>
      <td>395</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>419</td>
      <td>412</td>
      <td>419</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>420</td>
      <td>422</td>
      <td>420</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4cz8">4CZ8</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">IELSL</span><span class="topo-membrane">AEALFLILFTGVISMLIS</span><span class="topo-outside">RRTGI</span><span class="topo-membrane">SYVPIFILTGLVIG</span><span class="topo-inside">PLLKLIPRDLAHEI</span><span class="topo-membrane">FDF</span></span>
<span class="topo-line"><span class="topo-membrane">VRVFGLVIILFTEG</span><span class="topo-outside">HNLS</span><span class="topo-unknown">WRLLKK</span><span class="topo-outside">NMPTI</span><span class="topo-membrane">VTLDTIGLILTALIAGFIF</span><span class="topo-inside">KVVFNSSFLLGF</span></span>
<span class="topo-line"><span class="topo-membrane">LFGAIIGATDPAT</span><span class="topo-outside">LIPLFRQYRVKQDIETVIVTE</span><span class="topo-membrane">SIFNDPLGIVLTLI</span><span class="topo-inside">AISMLVPGYGGG</span></span>
<span class="topo-line"><span class="topo-unknown">IFSTLSEKL</span><span class="topo-inside">GIYAGG</span><span class="topo-membrane">VIYFLYNVSVSISLGIFLG</span><span class="topo-outside">ILGYKFIKRTGIFDFPEIE</span><span class="topo-membrane">AFSLSLA</span></span>
<span class="topo-line"><span class="topo-membrane">FLGFFIGERL</span><span class="topo-inside">D</span><span class="topo-membrane">ASGYLVATVTG</span><span class="topo-outside">IVLGNYKLLKPRENIRILKRLQRAIEKEVHF</span><span class="topo-membrane">NDTLAAL</span></span>
<span class="topo-line"><span class="topo-membrane">ATIFIFVLLGAEM</span><span class="topo-inside">N</span><span class="topo-unknown">LEVIWS</span><span class="topo-inside">NL</span><span class="topo-membrane">GKGLLVALGVMILARPLATLPL</span><span class="topo-outside">LKWWNFREYLFIA</span><span class="topo-membrane">LEG</span></span>
<span class="topo-line"><span class="topo-membrane">PRGVVPSALAS</span><span class="topo-inside">LPLSLALKYKSPLLTVHWGEIIM</span><span class="topo-membrane">ATVVITVLTSVIVETLW</span><span class="topo-outside">IPILKDKLD</span></span>
<span class="topo-line"><span class="topo-outside">VG</span></span>
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
      <td>6</td>
      <td>2</td>
      <td>6</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>7</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>43</td>
      <td>30</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>57</td>
      <td>44</td>
      <td>57</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>74</td>
      <td>58</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>78</td>
      <td>75</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>79</td>
      <td>84</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>89</td>
      <td>85</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>108</td>
      <td>90</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>120</td>
      <td>109</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>133</td>
      <td>121</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>168</td>
      <td>155</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>180</td>
      <td>169</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>189</td>
      <td>181</td>
      <td>189</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>195</td>
      <td>190</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>214</td>
      <td>196</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>233</td>
      <td>215</td>
      <td>233</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>250</td>
      <td>234</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>262</td>
      <td>252</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>293</td>
      <td>263</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>313</td>
      <td>294</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>315</td>
      <td>320</td>
      <td>315</td>
      <td>320</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>321</td>
      <td>322</td>
      <td>321</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>357</td>
      <td>345</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>371</td>
      <td>358</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>394</td>
      <td>372</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>411</td>
      <td>395</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>422</td>
      <td>412</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4cz9">4CZ9</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">IE</span><span class="topo-membrane">LSLAEALFLILFTGVISMLIS</span><span class="topo-outside">RRTGI</span><span class="topo-membrane">SYVPIFILTGLVIGPLL</span><span class="topo-inside">KLIPRDLA</span><span class="topo-membrane">HEIFDF</span></span>
<span class="topo-line"><span class="topo-membrane">VRVFGLVIILFTEGH</span><span class="topo-outside">NLS</span><span class="topo-unknown">WRLLKK</span><span class="topo-outside">NM</span><span class="topo-membrane">PTIVTLDTIGLILTALIAGFIF</span><span class="topo-inside">KVVFNSSFLLG</span><span class="topo-membrane">F</span></span>
<span class="topo-line"><span class="topo-membrane">LFGAIIGATDPATL</span><span class="topo-outside">IPLFRQYRVKQDIETVI</span><span class="topo-membrane">VTESIFNDPLGIVLTLIA</span><span class="topo-inside">ISMLVPGYGGG</span></span>
<span class="topo-line"><span class="topo-unknown">IFSTLSEKL</span><span class="topo-inside">GIY</span><span class="topo-membrane">AGGVIYFLYNVSVSISLGIFLGILG</span><span class="topo-unknown">YKFIKRT</span><span class="topo-outside">GIFDFP</span><span class="topo-membrane">EIEAFSLSLA</span></span>
<span class="topo-line"><span class="topo-membrane">FLGFFIGERL</span><span class="topo-inside">D</span><span class="topo-membrane">ASGYLVATVTGIV</span><span class="topo-outside">LGNYKLLKPRENIRILKRLQRAIEKEVHF</span><span class="topo-membrane">NDTLAAL</span></span>
<span class="topo-line"><span class="topo-membrane">ATIFIFVLLGAEM</span><span class="topo-inside">N</span><span class="topo-unknown">LEVIWS</span><span class="topo-inside">NL</span><span class="topo-membrane">GKGLLVALGVMILARPLATLPLLK</span><span class="topo-outside">WWNFREY</span><span class="topo-membrane">LFIALEG</span></span>
<span class="topo-line"><span class="topo-membrane">PRGVVPSALASL</span><span class="topo-inside">PLSLALKYKSPLLTVHWGEII</span><span class="topo-membrane">MATVVITVLTSVIVETLW</span><span class="topo-unknown">IPILKD</span><span class="topo-outside">KLD</span></span>
<span class="topo-line"><span class="topo-unknown">VG</span></span>
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
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>24</td>
      <td>4</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>54</td>
      <td>47</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>75</td>
      <td>55</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>78</td>
      <td>76</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>79</td>
      <td>84</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>86</td>
      <td>85</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>108</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>119</td>
      <td>109</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>134</td>
      <td>120</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>151</td>
      <td>135</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>152</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>180</td>
      <td>170</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>189</td>
      <td>181</td>
      <td>189</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>192</td>
      <td>190</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>217</td>
      <td>193</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>224</td>
      <td>218</td>
      <td>224</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>225</td>
      <td>230</td>
      <td>225</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>250</td>
      <td>231</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>264</td>
      <td>252</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>293</td>
      <td>265</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>313</td>
      <td>294</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>315</td>
      <td>320</td>
      <td>315</td>
      <td>320</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>321</td>
      <td>322</td>
      <td>321</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>346</td>
      <td>323</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>347</td>
      <td>353</td>
      <td>347</td>
      <td>353</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>372</td>
      <td>354</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>373</td>
      <td>393</td>
      <td>373</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>411</td>
      <td>394</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>417</td>
      <td>412</td>
      <td>417</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>418</td>
      <td>420</td>
      <td>418</td>
      <td>420</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4cz9">4CZ9</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MIE</span><span class="topo-membrane">LSLAEALFLILFTGVISMLIS</span><span class="topo-outside">RRTGI</span><span class="topo-membrane">SYVPIFILTGLVIGPLL</span><span class="topo-inside">KLIPRDL</span><span class="topo-membrane">AHEIFDF</span></span>
<span class="topo-line"><span class="topo-membrane">VRVFGLVIILFTEGH</span><span class="topo-outside">NLS</span><span class="topo-unknown">WRLLKK</span><span class="topo-outside">NMP</span><span class="topo-membrane">TIVTLDTIGLILTALIAGFIF</span><span class="topo-inside">KVVFNSSFLLG</span><span class="topo-membrane">F</span></span>
<span class="topo-line"><span class="topo-membrane">LFGAIIGATDPATL</span><span class="topo-outside">IPLFRQYRVKQDIETVI</span><span class="topo-membrane">VTESIFNDPLGIVLTLIA</span><span class="topo-inside">ISMLVPGYGG</span><span class="topo-unknown">G</span></span>
<span class="topo-line"><span class="topo-unknown">IFSTLSEKL</span><span class="topo-inside">GIY</span><span class="topo-membrane">AGGVIYFLYNVSVSISLGIFLGILG</span><span class="topo-unknown">YKFIKRT</span><span class="topo-outside">GIFDFP</span><span class="topo-membrane">EIEAFSLSLA</span></span>
<span class="topo-line"><span class="topo-membrane">FLGFFIGERL</span><span class="topo-inside">D</span><span class="topo-membrane">ASGYLVATVTGIV</span><span class="topo-outside">LGNYKLLKPRENIRILKRLQRAIEKEVHF</span><span class="topo-membrane">NDTLAAL</span></span>
<span class="topo-line"><span class="topo-membrane">ATIFIFVLLGAEM</span><span class="topo-inside">N</span><span class="topo-unknown">LEVIWS</span><span class="topo-inside">NL</span><span class="topo-membrane">GKGLLVALGVMILARPLATLPLLK</span><span class="topo-outside">WWNFREY</span><span class="topo-membrane">LFIALEG</span></span>
<span class="topo-line"><span class="topo-membrane">PRGVVPSALASL</span><span class="topo-inside">PLSLALKYKSPLLTVHWGEII</span><span class="topo-membrane">MATVVITVLTSVIVETLW</span><span class="topo-unknown">IPILKDKL</span><span class="topo-outside">D</span></span>
<span class="topo-line"><span class="topo-unknown">VG</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>24</td>
      <td>4</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>47</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>54</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>78</td>
      <td>76</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>79</td>
      <td>84</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>87</td>
      <td>85</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>108</td>
      <td>88</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>119</td>
      <td>109</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>134</td>
      <td>120</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>151</td>
      <td>135</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>152</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>179</td>
      <td>170</td>
      <td>179</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>189</td>
      <td>180</td>
      <td>189</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>192</td>
      <td>190</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>217</td>
      <td>193</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>224</td>
      <td>218</td>
      <td>224</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>225</td>
      <td>230</td>
      <td>225</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>250</td>
      <td>231</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>264</td>
      <td>252</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>293</td>
      <td>265</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>313</td>
      <td>294</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>315</td>
      <td>320</td>
      <td>315</td>
      <td>320</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>321</td>
      <td>322</td>
      <td>321</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>346</td>
      <td>323</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>347</td>
      <td>353</td>
      <td>347</td>
      <td>353</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>372</td>
      <td>354</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>373</td>
      <td>393</td>
      <td>373</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>411</td>
      <td>394</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>419</td>
      <td>412</td>
      <td>419</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>420</td>
      <td>420</td>
      <td>420</td>
      <td>420</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4cza">4CZA</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MIELS</span><span class="topo-membrane">LAEALFLILFTGVISMLIS</span><span class="topo-outside">RRTGI</span><span class="topo-membrane">SYVPIFILTGLVIGPLL</span><span class="topo-inside">KLIPRDLA</span><span class="topo-membrane">HEIFDF</span></span>
<span class="topo-line"><span class="topo-membrane">VRVFGLVIILFTEG</span><span class="topo-outside">HNLS</span><span class="topo-unknown">WRLLKK</span><span class="topo-outside">NMPTIV</span><span class="topo-membrane">TLDTIGLILTALIAGFIF</span><span class="topo-inside">KVVFNSSFLLG</span><span class="topo-membrane">F</span></span>
<span class="topo-line"><span class="topo-membrane">LFGAIIGATDPAT</span><span class="topo-outside">LIPLFRQYRVKQDIETVIVTE</span><span class="topo-membrane">SIFNDPLGIVLTLIAI</span><span class="topo-inside">SMLVPGYGGG</span></span>
<span class="topo-line"><span class="topo-inside">IFSTLSEKLGIY</span><span class="topo-membrane">AGGVIYFLYNVSVSISLGIFLG</span><span class="topo-outside">ILGYKFIKRTGIFDFPEIE</span><span class="topo-membrane">AFSLSLA</span></span>
<span class="topo-line"><span class="topo-membrane">FLGFFIGERL</span><span class="topo-inside">D</span><span class="topo-membrane">ASGYLVATVTG</span><span class="topo-outside">IVLGNYKLLKPRENIRILKRLQRAIEKEVHF</span><span class="topo-membrane">NDTLAAL</span></span>
<span class="topo-line"><span class="topo-membrane">ATIFIFVLLGAEM</span><span class="topo-inside">N</span><span class="topo-unknown">LEVIWS</span><span class="topo-inside">NL</span><span class="topo-membrane">GKGLLVALGVMILARPLATLP</span><span class="topo-outside">LLKWWNFREYLFIA</span><span class="topo-membrane">LEG</span></span>
<span class="topo-line"><span class="topo-membrane">PRGVVPSALASL</span><span class="topo-inside">PLSLALKYKSPLLTVHWGEII</span><span class="topo-membrane">MATVVITVLTSVIVETLW</span><span class="topo-outside">IPILKDKLD</span></span>
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
      <td>24</td>
      <td>6</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>54</td>
      <td>47</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>74</td>
      <td>55</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>78</td>
      <td>75</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>79</td>
      <td>84</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>90</td>
      <td>85</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>108</td>
      <td>91</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>119</td>
      <td>109</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>133</td>
      <td>120</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Outside</td>
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
      <td>192</td>
      <td>171</td>
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
      <td>233</td>
      <td>215</td>
      <td>233</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>250</td>
      <td>234</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>262</td>
      <td>252</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>293</td>
      <td>263</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>313</td>
      <td>294</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>315</td>
      <td>320</td>
      <td>315</td>
      <td>320</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>321</td>
      <td>322</td>
      <td>321</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>343</td>
      <td>323</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>372</td>
      <td>358</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>373</td>
      <td>393</td>
      <td>373</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>411</td>
      <td>394</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>420</td>
      <td>412</td>
      <td>420</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4cza">4CZA</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MI</span><span class="topo-membrane">ELSLAEALFLILFTGVISMLIS</span><span class="topo-outside">RRTGI</span><span class="topo-membrane">SYVPIFILTGLVIGPLL</span><span class="topo-inside">KLIPRDL</span><span class="topo-membrane">AHEIFDF</span></span>
<span class="topo-line"><span class="topo-membrane">VRVFGLVIILFTEG</span><span class="topo-outside">HNLS</span><span class="topo-unknown">WRLLKK</span><span class="topo-outside">NMPTIV</span><span class="topo-membrane">TLDTIGLILTALIAGFIF</span><span class="topo-inside">KVVFNSSFLLG</span><span class="topo-membrane">F</span></span>
<span class="topo-line"><span class="topo-membrane">LFGAIIGATDPAT</span><span class="topo-outside">LIPLFRQYRVKQDIETVIVTE</span><span class="topo-membrane">SIFNDPLGIVLTLIAI</span><span class="topo-inside">SMLVPGYGGG</span></span>
<span class="topo-line"><span class="topo-unknown">IFSTLSEKL</span><span class="topo-inside">GIY</span><span class="topo-membrane">AGGVIYFLYNVSVSISLGIFLG</span><span class="topo-outside">ILGYKFIKRTGIFDFPEIE</span><span class="topo-membrane">AFSLSLA</span></span>
<span class="topo-line"><span class="topo-membrane">FLGFFIGERL</span><span class="topo-inside">D</span><span class="topo-membrane">ASGYLVATVTG</span><span class="topo-outside">IVLGNYKLLKPRENIRILKRLQRAIEKEVHFN</span><span class="topo-membrane">DTLAAL</span></span>
<span class="topo-line"><span class="topo-membrane">ATIFIFVLLGAEM</span><span class="topo-inside">N</span><span class="topo-unknown">LEVIWS</span><span class="topo-inside">NL</span><span class="topo-membrane">GKGLLVALGVMILARPLATLP</span><span class="topo-outside">LLKWWNFREYLFIA</span><span class="topo-membrane">LEG</span></span>
<span class="topo-line"><span class="topo-membrane">PRGVVPSALASL</span><span class="topo-inside">PLSLALKYKSPLLTVHWGEII</span><span class="topo-membrane">MATVVITVLTSVIVETLW</span><span class="topo-outside">IPILKDKL</span><span class="topo-unknown">D</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>24</td>
      <td>3</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>47</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>74</td>
      <td>54</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>78</td>
      <td>75</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>79</td>
      <td>84</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>90</td>
      <td>85</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>108</td>
      <td>91</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>119</td>
      <td>109</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>133</td>
      <td>120</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Outside</td>
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
      <td>180</td>
      <td>171</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>189</td>
      <td>181</td>
      <td>189</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>192</td>
      <td>190</td>
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
      <td>233</td>
      <td>215</td>
      <td>233</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>250</td>
      <td>234</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>262</td>
      <td>252</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>294</td>
      <td>263</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>313</td>
      <td>295</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>315</td>
      <td>320</td>
      <td>315</td>
      <td>320</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>321</td>
      <td>322</td>
      <td>321</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>343</td>
      <td>323</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>372</td>
      <td>358</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>373</td>
      <td>393</td>
      <td>373</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>411</td>
      <td>394</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>419</td>
      <td>412</td>
      <td>419</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Architecture of the ion-binding site

The Na+ binding site in PaNhaP is formed by three acidic sidechains (Glu73 from H3, Asp130 from H5 unwound stretch, Asp159 from H6), a water molecule held by Asp130, the hydroxyl group of Ser155, and the main-chain carbonyl of Thr129. The trigonal bipyramidal coordination geometry is similar to that in Na+-translocating F-ATPase c-rings. The ion retains partial hydration via the water molecule. All ion-binding residues are in the first half of the inverted repeat.

### pH-dependent conformational changes

At pH 4 (compared to pH 8), the dimer undergoes significant rearrangements: (1) all six inter-protomer ion pairs break due to protonation; (2) protomers tilt away from the dimer interface; (3) H1 extends by one helical turn; (4) Asp130 shifts 2.7 A into the ion-binding space; (5) Asn158 reorients to potentially regulate ion access. These changes disrupt the Na+ binding site and prevent ion binding at low pH.

### pH-dependent cooperativity and allosteric regulation

PaNhaP shows positive cooperative Na+ transport at pH 6 (Hill coefficient 1.9) but non-cooperative transport at pH 5 (Hill coefficient ~1.1). Cooperativity is mediated by His292 at the dimer interface through a pH-dependent allosteric coupling mechanism. At neutral/basic pH, cooperative increase in Na+ affinity inhibits substrate release, serving as a safety mechanism against excessive Na+ influx. This mirrors the pH-dependent cooperativity observed in human NHE1.

### Dual proton access pathways

Protons (likely as H3O+) can access the binding pocket via two routes: (1) the negatively charged cytoplasmic funnel extending between the 6-helix bundle and the dimer interface, which serves as the Na+ access/egress path; (2) a narrow polar channel defined by bundle helices H5c, H12c, H6, and H13. Using separate pathways for Na+ and H+ currents in opposite directions may be advantageous at high transport rates. The narrow polar channel likely involves the conserved Glu154/Arg337 salt bridge and Asn158.

### Structural model for human NHE1

PaNhaP shares key features with human NHE1, including dimeric architecture, 13 TMHs, CPA1 family conservation of unwound H5/H12 stretches, ion-binding residues (Ser155, Asp130, ND motif), functionally important Arg337/Arg362, and pH-dependent Na+ cooperativity (Hill coefficient ~1.8 at pH 6.8 for NHE1). PaNhaP serves as an excellent structural model for the membrane domain of NHE1, a major drug target for heart and kidney diseases.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/mjnhaP1/">MjNhaP1 Sodium/Proton Antiporter</a> — Closely related CPA1 antiporter from Methanocaldococcus jannaschii; same functional family with conserved rocking-bundle mechanism
- <a href="/xray-mp-wiki/proteins/slc-transporters/nhaa/">Na+/H+ Antiporter NhaA from Escherichia coli</a> — Related E. coli CPA2 antiporter; electrogenic (2H+:1Na+) versus electroneutral PaNhaP; different fold but similar transport principles
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocking-bundle-mechanism/">Rocking-Bundle Mechanism</a> — PaNhaP uses a rocking-bundle alternating-access mechanism with 6-helix bundle tilting ~7 degrees during transport cycle
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/ph-dependent-gating/">pH-Dependent Gating</a> — PaNhaP transport activity is strongly pH-dependent with a bell-shaped profile; pH regulates both ion binding affinity and dimer cooperativity
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
