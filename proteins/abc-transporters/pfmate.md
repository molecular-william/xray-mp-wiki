---
title: PfMATE (Pyrococcus furiosus Multidrug and Toxic Compound Extrusion Transporter)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12014, doi/10.1073##pnas.1904210116]
verified: false
---

# PfMATE (Pyrococcus furiosus Multidrug and Toxic Compound Extrusion Transporter)

## Overview

PfMATE is a multidrug and toxic compound extrusion (MATE) family transporter from the hyperthermophilic archaeon Pyrococcus furiosus. It functions as an H⁺/drug antiporter, exporting a broad range of xenobiotics including norfloxacin and [Ethidium - Fluorescent Intercalating Dye](/xray-mp-wiki/reagents/ligands/ethidium/) bromide. PfMATE adopts two distinct conformations — a straight outward-open form and a bent form — that are central to its rocker-switch transport mechanism. The structure revealed an acidic cluster (Asp41, Asp184) critical for H⁺ coupling and drug export.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12014 |  | 2.4 | C2 | Full-length wild-type PfMATE | None (straight conformation) |
| doi/10.1038##nature12014 |  | 2.5 | C2 | Full-length wild-type PfMATE | None (bent conformation) |
| doi/10.1038##nature12014 |  | 2.45 | C2 | Full-length wild-type PfMATE | MaL6 macrocyclic peptide |
| doi/10.1038##nature12014 |  | 3.0 | C2 | Full-length wild-type PfMATE | MaD5 macrocyclic peptide |
| doi/10.1038##nature12014 |  | 2.6 | C2 | Full-length wild-type PfMATE | MaD3S macrocyclic peptide |
| doi/10.1038##nature12014 |  | 2.1 | C2 | PfMATE P26A mutant | None |
| doi/10.1038##nature12014 |  | 2.9 | P6 | Full-length wild-type PfMATE | Br-NRF (brominated norfloxacin) |
| doi/10.1073##pnas.1904210116 | 4MLB | 2.35 |  | Full-length wild-type PfMATE, C-terminal TEV-10xHis | None (outward-facing conformation) |
| doi/10.1073##pnas.1904210116 | 6FHZ |  |  | Full-length wild-type PfMATE with P. furiosus native lipid incubation | None (inward-facing conformation) |
| doi/10.1073##pnas.1904210116 | 6GWH |  |  | Full-length wild-type PfMATE | None (outward-facing conformation, LCP crystals) |
| doi/10.1073##pnas.1904210116 | 6HFB |  |  | Full-length wild-type PfMATE | CsCl heavy atom derivative (outward-facing) |

## Expression and Purification

### Purification Workflow

- **Expression system**: E. coli (pBAD-A2 vector)
- **Expression construct**: Full-length PfMATE with C-terminal TEV-10xHis tag
- **Tag info**: C-terminal 10xHis tag, TEV protease cleavable

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and harvest | Fermentation | — |  | Cells grown in LB medium at 37°C to OD600=0.5, induced with 0.02% arabinose |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | — |  | Standard His-tag purification |
| Lipid incubation (for inward-facing structure) | Incubation with total lipid extract from P. furiosus | — |  | Protein incubated with P. furiosus total lipid extract after [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL | 20 mM Hepes-NaOH pH 8.0, 15 mM NaCl, 0.06% (wt/vol) [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) | Copurified with P. furiosus lipids to capture inward-facing conformation |


## Crystallization

### doi/10.1073##pnas.1904210116

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 10 mg/mL PfMATE in 20 mM Hepes-NaOH pH 8.0, 150 mM NaCl, 0.05% (wt/vol) C10E5, 0.15% (wt/vol) octyl-β-D-selenoglucoside |
| Reservoir | 30% (wt/vol) [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/) monomethyl ether, 0.1 M ADA-HCl pH 6.5 |
| Temperature | 291 K |
| Growth time | 20-25 days |
| Cryoprotection | Crystals soaked in 1 M CsCl for heavy atom derivative |
| Notes | Outward-facing conformation (PDB 6HFB). |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | PfMATE in 20 mM Hepes-NaOH pH 8.0, 15 mM NaCl, 0.06% (wt/vol) [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (9.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/)) |
| Protein-to-lipid ratio | 2:3 (vol/vol) |
| Temperature | 295 K |
| Notes | Inward-facing (PDB 6FHZ): 0.1 M NaCl, 0.1 M MgCl2, 30% (vol/vol) [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/), 0.1 M sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 5.0. Outward-facing (PDB 6GWH): 0.1 M NaCl, 30% (vol/vol) PEG500 DME. |


## Biological / Functional Insights

### Rocker-switch mechanism of H⁺-driven drug export

PfMATE operates through a rocker-switch mechanism driven by alternating access between straight (outward-open) and bent conformations. In the drug-binding outward-open state, H⁺ binding to the conserved acidic cluster (Asp41, Asp184) induces bending of transmembrane helix 1 (TM1). This conformational change shifts the protein from the straight to the bent form, extruding the bound drug substrate. H⁺ is released on the intracellular side, and a new drug substrate binds from the inner membrane leaflet or cytoplasm to restart the cycle.

### Macrocyclic peptide inhibition

Three in-vitro selected macrocyclic peptides — MaD5, MaD3S, and MaL6 — inhibit PfMATE by occupying the drug-binding pocket or locking TM1 motion. MaD5 and MaD3S bind the N-lobe cavity, blocking the drug-binding pocket and restricting the rocker-switch motion of TM1. MaL6 binds between the N- and C-lobes at the extracellular entrance and has weaker inhibitory potency. The peptides penetrate the bacterial outer membrane to directly access and inhibit the MATE transporter.

### Inward-facing conformation via native lipids

Crystallization with P. furiosus native lipids (but not E. coli lipids) captured the first inward-facing state of any MATE family transporter (PDB 6FHZ). Transition from outward- to inward-facing involves rigid body movements of TM2-TM6 and TM8-TM12 forming an inverted V, facilitated by bending of TM1 (42° tilt) and TM7 (40° tilt). The intracellular opening is ~26 Å, wider than the ~18 Å extracellular opening.

### Na⁺-binding site and TM1 bending is pH-independent

MD simulations and Cs⁺ anomalous scattering identified a monovalent cation-binding site at Asp41 (coordinated by Asp41, Asn180, Asp184, Thr202). Outward-facing structures at low pH (5.0 and 6.5) by both vapor diffusion and LCP methods showed TM1 remains straight regardless of pH (Cα RMSD 0.64-1.10 Å), demonstrating TM1 bending is pH-independent and likely modulated by lipid interactions rather than protonation.

### Lipid-mediated conformational regulation

MD simulations in archaeal lipid bilayers (DPI, DPG, DPA) showed negatively charged PG lipids entering the positively charged cavity of PfMATE, interacting with Arg284, Arg402, Arg161, Thr399, Asn253, and Gln387. These results suggest specific lipid species modulate the conformational equilibrium, consistent with the model that lipid binding to conserved charged networks can induce conformational switching in secondary active transporters.


## Cross-References

- [MATE Transporter Family](/xray-mp-wiki/concepts/mate-transporter-family/) — PfMATE is a member of the MATE family
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — PfMATE inward- and outward-facing structures support the alternating access model
- [Monoolein (9.9 MAG)](/xray-mp-wiki/reagents/lipids/monoolein/) — Used in LCP crystallization of PfMATE
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Primary buffer used in purification and crystallization
- [Lipidic Cubic Phase (LCP)](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to obtain both inward- and outward-facing structures
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/) — Additive used in purification or crystallization buffers
- [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in purification or crystallization
