---
title: Chloride Ion Rhodopsin from Nonlabens marinus (CIR)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms12677]
verified: false
---

# Chloride Ion Rhodopsin from Nonlabens marinus (CIR)

## Overview

Chloride ion rhodopsin (CIR) from the flavobacterium Nonlabens marinus S1-08T is a light-driven inward chloride pump belonging to the NTQ rhodopsin family. The protein comprises seven transmembrane helices and is covalently bound to all-trans retinal via a Schiff base at Lys235. CIR contains a distinctive NTQ motif (Asn98-Thr102-Gln) in its putative ion conduction pathway, which distinguishes it from other microbial light-driven ion pumps. High-resolution crystal structures at 2.0 A and 1.56 A resolutions reveal two chloride-binding sites and provide insights into the chloride ion transduction pathway.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms12677 | 5G28 | 2.0 A | Not specified in paper | CIR from Nonlabens marinus S1-08T, wild-type, seven transmembrane helices | all-trans retinal (covalently bound via Schiff base to Lys235) |
| doi/10.1038##ncomms12677 | 5G54 | 1.56 A | Not specified in paper | CIR from Nonlabens marinus S1-08T, wild-type, seven transmembrane helices | all-trans retinal (covalently bound via Schiff base to Lys235) |
| doi/10.1038##ncomms12677 | 5G2A | Not specified in paper | Not specified in paper | CIR from Nonlabens marinus S1-08T, bromide-soaked crystal | all-trans retinal, bromide ion |
| doi/10.1038##ncomms12677 | 5G2D | Not specified in paper | Not specified in paper | CIR T102N mutant | all-trans retinal |
| doi/10.1038##ncomms12677 | 5G2C | Not specified in paper | Not specified in paper | CIR T102D mutant | all-trans retinal |

## Expression and Purification

- **Expression system**: E. coli BL21-CodonPlus
- **Construct**: CIR from Nonlabens marinus S1-08T, wild-type and various point mutants (N98A, N98D, N98L, T102D, T102N, T102V, P45A, K46A, F15A, W72A, Y83A, Delta255-272)
- **Induction**: 0.5 mM IPTG and 50 uM all-trans-retinal
- **Media**: YT media supplemented with 100 mg/ml ampicillin and 10 mg/ml chloramphenicol

### Purification Workflow

- **Expression system**: E. coli BL21-CodonPlus
- **Expression construct**: CIR from Nonlabens marinus S1-08T, wild-type and mutants

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and induction | Fermentation | -- | YT media with 100 mg/ml ampicillin and 10 mg/ml chloramphenicol + -- | Grown at 37C, induced with 0.5 mM IPTG and 50 uM all-trans-retinal, cultivated for 6h at 30C |
| Cell harvest and wash | Centrifugation | -- | 100 mM NaCl or 100 mM Na2SO4 + -- | Cells collected by centrifugation at 4000g for 5 min, washed three times |
| Buffer exchange | Size-exclusion desalting | PD midiTrap G-25 column (GE Healthcare) | 1% DDM in deionized water + 1% DDM | Buffer-exchange for UV-visible spectroscopy samples |


## Crystallization

### doi/10.1038##ncomms12677

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | CIR from Nonlabens marinus S1-08T, wild-type, solubilized in detergent |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Cryocooled for X-ray data collection |
| Notes | Two crystallization conditions: Type A at pH 6.0 (2.0 A, PDB 5G28) and Type B at pH 4.5 (1.56 A, PDB 5G54). Additional crystals for anomalous dispersion: bromide-soaked (5G2A), T102N (5G2D), T102D (5G2C). |


## Biological / Functional Insights

### Two chloride-binding sites

CIR contains two chloride ion-binding sites. Cl-I is located at the protonated Schiff base (PSB) environment, 3.1 A away from the PSB nitrogen, and interacts directly with PSB through electrostatic and hydrogen-bonding interactions. The conserved Asn98 and Thr102 residues of the NTQ motif are hydrogen-bonded with Cl-I, stabilizing its coordination. Three water molecules (W501, W502, W503) are well-resolved around Cl-I and PSB. Cl-II is a second chloride-binding site on the cytosolic surface, coordinated by Ala44, Pro45, and Lys46 on the A-B loop. Cl-II is hydrogen-bonded with the backbone amide nitrogen of Lys46.

### NTQ motif and chloride pumping mechanism

The NTQ motif (Asn98-Thr102-Gln) is central to chloride ion binding and transport. Asn98 and Thr102 are the only residues directly interacting with Cl-I. Mutagenesis studies show that most mutants (N98A, N98D, N98L, T102D, T102V) eliminate or substantially decrease chloride-pumping activity (less than 50% of wild-type), while T102N retains approximately 70% activity. The chloride pumping mechanism involves: (1) CIR opens to the extracellular side in the resting state; (2) chloride enters through IC1 and reaches the Cl-I binding site in IC2; (3) light absorption induces retinal isomerization; (4) chloride is translocated and released on the cytoplasmic side.

### 3 omega motif and C-terminal helix

CIR contains a 3 omega motif formed by three non-consecutive aromatic amino acids (F15 in TM A, W72 in TM B, Y83 in the B-C loop) that form pi-stacking interactions. CIR also has an additional C-terminal helix after TM G, which is amphipathic and interacts with oleic acid on TM A. The C-terminal helix is important for CIR stability (wild-type Tm: 75C vs Delta C-terminal helix Tm: 61C).

### Chloride transduction pathway

The chloride ion conductive pathway involves three internal cavities (IC1, IC2, IC3). IC1 is below the extracellular surface. IC2 contains four water molecules (W502-W505) and Cl-I, with water molecules forming hydrogen bonds with Thr228, Arg95, and Asp231. IC3 is formed around Gln109 of the NTQ motif on the cytosolic side. A putative chloride entry hole involves residues K2, Ser91, and Gln143.

### Comparison with halorhodopsin and NaR

CIR chloride-binding site at PSB is structurally similar to halorhodopsin (HR) but with key differences: (1) in CIR, Cl-I forms a direct hydrogen bond with PSB; (2) in HR, three well-resolved water molecules form a hydrogen bond network connecting Asp238-Arg108 to the chloride ion-PSB, whereas in CIR there is no such water-mediated network. CIR and NaR structures show that Cl-I in CIR corresponds to Asn112 in NaR. CIR and HR have independently evolved into light-driven chloride pumps with different NTQ and TSA motifs respectively.


## Cross-References

- [Bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhodopsin/) — Archetypal microbial light-driven proton pump with DTD motif
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore covalently bound to Lys235 via Schiff base
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — CIR crystallized using LCP method
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-photocycle/) — CIR functions through a rhodopsin photocycle
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for CIR solubilization
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Used in cell wash buffers
- [Oleic Acid](/xray-mp-wiki/reagents/lipids/oleic-acid/) — Binds to CIR C-terminal helix on TM A
- [NTQ Motif](/xray-mp-wiki/concepts/ntq-motif/) — CIR contains the defining NTQ motif
