---
title: "Human TRPML1 (Mucolipin-1) - Luminal Domain"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3362]
verified: false
---

# Human TRPML1 (Mucolipin-1) - Luminal Domain

## Overview

Human TRPML1 is a Ca2+-release channel primarily located in lysosomes, belonging to the transient receptor potential mucolipin (TRPML) subfamily of ion channels. It plays crucial roles in lysosome-dependent cellular events including exocytosis, membrane trafficking, and autophagy. Mutations in TRPML1 cause mucolipidosis type IV (MLIV), a severe lysosomal storage disorder characterized by neurodegeneration, mental retardation, and blindness. Crystal structures of the luminal I-II linker domain (residues 84-296) at pH 4.5, 6.0, and 7.5 revealed a tetrameric assembly with a novel highly electronegative central pore (the luminal pore) formed by a luminal pore loop, which is critical for the dual regulation of TRPML1 by luminal Ca2+ and pH.


## Publications

### doi/10.1038##nsmb.3362

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5tja">5TJA</a></td>
      <td>2.3</td>
      <td>I422</td>
      <td>Human TRPML1 residues 84-296 (luminal I-II linker domain) with N-terminal MBP tag and C-terminal hexahistidine tag, thrombin-cleaved</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5tjb">5TJB</a></td>
      <td>2.4</td>
      <td>P42(1)2</td>
      <td>Human TRPML1 residues 84-296 (luminal I-II linker domain), residues 200-213 removed, with N-terminal MBP tag and C-terminal hexahistidine tag, thrombin-cleaved</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5tjc">5TJC</a></td>
      <td>2.4</td>
      <td>F432</td>
      <td>Human TRPML1 residues 84-296 (luminal I-II linker domain), residues 200-213 removed, with N-terminal MBP tag and C-terminal hexahistidine tag, thrombin-cleaved</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli Rosetta-gami 2(DE3)
- **Construct**: Human TRPML1 luminal linker (residues 84-296) with N-terminal MBP tag (maltose-binding protein), thrombin recognition site between MBP and linker, and C-terminal hexahistidine tag
- **Induction**: 0.1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 22 degC for 12 hours
- **Media**: LB medium containing 50 ug/ml [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) and 34 ug/ml [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/)

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
      <td>Sonication</td>
      <td></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a>, pH 8.0, 300 mM NaCl, 2.5% (w/w) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Cells resuspended with 5 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.5 mg/ml lysozyme, 25 ug/ml DNase, 2 mM PMSF; debris removed by centrifugation at 17,000g for 30 min</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA His-Bind resin (Novagen)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a>, pH 8.0, 300 mM NaCl, 2.5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in solution A</td>
    </tr>
    <tr>
      <td>Amylose <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Amylose resin (NEB)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a>, pH 8.0, 300 mM NaCl, 2.5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Eluted with 20 mM <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> in solution A</td>
    </tr>
    <tr>
      <td>MBP tag cleavage</td>
      <td>Proteolytic cleavage</td>
      <td></td>
      <td>Same as gel filtration buffer</td>
      <td>Thrombin added at 4 U per mg protein, incubated at 16 degC overnight</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (GE Healthcare)</td>
      <td>10 mM HEPES, 150 mM NaCl, pH 7.5</td>
      <td>Removed MBP tag; peak fractions of tetrameric I-II linker collected and concentrated to 4 mg/ml</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TRPML1 luminal linker at 4 mg/ml in 10 mM HEPES, 150 mM NaCl, pH 7.5</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>1.38 M <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> monobasic monohydrate, 0.42 M potassium phosphate dibasic, pH 6.0, 5% pentaerythritol ethoxylate</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>16 degC</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal form for pH 6.0 (PDB 5TJA). For pH 4.5 (PDB 5TJB), crystallized at 20 degC; for pH 7.5 (PDB 5TJC), crystallized at 20 degC.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Dual Ca2+/pH regulation via the luminal pore

TRPML1 activity is regulated by both luminal Ca2+ and H+. Ca2+ inhibits the channel in a dose-dependent manner, and this inhibition is attenuated at acidic pH (lysosomal pH 4.6). The luminal pore contains 12 aspartate residues (D111, D114, D115 per subunit) that create a highly electronegative environment. Mutating all 12 aspartates to glutamine (3DQ mutant) greatly decreased Ca2+ inhibition. Crystal structures at pH 4.5, 6.0, and 7.5 show the luminal pore is virtually unchanged across pH conditions, indicating that Ca2+ inhibition is attenuated at low pH by protonation of the luminal-pore aspartates rather than by conformational changes. This mechanism allows high TRPML1 conductance in acidic lysosomes and low conductance at the neutral extracellular pH.

### MLIV-causing missense mutations disrupt luminal domain structure

Three MLIV-causing missense mutations (L106P, C166F, T232P) are located in the luminal linker domain. L106P is at the junction of the anchoring alpha-helix and luminal pore loop; C166F disrupts an intrasubunit disulfide bond (C166-C192); T232P is on beta5 of a core beta-sheet. All three mutations cause marked changes in secondary structure, disrupt tetrameric assembly, cause protein aggregation, and prevent proper lysosomal localization. The mutant channels produce little or no current.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/">Maltose-Binding Protein (MBP)</a> — Used as N-terminal fusion tag for expression and purification of the TRPML1 luminal linker
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Used in gel filtration buffer at 10 mM, pH 7.5
- <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate Buffer</a> — Used in purification buffer at 50 mM, pH 8.0 and in crystallization reservoir at 1.38 M
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Used for solubilization of full-length TRPML1 for biochemical analyses
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/kanamycin/">Kanamycin</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> — Additive used in purification or crystallization buffers
