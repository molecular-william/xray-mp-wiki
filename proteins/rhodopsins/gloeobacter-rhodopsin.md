---
title: "Gloeobacter Rhodopsin (GR) from Gloeobacter violaceus"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41598-019-47445-5]
verified: false
---

# Gloeobacter Rhodopsin (GR) from Gloeobacter violaceus

## Overview

Gloeobacter rhodopsin (GR) is a light-driven proton pump from the
cyanobacterium Gloeobacter violaceus PCC 7421, which lacks thylakoid
membranes. GR is a microbial rhodopsin with seven transmembrane helices
and [All-trans Retinal](/xray-mp-wiki/reagents/all-trans-retinal/) covalently bound via a protonated Schiff base to
Lys257. It belongs to the XR-type subgroup of eubacterial proton pumps
and features extended helices A, B and G, a 3-omega motif (Phe38, Trp95,
Tyr106), and a flipped B-C loop with antiparallel beta-sheet structure.
GR has carotenoid-binding capability similar to [Xanthorhodopsin](/xray-mp-wiki/proteins/rhodopsins/xanthorhodopsin/) (XR)
and shows pH-dependent pentameric oligomerization. Under specific
conditions, GR exhibits an inverted proton flux, an optogenetically
relevant feature. The crystal structure was solved at 2.0 Angstrom
resolution from crystals grown in bicelles.


## Publications

### doi/10.1038##s41598-019-47445-5

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6nwd">6NWD</a></td>
      <td>2.0</td>
      <td>C 2 2 2 1</td>
      <td>Full-length GR with C-terminal 6xHis tag</td>
      <td>All-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (chromophore)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: Full-length GR with C-terminal 6xHis tag

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
      <td>1. Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>1.0% <a href="/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/">OG</a> (OG) or <a href="/xray-mp-wiki/reagents/detergents/n-dodecyl-beta-d-maltoside/">DDM</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Solubilization at room temperature; ultracentrifugation at 100,000 x g to remove unsolubilized material</td>
    </tr>
    <tr>
      <td>2. <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Co2+ column</td>
      <td></td>
      <td>Eluted by lowering pH</td>
    </tr>
    <tr>
      <td>3. Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL</td>
      <td>20 mM HEPES pH 7.5, 300 mM NaCl + 1.0% OG or 0.04% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Bicelle crystallization (hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified GR at ~15 mg/mL in 1% OG</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Several weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>GR in 1% OG mixed with 24% (w/v) <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a>:<a href="/xray-mp-wiki/reagents/detergents/chapso/">CHAPSO</a> bicelles at 1:2 ratio (final 8% bicelles). Plate-like crystals grown at pH 3.4 in the dark. X-ray data collected at APS beamline 23ID-D with Pilatus 6M detector.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6nwd">6NWD</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MLMTVFSSAPELALLGSTFAQVDPSNLSVS</span><span class="topo-inside">DSLTYGQFNLVYN</span><span class="topo-membrane">AFSFAIAAMFASALFFF</span></span>
<span class="topo-line"><span class="topo-membrane">SAQALV</span><span class="topo-outside">GQRY</span><span class="topo-membrane">RLALLVSAIVVSIAGYHYFRIFN</span><span class="topo-inside">SWDAAYVLENGVYSLTSEKFND</span><span class="topo-membrane">AYRYV</span></span>
<span class="topo-line"><span class="topo-membrane">DWLLTVPLLLVETVAVL</span><span class="topo-outside">TLPAKEA</span><span class="topo-membrane">RPLLIKLTVASVLMIATGYPGE</span><span class="topo-inside">ISDDITTR</span><span class="topo-membrane">IIWGTV</span></span>
<span class="topo-line"><span class="topo-membrane">STIPFAYILYVLWVELSR</span><span class="topo-outside">SLVRQPAAVQ</span><span class="topo-membrane">TLVRNMRWLLLLSWGVYPIAYLL</span><span class="topo-inside">PMLGVSGTS</span></span>
<span class="topo-line"><span class="topo-inside">AAVG</span><span class="topo-membrane">VQVGYTIADVLAKPVFGLLVFAIAL</span><span class="topo-outside">VKTKADQ</span><span class="topo-unknown">ESSEPHAAIGAAANKSGGSLIS</span></span>
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
      <td>31</td>
      <td>43</td>
      <td>31</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>44</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>70</td>
      <td>67</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>93</td>
      <td>71</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>115</td>
      <td>94</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>137</td>
      <td>116</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>144</td>
      <td>138</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>174</td>
      <td>167</td>
      <td>174</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>198</td>
      <td>175</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>208</td>
      <td>199</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>231</td>
      <td>209</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>244</td>
      <td>232</td>
      <td>244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>269</td>
      <td>245</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>276</td>
      <td>270</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6nwd">6NWD</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MLMTVFSSAPELALLGSTFAQVDPSNLSVS</span><span class="topo-inside">DSLTYGQFNLVYN</span><span class="topo-membrane">AFSFAIAAMFASALFFF</span></span>
<span class="topo-line"><span class="topo-membrane">SAQALV</span><span class="topo-outside">GQRY</span><span class="topo-membrane">RLALLVSAIVVSIAGYHYFRIFN</span><span class="topo-inside">SWDAAYVLENGVYSLTSEKFND</span><span class="topo-membrane">AYRYV</span></span>
<span class="topo-line"><span class="topo-membrane">DWLLTVPLLLVETVAVL</span><span class="topo-outside">TLPAKEA</span><span class="topo-membrane">RPLLIKLTVASVLMIATGYPGE</span><span class="topo-inside">ISDDITTR</span><span class="topo-membrane">IIWGTV</span></span>
<span class="topo-line"><span class="topo-membrane">STIPFAYILYVLWVELSR</span><span class="topo-outside">SLVRQPAAVQ</span><span class="topo-membrane">TLVRNMRWLLLLSWGVYPIAYLL</span><span class="topo-inside">PMLGVSGTS</span></span>
<span class="topo-line"><span class="topo-inside">AAVG</span><span class="topo-membrane">VQVGYTIADVLAKPVFGLLVFAIAL</span><span class="topo-outside">VKTKADQ</span><span class="topo-unknown">ESSEPHAAIGAAANKSGGSLIS</span></span>
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
      <td>31</td>
      <td>43</td>
      <td>31</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>44</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>70</td>
      <td>67</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>93</td>
      <td>71</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>115</td>
      <td>94</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>137</td>
      <td>116</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>144</td>
      <td>138</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>174</td>
      <td>167</td>
      <td>174</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>198</td>
      <td>175</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>208</td>
      <td>199</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>231</td>
      <td>209</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>244</td>
      <td>232</td>
      <td>244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>269</td>
      <td>245</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>276</td>
      <td>270</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Overall structure of GR and relationship to XR

GR has overall similarity to [Xanthorhodopsin](/xray-mp-wiki/proteins/rhodopsins/xanthorhodopsin/) (XR, RMSD 1.69 Angstrom) with seven transmembrane helices. Like XR, GR has a B-C loop with antiparallel beta-sheet oriented towards helices A and B (flipped orientation), extended helices A, B and G, and a 3-omega motif (Phe38/Trp95/Tyr106) that tethers the B-C loop. The extracellular side of TM helices A, E and G are slightly tilted inward compared to XR.

### Hydrogen bonding network in XR-type proton pumps

GR has an Asp121-His87 pair as the Schiff base counterion (similar to XR and TR), confirming this as a conserved feature in XR-type proton pumps and proteorhodopsins. GR lacks the Glu194/Glu204 pair of BR; instead, a hydrogen-bonded network connecting Arg118, Gln246, and Asp115 is established, with Asp115 potentially serving as the proton donor for proton release.

### pH-dependent pentameric oligomerization

DEER-EPR spectroscopy revealed that GR forms pentamers at pH 8.0 and monomers at pH 3.0 in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) micelles. Two characteristic DEER distance peaks at 19 Angstrom and 29 Angstrom matched the expected distances from a pentameric model. His87 on helix B is proposed to play a key role in the protomer interacting surface, with the His87-Asp121 interaction disrupted at low pH.

### Structural determinants of oligomerization in bacterial pumps

The paper proposes a new classification of bacterial pumps based on the relationship between oligomerization states and conserved structural determinants. Eubacterial pumps with extended helices, 3-omega motif, and flipped B-C loop (XR-type: GR, XR, TR, [KR2 (Krokinobacter eikastus Rhodopsin 2) — Light-Driven Sodium Pump](/xray-mp-wiki/proteins/rhodopsins/kr2/), [CIR](/xray-mp-wiki/proteins/clir/)) form pentamers. Those with extended helices but lacking the 3-omega motif (proteorhodopsins: BPR, GPR, [ESR](/xray-mp-wiki/proteins/rhodopsins/exiguobacterium-sibiricum-rhodopsin/)) form pentamers/hexamers. Archaeal rhodopsins and trimeric eubacterial rhodopsins lack both features and form trimers exclusively.


## Cross-References

- <a href="/xray-mp-wiki/concepts/structural-mechanisms/3-omega-motif/">3 Omega Motif in Microbial Rhodopsins</a> — GR has a conserved 3-omega motif (Phe38, Trp95, Tyr106) essential for B-C loop orientation
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/">Microbial Rhodopsins</a> — GR is a microbial rhodopsin; the paper provides structural basis for function and oligomerization
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/proton-pump-mechanism/">Proton Pump Mechanism in Bacteriorhodopsin</a> — GR is a light-driven proton pump with a distinct hydrogen bonding network compared to BR
- <a href="/xray-mp-wiki/proteins/rhodopsins/xanthorhodopsin/">Xanthorhodopsin (XR)</a> — GR is structurally most similar to XR (RMSD 1.69 Angstroms) and shares the XR-type proton pump features
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin (bR)</a> — Compared with BR (RMSD 3.33 Angstroms) to highlight structural differences in hydrogen bonding network and oligomerization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/clir/">CIR</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/rhodopsins/exiguobacterium-sibiricum-rhodopsin/">ESR</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/rhodopsins/kr2/">KR2 (Krokinobacter eikastus Rhodopsin 2) — Light-Driven Sodium Pump</a> — Related protein structure
