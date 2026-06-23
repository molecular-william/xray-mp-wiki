---
title: Human GABA_B Receptor
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1903024116, doi/10.1038##nature12725]
verified: false
---

# Human GABA_B Receptor

## Overview

The human GABA_B receptor (GABA_B R) is a class C G-protein-coupled receptor that functions as an obligatory heterodimer of the subunits GBR1 and GBR2. It is the metabotropic receptor for GABA (gamma-aminobutyric acid), the predominant inhibitory neurotransmitter in the central nervous system, and mediates slow and prolonged synaptic inhibition through Gi or Go proteins. GABA_B receptor malfunction is linked to neurological disorders including spasticity and epilepsy. KCTD proteins (KCTD8, KCTD12, KCTD12b, [KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16)](/xray-mp-wiki/proteins/gpcr/kctd16/)) serve as auxiliary subunits that bind to the GABA_B2 C-terminal tail and modulate signaling kinetics. Ligand binding occurs within the large extracellular Venus flytrap (VFT) module of GBR1. Crystal structures of the heterodimeric GBR1b_VFT:GBR2_VFT complex in apo, agonist-bound, and antagonist-bound forms revealed a unique activation mechanism: the apo and antagonist-bound states adopt an open-open conformation (resting state), while agonist binding induces domain closure in GBR1 alone (closed-open active state) and formation of a novel LB2-LB2 heterodimer interface between subunits.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12725 | 4MQE | 3.3 | I222 | GBR1b_VFT (residues 48-459) with N-terminal gp67 signal peptide and C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/); GBR2_VFT (residues 1-466) with C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/); expressed in Sf9 insect cells via baculovirus co-infection at 23 C for 96 h; purified from cell supernatant by anti-Flag M2 affinity and [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) gel filtration | None (apo) |
| doi/10.1038##nature12725 | 4MSL | 3.3 | I222 | GBR1b_VFT (residues 48-459) with N-terminal gp67 signal peptide and C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/); GBR2_VFT (residues 1-466) with C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/); expressed and purified in presence of 10-20 uM CGP54626 | CGP54626 |
| doi/10.1038##nature12725 | 4MR7 | 3.1 | P212121 | GBR1b_VFT (residues 48-459) with N-terminal gp67 signal peptide and C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/); GBR2_VFT (residues 1-466) with C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/); expressed and purified in presence of 100 uM (R)-baclofen | (R)-Baclofen |
| doi/10.1038##nature12725 | 4MR9 | 3.2 | P212121 | GBR1b_VFT (residues 48-459) with N-terminal gp67 signal peptide and C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/); GBR2_VFT (residues 1-466) with C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/); expressed and purified in presence of 100 uM GABA | GABA |

## Expression and Purification

- **Expression system**: Sf9 insect cells via baculovirus co-infection (GBR1b_VFT and GBR2_VFT)
- **Construct**: GBR1b_VFT residues 48-459 with N-terminal gp67 signal peptide and C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) in pFBDM vector. GBR2_VFT residues 1-466 with C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) in pFBDM vector.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Co-expression | Baculovirus co-infection in Sf9 insect cells at 23 C for 96 h | -- | Not specified + -- | Sf9 cells co-infected with recombinant GBR1b_VFT and GBR2_VFT baculoviruses. For antagonist-bound complex, 10 uM CGP54626 present throughout expression. For agonist-bound complexes, 100 uM (R)-baclofen or GABA present throughout expression. |
| Anti-Flag [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Anti-Flag M2 antibody [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Anti-Flag M2 affinity resin | Not specified + -- | GBR1b_VFT:GBR2_VFT complex purified from cell supernatant. For antagonist-bound complex, 20 uM CGP54626 present during purification. For agonist-bound complexes, 100 uM (R)-baclofen or GABA present during purification. |
| Gel filtration | Size-exclusion chromatography ([Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/), GE Healthcare) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | Not specified + -- | Final purification step for the heterodimeric complex. |


## Crystallization

### doi/10.1038##nature12725

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | GBR1b_VFT:GBR2_VFT complex |
| Reservoir | 10% [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.12 M Na acetate pH 7.0 |
| Temperature | 4 C |
| Notes | Apo and antagonist-bound complexes crystallized under the same condition. CGP54626-bound complex crystallized using protein purified in presence of CGP54626. Other antagonist complexes (CGP46381, CGP35348, SCH50911, 2-OH-saclofen, phaclofen) crystallized by co-crystallization with 10 mM antagonist. Crystals frozen directly from drops. Data collected at APS 24ID-C and 24ID-E beamlines. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | (R)-Baclofen-GBR1b_VFT:GBR2_VFT complex |
| Reservoir | 20% [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/), 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.2 M NH4Cl, 0.1 M Na [Cacodylate (Sodium Dimethylarsenate)](/xray-mp-wiki/reagents/buffers/cacodylate/) pH 5.2 |
| Temperature | 20 C |
| Notes | Crystallized in presence of 10 mM (R)-baclofen. Crystals frozen in cryoprotecting solution containing 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) plus all crystallization components. Data collected at APS 24ID-C and 24ID-E beamlines. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | GABA-GBR1b_VFT:GBR2_VFT complex |
| Reservoir | 18% [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.15 M NH4Cl, 0.1 M Na [Cacodylate (Sodium Dimethylarsenate)](/xray-mp-wiki/reagents/buffers/cacodylate/) pH 5.0 |
| Temperature | 20 C |
| Notes | Crystallized in presence of 10 mM GABA. Crystals frozen in cryoprotecting solution containing 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) plus all crystallization components. Data collected at APS 24ID-C and 24ID-E beamlines. |


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

- [Human GABA_A Receptor Beta-3 Subunit](/xray-mp-wiki/proteins/cys-loop-receptors/gabar-b3/) — Related GABA receptor; GABA_A is an ion channel, GABA_B is a GPCR
- [G Protein-Coupled Receptor (GPCR)](/xray-mp-wiki/concepts/gpcr/) — GABA_B R is a class C GPCR that functions as an obligatory heterodimer
- [Baclofen](/xray-mp-wiki/reagents/ligands/baclofen/) — Selective GABA_B agonist used clinically to treat muscle spasticity
- [GABA](/xray-mp-wiki/reagents/ligands/gaba/) — Endogenous agonist for GABA_B receptor
- [Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Expression system used for GBR1b_VFT and GBR2_VFT in Sf9 cells
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16)](/xray-mp-wiki/proteins/gpcr/kctd16/) — Related protein structure
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/) — Additive used in purification or crystallization buffers
