---
title: "Human GABA_B Receptor"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12725]
verified: false
---

# Human GABA_B Receptor

## Overview

The human GABA_B receptor (GABA_B R) is a class C G-protein-coupled receptor that functions as an obligatory heterodimer of the subunits GBR1 and GBR2. It is the metabotropic receptor for GABA (gamma-aminobutyric acid), the predominant inhibitory neurotransmitter in the central nervous system, and mediates slow and prolonged synaptic inhibition through Gi or Go proteins. GABA_B receptor malfunction is linked to neurological disorders including spasticity and epilepsy. KCTD proteins (KCTD8, KCTD12, KCTD12b, [KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16)](/xray-mp-wiki/proteins/gpcr/kctd16/)) serve as auxiliary subunits that bind to the GABA_B2 C-terminal tail and modulate signaling kinetics. Ligand binding occurs within the large extracellular Venus flytrap (VFT) module of GBR1. Crystal structures of the heterodimeric GBR1b_VFT:GBR2_VFT complex in apo, agonist-bound, and antagonist-bound forms revealed a unique activation mechanism: the apo and antagonist-bound states adopt an open-open conformation (resting state), while agonist binding induces domain closure in GBR1 alone (closed-open active state) and formation of a novel LB2-LB2 heterodimer interface between subunits.

## Publications

### doi/10.1038##nature12725

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4mqe">4MQE</a></td>
      <td>3.3</td>
      <td>I222</td>
      <td>GBR1b_VFT (residues 48-459) with N-terminal gp67 signal peptide and C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>; GBR2_VFT (residues 1-466) with C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>; expressed in Sf9 insect cells via baculovirus co-infection at 23 C for 96 h; purified from cell supernatant by anti-Flag M2 affinity and <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> gel filtration</td>
      <td>None (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4msl">4MSL</a></td>
      <td>3.3</td>
      <td>I222</td>
      <td>GBR1b_VFT (residues 48-459) with N-terminal gp67 signal peptide and C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>; GBR2_VFT (residues 1-466) with C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>; expressed and purified in presence of 10-20 uM CGP54626</td>
      <td>CGP54626</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4mr7">4MR7</a></td>
      <td>3.1</td>
      <td>P212121</td>
      <td>GBR1b_VFT (residues 48-459) with N-terminal gp67 signal peptide and C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>; GBR2_VFT (residues 1-466) with C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>; expressed and purified in presence of 100 uM (R)-baclofen</td>
      <td>(R)-Baclofen</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4mr9">4MR9</a></td>
      <td>3.2</td>
      <td>P212121</td>
      <td>GBR1b_VFT (residues 48-459) with N-terminal gp67 signal peptide and C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>; GBR2_VFT (residues 1-466) with C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>; expressed and purified in presence of 100 uM GABA</td>
      <td>GABA</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells via baculovirus co-infection (GBR1b_VFT and GBR2_VFT)
- **Construct**: GBR1b_VFT residues 48-459 with N-terminal gp67 signal peptide and C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) in pFBDM vector. GBR2_VFT residues 1-466 with C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) in pFBDM vector.

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
      <td>Co-expression</td>
      <td>Baculovirus co-infection in Sf9 insect cells at 23 C for 96 h</td>
      <td>--</td>
      <td>Not specified + --</td>
      <td>Sf9 cells co-infected with recombinant GBR1b_VFT and GBR2_VFT baculoviruses. For antagonist-bound complex, 10 uM CGP54626 present throughout expression. For agonist-bound complexes, 100 uM (R)-baclofen or GABA present throughout expression.</td>
    </tr>
    <tr>
      <td>Anti-Flag <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">flag</a> M2 antibody <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">flag</a> M2 affinity resin</td>
      <td>Not specified + --</td>
      <td>GBR1b_VFT:GBR2_VFT complex purified from cell supernatant. For antagonist-bound complex, 20 uM CGP54626 present during purification. For agonist-bound complexes, 100 uM (R)-baclofen or GABA present during purification.</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography (<a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a>, GE Healthcare)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>Not specified + --</td>
      <td>Final purification step for the heterodimeric complex.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GBR1b_VFT:GBR2_VFT complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>10% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.12 M Na acetate pH 7.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Apo and antagonist-bound complexes crystallized under the same condition. CGP54626-bound complex crystallized using protein purified in presence of CGP54626. Other antagonist complexes (CGP46381, CGP35348, SCH50911, 2-OH-saclofen, phaclofen) crystallized by co-crystallization with 10 mM antagonist. Crystals frozen directly from drops. Data collected at APS 24ID-C and 24ID-E beamlines.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>(R)-Baclofen-GBR1b_VFT:GBR2_VFT complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a>, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.2 M NH4Cl, 0.1 M Na <a href="/xray-mp-wiki/reagents/buffers/cacodylate/">Cacodylate (Sodium Dimethylarsenate)</a> pH 5.2</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in presence of 10 mM (R)-baclofen. Crystals frozen in cryoprotecting solution containing 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> plus all crystallization components. Data collected at APS 24ID-C and 24ID-E beamlines.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GABA-GBR1b_VFT:GBR2_VFT complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>18% <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.15 M NH4Cl, 0.1 M Na <a href="/xray-mp-wiki/reagents/buffers/cacodylate/">Cacodylate (Sodium Dimethylarsenate)</a> pH 5.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in presence of 10 mM GABA. Crystals frozen in cryoprotecting solution containing 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> plus all crystallization components. Data collected at APS 24ID-C and 24ID-E beamlines.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Unique heterodimer activation mechanism

GABA_B receptor exhibits a unique activation mechanism distinct from homodimeric class C GPCRs like mGluRs. While mGluRs undergo a 70 degree rotation in dimer orientation and can adopt both closed-open and closed-closed conformations, GABA_B receptor's LB1-LB1 heterodimer interface undergoes only a minor 5 degree rotation on agonist binding and adopts only a closed-open active conformation. Activation involves formation of a novel LB2-LB2 heterodimer interface that buries >1,300 A^2 of surface area, dominated by polar interactions. Disulfide crosslinking studies confirmed the LB2-LB2 interface is present in full-length native receptor, and locking this interface via disulfide crosslinking (GBR1b T198C-GBR2 Q206C) produces constitutive activity.

### GBR1 domain closure as the activation switch

Agonist binding induces a 29 degree rotation of the GBR1 LB2 domain relative to the LB1 domain about a nearly horizontal interdomain axis, closing the ligand-binding cleft. The agonist becomes buried and inaccessible to bulk solvent. Antagonists block domain closure through bulky substituents that create steric clashes with Tyr250 and Trp278, or through tetrahedral geometry of alpha-acid motifs incompatible with the active-state Tyr250 conformation. The conformational adaptability of Trp278 (170 degree indole ring flip) enables recognition of structurally different ligands (GABA vs. R-baclofen) while maintaining specificity.

### Ligand recognition by overlapping but distinct residue sets

Both agonists and antagonists are anchored in the interdomain crevice of GBR1 by an overlapping set of residues. LB1 residues (Trp65, Ser130, Gly151, Ser153, His170, Glu349) are required for both agonist and antagonist recognition. LB2 residues (Tyr250, Trp278, Ile276) are essential specifically for agonist binding - Trp278 is critical for agonist recognition but plays only an auxiliary role in antagonist binding. The antagonist binding site accommodates a wider range of chemical structures (CGP54626, CGP46381, CGP35348, SCH50911, 2-OH-saclofen, phaclofen), all derivatives of GABA with gamma-amino acid structure.

### GBR2_VFT has constitutively open conformation

GBR2_VFT remains open in all states (apo, antagonist-bound, and agonist-bound), consistent with its constitutively open conformation. Although GBR2 does not bind any known GABA_B ligand, its ectodomain directly interacts with the GBR1 ectodomain to enhance agonist affinity. On agonist binding, the GBR2 LB2 domain undergoes a 9 degree twist motion around a nearly vertical axis, moving toward the GBR1 LB2 domain to form new heterodimeric contacts. The C-terminal distance between subunits shortens from 45 A (apo) to 32 A (agonist-bound), which may alter the relative orientation of the transmembrane domains for G protein coupling.

### KCTD16 auxiliary subunit binds GABA_B2 C-terminus

[KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16)](/xray-mp-wiki/proteins/gpcr/kctd16/) T1 domain forms an open pentamer that binds a single GABA_B2 C-terminal peptide (residues 895-909) within its interior. Key interfacial residues include F80 (from four [KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16)](/xray-mp-wiki/proteins/gpcr/kctd16/) subunits), Q34, and E102, which form hydrophobic and hydrogen-bonding interactions with GABA_B2 residues including Y903. Mutation of these interfacial residues disrupts both biochemical association and functional modulation of GIRK channel activation. This binding mode is conserved among all GABA_B-associated KCTD proteins (KCTD8, KCTD12, KCTD12b, [KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16)](/xray-mp-wiki/proteins/gpcr/kctd16/)).


## Cross-References

- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/gabar-b3/">Human GABA_A Receptor Beta-3 Subunit</a> — Related GABA receptor; GABA_A is an ion channel, GABA_B is a GPCR
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr/">G Protein-Coupled Receptor (GPCR)</a> — GABA_B R is a class C GPCR that functions as an obligatory heterodimer
- <a href="/xray-mp-wiki/reagents/ligands/baclofen/">Baclofen</a> — Selective GABA_B agonist used clinically to treat muscle spasticity
- <a href="/xray-mp-wiki/reagents/ligands/gaba/">GABA</a> — Endogenous agonist for GABA_B receptor
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression</a> — Expression system used for GBR1b_VFT and GBR2_VFT in Sf9 cells
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/gpcr/kctd16/">KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16)</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a> — Additive used in purification or crystallization buffers
