---
title: Human Smoothened Receptor (SMO)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12167, doi/10.1038##ncomms15383, doi/10.1038##ncomms5355]
verified: false
---

# Human Smoothened Receptor (SMO)

## Overview

The human smoothened (SMO) receptor is a class frizzled (class F) G-protein-coupled receptor (GPCR) and a key signal transducer in the hedgehog signalling pathway. SMO is responsible for the maintenance of normal embryonic development and is implicated in carcinogenesis. It shares the seven-transmembrane helical fold with class A GPCRs but has less than 10% sequence identity and distinct structural features. The structure reveals an unusually complex arrangement of long extracellular loops stabilized by four disulphide bonds.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12167 | 4FBP | 2.5 | P212121 | BRIL-ACRD-SMO-deltaC (BRIL fused to N-terminus of S190, C-terminus truncated at Q555) | LY2940680 |
| doi/10.1038##ncomms15383 | 5V56 | 2.90 | P21 | SMO-FLA fusion (residues 53-558, E194M, FLA fused to ICL3, N-term HA-FLAG-10xHis-TEV, C-term 10xHis) | TC114 |
| doi/10.1038##ncomms15383 | 5V57 | 3.00 | P21 | SMO-FLA fusion (residues 53-558, FLA fused to ICL3, N-term HA-FLAG-10xHis-TEV, C-term 10xHis, N-term further truncated by 5 residues) | TC114 |
| doi/10.1038##ncomms5355 | 4N4W | 2.80 | C2221 | BRIL-deltaCRD-SMO-deltaC (BRIL fused to ICL3 at P434-K440, residues S190-Q555) | SANT1 |
| doi/10.1038##ncomms5355 | 4QIM | 2.60 | P212121 | BRIL-deltaCRD-SMO-deltaC (BRIL fused to ICL3 at P434-K440, residues S190-Q555) | Anta XV |
| doi/10.1038##ncomms5355 | 4QIN | 2.60 | C2 | BRIL-deltaCRD-SMO-deltaC (BRIL fused to ICL3 at P434-K440, residues S190-Q555) | SAG1.5 |

## Expression and Purification

- **Expression system**: Sf9 insect cells (Spodoptera frugiperda)
- **Construct**: BRIL-ACRD-SMO-deltaC chimera: thermally stabilized apocytochrome b562 RIL (BRIL) fused to the truncated N-terminus of human SMO receptor (starting at residue 5190); extracellular cysteine-rich domain (CRD) and ECD linker domain included; C-terminus truncated at Q555. N-terminus: HA signal, Flag tag, 10xHis tag, TEV protease site.


### Purification Workflow

*Source: doi/10.1038##nature12167*

- **Expression system**: Sf9 insect cells (Spodoptera frugiperda)
- **Expression construct**: BRIL-ACRD-SMO-deltaC
- **Tag info**: HA signal, Flag tag, 10xHis tag, cleaved by His-tagged TEV protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl | Hypotonic buffer; extensive washing with 1.0 M NaCl high osmotic buffer |
| Solubilization | Solubilization | — | 50 mM HEPES pH 7.5, 200 mM NaCl + 1% (w/v) DDM, 0.2% (w/v) CHS | 3-4 h at 4 C; 30 uM LY2940680, 2 mg/ml iodoacetamide added before solubilization |
| IMAC | Immobilized metal ion affinity chromatography | TALON IMAC resin (Clontech) | 50 mM HEPES pH 7.5, 1 M NaCl, 20 mM imidazole + DDM, CHS | Overnight binding at 4 C; wash I buffer: 800 mM NaCl, 0.1% DDM, 0.02% CHS, 8 mM ATP, 20 mM imidazole, 10 mM MgCl2; wash II buffer: 500 mM NaCl, 0.05% DDM, 0.01% CHS, 50 mM imidazole
 |
| Reverse IMAC with TEV cleavage | Immobilized metal ion affinity chromatography | TALON IMAC resin |  | His-tagged tobacco etch virus (TEV) protease used to cleave N-terminal Flag-10xHis tags |

**Final sample**: 50-60 mg/ml in 50 mM HEPES pH 7.5, 300 mM NaCl, DDM, CHS

### Purification Workflow

*Source: doi/10.1038##ncomms15383*

- **Expression system**: HEK293F cells (human embryonic kidney 293F, suspended culture)
- **Expression construct**: SMO-FLA fusion (residues 53-558, E194M, FLA fused to ICL3 at P434-S443)
- **Tag info**: HA signal, FLAG tag, 10xHis tag at N-terminus (cleaved by TEV), 10xHis tag at C-terminus

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and transfection | Transient transfection | — |  | HEK293F cells transfected with PEI:DNA at 2:1 ratio, cultured at 37 C, collected 48 h post-transfection. 5 uM vismodegib present during expression. |
| Membrane preparation | Cell lysis and membrane fractionation | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, EDTA-free protease inhibitor cocktail | Hypotonic buffer wash; repeated centrifugation (3x) in high salt buffer (1.0 M NaCl) |
| Ligand incubation | Ligand binding | — |  | Membranes incubated with 30 uM TC114 and 2 mg/ml iodoacetamide on rocker at 4 C for 1 h |
| Solubilization | Solubilization | — | 50 mM HEPES pH 7.5, 200 mM NaCl + 1% (w/v) DDM, 0.2% (w/v) CHS | 2.5 h at 4 C |
| IMAC (first capture) | Immobilized metal ion affinity chromatography | TALON IMAC resin (Clontech) | 50 mM HEPES pH 7.5, 200 mM NaCl, 20 mM imidazole, 1.0 M NaCl + DDM, CHS | Overnight binding at 4 C |
| Wash and detergent exchange | Immobilized metal ion affinity chromatography | — | 50 mM HEPES pH 7.5, 800 mM NaCl, 10% glycerol, 0.5% LMNG, 0.1% CHS, 20 mM imidazole, 10 mM MgCl2, 6 mM ATP, 30 uM TC114 + LMNG, CHS | Wash I buffer; 2 h rocker incubation for complete detergent exchange |
| Wash II | Immobilized metal ion affinity chromatography | — | 25 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 0.03% LMNG, 0.006% CHS, 40 mM imidazole, 50 uM TC114 + LMNG, CHS | Six-column volume wash |
| Elution and TEV cleavage | Immobilized metal ion affinity chromatography | — | 25 mM HEPES pH 7.5, 500 mM NaCl, 0.03% LMNG, 0.006% CHS, 250 mM imidazole, 50 uM TC114 | Eluted with high imidazole; TEV protease cleavage of N-terminal tags |

**Final sample**: 25 mM HEPES pH 7.5, 500 mM NaCl, 0.03% LMNG, 0.006% CHS, 50 uM TC114

### Purification Workflow

*Source: doi/10.1038##ncomms5355*

- **Expression system**: Sf9 insect cells (Spodoptera frugiperda)
- **Expression construct**: BRIL-deltaCRD-SMO-deltaC (BRIL fused to ICL3 at P434-K440, residues S190-Q555)
- **Tag info**: N-term 10xHis tag, cleaved by Ni-NTA followed by thrombin protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Baculovirus expression | — |  | Sf9 cells infected with baculovirus containing BRIL-deltaCRD-SMO-deltaC construct |
| Membrane preparation | Cell lysis and membrane fractionation | — | 50 mM HEPES pH 7.5, 100 mM NaCl | Crude membrane fraction isolated |
| Solubilization | Solubilization | — | 50 mM HEPES pH 7.5, 100 mM NaCl + 0.1% DDM | Membranes solubilized in DDM |
| Ni-NTA affinity purification | Immobilized metal ion affinity chromatography | Ni-NTA agarose | 50 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DDM | His-tag captured on Ni-NTA; eluted with imidazole |
| SEC | Size exclusion chromatography | — |  | Purified protein in DDM buffer |

**Final sample**: SMO-ligand complex in DDM buffer


## Crystallization

### doi/10.1038##nature12167

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase |
| Protein sample | 50-60 mg/ml SMO-LY2940680 complex |
| Lipid | monoolein, cholesterol |
| Protein-to-lipid ratio | 40:54:6 (w/w/w) |
| Temperature | 20 |
| Notes | 40 nl protein-laden LCP boluses overlaid by 800 nl precipitant solution; crystals flash frozen in liquid nitrogen; data collected at 23ID-D beamline, Advanced Photon Source, wavelength 1.0330 A; phases obtained by SAD from tantalum bromide derivative
 |

### doi/10.1038##ncomms15383

| Parameter | Value |
|---|---|
| Method | Serial femtosecond crystallography (XFEL) |
| Protein sample | SMO-FLA-TC114 complex |
| Temperature | 20 |
| Notes | XFEL data collection at LCLS (Linac Coherent Light Source, SLAC). Room temperature (20 C). Space group P21. Cell dimensions: a=40.6, b=349.5, c=61.8, beta=101.1 deg. Resolution 24.90-2.90 A. Rsplit=13.3. CC*=0.9986.
 |

| Parameter | Value |
|---|---|
| Method | Synchrotron X-ray crystallography |
| Protein sample | SMO-FLA-TC114 complex |
| Temperature | -196 |
| Notes | Synchrotron data collection at BL41XU, SPring-8. Cryo-cooled (-196 C). Space group P21. Cell dimensions: a=40.1, b=356.4, c=59.1, beta=102.8 deg. Resolution 48.38-3.00 A. Rmerge=11.7. Rwork/Rfree=0.203/0.240.
 |

### doi/10.1038##ncomms5355

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | SMO-ligand complex in DDM |
| Temperature | 20 |
| Notes | Three structures crystallized by sitting drop vapor diffusion: SMO-SANT1 (PDB 4N4W, 2.8 A, C2221), SMO-Anta XV (PDB 4QIM, 2.6 A, P212121), SMO-SAG1.5 (PDB 4QIN, 2.6 A, C2). Crystals grew over 5-14 days at 20 degrees Celsius. Initial phase information obtained by molecular replacement with PHASER using search models from SMO_LY2940680 (PDB 4JKV). Refinements performed with REFMAC5 and autoBUSTER.
 |


## Biological / Functional Insights

### SMO as a Class F GPCR

The SMO receptor is classified as a class frizzled (class F) G-protein-coupled receptor, distinct from class A GPCRs with less than 10% sequence identity. This structure is the first reported for a class F GPCR. The seven-transmembrane helical fold is conserved, but most conserved motifs for class A GPCRs are absent. SMO is an essential component of the canonical hedgehog signalling pathway, which regulates embryonic development in animals.

### Distinct Structural Features Compared to Class A GPCRs

The SMO receptor 7TM fold lacks the most conserved prolines (P5.50, P6.50, P7.50) found in class A GPCRs that have pivotal roles in the activation process. Instead, SMO has an unusually high number of glycines in helices V, VI and VII that may facilitate flexibility and bending during activation. Helix VI is in an inactive-like, closed state in this antagonist-bound structure. The intracellular helix VIII has a distinct interface with helix I compared to class A GPCRs.

### Extracellular Loop Architecture

The SMO receptor features an unusually complex arrangement of long extracellular loops (ECL1, ECL2, ECL3) stabilized by four disulphide bonds. ECL1 is divided into two segments by a disulphide bond and forms a U-shaped loop. ECL2 forms a beta-hairpin deep within the 7TM cavity. ECL3 is the longest loop, forming a protrusion with an extended alpha-helical structure. These loops make extensive contacts with the bound ligand.

### LY2940680 Binding Pocket

The ligand-binding pocket has a long and narrow shape connected to the extracellular aqueous environment through a small opening. LY2940680 binds at the extracellular end of the seven-transmembrane helix bundle and forms extensive contacts with the extracellular loops, particularly ECL2 which is positioned deep within the cavity.

### Comparison with Frizzled Receptors

SMO and frizzled (FZD) receptors share structural features including the extracellular cysteine-rich domain (CRD), ECD linker domain, and 7TM domain. The SMO structure provides insight into FZD receptors, as the disulphide bond pattern in ECL3 is fully conserved in class F members (except FZD4 which has a very short ECL3 loop). The KTXXXW motif in helix VIII is conserved and stabilizes the alpha-helical structure of helix VIII that packs parallel to the membrane.

### Multi-domain Architecture and Allosteric Regulation

The multi-domain SMO structure (SMO-FLA, PDB: 5V56) reveals the complete three-domain architecture: a seven-transmembrane helices domain (TMD), a hinge domain (HD), and an intact extracellular cysteine-rich domain (CRD). This architecture enables allosteric interactions between the CRD and TMD. The CRD exerts an auto-inhibitory effect on receptor basal activity, and agonist binding to the CRD triggers a small tilt that pushes helix VI and ECL3 outward, transmitting the signal to the TMD.

### Unique GPCR Activation Mechanism

The SMO-FLA structure combined with HDX analysis and MD simulations reveals a unique GPCR activation mechanism distinct from other multi-domain GPCRs. Transmembrane helix VI, extracellular loop 3 (ECL3), and the hinge domain (HD) play a central role in signal transmission. Unlike the glucagon receptor (GCGR) which undergoes large-scale ECD swinging motion, SMO CRD motion is limited, with ECL3 acting as the critical modularity region for activation.

### TC114 Binding and Electrostatic Stabilization

The designed ligand TC114 (LY2940680 analogue with 4-nitro substitution) forms a precise electrostatic interaction with K395 on extracellular loop 2 at a distance of 3.4 A. This interaction significantly reduces conformational heterogeneity of the ECL2 beta-hairpin region, enabling successful crystallization of the multi-domain SMO construct. The TC114 binding pocket is located at the extracellular end of the 7TM helix bundle.

### CRD Conformational States and Sterol Binding

Comparison of SMO CRD structures with the Xenopus laevis SMO (xSMO) CRD structures (apo, OHC-bound, cyclopamine-bound) shows that the CRD always adopts a 'closed' conformation in the context of the full multi-domain SMO receptor, regardless of sterol binding. ECL3 interacts with the CRD hydrophobic groove to stabilize the CRD in the closed conformation. Point mutations on ECL3 (N493Q, I496R) lead to constitutive activity, consistent with the self-inhibitory role of CRD.

### Long and Narrow Ligand Binding Pocket

The newly solved structures of SMO bound to SANT1, Anta XV, and SAG1.5 reveal a long and narrow cavity defined by the 7TM helices, ECD, and ECLs. SANT1 binds very deep in the pocket, while other ligands remain closer to the extracellular entrance. The entire long and narrow pocket can be targeted by small molecule ligands. The extracellular entrance can accommodate reporter moieties or bulky groups through a long-chain flexible linker, as demonstrated with KAAD-cyclopamine.

### D473(6.54f) and Chemoresistance Mechanisms

The side chain of D473(6.54f) makes a direct interaction with Anta XV at 3.3 A, while its interaction with LY2940680 is much weaker (4.0 A in molecule A and 4.3 A in molecule B). The D473(6.54f)A mutation causes a >100-fold affinity drop for GDC-0449 and Anta XV, but has modest effect on LY2940680 (<7-fold) and no effect on SANT1. The D473(6.54f)H mutation confers chemoresistance to GDC-0449. These results provide a direct structural explanation for the differential effect of ligand binding pocket mutations on ligands with distinct binding poses.

### Agonist-Induced Conformational Changes

In the SAG1.5-bound structure, the positively charged amino group forms an ionic interaction with D473(6.54f), causing E518(7.38f) to move away and break its interaction with D473. R400(5.43f) moves up to form a hydrogen bond with Q477(ECL3). On the intracellular side, the hydrogen bond between Y262(ICL1) and H361(4.46f) is broken, associated with inward movement of P263(ICL1) contacting W535(7.55f). The W535(7.55f) mutation to leucine causes constitutive activation leading to carcinogenesis. This remodelling at R400, D473, and E518 differentiates the agonist-bound structure from antagonist-bound structures.

### Differential Binding Modes of Anta XV and LY2940680

Although Anta XV and LY2940680 share a phthalazine ring core and similar overall shape, they have distinct binding modes. LY2940680 forms extensive interactions with ECL3 residues (Q477, W480, E481, F484) through pi-pi stacking, while Anta XV does not contact ECL3. The phthalazine core of LY2940680 adopts an axial position in the chair conformation of the piperidine ring, while Anta XV places it in the equatorial position, resulting in a 1 A shift. The shift is associated with a shift at the guanidinium group of R400(5.43f).


## Cross-References

- [Human Beta2-Adrenergic Receptor](/xray-mp-wiki/proteins/beta2-adrenergic-receptor/) — Class A GPCR reference structure for comparison with SMO 7TM fold
- [Human 5-HT2A Receptor](/xray-mp-wiki/proteins/5ht2a-receptor/) — Class A GPCR structure used in comparative analysis
- [LY2940680](/xray-mp-wiki/reagents/ligands/ly2940680/) — Small-molecule antagonist bound in the SMO binding pocket
- [A2A-StaR2-bRIL](/xray-mp-wiki/proteins/a2a-psb1-bril/) — BRIL fusion protein used as crystallization scaffold for class F GPCR
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for SMO receptor crystallization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used in LCP matrix for SMO crystallization
- [TC114](/xray-mp-wiki/reagents/ligands/tc114/) — Designed ligand for multi-domain SMO crystallization (PDB: 5V56, 5V57)
- [SMO-FLA Fusion Construct](/xray-mp-wiki/proteins/smoothened-fla-fusion/) — Engineered SMO-Flavodoxin fusion used for XFEL and synchrotron structure determination
- [Vismodegib (GDC-0449)](/xray-mp-wiki/reagents/ligands/vismodegib/) — FDA-approved SMO antagonist; used in cell expression and structural comparison
- [20(S)-Hydroxycholesterol](/xray-mp-wiki/reagents/ligands/20s-hydroxycholesterol/) — CRD agonist of SMO; structural comparison with CRD-bound states
- [SANT1](/xray-mp-wiki/reagents/ligands/sant1/) — SMO antagonist that binds deep in the pocket; co-crystallized (PDB 4N4W)
- [Anta XV](/xray-mp-wiki/reagents/ligands/anta-xv/) — SMO antagonist with D473(6.54f) interaction; co-crystallized (PDB 4QIM)
- [SAG1.5](/xray-mp-wiki/reagents/ligands/sag1.5/) — SMO agonist inducing conformational changes; co-crystallized (PDB 4QIN)
- [Cyclopamine](/xray-mp-wiki/reagents/ligands/cyclopamine/) — First selective SMO ligand; referenced in structural comparison
- [Vismodegib (GDC-0449)](/xray-mp-wiki/reagents/ligands/gdc-0449/) — FDA-approved SMO antagonist; D473(6.54f)H mutation confers resistance
- [KAAD-cyclopamine](/xray-mp-wiki/reagents/ligands/kaad-cyclopamine/) — BODIPY-tagged cyclopamine derivative demonstrating bulky group accommodation
