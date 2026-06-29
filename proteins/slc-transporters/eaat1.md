---
title: "Human Excitatory Amino Acid Transporter 1 (EAAT1)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography, transporter]
sources: [doi/10.1038##nature22064, doi/10.15252##embj.2021108341]
verified: false
---

# Human Excitatory Amino Acid Transporter 1 (EAAT1)

## Overview

Human excitatory amino acid transporter 1 (EAAT1, SLC1A3) is a member of the
solute carrier 1 (SLC1) family of transporters that takes up the
neurotransmitter glutamate from the synaptic cleft into astrocytes and
neurons. EAAT1 uses energy stored in sodium, proton and potassium gradients
to maintain steep glutamate gradients. In addition to coupled transport,
EAAT1 conducts chloride ions through a channel-like process thermodynamically
uncoupled from transport. Crystal structures of a thermostabilized
EAAT1 construct (EAAT1_cryst) were determined in outward-facing conformations
with and without the allosteric inhibitor UCPH101, revealing the architecture
of the human transporter including the scaffold domain (ScaD) and transport
domain (TranD), and a mechanism of allosteric inhibition where UCPH101 locks
the transporter in outward-facing states. A co-structure with both UCPH101
and TBOA-TFB revealed how competitive and allosteric inhibitors can bind
simultaneously. [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) and X-ray structures of the archaeal homologue [Gltph](/xray-mp-wiki/proteins/slc-transporters/glt-ph/)
in a chloride ion-conducting state (CICS) revealed the molecular basis for
the uncoupled Cl- conductance, gated by two hydrophobic regions at the
domain interface. X-ray structures of EAAT1_CRYST in multiple ion-bound
states (Na+/L-asp, Rb+/Ba2+, E386Q mutant) and a [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of
wild-type EAAT1 at 3.99 A, combined with [HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/) and mutagenesis, revealed
the ion-coupling mechanism — how Na+, K+, and H+ gradients drive
substrate transport through an elevator-type alternating access mechanism.
The conserved E386 residue in EAAT1_CRYST (E406 in full-length numbering)
plays a critical role in the proton coupling mechanism, and its mutation
to glutamine alters the ion-bound conformation.

## Publications

### doi/10.1038##nature22064

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5llm">5LLM</a></td>
      <td>3.25</td>
      <td>P6_3</td>
      <td>EAAT1_cryst (thermostabilized, N155T/N204T, ASCT2 TM3-4c swap) with UCPH101 and L-Asp bound</td>
      <td>UCPH101, <a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">L Aspartate</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5llm">5LLM</a></td>
      <td>3.10</td>
      <td>P6_3</td>
      <td>EAAT1_cryst-II (M231I/F235I mutant) with UCPH101 bound</td>
      <td>UCPH101, <a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">L Aspartate</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5llm">5LLM</a></td>
      <td>3.32</td>
      <td>P6_3</td>
      <td>EAAT1_cryst-II (M231I/F235I mutant) UCPH101-unbound</td>
      <td><a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">L Aspartate</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5llm">5LLM</a></td>
      <td>3.71</td>
      <td>P6_3</td>
      <td>EAAT1_cryst with UCPH101 and TBOA-TFB bound</td>
      <td>UCPH101, TBOA-TFB</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293F cells
- **Construct**: EAAT1 with N-terminal Strep-tag II, eGFP, PreScission cleavage site; thermostabilizing consensus mutations; N155T/N204T; ASCT2 TM3-4c swap
- **Notes**: Transient transfection with PEI; cells grown in Excell293 medium; collected 48 h post-transfection

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
      <td>Solubilization</td>
      <td>Resuspension and douce homogenization</td>
      <td>—</td>
      <td>50 mM HEPES/Tris-base pH 7.4, 200 mM NaCl, 1 mM L-Asp, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">Pmsf</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 2% DDS (dodecanoyl <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a>) + 0.4% CHS</td>
      <td>1 h incubation at 4 C; ultracentrifugation at 247,000g for 45 min</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Strep-Tactin affinity</td>
      <td>Strep-Tactin resin</td>
      <td>50 mM HEPES/Tris-base pH 7.4, 200 mM NaCl, 1 mM L-Asp, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 3x CMC DDS + 0.01% CHS</td>
      <td>Fractions analyzed by FSEC; elution with <a href="/xray-mp-wiki/reagents/ligands/desthiobiotin/">Desthiobiotin</a></td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td>SEC polishing</td>
      <td>Superose 6 10/300</td>
      <td>50 mM HEPES/Tris-base pH 7.4, 200 mM NaCl, 1 mM L-Asp, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.0632% DDS + 0.01264% CHS</td>
      <td>Final purification step before crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified EAAT1_cryst in 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.4, 200 mM NaCl, 1 mM L-Asp, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a>, 0.0632% DDS, 0.01264% CHS, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in raw paper</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in presence of 0.5 mM UCPH101; space group P6_3</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5llm">5LLM</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLLAKKKVQNI</span><span class="topo-outside">TKEDVKSFLRRNALL</span><span class="topo-membrane">LLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLGFLLR</span><span class="topo-inside">PYPLSPRE</span><span class="topo-membrane">VKYFAFPGELLMRMLKMLILPLIV</span><span class="topo-outside">SSLITGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIILVLII</span><span class="topo-inside">HP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-inside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-inside">TT</span><span class="topo-unknown">YEERTITGTRVKV</span><span class="topo-inside">PVGQ</span><span class="topo-membrane">EVEGMNILGLVVFSMVF</span><span class="topo-outside">GFALGKM</span></span>
<span class="topo-line"><span class="topo-outside">GEQGQLLVDFFNSLNEATMKLVAII</span><span class="topo-membrane">MWYAPLGILFLIAGKIV</span><span class="topo-inside">E</span><span class="topo-unknown">MEDLEVL</span><span class="topo-inside">GGQLGMY</span><span class="topo-membrane">MVT</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLI</span><span class="topo-outside">YFLITRKNPFVFIAGI</span><span class="topo-unknown">LQALITALGTSSSSATLPIT</span><span class="topo-outside">FKCLEENN</span></span>
<span class="topo-line"><span class="topo-outside">GVDKRITRFV</span><span class="topo-membrane">LPVGATINMDGTALYEAVA</span><span class="topo-inside">AIFIAQ</span><span class="topo-unknown">VNNYELDFG</span><span class="topo-inside">QI</span><span class="topo-unknown">ITISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAGLVT</span><span class="topo-inside">MVIVLTAVGLPTDDITLIIAV</span><span class="topo-membrane">DWLLDRFRTMVNVLGDALG</span><span class="topo-outside">AGIVEHLSRK</span></span>
<span class="topo-line"><span class="topo-outside">ELEKQDA</span><span class="topo-unknown">ELGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>36</td>
      <td>1</td>
      <td>36</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>37</td>
      <td>51</td>
      <td>37</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>69</td>
      <td>52</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>77</td>
      <td>70</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>101</td>
      <td>78</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>120</td>
      <td>102</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>145</td>
      <td>121</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>147</td>
      <td>146</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>199</td>
      <td>198</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>212</td>
      <td>200</td>
      <td>212</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>213</td>
      <td>216</td>
      <td>213</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>233</td>
      <td>217</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>265</td>
      <td>234</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>282</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>283</td>
      <td>283</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>290</td>
      <td>284</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>297</td>
      <td>291</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>316</td>
      <td>298</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>332</td>
      <td>317</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>353</td>
      <td>370</td>
      <td>353</td>
      <td>370</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>389</td>
      <td>371</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>390</td>
      <td>395</td>
      <td>390</td>
      <td>395</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>404</td>
      <td>396</td>
      <td>404</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>405</td>
      <td>406</td>
      <td>405</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>430</td>
      <td>407</td>
      <td>430</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>431</td>
      <td>451</td>
      <td>431</td>
      <td>451</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>470</td>
      <td>452</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>487</td>
      <td>471</td>
      <td>487</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>488</td>
      <td>522</td>
      <td>488</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5llm">5LLM</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLLAKKKVQNI</span><span class="topo-outside">TKEDVKSFLRRNALL</span><span class="topo-membrane">LLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLGFLLR</span><span class="topo-inside">PYPLSPRE</span><span class="topo-membrane">VKYFAFPGELLMRMLKMLILPLIV</span><span class="topo-outside">SSLITGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIILVLII</span><span class="topo-inside">HP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-inside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-inside">TT</span><span class="topo-unknown">YEERTITGTRVKV</span><span class="topo-inside">PVGQ</span><span class="topo-membrane">EVEGMNILGLVVFSMVF</span><span class="topo-outside">GFALGKM</span></span>
<span class="topo-line"><span class="topo-outside">GEQGQLLVDFFNSLNEATMKLVAII</span><span class="topo-membrane">MWYAPLGILFLIAGKIV</span><span class="topo-inside">E</span><span class="topo-unknown">MEDLEVL</span><span class="topo-inside">GGQLGMY</span><span class="topo-membrane">MVT</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLI</span><span class="topo-outside">YFLITRKNPFVFIAGI</span><span class="topo-unknown">LQALITALGTSSSSATLPIT</span><span class="topo-outside">FKCLEENN</span></span>
<span class="topo-line"><span class="topo-outside">GVDKRITRFV</span><span class="topo-membrane">LPVGATINMDGTALYEAVA</span><span class="topo-inside">AIFIAQ</span><span class="topo-unknown">VNNYELDFG</span><span class="topo-inside">QI</span><span class="topo-unknown">ITISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAGLVT</span><span class="topo-inside">MVIVLTAVGLPTDDITLIIAV</span><span class="topo-membrane">DWLLDRFRTMVNVLGDALG</span><span class="topo-outside">AGIVEHLSRK</span></span>
<span class="topo-line"><span class="topo-outside">ELEKQDA</span><span class="topo-unknown">ELGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>36</td>
      <td>1</td>
      <td>36</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>37</td>
      <td>51</td>
      <td>37</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>69</td>
      <td>52</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>77</td>
      <td>70</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>101</td>
      <td>78</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>120</td>
      <td>102</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>145</td>
      <td>121</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>147</td>
      <td>146</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>199</td>
      <td>198</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>212</td>
      <td>200</td>
      <td>212</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>213</td>
      <td>216</td>
      <td>213</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>233</td>
      <td>217</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>265</td>
      <td>234</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>282</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>283</td>
      <td>283</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>290</td>
      <td>284</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>297</td>
      <td>291</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>316</td>
      <td>298</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>332</td>
      <td>317</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>353</td>
      <td>370</td>
      <td>353</td>
      <td>370</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>389</td>
      <td>371</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>390</td>
      <td>395</td>
      <td>390</td>
      <td>395</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>404</td>
      <td>396</td>
      <td>404</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>405</td>
      <td>406</td>
      <td>405</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>430</td>
      <td>407</td>
      <td>430</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>431</td>
      <td>451</td>
      <td>431</td>
      <td>451</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>470</td>
      <td>452</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>487</td>
      <td>471</td>
      <td>487</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>488</td>
      <td>522</td>
      <td>488</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5llm">5LLM</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLLAKKKVQNI</span><span class="topo-outside">TKEDVKSFLRRNALL</span><span class="topo-membrane">LLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLGFLLR</span><span class="topo-inside">PYPLSPRE</span><span class="topo-membrane">VKYFAFPGELLMRMLKMLILPLIV</span><span class="topo-outside">SSLITGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIILVLII</span><span class="topo-inside">HP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-inside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-inside">TT</span><span class="topo-unknown">YEERTITGTRVKV</span><span class="topo-inside">PVGQ</span><span class="topo-membrane">EVEGMNILGLVVFSMVF</span><span class="topo-outside">GFALGKM</span></span>
<span class="topo-line"><span class="topo-outside">GEQGQLLVDFFNSLNEATMKLVAII</span><span class="topo-membrane">MWYAPLGILFLIAGKIV</span><span class="topo-inside">E</span><span class="topo-unknown">MEDLEVL</span><span class="topo-inside">GGQLGMY</span><span class="topo-membrane">MVT</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLI</span><span class="topo-outside">YFLITRKNPFVFIAGI</span><span class="topo-unknown">LQALITALGTSSSSATLPIT</span><span class="topo-outside">FKCLEENN</span></span>
<span class="topo-line"><span class="topo-outside">GVDKRITRFV</span><span class="topo-membrane">LPVGATINMDGTALYEAVA</span><span class="topo-inside">AIFIAQ</span><span class="topo-unknown">VNNYELDFG</span><span class="topo-inside">QI</span><span class="topo-unknown">ITISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAGLVT</span><span class="topo-inside">MVIVLTAVGLPTDDITLIIAV</span><span class="topo-membrane">DWLLDRFRTMVNVLGDALG</span><span class="topo-outside">AGIVEHLSRK</span></span>
<span class="topo-line"><span class="topo-outside">ELEKQDA</span><span class="topo-unknown">ELGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>36</td>
      <td>1</td>
      <td>36</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>37</td>
      <td>51</td>
      <td>37</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>69</td>
      <td>52</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>77</td>
      <td>70</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>101</td>
      <td>78</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>120</td>
      <td>102</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>145</td>
      <td>121</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>147</td>
      <td>146</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>199</td>
      <td>198</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>212</td>
      <td>200</td>
      <td>212</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>213</td>
      <td>216</td>
      <td>213</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>233</td>
      <td>217</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>265</td>
      <td>234</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>282</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>283</td>
      <td>283</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>290</td>
      <td>284</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>297</td>
      <td>291</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>316</td>
      <td>298</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>332</td>
      <td>317</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>353</td>
      <td>370</td>
      <td>353</td>
      <td>370</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>389</td>
      <td>371</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>390</td>
      <td>395</td>
      <td>390</td>
      <td>395</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>404</td>
      <td>396</td>
      <td>404</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>405</td>
      <td>406</td>
      <td>405</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>430</td>
      <td>407</td>
      <td>430</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>431</td>
      <td>451</td>
      <td>431</td>
      <td>451</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>470</td>
      <td>452</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>487</td>
      <td>471</td>
      <td>487</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>488</td>
      <td>522</td>
      <td>488</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5llm">5LLM</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLLAKKKVQNI</span><span class="topo-outside">TKEDVKSFLRRNALL</span><span class="topo-membrane">LLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLGFLLR</span><span class="topo-inside">PYPLSPRE</span><span class="topo-membrane">VKYFAFPGELLMRMLKMLILPLIV</span><span class="topo-outside">SSLITGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIILVLII</span><span class="topo-inside">HP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-inside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-inside">TT</span><span class="topo-unknown">YEERTITGTRVKV</span><span class="topo-inside">PVGQ</span><span class="topo-membrane">EVEGMNILGLVVFSMVF</span><span class="topo-outside">GFALGKM</span></span>
<span class="topo-line"><span class="topo-outside">GEQGQLLVDFFNSLNEATMKLVAII</span><span class="topo-membrane">MWYAPLGILFLIAGKIV</span><span class="topo-inside">E</span><span class="topo-unknown">MEDLEVL</span><span class="topo-inside">GGQLGMY</span><span class="topo-membrane">MVT</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLI</span><span class="topo-outside">YFLITRKNPFVFIAGI</span><span class="topo-unknown">LQALITALGTSSSSATLPIT</span><span class="topo-outside">FKCLEENN</span></span>
<span class="topo-line"><span class="topo-outside">GVDKRITRFV</span><span class="topo-membrane">LPVGATINMDGTALYEAVA</span><span class="topo-inside">AIFIAQ</span><span class="topo-unknown">VNNYELDFG</span><span class="topo-inside">QI</span><span class="topo-unknown">ITISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAGLVT</span><span class="topo-inside">MVIVLTAVGLPTDDITLIIAV</span><span class="topo-membrane">DWLLDRFRTMVNVLGDALG</span><span class="topo-outside">AGIVEHLSRK</span></span>
<span class="topo-line"><span class="topo-outside">ELEKQDA</span><span class="topo-unknown">ELGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>36</td>
      <td>1</td>
      <td>36</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>37</td>
      <td>51</td>
      <td>37</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>69</td>
      <td>52</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>77</td>
      <td>70</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>101</td>
      <td>78</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>120</td>
      <td>102</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>145</td>
      <td>121</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>147</td>
      <td>146</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>199</td>
      <td>198</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>212</td>
      <td>200</td>
      <td>212</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>213</td>
      <td>216</td>
      <td>213</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>233</td>
      <td>217</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>265</td>
      <td>234</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>282</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>283</td>
      <td>283</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>290</td>
      <td>284</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>297</td>
      <td>291</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>316</td>
      <td>298</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>332</td>
      <td>317</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>353</td>
      <td>370</td>
      <td>353</td>
      <td>370</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>389</td>
      <td>371</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>390</td>
      <td>395</td>
      <td>390</td>
      <td>395</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>404</td>
      <td>396</td>
      <td>404</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>405</td>
      <td>406</td>
      <td>405</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>430</td>
      <td>407</td>
      <td>430</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>431</td>
      <td>451</td>
      <td>431</td>
      <td>451</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>470</td>
      <td>452</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>487</td>
      <td>471</td>
      <td>487</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>488</td>
      <td>522</td>
      <td>488</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.15252##embj.2021108341

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a></td>
      <td>3.25</td>
      <td>P6_3</td>
      <td>EAAT1_CRYST Na+/L-asp and UCPH101 bound</td>
      <td>Na+, <a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">L Aspartate</a>, UCPH101</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a></td>
      <td>3.60</td>
      <td>P6_3</td>
      <td>EAAT1_CRYST-E386Q Na+/L-asp and UCPH101 bound</td>
      <td>Na+, <a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">L Aspartate</a>, UCPH101</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a></td>
      <td>3.92</td>
      <td>P6_3</td>
      <td>EAAT1_CRYST Rb+/Ba2+ and UCPH101 bound</td>
      <td>Rb+, Ba2+, UCPH101</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a></td>
      <td>3.91</td>
      <td>P6_3</td>
      <td>EAAT1_CRYST-II Rb+/Ba2+ and UCPH101 bound</td>
      <td>Rb+, Ba2+, UCPH101</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a></td>
      <td>3.70</td>
      <td>P6_3</td>
      <td>EAAT1_CRYST-II Ba2+ and UCPH101 bound</td>
      <td>Ba2+, UCPH101</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a></td>
      <td>3.99</td>
      <td></td>
      <td>Wild-type human EAAT1 (full-length)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293F cells
- **Construct**: EAAT1 with N-terminal Strep-tag II, eGFP, PreScission cleavage site; thermostabilizing consensus mutations; N155T/N204T; ASCT2 TM3-4c swap
- **Notes**: Transient transfection with PEI; cells grown in Excell293 medium; collected 48 h post-transfection

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7awm">7AWM</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTKSNGEEPKMGGRMERFQQGVSKRTLL</span><span class="topo-inside">AKKKVQNITKEDVKSFLRRN</span><span class="topo-membrane">ALLLLTVLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">GVVLG</span><span class="topo-outside">FLLRPYPLSPREVKYF</span><span class="topo-membrane">AFPGELLMRMLKMLILPLIVSSLI</span><span class="topo-inside">TGLASLDAKASGRLG</span></span>
<span class="topo-line"><span class="topo-membrane">MRAVVYYMSTTIIAVVLGIIL</span><span class="topo-outside">VLIIHP</span><span class="topo-unknown">GAASAAITASVGAAGSAENAPSK</span><span class="topo-outside">EVLDC</span><span class="topo-unknown">FLDLA</span></span>
<span class="topo-line"><span class="topo-unknown">RNIFPSNLVSAAFRSYS</span><span class="topo-outside">T</span><span class="topo-unknown">TYEERTITGTRVKVPVG</span><span class="topo-outside">QE</span><span class="topo-membrane">VEGMNILGLVVFSMVFG</span><span class="topo-inside">FALGKM</span></span>
<span class="topo-line"><span class="topo-inside">GEQGQLLVDFFNSLNEA</span><span class="topo-membrane">TMKLVAIIMWYAPLGILFLIAG</span><span class="topo-outside">KIV</span><span class="topo-unknown">EMEDLEVL</span><span class="topo-outside">GGQLGMYMV</span><span class="topo-membrane">T</span></span>
<span class="topo-line"><span class="topo-membrane">VIVGLVIHGLIVLPLIYFL</span><span class="topo-inside">ITRKNP</span><span class="topo-membrane">FVFIAGILQALITALGTS</span><span class="topo-outside">S</span><span class="topo-membrane">SSATLPITFKCL</span><span class="topo-inside">EENN</span></span>
<span class="topo-line"><span class="topo-inside">GVDKRIT</span><span class="topo-membrane">RFVLPVGATINMDGTALYEAV</span><span class="topo-outside">AAIFIAQVNNYELDFGQII</span><span class="topo-unknown">TISITATAASIGA</span></span>
<span class="topo-line"><span class="topo-unknown">AGIPQAG</span><span class="topo-outside">LVTMVIVLTAVGLPTDDITLIIAVDW</span><span class="topo-membrane">LLDRFRTMVNVLGDALGAGIV</span><span class="topo-inside">EHLSRK</span></span>
<span class="topo-line"><span class="topo-inside">ELEKQDAE</span><span class="topo-unknown">LGNSVIEENEMKKPYQLIAQDNETEKPIDSETKM</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>66</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>120</td>
      <td>106</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>141</td>
      <td>121</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>147</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>170</td>
      <td>148</td>
      <td>170</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>171</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>215</td>
      <td>199</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>216</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>257</td>
      <td>235</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>282</td>
      <td>280</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>290</td>
      <td>283</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>325</td>
      <td>320</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>356</td>
      <td>345</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>357</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>388</td>
      <td>368</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>407</td>
      <td>389</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>428</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>454</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>488</td>
      <td>475</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>522</td>
      <td>489</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Allosteric inhibition locks EAAT1 in outward-facing states

UCPH101 binds in a hydrophobic pocket at the TranD-ScaD interface between TM3, TM7 and TM4c, wedging the two domains together. The compound makes ring-stacking interactions with Phe369 (TM7a) and hydrophobic contacts with residues in TM3, TM7a and TM4c. [HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/) analysis shows that UCPH101 binding decreases deuterium uptake in the TranD-ScaD interface, consistent with stabilization of the outward-facing state at the expense of inward-facing state(s).

### TM4b-c loop is a eukaryotic-specific insertion

The TM4b-c loop, an insertion in eukaryotic SLC1 transporters, protrudes into the central vestibule of the EAAT1 trimer forming the center of the propeller. It contains a conserved N-glycosylation site (Asn204) and makes extensive inter- and intra-subunit contacts. This architectural feature is absent in the prokaryotic homologue [Gltph](/xray-mp-wiki/proteins/slc-transporters/glt-ph/).

### TM1a forms membrane-interacting amphipathic helix

TM1 bends at the cytoplasmic side with TM1a lying nearly parallel to the
membrane plane, forming the tips of the propeller blades. Its amphipathic
nature and associated non-protein electron density between TM1a and HP1a
suggest interaction with the inner leaflet, likely representing bound
lipid or detergent molecules.

### Cl- channel gated by two hydrophobic regions in EAAT1

[Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) and X-ray structures of the [Gltph](/xray-mp-wiki/proteins/slc-transporters/glt-ph/) homologue revealed a chloride
ion-conducting state (CICS) with an aqueous cavity at the domain interface.
Electrophysiological studies in Xenopus laevis oocytes confirmed that the
same crosslinking strategy (XL2: L244C/G439C in EAAT1) traps EAAT1 in an
open-channel conformation with enhanced Cl- conductance. Mutation of
hydrophobic residues equivalent to those gating the [Gltph](/xray-mp-wiki/proteins/slc-transporters/glt-ph/) channel confirmed
a conserved mechanism: F50A, T54A, L88A, M89A, M286A, and L269A mutations
shifted the reversal potential to more hyperpolarized potentials (increased
Cl- conductance), while A289F essentially eliminated Cl- contribution to
net conductance (reversal potential shift to +76 ± 2 mV). The P290R
mutation associated with episodic ataxia type 6 results in increased Cl-
conductance and reduced glutamate transport, linking channel dysfunction
to neurological pathology.

### Ion-coupling mechanism of EAAT1 revealed by multi-ion bound structures and HDX-MS

X-ray structures of EAAT1_CRYST in multiple ion-bound states (Na+/L-asp,
Rb+/Ba2+, and the E386Q mutant), combined with a [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of
wild-type EAAT1 at 3.99 A and [HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/) analysis, revealed the molecular basis
of ion coupling. The E386 residue (E406 in full-length EAAT1 numbering) is
critical for proton coupling. The E386Q mutant structure shows the E386
sidechain adopts a similar position to wild-type, consistent with H-bonding
between protonated E386 and residues in HP2b, supporting a model where
Glu386 undergoes protonation during the transport cycle. The Rb+/Ba2+-bound
structures probe the K+ counter-transport pathway. [HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/) experiments with
K+-bound, Na+/L-asp-bound, and control conditions identified peptides
exhibiting reversible K+-induced HDX changes, mapping regions that undergo
conformational changes during the transport cycle. The HDX peptide coverage
map covers 55% of the EAAT1_CRYST sequence with 77 unique peptides.

### TM1a deletions impair glutamate transport

N-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) of EAAT1 (labeled with the N-terminal residue) show
that TM1a deletions progressively impair [L Glutamate](/xray-mp-wiki/reagents/substrates/l-glutamate/) uptake in HEK293 cells.
Radioactive [L Glutamate](/xray-mp-wiki/reagents/substrates/l-glutamate/) uptake decreases steeply in incremental N-term
truncated constructs, while protein expression (measured by GFP counts)
remains relatively constant compared to EAAT1_WT. This confirms the
functional importance of the TM1a amphipathic helix in the transport
mechanism.

### Tryptophan fluorescence as a probe of substrate binding

Intrinsic tryptophan fluorescence changes upon L-asp/Na+ binding serve as
a readout of conformational transitions. W287 and W473 mutations greatly
decreased or abolished, respectively, the Trp-intrinsic fluorescence change
associated with L-asp/Na+ binding, indicating these residues report on
substrate-induced conformational changes.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/glt-ph/">GltPh (Glutamate Transporter Homologue from Pyrococcus horikoshii)</a> — Prokaryotic homologue with same fold; structural basis for elevator mechanism
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/">Elevator Mechanism</a> — EAAT1 transports substrates via elevator-like rigid-body movements of the transport domain
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — SLC1 transporters operate by alternating access of the substrate binding site
- <a href="/xray-mp-wiki/reagents/ligands/ucph101/">UCPH101</a> — Selective allosteric inhibitor of EAAT1 bound in the TranD-ScaD interface
- <a href="/xray-mp-wiki/reagents/ligands/tboa/">TBOA (DL-threo-beta-benzyloxyaspartic acid)</a> — Competitive inhibitor bound in co-structure with UCPH101
- <a href="/xray-mp-wiki/reagents/detergents/dds/">DDS (Dodecanoyl Sucrose)</a> — Detergent used for solubilization and crystallization
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/anion-channel-gating/">Anion Channel Gating</a> — EAAT1 Cl- conductance is gated by two hydrophobic regions at the domain interface
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT (Dithiothreitol)</a> — Reducing agent used to test disulfide crosslinking in EAAT1 cysteine mutants
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/glutamate-transporter-family/">Glutamate Transporter Family (SLC1/EAAT)</a> — EAAT1 is a human SLC1 family member; ion-coupling mechanism is shared across the family
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/substrate-protonation-coupling/">Substrate-Protonation Coupling</a> — E386 protonation is coupled to substrate binding in EAAT1 transport mechanism
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Cryo-EM structure of wild-type EAAT1 determined at 3.99 A
