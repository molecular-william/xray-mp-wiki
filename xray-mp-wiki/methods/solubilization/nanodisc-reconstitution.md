---
title: Nanodisc Reconstitution
created: 2026-06-03
updated: 2026-06-03
type: method
category: methods
layout: default
tags: [solubilization-nanodisc, subdirectory-solubilization]
sources: [doi/10.1038##nature12232]
verified: false
---

# Nanodisc Reconstitution

## Overview

Nanodisc reconstitution is a technique for embedding membrane proteins into small, disc-like lipid bilayer assemblies called nanodiscs. Nanodiscs consist of a patch of lipid bilayer encircled by membrane scaffold proteins (MSPs) or synthetic polymers. They provide a near-native lipid environment for membrane proteins while remaining soluble and monodisperse. Nanodisc reconstitution is particularly valuable for functional assays of membrane proteins, as it allows access to both the extracellular and cytoplasmic sides of the membrane, enabling studies of periplasmic binding proteins and regulatory proteins that interact with the transporter from opposite membrane faces.

## Protocol

### Reagents and Materials

- MalFGK2 ([Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter) — ABC transporter reconstituted into nanodiscs
- 1,2-dimyristoyl-sn-glycero-3-phosphocholine ([DMPC](/xray-mp-wiki/reagents/lipids/dmpc/)) or equivalent phospholipid — bilayer lipid
- Membrane scaffold protein (MSP) or synthetic polymer — encircles the lipid bilayer
- Maltose-binding protein (MBP) — periplasmic binding protein for ATPase stimulation
- EIIA^Glc — regulatory protein for inhibition assays
- ATP — substrate for ATPase activity measurement
- NADH — coupled enzyme system for ATPase assay
- Phosphoenolpyruvate (PEP) — ATP regeneration substrate
- Pyruvate kinase — ATP regeneration enzyme
- Lactate dehydrogenase — coupled enzyme for NADH consumption monitoring

### Steps

1. {'step': 'Nanodisc preparation', 'description': 'Prepare lipid nanodiscs containing the membrane protein of interest. The protein is mixed with lipids and membrane scaffold protein, then self-assembles into nanodiscs. The lipid composition can be tuned to mimic the native membrane.\n'}
2. {'step': 'Functional assay setup', 'description': 'Reconstitute the membrane protein into nanodiscs to allow access of both MBP (from the extracellular/periplasmic side) and EIIA^Glc (from the cytoplasmic side) to both faces of the membrane. This enables measurement of ATPase activity in a near-native membrane environment.\n'}
3. {'step': 'ATPase activity measurement', 'description': 'Measure ATPase activity by recording absorption at 340 nm in an ATP regeneration- NADH consumption-coupled system. The [Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter reconstituted in nanodiscs is stimulated by MBP, and inhibition by EIIA^Glc is quantified. Data are fit to the Hill equation or Michaelis-Menten equation.\n'}

### Typical Conditions

- **temperature**: 22 C
- **measurement**: Absorption at 340 nm (NADH consumption)


## Advantages

- Provides a near-native lipid environment for functional assays
- Allows access to both sides of the membrane (extracellular and cytoplasmic)
- Enables measurement of regulatory protein inhibition (e.g., EIIA^Glc)
- Sample remains soluble and monodisperse
- Can be used for kinetic analysis (Hill equation, Michaelis-Menten fitting)

## Disadvantages

- Requires optimization of nanodisc composition for each protein
- More complex to prepare than detergent-solubilized samples
- Membrane scaffold protein must be compatible with the assay

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Maltose](/xray-mp-wiki/reagents/additives/maltose/) Transporter (MalFGK2) | N/A (functional assay) | N/A | Reconstituted into lipid nanodiscs for MBP-stimulated ATPase activity measurement and EIIA^Glc inhibition kinetics; IC50 of full-length EIIA^Glc = 1.61 uM, Delta(1-18) [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) = 91 uM |

## Related Methods

- [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) — Another lipid-based membrane protein technique using [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/)/CHAPSO bicelles
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC used for nanodisc size selection and sample homogeneity assessment

## Related Reagents

- [DMPC (1,2-Dimyristoyl-sn-glycero-3-phosphocholine)](/xray-mp-wiki/reagents/lipids/dmpc/) — Phospholipid component for nanodisc bilayer
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — Substrate for ATPase activity measurement
- [Nicotinamide Adenine Dinucleotide (NADH)](/xray-mp-wiki/reagents/cofactors/nadh/) — Coupled enzyme system for ATPase assay (absorption at 340 nm)
