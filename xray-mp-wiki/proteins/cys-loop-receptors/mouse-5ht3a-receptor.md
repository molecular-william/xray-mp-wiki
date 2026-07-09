---
title: "Mouse 5-HT3A Receptor"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13552]
verified: regex
uniprot_id: P09874
---

# Mouse 5-HT3A Receptor

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P09874">UniProt: P09874</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The mouse [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) 5-HT3A receptor is a pentameric ligand-gated ion channel (pLGIC) belonging to the Cys-loop receptor superfamily. It mediates fast excitatory neurotransmission in the central and peripheral nervous systems. This page covers the first high-resolution X-ray crystal structure of a mammalian Cys-loop receptor, solved at 3.5 Å resolution in complex with the [VHH15 Nanobody](/xray-mp-wiki/reagents/antibodies/vhh15/). The structure reveals the complete architecture including part of the intracellular domain, providing key insights into ion permeation, neurotransmitter binding, and the gating mechanism of serotonin-gated channels.


## Publications

### doi/10.1038##nature13552

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4hhz">4HHZ</a></td>
      <td>3.5</td>
      <td>P2₁2₁2₁</td>
      <td>residues 9-275, 280-334, 399-459 with N-terminal Strept-tag (trypsin-split construct)</td>
      <td><a href="/xray-mp-wiki/reagents/antibodies/vhh15/">VHH15 Nanobody</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: T-REX-293 (human embryonic kidney 293 derivative)
- **Construct**: N-terminal Strept-tag with TEV cleavage site, mouse 5-HT3A subunit

**Purification:**

- **Expression system**: T-REX-293
- **Expression construct**: N-terminal Strept-tag with TEV cleavage site

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
      <td>Cell culture</td>
      <td>Suspension culture</td>
      <td>—</td>
      <td></td>
      <td>Serum-free, orbital agitation, 4 L culture volume</td>
    </tr>
    <tr>
      <td>Protein induction</td>
      <td>Chemical induction</td>
      <td>—</td>
      <td></td>
      <td>4 µg/mL tetracycline and 4 mM <a href="/xray-mp-wiki/reagents/additives/sodium-butyrate/">Sodium Butyrate</a> at 4×10^6 cells/mL</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Centrifuration</td>
      <td>—</td>
      <td></td>
      <td>Ultra-Turrax T25 disruption, 100,000g for 45 min</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM Tris pH 7.4, 500 mM NaCl + 1% <a href="/xray-mp-wiki/reagents/detergents/c12e9/">C12E9</a></td>
      <td>2 h solubilization</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Streptactin affinity</td>
      <td>Streptactin Superflow (IBA)</td>
      <td>50 mM Tris pH 7.4, 125 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/c12e9/">C12E9</a></td>
      <td>Wash with buffer A, elute with 5 mM D-<a href="/xray-mp-wiki/reagents/ligands/desthiobiotin/">Desthiobiotin</a></td>
    </tr>
    <tr>
      <td>Deglycosylation</td>
      <td>Enzymatic treatment</td>
      <td>—</td>
      <td></td>
      <td>PNGase F, 5 units/µg, 2 h at 37°C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/limited-proteolysis/">Limited Proteolysis</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> digestion</td>
      <td>—</td>
      <td></td>
      <td>1 µg <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> per 80 µg receptor, 2 h at 30°C</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>Superose 6 column (GE Healthcare)</td>
      <td>50 mM Tris pH 7.4, 125 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/c12e9/">C12E9</a></td>
      <td>Pentameric receptor-detergent complex pooled</td>
    </tr>
  </tbody>
</table>
**Final sample**: ~4 mg/mL in 50 mM Tris pH 7.4, 125 mM NaCl, 0.02% [C12E9](/xray-mp-wiki/reagents/detergents/c12e9/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>5-HT3 receptor-<a href="/xray-mp-wiki/reagents/antibodies/vhh15/">VHH15 Nanobody</a> complex (~4 mg/mL) with 0.56 mM <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20-25% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 10000, 0.1 M Na2SO4, 0.1 M Tris pH 8.5</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-5 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> or 40% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 10000 in mother solution</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Recombination in SUVs with <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a>:<a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> (8.75:1:2.5) before complex formation with <a href="/xray-mp-wiki/reagents/antibodies/vhh15/">VHH15 Nanobody</a></td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Ion Permeation Pathway

The structure reveals a 60-Å high and 20-Å wide extracellular vestibule with a constriction at residues D105 and K108 of loop β4-β5. The M2 helices line the ~40-Å-long transmembrane pore, with hydrophobic residues at positions 16', 13', and 9' defining a funnel. A 4.6-Å hydrophobic constriction is located at L9' (L260). Below the constriction, the vestibule exhibits an electronegative surface that increases local cation concentration.

### Intracellular Domain Architecture

The intracellular domain comprises post-M3 loops, MX helices, and MA helices forming a tight bundle. The MA helices create a closed vestibule where lateral portals are obstructed by the post-M3 loops, leaving only a narrow tunnel (3.3 Å at thinnest). A tight hydrophobic juncture at the bottom of the MA helices (L402, L406, I409, L413) creates a 17-Å-long zone with minimum diameter of 4.2 Å. This structure does not offer an exit pathway for ions, suggesting conformational changes are required for ion exit during gating.

### Conductance-Defining Arginine Triplet

Three arginine residues (R416, R420, R424) in helix MA of the A subunit are responsible for the low conductance of homomeric 5-HT3A receptors (0.4 pS vs. 16 pS for heteromeric AB receptors). R416 faces the pore lumen; R420 is within salt-bridge distance to D312; R424 is exterior to the post-M3 loop. These arginines are surrounded by negatively charged residues (E414, D417, E418, E421, D425) creating a ladder of negative charges along the outer face of the MA helix.

### Neurotransmitter Binding Site

Each of the five equivalent [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) binding sites is located between two subunits in an electronegative cleft. Loops A, B, and C from the principal subunit and portions of β-strands D, E, G and loop F from the complementary subunit contribute to the site. The binding site is capped by the [VHH15 Nanobody](/xray-mp-wiki/reagents/antibodies/vhh15/), which binds at the subunit interfaces with sub-nanomolar affinity. Loop C adopts an extended conformation, intermediate between the contracted (agonist-bound) and open (antagonist-bound) states.

### Interface and Quaternary Structure

The pre-M1 loop arginine R218 is surrounded by negatively charged residues E53 (β1-β2 loop), D145 (Cys-loop), and E186 (β8-β9 loop), forming a charged sandwich with the conserved aromatic residue W187. This arrangement is conserved among Cys-loop receptors and may indicate the channel state. The Cys-loop penetrates into the four-helix bundle of the transmembrane domain. The M1 helix is broken at conserved proline P230, providing flexibility to the extracellular domain orientation relative to the transmembrane domain.


## Cross-References

- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC</a> — Bacterial pLGIC homolog used as search model for molecular replacement; structure comparison shows 5-HT3A is intermediate between open and closed states
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/glic/">GLIC</a> — Prokaryotic pLGIC homolog; M2 helix bundle in 5-HT3A resembles open GLIC conformation
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/glucl/">GluCl</a> — C. elegans pLGIC homolog; used in structural superposition to trace closed-to-open conformational trajectory
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/acetylcholine-binding-protein/">Acetylcholine-Binding Protein (AChBP)</a> — Soluble surrogate for Cys-loop receptor extracellular domains; used to explore binding site anatomy
- <a href="/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/">Cys-Loop Receptor Family</a> — 5-HT3A belongs to the Cys-loop receptor superfamily of pentameric ligand-gated ion channels
- <a href="/xray-mp-wiki/reagents/antibodies/vhh15/">VHH15 Nanobody</a> — Llama-derived nanobody used as crystallization chaperone; binds with sub-nanomolar affinity to stabilize non-conducting state
- <a href="/xray-mp-wiki/reagents/detergents/c12e9/">C12E9 (Nonyl Glucoside)</a> — Nonionic detergent used for solubilization of membrane fractions containing the 5-HT3A receptor
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/limited-proteolysis/">Limited Proteolysis</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
