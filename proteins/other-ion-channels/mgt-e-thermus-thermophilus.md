---
title: "MgtE (Magnesium Transport Channel)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##emboj.2009.288, doi/10.1038##ncomms6374]
verified: false
---

# MgtE (Magnesium Transport Channel)

## Overview

MgtE is a magnesium-selective ion channel from Thermus thermophilus that mediates
Mg2+ uptake across the cytoplasmic membrane. It functions as a homodimer, with
each subunit containing an N-terminal cytosolic domain followed by five
transmembrane helices. The cytosolic domain acts as a Mg2+ sensor that regulates
channel gating in response to intracellular Mg2+ concentration, enabling Mg2+
homeostasis. The N-terminal cytosolic domain comprises an N domain and two
tandem CBS (cystathionine beta-synthase) domains. The closed-state structure
shows the ion-conducting pore occluded on both the periplasmic side (by a
hydrophobic gate at Pro321) and the cytosolic side (by plug helices from the
CBS domains). Seven Mg2+-binding sites in the cytosolic domain cooperatively
stabilize the closed conformation at high intracellular Mg2+ concentrations.
A high-resolution (2.2 A) crystal structure of the MgtE transmembrane domain
revealed that the selectivity filter (M1 site) recognizes fully hydrated Mg2+
ions via carboxylate groups of Asp432, in contrast to dehydrated K+ recognition
by KcsA. Periplasmic M2 and M3 sites bind transition metal cations such as Mn2+
and regulate channel gating.

## Publications

### doi/10.1038##emboj.2009.288

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2zy9">2ZY9</a></td>
      <td>2.94</td>
      <td>Not specified</td>
      <td>Full-length Thermus thermophilus MgtE</td>
      <td>Mg2+ ions (7 binding sites: Mg1-Mg7)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length Thermus thermophilus MgtE with His6 tag in pET vector

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: His6 tag
- **Tag info**: His6 tag

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
      <td>Solubilization and extraction</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM HEPES pH 7.0, 150 mM NaCl + 0.1% (w/v) n-dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Protein expressed and solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> as described in Hattori et al., 2007</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA (Qiagen)</td>
      <td>50 mM HEPES pH 7.0, 150 mM NaCl + 0.25% (w/v) n-nonyl-beta-D-thiomaltoside (NTM)</td>
      <td>Detergent exchanged from <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> to NTM during purification. Wash with 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elute with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>HiLoad 16/60 <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM HEPES pH 7.0, 150 mM NaCl + 0.25% (w/v) NTM</td>
      <td>Final purification step</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified full-length MgtE in NTM at ~10 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>7-9% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000, 0.2 M MgCl2, 0.1 M MES pH 6.5</td>
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
      <td>9% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000, 0.2 M MgCl2, 0.1 M MES pH 6.5, 30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>New crystal form obtained by extensive detergent screening. Co2+-soaked crystals used for anomalous signal to confirm Mg2+-binding sites. Structure determined at 2.94 A resolution, improved from earlier 3.5 A structure.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2zy9">2ZY9</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLGVLPGGPLHMEEKLAVSLQEALQEGDTRALR</span><span class="topo-inside">EVLEEIHPQDLLALW</span></span>
<span class="topo-line"><span class="topo-inside">DELKGEHRYVVLTLLPKAKAAEVLSHLSPEEQAEYLKTLPPWRLREILEELSLDDLADAL</span></span>
<span class="topo-line"><span class="topo-inside">QAVRKEDPAYFQRLKDLLDPRTRAEVEALARYEEDEAGGLMTPEYVAVREGMTVEEVLRF</span></span>
<span class="topo-line"><span class="topo-inside">LRRAAPDAETIYYIYVVDEKGRLKGVLSLRDLIVADPRTRVAEIMNPKVVYVRTDTDQEE</span></span>
<span class="topo-line"><span class="topo-inside">VARLMADYDFTVLPVVDEEGRLVGIVTVDDVLDVLEAEATEDIHKLGAVDVPDLVYSEAG</span></span>
<span class="topo-line"><span class="topo-inside">PVAL</span><span class="topo-membrane">WLARVRWLVILILTGMVTSSILQG</span><span class="topo-outside">F</span><span class="topo-unknown">ESVLEA</span><span class="topo-outside">VTAL</span><span class="topo-membrane">AFYVPVLLGTGGNTGNQSA</span><span class="topo-inside">TL</span></span>
<span class="topo-line"><span class="topo-inside">IIRALATRDLDLRDWRRVF</span><span class="topo-membrane">LKEMGVGLLLGLTLSFLLVGKVYWD</span><span class="topo-outside">GHPLL</span><span class="topo-membrane">LPVVGVSLVLI</span></span>
<span class="topo-line"><span class="topo-membrane">VFFANLVGAML</span><span class="topo-unknown">PFLLRRL</span><span class="topo-inside">GVDPAL</span><span class="topo-membrane">VSNPLVATLSDVTGLLIYLSVA</span><span class="topo-outside">RLLLEA</span><span class="topo-unknown">V</span></span>
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
      <td>-22</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>46</td>
      <td>304</td>
      <td>23</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>328</td>
      <td>282</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>329</td>
      <td>306</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>335</td>
      <td>307</td>
      <td>312</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>336</td>
      <td>339</td>
      <td>313</td>
      <td>316</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>358</td>
      <td>317</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>379</td>
      <td>336</td>
      <td>356</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>404</td>
      <td>357</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>409</td>
      <td>382</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>431</td>
      <td>387</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>438</td>
      <td>409</td>
      <td>415</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>439</td>
      <td>444</td>
      <td>416</td>
      <td>421</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>466</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>472</td>
      <td>444</td>
      <td>449</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>473</td>
      <td>473</td>
      <td>450</td>
      <td>450</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2zy9">2ZY9</a> — Chain B (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLGVLPGGPLHMEEKLAVSLQEALQEGDTR</span><span class="topo-inside">ALREVLEEIHPQDLLALW</span></span>
<span class="topo-line"><span class="topo-inside">DELKGEHRYVVLTLLPKAKAAEVLSHLSPEEQAEYLKTLPPWRLREILEELSLDDLADAL</span></span>
<span class="topo-line"><span class="topo-inside">QAVRKEDPAYFQRLKDLLDPRTRAEVEALARYEEDEAGGLMTPEYVAVREGMTVEEVLRF</span></span>
<span class="topo-line"><span class="topo-inside">LRRAAPDAETIYYIYVVDEKGRLKGVLSLRDLIVADPRTRVAEIMNPKVVYVRTDTDQEE</span></span>
<span class="topo-line"><span class="topo-inside">VARLMADYDFTVLPVVDEEGRLVGIVTVDDVLDVLEAEATEDIHKLGAVDVPDLVYSEAG</span></span>
<span class="topo-line"><span class="topo-inside">PVAL</span><span class="topo-membrane">WLARVRWLVILILTGMVTSSILQG</span><span class="topo-outside">FESVLEAVTAL</span><span class="topo-membrane">AFYVPVLLGTGGNTGNQSA</span><span class="topo-inside">TL</span></span>
<span class="topo-line"><span class="topo-inside">IIRALATRDLDLRDWRRV</span><span class="topo-membrane">FLKEMGVGLLLGLTLSFLLVGKVYWD</span><span class="topo-outside">GHPLLL</span><span class="topo-membrane">PVVGVSLVLI</span></span>
<span class="topo-line"><span class="topo-membrane">VFFANLVGAMLP</span><span class="topo-inside">FLLRRLGVDPAL</span><span class="topo-membrane">VSNPLVATLSDVTGLLIYLSVA</span><span class="topo-outside">RLLLE</span><span class="topo-unknown">AV</span></span>
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
      <td>42</td>
      <td>-22</td>
      <td>19</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>43</td>
      <td>304</td>
      <td>20</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>328</td>
      <td>282</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>339</td>
      <td>306</td>
      <td>316</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>358</td>
      <td>317</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>378</td>
      <td>336</td>
      <td>355</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>404</td>
      <td>356</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>410</td>
      <td>382</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>432</td>
      <td>388</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>433</td>
      <td>444</td>
      <td>410</td>
      <td>421</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>466</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>471</td>
      <td>444</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>473</td>
      <td>449</td>
      <td>450</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##ncomms6374

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u9l">4U9L</a></td>
      <td>2.2</td>
      <td>P 2(1) 2(1) 2(1)</td>
      <td>MgtE transmembrane domain (MgtE-TMD) from Thermus thermophilus</td>
      <td>Mg2+, Mn2+, Ca2+ ions at M1 site; Mn2+ at M2, M2', M3 sites</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length Thermus thermophilus MgtE with His6 tag in pET vector

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified MgtE-TMD after TEV cleavage, in 0.1% DDM</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in detail</td>
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
      <td>MgtE-TMD crystals obtained after TEV protease cleavage of the loop connecting cytosolic and TM domains. Three data sets collected: Mg2+-bound (2.2 A), Mn2+-bound (2.2 A native, 2.84 A anomalous), and Ca2+-bound (3.2 A).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u9l">4U9L</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">LVYSEAGPVALW</span><span class="topo-membrane">LARVRWLVILILTGMVTSSILQG</span><span class="topo-outside">F</span><span class="topo-unknown">ESVLEA</span><span class="topo-outside">VTAL</span><span class="topo-membrane">AFYVPVLLGTGGNT</span></span>
<span class="topo-line"><span class="topo-membrane">GNQSATL</span><span class="topo-inside">IIRALATRDLDLRDW</span><span class="topo-membrane">RRVFLKEMGVGLLLGLTLSFLLVGKVYWD</span><span class="topo-outside">GHPLL</span><span class="topo-membrane">LPVV</span></span>
<span class="topo-line"><span class="topo-membrane">GVSLVLIVFFANLVGAMLPFLL</span><span class="topo-inside">RRLGVDP</span><span class="topo-membrane">ALVSNPLVATLSDVTGLLIYLSVA</span><span class="topo-outside">RLLLEA</span></span>
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
      <td>271</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>35</td>
      <td>283</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>36</td>
      <td>306</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>42</td>
      <td>307</td>
      <td>312</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>43</td>
      <td>46</td>
      <td>313</td>
      <td>316</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>67</td>
      <td>317</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>82</td>
      <td>338</td>
      <td>352</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>111</td>
      <td>353</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>116</td>
      <td>382</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>142</td>
      <td>387</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>149</td>
      <td>413</td>
      <td>419</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>173</td>
      <td>420</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>179</td>
      <td>444</td>
      <td>449</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u9l">4U9L</a> — Chain B (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">LVYSEAG</span><span class="topo-membrane">PVALWLARVRWLVILILTGMVTSSILQG</span><span class="topo-outside">F</span><span class="topo-unknown">ESVLEA</span><span class="topo-outside">VTALA</span><span class="topo-membrane">FYVPVLLGTGGNT</span></span>
<span class="topo-line"><span class="topo-membrane">GNQSATLI</span><span class="topo-inside">IRALATRDLDLRDW</span><span class="topo-membrane">RRVFLKEMGVGLLLGLTLSFLLVGKVYWD</span><span class="topo-outside">GHPLLL</span><span class="topo-membrane">PVV</span></span>
<span class="topo-line"><span class="topo-membrane">GVSLVLIVFFANLVGAMLPFLL</span><span class="topo-inside">RRLGVDPAL</span><span class="topo-membrane">VSNPLVATLSDVTGLLIYLSVA</span><span class="topo-outside">RLLLE</span><span class="topo-unknown">A</span></span>
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
      <td>271</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>35</td>
      <td>278</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>36</td>
      <td>306</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>42</td>
      <td>307</td>
      <td>312</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>43</td>
      <td>47</td>
      <td>313</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>68</td>
      <td>318</td>
      <td>338</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>82</td>
      <td>339</td>
      <td>352</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>111</td>
      <td>353</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>117</td>
      <td>382</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>142</td>
      <td>388</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>151</td>
      <td>413</td>
      <td>421</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>173</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>178</td>
      <td>444</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### MgtE is a highly Mg2+-selective channel gated by intracellular Mg2+ concentration

Patch-clamp electrophysiology of MgtE expressed in giant E. coli spheroplasts demonstrated single-channel currents with a conductance of 96 pS for Mg2+. The channel is highly selective for Mg2+ over Ca2+, Ni2+, and Mn2+. Increasing intracellular Mg2+ from 0.2 to 10 mM progressively decreased channel open probability, directly demonstrating Mg2+-dependent gating. Co(III) hexamine, a hydrated Mg2+ analog, completely blocked Mg2+ influx.

### Seven cooperative Mg2+-binding sites in the cytosolic domain control gating

The higher-resolution 2.94 A structure identified seven Mg2+-binding sites (Mg1-Mg7) in the cytosolic domain. Mg5 at the CBS domain dimer interface and Mg2/Mg3 on the plug helices are particularly important. Mutations at these sites (D226N/D250A for Mg5, E258Q for Mg2, D259N for Mg3) largely abolished Mg2+-dependent suppression of channel opening. The Mg7 site at the N domain-CBS interface contributes a weaker regulatory function. All sites function cooperatively to stabilize the closed state at high Mg2+.

### Dual occlusion of the MgtE pore in the closed state

The updated structure revealed that the MgtE pore is occluded on both sides: a hydrophobic gate at Pro321 (kinked TM2 helix with F318, P321, L324) on the periplasmic side, and plug helices from the CBS domains on the cytosolic side. This dual-gate architecture ensures complete channel closure at high intracellular Mg2+ concentrations. For channel opening, both the TM2 helices must move apart at Pro321 and the plug helices must disengage.

### Cooperativity model for Mg2+ sensing and channel gating

A three-state model is proposed: open state (low Mg2+), transiently closed state (intermediate Mg2+), and stable closed state (high Mg2+). Mg2+ binding to any temporary binding site stabilizes the closed conformation, facilitating further Mg2+ binding to other sites. All seven binding sites cooperatively regulate the structural transition, providing a sensitive homeostatic mechanism for maintaining intracellular Mg2+ concentration.

### Ion selectivity via hydrated Mg2+ recognition

The 2.2 A crystal structure of the MgtE-TMD revealed that the M1 site (selectivity filter) recognizes Mg2+ in a fully hydrated state. Asp432 carboxylate groups form hydrogen bonds with water molecules in the first hydration shell of Mg2+, while the ion itself remains hydrated with 6 water molecules in octahedral coordination (average Mg2+-O distance 2.11 A). This is fundamentally different from K+ channels like KcsA, which recognize dehydrated K+. The geometry of the hydration shell is critical: Mg2+ and Mn2+ (which form stable octahedral hydration) bind tightly, while Ca2+ (with flexible 6-8 coordination) binds more weakly. Na+ and K+ (monovalent, weaker electrostatic interaction with Asp432) also cannot compete effectively. This mechanism explains the high Mg2+ selectivity with minimal dehydration energy cost.

### Periplasmic gating sites for transition metal selectivity

Three periplasmic metal-binding sites (M2, M2', M3) were identified in the Mn2+-bound structure. The M2 site involves Gln304, Glu307, and His383 from adjacent protomers. The M3 site involves Glu307 and Glu311. Mn2+ binding at these sites decreases channel open probability (shown by patch-clamp), acting as a gating mechanism to prevent toxic transition metal uptake. The M2M3A mutant (disrupting these sites) loses Mn2+-dependent inhibition but retains Mg2+ selectivity at the M1 site, confirming the distinct roles of the selectivity filter and periplasmic gating sites.


## Cross-References

- <a href="/xray-mp-wiki/proteins/corA/">CorA Mg2+ Channel</a> — Functional homolog also involved in bacterial Mg2+ transport
- <a href="/xray-mp-wiki/concepts/magnesium-homeostasis/">Magnesium Homeostasis</a> — MgtE directly participates in cellular Mg2+ homeostasis
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used for protein extraction
- <a href="/xray-mp-wiki/reagents/detergents/ntm/">NTM (n-Nonyl-beta-D-Thiomaltoside)</a> — Detergent used for crystallization
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion Crystallization</a> — Crystallization method used for MgtE
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
