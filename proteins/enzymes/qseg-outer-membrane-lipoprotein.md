---
title: "QseG Outer Membrane Lipoprotein (E. coli)"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, porin]
sources: [doi/10.1107##s2053230x23009123]
verified: false
---

# QseG Outer Membrane Lipoprotein (E. coli)

## Overview

QseG (also known as YfhG) is an outer membrane lipoprotein from enterohemorrhagic Escherichia coli (EHEC) that functions as part of the QseE/F/G three-component system regulating virulence. It is encoded by the qseG gene within the qseEF operon. QseG co-localizes with the histidine kinase QseE in the periplasmic space and is required for QseE/F activity. Crystal structures were determined at 2.3, 2.35, and 2.60 Å resolution from three different crystallization conditions. QseG consists of an N-terminal globular domain (α1-α6 plus a 3₁₀-helix) and a long C-terminal α7 helix that mediates dimerization via a left-handed coiled-coil-like structure. A disulfide bond forms between Cys56 and Cys80. The C-terminal region of α7 (residues 197-207) exhibits structural flexibility, attributed to polar amino acid substitutions at the hydrophobic coiled-coil interface. The negatively charged α7c region likely interacts with the positively charged surface of QseE.

## Publications

### doi/10.1107##s2053230x23009123

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
      <td></td>
      <td>2.30</td>
      <td>P2_1</td>
      <td>Periplasmic region (residues 56-209) of QseG from E. coli with N-terminal His-tag</td>
      <td>None</td>
    </tr>
    <tr>
      <td></td>
      <td>2.35</td>
      <td>P2_1</td>
      <td>Periplasmic region (residues 56-209) of QseG from E. coli</td>
      <td>None</td>
    </tr>
    <tr>
      <td></td>
      <td>2.60</td>
      <td>P2_12_12_1</td>
      <td>Periplasmic region (residues 56-209) of QseG from E. coli</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: QseG periplasmic region (residues 56-209) with N-terminal His-tag and TEV cleavage site in pET-28a

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
      <td>Cell growth and lysis</td>
      <td>E. coli cells grown at 17°C for 20 h after induction with 0.1 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a>. Cells sonicated in buffer with protease inhibitors.</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 8.0, 200 mM NaCl, cOmplete Protease Inhibitor Cocktail</td>
      <td>Centrifuged at 20,000g for 1 h at 4°C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Supernatant loaded onto HiTrap <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> column</td>
      <td>HiTrap <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a></td>
      <td>50 mM Tris-HCl pH 8.0, 200 mM NaCl</td>
      <td>TEV protease added after elution for tag removal</td>
    </tr>
    <tr>
      <td>Reverse <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Dialyzed sample loaded onto HisTrap column; flowthrough collected</td>
      <td>HisTrap</td>
      <td>20 mM Tris-HCl pH 8.0, 300 mM NaCl</td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Purified on HiLoad 16/60 <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM Tris-HCl pH 8.0, 100 mM NaCl</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor-diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>10 mg/mL QseG in 20 mM Tris-HCl pH 8.0, 100 mM NaCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.08 M Mg acetate tetrahydrate, 0.1 M Na <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 6.0, 14% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> MME 5000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Soaked in crystallization solution supplemented with 20% ethylene glycol before flash-cooling in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal condition 1. Also obtained in condition 2 (0.32 M LiCl, 0.1 M Na <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 5.5, 14% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000) and condition 3 (0.1 M MgCl2, 0.1 M Tris pH 7.5, 13% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 8000). X-ray data collected at SPring-8 BL44XU with EIGER X 16M detector at 0.9 Å wavelength.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Coiled-coil structural polymorphism facilitates QseE interaction

QseG dimerizes through a left-handed coiled-coil formed by the α7 helices. Structural superposition of dimers from three different crystal conditions reveals significant polymorphism at the C-terminal region of the coiled-coil. Approximately one-quarter of the heptad-repeat interface positions are occupied by polar amino acids rather than hydrophobic residues, weakening the hydrophobic core and providing the flexibility needed for interaction with QseE.

### QseG is essential for full virulence

ΔqseG mutants of EHEC show reduced colony-forming units in infant rabbit models, and ΔqseG mutants of Citrobacter rodentium produce attenuated disease symptoms in mice. QseG is also essential for virulence in the fish pathogen Edwardsiella tarda, where it regulates haemolytic activity and invasion. QseG is conserved across multiple Enterobacteriaceae pathogens.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/qsee-periplasmic-domain/">QseE Periplasmic Sensor Domain</a> — QseG interacts with QseE in the periplasm to regulate virulence signaling
- <a href="/xray-mp-wiki/concepts/miscellaneous/qse-efg-three-component-system/">QseE/F/G Three-Component System</a> — QseG is the outer membrane lipoprotein component of this system
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component used in purification or crystallization
