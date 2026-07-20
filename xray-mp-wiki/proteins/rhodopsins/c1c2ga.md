---
title: "C1C2GA (C1C2 T198G/G202A)"
created: 2026-06-05
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms8177]
verified: agent
uniprot_id: ['Q8L435', 'Q8RUT8']
---

# C1C2GA (C1C2 T198G/G202A)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8L435">UniProt: Q8L435</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8RUT8">UniProt: Q8RUT8</a>

<span class="expr-badge">Chlamydomonas reinhardtii</span>

## Overview

C1C2GA is a blue-shifted mutant of the channelrhodopsin chimera C1C2, created by double mutation T198G/G202A. The mutant exhibits a 21 [NM](/xray-mp-wiki/reagents/detergents/nm/) blue shift in absorption maximum (from 476 [NM](/xray-mp-wiki/reagents/detergents/nm/) to 455 nm) compared to wild-type C1C2. The crystal structure at 2.5 A resolution (space group C2221) revealed that the mutations induce rotation of the beta-ionone ring of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore to a 6-s-cis twisted conformation, shrinking the pi-conjugated system. The N-terminal 10 residues (PDYVFHRAHE) form a short helix not seen in the C1C2WT structure, and a putative Zn2+ ion coordinated by Asp40, His44, His47, and Asp142 was found bound to the extracellular side of the protein. C1C2GA maintains functional ion channel activity in HEK293 cells and mouse neurons.

## Publications

### doi/10.1038##ncomms8177

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4yzi">4YZI</a></td>
      <td>2.5</td>
      <td>C2221</td>
      <td>C1C2 T198G/G202A mutant (C1C2GA)</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (twisted 6-s-cis conformation)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: C1C2 T198G/G202A mutant, [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) induction, [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) selection
- **Notes**: Transformed E. coli BL21(DE3) cells grown at 18 C overnight in LB medium containing [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) (50 ug/ml) and 5 uM all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/). [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) induction used for [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) expression.

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
      <td>Cell disruption and membrane fractionation</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> (pH 6.5) containing 1 M NaCl + --</td>
      <td>Cells harvested by centrifugation at 4 C, resuspended in buffer, disrupted by sonication or French press passage</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> (pH 6.5), 1 M NaCl + n-dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Cell membranes solubilized by <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Ni2+ <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni2+ affinity column (GE Healthcare)</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purified by chromatography on Ni2+ affinity column</td>
    </tr>
    <tr>
      <td>Concentration and buffer exchange</td>
      <td>Ultrafiltration concentration</td>
      <td>--</td>
      <td>1 M NaCl, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a>-Cl (pH 7.0) + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purified sample concentrated and buffer exchanged using Amicon Ultra filter (Millipore)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>C1C2GA mutant protein in buffer containing 1 M NaCl, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a>-Cl (pH 7.0), 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Lipidic cubic phase (MOS/DCG or similar LCP medium)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
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
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Yellow crystals obtained in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> under neutral pH conditions (pH 7.0). Structure determined by molecular replacement method using C1C2WT (PDB 3UG9) as template. Overall structure at pH 7.0 nearly identical to C1C2WT at pH 6.0 (RMSD 0.66 A over all Ca atoms).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yzi">4YZI</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PDYVFHRAHERMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLMFY</span><span class="topo-unknown">GYQTWKST</span><span class="topo-outside">CG</span><span class="topo-membrane">WEEIYVATIEMIKFIIEYF</span><span class="topo-inside">HEFDEPAVIYSSNGNKT</span><span class="topo-membrane">VWL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RYAEWLLTCPVILIHL</span><span class="topo-outside">SNLTGLANDYNKR</span><span class="topo-membrane">TMGLLVSDIGGIVWATTAAL</span><span class="topo-inside">SKGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTFFNAA</span><span class="topo-outside">KVYIEAYHTVPKGRCRQVVT</span><span class="topo-membrane">GMAWLFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300    </span>
<span class="topo-line"><span class="topo-inside">LSVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGLLGH</span><span class="topo-outside">YLRVLIHEHILIHGDIRKTTK</span><span class="topo-unknown">LNIGGTE</span><span class="topo-outside">IEVETLVEDE</span></span>
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
      <td>52</td>
      <td>39</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>71</td>
      <td>91</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>81</td>
      <td>118</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>100</td>
      <td>120</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>117</td>
      <td>139</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>156</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>149</td>
      <td>175</td>
      <td>187</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>169</td>
      <td>188</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>173</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>194</td>
      <td>212</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>214</td>
      <td>233</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>253</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>245</td>
      <td>273</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>266</td>
      <td>284</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>287</td>
      <td>305</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>304</td>
      <td>333</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yzi">4YZI</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PDYVFHRAHERMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLMFY</span><span class="topo-unknown">GYQTWKST</span><span class="topo-outside">CG</span><span class="topo-membrane">WEEIYVATIEMIKFIIEYF</span><span class="topo-inside">HEFDEPAVIYSSNGNKT</span><span class="topo-membrane">VWL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RYAEWLLTCPVILIHL</span><span class="topo-outside">SNLTGLANDYNKR</span><span class="topo-membrane">TMGLLVSDIGGIVWATTAAL</span><span class="topo-inside">SKGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTFFNAA</span><span class="topo-outside">KVYIEAYHTVPKGRCRQVVT</span><span class="topo-membrane">GMAWLFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300    </span>
<span class="topo-line"><span class="topo-inside">LSVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGLLGH</span><span class="topo-outside">YLRVLIHEHILIHGDIRKTTK</span><span class="topo-unknown">LNIGGTE</span><span class="topo-outside">IEVETLVEDE</span></span>
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
      <td>52</td>
      <td>39</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>71</td>
      <td>91</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>81</td>
      <td>118</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>100</td>
      <td>120</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>117</td>
      <td>139</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>156</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>149</td>
      <td>175</td>
      <td>187</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>169</td>
      <td>188</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>173</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>194</td>
      <td>212</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>214</td>
      <td>233</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>253</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>245</td>
      <td>273</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>266</td>
      <td>284</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>287</td>
      <td>305</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>304</td>
      <td>333</td>
      <td>342</td>
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

### Beta-ionone ring rotation induces blue-shifted absorption

The T198G/G202A mutations create space in the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) binding pocket, allowing the beta-ionone ring of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore to rotate from the all-trans planar conformation to a twisted 6-s-cis conformation with C6-C7 bond torsion of -27.7 degrees. This rotation shrinks the pi-conjugated system of the chromophore, producing a 21 [NM](/xray-mp-wiki/reagents/detergents/nm/) blue shift (476 to 455 nm). The twisted 6-s-cis conformation is thermodynamically more stable by -1.1 kcal/mol than the planar 6-s-trans form in the C1C2GA mutant.

### First evidence of Zn2+ binding to channelrhodopsin

The crystal structure revealed a putative endogenous Zn2+ ion bound at the N-terminal segment of C1C2GA, which was disordered in the C1C2WT structure. The N-terminal 10 residues (PDYVFHRAHE) form a short helix on the extracellular side of transmembrane helix 2 and extracellular loop 1. The Zn2+ ion is coordinated tetrahedrally by Asp40, His44, and His47 on the N-terminal helix, together with Asp142 on ECL1. This represents the first evidence of a Zn2+ ion bound to the extracellular side of a channelrhodopsin.

### Disappearance of vibrational fine structure in absorption spectrum

The C1C2GA absorption spectrum lacks the spectral shoulder at ~447 [NM](/xray-mp-wiki/reagents/detergents/nm/) present in C1C2WT, which represents vibrational fine structure. The beta-ionone ring rotation eliminates this fine structure by broadening the Franck-Condon vibrational distribution in the excited state and separating the energy levels of the S1 and S2 states through vibronic coupling.

### C1C2GA maintains functional ion channel activity

Despite the large blue shift in absorption, C1C2GA retains functional ion channel activity. Photocurrent measurements in HEK293 cells showed that C1C2GA produces inward currents upon blue light illumination (475 nm), comparable to wild-type C1C2. The mutant was also functional in mouse neurons, demonstrating its utility as a blue-shifted optogenetic tool for dual-light activation experiments.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/">Channelrhodopsin C1C2</a> — C1C2GA is the T198G/G202A mutant of C1C2; C1C2WT structure (PDB 3UG9) used as template for C1C2GA crystal structure determination
- <a href="/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-2/">Archaerhodopsin-2</a> — AR3 was also engineered with the same design principle (M128A/G132V/A225T) to produce a 100 nm blue shift (552 to 454 nm)
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Detergent used for membrane solubilization and protein purification
- <a href="/xray-mp-wiki/reagents/lipids/all-trans-retinal/">All-trans retinal</a> — Chromophore covalently bound to conserved lysine via protonated Schiff base; adopts twisted 6-s-cis conformation in C1C2GA
- <a href="/xray-mp-wiki/reagents/buffers/mes/">2-(N-morpholino)ethanesulfonic acid (MES)</a> — Buffer (50 mM, pH 6.5) used in cell lysis and membrane preparation
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl buffer)</a> — Buffer (50 mM, pH 7.0) used in final purification buffer
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate (CHS)</a> — CHS (0.01%) used in C1C2 absorption spectrum measurements
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Isopropyl-beta-D-thiogalactoside (IPTG)</a> — IPTG induction used for GR expression in E. coli
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used to grow C1C2GA crystals at pH 7.0
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — C1C2GA retains photocycle functionality; blue-shifted variant for optogenetics
- <a href="/xray-mp-wiki/reagents/additives/zinc-chloride/">Zinc Chloride</a> — Putative Zn2+ ion bound to N-terminal helix of C1C2GA (first evidence of Zn2+ binding to channelrhodopsin)
