---
title: "LmrP Multidrug Transporter from Lactococcus lactis"
created: 2026-06-16
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-020-0464-y]
verified: agent
uniprot_id: Q48658
---

# LmrP Multidrug Transporter from Lactococcus lactis

<div class="expr-badges"><span class="expr-badge expr-l-lactis">L. lactis</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q48658">UniProt: Q48658</a>

<span class="expr-badge">Lactococcus lactis</span>

## Overview

LmrP is a prototypical multidrug efflux pump from Lactococcus lactis belonging
to the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/)). It exports structurally diverse
lipophilic cationic compounds ranging from antibiotics to DNA dyes, including
[Hoechst 33342](/xray-mp-wiki/reagents/additives/hoechst-33342/), [Ethidium - Fluorescent Intercalating Dye](/xray-mp-wiki/reagents/ligands/ethidium/) bromide, roxithromycin, tetraphenyl phosphonium (TPP+),
[Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/), and tetracycline. LmrP uses a proton-motive force for drug efflux
and alternates between inward-open and outward-open conformations depending on
protonation states of key acidic residues (Asp68 and Glu327). The 2.9 A crystal
structure of LmrP bound to [Hoechst 33342](/xray-mp-wiki/reagents/additives/hoechst-33342/) in an outward-open state revealed an
embedded lipid ([Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/), PG) within the substrate-binding cavity,
suggesting a mechanism for polyspecificity where the lipid provides a malleable
hydrophobic component to accommodate diverse substrates.


## Publications

### doi/10.1038##s41594-020-0464-y

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6t1z">6T1Z</a></td>
      <td>2.9</td>
      <td>C2221</td>
      <td>LmrP delta199-202 (loop deletion mutant), expressed in Lactococcus lactis NZ9000</td>
      <td><a href="/xray-mp-wiki/reagents/additives/hoechst-33342/">Hoechst 33342</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Lactococcus lactis NZ9000
- **Construct**: Full-length LmrP with delta199-202 deletion; pHLP5-3C expression plasmid; nisin-inducible

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
      <td>1. Cell lysis and membrane vesicle preparation</td>
      <td>High-pressure homogenizer (6 passes at 15,000 psi)</td>
      <td>—</td>
      <td>100 mM HEPES pH 7, 300 mM NaCl, 20% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Cells treated with lysozyme (5 mg/mL), MgSO4 (10 mM), and DNase I (10 ug/mL) before lysis; membranes collected by ultracentrifugation at 125,000g</td>
    </tr>
    <tr>
      <td>2. Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/n-dodecyl-beta-d-maltoside/">DDM</a> (beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes solubilized with 2.4% (w/v) beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> in water for 1 h at 4 C; insoluble fragments removed at 100,000g</td>
    </tr>
    <tr>
      <td>3. <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> (Qiagen)</td>
      <td>50 mM HEPES pH 7, 150 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> for binding; 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> wash; 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> elution</td>
    </tr>
    <tr>
      <td>4. Desalting</td>
      <td>PD10 desalting column</td>
      <td>—</td>
      <td>50 mM HEPES pH 7, 150 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> removal</td>
    </tr>
    <tr>
      <td>5. Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td>SDX 200 10/300 GL increase (GE Lifescience)</td>
      <td>20 mM HEPES pH 7, 100 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.02% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Concentrated using spin-concentrators (VWR)</td>
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
      <td>Purified LmrP in 20 mM HEPES pH 7, 100 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.02% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, co-crystallized with <a href="/xray-mp-wiki/reagents/additives/hoechst-33342/">Hoechst 33342</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not explicitly specified in paper (see Methods for detailed crystallization screening)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallization required extensive screening; precise control of lipidation state essential; highest-resolution crystals required delta199-202 loop deletion; co-crystallization with <a href="/xray-mp-wiki/reagents/additives/hoechst-33342/">Hoechst 33342</a>; SeMet derivative crystals used for phasing</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>sitting-drop</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6t1z">6T1Z</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">GKEFWNLDKNLQLR</span><span class="topo-membrane">LGIVFLGAFSYGTVFSSM</span><span class="topo-outside">TIYYNQYLGSAITGIL</span><span class="topo-membrane">LALSAVATFVAGILAG</span><span class="topo-inside">FFADRNGRKPV</span><span class="topo-membrane">MVFGTIIQLLGAALAIAS</span><span class="topo-outside">NLPGHVNPWS</span><span class="topo-membrane">TFIAFLLISFGYNFVIT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AGN</span><span class="topo-inside">AMIIDASNAENRKVVFM</span><span class="topo-membrane">LDYWAQNLSVILGAALGAWL</span><span class="topo-outside">FRPAFE</span><span class="topo-membrane">ALLVILLLTVLVSFFLT</span><span class="topo-inside">TFVMTETFKPT</span><span class="topo-unknown">VKV</span><span class="topo-inside">DN</span><span class="topo-unknown">IFQAYKTVLQ</span><span class="topo-inside">DKTYM</span><span class="topo-membrane">IFMGANIATTFIIMQFDNFL</span><span class="topo-outside">PVHLSN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SFKTIT</span><span class="topo-unknown">FWGFEI</span><span class="topo-outside">YGQRML</span><span class="topo-membrane">TIYLILACVLVVLLMTTL</span><span class="topo-inside">NRLTKDWSHQKGF</span><span class="topo-membrane">IWGSLFMAIGMIFSFLT</span><span class="topo-outside">TTFT</span><span class="topo-membrane">PIFIAGIVYTLGEIVYTP</span><span class="topo-inside">SVQTLGADLMNPEKIGSYN</span><span class="topo-membrane">GVAAIKMPIASIL</span></span>
<span class="topo-ruler">       370       380       390       400       410 </span>
<span class="topo-line"><span class="topo-membrane">AGLLV</span><span class="topo-outside">SISPMIKA</span><span class="topo-membrane">IGVSLVLALTEVLAIIL</span><span class="topo-inside">VLVAVNRHQKTK</span><span class="topo-unknown">LNLEVLFQG</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Inside</td>
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
      <td>48</td>
      <td>33</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>64</td>
      <td>49</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>75</td>
      <td>65</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>93</td>
      <td>76</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>103</td>
      <td>94</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>123</td>
      <td>104</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>124</td>
      <td>140</td>
      <td>124</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>160</td>
      <td>141</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>166</td>
      <td>161</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>167</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>194</td>
      <td>184</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>199</td>
      <td>198</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>209</td>
      <td>204</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>210</td>
      <td>214</td>
      <td>214</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>219</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>246</td>
      <td>239</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>258</td>
      <td>257</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>276</td>
      <td>263</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>289</td>
      <td>281</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>306</td>
      <td>294</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>311</td>
      <td>314</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>328</td>
      <td>315</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>347</td>
      <td>333</td>
      <td>351</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>365</td>
      <td>352</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>366</td>
      <td>373</td>
      <td>370</td>
      <td>377</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>390</td>
      <td>378</td>
      <td>394</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>391</td>
      <td>402</td>
      <td>395</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Embedded lipid in the binding cavity

The crystal structure reveals a [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) (PG) lipid embedded within the substrate-binding cavity of LmrP, in close proximity to bound [Hoechst 33342](/xray-mp-wiki/reagents/additives/hoechst-33342/). The lipid likely originates from the native L. lactis membrane and remains bound through purification. Molecular dynamics simulations show that the anionic lipid ([POPG](/xray-mp-wiki/reagents/lipids/popg/)) stabilizes the observed ligand-bound conformation by maintaining the Arg14-Asp142 salt bridge in the N-lobe.

### Limited conformational adaptation to substrates

DEER spectroscopy with six structurally diverse substrates ([Hoechst 33342](/xray-mp-wiki/reagents/additives/hoechst-33342/), [Ethidium - Fluorescent Intercalating Dye](/xray-mp-wiki/reagents/ligands/ethidium/) bromide, roxithromycin, TPP+, [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/), tetracycline) shows that LmrP adopts a common outward-open conformation for high-affinity binding without requiring large conformational changes of the protein scaffold.

### Substrate-dependent role of embedded lipid

Mutations that disrupt lipid binding (S52Y, T56Y, N116Y) reduce transport of [Hoechst 33342](/xray-mp-wiki/reagents/additives/hoechst-33342/), tetracycline, and [Erythromycin](/xray-mp-wiki/reagents/ligands/erythromycin/), but do not affect clindamycin transport, demonstrating substrate-specific dependence on the embedded lipid. This suggests the lipid contributes to polyspecificity by providing a malleable hydrophobic environment.

### Native MS confirms tightly bound PG

[Native Mass Spectrometry](/xray-mp-wiki/methods/quality-assessment/native-mass-spectrometry/) of LmrP reconstituted in [DOPE](/xray-mp-wiki/reagents/lipids/dope/)/DOPG nanodiscs shows a tightly bound [DOPG](/xray-mp-wiki/reagents/lipids/dopg/) molecule that is lost in the N116Y mutant, confirming the specificity of PG binding in the cavity.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily</a> — LmrP is a prototypical MFS multidrug transporter
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/antibiotic-efflux-pump/">Antibiotic Efflux Pump</a> — LmrP is a multidrug efflux pump; the paper discusses mechanism of polyspecific drug export
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — LmrP alternates between inward-open and outward-open states depending on protonation
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/substrate-polyspecificity-smr-transporters/">Substrate Polyspecificity in SMR Transporters</a> — The embedded lipid mechanism proposed may relate to polyspecificity mechanisms across transporter families
- <a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> — POPG (DOPG analog) is the embedded lipid in LmrP binding cavity
- <a href="/xray-mp-wiki/reagents/additives/hoechst-33342/">Hoechst 33342</a> — Hoechst 33342 is the substrate in the crystal structure
- <a href="/xray-mp-wiki/proteins/mfs-transporters/mdfa/">MdfA (E. coli Multidrug Transporter)</a> — MdfA is another MFS multidrug transporter with known outward-open structure, used for comparison
- <a href="/xray-mp-wiki/reagents/detergents/n-dodecyl-beta-d-maltoside/">n-Dodecyl-beta-D-Maltoside (beta-DDM)</a> — Primary detergent used for LmrP solubilization and purification
- <a href="/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/">MFS</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
