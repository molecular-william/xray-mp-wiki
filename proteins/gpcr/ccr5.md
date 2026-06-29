---
title: "CCR5 Chemokine Receptor (C-C Chemokine Receptor Type 5)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1241475]
verified: false
---

# CCR5 Chemokine Receptor (C-C Chemokine Receptor Type 5)

## Overview

CCR5 (C-C chemokine receptor type 5) is a class A G protein-coupled receptor (GPCR) that functions as a chemokine receptor and is a major co-receptor for HIV-1 entry. The crystal structure of CCR5 bound to [Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/), an allosteric inverse agonist and HIV entry inhibitor, was determined by X-ray crystallography. CCR5 is structurally similar to the chemokine receptor [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) (Calpha RMSD of 1.8 Å within the 7TM bundle at 34% sequence identity) but differs in several key regions. ECL2 forms a beta-hairpin structure stabilized by disulfide bonds (Cys101(3.25)-Cys178 in ECL2 and Cys20-Cys269(7.25)). CCR5 features a short alpha helix VIII (absent in CXCR4), a tilted helix IV with a shorter intracellular portion, and a two-turn alpha helix in ICL2 that runs parallel to the membrane. [Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/) binds in a deep pocket defined by residues from helices I, II, III, V, VI, and VII, making no contacts with the extracellular loops, and functions as an allosteric inverse agonist by stabilizing CCR5 in an inactive conformation.


## Publications

### doi/10.1126##science.1241475

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4mbs">4MBS</a></td>
      <td>2.7</td>
      <td>—</td>
      <td>CCR5-<a href="/xray-mp-wiki/reagents/ligands/maraviroc/">Maraviroc</a> complex</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/maraviroc/">Maraviroc</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Insect cell expression (Sf9 or High Five cells)
- **Construct**: CCR5 with T4 lysozyme fusion (BRIL) for crystallization
- **Notes**: Detailed expression protocol described in supplementary materials

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
      <td>Membrane preparation and solubilization</td>
      <td>Standard membrane protein solubilization</td>
      <td>—</td>
      <td></td>
      <td>Methods described in supplementary materials</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity-chromatography</a> and size-exclusion chromatography</td>
      <td>—</td>
      <td></td>
      <td>Details in supplementary materials</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) or vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CCR5-<a href="/xray-mp-wiki/reagents/ligands/maraviroc/">Maraviroc</a> complex</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structure determined in complex with <a href="/xray-mp-wiki/reagents/ligands/maraviroc/">Maraviroc</a>. Detailed crystallization conditions in supplementary materials.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4mbs">4MBS</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GAPDYQVSSPIYDINYYTSE</span><span class="topo-inside">PCQKINVKQIAARL</span><span class="topo-membrane">LPPLYSLVFIFGFVGNMLVILILIN</span><span class="topo-outside">Y</span></span>
<span class="topo-line"><span class="topo-outside">KRLKSM</span><span class="topo-membrane">TDIYLLNLAISDLFFLLTVPFWAH</span><span class="topo-inside">YAAAQWDFGNT</span><span class="topo-membrane">MCQLLTGLYFIGFFSGIFF</span></span>
<span class="topo-line"><span class="topo-membrane">IILLTIDRY</span><span class="topo-outside">LAVVH</span><span class="topo-unknown">AVFALKA</span><span class="topo-outside">RTV</span><span class="topo-membrane">TFGVVTSVITWVVAVFASLPNII</span><span class="topo-inside">FTRSQKEGLHYTC</span></span>
<span class="topo-line"><span class="topo-inside">SSHFPYSQYQFWKN</span><span class="topo-membrane">FQTLKIVILGLVLPLLVMVICYSG</span><span class="topo-outside">ILKTLLRMKKYTCTVCGYIYNP</span></span>
<span class="topo-line"><span class="topo-outside">EDGDPDNGVNPGTDFKDIPDDWVCPLCGVGKDQFEEVEEEKKRHRDV</span><span class="topo-membrane">RLIFTIMIVYFLF</span></span>
<span class="topo-line"><span class="topo-membrane">WAPYNIVLLLNTFQ</span><span class="topo-inside">EFFGLNNCSSSNRLDQA</span><span class="topo-membrane">MQVTETLGMTHCCINPIIYAFVG</span><span class="topo-unknown">EEFRNY</span></span>
<span class="topo-line"><span class="topo-unknown">LLVFF</span><span class="topo-outside">Q</span><span class="topo-unknown">KHIAKRFCKCCSIFQQEAPERASSVYTRSTGEQEISVGLGRPLEVLFQ</span></span>
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
      <td>20</td>
      <td>-1</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>34</td>
      <td>19</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>59</td>
      <td>33</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>66</td>
      <td>58</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>90</td>
      <td>65</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>101</td>
      <td>89</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>129</td>
      <td>100</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>134</td>
      <td>128</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>141</td>
      <td>133</td>
      <td>139</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>142</td>
      <td>144</td>
      <td>140</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>167</td>
      <td>143</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>194</td>
      <td>166</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>218</td>
      <td>193</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>287</td>
      <td>217</td>
      <td>234</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>314</td>
      <td>235</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>331</td>
      <td>262</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>354</td>
      <td>279</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>365</td>
      <td>302</td>
      <td>312</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>366</td>
      <td>366</td>
      <td>313</td>
      <td>313</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>414</td>
      <td>314</td>
      <td>361</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Maraviroc binding mode and allosteric inverse agonism

[Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/) occupies the bottom of the CCR5 ligand-binding pocket, defined by residues from helices I, II, III, V, VI, and VII. Key interactions include: (1) salt bridge between the protonated tropane nitrogen and Glu283(7.39); (2) hydrogen bond between the carboxamide nitrogen and Tyr251(6.51); (3) hydrogen bonds between the triazole amine and Tyr37(1.39) and a water molecule; (4) hydrogen bonds between a fluorine of the cyclohexane ring and Thr195(5.39) and Thr259(6.59); and (5) hydrophobic interactions between the phenyl group and five aromatic residues (Tyr108(3.32), Phe109(3.33), Phe112(3.36), Trp248(6.48), Tyr251(6.51)). The length of the carbon chain between the tropane and carboxamide nitrogens correlates with anti-HIV activity. [Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/) acts as an allosteric inverse agonist by stabilizing CCR5 in an inactive conformation, reducing chemokine and gp120 binding.

### Structural basis for HIV-1 co-receptor selectivity between CCR5 and CXCR4

The ligand-binding pockets of CCR5 and [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) differ substantially in charge distribution. In [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/), acidic residues (Asp97(2.63), Asp171(4.60), Asp187 in ECL2, Asp193(5.32), Asp262(6.58)) are critical for ligand binding and HIV-1 infectivity. In CCR5, these are substituted by uncharged residues (Tyr89(2.63), Gly163(4.60), Ser179, Gln188(5.32), Asn258(6.58)). Moreover, the [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) N terminus contains nine acidic residues while CCR5 has only three. These differences correlate with the different charge distributions in the V3 loops of X4-tropic versus R5-tropic HIV-1 viruses. Models of CCR5-R5-V3 and [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/)-X4-V3 complexes suggest that differential charge distribution and steric hindrances from residue substitutions are major determinants of HIV-1 co-receptor selectivity.

### Structural differences between CCR5 and CXCR4

Beyond the binding pocket, CCR5 and [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) differ in several structural features: (1) CCR5 has a short helix VIII at the C terminus with a conserved F(RK)xx(FL)xxx(LF) motif, while [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) has an extended disordered C terminus; (2) helix IV in CCR5 is tilted ~15 degrees relative to [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/), with its intracellular portion 1.5 turns shorter; (3) ICL2 in CCR5 contains a two-turn alpha helix running parallel to the membrane, stabilized by hydrophobic interactions (Phe135, Ala136 with Leu128(3.53) and Ala129(3.54)), while ICL2 is unstructured in [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/); (4) the extracellular end of helix VII shifts ~3 Å away from the central axis in CCR5 versus [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/).


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/">Human Beta2-Adrenergic Receptor (beta2 AR)</a> — Class A GPCR for structural comparison of 7TM architecture
- <a href="/xray-mp-wiki/reagents/ligands/maraviroc/">Maraviroc</a> — Co-crystallized allosteric inverse agonist and HIV entry inhibitor bound to CCR5 in the structure
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/">Human Beta2-Adrenergic Receptor (beta2 AR)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/gpcr/cxcr4/">Human CXCR4 Chemokine Receptor</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/pumps-atpases/ribu/">RibU (ECF-Type Riboflavin Transporter S Component from Staphylococcus aureus)</a> — Related protein structure
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/reagents/ligands/maraviroc/">Maraviroc</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl beta-D-glucopyranoside (OG)</a> — Detergent used in the study
