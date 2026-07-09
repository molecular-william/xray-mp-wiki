---
title: "Acid-Sensing Ion Channel 1a"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature06163, doi/10.1016##j.cell.2014.01.011, doi/10.1038##nature11375, doi/10.1038##ncomms1917, doi/10.1038##nature25782]
verified: regex
uniprot_id: ['G9I929', 'G9I930', 'P60514', 'Q1XA76']
---

# Acid-Sensing Ion Channel 1a

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span> <span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/G9I929">UniProt: G9I929</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/G9I930">UniProt: G9I930</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P60514">UniProt: P60514</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1XA76">UniProt: Q1XA76</a>

<span class="expr-badge">Gallus gallus</span>

## Overview

Acid-sensing ion channel 1a (ASIC1a) is a proton-gated, sodium-selective ion channel from the degenerin/epithelial sodium channel (Deg/ENaC) superfamily. Expressed in vertebrate central and peripheral nervous systems, ASIC1a detects extracellular protons produced during inflammation or ischemic injury and initiates pain signals. The first high-resolution structure of the open state was solved by [Selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/) [SAD Phasing](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) at 1.9 A resolution (Kawate & Gouaux, Nature 2009). A later structure captured the open state in complex with the snake toxin [MitTx](/xray-mp-wiki/reagents/ligands/mittx/) (Cell 2014). The first structure of a gating modifier toxin bound to an ion channel was solved for the PcTx1-ASIC1 complex at 3.0 A resolution (Dawson et al., Nat Commun 2012).


## Publications

### doi/10.1038##nature06163

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3hv4">3HV4</a></td>
      <td>1.9 A</td>
      <td>P21</td>
      <td>Chicken delta ASIC1 (residues 147-526)</td>
      <td>Na+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293T cells (electrophysiology), E. coli (crystallography)
- **Construct**: Chicken ASIC1a (full-length for electrophysiology), Chicken delta ASIC1 (residues 147-526, truncated extracellular N-terminus for crystallography), Chicken ASIC1 (residues 26-463, for PcTx1 complex)

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
      <td>FSEC screening</td>
      <td>Fluorescence <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superose-6/">Superose 6</a> 10/300</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>N- and C-terminally EGFP-tagged chicken ASIC1 and delta ASIC1 constructs screened by FSEC. Solubilized in PBS with 20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> and protease inhibitors for 1 h. Monodisperse peak identified for delta ASIC1-EGFP fusion.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a> purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superose-6/">Superose 6</a> 10/300</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Monodisperse fractions of delta ASIC1 collected for crystallization. Molecular mass determined by light scattering: 165.9 +/- 1.4 kDa, consistent with a trimer.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Chicken delta ASIC1 (residues 147-526) at ~10 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in supplementary information</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Open state structure solved at 1.9 A resolution, space group P21. <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine</a> <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">SAD Phasing</a> used. Crystals also derivatized with platinum and bromine for additional phasing. Resolution: 50-1.9 A (outer shell 1.97-1.90 A). R_merge 6.6% (42.1% in outer shell). Completeness 93.6% (69.3% outer shell).</td>
    </tr>
  </tbody>
</table>
### doi/10.1016##j.cell.2014.01.011

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ntw">4NTW</a></td>
      <td>2.1 A</td>
      <td>R3</td>
      <td>Chicken delta13 ASIC1a</td>
      <td>Na+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ntx">4NTX</a></td>
      <td>2.3 A</td>
      <td>R3</td>
      <td>Chicken delta13 ASIC1a</td>
      <td>amiloride</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4nty">4NTY</a></td>
      <td>2.6 A</td>
      <td>R3</td>
      <td>Chicken delta13 ASIC1a</td>
      <td>Cs+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293T cells (electrophysiology), E. coli (crystallography)
- **Construct**: Chicken ASIC1a (full-length for electrophysiology), Chicken delta ASIC1 (residues 147-526, truncated extracellular N-terminus for crystallography), Chicken ASIC1 (residues 26-463, for PcTx1 complex)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntw">4NTW</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQPVSIQAFASSSTLHGISHIFSYERLSLKR</span><span class="topo-outside">VVWALC</span><span class="topo-membrane">FMGSLALLALVCTNRIQYYFLYP</span><span class="topo-inside">HVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">KQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTG</span><span class="topo-unknown">DS</span><span class="topo-inside">EFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGK</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450</span>
<span class="topo-line"><span class="topo-inside">ELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKA</span><span class="topo-membrane">YEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYA</span><span class="topo-unknown">YEVIKHR</span></span>
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
      <td>31</td>
      <td>14</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>37</td>
      <td>45</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>60</td>
      <td>51</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>283</td>
      <td>74</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>297</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>286</td>
      <td>411</td>
      <td>299</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>431</td>
      <td>425</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>443</td>
      <td>445</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>450</td>
      <td>457</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntw">4NTW</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-inside">EIRPAFCYEDPPFFQKCGAFVDSYYFNRSRITCVHFFYGQCDVNQNHFTTMSECNRVCHG</span></span>
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
      <td>60</td>
      <td>1</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntw">4NTW</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110         </span>
<span class="topo-line"><span class="topo-inside">NLNQFRLMIKCTNDRVWADFVDYGCYCVARDSNTPVDDLDRCCQAQKQCYDEAVKVHGCKPLVMFYSFECRYLASDLDCSGNNTKCRNFVCNCDRTATLCILTATYNRNNHKIDPSRC</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>118</td>
      <td>1</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntw">4NTW</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQPVSIQAFASSSTLHGISHIFSYERLSLKR</span><span class="topo-outside">VVWALC</span><span class="topo-membrane">FMGSLALLALVCTNRIQYYFLYP</span><span class="topo-inside">HVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">KQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTG</span><span class="topo-unknown">DS</span><span class="topo-inside">EFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGK</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450</span>
<span class="topo-line"><span class="topo-inside">ELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKA</span><span class="topo-membrane">YEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYA</span><span class="topo-unknown">YEVIKHR</span></span>
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
      <td>31</td>
      <td>14</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>37</td>
      <td>45</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>60</td>
      <td>51</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>283</td>
      <td>74</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>297</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>286</td>
      <td>411</td>
      <td>299</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>431</td>
      <td>425</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>443</td>
      <td>445</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>450</td>
      <td>457</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntw">4NTW</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-inside">EIRPAFCYEDPPFFQKCGAFVDSYYFNRSRITCVHFFYGQCDVNQNHFTTMSECNRVCHG</span></span>
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
      <td>60</td>
      <td>1</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntw">4NTW</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110         </span>
<span class="topo-line"><span class="topo-inside">NLNQFRLMIKCTNDRVWADFVDYGCYCVARDSNTPVDDLDRCCQAQKQCYDEAVKVHGCKPLVMFYSFECRYLASDLDCSGNNTKCRNFVCNCDRTATLCILTATYNRNNHKIDPSRC</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>118</td>
      <td>1</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntw">4NTW</a> — Chain G (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQPVSIQAFASSSTLHGISHIFSYERLSLKR</span><span class="topo-outside">VVWALC</span><span class="topo-membrane">FMGSLALLALVCTNRIQYYFLYP</span><span class="topo-inside">HVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">KQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTG</span><span class="topo-unknown">DS</span><span class="topo-inside">EFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGK</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450</span>
<span class="topo-line"><span class="topo-inside">ELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKA</span><span class="topo-membrane">YEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYA</span><span class="topo-unknown">YEVIKHR</span></span>
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
      <td>31</td>
      <td>14</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>37</td>
      <td>45</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>60</td>
      <td>51</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>283</td>
      <td>74</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>297</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>286</td>
      <td>411</td>
      <td>299</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>431</td>
      <td>425</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>443</td>
      <td>445</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>450</td>
      <td>457</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntw">4NTW</a> — Chain H (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-inside">EIRPAFCYEDPPFFQKCGAFVDSYYFNRSRITCVHFFYGQCDVNQNHFTTMSECNRVCHG</span></span>
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
      <td>60</td>
      <td>1</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntw">4NTW</a> — Chain I (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110         </span>
<span class="topo-line"><span class="topo-inside">NLNQFRLMIKCTNDRVWADFVDYGCYCVARDSNTPVDDLDRCCQAQKQCYDEAVKVHGCKPLVMFYSFECRYLASDLDCSGNNTKCRNFVCNCDRTATLCILTATYNRNNHKIDPSRC</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>118</td>
      <td>1</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntx">4NTX</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQPVSIQAFASSSTLHGISHIFSYERLSLKR</span><span class="topo-outside">VVWAL</span><span class="topo-membrane">CFMGSLALLALVCTNRIQYYFLYP</span><span class="topo-inside">HVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">KQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTG</span><span class="topo-unknown">DS</span><span class="topo-inside">EFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGK</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450</span>
<span class="topo-line"><span class="topo-inside">ELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKA</span><span class="topo-membrane">YEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYA</span><span class="topo-unknown">YEVIKHR</span></span>
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
      <td>31</td>
      <td>14</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>45</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>60</td>
      <td>50</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>283</td>
      <td>74</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>297</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>286</td>
      <td>411</td>
      <td>299</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>431</td>
      <td>425</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>443</td>
      <td>445</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>450</td>
      <td>457</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntx">4NTX</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-inside">EIRPAFCYEDPPFFQKCGAFVDSYYFNRSRITCVHFFYGQCDVNQNHFTTMSECNRVCHG</span></span>
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
      <td>60</td>
      <td>1</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntx">4NTX</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110         </span>
<span class="topo-line"><span class="topo-inside">NLNQFRLMIKCTNDRVWADFVDYGCYCVARDSNTPVDDLDRCCQAQKQCYDEAVKVHGCKPLVMFYSFECRYLASDLDCSGNNTKCRNFVCNCDRTATLCILTATYNRNNHKIDPSRC</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>118</td>
      <td>1</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntx">4NTX</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQPVSIQAFASSSTLHGISHIFSYERLSLKR</span><span class="topo-outside">VVWAL</span><span class="topo-membrane">CFMGSLALLALVCTNRIQYYFLYP</span><span class="topo-inside">HVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">KQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTG</span><span class="topo-unknown">DS</span><span class="topo-inside">EFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGK</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450</span>
<span class="topo-line"><span class="topo-inside">ELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKA</span><span class="topo-membrane">YEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYA</span><span class="topo-unknown">YEVIKHR</span></span>
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
      <td>31</td>
      <td>14</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>45</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>60</td>
      <td>50</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>283</td>
      <td>74</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>297</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>286</td>
      <td>411</td>
      <td>299</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>431</td>
      <td>425</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>443</td>
      <td>445</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>450</td>
      <td>457</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntx">4NTX</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-inside">EIRPAFCYEDPPFFQKCGAFVDSYYFNRSRITCVHFFYGQCDVNQNHFTTMSECNRVCHG</span></span>
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
      <td>60</td>
      <td>1</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntx">4NTX</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110         </span>
<span class="topo-line"><span class="topo-inside">NLNQFRLMIKCTNDRVWADFVDYGCYCVARDSNTPVDDLDRCCQAQKQCYDEAVKVHGCKPLVMFYSFECRYLASDLDCSGNNTKCRNFVCNCDRTATLCILTATYNRNNHKIDPSRC</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>118</td>
      <td>1</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntx">4NTX</a> — Chain G (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQPVSIQAFASSSTLHGISHIFSYERLSLKR</span><span class="topo-outside">VVWAL</span><span class="topo-membrane">CFMGSLALLALVCTNRIQYYFLYP</span><span class="topo-inside">HVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">KQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTG</span><span class="topo-unknown">DS</span><span class="topo-inside">EFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGK</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450</span>
<span class="topo-line"><span class="topo-inside">ELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKA</span><span class="topo-membrane">YEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYA</span><span class="topo-unknown">YEVIKHR</span></span>
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
      <td>31</td>
      <td>14</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>45</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>60</td>
      <td>50</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>283</td>
      <td>74</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>297</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>286</td>
      <td>411</td>
      <td>299</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>431</td>
      <td>425</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>443</td>
      <td>445</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>450</td>
      <td>457</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntx">4NTX</a> — Chain H (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-inside">EIRPAFCYEDPPFFQKCGAFVDSYYFNRSRITCVHFFYGQCDVNQNHFTTMSECNRVCHG</span></span>
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
      <td>60</td>
      <td>1</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ntx">4NTX</a> — Chain I (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110         </span>
<span class="topo-line"><span class="topo-inside">NLNQFRLMIKCTNDRVWADFVDYGCYCVARDSNTPVDDLDRCCQAQKQCYDEAVKVHGCKPLVMFYSFECRYLASDLDCSGNNTKCRNFVCNCDRTATLCILTATYNRNNHKIDPSRC</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>118</td>
      <td>1</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nty">4NTY</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQPVSIQAFASSSTLHGISHIFSYERLSLKRV</span><span class="topo-inside">VWALC</span><span class="topo-membrane">FMGSLALLALVCTNRIQYYFLYPHV</span><span class="topo-outside">TKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">KQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">DEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTG</span><span class="topo-unknown">DS</span><span class="topo-outside">EFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGK</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450</span>
<span class="topo-line"><span class="topo-outside">ELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQK</span><span class="topo-membrane">KAYEVAGLLGDIGGQMGLFIGA</span><span class="topo-inside">SILTVLELF</span><span class="topo-unknown">DYAYEVIKHR</span></span>
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
      <td>32</td>
      <td>14</td>
      <td>45</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>33</td>
      <td>37</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>62</td>
      <td>51</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>283</td>
      <td>76</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>297</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>286</td>
      <td>409</td>
      <td>299</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>431</td>
      <td>423</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>440</td>
      <td>445</td>
      <td>453</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>450</td>
      <td>454</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nty">4NTY</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-outside">EIRPAFCYEDPPFFQKCGAFVDSYYFNRSRITCVHFFYGQCDVNQNHFTT</span><span class="topo-unknown">MSECNRV</span><span class="topo-outside">CHG</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>50</td>
      <td>1</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>51</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nty">4NTY</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110         </span>
<span class="topo-line"><span class="topo-outside">NLNQFRLMIKCTNDRVWADFVDYGCYCVARDSNTPVDDLDRCCQAQKQCYDEAVKVHGCKPLVMFYSFECRYLASDLDCSGNNTKCRNFVCNCDRTATLCILTATYNRNNHKIDPSRC</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>118</td>
      <td>1</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nty">4NTY</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQPVSIQAFASSSTLHGISHIFSYERLSLKRV</span><span class="topo-inside">VWALC</span><span class="topo-membrane">FMGSLALLALVCTNRIQYYFLYPHV</span><span class="topo-outside">TKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">KQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">DEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTG</span><span class="topo-unknown">DS</span><span class="topo-outside">EFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGK</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450</span>
<span class="topo-line"><span class="topo-outside">ELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQK</span><span class="topo-membrane">KAYEVAGLLGDIGGQMGLFIGA</span><span class="topo-inside">SILTVLELF</span><span class="topo-unknown">DYAYEVIKHR</span></span>
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
      <td>32</td>
      <td>14</td>
      <td>45</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>33</td>
      <td>37</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>62</td>
      <td>51</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>283</td>
      <td>76</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>297</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>286</td>
      <td>409</td>
      <td>299</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>431</td>
      <td>423</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>440</td>
      <td>445</td>
      <td>453</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>450</td>
      <td>454</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nty">4NTY</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-outside">EIRPAFCYEDPPFFQKCGAFVDSYYFNRSRITCVHFFYGQCDVNQNHFTT</span><span class="topo-unknown">MSECNRV</span><span class="topo-outside">CHG</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>50</td>
      <td>1</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>51</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nty">4NTY</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110         </span>
<span class="topo-line"><span class="topo-outside">NLNQFRLMIKCTNDRVWADFVDYGCYCVARDSNTPVDDLDRCCQAQKQCYDEAVKVHGCKPLVMFYSFECRYLASDLDCSGNNTKCRNFVCNCDRTATLCILTATYNRNNHKIDPSRC</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>118</td>
      <td>1</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nty">4NTY</a> — Chain G (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQPVSIQAFASSSTLHGISHIFSYERLSLKRV</span><span class="topo-inside">VWALC</span><span class="topo-membrane">FMGSLALLALVCTNRIQYYFLYPHV</span><span class="topo-outside">TKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">KQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">DEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTG</span><span class="topo-unknown">DS</span><span class="topo-outside">EFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGK</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450</span>
<span class="topo-line"><span class="topo-outside">ELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQK</span><span class="topo-membrane">KAYEVAGLLGDIGGQMGLFIGA</span><span class="topo-inside">SILTVLELF</span><span class="topo-unknown">DYAYEVIKHR</span></span>
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
      <td>32</td>
      <td>14</td>
      <td>45</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>33</td>
      <td>37</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>62</td>
      <td>51</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>283</td>
      <td>76</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>297</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>286</td>
      <td>409</td>
      <td>299</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>431</td>
      <td>423</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>440</td>
      <td>445</td>
      <td>453</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>450</td>
      <td>454</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nty">4NTY</a> — Chain H (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-outside">EIRPAFCYEDPPFFQKCGAFVDSYYFNRSRITCVHFFYGQCDVNQNHFTT</span><span class="topo-unknown">MSECNRV</span><span class="topo-outside">CHG</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>50</td>
      <td>1</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>51</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nty">4NTY</a> — Chain I (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110         </span>
<span class="topo-line"><span class="topo-outside">NLNQFRLMIKCTNDRVWADFVDYGCYCVARDSNTPVDDLDRCCQAQKQCYDEAVKVHGCKPLVMFYSFECRYLASDLDCSGNNTKCRNFVCNCDRTATLCILTATYNRNNHKIDPSRC</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>118</td>
      <td>1</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature11375

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4h2n">4H2N</a></td>
      <td>3.35 A</td>
      <td>R3</td>
      <td>Chicken delta13 ASIC1a</td>
      <td>PcTx1</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4h2o">4H2O</a></td>
      <td>2.80 A</td>
      <td>C2</td>
      <td>Chicken delta13 ASIC1a</td>
      <td>PcTx1</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293T cells (electrophysiology), E. coli (crystallography)
- **Construct**: Chicken ASIC1a (full-length for electrophysiology), Chicken delta ASIC1 (residues 147-526, truncated extracellular N-terminus for crystallography), Chicken ASIC1 (residues 26-463, for PcTx1 complex)

### doi/10.1038##ncomms1917

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3s3w">3S3W</a></td>
      <td>1.9 A</td>
      <td>C2</td>
      <td>Chicken ASIC1 (residues 26-463, apo)</td>
      <td>none</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3s3x">3S3X</a></td>
      <td>3.0 A</td>
      <td>C2</td>
      <td>Chicken ASIC1 (residues 26-463) + Psalmotoxin 1</td>
      <td>Psalmotoxin 1</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293T cells (electrophysiology), E. coli (crystallography)
- **Construct**: Chicken ASIC1a (full-length for electrophysiology), Chicken delta ASIC1 (residues 147-526, truncated extracellular N-terminus for crystallography), Chicken ASIC1 (residues 26-463, for PcTx1 complex)

**Purification:**

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) ([Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/))
- **Expression construct**: Chicken ASIC1 (residues 26-463), [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/)-tagged
- **Tag info**: [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/), removed with [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) at 4 C or [Thrombin](/xray-mp-wiki/reagents/additives/thrombin/) at room temperature

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
      <td>Cell culture and membrane preparation</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus expression</a> in <a href="/xray-mp-wiki/methods/expression-systems/sf9-expression-system/">Sf9</a> cells</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>(HCl) pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> + --</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9 Insect Cells</a> infected with <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression</a> expressing chicken ASIC1(26-463). Cell debris removed by centrifugation at 488 g for 15 min, supernatant centrifuged at 95,700 g for 35 min at 4 C. Membranes resuspended in 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>(HCl) pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> and stored at -80 C.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>(HCl) pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> + 2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Purified membranes (corresponding to 100 g cells) solubilized in 200 ml buffer with 2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> under stirring for 60 min at 4 C. Supernatant isolated by centrifugation at 150,000 g for 20 min.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> purification</td>
      <td>Nickel-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Resin</a> Superflow <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> resin</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>(HCl) pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed and eluted with 45 mM or 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, respectively, at 4 C. Tag removed with <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> at 4 C or <a href="/xray-mp-wiki/reagents/additives/thrombin/">Thrombin</a> at room temperature for 1 h.</td>
    </tr>
    <tr>
      <td>Complex formation</td>
      <td>In-solution mixing</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>(HCl) pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>0.36 mg of synthetic, lyophilized PcTx1 (Peptanova) dissolved directly in protein solution after tag removal.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>Superose 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>(HCl) pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Excess PcTx1, protease and other buffer components removed. Isolated, monodisperse protein preparation concentrated to 2.7 mg/ml using Amicon Ultra Ultracel centrifugal filter (100 kDa MWCO).</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Chicken ASIC1 (residues 26-463) in complex with <a href="/xray-mp-wiki/reagents/ligands/pc-tx1/">Psalmotoxin</a> 1 at 2.7 mg/ml in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>(HCl) pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in supplementary information</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>matured within 1 week</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals in monoclinic space group C2 with one trimer per asymmetric unit. Collected directly from crystal well with 15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> for cryoprotection, flash frozen in liquid nitrogen. Diffraction data collected to 3.0 A resolution at wavelength 1.0000 A using PILATUS 6M detector at beamline X10SA, Swiss Light Source. Structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with PHASER using apo chicken delta ASIC1 as start model. Refinement with PHENIX using NCS restraints for extracellular domains. Three Ramachandran outliers (6.5% allowed), 6 rotamer outliers.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3s3w">3S3W</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSYYHHHHHHGASLVPRGSHMSTLHGISHIFSYERLSLKRVVW</span><span class="topo-outside">ALCF</span><span class="topo-membrane">MGSLALLALVCTNRIQYYFL</span><span class="topo-inside">YPHVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IPDTQTADEKQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GIKVQIHSQDEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKAT</span><span class="topo-unknown">TGDSEF</span><span class="topo-inside">YDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-inside">PCNVTRYGKELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKAY</span><span class="topo-membrane">EVAGLLGDIGGQMGLFIGAS</span><span class="topo-outside">ILTV</span><span class="topo-unknown">LELFDYAYEVIKHR</span></span>
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
      <td>43</td>
      <td>5</td>
      <td>47</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>44</td>
      <td>47</td>
      <td>48</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>67</td>
      <td>52</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>290</td>
      <td>72</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>296</td>
      <td>295</td>
      <td>300</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>297</td>
      <td>421</td>
      <td>301</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>441</td>
      <td>426</td>
      <td>445</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>445</td>
      <td>446</td>
      <td>449</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>446</td>
      <td>459</td>
      <td>450</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3s3w">3S3W</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSYYHHHHHHGASLVPRGSHMSTLHGISHIFSYERLSLKRVVWALCFM</span><span class="topo-membrane">GSLALLALVCTNRIQYYFL</span><span class="topo-inside">YPHVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IPDTQTADEKQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GIKVQIHSQDEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKAT</span><span class="topo-unknown">TGDS</span><span class="topo-inside">EFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-inside">PCNVTRYGKELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKAY</span><span class="topo-membrane">EVAGLLGDIGGQMGLFIGASILT</span><span class="topo-outside">VLEL</span><span class="topo-unknown">FDYAYEVIKHR</span></span>
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
      <td>47</td>
      <td>5</td>
      <td>51</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>49</td>
      <td>67</td>
      <td>53</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>290</td>
      <td>72</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>294</td>
      <td>295</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>295</td>
      <td>421</td>
      <td>299</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>444</td>
      <td>426</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>448</td>
      <td>449</td>
      <td>452</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>459</td>
      <td>453</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3s3w">3S3W</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSYYHHHHHHGASLVPRGSHMSTLHGISHIFSYERLSLKR</span><span class="topo-outside">VVWAL</span><span class="topo-membrane">CFMGSLALLALVCTNRIQYYFL</span><span class="topo-inside">YPHVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IPDTQTADEKQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GIKVQIHSQDEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKAT</span><span class="topo-unknown">TGDSE</span><span class="topo-inside">FYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-inside">PCNVTRYGKELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKAY</span><span class="topo-membrane">EVAGLLGDIGGQMGLFIGASIL</span><span class="topo-outside">TVL</span><span class="topo-unknown">ELFDYAYEVIKHR</span></span>
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
      <td>40</td>
      <td>5</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>41</td>
      <td>45</td>
      <td>45</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>67</td>
      <td>50</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>290</td>
      <td>72</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>295</td>
      <td>295</td>
      <td>299</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>296</td>
      <td>421</td>
      <td>300</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>426</td>
      <td>447</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>446</td>
      <td>448</td>
      <td>450</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>447</td>
      <td>459</td>
      <td>451</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3s3x">3S3X</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSYYHHHHHHGASLVPRGSHMSTLHGISHIFSYERLSLKR</span><span class="topo-outside">VVWALCFMGSLA</span><span class="topo-membrane">LLALVCTNRIQYYFLYPHV</span><span class="topo-inside">TKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IPDTQTADEKQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GIKVQIHSQDEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCK</span><span class="topo-unknown">ATT</span><span class="topo-inside">GDSEFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-inside">PCNVTRYGKELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQK</span><span class="topo-membrane">KAYEVAGLLGDIGGQMG</span><span class="topo-outside">LFIGASILT</span><span class="topo-unknown">VLELFDYAYEVIKHR</span></span>
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
      <td>40</td>
      <td>5</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>41</td>
      <td>52</td>
      <td>45</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>71</td>
      <td>57</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>288</td>
      <td>76</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>291</td>
      <td>293</td>
      <td>295</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>292</td>
      <td>418</td>
      <td>296</td>
      <td>422</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>435</td>
      <td>423</td>
      <td>439</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>436</td>
      <td>444</td>
      <td>440</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>459</td>
      <td>449</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3s3x">3S3X</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSYYHHHHHHGASLVPRGSHMSTLHGISHIFSYERLSLKRVVWA</span><span class="topo-outside">LCFMGS</span><span class="topo-membrane">LALLALVCTNRIQYYFLYPHV</span><span class="topo-inside">TKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IPDTQTADEKQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GIKVQIHSQDEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATT</span><span class="topo-unknown">GDS</span><span class="topo-inside">EFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-inside">PCNVTRYGKELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQK</span><span class="topo-membrane">KAYEVAGLLGDIGGQMGLF</span><span class="topo-outside">I</span><span class="topo-unknown">GASILTVLELFDYAYEVIKHR</span></span>
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
      <td>44</td>
      <td>5</td>
      <td>48</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>45</td>
      <td>50</td>
      <td>49</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>71</td>
      <td>55</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>291</td>
      <td>76</td>
      <td>295</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>294</td>
      <td>296</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>295</td>
      <td>418</td>
      <td>299</td>
      <td>422</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>437</td>
      <td>423</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>438</td>
      <td>438</td>
      <td>442</td>
      <td>442</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>439</td>
      <td>459</td>
      <td>443</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3s3x">3S3X</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSYYHHHHHHGASLVPRGSHMSTLHGISHIFSYERLSLKRVVWAL</span><span class="topo-outside">CFMGS</span><span class="topo-membrane">LALLALVCTNRIQYYFLYPHV</span><span class="topo-inside">TKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IPDTQTADEKQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GIKVQIHSQDEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKA</span><span class="topo-unknown">TTGD</span><span class="topo-inside">SEFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-inside">PCNVTRYGKELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQK</span><span class="topo-membrane">KAYEVAGLLGDIGGQMGLF</span><span class="topo-outside">IGASILTV</span><span class="topo-unknown">LELFDYAYEVIKHR</span></span>
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
      <td>45</td>
      <td>5</td>
      <td>49</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>46</td>
      <td>50</td>
      <td>50</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>71</td>
      <td>55</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>289</td>
      <td>76</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>293</td>
      <td>294</td>
      <td>297</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>294</td>
      <td>418</td>
      <td>298</td>
      <td>422</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>437</td>
      <td>423</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>438</td>
      <td>445</td>
      <td>442</td>
      <td>449</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>446</td>
      <td>459</td>
      <td>450</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3s3x">3S3X</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30       </span>
<span class="topo-line"><span class="topo-inside">DCIPKWKGCVNRHGDCCEGLECWKRRRSFEVCVPKTP</span></span>
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
      <td>37</td>
      <td>2</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3s3x">3S3X</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30       </span>
<span class="topo-line"><span class="topo-inside">DCIPKWKGCVNRHGDCCEGLECWKRRRSFEVCVPKTP</span></span>
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
      <td>37</td>
      <td>2</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3s3x">3S3X</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30       </span>
<span class="topo-line"><span class="topo-inside">DCIPKWKGCVNRHGDCCEGLECWKRRRSFEVCVPKTP</span></span>
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
      <td>37</td>
      <td>2</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature25782

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ave">6AVE</a></td>
      <td>3.7 A</td>
      <td>C3 (cryo-EM)</td>
      <td>Full-length chicken ASIC1a</td>
      <td>Ca2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5wku">5WKU</a></td>
      <td>2.95 A</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Chicken ASIC1a Delta25 (residues 25-463)</td>
      <td>Ba2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5wku">5WKU</a></td>
      <td>3.2 A</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Chicken ASIC1a Delta25 (residues 25-463)</td>
      <td>Ca2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293T cells (electrophysiology), E. coli (crystallography)
- **Construct**: Chicken ASIC1a (full-length for electrophysiology), Chicken delta ASIC1 (residues 147-526, truncated extracellular N-terminus for crystallography), Chicken ASIC1 (residues 26-463, for PcTx1 complex)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Chicken ASIC1a Delta25 at ~3 mg/mL in 300 mM NaCl, 20 mM Tris pH 8.0, 2 mM C10ThioM, 1 mM DTT, 0.2 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 5 mM CaCl2 or BaCl2</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM Tris pH 8.5-9.5, 150 mM salt, 10-30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 4000</a>, 0.2 M NaCl</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Several weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of Delta25-Ba2+ and Delta25-Ca2+ in space group P2(1)2(1)2(1). Delta25-Ba2+ diffracted to 2.95 A, Delta25-Ca2+ to 3.2 A. Ba2+ structure: Rwork 0.226, Rfree 0.258. Ca2+ structure: Rwork 0.287, Rfree 0.297. <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> added to protein before crystallization. X-ray data collected at Berkeley Center for Structural Biology and Northeastern Collaborative Access Team.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Cryo-EM single particle</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Full-length chicken ASIC1a</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>N/A (cryo-EM)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Full-length ASIC1a determined by cryo-EM to 3.7 A resolution. 26,117 particles, C3 symmetry. Voltage 300 kV, electron exposure 40-50 e-/A2, defocus range -1 to -3 um. Pixel size 1.04 A. Initial model PDB 5WKU. EMDB-7009, PDB-6AVE. Map sharpening B-factor -100 A2. MolProbity score not disclosed.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ave">6AVE</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MMDLKVDEEEVDSGQPVSIQAFASSSTLHGISHIFSYERL</span><span class="topo-outside">SLK</span><span class="topo-membrane">RVVWALCFMGSLALLALVCTNRIQYYF</span><span class="topo-inside">LYPHVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NRYEIPDTQTADEKQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDET</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SFEAGIKVQIHSQDEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTGDSEFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYC</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VCEMPCNVTRYGKELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKAY</span><span class="topo-membrane">EVAGLLGDIGGQMGLFIGASILTVLELFDYA</span><span class="topo-unknown">YEVIKHR</span><span class="topo-outside">L</span><span class="topo-unknown">CRRGKCRKNHKRNNTD</span></span>
<span class="topo-ruler">       490       500       510       520       </span>
<span class="topo-line"><span class="topo-unknown">KGVALSMDDVKRHNPCESLRGHPAGMTYAANILPHHPARGTFEDFTC</span></span>
<details class="topo-details"><summary>Topology coordinates (6 regions)</summary>
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
      <td>41</td>
      <td>43</td>
      <td>41</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>70</td>
      <td>44</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>425</td>
      <td>71</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>456</td>
      <td>426</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>463</td>
      <td>457</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>464</td>
      <td>464</td>
      <td>464</td>
      <td>464</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ave">6AVE</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MMDLKVDEEEVDSGQPVSIQAFASSSTLHGISHIFSYERL</span><span class="topo-outside">SLK</span><span class="topo-membrane">RVVWALCFMGSLALLALVCTNRIQYYF</span><span class="topo-inside">LYPHVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NRYEIPDTQTADEKQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDET</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SFEAGIKVQIHSQDEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTGDSEFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYC</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VCEMPCNVTRYGKELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKAY</span><span class="topo-membrane">EVAGLLGDIGGQMGLFIGASILTVLELFDYA</span><span class="topo-unknown">YEVIKHR</span><span class="topo-outside">L</span><span class="topo-unknown">CRRGKCRKNHKRNNTD</span></span>
<span class="topo-ruler">       490       500       510       520       </span>
<span class="topo-line"><span class="topo-unknown">KGVALSMDDVKRHNPCESLRGHPAGMTYAANILPHHPARGTFEDFTC</span></span>
<details class="topo-details"><summary>Topology coordinates (6 regions)</summary>
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
      <td>41</td>
      <td>43</td>
      <td>41</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>70</td>
      <td>44</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>425</td>
      <td>71</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>456</td>
      <td>426</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>463</td>
      <td>457</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>464</td>
      <td>464</td>
      <td>464</td>
      <td>464</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ave">6AVE</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MMDLKVDEEEVDSGQPVSIQAFASSSTLHGISHIFSYERL</span><span class="topo-outside">SLK</span><span class="topo-membrane">RVVWALCFMGSLALLALVCTNRIQYYF</span><span class="topo-inside">LYPHVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NRYEIPDTQTADEKQLEILQDKANFRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDET</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SFEAGIKVQIHSQDEPPLIDQLGFGVAPGFQTFVSCQEQRLIYLPPPWGDCKATTGDSEFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYC</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VCEMPCNVTRYGKELSMVKIPSKASAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKKAY</span><span class="topo-membrane">EVAGLLGDIGGQMGLFIGASILTVLELFDYA</span><span class="topo-unknown">YEVIKHR</span><span class="topo-outside">L</span><span class="topo-unknown">CRRGKCRKNHKRNNTD</span></span>
<span class="topo-ruler">       490       500       510       520       </span>
<span class="topo-line"><span class="topo-unknown">KGVALSMDDVKRHNPCESLRGHPAGMTYAANILPHHPARGTFEDFTC</span></span>
<details class="topo-details"><summary>Topology coordinates (6 regions)</summary>
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
      <td>41</td>
      <td>43</td>
      <td>41</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>70</td>
      <td>44</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>425</td>
      <td>71</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>456</td>
      <td>426</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>463</td>
      <td>457</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>464</td>
      <td>464</td>
      <td>464</td>
      <td>464</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wku">5WKU</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SSTLHGISHIFSYERLS</span><span class="topo-outside">LKRVV</span><span class="topo-membrane">WALCFMGSLALLALVCTNRIQYYFLY</span><span class="topo-inside">PHVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADEKQLEILQDKAN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQDEPPLIDQLGF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GVAPGFQTFVSCQEQRLIYLPPPWGDCKATTGDSEFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGKELSMVKIPSKA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430         </span>
<span class="topo-line"><span class="topo-inside">SAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKK</span><span class="topo-membrane">AYEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYAYE</span><span class="topo-unknown">VIKHR</span></span>
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
      <td>17</td>
      <td>25</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>22</td>
      <td>42</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>48</td>
      <td>47</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>399</td>
      <td>73</td>
      <td>423</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>420</td>
      <td>424</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>434</td>
      <td>445</td>
      <td>458</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>435</td>
      <td>439</td>
      <td>459</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wku">5WKU</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SSTLHGISHIFSYERLS</span><span class="topo-outside">LKRVV</span><span class="topo-membrane">WALCFMGSLALLALVCTNRIQYYFLYP</span><span class="topo-inside">HVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADEKQLEILQDKAN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FRNF</span><span class="topo-unknown">KPKP</span><span class="topo-inside">FNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQDEPPLIDQLGF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GVAPGFQTFVSCQEQRLIYLPPPWGDCKATTGDSEFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGKELSMVKIPSKA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430         </span>
<span class="topo-line"><span class="topo-inside">SAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKK</span><span class="topo-membrane">AYEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYAYEV</span><span class="topo-unknown">IKHR</span></span>
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
      <td>17</td>
      <td>25</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>22</td>
      <td>42</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>49</td>
      <td>47</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>124</td>
      <td>74</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>128</td>
      <td>149</td>
      <td>152</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>129</td>
      <td>399</td>
      <td>153</td>
      <td>423</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>420</td>
      <td>424</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>435</td>
      <td>445</td>
      <td>459</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>436</td>
      <td>439</td>
      <td>460</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wku">5WKU</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SSTLHGISHIFSYERLS</span><span class="topo-outside">LKRV</span><span class="topo-membrane">VWALCFMGSLALLALVCTNRIQYYFLYP</span><span class="topo-inside">HVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADEKQLEILQDKAN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQDEPPLIDQLGF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GVAPGFQTFVSCQEQRLIYLPPPWGDCKATTGDSEFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGKELSMVKIPSKA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430         </span>
<span class="topo-line"><span class="topo-inside">SAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKK</span><span class="topo-membrane">AYEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYAYEV</span><span class="topo-unknown">IKHR</span></span>
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
      <td>17</td>
      <td>25</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>21</td>
      <td>42</td>
      <td>45</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>49</td>
      <td>46</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>399</td>
      <td>74</td>
      <td>423</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>420</td>
      <td>424</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>435</td>
      <td>445</td>
      <td>459</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>436</td>
      <td>439</td>
      <td>460</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wku">5WKU</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SSTLHGISHIFSYERLS</span><span class="topo-outside">LKRVV</span><span class="topo-membrane">WALCFMGSLALLALVCTNRIQYYFLY</span><span class="topo-inside">PHVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADEKQLEILQDKAN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQDEPPLIDQLGF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GVAPGFQTFVSCQEQRLIYLPPPWGDCKATTGDSEFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGKELSMVKIPSKA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430         </span>
<span class="topo-line"><span class="topo-inside">SAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKK</span><span class="topo-membrane">AYEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYAYE</span><span class="topo-unknown">VIKHR</span></span>
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
      <td>17</td>
      <td>25</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>22</td>
      <td>42</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>48</td>
      <td>47</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>399</td>
      <td>73</td>
      <td>423</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>420</td>
      <td>424</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>434</td>
      <td>445</td>
      <td>458</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>435</td>
      <td>439</td>
      <td>459</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wku">5WKU</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SSTLHGISHIFSYERLS</span><span class="topo-outside">LKRVV</span><span class="topo-membrane">WALCFMGSLALLALVCTNRIQYYFLYP</span><span class="topo-inside">HVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADEKQLEILQDKAN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FRNF</span><span class="topo-unknown">KPKP</span><span class="topo-inside">FNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQDEPPLIDQLGF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GVAPGFQTFVSCQEQRLIYLPPPWGDCKATTGDSEFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGKELSMVKIPSKA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430         </span>
<span class="topo-line"><span class="topo-inside">SAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKK</span><span class="topo-membrane">AYEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYAYEV</span><span class="topo-unknown">IKHR</span></span>
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
      <td>17</td>
      <td>25</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>22</td>
      <td>42</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>49</td>
      <td>47</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>124</td>
      <td>74</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>128</td>
      <td>149</td>
      <td>152</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>129</td>
      <td>399</td>
      <td>153</td>
      <td>423</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>420</td>
      <td>424</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>435</td>
      <td>445</td>
      <td>459</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>436</td>
      <td>439</td>
      <td>460</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wku">5WKU</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SSTLHGISHIFSYERLS</span><span class="topo-outside">LKRV</span><span class="topo-membrane">VWALCFMGSLALLALVCTNRIQYYFLYP</span><span class="topo-inside">HVTKLDEVAATRLTFPAVTFCNLNEFRFSRVTKNDLYHAGELLALLNNRYEIPDTQTADEKQLEILQDKAN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FRNFKPKPFNMLEFYDRAGHDIREMLLSCFFRGEQCSPEDFKVVFTRYGKCYTFNAGQDGKPRLITMKGGTGNGLEIMLDIQQDEYLPVWGETDETSFEAGIKVQIHSQDEPPLIDQLGF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GVAPGFQTFVSCQEQRLIYLPPPWGDCKATTGDSEFYDTYSITACRIDCETRYLVENCNCRMVHMPGDAPYCTPEQYKECADPALDFLVEKDNEYCVCEMPCNVTRYGKELSMVKIPSKA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430         </span>
<span class="topo-line"><span class="topo-inside">SAKYLAKKYNKSEQYIGENILVLDIFFEALNYETIEQKK</span><span class="topo-membrane">AYEVAGLLGDIGGQMGLFIGA</span><span class="topo-outside">SILTVLELFDYAYEV</span><span class="topo-unknown">IKHR</span></span>
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
      <td>17</td>
      <td>25</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>21</td>
      <td>42</td>
      <td>45</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>49</td>
      <td>46</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>399</td>
      <td>74</td>
      <td>423</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>420</td>
      <td>424</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>435</td>
      <td>445</td>
      <td>459</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>436</td>
      <td>439</td>
      <td>460</td>
      <td>463</td>
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

### pH-dependent gating mechanism

At high pH, the finger and thumb domains of ASIC1 are separated, possibly with calcium ions bound in the interdomain cleft. Upon exposure to low pH, calcium ions are released, key acidic residues become protonated, and the thumb and finger domains move together, pivoting around the beta-ball domain. The ion channel then opens and desensitizes, coupled to the thumb domain through a ball-and-socket joint at Trp 288. This mechanism links extracellular proton sensing to transmembrane pore opening.

### Trimer stoichiometry confirmed by crosslinking and light scattering

Glutaraldehyde crosslinking of delta ASIC1 revealed trimeric (250 kDa), dimeric (150 kDa), and monomeric (100 kDa) species. Molecular mass determination by light scattering of the monodisperse peak indicated 165.9 +/- 1.4 kDa, consistent with a trimeric assembly.

### TM2 contains a degenerin (d) position analog

Gly 432 corresponds to the degenerin (d) position found in other Deg/ENaC family members. Maltoside groups from [DDM](/xray-mp-wiki/reagents/detergents/ddm/) detergent molecules are located near this position in the transmembrane domain, viewed parallel to the membrane bilayer plane.

### Chloride binding site in the pore

An anomalous difference Fourier map from crystals soaked in NaBr revealed a [Chloride Ion](/xray-mp-wiki/reagents/additives/chloride/) binding site coordinated by Lys 212 (subunit C), Arg 310, and Glu 314. This represents a specific ion coordination site within the transmembrane pore.

### MitTx acts as a bottle opener to stabilize the open state

[MitTx](/xray-mp-wiki/reagents/ligands/mittx/) binds to the wrist, palm, and thumb domains of ASIC1a like a churchkey bottle opener. The alpha subunit's Phe 14 inserts as a hook into the subunit interface, splaying subunits apart. The binding site overlaps with [Psalmotoxin](/xray-mp-wiki/reagents/ligands/pc-tx1/) binding, explaining why these toxins are mutually exclusive.

### TM2 is a discontinuous helix with a belt-like GAS selectivity filter

TM2 is not a continuous alpha helix but has a break approximately two-thirds of the way across the membrane, dividing it into TM2a (extracellular) and TM2b (cytoplasmic) segments. The GAS (Gly-Ala-Ser) selectivity filter motif adopts an extended, belt-like conformation aligned parallel to the membrane plane.

### TM2b swaps between subunits

The cytoplasmic one-third of TM2 (TM2b) undergoes a swap between adjacent subunits. The TM2b element of one subunit interacts with TM1a of an adjacent subunit, effectively generating a continuous TM2 helical segment.

### Ion selectivity by hydrated ion size barrier

The GAS selectivity filter positions the carbonyl oxygen of Gly 443 directly into the pore, forming a triangular ring with a radius of approximately 3.6 A that matches the radius of a hydrated Na+ ion. The channel is selective for Li+ and Na+ over K+ (~4:1) and nearly impermeable to larger cations Rb+ and Cs+.

### PcTx1 binding site at subunit interfaces

PcTx1 (pilidium toxin 1) binds at the subunit interfaces of the ASIC1a trimer, contacting residues across the wrist, palm, and thumb domains. The arginine residues of the toxin form key interactions at the subunit interface, and the aromatic residues engage in an 'aromatic embrace' with the channel. This binding site overlaps with the acidic pocket region, stabilizing the desensitized conformation of the channel.

### pH-dependent vestibule expansion

The vestibule region undergoes conformational changes between high pH and low pH structures. Flexing of beta1 and beta12 helices expands the vestibule at low pH. Residues Glu 80, Leu 414, and Asn 415 are key players in this conformational change. The E80A mutant shows altered activation kinetics (time constant ~10 ms vs ~400 ms for wild-type) and can be activated by PcTx1 at pH 7.25.

### Transmembrane pore constriction and hydrophobic gating

The high pH structure has a large pore (~10 A diameter at residue 433) while the low pH structure has an elliptical hydrophobic pore constriction lined by Leu 440 from all three subunits. Asp 433 is positioned above the hydrophobic constriction. The L440A and L440S mutants show altered channel function with steady-state currents of ~30% and ~20% of peak current, respectively.

### Cs+ binding site in the wrist region

Anomalous difference electron density maps from Cs+ soaks reveal a cesium binding site in the wrist region of the high pH complex. The Cs+ ion is coordinated by backbone carbonyl oxygens arranged in a specific geometry that can be compared between high pH, low pH, and desensitized state structures using Pro 287 and Pro 288 as reference.

### Correlated structural movements between extracellular and transmembrane domains

Structural rearrangements in the wrist region (Tyr 72 and Trp 288) couple extracellular and transmembrane domain movements. These residues are implicated in channel gating, and their side chains show rotational movements in opposite directions between the desensitized and pH-bound states. Five disulfide bonds in the thumb region (connecting residues 324-336, 322-344, 313-360, 309-362, and 291-366) provide structural stability to this coupling region.

### Peptide plane flip and main chain swap in linkers

A peptide plane flip occurs in the beta1-beta2 linker between residues Thr 84 and Arg 85, which is observed in the desensitized state but not in the toxin-bound high and low pH structures. Additionally, a main chain swap occurs in the beta11-beta12 linker involving residues 412-416, where Leu 414 mediates hydrophobic interactions that differ between the high pH and desensitized structures.

### Transmembrane domain intersubunit contacts

The high pH structure shows intersubunit hydrophobic contacts between Val 46 (TM1) of one subunit and Ile 446 (TM2) of an adjacent subunit. The low pH structure shows a leucine zipper-like motif in the TM domain with leucines at positions i and i+7 (L440 and L447). The TM domains do not participate in direct lattice contacts, suggesting crystal packing does not influence TM domain conformation.

### Hydrophobic seal enhances electrostatic interactions in PcTx1-ASIC1 complex

The hydrophobic patch of PcTx1 wraps around helix 5 of ASIC1 and shields the basic cluster (arginine residues) from bulk solvent. This hydrophobic seal enhances the electrostatic contribution of charge-charge interactions between the arginine guanidinium groups and ASIC1 carboxylates in the acidic pocket, similar to hydrophobic O-rings at protein-protein binding hot spots. The extensive hydrophobic surface (860 A^2 total, with ASIC1-specific residues providing 350 A^2) surrounds the positively charged guanidinium groups. Phe351 and Phe174 of ASIC1 account for 155 A^2 of the binding surface and are critical for PcTx1 selectivity.

### Cation-binding site in the central vestibule

Extra electron density was observed in the occluded central vestibule, approximately 20 A above the ion-selective pore. The vestibule is lined by acidic residues (Glu80, Glu374, Glu412, Gln277, Gln279, Glu417) and the density is located near Glu80 and Glu417. Carboxylate groups of Glu417 coordinate a putative cation right above Leu78, which separates the central from the extracellular vestibule. Arg370 is the only positively charged residue in the central vestibule, located about 7.5 A above the putative cation. This supports the model that the central vestibule functions as a cation reservoir.

### Resting state structure of ASIC1a at high pH

The X-ray and cryo-EM structures of chicken ASIC1a in the resting state at high pH complete the structural characterization of all three canonical functional states (resting, open, desensitized). The resting state shows an expanded extracellular domain with the thumb and finger domains positioned further from the three-fold molecular axis, exposing ~595 A2 additional solvent-accessible surface area per subunit compared to open and desensitized states. The acidic pocket is expanded. The pore is closed, with gate constrictions at Asp433 and Gly436. The transmembrane domain conformation closely resembles that of the desensitized channel, indicating that pore architecture is conserved across non-conducting states.

### Acidic pocket collapse drives channel activation

Proton-dependent gating involves collapse of the acidic pocket: the thumb domain closes into the acidic pocket, the lower palm domain expands, and there is an iris-like opening of the channel gate. Site-directed disulfide crosslinking (T84C-N357C) that anchors the thumb to the palm of a neighboring subunit prevents acidic pocket collapse and blocks proton-dependent activation, confirming that acidic pocket contraction is essential for channel opening. Gly235 and Asp238 alpha-carbon atoms shift by ~3 A between resting and open states.

### Beta11-beta12 linkers act as a molecular clutch for desensitization

The beta11-beta12 linkers that demarcate the upper and lower palm domains serve as a molecular clutch. In the desensitized state, Leu414 and Asn415 side chains swap positions, reorienting Leu414 by ~9 A toward the central vestibule and causing a notable rearrangement of the linkers. This decouples the collapsed acidic pocket from the lower channel, allowing TM1 and TM2a to relax by 6 A and 5 A respectively, re-forming the non-conducting channel. The resulting desensitized channel is conformationally chimeric: resembling the resting channel below the beta11-beta12 linkers and the open channel above them.

### Structural comparison of full-length and Delta25 constructs

The full-length ASIC1a cryo-EM structure at 3.7 A resolution closely resembles the Delta25 X-ray structures but reveals subtle differences. The Delta25 construct (lacking N-terminal 24 and C-terminal 64 residues) shows reduced Na+ selectivity and decreased Hill slope for proton activation compared to full-length. The TM2 domain swap and GAS belt are confirmed as functional features of ASIC1a architecture. The full-length structure confirms that the cytoplasmic domains influence ion selectivity.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for solubilization and SEC purification of ASIC1a
- <a href="/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/">Fluorescence Size-Exclusion Chromatography (FSEC)</a> — FSEC used to identify optimal detergent conditions for ASIC1a
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction (SAD)</a> — Se-Met SAD phasing used to solve the open state structure (3HV4)
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/gas-selectivity-filter/">GAS Selectivity Filter</a> — Central mechanism of ion selectivity in ASIC1a
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Used for Se-SAD phasing of ASIC1a crystals
- <a href="/xray-mp-wiki/reagents/ligands/pc-tx1/">Pilidium Toxin 1 (PcTx1)</a> — Toxin bound in ASIC1a complex structures (PDB 3S3X, 4H2N, 4H2O) at subunit interfaces
- <a href="/xray-mp-wiki/reagents/ligands/mittx/">MitTx (Texas coral snake toxin)</a> — Heteromeric toxin that binds to overlapping site on ASIC1a, stabilizing the open state
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized Metal Affinity Chromatography</a> — Referenced in asic1a
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a> — Referenced in asic1a
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> — Referenced in asic1a
