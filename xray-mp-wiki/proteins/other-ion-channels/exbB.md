---
title: "ExbB (E. coli)"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19757]
verified: agent
uniprot_id: P0ABU7
---

# ExbB (E. coli)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0ABU7">UniProt: P0ABU7</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

ExbB is an integral polytopic membrane protein from Escherichia coli that is a core component of the Ton complex, which transduces energy from the proton motive force at the inner membrane to [TonB (E. coli)](/xray-mp-wiki/proteins/tonB)-dependent transporters at the outer membrane. ExbB contains three transmembrane helices and a large cytoplasmic domain. It assembles as a pentamer with a transmembrane pore and a large enclosed cytoplasmic cavity featuring a strongly electropositive basic belt and an electronegative cap. The ExbB pentamer forms an ion channel with a conductance of approximately 220 pS at neutral pH.


## Publications

### doi/10.1038##nature19757

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5sv0">5SV0</a></td>
      <td>2.6 A</td>
      <td>P63</td>
      <td>ExbB (residues 1-237)</td>
      <td>calcium ion</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5sv0">5SV0</a></td>
      <td>3.5 A</td>
      <td>P212121</td>
      <td>ExbB (residues 1-237)</td>
      <td>calcium ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli K-12 BL21(DE3) cells transformed with pET26b/ExbB plasmid
- **Construct**: ExbB with C-terminal 6xHis tag, expressed in LB or SelenoMet medium

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
      <td>Cell lysis</td>
      <td>Emulsiflex-C3 high-pressure homogenization</td>
      <td>--</td>
      <td>1xPBS + --</td>
      <td>Cells resuspended in 1xPBS with 100 uM AEBSF, 100 uM DNase, 50 ug/ml lysozyme; disrupted at ~15,000 p.s.i.</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation</td>
      <td>--</td>
      <td>1xPBS or TBS + --</td>
      <td>Pelleted at 200,000g for 1 h at 4 C; membranes resuspended with dounce homogenizer</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization</td>
      <td>--</td>
      <td>1xPBS or TBS + 1% <a href="/xray-mp-wiki/reagents/detergents/triton-x-100">Triton X-100</a></td>
      <td>Solubilized by addition of <a href="/xray-mp-wiki/reagents/detergents/triton-x-100">Triton X-100</a> to 1% final concentration</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>His-tag <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>--</td>
      <td>1xPBS or TBS + 1% <a href="/xray-mp-wiki/reagents/detergents/triton-x-100">Triton X-100</a></td>
      <td>Purified using C-terminal 10xHis tag on <a href="/xray-mp-wiki/proteins/exbD">ExbD (E. coli)</a> in the ExbB-ExbD subcomplex</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>ExbB-<a href="/xray-mp-wiki/proteins/exbD">ExbD (E. coli)</a> subcomplex at pH 7.0</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in paper</td>
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
      <td>Initial phases calculated using Se-SAD at 5.2 A resolution (Extended Data Fig. 1). Native structure at 2.6 A solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> using the Se-SAD model. Two ExbB pentamers per asymmetric unit with some helical shifts indicating flexibility. Ring-like difference density observed along conserved residues T148 and T181 in the transmembrane pore.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Pentameric assembly with transmembrane pore and cytoplasmic cavity

ExbB forms a stable pentamer with approximately 3,000 A^2 of buried surface area between adjacent monomers (~20% of total surface area). The pentamer has a transmembrane pore with pore radius of approximately 2 A on the cytoplasmic side and 4 A along the transmembrane side. Five side fenestrations are observed that could allow solvent or ion passage. The large cytoplasmic domain forms an enclosed cavity with five-fold symmetry, edges measuring approximately 45 A.

### Electrostatic surface properties — basic belt and electronegative cap

Each ExbB monomer contributes six lysine residues (positions 44, 52, 56, 81, 108, 206) and twelve arginine residues (positions 53, 54, 57, 66, 110, 114, 117, 118, 124, 128, 200, 222) to form a strongly electropositive basic belt near the membrane interface. Seven aspartates (positions 73, 77, 102, 103, 211, 223, 225) and 11 glutamates (positions 47, 58, 64, 90, 94, 96, 99, 105, 109, 116, 227) form a strongly electronegative cap at the cytoplasmic end.

### Calcium ion binding at cytoplasmic pore

Residues E105 and E109 line the cytoplasmic pore and coordinate a single calcium ion observed in the crystal structure. This binding site is located at the narrowest point of the cytoplasmic cavity.

### Ion channel conductance properties

The ExbB pentamer alone forms ion channels with a conductance of 220 +/- 50 pS at neutral pH, approximately twice the conductance of the full ExbB-[ExbD (E. coli)](/xray-mp-wiki/proteins/exbD) subcomplex (120 +/- 30 pS). This is consistent with the transmembrane helix of ExbD plugging the transmembrane pore of the ExbB pentamer. The channel displays pH sensitivity, with conductance decreasing from 120 pS at pH 8.0 to 70 pS at pH 4.5, and channel closure below pH 4.5.

### Conformational flexibility of the ExbB pentamer

Two ExbB pentamers were observed per asymmetric unit with helical shifts between them, possibly indicating a propensity for movement within the membrane domain. The loops connecting alpha-helices 6 and 7 show variability between monomers and pentamers. B-factor analysis shows the most disordered regions in the periplasmic domain.


## Cross-References

- <a href="/xray-mp-wiki/proteins/other-ion-channels/exbD/">ExbD (E. coli)</a> — ExbB forms a stable pentamer that interacts with the [ExbD (E. coli)](/xray-mp-wiki/proteins/exbD) dimer to constitute the Ton subcomplex
- <a href="/xray-mp-wiki/proteins/other-ion-channels/tonB/">TonB (E. coli)</a> — TonB interacts with the ExbB-[ExbD (E. coli)](/xray-mp-wiki/proteins/exbD) subcomplex to form the fully assembled Ton complex
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for solubilization of the fully assembled Ton complex
- <a href="/xray-mp-wiki/reagents/detergents/triton-x-100/">Triton X-100</a> — Detergent used for solubilization of the Ton subcomplex (1% final concentration)
- <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">Calcium Chloride</a> — Calcium ion observed binding at the cytoplasmic pore (E105/E109) in the crystal structure
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction (SEMet-SAD)</a> — Initial phases calculated using Se-SAD at 5.2 A resolution
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Native 2.6 A structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) using the Se-SAD model
- <a href="/xray-mp-wiki/methods/quality-assessment/deer-spectroscopy/">DEER Spectroscopy</a> — DEER performed on ExbB C25S mutant labeled with MTSL at position C25 to confirm pentameric state
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a> — Crystallization method used for structure determination
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a> — Purification method used in protein preparation
