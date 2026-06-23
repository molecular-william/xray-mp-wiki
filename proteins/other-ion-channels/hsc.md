---
title: HSC (Hydrosulfide Channel from Clostridium difficile)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10881]
verified: false
---

# HSC (Hydrosulfide Channel from Clostridium difficile)

## Overview

HSC (hydrosulfide channel) is a pentameric membrane channel from Clostridium difficile that selectively transports hydrosulfide (HS-) ions across the cell membrane. With a molecular weight of approximately 28,538 Da, HSC forms a symmetrical pentamer in which each protomer contains ten transmembrane helices arranged from five tandemly repeated helical hairpins with inverted pseudo-two-fold symmetry. The cytoplasmic surface of HSC is highly positive, which helps attract HS- ions. The channel possesses a selectivity filter with structural similarity to the FocA formate channel, and unlike FocA, HSC appears to be locked in a closed state. HSC belongs to the FNT (formate/nitrite transporter) family of anion channels.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10881 | Not specified in paper text | 2.2 A | P212121 | Full-length HSC from Clostridium difficile | None specified |
| doi/10.1038##nature10881 | Not specified in paper text | 3.2 A | P21 | Full-length HSC from Clostridium difficile | None specified |
| doi/10.1038##nature10881 | Not specified in paper text | 3.0 A | C2221 | Full-length HSC from Clostridium difficile | None specified |
| doi/10.1038##nature10881 | Not specified in paper text | 2.3 A | P212121 | HSC K16S mutant | None specified |
| doi/10.1038##nature10881 | Not specified in paper text | 2.5 A | P212121 | HSC L82V mutant | None specified |
| doi/10.1038##nature10881 | Not specified in paper text | 2.4 A | P212121 | HSC T84A mutant | None specified |
| doi/10.1038##nature10881 | Not specified in paper text | 2.1 A | P212121 | HSC K148E mutant | None specified |
| doi/10.1038##nature10881 | Not specified in paper text | 2.0 A | P212121 | HSC F194I mutant | None specified |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length HSC from Clostridium difficile
- **Notes**: Expressed and purified for structural studies; molecular weight confirmed by MALDI-TOF mass spectrometry as 28537.8 Da

### Purification Workflow

- **Expression system**: Escherichia coli

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | Not specified in supplementary information | — |  | Purified protein analyzed by SEC for thermostability screening and by MALDI-TOF mass spectrometry |

**Final sample**: HSC protein in unspecified buffer


## Crystallization

### doi/10.1038##nature10881

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Wild type HSC |
| Notes | High pH crystal form; 2.2 A resolution structure viewed from periplasmic side |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Wild type HSC |
| Notes | Neutral pH crystal form |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Wild type HSC |
| Notes | Low pH crystal form |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | HSC K16S mutant |
| Notes | Salt-bridge-triad mutant |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | HSC L82V mutant |
| Notes | Point mutant |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | HSC T84A mutant |
| Notes | Disrupts His201-Thr84 hydrogen bond |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | HSC K148E mutant |
| Notes | Salt-bridge-triad mutant disrupting upper triad |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | HSC F194I mutant |
| Notes | Point mutant |


## Biological / Functional Insights

### Pentameric channel architecture

HSC forms a symmetrical pentamer with five identical protomers. The 2.2 A resolution structure from the high pH crystal form (pH 9.0) shows that all five protomers are structurally identical. Each protomer contains ten transmembrane helices arranged from five tandemly repeated helical hairpins, creating a twofold inverted symmetry between the N- and C-terminal halves of the protein.

### Positively charged cytoplasmic surface for HS- attraction

The cytoplasmic surface of HSC is highly positive, which helps attract HS- ions. Electrostatic surface representations generated in Pymol using the APBS plugin with -20 to 20 kT/e- electrostatic potential show a stark contrast with FocA from Vibrio cholerae, whose cytoplasmic surface lacks this strong positive potential.

### Selectivity filter structure

HSC possesses a selectivity filter with structural similarity to the FocA formate channel. Residues at the selectivity filter of HSC are superimposable with equivalent residues from FocA, suggesting a conserved mechanism for anion selectivity within the FNT family.

### Closed channel state

Pore radius calculations using HOLE software indicate that HSC is in its closed state. The pore radius shows red-colored constrictions that are impermeable to water, with the narrowest point below the 1.1 A boundary typically regarded as the threshold between open and closed states for water channels.

### Salt-bridge-triad mutants do not open the channel

Mutations disrupting the salt-bridge triad (K16S and K148E) did not cause conformational changes that opened the channel, as shown by HOLE pore calculations. The K148E mutant disrupts the upper triad (E200-K148-N205), while the K16S mutant disrupts the lower triad (N86-E81-K16). Neither mutation alone was sufficient to open the channel gate.

### His201-Thr84 hydrogen bond mutation does not open channel

The T84A mutant disrupts the His201-Thr84 hydrogen bond but did not cause large-scale conformational change to open the channel. The equivalent hydrogen bond between conserved residues in Vibrio cholerae FocA is believed to be important for the gating mechanism of that channel by formate concentration, suggesting different gating mechanisms between HSC and FocA.

### Thermostabilization by anions

Apparent melting temperatures of HSC were determined by fitting peak heights from [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) to a Boltzmann sigmoidal curve. Various anions were tested: control 53.3 C, Na2SO3 53.8 C, NaHCO3 57.1 C, NaCl 57.3 C, NaNO2 58.5 C, NaHS 61.7 C. The melting temperature increased progressively with different anions, with NaHS providing the highest [Protein Thermostabilization](/xray-mp-wiki/concepts/construct-design/thermostabilization/).

### pH-independent crystal structure

Backbone superimposition of HSC crystal structures from high pH (pH 9.0), neutral pH (pH 7.5), and low pH (pH 4.5) reveals that the three crystal structures are nearly identical, indicating that HSC does not undergo large conformational changes across the pH range tested.


## Cross-References

- [FocA (Formate Channel A from Vibrio cholerae)](/xray-mp-wiki/proteins/other-ion-channels/focA-vibrio-cholerae/) — Related FNT family channel; structural and functional comparison in the paper
- [HiTehA (TehA from Haemophilus influenzae)](/xray-mp-wiki/proteins/other-ion-channels/hiteha/) — Related anion channel; structural comparison within FNT superfamily
- [FNT Family (Formate/Nitrite Transporter Family)](/xray-mp-wiki/concepts/transport-mechanisms/fnt-family/) — HSC belongs to the FNT family of anion channels
- [Ion Channel Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — HSC selectivity filter compared with FocA in the paper
- [Thermal Shift Assay (Fluorescent CPM)](/xray-mp-wiki/methods/quality-assessment/thermal-shift-assay/) — Thermostability screening by SEC with Boltzmann curve fitting
- [Protein Thermostabilization](/xray-mp-wiki/concepts/construct-design/thermostabilization/) — Related biological concept
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
