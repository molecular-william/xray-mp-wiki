---
title: "TrVKORL (Pufferfish Vitamin K Epoxide Reductase-Like)"
created: 2026-06-10
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.abc5667]
verified: false
---

# TrVKORL (Pufferfish Vitamin K Epoxide Reductase-Like)

## Overview

TrVKORL is a [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide reductase-like protein from the pufferfish Takifugu rubripes. It shares 73% sequence identity with human VKOR-like (HsVKORL) and 52% with [HSVKOR](/xray-mp-wiki/proteins/enzymes/hsvkor/). TrVKORL is catalytically active and inhibitable by [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/), both in cells and after purification. Its higher expression level and better in vitro stability than HsVKORL enabled capture of both ligand-free and warfarin-bound states, providing the structural basis for understanding the conformational changes associated with VKOR catalysis and inhibition. The protein adopts two distinct conformations: an open conformation in the ligand-free state and a closed conformation induced by [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) or substrate binding.


## Publications

### doi/10.1126##science.abc5667

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6wvi">6WVI</a></td>
      <td>2.9</td>
      <td></td>
      <td>TrVKORL (6-175) wild-type, ligand-free</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6wvb">6WVB</a></td>
      <td>2.9</td>
      <td></td>
      <td>TrVKORL (6-175) with <a href="/xray-mp-wiki/reagents/ligands/warfarin/">Warfarin</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/warfarin/">Warfarin</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6wv9">6WV9</a></td>
      <td>2.8</td>
      <td></td>
      <td>TrVKORL (6-175) with <a href="/xray-mp-wiki/reagents/cofactors/vitamin-k/">Vitamin K</a> quinone (co-crystallized with KO)</td>
      <td><a href="/xray-mp-wiki/reagents/cofactors/vitamin-k/">Vitamin K</a> quinone (K)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6wva">6WVA</a></td>
      <td>2.9</td>
      <td></td>
      <td>TrVKORL (6-175) co-crystallized with <a href="/xray-mp-wiki/reagents/cofactors/vitamin-k/">Vitamin K</a> epoxide (KO)</td>
      <td><a href="/xray-mp-wiki/reagents/cofactors/vitamin-k/">Vitamin K</a> epoxide (KO)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6wv8">6WV8</a></td>
      <td>2.8</td>
      <td></td>
      <td>TrVKORL Cys132Ser mutant (6-175) with <a href="/xray-mp-wiki/reagents/cofactors/vitamin-k/">Vitamin K</a> quinone (K)</td>
      <td><a href="/xray-mp-wiki/reagents/cofactors/vitamin-k/">Vitamin K</a> quinone (K)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: TrVKORL (6-175)
- **Notes**: Higher expression level and better in vitro stability than HsVKORL, enabling crystallization without fusion tags

**Purification:**

- **Expression system**: Pichia pastoris
- **Expression construct**: TrVKORL (6-175) wild-type or Cys138Ser (Cys132Ser) mutant
- **Tag info**: Native, no purification tag

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
      <td>Cell culture and induction</td>
      <td><a href="/xray-mp-wiki/reagents/additives/methanol/">Methanol</a> induction in Pichia pastoris</td>
      <td></td>
      <td>BMG media (1.2% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.34% YNB, 1% <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a>, 0.4 ug/mL biotin, 100 mM potassium phosphate pH 6.0); BMM media for induction</td>
      <td>1 L culture in BMG at 30C for 20 hr, then switched to BMM with 0.7% <a href="/xray-mp-wiki/reagents/additives/methanol/">Methanol</a> at 25C for 2 days</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Ball mill</td>
      <td></td>
      <td>225 mM NaCl, 75 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 10 ug/mL DNase I + 2% n-Dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Frozen cells broken by ball mill; membranes solubilized with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for 3 hr at 4C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> metal-affinity resin (Clontech)</td>
      <td>Wash: 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 150 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 20 mM Tris pH 8.0; Elution: 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 150 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 20 mM Tris pH 8.0
 + 0.2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Protein incubated with <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin for 3 hr at 4C</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography (SEC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>150 mM NaCl, 20 mM Tris pH 8.0 + 0.05% Lauryl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol (<a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>)</td>
      <td>Peak fractions collected; concentrated to 40 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: 40 mg/mL in 150 mM NaCl, 20 mM Tris pH 8.0, 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TrVKORL (wild-type or mutant); 40 mg/mL</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (v/v)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals appeared within one week, optimal size after several weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>For ligand-free TrVKORL, no ligand added during purification. For <a href="/xray-mp-wiki/reagents/ligands/warfarin/">Warfarin</a> complex, 1 mM <a href="/xray-mp-wiki/reagents/ligands/warfarin/">Warfarin</a> added during cell lysis before <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> solubilization and maintained throughout. For substrate complexes (K, KO), ligands mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> for co-crystallization. Data collected at APS NE-CAT beamlines.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6wvi">6WVI</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTL</span><span class="topo-unknown">G</span><span class="topo-inside">VQCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IELKGIDFKEDGNILGHKLEYNLRVSTPRWERI</span><span class="topo-membrane">ARVLVCLLGILLSLYAFHVE</span><span class="topo-outside">REHARDPSYKALCDVSSSISCSKVFGSRWGRGFGLL</span><span class="topo-membrane">GSIFGNDSALNQPNSVYGIVFYAFQLLLG</span><span class="topo-inside">MT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VSAMAALI</span><span class="topo-membrane">LMTTSIMSVVGSLYLGYILYFV</span><span class="topo-outside">LKDL</span><span class="topo-membrane">CVICVTTYALNFILFVLN</span><span class="topo-inside">YKRLVYLNEAWKQKL</span><span class="topo-unknown">QA</span><span class="topo-inside">KQDNSHNVYITADKQKNGIKANFKIRHNVEDGSVQLADHYQQNTPIGDGPV</span></span>
<span class="topo-ruler">       370       380       390       400       410    </span>
<span class="topo-line"><span class="topo-inside">LLPDNHYLSTQSVLSKDPNEKRDHMVLLEFVTAAGITHGMDELYKSNSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>64</td>
      <td>1</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>65</td>
      <td>65</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>66</td>
      <td>153</td>
      <td>68</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>173</td>
      <td>156</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>209</td>
      <td>176</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>238</td>
      <td>212</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>248</td>
      <td>241</td>
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
      <td>292</td>
      <td>277</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>293</td>
      <td>307</td>
      <td>295</td>
      <td>309</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>309</td>
      <td>310</td>
      <td>311</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>310</td>
      <td>414</td>
      <td>312</td>
      <td>416</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6wvb">6WVB</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MS</span><span class="topo-inside">KGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTL</span><span class="topo-unknown">G</span><span class="topo-inside">VQCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IELKGIDFKEDGNILGHKLEYNLRVSTPRWERI</span><span class="topo-membrane">ARVLVCLLGILLSLYAF</span><span class="topo-outside">HVEREHARDPSYKALCDVSSSISCSKVFGSRWGRGFGLLGSIFGNDSALNQPN</span><span class="topo-membrane">SVYGIVFYAFQLLLG</span><span class="topo-inside">MT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VSAMAAL</span><span class="topo-membrane">ILMTTSIMSVVGSLYLGY</span><span class="topo-outside">ILYFVLKDLC</span><span class="topo-membrane">VICVTTYALNFILFVLN</span><span class="topo-inside">YKRLVYLNEAWKQKLQAKQDNSHNVYITADKQKNGIKANFKIRHNVEDGSVQLADHYQQNTPIGDGPV</span></span>
<span class="topo-ruler">       370       380       390       400       410    </span>
<span class="topo-line"><span class="topo-inside">LLPDNHYLSTQSVLSKDPNEKRDHMVLLEFVTAAGITH</span><span class="topo-unknown">GMD</span><span class="topo-inside">ELYKSNSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>64</td>
      <td>3</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>65</td>
      <td>65</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>66</td>
      <td>153</td>
      <td>68</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>170</td>
      <td>156</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>223</td>
      <td>173</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>238</td>
      <td>226</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>247</td>
      <td>241</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>265</td>
      <td>250</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>275</td>
      <td>268</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>292</td>
      <td>278</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>293</td>
      <td>398</td>
      <td>295</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>401</td>
      <td>401</td>
      <td>403</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>402</td>
      <td>414</td>
      <td>404</td>
      <td>416</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6wv9">6WV9</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTL</span><span class="topo-unknown">G</span><span class="topo-inside">VQCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IELKGIDFKEDGNILGHKLEYNLRVSTPRWERI</span><span class="topo-membrane">ARVLVCLLGILLSLYAF</span><span class="topo-outside">HVEREHARDPSYKALCDVSSSISCSKVFGSRWGRGFGLLGSIFGNDS</span><span class="topo-membrane">ALNQPNSVYGIVFYAFQLLL</span><span class="topo-inside">GMT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VSAMAALI</span><span class="topo-membrane">LMTTSIMSVVGSLYLGYILY</span><span class="topo-outside">FVLKDLC</span><span class="topo-membrane">VICVTTYALNFILFVL</span><span class="topo-inside">NYKRLVYLNEAWKQKL</span><span class="topo-unknown">QA</span><span class="topo-inside">KQDNSHNVYITADKQKNGIKANFKIRHNVEDGSVQLADHYQQNTPIGDGPV</span></span>
<span class="topo-ruler">       370       380       390       400       410    </span>
<span class="topo-line"><span class="topo-inside">LLPDNHYLSTQSVLSKDPNEKRDHMVLLEFVTAAGITHGMDELYKSNSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>64</td>
      <td>1</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>153</td>
      <td>68</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>170</td>
      <td>156</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>217</td>
      <td>173</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>237</td>
      <td>220</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>248</td>
      <td>240</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>268</td>
      <td>251</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>275</td>
      <td>271</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>278</td>
      <td>293</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>307</td>
      <td>294</td>
      <td>309</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>414</td>
      <td>312</td>
      <td>416</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6wva">6WVA</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTL</span><span class="topo-unknown">G</span><span class="topo-inside">VQCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IELKGIDFKEDGNILGHKLEYNLRVSTPRWERI</span><span class="topo-membrane">ARVLVCLLGILLSLYAFH</span><span class="topo-outside">VEREHARDPSYKALCDVSSSISCSKVFGSRWGRGFGLLGSIFGNDS</span><span class="topo-membrane">ALNQPNSVYGIVFYAFQLLL</span><span class="topo-inside">GMT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VSAMAALIL</span><span class="topo-membrane">MTTSIMSVVGSLYLGYILYFV</span><span class="topo-outside">LKDL</span><span class="topo-membrane">CVICVTTYALNFILFV</span><span class="topo-inside">LNYKRLVYLNEAWKQKL</span><span class="topo-unknown">QA</span><span class="topo-inside">KQDNSHNVYITADKQKNGIKANFKIRHNVEDGSVQLADHYQQNTPIGDGPV</span></span>
<span class="topo-ruler">       370       380       390       400       410    </span>
<span class="topo-line"><span class="topo-inside">LLPDNHYLSTQSVLSKDPNEKRDHMVLLEFVTAAGITHGMDELYKSNSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>64</td>
      <td>1</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>153</td>
      <td>68</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>171</td>
      <td>156</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>217</td>
      <td>174</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>237</td>
      <td>220</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>249</td>
      <td>240</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>270</td>
      <td>252</td>
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
      <td>290</td>
      <td>277</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>291</td>
      <td>307</td>
      <td>293</td>
      <td>309</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>414</td>
      <td>312</td>
      <td>416</td>
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

### Open and closed conformations

TrVKORL adopts an open conformation in the ligand-free state, characterized by a luminal helix that converts into loop 1 and beta-hairpin upon [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) or substrate binding. The closed conformation induced by [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) is very similar to that induced by substrate (K) binding, with the cap domain, loop 1, and beta-hairpin adopting essentially the same conformation. This open-to-closed transition is triggered by hydrogen bonding interactions with Asn80 and Tyr139.

### Warfarin-induced conformational changes

[Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) binding induces a global conformational change from open to closed state. In the closed state, Cys43-Cys51 are repositioned to interact with loop 3-4, the cap helix and beta-hairpin are formed, and Asp44 becomes a central residue holding these elements together. In the open conformation, Asp44 is located on the luminal helix and does not participate in stabilizing interactions.

### Substrate-induced reduction and charge-transfer complex

The Cys132Ser mutant of TrVKORL with K bound reveals a charge-transfer complex between Cys135 thiolate and the naphthoquinone ring of K (S to C2 distance ~3 A). This complex stabilizes K within the active site and triggers the open-to-closed conformational change, bringing Cys43-Cys51 close to Cys135-K for thiol-disulfide exchange that resolves the adduct and fully reduces K.

### Similarity between warfarin and substrate-bound states

The closed conformation induced by [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) closely resembles that induced by the Cys135-K charge-transfer adduct. [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) exploits features tailored for substrate binding: hydrogen bonding to Asn80 and Tyr139, and interaction of its side group with the same residues (Phe83, Phe87, Tyr88) that bind the isoprenyl chain of [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/). This explains how VKAs stably occupy the active site.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/hsvkor/">Human Vitamin K Epoxide Reductase (HsVKOR)</a> — Mammalian homolog; TrVKORL shares 52% sequence identity and same overall structure
- <a href="/xray-mp-wiki/proteins/enzymes/synechococcus-vkor/">VKOR from Synechococcus sp.</a> — Bacterial VKOR homolog providing complementary structural information
- <a href="/xray-mp-wiki/reagents/ligands/warfarin/">Warfarin</a> — VKA used to capture closed conformation of TrVKORL
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/vitamin-k-cycle/">Vitamin K Catalytic Cycle</a> — Catalytic cycle described through TrVKORL structures in different states
- <a href="/xray-mp-wiki/concepts/miscellaneous/termini-restraining/">Termini Restraining</a> — TrVKORL structure was determined using the termini-restraining approach with split sfGFP
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used for TrVKORL membrane solubilization
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used for LCP crystallization of TrVKORL
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
