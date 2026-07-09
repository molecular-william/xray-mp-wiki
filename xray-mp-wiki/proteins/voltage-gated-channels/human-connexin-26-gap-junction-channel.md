---
title: "Human Connexin 26 (Cx26/GJB2) Gap Junction Channel"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.1038##nature07869]
verified: regex
uniprot_id: P29033
---

# Human Connexin 26 (Cx26/GJB2) Gap Junction Channel

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P29033">UniProt: P29033</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Connexin 26 (Cx26, also known as GJB2) is a member of the connexin family of gap junction proteins. Gap junctions consist of arrays of intercellular channels between adjacent cells that permit the exchange of ions, metabolites, nucleotides and small peptides. A gap junction channel is formed by end-to-end docking of two hemichannels (connexons), each composed of six connexin subunits. The crystal structure of the human Cx26 gap junction channel was determined at 3.5 Å resolution by X-ray crystallography, revealing the arrangement of the four transmembrane helices (TM1-TM4), two extracellular loops (E1 and E2), a cytoplasmic loop, an N-terminal helix (NTH), and a C-terminal segment. The pore features a positively charged cytoplasmic entrance, a funnel formed by six N-terminal helices that determines molecular size restriction, a negatively charged transmembrane pathway, and an extracellular cavity. The structure shows no obstructions along the pore, consistent with an open conformation at neutral pH without aminosulphonate buffer or divalent ions. The N termini have a central role in voltage-dependent gating (Vj gating), with Asp 2, Trp 3 and Met 34 forming key interactions that maintain the funnel in the open state.

## Publications

### doi/10.1038##nature07869

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2zw3">2ZW3</a></td>
      <td>3.50</td>
      <td>Not specified</td>
      <td>Full-length human Cx26 (residues 1-226, C-terminal segment not visible in map)</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 cells (baculovirus expression system)
- **Construct**: Full-length human Cx26 cloned into pBlueBac4.5 via BamHI/EcoRI, expressed using Bac-N-Blue system

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
      <td>1. Cell disruption</td>
      <td>Alkali buffer treatment</td>
      <td>—</td>
      <td>20 mM NaOH, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/egta/">EGTA</a>, 2 mM DTT</td>
      <td>Cells disrupted in alkali buffer followed by ultracentrifugation to isolate gap junction membrane fraction</td>
    </tr>
    <tr>
      <td>2. Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>10 mM CAPS (pH 10.5), 1 M NaCl, 10 mM DTT + 1-1.5% n-dodecyl-β-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membrane fraction solubilized in DDM-containing buffer</td>
    </tr>
    <tr>
      <td>3. Cation exchange chromatography</td>
      <td>Cation exchange resin</td>
      <td>—</td>
      <td>10 mM HEPES (pH 7.5), 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 2 mM DTT, 500-1000 mM NaCl</td>
      <td>Elution with NaCl gradient</td>
    </tr>
    <tr>
      <td>4. Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>—</td>
      <td>10 mM HEPES (pH 7.5), 200 mM NaCl, 2 mM DTT, 0.01% n-undecyl-β-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/n-undecyl-beta-d-maltoside/">UDM</a>)</td>
      <td>Protein concentrated to 30 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified Cx26 in 10 mM HEPES (pH 7.5), 200 mM NaCl, 2 mM DTT, 0.01% [UDM](/xray-mp-wiki/reagents/detergents/n-undecyl-beta-d-maltoside/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified Cx26 at 30 mg/mL in HEPES/NaCl/DTT/UDM buffer</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM potassium phosphate (pH 7.5), 100 mM KCl, 10 mM DTT, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/egta/">EGTA</a>, 16-18% <a href="/xray-mp-wiki/reagents/additives/peg200/">PEG200</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 °C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained by vapor diffusion at 4°C. Crystals dehydrated by gradually adding triethyleneglycol to 25-30% final concentration and flash frozen in liquid nitrogen. Ta6Br14 derivative prepared by soaking crystals in 1 mM Ta6Br14 overnight. Data collected at BL44XU, SPring-8 and X06SA, Swiss Light Source. Structure determination by multiple isomorphous replacement with SAD/MAD using Ta derivatives and SeMet labeling.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2zw3">2ZW3</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DWGTLQTILGGVNKHSTSIGKIW</span><span class="topo-membrane">LTVLFIFRIMILVVAAKEVWGDEQAD</span><span class="topo-inside">FVCNTLQPGCKNVCY</span><span class="topo-membrane">DHYFPISHIRLWALQLIFVSTPAL</span><span class="topo-outside">LVAMHVAYRRHEKKRKFIKG</span><span class="topo-unknown">EIKSEFKDIEE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220      </span>
<span class="topo-line"><span class="topo-unknown">IKTQ</span><span class="topo-outside">KVRIEGSLWWTYTSS</span><span class="topo-membrane">IFFRVIFEAAFMYVFYVMYD</span><span class="topo-inside">GFSMQRLVKCNAWPCPNTVDCFV</span><span class="topo-membrane">SRPTEKTVFTVFMIAVSGICILLNVT</span><span class="topo-outside">ELCYLLIRY</span><span class="topo-unknown">CSGKSKKPV</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>24</td>
      <td>2</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>65</td>
      <td>51</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>89</td>
      <td>66</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>109</td>
      <td>90</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>124</td>
      <td>110</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>125</td>
      <td>139</td>
      <td>125</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>159</td>
      <td>140</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>182</td>
      <td>160</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>208</td>
      <td>183</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>217</td>
      <td>209</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>226</td>
      <td>218</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2zw3">2ZW3</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DWGTLQTILGGVNKHSTSIGKIW</span><span class="topo-membrane">LTVLFIFRIMILVVAAKEVWGDEQAD</span><span class="topo-inside">FVCNTLQPGCKNVCY</span><span class="topo-membrane">DHYFPISHIRLWALQLIFVSTPAL</span><span class="topo-outside">LVAMHVAYRRHEKKRKFIKG</span><span class="topo-unknown">EIKSEFKDIEE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220      </span>
<span class="topo-line"><span class="topo-unknown">IKTQ</span><span class="topo-outside">KVRIEGSLWWTYTSS</span><span class="topo-membrane">IFFRVIFEAAFMYVFYVMYD</span><span class="topo-inside">GFSMQRLVKCNAWPCPNTVDCFV</span><span class="topo-membrane">SRPTEKTVFTVFMIAVSGICILLNVT</span><span class="topo-outside">ELCYLLIRY</span><span class="topo-unknown">CSGKSKKPV</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>24</td>
      <td>2</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>65</td>
      <td>51</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>89</td>
      <td>66</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>109</td>
      <td>90</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>124</td>
      <td>110</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>125</td>
      <td>139</td>
      <td>125</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>159</td>
      <td>140</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>182</td>
      <td>160</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>208</td>
      <td>183</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>217</td>
      <td>209</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>226</td>
      <td>218</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2zw3">2ZW3</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DWGTLQTILGGVNKHSTSIGKIW</span><span class="topo-membrane">LTVLFIFRIMILVVAAKEVWGDEQAD</span><span class="topo-inside">FVCNTLQPGCKNVCY</span><span class="topo-membrane">DHYFPISHIRLWALQLIFVSTPAL</span><span class="topo-outside">LVAMHVAYRRHEKKRKFIKG</span><span class="topo-unknown">EIKSEFKDIEE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220      </span>
<span class="topo-line"><span class="topo-unknown">IKTQ</span><span class="topo-outside">KVRIEGSLWWTYTSS</span><span class="topo-membrane">IFFRVIFEAAFMYVFYVMYD</span><span class="topo-inside">GFSMQRLVKCNAWPCPNTVDCFV</span><span class="topo-membrane">SRPTEKTVFTVFMIAVSGICILLNVT</span><span class="topo-outside">ELCYLLIRY</span><span class="topo-unknown">CSGKSKKPV</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>24</td>
      <td>2</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>65</td>
      <td>51</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>89</td>
      <td>66</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>109</td>
      <td>90</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>124</td>
      <td>110</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>125</td>
      <td>139</td>
      <td>125</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>159</td>
      <td>140</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>182</td>
      <td>160</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>208</td>
      <td>183</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>217</td>
      <td>209</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>226</td>
      <td>218</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2zw3">2ZW3</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DWGTLQTILGGVNKHSTSIGKIW</span><span class="topo-membrane">LTVLFIFRIMILVVAAKEVWGDEQAD</span><span class="topo-inside">FVCNTLQPGCKNVCY</span><span class="topo-membrane">DHYFPISHIRLWALQLIFVSTPAL</span><span class="topo-outside">LVAMHVAYRRHEKKRKFIKG</span><span class="topo-unknown">EIKSEFKDIEE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220      </span>
<span class="topo-line"><span class="topo-unknown">IKTQ</span><span class="topo-outside">KVRIEGSLWWTYTSS</span><span class="topo-membrane">IFFRVIFEAAFMYVFYVMYD</span><span class="topo-inside">GFSMQRLVKCNAWPCPNTVDCFV</span><span class="topo-membrane">SRPTEKTVFTVFMIAVSGICILLNVT</span><span class="topo-outside">ELCYLLIRY</span><span class="topo-unknown">CSGKSKKPV</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>24</td>
      <td>2</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>65</td>
      <td>51</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>89</td>
      <td>66</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>109</td>
      <td>90</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>124</td>
      <td>110</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>125</td>
      <td>139</td>
      <td>125</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>159</td>
      <td>140</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>182</td>
      <td>160</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>208</td>
      <td>183</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>217</td>
      <td>209</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>226</td>
      <td>218</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2zw3">2ZW3</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DWGTLQTILGGVNKHSTSIGKIW</span><span class="topo-membrane">LTVLFIFRIMILVVAAKEVWGDEQAD</span><span class="topo-inside">FVCNTLQPGCKNVCY</span><span class="topo-membrane">DHYFPISHIRLWALQLIFVSTPAL</span><span class="topo-outside">LVAMHVAYRRHEKKRKFIKG</span><span class="topo-unknown">EIKSEFKDIEE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220      </span>
<span class="topo-line"><span class="topo-unknown">IKTQ</span><span class="topo-outside">KVRIEGSLWWTYTSS</span><span class="topo-membrane">IFFRVIFEAAFMYVFYVMYD</span><span class="topo-inside">GFSMQRLVKCNAWPCPNTVDCFV</span><span class="topo-membrane">SRPTEKTVFTVFMIAVSGICILLNVT</span><span class="topo-outside">ELCYLLIRY</span><span class="topo-unknown">CSGKSKKPV</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>24</td>
      <td>2</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>65</td>
      <td>51</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>89</td>
      <td>66</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>109</td>
      <td>90</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>124</td>
      <td>110</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>125</td>
      <td>139</td>
      <td>125</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>159</td>
      <td>140</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>182</td>
      <td>160</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>208</td>
      <td>183</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>217</td>
      <td>209</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>226</td>
      <td>218</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2zw3">2ZW3</a> — Chain F (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DWGTLQTILGGVNKHSTSIGKIW</span><span class="topo-membrane">LTVLFIFRIMILVVAAKEVWGDEQAD</span><span class="topo-inside">FVCNTLQPGCKNVCY</span><span class="topo-membrane">DHYFPISHIRLWALQLIFVSTPAL</span><span class="topo-outside">LVAMHVAYRRHEKKRKFIKG</span><span class="topo-unknown">EIKSEFKDIEE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220      </span>
<span class="topo-line"><span class="topo-unknown">IKTQ</span><span class="topo-outside">KVRIEGSLWWTYTSS</span><span class="topo-membrane">IFFRVIFEAAFMYVFYVMYD</span><span class="topo-inside">GFSMQRLVKCNAWPCPNTVDCFV</span><span class="topo-membrane">SRPTEKTVFTVFMIAVSGICILLNVT</span><span class="topo-outside">ELCYLLIRY</span><span class="topo-unknown">CSGKSKKPV</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>24</td>
      <td>2</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>65</td>
      <td>51</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>89</td>
      <td>66</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>109</td>
      <td>90</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>124</td>
      <td>110</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>125</td>
      <td>139</td>
      <td>125</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>159</td>
      <td>140</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>182</td>
      <td>160</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>208</td>
      <td>183</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>217</td>
      <td>209</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>226</td>
      <td>218</td>
      <td>226</td>
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

### Overall architecture of the Cx26 gap junction channel

The structure reveals a hexameric connexon with four transmembrane helices (TM1-TM4), two extracellular loops (E1, E2), a cytoplasmic loop, an N-terminal helix (NTH), and a C-terminal segment. TM1 and TM2 face the pore interior, while TM3 and TM4 face the hydrophobic membrane environment. TM1, lined by residues including Lys41, Glu42 and Gly45 at its boundary with E1, is the major pore-lining helix. The pore has an inner diameter of 40 Å at the cytoplasmic entrance, narrowing to 14 Å at the funnel, and widening to 25 Å in the extracellular cavity.

### The pore funnel determines molecular size restriction

The funnel is formed by six N-terminal helices (NTHs) lining the channel wall, stabilized by a circular network of hydrogen bonds between Asp2 and the main chain of Thr5. The NTH is drawn to the inner wall of the channel via hydrophobic interactions between Trp3 of the NTH and Met34 of TM1 of the neighboring protomer. This interaction maintains the funnel in the open state with an inner diameter of 14 Å. The size and electrical character of side chains at positions 2, 3, 5, 6 and 9 have a strong effect on molecular cutoff and charge selectivity.

### Electrostatic environment of the permeation pathway

The permeation pathway consists of an intracellular channel entrance, a pore funnel, and an extracellular cavity. The cytoplasmic entrance features nine positively charged residues in TM2 and two in TM3, generating a positively charged environment that concentrates negatively charged molecules. The funnel surface is lined by N-terminal residues Asp2, Trp3, Thr5, Leu6 and Ile9. A negatively charged path (Asp46, Asp50) with a diameter of 20 Å is found at the extracellular membrane surface. These regions contribute to size restriction and charge selectivity.

### Voltage-dependent gating mechanism by N-terminal movement

The N termini function as the voltage sensor within the conductive pore. The Met34Thr deafness mutation disrupts the Trp3-Met34 interaction that anchors the NTH to the pore wall. The structure suggests that an inside positive transjunctional voltage (Vj) causes inward movement of Asp2, disrupting the Asp2-Thr5 hydrogen bond network and the Trp3-Met34 interaction. The released NTHs could then assemble into a plug that physically blocks the pore. Release of any one of the six NTHs would break the circular hydrogen bond network, resulting in subconductance states. This is consistent with the observation that conformational change of a single subunit is sufficient to initiate Vj gating.

### Intercellular junction architecture

The two adjoining connexons interact through both E1 and E2 extracellular loops. In E1, Asn54 and Gln57 form symmetric hydrogen bonds with the opposite protomer. In E2, Lys168, Asp179, Thr177 and Asn176 form hydrogen bonds and salt bridges with the opposite protomer. These interactions create a tight double-layered wall bridging the 40 Å extracellular gap, separating the channel interior from the extracellular environment. Cys53-Cys180 and Cys60-Cys174 disulfide bonds stabilize the E1-E2 loop arrangement within each protomer.


## Cross-References

- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/egta/">EGTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg200/">PEG200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/n-undecyl-beta-d-maltoside/">UDM</a> — Detergent used in purification or crystallization
