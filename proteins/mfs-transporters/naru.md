---
title: "NarU Nitrate/Nitrite Transporter from Escherichia coli"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2013.03.007]
verified: false
---

# NarU Nitrate/Nitrite Transporter from Escherichia coli

## Overview

NarU is a nitrate/nitrite transporter from Escherichia coli belonging to the
[Nitrate/Nitrite Porter (NNP) Family](/xray-mp-wiki/concepts/protein-families/nnp-family/) of the major facilitator superfamily ([MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/)).
NarU shares 76% sequence identity with [NARK](/xray-mp-wiki/proteins/mfs-transporters/nark/) and transports both nitrate (NO3-)
and nitrite (NO2-), playing a key role during severe nutrient starvation in
bacteria. The crystal structure of NarU was determined at 3.1 A resolution by
[Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) single-wavelength anomalous dispersion (SeMet SAD) phasing.
The asymmetric unit contains two NarU molecules in distinct conformational
states: occluded (Mol A) and partially inward-open (Mol B and Mol B'),
providing insights into the transport mechanism. The substrate-binding site
is defined by four highly conserved residues (Arg87, Arg303, Asn173, Tyr261)
that coordinate nitrate through hydrogen bonds. The transport path features a
thin cytoplasmic gate (Phe145 and Phe367) and a thick periplasmic gate composed
of hydrophobic and polar layers. Unlike the canonical rocker-switch model for
[MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) transporters, NarU appears to employ a mechanism involving bending of
transmembrane helices TM10 and TM11 around conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues, rather
than rigid-body domain rotation.

## Publications

### doi/10.1016##j.celrep.2013.03.007

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4iu9">4IU9</a></td>
      <td>3.1</td>
      <td>P212121</td>
      <td>Native full-length NarU from E. coli K-12, selenomethionine-substituted for phasing</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (heterologous overexpression)
- **Construct**: Full-length NarU (E. coli K-12)
- **Notes**: Overexpressed in E. coli. Selenomethionine-substituted NarU produced in minimal medium for SAD phasing.

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
      <td>Expression and membrane preparation</td>
      <td>Standard membrane protein preparation</td>
      <td>—</td>
      <td></td>
      <td>Overexpressed NarU in E. coli, membrane purification.</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Standard purification (details in paper)</td>
      <td>—</td>
      <td></td>
      <td>Purified to homogeneity for crystallization.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop or hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified NarU (native or SeMet-substituted)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>-- (not specified in detail)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>-- (not specified)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>-- (not specified)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>-- (not specified)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in space group P212121 with two molecules per asymmetric unit. SeMet-NarU crystallized in presence of 5 mM nitrate for phasing. Native NarU crystallized in absence of substrate.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4iu9">4IU9</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MALQNEKNSRY</span><span class="topo-outside">LLRDWKPENPAFWENKGKHIARRNLWISV</span><span class="topo-membrane">SCLLLAFCVWMLFSAVTVNL</span></span>
<span class="topo-line"><span class="topo-inside">NKIGFNFTT</span><span class="topo-membrane">DQLFLLTALPSVSGALLR</span><span class="topo-outside">VPYSFMVPIFGGRRWTVF</span><span class="topo-membrane">STAILIIPCVWLGIA</span></span>
<span class="topo-line"><span class="topo-membrane">VQN</span><span class="topo-inside">PNT</span><span class="topo-membrane">PFGIFIVIALLCGFAGANF</span><span class="topo-outside">ASSMGNISFFFPKAKQGSALGING</span><span class="topo-membrane">GLGNLGVSVMQ</span></span>
<span class="topo-line"><span class="topo-membrane">LVAPLVIFV</span><span class="topo-inside">PVFAFLGVNGVPQADGSVMS</span><span class="topo-membrane">LANAAWIWVPLLAIATIA</span><span class="topo-outside">AWSGMNDI</span><span class="topo-unknown">ASSRA</span></span>
<span class="topo-line"><span class="topo-unknown">S</span><span class="topo-outside">IADQLPVLQRLHLWL</span><span class="topo-membrane">LSLLYLATFGSFIGFSAGFAMLA</span><span class="topo-inside">KTQFPDVNI</span><span class="topo-membrane">LRLAFFGPFIGA</span></span>
<span class="topo-line"><span class="topo-membrane">IARSVGG</span><span class="topo-outside">AISDKFGGVR</span><span class="topo-membrane">VTLINFIFMAIFSALLFLT</span><span class="topo-inside">LPGTGSGNFI</span><span class="topo-membrane">AFYAVFMGLFLTAG</span></span>
<span class="topo-line"><span class="topo-membrane">LGSGST</span><span class="topo-outside">FQMIAVIFRQITIYR</span><span class="topo-unknown">VKMKGGSDEQ</span><span class="topo-outside">AHKEAVTETAAALGFI</span><span class="topo-membrane">SAIGAVGGFFIPQ</span></span>
<span class="topo-line"><span class="topo-membrane">AFGMSLNM</span><span class="topo-inside">TGSP</span><span class="topo-membrane">VGAMKVFLIFYIVCVLLTWL</span><span class="topo-outside">VY</span><span class="topo-unknown">GRRKFSQKLEVLFQ</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>40</td>
      <td>12</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>60</td>
      <td>41</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>69</td>
      <td>61</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>70</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>88</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>123</td>
      <td>106</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>124</td>
      <td>126</td>
      <td>124</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>145</td>
      <td>127</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>169</td>
      <td>146</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>189</td>
      <td>170</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>209</td>
      <td>190</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>227</td>
      <td>210</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>235</td>
      <td>228</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>241</td>
      <td>236</td>
      <td>241</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>242</td>
      <td>256</td>
      <td>242</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>279</td>
      <td>257</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>288</td>
      <td>280</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>307</td>
      <td>289</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>317</td>
      <td>308</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>336</td>
      <td>318</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>346</td>
      <td>337</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>366</td>
      <td>347</td>
      <td>366</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>367</td>
      <td>381</td>
      <td>367</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>391</td>
      <td>382</td>
      <td>391</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>392</td>
      <td>407</td>
      <td>392</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>428</td>
      <td>408</td>
      <td>428</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>429</td>
      <td>432</td>
      <td>429</td>
      <td>432</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>452</td>
      <td>433</td>
      <td>452</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>453</td>
      <td>454</td>
      <td>453</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>468</td>
      <td>455</td>
      <td>468</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Substrate-binding site defined by four conserved residues

Nitrate is coordinated by four highly conserved amino acids: Arg87 (TM2),
Arg303 (TM8), Asn173 (TM5), and Tyr261 (TM7). Arg87 and Arg303 are essential
for transport activity. Mutagenesis of any of these four residues to Ala
reduces transport by 40-60%. The bound nitrate forms six hydrogen bonds with
these surrounding residues, positioning the substrate at the center of the
transporter.

### Two distinct conformational states reveal transport mechanism

Two NarU molecules in the asymmetric unit exhibit different conformations.
Mol A adopts an occluded conformation with the substrate-binding site isolated
from both sides. Mol B and Mol B' are partially open to the cytoplasmic side.
The main structural difference is the bending of TM10 and TM11: the C-terminal
half of TM10 and N-terminal half of TM11 rotate approximately 16 degrees and
23 degrees, respectively, around Gly364 and Gly405.

### Thin gate and thick gate architecture

The transport path is gated by two distinct barriers. A thin gate on the
cytoplasmic side consists of only two residues: Phe145 and Phe367, which must
separate for substrate release. A thick gate on the periplasmic side comprises
two hydrophobic layers (Phe47/Trp50/Phe265 and Met51/Phe268/Ile269) and a
polar layer (Ser54/Gln180/Ser272). The hydrophobic layers maintain the
outward-closed conformation through extensive van der Waals contacts.

### Proposed deviation from the rocker-switch model

Unlike the canonical rocker-switch mechanism of [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) transporters (involving
rigid-body rotation of N-terminal and C-terminal domains), NarU appears to
undergo conformational changes primarily through bending of transmembrane
helices, particularly TM10 and TM11, facilitated by conserved glycine-rich
nitrate signature motifs in TM5 and TM11, and additional [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues in
TM4, TM7, TM8, and TM10. This model may be favored by the small size of
nitrate (ionic radius ~1.96 A).

### Functional characterization by stopped-flow and ITC

NarU transports nitrate and nitrite at similar rates, with binding affinities
of ~33 uM for nitrate and ~373 uM for nitrite. Transport specificity was
demonstrated by much reduced rates for phosphate and ammonium. A liposome-based
stopped-flow assay showed that NarU-mediated nitrate transport reduces osmotic
pressure, favoring a symporter mechanism rather than a nitrate-nitrite
antiporter. No detectable pH change was observed, suggesting NarU is not
proton-coupled.


## Cross-References

- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction (SAD)</a> — SeMet SAD method used for experimental phasing of NarU structure
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — MR used to determine native NarU structure
- <a href="/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/">Isothermal Titration Calorimetry</a> — ITC used to measure nitrate and nitrite binding affinities to NarU
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Primary method used for structure determination
- <a href="/xray-mp-wiki/concepts/major-facilitator-superfamily/">MFS</a> — Related biological concept
- <a href="/xray-mp-wiki/concepts/protein-families/nnp-family/">Nitrate/Nitrite Porter (NNP) Family</a> — Related biological concept
- <a href="/xray-mp-wiki/proteins/mfs-transporters/nark/">NARK</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Buffer component used in purification or crystallization
