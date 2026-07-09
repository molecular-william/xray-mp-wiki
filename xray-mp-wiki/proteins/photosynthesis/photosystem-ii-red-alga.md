---
title: "Photosystem II from Cyanidium caldarium (red alga)"
created: 2026-06-09
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.M115.711689]
verified: regex
uniprot_id: Q9TLR0
---

# Photosystem II from Cyanidium caldarium (red alga)


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9TLR0">UniProt: Q9TLR0</a>

<span class="expr-badge">Cyanidium caldarium</span>

## Overview

[Photosystem II](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/) (PSII) catalyzes light-induced water-splitting, producing molecular oxygen essential for aerobic life. The first crystal structure of eukaryotic PSII was determined from the red alga Cyanidium caldarium at 2.76 A resolution by X-ray crystallography (Ago et al., 2016, JBC). The structure revealed a tetramer in the crystallographic asymmetric unit composed of two dimers stacked through their stromal surfaces. Each monomer contains 22 protein subunits, including 18 transmembrane and 4 peripheral subunits. Key features unique to eukaryotic PSII include the PsbQ' extrinsic protein, a 4-helix bundle located underneath CP43 that stabilizes the oxygen-evolving complex, and two additional transmembrane helices identified as PsbW and a novel helix not present in cyanobacterial PSII.


## Publications

### doi/10.1074##jbc.M115.711689

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4yuu">4YUU</a></td>
      <td>2.76</td>
      <td>P212121</td>
      <td>PSII core dimer from Cyanidium caldarium comprising D1 (PsbA), D2 (PsbD), CP43 (PsbC), CP47 (PsbB), cytochrome b-559 alpha and beta (PsbE, PsbF), PsbH, PsbI, PsbJ, PsbK, PsbL, PsbM, PsbT, PsbX, PsbZ, Ycf12 (Psb30), and extrinsic proteins PsbO, PsbV (cytochrome c550), PsbU, PsbQ'; also includes two novel TM helices (chains S and W, the latter identified as PsbW)</td>
      <td>Chlorophyll a, pheophytin a, <a href="/xray-mp-wiki/reagents/ligands/heme/">HEME</a>, non-<a href="/xray-mp-wiki/reagents/ligands/heme/">HEME</a> <a href="/xray-mp-wiki/reagents/additives/iron/">IRON</a>, Mn4CaO5 manganese cluster, <a href="/xray-mp-wiki/reagents/ligands/plastoquinone/">Plastoquinone</a>, bicarbonate, carotenoids, Cl- ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Cyanidium caldarium (red alga, eukaryotic)
- **Construct**: PSII core complex from wild-type cells
- **Notes**: Cells grown at 42 C for 12-15 days under bubbling air containing 3-5% CO2. Harvested cells broken by glass beads. PSII core complexes purified from thylakoid membranes.

**Purification:**

- **Expression system**: Cyanidium caldarium (acidophilic, thermophilic red alga)
- **Expression construct**: Wild-type PSII core complex
- **Tag info**: None (untagged native complex)

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
      <td>Cell growth</td>
      <td>Phototrophic culture</td>
      <td></td>
      <td></td>
      <td>Cells grown at 42 degrees C for 12-15 days under bubbling of air containing 3-5% CO2</td>
    </tr>
    <tr>
      <td>Cell breakage</td>
      <td>Glass bead homogenization</td>
      <td></td>
      <td></td>
      <td>Harvested cells broken by glass beads</td>
    </tr>
    <tr>
      <td>Thylakoid membrane isolation</td>
      <td>Differential centrifugation</td>
      <td></td>
      <td></td>
      <td>Thylakoid membranes isolated from broken cells</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>n-dodecyl-alpha-D-maltoside (alpha-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>alpha-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> used instead of beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for improved crystal quality</td>
    </tr>
    <tr>
      <td>Column purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Column Chromatography</a> (unspecified resin type)</td>
      <td></td>
      <td>alpha-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>All column purification steps and re-suspension buffers included alpha-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: Oxygen-evolving PSII core complexes; activity 3000-4000 umol O2/mg Chl/h
**Purity**: Confirmed by SDS-PAGE and mass spectrometry; all known PSII subunits present

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/batch-crystallization-free-interface-diffusion/">Batch Crystallization</a> with oil batch method</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PSII core complexes in buffer with alpha-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>7-10 days (second crystallization); microcrystals grown overnight at 0 degrees C (first crystallization)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 35% <a href="/xray-mp-wiki/reagents/additives/peg3000/">PEG 3000</a>; crystal dehydration against saturated NaBr humidity for 4 hours at 20 degrees C; then flash-frozen in nitrogen gas stream at 100 K</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Two-step crystallization process. Initially, microcrystals grown overnight at 0 degrees C from re-crystallization step. Microcrystals collected by centrifugation, re-dissolved, and used for the second crystallization with oil batch method. Large crystals obtained in 7-10 days at 4 degrees C, reaching 0.6 x 0.3 x 0.1 mm. Crystal dehydration was critical for improving resolution. Data collected at SPring-8 beamlines BL41XU and BL44XU. Phasing by <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> using Ta6Br14 derivative (peak, inflection, high remote) plus tungsten and <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury (HgCl2) - Aquaporin Inhibitor</a> derivatives. Initial phases at 4.5 A by SOLVE, extended to 2.9 A by RESOLVE. Space group P2(1)2(1)2(1) with 4 tetramers per unit cell.
</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### First eukaryotic PSII crystal structure

The 2.76 A structure of red algal PSII represents the first crystal structure of PSII from a eukaryotic oxygenic organism. The structure exists as a tetramer in the asymmetric unit (two dimers stacked through stromal surfaces, rotated ~20 degrees relative to each other). The dimer is the functional unit, with the tetramerization arising from crystal packing. Each monomer contains 22 protein subunits (18 TM, 4 peripheral), compared to 20 in cyanobacterial PSII.

### PsbQ' location and structure

The PsbQ' extrinsic protein was located underneath CP43 on the lumenal side, near PsbV. The structure reveals a 4-helix bundle similar to higher plant and cyanobacterial PsbQ. Helices I and II are bent due to interaction between PsbQ'-Arg150 and the PGGGD motif (Pro191-Asp195) in loop C of CP43. This electrostatic interaction explains the binding specificity of PsbQ' to red algal PSII. The four extrinsic proteins (PsbO, PsbQ', PsbU, PsbV) form a circle around the Mn4CaO5 cluster, providing a protective cap.

### Two novel transmembrane helices

Two additional transmembrane helices not present in cyanobacterial PSII were identified. One helix (chain S) is located outside PsbI near the N-terminal region of D1 (PsbA). The other (chain W) is adjacent to TM helix II of CP47 and near the N-terminal region of PsbH. Mass spectrometry identified PsbW, a subunit known only in eukaryotic PSII, corresponding to one of these helices. The second novel helix could correspond to PsbY (at a different location than in cyanobacteria) or Psb27.

### Oxygen-evolving complex conservation

The Mn4CaO5 cluster of the oxygen-evolving complex (OEC) was modeled based on the cyanobacterial structure, with inter-atomic distances restrained from the high-resolution cyanobacterial structure. A terminal water ligand on Mn4 corresponding to W1 in cyanobacterial PSII was observed. One chloride ion (Cl-2, near D1-Asn338 and CP43-Glu354) was found. The overall architecture of the OEC is conserved between eukaryotic and cyanobacterial PSII.

### Evolutionary significance of PSII subunit composition

The red algal PSII contains a mixture of cyanobacterial-type and eukaryotic-type features. It has three cyanobacteria-type extrinsic proteins (PsbO, PsbU, PsbV) plus the eukaryotic-specific PsbQ'. The presence of PsbW (absent in cyanobacteria) and two additional TM helices reveals an evolutionary transition from prokaryotic to eukaryotic PSII. The PsbW subunit in red algae likely serves a different function than in green algae/higher plants, since red algae use phycobilisomes (not LHCII) as light-harvesting antenna.


## Cross-References

- <a href="/xray-mp-wiki/proteins/photosynthesis/photosystem-ii-core-dimer/">Photosystem II core dimer from Thermosynechococcus elongatus</a> — Cyanobacterial PSII structure used for comparison with eukaryotic red algal PSII
- <a href="/xray-mp-wiki/proteins/photosynthesis/psba2-psii/">PsbA2-PSII dimer from Thermosynechococcus elongatus</a> — Higher resolution cyanobacterial PSII structure with D1-2 variant
- <a href="/xray-mp-wiki/proteins/photosynthesis/psba3-psii/">PsbA3-PSII dimer from Thermosynechococcus elongatus</a> — Higher resolution cyanobacterial PSII structure with D1-3 variant
- <a href="/xray-mp-wiki/concepts/miscellaneous/manganese-calcium-cluster/">Manganese-Calcium Cluster</a> — Catalytic center for water-splitting in PSII
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/kok-cycle/">Kok Cycle</a> — The S-state cycle of water oxidation catalyzed by the Mn4CaO5 cluster in PSII
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Structurally related detergent; alpha-DDM analog used for PSII solubilization and crystallization
- <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/">Photosystem II</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iron/">IRON</a> — Additive used in purification or crystallization buffers
