---
title: Spinach Chloroplast ATP Synthase c14-Ring
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41598-019-55092-z]
verified: false
---

# Spinach Chloroplast ATP Synthase c14-Ring

## Overview

The c14-ring of the F1Fo ATP synthase from spinach (Spinacia oleracea)
chloroplasts is a homo-tetradecameric ring composed of 14 identical
c-subunits that forms the rotor of the chloroplast FoF1 ATP synthase.
The structure was determined at 2.3 Angstrom resolution by in meso
crystallization, revealing the molecular mechanisms of intersubunit
contacts that determine the c14 stoichiometry. A remarkable feature is
the presence of additional electron densities inside the c-ring forming
circles parallel to the membrane plane at 5.4 Angstrom intervals,
hypothesized to originate from isoprenoid quinones such as
plastoquinone-9. The structure also reveals positive electron densities
at the external surface near the active site Glu61, which may
correspond to a fragment of the a-subunit in a fixed rotor/stator
state.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41598-019-55092-z |  | 2.3 | I 1 2 1 | Native c14-ring from spinach chloroplast FoF1 ATP synthase |  |

## Expression and Purification

- **Expression system**: Native (Spinacia oleracea L. chloroplast thylakoid membranes)
- **Construct**: Native c-subunit of chloroplast FoF1-ATPase

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Chloroplast membrane isolation | Membrane preparation | — |  | Fresh spinach leaves; thylakoid membrane isolation |
| 2. Membrane solubilization | Detergent solubilization | — | 23 mM sodium cholate, 55 mM octyl-beta-D-glucopyranoside |  |
| 3. Fractionated ammonium sulfate precipitation | Precipitation | — |  | Partial separation from lipids and contaminating proteins |
| 4. Rate zonal centrifugation | Ultracentrifugation | — | Azolectin 1 mg/mL, 8 mM DDM | Step gradient (15-50% sucrose); CFoF1 found in 36% and 43% fractions |
| 5. Desalting and dye-ligand chromatography | Affinity chromatography | HiTrap Desalting Column, Reactive Red 120 |  | Further purification by dye-ligand chromatography |


## Crystallization

### doi/10.1038##s41598-019-55092-z

| Parameter | Value |
|---|---|
| Method | In meso crystallization |
| Protein sample | Purified cF1Fo |
| Temperature | Room temperature |
| Growth time | 2 months |
| Notes | Type I plate-like crystals up to 20 um. Crystals had strong yellow color (characteristic of isoprenoids). Space group I121. |


## Biological / Functional Insights

### Molecular mechanisms of intersubunit contacts in the c14-ring

The structure reveals dense hydrogen bonding between inner helices close to the F1 side of the c-ring, mediated by water molecules. At the active center (Glu61), the glutamate sidechain is bonded directly to the backbone of the neighboring subunit in large c-rings (c14), while in small c-rings (c9, c10) this connection is mediated by water molecules, leading to increased distance between outer helices.

### Additional electron densities inside the c-ring

Three circles of additional electron density at 5.4 Angstrom intervals are observed inside the c14-ring, parallel to the membrane plane. These densities are present in all known high-resolution c-ring structures from mitochondria, bacteria, and archaea. The distance corresponds to the spacing of methyl groups in an isoprenoid chain (~5 Angstrom), suggesting the presence of isoprenoid molecules.

### Unusual hydrophobic pore dimensions

The internal pore of the c-ring has a hydrophobic thickness of 45.8 Angstrom (1.5 times larger than the external hydrophobic thickness of 32.6 Angstrom). The inner diameter varies from 30 Angstrom (stroma), 23 Angstrom (center), to 28 Angstrom (lumen). The conical shape and extreme hydrophobic thickness make it unlikely that regular membrane lipids fill the pore.

### External electron densities near active site

Additional positive electron densities at the external surface of the c-ring near Glu61 may correspond to an unfolded fragment of the a-subunit alpha-helix 5 or 6 that interacts with the active site in the intact ATP synthase, possibly representing a fixed rotor/stator state.

### Hypothesis: isoprenoid quinones as universal c-ring cofactors

The universality of the internal densities across species suggests a common molecule. Isoprenoid quinones (plastoquinone in chloroplasts, coenzyme Q in mitochondria, menaquinone in bacteria) are natural components of these membranes, have long hydrophobic tails matching the inner pore thickness, and are known to absorb in the 400-500 nm range consistent with the yellow crystal color. UV-Vis spectroscopy of dissolved crystals shows a peak at 335 nm consistent with plastosemiquinone-9, and differential spectroscopy with NaBH4 shows features matching trimethyl benzoquinone (the polar head group of plastoquinone-9). These molecules may stabilize the c-ring, prevent ion leakage, and protect against reactive oxygen species.


## Cross-References

- [Common Drug-Binding Site on ATP Synthase c-Ring](/xray-mp-wiki/concepts/common-drug-binding-site-atp-synthase-c-ring/) — The c-ring is the target of several drugs; the internal pore may have functional significance
- [Binding Change Mechanism of ATP Synthase](/xray-mp-wiki/concepts/binding-change-mechanism/) — The c-ring is the rotor of ATP synthase; its structure is essential for understanding the rotary mechanism
- [Chloroplast ATP Synthase c-Ring from Pisum sativum](/xray-mp-wiki/proteins/pumps-atpases/chloroplast-atp-synthase-c-ring/) — Earlier lower-resolution (3.4 Angstrom) structure of plant c14-ring from pea; the spinach structure provides higher resolution details
- [Yeast Mitochondrial ATP Synthase c10 Ring](/xray-mp-wiki/proteins/pumps-atpases/yeast-mitochondrial-atp-synthase-c10-ring/) — Mitochondrial c-ring with similar internal electron densities supporting the universality of the isoprenoid hypothesis
