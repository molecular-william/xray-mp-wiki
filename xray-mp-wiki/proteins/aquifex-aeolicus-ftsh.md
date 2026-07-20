---
title: "FtsH from Aquifex aeolicus (A. aeolicus AAA Protease)"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [membrane-protein, enzyme, xray-crystallography]
sources: [doi/10.1107##s1399004715005945]
verified: agent
uniprot_id: O67077
---

# FtsH from Aquifex aeolicus (A. aeolicus AAA Protease)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O67077">UniProt: O67077</a>

<span class="expr-badge">Aquifex aeolicus</span>

## Overview

FtsH is a universally conserved [ATP](/xray-mp-wiki/reagents/ligands/atp/)-dependent zinc metalloprotease found in eubacteria,
mitochondria and chloroplasts. It belongs to the AAA+ (ATPases associated with various cellular
activities) family and degrades both membrane-bound and soluble protein substrates. FtsH is a
membrane-anchored hexameric protease where each polypeptide chain contains two N-terminal
transmembrane helices, followed by cytosolic AAA and protease domains. The crystal structure
of a truncated soluble quadruple mutant (Delta-AaFtsH, residues 142-634) from Aquifex aeolicus
was determined in the [ADP](/xray-mp-wiki/reagents/ligands/adp/)-bound state at 2.96 A resolution (PDB 4ww0), revealing a C2-symmetric
AAA ring arrangement distinct from the Thermotoga maritima FtsH structure. The protease ring
exhibits sixfold symmetry and is identical to other FtsH structures. The AAA domains in a
related crystal form are highly disordered (PDB 4z8x at 3.25 A), highlighting their flexibility.
The active-site switch beta-strand in the protease domain was found to be critical for
proteolytic activity, and a conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) in the linker between [AAA](/xray-mp-wiki/reagents/ligands/aaa/) and protease domains
(Gly399) is essential for FtsH function.

## Publications

### doi/10.1107##s1399004715005945

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ww0">4WW0</a></td>
      <td>2.96</td>
      <td>I222</td>
      <td>Delta-AaFtsH (residues 142-634 with mutations I250M, F360L, K552R, E627G; N-terminal His tag cleaved</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4z8x">4Z8X</a></td>
      <td>3.25</td>
      <td>I222</td>
      <td>Delta-AaFtsH (residues 142-634 with mutations I250M, F360L, K552R, E627G</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21 (DE3 CodonPlus
- **Construct**: Truncated A. aeolicus FtsH (residues 142-634 with N-terminal thrombin-cleavable hexahistidine tag. Contains four mutations: I250M, F360L, K552R, E627G
- **Notes**: Expression was induced with 1 mM IPTG at OD600 0.8-1.0, grown overnight at 22 C. Purified by Ni-NTA affinity chromatography, Resource Q anion-exchange chromatography, and Superdex 200 size-exclusion chromatography. His tag cleaved with thrombin before SEC.

**Purification:**

- **Expression system**: E. coli BL21 (DE3 CodonPlus
- **Expression construct**: Delta-AaFtsH (142-634 with N-terminal thrombin-cleavable His tag
- **Tag info**: N-terminal hexahistidine tag, cleaved by thrombin

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
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French press</a> (3 passages at 6.9 MPa</td>
      <td>—</td>
      <td>20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> Propane-HCl pH 8.0, 300 mM NaCl, 0.02% NaN3</td>
      <td><a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>-</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) (Qiagen</td>
      <td>20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> Propane-HCl pH 8.0, 300 mM NaCl, 0.02% NaN3</td>
      <td></td>
    </tr>
    <tr>
      <td>Anion-exchange chromatography</td>
      <td>Ion-exchange</td>
      <td>Resource Q (GE Healthcare</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>His tag cleavage</td>
      <td>Thrombin digestion overnight at 4 C</td>
      <td>—</td>
      <td>20 mM Tris-HCl pH 8.0, 100 mM NaCl, 0.02% NaN3</td>
      <td>Followed by another <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) step to remove uncleaved</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td>Superdex S200 16/600 (GE Healthcare</td>
      <td>20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> Propane-HCl pH 8.0, 100 mM NaCl, 0.02% NaN3</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a> (<a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting drop</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Δ-AaFtsH at 10 mg/mL in 20 mM Tris-HCl pH 8.0, 100 mM NaCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M CaCl2, 0.1 M MES pH 6.0, 20% Pegg 6000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified (</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of form X1 appeared initially. After several months, smaller of form X2 (shrunken c-axis appeared alongside. X2 has ordered <a href="/xray-mp-wiki/reagents/ligands/aaa/">AAA</a> [</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### C2-symmetric AAA ring with ADP-bound state

The AAA domains assemble into a ring with C2 symmetry, in contrast to the sixfold symmetry of the protease ring. The breakdown of symmetry arises from different interdomain angles between the protease and AAA domains in the three crystallographically independent monomers. The domains move as rigid bodies by ~30 degrees rotation, with the hinge region around residues 400-410 in the linker. Unlike the T. maritima FtsH structure where rotations are mainly perpendicular to the protease ring (closure), the A. aeolicus FtsH shows more lateral (twisting) movements, resulting in a qualitatively different AAA ring arrangement.

### Closed pore and contiguous phenylalanine path

The pore in the A. aeolicus FtsH structure is completely closed. The pore phenylalanine residues (Phe228, part of the 228FGV motif) are partially disordered but line a contiguous funnel-shaped path. Compared to the T. maritima FtsH structure, the aromatic side chains are more buried inside the cleft, and inter-subunit contacts are tighter.

### Active-site switch beta-strand is critical for proteolytic activity

A conserved beta-strand (the active-site switch) covering the active site alpha-helix is disordered in all three copies of the A. aeolicus FtsH structure. This segment functions as an edge strand for substrate docking. The T450P mutation in this segment within the full-length FtsH severely impaired proteolytic activity while retaining ATPase activity, confirming its functional importance. The 'lid-helix' interpretation in the T. thermophilus FtsH structure is problematic due to model bias and flawed refinement data.

### Conserved glycine in AAA-protease linker is essential

An absolutely conserved glycine residue (Gly399 in A. aeolicus and T. thermophilus FtsH) in the linker region between the AAA and protease domains is crucial for FtsH activity. The G399L mutation in T. thermophilus FtsH causes the protein to elute exclusively as a monomer and eliminates both ATPase and proteolytic activity. This glycine provides the necessary flexibility for interdomain communication.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/">Bovine F1-ATPase (azide-inhibited form)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase-stator-complex/">Bovine Mitochondrial F1-ATPase-</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/other-ion-channels/gluN1-gluN2b-nmda-receptor/">GluN1-GluN2B NMDA Receptor (Xenopus laevis, Full-Length)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/rhodopsins/gtacr1/">GtACR1 Anion Channelrhodopsin from Guillardia theta</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mscs/">E. coli MscS (Mechanosensitive Channel of Small Conductance)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/abc-transporters/msba/">MsbA Lipid A Flippase</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mscs-a106v/">E. coli MscS Mechanosensitive Channel (A106V Open Form)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/gpcr/trex1/">Mouse TREX1 (Three Prime Repair Exonuclease 1)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/miscellaneous/rocker/">Rocker — De Novo Designed Zn²⁺ Transporter</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/concepts/miscellaneous/inducer-exclusion/">Inducer Exclusion</a> — Related concept; referenced in text
