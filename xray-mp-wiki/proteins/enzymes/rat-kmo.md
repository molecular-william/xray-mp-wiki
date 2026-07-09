---
title: "Rat Kynurenine 3-Monooxygenase (Rat KMO)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s42003-021-01666-5]
verified: regex
---

# Rat Kynurenine 3-Monooxygenase (Rat KMO)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


## Overview

Rat Kynurenine 3-monooxygenase (KMO) from Rattus norvegicus is a class A flavoprotein
monooxygenase and a single-pass transmembrane mitochondrial enzyme that catalyses
the hydroxylation of L-kynurenine to 3-hydroxykynurenine (3-HK) in the eukaryotic
tryptophan catabolic (kynurenine) pathway. Despite predictions suggesting two
transmembrane domains, the full-length crystal structure revealed KMO is actually
a single-pass transmembrane protein, with the other predicted transmembrane domain
lying laterally along the membrane where it forms part of the ligand-binding pocket.
KMO functions as a dimer and is linked to various neurological disorders including
Huntington's disease, pain, and neurodegenerative conditions. The structure was
determined in its membrane-embedded form using [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)
(in meso) crystallization, complexed with potent inhibitors identified through
medicinal chemistry and DNA-encoded chemical library screening.


## Publications

### doi/10.1038##s42003-021-01666-5

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/not explicitly stated in raw paper">NOT EXPLICITLY STATED IN RAW PAPER</a></td>
      <td>3.0</td>
      <td>C 1 2 1</td>
      <td>Full-length Rat KMO (residues 1-478), N-terminal GST-tag with thrombin cleavage site, C-terminal <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> site followed by <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG tag</a></td>
      <td>Compound 3 (KMO inhibitor) and FAD cofactor</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/not explicitly stated in raw paper">NOT EXPLICITLY STATED IN RAW PAPER</a></td>
      <td>3.0</td>
      <td>C 1 2 1</td>
      <td>Full-length Rat KMO (residues 1-478), N-terminal GST-tag with thrombin cleavage site, C-terminal <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> site followed by <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG tag</a></td>
      <td>Compound 4 (KMO inhibitor from DNA-encoded chemical library) and FAD cofactor</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 cells (Bac-to-Bac Baculovirus Expression System)
- **Construct**: Full-length KMO (1-478) with N-terminal GST-tag (thrombin-cleavable) and
C-terminal [TEV](/xray-mp-wiki/reagents/additives/tev-protease/)-[FLAG tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/)

- **Notes**: Sf9 cells infected at 2-3 x 10^6 cells/mL with baculovirus MOI of 0.1,
grown at 27°C, collected 2 days post-infection


**Purification:**

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus)
- **Expression construct**: GST-thrombin-KMO-[TEV](/xray-mp-wiki/reagents/additives/tev-protease/)-[FLAG tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) (full-length 1-478)
- **Tag info**: N-terminal GST (thrombin-cleavable), C-terminal [FLAG tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) ([TEV](/xray-mp-wiki/reagents/additives/tev-protease/)-cleavable)

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
      <td>Cell disruption and solubilization</td>
      <td>Sonication</td>
      <td>--</td>
      <td>20 mM potassium phosphate pH 7.5, 10% glycerol, 300 mM NaCl, 7 mM 2-mercaptoethanol, 50 µM FAD, protease inhibitors + 0.5% n-dodecyl β-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Cells disrupted by sonication in lysis buffer; insoluble debris removed by centrifugation</td>
    </tr>
    <tr>
      <td>Glutathione <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Batch purification</td>
      <td>Glutathione Sepharose 4 Fast Flow (GE Healthcare)</td>
      <td>20 mM potassium phosphate pH 7.5, 10% glycerol, 300 mM NaCl + 0.012% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Resin washed with same buffer; eluted with 33 mM glutathione</td>
    </tr>
    <tr>
      <td>Buffer exchange and concentration</td>
      <td>Ultrafiltration</td>
      <td>AmiconUltra-15 Centrifugal Filters 50k (Millipore)</td>
      <td>20 mM potassium phosphate pH 7.5, 10% glycerol, 300 mM NaCl + 0.012% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Concentrated, then desalted via PD-10 (GE Healthcare) to remove glutathione</td>
    </tr>
    <tr>
      <td>Thrombin digestion</td>
      <td>Proteolytic tag removal</td>
      <td>--</td>
      <td>Not specified + Not specified</td>
      <td>Digested with thrombin (Novagen) at 10 U/mg at 4°C to remove GST tag</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase</a> (in meso) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified Rat KMO after thrombin cleavage, in complex with compound 3</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
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
      <td>Structure determined at 3.0 A resolution. Space group C 1 2 1, cell dimensions: a=160.97, b=63.43, c=152.42 A, beta=113.5 deg. Two structures solved: complex with compound 3 and complex with compound 4.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase</a> (in meso) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified Rat KMO after thrombin cleavage, in complex with compound 4</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
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
      <td>Structure determined at 3.0 A resolution. Space group C 1 2 1, cell dimensions: a=161.51, b=63.42, c=152.66 A, beta=113.4 deg.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Single-pass transmembrane architecture

Despite computational predictions suggesting two transmembrane domains, the
crystal structure revealed that KMO is a single-pass transmembrane protein.
The second predicted transmembrane segment (alpha-12) lies laterally along the
membrane surface and forms part of the ligand-binding pocket. Electrostatic
potential and hydrophobicity analysis confirmed the non-polar surface of the
alpha-12 helix is partially embedded in the membrane.

### KMO functions as a physiological dimer

The crystal structure reveals a dimeric arrangement with 10 inter-beta-sheet
hydrogen bonds linking protomers. NanoBRET measurements in HEK293T cells
confirmed dimerization of human KMO at the cellular level. Mutations at the
dimer interface (D184A, Y185P, Q187A) significantly reduced BRET signal and
abolished catalytic activity, confirming the functional unit of KMO is a dimer.

### Ligand-binding pocket architecture

The ligand-binding pocket features a polar side (interacting with R85) and a
hydrophobic side. The carboxylic acid moiety of inhibitors fits into the polar
side, while hydrophobic regions engage the opposite side. The alpha-12 helix
contributes to the binding pocket. Compound 4 binding induced a conformational
change in Y398, which flips to accommodate the methyl group and isoindoline
ring of compound 4.

### Brain-penetrant inhibitor design

Replacing the carboxylic acid moiety of compound 3 yielded compound 5, which
showed significantly improved brain penetration (Kp,brain = 0.80) compared to
compound 1 (Kp,brain = 0.029). Compound 5 achieved 6025 ng/g in brain tissue
versus 7560 ng/mL in plasma. This bioisosteric approach enables targeting of
KMO for neurological indications where blood-brain barrier penetration is critical.


## Cross-References

- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — KMO was crystallized in meso (lipidic cubic phase) for structure determination
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> — KMO was expressed in Sf9 insect cells using the Bac-to-Bac baculovirus system
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — [DDM](/xray-mp-wiki/reagents/detergents/ddm/) used for membrane protein solubilization and throughout purification
- <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> — C-terminal [FLAG tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) used in KMO expression construct
- <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> — [TEV](/xray-mp-wiki/reagents/additives/tev-protease/) cleavage site included between KMO and C-terminal [FLAG tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/)
