---
title: "Pyrococcus furiosus SecYE Translocon"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1012556107]
verified: false
---

# Pyrococcus furiosus SecYE Translocon

## Overview

The [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/)/SecE complex (SecYE) from Pyrococcus furiosus is the core of the archaeal
Sec translocon, a heterotrimeric protein-conducting channel that mediates protein
translocation across the membrane and integration of membrane proteins. The structure
was determined at 3.1 A resolution (anisotropic data truncated to 2.9 A) and reveals
the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) subunit forming an hourglass-shaped channel with 10 transmembrane helices
organized in two pseudo-symmetrical halves (TMs 1-5 and 6-10). [SECE](/xray-mp-wiki/proteins/secretion-translocon/sece/) wraps around [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/)
as a clamp holding the two halves together, while the third subunit Secβ associates at
the periphery. The structure captured a primed intermediate state of the translocon: the
lateral gate (formed by TMs 2/3 and 7/8) is fully open, while the central plug helix
still occludes the pore. This lateral opening creates a cavity above the plug large
enough to accommodate a signal sequence helix, suggesting a mechanism for early
topological arbitration during membrane protein insertion. Crystal packing revealed a
C-terminal alpha-helix from a symmetry-related molecule inserting into the cytoplasmic
vestibule, acting as a nascent chain mimic. In vivo complementation assays showed that
[Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) of the 15 C-terminal residues of [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) fails to rescue a secY-deficient
E. coli strain, confirming the essential role of this helix in protein targeting.

## Publications

### doi/10.1073##pnas.1012556107

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3mp7">3MP7</a></td>
      <td>3.1 A</td>
      <td>P2_1 2_1 2_1</td>
      <td>Full-length Pyrococcus furiosus SecYEbeta complex; <a href="/xray-mp-wiki/proteins/secretion-translocon/secy/">SECY</a> (1-468), <a href="/xray-mp-wiki/proteins/secretion-translocon/sece/">SECE</a> (1-61), Secbeta (1-130)</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length Pfu-SecYEbeta complex; [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/), [SECE](/xray-mp-wiki/proteins/secretion-translocon/sece/), Secbeta co-expressed

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
      <td>Expression</td>
      <td>Overexpression in E. coli</td>
      <td>--</td>
      <td>-- + --</td>
      <td>SecYEbeta complex expressed in E. coli</td>
    </tr>
    <tr>
      <td>Selective heat precipitation</td>
      <td>Heat treatment</td>
      <td>--</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td>Selective heat precipitation of thermostable Pfu proteins</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (His-tag)</td>
      <td>Ni-NTA</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td>--</td>
    </tr>
    <tr>
      <td>Gel-filtration chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>--</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td>Final purification step</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified in main text</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Purified in <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>. Data collected at ALS beamline 8.3.1. Seleno-MAD phasing at 3.5 A resolution. Anisotropic data truncated along a*, b*, c* to 3.3, 4.1, and 2.9 A respectively with anisotropic scaling.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3mp7">3MP7</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGARDIIYALERWFPEVERPKRRVP</span><span class="topo-inside">LRERFMWT</span><span class="topo-membrane">GVALILYYVLAEIPV</span><span class="topo-outside">YGIPERIQDYFQFLRVVLAGRNGS</span><span class="topo-membrane">ILTLGIGPIVTAGIIL</span><span class="topo-inside">QL</span><span class="topo-unknown">LVGSEIIKLDLANPEDRRFYQAL</span><span class="topo-inside">QR</span><span class="topo-membrane">VFSVF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MCFFEAAVWI</span><span class="topo-outside">LGGAFGRV</span><span class="topo-unknown">GVDVTY</span><span class="topo-outside">AIAV</span><span class="topo-membrane">LMILQLAMGGIVLIILDE</span><span class="topo-inside">LVSKWGIGSG</span><span class="topo-membrane">ISLFIAAGVSQTILTRSLNP</span><span class="topo-outside">LTDPN</span><span class="topo-unknown">IID</span><span class="topo-outside">PLTGQPAIVGAIPYFIQHILKGDLWGAIYRGGSAP</span><span class="topo-membrane">D</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">MLSVVATIVVFFIVVYF</span><span class="topo-inside">ESMRVEI</span><span class="topo-unknown">PLGYRGVTVRGS</span><span class="topo-inside">YPIRFLYVS</span><span class="topo-membrane">NIPIILTFALYANIQLWA</span><span class="topo-outside">RVLDRLGHPWLGRFDPTTGSPISGFVLYVIPPRNIFSVIDNP</span><span class="topo-membrane">VRAIVYLILTVIFSL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LFG</span><span class="topo-inside">YLWVELTGLDARSIAR</span><span class="topo-unknown">QLQRAGLQ</span><span class="topo-inside">IPGFRRDPRTLEK</span><span class="topo-unknown">VLQRYI</span><span class="topo-inside">PYVTFW</span><span class="topo-membrane">GSLTVALIAVLADFL</span><span class="topo-outside">G</span><span class="topo-membrane">ALGTGTGILLTVGIL</span><span class="topo-inside">YRFYEEIAREQITEMFPALRKLFGAGT</span><span class="topo-unknown">LVPRGSHHHH</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">HH</span></span>
<details class="topo-details"><summary>Topology coordinates (35 regions)</summary>
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
      <td>25</td>
      <td>1</td>
      <td>25</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>33</td>
      <td>26</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>48</td>
      <td>34</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>72</td>
      <td>49</td>
      <td>72</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>88</td>
      <td>73</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>90</td>
      <td>89</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>113</td>
      <td>91</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>114</td>
      <td>115</td>
      <td>114</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>130</td>
      <td>116</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>138</td>
      <td>131</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>144</td>
      <td>139</td>
      <td>144</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>145</td>
      <td>148</td>
      <td>145</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>149</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>176</td>
      <td>167</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>196</td>
      <td>177</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>201</td>
      <td>197</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>204</td>
      <td>202</td>
      <td>204</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>205</td>
      <td>239</td>
      <td>205</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>257</td>
      <td>240</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>264</td>
      <td>258</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>276</td>
      <td>265</td>
      <td>276</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>277</td>
      <td>285</td>
      <td>277</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>303</td>
      <td>286</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>345</td>
      <td>304</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>363</td>
      <td>346</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>379</td>
      <td>364</td>
      <td>379</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>387</td>
      <td>380</td>
      <td>387</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>388</td>
      <td>400</td>
      <td>388</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>406</td>
      <td>401</td>
      <td>406</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>407</td>
      <td>412</td>
      <td>407</td>
      <td>412</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>427</td>
      <td>413</td>
      <td>427</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>428</td>
      <td>428</td>
      <td>428</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>443</td>
      <td>429</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>470</td>
      <td>444</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>482</td>
      <td>471</td>
      <td>482</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3mp7">3MP7</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60 </span>
<span class="topo-line"><span class="topo-unknown">MAELQER</span><span class="topo-inside">IRHFWKESRRAFLVTKKPNWA</span><span class="topo-unknown">TYKRAA</span><span class="topo-membrane">KITGLGIILIGLIGMLIRIVG</span><span class="topo-outside">ILILGG</span></span>
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
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>7</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>34</td>
      <td>29</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>55</td>
      <td>35</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>61</td>
      <td>56</td>
      <td>61</td>
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

### Lateral gate opening independent of plug displacement

The Pfu-SecYE structure provides the first view of a translocon with a fully open
lateral gate while the central plug helix still occludes the pore. This demonstrates
that lateral gate opening and plug displacement are independent events during the
translocation cycle. The crevice generated by lateral gate opening can accommodate
a signal sequence and allows interaction with host phospholipids without compromising
membrane permeability.

### Nascent chain mimic in crystal packing

Crystal packing reveals the C-terminal alphaC-helix of [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) from a symmetry-related
molecule inserting into the cytoplasmic vestibule, acting as a nascent chain mimic.
This interaction buries approximately 1,000 A2 of surface area and suggests a general
binding mode for diverse nascent chains at the exit of the ribosomal tunnel.
Entry of this pseudo-substrate is in concert with widening of the cytoplasmic
vestibule and opening of the lateral gate.

### C-terminal helix of SecY essential for function

An in vivo complementation assay using the E. coli secY24 thermo-sensitive mutant
demonstrated that deletion of 15 C-terminal residues of Pfu-[SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) (Met1-Glu453)
fails to rescue growth at the non-permissive temperature. Point mutation analysis
showed the R463A/K464A double mutant (removing the only basic cluster) also fails
to rescue, suggesting these residues anchor the channel to the ribosome. The F459P/A461P
double mutant (disrupting alpha-helical conformation) also fails, indicating the helix
conformation is essential for nascent chain sensing and guidance.

### SecE clamp release mechanism

Compared to Mja-[SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/), the first helix of Pfu-[SECE](/xray-mp-wiki/proteins/secretion-translocon/sece/) is tilted away from the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) core
by an additional 30 degrees, releasing the clamp that [SECE](/xray-mp-wiki/proteins/secretion-translocon/sece/) exerts on [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/). This
conformational change allows the N- and C-terminal halves of [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) to separate,
opening the lateral gate. The release of the [SECE](/xray-mp-wiki/proteins/secretion-translocon/sece/) clamp appears to be triggered by
docking of the nascent chain mimic at the cytoplasmic vestibule.

### Hydrophobic seal compromised on lateral gate opening

The hydrophobic seal provided by ring residues (Ile78, Val82, Ile177, Leu181, Leu291,
Leu438 in Pfu) is compromised upon lateral gate opening. The narrowest constriction
increases from 4.6 A in the closed Mja state to 13.6 A in Pfu, while the widest
point increases from 7.9 A to 10.3 A. This creates a cavity large enough to
accommodate a signal sequence helix, potentially acting as an Anfinsen cage for
topological arbitration of the incoming nascent chain.


## Cross-References

- <a href="/xray-mp-wiki/proteins/secretion-translocon/secy/">Thermus thermophilus SecY Core Channel Subunit</a> — Homologous SecY channel protein from a different organism
- <a href="/xray-mp-wiki/proteins/secretion-translocon/secyeg/">Thermus thermophilus SecYEG Translocon Complex</a> — Homologous SecYEG complex from a different organism
- <a href="/xray-mp-wiki/proteins/secretion-translocon/sece/">SecE Accessory Subunit</a> — SecE is the essential accessory subunit of the SecY complex
- <a href="/xray-mp-wiki/proteins/secretion-translocon/secg/">SecG Accessory Subunit</a> — SecG (homolog of Secbeta) is the accessory subunit of the SecY complex
- <a href="/xray-mp-wiki/proteins/secretion-translocon/methanococcus-jannaschii-secy/">Methanococcus jannaschii SecY Translocation Channel</a> — Homologous archaeal SecY; used as molecular replacement model for Pfu-SecYE structure solution
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — The SecY channel undergoes conformational changes to alternately open the lateral gate and displace the plug during translocation
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> — Additive used in purification or crystallization buffers
