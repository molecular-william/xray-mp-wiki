---
title: Molecular Docking
created: 2026-06-08
updated: 2026-06-08
type: method
category: methods
layout: default
tags: [structure-xray, subdirectory-structure-determination]
sources: [doi/10.1038##s42003-019-0427-1, doi/10.1074##jbc.M116.766964, doi/10.1107##s2059798320015004]
verified: false
---

# Molecular Docking

## Overview

Molecular docking is a computational method used to predict the preferred
orientation and binding mode of a small molecule (ligand) when bound to a
target protein of known three-dimensional structure. It enables
structure-based prediction of ligand binding sites, binding affinities,
and protein-ligand interactions. In the context of membrane protein
crystallography, docking is used when experimental co-crystallization or
soaking of a substrate is unsuccessful, often due to low binding affinity
or competition from crystallization components.

## Protocol

### Reagents and Materials

- Protein crystal structure (PDB format)
- Ligand structure file (SDF or MOL2 format)

### Steps

1. {'step': 'Protein structure preparation', 'description': 'Remove all ligands, solvent, and non-protein atoms from the crystal structure. Add hydrogen atoms, assign protonation states. Generate receptor grid around the predicted or known binding site.', 'notes': 'For M. tuberculosis PgsA1, three structural models were used — apo, CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) bound, and Mn-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) bound — with all ligands removed prior to docking.'}
2. {'step': 'Ligand preparation', 'description': 'Generate three-dimensional conformer of the small molecule ligand. Assign bond orders, formal charges, tautomers, and stereochemistry. Generate multiple conformations.', 'notes': '[D-myo-Inositol-3-Phosphate](/xray-mp-wiki/reagents/ligands/d-myo-inositol-3-phosphate/) was prepared with correct stereochemistry and protonation state for docking.'}
3. {'step': 'Docking calculation', 'description': 'Sample ligand poses in the receptor binding site using a scoring function that evaluates steric and electrostatic complementarity. Score each pose and rank by binding energy.', 'notes': 'Two representative binding poses (clusters) were obtained for ino-P docking against PgsA1 structures. Binding mode'}
4. {'step': 'Cluster analysis and pose selection', 'description': 'Group docked poses by spatial similarity into clusters. Select top-ranked poses from each major cluster for analysis.', 'notes': 'The two top clusters placed the ino-P 1-prime hydroxyl within hydrogen bonding distance of the catalytic base D93, consistent with reaction chemistry.'}
5. {'step': 'Experimental validation', 'description': 'Test predicted binding modes through mutagenesis and functional assays.', 'notes': 'Mutations A90Y, R94K/Q, Y133F/E, and R137K/Q were designed based on docking predictions and tested by activity assays in proteoliposomes. R94K dramatically reduced activity, supporting binding mode'}


## Advantages

- Can provide structural information on ligand binding when experimental co-crystallization is not feasible
- Enables hypothesis-driven mutagenesis studies
- Computationally efficient compared to experimental screening

## Disadvantages

- Results require experimental validation (mutagenesis, activity assays)
- Scoring functions have limited accuracy for binding energy prediction
- Protein flexibility and solvation effects are challenging to model
- May not capture induced-fit conformational changes fully
