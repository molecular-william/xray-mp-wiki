---
title: GltPh Glutamate Transporter Homolog from Pyrococcus horikoshii
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.aba9854]
verified: false
---

# GltPh Glutamate Transporter Homolog from Pyrococcus horikoshii

## Overview

GltPh is a prokaryotic glutamate transporter homolog from the hyperthermophilic archaeon Pyrococcus horikoshii. It belongs to the SLC1 family of excitatory amino acid transporters (EAATs) and serves as the primary structural model for understanding glutamate transport mechanisms. GltPh functions as a trimeric secondary active transporter that couples aspartate transport to Na+, K+, and H+ gradients using an elevator-like alternating-access mechanism. Each protomer operates independently, consisting of a static scaffold/trimerization domain and a mobile transport domain containing the substrate- and ion-binding sites. The hairpin loop 2 (HP2) serves as an extracellular gate controlling access to the substrate-binding pocket.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##sciadv.aba9854 |  | 2.5 | P321 | Wild-type GltPh | Na+ (Na1 and Na3 sites occupied), phosphate (cocrystallized) |
| doi/10.1126##sciadv.aba9854 | 4OYE |  |  | R397A GltPh apo |  |
| doi/10.1126##sciadv.aba9854 | 4OYF |  |  | R397A GltPh Na1-bound | Na+ (Na1 site) |
| doi/10.1126##sciadv.aba9854 | 2NWX |  |  | Wild-type GltPh | Na+, aspartate |
| doi/10.1126##sciadv.aba9854 | 2NWW |  |  | Wild-type GltPh | [TBOA](/xray-mp-wiki/reagents/tboa/), Na+ (Na1 site) |

## Expression and Purification

- **Expression system**: Escherichia coli Top10F
- **Construct**: Wild-type GltPh and mutants (F273W, R397A, M311A)
- **Notes**: Expression induced with 0.1% L-arabinose at OD600 of 2.5. Used for both crystallography and stopped-flow fluorescence experiments.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity chromatography | HIS-tag nickel-nitrilotriacetic acid (Ni-NTA) affinity gel | — | 200 mM NaCl, 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/), 1 mM n-dodecyl beta-D-maltoside (DDM), pH 7.4 |  |
| Size exclusion chromatography | SEC | — | 200 mM NaCl, 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/), 1 mM DDM, pH 7.4 |  |


## Crystallization

### doi/10.1126##sciadv.aba9854

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Notes | In meso approach to membrane protein crystallization. Structure solved at 2.5-A resolution — the highest resolution reported for any SLC1 transporter at the time. |


## Biological / Functional Insights

### Na+-dependent HP2 gate dynamics

HP2 gate is intrinsically flexible and can spontaneously open in the apo state. Na+ binding to the Na1 and Na3 sites occurs via a conformational selection-like mechanism rather than induced fit. HP2 opening precedes Na+ binding, and Na+ occupancy at Na1 and Na3 stabilizes the fully open HP2 conformation.

### Electrostatic Na+:substrate coupling

Na+ ions bound at Na1 and Na3 sites facilitate aspartate binding through long-range electrostatic attraction, ensuring strict 3:1 Na+:substrate transport stoichiometry even when HP2 is open. This represents a second, direct coupling mechanism in addition to allosteric regulation.

### Conserved residues mediating gating

Key residues R397 and M311 serve as mediators of Na+-dependent HP2 gating. R397 moves upward upon Na1 binding, while M311 flips upon Na3 occupancy to lock HP2 in the fully open state. Both residues are highly conserved across the glutamate transporter family.

### Na+ binding pathways

Na1 binding occurs through an extracellular pathway accessible upon HP2 opening. Na3 binding can occur via two pathways: (1) transient Na1 occupation followed by hopping to Na3, or (2) direct binding through a narrow hydrophobic pathway lined by M311 and M362 that becomes accessible upon HP2 opening.


## Cross-References

- [Human Excitatory Amino Acid Transporter 1 (EAAT1)](/xray-mp-wiki/proteins/slc-transporters/eaat1/) — GltPh is the prokaryotic homolog of human EAATs and shares the same elevator transport mechanism
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Used as the LCP matrix for GltPh crystallization
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in gltph text
- [TBOA](/xray-mp-wiki/reagents/tboa/) — Referenced in gltph text
