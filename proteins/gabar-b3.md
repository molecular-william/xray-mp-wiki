---
title: Human GABA_A Receptor Beta-3 Subunit
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NATURE13293]
verified: false
---

# Human GABA_A Receptor Beta-3 Subunit

## Overview

The human GABA_A receptor beta-3 subunit (GABA_A R-β3) is a pentameric ligand-gated chloride channel that serves as the principal mediator of rapid inhibitory synaptic transmission in the human brain. GABA_A receptors belong to the Cys-loop receptor superfamily of pentameric ligand-gated ion channels (pLGICs), which also includes nicotinic acetylcholine receptors and serotonin 5-HT3 receptors. The β3 subunit can form functional homomeric channels and serves as a model for understanding heteromeric GABA_A receptor architecture. This structure represents the first three-dimensional structure of any GABA_A receptor, revealing architectural elements unique to eukaryotic Cys-loop receptors and the structural basis of channel desensitization.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NATURE13293 | 4COF | 3.0 A | C2 | Full-length human GABA_A receptor beta-3 subunit (UniProt P28472, residues 26-447), N-terminally tagged with monoVenus fluorescent protein, C-terminally tagged with Rho-1D4 epitope (TETSQVAPA). Based on GenBank M82919, codon-optimized for mammalian expression.
 | Benzamidine (crystallization ligand, EC50 = 61 uM agonist) |

## Expression and Purification

- **Expression system**: HEK293S-GnTI- cells
- **Construct**: Synthetic cDNA encoding full-length human GABA_A R beta-3 subunit (GenBank M82919), codon-optimized for mammalian expression. Cloned into pHILsec vector with secretion signal sequence. N-terminal monoVenus tag (10 amino acids) and C-terminal Rho-1D4 epitope tag (TETSQVAPA, 9 amino acids).


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell expression | Transient transfection in HEK293S-GnTI- cells | -- | Protein expression media (PEM, Invitrogen) with L-glutamine, non-essential amino acids, 1% fetal calf serum + -- | 61 batches grown in suspension to 2 x 10^6 cells/ml. Transfected with PEI Max and plasmid DNA. 40-70% transfection efficiency. 48-72 h post-transfection.
 |
| Cell lysis and solubilization | Detergent solubilization of membrane fraction | -- | 10 mM HEPES pH 7.2, 300 mM NaCl, 1:100 mammalian protease inhibitor + 1% DDM | Cells resuspended and solubilized for 2 h at 4 C. Insoluble material removed by centrifugation (10,000g, 15 min).
 |
| Immuno-affinity purification | Rho-1D4 antibody-coated sepharose beads | Rho-1D4 antibody coupled to CNBr-activated sepharose | 10 mM HEPES pH 7.2, 300 mM NaCl, 1% DDM + 1% DDM | Incubated for 2 h at 4 C with purified Rho-1D4 antibody on beads. Washed with buffer at 3x CMC. Eluted overnight with 500 uM TETSQVAPA peptide.
 |
| Size-exclusion chromatography | Superdex 200 3.2/300 SEC | Superdex 200 3.2/300 (GE Healthcare) | 10 mM HEPES pH 7.2, 300 mM NaCl, 0.02% DDM + 0.02% DDM | HPLC system with automated micro-volume loader and in-line fluorescence detection (Shimadzu). Peak fractions concentrated to 3 mg/ml.
 |

**Final sample**: 3 mg/ml in 10 mM HEPES pH 7.2, 300 mM NaCl, 0.02% DDM


## Crystallization

### doi/10.1038##NATURE13293

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | GABA_A R-β3 cryst (3 mg/ml) with benzamidine |
| Reservoir | 11.5% PEG 4000, 100 mM NaCl, 100 mM Li2SO4, 100 mM ACES buffer (N-(2-Acetamido)iminodiacetic acid) pH 6.5, 2% (v/v) benzamidine
 |
| Mixing ratio | Not specified |
| Temperature | 4 C |
| Growth time | Not specified |
| Cryoprotection | Soaking in precipitant solution supplemented with 20% glycerol for 30 min before flash freezing in liquid nitrogen
 |
| Notes | Structure solved at 3.0 A resolution by molecular replacement using GluCl (PDB 3RIF) as search model. R_work = 0.207, R_free = 0.227. 13972 atoms (13643 protein, 279 glycans, 45 benzamidine, 5 chloride).
 |


## Biological / Functional Insights

### Closed gate in desensitized state

The channel forms a closed gate at the base of the pore, at the -2' position (Ala 248), with a diameter of only 3.15 A — too narrow for chloride anion passage (Pauling radius 1.8 A). The M2 helix trajectory is narrowest at the intracellular border, resembling open conformations of GLIC and GluCl, but the pore remains shut due to a unique Tyr 299 conformation that presses M2 inward. This differs fundamentally from ELIC and Torpedo nAChR, which have closed gates in the extracellular portion (9' to 20') formed by hydrophobic side chains. None of the conserved M2 hydrophobic rings (1' Val, 3' Leu, 5' Ile, 8' Val, 9' Leu, 11' Met, 14' Ile, 18' Leu) line the pore in GABA_A R-β3. Instead, 9' Leu side chains rotate out of the pore, placed between adjacent M2 helices.

### Chloride binding sites in the vestibule

A water-filled extracellular domain vestibule and transmembrane pore runs through the five-fold pseudo-symmetry axis, joined by lateral tunnels from between each subunit. A positively charged ring halfway down the vestibule hosts putative anion binding sites at each inter-subunit interface, revealed by electron density peaks at ~6 sigma level. These sites correspond to the previously proposed ion selectivity filter in Cys-loop receptors and are in spatial proximity to the 'anion site 1' reported in GLIC. Five chloride ions were placed and refined in the final model, suggesting chloride ions may be important stabilizers of pLGIC assembly.

### Anaesthetic binding pockets

Two large non-overlapping pockets near residues previously inferred to bind intravenous anaesthetics etomidate and propofol. The putative propofol-binding pocket is structurally distinct from the one in GLIC. The binding and transduction modes of propofol on GABA_A R-β3 and GLIC are unrelated; propofol potentiates and activates GABA_A Rs but inhibits GLIC. The etomidate-binding pocket is located near His 267 (17' position in M2).

### Benzamidine as a novel agonist

Benzamidine was discovered to act as a GABA_A R agonist capable of inducing desensitization. EC50 = 61 +/- 12 uM in whole-cell patch-clamp recordings. In thermostabilization assays, EC50 = 370 +/- 180 uM, similar to histamine (400 +/- 150 uM). Classically, benzamidine is known as a serine-protease inhibitor. The benzamidine benzyl ring stacks between Phe 200 and Tyr 62, while its amidinium group forms hydrogen bonds with Glu 155, Ser 156, and Tyr 157, with putative cation-pi interactions with Tyr 157 and Tyr 205. This binding mode is reminiscent of the principal face in GluCl and AChBP.


## Cross-References

- [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine/) — Novel GABA_A R agonist ligand; EC50 = 61 uM; crystallization additive at 2%
- [ACES Buffer (N-(2-Acetamido)iminodiacetic Acid)](/xray-mp-wiki/reagents/buffers/aces/) — Crystallization buffer at 100 mM, pH 6.5
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Structure solved by MR using GluCl (PDB 3RIF) as search model
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC on Superdex 200 3.2/300 for final purification step
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent at 1%
- [N-Dodecyl-D-maltopyranoside (DMNG)](/xray-mp-wiki/reagents/detergents/dmng/) — Used in thermostabilization assay buffer at 0.007%
- [Cholesterol Hemisuccinate (CHS)](/xray-mp-wiki/reagents/lipids/cholesterol-hydrogen-succinate/) — Used in thermostabilization assay buffer at 0.0006%
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Cryoprotectant at 20% in crystallization
