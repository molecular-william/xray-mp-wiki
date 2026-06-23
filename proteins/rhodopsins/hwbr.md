---
title: Haloquadratum walsbyi Bacteriorhodopsin (HwBR)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.M115.685065, doi/10.1016##j.str.2016.12.004]
verified: false
---

# Haloquadratum walsbyi Bacteriorhodopsin (HwBR)

## Overview

HwBR is a light-driven proton pump from the square halophilic archaeon Haloquadratum walsbyi,
belonging to the microbial rhodopsin family. The protein comprises seven transmembrane helices
and contains an all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore covalently bound via a Schiff base to Lys224.
Two crystal structures were solved: a trimeric form at 1.85 A resolution and an antiparallel
dimeric form at 2.58 A resolution (PDB 4QI1; Hsu et al., JBC 2015), both in space group C2
using [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/). HwBR could not be classified into any existing
subgroup of archaeal BR proteins based on phylogeny, and was assigned to a new subfamily
named qR (along with HmBRII from Haloarcula marismortui). All structures revealed a unique
hydrogen-bonding network between Arg82 and Thr201 linking the BC and FG loops to shield the
retinal-binding pocket from the extracellular environment, which explains HwBR's remarkable
optical stability under acidic conditions (pH 2-8). The Arg82-Thr201 cap acts as a proton
shield, maintaining the protonation status of the retinal-binding pocket interior even at
low pH values. This was validated by R82E mutation which attenuated optical stability
(pKa shifted from 1.97 to 2.24). HwBR functions as a light-driven proton pump and the
conserved Asp104 (equivalent to Asp96 in HsBR) serves as the proton uptake accelerator.
HwBR was also used as a model membrane protein to demonstrate the SMA-LCP crystallization
approach (Broecker et al., Structure 2017), yielding a 2.0 A structure (PDB 5ITC) virtually
identical to the detergent-based structure.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2016.12.004 | 5ITC | 2.0 A | P3 | Full-length HwBR from Haloquadratum walsbyi, solubilized and purified in SMA copolymer nanodiscs, crystallized in LCP | all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) (covalently bound to Lys224 via Schiff base) |
| doi/10.1016##j.str.2016.12.004 | 5ITE | 2.2 A | P3 | Full-length HwBR, detergent-based purification in OG micelles, crystallized in LCP | all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) (covalently bound to Lys224 via Schiff base) |
| doi/10.1074##jbc.M115.685065 | 4QI1 | 1.85 | C2 | Wild-type HwBR, trimeric form, crystallized in LCP | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length HwBR with double [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Differential centrifugation | -- | Breakage buffer (composition not fully specified) + -- | E. coli inner cell membranes isolated by differential centrifugation |
| Solubilization (SMA approach) | SMA copolymer solubilization | -- | Breakage buffer with [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/) addition + SMA copolymer (styrene-maleic acid) | Membranes solubilized with SMA copolymers. Externally added [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/) (1,2-dimyristoyl-sn-glycero-3-phosphocholine) increased solubilization yield to close to that of [DDM](/xray-mp-wiki/reagents/detergents/ddm/) solubilization. |
| IMAC | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA Superflow (QIAGEN) | 50 mM Tris pH 8, 100 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + SMA (nanodisc-embedded) | Double [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) enabled efficient separation of HwBR-containing SMA nanodiscs from empty nanodiscs. Washed with 10 CV breakage buffer and 10 CV wash buffer. Eluted with 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/). |
| SEC | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL (GE Healthcare) | Breakage buffer + SMA (nanodisc-embedded) | Concentrated in 100 kDa MWCO centrifugal filter unit. Fractions with A550nm signal collected and concentrated to ~13 mg/mL. |


## Crystallization

### doi/10.1016##j.str.2016.12.004

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization - SMA-LCP approach |
| Protein sample | HwBR in SMA nanodiscs at ~13 mg/mL |
| Temperature | 20C |
| Growth time | Not specified |
| Cryoprotection | Crystals harvested from LCP and cryocooled |
| Notes | Protein in SMA nanodiscs was mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) at 2:3 (v/v) protein-to-lipid ratio (60% hydration). LCP bolus remained non-birefringent. Increased LCP viscosity observed with SMA approach. Several hundred conditions screened. Slight protocol modifications needed for LCP robot dispensing and crystal harvesting. Data collection at APS beamlines. |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization - detergent approach (reference) |
| Protein sample | HwBR in OG micelles at ~15.5 mg/mL |
| Temperature | 20C |
| Growth time | Not specified |
| Cryoprotection | Crystals harvested from LCP and cryocooled |
| Notes | Reference structure. Protein purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) micelles and OG micelles, then transferred into [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) LCP. |


## Biological / Functional Insights

### HwBR belongs to a new qR subfamily with acid-resistant proton pumping

Based on phylogenetic analysis of BR protein sequences, HwBR and HmBRII were assigned
to a new subfamily named qR, distinct from existing bR, aR, dR, and cR subgroups.
HwBR showed remarkable optical stability across a wide pH range (pH 2-8), with a
pKa of 1.97 for the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base counterion — significantly lower than the
pKa of ~2.6 for HsBR. This contrasts with most BR proteins which exhibit a marked
red-shift in absorption maximum at acidic pH due to protonation of the Schiff base
proton acceptor (Asp85 in HsBR, Asp93 in HwBR). The D93N fully protonated mutant
showed lambda_max = 581 nm. Light-driven proton pump activity was confirmed using
a photocurrent device and pH electrode measurements.

### Unique Arg82-Thr201 hydrogen-bonding network acts as a proton shield

The 1.85 A crystal structure of HwBR revealed a unique hydrogen-bonding network
between Arg82 (located on the BC loop) and Thr201 (located on the FG loop in the
extracellular region). Two guanidinium nitrogen atoms of Arg82 form hydrogen bonds
with the main-chain carbonyl oxygen of Thr201, creating a beta-hairpin cap covering
the proton translocation channel exit site. This Arg82-Thr201 interaction has never
been observed in any other known BR protein, where the corresponding residues are
typically glutamic acid (e.g., Glu74 in HsBR). The R82E mutant showed a 21-nm red-shift
at pH 2 (lambda_max = 568 nm vs 559 nm for wild-type at pH 2) with an increased pKa of
2.24, confirming the cap's role in shielding the retinal-binding pocket from the
extracellular proton concentration. Time-dependent denaturation assays showed R82E/HwBR
had faster denaturation at pH 8 within 15 min, suggesting the cap contributes to overall
pH-dependent thermal stability.

### Negatively charged cytoplasmic surface drives proton uptake

Electrostatic analysis of HwBR revealed a negatively charged cytoplasmic side with
significantly enlarged surface area compared to other BR proteins. This negatively
charged region may drive the re-uptake of protons from the cytoplasm, potentially
increasing proton uptake efficiency. Combining the Arg82-Thr201 cap on the extracellular
side (protecting the retinal-binding pocket microenvironment) with the negatively charged
cytoplasmic surface (enhancing proton uptake), HwBR appears to be a highly efficient
proton pump optimized for acidic conditions.

### SMA-LCP crystallography preserves native structure

The 2.0 A structure of HwBR obtained from SMA nanodisc-LCP crystallization is virtually identical to the 2.2 A structure from detergent-based LCP crystallization (C-alpha RMSD 0.22 A for the trimer). All key structural features are preserved, including the retinal-binding pocket, proton translocation path residues (Asp93, Glu202, Lys224), and the proton-releasing complex. The SMA copolymer does not compromise diffraction quality or electron density maps.

### Proton translocation pathway

HwBR pumps protons from the intracellular to extracellular side via a conserved mechanism. Key functional residues include Asp93 (proton re-uptake residue), Glu202 (proton-releasing complex), and Lys224 (Schiff base linkage to all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/)). The proton outward cap region involves hydrogen-bonded residues.


## Cross-References

- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — HwBR was crystallized in monoolein LCP for both detergent-based and SMA-based approaches
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-photocycle/) — HwBR is a microbial rhodopsin proton pump with a photocycle mechanism
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — All-trans-retinal chromophore covalently bound to Lys224
- [SMA Nanodisc Purification](/xray-mp-wiki/methods/solubilization/sma-nanodisc-purification/) — Novel polymer-based solubilization and purification method demonstrated with HwBR
- [SMA-LCP Crystallization](/xray-mp-wiki/methods/crystallization/sma-lcp-crystallization/) — Novel polymer-mediated in meso crystallization approach validated with HwBR
- [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/) — Synthetic phospholipid added to improve SMA solubilization efficiency
- [N-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for reference purification and solubilization
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used for reference purification and LCP crystallization
- [Proton Pump Mechanism](/xray-mp-wiki/concepts/proton-pump-mechanism/) — HwBR is a light-driven proton pump with a unique Arg82-Thr201 extracellular cap that shields the retinal pocket at low pH
- [Microbial Rhodopsins](/xray-mp-wiki/concepts/microbial-rhodopsins/) — HwBR belongs to the qR subfamily of archaeal rhodopsins with acid-resistant optical properties
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-photocycle/) — HwBR follows the conserved BR photocycle with Asp104 as the proton uptake accelerator
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — All-trans-retinal chromophore covalently bound to Lys224 via Schiff base
- [pKa Tuning in Membrane Proteins](/xray-mp-wiki/concepts/pka-tuning/) — The Arg82-Thr201 cap tunes the pKa of the Schiff base counterion from ~2.6 in HsBR to 1.97 in HwBR
