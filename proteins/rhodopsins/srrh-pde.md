---
title: "Rhodopsin Phosphodiesterase (Rh-PDE) from Salpingoeca rosetta"
created: 2026-06-22
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-19376-7]
verified: false
---

# Rhodopsin Phosphodiesterase (Rh-PDE) from Salpingoeca rosetta

## Overview

Rhodopsin phosphodiesterase (Rh-PDE) is an enzyme rhodopsin from the
choanoflagellate Salpingoeca rosetta (SrRh-PDE). It consists of an
N-terminal rhodopsin domain and a C-terminal phosphodiesterase (PDE)
domain connected by a 76-residue linker. Rh-PDE hydrolyzes both cAMP
and cGMP in a light-dependent manner, with ~2-fold light-induced
activation. The crystal structure revealed a new 8-TM rhodopsin
topology, including an N-terminal extra transmembrane helix TM0.
Rh-PDE has potential for optogenetic manipulation of cyclic nucleotide
concentrations.


## Publications

### doi/10.1038##s41467-020-19376-7

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7cj3">7CJ3</a></td>
      <td>2.6</td>
      <td>—</td>
      <td>SrRh-PDE TMD (residues 33-316), C-terminal GFP-His6, TEV cleaved</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7cj3">7CJ3</a></td>
      <td>3.5</td>
      <td>—</td>
      <td>SrRh-PDE TMD-Linker (residues 33-378), C-terminal GFP-His6, TEV cleaved</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7cj3">7CJ3</a></td>
      <td>2.1</td>
      <td>—</td>
      <td>SrRh-PDE Linker-PDE domain, C-terminal His8, TEV cleaved</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnTI- cells (TMD/TMD-Linker); Rosetta2 (DE3) E. coli (PDE domain)
- **Construct**: SrRh-PDE TMD (aa 33-316) and TMD-Linker (aa 33-378) in pEG BacMam vector with C-terminal GFP-His6 tag and TEV cleavage site; PDE domain in modified pEG-CGFP-BC vector with C-terminal His8 tag and TEV cleavage site
- **Induction**: 0.2 µg/mL anhydrotetracycline (E. coli); BacMam transduction (HEK)
- **Media**: DMEM with FBS and penicillin-streptomycin (HEK)

**Purification:**

- **Expression system**: HEK293S GnTI-
- **Expression construct**: SrRh-PDE TMD (aa 33-316) or TMD-Linker (aa 33-378) with C-terminal GFP-His6, TEV cleaved
- **Tag info**: GFP-His6, removed by TEV cleavage

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
      <td>Cell disruption</td>
      <td>Sonication</td>
      <td>—</td>
      <td>20 mM Tris pH 8.0, 200 mM NaCl, 20% glycerol, 100 µM all-trans retinal</td>
      <td>Supplemented with 100 µM all-trans retinal (Sigma)</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>20 mM Tris pH 8.0, 200 mM NaCl, 20% glycerol</td>
      <td>185,500×g, 1 h, 4°C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>20 mM Tris pH 8.0, 200 mM NaCl, 10 mM MgCl2, 20% glycerol + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>1 h at 4°C</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> metal affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Metal Affinity Resin (Clontech)</td>
      <td>20 mM Tris pH 8.0, 500 mM NaCl, 10 mM MgCl2, 15 mM imidazole, 10% glycerol + 0.1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>30 min incubation at 4°C</td>
    </tr>
    <tr>
      <td>TEV cleavage</td>
      <td>Protease digestion</td>
      <td>—</td>
      <td></td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease treatment to remove GFP-His6 tag</td>
    </tr>
    <tr>
      <td>Reverse affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> (flow-through)</td>
      <td>—</td>
      <td></td>
      <td>Remove <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease and cleaved tag</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase column</td>
      <td>20 mM Tris pH 8.0, 150 mM NaCl + 0.1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: ~10 mg/mL in SEC buffer

- **Expression system**: Rosetta2 (DE3) E. coli
- **Expression construct**: SrRh-PDE PDE domain with C-terminal His8, TEV cleaved
- **Tag info**: His8, removed by TEV cleavage

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
      <td>Cell disruption</td>
      <td>Sonication</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 100 mM NaCl, 10 mM MgCl2, 20 mM imidazole</td>
      <td></td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin (Qiagen)</td>
      <td>50 mM Tris pH 8.0, 100 mM NaCl, 10 mM MgCl2, 200 mM imidazole (elution)</td>
      <td>Wash with buffer A, elute with 200 mM imidazole</td>
    </tr>
    <tr>
      <td>TEV cleavage and dialysis</td>
      <td>Protease digestion + dialysis</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 100 mM NaCl, 10 mM MgCl2</td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease treatment, then dialyzed</td>
    </tr>
    <tr>
      <td>Reverse affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> (flow-through)</td>
      <td>—</td>
      <td></td>
      <td>Remove <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease and His8 tag</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>HiLoad 16/600 <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> pg (GE Healthcare)</td>
      <td>50 mM Tris pH 8.0, 100 mM NaCl, 10 mM MgCl2</td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: 10 mg/mL for crystallization

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SrRh-PDE TMD or TMD-Linker in <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> buffer</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Overnight</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained for TMD (2.6 Å) and TMD-Linker (3.5 Å)</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SrRh-PDE Linker-PDE, 10 mg/mL in 50 mM Tris pH 8.0, 100 mM NaCl, 10 mM MgCl2</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>29% (v/v) PEG400, 50 mM calcium acetate pH 5.0, 200 mM NaCl</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1 week</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>15% ethylene glycol</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in dark; data collected at SPring-8 BL32XU</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cj3">7CJ3</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGRGKRRAKTRNIAIAS</span><span class="topo-outside">TKE</span><span class="topo-membrane">VQWQGIFMIIVWLCVMGSLIF</span><span class="topo-inside">FAN</span><span class="topo-unknown">PEASRRVFAK</span><span class="topo-inside">FSHL</span><span class="topo-membrane">QS</span></span>
<span class="topo-line"><span class="topo-membrane">FYGATSVAFAFATGLDILAY</span><span class="topo-outside">VNAVSDEKRVL</span><span class="topo-membrane">SGILAYVDGVACISYLSMATL</span><span class="topo-inside">NLYFLVDS</span></span>
<span class="topo-line"><span class="topo-inside">TQGNPV</span><span class="topo-membrane">WLMRYAEWIITCPTLLYWCG</span><span class="topo-outside">LASRADR</span><span class="topo-membrane">SSVSDIATADALLLAGGALSS</span><span class="topo-inside">ILPSWP</span></span>
<span class="topo-line"><span class="topo-membrane">AFFVFAGSFATYIYVMLHMWGMF</span><span class="topo-outside">GKAMQPDFQPPPPLPRHA</span><span class="topo-membrane">LHLLRCEIVMSWSIFPLVE</span></span>
<span class="topo-line"><span class="topo-membrane">FLR</span><span class="topo-inside">RQGYIDFQV</span><span class="topo-membrane">GEAMNCVADYAAKVGLAMIMVN</span><span class="topo-outside">CNLEQ</span><span class="topo-unknown">INALRVENLYFQ</span></span>
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
      <td>18</td>
      <td>20</td>
      <td>49</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>41</td>
      <td>52</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>44</td>
      <td>73</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>54</td>
      <td>76</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>86</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>80</td>
      <td>90</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>91</td>
      <td>112</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>112</td>
      <td>123</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>126</td>
      <td>144</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>146</td>
      <td>158</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>153</td>
      <td>178</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>185</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>180</td>
      <td>206</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>203</td>
      <td>212</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>221</td>
      <td>235</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>243</td>
      <td>253</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>252</td>
      <td>275</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>274</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>279</td>
      <td>306</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cj3">7CJ3</a> — Chain B (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGRGKRRAKTRNIAI</span><span class="topo-outside">ASTK</span><span class="topo-membrane">EVQWQGIFMIIVWLCVMGSLIF</span><span class="topo-inside">FAN</span><span class="topo-unknown">PEASRRVFAK</span><span class="topo-inside">FSHL</span><span class="topo-membrane">QS</span></span>
<span class="topo-line"><span class="topo-membrane">FYGATSVAFAFATGLDILAY</span><span class="topo-outside">VNAVSDEKRV</span><span class="topo-membrane">LSGILAYVDGVACISYLSMATL</span><span class="topo-inside">NLYFLVDS</span></span>
<span class="topo-line"><span class="topo-inside">TQGNPV</span><span class="topo-membrane">WLMRYAEWIITCPTLLYWCGL</span><span class="topo-outside">ASRADR</span><span class="topo-membrane">SSVSDIATADALLLAGGALSS</span><span class="topo-inside">ILPSWP</span></span>
<span class="topo-line"><span class="topo-membrane">AFFVFAGSFATYIYVMLHMWGMFG</span><span class="topo-outside">KAMQPDFQPPPPLPRHA</span><span class="topo-membrane">LHLLRCEIVMSWSIFPLVE</span></span>
<span class="topo-line"><span class="topo-membrane">FLR</span><span class="topo-inside">RQGYIDFQV</span><span class="topo-membrane">GEAMNCVADYAAKVGLAMIMVN</span><span class="topo-outside">CNLEQ</span><span class="topo-unknown">INALRVENLYFQ</span></span>
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
      <td>16</td>
      <td>19</td>
      <td>47</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>41</td>
      <td>51</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>44</td>
      <td>73</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>54</td>
      <td>76</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>86</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>80</td>
      <td>90</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>112</td>
      <td>122</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>126</td>
      <td>144</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>147</td>
      <td>158</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>153</td>
      <td>179</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>185</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>180</td>
      <td>206</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>204</td>
      <td>212</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>221</td>
      <td>236</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>243</td>
      <td>253</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>252</td>
      <td>275</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>274</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>279</td>
      <td>306</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cj3">7CJ3</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGRGKRRAKTRNIAIAS</span><span class="topo-outside">TKE</span><span class="topo-membrane">VQWQGIFMIIVWLCVMGSLIF</span><span class="topo-inside">FAN</span><span class="topo-unknown">PEASRRVFAK</span><span class="topo-inside">FSHL</span><span class="topo-membrane">QS</span></span>
<span class="topo-line"><span class="topo-membrane">FYGATSVAFAFATGLDILAY</span><span class="topo-outside">VNAVSDEKRVL</span><span class="topo-membrane">SGILAYVDGVACISYLSMATL</span><span class="topo-inside">NLYFLVDS</span></span>
<span class="topo-line"><span class="topo-inside">TQGNPV</span><span class="topo-membrane">WLMRYAEWIITCPTLLYWCG</span><span class="topo-outside">LASRADR</span><span class="topo-membrane">SSVSDIATADALLLAGGALSS</span><span class="topo-inside">ILPSWP</span></span>
<span class="topo-line"><span class="topo-membrane">AFFVFAGSFATYIYVMLHMWGMF</span><span class="topo-outside">GKAMQPDFQPPPPLPRHA</span><span class="topo-membrane">LHLLRCEIVMSWSIFPLVE</span></span>
<span class="topo-line"><span class="topo-membrane">FLR</span><span class="topo-inside">RQGYIDFQV</span><span class="topo-membrane">GEAMNCVADYAAKVGLAMIMVN</span><span class="topo-outside">CNLEQ</span><span class="topo-unknown">INALRVENLYFQ</span></span>
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
      <td>18</td>
      <td>20</td>
      <td>49</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>41</td>
      <td>52</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>44</td>
      <td>73</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>54</td>
      <td>76</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>86</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>80</td>
      <td>90</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>91</td>
      <td>112</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>112</td>
      <td>123</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>126</td>
      <td>144</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>146</td>
      <td>158</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>153</td>
      <td>178</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>185</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>180</td>
      <td>206</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>203</td>
      <td>212</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>221</td>
      <td>235</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>243</td>
      <td>253</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>252</td>
      <td>275</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>274</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>279</td>
      <td>306</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cj3">7CJ3</a> — Chain B (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGRGKRRAKTRNIAI</span><span class="topo-outside">ASTK</span><span class="topo-membrane">EVQWQGIFMIIVWLCVMGSLIF</span><span class="topo-inside">FAN</span><span class="topo-unknown">PEASRRVFAK</span><span class="topo-inside">FSHL</span><span class="topo-membrane">QS</span></span>
<span class="topo-line"><span class="topo-membrane">FYGATSVAFAFATGLDILAY</span><span class="topo-outside">VNAVSDEKRV</span><span class="topo-membrane">LSGILAYVDGVACISYLSMATL</span><span class="topo-inside">NLYFLVDS</span></span>
<span class="topo-line"><span class="topo-inside">TQGNPV</span><span class="topo-membrane">WLMRYAEWIITCPTLLYWCGL</span><span class="topo-outside">ASRADR</span><span class="topo-membrane">SSVSDIATADALLLAGGALSS</span><span class="topo-inside">ILPSWP</span></span>
<span class="topo-line"><span class="topo-membrane">AFFVFAGSFATYIYVMLHMWGMFG</span><span class="topo-outside">KAMQPDFQPPPPLPRHA</span><span class="topo-membrane">LHLLRCEIVMSWSIFPLVE</span></span>
<span class="topo-line"><span class="topo-membrane">FLR</span><span class="topo-inside">RQGYIDFQV</span><span class="topo-membrane">GEAMNCVADYAAKVGLAMIMVN</span><span class="topo-outside">CNLEQ</span><span class="topo-unknown">INALRVENLYFQ</span></span>
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
      <td>16</td>
      <td>19</td>
      <td>47</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>41</td>
      <td>51</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>44</td>
      <td>73</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>54</td>
      <td>76</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>86</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>80</td>
      <td>90</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>112</td>
      <td>122</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>126</td>
      <td>144</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>147</td>
      <td>158</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>153</td>
      <td>179</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>185</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>180</td>
      <td>206</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>204</td>
      <td>212</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>221</td>
      <td>236</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>243</td>
      <td>253</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>252</td>
      <td>275</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>274</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>279</td>
      <td>306</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cj3">7CJ3</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGRGKRRAKTRNIAIAS</span><span class="topo-outside">TKE</span><span class="topo-membrane">VQWQGIFMIIVWLCVMGSLIF</span><span class="topo-inside">FAN</span><span class="topo-unknown">PEASRRVFAK</span><span class="topo-inside">FSHL</span><span class="topo-membrane">QS</span></span>
<span class="topo-line"><span class="topo-membrane">FYGATSVAFAFATGLDILAY</span><span class="topo-outside">VNAVSDEKRVL</span><span class="topo-membrane">SGILAYVDGVACISYLSMATL</span><span class="topo-inside">NLYFLVDS</span></span>
<span class="topo-line"><span class="topo-inside">TQGNPV</span><span class="topo-membrane">WLMRYAEWIITCPTLLYWCG</span><span class="topo-outside">LASRADR</span><span class="topo-membrane">SSVSDIATADALLLAGGALSS</span><span class="topo-inside">ILPSWP</span></span>
<span class="topo-line"><span class="topo-membrane">AFFVFAGSFATYIYVMLHMWGMF</span><span class="topo-outside">GKAMQPDFQPPPPLPRHA</span><span class="topo-membrane">LHLLRCEIVMSWSIFPLVE</span></span>
<span class="topo-line"><span class="topo-membrane">FLR</span><span class="topo-inside">RQGYIDFQV</span><span class="topo-membrane">GEAMNCVADYAAKVGLAMIMVN</span><span class="topo-outside">CNLEQ</span><span class="topo-unknown">INALRVENLYFQ</span></span>
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
      <td>18</td>
      <td>20</td>
      <td>49</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>41</td>
      <td>52</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>44</td>
      <td>73</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>54</td>
      <td>76</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>86</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>80</td>
      <td>90</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>91</td>
      <td>112</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>112</td>
      <td>123</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>126</td>
      <td>144</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>146</td>
      <td>158</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>153</td>
      <td>178</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>185</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>180</td>
      <td>206</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>203</td>
      <td>212</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>221</td>
      <td>235</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>243</td>
      <td>253</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>252</td>
      <td>275</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>274</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>279</td>
      <td>306</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cj3">7CJ3</a> — Chain B (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGRGKRRAKTRNIAI</span><span class="topo-outside">ASTK</span><span class="topo-membrane">EVQWQGIFMIIVWLCVMGSLIF</span><span class="topo-inside">FAN</span><span class="topo-unknown">PEASRRVFAK</span><span class="topo-inside">FSHL</span><span class="topo-membrane">QS</span></span>
<span class="topo-line"><span class="topo-membrane">FYGATSVAFAFATGLDILAY</span><span class="topo-outside">VNAVSDEKRV</span><span class="topo-membrane">LSGILAYVDGVACISYLSMATL</span><span class="topo-inside">NLYFLVDS</span></span>
<span class="topo-line"><span class="topo-inside">TQGNPV</span><span class="topo-membrane">WLMRYAEWIITCPTLLYWCGL</span><span class="topo-outside">ASRADR</span><span class="topo-membrane">SSVSDIATADALLLAGGALSS</span><span class="topo-inside">ILPSWP</span></span>
<span class="topo-line"><span class="topo-membrane">AFFVFAGSFATYIYVMLHMWGMFG</span><span class="topo-outside">KAMQPDFQPPPPLPRHA</span><span class="topo-membrane">LHLLRCEIVMSWSIFPLVE</span></span>
<span class="topo-line"><span class="topo-membrane">FLR</span><span class="topo-inside">RQGYIDFQV</span><span class="topo-membrane">GEAMNCVADYAAKVGLAMIMVN</span><span class="topo-outside">CNLEQ</span><span class="topo-unknown">INALRVENLYFQ</span></span>
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
      <td>16</td>
      <td>19</td>
      <td>47</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>41</td>
      <td>51</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>44</td>
      <td>73</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>54</td>
      <td>76</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>86</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>80</td>
      <td>90</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>112</td>
      <td>122</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>126</td>
      <td>144</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>147</td>
      <td>158</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>153</td>
      <td>179</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>185</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>180</td>
      <td>206</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>204</td>
      <td>212</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>221</td>
      <td>236</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>243</td>
      <td>253</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>252</td>
      <td>275</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>274</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>279</td>
      <td>306</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### 8-TM Rhodopsin Topology

The crystal structure revealed a new 8-TM topology for rhodopsins,
including an N-terminal extra transmembrane helix (TM0, residues
50-73) located between TM2 and TM3. TM0 interacts with TM2 and TM3
through hydrophobic interactions and a hydrogen bond between Trp63
and Ser136. TM0 stabilizes the overall folding of the TMD and
facilitates interactions with the retinal chromophore, playing a
crucial role in enzymatic photoactivity. Truncation of TM0 (Δ76)
abolished rhodopsin-related absorption.

### Photoactivation Mechanism

The retinal isomerization displaces TM7, followed by movement of
the linker region, inducing conformational change in the PDE
domain. Bulky hydrophobic residues between TM7 and the retinal
chromophore (Leu299, Met303) are critical for photoactivity.
Mutations of Met301 and Val304 at the dimer interface reduce
dimer stability and photoactivity. The intracellular loop ICL3
contains a Pro-rich PPPPLP sequence forming a right-handed helical
loop that limits TM7 movement. Unlike BR, Rh-PDE lacks pump or
channel activity due to replacement of key proton-transfer
residues (Asp96 replaced by Trp175) and protonated Glu164.

### Full-Length Model and Dimer Architecture

Combining the three crystal structures (TMD, TMD-Linker,
Linker-PDE) with HS-AFM observations and computational modeling,
a full-length model was proposed. The linker region forms a
dimeric, four-helical coiled-coil resembling a HAMP domain. The
TMD and PDE domains do not form direct interactions. Rh-PDE forms
a dimer under physiological conditions.


## Cross-References

- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/">Microbial Rhodopsins</a> — Rh-PDE belongs to the microbial rhodopsin family with a unique 8-TM topology
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/enzyme-rhodopsins/">Enzyme Rhodopsins</a> — Rh-PDE is a member of the enzyme rhodopsin class, with light-dependent enzymatic activity
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM (n-Dodecyl-β-D-Maltopyranoside)</a> — Used for membrane protein extraction and solubilization of Rh-PDE
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG (2,2-Didecylpropane-1,3-bis-β-D-maltopyranoside)</a> — Used during purification of Rh-PDE after solubilization
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Used as additive during solubilization and purification to stabilize Rh-PDE
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">All-trans Retinal</a> — Chromophore bound to Rh-PDE via Schiff base; essential for photoactivity
