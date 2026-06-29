---
title: "QseE Periplasmic Sensor Domain (E. coli)"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1107##s2053230x23009123]
verified: false
---

# QseE Periplasmic Sensor Domain (E. coli)

## Overview

QseE is a histidine kinase (HK) and the sensor component of the QseE/F/G three-component system from enterohemorrhagic Escherichia coli (EHEC). It regulates virulence gene expression in response to environmental signals such as sulfate, phosphate, and host hormones ([Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) and [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/)). The crystal structure of the periplasmic sensor domain (amino acids 41-167) was determined at 1.33 Å resolution. The domain forms a four-α-helix bundle, similar to other periplasmic sensor domains of HKs such as NarX, KinB, and McpN. Conserved arginine residues (Arg70, Arg74, Arg154) at the putative dimer interface suggest QseE interacts with negatively charged ligands. Cys76 and Cys126 form a disulfide bond. The structure was solved with the aid of AlphaFold models and is monomeric in both solution and the crystal environment.

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
      <td>1.33</td>
      <td>P2_12_12_1</td>
      <td>Periplasmic domain (amino acids 41-167) of QseE from E. coli with N-terminal His-tag</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: QseE periplasmic domain (residues 41-167) with N-terminal His-tag and TEV cleavage site in pET-28a

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
      <td>E. coli cells grown at 17°C for 20 h after induction with 0.1 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a>. Cells collected by centrifugation and sonicated in buffer with protease inhibitors.</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 8.0, 200 mM NaCl, cOmplete Protease Inhibitor Cocktail</td>
      <td>Centrifugation at 20,000g for 1 h at 4°C</td>
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
      <td>Cleaved tag and undigested protein bind; flowthrough contains pure QseE</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Flowthrough fraction purified on HiLoad 16/60 <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> gel-filtration column</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM Tris-HCl pH 8.0, 100 mM NaCl</td>
      <td>Final purification step</td>
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
      <td>10 mg/mL QseE in 20 mM Tris-HCl pH 8.0, 100 mM NaCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.15 M sodium formate, 0.1 M HEPES pH 7.2, 18% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350</td>
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
      <td>Crystals also obtained in condition B (0.1 M <a href="/xray-mp-wiki/reagents/additives/sodium-malonate/">Sodium Malonate</a> pH 8.0, 0.1 M Tris pH 8.0, 30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 1000). X-ray data collected at SPring-8 BL41XU with EIGER X 16M detector at 1.0 Å wavelength.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Conserved arginine residues define the putative ligand-binding site

Three conserved arginine residues (Arg70, Arg74, Arg154) are positioned at the putative dimer interface of QseE, analogous to other HK sensor domains that bind negatively charged ligands (nitrate/nitrite for NarX, phosphate for PhoQ). This suggests QseE senses negatively charged signals such as sulfate and phosphate through electrostatic interactions with these arginine residues. Sequence alignment shows these arginines are conserved across Enterobacteriaceae.

### QseG interacts with QseE in the periplasm

QseG, an outer membrane lipoprotein, co-localizes with QseE in the periplasmic space and is required for QseE/F activity. The positively charged surface of QseE (opposite the ligand-binding site) may interact with the negatively charged C-terminal coiled-coil region (α7c) of QseG. The structural flexibility of QseG's C-terminal region, derived from weakened hydrophobic interactions in its coiled-coil interface, likely facilitates complex formation with QseE.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/qseg-outer-membrane-lipoprotein/">QseG Outer Membrane Lipoprotein</a> — QseG interacts with QseE in the periplasm to form the three-component system
- <a href="/xray-mp-wiki/concepts/miscellaneous/qse-efg-three-component-system/">QseE/F/G Three-Component System</a> — QseE is the histidine kinase sensor component of this system
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/sodium-malonate/">Sodium Malonate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/ligands/epinephrine/">Epinephrine</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/ligands/norepinephrine/">Norepinephrine</a> — Related ligand or cofactor
