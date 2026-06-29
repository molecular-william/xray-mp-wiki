---
title: "CpTRIC Channel from Clostridium perfringens"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms15103]
verified: false
---

# CpTRIC Channel from Clostridium perfringens

## Overview

CpTRIC is a Trimeric Intracellular Cation (TRIC) channel from the bacterium Clostridium perfringens. It forms a homotrimeric complex with each monomer containing seven transmembrane helices. The channel was crystallized in both native and [Selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/) (Se-Met) labeled forms at similar resolution, enabling SAD phasing. A distinctive feature of CpTRIC is the binding of Cd2+ ions at four distinct sites per protomer, including a site at the protomer interface and sites within the ion-conducting pore.


## Publications

### doi/10.1038##ncomms15103

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
      <td>2.4 A</td>
      <td>R32</td>
      <td>CpTRIC residues 1-219, wild-type, Se-Met labeled</td>
      <td>Cd2+ (4 binding sites per protomer), Se-Met for phasing</td>
    </tr>
    <tr>
      <td></td>
      <td>2.4 A</td>
      <td>R32</td>
      <td>CpTRIC residues 1-219, wild-type, Native</td>
      <td>Cd2+ (4 binding sites per protomer)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: not specified in supplementary tables
- **Construct**: CpTRIC from Clostridium perfringens. The crystallization construct covers residues 1-219, encompassing the transmembrane domain. [Selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/) (Se-Met) labeled protein was prepared for SAD phasing.


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
      <td>Protein solution</td>
      <td>not specified</td>
      <td>--</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> 20 mM pH 7.5, NaCl 200 mM + not specified</td>
      <td>Protein solution for CpTRIC crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CpTRIC residues 1-219 WT, Se-Met labeled, in <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> 20 mM pH 7.5, NaCl 200 mM</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>CpTRIC Se-Met crystal form. Wavelength 0.97876 A, space group R32, resolution ~2.4 A. Se-Met used for SAD phasing. Cd2+ bound at four distinct sites per protomer.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Cd2+ binding at four distinct sites

CpTRIC binds Cd2+ ions at four distinct sites per protomer, as revealed by anomalous diffraction at 3.5 sigma contour level. Site 1 is located near the protomer interface and involves coordination by Asp40 residues from adjacent protomers. Site 2 is involved in molecular packing in the R32 crystal lattice. Site 3 is positioned near the cytoplasmic side of the membrane, and Site 4 is located at the entrance of the ion-conducting pore near the extracellular side. The Cd2+ binding network involves specific residues that coordinate the metal ion, providing structural insight into divalent cation selectivity in TRIC channels.

### Prokaryotic TRIC structure with ion-binding sites

The CpTRIC structure (R32, 2.4 A) reveals the overall architecture of a prokaryotic TRIC channel with bound Cd2+ ions. The structure shares the characteristic 7-TM per monomer topology with SaTRIC and eukaryotic TRIC-B channels. The Cd2+ binding sites provide a model for understanding how TRIC channels discriminate between different cation species. The protomer interface site (Site 1) is particularly notable as it involves inter-protomer coordination by Asp40, suggesting that trimeric assembly is critical for metal ion binding.

### Structural comparison with SaTRIC

CpTRIC structure was superimposed onto SaTRIC (Type 2a, Na+ bound) for structural comparison. The overall fold is conserved, with the characteristic hourglass-shaped pore and 3+3+1 helix organization. The comparison reveals both conserved features of the TRIC channel fold and species-specific differences in the ion-binding environment, particularly in the pore region where different cations (Na+ in SaTRIC vs. Cd2+ in CpTRIC) occupy distinct binding sites.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/sa-tric/">SaTRIC Channel from Sulfolobus acidocaldarius</a> — Homologous prokaryotic TRIC channel; structural comparison between prokaryotic TRIC channels from different organisms
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/">C. elegans TRIC-B1 Channel</a> — Eukaryotic TRIC channel homolog; shared 7-TM hourglass architecture
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — CpTRIC crystallized by LCP method with PEG400 precipitant
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/tric-channel-gating/">TRIC Channel Gating Mechanism</a> — CpTRIC belongs to the TRIC channel family with ion-dependent gating
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — Buffer component (20 mM, pH 7.5) used in protein solution and crystallization
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine</a> — Se-Met labeled CpTRIC used for SAD phasing at 0.97876 A wavelength
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine</a> — Referenced in the context of Selenomethionine
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> — Referenced in the context of Hepes
- <a href="/xray-mp-wiki/reagents/peg400/">PEG400</a> — Referenced in the context of PEG400
