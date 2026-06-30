---
title: "ECF-FoIT Energy-Coupling Factor Transporter for Folate from Lactobacillus delbrueckii"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms11072]
verified: false
---

# ECF-FoIT Energy-Coupling Factor Transporter for Folate from Lactobacillus delbrueckii

## Overview

ECF-FoIT is a group II energy-coupling factor (ECF) transporter from Lactobacillus delbrueckii that mediates high-affinity uptake of folate. The transporter consists of the S-component FolT (which binds and transports folate) and the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module (EcfA, EcfA', and EcfT) that energizes transport via  hydrolysis. Crystal structures of solitary FolT1 in the folate-bound state (3.01 A), and of the complete ECF-FoIT2 complex in both the apo (3.00 A) and -bound (3.30 A) states, reveal the structural basis of the toppling transport mechanism. The S-component topples in the membrane to alternately expose its binding site to the extracellular side (outward-facing) or the cytosolic side (inward-facing, captured in the complex). Association with the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module allosterically disrupts the high-affinity folate-binding site, allowing substrate release into the cytosol.


## Publications

### doi/10.1038##ncomms11072

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5d0y">5D0Y</a></td>
      <td>3.01</td>
      <td>C121</td>
      <td>Solitary FolT1 (folate-bound)</td>
      <td>folate</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5d3m">5D3M</a></td>
      <td>3.30</td>
      <td>P1</td>
      <td>ECF-FoIT2 complex (-bound)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5d7t">5D7T</a></td>
      <td>3.00</td>
      <td>P1</td>
      <td>ECF-FoIT2 complex (apo)</td>
      <td>none (apo)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli MC1061 with p2BAD vector; arabinose induction at 25 C for 3 h
- **Construct**: ECF-FoIT1/2: N-terminal His10-tag on EcfA, C-terminal StrepII-tag on FolT1/2; solitary FolT1/2: N-terminal His10-tag in L. lactis NZ9000

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5d0y">5D0Y</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">HHHHHHHHMKSESKVSSKLE</span><span class="topo-outside">LRELV</span><span class="topo-membrane">LLAMVIAIKVVLGQFK</span><span class="topo-inside">VGDATL</span><span class="topo-membrane">QVGLGFIGSVMLGY</span><span class="topo-outside">LFGPWWG</span><span class="topo-membrane">FAGGALSDLVSSAIFGN</span><span class="topo-inside">LGGF</span><span class="topo-membrane">FIGFTLTAALESMIY</span><span class="topo-outside">GFFLYKKPIQIWRV</span><span class="topo-membrane">IA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180    </span>
<span class="topo-line"><span class="topo-membrane">SVICVTVICYIGLNTLWVSM</span><span class="topo-inside">LGGTN</span><span class="topo-unknown">FMVALSSR</span><span class="topo-membrane">ILKEMITPWIHMVVVWFILEGL</span><span class="topo-unknown">SRVKLSRKF</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>21</td>
      <td>25</td>
      <td>13</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>41</td>
      <td>18</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>47</td>
      <td>34</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>61</td>
      <td>40</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>68</td>
      <td>54</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>85</td>
      <td>61</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>89</td>
      <td>78</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>104</td>
      <td>82</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>118</td>
      <td>97</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>140</td>
      <td>111</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>145</td>
      <td>133</td>
      <td>137</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>153</td>
      <td>138</td>
      <td>145</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>154</td>
      <td>175</td>
      <td>146</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5d0y">5D0Y</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">HHHHHHHHMKSESKVSSKLE</span><span class="topo-outside">LRELV</span><span class="topo-membrane">LLAMVIAIKVVLGQFK</span><span class="topo-inside">VGDATL</span><span class="topo-membrane">QVGLGFIGSVMLG</span><span class="topo-outside">YLFGPWWG</span><span class="topo-membrane">FAGGALSDLVSSAIFGN</span><span class="topo-inside">LGGF</span><span class="topo-membrane">FIGFTLTAALESMIY</span><span class="topo-outside">GFFLYKKPIQIWRV</span><span class="topo-membrane">IA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180    </span>
<span class="topo-line"><span class="topo-membrane">SVICVTVICYIGLNTLWVSM</span><span class="topo-inside">LGGTN</span><span class="topo-unknown">FMVALSSR</span><span class="topo-membrane">ILKEMITPWIHMVVVWFILEGL</span><span class="topo-unknown">SRVKLSRKF</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>21</td>
      <td>25</td>
      <td>13</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>41</td>
      <td>18</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>47</td>
      <td>34</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>60</td>
      <td>40</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>68</td>
      <td>53</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>85</td>
      <td>61</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>89</td>
      <td>78</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>104</td>
      <td>82</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>118</td>
      <td>97</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>140</td>
      <td>111</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>145</td>
      <td>133</td>
      <td>137</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>153</td>
      <td>138</td>
      <td>145</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>154</td>
      <td>175</td>
      <td>146</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5d3m">5D3M</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHHHGENLYFQ</span><span class="topo-outside">GSDNIISFDHVTFTYPDSPRPALSDLSFAIERGSWTALIGHNGSGKSTVSKLINGLLAPDDLDKSSITVDGVKLGADTVWEVREKVGIVFQNPDNQFVGATV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SDDVAFGLENRAVPRPEMLKIVAQAVADVGMADYADSEPSNLSGGQKQRVAIAGILAVKPQVIILDESTSMLDPEGKEQILDLVRKIKEDNNLTVISITHDLEEAAGADQVLVLDDGQLL</span></span>
<span class="topo-ruler">       250       260       270       280       290        </span>
<span class="topo-line"><span class="topo-outside">DQGKPEEIFPKVEMLKRIGLDIPFVYRLKQLLKERGIVLPDEIDDDEKLVQSLWQLNS</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>19</td>
      <td>298</td>
      <td>1</td>
      <td>280</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5d3m">5D3M</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AIKFENVSYVYSPGSPLEAIGLDQLNFSLEEGKFIALVGHTGSGKSTLMQHFNALLKPTSGKIEIAGYTITPETGNKGLKDLRRKVSLAFQFSEAQLFENTVLKDVEYGPRNFGFSEDE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">AREAALKWLKKVGLKDDLIEHSPFDLSGGQMRRVALAGVLAYEPEIICLDEPAAGLDPMGRLEMMQLFKDYQAAGHTVILVTHNMDDVADYADDVLALEHGRLIKHASPKEVFKDSEWLQ</span></span>
<span class="topo-ruler">       250       260       270       280       </span>
<span class="topo-line"><span class="topo-outside">KHHLAEPRSARFAAKLEAAGLKLPGQPLTMPELADAIKQSLK</span><span class="topo-unknown">GGEHE</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>2</td>
      <td>282</td>
      <td>2</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5d3m">5D3M</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKSESKV</span><span class="topo-outside">SSKLELRELVLLAMVIAIKVILGQFKVGNATLQVGLGFIGSVMLGYLFGPWWGFAGGALSDLVSSVIFGNLGGFFIG</span><span class="topo-unknown">FTLTAALGPMIYGFFL</span><span class="topo-outside">YKQPIQIWRVIASVICVTVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180    </span>
<span class="topo-line"><span class="topo-outside">CNI</span><span class="topo-unknown">GLNTLWVSMMYGINFMVALSSRI</span><span class="topo-outside">LKEMITPWIQMVAVWFILEGLSRVKLSRK</span><span class="topo-unknown">FWSHPQFEK</span></span>
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
      <td>8</td>
      <td>84</td>
      <td>8</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>100</td>
      <td>85</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>101</td>
      <td>123</td>
      <td>101</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>146</td>
      <td>124</td>
      <td>146</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>147</td>
      <td>175</td>
      <td>147</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5d3m">5D3M</a> — Chain D (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKII</span><span class="topo-outside">IGRYLPGTTFVYRVDPRAKLL</span><span class="topo-membrane">TTFYFIIMIFLANNW</span><span class="topo-inside">V</span><span class="topo-membrane">SYLVISIFGLAYVFA</span><span class="topo-outside">TGLKA</span><span class="topo-unknown">RVFWDGV</span><span class="topo-outside">KPMI</span><span class="topo-membrane">WMIVFTSLLQTFFM</span><span class="topo-inside">AGGKVYWHWWIFTLSSEG</span><span class="topo-membrane">LINGLYVFIRFAMII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-outside">STVMTVTTKPLEIADAME</span><span class="topo-unknown">WMLTPL</span><span class="topo-outside">KLFKVNVGMISLVISIALRFVPTLFDQTVKIMNAQRSRGADFNDGGLVKRAKSVVPMLVPLFIDSLEVALDLSTAMESRGYKGSEGRTRYRILE</span></span>
<span class="topo-ruler">       250       260     </span>
<span class="topo-line"><span class="topo-outside">WSKVD</span><span class="topo-membrane">LIPVAYCLLLTILMI</span><span class="topo-inside">TTRK</span><span class="topo-unknown">H</span></span>
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
      <td>6</td>
      <td>26</td>
      <td>6</td>
      <td>26</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>41</td>
      <td>27</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>42</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>57</td>
      <td>43</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>62</td>
      <td>58</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>69</td>
      <td>63</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>70</td>
      <td>73</td>
      <td>70</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>87</td>
      <td>74</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>88</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>122</td>
      <td>106</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>140</td>
      <td>123</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>146</td>
      <td>141</td>
      <td>146</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>147</td>
      <td>245</td>
      <td>147</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>260</td>
      <td>246</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>264</td>
      <td>261</td>
      <td>264</td>
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

### Toppling mechanism for substrate transport

The S-component FolT undergoes a dramatic reorientation in the membrane, rotating approximately 90 degrees so that its six transmembrane helices lie roughly parallel to the membrane plane in the toppled state. This movement alternately exposes the folate-binding site to the extracellular side for substrate capture (outward-facing) or to the cytosolic side for substrate release (inward-facing, post-translocation state). The toppled state is captured in the crystal structures of the full ECF-FoIT2 complex.

### Allosteric disruption of the folate-binding site by ECF module binding

In solitary FolT1, folate is bound with high affinity in a binding site formed by loops L1 and L3. When FolT docks onto the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module via complementary hydrophobic surfaces (the coupling helices of EcfT form a hydrophobic platform that binds helices 1 and 3 of FolT), loops L1 and L3 are displaced because they would sterically clash with TMH3 of EcfT at the conserved P71 position. This displacement disrupts the folate-binding site, allowing substrate release into the cytosol. High-affinity folate binding and [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module interaction are mutually exclusive.

### Transport cycle model and competition among S-components

The working model proposes: (1)  binding drives release of the empty S-component from the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module by disrupting the hydrophobic interface. (2) The solitary S-component reorients to an outward-facing state and binds substrate from the extracellular side. (3)  hydrolysis resets the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module. (4) Substrate-bound S-components have an intrinsic ability to topple spontaneously and are trapped by the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module's binding platform, which simultaneously destroys the binding site and releases substrate. Substrate-loaded S-components out-compete empty ones for [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module binding, explaining the preferential transport of scarce nutrients. The [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module exhibits high futile ATPase activity characteristic of this transporter family.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/amp-pnp/">Amp Pnp</a> — Referenced in ecf-foit-lactobacillus-delbrueckii text
- <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> — Referenced in ecf-foit-lactobacillus-delbrueckii text
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/">ECF (Energy Coupling Factor) Transporter Family</a> — Referenced in ecf-foit-lactobacillus-delbrueckii text
