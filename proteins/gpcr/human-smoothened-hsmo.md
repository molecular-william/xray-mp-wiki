---
title: "Human Smoothened (SMO) — Extracellular Domain Regulation"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein]
sources: [doi/10.1038##nature18934]
verified: false
---

# Human Smoothened (SMO) — Extracellular Domain Regulation

## Overview

Human Smoothened (SMO) is a Class F G-protein-coupled receptor (GPCR) and Hedgehog (Hh) signal transducer that contains two distinct ligand-binding sites: one in its heptahelical transmembrane domain (TMD) and one in its extracellular cysteine-rich domain (CRD). The crystal structure of human SMO (SMOΔC, residues 32-555) was determined at 3.2 Å resolution (PDB 5L7D), revealing the CRD stacked atop the TMD via an intervening wedge-like linker domain. A cholesterol molecule was discovered bound to the CRD binding site, positioned at the interface between the CRD, linker domain, and TMD. Mutations that prevent cholesterol binding (Asp95Ala, Tyr130Phe in human) impair SMO's ability to transmit native Hh signals. Binding of the clinically used antagonist vismodegib to the TMD induces a conformational change propagated to the CRD, resulting in loss of cholesterol from the CRD-linker domain-TMD interface. A second structure with vismodegib bound (SMOΔC-vismodegib) was also determined (PDB 5L7I), showing the allosteric communication between the two binding sites.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature18934 | 5L7D | 3.20 | P212121 | Human SMO residues 32-555 (SMOΔC) with ICL3 (429-440) replaced by BRIL fusion; C-terminal Rho1D4 epitope tag | Cholesterol (CRD site) |
| doi/10.1038##nature18934 | 5L7I | 3.70 | P212121 | Human SMO residues 32-555 (SMOΔC) with ICL3 (429-440) replaced by BRIL fusion; C-terminal Rho1D4 epitope tag | Vismodegib (TMD site) |

## Expression and Purification

- **Expression system**: HEK-293S-GnTI- cells (transient transfection)
- **Construct**: Human SMO residues 32-555 with ICL3 replaced by BRIL (residues 23-128); C-terminal Rho1D4 or monoVenus tag; Val329Phe inactivating mutation

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Membrane solubilization | DDM extraction | — | 10 mM HEPES pH 7.5, 300 mM NaCl, 1% DDM, 0.5% DDM / 0.1% CHS | 2 h at 4°C; removal of insoluble material by ultracentrifugation (100,000g, 30 min) |
| 2. Affinity capture | 20(S)-OHC beads or 1D4 immunoaffinity | — | 10 mM HEPES pH 7.5, 300 mM NaCl, 0.1% DDM | Captured on 20(S)-OHC beads for ligand-binding validation; 1D4 antibody beads for structural samples |
| 3. LCP reconstitution | Lipidic cubic phase mixing | — | Protein mixed with 10% cholesterol / 90% monoolein (60:40 ratio) | Protein at 30 mg/ml; with or without 10 mM vismodegib |


## Crystallization

### doi/10.1038##nature18934

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | SMOΔC at 30 mg/ml in LCP (10% cholesterol, 90% monoolein) |
| Temperature | 20°C |
| Growth time | Several weeks |
| Notes | Crystals grown in LCP; data collected at Diamond Light Source beamlines I24 and B21. Structure solved by molecular replacement using SMO TMD structure (PDB 4O9R) and CRD solution structure |


## Biological / Functional Insights

### Cholesterol as endogenous SMO ligand

A cholesterol molecule was unexpectedly discovered bound to the CRD of human SMO, occupying a central position at the interface between the CRD, linker domain, and TMD. The cholesterol's tetracyclic sterol ring binds in a shallow groove in the CRD (a site previously shown to bind 20(S)-OHC), while its iso-octyl tail is buried in the SMO protein core some 12 Å from the membrane bilayer. Mutations in the hydrogen-bonding network (Asp99Ala, Tyr134Phe in mouse; corresponding to Asp95, Tyr130 in human) that coordinates the cholesterol 3β-hydroxyl group impair SMO signalling in response to both SHH and 20(S)-OHC, confirming functional relevance.

### Allosteric communication between CRD and TMD binding sites

Vismodegib binding to the TMD site induces a conformational change that is propagated to the CRD via ECL3, resulting in rearrangement of the sterol-binding site and loss of cholesterol from the CRD-linker domain-TMD interface. This provides structural evidence for allosteric communication between the two known ligand-binding sites of SMO and explains how antagonists binding in the TMD can functionally antagonize CRD-mediated activation.

### CRD-linker domain-TMD interface stabilizes inactive state

The interface between the CRD, linker domain, and TMD stabilizes the inactive state of SMO. Mutations that disrupt CRD-linker domain contacts (Pro120Ser in human), alter the CRD surface (Ile160Asn/Glu162Thr), or disrupt a disulfide bond within the linker domain (Cys197Ser/Cys217Ser) all increase constitutive signalling activity of SMO. SAXS experiments show that 20(S)-OHC binding induces a conformational change that increases the maximum particle size from 120 Å to 129 Å, suggesting CRD displacement upon activation.


## Cross-References

- [Mouse Smoothened (SMO) — Class F GPCR](/xray-mp-wiki/proteins/gpcr/smoothened/) — Active state mouse SMO structure (PDB 6O3C) showing deep 7TM sterol pocket, complementary to the human CRD-bound cholesterol structure
- [Deep 7TM Sterol-Binding Site of Smoothened](/xray-mp-wiki/concepts/structural-mechanisms/deep-7tm-sterol-binding-site/) — The 7TM sterol site is a distinct binding pocket deeper in the helical bundle, separate from the CRD cholesterol site described here
