---
title: "CopA from Archaeoglobus fulgidus (AfCopA)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-022-32751-w]
verified: agent
uniprot_id: W0UUV5
---

# CopA from Archaeoglobus fulgidus (AfCopA)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/W0UUV5">UniProt: W0UUV5</a>

<span class="expr-badge">Sulfolobus monocaudavirus SMV1</span>

## Overview

CopA from Archaeoglobus fulgidus (AfCopA) is a copper-transporting P1B-type ATPase that facilitates cellular export of copper. P1B-ATPases are present in all kingdoms of life and are essential for copper homeostasis. This paper presents the first inward-facing E1 conformation structure of a P1B-ATPase at 2.7 A resolution, revealing the mechanism of Cu+ uptake from cytosolic chaperones. The structure shows a unique A-domain arrangement and identifies a methionine (M158) that plays a key role in chaperone-mediated Cu+ transfer to the transmembrane core, together with the CPC signature motif cysteines (C380, C382).


## Publications

### doi/10.1038##s41467-022-32751-w

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7roi">7ROI</a></td>
      <td>2.7</td>
      <td>Not specified</td>
      <td>AfCopA truncated construct lacking N- and C-terminal heavy metal binding domains (residues G80-G736), expressed in E. coli</td>
      <td>Cu+ (in the presence of copper)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7roh">7ROH</a></td>
      <td>3.3</td>
      <td>Not specified</td>
      <td>AfCopA truncated construct (residues G80-G736)</td>
      <td>Cu+ (data collected at copper absorption edge, 1.37 A)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7rog">7ROG</a></td>
      <td>2.8</td>
      <td>Not specified</td>
      <td>AfCopA truncated construct (residues G80-G736)</td>
      <td>Apo (no copper)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C43 strain
- **Construct**: AfCopA deltaNdeltaC (residues G80-G736, UniProtKB O29777) cloned into pET-22b(+); expression induced with 1 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg) at 20 C for 16 h
- **Induction**: 1 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg), 20 C, 16 h

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>HiLiDe (high lipid and detergent) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AfCopA at 2.25 mg/mL DOPC and 5 mg/mL <a href="/xray-mp-wiki/reagents/detergents/c12e8">Octaethylene Glycol Monododecyl Ether (C12E8)</a>, incubated 16 h at 4 C; 1 mM CuSO4 added for Cu+ bound structures</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>1.5 M ammonium <a href="/xray-mp-wiki/reagents/buffers/citrate/">citrate</a>, 0.1 M MES pH 5.5, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">Beta-Mercaptoethanol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging drop vapor diffusion</a>; 5.0 mM 06:0 Lyso PC additive used for final data collection; crystals flash-frozen in liquid nitrogen</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>pH</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Mes: 0.1 M [buffer]  
- Beta Mercaptoethanol: 5 mM [additive]</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### E1 inward-facing conformation

The AfCopA E1 structure represents the first metal-bound conformation of a P1B-ATPase. The A-domain arrangement differs from classical P2-ATPases (like SERCA), suggesting the P-type ATPase transport mechanism is less conserved than previously assumed. MA-M2 and M3-M6 form two helix bundles that shift relative to each other in the E2 to E1 transition, exposing the CPC motif of M4 to the cytoplasm.

### Chaperone-mediated copper delivery

The structure reveals a mechanism for direct Cu+ transfer from the cytosolic chaperone CopZ to the ATPase core. M158 at the MB'-M1 transition forms a transient entry site together with C380 and C382 of the CPC motif in M4. Computational docking shows CopZ fits in the groove between MB' and M2-4, with M158 conformations positioned within 6 A of the CopZ-bound Cu+ ion, enabling direct Cu+ transfer.

### CPC motif exposure in E1 state

In the E1 conformation, C380 and C382 of the conserved CPC motif in M4 are surface exposed and oriented toward M1-2 including M158, indicative of an early E1 conformation congruent with ion uptake. Molecular dynamics simulations support trigonal-planar Cu+ coordination by M158, C380, and C382 following uptake from the aqueous environment.


## Cross-References

- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a> — Purification method used in protein preparation
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography (SEC)</a> — Purification method used in protein preparation
- <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superose-6-increase">Superose 6 Increase SEC Resin</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/c12e8">C12E8</a> — Detergent used for membrane protein solubilization
- <a href="/xray-mp-wiki/reagents/buffers/tris">Tris Hcl</a> — Buffer component in purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">Beta-Mercaptoethanol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg">Iptg</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/tev-protease">Tev Protease</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for membrane protein solubilization
