---
title: "AaWzmWzt (O Antigen ABC Transporter from Aquifex aeolicus)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-08646-8, doi/10.1016##j.str.2019.11.020]
verified: false
---

# AaWzmWzt (O Antigen ABC Transporter from Aquifex aeolicus)

## Overview

AaWzmWzt is an [ABC Transporter](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) from Aquifex aeolicus responsible for translocating O antigen polysaccharides across the inner membrane in Gram-negative bacteria. The ATP-bound crystal structure (EQ mutant) reveals a continuous transmembrane channel with lateral openings toward the periplasm. The structure shows large structural changes in NBDs and TMDs upon ATP binding, pushing conserved hydrophobic residues at the substrate entry site toward the periplasm. The channel's periplasmic exit is sealed by lipid molecules in a proposed lipid gating mechanism that maintains the membrane permeability barrier. The isolated carbohydrate-binding domain (CBD) of Wzt was determined at 2.65 A resolution, revealing a jelly-roll fold with beta strand exchange between protomers in the dimer. The CBD interacts with the O antigen polysaccharide and may regulate the transporter's ATPase activity.


## Publications

### doi/10.1038##s41467-019-08646-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6m96">6M96</a></td>
      <td>2.7</td>
      <td>—</td>
      <td>AaWzmWzt EQ mutant (E164Q)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/atp/">Adenosine Triphosphate (ATP)</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: EQ mutant (Walker B E164Q in Wzt)

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
      <td>Membrane preparation</td>
      <td>Microfluidizer lysis, <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 200,000 x g</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 7.5, 100 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> pH 7.2, 100 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> + 2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/c12e8/">Octaethylene Glycol Monododecyl Ether (C12E8)</a></td>
      <td>60 min at 4 C</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td>Immobilized metal-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> agarose</td>
      <td>Sequential washes with 22 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao">LDAO</a>, 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao">LDAO</a>, 1.5 M NaCl + 22 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao">LDAO</a></td>
      <td>Eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao">LDAO</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Gel filtration</a></td>
      <td>S200 <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">gel filtration</a> column (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 7.5, 100 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride (MgCl₂)</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">Tris(2-carboxyethyl)phosphine (TCEP)</a>, 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao">LDAO</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor diffusion</a>, <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion">sitting drop</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>7.5 mg/ml AaWzmWzt_EQ + 2 mM <a href="/xray-mp-wiki/reagents/ligands/atp/">Adenosine Triphosphate (ATP)</a> + 5 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride (MgCl₂)</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown with <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> and magnesium. <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a> and <a href="/xray-mp-wiki/reagents/detergents/ldao">LDAO</a> were used as detergents throughout purification.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m96">6M96</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MGIRVFDVWKKYKYYKKPQDRLKEIIFRKPFHEELWVLKGINLEIEKGEVLGIVGPNGAGKSTLLKVITGVTEPDKGFVERSGKVVGLLELGTGFNYELSGLENIYVNASLLGLSRREID</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EKLESIIEFSELDDFINKPLKTYSSGMIMRLAFSIAIHTEPECFIIDQALAVGDAHFQQKCFRKLKEHKQKGGSIIFVSHDMNAVKILCDRAILLHKGEIIEEGSPETVTQAYYKLKL</span><span class="topo-unknown">HH</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-unknown">HHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>238</td>
      <td>0</td>
      <td>237</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>244</td>
      <td>238</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m96">6M96</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MNLSLILELVRQEIKNRYADT</span><span class="topo-membrane">VLGIWWAFLWPILLVLIY</span><span class="topo-inside">TLIFSHLIGAKLGHENTVYAYSI</span><span class="topo-membrane">YLSSGIFPWFFFSNSLSRITG</span><span class="topo-outside">IFTEKKFLFTKIPIRLEVFPVVV</span><span class="topo-membrane">IISELINYLIGISL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VTLISFI</span><span class="topo-inside">TLGFEG</span><span class="topo-membrane">IKYFYLFPVALYLMIVYSFSIGMVLG</span><span class="topo-outside">TLNVFFRD</span><span class="topo-membrane">IKEIIGVFLQIFFWFTPIV</span><span class="topo-inside">YTLDILPPFVKK</span><span class="topo-unknown">LIYYNPMYPVVSIHHLVFV</span><span class="topo-inside">NYLDL</span><span class="topo-membrane">HLYSLLGFLLASPLVFFV</span></span>
<span class="topo-ruler">       250      </span>
<span class="topo-line"><span class="topo-membrane">S</span><span class="topo-outside">YYFFKKLEKDIKDFA</span></span>
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
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>39</td>
      <td>22</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>62</td>
      <td>40</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>83</td>
      <td>63</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>106</td>
      <td>84</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>127</td>
      <td>107</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>133</td>
      <td>128</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>159</td>
      <td>134</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>167</td>
      <td>160</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>186</td>
      <td>168</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>198</td>
      <td>187</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>217</td>
      <td>199</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>241</td>
      <td>223</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>256</td>
      <td>242</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m96">6M96</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MNLSLILELVRQEIKNRYADT</span><span class="topo-membrane">VLGIWWAFLWPILLVLIY</span><span class="topo-inside">TLIFSHLIGAKLGHENTVYAYSIYL</span><span class="topo-membrane">SSGIFPWFFFSNSLSRITG</span><span class="topo-outside">IFTEKKFLFTKIPIRLEVFP</span><span class="topo-membrane">VVVIISELINYLIGISL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VTLIS</span><span class="topo-inside">FITLGFEGIKYF</span><span class="topo-membrane">YLFPVALYLMIVYSFSIGMVLGTLN</span><span class="topo-outside">VFF</span><span class="topo-membrane">RDIKEIIGVFLQIFFWFT</span><span class="topo-inside">PIVYTLDILPPFVKKLI</span><span class="topo-unknown">YYNPMYPVVSIH</span><span class="topo-inside">HLVFVNYLDLHLYS</span><span class="topo-membrane">LLGFLLASPLVFFV</span></span>
<span class="topo-ruler">       250      </span>
<span class="topo-line"><span class="topo-membrane">SYYFF</span><span class="topo-outside">KKLEKDIKDFA</span></span>
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
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>39</td>
      <td>22</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>64</td>
      <td>40</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>83</td>
      <td>65</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>103</td>
      <td>84</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>125</td>
      <td>104</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>137</td>
      <td>126</td>
      <td>137</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>162</td>
      <td>138</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>165</td>
      <td>163</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>183</td>
      <td>166</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>200</td>
      <td>184</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>212</td>
      <td>201</td>
      <td>212</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>213</td>
      <td>226</td>
      <td>213</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>245</td>
      <td>227</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>246</td>
      <td>256</td>
      <td>246</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.str.2019.11.020

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6o14">6O14</a></td>
      <td>2.65</td>
      <td>Not specified</td>
      <td>Aa Wzt CBD (short construct, residues 245-395)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: EQ mutant (Walker B E164Q in Wzt)

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
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> agarose</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> HCl pH 8.5, 0.5 M NaCl, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a>, 5 mM beta-ME (wash 1); 25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> HCl pH 8.5, 50 mM NaCl, 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a>, 5 mM beta-ME (wash 2)</td>
      <td>CBD construct (residues 235-395) with C-terminal hexahistidine tag</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Gel filtration</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex-200</a></td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> HCl pH 8.5, 50 mM NaCl, 5 mM beta-ME</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor diffusion</a>, <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion">sitting drop</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>7.6 mg/ml Aa CBD (long construct, residues 235-395) or 3.7 mg/ml Aa CBD (short construct, residues 245-395)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M citric acid pH 5.5, 0.5 M tri-<a href="/xray-mp-wiki/reagents/buffers/citrate/">sodium citrate</a> (long construct); 0.1 M <a href="/xray-mp-wiki/reagents/buffers/mops/">MOPS</a> pH 7, 1.5 M <a href="/xray-mp-wiki/reagents/buffers/acetate/">sodium acetate</a> (short construct)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>27-30 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3 days to 3 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>25% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> (long construct); 3 M <a href="/xray-mp-wiki/reagents/buffers/acetate/">sodium acetate</a> (short construct)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Long construct crystallized as needle-shaped crystals diffracting to 3.6 A. Truncated construct (lacking 8 N-terminal residues) diffracted to 2.65 A and was used for refinement. Structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using E. coli O9a CBD (PDB 2R5O) as search model.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### CBD structure reveals dimeric jelly-roll fold

The Aa CBD forms a partially SDS-resistant dimer with each protomer adopting a jelly-roll fold. The dimer is stabilized by beta strand exchange between protomers: C-terminal residues of one protomer complete the jelly-roll fold of the other. The domain contains a conserved flat surface and a variable twisted jelly-roll surface.

### CBD interacts with O antigen via glycan array

Microbial glycan array binding studies with 313 LPS/O antigen structures identified selective binding to Pseudomonas aeruginosa 7a,7d O antigen. The CBD discriminates between 4-acetylated and unmodified FucNAc, suggesting specificity toward the natural O antigen cap structure.

### CBD-NBD interaction may regulate ATPase activity

The CBD likely contacts the NBD at a short alpha helix following the conserved H-loop. CBD binding could perturb the H-loop (containing His199), affecting the transporter's hydrolytic activity. The CBD may function to increase local O antigen concentration near the ABC transporter.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — WzmWzt is a type II ABC transporter for O antigen export
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/type-ii-abc-transporter-family/">Type II ABC Transporter Family</a> — WzmWzt is a member of the type II ABC transporter family
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/outward-facing-conformation/">Outward-Facing Conformation</a> — The ATP-bound structure represents the outward-facing state
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Ni-NTA affinity chromatography was used for purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — SEC was used as a final purification step
- <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a> — Detergent used for solubilization at 2% (w/v)
- <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> — Reducing agent in SEC buffer
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> — Reducing agent in purification buffers
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a> — Used in crystallization and SEC buffers
- <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> — Added for ATP-bound crystallization and structure determination
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Primary buffer component
- <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> — Buffer used during solubilization step
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used in Ni-NTA affinity chromatography buffers
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used for structure determination of the ATP-bound state
