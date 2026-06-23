---
title: Human Prostaglandin E Receptor EP4
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41589-018-0131-3]
verified: false
---

# Human Prostaglandin E Receptor EP4

## Overview

The prostaglandin E2 receptor EP4 (EP4) is a class A G protein-coupled receptor (GPCR) for prostaglandin E2 (PGE2). EP4 couples primarily to Gs and Gi proteins and plays important roles in inflammation, pain, cancer, and bone metabolism. The crystal structure of the human EP4 receptor was determined in complex with the antagonist ONO-AE3-208 at 3.2 A resolution (PDB 5YWY), revealing the molecular basis of ligand recognition at the lipid-bilayer interface. The structure was enabled by a thermostabilized construct with an ICL3 deletion and double mutation A62L/G106R, in complex with the Fab001 antibody fragment for crystallization in lipidic cubic phase.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41589-018-0131-3 | 5YWY | 3.2 A | C2221 | Human EP4 with ICL3 deletion (residues 243-263 replaced by GG), thermostabilizing mutations A62L (2.47) and G106R (3.39), N-terminal HA signal peptide and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), C-terminal octa-histidine tag, complexed with Fab001 antibody fragment | ONO-AE3-208 (antagonist) |
| doi/10.1038##s41589-018-0131-3 | 5YFI | 1.85 A | P212121 | Fab001 antibody fragment alone | -- |

## Expression and Purification

- **Expression system**: HEK293S GnTI- cells
- **Construct**: Human EP4 with ICL3 deletion (243-263 replaced by GG), N-terminal HA signal peptide and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), C-terminal octa-histidine tag, thermostabilizing mutations A62L (2.47) and G106R (3.39)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | HEK293S GnTI- cell expression | — |  | Cells expressing EP4 harvested, membranes prepared by ultracentrifugation |
| Solubilization | Detergent solubilization | — |  | Membranes solubilized in buffer containing detergent |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA |  | C-terminal octa-histidine tag used for affinity capture |
| Antibody complex formation | Incubation with Fab001 | — |  | Purified EP4 mixed with excess Fab001 antibody fragment for complex formation |
| Size-exclusion chromatography | Size-exclusion chromatography | — |  | Final purification step to isolate EP4-Fab001 complex |


## Crystallization

### doi/10.1038##s41589-018-0131-3

| Parameter | Value |
|---|---|
| Method | Lipidic Cubic Phase (LCP) |
| Protein sample | EP4-Fab001 complex at ~30 mg/mL |
| Temperature | 20 |
| Growth time | Not specified |
| Cryoprotection | Crystals flash-frozen in liquid nitrogen |
| Notes | Crystals grown in LCP using [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/). Data collected at SPring-8 BL32XU. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using Fab001 structure and a GPCR homology model. The structure reveals a ligand-binding pocket at the lipid-bilayer interface formed by TM1, TM2, TM7, and ECL2. |


## Biological / Functional Insights

### Ligand binding at the lipid-bilayer interface

The EP4 crystal structure revealed that the antagonist ONO-AE3-208 binds at an unconventional site at the lipid-bilayer interface, rather than in the canonical GPCR orthosteric pocket. The ligand-binding pocket is formed by TM1, TM2, TM7, and ECL2, with the carboxyl group of ONO-AE3-208 projecting toward the extracellular leaflet of the membrane. This binding mode is distinct from other prostanoid receptors and represents the first structural observation of ligand binding at the GPCR-lipid interface.

### ECL2 forms a beta-hairpin cap

EP4 features a unique extended ECL2 that forms a beta-hairpin structure capping the extracellular side. This beta-hairpin is structurally similar to that found in rhodopsin and is stabilized by extensive intramolecular hydrogen bonds. The ECL2 contributes several residues to the ligand-binding pocket and restricts access to the orthosteric binding site.

### Thermostabilizing mutations enable crystallization

The double thermostabilizing mutation A62L(2.47) and G106R(3.39) was critical for EP4 crystallization. The G106R mutation introduces a guanidinium group that occupies the conserved sodium-binding pocket in Class A GPCRs, mimicking the allosteric sodium ion and stabilizing the receptor in an inactive-like conformation. The A62L mutation enhances hydrophobic packing in TM2.

### Sodium-binding pocket as a target for thermostabilization

The G106R(3.39) mutation places a positively charged arginine side chain in the conserved sodium-binding pocket of class A GPCRs. This pocket is normally occupied by a sodium ion that acts as a negative allosteric modulator. The arginine locks the receptor in the inactive state, similar to mutations found in other thermostabilized GPCRs such as A2AAR S91K.

### Molecular dynamics of ligand access

Metadynamics simulations revealed that ONO-AE3-208 accesses the EP4 binding pocket through a lateral opening between TM1 and TM7 at the lipid-bilayer interface, consistent with the membrane-lateral access model. The simulations captured spontaneous ligand binding events, supporting the crystallographically observed binding pose and revealing the pathway of ligand entry from the membrane.

### Fab001 binding at ECL2 interface

The Fab001 antibody fragment binds to the extracellular surface of EP4, primarily recognizing epitopes on ECL2. The Fab001 interaction stabilizes the beta-hairpin conformation of ECL2 and contributes to crystal packing. Mutagenesis of key ECL2 residues (D167G) disrupted Fab001 binding, confirming the antibody-binding interface.


## Cross-References

- [Prostaglandin Receptors](/xray-mp-wiki/proteins/prostaglandin-receptors/) — EP4 is a member of the prostanoid receptor family
- [G Protein-Coupled Receptors (GPCRs)](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) — EP4 is a class A GPCR
- [GPCR Inactive Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-inactive-conformation/) — The EP4 structure represents an inactive-like receptor conformation
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for EP4-Fab001 crystallization
- [Sodium Ion Allosteric Modulation in GPCRs](/xray-mp-wiki/concepts/signaling-receptors/sodium-allosteric-modulation/) — G106R mutation occupies the conserved sodium-binding pocket
- [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) — N-terminal FLAG tag used for purification
- [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — C-terminal octa-histidine tag for purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Host lipid for LCP crystallization
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
