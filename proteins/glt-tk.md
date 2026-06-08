---
title: GltTk (Glutamate Transporter Homologue from Thermococcus kodakarensis)
created: 2026-05-29
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1021##jacs.0c11336, doi/10.1038##ncomms13420]
verified: false
---

# GltTk (Glutamate Transporter Homologue from Thermococcus kodakarensis)

## Overview

GltTk is a homotrimeric glutamate transporter homologue from the archaeon Thermococcus kodakarensis. It belongs to the SLC1A family of excitatory amino acid transporters and functions as a Na+-coupled glutamate transporter. GltTk operates via the elevator transport mechanism, where a transport domain undergoes large-scale conformational changes to move substrate across the membrane. Crystal structures have been solved at high resolution in both substrate-bound and substrate-free states, revealing the strict coupling mechanism between three sodium ions and aspartate binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##jacs.0c11336 | not specified in paper | not specified in paper | not specified in paper | His-tagged wild-type GltTk | p-OMe-azo-TBOA (trans isomer) |
| doi/10.1021##jacs.0c11336 | not specified in paper | not specified in paper | not specified in paper | His-tagged wild-type GltTk | p-OMe-azo-TBOA (cis isomer) |
| doi/10.1021##jacs.0c11336 | not specified in paper | not specified in paper | not specified in paper | His-tagged wild-type GltTk | ONB-hydroxyaspartate |
| doi/10.1038##ncomms13420 | 5E9S | 2.8 | not specified in paper | His8-tagged wild-type GltTk | L-aspartate, three Na+ ions (Na+1, Na+2, Na+3) |
| doi/10.1038##ncomms13420 | 5DWY | 2.7 | not specified in paper | His8-tagged wild-type GltTk (apo) | none |

## Expression and Purification

- **Expression system**: Escherichia coli MC1061
- **Construct**: C-terminally His8-tagged GltTk, expressed from pBAD24-derived plasmid, induced with 0.05% L-arabinose

### Purification Workflow

*Source: doi/10.1021##jacs.0c11336*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification in apo state | Wild-type GltTk purified in apo state in 10 mM HEPES KOH pH 8.0, 100 mM KCl, 0.15% DM, supplemented with 300 mM NaCl. Concentrated to ~7 mg/mL using Vivaspin 5000 MWCO centrifugal filter (Vivaproducts). | -- | 10 mM HEPES KOH pH 8.0, 100 mM KCl, 0.15% DM, 300 mM NaCl + 0.15% DM (n-dodecyl-beta-D-maltoside) | Concentrated to ~7 mg/mL; supplemented with 300 mM NaCl before crystallization |

### Purification Workflow

*Source: doi/10.1038##ncomms13420*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | E. coli MC1061 cells cultivated in LB medium (37 C, 200 rpm), expression induced with 0.05% L-arabinose for 3 h. Harvested, membrane vesicles prepared. Solubilized in n-Dodecyl-beta-D-Maltopyranoside (DDM). Centrifuged at 4 C, 265,000 g for 30 min. | -- | DDM-containing buffer + n-Dodecyl-beta-D-Maltopyranoside (DDM) | For apo-GltTk, Na+ omitted from all buffers |
| Ni-affinity chromatography | Supernatant incubated with Ni-Sepharose pre-equilibrated with 50 mM Tris HCl pH 8, 300 mM KCl, 0.15% DM, 15 mM imidazole pH 8. Washed with 60 mM imidazole. Eluted with 500 mM imidazole. | Ni-Sepharose (GE Healthcare, 0.5 ml bed volume) | 50 mM Tris HCl pH 8, 300 mM KCl, 0.15% DM, 500 mM imidazole pH 8 + 0.15% DM (n-Decyl-beta-D-Maltopyranoside) | His8-tagged GltTk captured via Ni-affinity |
| Size-exclusion chromatography | Further purified by SEC on Superdex 200 10/300 GL (GE Healthcare) column. | Superdex 200 10/300 GL | 10 mM Hepes KOH pH 8, 100 mM KCl, 0.15% DM + 0.15% DM (n-Decyl-beta-D-Maltopyranoside) | Final purified sample |


## Crystallization

### doi/10.1038##ncomms13420

| Parameter | Value |
|---|---|
| Method | not specified in paper |
| Protein sample | GltTk in presence of aspartate and sodium ions |
| Reservoir | not specified in paper |
| Temperature | not specified in paper |
| Growth time | not specified |
| Cryoprotection | not specified in paper |
| Notes | Substrate-bound structure (GltTk^sub), PDB 5E9S, 2.8 A resolution. Well-defined electron density for all loops and N-termini. Trimeric organization with transport domains in outward-occluded position. |

| Parameter | Value |
|---|---|
| Method | not specified in paper |
| Protein sample | Substrate-free GltTk (apo-GltTk) |
| Reservoir | not specified in paper |
| Temperature | not specified in paper |
| Growth time | not specified |
| Cryoprotection | not specified in paper |
| Notes | Apo structure (GltTk^apo), PDB 5DWY, 2.7 A resolution. Improved crystals over previous substrate-free form. Used as molecular replacement model. |


## Biological / Functional Insights

### Coupled binding mechanism of three sodium ions and aspartate

GltTk exhibits strict coupling between the binding of three sodium ions and aspartate. Isothermal titration calorimetry confirmed binding of three sodium ions per aspartate molecule (slope of -2.8 in Na+ concentration dependence). The binding order is: Na+1 and Na+3 bind first (possibly in random or obligatory route order), followed by aspartate, and finally Na+2 binds last. This ordered binding ensures tight coupling between ion and substrate transport, preventing uncoupled ion flux. The Na+3 site has the shortest interaction distances (~2.2-2.4 A) indicating tighter binding, while Na+2 site has lower affinity and is the last to bind and first to leave.

### Three sodium binding sites and their coordination

Three distinct sodium binding sites were identified at high resolution. Na+1 is coordinated by the beta-carboxylate of D409 (TMS8), main-chain carbonyls of G309 and N313 (unwound TMS7), and N405 (TMS8). Na+2 is coordinated by main-chain carbonyls of S352, I353, T355 (HP2) and T311 (TMS7), with the sulfur of M314 within interacting distance (<3 A). Na+3 is coordinated by hydroxyls of T94 and S95 (TMS3), the carboxamide of N313, the carboxylate of D315 (TMS8), and the main-chain carbonyl of Y91 (TMS3). The Na+3 site location matches predictions from MD simulations and mutagenesis studies on mammalian transporters.

### HP2 gate dynamics and sodium coupling

The HP2 loop (connecting TMS7 and TMS8) acts as an extracellular gate. Its tip displays enhanced local flexibility in the absence of ligands. The loop wraps around the outer face of the transport domain, preventing excessive HP2 movements while allowing small-scale motions required for substrate and sodium access. Binding of Na+2 closes the gate, enabling the transport domain to reorient to the inward-facing state. M314 at the HP2 tip is highly mobile, pointing away from the binding site in the apo state and toward it in the substrate-bound state.

### Structural basis of sodium-aspartate cooperativity

Sodium binding at Na+1 and Na+3 sites triggers conformational changes that create the aspartate binding site. Sodium binding moves the NMDGT region of TMS7, placing T317 in optimal position for aspartate binding and forcing R401 to reorient, which creates space for aspartate and orients its guanidium group to interact with the aspartate beta-carboxylate. Additionally, Na+3 binding pushes TMS3 toward TMS7, further positioning T317. This explains the cooperativity between Na+ and aspartate binding observed in ITC experiments.


## Cross-References

- [GltPh (Glutamate Transporter Homologue from Pyrococcus horikoshii)](/xray-mp-wiki/proteins/glt-ph/) — Archaeal homologue with 77% sequence identity; similar Na+-coupled aspartate transport mechanism
- [L-Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) — Canonical substrate; ITC shows GltTk binds three Na+ ions per aspartate molecule
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for GltTk membrane solubilization during purification
- [Decyl Maltoside](/xray-mp-wiki/reagents/detergents/decyl-maltoside/) — DM (n-decyl-beta-D-maltopyranoside) used at 0.15% in purification buffers
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — HEPES KOH pH 8 used in SEC buffer for GltTk purification
- [Potassium Chloride (KCl)](/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/) — KCl used in purification buffers (300 mM in affinity, 100 mM in SEC)
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Imidazole gradient (15-500 mM) used for His8-tag elution from Ni-Sepharose
- [Elevator Mechanism](/xray-mp-wiki/concepts/elevator-mechanism/) — GltTk operates via the elevator transport mechanism with large-scale conformational changes of the transport domain
