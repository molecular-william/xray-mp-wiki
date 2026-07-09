---
title: "D4 Dopamine Receptor (DRD4)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aan5468]
verified: regex
uniprot_id: P21917
---

# D4 Dopamine Receptor (DRD4)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P21917">UniProt: P21917</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The human D4 [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor (DRD4) is a class A G protein-coupled receptor
(GPCR) belonging to the D2-like [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor subfamily (D2, D3, D4). DRD4
is implicated in attention deficit disorder, metastatic progression, and penile
erection, making DRD4-selective drugs therapeutically promising. The crystal
structures of DRD4 in its inactive state bound to the antipsychotic drug
[Nemonapride](/xray-mp-wiki/reagents/ligands/nemonapride/) were determined at resolutions up to 1.95 Å using a [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion
strategy. The structures reveal a full network of water molecules and ions,
including the first direct structural evidence for a sodium ion in its allosteric
binding site in a [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor. The extended binding pocket (EBP) defined
by non-conserved residues V87^2.57, L90^2.60, F91^2.61, and L111^3.28
provides an atomic-resolution model for DRD4 ligand selectivity.


## Publications

### doi/10.1126##science.aan5468

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5wiu">5WIU</a></td>
      <td>1.95</td>
      <td>—</td>
      <td>DRD4-BRIL fusion (residues 228-336 of ICL3 replaced with thermostabilized apocytochrome b562RIL), bound to <a href="/xray-mp-wiki/reagents/ligands/nemonapride/">Nemonapride</a>, 200 mM Na+ added</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/nemonapride/">Nemonapride</a>, Na+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5wiv">5WIV</a></td>
      <td>2.15</td>
      <td>—</td>
      <td>DRD4-BRIL fusion (residues 228-336 of ICL3 replaced with <a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a>), bound to <a href="/xray-mp-wiki/reagents/ligands/nemonapride/">Nemonapride</a>, no added Na+</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/nemonapride/">Nemonapride</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells via baculovirus
- **Construct**: DRD4-BRIL — residues 228-336 of ICL3 replaced with thermostabilized apocytochrome b562RIL ([Bril](/xray-mp-wiki/reagents/protein-tags/bril/))
- **Notes**: DRD4-BRIL has binding affinity for 3H-N-methylspiperone similar to native DRD4. [Nemonapride](/xray-mp-wiki/reagents/ligands/nemonapride/) added during purification to form complex.

**Purification:**

- **Expression system**: Sf9 insect cells, baculovirus
- **Expression construct**: DRD4-BRIL (ICL3 replaced with BRIL)
- **Tag info**: BRIL fusion (no affinity tag mentioned for DRD4 portion)

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
      <td>Baculovirus infection</td>
      <td>—</td>
      <td></td>
      <td>Sf9 cells infected with recombinant baculovirus encoding DRD4-<a href="/xray-mp-wiki/reagents/protein-tags/bril/">bril</a> construct</td>
    </tr>
    <tr>
      <td>Complex formation</td>
      <td>Ligand addition</td>
      <td>—</td>
      <td></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/nemonapride/">Nemonapride</a> added during purification to stabilize the receptor-ligand complex</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity-chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Purification details in supplementary materials; DRD4/nemonapride complex purified to homogeneity</td>
    </tr>
  </tbody>
</table>
**Final sample**: DRD4/nemonapride complex in crystallization buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in presence and absence of 200 mM added sodium. DRD4/nemonapride complex crystals diffracted to 1.95 Å resolution. Data collected at GM/CA@APS, Advanced Photon Source.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wiu">5WIU</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGTTMGNRSTADADGLLAGRGPAAGASAGASAGLAGQ</span><span class="topo-outside">GAA</span><span class="topo-membrane">ALVGGVLLIGAVLAGNSLVCVSV</span><span class="topo-inside">ATERALQTPT</span><span class="topo-membrane">NSFIVSLAAADLLLALLVLPLFV</span><span class="topo-outside">YSEVQGGAWLLSPRLCDA</span><span class="topo-membrane">LMAMDV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLCTASIFNLCAISVDRFV</span><span class="topo-inside">AVAVPLRYNRQGGSRR</span><span class="topo-membrane">QLLLIGATWLLSAAVAAPVL</span><span class="topo-outside">CGLND</span><span class="topo-unknown">VRGRD</span><span class="topo-outside">PAVCRLEDRDYVVY</span><span class="topo-membrane">SSVCSFFLPCPLMLLLYWATFR</span><span class="topo-inside">GLQRWEVARRADLEDNWET</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">LNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSP</span><span class="topo-unknown">DS</span><span class="topo-inside">PEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLAKITGRERKAM</span><span class="topo-membrane">RVLPVVVGAFLL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420  </span>
<span class="topo-line"><span class="topo-membrane">CWTPFFV</span><span class="topo-outside">VHITQALCPACSVPPRLVSA</span><span class="topo-membrane">VTWLGYVNSALNPVIYTVFN</span><span class="topo-unknown">AEFRNVFR</span><span class="topo-inside">KA</span><span class="topo-unknown">LRACC</span></span>
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
      <td>38</td>
      <td>40</td>
      <td>34</td>
      <td>36</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>63</td>
      <td>37</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>73</td>
      <td>60</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>96</td>
      <td>70</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>114</td>
      <td>93</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>139</td>
      <td>111</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>155</td>
      <td>136</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>175</td>
      <td>152</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>180</td>
      <td>172</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>199</td>
      <td>182</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>221</td>
      <td>196</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>284</td>
      <td>218</td>
      <td>1053</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>348</td>
      <td>1056</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>349</td>
      <td>367</td>
      <td>394</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>387</td>
      <td>413</td>
      <td>432</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>407</td>
      <td>433</td>
      <td>452</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>415</td>
      <td>453</td>
      <td>460</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>416</td>
      <td>417</td>
      <td>461</td>
      <td>462</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wiv">5WIV</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGTTMGNRSTADADGLLAGRGPAAGASAGASAGLA</span><span class="topo-inside">GQGAA</span><span class="topo-membrane">ALVGGVLLIGAVLAGNSLVCVS</span><span class="topo-outside">VATERALQTPTNS</span><span class="topo-membrane">FIVSLAAADLLLALLVLPLFV</span><span class="topo-inside">YSEVQGGAWLLSPRLCDA</span><span class="topo-membrane">LMAMDV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MLCTASIFNLCAISV</span><span class="topo-outside">DRFVAVAVPLRYNRQGGSRRQ</span><span class="topo-membrane">LLLIGATWLLSAAVAAPVLC</span><span class="topo-inside">GLND</span><span class="topo-unknown">VRGRD</span><span class="topo-inside">PAVCRLEDRD</span><span class="topo-membrane">YVVYSSVCSFFLPCPLMLLLY</span><span class="topo-outside">WATFRGLQRWEVARRADLEDNWET</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">LNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLAKITGRERKAMRVL</span><span class="topo-membrane">PVVVGAFLL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420  </span>
<span class="topo-line"><span class="topo-membrane">CWTPFFVVHITQAL</span><span class="topo-inside">CPACSVPPRL</span><span class="topo-membrane">VSAVTWLGYVNSALNPVIYTV</span><span class="topo-outside">FN</span><span class="topo-unknown">AEFRNVFR</span><span class="topo-outside">KALR</span><span class="topo-unknown">ACC</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>62</td>
      <td>37</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>75</td>
      <td>59</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>96</td>
      <td>72</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>114</td>
      <td>93</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>135</td>
      <td>111</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>156</td>
      <td>132</td>
      <td>152</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>176</td>
      <td>153</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>180</td>
      <td>173</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>195</td>
      <td>182</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>216</td>
      <td>192</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>351</td>
      <td>213</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>374</td>
      <td>397</td>
      <td>419</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>375</td>
      <td>384</td>
      <td>420</td>
      <td>429</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>405</td>
      <td>430</td>
      <td>450</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>407</td>
      <td>451</td>
      <td>452</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>415</td>
      <td>453</td>
      <td>460</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>416</td>
      <td>419</td>
      <td>461</td>
      <td>464</td>
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

### First dopamine receptor structures at atomic resolution

The D4 [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor structures at 1.95 Å and 2.15 Å resolution are the highest-resolution [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor structures reported. The unusually high resolution enabled visualization of a full network of water molecules and ions, providing unprecedented detail of [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor architecture.

### Sodium ion allosteric modulation

The structures provide the first direct structural evidence for a sodium ion in its allosteric binding site in a [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor. Sodium forms a salt bridge with D80^2.50 and polar interactions with S122^3.39 and two water molecules. DRD4 has lower sodium affinity than δ-OR, μ-OR or A2AAR. Lowering [Na+] potentiates DRD4 constitutive activity in a nemonapride-sensitive fashion. MD simulations show the sodium-free pocket fills with water and does not collapse.

### Mechanism of constitutive signaling control

In DRD4, the absence of a hydrogen bond between position 7.35 and 6.55 (V430^7.35 cannot hydrogen bond with H414^6.55) leads to closer proximity of TM V and TM VI, explaining the more inactive DRD4/nemonapride structure compared to DRD3. A V430^7.35Y mutation in DRD4 recapitulates the DRD3 inter-helical hydrogen bond and increases constitutive activity. The reverse mutation in DRD3 (Y365^7.35V) diminishes constitutive activity. Thus, the 7.35-6.55 hydrogen bond potentiates DRD3 constitutive activity while its absence in DRD4 suppresses it.

### Extended binding pocket (EBP) for DRD4 selectivity

The high-resolution structure revealed an extended binding pocket (EBP) bordered by non-conserved residues V87^2.57, L90^2.60, F91^2.61, and L111^3.28. In DRD3, the corresponding residues are V86^2.61 and F106^3.28, which create steric clashes with DRD4-selective ligands. A F^2.61V/L^3.28F double substitution in DRD4 attenuates affinities of DRD4-selective compounds, while the reverse double mutant in [DRD2](/xray-mp-wiki/proteins/gpcr/drd2/) (V^2.61F/F^3.28L) increases affinity for DRD4-selective ligands, providing an atomic resolution model of DRD4 ligand selectivity.

### Structure-based discovery of DRD4-selective agonists

Using the 1.95 Å DRD4 structure, a virtual screen of over 600,000 cationic lead-like molecules from ZINC was performed. Hit compound 9 was optimized through 75 docked analogs to yield 9-6 and 9-11, which were DRD4-selective partial agonists. Further optimization produced 9-6-23 and 9-6-24 with Ki of 30 [NM](/xray-mp-wiki/reagents/detergents/nm/) and 3 [NM](/xray-mp-wiki/reagents/detergents/nm/) at DRD4, respectively, with >3,300-fold selectivity over [DRD2](/xray-mp-wiki/proteins/gpcr/drd2/) and DRD3. 9-6-24 (UCSF924) is a DRD4 partial agonist with 7.4-fold bias toward arrestin over Gαi/o signaling and no substantial agonist activity against 320 non-olfactory GPCRs.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/human-dopamine-d3-receptor/">Human Dopamine D3 Receptor (D3R)</a> — DRD3 is the closest structural homolog; comparison of EBP and constitutive activity mechanisms
- <a href="/xray-mp-wiki/concepts/signaling-receptors/sodium-allosteric-modulation/">Sodium Ion Allosteric Modulation in GPCRs</a> — First direct structural evidence for sodium allosteric site in a dopamine receptor
- <a href="/xray-mp-wiki/concepts/signaling-receptors/biased-agonism/">Biased Agonism in G Protein-Coupled Receptors</a> — Compound 9-6-24 shows 7.4-fold arrestin bias over Gαi/o signaling
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/drd2-extended-binding-pocket/">DRD2 Extended Binding Pocket (DRD2-EBP)</a> — Closely related concept — DRD4 EBP is the DRD4-specific analog driving subtype selectivity
- <a href="/xray-mp-wiki/reagents/ligands/dopamine/">Dopamine</a> — Referenced in context related to Dopamine
- <a href="/xray-mp-wiki/reagents/ligands/nemonapride/">Nemonapride</a> — Referenced in context related to Nemonapride
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a> — Referenced in context related to Bril
- <a href="/xray-mp-wiki/proteins/gpcr/drd2/">DRD2</a> — Referenced in context related to DRD2
- <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> — Referenced in context related to NM
