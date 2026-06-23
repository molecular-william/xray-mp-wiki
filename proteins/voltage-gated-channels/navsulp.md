---
title: "NavSulP (Sulfitobacter pontiacus Voltage-Gated Sodium Channel)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms1797]
verified: false
---

# NavSulP (Sulfitobacter pontiacus Voltage-Gated Sodium Channel)

## Overview

NavSulP is a prokaryotic voltage-gated sodium channel (NavBac) cloned from
Sulfitobacter pontiacus. As a homotetrameric channel, each subunit contains six
transmembrane alpha-helices (S1-S6), with S5 and S6 forming the pore domain and
S1-S4 forming voltage sensors. NavSulP exhibits a typical inward sodium current
with half-maximum potentials for activation at -31.2 mV and inactivation at
-62.1 mV. The C-terminal region of NavSulP forms a four-helix bundle (4HB)
that plays critical roles in stabilizing the channel tetramer and accelerating
the channel inactivation rate. The 4HB was visualized by grafting the NavSulP
C-terminal region into the C-terminus of the NaK channel and determining the
crystal structure at 3.2 A resolution. The 4HB connects directly to the inner
helix of the pore domain and promotes the conformational change of the inner
helix required for inactivation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms1797 | 3VOU | 3.2 | P3121 | NaK-NavSulP C239 chimera channel (NavSulP C-terminal region grafted into NaK channel) | None |

## Expression and Purification

- **Expression system**: Escherichia coli KRX strain (Promega)
- **Construct**: Full-length NavSulP with C-terminal His-tag

### Purification Workflow

- **Expression system**: E. coli KRX (Promega)
- **Expression construct**: Full-length NavSulP with C-terminal His-tag
- **Tag info**: C-terminal His-tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression | — |  | Cells grown at 37 C to OD600 of 0.8, induced with 0.1% rhamnose, grown for 16 h at 18 C |
| Cell lysis | French Press | — | TBS (20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl) | Cells suspended in TBS buffer and lysed at 12,000 psi |
| Membrane collection | Ultracentrifugation | — | TBS | Membranes collected by centrifugation at 100,000g for 1 h at 4 C |
| Solubilization | Detergent solubilization | — | TBS with 40 mM [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) (Anatrace) + 40 mM [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) |  |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | HIS-Select cobalt affinity gel (Sigma) | TBS + 3 mM [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) + 0.1 mg/ml [E. coli Polar Lipids](/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/) + 3 mM [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) | Washed with 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 150 mM NaCl, 20 mM HEPES-NaOH pH 8.0 + 3 mM [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) + 0.1 mg/ml [E. coli Polar Lipids](/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/) + 3 mM [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) | Final purification step in gel filtration buffer |


## Crystallization

### doi/10.1038##ncomms1797

| Parameter | Value |
|---|---|
| Protein sample | NaK-NavSulP C239 chimera channel |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystal structure of the NaK-NavSulP C239 chimera at 3.2 A resolution. Space group P3121. Data collected at BL38B1 in SPring-8 with approval of JASRI (Proposal numbers 2009B1211, 2010A1270, 2010A1803, 2010B1232). Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using NaK structure (PDB 2AHY) as search model. |


## Biological / Functional Insights

### C-terminal four-helix bundle stabilizes the channel tetramer

The C-terminal region of NavSulP (residues 239-260) forms a four-helix bundle (4HB) that stabilizes the tetrameric channel. The 4HB is composed of hydrophobic residues forming a hydrophobic core. Mutations of interface residues (V246R, L250R, I253R, L257R) destabilized the tetramer and reduced the inactivation rate. The NavSulP DeltaC239 deletion mutant migrated predominantly as monomers in size-exclusion chromatography and crosslinking analysis, confirming that the C-terminal region is essential for tetramer stability.

### Four-helix bundle accelerates channel inactivation

Deletion of the C-terminal region (NavSulP DeltaC239) dramatically reduced the inactivation rate by approximately 40-fold (tau_inact = 1,701 ms vs 40.6 ms for wild-type at 0 mV). Point mutations in the 4HB hydrophobic core similarly reduced inactivation rates. The 4HB is directly connected to the inner helix (S6) of the pore domain via a conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residue (G221). The G221A mutation, which increases inner helix rigidity, also severely reduced inactivation (tau_inact = 1,850 ms), suggesting the 4HB promotes inactivation by facilitating conformational changes in the inner helix.

### Distinct inactivation mechanism from potassium channels

Unlike [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), where the C-terminal bundle reduces inactivation, the NavSulP 4HB accelerates inactivation. This suggests that the inactivation mechanism of prokaryotic sodium channels (NavBacs) differs from the C-type inactivation of potassium channels. The 4HB generates a counter force on the inner helix that promotes conformational changes leading to pore inactivation. The selectivity filter of NavSulP, which features an elaborate intersubunit hydrogen-bond network (as seen in [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/)), may collapse during inactivation promoted by the 4HB through inner helix conformational changes.

### Role of Lys249 in intersubunit interactions

The 4HB involves specific intersubunit interactions, including a salt bridge of Lys249 with Glu251 and Glu254 of adjacent subunits. Mutation K249E reduced the inactivation rate to a level similar to the C-terminal deletion mutant, while E251K and E254K mutations alone did not significantly reduce inactivation. This suggests Lys249 interacts with other residues in addition to Glu251 and Glu254 for accelerating channel inactivation.


## Cross-References

- [NavAb Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — Prokaryotic voltage-gated sodium channel homolog from Arcobacter butzleri, used for structural comparison (PDB 3RVZ)
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Related protein structure
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Buffer component in purification or crystallization
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) — Detergent used in purification or crystallization
- [E. coli Polar Lipids](/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/) — Additive used in purification or crystallization buffers
