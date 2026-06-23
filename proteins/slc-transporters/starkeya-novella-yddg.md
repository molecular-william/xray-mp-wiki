---
title: "Starkeya novella YddG (SnYddG)"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17991]
verified: false
---

# Starkeya novella YddG (SnYddG)

## Overview

SnYddG is a member of the drug/metabolite transporter (DMT) superfamily from the bacterium Starkeya novella. It functions as an amino acid exporter, expelling aromatic amino acids and exogenous toxic compounds to maintain cellular homeostasis. The crystal structure was determined at 2.4 A resolution in an outward-facing conformation, revealing a novel membrane transporter topology with ten transmembrane segments arranged as two five-helix inverted repeats related by two-fold pseudo-symmetry. The overall structure is basket-shaped with a large central substrate-binding cavity. The DMT superfamily comprises more than 32 families of membrane transporters ubiquitously found in eukaryotes, bacteria, and archaea.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature17991 | 5KJF | 2.4 A | P2 | SnYddG with C-terminal (His)8 tag and TEV protease cleavage site | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (in LCP matrix) |

## Expression and Purification

- **Expression system**: E. coli Rosetta2 (DE3)
- **Construct**: S. novella yddG gene (gi:502932551) cloned from S. novella genomic DNA (strain JCM 20403) into a pET-derived plasmid with C-terminal (His)8 tag and TEV protease cleavage site. Overexpressed and induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 2 h at 37 C.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption and membrane isolation | Cells disrupted with Microfluidizer, membrane fractions collected by ultracentrifugation at 12,000g followed by ultracentrifugation at 200,000g | -- | -- + -- | Cells grown in LB medium with 50 ug/mL [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) |
| Solubilization | Membrane solubilization | -- | 50 mM HEPES (pH 7.0), 300 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 1 mM PMSF + 1.2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.24% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Insoluble material removed by ultracentrifugation at 150,000g for 30 min |
| Ni-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (Ni-NTA resin, QIAGEN) | Ni-NTA resin (QIAGEN) | 50 mM HEPES (pH 7.0), 300 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 1.2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.24% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 1.2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | (His)8 tag cleaved by TEV protease at 4 C overnight |
| Second Ni-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) to remove TEV protease and uncleaved protein | Ni-NTA resin | 50 mM HEPES (pH 7.0), 300 mM NaCl, 1.2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.24% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 1.2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | (His)8 tag-cleaved protein collected in flow-through |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Gel-filtration chromatography ([Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) Increase 10/300 GL, GE Healthcare) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) Increase 10/300 GL (GE Healthcare) | 20 mM HEPES (pH 7.0), 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Protein concentrated to ~15 mg/mL using Amicon Ultra 50K filter (Millipore) |


## Crystallization

### doi/10.1038##nature17991

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | 15 mg/mL SnYddG in 20 mM HEPES (pH 7.0), 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Twin-syringe mixing method for protein-LCP mixture. Sandwich-drop crystallization on 96-well glass plates using Gryphon LCP (Art Robbins Instruments). Initial hits optimized by hanging-drop method on siliconized glass coverslips. Data collected at SPring-8 BL32XU beamline. Space group P2 with cell dimensions a=105.84, b=84.65, c=112.25 A, alpha=90, beta=108.46, gamma=90. Rwork/Rfree 0.2264/0.2495 for 50-2.4 A data. Molecule B selected from asymmetric unit based on best electron density quality. |


## Biological / Functional Insights

### Novel 10-TM topology with inverted structural repeats

SnYddG comprises 10 alpha-helical transmembrane segments arranged as four pairs of two
consecutive segments forming two-helix hairpins: TM1-TM2, TM3-TM4, TM6-TM7, and TM8-TM9,
arranged alternately to surround the central cavity. The N-half (TM1-TM5) and C-half
(TM6-TM10) surround the cavity in anticlockwise and clockwise manners respectively, as
viewed from the periplasmic side. TM5 and TM10 form a four-helix bundle with TM4 and TM9,
sealing one side of the central cavity. The N and C halves share weak sequence similarity
but superimpose with an r.m.s.d. of 2.7 A for 90 C-alpha atoms, related by two-fold
pseudo-symmetry with an axis running parallel to the membrane. This topology is unique
and completely different from those of other known membrane transporters.

### Central substrate-binding cavity

The central cavity deeply penetrates the inner leaflet of the membrane and is formed by
six transmembrane segments: TM1, TM3, TM4, TM6, TM8 and TM9. At the bottom of the cavity,
strictly conserved Trp residues (Trp17 in TM1, Trp101 in TM4a, Trp163 in TM6) form the
binding site floor. The cavity wall is created by conserved hydrophobic residues including
Leu20 (TM1), Phe40 (TM2), and Phe225 (TM8). A hydrogen-bonding network involving the
main-chain carbonyl of Phe225 and side chains of His70, Tyr166, Ser170, and Asp229 captures
water molecules, suggesting dynamic interactions during the transport cycle.

### Intracellular gate mechanism

The intracellular gate is sealed by tight interactions among conserved residues including
Phe94 (TM4b), His97 (TM4b), Tyr99 (TM4b), Val237 (TM9a), and other weakly conserved
hydrophobic residues. A hydrogen-bonding network between Phe225 main-chain carbonyl and
side chains of His70, Tyr166, Ser170, and Asp229 captures water molecules, suggesting
that these interactions are impermanent and can dissociate during the transport cycle.
Arg171 (TM6) and Lys233 (TM8) form hydrogen bonds with main-chain carbonyl groups in the
TM8-TM9a and TM6-TM7 loops, sealing the intracellular side of the gate.

### Alternating-access conformational change

Based on the intramolecular symmetry between N and C halves, a structural model for the
inward-facing state was proposed. In this model, the intracellular gate interactions
observed in the outward-facing crystal structure are completely dissociated, opening the
pathway toward the intracellular side while the extracellular gate remains occluded.
Molecular dynamics simulations (500 ns each for outward-to-occluded and occluded-to-inward
transitions) support this model. The transport mechanism involves bending and straightening
of transmembrane helices, particularly TM3 and TM4, during the outward-inward conformational
change.

### Evolutionary relationship to SMR family

Bioinformatics analyses suggest the small multidrug resistance (SMR) family is the progenitor
of DMT proteins. The crystal structure of [EMRE](/xray-mp-wiki/proteins/abc-transporters/emre/) (PDB 3B5D), the best-characterized SMR family
member, reveals a dimeric architecture with four-transmembrane segment protomers. Despite
no detectable sequence similarity and different transmembrane topologies, superimposition of
the transmembrane helices of YddG and the [EMRE](/xray-mp-wiki/proteins/abc-transporters/emre/) dimer reveals good structural alignment
(r.m.s.d. of 2.9 A over 127 C-alpha atoms), supporting the evolutionary relationship
between four-transmembrane SMR and ten-transmembrane DMT proteins.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent (1.2% for solubilization, 0.03% for SEC purification) used throughout SnYddG purification
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Lipid additive (0.24% for solubilization, 0.006% for SEC) used to stabilize SnYddG during purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used as LCP matrix (2:3 protein-to-lipid ratio) for SnYddG crystallization
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer (50 mM pH 7.0 for solubilization, 20 mM pH 7.0 for SEC) used in SnYddG purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Eluent (20 mM) used in Ni-NTA affinity chromatography for SnYddG purification
- [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) — Used to cleave C-terminal (His)8 tag from SnYddG at 4 C overnight
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Size-exclusion chromatography resin (Superdex 200 Increase 10/300 GL) used for final SnYddG purification step
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for SnYddG structure determination via twin-syringe mixing with monoolein
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
