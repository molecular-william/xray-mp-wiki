---
title: Human Equilibrative Nucleoside Transporter 1 (hENT1)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-019-0245-7]
verified: false
---

# Human Equilibrative Nucleoside Transporter 1 (hENT1)

## Overview

hENT1 (SLC29A1) is the founding member of the SLC29 family of equilibrative nucleoside transporters. It mediates the energy-independent facilitative diffusion of adenosine and other nucleosides across cellular membranes, playing crucial roles in adenosine signaling, nucleoside salvage for DNA/RNA synthesis, and cellular uptake of nucleoside-derived anticancer and antiviral drugs. hENT1 is the target of adenosine reuptake inhibitors (AdoRIs), clinically used as vasodilators and antithrombotic agents. The crystal structures of hENT1 in complex with [Dilazep](/xray-mp-wiki/reagents/ligands/dilazep/) and [NBMPR](/xray-mp-wiki/reagents/ligands/nbmpr/) revealed an 11-TM helix architecture with a pseudo-symmetric 6+5 topology distinct from the canonical 12-TM [MFS](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) fold, representing the first experimental structures of any SLC29 family member.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41594-019-0245-7 | 6OB7 | 2.3 A | P3_221 | hENT1_cryst (mutations L168F, P175A, N288K, loop [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) Delta243-274) | [Dilazep](/xray-mp-wiki/reagents/ligands/dilazep/) |
| doi/10.1038##s41594-019-0245-7 | 6OB6 | 2.9 A | P6_1 | hENT1_cryst (mutations L168F, P175A, N288K, loop [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) Delta243-274) | [NBMPR](/xray-mp-wiki/reagents/ligands/nbmpr/) (S-(4-Nitrobenzyl)-6-thioinosine) |

## Expression and Purification

- **Expression system**: HEK293S GnTI-/- cells, BacMam viral transduction
- **Construct**: Codon-optimized hENT1_cryst with C-terminal GFP-FLAG-His10 tag in [PEG](/xray-mp-wiki/reagents/additives/peg/) BacMam vector. hENT1_cryst contains mutations L168F, P175A, N288K and TM6-7 loop [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) Delta243-274. Cleavable by Precission Protease.

- **Notes**: Cells harvested 72 h post-infection
- **Induction**: 10 mM [Sodium Butyrate](/xray-mp-wiki/reagents/additives/sodium-butyrate/) + 10 uM [Dilazep](/xray-mp-wiki/reagents/ligands/dilazep/) (for dilazep-bound) at 24 h post-infection

### Purification Workflow

- **Expression system**: HEK293S GnTI-/- cells
- **Expression construct**: hENT1_cryst-GFP-FLAG-His10
- **Tag info**: FLAG-His10 tag, cleaved by Precission Protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent extraction | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.5 mM TCEP + 40 mM n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | 1 hour solubilization, followed by centrifugation at 16,000 rpm for 25 min |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | FLAG M2 affinity | FLAG M2 affinity resin | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.5 mM TCEP, 1.0 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 1.0 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | High salt wash (500 mM NaCl) then low salt wash, elution with 0.2 mg/mL FLAG peptide. 10 uM [Dilazep](/xray-mp-wiki/reagents/ligands/dilazep/) or [NBMPR](/xray-mp-wiki/reagents/ligands/nbmpr/) included throughout. |
| Tag cleavage and deglycosylation | Protease treatment | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.5 mM TCEP + 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | 1:10 Precission Protease and 1:10 [ENDOH](/xray-mp-wiki/reagents/additives/endoh/) for 2 hours at 0.75 mg/mL |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.5 mM TCEP + 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | 10 uM [Dilazep](/xray-mp-wiki/reagents/ligands/dilazep/) or 1.0 uM [NBMPR](/xray-mp-wiki/reagents/ligands/nbmpr/) included in gel filtration buffer. For apo (proteoliposome), 5 mM DM used in final step. |


## Crystallization

### doi/10.1038##s41594-019-0245-7

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | 40:60 (w/w) |
| Temperature | 20 |
| Growth time | 3-5 days ([Dilazep](/xray-mp-wiki/reagents/ligands/dilazep/)); 7 days ([NBMPR](/xray-mp-wiki/reagents/ligands/nbmpr/)) |
| Cryoprotection | Directly cooled in LN2 |
| Notes | Dilazep-bound: Concentrated to 40 mg/mL, mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) 40:60. Reservoir: 35-50% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 0.1 M [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) pH 9.0, 0.5 M NaCl. Plate-like crystals 50x20 um appeared after 12 h. For [NBMPR](/xray-mp-wiki/reagents/ligands/nbmpr/): Reservoir 30% [PEG](/xray-mp-wiki/reagents/additives/peg/) 500 MME, 0.1 M MgCl2, 0.1 M [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0.
 |


## Biological / Functional Insights

### SLC29 family architecture

hENT1 is composed of 11 transmembrane helices with a pseudo-symmetric 6+5 topology, distinct from the canonical 12-TM [MFS](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) fold. The N-domain (TM1-TM6) and C-domain (TM7-TM11) form the central cavity accessible from the extracellular side. An extracellular thin gate (Met33-Pro308) and intracellular thick gate (including Arg111-Glu428 salt bridge) define the outward-facing conformation.

### Adenosine reuptake inhibitor mechanisms

[Dilazep](/xray-mp-wiki/reagents/ligands/dilazep/) occupies the orthosteric site and an opportunistic site 1 at the extracellular thin gate, sterically preventing gate closure and locking the transporter in an outward-facing state. [NBMPR](/xray-mp-wiki/reagents/ligands/nbmpr/), an adenosine analog, occupies the orthosteric site and an opportunistic site 2 (a deep hydrophobic pocket in the N-domain), allowing thin gate closure but preventing domain reorientation. Gly154 in opportunistic site 2 is a key determinant of [NBMPR](/xray-mp-wiki/reagents/ligands/nbmpr/) isoform specificity.

### Nucleoside recognition

Adenosine recognition by hENT1 involves conserved charged residues Arg345 and Asp341 for ribose coordination, Gln158 for nucleobase recognition (N-1/N-3 coordination), and hydrophobic contacts (Leu26, Met89, Leu92, Leu442) surrounding the purine moiety. Leu442Ile mutation converts nucleoside preference from adenosine to uridine.


## Cross-References

- [SLC29 Family of Nucleoside Transporters](/xray-mp-wiki/concepts/transport-mechanisms/slc29-family/) — hENT1 is the founding member of the SLC29 family
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — hENT1 utilizes rocker-switch-like reorientation for transport
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization and purification detergent
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Method used to crystallize hENT1
- [MFS](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) — Related biological concept
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [ENDOH](/xray-mp-wiki/reagents/additives/endoh/) — Additive used in purification or crystallization buffers
