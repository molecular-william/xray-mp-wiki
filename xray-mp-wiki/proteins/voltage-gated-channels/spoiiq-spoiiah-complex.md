---
title: "SpoIIQ-SpoIIIAH Intercellular Channel Complex from Bacillus subtilis"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1120087109, doi/10.1073##pnas.1120113109]
verified: agent
uniprot_id: ['P49785', 'P71044']
---

# SpoIIQ-SpoIIIAH Intercellular Channel Complex from Bacillus subtilis

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P49785">UniProt: P49785</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P71044">UniProt: P71044</a>

<span class="expr-badge">Bacillus subtilis</span>

## Overview

The SpoIIQ-SpoIIIAH complex is an intercellular channel formed between the forespore
and mother cell during endospore development in Bacillus subtilis. SpoIIQ is produced
in the forespore and consists of an N-terminal transmembrane segment and an extracellular
LytM-like domain with a degenerate zinc-metalloprotease fold. SpoIIIAH is produced in
the mother cell and consists of a transmembrane segment and an extracellular YscJ/FliF
family ring-building domain. The two proteins interact across the intercellular space
through their extracellular domains to form a heterodimer that oligomerizes into a
dodecameric (Levdikov model) or 15-18 mer (Meisner model) ring assembly surrounding
a ~58-82 A channel. This complex serves as the core component of a gap junction-like
feeding tube through which the mother cell supplies small molecules to the forespore
for late-stage gene expression during sporulation.


## Publications

### doi/10.1073##pnas.1120087109

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3tuf">3TUF</a></td>
      <td>2.75 A</td>
      <td>Not specified</td>
      <td>SpoIIQ(43-283) + SpoIIIAH(32-218) complex</td>
      <td>none (apo)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: SpoIIQ extracellular domain (residues 43-283) and SpoIIIAH extracellular domain (residues 32-218) expressed separately as recombinant proteins

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: SpoIIQ(43-283) and SpoIIIAH(32-218) with N-terminal cleavable [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/)
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/), removed by [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/) leaving residual GPA tag

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
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>Nickel affinity resin</td>
      <td>Not specified + Not specified</td>
      <td>His6-tagged proteins purified by nickel <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Proteolytic digestion</td>
      <td>Not specified</td>
      <td>Not specified + Not specified</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a> removed by <a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">HRV 3C Protease</a></td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>Superdex S200</td>
      <td>Not specified + Not specified</td>
      <td>Purification of complex by <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a>-MALLS; Superdex S200 10/300 column</td>
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
      <td>SpoIIQ(43-283)-SpoIIIAH(32-218) complex at 45 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a>, pH 4.5, 50% (vol/vol) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1 (complex:reservoir)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Large single crystals obtained. X-ray diffraction data at Diamond Light Source beamlines I04 and I02. SAD phasing at 0.9796 A using selenomethionine-derivatized SpoIIQ.</td>
    </tr>
  </tbody>
</table>
### doi/10.1073##pnas.1120113109

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3uz0">3UZ0</a></td>
      <td>2.8 A</td>
      <td>P2_12_12_1</td>
      <td>SpoIIQ(73-220) + SpoIIIAH(90-218) truncated complex</td>
      <td>none (apo)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: SpoIIQ extracellular domain (residues 43-283) and SpoIIIAH extracellular domain (residues 32-218) expressed separately as recombinant proteins

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: SpoIIQ(73-220) and SpoIIIAH(90-218) truncated constructs
- **Tag info**: Not specified

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
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>Not specified</td>
      <td>Not specified + Not specified</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a> affinity purification of truncated complex</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>Not specified</td>
      <td>Not specified + Not specified</td>
      <td>Purification of truncated SpoIIQ(73-220)-SpoIIIAH(90-218) complex</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Truncated SpoIIQ(73-220)-SpoIIIAH(90-218) complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in orthorhombic space group P2_12_12_1 with two complexes per asymmetric unit. SAD phasing at 0.979 A using <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> derivative. Data collected at NE-CAT 24-ID, Advanced Photon Source.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Intercellular channel during bacterial sporulation

The SpoIIQ-SpoIIIAH complex forms the core of an intercellular channel connecting
the forespore and mother cell during Bacillus subtilis sporulation. SpoIIQ,
expressed in the forespore, and SpoIIIAH, expressed in the mother cell, interact
across the intercellular space to form a heterodimeric complex. The structure
reveals that SpoIIIAH adopts a YscJ/FliF-like fold capable of oligomerizing into
a ring, while SpoIIQ binds to this ring via its LytM-like domain. The resulting
assembly forms a channel with an inner diameter of ~58-82 A that is thought to
allow passage of small molecules required for sigma-G activation and late-stage
forespore gene expression. This represents the first example of a gap junction-like
intercellular channel in bacteria.

### SpoIIQ adopts an inactive LytM-like metalloprotease fold

The extracellular domain of SpoIIQ adopts a LytM-like zinc-metalloprotease fold
but with an incomplete zinc coordination sphere and no bound metal. Two of the
four metal-coordinating residues conserved in active LytM proteins (Asp123,
His204, and His202) are conserved in SpoIIQ, but the other two histidines are
replaced by serines. The substrate-binding groove characteristic of active LytM
proteases is closed off in SpoIIQ by a beta2-beta3 hairpin. Consistent with
these structural observations, there is no evidence that SpoIIQ functions as a
protease. The degenerate active site and the acquisition of a SpoIIIAH-binding
beta-hairpin demonstrate how inactive enzyme homologues can acquire new functions
as binding/scaffolding proteins.

### SpoIIIAH ring-building motif homologous to type III secretion systems

SpoIIIAH adopts a wedge-shaped fold consisting of two long antiparallel alpha-helices
(alpha1 and alpha2) and a three-stranded beta-sheet, closely resembling the
ring-forming domains of YscJ/FliF family proteins from type III secretion systems
(e.g., EscJ from enteropathogenic E. coli, PDB 1YJ7). Using this structural homology,
Levdikov et al. modeled a dodecameric SpoIIIAH ring with ~58 A inner diameter,
while Meisner et al. used Rosetta docking simulations to predict 15-mer or 18-mer
rings with ~82 A inner diameter. Both models are compatible with the formation of
a channel large enough to accommodate small metabolites and multiple copies of other
integral membrane proteins encoded by the spoIIIA operon.

### Composite beta-sheet interface between SpoIIQ and SpoIIIAH

The interaction between SpoIIQ and SpoIIIAH is mediated by a beta-hairpin
(beta2-beta3) that protrudes from the N-terminal region of the SpoIIQ LytM domain.
This hairpin, stabilized by a backbone hydrogen bond between Y112 and T115, interacts
in an antiparallel manner with the C-terminal beta-strand (beta3) of SpoIIIAH,
forming a composite five-stranded beta-sheet. The interface is stabilized by both
main-chain hydrogen bonds and a hydrophobic core involving SpoIIQ residues Y96,
L109, Y116, L118 and SpoIIIAH residues A193, I197, M207, V210, V212, F214.
The degenerate active site residues of SpoIIQ (S119, D123, S169, H204) do not
participate in SpoIIIAH binding, confirming that the LytM domain has been repurposed
for a structural/scaffolding role.


## Cross-References

- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction (SAD)</a> — SAD phasing used for structure solution of the SpoIIQ-SpoIIIAH complex
- <a href="/xray-mp-wiki/methods/quality-assessment/sec-mals/">Size Exclusion Chromatography with Multi-Angle Light Scattering (SEC-MALS)</a> — SEC-MALLS used to determine oligomeric state of the complex
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Ni-NTA affinity chromatography used for initial purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a> — Gel filtration used for complex purification and SEC-MALLS analysis
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Crystallization method for the SpoIIQ-SpoIIIAH complex
- <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a> — Sodium acetate pH 4.5 used as crystallization reservoir buffer
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Nickel-NTA (Ni-NTA) Resin</a> — Nickel affinity resin used for His6-tagged protein purification
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">Polyethylene Glycol 400 (PEG400)</a> — PEG 400 used as precipitant in crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">HRV 3C Protease</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
