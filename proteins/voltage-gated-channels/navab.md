---
title: "NavAb Bacterial Voltage-Gated Sodium Channel"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein]
sources: [doi/10.1038##nature11077, doi/10.1073##pnas.1700761114, doi/10.1073##pnas.1814928115, doi/10.1038##s41586-018-0120-4, doi/10.1085##jgp.201711884]
verified: false
---

# NavAb Bacterial Voltage-Gated Sodium Channel

## Overview

NavAb is a bacterial voltage-gated sodium channel (BacNav) from Arcobacter butzleri
that serves as a model for vertebrate voltage-gated sodium channels. NavAb forms a
homotetramer of four identical subunits, each with six transmembrane segments (S1-S6).
The landmark wild-type NavAb structure at 3.2 A resolution captured the channel in two potentially slow-inactivated states, revealing an asymmetric dimer-of-dimers S6 activation gate collapse and providing the first structural insights into Nav channel slow inactivation. Using two Na_vAb mutants (Na_vAb/FY: T206F/V213Y and Na_vAb/1-226: C-terminal
[Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/)), additional structures were determined that capture tightly closed and open states
of the activation gate at 2.8-3.2 A resolution, allowing completion of a closed-open-inactivated
conformational cycle in a single voltage-gated sodium channel. Additional high-resolution
structures of NavAb with gating-charge mutations (R2G and R3G) analogous to those
causing periodic paralysis in human Nav1.4 reveal the structural basis of pathogenic
gating pore currents in the voltage sensor domain.


## Publications

### doi/10.1038##nature11077

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ekw">4EKW</a></td>
      <td>3.20</td>
      <td>P4(3)2(1)2</td>
      <td>Wild-type NavAb (full-length), expressed in Trichoplusia ni insect cells, purified via anti-Flag resin + SEC, reconstituted in DMPC:CHAPSO bicelles</td>
      <td>None (apo, potentially slow-inactivated states)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Trichoplusia ni insect cells (Bac-to-Bac baculovirus system)
- **Construct**: Full-length Na_vAb wild-type and mutants
- **Notes**: Na_vAb/FY constructed by site-directed mutagenesis (QuikChange); Na_vAb/1-226 constructed by introduction of stop codon at Lys-227

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Wild-type NavAb at ~20 mg/mL reconstituted in DMPC:CHAPSO bicelles</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>~2 M ammonium sulfate, 100 mM sodium citrate pH 4.75</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>28% glucose (wt/v) in reservoir solution, added in ~6% increments; nicotinic acid at saturating concentration in cryo solution prolonged crystal lifetime</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Over 1,500 crystals screened at ALS (BL8.2.1, BL8.2.2). Most WT crystals did not diffract beyond 3.5 A. Best SAD data from single SeMet-labeled crystal at Se edge (lambda=0.9792 A). Initial rigid-body refinement with NavAb-I217C model stalled at Rfree ~40% due to perfect merohedral twinning. Manual placement into experimentally phased SAD map with PHENIX resolved twinning. S5 gating hinge boundaries defined rigid bodies, leading to immediate ~6% drop in Rfree.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ekw">4EKW</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-inside">M</span><span class="topo-unknown">YLRITNIV</span><span class="topo-inside">ESSFFT</span><span class="topo-membrane">KFIIYLIVLNGITMGLET</span><span class="topo-outside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-outside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-inside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-outside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-inside">SVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMAT</span><span class="topo-outside">QLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-outside">L</span><span class="topo-unknown">GESFYTLFQVMTLESWSMGIVRPLMEV</span><span class="topo-outside">YPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMINLV</span><span class="topo-inside">VAIIVD</span><span class="topo-unknown">AMA</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>19</td>
      <td>1001</td>
      <td>1001</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>27</td>
      <td>1002</td>
      <td>1009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>1010</td>
      <td>1015</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>51</td>
      <td>1016</td>
      <td>1033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>62</td>
      <td>1034</td>
      <td>1044</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>1045</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>1065</td>
      <td>1075</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>1076</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>115</td>
      <td>1092</td>
      <td>1097</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>131</td>
      <td>1098</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>1114</td>
      <td>1124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>1125</td>
      <td>1130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>167</td>
      <td>1131</td>
      <td>1149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>181</td>
      <td>1150</td>
      <td>1163</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>1164</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>208</td>
      <td>1181</td>
      <td>1190</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>209</td>
      <td>211</td>
      <td>1191</td>
      <td>1193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>1194</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>237</td>
      <td>1214</td>
      <td>1219</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>285</td>
      <td>1220</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ekw">4EKW</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-inside">MYL</span><span class="topo-unknown">RITNIV</span><span class="topo-inside">ESSFFTKF</span><span class="topo-membrane">IIYLIVLNGITMGLETS</span><span class="topo-outside">KTFMQSF</span><span class="topo-membrane">G</span></span>
<span class="topo-line"><span class="topo-membrane">VYTTLFNQIVITIFTIEII</span><span class="topo-inside">LRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTSSG</span><span class="topo-outside">F</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVT</span><span class="topo-inside">AV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-inside">SVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-outside">FGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-unknown">LGESFYTLFQVMTLESWS</span><span class="topo-outside">MGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMINLV</span><span class="topo-inside">VAIIVD</span><span class="topo-unknown">AMA</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>21</td>
      <td>1001</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>27</td>
      <td>1004</td>
      <td>1009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>35</td>
      <td>1010</td>
      <td>1017</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>1018</td>
      <td>1034</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>1035</td>
      <td>1041</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>79</td>
      <td>1042</td>
      <td>1061</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>96</td>
      <td>1062</td>
      <td>1078</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>112</td>
      <td>1079</td>
      <td>1094</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>113</td>
      <td>1095</td>
      <td>1095</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>129</td>
      <td>1096</td>
      <td>1111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>131</td>
      <td>1112</td>
      <td>1113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>1114</td>
      <td>1124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>151</td>
      <td>1125</td>
      <td>1133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>1134</td>
      <td>1151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>180</td>
      <td>1152</td>
      <td>1162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>198</td>
      <td>1163</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>211</td>
      <td>1181</td>
      <td>1193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>1194</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>237</td>
      <td>1214</td>
      <td>1219</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>285</td>
      <td>1220</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ekw">4EKW</a> — Chain E (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-inside">M</span><span class="topo-unknown">YLRITNIV</span><span class="topo-inside">ESSFFT</span><span class="topo-membrane">KFIIYLIVLNGITMGLET</span><span class="topo-outside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-outside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-inside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-outside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-inside">SVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMAT</span><span class="topo-outside">QLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-outside">L</span><span class="topo-unknown">GESFYTLFQVMTLESWSMGIVRPLMEV</span><span class="topo-outside">YPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMINLV</span><span class="topo-inside">VAIIVD</span><span class="topo-unknown">AMA</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>19</td>
      <td>1001</td>
      <td>1001</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>27</td>
      <td>1002</td>
      <td>1009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>1010</td>
      <td>1015</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>51</td>
      <td>1016</td>
      <td>1033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>62</td>
      <td>1034</td>
      <td>1044</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>1045</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>1065</td>
      <td>1075</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>1076</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>115</td>
      <td>1092</td>
      <td>1097</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>131</td>
      <td>1098</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>1114</td>
      <td>1124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>1125</td>
      <td>1130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>167</td>
      <td>1131</td>
      <td>1149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>181</td>
      <td>1150</td>
      <td>1163</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>1164</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>208</td>
      <td>1181</td>
      <td>1190</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>209</td>
      <td>211</td>
      <td>1191</td>
      <td>1193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>1194</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>237</td>
      <td>1214</td>
      <td>1219</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>285</td>
      <td>1220</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ekw">4EKW</a> — Chain F (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-inside">MYL</span><span class="topo-unknown">RITNIV</span><span class="topo-inside">ESSFFTKF</span><span class="topo-membrane">IIYLIVLNGITMGLETS</span><span class="topo-outside">KTFMQSF</span><span class="topo-membrane">G</span></span>
<span class="topo-line"><span class="topo-membrane">VYTTLFNQIVITIFTIEII</span><span class="topo-inside">LRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTSSG</span><span class="topo-outside">F</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVT</span><span class="topo-inside">AV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-inside">SVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-outside">FGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-unknown">LGESFYTLFQVMTLESWS</span><span class="topo-outside">MGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMINLV</span><span class="topo-inside">VAIIVD</span><span class="topo-unknown">AMA</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>21</td>
      <td>1001</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>27</td>
      <td>1004</td>
      <td>1009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>35</td>
      <td>1010</td>
      <td>1017</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>1018</td>
      <td>1034</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>1035</td>
      <td>1041</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>79</td>
      <td>1042</td>
      <td>1061</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>96</td>
      <td>1062</td>
      <td>1078</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>112</td>
      <td>1079</td>
      <td>1094</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>113</td>
      <td>1095</td>
      <td>1095</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>129</td>
      <td>1096</td>
      <td>1111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>131</td>
      <td>1112</td>
      <td>1113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>1114</td>
      <td>1124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>151</td>
      <td>1125</td>
      <td>1133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>1134</td>
      <td>1151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>180</td>
      <td>1152</td>
      <td>1162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>198</td>
      <td>1163</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>211</td>
      <td>1181</td>
      <td>1193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>1194</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>237</td>
      <td>1214</td>
      <td>1219</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>285</td>
      <td>1220</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1700761114

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vb2">5VB2</a></td>
      <td>2.80</td>
      <td>P2(1)22(1)</td>
      <td>NavAb/FY (T206F/V213Y double mutant), full-length, homotetramer</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vb2">5VB2</a></td>
      <td>2.85</td>
      <td>—</td>
      <td>NavAb/1-226 (C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> at Lys-227 + I217C mutation)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Trichoplusia ni insect cells (Bac-to-Bac baculovirus system)
- **Construct**: Full-length Na_vAb wild-type and mutants
- **Notes**: Na_vAb/FY constructed by site-directed mutagenesis (QuikChange); Na_vAb/1-226 constructed by introduction of stop codon at Lys-227

**Purification:**

- **Expression system**: Trichoplusia ni insect cells
- **Expression construct**: Full-length Na_vAb with T206F/V213Y mutations (Na_vAb/FY) or C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) to residue 226 (Na_vAb/1-226)

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
      <td>Protein production</td>
      <td>Baculovirus infection of T. ni cells</td>
      <td>—</td>
      <td></td>
      <td>Recombinant baculovirus generated using Bac-to-Bac system (Invitrogen)</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>As described in Payandeh et al. (2012) Nature</td>
      <td>—</td>
      <td></td>
      <td>Protien produced and purified as described in reference 8</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NavAb reconstituted in <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a>:<a href="/xray-mp-wiki/reagents/detergents/chapso/">CHAPSO</a> bicelles</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>1.8 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> pH 4.8</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:2 protein:bicelle mix in hanging drop</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-5 days to appear, ~1 week to full size (~50x100 um)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Slow addition of well solution supplemented with <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> to 30% final</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals highly radiation sensitive; data collected at ALS beamlines BL821 and BL822 at 0.9999-1.1000 Å wavelength</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vb2">5VB2</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGS</span><span class="topo-outside">HMYLRITNIVESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YTTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-unknown">SSGF</span><span class="topo-inside">E</span><span class="topo-membrane">ILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMATQ</span><span class="topo-inside">LFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-unknown">GESFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVFFVMINLY</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSL</span><span class="topo-unknown">KN</span></span>
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
      <td>17</td>
      <td>983</td>
      <td>999</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>32</td>
      <td>1000</td>
      <td>1014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>51</td>
      <td>1015</td>
      <td>1033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>61</td>
      <td>1034</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>82</td>
      <td>1044</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>1065</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>1076</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>113</td>
      <td>1092</td>
      <td>1095</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>114</td>
      <td>114</td>
      <td>1096</td>
      <td>1096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>131</td>
      <td>1097</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>148</td>
      <td>1114</td>
      <td>1130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>168</td>
      <td>1131</td>
      <td>1150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>181</td>
      <td>1151</td>
      <td>1163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>1164</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>211</td>
      <td>1181</td>
      <td>1193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>1194</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>283</td>
      <td>1214</td>
      <td>1265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>1266</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vb2">5VB2</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFT</span><span class="topo-membrane">KFIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YTTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SS</span><span class="topo-unknown">G</span><span class="topo-inside">F</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMATQ</span><span class="topo-inside">LFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-unknown">GESFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVFFVMINLY</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKEL</span><span class="topo-unknown">IKTSLKN</span></span>
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
      <td>18</td>
      <td>1983</td>
      <td>2000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>2001</td>
      <td>2015</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>51</td>
      <td>2016</td>
      <td>2033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>61</td>
      <td>2034</td>
      <td>2043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>82</td>
      <td>2044</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>2076</td>
      <td>2091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>111</td>
      <td>2092</td>
      <td>2093</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>112</td>
      <td>2094</td>
      <td>2094</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>113</td>
      <td>2095</td>
      <td>2095</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>131</td>
      <td>2096</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>148</td>
      <td>2114</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>168</td>
      <td>2131</td>
      <td>2150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>181</td>
      <td>2151</td>
      <td>2163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>2164</td>
      <td>2180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>211</td>
      <td>2181</td>
      <td>2193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>2194</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>278</td>
      <td>2214</td>
      <td>2260</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>285</td>
      <td>2261</td>
      <td>2267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vb2">5VB2</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSHM</span><span class="topo-outside">YLRITNIVESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YTTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPTS</span><span class="topo-unknown">SG</span><span class="topo-inside">FE</span><span class="topo-membrane">ILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-unknown">GESFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVFFVMINLY</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTS</span><span class="topo-unknown">LKN</span></span>
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
      <td>19</td>
      <td>983</td>
      <td>1001</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>32</td>
      <td>1002</td>
      <td>1014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>51</td>
      <td>1015</td>
      <td>1033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>61</td>
      <td>1034</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>82</td>
      <td>1044</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>1065</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>110</td>
      <td>1076</td>
      <td>1092</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>112</td>
      <td>1093</td>
      <td>1094</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>114</td>
      <td>1095</td>
      <td>1096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>131</td>
      <td>1097</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>148</td>
      <td>1114</td>
      <td>1130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>169</td>
      <td>1131</td>
      <td>1151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>181</td>
      <td>1152</td>
      <td>1163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>1164</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>211</td>
      <td>1181</td>
      <td>1193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>1194</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>282</td>
      <td>1214</td>
      <td>1264</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>285</td>
      <td>1265</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vb2">5VB2</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSL</span><span class="topo-outside">VPRGSHMYLRITNIVESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGF</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-unknown">GESFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVFFVMINLY</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIK</span><span class="topo-unknown">TSLKN</span></span>
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
      <td>12</td>
      <td>1983</td>
      <td>1994</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>1995</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>51</td>
      <td>2015</td>
      <td>2033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>62</td>
      <td>2034</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>2076</td>
      <td>2091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>113</td>
      <td>2092</td>
      <td>2095</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>131</td>
      <td>2096</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>148</td>
      <td>2114</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>169</td>
      <td>2131</td>
      <td>2151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>181</td>
      <td>2152</td>
      <td>2163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>2164</td>
      <td>2180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>211</td>
      <td>2181</td>
      <td>2193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>2194</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>280</td>
      <td>2214</td>
      <td>2262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>285</td>
      <td>2263</td>
      <td>2267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vb2">5VB2</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGS</span><span class="topo-outside">HMYLRITNIVESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YTTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-unknown">SSGF</span><span class="topo-inside">E</span><span class="topo-membrane">ILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMATQ</span><span class="topo-inside">LFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-unknown">GESFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVFFVMINLY</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSL</span><span class="topo-unknown">KN</span></span>
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
      <td>17</td>
      <td>983</td>
      <td>999</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>32</td>
      <td>1000</td>
      <td>1014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>51</td>
      <td>1015</td>
      <td>1033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>61</td>
      <td>1034</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>82</td>
      <td>1044</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>1065</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>1076</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>113</td>
      <td>1092</td>
      <td>1095</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>114</td>
      <td>114</td>
      <td>1096</td>
      <td>1096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>131</td>
      <td>1097</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>148</td>
      <td>1114</td>
      <td>1130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>168</td>
      <td>1131</td>
      <td>1150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>181</td>
      <td>1151</td>
      <td>1163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>1164</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>211</td>
      <td>1181</td>
      <td>1193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>1194</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>283</td>
      <td>1214</td>
      <td>1265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>1266</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vb2">5VB2</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFT</span><span class="topo-membrane">KFIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YTTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SS</span><span class="topo-unknown">G</span><span class="topo-inside">F</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMATQ</span><span class="topo-inside">LFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-unknown">GESFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVFFVMINLY</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKEL</span><span class="topo-unknown">IKTSLKN</span></span>
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
      <td>18</td>
      <td>1983</td>
      <td>2000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>2001</td>
      <td>2015</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>51</td>
      <td>2016</td>
      <td>2033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>61</td>
      <td>2034</td>
      <td>2043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>82</td>
      <td>2044</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>2076</td>
      <td>2091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>111</td>
      <td>2092</td>
      <td>2093</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>112</td>
      <td>2094</td>
      <td>2094</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>113</td>
      <td>2095</td>
      <td>2095</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>131</td>
      <td>2096</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>148</td>
      <td>2114</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>168</td>
      <td>2131</td>
      <td>2150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>181</td>
      <td>2151</td>
      <td>2163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>2164</td>
      <td>2180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>211</td>
      <td>2181</td>
      <td>2193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>2194</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>278</td>
      <td>2214</td>
      <td>2260</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>285</td>
      <td>2261</td>
      <td>2267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vb2">5VB2</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSHM</span><span class="topo-outside">YLRITNIVESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YTTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPTS</span><span class="topo-unknown">SG</span><span class="topo-inside">FE</span><span class="topo-membrane">ILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-unknown">GESFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVFFVMINLY</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTS</span><span class="topo-unknown">LKN</span></span>
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
      <td>19</td>
      <td>983</td>
      <td>1001</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>32</td>
      <td>1002</td>
      <td>1014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>51</td>
      <td>1015</td>
      <td>1033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>61</td>
      <td>1034</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>82</td>
      <td>1044</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>1065</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>110</td>
      <td>1076</td>
      <td>1092</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>112</td>
      <td>1093</td>
      <td>1094</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>114</td>
      <td>1095</td>
      <td>1096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>131</td>
      <td>1097</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>148</td>
      <td>1114</td>
      <td>1130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>169</td>
      <td>1131</td>
      <td>1151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>181</td>
      <td>1152</td>
      <td>1163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>1164</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>211</td>
      <td>1181</td>
      <td>1193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>1194</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>282</td>
      <td>1214</td>
      <td>1264</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>285</td>
      <td>1265</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vb2">5VB2</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSL</span><span class="topo-outside">VPRGSHMYLRITNIVESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGF</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-unknown">GESFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVFFVMINLY</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIK</span><span class="topo-unknown">TSLKN</span></span>
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
      <td>12</td>
      <td>1983</td>
      <td>1994</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>1995</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>51</td>
      <td>2015</td>
      <td>2033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>62</td>
      <td>2034</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>2076</td>
      <td>2091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>113</td>
      <td>2092</td>
      <td>2095</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>131</td>
      <td>2096</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>148</td>
      <td>2114</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>169</td>
      <td>2131</td>
      <td>2151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>181</td>
      <td>2152</td>
      <td>2163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>2164</td>
      <td>2180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>211</td>
      <td>2181</td>
      <td>2193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>231</td>
      <td>2194</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>280</td>
      <td>2214</td>
      <td>2262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>285</td>
      <td>2263</td>
      <td>2267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1814928115

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6mvv">6MVV</a></td>
      <td>not specified</td>
      <td>—</td>
      <td>NavAb/I217C/Delta40 in complex with <a href="/xray-mp-wiki/reagents/ligands/lidocaine/">Lidocaine</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6mvv">6MVV</a></td>
      <td>not specified</td>
      <td>—</td>
      <td>NavAb/I217C/Delta40 in complex with <a href="/xray-mp-wiki/reagents/ligands/flecainide/">Flecainide</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Trichoplusia ni insect cells (Bac-to-Bac baculovirus system)
- **Construct**: Full-length Na_vAb wild-type and mutants
- **Notes**: Na_vAb/FY constructed by site-directed mutagenesis (QuikChange); Na_vAb/1-226 constructed by introduction of stop codon at Lys-227

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mvv">6MVV</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSF</span><span class="topo-membrane">FTKFIIYLIVLNGITMGL</span><span class="topo-inside">ETSKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKD</span><span class="topo-membrane">PWSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFE</span><span class="topo-membrane">ILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPG</span><span class="topo-membrane">MLSVIALMTLFFYIFAIMAT</span><span class="topo-inside">QLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGE</span><span class="topo-unknown">SFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYP</span><span class="topo-membrane">YAWVFFIPFIAVVTFVMINLV</span><span class="topo-outside">VAICVDAMA</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>31</td>
      <td>1001</td>
      <td>1013</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>49</td>
      <td>1014</td>
      <td>1031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>62</td>
      <td>1032</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>1045</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>92</td>
      <td>1065</td>
      <td>1074</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>109</td>
      <td>1075</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>1092</td>
      <td>1096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>131</td>
      <td>1097</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>147</td>
      <td>1114</td>
      <td>1129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>167</td>
      <td>1130</td>
      <td>1149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>183</td>
      <td>1150</td>
      <td>1165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>198</td>
      <td>1166</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>210</td>
      <td>1181</td>
      <td>1192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>231</td>
      <td>1193</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>240</td>
      <td>1214</td>
      <td>1222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>285</td>
      <td>1223</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mvv">6MVV</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSHM</span><span class="topo-outside">YLRITNIVESSFFT</span><span class="topo-membrane">KFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YTTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKD</span><span class="topo-membrane">PWSLFDFFVVAISLVP</span><span class="topo-inside">TSSGFE</span><span class="topo-membrane">ILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPG</span><span class="topo-membrane">MLSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGE</span><span class="topo-unknown">SFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPYA</span><span class="topo-membrane">WVFFIPFIAVVTFVMINLV</span><span class="topo-outside">VAICVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEE</span><span class="topo-unknown">QHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>1983</td>
      <td>2001</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>33</td>
      <td>2002</td>
      <td>2015</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>2016</td>
      <td>2032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>61</td>
      <td>2033</td>
      <td>2043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>82</td>
      <td>2044</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>92</td>
      <td>2065</td>
      <td>2074</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>108</td>
      <td>2075</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>114</td>
      <td>2091</td>
      <td>2096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>131</td>
      <td>2097</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>147</td>
      <td>2114</td>
      <td>2129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>2130</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>2149</td>
      <td>2165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>198</td>
      <td>2166</td>
      <td>2180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>212</td>
      <td>2181</td>
      <td>2194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>231</td>
      <td>2195</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>247</td>
      <td>2214</td>
      <td>2229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>285</td>
      <td>2230</td>
      <td>2267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mvv">6MVV</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSHM</span><span class="topo-outside">YLRITNIVESSFFTK</span><span class="topo-membrane">FIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-membrane">VYTTLFNQIVITIFTIEII</span><span class="topo-outside">LRIYVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SS</span><span class="topo-membrane">GFEILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVT</span><span class="topo-outside">AVPQMRKIVSALISVIPG</span><span class="topo-membrane">MLSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGE</span><span class="topo-unknown">SFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPYA</span><span class="topo-membrane">WVFFIPFIAVVTFVMINLV</span><span class="topo-outside">VAICV</span><span class="topo-unknown">DAMA</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>983</td>
      <td>1001</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>34</td>
      <td>1002</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>51</td>
      <td>1017</td>
      <td>1033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>60</td>
      <td>1034</td>
      <td>1042</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>79</td>
      <td>1043</td>
      <td>1061</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>93</td>
      <td>1062</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>1076</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>111</td>
      <td>1092</td>
      <td>1093</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>129</td>
      <td>1094</td>
      <td>1111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>1112</td>
      <td>1129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>1130</td>
      <td>1148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>1149</td>
      <td>1165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>198</td>
      <td>1166</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>212</td>
      <td>1181</td>
      <td>1194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>231</td>
      <td>1195</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>236</td>
      <td>1214</td>
      <td>1218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>285</td>
      <td>1219</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mvv">6MVV</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTK</span><span class="topo-membrane">FIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YTTLFNQIVITIFTIEII</span><span class="topo-outside">LRIYVHRISFFKDPW</span><span class="topo-membrane">SLFDFFVVAISLVPT</span><span class="topo-inside">SSGFE</span><span class="topo-membrane">ILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTA</span><span class="topo-outside">VPQMRKIVSALISVIPGMLS</span><span class="topo-membrane">VIALMTLFFYIFAIMAT</span><span class="topo-inside">QLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-unknown">LGESFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYP</span><span class="topo-membrane">YAWVFFIPFIAVVTFVMINLV</span><span class="topo-outside">VAICVDAMA</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>1983</td>
      <td>2000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>34</td>
      <td>2001</td>
      <td>2016</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>51</td>
      <td>2017</td>
      <td>2033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>61</td>
      <td>2034</td>
      <td>2043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>79</td>
      <td>2044</td>
      <td>2061</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>94</td>
      <td>2062</td>
      <td>2076</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>109</td>
      <td>2077</td>
      <td>2091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>2092</td>
      <td>2096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>130</td>
      <td>2097</td>
      <td>2112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>150</td>
      <td>2113</td>
      <td>2132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>167</td>
      <td>2133</td>
      <td>2149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>180</td>
      <td>2150</td>
      <td>2162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>198</td>
      <td>2163</td>
      <td>2180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>210</td>
      <td>2181</td>
      <td>2192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>231</td>
      <td>2193</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>240</td>
      <td>2214</td>
      <td>2222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>285</td>
      <td>2223</td>
      <td>2267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mvv">6MVV</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSF</span><span class="topo-membrane">FTKFIIYLIVLNGITMGL</span><span class="topo-inside">ETSKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKD</span><span class="topo-membrane">PWSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFE</span><span class="topo-membrane">ILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPG</span><span class="topo-membrane">MLSVIALMTLFFYIFAIMAT</span><span class="topo-inside">QLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGE</span><span class="topo-unknown">SFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYP</span><span class="topo-membrane">YAWVFFIPFIAVVTFVMINLV</span><span class="topo-outside">VAICVDAMA</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>31</td>
      <td>1001</td>
      <td>1013</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>49</td>
      <td>1014</td>
      <td>1031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>62</td>
      <td>1032</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>1045</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>92</td>
      <td>1065</td>
      <td>1074</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>109</td>
      <td>1075</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>1092</td>
      <td>1096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>131</td>
      <td>1097</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>147</td>
      <td>1114</td>
      <td>1129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>167</td>
      <td>1130</td>
      <td>1149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>183</td>
      <td>1150</td>
      <td>1165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>198</td>
      <td>1166</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>210</td>
      <td>1181</td>
      <td>1192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>231</td>
      <td>1193</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>240</td>
      <td>1214</td>
      <td>1222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>285</td>
      <td>1223</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mvv">6MVV</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSHM</span><span class="topo-outside">YLRITNIVESSFFT</span><span class="topo-membrane">KFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YTTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKD</span><span class="topo-membrane">PWSLFDFFVVAISLVP</span><span class="topo-inside">TSSGFE</span><span class="topo-membrane">ILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPG</span><span class="topo-membrane">MLSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGE</span><span class="topo-unknown">SFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPYA</span><span class="topo-membrane">WVFFIPFIAVVTFVMINLV</span><span class="topo-outside">VAICVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEE</span><span class="topo-unknown">QHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>1983</td>
      <td>2001</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>33</td>
      <td>2002</td>
      <td>2015</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>2016</td>
      <td>2032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>61</td>
      <td>2033</td>
      <td>2043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>82</td>
      <td>2044</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>92</td>
      <td>2065</td>
      <td>2074</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>108</td>
      <td>2075</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>114</td>
      <td>2091</td>
      <td>2096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>131</td>
      <td>2097</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>147</td>
      <td>2114</td>
      <td>2129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>2130</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>2149</td>
      <td>2165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>198</td>
      <td>2166</td>
      <td>2180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>212</td>
      <td>2181</td>
      <td>2194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>231</td>
      <td>2195</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>247</td>
      <td>2214</td>
      <td>2229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>285</td>
      <td>2230</td>
      <td>2267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mvv">6MVV</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSHM</span><span class="topo-outside">YLRITNIVESSFFTK</span><span class="topo-membrane">FIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-membrane">VYTTLFNQIVITIFTIEII</span><span class="topo-outside">LRIYVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SS</span><span class="topo-membrane">GFEILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVT</span><span class="topo-outside">AVPQMRKIVSALISVIPG</span><span class="topo-membrane">MLSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGE</span><span class="topo-unknown">SFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYPYA</span><span class="topo-membrane">WVFFIPFIAVVTFVMINLV</span><span class="topo-outside">VAICV</span><span class="topo-unknown">DAMA</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>983</td>
      <td>1001</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>34</td>
      <td>1002</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>51</td>
      <td>1017</td>
      <td>1033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>60</td>
      <td>1034</td>
      <td>1042</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>79</td>
      <td>1043</td>
      <td>1061</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>93</td>
      <td>1062</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>1076</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>111</td>
      <td>1092</td>
      <td>1093</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>129</td>
      <td>1094</td>
      <td>1111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>1112</td>
      <td>1129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>1130</td>
      <td>1148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>1149</td>
      <td>1165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>198</td>
      <td>1166</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>212</td>
      <td>1181</td>
      <td>1194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>231</td>
      <td>1195</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>236</td>
      <td>1214</td>
      <td>1218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>285</td>
      <td>1219</td>
      <td>1267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mvv">6MVV</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTK</span><span class="topo-membrane">FIIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFG</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">YTTLFNQIVITIFTIEII</span><span class="topo-outside">LRIYVHRISFFKDPW</span><span class="topo-membrane">SLFDFFVVAISLVPT</span><span class="topo-inside">SSGFE</span><span class="topo-membrane">ILRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTA</span><span class="topo-outside">VPQMRKIVSALISVIPGMLS</span><span class="topo-membrane">VIALMTLFFYIFAIMAT</span><span class="topo-inside">QLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-unknown">LGESFYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPLMEVYP</span><span class="topo-membrane">YAWVFFIPFIAVVTFVMINLV</span><span class="topo-outside">VAICVDAMA</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>1983</td>
      <td>2000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>34</td>
      <td>2001</td>
      <td>2016</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>51</td>
      <td>2017</td>
      <td>2033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>61</td>
      <td>2034</td>
      <td>2043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>79</td>
      <td>2044</td>
      <td>2061</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>94</td>
      <td>2062</td>
      <td>2076</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>109</td>
      <td>2077</td>
      <td>2091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>2092</td>
      <td>2096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>130</td>
      <td>2097</td>
      <td>2112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>150</td>
      <td>2113</td>
      <td>2132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>167</td>
      <td>2133</td>
      <td>2149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>180</td>
      <td>2150</td>
      <td>2162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>198</td>
      <td>2163</td>
      <td>2180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>210</td>
      <td>2181</td>
      <td>2192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>231</td>
      <td>2193</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>240</td>
      <td>2214</td>
      <td>2222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>285</td>
      <td>2223</td>
      <td>2267</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##s41586-018-0120-4

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6c1e">6C1E</a></td>
      <td>2.50</td>
      <td>not specified</td>
      <td>NavAb(R2G) double mutant (R1G/R2G) in complex with guanidinium</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6c1e">6C1E</a></td>
      <td>2.70</td>
      <td>not specified</td>
      <td>NavAb(R3G) gating-charge mutant</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Trichoplusia ni insect cells (Bac-to-Bac baculovirus system)
- **Construct**: Full-length Na_vAb wild-type and mutants
- **Notes**: Na_vAb/FY constructed by site-directed mutagenesis (QuikChange); Na_vAb/1-226 constructed by introduction of stop codon at Lys-227

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c1e">6C1E</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">M</span><span class="topo-unknown">YLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TS</span><span class="topo-unknown">KTFMQS</span><span class="topo-inside">FG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLGLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-outside">SVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLVV</span><span class="topo-outside">AICVDAM</span><span class="topo-unknown">A</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>1001</td>
      <td>1001</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>27</td>
      <td>1002</td>
      <td>1009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>1010</td>
      <td>1014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>1015</td>
      <td>1032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>58</td>
      <td>1035</td>
      <td>1040</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>62</td>
      <td>1041</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>1045</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>1065</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>1076</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>115</td>
      <td>1092</td>
      <td>1097</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>131</td>
      <td>1098</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>1114</td>
      <td>1124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>1125</td>
      <td>1130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>1131</td>
      <td>1148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>1149</td>
      <td>1166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>1167</td>
      <td>1177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>1178</td>
      <td>1195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>232</td>
      <td>1196</td>
      <td>1214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>1215</td>
      <td>1221</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c1e">6C1E</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">M</span><span class="topo-unknown">YLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TS</span><span class="topo-unknown">KTFMQS</span><span class="topo-inside">FG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLGLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-outside">SVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLVV</span><span class="topo-outside">AICVDAM</span><span class="topo-unknown">A</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>2001</td>
      <td>2001</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>27</td>
      <td>2002</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>2015</td>
      <td>2032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>2033</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>58</td>
      <td>2035</td>
      <td>2040</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>62</td>
      <td>2041</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>2076</td>
      <td>2091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>115</td>
      <td>2092</td>
      <td>2097</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>131</td>
      <td>2098</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>2114</td>
      <td>2124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>2125</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>232</td>
      <td>2196</td>
      <td>2214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>2215</td>
      <td>2221</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c1e">6C1E</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">M</span><span class="topo-unknown">YLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TS</span><span class="topo-unknown">KTFMQS</span><span class="topo-inside">FG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLGLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-outside">SVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLVV</span><span class="topo-outside">AICVDAM</span><span class="topo-unknown">A</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>1001</td>
      <td>1001</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>27</td>
      <td>1002</td>
      <td>1009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>1010</td>
      <td>1014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>1015</td>
      <td>1032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>58</td>
      <td>1035</td>
      <td>1040</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>62</td>
      <td>1041</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>1045</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>1065</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>1076</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>115</td>
      <td>1092</td>
      <td>1097</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>131</td>
      <td>1098</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>1114</td>
      <td>1124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>1125</td>
      <td>1130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>1131</td>
      <td>1148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>1149</td>
      <td>1166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>1167</td>
      <td>1177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>1178</td>
      <td>1195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>232</td>
      <td>1196</td>
      <td>1214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>1215</td>
      <td>1221</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c1e">6C1E</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">M</span><span class="topo-unknown">YLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TS</span><span class="topo-unknown">KTFMQS</span><span class="topo-inside">FG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLGLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-outside">SVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLVV</span><span class="topo-outside">AICVDAM</span><span class="topo-unknown">A</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>2001</td>
      <td>2001</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>27</td>
      <td>2002</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>2015</td>
      <td>2032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>2033</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>58</td>
      <td>2035</td>
      <td>2040</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>62</td>
      <td>2041</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>2076</td>
      <td>2091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>115</td>
      <td>2092</td>
      <td>2097</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>131</td>
      <td>2098</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>2114</td>
      <td>2124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>2125</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>232</td>
      <td>2196</td>
      <td>2214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>2215</td>
      <td>2221</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c1e">6C1E</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">M</span><span class="topo-unknown">YLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TS</span><span class="topo-unknown">KTFMQS</span><span class="topo-inside">FG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLGLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-outside">SVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLVV</span><span class="topo-outside">AICVDAM</span><span class="topo-unknown">A</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>1001</td>
      <td>1001</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>27</td>
      <td>1002</td>
      <td>1009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>1010</td>
      <td>1014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>1015</td>
      <td>1032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>58</td>
      <td>1035</td>
      <td>1040</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>62</td>
      <td>1041</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>1045</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>1065</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>1076</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>115</td>
      <td>1092</td>
      <td>1097</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>131</td>
      <td>1098</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>1114</td>
      <td>1124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>1125</td>
      <td>1130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>1131</td>
      <td>1148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>1149</td>
      <td>1166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>1167</td>
      <td>1177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>1178</td>
      <td>1195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>232</td>
      <td>1196</td>
      <td>1214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>1215</td>
      <td>1221</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c1e">6C1E</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">M</span><span class="topo-unknown">YLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TS</span><span class="topo-unknown">KTFMQS</span><span class="topo-inside">FG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLGLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-outside">SVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLVV</span><span class="topo-outside">AICVDAM</span><span class="topo-unknown">A</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>2001</td>
      <td>2001</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>27</td>
      <td>2002</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>2015</td>
      <td>2032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>2033</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>58</td>
      <td>2035</td>
      <td>2040</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>62</td>
      <td>2041</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>2076</td>
      <td>2091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>115</td>
      <td>2092</td>
      <td>2097</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>131</td>
      <td>2098</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>2114</td>
      <td>2124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>2125</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>232</td>
      <td>2196</td>
      <td>2214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>2215</td>
      <td>2221</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c1e">6C1E</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">M</span><span class="topo-unknown">YLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TS</span><span class="topo-unknown">KTFMQS</span><span class="topo-inside">FG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLGLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-outside">SVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLVV</span><span class="topo-outside">AICVDAM</span><span class="topo-unknown">A</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>1001</td>
      <td>1001</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>27</td>
      <td>1002</td>
      <td>1009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>1010</td>
      <td>1014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>1015</td>
      <td>1032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>58</td>
      <td>1035</td>
      <td>1040</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>62</td>
      <td>1041</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>1045</td>
      <td>1064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>1065</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>1076</td>
      <td>1091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>115</td>
      <td>1092</td>
      <td>1097</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>131</td>
      <td>1098</td>
      <td>1113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>1114</td>
      <td>1124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>1125</td>
      <td>1130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>1131</td>
      <td>1148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>1149</td>
      <td>1166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>1167</td>
      <td>1177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>1178</td>
      <td>1195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>232</td>
      <td>1196</td>
      <td>1214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>1215</td>
      <td>1221</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c1e">6C1E</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">M</span><span class="topo-unknown">YLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TS</span><span class="topo-unknown">KTFMQS</span><span class="topo-inside">FG</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLGLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALI</span><span class="topo-outside">SVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLVV</span><span class="topo-outside">AICVDAM</span><span class="topo-unknown">A</span></span>
<span class="topo-line"><span class="topo-unknown">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>19</td>
      <td>2001</td>
      <td>2001</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>27</td>
      <td>2002</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>2015</td>
      <td>2032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>2033</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>58</td>
      <td>2035</td>
      <td>2040</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>62</td>
      <td>2041</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>2076</td>
      <td>2091</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>115</td>
      <td>2092</td>
      <td>2097</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>131</td>
      <td>2098</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>2114</td>
      <td>2124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>2125</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>232</td>
      <td>2196</td>
      <td>2214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>2215</td>
      <td>2221</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1085##jgp.201711884

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a></td>
      <td>2.30</td>
      <td>not specified</td>
      <td>NavAbDelta28 (C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> of last 28 residues)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a></td>
      <td>not specified</td>
      <td>—</td>
      <td>NavAbDelta28/T206A</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a></td>
      <td>not specified</td>
      <td>—</td>
      <td>NavAbDelta28/T206S</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a></td>
      <td>not specified</td>
      <td>—</td>
      <td>NavAbDelta28/T206V</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Trichoplusia ni insect cells (Bac-to-Bac baculovirus system)
- **Construct**: Full-length Na_vAb wild-type and mutants
- **Notes**: Na_vAb/FY constructed by site-directed mutagenesis (QuikChange); Na_vAb/1-226 constructed by introduction of stop codon at Lys-227

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mwa">6MWA</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRG</span><span class="topo-outside">S</span><span class="topo-unknown">HMYLRITNIV</span><span class="topo-outside">ESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGL</span><span class="topo-inside">ETS</span><span class="topo-unknown">KTFMQSF</span><span class="topo-inside">G</span></span>
<span class="topo-line"><span class="topo-inside">VY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TS</span><span class="topo-unknown">SGF</span><span class="topo-inside">EIL</span><span class="topo-membrane">RVLR</span></span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-unknown">PQMRKIVSALIS</span><span class="topo-outside">VIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGT</span></span>
<span class="topo-line"><span class="topo-inside">LGES</span><span class="topo-unknown">FYTLFQVMTLE</span><span class="topo-inside">SWSMGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>1999</td>
      <td>1999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>27</td>
      <td>2000</td>
      <td>2009</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>2010</td>
      <td>2014</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>2015</td>
      <td>2031</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>2032</td>
      <td>2034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>2035</td>
      <td>2041</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>62</td>
      <td>2042</td>
      <td>2044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>82</td>
      <td>2045</td>
      <td>2064</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>2065</td>
      <td>2075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>2076</td>
      <td>2090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>110</td>
      <td>2091</td>
      <td>2092</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>2096</td>
      <td>2098</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>2099</td>
      <td>2113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>143</td>
      <td>2114</td>
      <td>2125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>148</td>
      <td>2126</td>
      <td>2130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>2131</td>
      <td>2148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>2149</td>
      <td>2166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>2167</td>
      <td>2177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>2178</td>
      <td>2195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>2196</td>
      <td>2213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>257</td>
      <td>2214</td>
      <td>2239</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Wild-type NavAb in two potentially slow-inactivated states

The WT NavAb structure captured two distinct potentially inactivated conformations (NavAb-AB and NavAb-CD) at 3.2 A resolution, revealing asymmetric collapse of the S6 activation gate into a dimer-of-dimers arrangement. Two diagonal S6 helices moved toward the central pore axis while the other two shifted outward, unlike the square array of closed NavAb-I217C. This unprecedented asymmetric activation gate collapse is proposed as a hallmark of the slow-inactivated state in Nav channels, consistent with biophysical studies and disease mutations that affect slow inactivation. (DOI: 10.1038/nature11077)

### Selectivity filter destabilization during slow inactivation

Structural changes in the selectivity filter of WT NavAb include disengagement of the Gln172-Glu177 backbone interaction in NavAb-CD and unlatching of the Thr175-Trp179 network in NavAb-AB. These changes destabilize the selectivity filter, correlating with increased B-factors along the P-helix. This destabilization of the selectivity filter and remodelling of the outer pore vestibule may be required for entry into the inactivated state, consistent with effects of toxin binding, permeant ions, and selectivity filter mutations on slow inactivation in mammalian Nav channels. (DOI: 10.1038/nature11077)

### Evolutionarily conserved network coupling activation gate to selectivity filter

Structure-based alignment identified a conserved network of residues in the NavAb pore module that scaffold the selectivity filter and line surrounding S5/S6 segments: Phe144, Phe152 (S5), Leu170, Phe171 (P-helix), Trp179 (P2-helix), Phe198, Ile202 (S6). Mutations of Leu170 and Ile202 equivalents in Nav1.4 dramatically alter slow inactivation. This network couples intracellular activation gate conformation to the selectivity filter through a mechanism resulting in collapse into a dimer-of-dimers arrangement of all pore functional elements. (DOI: 10.1038/nature11077)

### VSD displacement and coupling to pore during inactivation

The voltage-sensing domains (VSDs) shifted around the perimeter of the pore module in WT NavAb compared to the I217C mutant, with displacements up to ~5 A. A major hinge point at the base of the S5 segment was identified. The VSDs remained in activated conformation but were repositioned relative to the PM, suggesting that pivoting of the VSD around the PM at the S5 gating hinge forces collapse of two S6 segments into the asymmetric dimer-of-dimers conformation at the activation gate. This gating movement is a potential target for next-generation Nav blocking drugs. (DOI: 10.1038/nature11077)

### Closed and open states of the BacNav activation gate

Na_vAb/FY (T206F/V213Y) captures a tightly closed activation gate with I217 and M221
narrowing the pore orifice to 3.2 Å, occluding hydrated Na+ permeation. Na_vAb/1-226
(C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/)) captures an open activation gate with an orifice of ~10.3 Å,
allowing hydrated Na+ permeation. The S6 helix in the closed state is straight, while
in the open state it develops a kink at T206, the hinge residue. These structures
establish the full range of motion of the activation gate from closed (fully occluded)
to open (~10 Å) in a single BacNav channel.

### Hydrophobic gating mechanism for ion permeation

Molecular dynamics and free-energy simulations confirmed that Na_vAb/1-226 represents
an open state allowing permeation of hydrated Na+. The results support a hydrophobic
gating mechanism where changes in the size of a narrow hydrophobic lumen segment shift
the equilibrium between hydrated (wetted) and dehydrated (dewetted) states, enabling or
precluding ion passage. The activation gate induces a small desolvation penalty of
~2 kcal/mol for Na+ in the open state, which doubles to ~4 kcal/mol upon structural
relaxation toward a partially collapsed state.

### C-terminal domain structure of NavAb

The Na_vAb/FY structure reveals the complete four-helix bundle of the C-terminal domain
(CTD). The CTD has a proximal "neck" portion with hydrophilic residues (N225, E228)
on the interior and a distal portion forming a classical four-helix bundle with
hydrophobic residues. Unlike Na_vAep1, NavAb contains only alpha helices in the neck
region (no pi-helix). Removing the CTD in Na_vAb/1-226 favored channel activation and
pore-opening, indicating the CTD influences voltage-dependent activation.

### Closed-open-inactivated conformational cycle

Comparison of NavAb/FY (closed), NavAb/1-226 (open), and NavAb/WT (inactivated) structures
reveals distinct pore diameters: closed (3.2 Å at M221), open (10.3 Å at C217), and
inactivated (intermediate, asymmetric). The S6 segment undergoes twisting/bending motions
that change side chain positions at the central cavity (CC), a target site for sodium
channel-blocking drugs. The transition from open to deep resting states likely has
substantial effects on drug binding, providing structural basis for hyperpolarization-
dependent drug dissociation.

### Drug binding site for local anesthetics and antiarrhythmic drugs in NavAb

Crystal structures of NavAb in complex with [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/) and [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/) reveal the receptor site for LAs and AADs in the central cavity of the pore, on the intracellular side of the selectivity filter. The positively charged amino groups of both drugs point toward the selectivity filter (formed by backbone carbonyl groups of T175). Mutation of T206 to alanine reduces drug potency 17.8-fold for [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/) and 18.5-fold for [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/). [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/) shows fourfold-averaged electron density, while [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/) shows a single well-defined pose.

### Fenestrations control resting-state block by LAs and AADs

Fenestrations in the NavAb pore connect the lipid phase to the central cavity. Mutations of the fenestration cap residue F203 change fenestration size (F203A widens, F203W narrows) without altering pore conformation. For [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/), these cause a 51-fold range in drug potency: F203A IC50 0.9 uM (7.7-fold more potent) to F203W IC50 46 uM (6.5-fold less potent). For [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/), F203W shifts potency 3.4-fold (IC50 458 uM vs 135 uM WT). Effects scale with molecular size.

### Implications for structure-based drug design targeting sodium channels

Fenestration size modulation of drug potency introduces a new concept for structure-based design of LAs, AADs, analgesics, and antiepileptics. Fenestration architecture varies between Nav channel isoforms and can be altered by disease mutations. Differences in binding poses between [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/) (class IB, ventricular arrhythmias) and [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/) (class IC, atrial arrhythmias) may underlie their distinct clinical uses.

### Structural basis of gating pore current in periodic paralysis

High-resolution structures of NavAb with R2G and R3G gating-charge mutations, analogous to those causing hypokalaemic and normokalaemic periodic paralysis in human Nav1.4, reveal the atomic mechanism of pathogenic gating pore currents. The R2G and R3G mutations have no effect on the backbone structure of the voltage sensor but create an aqueous cavity near the hydrophobic constriction site (HCS) that controls gating charge movement. R3G extends the extracellular aqueous cleft through the entire activated voltage sensor, creating a continuous aqueous path. R2G creates a continuous path only in the resting state. Crystal structures of NavAb(R2G) in complex with guanidinium define a potential drug target site. MD simulations show Na+ permeation through the mutant gating pore in concert with conformational fluctuations of gating charge R4.

### Thr206 as a molecular hub for activation-inactivation coupling

Mutation of Thr206 in the S6 segment to Ala or Ser (small side-chain volume ~88-92 A^3) abolishes the early voltage-dependent inactivation during single depolarizations, while mutation to Val (larger volume 141.7 A^3) preserves it. This reveals a size-dependent mechanism: the S6 helix kinks at Thr206 during activation and unkinks during inactivation. In the closed state, Thr206 is ~5 A from Met174 carbonyl; in the open/activated state, it moves to 3.6 A (forming a potential weak H-bond); in the inactivated state, it is 6.1 A away. Smaller side chains at position 206 prevent proper kinking/unkinking dynamics, thereby uncoupling activation from early inactivation. T206A also shifts activation V1/2 by ~25 mV in the negative direction. (DOI: 10.1085/jgp.201711884)

### Two-step model of multiphase inactivation in NavAb

The multiphase slow inactivation of NavAb proceeds via a two-step mechanism. (1) Early voltage-dependent inactivation (during a single depolarization) is triggered by bending of the S6 segment at Thr206, followed by local protein interactions and exchange of hydrogen-bonding partners. The side-chain volume at position 206 determines the kinetics of this early phase. (2) Late use-dependent inactivation (during repetitive depolarizations) requires the C-terminal tail. [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) of 10 residues (NavAbDelta10) from the distal CTD abolishes late use-dependent inactivation at 0.2 Hz, while deleting 3, 7, 28, or 40 residues has graded effects. The C-terminal tail forms a four-helix bundle that is maintained even in large truncations. The hydrophobic distal 20 residues of the CTD (coiled-coil region) stabilize this late inactivation phase. Asymmetric pore collapse occurs during the open-to-inactivated transition, with two S6 segments moving toward the pore axis and two moving away. (DOI: 10.1085/jgp.201711884)


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/chapso/">CHAPSO</a> — Detergent used for bicelle reconstitution and crystallization
- <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a> — Lipid used for bicelle formation in crystallization
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/navms/">NavMs Bacterial Voltage-Gated Sodium Channel</a> — Related bacterial sodium channel for pore gating comparison
- <a href="/xray-mp-wiki/reagents/ligands/lidocaine/">Lidocaine</a> — Local anesthetic and class IB antiarrhythmic drug co-crystallized with NavAb
- <a href="/xray-mp-wiki/reagents/ligands/flecainide/">Flecainide</a> — Class IC antiarrhythmic drug co-crystallized with NavAb
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/gating-pore-current/">Gating Pore Current (Omega Current)</a> — NavAb R2G and R3G mutant structures reveal structural basis of gating pore currents in periodic paralysis
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> — Related biological concept
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Additive used in purification or crystallization buffers
