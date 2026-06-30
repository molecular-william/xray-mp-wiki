---
title: "RsTSPO Translocator Protein from Rhodobacter sphaeroides"
created: 2026-06-10
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1126##science.1260590]
verified: false
---

# RsTSPO Translocator Protein from Rhodobacter sphaeroides

## Overview

The 18-kDa translocator protein (TSPO) from *Rhodobacter sphaeroides* (RsTSPO) is a bacterial homolog of the mammalian TSPO, a key player in [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) transport into mitochondria and a major target for diagnostic imaging and therapeutic intervention. Crystal structures were determined at 1.8-2.5 Å resolution for wild-type and the A139T mutant (mimicking the human A147T polymorphism associated with psychiatric disorders). All structures show a tightly interacting parallel dimer formed by five-transmembrane-helix monomers. The A139T mutation causes conformational changes in TM-II and TM-V that alter the [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) recognition consensus sequence (CRAC) site and reduce ligand binding affinity. An endogenous porphyrin ligand is bound in a cavity between TM-I and TM-II, and an external surface transport mechanism is proposed.


## Publications

### doi/10.1126##science.1260590

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4uc3">4UC3</a></td>
      <td>2.5</td>
      <td>P2₁</td>
      <td>Wild-type RsTSPO</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4uc1">4UC1</a></td>
      <td>1.8</td>
      <td>C2</td>
      <td>A139T mutant</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4uc2">4UC2</a></td>
      <td>2.4</td>
      <td>P2₁2₁2₁</td>
      <td>A139T mutant</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: RsTSPO wild-type and A139T mutant

**Purification:**

- **Expression system**: E. coli

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
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Purified RsTSPO used for ligand binding studies and crystallization</td>
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
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained in three different space groups. <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> and <a href="/xray-mp-wiki/reagents/ligands/pk11195/">PK11195</a> added to crystallization medium improved crystal quality but were not resolved in the electron density.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4uc3">4UC3</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MDW</span><span class="topo-membrane">ALFLTFLAACGAPATTGA</span><span class="topo-inside">LLKPD</span><span class="topo-unknown">EWYDNLNKPWWN</span><span class="topo-inside">PPRW</span><span class="topo-membrane">VFPLAWTSLYFLMSLAAM</span><span class="topo-outside">RVAQLEGSG</span><span class="topo-membrane">QALAFYAAQLAFNTLWT</span><span class="topo-inside">PVFFGMKRMAT</span><span class="topo-membrane">ALAVVMVMWLFVAATMWAFF</span><span class="topo-outside">QLD</span></span>
<span class="topo-ruler">       130       140       150     </span>
<span class="topo-line"><span class="topo-outside">TW</span><span class="topo-membrane">AGVLFVPYLIWATAATGLNF</span><span class="topo-inside">EAMRLNWNRPEAR</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>21</td>
      <td>6</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>26</td>
      <td>24</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>42</td>
      <td>41</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>69</td>
      <td>63</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>86</td>
      <td>72</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>97</td>
      <td>89</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>117</td>
      <td>100</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>122</td>
      <td>120</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>123</td>
      <td>142</td>
      <td>125</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>155</td>
      <td>145</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4uc3">4UC3</a> — Chain B (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MDW</span><span class="topo-membrane">ALFLTFLAACGAPATTGA</span><span class="topo-inside">LLKPD</span><span class="topo-unknown">EWYDNLNKPWWN</span><span class="topo-inside">PPRW</span><span class="topo-membrane">VFPLAWTSLYFLMSLAAM</span><span class="topo-outside">RVAQLEGSG</span><span class="topo-membrane">QALAFYAAQLAFNTLWTP</span><span class="topo-inside">VFFGMKRMAT</span><span class="topo-membrane">ALAVVMVMWLFVAATMWAFF</span><span class="topo-outside">QLD</span></span>
<span class="topo-ruler">       130       140       150     </span>
<span class="topo-line"><span class="topo-outside">TW</span><span class="topo-membrane">AGVLFVPYLIWATAATGLNF</span><span class="topo-inside">EA</span><span class="topo-unknown">MRLNWNRPEAR</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>21</td>
      <td>6</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>26</td>
      <td>24</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>42</td>
      <td>41</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>69</td>
      <td>63</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>72</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>97</td>
      <td>90</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>117</td>
      <td>100</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>122</td>
      <td>120</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>123</td>
      <td>142</td>
      <td>125</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>144</td>
      <td>145</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4uc1">4UC1</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MNM</span><span class="topo-membrane">DWALFLTFLAACGAPATTGAL</span><span class="topo-inside">LKPDEWYDNLNKPWW</span><span class="topo-membrane">NPPRWVFPLAWTSLYFLMSLAAMRVA</span><span class="topo-outside">QLEGSG</span><span class="topo-membrane">QALAFYAAQLAFNTLWTPVF</span><span class="topo-inside">FGMKRMA</span><span class="topo-membrane">TALAVVMVMWLFVAATMWAFF</span><span class="topo-outside">Q</span></span>
<span class="topo-ruler">       130       140       150       </span>
<span class="topo-line"><span class="topo-outside">LDT</span><span class="topo-membrane">WAGVLFVPYLIWATATTGLNFE</span><span class="topo-inside">AMRLNWNRPEAR</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>24</td>
      <td>4</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>39</td>
      <td>25</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>65</td>
      <td>40</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>71</td>
      <td>66</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>91</td>
      <td>72</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>119</td>
      <td>99</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>123</td>
      <td>120</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>145</td>
      <td>124</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>157</td>
      <td>146</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4uc1">4UC1</a> — Chain B (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">NMD</span><span class="topo-membrane">WALFLTFLAACGAPATTGALLK</span><span class="topo-inside">PDEWYDNLNKP</span><span class="topo-membrane">WWNPPRWVFPLAWTSLYFLMSLAAMRVA</span><span class="topo-outside">QLEGSG</span><span class="topo-membrane">QALAFYAAQLAFNTLWTPVF</span><span class="topo-inside">FGMKRM</span><span class="topo-membrane">ATALAVVMVMWLFVAATMWAFF</span><span class="topo-outside">Q</span></span>
<span class="topo-ruler">       130       140       150       </span>
<span class="topo-line"><span class="topo-outside">LDTW</span><span class="topo-membrane">AGVLFVPYLIWATATTGLNFE</span><span class="topo-inside">AMRLNWNRPEAR</span></span>
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
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>26</td>
      <td>5</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>37</td>
      <td>27</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>65</td>
      <td>38</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>71</td>
      <td>66</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>91</td>
      <td>72</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>97</td>
      <td>92</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>119</td>
      <td>98</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>124</td>
      <td>120</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>157</td>
      <td>146</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4uc2">4UC2</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">NMDW</span><span class="topo-membrane">ALFLTFLAACGAPATTGAL</span><span class="topo-outside">LKPDEWYDNLNKPWW</span><span class="topo-membrane">NPPRWVFPLAWTSLYFLMSLAAM</span><span class="topo-inside">RVAQLEGSG</span><span class="topo-membrane">QALAFYAAQLAFNTLWTPVF</span><span class="topo-outside">FGMKRMA</span><span class="topo-membrane">TALAVVMVMWLFVAATMWAFF</span><span class="topo-inside">QL</span></span>
<span class="topo-ruler">       130       140       150      </span>
<span class="topo-line"><span class="topo-inside">DTW</span><span class="topo-membrane">AGVLFVPYLIWATATTGLNFE</span><span class="topo-outside">AMRLNWNRPEAR</span></span>
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
      <td>4</td>
      <td>2</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>23</td>
      <td>6</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>38</td>
      <td>25</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>61</td>
      <td>40</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>70</td>
      <td>63</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>90</td>
      <td>72</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>97</td>
      <td>92</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>118</td>
      <td>99</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>123</td>
      <td>120</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>144</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>156</td>
      <td>146</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4uc2">4UC2</a> — Chain B (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">N</span><span class="topo-inside">MDW</span><span class="topo-membrane">ALFLTFLAACGAPATTGAL</span><span class="topo-outside">LKPDEWYDNLNKPWW</span><span class="topo-membrane">NPPRWVFPLAWTSLYFLMSLAAM</span><span class="topo-inside">RVAQLEGSG</span><span class="topo-membrane">QALAFYAAQLAFNTLWTPVF</span><span class="topo-outside">FGMKRMA</span><span class="topo-membrane">TALAVVMVMWLFVAATMWAFF</span><span class="topo-inside">QL</span></span>
<span class="topo-ruler">       130       140       150      </span>
<span class="topo-line"><span class="topo-inside">DTW</span><span class="topo-membrane">AGVLFVPYLIWATATTGLNFE</span><span class="topo-outside">AMRLNWNRPEAR</span></span>
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
      <td>2</td>
      <td>4</td>
      <td>3</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>23</td>
      <td>6</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>38</td>
      <td>25</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>61</td>
      <td>40</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>70</td>
      <td>63</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>90</td>
      <td>72</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>97</td>
      <td>92</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>118</td>
      <td>99</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>123</td>
      <td>120</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>144</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>156</td>
      <td>146</td>
      <td>157</td>
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

### Dimeric architecture with tight interface

RsTSPO forms a stable parallel dimer with a flat interface primarily composed of TM-I and TM-III (~1250 Å², ~15% of monomer surface area). The interface is dominated by alanines and leucines with a G/A-xxx-G/A motif favoring helical dimerization. Five hydrogen bonds at the periphery between TM-I and TM-III anchor the interface. The dimer is unaltered by the A139T mutation.

### A139T mutation alters CRAC site and ligand binding

The A139T mutation (mimicking human A147T) causes TM-II to tilt 7.7° toward TM-V and TM-V to straighten by 6.3°, resulting in closer association of these helices. Side-chain rearrangements of F46, L142, F144, and W135 alter the CRAC motif, reducing binding affinity 4-5 fold for [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/), [PK11195](/xray-mp-wiki/reagents/ligands/pk11195/), and protoporphyrin IX. This provides a molecular basis for the diminished [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) metabolism and altered ligand binding observed in humans carrying the A147T polymorphism.

### Porphyrin as an endogenous ligand

Electron density in the A139T structure between TM-I and TM-II underneath LP1 corresponds to a porphyrin compound that copurifies with the protein. This supports the proposed role of TSPO in porphyrin transport and regulation of the switch between photosynthesis and respiration in R. sphaeroides.

### External surface transport mechanism

The dimeric structure with a tight interface makes an internal pore or transport pathway through the monomer unlikely. Long electron density along surface grooves extending from the porphyrin binding site to the bottom surface of the protein suggests a possible external surface transport mechanism, similar to maltoporin. This would require association with protein partners such as StAR and VDAC.


## Cross-References

- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Primary lipid component of the lipidic cubic phase used for crystallization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/ligands/pk11195/">PK11195</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Additive used in purification or crystallization buffers
