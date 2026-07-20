---
title: "M1-StaR-T4L"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2021.11.001]
verified: agent
uniprot_id: P11229
---

# M1-StaR-T4L

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P11229">UniProt: P11229</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) is a thermostabilized, engineered construct of the human [M1 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/) designed for X-ray crystallography. It combines multiple stability-enhancing modifications: a chimeric M4 N-terminus, 12 thermostabilizing mutations (StaR), C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), and [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) ([T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)) fusion in the third intracellular loop (ICL3). This construct enabled the determination of three high-resolution structures of the M1 receptor bound to orthosteric agonists ([77-LH-28-1](/xray-mp-wiki/reagents/ligands/77-lh-28-1/), [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/), [GSK1034702](/xray-mp-wiki/reagents/ligands/gsk1034702/)), providing key insights into muscarinic receptor activation and agonist selectivity.


## Publications

### doi/10.1016##j.cell.2021.11.001

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zfz">6ZFZ</a></td>
      <td>2.17 A</td>
      <td>C 2 2 21</td>
      <td>M1-StaR-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> in ICL3)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/77-lh-28-1/">77-LH-28-1</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zg4">6ZG4</a></td>
      <td>2.17 A</td>
      <td>C 2 2 21</td>
      <td>M1-StaR-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> in ICL3)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/htl9936/">HTL9936</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zg9">6ZG9</a></td>
      <td>2.17 A</td>
      <td>C 2 2 21</td>
      <td>M1-StaR-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> in ICL3)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/gsk1034702/">GSK1034702</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf21 insect cells (baculovirus expression vector system)
- **Construct**: M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) construct with N-terminal GP64 signal sequence, chimeric M4 N-terminus (residues 1-95 of M4 replacing residues 1-87 of M1), residues 88-438 of M1 receptor, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (residues 439-460 removed), [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) inserted into ICL3 between residues 219 and 354, and C-terminal deca-histidine tag. The StaR variant contains 12 thermostabilizing mutations: F27A, T32A, V46L, L64A, T95A, W101A, S112A, A143L, A196T, K362A, A364L, S411A.


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
      <td>Cell culture and infection</td>
      <td>Sf21 cells infected with baculovirus at multiplicity of infection 2, harvested 48 hours post-infection</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cells grown at 27 degrees Celsius with constant shaking in ESF 921 medium supplemented with 10% FBS and 1% penicillin/streptomycin</td>
    </tr>
    <tr>
      <td>Cell disruption and membrane preparation</td>
      <td>Cell disruption at 15000 psi using microfluidizer, membranes pelleted by ultracentrifugation at 200000 g for 50 min, high salt washes</td>
      <td>--</td>
      <td>PBS, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, protease inhibitor cocktail; wash buffer: PBS, 1 M NaCl, protease inhibitor cocktail + --</td>
      <td>Membranes resuspended in 40 mM Tris pH 7.6, 500 mM NaCl with protease inhibitors and stored at -80 degrees Celsius</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membranes incubated with ligand (40 uM <a href="/xray-mp-wiki/reagents/ligands/htl9936/">HTL9936</a> or <a href="/xray-mp-wiki/reagents/ligands/gsk1034702/">GSK1034702</a> or <a href="/xray-mp-wiki/reagents/ligands/77-lh-28-1/">77-LH-28-1</a>) for 40 min at room temperature, then solubilized with 1.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for 1 hour at 4 degrees Celsius</td>
      <td>--</td>
      <td>40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 500 mM NaCl, protease inhibitor cocktail + 1.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Solubilized material clarified by centrifugation at 145000 g for 60 min</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Batch binding to <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)](/xray-mp-wiki/reagents/additives/nickel-nta/) Superflow resin for 3 hours, gradient wash (10 to 60 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>), elution with 245 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)](/xray-mp-wiki/reagents/additives/nickel-nta/) Superflow resin</td>
      <td>40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (binding); 40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 500 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 70 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash); 40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 500 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 245 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (elution) + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Ligand (20 uM) included in all binding and wash buffers</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) on <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column pre-equilibrated with buffer containing ligand</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 40 uM ligand + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Protein concentrated to approximately 60 mg/mL using 100 kDa cut-off membrane prior to crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified M1-StaR-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> at approximately 60 mg/mL in 40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 40 uM ligand</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 degrees Celsius</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals were flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Three structures were solved: M1-StaR-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> with <a href="/xray-mp-wiki/reagents/ligands/77-lh-28-1/">77-LH-28-1</a> (PDB 6ZFZ), <a href="/xray-mp-wiki/reagents/ligands/htl9936/">HTL9936</a> (PDB 6ZG4), and <a href="/xray-mp-wiki/reagents/ligands/gsk1034702/">GSK1034702</a> (PDB 6ZG9). All structures were solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using the turkey beta1-adrenergic receptor (PDB 2Y00) as the search model. Iterative rounds of model refinement with BUSTER were interspersed with manual model building in COOT. Two TLS groups corresponding to the receptor and <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> were defined.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zfz">6ZFZ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">METV</span><span class="topo-membrane">EMVAIATVAGLLSLATVTGNILLML</span><span class="topo-outside">SIKVNRQLQTVNNY</span><span class="topo-membrane">FAFSLACADLIIGAFSMNLYTVYII</span><span class="topo-inside">MGHWALGAL</span><span class="topo-membrane">ACDLALALDYVASNAAVMNLLLISF</span><span class="topo-outside">DRYFSVTRPLSYRAKRTP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">RRAL</span><span class="topo-membrane">LMIGLAWLVSFVLWAPAILFW</span><span class="topo-inside">QYLVGERTVLAGQC</span><span class="topo-membrane">YIQFLSQPIITFGTAMATFYLPVTVMCTLYW</span><span class="topo-outside">RIYRETENRANIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-outside">TFSLVKEKAALRT</span><span class="topo-membrane">LSAILLAFILTWTPYNIMVLVSTF</span><span class="topo-inside">CKDCVPE</span><span class="topo-membrane">TLWELGYWLCYVNATINPMCYAL</span><span class="topo-outside">CNKAFRDTFRLLLLARWDH</span><span class="topo-unknown">HHHHHHHHH</span></span>
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
      <td>1</td>
      <td>4</td>
      <td>20</td>
      <td>23</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>24</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>43</td>
      <td>49</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>68</td>
      <td>63</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>77</td>
      <td>88</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>97</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>124</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>144</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>159</td>
      <td>165</td>
      <td>178</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>190</td>
      <td>179</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>200</td>
      <td>210</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>360</td>
      <td>1002</td>
      <td>1161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>373</td>
      <td>354</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>397</td>
      <td>367</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>404</td>
      <td>391</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>405</td>
      <td>427</td>
      <td>398</td>
      <td>420</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>446</td>
      <td>421</td>
      <td>439</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>447</td>
      <td>455</td>
      <td>440</td>
      <td>448</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg4">6ZG4</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">METVEMV</span><span class="topo-membrane">AIATVAGLLSLATVTGNILLMLSIKV</span><span class="topo-inside">NRQLQTVNN</span><span class="topo-membrane">YFAFSLACADLIIGAFSMNLYTVYI</span><span class="topo-outside">IMGHWALGAL</span><span class="topo-membrane">ACDLALALDYVASNAAVMNLLLISF</span><span class="topo-inside">DRYFSVTRPLSYRAKRTP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RRA</span><span class="topo-membrane">LLMIGLAWLVSFVLWAPAILFWQYL</span><span class="topo-outside">VGERTVLAGQCYIQFL</span><span class="topo-membrane">SQPIITFGTAMATFYLPVTVMCTLY</span><span class="topo-inside">WRIYRETENRANIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">AKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-inside">TFSLVKEKAALRT</span><span class="topo-membrane">LSAILLAFILTWTPYNIMVLVSTFC</span><span class="topo-outside">KDCVPET</span><span class="topo-membrane">LWELGYWLCYVNATINPMCYALC</span><span class="topo-inside">NKAF</span><span class="topo-unknown">RDTFRLLLLARWDHHHHHHHHHH</span></span>
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
      <td>1</td>
      <td>7</td>
      <td>20</td>
      <td>26</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>33</td>
      <td>27</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>42</td>
      <td>53</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>67</td>
      <td>62</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>77</td>
      <td>87</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>97</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>123</td>
      <td>122</td>
      <td>142</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>148</td>
      <td>143</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>164</td>
      <td>168</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>184</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>373</td>
      <td>209</td>
      <td>366</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>398</td>
      <td>367</td>
      <td>391</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>399</td>
      <td>405</td>
      <td>392</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>428</td>
      <td>399</td>
      <td>421</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>429</td>
      <td>432</td>
      <td>422</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>446</td>
      <td>426</td>
      <td>439</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg9">6ZG9</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">METV</span><span class="topo-membrane">EMVAIATVAGLLSLATVTGNILLM</span><span class="topo-inside">LSIKVNRQLQTVNNYF</span><span class="topo-membrane">AFSLACADLIIGAFSMNLYTVYII</span><span class="topo-outside">MGHWAL</span><span class="topo-membrane">GALACDLALALDYVASNAAVMNLLLIS</span><span class="topo-inside">FDRYFSVTRPLSYRAKRTP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RRALLM</span><span class="topo-membrane">IGLAWLVSFVLWAPAILFW</span><span class="topo-outside">QYLVGERTVLAGQC</span><span class="topo-membrane">YIQFLSQPIITFGTAMATFYLPVTVMCTLY</span><span class="topo-inside">WRIYRETENRANIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">AKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-inside">TFSLVKEKAALRTL</span><span class="topo-membrane">SAILLAFILTWTPYNIMVLVSTF</span><span class="topo-outside">CKDCVPET</span><span class="topo-membrane">LWELGYWLCYVNATINPMC</span><span class="topo-inside">YALCN</span><span class="topo-unknown">KAFRDTFRLLLLARW</span><span class="topo-inside">DH</span><span class="topo-unknown">HHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>4</td>
      <td>20</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>24</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>44</td>
      <td>48</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>68</td>
      <td>64</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>74</td>
      <td>88</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>101</td>
      <td>94</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>126</td>
      <td>121</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>145</td>
      <td>146</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>159</td>
      <td>165</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>189</td>
      <td>179</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>374</td>
      <td>209</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>397</td>
      <td>368</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>405</td>
      <td>391</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>424</td>
      <td>399</td>
      <td>417</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>425</td>
      <td>429</td>
      <td>418</td>
      <td>422</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>444</td>
      <td>423</td>
      <td>437</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>445</td>
      <td>446</td>
      <td>438</td>
      <td>439</td>
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

### StaR thermostabilization mutations

The M1-StaR construct contains 12 thermostabilizing mutations: F27A (1.34),
T32A (1.39), V46L (1.53), L64A (2.43), T95A, W101A (3.28), S112A (3.39),
A143L (4.43), A196T (5.46), K362A (6.32), A364L (6.34), S411A (7.46).
These mutations were identified through a directed evolution approach that
selected for thermostability in the presence of radioligand. The W101A
mutation was additionally designed to enable direct access of small molecule
agonists to the orthosteric binding site.

### T4-lysozyme fusion strategy

[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) ([T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)) was inserted into the third intracellular loop (ICL3) of
the M1 receptor between residues R220 and F355, replacing residues R220-F355.
This fusion strategy, pioneered for GPCR crystallization, replaces the flexible
ICL3 loop with a rigid, well-folded protein domain that promotes crystal
contacts. The [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion did not alter the ligand binding properties of the
receptor compared to wild-type M1 receptor.

### Construct engineering for crystallization

The M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) construct was engineered through a stepwise approach:
first, a chimeric M4 N-terminus (residues 1-95 of M4 replacing residues
1-87 of M1) was introduced to reduce toxicity associated with high
expression levels. Second, 12 thermostabilizing mutations (StaR) were
introduced. Third, the C-terminal 22 residues were truncated. Fourth,
[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) was inserted into ICL3. These modifications together
enabled the crystallization of the M1 receptor in complex with agonists.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/">M1 Muscarinic Acetylcholine Receptor</a> — Wild-type M1 receptor; M1-StaR-T4L is the crystallization-optimized construct
- <a href="/xray-mp-wiki/proteins/gpcr/turkey-beta1-ar-m23/">Turkey Beta1-Adrenergic Receptor M23</a> — Template structure (PDB 2Y00) used for molecular replacement
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL Fusion Protein</a> — Alternative fusion protein tag used for GPCR crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-Maltopyranoside (DDM)</a> — Primary detergent used for solubilization and purification
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for all M1-StaR-T4L structures
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
