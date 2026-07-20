---
title: "Human Smoothened (SMO) — Extracellular Domain Regulation"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein]
sources: [doi/10.1038##nature18934]
verified: agent
uniprot_id: Q99835
---

# Human Smoothened (SMO) — Extracellular Domain Regulation

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q99835">UniProt: Q99835</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human Smoothened (SMO) is a Class F G-protein-coupled receptor (GPCR) and Hedgehog (Hh) signal transducer that contains two distinct ligand-binding sites: one in its heptahelical transmembrane domain (TMD) and one in its extracellular cysteine-rich domain (CRD). The crystal structure of human SMO (SMOΔC, residues 32-555) was determined at 3.2 Å resolution (PDB 5L7D), revealing the CRD stacked atop the TMD via an intervening wedge-like linker domain. A cholesterol molecule was discovered bound to the CRD binding site, positioned at the interface between the CRD, linker domain, and TMD. Mutations that prevent cholesterol binding (Asp95Ala, Tyr130Phe in human) impair SMO's ability to transmit native Hh signals. Binding of the clinically used antagonist vismodegib to the TMD induces a conformational change propagated to the CRD, resulting in loss of cholesterol from the CRD-linker domain-TMD interface. A second structure with vismodegib bound (SMOΔC-vismodegib) was also determined (PDB 5L7I), showing the allosteric communication between the two binding sites.

## Publications

### doi/10.1038##nature18934

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5l7d">5L7D</a></td>
      <td>3.20</td>
      <td>P212121</td>
      <td>Human SMO residues 32-555 (SMOΔC) with ICL3 (429-440) replaced by BRIL fusion; C-terminal Rho1D4 epitope tag</td>
      <td>Cholesterol (CRD site)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5l7d">5L7D</a></td>
      <td>3.70</td>
      <td>P212121</td>
      <td>Human SMO residues 32-555 (SMOΔC) with ICL3 (429-440) replaced by BRIL fusion; C-terminal Rho1D4 epitope tag</td>
      <td>Vismodegib (TMD site)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK-293S-GnTI- cells (transient transfection)
- **Construct**: Human SMO residues 32-555 with ICL3 replaced by BRIL (residues 23-128); C-terminal Rho1D4 or monoVenus tag; Val329Phe inactivating mutation

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
      <td>1. Membrane solubilization</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> extraction</td>
      <td>—</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> / 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>2 h at 4°C; removal of insoluble material by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> (100,000g, 30 min)</td>
    </tr>
    <tr>
      <td>2. Affinity capture</td>
      <td>20(S)-OHC beads or 1D4 immunoaffinity</td>
      <td>—</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Captured on 20(S)-OHC beads for ligand-binding validation; 1D4 antibody beads for structural samples</td>
    </tr>
    <tr>
      <td>3. LCP reconstitution</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) mixing</td>
      <td>—</td>
      <td>Protein mixed with 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">cholesterol</a> / 90% <a href="/xray-mp-wiki/reagents/lipids/monoolein/">monoolein</a> (60:40 ratio)</td>
      <td>Protein at 30 mg/ml; with or without 10 mM vismodegib</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase (LCP)</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SMOΔC at 30 mg/ml in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">cholesterol</a>, 90% <a href="/xray-mp-wiki/reagents/lipids/monoolein/">monoolein</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Several weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>; data collected at Diamond Light Source beamlines I24 and B21. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using SMO TMD structure (PDB 4O9R) and CRD solution structure</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l7d">5L7D</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SSGNATGPGPRSAGGSARRSAAVTGP</span><span class="topo-outside">PPPLSHCGRAAPCEPLRYNVCLGSVLPYGATSTLLAGDSDSQEEAHGKLVLWSGLRNAPRCWAVIQPLLCAVYMPKCENDRVELPSRTLCQATR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GPCAIVERERGWPDFLRCTPDRFPEGCTNEVQNIKFNSSGQCEVPLVRTDNPKSWYEDVEGCGIQCQNPLFTEAEHQDMHSY</span><span class="topo-membrane">IAAFGAVTGLCTLFTLATFVA</span><span class="topo-inside">DWRNSNRYPAV</span><span class="topo-membrane">ILFYVN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">ACFFVGSIGWLA</span><span class="topo-outside">QFMDGARREIVCRADGTMRLGEPTSNETLSCV</span><span class="topo-membrane">IIFVIVYYALMAGFVWFVVLTY</span><span class="topo-inside">AWHTSFKAL</span><span class="topo-unknown">GTTY</span><span class="topo-inside">QPLSGKTSY</span><span class="topo-membrane">FHLLTWSLPFVLTVAILAV</span><span class="topo-outside">AQVDGDSVSGICF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">VGYKNYRY</span><span class="topo-membrane">RAGFVLAPIGLVLIVGGYFLIR</span><span class="topo-inside">GVMTLFSARRQLADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPP</span><span class="topo-unknown">KLEDKSPD</span><span class="topo-inside">SPEMKDFRHGFDILVGQIDDALKL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">ANEGKVKEAQAAAEQLKTTRNAYIQKYLERARSTLSKINETMLR</span><span class="topo-membrane">LGIFGFLAFGFVLITFSCHFY</span><span class="topo-outside">DFFNQAEWERSFRDYVLCQANVTIGLPTKQPIPDCEIKNRPSLLV</span><span class="topo-membrane">EKINLFAMFG</span></span>
<span class="topo-ruler">       610       620       630        </span>
<span class="topo-line"><span class="topo-membrane">TGIAMSTWVWT</span><span class="topo-inside">KATLLIWRRTWCRLT</span><span class="topo-unknown">GQGTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>26</td>
      <td>32</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>202</td>
      <td>58</td>
      <td>233</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>223</td>
      <td>234</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>234</td>
      <td>255</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>252</td>
      <td>266</td>
      <td>283</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>253</td>
      <td>284</td>
      <td>284</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>306</td>
      <td>316</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>315</td>
      <td>338</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>319</td>
      <td>347</td>
      <td>350</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>320</td>
      <td>328</td>
      <td>351</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>347</td>
      <td>360</td>
      <td>378</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>368</td>
      <td>379</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>390</td>
      <td>400</td>
      <td>421</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>391</td>
      <td>397</td>
      <td>422</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>448</td>
      <td>1011</td>
      <td>1061</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>456</td>
      <td>1062</td>
      <td>1069</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>457</td>
      <td>518</td>
      <td>1070</td>
      <td>1131</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>524</td>
      <td>446</td>
      <td>451</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>545</td>
      <td>452</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>546</td>
      <td>590</td>
      <td>473</td>
      <td>517</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>591</td>
      <td>611</td>
      <td>518</td>
      <td>538</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>612</td>
      <td>626</td>
      <td>539</td>
      <td>553</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>638</td>
      <td>554</td>
      <td>565</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l7i">5L7I</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SSGNATGPGPRSAGGSARRSAAVTG</span><span class="topo-outside">PPPPLSHCGRAAPCEPLRYNVCLGSVLPYGATSTLLAGDSDSQEEAHGKLVLWSGLRNAPRCWAVIQPLLCAVYMPKCENDRVELPSRTLCQATR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GPCAIVERERGWPDFLRCTPDRFPEGCTNEVQNIKFNSSGQCEVPLVRTDNPKSWYEDVEGCGIQCQNPLFTEAEHQDM</span><span class="topo-membrane">HSYIAAFGAVTGLCTLFTLATFVA</span><span class="topo-inside">DWRNSNRYPA</span><span class="topo-membrane">VILFYVN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">ACFFVGSIGWLAQFMD</span><span class="topo-outside">GARREIVCRADGTMRLGEPTSNET</span><span class="topo-membrane">LSCVIIFVIVYYALMAGFVWFVVLTYAW</span><span class="topo-inside">HTSF</span><span class="topo-unknown">KALGTTYQP</span><span class="topo-inside">LSGKT</span><span class="topo-membrane">SYFHLLTWSLPFVLTVAILAVAQVD</span><span class="topo-outside">GDSVSGICF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">VGYKNY</span><span class="topo-membrane">RYRAGFVLAPIGLVLIVGGYFLIRGV</span><span class="topo-inside">MTLFSARRQLADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQK</span><span class="topo-unknown">ATPPKLEDKSPDSPEM</span><span class="topo-inside">KDFRHGFDILVGQIDDALKL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">ANEGKVKEAQAAAEQLKTTRNAYIQKYLERARSTLSKINETMLR</span><span class="topo-membrane">LGIFGFLAFGFVLITFSCHFYDFF</span><span class="topo-outside">NQAEWERSFRDYVLCQANVT</span><span class="topo-unknown">IGLPTKQPIP</span><span class="topo-outside">DCEIKNRPSL</span><span class="topo-membrane">LVEKINLFAMFG</span></span>
<span class="topo-ruler">       610       620       630        </span>
<span class="topo-line"><span class="topo-membrane">TGIAMSTWVWT</span><span class="topo-inside">KATLLIWRRTWCR</span><span class="topo-unknown">LTGQGTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>32</td>
      <td>56</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>199</td>
      <td>57</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>223</td>
      <td>231</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>233</td>
      <td>255</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>256</td>
      <td>265</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>257</td>
      <td>280</td>
      <td>288</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>308</td>
      <td>312</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>309</td>
      <td>312</td>
      <td>340</td>
      <td>343</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>313</td>
      <td>321</td>
      <td>344</td>
      <td>352</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>322</td>
      <td>326</td>
      <td>353</td>
      <td>357</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>351</td>
      <td>358</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>366</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>392</td>
      <td>398</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>397</td>
      <td>424</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>444</td>
      <td>1011</td>
      <td>1057</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>460</td>
      <td>1058</td>
      <td>1073</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>461</td>
      <td>518</td>
      <td>1074</td>
      <td>1131</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>524</td>
      <td>446</td>
      <td>451</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>548</td>
      <td>452</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>549</td>
      <td>568</td>
      <td>476</td>
      <td>495</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>569</td>
      <td>578</td>
      <td>496</td>
      <td>505</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>579</td>
      <td>588</td>
      <td>506</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>589</td>
      <td>611</td>
      <td>516</td>
      <td>538</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>612</td>
      <td>624</td>
      <td>539</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>625</td>
      <td>638</td>
      <td>552</td>
      <td>565</td>
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

### Cholesterol as endogenous SMO ligand

A cholesterol molecule was unexpectedly discovered bound to the CRD of human SMO, occupying a central position at the interface between the CRD, linker domain, and TMD. The cholesterol's tetracyclic sterol ring binds in a shallow groove in the CRD (a site previously shown to bind 20(S)-OHC), while its iso-octyl tail is buried in the SMO protein core some 12 Å from the membrane bilayer. Mutations in the hydrogen-bonding network (Asp99Ala, Tyr134Phe in mouse; corresponding to Asp95, Tyr130 in human) that coordinates the cholesterol 3β-hydroxyl group impair SMO signalling in response to both SHH and 20(S)-OHC, confirming functional relevance.

### Allosteric communication between CRD and TMD binding sites

Vismodegib binding to the TMD site induces a conformational change that is propagated to the CRD via ECL3, resulting in rearrangement of the sterol-binding site and loss of cholesterol from the CRD-linker domain-TMD interface. This provides structural evidence for allosteric communication between the two known ligand-binding sites of SMO and explains how antagonists binding in the TMD can functionally antagonize CRD-mediated activation.

### CRD-linker domain-TMD interface stabilizes inactive state

The interface between the CRD, linker domain, and TMD stabilizes the inactive state of SMO. Mutations that disrupt CRD-linker domain contacts (Pro120Ser in human), alter the CRD surface (Ile160Asn/Glu162Thr), or disrupt a disulfide bond within the linker domain (Cys197Ser/Cys217Ser) all increase constitutive signalling activity of SMO. SAXS experiments show that 20(S)-OHC binding induces a conformational change that increases the maximum particle size from 120 Å to 129 Å, suggesting CRD displacement upon activation.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/smoothened/">Mouse Smoothened (SMO) — Class F GPCR</a> — Active state mouse SMO structure (PDB 6O3C) showing deep 7TM sterol pocket, complementary to the human CRD-bound cholesterol structure
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/deep-7tm-sterol-binding-site/">Deep 7TM Sterol-Binding Site of Smoothened</a> — The 7TM sterol site is a distinct binding pocket deeper in the helical bundle, separate from the CRD cholesterol site described here
