---
title: "HpnN Hopanoid Transporter from Burkholderia multivorans"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1073##pnas.1619660114]
verified: false
---

# HpnN Hopanoid Transporter from Burkholderia multivorans

## Overview

HpnN from *Burkholderia multivorans* is a member of the hopanoid biosynthesis-associated RND (HpnN) subfamily of transporters. It is responsible for shuttling hopanoids from the cytoplasmic membrane to the outer membrane, playing a critical role in cell wall remodeling and multidrug resistance in *Burkholderia* species, including the opportunistic pathogen *B. cepacia* complex (Bcc). The crystal structure reveals a dimeric molecule with an overall butterfly shape, where each subunit contains 12 transmembrane helices and two large periplasmic loops. Two distinct conformations (forms I and II) were captured, representing open and closed states of the transporter, suggesting a rigid-body swinging motion of the periplasmic domain drives substrate translocation.


## Publications

### doi/10.1073##pnas.1619660114

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length HpnN (877 residues)
- **Notes**: Detailed expression conditions described in SI Appendix

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
      <td>Protein purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Detailed purification protocol described in SI Appendix</td>
    </tr>
  </tbody>
</table>
**Final sample**: 20 mg/mL HpnN in 20 mM Na-Hepes pH 7.5, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>20 mg/mL HpnN in 20 mM Na-Hepes pH 7.5, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>16% <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a>, 0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 3.5, 0.2 M Li2SO4</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1 (protein:reservoir)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>25 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1 month</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> stepwise to 30%</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Form I crystals. Dimersions ~0.2 mm. SeMet-HpnN crystallized under form II conditions.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>20 mg/mL HpnN in 20 mM Na-Hepes pH 7.5, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>15% <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a>, 0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 4.0, 0.2 M (NH4)2SO4</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1 (protein:reservoir)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>25 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1 month</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> stepwise to 30%</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Form II crystals. Dimersions ~0.2 mm.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Dimeric Butterfly Architecture

HpnN forms a dimer with a butterfly shape (110 Å tall, 100 Å wide, 52 Å thick). Each protomer has 12 transmembrane helices. The dimer interface involves TMs 7-9 and several α-helices and β-strands, primarily through van der Waals interactions.

### Open and Closed Conformations

Two crystal forms capture different transient states. Form I represents an open state with an elongated channel for hopanoid transport, while form II represents a closed state. A rigid-body swinging motion of the periplasmic domain converts between these conformations.

### Proton-Relay Network

Conserved residues D344, T818, and T819 form a hydrogen-bonded triad within the transmembrane region, likely establishing a proton-relay network for energy coupling. Mutagenesis of these residues (D344Y, T818A, T819A) abolishes transporter function.

### Conserved Channel Residues

Conserved aromatic residues F117, F541, and W661 line the exit site of the channel, while L48 and L826 are critical for gating. Mutations L48F and L826F abrogate multidrug resistance.

### Role in Multidrug Resistance

HpnN is critical for mediating resistance to [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/), novobiocin, and polymyxin B in *Burkholderia*. Knockout of *hpnN* in *B. thailandensis* severely attenuates growth in the presence of these antibiotics.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/rnd-efflux-pumps/">RND Efflux Pumps</a> — HpnN is a member of the RND superfamily of transporters
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM (n-Dodecyl-β-D-Maltoside)</a> — Used for solubilization and crystallization of HpnN
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Buffer HEPES</a> — Used in purification buffer for HpnN
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> — Crystallization method used for HpnN
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/antibiotics/chloramphenicol/">Chloramphenicol</a> — Antibiotic used in selection
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component in purification or crystallization
