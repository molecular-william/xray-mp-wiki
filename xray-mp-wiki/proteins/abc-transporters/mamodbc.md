---
title: "Methanosarcina acetivorans ModBC Molybdate/Tungstate ABC Transporter (MaModBC)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1156213]
verified: agent
uniprot_id: ['Q8TTZ3', 'Q8TTZ4']
---

# Methanosarcina acetivorans ModBC Molybdate/Tungstate ABC Transporter (MaModBC)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8TTZ3">UniProt: Q8TTZ3</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8TTZ4">UniProt: Q8TTZ4</a>

<span class="expr-badge">Methanosarcina acetivorans</span>

## Overview

The crystal structure of Methanosarcina acetivorans ModBC (MaModBC),
a binding protein-dependent ABC transporter specific for molybdate and
[Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/), reveals the structural basis of trans-inhibition. The transporter
consists of two transmembrane domains (TMDs, ModB subunits) forming the
translocation pathway, and two cytoplasmic nucleotide-binding domains (NBDs,
ModC subunits) with C-terminal regulatory domains (~120 amino acids each).
In the trans-inhibited state, molybdate or [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) binds to oxyanion
binding pockets at the interface of the regulatory domains, locking the
transporter in an inward-facing conformation with the NBDs separated and
ATP hydrolysis inhibited. This represents a feedback mechanism where
intracellular substrate accumulation downregulates further uptake.


## Publications

### doi/10.1126##science.1156213

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3d31">3D31</a></td>
      <td>3.0</td>
      <td>not specified</td>
      <td>Full-length MaModBC with bound <a href="/xray-mp-wiki/reagents/ligands/tungstate/">Tungstate (WO4 2-)</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tungstate/">Tungstate (WO4 2-)</a> (WO4^2-)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3d31">3D31</a></td>
      <td>3.5</td>
      <td>not specified</td>
      <td>Full-length MaModBC with bound <a href="/xray-mp-wiki/reagents/ligands/tungstate/">Tungstate (WO4 2-)</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tungstate/">Tungstate (WO4 2-)</a> (WO4^2-)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length MaModBC (ModB + ModC with regulatory domains)

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: Full-length MaModBC

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
      <td>Protein purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>—</td>
      <td></td>
      <td>Purified in detergent solution; detailed purification protocol in supporting online material</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified MaModBC in detergent solution with bound [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) for crystallization

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Co-crystallization with <a href="/xray-mp-wiki/reagents/ligands/tungstate/">Tungstate (WO4 2-)</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained by co-crystallization with <a href="/xray-mp-wiki/reagents/ligands/tungstate/">Tungstate (WO4 2-)</a>. Structure determined by three-wavelength MAD around tungsten edge. Diffraction data anisotropic, truncated to 3.0, 3.3, and 3.5 Å in three directions. Phases improved by solvent flattening and <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> averaging.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d31">3D31</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIEIESLSRKWKNFSLDNLSLKVESGEYFVILGPTGAGKTLFLELIAGFHVPDSGRILLDGKDVTDLSPEKHDIAFVYQNYSLFPHMNVKKNLEFGMRMKKIKDPKRVLDTARDLKIEHL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LDRNPLTLSGGEQQRVALARALVTNPKILLLDEPLSALDPRTQENAREMLSVLHKKNKLTVLHITHDQTEARIMADRIAVVMDGKLIQVGKPEEIFEKPVEGRVASFVGFENVLKGRVIS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">AEQGLLRIRVGEVVIDAAGDMEVGDQVYAFLRPENIALSKSSTQSSIRNSLQGRVTEAWVLGALVRVKVDCGVPLNVLITRRSAEEMELSPGVQIYARFKASSVHVLR</span></span>
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
      <td>1</td>
      <td>348</td>
      <td>1</td>
      <td>348</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d31">3D31</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIEIESLSRKWKNFSLDNLSLKVESGEYFVILGPTGAGKTLFLELIAGFHVPDSGRILLDGKDVTDLSPEKHDIAFVYQNYSLFPHMNVKKNLEFGMRMKKIKDPKRVLDTARDLKIEHL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LDRNPLTLSGGEQQRVALARALVTNPKILLLDEPLSALDPRTQENAREMLSVLHKKNKLTVLHITHDQTEARIMADRIAVVMDGKLIQVGKPEEIFEKPVEGRVASFVGFENVLKGRVIS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">AEQGLLRIRVGEVVIDAAGDMEVGDQVYAFLRPENIALSKSSTQSSIRNSLQGRVTEAWVLGALVRVKVDCGVPLNVLITRRSAEEMELSPGVQIYARFKASSVHVLR</span></span>
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
      <td>1</td>
      <td>348</td>
      <td>1</td>
      <td>348</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d31">3D31</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHHHHHSSGENLYFQGHMKAKNRKTRKFE</span><span class="topo-inside">PLTFV</span><span class="topo-membrane">FSFLLLVLFLFIFLTLSNMIFE</span><span class="topo-outside">QITED</span><span class="topo-unknown">FSGLVKAAG</span><span class="topo-outside">NRSVISSI</span><span class="topo-membrane">FLSLYAGFLATLLALLLGAPTG</span><span class="topo-inside">YILARFDFPGKR</span><span class="topo-membrane">LV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ESIIDVPVVVPHTVAGIAL</span><span class="topo-outside">LTVFGSRGLIGEPLESYIQFRDAL</span><span class="topo-membrane">PGIVVAMLFVSMPYLANSA</span><span class="topo-inside">REGFKSVDPRLENAARSLGAP</span><span class="topo-unknown">LWKAFFF</span><span class="topo-inside">VTLPLSARYL</span><span class="topo-membrane">LIGSVMTWARAISEFGAV</span><span class="topo-outside">VI</span></span>
<span class="topo-ruler">       250       260       270       280       290     </span>
<span class="topo-line"><span class="topo-outside">LAYYPMVGPTLIYDRFISYGLSASRPIA</span><span class="topo-membrane">VLLILVTLSIFLVIR</span><span class="topo-unknown">TLSAGWSIYDRD</span></span>
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
      <td>35</td>
      <td>-22</td>
      <td>12</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>40</td>
      <td>13</td>
      <td>17</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>62</td>
      <td>18</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>40</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>76</td>
      <td>45</td>
      <td>53</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>77</td>
      <td>84</td>
      <td>54</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>106</td>
      <td>62</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>118</td>
      <td>84</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>139</td>
      <td>96</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>163</td>
      <td>117</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>182</td>
      <td>141</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>160</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>210</td>
      <td>181</td>
      <td>187</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>220</td>
      <td>188</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>198</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>268</td>
      <td>216</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>283</td>
      <td>246</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>284</td>
      <td>295</td>
      <td>261</td>
      <td>272</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d31">3D31</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHHHHHSSGENLYFQGHMKAKNRKTRKFE</span><span class="topo-inside">PLTF</span><span class="topo-membrane">VFSFLLLVLFLFIFLTLSNMIFE</span><span class="topo-outside">QITED</span><span class="topo-unknown">FSGLVKAAG</span><span class="topo-outside">NRSVISSI</span><span class="topo-membrane">FLSLYAGFLATLLALLLGAPTG</span><span class="topo-inside">YILARFDFPGKR</span><span class="topo-membrane">LV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ESIIDVPVVVPHTVAGIAL</span><span class="topo-outside">LTVFGSRGLIGEPLESYIQFRDAL</span><span class="topo-membrane">PGIVVAMLFVSMPYLANSA</span><span class="topo-inside">REGFKSVDPRLENAARSLGAP</span><span class="topo-unknown">LWKAFFF</span><span class="topo-inside">VTLPLSARYL</span><span class="topo-membrane">LIGSVMTWARAISEFGAV</span><span class="topo-outside">VI</span></span>
<span class="topo-ruler">       250       260       270       280       290     </span>
<span class="topo-line"><span class="topo-outside">LAYYPMVGPTLIYDRFISYGLSASRPIA</span><span class="topo-membrane">VLLILVTLSIFLVIR</span><span class="topo-unknown">TLSAGWSIYDRD</span></span>
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
      <td>35</td>
      <td>-22</td>
      <td>12</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>39</td>
      <td>13</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>62</td>
      <td>17</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>40</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>76</td>
      <td>45</td>
      <td>53</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>77</td>
      <td>84</td>
      <td>54</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>106</td>
      <td>62</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>118</td>
      <td>84</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>139</td>
      <td>96</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>163</td>
      <td>117</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>182</td>
      <td>141</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>160</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>210</td>
      <td>181</td>
      <td>187</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>220</td>
      <td>188</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>198</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>268</td>
      <td>216</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>283</td>
      <td>246</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>284</td>
      <td>295</td>
      <td>261</td>
      <td>272</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d31">3D31</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIEIESLSRKWKNFSLDNLSLKVESGEYFVILGPTGAGKTLFLELIAGFHVPDSGRILLDGKDVTDLSPEKHDIAFVYQNYSLFPHMNVKKNLEFGMRMKKIKDPKRVLDTARDLKIEHL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LDRNPLTLSGGEQQRVALARALVTNPKILLLDEPLSALDPRTQENAREMLSVLHKKNKLTVLHITHDQTEARIMADRIAVVMDGKLIQVGKPEEIFEKPVEGRVASFVGFENVLKGRVIS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">AEQGLLRIRVGEVVIDAAGDMEVGDQVYAFLRPENIALSKSSTQSSIRNSLQGRVTEAWVLGALVRVKVDCGVPLNVLITRRSAEEMELSPGVQIYARFKASSVHVLR</span></span>
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
      <td>1</td>
      <td>348</td>
      <td>1</td>
      <td>348</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d31">3D31</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIEIESLSRKWKNFSLDNLSLKVESGEYFVILGPTGAGKTLFLELIAGFHVPDSGRILLDGKDVTDLSPEKHDIAFVYQNYSLFPHMNVKKNLEFGMRMKKIKDPKRVLDTARDLKIEHL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LDRNPLTLSGGEQQRVALARALVTNPKILLLDEPLSALDPRTQENAREMLSVLHKKNKLTVLHITHDQTEARIMADRIAVVMDGKLIQVGKPEEIFEKPVEGRVASFVGFENVLKGRVIS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">AEQGLLRIRVGEVVIDAAGDMEVGDQVYAFLRPENIALSKSSTQSSIRNSLQGRVTEAWVLGALVRVKVDCGVPLNVLITRRSAEEMELSPGVQIYARFKASSVHVLR</span></span>
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
      <td>1</td>
      <td>348</td>
      <td>1</td>
      <td>348</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d31">3D31</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHHHHHSSGENLYFQGHMKAKNRKTRKFE</span><span class="topo-inside">PLTFV</span><span class="topo-membrane">FSFLLLVLFLFIFLTLSNMIFE</span><span class="topo-outside">QITED</span><span class="topo-unknown">FSGLVKAAG</span><span class="topo-outside">NRSVISSI</span><span class="topo-membrane">FLSLYAGFLATLLALLLGAPTG</span><span class="topo-inside">YILARFDFPGKR</span><span class="topo-membrane">LV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ESIIDVPVVVPHTVAGIAL</span><span class="topo-outside">LTVFGSRGLIGEPLESYIQFRDAL</span><span class="topo-membrane">PGIVVAMLFVSMPYLANSA</span><span class="topo-inside">REGFKSVDPRLENAARSLGAP</span><span class="topo-unknown">LWKAFFF</span><span class="topo-inside">VTLPLSARYL</span><span class="topo-membrane">LIGSVMTWARAISEFGAV</span><span class="topo-outside">VI</span></span>
<span class="topo-ruler">       250       260       270       280       290     </span>
<span class="topo-line"><span class="topo-outside">LAYYPMVGPTLIYDRFISYGLSASRPIA</span><span class="topo-membrane">VLLILVTLSIFLVIR</span><span class="topo-unknown">TLSAGWSIYDRD</span></span>
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
      <td>35</td>
      <td>-22</td>
      <td>12</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>40</td>
      <td>13</td>
      <td>17</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>62</td>
      <td>18</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>40</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>76</td>
      <td>45</td>
      <td>53</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>77</td>
      <td>84</td>
      <td>54</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>106</td>
      <td>62</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>118</td>
      <td>84</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>139</td>
      <td>96</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>163</td>
      <td>117</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>182</td>
      <td>141</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>160</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>210</td>
      <td>181</td>
      <td>187</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>220</td>
      <td>188</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>198</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>268</td>
      <td>216</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>283</td>
      <td>246</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>284</td>
      <td>295</td>
      <td>261</td>
      <td>272</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d31">3D31</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHHHHHSSGENLYFQGHMKAKNRKTRKFE</span><span class="topo-inside">PLTF</span><span class="topo-membrane">VFSFLLLVLFLFIFLTLSNMIFE</span><span class="topo-outside">QITED</span><span class="topo-unknown">FSGLVKAAG</span><span class="topo-outside">NRSVISSI</span><span class="topo-membrane">FLSLYAGFLATLLALLLGAPTG</span><span class="topo-inside">YILARFDFPGKR</span><span class="topo-membrane">LV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ESIIDVPVVVPHTVAGIAL</span><span class="topo-outside">LTVFGSRGLIGEPLESYIQFRDAL</span><span class="topo-membrane">PGIVVAMLFVSMPYLANSA</span><span class="topo-inside">REGFKSVDPRLENAARSLGAP</span><span class="topo-unknown">LWKAFFF</span><span class="topo-inside">VTLPLSARYL</span><span class="topo-membrane">LIGSVMTWARAISEFGAV</span><span class="topo-outside">VI</span></span>
<span class="topo-ruler">       250       260       270       280       290     </span>
<span class="topo-line"><span class="topo-outside">LAYYPMVGPTLIYDRFISYGLSASRPIA</span><span class="topo-membrane">VLLILVTLSIFLVIR</span><span class="topo-unknown">TLSAGWSIYDRD</span></span>
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
      <td>35</td>
      <td>-22</td>
      <td>12</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>39</td>
      <td>13</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>62</td>
      <td>17</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>40</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>76</td>
      <td>45</td>
      <td>53</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>77</td>
      <td>84</td>
      <td>54</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>106</td>
      <td>62</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>118</td>
      <td>84</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>139</td>
      <td>96</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>163</td>
      <td>117</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>182</td>
      <td>141</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>160</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>210</td>
      <td>181</td>
      <td>187</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>220</td>
      <td>188</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>198</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>268</td>
      <td>216</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>283</td>
      <td>246</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>284</td>
      <td>295</td>
      <td>261</td>
      <td>272</td>
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

### Trans-Inhibition by Substrate Binding to Regulatory Domains

The regulatory domains appended to the C-terminus of the NBDs form two oxyanion binding pockets at their shared interface. Each pocket is contributed by residues from both regulatory domains. Key residues Ser286, Thr320, Ser323, and Lys340 serve as hydrogen bond donors. Binding of molybdate or [Tungstate (WO4 2-)](/xray-mp-wiki/reagents/ligands/tungstate/) to these pockets allosterically inhibits ATPase activity (Ki ~5 µM), locking the transporter in an inward-facing conformation with the catalytic RecA-like and helical subdomains of the NBDs separated by ~23 Å (compared to ~10 Å in the uninhibited AfModBC). This trans-inhibition provides feedback regulation where intracellular molybdate accumulation downregulates further import.

### Comparison with Other ABC Transporter Conformations

The structure reveals a more pronounced inward-facing conformation compared to the nucleotide-free AfModBC, with increased angles between the two TMDs and a larger distance between coupling helices. Cross-linking experiments using engineered cysteines at position 153 in AfModB demonstrated that ATP binding induces closure of the NBDs, forcing the cytoplasmic ends of TM helices together and converting the translocation pathway to an outward-facing conformation similar to MalFGK2. This provides biochemical support for the [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) in ABC transporters.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/trans-inhibition-in-abc-transporters/">Trans-Inhibition in ABC Transporters</a> — MaModBC is the structural prototype for trans-inhibition in ABC transporters
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — Related biological concept
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/ligands/tungstate/">Tungstate (WO4 2-)</a> — Related ligand or cofactor
