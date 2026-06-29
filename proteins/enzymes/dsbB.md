---
title: "DsbB (Disulfide Bond Formation Protein B)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##emboj.2009.21, doi/10.1126##sciadv.abe3717]
verified: false
---

# DsbB (Disulfide Bond Formation Protein B)

## Overview

DsbB is an integral membrane protein from Escherichia coli that functions as the
central oxidase in the bacterial disulfide bond formation pathway. Together with
the periplasmic protein [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/), DsbB catalyzes the de novo generation of disulfide
bonds in substrate proteins. DsbB spans the cytoplasmic membrane with four
transmembrane helices and contains two periplasmic loops (P1 and P2) that harbor
essential cysteine residues (Cys41-Cys44 in P1 and Cys104-Cys130 in P2). The
enzyme uses bound [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) (UQ) as an electron acceptor to generate disulfide
bonds and transfer them to [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/). DsbB undergoes elaborate conformational
transitions during catalysis, driven by the sequential relocation of its active-site
cysteines, which is regulated by a membrane-associated amphiphilic "horizontal
helix" in the P2 loop.

## Publications

### doi/10.1038##emboj.2009.21

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2zuq">2ZUQ</a></td>
      <td>3.4</td>
      <td>C2</td>
      <td>DsbB(Cys41Ser) mutant in complex with Fab antibody fragment</td>
      <td><a href="/xray-mp-wiki/reagents/cofactors/ubiquinone/">Ubiquinone</a> (UQ)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2hi7">2HI7</a></td>
      <td>3.7</td>
      <td>P4(2)2(1)2</td>
      <td>DsbB(Cys130Ser) in disulfide-linked complex with DsbA(Cys33Ala)</td>
      <td><a href="/xray-mp-wiki/reagents/cofactors/ubiquinone/">Ubiquinone</a> (UQ)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length DsbB with His6-myc tag; Cys41Ser mutant and Cys130Ser mutant variants

**Purification:**

- **Expression system**: E. coli SS141 (dsbB::kan5)
- **Expression construct**: His6-myc tag

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
      <td>Complex formation</td>
      <td>Size-exclusion chromatography</td>
      <td>--</td>
      <td>-- + --</td>
      <td>DsbB-Fab complex of 1:1 stoichiometry prepared by size-exclusion chromatography</td>
    </tr>
    <tr>
      <td>Crystal growth</td>
      <td>Sitting-drop vapor diffusion</td>
      <td>--</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/mops/">Mops</a> pH 7.0 + --</td>
      <td>Crystallized in 15% PEG3350, 0.1 M magnesium formate, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/mops/">Mops</a> (pH 7.0)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DsbB(Cys41Ser)-Fab complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>15% PEG3350, 0.1 M magnesium formate, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/mops/">Mops</a> (pH 7.0)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>10 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>27% PEG3350, 0.1 M magnesium formate, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/mops/">Mops</a> pH 7.0, 0.1% <a href="/xray-mp-wiki/reagents/detergents/dhpc/">DHPC</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Co-crystallization with monoclonal Fab antibody fragment was essential for obtaining diffracting crystals. Wild-type DsbB was conformationally heterogeneous; the Cys41Ser mutant provided homogeneous initial-state conformation.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2zuq">2ZUQ</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MLRFLNQAS</span><span class="topo-inside">QGR</span><span class="topo-membrane">GAWLLMAFTALALELT</span><span class="topo-outside">ALWFQHVMLLKPSVLCIYER</span><span class="topo-membrane">VALFGVLGAALI</span></span>
<span class="topo-line"><span class="topo-membrane">GAIA</span><span class="topo-inside">PKTPL</span><span class="topo-membrane">RYVAMVIWLYSAFRGVQ</span><span class="topo-outside">LTYEHTMLQLYPSPFATCDFMV</span><span class="topo-unknown">RFPEW</span><span class="topo-outside">LPLDKWV</span></span>
<span class="topo-line"><span class="topo-outside">PQVFVASGDCAERQWDFLGLEMPQW</span><span class="topo-membrane">LLGIFIAYLIVAVLVVI</span><span class="topo-unknown">SQPFKAKKRDLFGR</span></span>
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
      <td>9</td>
      <td>1</td>
      <td>9</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>12</td>
      <td>10</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>28</td>
      <td>13</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>29</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>64</td>
      <td>49</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>69</td>
      <td>65</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>86</td>
      <td>70</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>108</td>
      <td>87</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>113</td>
      <td>109</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>114</td>
      <td>145</td>
      <td>114</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>162</td>
      <td>146</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>176</td>
      <td>163</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2hi7">2HI7</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">AQYEDGKQYTTLEKPVAGAPQVLEFFSFFCPHAYQFEEVLHISDNVKKKLPEGVKMTKYH</span></span>
<span class="topo-line"><span class="topo-inside">VNFMGGDLGKDLTQAWAVAMALGVEDKVTVPLFEGVQKTQTIRSASDIRDVFINAGIKGE</span></span>
<span class="topo-line"><span class="topo-inside">EYDAAWNSFVVKSLVAQQEKAAADVQLRGVPAMFVNGKYQLNPQGMDTSNMDVFVQQYAD</span></span>
<span class="topo-line"><span class="topo-inside">TVKYLSEK</span><span class="topo-unknown">K</span></span>
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
      <td>188</td>
      <td>1</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>189</td>
      <td>189</td>
      <td>189</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2hi7">2HI7</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MLRFLNQASQGRG</span><span class="topo-outside">A</span><span class="topo-membrane">WLLMAFTALALELTALW</span><span class="topo-inside">FQHVMLLKPCVLCIYE</span><span class="topo-membrane">RVALFGVLGAALI</span></span>
<span class="topo-line"><span class="topo-membrane">GAIAP</span><span class="topo-outside">KTPL</span><span class="topo-membrane">RYVAMVIWLYSAFRGV</span><span class="topo-inside">QLTYEHTMLQLYPSPFATCDFMVRFPEWLPLDKWV</span></span>
<span class="topo-line"><span class="topo-inside">PQVFVA</span><span class="topo-unknown">SGDSAERQWDFLGLE</span><span class="topo-inside">MPQW</span><span class="topo-membrane">LLGIFIAYLIVAVLVVI</span><span class="topo-unknown">SQPFKAKKRDLFGR</span></span>
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
      <td>13</td>
      <td>1</td>
      <td>13</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>31</td>
      <td>15</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>47</td>
      <td>32</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>65</td>
      <td>48</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>69</td>
      <td>66</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>85</td>
      <td>70</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>126</td>
      <td>86</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>141</td>
      <td>127</td>
      <td>141</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>142</td>
      <td>145</td>
      <td>142</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>162</td>
      <td>146</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>176</td>
      <td>163</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1126##sciadv.abe3717

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6wvf">6WVF</a></td>
      <td>2.9</td>
      <td></td>
      <td>DsbB with termini restrained by split sfGFP</td>
      <td><a href="/xray-mp-wiki/reagents/cofactors/ubiquinone/">Ubiquinone</a> (UQ)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length DsbB with His6-myc tag; Cys41Ser mutant and Cys130Ser mutant variants

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6wvf">6WVF</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MS</span><span class="topo-inside">KGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTL</span></span>
<span class="topo-line"><span class="topo-inside">VTTL</span><span class="topo-unknown">G</span><span class="topo-inside">VQCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNR</span></span>
<span class="topo-line"><span class="topo-inside">IELKGIDFKEDGNILGHKLEYNNQASQGR</span><span class="topo-membrane">GAWLLMAFTALALEL</span><span class="topo-outside">TALWFQHVMLLKPCVL</span></span>
<span class="topo-line"><span class="topo-outside">CIYE</span><span class="topo-membrane">RVALFGVLGAALIGAI</span><span class="topo-inside">APK</span><span class="topo-unknown">T</span><span class="topo-inside">PL</span><span class="topo-membrane">RYVAMVIWLYSAFRGVQ</span><span class="topo-outside">LTYEHTMLQLYPSPFAT</span></span>
<span class="topo-line"><span class="topo-outside">SDFMVRFPEWLPLDKWVPQVFVASGDCAERQWDFLGLEMPQWL</span><span class="topo-membrane">LGIFIAYLIVAVLVVI</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-inside">QPFKNSHNVYITADKQKNGIKANFKIRHNVEDGSVQLADHYQQNTPIGDGPVLLPDNHYL</span></span>
<span class="topo-line"><span class="topo-inside">STQSVLSKDPNEKRDHMVLLEFVTAAGITH</span><span class="topo-unknown">HHHHHHHHH</span></span>
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
      <td>3</td>
      <td>64</td>
      <td>3</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>149</td>
      <td>68</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>164</td>
      <td>152</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>184</td>
      <td>167</td>
      <td>186</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>200</td>
      <td>187</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>203</td>
      <td>203</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>206</td>
      <td>207</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>223</td>
      <td>209</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>283</td>
      <td>226</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>299</td>
      <td>286</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>390</td>
      <td>302</td>
      <td>392</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Cys104-Cys130 disulfide is the initial-state substrate for DsbA

The 3.4 A structure of DsbB(Cys41Ser)-Fab directly visualizes the Cys104-Cys130 disulfide bond that is ready to interact with reduced [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/). This represents the initial state of DsbB before [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) binding, confirming the 'cysteine relocation' mechanism proposed previously. Upon [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) binding, Cys104 is pulled into the hydrophobic groove of [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/), separating it from Cys130.

### Amphiphilic horizontal helix regulates DsbB activity

The P2 loop of DsbB contains a membrane-parallel amphiphilic alpha-helix (horizontal helix, residues 116-120) that associates peripherally with the cytoplasmic membrane through hydrophobic side chains. Systematic mutagenesis showed that disrupting this membrane association with charged or helix-breaking residues severely impaired [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) oxidation activity. The horizontal helix acts as a membrane tether that restricts movement of the catalytically essential P2 cysteines, functioning as a ratchet for thiol-disulfide exchange.

### Conformational transitions during DsbB catalysis

Comparison of three DsbB states - the initial state (DsbB(Cys41Ser)-Fab), the DsbA-bound state (DsbB(Cys130Ser)-DsbA(Cys33Ala)), and the NMR structure of DsbB[CSSC] - reveals sequential cysteine relocations. In the initial state, Cys104-Cys130 are paired. Upon [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) binding, Cys104 separates from Cys130 and forms an intermolecular disulfide with [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) Cys30. After [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) release, the Cys130-containing loop moves to approach Cys41 in P1, enabling the next catalytic cycle.

### Charge-transfer complex between Cys44 and ubiquinone

The 3.4 A structure provides direct evidence of a charge-transfer complex between Cys44 of DsbB and bound [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) (UQ), with the sulfur atom of Cys44 only 3.1 A from the C1 atom of the UQ ring. Arg48 forms a hydrogen bond with the thiolate form of Cys44, stabilizing the complex. This supports the proposed mechanism of de novo disulfide bond generation on DsbB using the oxidizing equivalents of quinone species.

### Catalytic triad mechanism revealed by high-resolution structure

The 2.9 A structure of termini-restrained DsbB (PDB 6WVF) reveals that the thiol oxidoreductase is activated through a catalytic triad (Arg48, His91, Glu47), similar to cysteine proteases. Arg48 and His91 form hydrogen bonds with the two carbonyl oxygens of the bound ubiquinone, stabilizing the charge-transfer complex and facilitating its formation through induced polarization of the quinone ring. Glu47 is positioned to maintain the correct orientation of Arg48. Arg48 and His91 are among the most conserved residues in DsbB homologs, and mutations of these residues show accumulation of DsbB-DsbA complex and reduced quinone binding, confirming impaired Cys44 reactivity.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/dsbA/">DsbA</a> — Direct functional partner in periplasmic disulfide bond formation
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/disulfide-bond-formation/">Disulfide Bond Formation</a> — DsbB is the central enzyme in the bacterial disulfide bond formation pathway
- <a href="/xray-mp-wiki/concepts/miscellaneous/termini-restraining/">Termini Restraining</a> — High-resolution DsbB structure (6WVF) was determined using termini-restraining approach with split sfGFP
- <a href="/xray-mp-wiki/reagents/detergents/dhpc/">DHPC</a> — Detergent used in cryoprotection during crystallization
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion-sitting-drop/">Sitting Drop Vapor Diffusion</a> — Crystallization method used for DsbB-Fab complex
- <a href="/xray-mp-wiki/reagents/cofactors/ubiquinone/">Ubiquinone</a> — Referenced in context related to Ubiquinone
- <a href="/xray-mp-wiki/reagents/buffers/mops/">Mops</a> — Referenced in context related to Mops
