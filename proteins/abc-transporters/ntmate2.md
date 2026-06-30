---
title: "NtMATE2 (Nicotiana tabacum MATE2) - Nicotine MATE transporter"
created: 2026-05-26
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1002##1873-3468.14136]
verified: false
---

# NtMATE2 (Nicotiana tabacum MATE2) - Nicotine MATE transporter

## Overview

NtMATE2 is a multidrug and toxic compound extrusion (MATE) family transporter from Nicotiana tabacum (tobacco) that mediates vacuolar sequestration of [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/), a specialized alkaloid. As one of three MATE transporters in tobacco roots, NtMATE2 transports [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine) from the cytosol into the vacuolar lumen in exchange for protons, protecting the plant from its own toxic metabolite. The crystal structures reveal two outward-facing conformations with unprecedented TM7 movement distinct from other eukaryotic MATE proteins.

## Publications

### doi/10.1002##1873-3468.14136

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7dqk">7DQK</a></td>
      <td>3.5 A</td>
      <td>P212121</td>
      <td>NtMATE2-EFPGENLYFQGQF-eGFP(3-239)-H8, residues 18-493 (Mol-A), 15-493 (Mol-B)</td>
      <td>Unidentified molecule in Mol-B C-lobe cavity (possibly partial <a href="/xray-mp-wiki/reagents/ligands/nicotine/">Nicotine</a> mimic)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris yeast strain SMD1168
- **Construct**: C-terminal [GFP](/xray-mp-wiki/reagents/protein-tags/gfp/)-[His8 Tag](/xray-mp-wiki/reagents/protein-tags/his8-tag/) fusion, induced with 0.5% [Methanol](/xray-mp-wiki/reagents/additives/methanol/) in BMMY medium at 20 C for 72 h

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
      <td>Cell harvesting and membrane fractionation</td>
      <td>Cell lysis using Microfluidizer at 22,000 p.s.i. (five passes); membrane fraction separated by centrifugation</td>
      <td>--</td>
      <td>300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">TRIS</a>-HCl pH 8.0, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + --</td>
      <td>Transformed cells selected with stepwise <a href="/xray-mp-wiki/reagents/additives/g418/">G418</a> at 50, 100, and 200 ug/mL on YPD medium plates</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization of membrane fraction</td>
      <td>--</td>
      <td>300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">TRIS</a>-HCl pH 8.0, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (Glycon), 2 h incubation</td>
      <td>After solubilization, centrifuged at 130,000 g for 30 min; supernatant collected</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (Clontech)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> cobalt affinity resin (Clontech)</td>
      <td>Equilibration: 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a>-Na pH 7.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> pH 8.0 + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his8-tag/">His8-Tag</a>-tagged NtMATE2 bound; washed with buffer containing 0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.003% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20-40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> pH 8.0; eluted with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> pH 8.0</td>
    </tr>
    <tr>
      <td>Tag cleavage and SEC polishing</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> tag cleavage followed by <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>Superdex 200 Increase 10/30 GL (GE Healthcare)</td>
      <td>300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a>-Na pH 7.0, 1% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.003% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.003% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Eluate concentrated using Amicon Ultra 100K filter; mixed with <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV(S219V) Protease</a> at 4 C for 16 h to remove GFP-His8 tag; concentrated to 12 mg/mL for crystallization</td>
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
      <td>Purified NtMATE2 at 12 mg/mL in 300 mM NaCl, 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>-Na pH 7.0, 1% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng">LMNG</a>, 0.003% CHS; <a href="/xray-mp-wiki/reagents/ligands/nicotine/">Nicotine</a> added to 2.5 mM, incubated at 4 C for 10 min; mixed 1:1 with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (NU-CHEK-PREP) using twin-syringe mixing method</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>LCP crystallization performed in glass sandwich plates; 30 nL LCP mixed with 30 nL reservoir. Two outward-facing conformations (Mol-A and Mol-B) found in asymmetric unit. Initial phases calculated by molecular replacement using <a href="/xray-mp-wiki/proteins/casmate">CasMATE (Camelina sativa MATE Transporter)</a> (PDB 5XJJ) with PHASER. Rwork/Rfree = 0.265/0.313. Data collected at SPring-8 BL32XU beamline. Final model contains residues 18-493 for Mol-A and 15-493 for Mol-B.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7dqk">7DQK</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGKSMKSEVEQPLLAAA</span><span class="topo-outside">HGGSSELEEVLSDSQLP</span><span class="topo-unknown">YFRRLRYASWIEFQLL</span><span class="topo-membrane">YRLAAPSVAVYMINNAMSMSTR</span><span class="topo-inside">IFSGQLGNLQLAAASL</span><span class="topo-membrane">GNQGIQLFAYGLMLGMGSAVE</span><span class="topo-outside">TLCGQAYGAHR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YEMLGVYLQRA</span><span class="topo-membrane">TVVLSLTGIPLAVVYLFS</span><span class="topo-inside">KNILLALGESKLVASAAA</span><span class="topo-membrane">VFVYGLIPQIFAYAVNFPIQKFLQ</span><span class="topo-outside">SQSI</span><span class="topo-membrane">VAPSAFISLGTLFVHILLSWVV</span><span class="topo-inside">VYKIGLGLL</span><span class="topo-membrane">GASLVLSFSWWIIV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">VAQFIY</span><span class="topo-outside">ILKSERCKATWAGFRWEAFSGLWQFV</span><span class="topo-membrane">KLSAGSAVMLCLETWYFQILV</span><span class="topo-inside">LLSGLLKNPEIALASISVC</span><span class="topo-membrane">LAVNGLMFMVAVGFNAAAS</span><span class="topo-outside">VRVSNELGAAHPKSAAFSV</span><span class="topo-membrane">FMVTFISFLI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">AVVEAIIVLS</span><span class="topo-inside">L</span><span class="topo-unknown">RNVISYAF</span><span class="topo-inside">TEGEVVAKEVSSLC</span><span class="topo-membrane">PYLAVTLILNGIQPVLSGVAV</span><span class="topo-outside">GCGW</span><span class="topo-membrane">QAFVAYVNVGCYYGVGIPLGCLL</span><span class="topo-inside">GFKFDFGAKG</span><span class="topo-membrane">IWTGMIGGTVMQTIILLWVT</span><span class="topo-outside">FSTDWNKEV</span></span>
<span class="topo-ruler">       490       500       510</span>
<span class="topo-line"><span class="topo-outside">ESARKRLDKWENL</span><span class="topo-unknown">KGPLNKEEFPGENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (28 regions)</summary>
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
      <td>34</td>
      <td>18</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>50</td>
      <td>35</td>
      <td>50</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>72</td>
      <td>51</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>88</td>
      <td>73</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>109</td>
      <td>89</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>131</td>
      <td>110</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>149</td>
      <td>132</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>167</td>
      <td>150</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>191</td>
      <td>168</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>195</td>
      <td>192</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>217</td>
      <td>196</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>226</td>
      <td>218</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>246</td>
      <td>227</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>272</td>
      <td>247</td>
      <td>272</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>293</td>
      <td>273</td>
      <td>293</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>312</td>
      <td>294</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>313</td>
      <td>331</td>
      <td>313</td>
      <td>331</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>332</td>
      <td>350</td>
      <td>332</td>
      <td>350</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>370</td>
      <td>351</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>371</td>
      <td>371</td>
      <td>371</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>379</td>
      <td>372</td>
      <td>379</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>380</td>
      <td>393</td>
      <td>380</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>414</td>
      <td>394</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>415</td>
      <td>418</td>
      <td>415</td>
      <td>418</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>441</td>
      <td>419</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>451</td>
      <td>442</td>
      <td>451</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>471</td>
      <td>452</td>
      <td>471</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>472</td>
      <td>493</td>
      <td>472</td>
      <td>493</td>
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

### Bilobate V-shaped architecture with pseudo-symmetry

The overall NtMATE2 structure has a bilobate V-shape with pseudo-symmetrical assembly of the N- and C-lobes (TM1-6 and TM7-12), consistent with the MATE family architecture. The N- and C-terminal regions form alpha-helices parallel to the membrane on the cytoplasmic surface. The N-terminal region, not modeled in previous structures of AtDTX14 and [CasMATE (Camelina sativa MATE Transporter)](/xray-mp-wiki/proteins/casmate) (PDB 5XJJ), contributes to NtMATE2 stability as N-terminal deletion mutants could not be purified.

### Outward-releasing form (Mol-B) stabilized by unidentified ligand

Mol-B contains an elongated non-water electron density adjacent to N316 in TM8, near E285 in TM7. This density is not present in Mol-A. The average B-factor for Mol-B (93.2) is lower than Mol-A (101.5), suggesting the unidentified ligand stabilizes Mol-B. The site is surrounded by Y288, F289, F320, Y430, and W453, which may participate in substrate recognition via cation-pi interactions similar to those observed for [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/) in PDB structures 6PV7 and 2YK1.

### Unprecedented TM7 conformational movement

TM7 shows the highest RMSD between Mol-A and Mol-B (1.671 A) among all transmembrane helices. Unlike [CasMATE (Camelina sativa MATE Transporter)](/xray-mp-wiki/proteins/casmate) (PDB 5XJJ) and AtDTX14 where TM7 bends around G255-P257, NtMATE2 TM7 undergoes an overall arrangement change without alpha-helix bending. The conserved Asp in TM10 of [CasMATE (Camelina sativa MATE Transporter)](/xray-mp-wiki/proteins/casmate) (PDB 5XJJ)/AtDTX14 is replaced by Asn403 in NtMATE2, which may interact with E285 via hydrogen bonding instead. Q406 can also hydrogen bond with E285. This suggests a different TM7 conformational transition mechanism in NtMATE2.

### Proton-coupled transport mechanism

NtMATE2 is proposed to transport [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/) in exchange for protons. The vacuolar pH (~5.1) versus cytoplasmic pH (~7.6) creates a proton gradient. At the near-neutral pH of crystallization (pH 7.5), the conserved E285 on the cavity surface is deprotonated. At the lower pH in the vacuole lumen, E285 is more likely protonated in outward-facing forms, potentially converting NtMATE2 to its inward-open form. The Na+-binding site in the N-lobe did not show sodium or water molecules, though a phosphate ion was observed between TM1 and TM2.

### Rocker switch model with three conformational states

NtMATE2 follows the [Rocker Switch](/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/) mechanism of alternating-access transport. The proposed mechanism: NtMATE2 interacts with its substrate ([Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/)) in an inward-facing form, converts to the outward-releasing form (Mol-B) with substrate, releases the substrate into the vacuole, and then changes into the outward-open form (Mol-A). Mol-B is proposed as the stable outward-releasing state. This contrasts with [CasMATE (Camelina sativa MATE Transporter)](/xray-mp-wiki/proteins/casmate) (PDB 5XJJ) and AtDTX14 where the transition involves TM7 bending.


## Cross-References

- <a href="/xray-mp-wiki/proteins/ntmate1/">NtMATE1 - Tobacco Nicotine MATE Transporter</a> — NtMATE1 is 95% identical to NtMATE2 and also functions as a nicotine transporter in tobacco roots
- <a href="/xray-mp-wiki/proteins/abc-transporters/casmate/">CasMATE (Camelina sativa MATE Transporter)</a> — CasMATE (PDB 5XJJ, 2.9 A) was used as the search model for molecular replacement; key reference for eukaryotic MATE structural comparisons
- <a href="/xray-mp-wiki/proteins/atdtx14/">AtDTX14 - Arabidopsis thaliana MATE Transporter</a> — AtDTX14 is another eukaryotic MATE transporter from Arabidopsis; structural comparisons reveal conserved features and NtMATE2-specific differences
- <a href="/xray-mp-wiki/proteins/ntjat2/">NtJAT2 - Tobacco Leaf-Specific Nicotine MATE Transporter</a> — NtJAT2 is another tobacco nicotine transporter; TM7 sequence identity between NtMATE2 and NtJAT2 is higher than other TM regions
- <a href="/xray-mp-wiki/reagents/ligands/nicotine/">Nicotine</a> — Nicotine is the physiological substrate of NtMATE2; added at 2.5 mM before LCP crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-maltopyranoside (DDM)</a> — 2% DDM used for initial membrane solubilization of NtMATE2 from Pichia pastoris
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — 0.03% LMNG used as maintenance detergent during TALON affinity chromatography and SEC polishing
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate (CHS)</a> — 0.005% CHS during equilibration and 0.003% during wash/elution for protein stabilization
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Monoolein used as the lipidic cubic phase matrix for LCP crystallization (1:1 protein-to-lipid ratio)
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> — TALON cobalt affinity resin used for initial His-tag capture of NtMATE2
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a> — Superdex 200 Increase 10/30 GL used for final SEC polishing step
- <a href="/xray-mp-wiki/reagents/additives/g418/">G418 (Geneticin)</a> — G418 (geneticin) used at 50, 100, and 200 ug/mL for selection of Pichia pastoris transformants
- <a href="/xray-mp-wiki/methods/expression-systems/pichia-pastoris/">Pichia Pastoris Expression System</a> — Pichia pastoris SMD1168 used as the expression host for NtMATE2
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP crystallization method used to grow NtMATE2 microcrystals
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Size-exclusion chromatography used for final polishing of NtMATE2
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/">Rocker-Switch Mechanism in MFS Transporters</a> — NtMATE2 operates via the rocker switch alternating-access mechanism
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — HEPES-Na (pH 7.0 for purification, pH 7.5 for crystallization) used throughout
