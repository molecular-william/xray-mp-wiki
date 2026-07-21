---
title: "E. coli SemiSWEET (EcSemiSWEET)"
created: 2026-06-05
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms7112]
verified: agent
uniprot_id: O75469
---

# E. coli SemiSWEET (EcSemiSWEET)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O75469">UniProt: O75469</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

EcSemiSWEET is a sugar transporter from the SWEET family found in Escherichia coli. It is a bacterial homolog of eukaryotic SWEET transporters and belongs to the PQ-loop family characterized by a conserved Pro-Gln motif. EcSemiSWEET functions as a dimer of three-helix bundles and mediates facilitative diffusion of sugars across biological membranes. Crystal structures in both inward-open and outward-open conformations reveal a 'binder clip-like' conformational mechanism driven by the PQ-loop hinge motif.


## Publications

### doi/10.1038##ncomms7112

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4x5m">4X5M</a></td>
      <td>2.0</td>
      <td>P212121</td>
      <td><a href="/xray-mp-wiki/concepts/semisweet">SemiSWEET Transporter Family</a>-LESSGEN-LYFQGQFTS-H8</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4x5m">4X5M</a></td>
      <td>3.0</td>
      <td>C2</td>
      <td><a href="/xray-mp-wiki/concepts/semisweet">SemiSWEET Transporter Family</a>-LESSGEN-LYFQGQFTS-H8</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli Rosetta 2 (DE3)
- **Construct**: [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet)-LESSGEN-LYFQGQFTS-H8
- **Induction**: 0.2 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg), OD600 0.6, 20 C for 20 h

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
      <td>Microfluidizer processor</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a></td>
      <td>Three passes at 15,000 psi; debris removed by 10,000g for 10 min</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td><a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">Ultracentrifugation</a></td>
      <td>--</td>
      <td>--</td>
      <td>138,000g for 1 h to collect membrane fraction</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM Tris-HCl pH 8.0, 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> (2%), <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) (0.4%)</td>
      <td>90 min at 4 C; insoluble removed by 138,000g for 30 min</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">IMAC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) resin (Qiagen)</td>
      <td>20 mM Tris-HCl pH 8.0, 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Incubated 90 min; washed; eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV Protease</a> cleavage</td>
      <td>--</td>
      <td><a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>-free Tris buffer</td>
      <td>His8-tag cleaved by tobacco etch virus protease; dialysed overnight</td>
    </tr>
    <tr>
      <td>Secondary affinity purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">IMAC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) resin</td>
      <td><a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>-free Tris buffer</td>
      <td>Remove cleaved His8-tag and <a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV Protease</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/concepts/semisweet">SemiSWEET Transporter Family</a>-H8 (inward-open)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Inward-open structure (Crystal-I) with <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a> in substrate pocket</td>
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
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/concepts/semisweet">SemiSWEET Transporter Family</a>-H8 (outward-open)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Outward-open structure (Crystal-II); both conformations captured simultaneously</td>
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

## Biological / Functional Insights

### Binder clip-like conformational mechanism

EcSemiSWEET undergoes intramolecular conformational changes in each protomer, not rigid-body movement. The conserved PQ-loop motif (Pro21, Gln22) serves as a flexible molecular hinge enabling a 'binder clip-like' motion. TM1 bends at Pro21, allowing the structural unit (TM1b, TM2, TM3, TM1a') to rotate relative to its counterpart in the dimer.

### Dual gating mechanism

Two gates control substrate access to the central binding pocket. The extracellular gate (Tyr53, Arg57, Asp59) seals the pocket from outside in the inward-open state via salt bridges and hydrogen bonds. The intracellular gate (Phe19, Met39, Tyr40, Phe43) blocks access from the cytoplasm in the outward-open state via hydrophobic interactions. Mutagenesis reveals opposite effects: disrupting extracellular gate increases activity, while disrupting intracellular gate decreases it.

### Substrate binding pocket

The central pocket (8-9 A wide, 11 A long) is lined by Trp50 and Asn66 residues. [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) bound in the inward-open structure mimics sugar substrate via its glycerol head group forming hydrogen bonds with Asn66 and sandwiched between Trp50 aromatic rings. N66A mutation significantly decreases sucrose uptake. W50A mutation increases uptake (enlarged pocket), while W50F has no effect.

### Low-affinity sucrose transport

EcSemiSWEET mediates slow but significant [14C]-[Sucrose](/xray-mp-wiki/reagents/ligands/sucrose) uptake in proteoliposomes. Uptake rate increases linearly with sucrose concentration up to 300 mM without saturation, indicating low-affinity binding. This contrasts with higher-affinity eukaryotic SWEET transporters, suggesting sucrose may not be the physiological substrate.

### Transport cycle model

Proposed transport cycle: inward-open state captures substrate -> PQ-loop hinge enables transition -> slight TM2 bend closes intracellular gate (occluded state) -> extracellular gate opens -> substrate exits -> inward-open and outward-open conformations can interconvert spontaneously without substrate.


## Cross-References

- <a href="/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/">LbSemiSWEET</a> — Related bacterial [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet) from Leptospira biflexa with solved outward-open and occluded structures
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sweet-transporter/">SWEET Transporter Family</a> — EcSemiSWEET is a bacterial member of the SWEET family of sugar transporters
- <a href="/xray-mp-wiki/concepts/protein-families/pq-loop-family/">PQ-Loop Family</a> — EcSemiSWEET is a PQ-loop family member characterized by conserved Pro-Gln motif
- <a href="/xray-mp-wiki/concepts/miscellaneous/binder-clip-motion/">Binder Clip Motion</a> — EcSemiSWEET undergoes binder clip-like conformational change mediated by PQ-loop hinge
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Primary detergent used for solubilization of EcSemiSWEET membrane fraction
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Stabilizing additive used with [DDM](/xray-mp-wiki/reagents/detergents/ddm) during solubilization and purification
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Inducer for protein expression at 0.2 mM
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Primary buffer component (50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris) pH 8.0) for expression and purification
- <a href="/xray-mp-wiki/reagents/affinity-resins/ni-nta/">Ni-NTA Agarose Resin</a> — Affinity resin used for His8-tag purification of EcSemiSWEET
- <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> — Tobacco etch virus protease used to cleave His8-tag from EcSemiSWEET
