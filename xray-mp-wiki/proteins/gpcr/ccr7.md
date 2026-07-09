---
title: "Human CC Chemokine Receptor 7 (CCR7)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2019.07.028]
verified: regex
uniprot_id: P32248
---

# Human CC Chemokine Receptor 7 (CCR7)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P32248">UniProt: P32248</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The CC chemokine receptor 7 (CCR7) is a class A G protein-coupled receptor (GPCR)
that balances immunity and tolerance by homeostatic trafficking of immune cells.
CCR7 mediates responses to chemokines CCL19 and CCL21, guiding B cells, T cells,
and antigen-presenting dendritic cells to lymph nodes. In cancer, CCR7-mediated
trafficking promotes lymph node metastasis, making the receptor a promising
therapeutic target. The crystal structure of human CCR7 was determined at 2.1 A
resolution using a Sialidase NanA fusion protein for crystallization. The structure
reveals the ligand Cmp2105 bound to an intracellular allosteric binding pocket
located between transmembrane helix 7 and helix 8 (TM7-H8 turn), a conserved
pharmacological hotspot among chemokine receptors. Cmp2105 contains a
thiadiazole-dioxide core motif and acts as an intracellular allosteric antagonist
that stabilizes an inactive CCR7 conformation, interfering with G protein and
arrestin binding. A computational screen identified additional CCR7 modulators
including Navarixin (a CXCR1/CXCR2 phase II antagonist), CS-1, and CS-2,
demonstrating that the TM7-H8 allosteric pocket can be targeted by diverse
chemotypes with selectivity across chemokine receptor subtypes.

## Publications

### doi/10.1016##j.cell.2019.07.028

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6qzh">6QZH</a></td>
      <td>2.1</td>
      <td>P212121</td>
      <td>Human CCR7-Sialidase NanA fusion with L145W mutation, HRV 3C cleavage sites, deletion of ICL3 residues 248-256 (replaced by NanA residues 1-470)</td>
      <td>Cmp2105</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells using Bac-to-Bac baculovirus system
- **Construct**: CCR7-Sialidase NanA fusion: N-terminal decahistidine tag, two HRV 3C protease cleavage sites (between residues 36-43 and 352-359), deletion of Arg248-Phe256 (ICL3) replaced by Sialidase NanA (residues 1-470, PDB: 2YA4) flanked by GS linkers, L145W thermostabilizing mutation
- **Notes**: Expressed in 10 L Wave Bioreactors at 27 C, 19 rocks/min, 40% oxygen. Infection at 2x10^6 cells/mL, harvested at 72 h post-infection.

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
      <td>Cell lysis and membrane preparation</td>
      <td>Dounce homogenization and ultracentrifugation</td>
      <td>—</td>
      <td>10 mM HEPES/NaOH pH 7.5, 10 mM MgCl2, 20 mM KCl, Roche protease inhibitors</td>
      <td>Membranes washed extensively with low salt buffer, high salt buffer (1 M NaCl), and low salt buffer.</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM HEPES/NaOH pH 7.5, 300 mM NaCl, 20 mM imidazole/HCl pH 7.5, 23 uM Cmp2105, protease inhibitors + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Membranes pre-treated with 23 uM Cmp2105 and 2 mg/mL iodoacetamide for 1 h at 4 C before solubilization.</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Decahistidine-tagged CCR7-NanA fusion purified using <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Superflow resin.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td>—</td>
      <td></td>
      <td>Final polishing step.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified CCR7-Sialidase NanA complex with Cmp2105 in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> buffer</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>-- (not specified)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>-- (not specified)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> crystallization in meso. Data collected at X06SA (PXI) beamline, Swiss Light Source. 5x5 um collimated beam. Data from 11 crystals merged.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qzh">6QZH</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPGSSLCSKK</span><span class="topo-outside">DVRNFKAWF</span><span class="topo-membrane">LPIMYSIICFVGLLGNGLVVLTYIY</span><span class="topo-inside">FKRLKTMT</span><span class="topo-membrane">DTYLLNLAVADILFLLTLPFWAY</span><span class="topo-outside">SAAKSWVFGVH</span><span class="topo-membrane">FCKLIFAIYKMSFFSGMWLLLCIS</span><span class="topo-inside">IDRYVAIV</span><span class="topo-unknown">QA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">VSA</span><span class="topo-inside">HRHRARVLLISK</span><span class="topo-membrane">LSCVGIWILATVLSIPELLYS</span><span class="topo-outside">DLQRSSSEQAMRCSLITEHVE</span><span class="topo-membrane">AFITIQVAQMVIGFLVPLLAMSF</span><span class="topo-inside">CYLVIISKLHALTEKTDIFESGRNGNPNKDGIKSYRIPAL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">LKTDKGTLIAGADERRLHSSDWGDIGMVIRRSEDNGKTWGDRVTITNLRDNPKASDPSIGSPVNIDMVLVQDPETKRIFSIYDMFPEGKGIFGMSSQKEEAYKKIDGKTYQILYREGEKG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">AYTIRENGTVYTPDGKATDYRVVVDPVKPAYSDKGDLYKGDQLLGNIYFTTNKTSPFRIAKDSYLWMSYSDDDGKTWSAPQDITPMVKADWMKFLGVGPGTGIVLRNGPHKGRILIPVYT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">TNNVSHLDGSQSSRVIYSDDHGKTWHAGEAVNDNRQVDGQKIHSSTMNNRRAQNTESTVVQLNNGDVKLFMRGLTGDLQVATSKDGGVTWEKDIKRYPQVKDVYVQMSAIHTMHEGKEYI</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">ILSNAGGPKRENGMVHLARVEENGELTWLKHNPIQKGEFAYNSLQELGNGEYGILYEHTEKGQNAYTLSFRKFNWEFLSKSKGHERN</span><span class="topo-unknown">KA</span><span class="topo-inside">IKV</span><span class="topo-membrane">IIAVVVVFIVFQLPYNGVVLAQTV</span><span class="topo-unknown">ANFN</span></span>
<span class="topo-ruler">       730       740       750       760       770       780     </span>
<span class="topo-line"><span class="topo-unknown">ITSS</span><span class="topo-outside">TCELSKQ</span><span class="topo-membrane">LNIAYDVTYSLACVRCCVNPFLYAFIG</span><span class="topo-inside">VKFRNDLFKLF</span><span class="topo-unknown">KDLGCLSGGRLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>10</td>
      <td>42</td>
      <td>51</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>19</td>
      <td>52</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>44</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>52</td>
      <td>86</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>75</td>
      <td>94</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>86</td>
      <td>117</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>110</td>
      <td>128</td>
      <td>151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>118</td>
      <td>152</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>123</td>
      <td>160</td>
      <td>164</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>124</td>
      <td>135</td>
      <td>165</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>156</td>
      <td>177</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>157</td>
      <td>177</td>
      <td>198</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>200</td>
      <td>219</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>210</td>
      <td>242</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>682</td>
      <td>1001</td>
      <td>1472</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>683</td>
      <td>687</td>
      <td>255</td>
      <td>259</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>688</td>
      <td>689</td>
      <td>260</td>
      <td>261</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>690</td>
      <td>692</td>
      <td>262</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>693</td>
      <td>716</td>
      <td>265</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>717</td>
      <td>724</td>
      <td>289</td>
      <td>296</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>725</td>
      <td>731</td>
      <td>297</td>
      <td>303</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>732</td>
      <td>758</td>
      <td>304</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>759</td>
      <td>769</td>
      <td>331</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>770</td>
      <td>785</td>
      <td>342</td>
      <td>357</td>
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

### Intracellular allosteric binding pocket in CCR7

Cmp2105 binds to an intracellular allosteric pocket located between TM1, TM2,
TM3, TM6, and the TM7-H8 turn. The thiadiazole-dioxide core motif positions
the sulfonamide group to interact with a conserved patch of residues at the
TM7-H8 turn (Tyr326, Gly330, Val331, Lys332, Phe333). This binding site
spatially overlaps with the Gi protein binding site, allowing Cmp2105 to
function as an intracellular allosteric antagonist.

### TM7-H8 turn as a pharmacological hotspot for chemokine receptors

The TM7-H8 turn is a conserved structural motif among CC and CXC chemokine
receptors. The Gly330 residue at the end of TM8 is conserved among most human
chemokine receptors and enables the tight interhelical joint that forms the
allosteric pocket. Multiple chemokine receptor ligands (CCR2-RA-[R] in CCR2,
Vercirnon in CCR9, Cmp2105 in CCR7) bind this motif, suggesting it is a
promising hotspot for multi-target drug design against chemokine receptors.

### Cross-reactivity of Navarixin at CCR7

Navarixin (SCH-527123 / MK-7123), a clinical phase II antagonist for CXCR1
and CXCR2, was identified as a CCR7 modulator by 3D shape similarity screening.
Its cyclobutene-dione core motif is almost identical to the thiadiazole-dioxide
of Cmp2105 in overall geometry. Navarixin suppresses arrestin recruitment in
response to CCL19 (IC50 33.9 uM) and stabilizes CCR7 (EC50 13.38 uM). This
finding suggests that part of Navarixin's anticancer effects may involve
silencing CCR7 in addition to CXCR1/CXCR2.

### Structural comparison with other chemokine receptors

CCR7 shares the canonical 7TM GPCR fold with Ca RMSD of 1.28-1.97 A to CCR2,
CCR5, CCR9, and CXCR4 at 29.9-39.1% sequence identity. Sequence and structural
differences between receptors are higher in the orthosteric chemokine binding
pocket (extracellular half) than in the intracellular side, which opens upon
activation. Cmp2105 stabilizes an inactive CCR7 conformation, confirmed by a
putative sodium ion in a conserved site between TM2, TM3, TM6, and TM7.

### Thermofluor-based drug discovery approach

An automated thermofluor (CPM thermal shift) screening methodology was used to
identify CCR7-binding compounds from a focused library of 293 compounds
selected by 3D shape similarity search from Roche's 2.3 million compound
repository. This approach detected both novel (CS-1, CS-2) and clinically
relevant (Navarixin) CCR7 modulators, demonstrating the utility of combining
structural data with thermal stability screening for GPCR drug discovery.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/ccr5/">CCR5 Chemokine Receptor</a> — Related human CC chemokine receptor for structural comparison
- <a href="/xray-mp-wiki/proteins/gpcr/us28/">US28 Viral Chemokine Receptor</a> — Viral chemokine receptor for comparison of active/inactive conformations
- <a href="/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/">Human Beta2-Adrenergic Receptor (beta2 AR)</a> — Class A GPCR for comparison of intracellular allosteric binding
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used for CCR7 crystallization
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — MR method used with homology model of CCR7 and Sialidase NanA (PDB 2YA4)
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction (SAD)</a> — Native SAD used in combination with MR for structure determination
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-docking/">Molecular Docking</a> — Docking of CS-1 and Navarixin into CCR7 allosteric pocket using GOLD
- <a href="/xray-mp-wiki/methods/quality-assessment/thermal-shift-assay/">Thermal Shift Assay</a> — CPM-based thermofluor assay used to validate ligand binding to CCR7
