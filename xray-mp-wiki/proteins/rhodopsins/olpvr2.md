---
title: "OLPVRII (Organic Lake Phycodnavirus Rhodopsin II)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-12718-0]
verified: agent
uniprot_id: A0A8I3AZZ2
---

# OLPVRII (Organic Lake Phycodnavirus Rhodopsin II)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A8I3AZZ2">UniProt: A0A8I3AZZ2</a>

<span class="expr-badge">Bacillus subtilis</span>

## Overview

OLPVRII (Organic Lake Phycodnavirus Rhodopsin II) is a viral rhodopsin from group 2, encoded by a nucleocytoplasmic large DNA virus (NCLDV) that infects marine phytoplankton. With only 211 amino acids, it is the smallest microbial rhodopsin with a known crystal structure. OLPVRII assembles into a pentamer with a unique bottle-like central channel featuring a narrow vestibule lined by a ring of five arginine residues (R29) on the cytoplasmic side and a hydrophobic barrier formed by five phenylalanine residues (F24). The proton donor is Glu42 located in helix B, whereas most microbial rhodopsins have the proton donor in helix C. Functional characterization and molecular dynamics simulations suggest that OLPVRII acts as an outward proton pump in liposomes, but its unique pentameric architecture with a central pore analogous to pentameric ligand-gated ion channels suggests it may function as a light-gated ion channel.


## Publications

### doi/10.1038##s41467-019-12718-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6sqg">6SQG</a></td>
      <td>2.50</td>
      <td>P21</td>
      <td>Full-length OLPVRII (residues 1-211)</td>
      <td>all-trans Retinal</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (C41 strain)
- **Construct**: Codon-optimized OLPVRII (Uniprot F2Y2Z0) in pEKT vector
- **Induction**: Not specified
- **Media**: 2xYT medium

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>--</td>
      <td>2xYT medium + --</td>
      <td>5L culture</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Cell disruption and membrane isolation</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 7.6, 300 mM NaCl + --</td>
      <td>Standard membrane preparation protocols</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 7.6, 300 mM NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Protein solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Immobilized metal-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td>50 mM Tris-HCl pH 7.6, 300 mM NaCl, 20 mM imidazole + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His-tag purification</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>10 mM Tris-HCl pH 7.6, 100 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Monomeric and pentameric fractions separated</td>
    </tr>
  </tbody>
</table>
**Final sample**: 20 mg/ml in [DDM](/xray-mp-wiki/reagents/detergents/ddm/)
**Purity**: High (A280/A520 ratio 1.0-1.3 for monomers, 1.3-1.7 for pentamers)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>20-25 mg/ml OLPVRII in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>60:40 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>6-12 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown using in meso approach. Diffraction data collected at P14 beamline (PETRAIII, Hamburg). Structure solved by molecular replacement using archaerhodopsin-2 (PDB 2Ei4) as search model.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Unique pentameric architecture with central channel

OLPVRII assembles as a pentamer with a bottle-shaped central pore formed by the A and B helices of the protomers. The narrowest section (vestibule) is 11 Å long with a mean diameter of 6 Å. On the cytoplasmic side, a ring of five conserved arginine residues (R29) forms the entrance, while five phenylalanine residues (F24) create a hydrophobic barrier deeper in the pore. This architecture is unique among microbial rhodopsins and is structurally analogous to the transmembrane channels of pentameric ligand-gated ion channels (pLGICs) such as GLIC.

### Proton donor relocated to helix B

Unlike most microbial rhodopsins where the proton donor is Asp96 in helix C (as in bacteriorhodopsin), OLPVRII has its proton donor Glu42 located in helix B. This is a striking difference in the architecture of the proton translocation pathway. The E42Q mutant showed a prolonged M-state decay (similar to D96N in bacteriorhodopsin), confirming its role as the proton donor. The proton acceptor is Asp75, as the D75N mutant failed to form the M-state.

### Photocycle kinetics

The total photocycle of OLPVRII is approximately 70 ms at pH 7.5, with seven exponential components. The microsecond part (1-340 µs) includes K540-like to M410-like transitions representing RSB deprotonation. The millisecond part (10-73 ms) involves recovery of the ground state via M410-, N525-, and O550-like intermediates. The pKa of the RSB is 10.36 ± 0.08, and the pKa of the proton acceptor Asp75 is 3.34 ± 0.11.

### Outward proton pump activity

Black lipid membrane (BLM) experiments showed that OLPVRII generates photocurrents upon illumination. Without protonophores, a transient current was observed; with the ionophores 1799 and monensin, continuous pumping was detected. Time-resolved BLM measurements identified charge movements with time constants of 24 µs, 6 ms, 90 ms, and 950 ms, corresponding to the photocycle transitions. Direct pH measurements in liposomes confirmed outward proton pumping, although the charge transfer per photocycle is small compared to expected channel activity.

### Pentameric assembly is conserved in group II viral rhodopsins

The key amino acids forming the pentamer (E26, R36, W203) are highly conserved in group II viral rhodopsins. A triple mutant (E26A/R36A/W203A) showed reduced pentamer:monomer ratio (1:1 vs 4:1 for WT), confirming the importance of these residues for pentamerization. The pentameric assembly is required for the formation of the central pore/channel and likely determines the function of group II viral rhodopsins.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/olpvr1/">OLPVR1</a> — Related group 1 viral channelrhodopsin from the same virus
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Archetypal microbial rhodopsin for structural comparison
- <a href="/xray-mp-wiki/proteins/rhodopsins/kr2/">KR2 (Krokinobacter eikastus sodium-pumping rhodopsin)</a> — Reference for pentameric rhodopsin structure comparison
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/glic/">GLIC (Gloeobacter violaceus ligand-gated ion channel)</a> — Structural analog for pentameric channel architecture
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">All-trans retinal</a> — Chromophore cofactor covalently bound via Schiff base to Lys195
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization lipid matrix
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent for protein solubilization and purification
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> — Immobilized metal affinity chromatography resin
- <a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> — Size-exclusion chromatography resin
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> — Crystallization method used for structure determination
