---
title: "Human Glycine Transporter 1 (GlyT1)"
created: 2021-03-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-021-03274-z]
verified: false
---

# Human Glycine Transporter 1 (GlyT1)

## Overview

Human [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) transporter 1 (GlyT1, encoded by the SLC6A9 gene) is a member of the [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/transport-mechanisms/nss-family/) (SLC6) that regulates glycine-mediated neuronal excitation and inhibition through sodium- and chloride-dependent reuptake of [Glycine](/xray-mp-wiki/reagents/buffers/glycine/). GlyT1 is located on presynaptic neurons and astrocytes surrounding both inhibitory glycinergic and excitatory glutamatergic synapses, and is the main regulator of extracellular [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) levels in the brain. Inhibition of GlyT1 prolongs neurotransmitter signaling and has been a key strategy for treating schizophrenia and cognitive impairments. The structure of GlyT1 in complex with a benzoylisoindoline inhibitor (Cmpd1) and a synthetic single-domain antibody (sybody Sb_GlyT1#7) was determined at 3.4 A resolution using serial synchrotron crystallography (Shahsavar et al., 2021, PDB 6ZBV). The inhibitor locks GlyT1 in an inward-open conformation and binds at the intracellular gate of the release pathway, overlapping with the glycine-release site. A second structure of GlyT1 with an N-terminal lichenase fusion (GlyT1-Lic) was determined at 3.9 A resolution (PDB 6ZPL).

## Publications

### doi/10.1038##s41586-021-03274-z

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zbv">6ZBV</a></td>
      <td>3.4 A</td>
      <td>P2_1</td>
      <td>Human GlyT1 minimal construct with N- and C-terminal deletions (Delta1-90, Delta685-706), EL2 deletion (Delta240-256), point mutations L153A, S297A, I368A, C633A; C-terminal eGFP and decahistidine tag</td>
      <td>Cmpd1 (benzoylisoindoline inhibitor)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zpl">6ZPL</a></td>
      <td>3.9 A</td>
      <td>P2_1</td>
      <td>GlyT1-Lic fusion with N-terminal lichenase (residues 9-281, PDB 2CIT), C-terminal eGFP and decahistidine tag</td>
      <td>Cmpd1 (benzoylisoindoline inhibitor)</td>
    </tr>
  </tbody>
</table>

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
      <td>Expression</td>
      <td>Transient transfection (HEK293) or baculovirus infection (Sf9)</td>
      <td>—</td>
      <td>FreeStyle 293 expression medium (HEK293) or Sf900-III medium (Sf9)</td>
      <td>HEK293 cells transfected with 25 kDa linear polyethylenimine (LPEI) at a GlyT1 DNA:LPEI ratio of 1:2. Cells collected 60 h post-transfection at ~70% viability. Sf9 cells infected at 2-3x10^6 cells/ml, collected 72 h post-infection at ~80% viability.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 150 mM NaCl + 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> (lauryl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol) or 1% <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a> (decyl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol) with 0.1% cholesteryl hemisuccinate (<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>)</td>
      <td>Solubilization performed in the continuous presence of Cmpd1 to stabilize the inhibited conformation</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> or Ni-NTA resin</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 150 mM NaCl, 0.001% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a></td>
      <td>Purified in the presence of 100 uM Cmpd1</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) with serial synchrotron crystallography</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature or 4 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Microcrystals of GlyT1 in complex with sybody Sb_GlyT1#7 and Cmpd1 were grown in LCP. Oscillation patterns collected from 409 mounted loops containing microcrystals by serial synchrotron crystallography at P14 beamline (PETRA III, DESY). Merged dataset yielded 3.4 A resolution. <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using <a href="/xray-mp-wiki/proteins/slc-transporters/mhsT/">MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans</a> (PDB 4US3) and human <a href="/xray-mp-wiki/proteins/slc-transporters/ssert/">SERT</a> (PDB 6DZZ).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zbv">6ZBV</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ATKRDQNLK</span><span class="topo-outside">RGNWGNQIEFV</span><span class="topo-membrane">LTSVGYAVGLGNVWRFPYLC</span><span class="topo-inside">YRNGG</span><span class="topo-membrane">GAFMFPYFIMLIFCGIPAFF</span><span class="topo-outside">MELSFGQFASQGCLGVWRISPMF</span><span class="topo-membrane">KGVGYGMMVVSTYIGIYYNVVICIAFY</span><span class="topo-inside">YFFSS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MTHVLPWAYCNNPWNTHDCAGVLD</span><span class="topo-unknown">ASN</span><span class="topo-inside">LTHSLQRTSPSEEYWRLYVLKLSDDIGNFGEVRLPLL</span><span class="topo-membrane">GCLGVAWLVVFLCLIRG</span><span class="topo-unknown">VKSSGK</span><span class="topo-outside">V</span><span class="topo-membrane">VYFTATFPYVVLTILFV</span><span class="topo-inside">RGVTLEGAFDGIMYY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">LTPQWDKI</span><span class="topo-membrane">LEAKVWGDAASQAFYSLGCAWGGLI</span><span class="topo-outside">TMASYNKFHNNCYRDS</span><span class="topo-membrane">VIISITNCATSVYAGFV</span><span class="topo-inside">IFSILGFMANHLGVDVSRVADHGPG</span><span class="topo-unknown">LAFVAYPEAL</span><span class="topo-inside">TLLPISPL</span><span class="topo-membrane">WSLLFFFMLIL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGLGTQFCLLETLVTAI</span><span class="topo-outside">VDEVGNEWILQK</span><span class="topo-membrane">KTYVTLGVAVAGFLLGIPL</span><span class="topo-inside">TSQAGIYW</span><span class="topo-membrane">LLLMDNYAASFSLVVISCIMCV</span><span class="topo-outside">AIMYIYGHRNYFQDIQMMLGFPPPLFFQI</span><span class="topo-membrane">CWRFVSPAIIFFI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       </span>
<span class="topo-line"><span class="topo-membrane">LVFTVIQY</span><span class="topo-inside">QPITYNHYQYPGWAVA</span><span class="topo-membrane">IGFLMALSSVLCIPLYAMF</span><span class="topo-outside">RLARTDGDTLL</span><span class="topo-unknown">QRLKNAT</span><span class="topo-outside">KPSRDWGPALLEHRTG</span><span class="topo-unknown">RYAPTIAPSPEDGFEVQPLH</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>10</td>
      <td>20</td>
      <td>100</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>40</td>
      <td>111</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>41</td>
      <td>45</td>
      <td>131</td>
      <td>135</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>65</td>
      <td>136</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>88</td>
      <td>156</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>115</td>
      <td>179</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>144</td>
      <td>206</td>
      <td>234</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>184</td>
      <td>238</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>201</td>
      <td>292</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>208</td>
      <td>315</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>225</td>
      <td>316</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>248</td>
      <td>333</td>
      <td>355</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>273</td>
      <td>356</td>
      <td>380</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>289</td>
      <td>381</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>306</td>
      <td>397</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>331</td>
      <td>414</td>
      <td>438</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>341</td>
      <td>439</td>
      <td>448</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>342</td>
      <td>349</td>
      <td>449</td>
      <td>456</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>377</td>
      <td>457</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>389</td>
      <td>485</td>
      <td>496</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>408</td>
      <td>497</td>
      <td>515</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>416</td>
      <td>516</td>
      <td>523</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>438</td>
      <td>524</td>
      <td>545</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>467</td>
      <td>546</td>
      <td>574</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>488</td>
      <td>575</td>
      <td>595</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>489</td>
      <td>504</td>
      <td>596</td>
      <td>611</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>505</td>
      <td>523</td>
      <td>612</td>
      <td>630</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>524</td>
      <td>534</td>
      <td>631</td>
      <td>641</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>535</td>
      <td>541</td>
      <td>642</td>
      <td>648</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>542</td>
      <td>557</td>
      <td>649</td>
      <td>664</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zpl">6ZPL</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">TKRDQNLKRGNWGNQ</span><span class="topo-inside">I</span><span class="topo-membrane">EFVLTSVGYAVGLGNVWRFP</span><span class="topo-outside">YLCYRNGGGAF</span><span class="topo-membrane">MFPYFIMLIFCGIPAFFMEL</span><span class="topo-inside">SFGQFASQGCL</span><span class="topo-unknown">GVWRIS</span><span class="topo-inside">PMFKG</span><span class="topo-membrane">VGYGMMVVSTYIGIYYNVVICIAFY</span><span class="topo-outside">YFFSSM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">THVLPWAYCNNPWNTHDCAGVLD</span><span class="topo-unknown">ASNLT</span><span class="topo-outside">HSLQRTSPSEEYWRLYVLKLSDDIGNFGEVRL</span><span class="topo-membrane">PLLGCLGVAWLVVFLCLIRG</span><span class="topo-unknown">VKSSGK</span><span class="topo-inside">V</span><span class="topo-membrane">VYFTATFPYVVLTI</span><span class="topo-outside">LFVRGVTLEGAFDGIMYYL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPQWDKILEA</span><span class="topo-membrane">KVWGDAASQAFYSLGCAWGGLI</span><span class="topo-inside">TMASYNKFHNNCY</span><span class="topo-membrane">RDSVIISITNCATSVYAG</span><span class="topo-outside">FVIFSILGFMANHLGVDVSRVADHGPGLAFVA</span><span class="topo-unknown">YPEALT</span><span class="topo-outside">LLPISPLWSL</span><span class="topo-membrane">LFFFMLILL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">GLGTQFCLLETLV</span><span class="topo-inside">TAIVDEVGNEWILQKKTY</span><span class="topo-membrane">VTLGVAVAGFLLGIPLTS</span><span class="topo-outside">QAGIYW</span><span class="topo-membrane">LLLMDNYAASFSLVVISCIMCV</span><span class="topo-inside">AIMYIYG</span><span class="topo-unknown">HRNYFQDIQMML</span><span class="topo-inside">GFPPP</span><span class="topo-membrane">LFFQICWRFVSPAIIFFIL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570      </span>
<span class="topo-line"><span class="topo-membrane">VFTVIQY</span><span class="topo-outside">QPITYNHYQYPGW</span><span class="topo-membrane">AVAIGFLMALSSVLCIPLY</span><span class="topo-inside">AMFRLARTDGDTLLQRLKNATKPSRDWGPALLEHRTG</span><span class="topo-unknown">RYAPTIAPSPEDGFEVQPLH</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
      <td>16</td>
      <td>16</td>
      <td>107</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>36</td>
      <td>108</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>47</td>
      <td>128</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>67</td>
      <td>139</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>78</td>
      <td>159</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>170</td>
      <td>175</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>89</td>
      <td>176</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>114</td>
      <td>181</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>143</td>
      <td>206</td>
      <td>234</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>180</td>
      <td>257</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>200</td>
      <td>289</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>207</td>
      <td>315</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>221</td>
      <td>316</td>
      <td>329</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>250</td>
      <td>330</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>272</td>
      <td>359</td>
      <td>380</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>285</td>
      <td>381</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>303</td>
      <td>394</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>335</td>
      <td>412</td>
      <td>443</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>341</td>
      <td>444</td>
      <td>449</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>342</td>
      <td>351</td>
      <td>450</td>
      <td>459</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>373</td>
      <td>460</td>
      <td>481</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>391</td>
      <td>482</td>
      <td>499</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>409</td>
      <td>500</td>
      <td>517</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>415</td>
      <td>518</td>
      <td>523</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>437</td>
      <td>524</td>
      <td>545</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>438</td>
      <td>444</td>
      <td>546</td>
      <td>552</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>456</td>
      <td>553</td>
      <td>564</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>457</td>
      <td>461</td>
      <td>565</td>
      <td>569</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>462</td>
      <td>487</td>
      <td>570</td>
      <td>595</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>500</td>
      <td>596</td>
      <td>608</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>501</td>
      <td>519</td>
      <td>609</td>
      <td>627</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>520</td>
      <td>556</td>
      <td>628</td>
      <td>664</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zpl">6ZPL</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">TKRDQNLKRGNWG</span><span class="topo-inside">NQI</span><span class="topo-membrane">EFVLTSVGYAVGLGNVWRFPYLC</span><span class="topo-outside">YRNGGGA</span><span class="topo-membrane">FMFPYFIMLIFCGIPAFF</span><span class="topo-inside">MELSFGQFASQGCLGVWRISPMFKG</span><span class="topo-membrane">VGYGMMVVSTYIGIYYNVVICIAFY</span><span class="topo-outside">YFFSSM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">THVLPWAYCNNPWNTHDCAGVLD</span><span class="topo-unknown">ASNLT</span><span class="topo-outside">HSLQRTSPSEEYWRLYVLKLSDDIGNFGEVRLPL</span><span class="topo-membrane">LGCLGVAWLVVFLCLIRG</span><span class="topo-unknown">VKSSGK</span><span class="topo-inside">V</span><span class="topo-membrane">VYFTATFPYVVLTI</span><span class="topo-outside">LFVRGVTLEGAFDGIMYYL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPQWDKI</span><span class="topo-membrane">LEAKVWGDAASQAFYSLGCAWGGL</span><span class="topo-inside">ITMASYNKFHNNCYRD</span><span class="topo-membrane">SVIISITNCATSVYAGF</span><span class="topo-outside">VIFSILGFMANHLGVDVSRVADHGPG</span><span class="topo-unknown">LAFVAYPEALT</span><span class="topo-outside">LLPISPLWSL</span><span class="topo-membrane">LFFFMLILL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">GLGTQFCLLETLV</span><span class="topo-inside">TAIVDEVGNEWILQKKT</span><span class="topo-membrane">YVTLGVAVAGFLLGIPLT</span><span class="topo-outside">SQAGIYW</span><span class="topo-membrane">LLLMDNYAASFSLVVISCIMCV</span><span class="topo-inside">AIMYIYGHRNYFQDIQMMLGFPPPLFFQI</span><span class="topo-membrane">CWRFVSPAIIFFIL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570      </span>
<span class="topo-line"><span class="topo-membrane">VFTVIQY</span><span class="topo-outside">QPITYNHYQYPGW</span><span class="topo-membrane">AVAIGFLMALSSVLCIPL</span><span class="topo-inside">YAMFRLARTDGDTLLQRLKNATKP</span><span class="topo-unknown">SRDWGPALLEHRTGRYAPTIAPSPEDGFEVQPLH</span></span>
<details class="topo-details"><summary>Topology coordinates (28 regions)</summary>
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
      <td>14</td>
      <td>16</td>
      <td>105</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>39</td>
      <td>108</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>46</td>
      <td>131</td>
      <td>137</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>64</td>
      <td>138</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>89</td>
      <td>156</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>114</td>
      <td>181</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>143</td>
      <td>206</td>
      <td>234</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>182</td>
      <td>257</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>291</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>207</td>
      <td>315</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>221</td>
      <td>316</td>
      <td>329</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>247</td>
      <td>330</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>271</td>
      <td>356</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>287</td>
      <td>380</td>
      <td>395</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>304</td>
      <td>396</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>305</td>
      <td>330</td>
      <td>413</td>
      <td>438</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>341</td>
      <td>439</td>
      <td>449</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>342</td>
      <td>351</td>
      <td>450</td>
      <td>459</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>373</td>
      <td>460</td>
      <td>481</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>390</td>
      <td>482</td>
      <td>498</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>408</td>
      <td>499</td>
      <td>516</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>415</td>
      <td>517</td>
      <td>523</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>437</td>
      <td>524</td>
      <td>545</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>438</td>
      <td>466</td>
      <td>546</td>
      <td>574</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>467</td>
      <td>487</td>
      <td>575</td>
      <td>595</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>500</td>
      <td>596</td>
      <td>608</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>501</td>
      <td>518</td>
      <td>609</td>
      <td>626</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>519</td>
      <td>542</td>
      <td>627</td>
      <td>650</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zpl">6ZPL</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">LKIGAWVGTQPSESAIKSFQELQGRKLDIVHQFINWSTD</span><span class="topo-unknown">FSWVRPYADAVYNN</span><span class="topo-inside">GSILMITWEPWEYNTVDIKNGKADAYITRMAQDMKAYGKEIWLRPLHAANGDWYPWAIGYSSRVNTN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ETYIAAFRHIVDIFRANGATNVKWVFNVNCDNVGNGTSYLGHYPGDNYVDYTSIDGYNWGTTQSWGSQWQSFDQVFSRAYQALASINKPIIIAEFASAEIGGNKARWITEAYNSIRTSYN</span></span>
<span class="topo-ruler">       250       260       270   </span>
<span class="topo-line"><span class="topo-inside">KVIAAVWFHENKETDWRINSSPEALAAYREAIG</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>39</td>
      <td>9</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>53</td>
      <td>48</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>273</td>
      <td>62</td>
      <td>281</td>
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

### Unique inhibition mechanism among NSS transporters

Cmpd1 binds at a unique site among NSS-inhibitor complexes, located at the intracellular gate of the release pathway and overlapping with the glycine-release site. The inhibitor is 5.6 A further from the transporter center compared to [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/), ibogaine, and [Cocaine](/xray-mp-wiki/reagents/ligands/cocaine/) bound to [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/) and DAT. Cmpd1 locks GlyT1 in an inward-open conformation, shifting the conformational equilibrium and preventing the reuptake cycle.

### Inhibitor binding mode

The benzoylisoindoline scaffold of Cmpd1 forms a pi-stacking interaction with Tyr116 (TM1), while the phenyl ring engages in an edge-to-face stacking with Trp376 (TM6). The inhibitor is further stabilized by hydrogen bonds: backbone amines of Gly121 and Leu120 with sulfonyl oxygens, Asn386 (TM6) with the tetrahydropyran oxygen, and Thr472 (TM8) with the carbonyl oxygen. The binding mode provides a template for rational design of new GlyT1 inhibitors.

### Binding pocket plasticity and selectivity

Cmpd1 is >1000-fold selective for GlyT1 over GlyT2. Key differences: Gly373 in GlyT1 corresponds to Ser497 in GlyT2 (steric clash with the inhibitor), and Met382/Ile399 in GlyT1 correspond to Leu/Val in GlyT2 (diminished van der Waals interactions). [Molecular Docking](/xray-mp-wiki/methods/structure-determination/molecular-docking/) of bitopertin places it in the same pocket, with the benzoylpiperazine scaffold matching the benzoylisoindoline scaffold of Cmpd1. The R3 (tetrahydropyran) pocket is solvent-exposed and can accommodate diverse groups.

### Sybody stabilization

The synthetic single-domain antibody sybody Sb_GlyT1#7 binds GlyT1 with 9 nM affinity and stabilizes the inward-open inhibited conformation. The sybody increases thermal stability by 10 C and enhances apparent affinity for the radioligand [3H]Org24598 by almost twofold. The sybody also plays a central role in crystal lattice contacts, essential for successful serial crystallography data collection.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/d-dat/">dDAT (Drosophila Dopamine Transporter)</a> — Related NSS family transporter used as search model for outward-open conformation
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-coupling/">GPCR-G Protein Coupling</a> — GlyT1 regulates glycine levels at NMDA receptor synapses, relevant to glutamatergic signaling
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG (Lauryl Maltose Neopentyl Glycol)</a> — Primary detergent for solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hemisuccinate (CHS)</a> — Used as stabilizing additive during solubilization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Crystallization method used for GlyT1 structure determination
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> — Used for GlyT1-Lic expression in Sf9 insect cells
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — IMAC purification using Talon/Ni-NTA resin
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/nss-family/">Neurotransmitter/Sodium Symporter (NSS) Family</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-docking/">Molecular Docking</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
