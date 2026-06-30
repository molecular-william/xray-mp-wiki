---
title: "YajR Transporter (E. coli MFS Drug Efflux Transporter)"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1308127110]
verified: false
---

# YajR Transporter (E. coli MFS Drug Efflux Transporter)

## Overview

YajR is a 49-kDa putative proton-driven [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) (Major Facilitator Superfamily) drug efflux
transporter from Escherichia coli. It consists of 454 amino acid residues and features
the canonical 12-transmembrane (TM) helix core characteristic of [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) transporters,
as well as a unique 65-residue C-terminal YAM domain (YajR/AraEP/MBD) with a
ferredoxin-like fold. The crystal structure of YajR was determined at 3.15 Å resolution
in an outward-facing conformation, revealing the functional role of the conserved
"sequence motif A" in stabilizing the outward conformation and suggesting a general
mechanism for the conformational change between inward and outward states of [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/)
transporters. YajR belongs to the DHA12 (12-TM drug-resistance H+-driven antiporter)
subfamily and shares highest sequence homology with [EMRD](/xray-mp-wiki/proteins/mfs-transporters/emrd/) (21% identity).



## Publications

### doi/10.1073##pnas.1308127110

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3wdo">3WDO</a></td>
      <td>3.15 A</td>
      <td>TBD</td>
      <td>Full-length YajR (residues 1-454) from E. coli, including YAM domain (residues 389-454)</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length YajR (wild-type and mutants G69W, D73R, G55C-G355C)

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
      <td>Standard culture media</td>
      <td>YajR expressed in E. coli cells</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Standard affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> (presumed, based on His-tag immunoblot)</td>
      <td>Not explicitly reported in main text + Not explicitly reported</td>
      <td>Purification details in SI Appendix</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Standard crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified YajR</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not explicitly reported in main text</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not reported</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not reported</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 3.15 Å resolution. The structure reveals an outward-facing conformation with the cytoplasmic side closed and the periplasmic side accessible to solvent.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3wdo">3WDO</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">DYKMTPGER</span><span class="topo-membrane">RATWGLGTVFSLRMLGMFMVLP</span><span class="topo-inside">VLTTYGMALQGASEALIGI</span><span class="topo-membrane">AIGIYGLTQAVFQIPFGLLS</span><span class="topo-outside">DRIGRK</span><span class="topo-membrane">PLIVGGLAVFAAGSVIAALS</span><span class="topo-inside">DSIW</span><span class="topo-membrane">GIILGRALQGSGAIAAAVMA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LLSDLTREQNR</span><span class="topo-membrane">TKAMAFIGVSFGITFAIAMVLG</span><span class="topo-inside">PIITHKL</span><span class="topo-membrane">GLHALFWMIAILATTGIALTIWV</span><span class="topo-outside">VPNSSTHVLNRESGMVK</span><span class="topo-unknown">GSFSKVL</span><span class="topo-membrane">AEPRLLKLNFGIMCLHMLLMSTF</span><span class="topo-inside">VALPGQLADA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GFPAAEHW</span><span class="topo-membrane">KVYLATMLIAFGSVVPFIIYAE</span><span class="topo-outside">VKRK</span><span class="topo-membrane">MKQVFVFCVGLIVVAEIVLW</span><span class="topo-inside">NAQTQFWQLV</span><span class="topo-membrane">VGVQLFFVAFNLMEALLPSLIS</span><span class="topo-outside">KESPAGYKG</span><span class="topo-membrane">TAMGVYSTSQFLGVAIGGSLG</span><span class="topo-inside">GWID</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450   </span>
<span class="topo-line"><span class="topo-inside">GMFDGQGV</span><span class="topo-membrane">FLAGAMLAAVWLAVASTM</span><span class="topo-outside">KEPPYVSSLRIEIPADIAANEALKVRLLETEGVKEVLIAEEEHSAYVKIDSKVTNRFEVEQAIRQAL</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>9</td>
      <td>3</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>31</td>
      <td>12</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>50</td>
      <td>34</td>
      <td>52</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>70</td>
      <td>53</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>76</td>
      <td>73</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>96</td>
      <td>79</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>100</td>
      <td>99</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>120</td>
      <td>103</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>131</td>
      <td>123</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>153</td>
      <td>134</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>160</td>
      <td>156</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>183</td>
      <td>163</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>200</td>
      <td>186</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>207</td>
      <td>203</td>
      <td>209</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>208</td>
      <td>230</td>
      <td>210</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>233</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>270</td>
      <td>251</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>271</td>
      <td>274</td>
      <td>273</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>277</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>304</td>
      <td>297</td>
      <td>306</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>326</td>
      <td>307</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>335</td>
      <td>329</td>
      <td>337</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>356</td>
      <td>338</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>368</td>
      <td>359</td>
      <td>370</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>386</td>
      <td>371</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>453</td>
      <td>389</td>
      <td>455</td>
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

### Outward-facing conformation with 12-TM core and C-terminal YAM domain

The YajR structure features 12 canonical TM helices organized as N-domain (TMs 1-6)
and C-domain (TMs 7-12), forming a central TM channel. The structure also includes
a unique 65-residue C-terminal domain (YAM domain, residues 389-454) with a
ferredoxin-like fold, located cytoplasmically. The central cavity between the N and C
domains is closed on the cytoplasmic side and open to the periplasm, defining the
outward-facing conformation. Based on sequence analysis, the TM core of YajR shares
highest homology with [EMRD](/xray-mp-wiki/proteins/mfs-transporters/emrd/) (21% identity), a DHA12 subfamily member.

### Motif A stabilizes the outward conformation via interdomain interactions

The conserved [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) motif A (G69LLSD73RIGR77KP in YajR) is located in the loop L2-3
connecting TMs 2 and 3. Key interactions: (i) Gly69(+1) of TM2 forms close helix-helix
contacts with conserved Gly337 and Gly341 of TM11, creating an interdomain helical
bundle essential for the outward conformation. (ii) Asp73(+5) is completely buried in
the domain interface in the outward conformation (zero side-chain solvent-accessible
surface) and acts as an N-cap for TM11, stabilizing the helix via a charge-helix dipole
interaction. A D73R mutation decreased melting temperature by ~20 °C. (iii) Arg77(+9)
interacts with both Asp73(+5) and conserved Asp126 at the C-terminal end of TM4,
forming a charge-relay system. (iv) The charge-helix dipole interaction provides
~4 kJ/mol stabilization energy.

### Transport mechanism based on membrane potential and protonation

The paper proposes that for H+-driven electrogenic [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) transporters: (i) The outward
conformation is the ground state. (ii) The inward conformation is an excited state.
(iii) The outward-to-inward transition is triggered by protonation inside the central
cavity (by His225-Glu320 pair in YajR) combined with the negative-inside membrane
potential (ΔΨ ~150 mV). The membrane potential applies an electrostatic force on the
protonated residue, producing ~15 kJ/mol (FΔΨ) energy. (iv) The inward-to-outward
return is driven by deprotonation (due to alkaline cytosol) and basic residue
distribution on the cytoplasmic side. Motif A functions as a molecular switch
regulating these conformational changes.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — YajR is an MFS transporter; the paper elucidates MFS transport mechanisms
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/">Rocker-Switch Mechanism</a> — MFS transporters including YajR use the rocker-switch mechanism for alternating access
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/motif-a-mfs/">MFS Motif A and Charge-Helix Dipole Interactions</a> — The paper is the primary structural elucidation of motif A function in MFS transporters
- <a href="/xray-mp-wiki/concepts/major-facilitator-superfamily/">MFS</a> — Related biological concept
- <a href="/xray-mp-wiki/proteins/mfs-transporters/emrd/">EMRD</a> — Related protein structure
