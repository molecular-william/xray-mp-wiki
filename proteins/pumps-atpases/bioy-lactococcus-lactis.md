---
title: BioY - Biotin S Component from Lactococcus lactis
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1073##pnas.1203219109]
verified: false
---

# BioY - Biotin S Component from Lactococcus lactis

## Overview

BioY is the biotin-specific S component of the Energy-Coupling Factor (ECF) transporter from [Lactococcus lactis](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter/). It is a six-transmembrane helix integral membrane protein that binds D-biotin with subnanomolar affinity (Kd 0.3 [NM](/xray-mp-wiki/reagents/detergents/nm/)) and delivers it to the ECF module (EcfA-EcfA'-EcfT) for ATP-driven translocation. BioY shares only 16% sequence identity with the thiamin-specific S component [Thit](/xray-mp-wiki/proteins/pumps-atpases/thit/) from the same organism, yet both interact with the same ECF module. The 2.1 A crystal structure revealed that S components contain a structurally conserved N-terminal domain (helices 1-3) involved in ECF module interaction and a highly divergent C-terminal domain (helices 4-6) that binds substrate. The conserved AXXXA motif in helix 1 is essential for ECF module interaction.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1203219109 |  | 2.10 | C2 | SeMet-substituted BioY with N-terminal decahistidine tag | D-biotin |

## Expression and Purification

- **Expression system**: Lactococcus lactis strain NZ9000, grown semi-anaerobically in chemically defined medium (CDM) at 30 C; expression induced with 0.1% nisin A culture supernatant

- **Construct**: N-terminal decahistidine-tagged BioY; SeMet-substituted for crystallography
- **Notes**: Cells grown to OD600 1.5, then resuspended in CDM with SeMet instead of methionine for 20 min before induction. Harvested at OD600 4.


### Purification Workflow

- **Expression system**: L. lactis NZ9000
- **Expression construct**: N-terminal decahistidine-tagged BioY
- **Tag info**: Decahistidine tag (not removed)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Cell disruptor (Constant Systems) | — | 50 mM Na-Hepes pH 7.5, 300 mM NaCl, 10% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Passed twice at 39 kpsi, 4 C. MgSO4 (5 mM) and DNase (100 ug/mL) added prior to disruption. |
| Membrane collection | Ultracentrifugation | — | 50 mM Na-Hepes pH 7.5, 300 mM NaCl, 10% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Unbroken cells removed at 6,000 x g for 15 min. Membranes collected at 267,000 x g for 80 min, resuspended to 40 mg/mL, flash frozen. |
| Solubilization | Detergent solubilization | — | 1% (w/v) dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membranes diluted to 5 mg/mL total protein in buffer A. 1 h at 4 C with gentle rotation. Unsolubilized material removed at 267,000 x g. |
| Affinity chromatography | Ni-Sepharose batch binding | Ni-Sepharose | 50 mM Na-Hepes pH 7.5, 300 mM NaCl, 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.35% (w/v) [NG](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) (NG) | 15 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) added to supernatant before incubation with resin. Washed with 20 CV buffer B. Eluted with 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in buffer B. |
| Size-exclusion chromatography | SEC | Superdex 200 10/300 GL | 20 mM Na-Hepes pH 7.5, 150 mM NaCl + 0.35% (w/v) NG | Peak fractions concentrated to 7 mg/mL using Vivaspin 30 kDa MWCO concentrator. |

**Final sample**: 7 mg/mL in 20 mM Na-Hepes pH 7.5, 150 mM NaCl, 0.35% NG

- **Expression system**: L. lactis NZ9000
- **Expression construct**: N-terminal decahistidine-tagged BioY (biotin-free)
- **Tag info**: Decahistidine tag (not removed)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent solubilization | — | 50 mM potassium-phosphate pH 7.5, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% maltose-neopentyl glycol 3 (MNG-3) | Alternative solubilization for biochemical characterization |
| Affinity chromatography | Ni-Sepharose | Ni-Sepharose | 50 mM potassium phosphate pH 7.5, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.03% MNG-3 | Washed with 20 CV, eluted with 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |


## Crystallization

### doi/10.1073##pnas.1203219109

| Parameter | Value |
|---|---|
| Notes | Crystallization details for SeMet-BioY. Protein at 7 mg/mL in 20 mM Na-Hepes pH 7.5, 150 mM NaCl, 0.35% NG. Crystals belong to space group C2. |


## Biological / Functional Insights

### Conserved N-terminal domain mediates ECF module interaction

BioY and [Thit](/xray-mp-wiki/proteins/pumps-atpases/thit/) share only 16% sequence identity but both interact with the same ECF module. The crystal structure reveals that helices 1-3 form a structurally conserved N-terminal domain (rmsd 5.1 A overall, but helices 1 and 3 superimpose well). The conserved AXXXA motif in helix 1 positions two alanine residues on the lipid-exposed face, essential for interaction with EcfT. This domain architecture explains how structurally divergent S components can interact with the same ECF module.

### Divergent C-terminal domain determines substrate specificity

Helices 4-6 form the highly variable C-terminal domain that binds the substrate. BioY binds D-biotin near the extracellular face, with the ligand mostly occluded except for the carboxylate tail accessible via a narrow tunnel. Biotin interacts with helices 4, 5, and 6 and the loop between helices 3 and 4. The structural divergence of this domain between BioY, [Thit](/xray-mp-wiki/proteins/pumps-atpases/thit/) (thiamin-specific), and [Ribu](/xray-mp-wiki/proteins/pumps-atpases/ribu/) (riboflavin-specific) reflects the chemical diversity of their respective substrates.

### BioY is monomeric and does not transport without ECF module

SEC-MALLS experiments confirm that BioY is monomeric in detergent solution, consistent with other S components ([Thit](/xray-mp-wiki/proteins/pumps-atpases/thit/), [Ribu](/xray-mp-wiki/proteins/pumps-atpases/ribu/)). Solitary BioY binds D-biotin with high affinity (Kd 0.3 [NM](/xray-mp-wiki/reagents/detergents/nm/), 1:1 stoichiometry) but does not transport substrate across the membrane in the absence of the ECF module. This demonstrates that S components are binding proteins that require the ECF module for transport, supporting a unifying mechanism for all ECF transporters.


## Cross-References

- [ECF Transporter (Energy-Coupling Factor Transporter)](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter/) — BioY is the biotin-specific S component of ECF transporters from L. lactis
- [NM](/xray-mp-wiki/reagents/detergents/nm/) — Referenced in the context of NM
- [Thit](/xray-mp-wiki/proteins/pumps-atpases/thit/) — Referenced in the context of Thit
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in the context of DDM
- [NG](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) — Referenced in the context of NG
- [Ribu](/xray-mp-wiki/proteins/pumps-atpases/ribu/) — Referenced in the context of Ribu
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in the context of Glycerol
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in the context of Imidazole
