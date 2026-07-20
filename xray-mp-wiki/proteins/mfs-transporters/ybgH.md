---
title: "E. coli YbgH Peptide Transporter"
created: 2026-05-28
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1016##j.str.2014.06.008]
verified: agent
uniprot_id: P75742
---

# E. coli YbgH Peptide Transporter

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P75742">UniProt: P75742</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

YbgH (also known as DtpD) is a proton-dependent oligopeptide transporter (POT) from
Escherichia coli. It belongs to the POT family, a subfamily of the major facilitator
superfamily (MFS) of secondary active transporters. YbgH specifically transports
di- and tripeptides with a preference for substrates bearing a C-terminal basic
residue. It couples peptide uptake to proton symport across the inner membrane.


## Publications

### doi/10.1016##j.str.2014.06.008

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4q65">4Q65</a></td>
      <td>3.4</td>
      <td>P21212</td>
      <td>YbgH residues 6-482, His6-tag at C terminus</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43 (DE3)
- **Construct**: YbgH coding sequence fused to His6 tag at C terminus, cloned in pET-28a vector
- **Notes**: Gene amplified from E. coli BL21 genomic DNA, ligated into ligation-independent
cloning-compatible pET-28a vector. Transformed into E. coli C43 (DE3) cells.
Induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at 16C for 20 hr.


**Purification:**

- **Expression system**: E. coli C43 (DE3)
- **Expression construct**: YbgH residues 6-482, [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) C-terminal

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>--</td>
      <td>Terrific broth + 25 ug/ml <a href="/xray-mp-wiki/reagents/additives/kanamycin">Kanamycin</a></td>
      <td>Grown at 37C to OD600 0.6, induced with 0.5 mM <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a>, shifted to 16C for 20 hr</td>
    </tr>
    <tr>
      <td>Cell harvest</td>
      <td>Centrifugation</td>
      <td>--</td>
      <td>Lysis buffer</td>
      <td>4000 x g for 30 min</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Sonication</td>
      <td>--</td>
      <td>Lysis buffer</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Membrane fraction solubilized with detergent</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8, 300 mM NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">Polyhistidine Tag (His6)</a> affinity purification</td>
    </tr>
    <tr>
      <td>Final sample</td>
      <td>Buffer exchange</td>
      <td>--</td>
      <td>Crystallization buffer + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structure determined by single-wavelength anomalous dispersion (SAD) phasing.
Se-Met labeled protein used for phasing. Also tested <a href="/xray-mp-wiki/reagents/additives/mercury">Mercury (HgCl2) - Aquaporin Inhibitor</a> derivative
(C9H9O2HgNaS). Type I membrane crystals with TM helices parallel to crystallographic a axis.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4q65">4Q65</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNKHA</span><span class="topo-outside">SQPRAIYYV</span><span class="topo-membrane">VALQIWEYFSFYGMRALL</span><span class="topo-inside">ILYLTNQLKYNDTHAYELF</span><span class="topo-membrane">SAYCSLVYVTPILGGFL</span><span class="topo-outside">ADKVLGNRM</span><span class="topo-membrane">AVMLGALLMAIGHVVLG</span><span class="topo-inside">ASEIHPSFLY</span><span class="topo-membrane">LSLAIIVCGYGLFKSN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">V</span><span class="topo-outside">SCLLGELYEPTDPRRDGGFSLM</span><span class="topo-membrane">YAAGNVGSIIAPIACGYA</span><span class="topo-inside">QEEYSWAM</span><span class="topo-membrane">GFGLAAVGMIAGLVIFLC</span><span class="topo-outside">GNRHFTHTRGV</span><span class="topo-unknown">NKKVL</span><span class="topo-outside">RATNF</span><span class="topo-membrane">LLPNWGWLLVLLVATPALITIL</span><span class="topo-inside">FWKEW</span><span class="topo-membrane">SVYAL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">IVATIIGLGVLA</span><span class="topo-outside">KIY</span><span class="topo-unknown">RKA</span><span class="topo-outside">ENQKQR</span><span class="topo-unknown">K</span><span class="topo-outside">ELG</span><span class="topo-membrane">LIVTLTFFSMLFWAFAQQGGS</span><span class="topo-inside">SISLYIDRFVN</span><span class="topo-unknown">RDMFGY</span><span class="topo-inside">TVPTA</span><span class="topo-membrane">MFQSINAFAVMLCGVFL</span><span class="topo-outside">AWVV</span><span class="topo-unknown">KESVAG</span><span class="topo-outside">NRTVRI</span><span class="topo-membrane">WGKFALGLGLMSAGFC</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">IL</span><span class="topo-inside">TLSARWSAMYG</span><span class="topo-unknown">HSS</span><span class="topo-inside">LPLMV</span><span class="topo-membrane">LGLAVMGFAELFIDPVAM</span><span class="topo-outside">SQITRIE</span><span class="topo-unknown">IPG</span><span class="topo-outside">VTGVLT</span><span class="topo-membrane">GIYMLLSGAIANYLAG</span><span class="topo-inside">VIADQTS</span><span class="topo-unknown">QASFDASGAINY</span><span class="topo-inside">SINAYIEVFDQI</span><span class="topo-membrane">TWGALACVGVVLMIWLY</span><span class="topo-outside">Q</span></span>
<span class="topo-ruler">       490   </span>
<span class="topo-line"><span class="topo-outside">A</span><span class="topo-unknown">LKFRNRALALES</span></span>
<details class="topo-details"><summary>Topology coordinates (47 regions)</summary>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>14</td>
      <td>6</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>15</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>51</td>
      <td>33</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>68</td>
      <td>52</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>77</td>
      <td>69</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>94</td>
      <td>78</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>104</td>
      <td>95</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>121</td>
      <td>105</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>143</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>161</td>
      <td>144</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>169</td>
      <td>162</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>187</td>
      <td>170</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>198</td>
      <td>188</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>203</td>
      <td>199</td>
      <td>203</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>208</td>
      <td>204</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>230</td>
      <td>209</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>235</td>
      <td>231</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>252</td>
      <td>236</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>253</td>
      <td>255</td>
      <td>253</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>258</td>
      <td>256</td>
      <td>258</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>259</td>
      <td>264</td>
      <td>259</td>
      <td>264</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>265</td>
      <td>265</td>
      <td>265</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>266</td>
      <td>268</td>
      <td>266</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>289</td>
      <td>269</td>
      <td>289</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>300</td>
      <td>290</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>306</td>
      <td>301</td>
      <td>306</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>307</td>
      <td>311</td>
      <td>307</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>328</td>
      <td>312</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>332</td>
      <td>329</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>338</td>
      <td>333</td>
      <td>338</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>339</td>
      <td>344</td>
      <td>339</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>362</td>
      <td>345</td>
      <td>362</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>373</td>
      <td>363</td>
      <td>373</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>376</td>
      <td>374</td>
      <td>376</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>377</td>
      <td>381</td>
      <td>377</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>399</td>
      <td>382</td>
      <td>399</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>400</td>
      <td>406</td>
      <td>400</td>
      <td>406</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>409</td>
      <td>407</td>
      <td>409</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>410</td>
      <td>415</td>
      <td>410</td>
      <td>415</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>431</td>
      <td>416</td>
      <td>431</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>438</td>
      <td>432</td>
      <td>438</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>439</td>
      <td>450</td>
      <td>439</td>
      <td>450</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>451</td>
      <td>462</td>
      <td>451</td>
      <td>462</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>463</td>
      <td>479</td>
      <td>463</td>
      <td>479</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>481</td>
      <td>480</td>
      <td>481</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>493</td>
      <td>482</td>
      <td>493</td>
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

### Glu21 is the essential protonation site

Glu21 (first residue of motif 1) is the only conserved proton-titratable residue
located in the central cavity among POTs. Mutations E21Q and E21A abolished
transport activity, confirming its critical role. Glu21 is proposed to be the
site of protonation induced by substrate binding, driving the COut-to-CIn
conformational change via the negative-inside membrane potential.

### Motif 2 functions as a conformational switch

Motif 2 (motif A of MFS), with consensus sequence GGxxaDRxxG, is located between
TMs 2 and 3 of the N-terminal domain. The Asp70 residue within motif 2 is proposed
to form a charge-dipole interaction with the N-terminal end of TM 11, stabilizing
the COut state. Motif 2 acts as a conformational switch that senses and responds
to protonation inside the central cavity.

### HA-HB insertion regulates transport activity

Two TM helices HA and HB are inserted between the two MFS domains of YbgH. They
form a V-shaped structure in the Cin state with the opening end facing the cytosol.
Insertion of Gly residues at the closed end completely abolished activity, indicating
that rigidity of the V-shaped helix pair is essential. Mutations at positively
charged residues N-terminal to HA also lost transport activity, supporting a
regulatory role for the HA-HB insert.

### Stability balance between Cin and COut states

The balance between stabilities of the two major conformations is critical for
efficient transport. Charge-dipole interaction between Glu163 and TM8, and salt
bridge between Asp44 and Arg297, both on the periplasmic side, stabilize the
Cin state. Mutations E163A and R297A disrupted these interactions and reduced
activity, while the double mutant E163A/R297A was inactive.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/pot-family/">POT Family</a> — YbgH is a member of the POT family of proton-dependent oligopeptide transporters
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily</a> — POT family is a subfamily of MFS transporters
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — YbgH alternates between inward-facing and outward-facing conformations
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/scissor-switch-gating/">Scissor-Switch Gating</a> — POT-specific gating mechanism involving motif 2
- <a href="/xray-mp-wiki/proteins/mfs-transporters/pept-so/">PepT_So Oligopeptide Transporter</a> — Another POT family member with reported crystal structure
- <a href="/xray-mp-wiki/reagents/additives/mercury">Mercury (HgCl2) - Aquaporin Inhibitor</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/kanamycin">Kanamycin</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">Polyhistidine Tag (His6)</a> — Entity mentioned in text
