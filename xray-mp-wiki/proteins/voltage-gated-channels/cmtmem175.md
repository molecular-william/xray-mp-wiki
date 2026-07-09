---
title: "CmTMEM175 — Prokaryotic TMEM175 Lysosomal Potassium Channel"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature23269]
verified: regex
uniprot_id: K9UJK2
---

# CmTMEM175 — Prokaryotic TMEM175 Lysosomal Potassium Channel

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/K9UJK2">UniProt: K9UJK2</a>

<span class="expr-badge">Chamaesiphon minutus PCC 6605</span>

## Overview

CmTMEM175 is a prokaryotic homologue of the lysosomal potassium channel TMEM175 from Chamaesiphon minutus. TMEM175 is a lysosomal K+ channel important for maintaining membrane potential and pH stability in lysosomes. Unlike canonical 6-TM tetrameric K+ channels, TMEM175 has no TVGYG selectivity filter motif and adopts a completely novel fold. The structure reveals that all six transmembrane helices are tightly packed within each subunit without domain swapping, with TM1 acting as the pore-lining inner helix. Three layers of hydrophobic residues (Ile23, Leu27, Leu30) form an hourglass-shaped ion permeation pathway, with the first isoleucine layer primarily responsible for K+ selectivity. The structure represents a novel architecture of a tetrameric cation channel with a distinct ion selectivity mechanism.


## Publications

### doi/10.1038##nature23269

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vre">5VRE</a></td>
      <td>3.3</td>
      <td>C2</td>
      <td>Full-length CmTMEM175 with N-terminal hexahistidine tag (removed by thrombin cleavage)</td>
      <td>none (apo)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21 (DE3)
- **Construct**: Full-length CmTMEM175 (NCBI WP_015160509.1) in pET15b vector with N-terminal hexahistidine tag and thrombin cleavage site

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
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.4, 200 mM KCl, 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, protease inhibitors (leupeptin, pepstatin A, DNaseI, aprotinin, <a href="/xray-mp-wiki/reagents/additives/pmsf/">Pmsf</a>) + n-Dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>3 h incubation at room temperature for protein extraction</td>
    </tr>
    <tr>
      <td>Immobilized metal affinity chromatography</td>
      <td>Co2+ affinity column</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> Co2+ affinity resin (Clontech)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.4, 200 mM KCl, 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 5-300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + n-Dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; His-tag removed by overnight thrombin digestion at 4 C</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (10/30 GL)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.4, 200 mM KCl, 3 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Purified in <a href="/xray-mp-wiki/reagents/detergents/dmng/">Dmng</a> for crystallization; CmTMEM175 elutes as monodispersed tetramer</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>6 mg/mL CmTMEM175 in <a href="/xray-mp-wiki/reagents/detergents/dmng/">Dmng</a> detergent</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>16-22% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 1000, 50 mM CaCl2, 50 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a>, 100 mM NaAc pH 4.6</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3 days to 2-4 weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Cryoprotected with 25% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 1000, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 50 mM CaCl2, 50 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/dmng/">Dmng</a>, 100 mM NaAc pH 4.6. Heavy atom derivatization with methyl <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury</a> chloride (CH3HgCl) for experimental phasing.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vre">5VRE</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVEAPE</span><span class="topo-outside">QSETGRIEAF</span><span class="topo-membrane">SDGVFAIAITLLVLEIKVP</span><span class="topo-inside">Q</span><span class="topo-unknown">HKIVETV</span><span class="topo-inside">GLVSSL</span><span class="topo-membrane">LSLWPSYLAFLTSFASILVMWVNH</span><span class="topo-outside">HRIFSLVARTDHAFFY</span><span class="topo-membrane">WNGLLLMLVTFVPFPTALLAEYLI</span><span class="topo-inside">HPQA</span><span class="topo-membrane">RVA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200   </span>
<span class="topo-line"><span class="topo-membrane">ASVYAGIFLAIAIVFNRL</span><span class="topo-outside">WKHAAT</span><span class="topo-unknown">ADRLLAQKA</span><span class="topo-outside">DRHEVDAITKQ</span><span class="topo-membrane">YRFGPGLYLVAFALSFIS</span><span class="topo-inside">V</span><span class="topo-membrane">WLSVGVCFVLAIYFALRS</span><span class="topo-outside">NA</span></span>
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
      <td>7</td>
      <td>16</td>
      <td>7</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>35</td>
      <td>17</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>36</td>
      <td>36</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>43</td>
      <td>37</td>
      <td>43</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>44</td>
      <td>49</td>
      <td>44</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>73</td>
      <td>50</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>89</td>
      <td>74</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>113</td>
      <td>90</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>117</td>
      <td>114</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>138</td>
      <td>118</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>144</td>
      <td>139</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>164</td>
      <td>154</td>
      <td>164</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>182</td>
      <td>165</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>183</td>
      <td>183</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>201</td>
      <td>184</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>203</td>
      <td>202</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vre">5VRE</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVEAPE</span><span class="topo-outside">QSETGRIEAF</span><span class="topo-membrane">SDGVFAIAITLLVLEIKVP</span><span class="topo-inside">Q</span><span class="topo-unknown">HKIVETV</span><span class="topo-inside">GLVSSL</span><span class="topo-membrane">LSLWPSYLAFLTSFASILVMWVNH</span><span class="topo-outside">HRIFSLVARTDHAFFY</span><span class="topo-membrane">WNGLLLMLVTFVPFPTALLAEYLI</span><span class="topo-inside">HPQA</span><span class="topo-membrane">RVA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200   </span>
<span class="topo-line"><span class="topo-membrane">ASVYAGIFLAIAIVFNRL</span><span class="topo-outside">WKHAAT</span><span class="topo-unknown">ADRLLAQKA</span><span class="topo-outside">DRHEVDAITKQ</span><span class="topo-membrane">YRFGPGLYLVAFALSFIS</span><span class="topo-inside">V</span><span class="topo-membrane">WLSVGVCFVLAIYFALRS</span><span class="topo-outside">NA</span></span>
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
      <td>7</td>
      <td>16</td>
      <td>7</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>35</td>
      <td>17</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>36</td>
      <td>36</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>43</td>
      <td>37</td>
      <td>43</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>44</td>
      <td>49</td>
      <td>44</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>73</td>
      <td>50</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>89</td>
      <td>74</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>113</td>
      <td>90</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>117</td>
      <td>114</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>138</td>
      <td>118</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>144</td>
      <td>139</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>164</td>
      <td>154</td>
      <td>164</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>182</td>
      <td>165</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>183</td>
      <td>183</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>201</td>
      <td>184</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>203</td>
      <td>202</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vre">5VRE</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVEAPE</span><span class="topo-outside">QSETGRIEAF</span><span class="topo-membrane">SDGVFAIAITLLVLEIKVP</span><span class="topo-inside">Q</span><span class="topo-unknown">HKIVETV</span><span class="topo-inside">GLVSSL</span><span class="topo-membrane">LSLWPSYLAFLTSFASILVMWVNH</span><span class="topo-outside">HRIFSLVARTDHAFFY</span><span class="topo-membrane">WNGLLLMLVTFVPFPTALLAEYLI</span><span class="topo-inside">HPQA</span><span class="topo-membrane">RVA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200   </span>
<span class="topo-line"><span class="topo-membrane">ASVYAGIFLAIAIVFNRL</span><span class="topo-outside">WKHAAT</span><span class="topo-unknown">ADRLLAQKA</span><span class="topo-outside">DRHEVDAITKQ</span><span class="topo-membrane">YRFGPGLYLVAFALSFIS</span><span class="topo-inside">V</span><span class="topo-membrane">WLSVGVCFVLAIYFALRS</span><span class="topo-outside">NA</span></span>
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
      <td>7</td>
      <td>16</td>
      <td>7</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>35</td>
      <td>17</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>36</td>
      <td>36</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>43</td>
      <td>37</td>
      <td>43</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>44</td>
      <td>49</td>
      <td>44</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>73</td>
      <td>50</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>89</td>
      <td>74</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>113</td>
      <td>90</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>117</td>
      <td>114</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>138</td>
      <td>118</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>144</td>
      <td>139</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>164</td>
      <td>154</td>
      <td>164</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>182</td>
      <td>165</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>183</td>
      <td>183</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>201</td>
      <td>184</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>203</td>
      <td>202</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vre">5VRE</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVEAPE</span><span class="topo-outside">QSETGRIEAF</span><span class="topo-membrane">SDGVFAIAITLLVLEIKVP</span><span class="topo-inside">Q</span><span class="topo-unknown">HKIVETV</span><span class="topo-inside">GLVSSL</span><span class="topo-membrane">LSLWPSYLAFLTSFASILVMWVNH</span><span class="topo-outside">HRIFSLVARTDHAFFY</span><span class="topo-membrane">WNGLLLMLVTFVPFPTALLAEYLI</span><span class="topo-inside">HPQA</span><span class="topo-membrane">RVA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200   </span>
<span class="topo-line"><span class="topo-membrane">ASVYAGIFLAIAIVFNRL</span><span class="topo-outside">WKHAAT</span><span class="topo-unknown">ADRLLAQKA</span><span class="topo-outside">DRHEVDAITKQ</span><span class="topo-membrane">YRFGPGLYLVAFALSFIS</span><span class="topo-inside">V</span><span class="topo-membrane">WLSVGVCFVLAIYFALRS</span><span class="topo-outside">NA</span></span>
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
      <td>7</td>
      <td>16</td>
      <td>7</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>35</td>
      <td>17</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>36</td>
      <td>36</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>43</td>
      <td>37</td>
      <td>43</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>44</td>
      <td>49</td>
      <td>44</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>73</td>
      <td>50</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>89</td>
      <td>74</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>113</td>
      <td>90</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>117</td>
      <td>114</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>138</td>
      <td>118</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>144</td>
      <td>139</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>164</td>
      <td>154</td>
      <td>164</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>182</td>
      <td>165</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>183</td>
      <td>183</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>201</td>
      <td>184</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>203</td>
      <td>202</td>
      <td>203</td>
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

### Novel tetrameric potassium channel architecture

CmTMEM175 represents a completely new fold for tetrameric K+ channels. Unlike canonical 6-TM K+ channels (e.g., Kv channels), all six TM helices are tightly packed within each subunit without domain swapping. TM1 (not TM6) forms the pore-lining inner helix, and there is no separate pore helix or TVGYG selectivity filter motif. DALI structure search yielded no similar structures, confirming the novel architecture.

### Hydrophobic bottleneck as selectivity filter

Three layers of conserved hydrophobic residues (Ile23, Leu27, Leu30) on the C-terminal half of TM1 helices create a ~10 A-long bottleneck with ~3 A diameter at each constriction point. This narrow hydrophobic pathway serves as the ion selectivity filter. Mutagenesis shows that the first isoleucine layer (Ile23) is primarily responsible for K+ selectivity — replacement with asparagine abolishes K+/Cs+ selectivity.

### Hourglass-shaped ion conduction pathway

The four TM1 helices and their extended C-terminal tails create an hourglass-shaped ion permeation pathway. The N-terminal half of TM1 lines the cytosolic entrance with a negatively charged surface potential. No specifically bound ions were observed in the pathway even in crystals soaked with heavy monovalent or divalent cations.

### Conserved RxxxFSD motif for inter-subunit interactions

A conserved RxxxFSD motif (Arg18, Phe22, Ser26, Asp18) mediates key intra- and inter-subunit interactions important for tetramer assembly. Arg18 forms a salt bridge with Asp18 of the same subunit; Asp18 forms a hydrogen bond with Trp70; Phe22 participates in pi-pi stacking with Phe16 of the neighboring subunit.


## Cross-References

- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> — Referenced in the context of Hepes
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in the context of DDM
- <a href="/xray-mp-wiki/reagents/additives/pmsf/">Pmsf</a> — Referenced in the context of Pmsf
- <a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> — Referenced in the context of Talon
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in the context of Imidazole
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Referenced in the context of Superdex 200
- <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> — Referenced in the context of DM
- <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> — Referenced in the context of DM
- <a href="/xray-mp-wiki/reagents/detergents/dmng/">Dmng</a> — Referenced in the context of Dmng
- <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> — Referenced in the context of Peg
