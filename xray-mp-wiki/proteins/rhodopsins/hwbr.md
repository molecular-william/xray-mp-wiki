---
title: "Haloquadratum walsbyi Bacteriorhodopsin (HwBR)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2016.12.004, doi/10.1074##jbc.M115.685065]
verified: agent
uniprot_id: Q18DH8
---

# Haloquadratum walsbyi Bacteriorhodopsin (HwBR)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q18DH8">UniProt: Q18DH8</a>

<span class="expr-badge">Haloquadratum walsbyi</span>

## Overview

HwBR is a light-driven proton pump from the square halophilic archaeon Haloquadratum walsbyi,
belonging to the microbial rhodopsin family. The protein comprises seven transmembrane helices
and contains an all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore covalently bound via a Schiff base to Lys224.
Two crystal structures were solved: a trimeric form at 1.85 A resolution and an antiparallel
dimeric form at 2.58 A resolution (PDB 4QI1; Hsu et al., JBC 2015), both in space group C2
using [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/). HwBR could not be classified into any existing
subgroup of archaeal BR proteins based on phylogeny, and was assigned to a new subfamily
named qR (along with HmBRII from Haloarcula marismortui). All structures revealed a unique
hydrogen-bonding network between Arg82 and Thr201 linking the BC and FG loops to shield the
retinal-binding pocket from the extracellular environment, which explains HwBR's remarkable
optical stability under acidic conditions (pH 2-8). The Arg82-Thr201 cap acts as a proton
shield, maintaining the protonation status of the retinal-binding pocket interior even at
low pH values. This was validated by R82E mutation which attenuated optical stability
(pKa shifted from 1.97 to 2.24). HwBR functions as a light-driven proton pump and the
conserved Asp104 (equivalent to Asp96 in HsBR) serves as the proton uptake accelerator.
HwBR was also used as a model membrane protein to demonstrate the SMA-LCP crystallization
approach (Broecker et al., Structure 2017), yielding a 2.0 A structure (PDB 5ITC) virtually
identical to the detergent-based structure.

## Publications

### doi/10.1016##j.str.2016.12.004

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5itc">5ITC</a></td>
      <td>2.0 A</td>
      <td>P3</td>
      <td>Full-length HwBR from Haloquadratum walsbyi, solubilized and purified in SMA copolymer nanodiscs, crystallized in LCP</td>
      <td>all-trans-<a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (covalently bound to Lys224 via Schiff base)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ite">5ITE</a></td>
      <td>2.2 A</td>
      <td>P3</td>
      <td>Full-length HwBR, detergent-based purification in OG micelles, crystallized in LCP</td>
      <td>all-trans-<a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (covalently bound to Lys224 via Schiff base)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length HwBR with double [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/)

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
      <td>Differential centrifugation</td>
      <td>--</td>
      <td>Breakage buffer (composition not fully specified) + --</td>
      <td>E. coli inner cell membranes isolated by differential centrifugation</td>
    </tr>
    <tr>
      <td>Solubilization (SMA approach)</td>
      <td>SMA copolymer solubilization</td>
      <td>--</td>
      <td>Breakage buffer with <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a> addition + SMA copolymer (styrene-maleic acid)</td>
      <td>Membranes solubilized with SMA copolymers. Externally added <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a> (1,2-dimyristoyl-sn-glycero-3-phosphocholine) increased solubilization yield to close to that of <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> solubilization.</td>
    </tr>
    <tr>
      <td>IMAC</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> Superflow (QIAGEN)</td>
      <td>50 mM Tris pH 8, 100 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + SMA (nanodisc-embedded)</td>
      <td>Double <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a> enabled efficient separation of HwBR-containing SMA nanodiscs from empty nanodiscs. Washed with 10 CV breakage buffer and 10 CV wash buffer. Eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>.</td>
    </tr>
    <tr>
      <td>SEC</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL (GE Healthcare)</td>
      <td>Breakage buffer + SMA (nanodisc-embedded)</td>
      <td>Concentrated in 100 kDa MWCO centrifugal filter unit. Fractions with A550nm signal collected and concentrated to ~13 mg/mL.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization - SMA-LCP approach</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>HwBR in SMA nanodiscs at ~13 mg/mL</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested from LCP and cryocooled</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein in SMA nanodiscs was mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> at 2:3 (v/v) protein-to-lipid ratio (60% hydration). LCP bolus remained non-birefringent. Increased LCP viscosity observed with SMA approach. Several hundred conditions screened. Slight protocol modifications needed for LCP robot dispensing and crystal harvesting. Data collection at APS beamlines.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization - detergent approach (reference)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>HwBR in OG micelles at ~15.5 mg/mL</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested from LCP and cryocooled</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Reference structure. Protein purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> micelles and OG micelles, then transferred into <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> LCP.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5itc">5ITC</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAQLALQMSS</span><span class="topo-outside">LGVEGEG</span><span class="topo-membrane">IWLALGTIGMLLGMLYFIA</span><span class="topo-inside">DGLDVQDPRQKEFYV</span><span class="topo-membrane">ITILIPAIAAASYLSMFF</span><span class="topo-outside">GFGLTEVSLANGRVVDVY</span><span class="topo-membrane">WARYADWLFTTPLLLL</span><span class="topo-inside">DIGLLAGASQRDIG</span><span class="topo-membrane">ALV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GIDAFMIVTGLVATLT</span><span class="topo-outside">KVVVA</span><span class="topo-membrane">RYAFWTISTISMVFLLYYL</span><span class="topo-inside">VAVFGEAVSDADEDTRSTFNAL</span><span class="topo-membrane">RNIILVTWAIYPVAWLVG</span><span class="topo-outside">TEGLALTGLYG</span><span class="topo-membrane">ETLLFMVLDLVAKVGFGFI</span><span class="topo-inside">LLRSRAIM</span><span class="topo-unknown">GG</span></span>
<span class="topo-ruler">       250       260        </span>
<span class="topo-line"><span class="topo-unknown">GSEPTPSAQETAADHHHHHHLEHHHHHH</span></span>
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
      <td>11</td>
      <td>17</td>
      <td>11</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>36</td>
      <td>18</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>51</td>
      <td>37</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>69</td>
      <td>52</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>70</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>103</td>
      <td>88</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>117</td>
      <td>104</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>118</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>141</td>
      <td>137</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>160</td>
      <td>142</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>211</td>
      <td>201</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>230</td>
      <td>212</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>238</td>
      <td>231</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5itc">5ITC</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAQLALQMSS</span><span class="topo-outside">LGVEGEG</span><span class="topo-membrane">IWLALGTIGMLLGMLYFIA</span><span class="topo-inside">DGLDVQDPRQKEFYV</span><span class="topo-membrane">ITILIPAIAAASYLSMFF</span><span class="topo-outside">GFGLTEVSLANGRVVDVY</span><span class="topo-membrane">WARYADWLFTTPLLLL</span><span class="topo-inside">DIGLLAGASQRDIG</span><span class="topo-membrane">ALV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GIDAFMIVTGLVATLT</span><span class="topo-outside">KVVVA</span><span class="topo-membrane">RYAFWTISTISMVFLLYYL</span><span class="topo-inside">VAVFGEAVSDADEDTRSTFNAL</span><span class="topo-membrane">RNIILVTWAIYPVAWLVG</span><span class="topo-outside">TEGLALTGLYG</span><span class="topo-membrane">ETLLFMVLDLVAKVGFGFI</span><span class="topo-inside">LLRSRAIM</span><span class="topo-unknown">GG</span></span>
<span class="topo-ruler">       250       260        </span>
<span class="topo-line"><span class="topo-unknown">GSEPTPSAQETAADHHHHHHLEHHHHHH</span></span>
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
      <td>11</td>
      <td>17</td>
      <td>11</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>36</td>
      <td>18</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>51</td>
      <td>37</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>69</td>
      <td>52</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>70</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>103</td>
      <td>88</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>117</td>
      <td>104</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>118</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>141</td>
      <td>137</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>160</td>
      <td>142</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>211</td>
      <td>201</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>230</td>
      <td>212</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>238</td>
      <td>231</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5itc">5ITC</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAQLALQMSS</span><span class="topo-outside">LGVEGEG</span><span class="topo-membrane">IWLALGTIGMLLGMLYFIA</span><span class="topo-inside">DGLDVQDPRQKEFYV</span><span class="topo-membrane">ITILIPAIAAASYLSMFF</span><span class="topo-outside">GFGLTEVSLANGRVVDV</span><span class="topo-membrane">YWARYADWLFTTPLLLL</span><span class="topo-inside">DIGLLAGASQRDIG</span><span class="topo-membrane">ALV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GIDAFMIVTGLVATLT</span><span class="topo-outside">KVVV</span><span class="topo-membrane">ARYAFWTISTISMVFLLYYL</span><span class="topo-inside">VAVFGEAVSDADEDTRSTFNAL</span><span class="topo-membrane">RNIILVTWAIYPVAWLVG</span><span class="topo-outside">TEGLALTGLYG</span><span class="topo-membrane">ETLLFMVLDLVAKVGFGFI</span><span class="topo-inside">LLRSRAIM</span><span class="topo-unknown">GG</span></span>
<span class="topo-ruler">       250       260        </span>
<span class="topo-line"><span class="topo-unknown">GSEPTPSAQETAADHHHHHHLEHHHHHH</span></span>
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
      <td>11</td>
      <td>17</td>
      <td>11</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>36</td>
      <td>18</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>51</td>
      <td>37</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>69</td>
      <td>52</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>86</td>
      <td>70</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>87</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>117</td>
      <td>104</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>118</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>140</td>
      <td>137</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>160</td>
      <td>141</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>211</td>
      <td>201</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>230</td>
      <td>212</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>238</td>
      <td>231</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ite">5ITE</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAQLALQMSS</span><span class="topo-outside">LGVEGEG</span><span class="topo-membrane">IWLALGTIGMLLGMLYFIAD</span><span class="topo-inside">GLDVQDPRQKEFY</span><span class="topo-membrane">VITILIPAIAAASYLSMFF</span><span class="topo-outside">GFGLTEVSLANGRVVDVY</span><span class="topo-membrane">WARYADWLFTTPLLLLD</span><span class="topo-inside">IGLLAGASQRDIG</span><span class="topo-membrane">ALV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GIDAFMIVTGLVATLT</span><span class="topo-outside">KVVVA</span><span class="topo-membrane">RYAFWTISTISMVFLLYYL</span><span class="topo-inside">VAVFGEAVSDADEDTRSTFNAL</span><span class="topo-membrane">RNIILVTWAIYPVAWLVG</span><span class="topo-outside">TEGLALTGLYG</span><span class="topo-membrane">ETLLFMVLDLVAKVGFGFI</span><span class="topo-inside">LLRSRAIM</span><span class="topo-unknown">GG</span></span>
<span class="topo-ruler">       250       260        </span>
<span class="topo-line"><span class="topo-unknown">GSEPTPSAQETAADLVPRGSLEHHHHHH</span></span>
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
      <td>11</td>
      <td>17</td>
      <td>11</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>37</td>
      <td>18</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>50</td>
      <td>38</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>69</td>
      <td>51</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>70</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>104</td>
      <td>88</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>117</td>
      <td>105</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>118</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>141</td>
      <td>137</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>160</td>
      <td>142</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>211</td>
      <td>201</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>230</td>
      <td>212</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>238</td>
      <td>231</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ite">5ITE</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAQLALQMSS</span><span class="topo-outside">LGVEGEG</span><span class="topo-membrane">IWLALGTIGMLLGMLYFIAD</span><span class="topo-inside">GLDVQDPRQKEFY</span><span class="topo-membrane">VITILIPAIAAASYLSMFF</span><span class="topo-outside">GFGLTEVSLANGRVVDVY</span><span class="topo-membrane">WARYADWLFTTPLLLLD</span><span class="topo-inside">IGLLAGASQRDIG</span><span class="topo-membrane">ALV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GIDAFMIVTGLVATLT</span><span class="topo-outside">KVVVA</span><span class="topo-membrane">RYAFWTISTISMVFLLYYL</span><span class="topo-inside">VAVFGEAVSDADEDTRSTFNAL</span><span class="topo-membrane">RNIILVTWAIYPVAWLVG</span><span class="topo-outside">TEGLALTGLYG</span><span class="topo-membrane">ETLLFMVLDLVAKVGFGFI</span><span class="topo-inside">LLRSRAIM</span><span class="topo-unknown">GG</span></span>
<span class="topo-ruler">       250       260        </span>
<span class="topo-line"><span class="topo-unknown">GSEPTPSAQETAADLVPRGSLEHHHHHH</span></span>
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
      <td>11</td>
      <td>17</td>
      <td>11</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>37</td>
      <td>18</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>50</td>
      <td>38</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>69</td>
      <td>51</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>70</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>104</td>
      <td>88</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>117</td>
      <td>105</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>118</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>141</td>
      <td>137</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>160</td>
      <td>142</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>211</td>
      <td>201</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>230</td>
      <td>212</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>238</td>
      <td>231</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ite">5ITE</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAQLALQMSS</span><span class="topo-outside">LGVEGEG</span><span class="topo-membrane">IWLALGTIGMLLGMLYFIAD</span><span class="topo-inside">GLDVQDPRQKEFY</span><span class="topo-membrane">VITILIPAIAAASYLSMFF</span><span class="topo-outside">GFGLTEVSLANGRVVDVY</span><span class="topo-membrane">WARYADWLFTTPLLLLD</span><span class="topo-inside">IGLLAGASQRDIG</span><span class="topo-membrane">ALV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GIDAFMIVTGLVATLT</span><span class="topo-outside">KVVVA</span><span class="topo-membrane">RYAFWTISTISMVFLLYYL</span><span class="topo-inside">VAVFGEAVSDADEDTRSTFNAL</span><span class="topo-membrane">RNIILVTWAIYPVAWLVG</span><span class="topo-outside">TEGLALTGLYG</span><span class="topo-membrane">ETLLFMVLDLVAKVGFGFI</span><span class="topo-inside">LLRSRAIM</span><span class="topo-unknown">GG</span></span>
<span class="topo-ruler">       250       260        </span>
<span class="topo-line"><span class="topo-unknown">GSEPTPSAQETAADLVPRGSLEHHHHHH</span></span>
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
      <td>11</td>
      <td>17</td>
      <td>11</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>37</td>
      <td>18</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>50</td>
      <td>38</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>69</td>
      <td>51</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>70</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>104</td>
      <td>88</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>117</td>
      <td>105</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>118</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>141</td>
      <td>137</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>160</td>
      <td>142</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>211</td>
      <td>201</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>230</td>
      <td>212</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>238</td>
      <td>231</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1074##jbc.M115.685065

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4qi1">4QI1</a></td>
      <td>1.85</td>
      <td>C2</td>
      <td>Wild-type HwBR, trimeric form, crystallized in LCP</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length HwBR with double [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4qi1">4QI1</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAQLALQMSS</span><span class="topo-outside">LGVEGEG</span><span class="topo-membrane">IWLALGTIGMLLGMLYFIAD</span><span class="topo-inside">GLDVQDPRQKEFY</span><span class="topo-membrane">VITILIPAIAAASYLSMFF</span><span class="topo-outside">GFGLTEVSLANGRVVDVY</span><span class="topo-membrane">WARYADWLFTTPLLLLD</span><span class="topo-inside">IGLLAGASQRDIG</span><span class="topo-membrane">ALV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GIDAFMIVTGLVATLT</span><span class="topo-outside">KVVV</span><span class="topo-membrane">ARYAFWTISTISMVFLLYYL</span><span class="topo-inside">VAVFGEAVSDADEDTRSTFNAL</span><span class="topo-membrane">RNIILVTWAIYPVAWLVG</span><span class="topo-outside">TEGLALTGLYG</span><span class="topo-membrane">ETLLFMVLDLVAKVGFGFI</span><span class="topo-inside">LLRSRAIM</span><span class="topo-unknown">GG</span></span>
<span class="topo-ruler">       250       260  </span>
<span class="topo-line"><span class="topo-unknown">GSEPTPSAQETAADLEHHHHHH</span></span>
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
      <td>11</td>
      <td>17</td>
      <td>11</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>37</td>
      <td>18</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>50</td>
      <td>38</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>69</td>
      <td>51</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>70</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>104</td>
      <td>88</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>117</td>
      <td>105</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>118</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>140</td>
      <td>137</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>160</td>
      <td>141</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>211</td>
      <td>201</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>230</td>
      <td>212</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>238</td>
      <td>231</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4qi1">4QI1</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAQLALQMSS</span><span class="topo-outside">LGVEGEG</span><span class="topo-membrane">IWLALGTIGMLLGMLYFIAD</span><span class="topo-inside">GLDVQDPRQKEFY</span><span class="topo-membrane">VITILIPAIAAASYLSMFF</span><span class="topo-outside">GFGLTEVSLANGRVVDVY</span><span class="topo-membrane">WARYADWLFTTPLLLLD</span><span class="topo-inside">IGLLAGASQRDIG</span><span class="topo-membrane">ALV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GIDAFMIVTGLVATLT</span><span class="topo-outside">KVVV</span><span class="topo-membrane">ARYAFWTISTISMVFLLYYL</span><span class="topo-inside">VAVFGEAVSDADEDTRSTFNAL</span><span class="topo-membrane">RNIILVTWAIYPVAWLVG</span><span class="topo-outside">TEGLALTGLYG</span><span class="topo-membrane">ETLLFMVLDLVAKVGFGFI</span><span class="topo-inside">LLRSRAIM</span><span class="topo-unknown">GG</span></span>
<span class="topo-ruler">       250       260  </span>
<span class="topo-line"><span class="topo-unknown">GSEPTPSAQETAADLEHHHHHH</span></span>
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
      <td>11</td>
      <td>17</td>
      <td>11</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>37</td>
      <td>18</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>50</td>
      <td>38</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>69</td>
      <td>51</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>70</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>104</td>
      <td>88</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>117</td>
      <td>105</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>118</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>140</td>
      <td>137</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>160</td>
      <td>141</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>211</td>
      <td>201</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>230</td>
      <td>212</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>238</td>
      <td>231</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4qi1">4QI1</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAQLALQMSS</span><span class="topo-outside">LGVEGEG</span><span class="topo-membrane">IWLALGTIGMLLGMLYFIAD</span><span class="topo-inside">GLDVQDPRQKEFY</span><span class="topo-membrane">VITILIPAIAAASYLSMFF</span><span class="topo-outside">GFGLTEVSLANGRVVDVY</span><span class="topo-membrane">WARYADWLFTTPLLLLD</span><span class="topo-inside">IGLLAGASQRDIG</span><span class="topo-membrane">ALV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GIDAFMIVTGLVATLT</span><span class="topo-outside">KVVV</span><span class="topo-membrane">ARYAFWTISTISMVFLLYYL</span><span class="topo-inside">VAVFGEAVSDADEDTRSTFNAL</span><span class="topo-membrane">RNIILVTWAIYPVAWLVG</span><span class="topo-outside">TEGLALTGLYG</span><span class="topo-membrane">ETLLFMVLDLVAKVGFGFI</span><span class="topo-inside">LLRSRAIM</span><span class="topo-unknown">GG</span></span>
<span class="topo-ruler">       250       260  </span>
<span class="topo-line"><span class="topo-unknown">GSEPTPSAQETAADLEHHHHHH</span></span>
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
      <td>11</td>
      <td>17</td>
      <td>11</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>37</td>
      <td>18</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>50</td>
      <td>38</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>69</td>
      <td>51</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>70</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>104</td>
      <td>88</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>117</td>
      <td>105</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>118</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>140</td>
      <td>137</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>160</td>
      <td>141</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>211</td>
      <td>201</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>230</td>
      <td>212</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>238</td>
      <td>231</td>
      <td>238</td>
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

### HwBR belongs to a new qR subfamily with acid-resistant proton pumping

Based on phylogenetic analysis of BR protein sequences, HwBR and HmBRII were assigned
to a new subfamily named qR, distinct from existing bR, aR, dR, and cR subgroups.
HwBR showed remarkable optical stability across a wide pH range (pH 2-8), with a
pKa of 1.97 for the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base counterion — significantly lower than the
pKa of ~2.6 for HsBR. This contrasts with most BR proteins which exhibit a marked
red-shift in absorption maximum at acidic pH due to protonation of the Schiff base
proton acceptor (Asp85 in HsBR, Asp93 in HwBR). The D93N fully protonated mutant
showed lambda_max = 581 nm. Light-driven proton pump activity was confirmed using
a photocurrent device and pH electrode measurements.

### Unique Arg82-Thr201 hydrogen-bonding network acts as a proton shield

The 1.85 A crystal structure of HwBR revealed a unique hydrogen-bonding network
between Arg82 (located on the BC loop) and Thr201 (located on the FG loop in the
extracellular region). Two guanidinium nitrogen atoms of Arg82 form hydrogen bonds
with the main-chain carbonyl oxygen of Thr201, creating a beta-hairpin cap covering
the proton translocation channel exit site. This Arg82-Thr201 interaction has never
been observed in any other known BR protein, where the corresponding residues are
typically glutamic acid (e.g., Glu74 in HsBR). The R82E mutant showed a 21-nm red-shift
at pH 2 (lambda_max = 568 nm vs 559 nm for wild-type at pH 2) with an increased pKa of
2.24, confirming the cap's role in shielding the retinal-binding pocket from the
extracellular proton concentration. Time-dependent denaturation assays showed R82E/HwBR
had faster denaturation at pH 8 within 15 min, suggesting the cap contributes to overall
pH-dependent thermal stability.

### Negatively charged cytoplasmic surface drives proton uptake

Electrostatic analysis of HwBR revealed a negatively charged cytoplasmic side with
significantly enlarged surface area compared to other BR proteins. This negatively
charged region may drive the re-uptake of protons from the cytoplasm, potentially
increasing proton uptake efficiency. Combining the Arg82-Thr201 cap on the extracellular
side (protecting the retinal-binding pocket microenvironment) with the negatively charged
cytoplasmic surface (enhancing proton uptake), HwBR appears to be a highly efficient
proton pump optimized for acidic conditions.

### SMA-LCP crystallography preserves native structure

The 2.0 A structure of HwBR obtained from SMA nanodisc-LCP crystallization is virtually identical to the 2.2 A structure from detergent-based LCP crystallization (C-alpha RMSD 0.22 A for the trimer). All key structural features are preserved, including the retinal-binding pocket, proton translocation path residues (Asp93, Glu202, Lys224), and the proton-releasing complex. The SMA copolymer does not compromise diffraction quality or electron density maps.

### Proton translocation pathway

HwBR pumps protons from the intracellular to extracellular side via a conserved mechanism. Key functional residues include Asp93 (proton re-uptake residue), Glu202 (proton-releasing complex), and Lys224 (Schiff base linkage to all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/)). The proton outward cap region involves hydrogen-bonded residues.


## Cross-References

- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — HwBR was crystallized in monoolein LCP for both detergent-based and SMA-based approaches
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — HwBR is a microbial rhodopsin proton pump with a photocycle mechanism
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> — All-trans-retinal chromophore covalently bound to Lys224
- <a href="/xray-mp-wiki/methods/solubilization/sma-nanodisc-purification/">SMA Nanodisc Purification</a> — Novel polymer-based solubilization and purification method demonstrated with HwBR
- <a href="/xray-mp-wiki/methods/crystallization/sma-lcp-crystallization/">SMA-LCP Crystallization</a> — Novel polymer-mediated in meso crystallization approach validated with HwBR
- <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a> — Synthetic phospholipid added to improve SMA solubilization efficiency
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-maltopyranoside (beta-DDM)</a> — Detergent used for reference purification and solubilization
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl beta-D-glucopyranoside (OG)</a> — Detergent used for reference purification and LCP crystallization
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/proton-pump-mechanism/">Proton Pump Mechanism</a> — HwBR is a light-driven proton pump with a unique Arg82-Thr201 extracellular cap that shields the retinal pocket at low pH
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/">Microbial Rhodopsins</a> — HwBR belongs to the qR subfamily of archaeal rhodopsins with acid-resistant optical properties
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — HwBR follows the conserved BR photocycle with Asp104 as the proton uptake accelerator
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> — All-trans-retinal chromophore covalently bound to Lys224 via Schiff base
- <a href="/xray-mp-wiki/concepts/pka-tuning/">pKa Tuning in Membrane Proteins</a> — The Arg82-Thr201 cap tunes the pKa of the Schiff base counterion from ~2.6 in HsBR to 1.97 in HwBR
