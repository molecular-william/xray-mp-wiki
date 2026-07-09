---
title: "Mouse Smoothened (SMO) — Class F GPCR"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein]
sources: [doi/10.1038##s41586-019-1355-4]
verified: regex
uniprot_id: P56726
---

# Mouse Smoothened (SMO) — Class F GPCR

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P56726">UniProt: P56726</a>

<span class="expr-badge">Mus musculus</span>

## Overview

Smoothened (SMO) is a seven-transmembrane (7TM) oncoprotein and member of the class F G protein-coupled receptor (GPCR) superfamily that serves as the central signal transducer in the Hedgehog (Hh) signalling pathway. Hh proteins bind to and inhibit the transmembrane cholesterol transporter Patched-1 (PTCH1), which permits activation of SMO. The crystal structure of active mouse SMO (mSMO) bound to the agonist SAG21k and a conformation-specific nanobody (NbSmo8) was determined at 2.8 Å resolution (PDB 6O3C), revealing a cholesterol molecule bound deep within the 7TM pocket that is critical for SMO activation. Activation involves outward displacement of TM6 (8 Å), inward movement of TM5 (6 Å), and upward displacement of TM6 and ECL3. The structure identified a hydrophobic tunnel between TM5 and TM6 connecting the inner membrane leaflet to the 7TM sterol site, providing a direct link between the cholesterol transporter-like activity of PTCH1 and SMO regulation.

## Publications

### doi/10.1038##s41586-019-1355-4

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6o3c">6O3C</a></td>
      <td>2.80</td>
      <td>P2221</td>
      <td>Mouse SMO residues 64-566 with N-terminal HA signal sequence, Flag tag, streptavidin binding peptide, TEV site, and C-terminal Gαo fusion; complexed with SAG21k agonist and NbSmo8 nanobody</td>
      <td>SAG21k, cholesterol (7TM site), cholesterol (CRD site)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnTI- cells (BacMam expression system) with 10 mM sodium butyrate; also in Sf9 insect cells for nanobody generation
- **Construct**: Wild-type mouse Smo gene residues 64-566, N-terminal HA/Flag/SBP/TEV tag, C-terminal sortase-3C-Gαo fusion

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
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> extraction</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 300 mM NaCl, 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 5 mM MgCl2, 20 mM KCl, 5 mM ATP, 1 µM vismodegib</td>
      <td>Solubilization from frozen cell pellets for 1 h at 4°C</td>
    </tr>
    <tr>
      <td>2. Affinity purification</td>
      <td>M1 anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> antibody Sepharose</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 300 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Detergent exchange to 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, ligand exchange from vismodegib to SAG21k on-column</td>
    </tr>
    <tr>
      <td>3. Elution and deglycosylation</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> peptide elution + endoglycosidase treatment</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 150 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 1 pM SAG21k</td>
      <td>Deglycosylated with endoglycosidase F1 and H for 30 min at RT</td>
    </tr>
    <tr>
      <td>4. Nanobody complex formation</td>
      <td>3-fold molar excess NbSmo8 incubation</td>
      <td>—</td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Overnight incubation at 4°C</td>
    </tr>
    <tr>
      <td>5. Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>—</td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl, 0.1 pM SAG21k, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Peak fractions concentrated to 50 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: SMO-SAG21k-NbSmo8 complex at 50 mg/ml

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SMO-SAG21k-NbSmo8 complex at 50 mg/ml in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4°C for 10 days, then 20°C for 10 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> formed with 90% 9.9 MAG (monoolein) / 10% cholesterol. Data merged from 20 crystals. Structure solved by molecular replacement using hSMO (5L7D) and Nb6B9 (4LDE). Final Rwork/Rfree 24.5%/29.4%. Data collected at APS beamlines 23-ID-B and 23-ID-D.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o3c">6O3C</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDAGSENLYFQGSGSPRL</span><span class="topo-outside">LSHCGRAAHCEPLRYNVCLGSALPYGATTTLLAGDSDSQEEAHGKLVLWSGLRNAPRCWAVIQPLLCAVYMPKCENDRVELPSRTLCQATRGPCAIV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ERERGWPDFLRCTPDHFPEGCPNEVQNIKFNSSGQCEAPLVRTDNPKSWYEDVEGCGIQCQNPLFTEAEHQDMH</span><span class="topo-membrane">SYIAAFGAVTGLCTLFTLATFV</span><span class="topo-inside">ADWRNSNRYPAVI</span><span class="topo-membrane">LFYVNACFFVG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SIGWLA</span><span class="topo-outside">QFMDG</span><span class="topo-unknown">ARREIV</span><span class="topo-outside">CRADGTMRFGEPTSSETLSCVI</span><span class="topo-membrane">IFVIVYYALMAGVVWFVVL</span><span class="topo-inside">TYAWHTSFKALGTTYQPLSGKTS</span><span class="topo-membrane">YFHLLTWSLPFVLTVAI</span><span class="topo-outside">LAVAQVDGDSVSGICFVGYKNY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">RY</span><span class="topo-membrane">RAGFVLAPIGLVLIVGGY</span><span class="topo-inside">FLIRGVMTLFSIKSNHPGLLSEKAASKINETMLRLGI</span><span class="topo-membrane">FGFLAFGFVLITFSCHFY</span><span class="topo-outside">DFFNQAEWERSFRDYVLCQANVTIG</span><span class="topo-unknown">LPTKKPIP</span><span class="topo-outside">DCEIKNRPSLL</span><span class="topo-membrane">V</span></span>
<span class="topo-ruler">       490       500       510       520     </span>
<span class="topo-line"><span class="topo-membrane">EKINLFAMFGTGIAMST</span><span class="topo-inside">WVWT</span><span class="topo-unknown">KATLLIWRRTWC</span><span class="topo-inside">RL</span><span class="topo-unknown">TGHSDDEPKR</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>24</td>
      <td>194</td>
      <td>65</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>216</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>229</td>
      <td>258</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>246</td>
      <td>271</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>251</td>
      <td>288</td>
      <td>292</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>257</td>
      <td>293</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>299</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>298</td>
      <td>321</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>321</td>
      <td>340</td>
      <td>362</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>338</td>
      <td>363</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>362</td>
      <td>380</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>380</td>
      <td>404</td>
      <td>421</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>381</td>
      <td>417</td>
      <td>422</td>
      <td>458</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>418</td>
      <td>435</td>
      <td>459</td>
      <td>476</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>436</td>
      <td>460</td>
      <td>477</td>
      <td>501</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>479</td>
      <td>510</td>
      <td>520</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>497</td>
      <td>521</td>
      <td>538</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>498</td>
      <td>501</td>
      <td>539</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>502</td>
      <td>513</td>
      <td>543</td>
      <td>554</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>514</td>
      <td>515</td>
      <td>555</td>
      <td>556</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o3c">6O3C</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">QVQLQESGGGLVQAGGSLRLSCAASGYIFSSYAMGWYRQAPGKEREFVATIGWGTITYYADSVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCAAQDLLYYSFPGDHAYWGQGTQVTV</span></span>
<span class="topo-ruler">        </span>
<span class="topo-line"><span class="topo-inside">SS</span><span class="topo-unknown">HHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>122</td>
      <td>1</td>
      <td>122</td>
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

### 7TM sterol binding site is critical for SMO activation

A cholesterol molecule was identified deep within the 7TM core of active SMO. The 7TM-bound cholesterol stabilizes the outward displacement of TM6, analogous to agonist action in other GPCRs. Mutations lining the 7TM site (V333F, V408F, I412F, T470Q) ablated GLI activation by SAG21k and Sonic hedgehog. Cholesterol delivered via methyl-β-cyclodextrin activated GLI, and this was fully lost in V333F and T470Q mutants. In cholesterol-laden micelles, NbSmo8 bound wild-type SMO but not V333F SMO.

### Hydrophobic tunnel for sterol access

A hydrophobic tunnel between TM5 and TM6 opens to the inner leaflet of the membrane bilayer, providing a conduit for sterols to reach the deep 7TM site without desolvation from the membrane. Mutations occluding the tunnel entrance (A463F) rendered SMO unresponsive to ShhNp stimulation. The structurally observed tunnel is almost identical to one recently observed in Xenopus SMO.

### CRD sterol binding and allosteric communication

Active SMO binds a second sterol within the conserved CRD lipid-binding site. A resolved N-acetyl glucosamine on N497 forms part of the CRD sterol pocket and relays sterol binding to ECL3. The entire ECL3-TM6 helix is displaced 3 Å upward compared to inactive SMO, illustrating allosteric communication between three distinct binding sites: the deep 7TM sterol pocket, the SAG21k/cyclopamine site, and the CRD sterol pocket.

### NbSmo8 nanobody enables active state capture

A conformation-specific nanobody (NbSmo8) was developed using yeast surface display, selectively binding agonist-occupied SMO but not apo or antagonist-occupied SMO. NbSmo8 recognized a unique 3D epitope with CDR3 reaching deep inside the active SMO cavity to stabilize the outwardly displaced TM6 conformation. In cellular imaging, NbSmo8-GFP plasma membrane recruitment faithfully reflected SMO activation state.

### Relationship to SMO inhibitor resistance

Several clinically observed SMO resistance mutations map to the 7TM sterol pocket. SANT-1 extensively overlaps with 7TM cholesterol binding, and antagonists that are isosteric with 7TM cholesterol may be less susceptible to resistance mutations, since mutations blocking antagonist binding would also prevent sterol binding and SMO activation.


## Cross-References
