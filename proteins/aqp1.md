---
title: Aquaporin-1 (AQP1)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##414872a]
verified: false
---

# Aquaporin-1 (AQP1)

## Overview

Aquaporin-1 (AQP1) is a water-selective channel protein from bovine red blood cells that facilitates rapid water transport across cell membranes in response to osmotic gradients. AQP1 forms functional tetramers, with each monomer containing six transmembrane helices and two membrane-inserted non-membrane-spanning helices. The high-resolution structure reveals a dumbbell-shaped pore with an extracellular vestibule, a narrow selectivity filter containing the constriction region, and a cytoplasmic vestibule. Four water molecules are bound within the selectivity filter at three hydrophilic nodes, and the constriction region residues H182, R197, and F58 establish water specificity while energetically preventing proton transport.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##414872a | 1J4N | 2.2 A | I422 | Full-length bovine AQP1 | Three nonylglucoside detergent molecules |

## Expression and Purification

- **Expression system**: Not specified in this paper
- **Construct**: Full-length bovine AQP1

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Membrane solubilization | -- | -- + Nonylglucoside | Native membrane protein solubilized for crystallization; details described in reference 27 |


## Crystallization

### doi/10.1038##414872a

| Parameter | Value |
|---|---|
| Method | Co-crystallization with thallium heavy atom |
| Protein sample | Native bovine AQP1 |
| Reservoir | Not specified in detail; native crystals obtained as described in reference 27 |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Native crystals obtained as described previously (reference 27). Co-crystallization with thallium yielded thallium-derivatized crystals suitable for MAD phasing. Space group I422, unit cell a = b = 93.3 A, c = 180.5 A, one molecule per asymmetric unit. Best crystals diffracted to 2.1 A. |


## Biological / Functional Insights

### Pore architecture and water-specific selectivity mechanism

The AQP1 pore is dumbbell-shaped with three elements: an extracellular vestibule (~15 A diameter mouth), a ~20 A-long selectivity filter, and a cytoplasmic vestibule (~15 A diameter mouth). The constriction region at ~2.8 A diameter is formed by H182 (imidazole ring extended into pore), R197 (pointed upward parallel to pore axis), F58 (hydrophobic face), and the backbone carbonyl oxygen of C191. These four residues establish steric and chemical criteria for water selectivity. About half the pore wall is hydrophobic and half hydrophilic; the hydrophilic face provides hydrogen-bond-forming groups that replace hydration shell waters of water molecules during transit.

### Four bound waters at three hydrophilic nodes

Four water molecules are localized within the selectivity filter at three hydrophilic nodes. Water 1 is adjacent to the constriction region, coordinated by H182 epsilon2 nitrogen and G192 backbone carbonyl. Waters 2 and 3 are centered about the pseudo two-fold axis, hydrogen-bonded to N194 and N78 asparagine side chains respectively. Water 4 is near the cytoplasmic end, coordinated by H76 and A75 backbone carbonyl oxygens. Only the middle two waters form a water-water hydrogen bond; the hydrophobic pore segments prevent a contiguous hydrogen-bonded chain.

### Proton exclusion mechanism

Proton transport through AQP1 is highly energetically unfavorable. The positive helical dipole ends of M3 and M7 helices (pointing into the pore) disrupt water dipole alignment needed for Grotthuss proton-wire mechanism. Additionally, R197 (near constriction), the amine groups of N78 and N194 (at the pseudo two-fold axis), and histidines H182 and H76 (at opposite ends of the selectivity filter) create repulsive forces against positively charged ions. Negatively charged ions experience repulsion from pore-accessible carbonyl oxygen atoms lining the selectivity filter.

### Structural comparison with GlpF glycerol facilitator

The constriction region of AQP1 is approximately 1 A narrower than that of GlpF. In GlpF, H182 of AQP1 is replaced by glycine, and C191 is replaced by phenylalanine. These substitutions increase the constriction size and hydrophobicity, allowing glycerol passage. In AQP1, H182 is critical for water specificity and is conserved across all water-specific aquaporins. The aromatic/arginine (ar/R) selectivity filter motif (H182-R197) is a defining feature of water-specific aquaporins.


## Cross-References

- [Glycerol Facilitator (GlpF)](/xray-mp-wiki/proteins/glycerol-facilitator/) — E. coli glycerol facilitator used as structural comparison; GlpF constriction region is wider and more hydrophobic to accommodate glycerol
- [Aquaporin Family](/xray-mp-wiki/concepts/aquaporin/) — AQP1 is the archetypal water-specific aquaporin; structure reveals fundamental selectivity mechanism of the superfamily
- [Aquaporin Z (AqpZ)](/xray-mp-wiki/proteins/aquaporin-z/) — Bacterial homolog of AQP1 from E. coli; shares conserved water channel architecture
- [Multi-Wavelength Anomalous Diffraction (MAD)](/xray-mp-wiki/methods/structure-determination/multi-wavelength-anomalous-diffraction/) — MAD phasing with thallium heavy-atom derivative was used to solve the AQP1 structure
