---
title: "Mitochondrial Calcium Uniporter (MCU)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-018-0330-9]
verified: agent
uniprot_id: Q21121
---

# Mitochondrial Calcium Uniporter (MCU)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q21121">UniProt: Q21121</a>

<span class="expr-badge">Caenorhabditis elegans</span>

## Overview

The mitochondrial calcium uniporter (MCU) is the pore-forming subunit of the mitochondrial Ca2+ channel that mediates rapid Ca2+ uptake into the mitochondrial matrix, critical for ATP production, intracellular Ca2+ signaling, and cell death. Crystal structures of MCU from the fungi Metarhizium acridum (MaMCU) and [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structures from Fusarium graminearum (FgMCU) reveal a tetrameric dimer-of-dimers architecture with a truncated pyramid shape, fundamentally different from the previously reported pentameric NMR structure of C. elegans MCU. Each protomer contains two transmembrane helices (TM1 and TM2), with TM2 lining the central ion conduction pore. The selectivity filter is formed by a conserved DXXE motif (Asp333-Glu336 in MaMCU) at the first helical turn of TM2, with Glu336 carboxylate groups coordinating Ca2+ at the pore centre. The structures reveal a new ion channel architecture and provide a structural framework for understanding mitochondrial calcium uniporter function, selectivity, and regulation.


## Publications

### doi/10.1038##s41586-018-0330-9

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6c5w">6C5W</a></td>
      <td>3.10</td>
      <td>P2_1_2_1_2</td>
      <td>MaMCU-Rub (Metarhizium acridum MCU residues 62-484 with Rubredoxin fusion, truncations 62-98, 190-205, 427-484, mutations H327W, M330F) in complex with nanobody</td>
      <td>Ca2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6c5r">6C5R</a></td>
      <td>3.10</td>
      <td>C2</td>
      <td>MaMCU soluble domain (NTD only, residues 62-294 with TM domain deleted)</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21 (DE3)
- **Construct**: MaMCU (Metarhizium acridum MCU, residues 62-484, lacking mitochondrial signal peptide 1-61); engineered construct MaMCU-Rub added Clostridium pasteurianum [Rubredoxin Fusion Protein](/xray-mp-wiki/reagents/protein-tags/rubredoxin/) fusion in NTD loop (S213-G214) plus point mutations H327W and M330F for improved crystallization
- **Notes**: Purified with N-terminal His6-GFPuv tag, cleaved by 3C protease; FgMCU construct also expressed in E. coli with similar vector

**Purification:**

- **Expression system**: E. coli BL21 (DE3)
- **Expression construct**: MaMCU (His6-GFPuv-3C-MaMCU)
- **Tag info**: N-terminal His6-GFPuv tag, cleaved by 3C protease

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
      <td>Cell lysis</td>
      <td>Sonication</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 150 mM NaCl, 2 mM CaCl2, protease inhibitor cocktail</td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>2 h at 4C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt resin (<a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a>)</td>
      <td>—</td>
      <td></td>
      <td>Batch binding 2 h at 4C; washed with 10-20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>3C protease overnight</td>
      <td>—</td>
      <td></td>
      <td>On-column cleavage</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> (<a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase)</td>
      <td>—</td>
      <td>20 mM Tris pH 8.0, 150 mM NaCl, 2 mM CaCl2, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Peak fractions concentrated to 10-15 mg/mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>10-15 mg/mL MaMCU-Rub in 20 mM Tris pH 8.0, 150 mM NaCl, 2 mM CaCl2, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM Tris pH 8.0, 200 mM Li2SO4, 35% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 3.5 A; P2_1_2_1_2 space group; also crystallized MaMCU-<a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> complex (C222_1 space group) and MaMCU soluble domain (C2 space group)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c5w">6C5W</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MAALSVDEYKLSREKKLLLQLENAETLLAPLHDAKRKIEQEAEAHTDRV</span><span class="topo-membrane">AWAGFAASGVQTGLFARLTW</span><span class="topo-inside">WEYSW</span><span class="topo-membrane">DIVEPVTYFATYSTVAA</span><span class="topo-outside">TFGYYLYTQQSFEYPSARERVYTKQFYRR</span></span>
<span class="topo-ruler">       130       140       150         </span>
<span class="topo-line"><span class="topo-outside">AQKQNFDIEKYNRLVTEVDELRNQLKRLRDPLE</span><span class="topo-unknown">HHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>49</td>
      <td>166</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>69</td>
      <td>215</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>74</td>
      <td>235</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>91</td>
      <td>240</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>153</td>
      <td>257</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c5w">6C5W</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MAALSVDEYKLSREKKLLLQLENAETLLAPLHDAKRKIEQEAEAHT</span><span class="topo-membrane">DRVAWAGFAASGVQTGLFARL</span><span class="topo-inside">TWWEYSW</span><span class="topo-membrane">DIVEPVTYFATYSTVAAT</span><span class="topo-outside">FGYYLYTQQSFEYPSARERVYTKQFYRR</span></span>
<span class="topo-ruler">       130       140       150         </span>
<span class="topo-line"><span class="topo-outside">AQKQNFDIEKYNRLVTEVDELRNQLKRLRDPLE</span><span class="topo-unknown">HHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>46</td>
      <td>166</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>67</td>
      <td>212</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>74</td>
      <td>233</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>92</td>
      <td>240</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>153</td>
      <td>258</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c5w">6C5W</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MAALSVDEYKLSREKKLLLQLENAETLLAPLHDAKRKIEQEAEAHT</span><span class="topo-membrane">DRVAWAGFAASGVQTGLFARL</span><span class="topo-inside">TWWEYSW</span><span class="topo-membrane">DIVEPVTYFATYSTVAATF</span><span class="topo-outside">GYYLYTQQSFEYPSARERVYTKQFYRR</span></span>
<span class="topo-ruler">       130       140       150         </span>
<span class="topo-line"><span class="topo-outside">AQKQNFDIEKYNRLVTEVDELRNQLKRLRDPLE</span><span class="topo-unknown">HHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>46</td>
      <td>166</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>67</td>
      <td>212</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>74</td>
      <td>233</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>93</td>
      <td>240</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>153</td>
      <td>259</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c5w">6C5W</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MAALSVDEYKLSREKKLLLQLENAETLLAPLHDAKRKIEQEAEAHTDRV</span><span class="topo-membrane">AWAGFAASGVQTGLFARLT</span><span class="topo-inside">WWEYSW</span><span class="topo-membrane">DIVEPVTYFATYSTVAAT</span><span class="topo-outside">FGYYLYTQQSFEYPSARERVYTKQFYRR</span></span>
<span class="topo-ruler">       130       140       150         </span>
<span class="topo-line"><span class="topo-outside">AQKQNFDIEKYNRLVTEVDELRNQLKRLRDPLE</span><span class="topo-unknown">HHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>49</td>
      <td>166</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>68</td>
      <td>215</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>74</td>
      <td>234</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>92</td>
      <td>240</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>153</td>
      <td>258</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c5w">6C5W</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MAALSVDEYKLSREKKLLLQLENAETLLAPLHDAKRKIEQEAEAHTDRVA</span><span class="topo-membrane">WAGFAASGVQTGLFARLTWW</span><span class="topo-inside">EYSW</span><span class="topo-membrane">DIVEPVTYFATYSTVAAT</span><span class="topo-outside">FGYYLYTQQSFEYPSARERVYTKQFYRR</span></span>
<span class="topo-ruler">       130       140       150         </span>
<span class="topo-line"><span class="topo-outside">AQKQNFDIEKYNRLVTEVDELRNQLKRLRDPLE</span><span class="topo-unknown">HHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>50</td>
      <td>166</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>70</td>
      <td>216</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>74</td>
      <td>236</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>92</td>
      <td>240</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>153</td>
      <td>258</td>
      <td>318</td>
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

### Dimer-of-Dimers Architecture

MCU forms a tetrameric channel with a dimer-of-dimers assembly, where two pairs of protomers assemble around a central ion conduction pore. This architecture was consistently observed by X-ray crystallography and [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) across species (M. acridum and F. graminearum) and in multiple chemical environments (detergent, amphipol, nanodisc). The N-terminal domain (NTD) also forms a dimer-of-dimers arrangement, with a conserved interface matching human MCU NTD crystal forms.

### DXXE Selectivity Filter

The selectivity filter of MCU is formed by the conserved DXXE motif (Asp333-X-X-Glu336 in MaMCU) at the first helical turn of TM2. Glu336 carboxylate groups from all four subunits point to the pore centre and coordinate a bound Ca2+ ion. This high-affinity Ca2+ binding site is essential for the remarkable Ca2+ selectivity of MCU (which operates at sub-micromolar Ca2+ concentrations). The mechanism parallels Ca2+ channels like Orai and CavAb, using carboxylate rings for Ca2+ coordination.

### Truncated Pyramid Pore Architecture

Unlike conventional ion channels, MCU has a truncated pyramid shape with the wider base at the mitochondrial matrix side and the narrower apex at the intermembrane space. TM2 helices line the central pore with near four-fold symmetry. The pore is mostly hydrophilic and wider than typical channels, contributing to the relatively high conductance of MCU. The Asp333 residue at the intermembrane-space entrance likely recruits Ca2+ and is the site of ruthenium red inhibition.

### Conserved Architecture from Fungi to Humans

Although the N-terminal domain shows sequence conservation only among metazoans, the NTD fold is conserved between MaMCU and human MCU (r.m.s.d. 1.6 A despite no sequence similarity). The dimer interface of NTDs in MaMCU matches a crystal form of human MCU NTD, supporting a conserved tetrameric architecture from fungi to humans.


## Cross-References

- <a href="/xray-mp-wiki/concepts/dimer-of-dimers/">Dimer-of-Dimers Architecture</a> — MCU represents a paradigm for this quaternary assembly in ion channels
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-ion-coordination/">Intramembrane Ion Coordination</a> — Glu336 ring provides a carboxylate-based Ca2+ selectivity mechanism shared with Orai and CavAb channels
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> — Fusion tag for crystallization or purification
