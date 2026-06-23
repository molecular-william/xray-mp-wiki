---
title: "MtCorB Delta-C from Methanoculleus thermophilus"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-24282-7]
verified: false
---

# MtCorB Delta-C from Methanoculleus thermophilus

## Overview

MtCorB Delta-C is a CNNM/CorB family magnesium transporter from the thermophilic archaeon *Methanoculleus thermophilus*. CNNM/CorB proteins are a broadly conserved family of integral membrane proteins implicated in Mg2+ homeostasis and divalent cation transport, with mutations in human CNNM proteins linked to genetic diseases including hypomagnesemia and Jalili syndrome. This archaeal ortholog shares 26% sequence identity to the conserved core of human CNNM2. The structure was determined in two conformations: an Mg2+-[ATP](/xray-mp-wiki/reagents/ligands/atp) bound state and an apo state (via a disease-mimicking R235L mutant homologous to the human CNNM4 Jalili syndrome mutant R407L). The transmembrane domain exists in an inward-facing conformation with a negatively charged cavity and a conserved pi-helical turn that coordinates a Mg2+ ion. The CBS-pair domain undergoes major conformational rearrangements upon Mg2+-[ATP](/xray-mp-wiki/reagents/ligands/atp) binding, switching from an elongated dimeric configuration to a disc-like dimeric form. Functional liposome-based assays demonstrated direct Mg2+ transport by CorB proteins through an electroneutral antiporter mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-021-24282-7 | 7MSU | 1.60 | P 1 21 1 | MtCorB CBS-pair domain (residues 199-322) in complex with Mg2+-ATP | Mg2+-ATP |
| doi/10.1038##s41467-021-24282-7 | 7M1T | 3.25 | C 1 21 1 | MtCorB Delta-C Delta-loop (residues 5-322) in complex with Mg2+-ATP | Mg2+-ATP, UDM |
| doi/10.1038##s41467-021-24282-7 | 7M1U | 3.80 | P 1 21 1 | MtCorB Delta-C R235L mutant (residues 5-322) in apo state | none |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: MtCorB Delta-C (residues 1-322, C-terminal CorC domain deletion) with internal loop deletion
- **Notes**: Codon-optimized cDNA subcloned into pET29a vector with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag). Expressed in E. coli and purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm), optimized to [UDM](/xray-mp-wiki/reagents/detergents/udm) for crystallization.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1 | Cell lysis by sonication | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.0, 0.5 mM Na-[EDTA](/xray-mp-wiki/reagents/additives/edta), 1 mM [MgCl2](/xray-mp-wiki/reagents/additives/magnesium-chloride) + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Membrane fraction collected by ultracentrifugation |
| 2 | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) ([Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta)) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) Superflow (Qiagen) | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.0, 300 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride), 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) + 0.05% [UDM](/xray-mp-wiki/reagents/detergents/udm) | [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) purification |
| 3 | Size-exclusion chromatography | — | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride) + 0.05% [UDM](/xray-mp-wiki/reagents/detergents/udm) | Final purification step for crystallization |


## Crystallization

### doi/10.1038##s41467-021-24282-7

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | 20 mg/mL MtCorB Delta-C Delta-loop in 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride), 0.05% [UDM](/xray-mp-wiki/reagents/detergents/udm), 5 mM Mg2+-[ATP](/xray-mp-wiki/reagents/ligands/atp) |
| Reservoir | 0.1 M sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate) pH 5.5, 0.1 M Li2SO4, 0.1 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride), 20 mM [MgCl2](/xray-mp-wiki/reagents/additives/magnesium-chloride), 34% [PEG400](/xray-mp-wiki/reagents/additives/peg400), 5 mM [ATP](/xray-mp-wiki/reagents/ligands/atp) |
| Temperature | 293 |
| Notes | Crystals of 7M1T obtained after construct and detergent optimization |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | 20 mg/mL MtCorB Delta-C R235L mutant in 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride), 0.05% [UDM](/xray-mp-wiki/reagents/detergents/udm) |
| Reservoir | 0.1 M sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate) pH 5.5, 50 mM Li2SO4, 11% [PEG400](/xray-mp-wiki/reagents/additives/peg400)0, 10 mM MgSO4 |
| Temperature | 293 |
| Notes | Apo state captured via disease-mimicking R235L mutant |


## Biological / Functional Insights

### Mg2+-ATP sensing and transport mechanism

MtCorB demonstrates a rocker-switch transport mechanism. In the apo state, the CBS-pair domain adopts an elongated dimeric configuration and the acidic helical bundle (AHB) dissociates, forming a CBS-TMD contact that locks the transmembrane domain in the inward-facing conformation, inactivating the transporter. Upon Mg2+-[ATP](/xray-mp-wiki/reagents/ligands/atp) binding, the CBS-pair domain switches to a disc-like dimeric configuration, disrupting the CBS-TMD contact and allowing the transporter to transition to other conformational states required for Mg2+ transport. The Mg2+ ion in the transmembrane cavity is coordinated by Ser21, Ser25, Ser71, Glu111, and main-chain carbonyls of Ser21 and Gly110. A conserved pi-helical turn in TM3 (involving Pro114) is essential for transport activity.

### Direct Mg2+ transport by CorB proteins

Liposome-based Mg2+ transport assays with [MAG](/xray-mp-wiki/reagents/lipids/mag)-fura-2 demonstrated that CorB proteins mediate direct Mg2+ transport, resolving a longstanding debate in the field. The transport occurs through an electroneutral antiporter mechanism, as shown by the lack of [Valinomycin](/xray-mp-wiki/reagents/ligands/valinomycin)-sensitive enhancement (unlike the electrogenic CorA channel). Mutations near the pi-helical turn (S117A, E118A, P121G, K122A) consistently reduced transport activity, while mutations in the Mg2+ binding site (S26A, S30A, N76A) increased activity.


## Cross-References

- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) — Entity mentioned in text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm) — Entity mentioned in text
- [EDTA](/xray-mp-wiki/reagents/additives/edta) — Entity mentioned in text
- [ATP](/xray-mp-wiki/reagents/ligands/atp) — Entity mentioned in text
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) — Entity mentioned in text
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride) — Entity mentioned in text
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) — Entity mentioned in text
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes) — Entity mentioned in text
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate) — Entity mentioned in text
- [Valinomycin](/xray-mp-wiki/reagents/ligands/valinomycin) — Entity mentioned in text
