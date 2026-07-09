---
title: "ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.51511, doi/10.1074##jbc.M112.424507, doi/10.1038##ncomms1703, doi/10.1038##s41589-019-0369-4]
verified: regex
uniprot_id: P0C7B7
---

# ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0C7B7">UniProt: P0C7B7</a>

<span class="expr-badge">Dickeya chrysanthemi</span>

## Overview

ELIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from the bacterium Erwinia chrysanthemi (now Dickeya dadantii). It is a homopentameric channel gated by GABA that serves as a bacterial homolog of eukaryotic Cys-loop receptors including nicotinic  receptors,  5-HT3 receptors, GABA-A receptors, and  receptors. ELIC has been extensively used as a model system for understanding pLGIC structure, allosteric modulation, and ion channel gating. The channel exhibits distinct Ω-loop conformations at the vestibule entrance that determine access to an allosteric binding site, with ELIC adopting the Ω-open conformation that creates an accessible vestibule site.


## Publications

### doi/10.7554##eLife.51511

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ssi">6SSI</a></td>
      <td>2.59</td>
      <td>Not specified</td>
      <td>ELIC + PAM-Nb complex</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ssp">6SSP</a></td>
      <td>3.25</td>
      <td>Not specified</td>
      <td>ELIC + NAM-Nb complex</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43
- **Construct**: Signal sequence of human α7 nAChR followed by mature ELIC sequence, pGEM-HE plasmid
- **Notes**: Also expressed in Xenopus oocytes for electrophysiology using the pGEM-HE expression plasmid

**Purification:**

- **Expression system**: E. coli C43
- **Expression construct**: Full-length ELIC in pGEM-HE or similar expression vector

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
      <td>LB medium</td>
      <td>—</td>
      <td></td>
      <td>Expression induced with 200 uM </td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Not detailed in this paper</td>
      <td>—</td>
      <td></td>
      <td>Referenced to Spurny et al. 2012 methods</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>IMAC</td>
      <td>Ni-NTA</td>
      <td></td>
      <td>Referenced to Spurny et al. 2012 for standard ELIC purification protocol</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>SEC</td>
      <td>—</td>
      <td></td>
      <td>ELIC purified in detergent solution prior to  complex formation</td>
    </tr>
    <tr>
      <td> complex formation</td>
      <td>Co-incubation</td>
      <td>—</td>
      <td></td>
      <td>Purified ELIC incubated with excess PAM-Nb or NAM-Nb prior to crystallization</td>
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
      <td>ELIC + PAM-Nb complex</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>ELIC + NAM-Nb complex</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ssi">6SSI</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPVD</span><span class="topo-outside">ARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLS</span><span class="topo-unknown">SVQ</span><span class="topo-outside">PNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-inside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-outside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-inside">AHHRQAN</span><span class="topo-unknown">GVE</span><span class="topo-inside">DDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCV</span><span class="topo-outside">LVI</span><span class="topo-unknown">RGITG</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>4</td>
      <td>5</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>175</td>
      <td>9</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>178</td>
      <td>180</td>
      <td>182</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>179</td>
      <td>206</td>
      <td>183</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>221</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>225</td>
      <td>226</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>246</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>285</td>
      <td>283</td>
      <td>289</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>288</td>
      <td>290</td>
      <td>292</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>293</td>
      <td>293</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>310</td>
      <td>298</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>313</td>
      <td>315</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>318</td>
      <td>318</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ssi">6SSI</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GP</span><span class="topo-outside">VDARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLS</span><span class="topo-unknown">SVQ</span><span class="topo-outside">PNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-inside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-outside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-inside">AHHRQANG</span><span class="topo-unknown">VE</span><span class="topo-inside">DDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCV</span><span class="topo-outside">LVIRG</span><span class="topo-unknown">ITG</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>5</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>175</td>
      <td>7</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>178</td>
      <td>180</td>
      <td>182</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>179</td>
      <td>206</td>
      <td>183</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>221</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>225</td>
      <td>226</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>246</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>286</td>
      <td>283</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>288</td>
      <td>291</td>
      <td>292</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>293</td>
      <td>293</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>310</td>
      <td>298</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>315</td>
      <td>315</td>
      <td>319</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>318</td>
      <td>320</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ssi">6SSI</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GP</span><span class="topo-outside">VDARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLS</span><span class="topo-unknown">SVQ</span><span class="topo-outside">PNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-inside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-outside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIFA</span><span class="topo-inside">HHRQAN</span><span class="topo-unknown">GVE</span><span class="topo-inside">DDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCV</span><span class="topo-outside">LVIRG</span><span class="topo-unknown">ITG</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>5</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>175</td>
      <td>7</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>178</td>
      <td>180</td>
      <td>182</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>179</td>
      <td>206</td>
      <td>183</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>221</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>225</td>
      <td>226</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>246</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>279</td>
      <td>266</td>
      <td>283</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>285</td>
      <td>284</td>
      <td>289</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>288</td>
      <td>290</td>
      <td>292</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>293</td>
      <td>293</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>310</td>
      <td>298</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>315</td>
      <td>315</td>
      <td>319</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>318</td>
      <td>320</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ssi">6SSI</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GP</span><span class="topo-outside">VDARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLS</span><span class="topo-unknown">S</span><span class="topo-outside">VQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-inside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-outside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-inside">AHHRQAN</span><span class="topo-unknown">GVED</span><span class="topo-inside">DLLIQR</span><span class="topo-membrane">CRLAFPLGFLAIGCV</span><span class="topo-outside">LV</span><span class="topo-unknown">IRGITG</span></span>
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
      <td>5</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>175</td>
      <td>7</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>206</td>
      <td>181</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>221</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>225</td>
      <td>226</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>246</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>285</td>
      <td>283</td>
      <td>289</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>289</td>
      <td>290</td>
      <td>293</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>290</td>
      <td>295</td>
      <td>294</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>310</td>
      <td>300</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>312</td>
      <td>315</td>
      <td>316</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>313</td>
      <td>318</td>
      <td>317</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ssi">6SSI</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPVD</span><span class="topo-outside">ARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLS</span><span class="topo-unknown">SVQ</span><span class="topo-outside">PNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-inside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-outside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-inside">AHHRQANGV</span><span class="topo-unknown">ED</span><span class="topo-inside">DLLIQ</span><span class="topo-membrane">RCRLAFPLGFLAIGCV</span><span class="topo-outside">LVI</span><span class="topo-unknown">RGITG</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>4</td>
      <td>5</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>175</td>
      <td>9</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>178</td>
      <td>180</td>
      <td>182</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>179</td>
      <td>206</td>
      <td>183</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>221</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>225</td>
      <td>226</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>246</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>287</td>
      <td>283</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>289</td>
      <td>292</td>
      <td>293</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>290</td>
      <td>294</td>
      <td>294</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>310</td>
      <td>299</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>313</td>
      <td>315</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>318</td>
      <td>318</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ssp">6SSP</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPVD</span><span class="topo-inside">ARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHL</span><span class="topo-unknown">SSVQP</span><span class="topo-inside">NQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-inside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQA</span><span class="topo-unknown">NG</span><span class="topo-outside">VEDDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCV</span><span class="topo-unknown">LVIRGITG</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>5</td>
      <td>174</td>
      <td>9</td>
      <td>178</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>206</td>
      <td>184</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>221</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>225</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>246</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>284</td>
      <td>283</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>293</td>
      <td>291</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>310</td>
      <td>298</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ssp">6SSP</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPVDA</span><span class="topo-inside">RPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-inside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQAN</span><span class="topo-unknown">GV</span><span class="topo-outside">EDDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCVL</span><span class="topo-unknown">VIRGITG</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>6</td>
      <td>206</td>
      <td>10</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>221</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>225</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>246</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>285</td>
      <td>283</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>293</td>
      <td>292</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>311</td>
      <td>298</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ssp">6SSP</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPVDA</span><span class="topo-inside">RPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSV</span><span class="topo-unknown">QP</span><span class="topo-inside">NQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-inside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCVL</span><span class="topo-unknown">VIRGITG</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>6</td>
      <td>177</td>
      <td>10</td>
      <td>181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>206</td>
      <td>184</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>221</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>225</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>246</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>293</td>
      <td>283</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>311</td>
      <td>298</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ssp">6SSP</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPVD</span><span class="topo-inside">ARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QFVLELEPFSYNNQQLRFSDIQVYT</span><span class="topo-unknown">ENID</span><span class="topo-inside">NEEIDEWWIRGKASTHISDIRYDHL</span><span class="topo-unknown">SSVQ</span><span class="topo-inside">PNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-inside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQAN</span><span class="topo-unknown">GV</span><span class="topo-outside">EDDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCVL</span><span class="topo-inside">VI</span><span class="topo-unknown">RGITG</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>5</td>
      <td>145</td>
      <td>9</td>
      <td>149</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>174</td>
      <td>154</td>
      <td>178</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>206</td>
      <td>183</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>221</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>225</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>246</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>285</td>
      <td>283</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>293</td>
      <td>292</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>311</td>
      <td>298</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>313</td>
      <td>316</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ssp">6SSP</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPVDA</span><span class="topo-inside">RPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-inside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHR</span><span class="topo-unknown">QANGV</span><span class="topo-outside">EDDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCVL</span><span class="topo-inside">VI</span><span class="topo-unknown">RGITG</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>6</td>
      <td>206</td>
      <td>10</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>221</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>225</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>246</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>282</td>
      <td>283</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>293</td>
      <td>292</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>311</td>
      <td>298</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>313</td>
      <td>316</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1074##jbc.M112.424507

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3zkr">3ZKR</a></td>
      <td>3.65</td>
      <td>P2_1</td>
      <td>Full-length ELIC (wild-type) in complex with </td>
      <td> (three binding sites: channel pore, transmembrane intersubunit, extracellular domain)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43
- **Construct**: Signal sequence of human α7 nAChR followed by mature ELIC sequence, pGEM-HE plasmid
- **Notes**: Also expressed in Xenopus oocytes for electrophysiology using the pGEM-HE expression plasmid

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: ELIC cDNA in pGEM-HE or similar vector

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
      <td>Referenced to previously described protocols</td>
      <td>—</td>
      <td></td>
      <td>Expression and purification of ELIC performed as described in the original ELIC structure paper</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Referenced to previously described protocols (Hilf and Dutzler, 2008)</td>
      <td>—</td>
      <td></td>
      <td>Purified ELIC protein concentrated and exchanged into buffer containing  for crystallization</td>
    </tr>
    <tr>
      <td>Electrophysiology</td>
      <td><a href="/xray-mp-wiki/methods/quality-assessment/two-electrode-voltage-clamp/">TEVC</a> in Xenopus oocytes</td>
      <td>—</td>
      <td></td>
      <td>cRNA transcribed from linearized pGEM-HE plasmids. Oocytes injected with 30 nl cRNA (100 ng/nl). Recordings at -60 mV (ELIC) or -80 mV (GlyR) using Axoclamp 900A or HiClamp apparatus. Currents sampled at 100 Hz, low pass-filtered at 10 Hz.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified (likely vapor diffusion)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified ELIC with 1 mM </td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of ELIC- complex. Two data sets collected: crystal 1 at 3.65 A resolution (P2_1, a=105.11, b=266.25, c=110.75 A, beta=109.78 deg) and merged data from three crystals at 5.0 A resolution (a=105.63, b=266.33, c=110.97 A, beta=108.63 deg). Data collected at Swiss Light Source X06A beamline.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3zkr">3ZKR</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVLEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVAY</span><span class="topo-inside">AFYTS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       </span>
<span class="topo-line"><span class="topo-inside">NILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCVL</span><span class="topo-inside">VI</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>200</td>
      <td>11</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>215</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>219</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>235</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>255</td>
      <td>246</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>272</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>287</td>
      <td>283</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>305</td>
      <td>298</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>307</td>
      <td>316</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3zkr">3ZKR</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVLEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVAY</span><span class="topo-inside">AFYTS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       </span>
<span class="topo-line"><span class="topo-inside">NILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCVL</span><span class="topo-inside">VI</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>200</td>
      <td>11</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>215</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>219</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>235</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>255</td>
      <td>246</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>272</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>287</td>
      <td>283</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>305</td>
      <td>298</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>307</td>
      <td>316</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3zkr">3ZKR</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVLEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVAY</span><span class="topo-inside">AFYTS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       </span>
<span class="topo-line"><span class="topo-inside">NILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCVL</span><span class="topo-inside">VI</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>200</td>
      <td>11</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>215</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>219</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>235</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>255</td>
      <td>246</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>272</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>287</td>
      <td>283</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>305</td>
      <td>298</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>307</td>
      <td>316</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3zkr">3ZKR</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVLEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVAY</span><span class="topo-inside">AFYTS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       </span>
<span class="topo-line"><span class="topo-inside">NILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLIQR</span><span class="topo-membrane">CRLAFPLGFLAIGCVL</span><span class="topo-inside">VI</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>200</td>
      <td>11</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>215</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>219</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>235</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>255</td>
      <td>246</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>272</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>289</td>
      <td>283</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>305</td>
      <td>300</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>307</td>
      <td>316</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3zkr">3ZKR</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVLEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVAY</span><span class="topo-inside">AFYTS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       </span>
<span class="topo-line"><span class="topo-inside">NILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLIQR</span><span class="topo-membrane">CRLAFPLGFLAIGCVL</span><span class="topo-inside">VI</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>200</td>
      <td>11</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>215</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>219</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>235</td>
      <td>230</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>255</td>
      <td>246</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>272</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>289</td>
      <td>283</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>305</td>
      <td>300</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>307</td>
      <td>316</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##ncomms1703

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2vl0">2VL0</a></td>
      <td>3.28</td>
      <td>—</td>
      <td>ELIC wild-type</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43
- **Construct**: Signal sequence of human α7 nAChR followed by mature ELIC sequence, pGEM-HE plasmid
- **Notes**: Also expressed in Xenopus oocytes for electrophysiology using the pGEM-HE expression plasmid

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2vl0">2VL0</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">APADNAADAR</span><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDRQQFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320 </span>
<span class="topo-line"><span class="topo-membrane">VVAY</span><span class="topo-inside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLI</span><span class="topo-membrane">QRCRLAFPLGFLAIGCV</span><span class="topo-inside">LVI</span><span class="topo-unknown">RGITL</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>209</td>
      <td>11</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>224</td>
      <td>210</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>228</td>
      <td>225</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>244</td>
      <td>229</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>264</td>
      <td>245</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>281</td>
      <td>265</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>296</td>
      <td>282</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>313</td>
      <td>297</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>316</td>
      <td>314</td>
      <td>316</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>321</td>
      <td>317</td>
      <td>321</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2vl0">2VL0</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">APADNAADAR</span><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDRQQFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320 </span>
<span class="topo-line"><span class="topo-membrane">VVAY</span><span class="topo-inside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLIQR</span><span class="topo-membrane">CRLAFPLGFLAIGCV</span><span class="topo-inside">LVI</span><span class="topo-unknown">RGITL</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>209</td>
      <td>11</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>224</td>
      <td>210</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>228</td>
      <td>225</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>244</td>
      <td>229</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>264</td>
      <td>245</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>281</td>
      <td>265</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>298</td>
      <td>282</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>313</td>
      <td>299</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>316</td>
      <td>314</td>
      <td>316</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>321</td>
      <td>317</td>
      <td>321</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2vl0">2VL0</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">APADNAADAR</span><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDRQQFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320 </span>
<span class="topo-line"><span class="topo-membrane">VVAY</span><span class="topo-inside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLIQR</span><span class="topo-membrane">CRLAFPLGFLAIGCV</span><span class="topo-inside">LVI</span><span class="topo-unknown">RGITL</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>209</td>
      <td>11</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>224</td>
      <td>210</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>228</td>
      <td>225</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>244</td>
      <td>229</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>264</td>
      <td>245</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>281</td>
      <td>265</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>298</td>
      <td>282</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>313</td>
      <td>299</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>316</td>
      <td>314</td>
      <td>316</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>321</td>
      <td>317</td>
      <td>321</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2vl0">2VL0</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">APADNAADAR</span><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDRQQFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320 </span>
<span class="topo-line"><span class="topo-membrane">VVAY</span><span class="topo-inside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLIQR</span><span class="topo-membrane">CRLAFPLGFLAIGCV</span><span class="topo-inside">LVI</span><span class="topo-unknown">RGITL</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>209</td>
      <td>11</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>224</td>
      <td>210</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>228</td>
      <td>225</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>244</td>
      <td>229</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>264</td>
      <td>245</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>281</td>
      <td>265</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>298</td>
      <td>282</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>313</td>
      <td>299</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>316</td>
      <td>314</td>
      <td>316</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>321</td>
      <td>317</td>
      <td>321</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2vl0">2VL0</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">APADNAADAR</span><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDRQQFVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320 </span>
<span class="topo-line"><span class="topo-membrane">VVAY</span><span class="topo-inside">AFYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLIQR</span><span class="topo-membrane">CRLAFPLGFLAIGCV</span><span class="topo-inside">LVI</span><span class="topo-unknown">RGITL</span></span>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>209</td>
      <td>11</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>224</td>
      <td>210</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>228</td>
      <td>225</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>244</td>
      <td>229</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>264</td>
      <td>245</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>281</td>
      <td>265</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>298</td>
      <td>282</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>313</td>
      <td>299</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>316</td>
      <td>314</td>
      <td>316</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>321</td>
      <td>317</td>
      <td>321</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41589-019-0369-4

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hjx">6HJX</a></td>
      <td>2.50</td>
      <td>Not specified</td>
      <td>ELIC 7'C pore mutant (L238C) bound to  72 (Nb72); highest resolution ELIC structure to date</td>
      <td> (PE), <a href="/xray-mp-wiki/reagents/ligands/sodium-ion/">Sodium Ion (Na+)</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hjy">6HJY</a></td>
      <td>2.78</td>
      <td>Not specified</td>
      <td>ELIC Delta8 deletion mutant (M4 C-terminal 8 residues deleted) bound to Nb72</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hk0">6HK0</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>ELIC F16'S mutant with alternative unkinked M4 conformation</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43
- **Construct**: Signal sequence of human α7 nAChR followed by mature ELIC sequence, pGEM-HE plasmid
- **Notes**: Also expressed in Xenopus oocytes for electrophysiology using the pGEM-HE expression plasmid

**Purification:**

- **Expression system**: E. coli C43
- **Expression construct**: MBP-ELIC fusion with 3C protease cleavage site; ELIC cDNA cloned into pET-11a with N-terminal [MBP (Escherichia coli Maltose-Binding Protein)](/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/) fusion tag
- **Tag info**: N-terminal [MBP (Escherichia coli Maltose-Binding Protein)](/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/) fusion tag removed by 3C protease

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
      <td>LB medium</td>
      <td>—</td>
      <td></td>
      <td>C43 E. coli grown to A600 ~1.8, induced with 200 uM  at 20 C overnight</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td></td>
      <td>Membrane fraction collected at 125,000g</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>10 mM Na-phosphate pH 8.0, 150 mM NaCl, 0.15%  + 2% <a href="/xray-mp-wiki/reagents/undecylmaltoside/">UDM</a> ()</td>
      <td>Solubilized at 4 C overnight</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Amylose resin affinity</td>
      <td>Amylose resin (New England Biolabs)</td>
      <td></td>
      <td>Batch purification on amylose resin; column-bound ELIC cleaved by 3C protease in presence of 1 mM  + 1 mM  at 4 C overnight</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>SEC</td>
      <td>Superdex 200 10/300 GL</td>
      <td>10 mM Na-phosphate pH 8.0, 150 mM NaCl, 0.15% </td>
      <td>Final purification step; concentrated protein (10 mg/mL) supplemented with 0.5 mg/mL E. coli lipids</td>
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
      <td>ELIC 7'C mutant + Nb72 complex, 10 mg/mL supplemented with 0.5 mg/mL E. coli lipids</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown using E. coli lipid extract (58% PE, 15% PG, 10% ) as essential crystallization additive. Structure solved at 2.5 A resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hjx">6HJX</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">ARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-inside">ESFS</span><span class="topo-membrane">ERLQTSFTCMLTVVAYA</span><span class="topo-outside">FY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300      </span>
<span class="topo-line"><span class="topo-outside">TSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-inside">AHHRQA</span><span class="topo-unknown">NGV</span><span class="topo-inside">EDDLLIQ</span><span class="topo-membrane">RSRLAFPLGFLAIGSV</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>202</td>
      <td>9</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>217</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>221</td>
      <td>226</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>238</td>
      <td>230</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>257</td>
      <td>247</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>280</td>
      <td>283</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>290</td>
      <td>292</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>306</td>
      <td>299</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hjx">6HJX</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">PVDARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-inside">ESFS</span><span class="topo-membrane">ERLQTSFTCMLTVVAY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300         </span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">FYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-inside">AHHRQANGVEDDLLI</span><span class="topo-membrane">QRSRLAFPLGFLAIGSV</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>205</td>
      <td>6</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>220</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>224</td>
      <td>226</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>241</td>
      <td>230</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>260</td>
      <td>247</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>277</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>292</td>
      <td>283</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>309</td>
      <td>298</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hjx">6HJX</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">PVDARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHL</span><span class="topo-unknown">SSV</span><span class="topo-outside">QPNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-inside">ESFS</span><span class="topo-membrane">ERLQTSFTCMLTVVAY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310  </span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">FYTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-inside">AHHRQA</span><span class="topo-unknown">NGVE</span><span class="topo-inside">DDLLIQRS</span><span class="topo-membrane">RLAFPLGFLAIGSVL</span><span class="topo-outside">VI</span></span>
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
      <td>173</td>
      <td>6</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>205</td>
      <td>182</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>220</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>224</td>
      <td>226</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>241</td>
      <td>230</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>260</td>
      <td>247</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>277</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>283</td>
      <td>283</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>295</td>
      <td>293</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>310</td>
      <td>301</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>312</td>
      <td>316</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hjx">6HJX</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">ARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLS</span><span class="topo-unknown">SVQ</span><span class="topo-outside">PNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-inside">ESFS</span><span class="topo-membrane">ERLQTSFTCMLTVVAYA</span><span class="topo-outside">FY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310</span>
<span class="topo-line"><span class="topo-outside">TSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-inside">AHHRQ</span><span class="topo-unknown">ANGVE</span><span class="topo-inside">DDLLI</span><span class="topo-membrane">QRSRLAFPLGFLAIGSVL</span><span class="topo-outside">VIR</span></span>
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
      <td>171</td>
      <td>9</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>202</td>
      <td>183</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>217</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>221</td>
      <td>226</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>238</td>
      <td>230</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>257</td>
      <td>247</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>279</td>
      <td>283</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>289</td>
      <td>293</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>307</td>
      <td>298</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>310</td>
      <td>316</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hjx">6HJX</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">DARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSS</span><span class="topo-unknown">VQ</span><span class="topo-outside">PNQNEFSRITVRIDAVRNPSYYLWSFIL</span><span class="topo-membrane">PLGLIIAASWSVFWL</span><span class="topo-inside">ESFS</span><span class="topo-membrane">ERLQTSFTCMLTVVAYA</span><span class="topo-outside">F</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       </span>
<span class="topo-line"><span class="topo-outside">YTSNILPRLPYTTVIDQM</span><span class="topo-membrane">IIAGYGSIFAAILLIIF</span><span class="topo-inside">AHHR</span><span class="topo-unknown">QANGVE</span><span class="topo-inside">DDLLIQ</span><span class="topo-membrane">RSRLAFPLGFLAIGSV</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>173</td>
      <td>8</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>203</td>
      <td>183</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>218</td>
      <td>211</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>222</td>
      <td>226</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>239</td>
      <td>230</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>258</td>
      <td>247</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>275</td>
      <td>266</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>279</td>
      <td>283</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>291</td>
      <td>293</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>307</td>
      <td>299</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hjy">6HJY</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">ARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPS</span><span class="topo-membrane">YYLWSFILPLGLIIAASWSVFWL</span><span class="topo-inside">ESFSE</span><span class="topo-membrane">RLQTSFTCMLTVVAYAFY</span></span>
<span class="topo-ruler">       250       260       270       </span>
<span class="topo-line"><span class="topo-membrane">TSN</span><span class="topo-outside">ILPRLPYT</span><span class="topo-membrane">TVIDQMIIAGYGSIFAAILLIIF</span><span class="topo-inside">AHH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>194</td>
      <td>9</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>203</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>226</td>
      <td>230</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>243</td>
      <td>231</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>251</td>
      <td>252</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>260</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>277</td>
      <td>283</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hjy">6HJY</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">P</span><span class="topo-outside">VDARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSY</span><span class="topo-membrane">YLWSFILPLGLIIAASWSVFWL</span><span class="topo-inside">ESFSE</span><span class="topo-membrane">RLQTSFTCMLTVVAY</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-membrane">AFYTSN</span><span class="topo-outside">ILPRLPYT</span><span class="topo-membrane">TVIDQMIIAGYGSIFAAILLIIF</span><span class="topo-inside">AHH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>2</td>
      <td>198</td>
      <td>7</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>220</td>
      <td>204</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>225</td>
      <td>226</td>
      <td>230</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>246</td>
      <td>231</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>254</td>
      <td>252</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>277</td>
      <td>260</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>280</td>
      <td>283</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hjy">6HJY</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">P</span><span class="topo-outside">VDARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FVLELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPS</span><span class="topo-membrane">YYLWSFILPLGLIIAASWSVFWL</span><span class="topo-inside">ESFSE</span><span class="topo-membrane">RLQTSFTCMLTVVAY</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-membrane">AFYTSN</span><span class="topo-outside">ILPRLPYT</span><span class="topo-membrane">TVIDQMIIAGYGSIFAAILLIIF</span><span class="topo-inside">AHH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>2</td>
      <td>197</td>
      <td>7</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>220</td>
      <td>203</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>225</td>
      <td>226</td>
      <td>230</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>246</td>
      <td>231</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>254</td>
      <td>252</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>277</td>
      <td>260</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>280</td>
      <td>283</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hjy">6HJY</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">RPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVLE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPS</span><span class="topo-membrane">YYLWSFILPLGLIIAASWSVFW</span><span class="topo-inside">LESFSE</span><span class="topo-membrane">RLQTSFTCMLTVVAYAFYT</span></span>
<span class="topo-ruler">       250       260       270      </span>
<span class="topo-line"><span class="topo-membrane">SNI</span><span class="topo-outside">LPRLPYT</span><span class="topo-membrane">TVIDQMIIAGYGSIFAAILLIIF</span><span class="topo-inside">AHH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>193</td>
      <td>10</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>215</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>221</td>
      <td>225</td>
      <td>230</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>243</td>
      <td>231</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>250</td>
      <td>253</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>273</td>
      <td>260</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>276</td>
      <td>283</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hjy">6HJY</a> — Chain E (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">DARPVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LELEPFSYNNQQLRFSDIQVYTENIDNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPS</span><span class="topo-membrane">YYLWSFILPLGLIIAASWSVFW</span><span class="topo-inside">LESFSE</span><span class="topo-membrane">RLQTSFTCMLTVVAYAF</span></span>
<span class="topo-ruler">       250       260       270        </span>
<span class="topo-line"><span class="topo-membrane">YTSNI</span><span class="topo-outside">LPRLPYT</span><span class="topo-membrane">TVIDQMIIAGYGSIFAAILLIIF</span><span class="topo-inside">AHH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>195</td>
      <td>8</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>217</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>225</td>
      <td>230</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>245</td>
      <td>231</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>246</td>
      <td>252</td>
      <td>253</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>275</td>
      <td>260</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>278</td>
      <td>283</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hk0">6HK0</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVLEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EPFSYNNQQQRFSDIQVYTENADNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFI</span><span class="topo-membrane">LPLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVAYAF</span><span class="topo-inside">YTS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       </span>
<span class="topo-line"><span class="topo-inside">NILPRLPYTTVIDQ</span><span class="topo-membrane">MIIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLL</span><span class="topo-membrane">IQRCRLAFPLGFLAIGCVL</span><span class="topo-inside">VI</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>199</td>
      <td>11</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>215</td>
      <td>210</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>219</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>237</td>
      <td>230</td>
      <td>247</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>254</td>
      <td>248</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>265</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>286</td>
      <td>283</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>305</td>
      <td>297</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>307</td>
      <td>316</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hk0">6HK0</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVLEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EPFSYNNQQQRFSDIQVYTENADNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFI</span><span class="topo-membrane">LPLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVAYA</span><span class="topo-inside">FYTS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       </span>
<span class="topo-line"><span class="topo-inside">NILPRLPYTTVIDQ</span><span class="topo-membrane">MIIAGYGSIFAAILLIIFA</span><span class="topo-outside">HHRQANGVEDDLLIQR</span><span class="topo-membrane">CRLAFPLGFLAIGCVLV</span><span class="topo-inside">I</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>199</td>
      <td>11</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>215</td>
      <td>210</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>219</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>236</td>
      <td>230</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>254</td>
      <td>247</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>273</td>
      <td>265</td>
      <td>283</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>289</td>
      <td>284</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>306</td>
      <td>300</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>307</td>
      <td>317</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hk0">6HK0</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVLEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EPFSYNNQQQRFSDIQVYTENADNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFI</span><span class="topo-membrane">LPLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVAYA</span><span class="topo-inside">FYTS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       </span>
<span class="topo-line"><span class="topo-inside">NILPRLPYTTVIDQ</span><span class="topo-membrane">MIIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLIQR</span><span class="topo-membrane">CRLAFPLGFLAIGCVLV</span><span class="topo-inside">I</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>199</td>
      <td>11</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>215</td>
      <td>210</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>219</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>236</td>
      <td>230</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>254</td>
      <td>247</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>265</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>289</td>
      <td>283</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>306</td>
      <td>300</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>307</td>
      <td>317</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hk0">6HK0</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVLEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EPFSYNNQQQRFSDIQVYTENADNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFI</span><span class="topo-membrane">LPLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVAYA</span><span class="topo-inside">FYTS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       </span>
<span class="topo-line"><span class="topo-inside">NILPRLPYTTVIDQ</span><span class="topo-membrane">MIIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLIQR</span><span class="topo-membrane">CRLAFPLGFLAIGCVL</span><span class="topo-inside">VI</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>199</td>
      <td>11</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>215</td>
      <td>210</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>219</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>236</td>
      <td>230</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>254</td>
      <td>247</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>265</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>289</td>
      <td>283</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>305</td>
      <td>300</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>307</td>
      <td>316</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hk0">6HK0</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PVDVSVSIFINKIYGVNTLEQTYKVDGYIVAQWTGKPRKTPGDKPLIVENTQIERWINNGLWVPALEFINVVGSPDTGNKRLMLFPDGRVIYNARFLGSFSNDMDFRLFPFDRQQFVLEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EPFSYNNQQQRFSDIQVYTENADNEEIDEWWIRGKASTHISDIRYDHLSSVQPNQNEFSRITVRIDAVRNPSYYLWSFI</span><span class="topo-membrane">LPLGLIIAASWSVFWL</span><span class="topo-outside">ESFS</span><span class="topo-membrane">ERLQTSFTLMLTVVAYA</span><span class="topo-inside">FYTS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       </span>
<span class="topo-line"><span class="topo-inside">NILPRLPYTTVIDQ</span><span class="topo-membrane">MIIAGYGSIFAAILLIIF</span><span class="topo-outside">AHHRQANGVEDDLLIQR</span><span class="topo-membrane">CRLAFPLGFLAIGCVLV</span><span class="topo-inside">I</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>199</td>
      <td>11</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>215</td>
      <td>210</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>219</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>236</td>
      <td>230</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>254</td>
      <td>247</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>265</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>289</td>
      <td>283</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>306</td>
      <td>300</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>307</td>
      <td>317</td>
      <td>317</td>
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

### Nanobodies as allosteric modulators of ELIC

PAM-Nb acts as a positive allosteric modulator with EC50 of 4.2 uM (pEC50 5.37) and Imax of 257%, enhancing GABA-evoked responses. NAM-Nb acts as a negative allosteric modulator with IC50 of 0.13 uM (pIC50 6.89) and inhibition to 34% of control, with inhibition plateauing at ~70% of GABA alone, consistent with NAM mechanism rather than competitive antagonism.

### PAM-Nb and NAM-Nb bind distinct allosteric sites on ELIC

PAM-Nb binds at an intrasubunit site in the ELIC extracellular ligand binding domain, overlapping with the CU2017 small molecule fragment binding site (a NAM in related pLGICs). NAM-Nb binds at the channel vestibule entrance near the N-terminal alpha-helix, adjacent to the flurazepam binding site (a PAM in ELIC). Remarkably, each  has the opposite functional effect of the small molecule at the same site, demonstrating that the same allosteric site can support both positive and negative modulation depending on side chain interactions.

### Omega-loop conformations control vestibule site access

The outer rim of the vestibule site (residues N60-F95 in ELIC) adopts one of three conformations across pLGICs: Ω-in, Ω-out, and Ω-open. ELIC and 5-HT3A receptors adopt the Ω-open conformation, creating an accessible vestibule site. Anionic receptors (GlyR, GABA-AR, ) adopt Ω-out which occludes access. Some nAChR subunits adopt Ω-in which also occludes access. The Ω-open conformation is the only one that leaves the vestibule site accessible for allosteric modulation.

### Vestibule site modulation is conserved between ELIC and human 5-HT3A receptor

Cysteine-scanning mutagenesis (SCAM) of the 5-HT3A receptor vestibule site showed that modification of residues L151C, T112C, and K149C with MTSEA-biotin causes a leftward shift of the concentration-activation curve (PAM effect), confirming functional conservation of the vestibule allosteric site between ELIC and an evolutionarily distant human pLGIC. L151C showed the largest effect (~50-fold EC50 decrease toward wild-type value).

### Phospholipid binding site at M1-M4 interface shapes ELIC function

A high-resolution (2.5 A) structure of ELIC 7'C mutant bound to Nb72 reveals a  (PE) molecule at a site in the lower half of the TMD, located between M1 and M4 helices of one subunit and M3 of the neighboring subunit. The lipid site is shaped by a conserved M4-helix Pro kink (P305) and a Trp-Arg-Pro triad (W224-R301-P305) that is highly conserved in eukaryotic GABA-A/C and  receptors. This site overlaps with known binding sites for neurosteroids in GABA-A receptors and  in the alpha1beta2gamma2 GABA-A receptor, suggesting functional conservation across prokaryote and eukaryote channels.

### M4 helix dynamics and lipid interactions regulate ELIC desensitization

Mutagenesis of the lipid-binding site residues (F274A, I281A, W220A, P305A, W224R) each accelerates desensitization in ELIC. The P305A mutation, which disrupts the M4-helix Pro kink that shapes the lipid-binding site, exhibits a particularly rapid desensitization rate. Reconstitution of ELIC into liposomes with different lipid compositions also alters desensitization kinetics, with PE-containing lipids slowing desensitization. Deletion of up to 7 C-terminal M4 residues has little effect on expression or function, but deletion of 8+ residues or the entire M4 helix (DeltaM4) produces rapid desensitization similar to alpha7 nAChR.

### Alternative unkinked M4 conformation reveals mechanism of lipid regulation

An alternate crystal structure (PDB 6HK0) and MD simulations reveal that M4 can adopt an unkinked conformation, tilting by up to 19.4 A (measured at I317 C-alpha) to interact with M3 of the neighboring subunit. In this conformation, M4 is pinched between W220 and W224 in M1, sterically hindering access to the lipid-binding site. Disulfide crosslinking experiments (L278C/F308C and F274C/I311C) confirm that this alternate conformation is sampled under detergent-solubilized conditions. Voltage clamp fluorometry (VCF) studies show conformational changes in post-M4 residues during channel opening.

### Conservation of kinked M4 fold in anion-selective pLGICs

The architectural feature of a kinked M4 helix with a Pro kink and Trp-Arg triad is conserved in eukaryotic anion-selective pLGICs (GABA-A/C and  receptors) but not in cation-selective pLGICs (nAChR, 5-HT3R). This suggests that the mechanistic insights from ELIC about lipid modulation of channel desensitization extend across the anion-selective subfamily of pLGICs. The phospholipid-binding site closely overlaps with known sites for neurosteroids, , and general anesthetics, offering strategies for designing therapeutics that modulate channel function in human disease.

### Multisite binding of general anesthetics to ELIC

The -bound ELIC structure reveals three distinct anesthetic binding sites, supporting a multisite model of allosteric modulation in pLGICs. Site 1 (channel pore):  binds between 9'L and 16'F near 13'A of the M2-helix, constricting the pore radius (to 1.1-2.5 A vs 1.5-3.3 A in apoELIC). The L9'S mutation eliminates  inhibition, and F16'S significantly reduces it. Site 2 (transmembrane intersubunit): a novel site at the interface between M1/M4 of one subunit and M3 of the neighboring subunit, lined by Trp-221, Trp-225, Phe-275, and Pro-307. This pre-existing cavity is absent in  and . Site 3 (extracellular): a hydrophobic pocket between beta7-beta10 strands involving Leu-128 and Ile-195. Equivalent sites in human  receptors (F295, Y301 in alpha1 GlyR) affect  modulation when mutated. Together with previously identified propofol/desflurane and alcohol/ sites, these findings substantiate multisite allosteric modulation by general anesthetics in the pLGIC family.


## Cross-References

- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/glic/">GLIC (Gloeobacter violaceus Ion Channel)</a> — Homologous prokaryotic pLGIC often studied alongside ELIC
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid)</a> — Used in electrophysiology recording buffers
- <a href="/xray-mp-wiki/reagents/detergents/udm/">n-Undecyl-beta-D-maltoside (UDM)</a> — Detergent used for ELIC purification
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer used in nanobody expression and purification
- <a href="/xray-mp-wiki/reagents/buffers/buffer-mes/">MES (2-(N-Morpholino)ethanesulfonic Acid) Buffer</a> — Buffer used in ELIC-PAM-Nb crystallization
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> — PAM-Nb and NAM-Nb are camelid-derived nanobodies engineered as allosteric modulators
- <a href="/xray-mp-wiki/concepts/signaling-receptors/negative-allosteric-modulation/">Negative Allosteric Modulation</a> — NAM-Nb is a negative allosteric modulator of ELIC
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/positive-allosteric-modulation/">Positive Allosteric Modulation</a> — PAM-Nb is a positive allosteric modulator of ELIC
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/stelic/">sTeLIC (Tevnia jerichonana Endosymbiont pLGIC)</a> — Homologous prokaryotic pLGIC with 28% sequence identity; crystallized in an open/active conformation
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/">Phosphatidylethanolamine (PE)</a> — Phospholipid bound at ELIC M1-M4 interface revealed in 2.5 A crystal structure
