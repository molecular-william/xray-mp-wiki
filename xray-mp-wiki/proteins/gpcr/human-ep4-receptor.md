---
title: "Human Prostaglandin E Receptor EP4"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41589-018-0131-3]
verified: regex
uniprot_id: P35408
---

# Human Prostaglandin E Receptor EP4

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P35408">UniProt: P35408</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The prostaglandin E2 receptor EP4 (EP4) is a class A G protein-coupled receptor (GPCR) for prostaglandin E2 (PGE2). EP4 couples primarily to Gs and Gi proteins and plays important roles in inflammation, pain, cancer, and bone metabolism. The crystal structure of the human EP4 receptor was determined in complex with the antagonist ONO-AE3-208 at 3.2 A resolution (PDB 5YWY), revealing the molecular basis of ligand recognition at the lipid-bilayer interface. The structure was enabled by a thermostabilized construct with an ICL3 deletion and double mutation A62L/G106R, in complex with the Fab001 antibody fragment for crystallization in lipidic cubic phase.

## Publications

### doi/10.1038##s41589-018-0131-3

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ywy">5YWY</a></td>
      <td>3.2 A</td>
      <td>C2221</td>
      <td>Human EP4 with ICL3 deletion (residues 243-263 replaced by GG), thermostabilizing mutations A62L (2.47) and G106R (3.39), N-terminal HA signal peptide and <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>, C-terminal octa-histidine tag, complexed with Fab001 antibody fragment</td>
      <td>ONO-AE3-208 (antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5yfi">5YFI</a></td>
      <td>1.85 A</td>
      <td>P212121</td>
      <td>Fab001 antibody fragment alone</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnTI- cells
- **Construct**: Human EP4 with ICL3 deletion (243-263 replaced by GG), N-terminal HA signal peptide and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), C-terminal octa-histidine tag, thermostabilizing mutations A62L (2.47) and G106R (3.39)

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
      <td>Cell culture and membrane preparation</td>
      <td>HEK293S GnTI- cell expression</td>
      <td>—</td>
      <td></td>
      <td>Cells expressing EP4 harvested, membranes prepared by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td></td>
      <td>Membranes solubilized in buffer containing detergent</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td></td>
      <td>C-terminal octa-histidine tag used for affinity capture</td>
    </tr>
    <tr>
      <td>Antibody complex formation</td>
      <td>Incubation with Fab001</td>
      <td>—</td>
      <td></td>
      <td>Purified EP4 mixed with excess Fab001 antibody fragment for complex formation</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>—</td>
      <td></td>
      <td>Final purification step to isolate EP4-Fab001 complex</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic Cubic Phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/))</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>EP4-Fab001 complex at ~30 mg/mL</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) using <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>. Data collected at SPring-8 BL32XU. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using Fab001 structure and a GPCR homology model. The structure reveals a ligand-binding pocket at the lipid-bilayer interface formed by TM1, TM2, TM7, and ECL2.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ywy">5YWY</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GTSPGVQSSASLSPDRL</span><span class="topo-outside">NSPVT</span><span class="topo-membrane">IPAVMFIFGVVGNLVAIVVLCKS</span><span class="topo-inside">RKEQKETT</span><span class="topo-membrane">FYTLVCGLLVTDLLGTLLVSPVTI</span><span class="topo-outside">ATYMKGQWPGGQPLCE</span><span class="topo-membrane">YSTFILLFFSLSRLSIICAMSVERY</span><span class="topo-inside">LA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">INHAYFYSHYVD</span><span class="topo-membrane">KRLAGLTLFAVYASNVLFCALPNMGLG</span><span class="topo-outside">SSRLQYPDTWCFIDWTTQVT</span><span class="topo-membrane">AHAAYSYMYAGFSSFLILATVLCNVLVC</span><span class="topo-inside">GALLRMH</span><span class="topo-unknown">RQFFRRI</span><span class="topo-inside">AGAEIQM</span><span class="topo-membrane">VILLIATSLVVL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330  </span>
<span class="topo-line"><span class="topo-membrane">ICSIPLVVRVFVNQLY</span><span class="topo-outside">QPSLEREVSKNP</span><span class="topo-membrane">DLQAIRIASVNPILDPWIYILLRKTVL</span><span class="topo-inside">SKAIEKIKC</span><span class="topo-unknown">LFCRIGGSRRERSGQHCSDSLEENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>18</td>
      <td>22</td>
      <td>18</td>
      <td>22</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>45</td>
      <td>23</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>53</td>
      <td>46</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>77</td>
      <td>54</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>93</td>
      <td>78</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>118</td>
      <td>94</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>132</td>
      <td>119</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>159</td>
      <td>133</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>179</td>
      <td>160</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>207</td>
      <td>180</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>214</td>
      <td>208</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>228</td>
      <td>264</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>256</td>
      <td>271</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>257</td>
      <td>268</td>
      <td>299</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>295</td>
      <td>311</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>304</td>
      <td>338</td>
      <td>346</td>
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

### Ligand binding at the lipid-bilayer interface

The EP4 crystal structure revealed that the antagonist ONO-AE3-208 binds at an unconventional site at the lipid-bilayer interface, rather than in the canonical GPCR orthosteric pocket. The ligand-binding pocket is formed by TM1, TM2, TM7, and ECL2, with the carboxyl group of ONO-AE3-208 projecting toward the extracellular leaflet of the membrane. This binding mode is distinct from other prostanoid receptors and represents the first structural observation of ligand binding at the GPCR-lipid interface.

### ECL2 forms a beta-hairpin cap

EP4 features a unique extended ECL2 that forms a beta-hairpin structure capping the extracellular side. This beta-hairpin is structurally similar to that found in rhodopsin and is stabilized by extensive intramolecular hydrogen bonds. The ECL2 contributes several residues to the ligand-binding pocket and restricts access to the orthosteric binding site.

### Thermostabilizing mutations enable crystallization

The double thermostabilizing mutation A62L(2.47) and G106R(3.39) was critical for EP4 crystallization. The G106R mutation introduces a guanidinium group that occupies the conserved sodium-binding pocket in Class A GPCRs, mimicking the allosteric sodium ion and stabilizing the receptor in an inactive-like conformation. The A62L mutation enhances hydrophobic packing in TM2.

### Sodium-binding pocket as a target for thermostabilization

The G106R(3.39) mutation places a positively charged arginine side chain in the conserved sodium-binding pocket of class A GPCRs. This pocket is normally occupied by a sodium ion that acts as a negative allosteric modulator. The arginine locks the receptor in the inactive state, similar to mutations found in other thermostabilized GPCRs such as A2AAR S91K.

### Molecular dynamics of ligand access

Metadynamics simulations revealed that ONO-AE3-208 accesses the EP4 binding pocket through a lateral opening between TM1 and TM7 at the lipid-bilayer interface, consistent with the membrane-lateral access model. The simulations captured spontaneous ligand binding events, supporting the crystallographically observed binding pose and revealing the pathway of ligand entry from the membrane.

### Fab001 binding at ECL2 interface

The Fab001 antibody fragment binds to the extracellular surface of EP4, primarily recognizing epitopes on ECL2. The Fab001 interaction stabilizes the beta-hairpin conformation of ECL2 and contributes to crystal packing. Mutagenesis of key ECL2 residues (D167G) disrupted Fab001 binding, confirming the antibody-binding interface.


## Cross-References

- <a href="/xray-mp-wiki/proteins/prostaglandin-receptors/">Prostaglandin Receptors</a> — EP4 is a member of the prostanoid receptor family
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr/">G Protein-Coupled Receptors (GPCRs)</a> — EP4 is a class A GPCR
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-inactive-conformation/">GPCR Inactive Conformation</a> — The EP4 structure represents an inactive-like receptor conformation
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used for EP4-Fab001 crystallization
- <a href="/xray-mp-wiki/concepts/signaling-receptors/sodium-allosteric-modulation/">Sodium Ion Allosteric Modulation in GPCRs</a> — G106R mutation occupies the conserved sodium-binding pocket
- <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> — N-terminal FLAG tag used for purification
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His Tag</a> — C-terminal octa-histidine tag for purification
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Host lipid for LCP crystallization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
