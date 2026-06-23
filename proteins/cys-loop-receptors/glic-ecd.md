---
title: GLIC ECD (Extracellular Domain of Gloeobacter violaceus Ion Channel)
created: 2026-05-27
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.1016##j.jmb.2009.11.024, doi/10.1038##emboj.2013.17]
verified: true
---

# GLIC ECD (Extracellular Domain of Gloeobacter violaceus Ion Channel)

## Overview

The extracellular domain (ECD) of the [Pentameric Ligand-Gated Ion Channel (pLGIC)](/xray-mp-wiki/concepts/cys-loop-receptor-family/) ([Pentameric Ligand-Gated Ion Channel (pLGIC)](/xray-mp-wiki/concepts/cys-loop-receptor-family/)) from *Gloeobacter violaceus* ([GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic)). [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic) is a bacterial proton-gated ion channel homologous to eukaryotic Cys-loop receptors including the nicotinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine) receptor (nAChR). The isolated ECD was crystallized at neutral pH, revealing an unexpected hexameric quaternary structure instead of the expected pentameric assembly. This finding demonstrated that the transmembrane domain is necessary for proper pentameric oligomeric assembly of [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic).

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2009.11.024 | 3IGQ | 2.3 | P21212 | ECD residues 3-193, F116G Y119T P120E F121S, C-terminal His-tag | chloride ion, sodium ion, acetate |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press in 20 mM [Tris (Hydroxymethyl) Aminomethane](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 300 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) | — |  |  |
| Affinity purification | [Ni-NTA Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) resin | — |  |  |
| [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Superose 6 SEC Resin](/xray-mp-wiki/reagents/additives/superose-6/) 10/300 GL column in 20 mM [Tris (Hydroxymethyl) Aminomethane](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 300 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) | — |  |  |


## Crystallization

### doi/10.1016##j.jmb.2009.11.024

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) |
| Temperature | 20 |


## Biological / Functional Insights

### Hexameric quaternary structure at neutral pH

The isolated [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic) ECD forms hexamers in the crystal at neutral pH (pH 7), replacing the expected pentameric assembly seen in the full-length [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic) protein. The six molecules in the asymmetric unit form two similar hexamers that superimpose with an RMSD of 0.50 A for 535 Ca atoms. The crystal lattice consists of 2D layers of hexamers, which is geometrically possible (unlike pentamers). A second crystal form in space group P6 also displayed hexameric 2D layers.

### Monomeric state in solution

[Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) and analytical ultracentrifugation (sedimentation velocity) experiments confirmed that the mutated ECD exists as a monomer in solution at both 4 and 12 mg/ml concentrations (s = 1.9 +/- 0.2 S). The wild-type (unmutated) ECD construct showed identical [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) profiles. This indicates that the hexameric assembly is driven by crystal packing rather than solution thermodynamics.

### Tertiary fold flexibility and rigid core

The ECD monomer fold closely matches the equivalent portion of full-length [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic). The inner beta-sheet (strands beta1, beta2, beta3, beta5, beta6, beta8) forms a rigid core with C-alpha deviations less than 1 A. The outer beta-sheet is more flexible with deviations of 1-2 A. Highly flexible regions include the C-loop and the zone normally contacting the TMD. The beta1-beta2 loop shows strong motion due to a broken salt bridge (D32-R192) that is present in full-length [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic).

### Subunit-interface plasticity and allosteric implications

Comparison of hexameric versus pentameric interfaces shows that subunit-subunit contacts bury approximately the same surface (10.3% for hexamer vs 8.5% for pentamer). The reorganization from pentamer to hexamer can be described as a downward translation by one inter-beta-strand distance (~5 A) and a global rotation of the complementary subunit. The C-loop is excluded from the hexameric interface, being unstructured in this form. Interface curvature analysis (fitting to quadratic surface) gives g = -0.075 for hexamer and -0.079 for pentamer, both negative. AChBP has positive curvature (0.006 to 0.022). The weak subunit-subunit interactions in [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic) ECD may facilitate allosteric transitions during channel gating.

### Ion binding sites are conserved between GLIC-ECD and full-length GLIC

The crystal structure of the [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic)-ECD was solved at 2.3 A resolution at neutral pH (pH 7). Quality of the electron density map and chemical reasoning led to model several well-resolved peaks in the vestibule region as one chloride ion, one sodium ion, and one [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate) molecule, the latter being present in the crystallization buffer at a high concentration of 2.4 M. Superimposing the structures of [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic) and [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic)-ECD shows that the positions of these ions coincide exactly with the cation 1, anion 1, and [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate) 1 binding sites described for the whole molecule. Surprisingly, the ECD alone displayed a hexameric quaternary structure with a 6-fold axis replacing the 5-fold axis of the whole molecule. As the hexameric [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic)-ECD and pentameric [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic) structures were solved at neutral (pH 7) and acidic pH (pH 4), respectively, it suggests that these binding sites are not pH-dependent.


## Cross-References

- [Pentameric Ligand-Gated Ion Channel (pLGIC)](/xray-mp-wiki/concepts/cys-loop-receptor-family/) — Referenced in glic-ecd
- [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Referenced in glic-ecd
- [Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) — Referenced in glic-ecd
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Referenced in glic-ecd
- [Bis-Tris Propane Buffer](/xray-mp-wiki/reagents/buffers/bis-tris-propane/) — Referenced in glic-ecd
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Referenced in glic-ecd
- [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine) — Referenced in glic-ecd
- [Ni-NTA Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) — Referenced in glic-ecd
- [Superose 6 SEC Resin](/xray-mp-wiki/reagents/additives/superose-6/) — Referenced in glic-ecd
- [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate) — Referenced in glic-ecd
