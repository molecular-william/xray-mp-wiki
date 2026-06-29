---
title: "Thermus thermophilus SecG Accessory Subunit"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2015.10.025]
verified: false
---

# Thermus thermophilus SecG Accessory Subunit

## Overview

SecG is an accessory subunit of the bacterial Sec translocon that comprises two transmembrane helices (TM1 and TM2) connected by a large cytoplasmic loop. The high-resolution structure of the full [SECYEG](/xray-mp-wiki/proteins/secyeg) complex reveals that SecG is peripherally located and tightly bound to [SECY](/xray-mp-wiki/proteins/secy) through hydrophobic interactions. The TM regions of SecG have low B factors compared to SecY, indicating they are not flexible. The cytoplasmic loop of SecG covers the channel at the pore ring level, contributing to sealing the cytoplasmic side of the protein-conducting channel. This finding was confirmed by disulfide bond formation analysis and molecular dynamics simulations.


## Publications

### doi/10.1016##j.celrep.2015.10.025

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5aww">5AWW</a></td>
      <td>2.7 A</td>
      <td>I222</td>
      <td>Thermus thermophilus SecG; part of full-length SecYEG heterotrimer; expressed in E. coli BL21(DE3)</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecG; co-expressed with SecY(R252G)-His6 and SecE from dual plasmid system (pAK22 encodes two copies of SecG; pAK24 encodes SecY-R252G-His6, SecE, and SecG)

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
      <td>Membrane fraction preparation</td>
      <td>Differential centrifugation</td>
      <td>--</td>
      <td>Not specified + --</td>
      <td>Total membrane fraction from E. coli BL21(DE3) cells co-expressing <a href="/xray-mp-wiki/proteins/secyeg">SECYEG</a></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a> + 2% n-dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>)</td>
      <td>1 hr at 4 C; ultracentrifugation at 138,000 x g for 30 min</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td>Affinity chromatography (His-tag on <a href="/xray-mp-wiki/proteins/secy">SECY</a>)</td>
      <td>Ni-NTA agarose</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Co-purification of SecG with His-tagged <a href="/xray-mp-wiki/proteins/secy">SECY</a>; equilibration with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>; wash with 40 mM imidazole; elution with 300 mM imidazole</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex 200 10/300 GL column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>SecG co-elutes with <a href="/xray-mp-wiki/proteins/secy">SECY</a> and <a href="/xray-mp-wiki/proteins/sece">SECE</a> as a stable heterotrimeric complex</td>
    </tr>
    <tr>
      <td>Ion-exchange chromatography</td>
      <td>Ion-exchange chromatography</td>
      <td>HiTrap SP HP column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 0.25% n-decyl-beta-D-maltoside (DM), 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 0.25% DM</td>
      <td><a href="/xray-mp-wiki/proteins/secyeg">SECYEG</a> heterotrimer eluted with linear gradient of 0-100% elution buffer (1 M NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 0.25% DM, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>)</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aww">5AWW</a> — Chain Y (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">VKAFWSALQ</span><span class="topo-outside">IPELRQRVLFT</span><span class="topo-membrane">LLVLAAYRLGAFI</span><span class="topo-inside">PTPGVDLDKIQEFLRTAQGGVFGIIN</span></span>
<span class="topo-line"><span class="topo-inside">LFSGGNFERFS</span><span class="topo-membrane">IFALGIMPYITAAIIM</span><span class="topo-outside">QILVTVVPALEKLSKEGEEGRRIINQY</span><span class="topo-membrane">TRIGGI</span></span>
<span class="topo-line"><span class="topo-membrane">ALGAFQGF</span><span class="topo-inside">FLATAFLGAEGGRFLLPGWSPGPFFWFVVV</span><span class="topo-membrane">VTQVAGIALLLWMA</span><span class="topo-outside">ERITEYGI</span></span>
<span class="topo-line"><span class="topo-outside">GNG</span><span class="topo-membrane">TSLIIFAGIVVEWLPQIL</span><span class="topo-inside">RTIGLIRTGEVNLV</span><span class="topo-membrane">AFLFFLAFIVLAFAGM</span><span class="topo-outside">AAVQQAERR</span></span>
<span class="topo-line"><span class="topo-outside">IPVQYARKVVGGRVYGGQATYIPIKLNAAGV</span><span class="topo-membrane">IPIIFAAAILQIPIFL</span><span class="topo-inside">AAPFQDNPVLQGI</span></span>
<span class="topo-line"><span class="topo-inside">ANFFNPTRP</span><span class="topo-membrane">SGLFIEVLLVILF</span><span class="topo-outside">TYVYTAVQFDPKRIAESLREYGGFIPGIRPGEPTVKFL</span></span>
<span class="topo-line"><span class="topo-outside">EHIVSRLTLWGAL</span><span class="topo-membrane">FLGLVTLLPQIIQ</span><span class="topo-inside">NLTGIHS</span><span class="topo-membrane">IAFSGIGLLIVVGVA</span><span class="topo-outside">LDTLRQVESQLM</span></span>
<span class="topo-line"><span class="topo-outside">LRSY</span><span class="topo-unknown">EGFLSRGRLRGRNRHHHHHH</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>10</td>
      <td>2</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>21</td>
      <td>11</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>34</td>
      <td>22</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>71</td>
      <td>35</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>87</td>
      <td>72</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>114</td>
      <td>88</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>128</td>
      <td>115</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>158</td>
      <td>129</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>172</td>
      <td>159</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>183</td>
      <td>173</td>
      <td>183</td>
      <td>Outside</td>
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
      <td>215</td>
      <td>202</td>
      <td>215</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>231</td>
      <td>216</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>271</td>
      <td>232</td>
      <td>271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>287</td>
      <td>272</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>309</td>
      <td>288</td>
      <td>309</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>322</td>
      <td>310</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>373</td>
      <td>323</td>
      <td>373</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>386</td>
      <td>374</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>393</td>
      <td>387</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>408</td>
      <td>394</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>424</td>
      <td>409</td>
      <td>424</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aww">5AWW</a> — Chain E (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">FARLIRYFQEARAELA</span><span class="topo-outside">RVTWPTREQVVEGTQAI</span><span class="topo-membrane">LLFTLAFMVILGLYDTVF</span><span class="topo-inside">RFLIGLLR</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>17</td>
      <td>2</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>34</td>
      <td>18</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>52</td>
      <td>35</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>60</td>
      <td>53</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aww">5AWW</a> — Chain G (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MDLLYTLVIL</span><span class="topo-membrane">FYLGVAGLLVYLVL</span><span class="topo-outside">VQEPKQGAGDLMGGSADLFSARGVTGGLYR</span><span class="topo-membrane">LTVILG</span></span>
<span class="topo-line"><span class="topo-membrane">VVFAALA</span><span class="topo-inside">LVIGLWPR</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>54</td>
      <td>25</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>67</td>
      <td>55</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>75</td>
      <td>68</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Cytoplasmic loop covers the protein-conducting channel

The cytoplasmic loop of SecG covers the hourglass-shaped [SECY](/xray-mp-wiki/proteins/secy) channel exactly over the pore ring, contributing to channel sealing on the cytoplasmic side. The C4 loop of SecY and the cytoplasmic loop of SecG are in close proximity; L35 of SecG is located near I272 of SecY, with a C-alpha-C-alpha distance of approximately 4.5 A. Disulfide bond crosslinking between SecY(I272C) and SecG(L35C) confirmed this proximity in the membrane. This arrangement prevents uncontrolled ion flux across the membrane while allowing regulated protein translocation. The proposed topology inversion of SecG during translocation of its hydrophilic cytoplasmic loop across the hydrophobic membrane (Nishiyama et al., 1996) does not appear to occur based on the crystal structure.

### Transmembrane helices tightly bound to SecY

SecG comprises TM1 and TM2 connected by a cytoplasmic loop. The TMs of SecG are tightly bound to [SECY](/xray-mp-wiki/proteins/secy) through hydrophobic interactions, with an interaction area involving TM3, TM4, C2, and C3 of SecY that accounts for approximately 30% of the SecG surface. The B factors of SecG TM regions are low compared to those of SecY, indicating that these transmembrane regions are not flexible. Disulfide bond formation analysis confirmed the interaction between SecG and SecY (Satoh et al., 2003).


## Cross-References

- <a href="/xray-mp-wiki/proteins/secretion-translocon/secyeg/">Thermus thermophilus SecYEG Translocon Complex</a> — SecG is the accessory subunit that covers the cytoplasmic side of the SecYEG channel
- <a href="/xray-mp-wiki/proteins/secretion-translocon/secy/">Thermus thermophilus SecY Core Channel Subunit</a> — SecG binds to SecY and covers the cytoplasmic side of the SecY channel
- <a href="/xray-mp-wiki/proteins/secretion-translocon/sece/">Thermus thermophilus SecE Accessory Subunit</a> — SecE and SecG are both accessory subunits of the SecYEG translocon
- <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> — Main buffer component in purification
- <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> — Cryoprotectant and buffer additive
- <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> — Detergent used in solubilization and purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> — Eluent for affinity chromatography
