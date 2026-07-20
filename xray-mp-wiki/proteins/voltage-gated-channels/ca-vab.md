---
title: "CaVAb Bacterial Voltage-Gated Calcium Channel"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12775, doi/10.1038##nature19102]
verified: agent
uniprot_id: A8EVM5
---

# CaVAb Bacterial Voltage-Gated Calcium Channel

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-mammalian">Mammalian</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A8EVM5">UniProt: A8EVM5</a>

<span class="expr-badge">Arcobacter butzleri (strain RM4018)</span>

## Overview

CaVAb is a bacterial voltage-gated calcium channel that serves as an evolutionary link between prokaryotic sodium channels and eukaryotic voltage-gated calcium channels. CaVAb shares structural homology with [NavAb](/xray-mp-wiki/proteins/navab) but has evolved distinct selectivity filter chemistry that confers calcium permeability. The selectivity filter sequence FQVMTLDDWSDG differs from NavAb's TLESW motif through key substitutions that create a high-affinity calcium binding site. This paper reports the first structural analysis of a bacterial calcium channel, revealing how selectivity filter architecture determines ion selectivity between sodium and calcium. Subsequent studies have determined high-resolution structures of CaVAb in complex with multiple classes of Ca2+ antagonist drugs, revealing distinct binding sites and mechanisms for dihydropyridines and phenylalkylamines.


## Publications

### doi/10.1038##nature12775

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ms2">4MS2</a></td>
      <td>3.3</td>
      <td>C 1 21</td>
      <td>CaVAb 175TLDDWSD181 variant; homotetramer; selectivity filter sequence FQVMTLDDWSDG with key substitutions E177 (vs T in <a href="/xray-mp-wiki/proteins/navab">NavAb</a>), D178 (vs L), D181 (vs W); crystallized with 100 mM Cd2+ and 100 mM Mn2+ soaking</td>
      <td>Cd2+ (100 mM soaking), Mn2+ (100 mM soaking)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ms2">4MS2</a></td>
      <td>3.3</td>
      <td>C 1 21</td>
      <td>CaVAb 175TLDDWSD181 variant; homotetramer; crystallized with 15 mM Ca2+ soaking</td>
      <td>Ca2+ (15 mM soaking)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system) expression in Trichoplusia ni (High5) insect cells
- **Construct**: pFastBac-[FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag)-CaVAb; multiple variants including I199S, W195Y, T206S, E177D S178D M181N, E177D S178D M181N W195Y; all on N49K mutation background

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Not specified in supplementary information</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in supplementary information</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals in space group C 1 21. Ca2+ binding sites identified at the selectivity filter through anomalous difference Fourier maps. Multiple soaking conditions tested: 0.5, 2.5, 5, 10, and 15 mM Ca2+. Cd2+ and Mn2+ soaking at 100 mM also performed.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ms2">4MS2</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSF</span><span class="topo-membrane">FTKFIIYLIVLNGITMGL</span><span class="topo-inside">ETSKTFMQSFGVYTTLF</span><span class="topo-membrane">NQIVITIFTIEIILRIY</span><span class="topo-outside">VHRISFFKD</span><span class="topo-membrane">PWSLFDFFVVAISLV</span><span class="topo-inside">PTSSGFEILRV</span><span class="topo-membrane">LR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       </span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGTL</span><span class="topo-unknown">GESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYP</span><span class="topo-membrane">YAWVFFIPFIFVVTFVMI</span><span class="topo-outside">NLVVAICVD</span></span>
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
      <td>66</td>
      <td>1032</td>
      <td>1048</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>83</td>
      <td>1049</td>
      <td>1065</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>92</td>
      <td>1066</td>
      <td>1074</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>107</td>
      <td>1075</td>
      <td>1089</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>118</td>
      <td>1090</td>
      <td>1100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>131</td>
      <td>1101</td>
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
      <td>210</td>
      <td>1181</td>
      <td>1192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>228</td>
      <td>1193</td>
      <td>1210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>237</td>
      <td>1211</td>
      <td>1219</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ms2">4MS2</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKF</span><span class="topo-membrane">IIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFGV</span><span class="topo-membrane">YTTLFNQIVITIFTIEI</span><span class="topo-outside">ILRIYVHRISFFKDPWSLF</span><span class="topo-membrane">DFFVVAISLVPTSSG</span><span class="topo-inside">F</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       </span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLV</span><span class="topo-outside">TAVPQMRKIVSALISVIPGMLSVI</span><span class="topo-membrane">ALMTLFFYIFAIMATQLFG</span><span class="topo-inside">ERFPEW</span><span class="topo-unknown">FGTLGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYP</span><span class="topo-membrane">YAWVFFIPFIFVVTFVMI</span><span class="topo-outside">NLVVAICVD</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>1001</td>
      <td>1017</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>51</td>
      <td>1018</td>
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
      <td>78</td>
      <td>1044</td>
      <td>1060</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>97</td>
      <td>1061</td>
      <td>1079</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>112</td>
      <td>1080</td>
      <td>1094</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>113</td>
      <td>1095</td>
      <td>1095</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>128</td>
      <td>1096</td>
      <td>1110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>152</td>
      <td>1111</td>
      <td>1134</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>171</td>
      <td>1135</td>
      <td>1153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>177</td>
      <td>1154</td>
      <td>1159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>198</td>
      <td>1160</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>210</td>
      <td>1180</td>
      <td>1192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>228</td>
      <td>1193</td>
      <td>1210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>237</td>
      <td>1211</td>
      <td>1219</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ms2">4MS2</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKF</span><span class="topo-membrane">IIYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEIIL</span><span class="topo-outside">RIYVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       </span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTA</span><span class="topo-outside">VPQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTLGES</span><span class="topo-unknown">FYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAICVD</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>1001</td>
      <td>1017</td>
      <td>Outside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>80</td>
      <td>1042</td>
      <td>1062</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>93</td>
      <td>1063</td>
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
      <td>130</td>
      <td>1098</td>
      <td>1112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>1113</td>
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
      <td>198</td>
      <td>1167</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>213</td>
      <td>1181</td>
      <td>1195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>1196</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>237</td>
      <td>1214</td>
      <td>1219</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ms2">4MS2</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKFIIYL</span><span class="topo-membrane">IVLNGITMGLETSKTFM</span><span class="topo-inside">Q</span><span class="topo-membrane">SFGVYTTLFNQIVITIFT</span><span class="topo-outside">IEIILRIYVHRISFFKDPWSLFDFF</span><span class="topo-membrane">VVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       </span>
<span class="topo-line"><span class="topo-membrane">VLRLFR</span><span class="topo-outside">LVTAVPQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQ</span><span class="topo-inside">LFGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPYA</span><span class="topo-membrane">WVFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAICVD</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>39</td>
      <td>1001</td>
      <td>1021</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>56</td>
      <td>1022</td>
      <td>1038</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>57</td>
      <td>1039</td>
      <td>1039</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>75</td>
      <td>1040</td>
      <td>1057</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>100</td>
      <td>1058</td>
      <td>1082</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>109</td>
      <td>1083</td>
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
      <td>126</td>
      <td>1098</td>
      <td>1108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>151</td>
      <td>1109</td>
      <td>1133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>168</td>
      <td>1134</td>
      <td>1150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>180</td>
      <td>1151</td>
      <td>1162</td>
      <td>Inside</td>
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
      <td>237</td>
      <td>1214</td>
      <td>1219</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ms2">4MS2</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSF</span><span class="topo-membrane">FTKFIIYLIVLNGITMGL</span><span class="topo-inside">ETSKTFMQSFGVYTTLF</span><span class="topo-membrane">NQIVITIFTIEIILRIY</span><span class="topo-outside">VHRISFFKD</span><span class="topo-membrane">PWSLFDFFVVAISLV</span><span class="topo-inside">PTSSGFEILRV</span><span class="topo-membrane">LR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       </span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGTL</span><span class="topo-unknown">GESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYP</span><span class="topo-membrane">YAWVFFIPFIFVVTFVMI</span><span class="topo-outside">NLVVAICVD</span></span>
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
      <td>66</td>
      <td>1032</td>
      <td>1048</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>83</td>
      <td>1049</td>
      <td>1065</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>92</td>
      <td>1066</td>
      <td>1074</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>107</td>
      <td>1075</td>
      <td>1089</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>118</td>
      <td>1090</td>
      <td>1100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>131</td>
      <td>1101</td>
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
      <td>210</td>
      <td>1181</td>
      <td>1192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>228</td>
      <td>1193</td>
      <td>1210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>237</td>
      <td>1211</td>
      <td>1219</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ms2">4MS2</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKF</span><span class="topo-membrane">IIYLIVLNGITMGLET</span><span class="topo-inside">SKTFMQSFGV</span><span class="topo-membrane">YTTLFNQIVITIFTIEI</span><span class="topo-outside">ILRIYVHRISFFKDPWSLF</span><span class="topo-membrane">DFFVVAISLVPTSSG</span><span class="topo-inside">F</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       </span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLV</span><span class="topo-outside">TAVPQMRKIVSALISVIPGMLSVI</span><span class="topo-membrane">ALMTLFFYIFAIMATQLFG</span><span class="topo-inside">ERFPEW</span><span class="topo-unknown">FGTLGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYP</span><span class="topo-membrane">YAWVFFIPFIFVVTFVMI</span><span class="topo-outside">NLVVAICVD</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>1001</td>
      <td>1017</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>51</td>
      <td>1018</td>
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
      <td>78</td>
      <td>1044</td>
      <td>1060</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>97</td>
      <td>1061</td>
      <td>1079</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>112</td>
      <td>1080</td>
      <td>1094</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>113</td>
      <td>1095</td>
      <td>1095</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>128</td>
      <td>1096</td>
      <td>1110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>152</td>
      <td>1111</td>
      <td>1134</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>171</td>
      <td>1135</td>
      <td>1153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>177</td>
      <td>1154</td>
      <td>1159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>198</td>
      <td>1160</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>210</td>
      <td>1180</td>
      <td>1192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>228</td>
      <td>1193</td>
      <td>1210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>237</td>
      <td>1211</td>
      <td>1219</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ms2">4MS2</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKF</span><span class="topo-membrane">IIYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEIIL</span><span class="topo-outside">RIYVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       </span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTA</span><span class="topo-outside">VPQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTLGES</span><span class="topo-unknown">FYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAICVD</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>1001</td>
      <td>1017</td>
      <td>Outside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>80</td>
      <td>1042</td>
      <td>1062</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>93</td>
      <td>1063</td>
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
      <td>130</td>
      <td>1098</td>
      <td>1112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>1113</td>
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
      <td>198</td>
      <td>1167</td>
      <td>1180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>213</td>
      <td>1181</td>
      <td>1195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>1196</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>237</td>
      <td>1214</td>
      <td>1219</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ms2">4MS2</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKFIIYL</span><span class="topo-membrane">IVLNGITMGLETSKTFM</span><span class="topo-inside">Q</span><span class="topo-membrane">SFGVYTTLFNQIVITIFT</span><span class="topo-outside">IEIILRIYVHRISFFKDPWSLFDFF</span><span class="topo-membrane">VVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       </span>
<span class="topo-line"><span class="topo-membrane">VLRLFR</span><span class="topo-outside">LVTAVPQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQ</span><span class="topo-inside">LFGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPYA</span><span class="topo-membrane">WVFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAICVD</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>39</td>
      <td>1001</td>
      <td>1021</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>56</td>
      <td>1022</td>
      <td>1038</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>57</td>
      <td>1039</td>
      <td>1039</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>75</td>
      <td>1040</td>
      <td>1057</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>100</td>
      <td>1058</td>
      <td>1082</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>109</td>
      <td>1083</td>
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
      <td>126</td>
      <td>1098</td>
      <td>1108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>151</td>
      <td>1109</td>
      <td>1133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>168</td>
      <td>1134</td>
      <td>1150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>180</td>
      <td>1151</td>
      <td>1162</td>
      <td>Inside</td>
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
      <td>237</td>
      <td>1214</td>
      <td>1219</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature19102

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a></td>
      <td>2.7 A</td>
      <td>P212121</td>
      <td>CaVAb with 5 mM Ca2+; wild-type channel without drug</td>
      <td>Ca2+ (5 mM)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a></td>
      <td>3.2 A</td>
      <td>P212121</td>
      <td>CaVAb (W195Y) with <a href="/xray-mp-wiki/reagents/ligands/amlodipine">Amlodipine</a> and 5 mM Ca2+; W195Y mutation substituted the Y residue from mammalian CaV1.1 for W195 in CaVAb for better drug resolution</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/amlodipine">Amlodipine</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a></td>
      <td>3.2 A</td>
      <td>P212121</td>
      <td>CaVAb (W195Y) with <a href="/xray-mp-wiki/reagents/ligands/nimodipine">Nimodipine</a> and 5 mM Ca2+</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/nimodipine">Nimodipine</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a></td>
      <td>3.3 A</td>
      <td>P212121</td>
      <td>CaVAb (W195Y) with <a href="/xray-mp-wiki/reagents/ligands/uk-59811">UK-59811</a> and 5 mM Ca2+</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/uk-59811">UK-59811</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a></td>
      <td>3.3 A</td>
      <td>P212121</td>
      <td>CaVAb with <a href="/xray-mp-wiki/reagents/ligands/br-verapamil">Br-Verapamil</a> and 5 mM Ca2+</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/br-verapamil">Br-Verapamil</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system) expression in Trichoplusia ni (High5) insect cells
- **Construct**: pFastBac-[FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag)-CaVAb; multiple variants including I199S, W195Y, T206S, E177D S178D M181N, E177D S178D M181N W195Y; all on N49K mutation background

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CaVAb with 5 mM Ca2+</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Wild-type CaVAb crystals without drug in P212121 space group at 2.7 A resolution; serves as baseline for drug-bound structures</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CaVAb (W195Y) with <a href="/xray-mp-wiki/reagents/ligands/amlodipine">Amlodipine</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/amlodipine">Amlodipine</a>-bound structure in P212121 at 3.2 A resolution; W195Y mutation enables better resolution of drug binding site</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CaVAb (W195Y) with <a href="/xray-mp-wiki/reagents/ligands/nimodipine">Nimodipine</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/nimodipine">Nimodipine</a>-bound structure in P212121 at 3.2 A resolution</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CaVAb (W195Y) with <a href="/xray-mp-wiki/reagents/ligands/uk-59811">UK-59811</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/uk-59811">UK-59811</a>-bound structure in P212121 at 3.3 A resolution; anomalous scattering of Br confirms binding location</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CaVAb with <a href="/xray-mp-wiki/reagents/ligands/br-verapamil">Br-Verapamil</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/br-verapamil">Br-Verapamil</a>-bound structure in P212121 at 3.3 A resolution; anomalous scattering of Br defines exact binding location in central cavity</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFGVY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMI</span><span class="topo-outside">NLVVAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>32</td>
      <td>1001</td>
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
      <td>62</td>
      <td>1033</td>
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
      <td>151</td>
      <td>1114</td>
      <td>1133</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>228</td>
      <td>1194</td>
      <td>1210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>285</td>
      <td>1211</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKF</span><span class="topo-membrane">IIYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEII</span><span class="topo-outside">LRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTS</span><span class="topo-inside">SGF</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVT</span><span class="topo-outside">AVPQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTL</span><span class="topo-unknown">GESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>1001</td>
      <td>1017</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>110</td>
      <td>1079</td>
      <td>1092</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>113</td>
      <td>1093</td>
      <td>1095</td>
      <td>Inside</td>
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
      <td>148</td>
      <td>1112</td>
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
      <td>181</td>
      <td>1149</td>
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
      <td>213</td>
      <td>1181</td>
      <td>1195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>1196</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>285</td>
      <td>1214</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSF</span><span class="topo-membrane">FTKFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFGVY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRIY</span><span class="topo-outside">VHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TSSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTLGES</span><span class="topo-unknown">FYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>50</td>
      <td>1014</td>
      <td>1032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>1033</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>83</td>
      <td>1045</td>
      <td>1065</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>1066</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>1076</td>
      <td>1090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>115</td>
      <td>1091</td>
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
      <td>148</td>
      <td>1114</td>
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
      <td>198</td>
      <td>1167</td>
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
      <td>285</td>
      <td>1214</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKFI</span><span class="topo-membrane">IYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEI</span><span class="topo-outside">ILRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTSSG</span><span class="topo-inside">F</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLV</span><span class="topo-outside">TAVPQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMIN</span><span class="topo-outside">LVVAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>36</td>
      <td>1001</td>
      <td>1018</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>52</td>
      <td>1019</td>
      <td>1034</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>1035</td>
      <td>1041</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>78</td>
      <td>1042</td>
      <td>1060</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>96</td>
      <td>1061</td>
      <td>1078</td>
      <td>Outside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>128</td>
      <td>1096</td>
      <td>1110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>151</td>
      <td>1111</td>
      <td>1133</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>229</td>
      <td>1194</td>
      <td>1211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>285</td>
      <td>1212</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFGVY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMI</span><span class="topo-outside">NLVVAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>32</td>
      <td>1001</td>
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
      <td>62</td>
      <td>1033</td>
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
      <td>151</td>
      <td>1114</td>
      <td>1133</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>228</td>
      <td>1194</td>
      <td>1210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>285</td>
      <td>1211</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKF</span><span class="topo-membrane">IIYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEII</span><span class="topo-outside">LRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTS</span><span class="topo-inside">SGF</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVT</span><span class="topo-outside">AVPQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTL</span><span class="topo-unknown">GESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>1001</td>
      <td>1017</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>110</td>
      <td>1079</td>
      <td>1092</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>113</td>
      <td>1093</td>
      <td>1095</td>
      <td>Inside</td>
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
      <td>148</td>
      <td>1112</td>
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
      <td>181</td>
      <td>1149</td>
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
      <td>213</td>
      <td>1181</td>
      <td>1195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>1196</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>285</td>
      <td>1214</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSF</span><span class="topo-membrane">FTKFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFGVY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRIY</span><span class="topo-outside">VHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TSSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTLGES</span><span class="topo-unknown">FYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>50</td>
      <td>1014</td>
      <td>1032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>1033</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>83</td>
      <td>1045</td>
      <td>1065</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>1066</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>1076</td>
      <td>1090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>115</td>
      <td>1091</td>
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
      <td>148</td>
      <td>1114</td>
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
      <td>198</td>
      <td>1167</td>
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
      <td>285</td>
      <td>1214</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKFI</span><span class="topo-membrane">IYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEI</span><span class="topo-outside">ILRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTSSG</span><span class="topo-inside">F</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLV</span><span class="topo-outside">TAVPQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMIN</span><span class="topo-outside">LVVAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>36</td>
      <td>1001</td>
      <td>1018</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>52</td>
      <td>1019</td>
      <td>1034</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>1035</td>
      <td>1041</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>78</td>
      <td>1042</td>
      <td>1060</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>96</td>
      <td>1061</td>
      <td>1078</td>
      <td>Outside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>128</td>
      <td>1096</td>
      <td>1110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>151</td>
      <td>1111</td>
      <td>1133</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>229</td>
      <td>1194</td>
      <td>1211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>285</td>
      <td>1212</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFGVY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMI</span><span class="topo-outside">NLVVAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>32</td>
      <td>1001</td>
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
      <td>62</td>
      <td>1033</td>
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
      <td>151</td>
      <td>1114</td>
      <td>1133</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>228</td>
      <td>1194</td>
      <td>1210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>285</td>
      <td>1211</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKF</span><span class="topo-membrane">IIYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEII</span><span class="topo-outside">LRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTS</span><span class="topo-inside">SGF</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVT</span><span class="topo-outside">AVPQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTL</span><span class="topo-unknown">GESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>1001</td>
      <td>1017</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>110</td>
      <td>1079</td>
      <td>1092</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>113</td>
      <td>1093</td>
      <td>1095</td>
      <td>Inside</td>
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
      <td>148</td>
      <td>1112</td>
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
      <td>181</td>
      <td>1149</td>
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
      <td>213</td>
      <td>1181</td>
      <td>1195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>1196</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>285</td>
      <td>1214</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSF</span><span class="topo-membrane">FTKFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFGVY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRIY</span><span class="topo-outside">VHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TSSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTLGES</span><span class="topo-unknown">FYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>50</td>
      <td>1014</td>
      <td>1032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>1033</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>83</td>
      <td>1045</td>
      <td>1065</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>1066</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>1076</td>
      <td>1090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>115</td>
      <td>1091</td>
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
      <td>148</td>
      <td>1114</td>
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
      <td>198</td>
      <td>1167</td>
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
      <td>285</td>
      <td>1214</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKFI</span><span class="topo-membrane">IYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEI</span><span class="topo-outside">ILRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTSSG</span><span class="topo-inside">F</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLV</span><span class="topo-outside">TAVPQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMIN</span><span class="topo-outside">LVVAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>36</td>
      <td>1001</td>
      <td>1018</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>52</td>
      <td>1019</td>
      <td>1034</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>1035</td>
      <td>1041</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>78</td>
      <td>1042</td>
      <td>1060</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>96</td>
      <td>1061</td>
      <td>1078</td>
      <td>Outside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>128</td>
      <td>1096</td>
      <td>1110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>151</td>
      <td>1111</td>
      <td>1133</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>229</td>
      <td>1194</td>
      <td>1211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>285</td>
      <td>1212</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFGVY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMI</span><span class="topo-outside">NLVVAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>32</td>
      <td>1001</td>
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
      <td>62</td>
      <td>1033</td>
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
      <td>151</td>
      <td>1114</td>
      <td>1133</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>228</td>
      <td>1194</td>
      <td>1210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>285</td>
      <td>1211</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKF</span><span class="topo-membrane">IIYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEII</span><span class="topo-outside">LRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTS</span><span class="topo-inside">SGF</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVT</span><span class="topo-outside">AVPQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTL</span><span class="topo-unknown">GESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>1001</td>
      <td>1017</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>110</td>
      <td>1079</td>
      <td>1092</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>113</td>
      <td>1093</td>
      <td>1095</td>
      <td>Inside</td>
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
      <td>148</td>
      <td>1112</td>
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
      <td>181</td>
      <td>1149</td>
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
      <td>213</td>
      <td>1181</td>
      <td>1195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>1196</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>285</td>
      <td>1214</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSF</span><span class="topo-membrane">FTKFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFGVY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRIY</span><span class="topo-outside">VHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TSSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTLGES</span><span class="topo-unknown">FYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>50</td>
      <td>1014</td>
      <td>1032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>1033</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>83</td>
      <td>1045</td>
      <td>1065</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>1066</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>1076</td>
      <td>1090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>115</td>
      <td>1091</td>
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
      <td>148</td>
      <td>1114</td>
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
      <td>198</td>
      <td>1167</td>
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
      <td>285</td>
      <td>1214</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKFI</span><span class="topo-membrane">IYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEI</span><span class="topo-outside">ILRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTSSG</span><span class="topo-inside">F</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLV</span><span class="topo-outside">TAVPQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMIN</span><span class="topo-outside">LVVAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>36</td>
      <td>1001</td>
      <td>1018</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>52</td>
      <td>1019</td>
      <td>1034</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>1035</td>
      <td>1041</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>78</td>
      <td>1042</td>
      <td>1060</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>96</td>
      <td>1061</td>
      <td>1078</td>
      <td>Outside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>128</td>
      <td>1096</td>
      <td>1110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>151</td>
      <td>1111</td>
      <td>1133</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>229</td>
      <td>1194</td>
      <td>1211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>285</td>
      <td>1212</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFF</span><span class="topo-membrane">TKFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFGVY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRI</span><span class="topo-outside">YVHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVPT</span><span class="topo-inside">SSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMI</span><span class="topo-outside">NLVVAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>32</td>
      <td>1001</td>
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
      <td>62</td>
      <td>1033</td>
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
      <td>151</td>
      <td>1114</td>
      <td>1133</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>228</td>
      <td>1194</td>
      <td>1210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>285</td>
      <td>1211</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKF</span><span class="topo-membrane">IIYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEII</span><span class="topo-outside">LRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTS</span><span class="topo-inside">SGF</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVT</span><span class="topo-outside">AVPQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTL</span><span class="topo-unknown">GESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPYAW</span><span class="topo-membrane">VFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>1001</td>
      <td>1017</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>110</td>
      <td>1079</td>
      <td>1092</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>113</td>
      <td>1093</td>
      <td>1095</td>
      <td>Inside</td>
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
      <td>148</td>
      <td>1112</td>
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
      <td>181</td>
      <td>1149</td>
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
      <td>213</td>
      <td>1181</td>
      <td>1195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>1196</td>
      <td>1213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>285</td>
      <td>1214</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSF</span><span class="topo-membrane">FTKFIIYLIVLNGITMGLE</span><span class="topo-inside">TSKTFMQSFGVY</span><span class="topo-membrane">TTLFNQIVITIFTIEIILRIY</span><span class="topo-outside">VHRISFFKDP</span><span class="topo-membrane">WSLFDFFVVAISLVP</span><span class="topo-inside">TSSGFEI</span><span class="topo-membrane">LRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLVTAV</span><span class="topo-outside">PQMRKIVSALISVIPGM</span><span class="topo-membrane">LSVIALMTLFFYIFAIMA</span><span class="topo-inside">TQLFGERFPEWFGTLGES</span><span class="topo-unknown">FYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMINLV</span><span class="topo-outside">VAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>50</td>
      <td>1014</td>
      <td>1032</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>1033</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>83</td>
      <td>1045</td>
      <td>1065</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>1066</td>
      <td>1075</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>1076</td>
      <td>1090</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>115</td>
      <td>1091</td>
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
      <td>148</td>
      <td>1114</td>
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
      <td>198</td>
      <td>1167</td>
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
      <td>285</td>
      <td>1214</td>
      <td>1267</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5klb">5KLB</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKGSLVPRGSH</span><span class="topo-outside">MYLRITNIVESSFFTKFI</span><span class="topo-membrane">IYLIVLNGITMGLETS</span><span class="topo-inside">KTFMQSF</span><span class="topo-membrane">GVYTTLFNQIVITIFTIEI</span><span class="topo-outside">ILRIYVHRISFFKDPWSL</span><span class="topo-membrane">FDFFVVAISLVPTSSG</span><span class="topo-inside">F</span><span class="topo-membrane">EILRVLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VLRLFRLV</span><span class="topo-outside">TAVPQMRKIVSALISVIPGMLSV</span><span class="topo-membrane">IALMTLFFYIFAIMATQL</span><span class="topo-inside">FGERFPEWFGT</span><span class="topo-unknown">LGESFYTLFQVMTLDDWS</span><span class="topo-inside">NGIVRPLMEVYPY</span><span class="topo-membrane">AWVFFIPFIFVVTFVMIN</span><span class="topo-outside">LVVAIIVDAMA</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">ILNQKEEQHIIDEVQSHEDNINNEIIKLREEIVELKELIKTSLKN</span></span>
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
      <td>18</td>
      <td>983</td>
      <td>1000</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>36</td>
      <td>1001</td>
      <td>1018</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>52</td>
      <td>1019</td>
      <td>1034</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>1035</td>
      <td>1041</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>78</td>
      <td>1042</td>
      <td>1060</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>96</td>
      <td>1061</td>
      <td>1078</td>
      <td>Outside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>128</td>
      <td>1096</td>
      <td>1110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>151</td>
      <td>1111</td>
      <td>1133</td>
      <td>Outside</td>
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
      <td>Inside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>229</td>
      <td>1194</td>
      <td>1211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>285</td>
      <td>1212</td>
      <td>1267</td>
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

### Calcium selectivity filter architecture

The CaVAb selectivity filter has the sequence FQVMTLDDWSDG, which differs from [NavAb](/xray-mp-wiki/proteins/navab) (FQVMTLESWSMG) at positions 177 (E vs L), 178 (D vs E), 180 (D vs S), and 181 (D vs G). The introduction of two adjacent negatively charged residues (E177 and D178) at the high-field-strength site creates a calcium-coordinating environment. This is consistent with the EEEE motif found in eukaryotic voltage-gated calcium channels, where four glutamate residues from each domain coordinate Ca2+ ions.

### Ca2+ binding sites at the selectivity filter

Anomalous difference Fourier maps reveal three Ca2+ binding sites (Site 1, 2, and 3) at the selectivity filter. Site 1 and Site 2 show clear anomalous density for Ca2+ when crystals are soaked with calcium solutions. The Ca2+ ions are coordinated by oxygen atoms from selectivity filter residues and water molecules. Evidence for hydration shells around bound Ca2+ ions is observed through omit maps, with Ca2+-8H2O complexes modeled at the binding sites.

### Mutagenesis of selectivity filter residues

Systematic mutagenesis of the selectivity filter residues reveals how each position contributes to ion selectivity. The 175TLDDWSN181 mutant (D181N) shows altered permeability with E_rev of +35 mV for Ca2+ and +7.5 mV for Ba2+. The 175TLEDWSD181 mutant (E177D) has E_rev of +30 mV for Ca2+ and +14.5 mV for Ba2+. The 175TLEDWSM181 mutant (E177D, D181M) shows E_rev of +20 mV for Ca2+ and -6.38 mV for Ba2+. The 175TLDDWSM181 mutant (D181M) fails to produce ionic current in Ca2+/Ba2+ solutions but shows large Na+ currents when [EGTA (Ethylene Glycol Tetraacetic Acid)](/xray-mp-wiki/reagents/additives/egta) is added. The 175TLDSWSM181 mutant (D178S, D181M) also shows altered permeation properties.

### Structural comparison with NavAb

The CaVAb selectivity filter structure can be compared to [NavAb](/xray-mp-wiki/proteins/navab) to understand the molecular basis of calcium versus sodium selectivity. The key differences are at positions 177, 178, and 181 where CaVAb has negatively charged residues (E, D, D) compared to NavAb (L, E, G). These substitutions create a calcium-binding pocket while maintaining the overall selectivity filter fold. The distance between the carboxyl oxygen of E177 and the main chain nitrogen of S180/D181 is approximately 2.9 A and 3.3 A respectively.

### Allosteric mechanism of dihydropyridine binding

Dihydropyridines ([Amlodipine](/xray-mp-wiki/reagents/ligands/amlodipine), nimodipine, UK-59811) bind at the external, lipid-facing surface of the pore module at the interface between two subunits. Their binding site is exposed to the extracellular side of the membrane but not to the intracellular side. Binding displaces an endogenous lipid molecule from the common binding site and allosterically induces an asymmetric conformation of the selectivity filter. In the asymmetric state, partially dehydrated Ca2+ binds to Site 1 off-axis, closer to one or two D178 carboxylate groups at a distance of 2.8-3.3 A, suggesting direct interaction of bound Ca2+ with the carboxylate side chain and blocking the pore. Drug-free Ca2+ binds near the central axis in a fully hydrated state, coordinated symmetrically by four D178 carboxylate side chains.

### Pore-blocking mechanism of phenylalkylamine binding

Phenylalkylamines (verapamil, [Br-Verapamil](/xray-mp-wiki/reagents/ligands/br-verapamil)) bind in the central cavity of the pore on the intracellular side of the ion selectivity filter, physically blocking the ion-conducting pathway. Br-verapamil is stretched between two subunits, consistent with drug binding at the interface of domains III and IV in mammalian CaV1.2 channels. Binding is state-dependent: the IC50 for resting state block is 24 uM, 30-fold higher than after depolarizing stimuli (810 nM), revealing that access is greatly enhanced by opening the intracellular activation gate. Drug binding disrupts the fourfold symmetry of the pore, similar to dihydropyridine binding.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/navab/">NavAb Bacterial Voltage-Gated Sodium Channel</a> — Related bacterial voltage-gated channel with similar fold and selectivity filter architecture
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/">Ion Channel Selectivity Filter</a> — Paper provides detailed structural analysis of CaVAb selectivity filter
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-ion-coordination/">Intramembrane Ion Coordination</a> — Paper reveals Ca2+ coordination geometry at selectivity filter sites
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a> — Crystallization method used for structure determination
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system">Baculovirus Expression System</a> — Expression system used for protein production
- <a href="/xray-mp-wiki/reagents/ligands/amlodipine">Amlodipine</a> — Ligand or small molecule used in this study
- <a href="/xray-mp-wiki/reagents/additives/egta">Egta</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/ligands/br-verapamil">Br Verapamil</a> — Ligand or small molecule used in this study
- <a href="/xray-mp-wiki/reagents/ligands/uk-59811">Uk 59811</a> — Ligand or small molecule used in this study
- <a href="/xray-mp-wiki/reagents/buffers/tris">Tris Hcl</a> — Buffer component in purification and crystallization
