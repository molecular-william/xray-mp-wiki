---
title: "Human Nav1.7 Voltage-Gated Sodium Channel"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aac5464]
verified: agent
---

# Human Nav1.7 Voltage-Gated Sodium Channel

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span> <span class="expr-badge expr-mammalian">Mammalian</span></div>


## Overview

Nav1.7 (encoded by SCN9A) is a voltage-gated sodium channel isoform highly expressed in peripheral nervous system neurons, particularly in dorsal root ganglion and olfactory epithelium. It plays a central role in pain perception: gain-of-function mutations cause extreme pain disorders, while loss-of-function mutations cause congenital insensitivity to pain. Nav1.7 is a validated target for analgesic drug development. The first X-ray crystal structure of the Nav1.7 VSD4 (voltage-sensor domain IV) was determined as a chimera fused onto the bacterial [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) channel, revealing the binding mode of isoform-selective aryl sulfonamide antagonists that trap VSD4 in an activated conformation.


## Publications

### doi/10.1126##science.aac5464

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ek0">5EK0</a></td>
      <td>3.53</td>
      <td>—</td>
      <td>Nav1.7 VSD4-<a href="/xray-mp-wiki/proteins/voltage-gated-channels/navab/">NAVAB</a> chimeric channel — human Nav1.7 VSD4 (S1-S4, residues 1525-1625) grafted onto bacterial <a href="/xray-mp-wiki/proteins/voltage-gated-channels/navab/">NAVAB</a> channel scaffold</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/gx-936/">GX-936</a> (aryl sulfonamide antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ek0">5EK0</a></td>
      <td>3.85</td>
      <td>—</td>
      <td>Nav1.7 VSD4-<a href="/xray-mp-wiki/proteins/voltage-gated-channels/navab/">NAVAB</a> with GX-629 (brominated analog for SAD phasing)</td>
      <td>GX-629</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ek0">5EK0</a></td>
      <td>4.35</td>
      <td>—</td>
      <td>Nav1.7 VSD4-<a href="/xray-mp-wiki/proteins/voltage-gated-channels/navab/">NAVAB</a> (selenomethionine-incorporated, 5 Met landmarks)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/gx-936/">GX-936</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293 cells (mammalian expression)
- **Construct**: Nav1.7 VSD4-[NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) chimera with grafted human Nav1.7 VSD4 residues (S1-S4, residues 1525-1625)
- **Notes**: Exploiting evolutionary relationship between human and bacterial Nav channels. The chimera preserved high-affinity antagonist binding as confirmed by radioligand binding and alanine-scanning mutagenesis.

**Purification:**

- **Expression system**: HEK293 cells
- **Expression construct**: Nav1.7 VSD4-[NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) chimeric protein

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
      <td>Cell culture and expression</td>
      <td>Transient transfection of HEK293 cells</td>
      <td>—</td>
      <td></td>
      <td>Protein production for crystallization studies</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Affinity and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>Not specified in main text</td>
      <td>Not specified in main text + Not specified in main text</td>
      <td>Standard membrane protein purification protocol</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle Crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Nav1.7 VSD4-<a href="/xray-mp-wiki/proteins/voltage-gated-channels/navab/">NAVAB</a> chimera</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown from PC-based bicelle system. <a href="/xray-mp-wiki/reagents/ligands/gx-936/">GX-936</a>, GX-629, or GX-674 included for cocrystallization. Data collected at Br absorption edge (0.9199 A) for SAD phasing with GX-629. SeMet protein used for landmarking.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Aryl sulfonamides trap Nav1.7 VSD4 in activated state via voltage-sensor trapping mechanism

[GX-936](/xray-mp-wiki/reagents/ligands/gx-936/) and related aryl sulfonamide antagonists bind to VSD4 only when the voltage-sensor domain is in its activated conformation (depolarized membrane potential). The anionic aryl sulfonamide warhead directly engages the R4 gating charge (R1608) through a bidentate salt bridge, effectively trapping VSD4 in the activated state. This prevents VSD4 deactivation, stabilizes inactivated channel states, and thereby inhibits Nav1.7 with extreme state dependence (IC50 0.1 nM at -40 mV vs 240 nM at -120 mV).

### Isoform selectivity determined by S2 and S3 helix residues

Isoform selectivity of aryl sulfonamide inhibitors is achieved through interactions with nonconserved residues on the S2 and S3 helices of VSD4. Key selectivity motifs were identified: YWxxV on S2 (Y1537, W1538) and GMxxA on S3 (G1581, M1582, A1585). The selectivity pocket distinguishes Nav1.7 from other isoforms like Nav1.5 (cardiac) where GX-674 shows 100,000-fold selectivity.

### Phospholipids form a tripartite complex with antagonist and VSD4

Bound [Phosphatidylcholine](/xray-mp-wiki/reagents/lipids/phosphatidylcholine/) (PC) molecules were observed in the structure, with one lipid (PC2) directly buttressing the [GX-936](/xray-mp-wiki/reagents/ligands/gx-936/) binding site. This peripherally bound lipid covers ~200 A^2 of [GX-936](/xray-mp-wiki/reagents/ligands/gx-936/) surface and forms specific interactions with S2 and S3 helix residues (E1534 and D1586). The observation of a lipid-antagonist-VSD4 ternary complex suggests that membrane lipids can directly modulate the VSD4 receptor site.

### VSD chimeric engineering strategy for crystallography

A novel protein-engineering strategy was devised by exploiting the evolutionary relationship between human and bacterial Nav channels. The human Nav1.7 VSD4 (S1-S4) was grafted onto the bacterial [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) channel scaffold, creating a functional chimeric channel that preserved the antagonist binding site. This approach overcame the technical complexity of producing full-length human Nav channels for crystallographic studies.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/gx-936/">GX-936</a> — Co-crystallized aryl sulfonamide antagonist that traps Nav1.7 VSD4 in activated state
- <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle Crystallization</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/navab/">NAVAB</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylcholine/">Phosphatidylcholine</a> — Additive used in purification or crystallization buffers
