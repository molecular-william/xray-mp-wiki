---
title: "Human Sigma-2 Receptor (TMEM97)"
created: 2026-06-09
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-021-04175-x]
verified: false
---

# Human Sigma-2 Receptor (TMEM97)

## Overview

The human sigma-2 receptor (σ2 receptor, encoded by TMEM97) is an orphan transmembrane protein
that is highly expressed in the central nervous system and various cancer cell lines. It has been
a long-standing target for neuropathic pain treatment and cancer diagnostics, though its endogenous
ligand and native function remain unknown. The first X-ray crystal structures of the sigma-2
receptor, determined in complex with three different ligands (PB28, Roluperidone, and [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/)),
revealed a novel membrane protein fold consisting of a four-helix bundle with an intramembrane
ligand-binding pocket. The structures enabled large-scale docking-based virtual screening that
identified potent sigma-2 ligands with efficacy in animal models of neuropathic pain, including
several with activity comparable to gabapentinoids.


## Publications

### doi/10.1038##s41586-021-04175-x

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m93">7M93</a></td>
      <td>2.7 A</td>
      <td>Not stated in raw paper</td>
      <td>Human sigma-2 receptor (TMEM97) expressed in Sf9 insect cells</td>
      <td>PB28 (sigma-2 agonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m93">7M93</a></td>
      <td>3.3 A</td>
      <td>Not stated in raw paper</td>
      <td>Human sigma-2 receptor (TMEM97) expressed in Sf9 insect cells</td>
      <td>Roluperidone (sigma-2 antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m93">7M93</a></td>
      <td>3.2 A</td>
      <td>Not stated in raw paper</td>
      <td>Human sigma-2 receptor (TMEM97) expressed in Sf9 insect cells</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus expression in Sf9 insect cells
- **Construct**: Human sigma-2 receptor (TMEM97) with N-terminal purification tag

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
      <td>Baculovirus expression in Sf9 insect cells</td>
      <td>—</td>
      <td>Not specified</td>
      <td>Expressed using baculovirus system</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>Buffer containing <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> and <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Protein solubilized in <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/CHS mixed micelles</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Affinity purification</td>
      <td>—</td>
      <td>Standard purification buffer with <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/CHS</td>
      <td>Purified via affinity tag, followed by size-exclusion chromatography</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>—</td>
      <td>SEC buffer with <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/CHS</td>
      <td>Final purification step; protein concentrated for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified sigma-2 receptor in <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/CHS</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structures determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a>. Three distinct structures obtained
with different ligands: PB28 (agonist), Roluperidone (antagonist), and <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a>.
The structures enabled large-scale docking-based virtual screening that identified
novel sigma-2 ligands with nanomolar potency.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m93">7M93</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPGGSSMGT</span><span class="topo-outside">LGA</span><span class="topo-membrane">RRGLEWFLGFYFLSHIPITLLMDLQGVLPRD</span><span class="topo-inside">LYPVELRNLQQWYIEEFKDPLLQTP</span><span class="topo-membrane">PAWFKSFLFCELVFQLPFFPIAAYAFF</span><span class="topo-outside">KGGCKWI</span><span class="topo-membrane">RTPAIIYSVHTMTTLIPI</span></span>
<span class="topo-ruler">       130       140       150       160       170    </span>
<span class="topo-line"><span class="topo-membrane">LSTLLL</span><span class="topo-inside">DDFSKASHFRGQGPKTFQ</span><span class="topo-membrane">ERLFLISVYIPYFLIPLILLLFMVR</span><span class="topo-outside">NPYYK</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>-5</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>12</td>
      <td>4</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>43</td>
      <td>7</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>68</td>
      <td>38</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>95</td>
      <td>63</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>102</td>
      <td>90</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>126</td>
      <td>97</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>144</td>
      <td>121</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>169</td>
      <td>139</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>174</td>
      <td>164</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m93">7M93</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPGGSSMG</span><span class="topo-outside">TLGA</span><span class="topo-membrane">RRGLEWFLGFYFLSHIPITLLMDLQGVLPRD</span><span class="topo-inside">LYPVELRNLQQWYIEEFKDPLLQTP</span><span class="topo-membrane">PAWFKSFLFCELVFQLPFFPIAAYAFF</span><span class="topo-outside">KGGCKW</span><span class="topo-membrane">IRTPAIIYSVHTMTTLIPI</span></span>
<span class="topo-ruler">       130       140       150       160       170    </span>
<span class="topo-line"><span class="topo-membrane">LSTLLL</span><span class="topo-inside">DDFSKASHFRGQGPKTFQER</span><span class="topo-membrane">LFLISVYIPYFLIPLILLLFMVR</span><span class="topo-outside">NPYY</span><span class="topo-unknown">K</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>8</td>
      <td>-5</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>12</td>
      <td>3</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>43</td>
      <td>7</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>68</td>
      <td>38</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>95</td>
      <td>63</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>101</td>
      <td>90</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>126</td>
      <td>96</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>146</td>
      <td>121</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>169</td>
      <td>141</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>173</td>
      <td>164</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>174</td>
      <td>168</td>
      <td>168</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m93">7M93</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPGGSSMGT</span><span class="topo-outside">LGA</span><span class="topo-membrane">RRGLEWFLGFYFLSHIPITLLMDLQGVLPRD</span><span class="topo-inside">LYPVELRNLQQWYIEEFKDPLLQTP</span><span class="topo-membrane">PAWFKSFLFCELVFQLPFFPIAAYAFF</span><span class="topo-outside">KGGCKWI</span><span class="topo-membrane">RTPAIIYSVHTMTTLIPI</span></span>
<span class="topo-ruler">       130       140       150       160       170    </span>
<span class="topo-line"><span class="topo-membrane">LSTLLL</span><span class="topo-inside">DDFSKASHFRGQGPKTFQ</span><span class="topo-membrane">ERLFLISVYIPYFLIPLILLLFMVR</span><span class="topo-outside">NPYYK</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>-5</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>12</td>
      <td>4</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>43</td>
      <td>7</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>68</td>
      <td>38</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>95</td>
      <td>63</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>102</td>
      <td>90</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>126</td>
      <td>97</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>144</td>
      <td>121</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>169</td>
      <td>139</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>174</td>
      <td>164</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m93">7M93</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPGGSSMG</span><span class="topo-outside">TLGA</span><span class="topo-membrane">RRGLEWFLGFYFLSHIPITLLMDLQGVLPRD</span><span class="topo-inside">LYPVELRNLQQWYIEEFKDPLLQTP</span><span class="topo-membrane">PAWFKSFLFCELVFQLPFFPIAAYAFF</span><span class="topo-outside">KGGCKW</span><span class="topo-membrane">IRTPAIIYSVHTMTTLIPI</span></span>
<span class="topo-ruler">       130       140       150       160       170    </span>
<span class="topo-line"><span class="topo-membrane">LSTLLL</span><span class="topo-inside">DDFSKASHFRGQGPKTFQER</span><span class="topo-membrane">LFLISVYIPYFLIPLILLLFMVR</span><span class="topo-outside">NPYY</span><span class="topo-unknown">K</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>8</td>
      <td>-5</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>12</td>
      <td>3</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>43</td>
      <td>7</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>68</td>
      <td>38</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>95</td>
      <td>63</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>101</td>
      <td>90</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>126</td>
      <td>96</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>146</td>
      <td>121</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>169</td>
      <td>141</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>173</td>
      <td>164</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>174</td>
      <td>168</td>
      <td>168</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m93">7M93</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPGGSSMGT</span><span class="topo-outside">LGA</span><span class="topo-membrane">RRGLEWFLGFYFLSHIPITLLMDLQGVLPRD</span><span class="topo-inside">LYPVELRNLQQWYIEEFKDPLLQTP</span><span class="topo-membrane">PAWFKSFLFCELVFQLPFFPIAAYAFF</span><span class="topo-outside">KGGCKWI</span><span class="topo-membrane">RTPAIIYSVHTMTTLIPI</span></span>
<span class="topo-ruler">       130       140       150       160       170    </span>
<span class="topo-line"><span class="topo-membrane">LSTLLL</span><span class="topo-inside">DDFSKASHFRGQGPKTFQ</span><span class="topo-membrane">ERLFLISVYIPYFLIPLILLLFMVR</span><span class="topo-outside">NPYYK</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>-5</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>12</td>
      <td>4</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>43</td>
      <td>7</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>68</td>
      <td>38</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>95</td>
      <td>63</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>102</td>
      <td>90</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>126</td>
      <td>97</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>144</td>
      <td>121</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>169</td>
      <td>139</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>174</td>
      <td>164</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m93">7M93</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPGGSSMG</span><span class="topo-outside">TLGA</span><span class="topo-membrane">RRGLEWFLGFYFLSHIPITLLMDLQGVLPRD</span><span class="topo-inside">LYPVELRNLQQWYIEEFKDPLLQTP</span><span class="topo-membrane">PAWFKSFLFCELVFQLPFFPIAAYAFF</span><span class="topo-outside">KGGCKW</span><span class="topo-membrane">IRTPAIIYSVHTMTTLIPI</span></span>
<span class="topo-ruler">       130       140       150       160       170    </span>
<span class="topo-line"><span class="topo-membrane">LSTLLL</span><span class="topo-inside">DDFSKASHFRGQGPKTFQER</span><span class="topo-membrane">LFLISVYIPYFLIPLILLLFMVR</span><span class="topo-outside">NPYY</span><span class="topo-unknown">K</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>8</td>
      <td>-5</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>12</td>
      <td>3</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>43</td>
      <td>7</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>68</td>
      <td>38</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>95</td>
      <td>63</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>101</td>
      <td>90</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>126</td>
      <td>96</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>146</td>
      <td>121</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>169</td>
      <td>141</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>173</td>
      <td>164</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>174</td>
      <td>168</td>
      <td>168</td>
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

### Novel four-helix bundle architecture

The sigma-2 receptor adopts a novel four-helix bundle fold with an intramembrane
ligand-binding pocket, distinct from any previously characterized [GPCR](/xray-mp-wiki/concepts/gpcr/) or
membrane protein fold. The binding pocket is completely buried within the
transmembrane region.

### Ligand recognition and docking-based discovery

The three structures reveal how diverse ligands (agonists, antagonists, and
[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/)) bind to the sigma-2 receptor. The structures enabled successful
retrospective docking validation followed by prospective virtual screening of
a large compound library, yielding potent and selective sigma-2 ligands that
showed efficacy in a mouse model of neuropathic pain.


## Cross-References

- <a href="/xray-mp-wiki/proteins/receptors-signaling/sigma-1-receptor/">Human Sigma-1 Receptor (SIGMAR1)</a> — Related sigma receptor family member with distinct pharmacology and fold
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — Primary detergent for solubilization and purification
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/cupin-fold/">Cupin Fold</a> — Sigma-2 receptor adopts a four-helix bundle distinct from cupin fold of sigma-1
