---
title: "Vcx1 (Saccharomyces cerevisiae Vacuolar Ca2+/H+ Exchanger)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12233]
verified: false
---

# Vcx1 (Saccharomyces cerevisiae Vacuolar Ca2+/H+ Exchanger)

## Overview

Vcx1 (also known as Hum1p) is a vacuolar Ca2+/H+ exchanger from Saccharomyces cerevisiae belonging to the CAX (Ca2+/H+ exchanger) family within the Ca2+:cation (CaCA) superfamily. It catalyses low-affinity (Km ~25 µM), high-capacity (Vmax ~35 nmol Ca2+ min-1 mg-1) vacuolar Ca2+ exchange, playing a key role in cytosolic Ca2+ homeostasis. The 2013 crystal structure of Vcx1 at 2.3 Å resolution (Waight et al., Nature 2013) was the first CAX family structure determined, and the first structure of the CaCA superfamily in a cytosol-facing, substrate-bound conformation. Vcx1 is approximately 400 residues long with 11 predicted transmembrane helices comprising a regulatory helix (MR) and 10 transport-performing helices (M1-M10) arranged as two symmetrically related halves (M1-M5 and M6-M10).


## Publications

### doi/10.1038##nature12233

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4kna">4KNA</a></td>
      <td>2.3</td>
      <td>C2</td>
      <td>Full-length Vcx1 with N-terminal and C-terminal decahistidine tags</td>
      <td>Ca2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae (strain DSY-5; MATa his3::GAL1-GAL4 pep4 prb1-1122)
- **Construct**: Full-length Vcx1 (Uniprot Q99385) in 2µ expression plasmid p423-GAL1 with N-terminal and C-terminal decahistidine purification tags
- **Notes**: High-density fermentation in Biostat C15L fermenter; ~1.8-2 kg wet cell weight harvested per preparation
- **Induction**: Fed-batch with 40% galactose for 18-22 h

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
      <td>Bead mill</td>
      <td>—</td>
      <td>100 mM Tris pH 7.0, 700 mM NaCl, 1 mM PMSF + protease inhibitors</td>
      <td>Frozen pellets thawed in lysis buffer; homogenate centrifuged at 21,600g for 25 min</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>50 mM Tris pH 7.0, 600 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Sedimentation at 185,000g for 150 min; 100 g yeast yields ~20-25 g membrane</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>n-Dodecyl-β-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>50 mM Tris pH 7.0, 600 mM NaCl, 20 mM CaCl2, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM PMSF + protease inhibitors</td>
      <td>1:0.19 (w/w) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>:protein ratio; 30 min at 4 °C; unsolubilized material removed at 120,000g for 30 min</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Co2+ resin</td>
      <td>50 mM Tris pH 7.0, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 20 mM CaCl2, 5 mM MnCl2, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Lysate supplemented with 8 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> pH 6.5 before loading; washes with 15 mM and 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; elution with increasing <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> concentration</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>—</td>
      <td>20 mM HEPES pH 7.0, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final polishing step; protein concentrated for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) with Jeffamine M-600 sponge phase and vapour phase diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified Vcx1 in 20 mM HEPES pH 7.0, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in-meso by combining LCP with Jeffamine M-600 sponge phase conditions; structure solved by MR-SAD using mjNCX (PDB 3V5U) as search model</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Alternating access mechanism for CaCA superfamily

The Vcx1 structure reveals a cytosol-facing, substrate-bound conformation, providing the structural basis for an [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) in the CaCA superfamily. Comparison with the archaeal mjNCX (PDB 3V5U), which represents a periplasm-facing conformation, shows that translational movements of the M1/M6 helices act as a piston-like mechanism to alternately occlude and expose intake and efflux pathways. The M2a helix shifts by ~16 Å between the two conformations. Key residues Glu106 and Glu302 coordinate the active site Ca2+ ion, while Glu83, Asp234, and Glu230 coordinate two regulatory Ca2+ ions at the acidic helix.

### Acidic helix regulation

The acidic motif (the negatively charged loop connecting helices M5 and M6) forms an α-helix that coordinates two Ca2+ ions via Asp234, Glu230, and Glu83. Molecular dynamics simulations suggest this helix becomes more flexible in the absence of Ca2+, indicating a possible Ca2+-dependent regulatory function analogous to the CBD1 domain in mammalian NCX members.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Used for membrane solubilization and purification of Vcx1
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris(hydroxymethyl)aminomethane)</a> — Used in lysis, membrane solubilization, and purification buffers
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
