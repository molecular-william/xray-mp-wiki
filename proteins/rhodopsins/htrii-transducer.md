---
title: "HtrII Transducer (Sensory Rhodopsin II Transducer)"
created: 2026-06-11
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NATURE01109]
verified: false
---

# HtrII Transducer (Sensory Rhodopsin II Transducer)

## Overview

HtrII (Halobacterial transducer for sensory rhodopsin II) is the cognate
transmembrane transducer protein that forms a tight complex with sensory
rhodopsin II (NpSRII) from Natronobacterium pharaonis. HtrII mediates
phototaxis signal transduction by coupling light activation of SRII to a
downstream two-component signalling cascade homologous to eubacterial
chemotaxis. The transducer contains two transmembrane helices (TM1, TM2)
and a cytoplasmic domain that interacts with CheA-like histidine kinases.
A truncated construct comprising residues 1-114 (HtrII_114) retains the
two TM helices and a short cytoplasmic fragment and forms a functionally
unimpaired complex with SRII.


## Publications

### doi/10.1038##NATURE01109

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1h2s">1H2S</a></td>
      <td>1.94</td>
      <td>Orthorhombic</td>
      <td>HtrII_114 (residues 1-114, C-terminal truncated) in complex with NpSRII</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21 (DE3)
- **Construct**: C-terminal 7x His-tagged HtrII_114 (residues 1-114)
- **Notes**: Co-expressed and co-purified with NpSRII

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
      <td>Affinity purification</td>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td>Imidazole-containing buffer</td>
      <td>His-tagged HtrII_114 purified via C-terminal His tag</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a></td>
      <td>DEAE chromatography</td>
      <td>—</td>
      <td>Buffer with 2% n-octyl-beta-D-glucopyranoside</td>
      <td>Imidazol removed by DEAE chromatography before complex formation</td>
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
      <td>NpSRII-HtrII_114 complex (1:1 ratio) reconstituted into H. salinarum polar lipids</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monovacccin</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Thin orange orthorhombic crystals ~140 um. Complex solubilized in 2% n-octyl-beta-D-glucopyranoside, 150 mM NaCl, 25 mM Na/KPi pH 5.1. Data collected at ESRF beamline ID14-1.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1h2s">1H2S</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MVGL</span><span class="topo-membrane">TTLFWLGAIGMLVGTLAFA</span><span class="topo-inside">WAGRDAGSGERRYYV</span><span class="topo-membrane">TLVGISGIAAVAYVVMAL</span><span class="topo-outside">GVGWVPVAERTVF</span><span class="topo-membrane">APRYIDWILTTPLIVY</span><span class="topo-inside">FLGLLAGLDSREFG</span><span class="topo-membrane">IVITLNTVVMLAGFAGA</span><span class="topo-outside">MVPG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-outside">IER</span><span class="topo-membrane">YALFGMGAVAFLGLVYY</span><span class="topo-inside">LVGPMTESASQRSSGIKSLYVRLRN</span><span class="topo-membrane">LTVILWAIYPFIWLLG</span><span class="topo-outside">PPGVALLTPT</span><span class="topo-membrane">VDVALIVYLDLVTKVGFGF</span><span class="topo-inside">IALDAAATLRAEHGE</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>23</td>
      <td>5</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>38</td>
      <td>24</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>56</td>
      <td>39</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>69</td>
      <td>57</td>
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
      <td>99</td>
      <td>86</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>116</td>
      <td>100</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>123</td>
      <td>117</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>140</td>
      <td>124</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>181</td>
      <td>166</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>191</td>
      <td>182</td>
      <td>191</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>210</td>
      <td>192</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>225</td>
      <td>211</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1h2s">1H2S</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-inside">G</span><span class="topo-membrane">AVFIFVGALTVLFGAIA</span><span class="topo-outside">YGEVTAAAATGDAAAVQEAAVS</span><span class="topo-membrane">AILGLIILLGINLGLVAA</span><span class="topo-inside">TL</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>1</td>
      <td>23</td>
      <td>23</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>18</td>
      <td>24</td>
      <td>40</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>40</td>
      <td>41</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>58</td>
      <td>63</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>60</td>
      <td>81</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1h2s">1H2S</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MVGL</span><span class="topo-membrane">TTLFWLGAIGMLVGTLAFA</span><span class="topo-inside">WAGRDAGSGERRYYV</span><span class="topo-membrane">TLVGISGIAAVAYVVMAL</span><span class="topo-outside">GVGWVPVAERTVF</span><span class="topo-membrane">APRYIDWILTTPLIVY</span><span class="topo-inside">FLGLLAGLDSREFG</span><span class="topo-membrane">IVITLNTVVMLAGFAGA</span><span class="topo-outside">MVPG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-outside">IER</span><span class="topo-membrane">YALFGMGAVAFLGLVYY</span><span class="topo-inside">LVGPMTESASQRSSGIKSLYVRLRN</span><span class="topo-membrane">LTVILWAIYPFIWLLG</span><span class="topo-outside">PPGVALLTPT</span><span class="topo-membrane">VDVALIVYLDLVTKVGFGF</span><span class="topo-inside">IALDAAATLRAEHGE</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>23</td>
      <td>5</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>38</td>
      <td>24</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>56</td>
      <td>39</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>69</td>
      <td>57</td>
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
      <td>99</td>
      <td>86</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>116</td>
      <td>100</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>123</td>
      <td>117</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>140</td>
      <td>124</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>181</td>
      <td>166</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>191</td>
      <td>182</td>
      <td>191</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>210</td>
      <td>192</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>225</td>
      <td>211</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1h2s">1H2S</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-inside">G</span><span class="topo-membrane">AVFIFVGALTVLFGAIA</span><span class="topo-outside">YGEVTAAAATGDAAAVQEAAVS</span><span class="topo-membrane">AILGLIILLGINLGLVAA</span><span class="topo-inside">TL</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>1</td>
      <td>23</td>
      <td>23</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>18</td>
      <td>24</td>
      <td>40</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>40</td>
      <td>41</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>58</td>
      <td>63</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>60</td>
      <td>81</td>
      <td>82</td>
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

### SRII-HtrII complex structure reveals signal transduction interface

The 1.94 A structure of the NpSRII-HtrII_114 complex reveals how the
transducer TM1 and TM2 helices pack against receptor helices F and G.
The complex forms a dimer along a crystallographic two-fold axis with
TM1-TM2 TM1'-TM2' packing. The transducer extends ~3 helical turns
beyond the extracellular side (residues 44-59), a structural element
absent in HtrI but present in H. salinarum HtrII. High B-factors at
the cytoplasmic ends indicate conformational flexibility essential for
signal transduction. The structure supports a mechanism where light-
induced outward motion of SRII helix F triggers a clockwise rotation
of TM2, which propagates the signal to the downstream CheA/CheY
two-component cascade.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/sensory-rhodopsin-ii/">Sensory Rhodopsin II (NpSRII)</a> — HtrII forms a tight complex with NpSRII and mediates phototaxis signal transduction
- <a href="/xray-mp-wiki/concepts/signaling-receptors/two-component-signaling-system/">Two-Component Signaling System (TCS) in Membrane Sensors</a> — HtrII links SRII photoactivation to the CheA/CheY two-component signalling cascade
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a> — Method used in structure determination or purification
