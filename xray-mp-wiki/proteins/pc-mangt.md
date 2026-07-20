---
title: "PcManGT Mannosyltransferase"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2020.06.016]
verified: agent
uniprot_id: A3MTD6
---

# PcManGT Mannosyltransferase

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A3MTD6">UniProt: A3MTD6</a>

<span class="expr-badge">Pyrobaculum calidifontis (strain JCM 11548 / VA1)</span>

## Overview

PcManGT is a crenarchaeal membrane glycosyltransferase from Pyrobaculum calidifontis involved in N-glycan biosynthesis. It belongs to the GT2 family of inverting glycosyltransferases and is the first glycosyltransferase of TACK superphylum origin to be characterized structurally and biochemically. PcManGT is a GDP-, dolichylphosphate-, and manganese-dependent mannosyltransferase. Its membrane domain includes three transmembrane helices (TMH1-TMH3) that topologically coincide with half of the six-transmembrane helix cellulose-binding tunnel in Rhodobacter spheroides cellulose synthase [BCSA](/xray-mp-wiki/proteins/enzymes/bcsa/). The enzyme is specifically stabilized by anionic dolichylphosphates and phospholipids, and shows a remarkable increase in catalytic activity when incorporated into bicelle membranes in the presence of Dol55-P. The crystal structures were determined in the unliganded state (2.6 A), in complex with GDP·Mn2+ (2.7 A), and with GDP-alpha-Man·Mn2+ (2.7 A).


## Publications

### doi/10.1016##j.jmb.2020.06.016

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6yv7">6YV7</a></td>
      <td>2.6</td>
      <td>P212121</td>
      <td>Full-length PcManGT (UniProt A3MTD6, residues 1-351) from Pyrobaculum calidifontis, TEV-cleaved from GFP-His8 tag</td>
      <td>Unliganded (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6yv8">6YV8</a></td>
      <td>2.7</td>
      <td>P212121</td>
      <td>Full-length PcManGT, TEV-cleaved from GFP-His8 tag, soaked with GDP and MnCl2</td>
      <td>GDP, Mn2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6yv9">6YV9</a></td>
      <td>2.7</td>
      <td>P212121</td>
      <td>Full-length PcManGT, TEV-cleaved from GFP-His8 tag, soaked with GDP-alpha-Man and MnCl2</td>
      <td>GDP-alpha-Mannose, Mn2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: PcManGT-TEV-GFP-His8 (codon-optimized Pcal_0472 gene) in pWaldo-GFPd vector, expressed in E. coli BL21(DE3)

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
      <td><a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> induction</td>
      <td>--</td>
      <td>Terrific Broth + --</td>
      <td>Expression induced with 0.2 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> at OD600=1.0, 15-17 h at 18 C</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Homogenization</td>
      <td>--</td>
      <td>PBS with protease inhibitor cocktail + --</td>
      <td>Cells lysed using Avestin EmulsiFlex C3 homogenizer, followed by sonication</td>
    </tr>
    <tr>
      <td>Membrane collection</td>
      <td>Centrifugation</td>
      <td>--</td>
      <td>25 mM K2HPO4 (pH 7.2), 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + --</td>
      <td>Low-speed spin at 10,000 rpm, then membrane pellet at 35,000 rpm (125,749 g)</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>25 mM K2HPO4 (pH 7.2), 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1.5% <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a> (or <a href="/xray-mp-wiki/reagents/detergents/lapao/">LAPAO</a>, <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>)</td>
      <td>Membranes resuspended and solubilized in detergent</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>25 mM K2HPO4 (pH 7.2), 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient (30-500 mM) + 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a> (or 0.3% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, 0.08% <a href="/xray-mp-wiki/reagents/detergents/lapao/">LAPAO</a>)</td>
      <td>Wash with 30 mM and 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elution with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>TEV cleavage</td>
      <td>Enzymatic cleavage</td>
      <td>--</td>
      <td>25 mM K2HPO4 (pH 7.2), 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease at 1:10 molar ratio, overnight at 4 C. Cleaved PcManGT recovered as flow-through from reverse IMAC.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 16/60</td>
      <td>50 mM HEPES (pH 7.5), 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (or 0.05% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, 0.07% <a href="/xray-mp-wiki/reagents/detergents/lapao/">LAPAO</a>)</td>
      <td>Final buffer: 50 mM HEPES pH 7.5, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle Crystallization</a> (in meso)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified PcManGT at 5.5 mg/ml in 50 mM HEPES (pH 7.5), 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1% DM, mixed with 8% bicelles (<a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a>:<a href="/xray-mp-wiki/reagents/detergents/chapso/">CHAPSO</a>, 2.8:1)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 mM HEPES (pH 7.5), 20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000, 10% isopropanol, 10 mM MnCl2, 2% 1,2,3-heptanetriol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew in space group P212121 with two molecules per asymmetric unit and ~50% solvent content. Experimental phases determined by SIRAS using Na2WO4 derivative. Data collected at Diamond Light Source (I24, I02), SOLEIL (PROXIMA1), ESRF (ID23-1), and Swiss Light Source (PXI X06SA).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yv7">6YV7</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MLL</span><span class="topo-membrane">EAIAIALTAAHFGAPLLYYWR</span><span class="topo-inside">AKRWLKKPWDVAPDPTYRPRVTVIVPTYNEAPLIEEKLDNIYEQDYPRDKLEVVVVDSASTDGTPSAVRRWAETHPDLALTLVEETERRGKAHALN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TALRHATGEIVVITDADALWPARDTLANAVKWLADPTVGAVSCVKRP</span><span class="topo-unknown">AGPAGVEDSY</span><span class="topo-inside">RDFYNVLRVAESKAWATPIFHGELAAFKRELLERLGGFPTDVGADDSHTATKIAMMGYRAITP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350      </span>
<span class="topo-line"><span class="topo-inside">PDVVCVEAVPKRGYHAWRIRRAQHLVQHFAKAIRDGKAPPPFKPILHAEA</span><span class="topo-membrane">YLHLANPWALPTAAAALAAAAA</span><span class="topo-outside">AGSLP</span><span class="topo-membrane">AAALLATGAALALYKPYR</span><span class="topo-unknown">T</span><span class="topo-inside">WTTMQAYLIAAAVKNLWDK</span><span class="topo-unknown">E</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>24</td>
      <td>4</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>167</td>
      <td>25</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>177</td>
      <td>168</td>
      <td>177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>178</td>
      <td>290</td>
      <td>178</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>312</td>
      <td>291</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>317</td>
      <td>313</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>335</td>
      <td>318</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>355</td>
      <td>337</td>
      <td>355</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yv8">6YV8</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">ML</span><span class="topo-membrane">LEAIAIALTAAHFGAPLL</span><span class="topo-inside">YYWRAKRWLKKPWDVAPDPTYRPRVTVIVPTYNEAPLIEEKLDNIYEQDYPRDKLEVVVVDSASTDGTPSAVRRWAETHPDLALTLVEETERRGKAHALN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TALRHATGEIVVITDADALWPARDTLANAVKWLADPTVGAVSCVKRP</span><span class="topo-unknown">AGPAGVEDSY</span><span class="topo-inside">RDFYNVLRVAESKAWATPIFHGELAAFKRELLERLGGFPTDVGADDSHTATKIAMMGYRAITP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350      </span>
<span class="topo-line"><span class="topo-inside">PDVVCVEAVPKRGYHAWRIRRAQHLVQHFAKAIRDGKAPPPFKPILHAEAYLHL</span><span class="topo-membrane">ANPWALPTAAAALAAAAA</span><span class="topo-outside">AGSL</span><span class="topo-membrane">PAAALLATGAALALYKPYR</span><span class="topo-unknown">T</span><span class="topo-inside">WTTMQAYLIAAAVKNLWDK</span><span class="topo-unknown">E</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>20</td>
      <td>3</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>167</td>
      <td>21</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>177</td>
      <td>168</td>
      <td>177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>178</td>
      <td>294</td>
      <td>178</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>312</td>
      <td>295</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>316</td>
      <td>313</td>
      <td>316</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>335</td>
      <td>317</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>355</td>
      <td>337</td>
      <td>355</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yv9">6YV9</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ML</span><span class="topo-membrane">LEAIAIALTAAHFGAPLLYYW</span><span class="topo-outside">RAKRWLKKPWDVAPDPTYRPRVTVIVPTYNEAPLIEEKLDNIYEQDYPRDKLEVVVVDSASTDGTPSAVRRWAETHPDLALTLVEETERRGKAHALN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TALRHATGEIVVITDADALWPARDTLANAVKWLADPTVGAVSCVKRP</span><span class="topo-unknown">AGPAGVEDSY</span><span class="topo-outside">RDFYNVLRVAESKAWATPIFHGELAAFKRELLERLGGFPTDVGADDSHTATKIAMMGYRAITP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350      </span>
<span class="topo-line"><span class="topo-outside">PDVVCVEAVPKRGYHAWRIRRAQHLVQHFAKAIRDGKAPPPFKPILHAEAY</span><span class="topo-membrane">LHLANPWALPTAAAALAAAAA</span><span class="topo-inside">AGSL</span><span class="topo-membrane">PAAALLATGAALALYKPYR</span><span class="topo-unknown">T</span><span class="topo-outside">WTTMQAYLIAAAVKNLWDK</span><span class="topo-unknown">E</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>23</td>
      <td>3</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>167</td>
      <td>24</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>177</td>
      <td>168</td>
      <td>177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>178</td>
      <td>291</td>
      <td>178</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>312</td>
      <td>292</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>316</td>
      <td>313</td>
      <td>316</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>335</td>
      <td>317</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>355</td>
      <td>337</td>
      <td>355</td>
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

### First crystal structure of a crenarchaeal membrane glycosyltransferase

PcManGT is the first glycosyltransferase from the TACK superphylum of archaea to be structurally characterized. The overall fold features a catalytic GT-A extramembrane domain connected to two membrane-interface helices (IFH1, IFH2) and a transmembrane domain of three antiparallel TM helices. TMH3 is kinked 90 degrees midway across the membrane, forming a substratum interface helix (sub-IFH3). The three-TMH domain represents half of the six-helix cellulose-binding tunnel in [BCSA](/xray-mp-wiki/proteins/enzymes/bcsa/).

### Dolichylphosphate-dependent stabilization and activity

PcManGT is specifically stabilized by anionic dolichylphosphates (Dol55-P and Dol95-P) with DeltaTm values of 30 C and 22 C, respectively. Anionic phospholipids (PS, PG) also provide substantial stabilization. The dolichylphosphate-dependent behavior parallels that of PfDPMS. When incorporated into bicelles with Dol55-P, PcManGT shows five-fold increased donor hydrolysis activity, indicating that the natural acceptor is a Dol-PP-linked sugar intermediate of the N-glycan biosynthesis pathway.

### Donor specificity and catalytic mechanism

PcManGT uses GDP-alpha-Man as the natural donor substrate, with Mn2+ as the preferred divalent metal cofactor. [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) binding studies show Kd values in the low micromolar range for GDP and GDP-alpha-Man. The DXD motif (Asp135-Asp137) coordinates the diphosphate group via Mn2+. Despite classification as a GT2 inverting glycosyltransferase, PcManGT catalyzes hydrolytic side-reaction in the absence of acceptor, a feature associated with retaining mechanism.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Primary solubilization and purification detergent
- <a href="/xray-mp-wiki/reagents/detergents/lapao/">LAPAO</a> — Alternative detergent for solubilization and crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> — Alternative detergent for solubilization
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — 50 mM HEPES (pH 7.5) in SEC buffer and crystallization
- <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle Crystallization</a> — Crystallization performed in bicelles (in meso method)
- <a href="/xray-mp-wiki/methods/purification/ninta-affinity-chromatography/">Ni-NTA Affinity Chromatography</a> — His8-tag purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography (SEC)</a> — Final polishing step using Superdex 200
- <a href="/xray-mp-wiki/concepts/protein-glycosylation/">Protein N-Glycosylation</a> — PcManGT involved in N-glycan biosynthesis in Pyrobaculum calidifontis
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/">ITC</a> — Method used in structure determination or purification
