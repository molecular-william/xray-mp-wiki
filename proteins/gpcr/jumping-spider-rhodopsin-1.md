---
title: "Jumping Spider Rhodopsin-1 (JSR1)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1902192116]
verified: false
---

# Jumping Spider Rhodopsin-1 (JSR1)

## Overview

The jumping spider rhodopsin-1 (JSR1) from Hasarius adansoni is a class A G protein-coupled receptor (GPCR) that functions as a bistable, light-sensitive rhodopsin. The crystal structure of JSR1 bound to the inverse agonist 9-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) was determined at 2.1 Å resolution (Varma et al., 2019, PDB 6I9K). Unlike monostable rhodopsins such as [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/), bistable rhodopsins undergo a two-photon bidirectional photoreaction in which the Schiff base remains protonated and the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) bound throughout the photocycle. The JSR1 structure reveals a water-mediated hydrogen bond network around the Schiff base involving Glu-194 and Ser-199 that serves as the counterion system, with Tyr-126 occupying the proximal counterion position instead of a glutamate. This architecture is similar to squid rhodopsin but distinct from [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/). The transmembrane bundle of JSR1 adopts an "activation-ready" conformation more similar to non-photosensitive class A GPCRs than to [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/). The receptor also contains a DRY motif (rather than the ERY motif in vertebrate opsins) and an extended water trail connecting the ligand-binding pocket to the G protein-binding site, suggesting JSR1 as a potential model system for studying structure-function relationships of both photosensitive and non-photosensitive class A GPCRs.


## Publications

### doi/10.1073##pnas.1902192116

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6i9k">6I9K</a></td>
      <td>2.1 A</td>
      <td>P 1 21 1</td>
      <td>Wild-type JSR1 expressed in HEK293 GnTI- cells; reconstituted with 9-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>; purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>; deglycosylated with <a href="/xray-mp-wiki/reagents/additives/endoh/">ENDOH</a></td>
      <td>9-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (inverse agonist)</td>
    </tr>
  </tbody>
</table>

**Purification:**

- **Expression system**: HEK293 GnTI- cells (mammalian suspension culture)
- **Expression construct**: Wild-type JSR1
- **Tag info**: C-terminal 1D4 tag (for immunoaffinity purification)

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
      <td>Mechanical lysis using handheld dounce homogenizer</td>
      <td></td>
      <td>50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2, cOmplete EDTA-free protease inhibitors</td>
      <td>Frozen cell pellets thawed and lysed; all steps under 640 nm dim red light</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> reconstitution</td>
      <td>Incubation with 30 uM 9-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a></td>
      <td></td>
      <td>50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2</td>
      <td>Overnight incubation at 4 C; identical procedure for 11-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> sample</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Differential centrifugation</td>
      <td></td>
      <td>50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2</td>
      <td>Sequential spins at 500 x g and 100,000 x g; membrane resuspended in buffer B</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> solubilization</td>
      <td></td>
      <td>50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2 + 19.5 mM n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>2 h incubation at 4 C; centrifuged at 100,000 x g for 50 min</td>
    </tr>
    <tr>
      <td>Immunoaffinity chromatography</td>
      <td>Anti-1D4 antibody affinity</td>
      <td>CNBr-activated Sepharose 4B conjugated with anti-1D4 antibody</td>
      <td>50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2, 0.195 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.195 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Resin incubated overnight at 4 C; eluted in buffer D (same buffer with 0.8 mg/ml 1D4 peptide)</td>
    </tr>
    <tr>
      <td>ConA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Concavalin A lectin affinity</td>
      <td>Concavalin A Sepharose 4B</td>
      <td>50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2, 0.195 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 1 mM CaCl2, 1 mM MnCl2 + 0.195 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Removes misfolded/non-glycosylated receptor; elution with linear gradient of methyl-alpha-D-mannopyranoside</td>
    </tr>
    <tr>
      <td>Deglycosylation</td>
      <td>Endoglycosidase H treatment</td>
      <td></td>
      <td>50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2, 0.195 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.195 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>1/500x <a href="/xray-mp-wiki/reagents/additives/endoh/">ENDOH</a> (2.5 U stock), overnight incubation at 4 C</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified JSiR1 (9-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) bound) in [DDM](/xray-mp-wiki/reagents/detergents/ddm/)
**Purity**: OD 280/505 nm ratio between 2.8 and 3.5

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic Cubic Phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/))</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (9.9 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>JSiR1 concentrated to 20-30 mg/ml and mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> in 40:60 ratio (protein:lipid) to form <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/). Crystallization screening using mosquito <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">lcp</a> robot at 4 C with 100 um glass Laminex plates. Optimized conditions: 31-36% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 100 mM Bis-Tris pH 6.5. Data collected at SLS beamline PX1 (wavelength 1.000 A, 16 M Eiger detector). Anisotropic diffraction: 2.5 A, 2.1 A, 2.3 A along a*, b*, c* axes. STARANISO-processed data. Two datasets merged and scaled with Aimless. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using squid rhodopsin (PDB 2Z73).
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6i9k">6I9K</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MLPHAAKMAARVAGDHDGR</span><span class="topo-inside">NISIVDLLPEDMLPMIHEHWYKFPPMETS</span><span class="topo-membrane">MHYILGMLIIVIGIISVSGNGVVMYLMMT</span><span class="topo-outside">VKNLRTP</span><span class="topo-membrane">GNFLVLNLALSDFGMLFFMMPTMSI</span><span class="topo-inside">NCFAETWVIGP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FMCE</span><span class="topo-membrane">LYGMIGSLFGSASIWSLVMITLD</span><span class="topo-outside">RYNVIVKGMAGKPLTK</span><span class="topo-membrane">VGALLRMLFVWIWSLGWTIAPM</span><span class="topo-inside">YGWSRYVPEGSMTSCTIDYIDTAINPM</span><span class="topo-membrane">SYLIAYAIFVYFVPLFIIIYCYA</span><span class="topo-outside">FIVMQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VAAHEKSLREQAKKMN</span><span class="topo-unknown">IKSLRS</span><span class="topo-outside">NEDNKKASAEFRLAKV</span><span class="topo-membrane">AFMTICCWFMAWTPYLTLSFLGIFS</span><span class="topo-inside">DRTWLTPM</span><span class="topo-membrane">TSVWGAIFAKASACYNPIVYGI</span><span class="topo-outside">SH</span><span class="topo-unknown">PKYRAALHDKFPCLKCGSDSPKGDS</span></span>
<span class="topo-ruler">       370       380</span>
<span class="topo-line"><span class="topo-unknown">ASTVAESEKAGEETSQVAPA</span></span>
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
      <td>20</td>
      <td>48</td>
      <td>20</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>77</td>
      <td>49</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>84</td>
      <td>78</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>109</td>
      <td>85</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>124</td>
      <td>110</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>147</td>
      <td>125</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>163</td>
      <td>148</td>
      <td>163</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>185</td>
      <td>164</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>212</td>
      <td>186</td>
      <td>212</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>235</td>
      <td>213</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>256</td>
      <td>236</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>278</td>
      <td>263</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>303</td>
      <td>279</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>311</td>
      <td>304</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>333</td>
      <td>312</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>335</td>
      <td>334</td>
      <td>335</td>
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

### Water-mediated counterion system in bistable rhodopsins

The JSR1 structure reveals a water-mediated hydrogen bond network connecting the protonated Schiff base to Glu-194 (distal counterion) via Ser-199. This "Glu-water-Ser" triad differs from [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) where Glu-113 serves as a direct proximal counterion. In JSR1, Tyr-126 occupies the proximal position (3.28), which is Glu-113 in [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/). This water-mediated system is a key feature distinguishing bistable from monostable rhodopsins and enables the two-photon bidirectional photocycle where the Schiff base remains protonated throughout.

### DRY motif and activation-ready conformation

JSR1 contains a DRY motif (Asp-147, Arg-148, Tyr-149) at the cytoplasmic end of TM3, characteristic of ligand-binding class A GPCRs, in contrast to the ERY motif in vertebrate visual opsins. Molecular dynamics simulations show a double ionic lock: an intrahelical salt bridge between Arg-148 and Asp-147, and an interhelical salt bridge between Arg-148 and Glu-272. The interhelical interaction is more stable than the intrahelical component. The transmembrane bundle conformation resembles the inactive state of other class A GPCRs, with conserved tyrosine residues (5.58 and 7.53) oriented toward the DRY motif, unlike [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) where they point away from the bundle.

### Extended water trail connecting ligand pocket to G protein site

A network of ordered water molecules spans the entire length of the transmembrane region, connecting the retinal-binding pocket to the cytoplasmic G protein-binding site. This water trail is more extensive than in [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) and includes water molecules that participate in the Schiff base counterion system. The extensive hydration of the transmembrane region may contribute to the conformational plasticity of bistable rhodopsins and their ability to undergo reversible photocycles.

### G protein promiscuity of JSR1

Functional assays demonstrated that JSR1 activates Gi in vitro, and previous studies suggested it also activates Gq in vivo, indicating inherent promiscuity in G protein activation similar to many class A GPCRs. This is distinct from the highly specialized G protein coupling of [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) (transducin) and highlights the similarity of JSR1 to non-photosensitive GPCRs.

### Conserved structural features between bistable rhodopsins

Comparison of JSR1 with squid rhodopsin reveals shared architectural features: both have a tyrosine at the proximal counterion position (3.28), a distal glutamate counterion (45.44), and a DRY motif. However, they differ at position 45.49 (Ser in JSR1, Asn in squid rhodopsin) and in the presence of an ordered water molecule mediating the Glu-194-Ser-199-Schiff base network in JSR1, which is absent in squid rhodopsin structures. These differences may reflect distinct dynamical properties of the two bistable rhodopsins.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/">Bovine Rhodopsin (Monostable)</a> — Reference monostable rhodopsin; structural comparison of counterion system and activation mechanism
- <a href="/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/">Squid Rhodopsin (Bistable)</a> — Reference bistable rhodopsin; comparison of water-mediated counterion network and retinal-binding pocket
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used for crystallization of JSR1
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (beta-DDM)</a> — Detergent used for solubilization and purification of JSR1
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Lipid component used in LCP crystallization
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Buffer used in JSR1 purification and crystallization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/endoh/">ENDOH</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> — Additive used in purification or crystallization buffers
