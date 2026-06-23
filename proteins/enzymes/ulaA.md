---
title: UlaA Vitamin C Transporter (E. coli)
created: 2026-06-09
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2975]
verified: false
---

# UlaA Vitamin C Transporter (E. coli)

## Overview

UlaA is the membrane-embedded transporter component of the phosphoenolpyruvate-dependent phosphotransferase system (PTS) for vitamin C (L-ascorbic acid) uptake in Escherichia coli. It belongs to the PTS-AG (ascorbate and galactitol) superfamily and, together with the IIB-like UlaB and IIA-like UlaC enzymes, is responsible for the anaerobic uptake of vitamin C and its phosphorylation to L-ascorbate 6-phosphate. UlaA forms a homodimer and exhibits a completely new fold consisting of 11 transmembrane segments arranged into a 'V-motif' domain and a 'core' domain. The V motifs form the dimer interface, and the core-domain residues coordinate vitamin C. The crystal structures of UlaA in two conformations — outward-open (1.65 A, C2 space group) and occluded (2.35 A, P2_1 space group) — reveal that substrate transport may occur via an 'elevator' mechanism involving rigid-body rotation of the core domain relative to the V-motif domain.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.2975 | 4RP7 | 1.65 A | C2 | Full-length E. coli UlaA (residues 1-441) with C-terminal His8 tag; limited [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) proteolysis removed C-terminal 7 residues and His8 tag during crystallization; purified in [DM](/xray-mp-wiki/reagents/detergents/dm/) (DM) and crystallized with [NG](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) (beta-NG) additive | L-Ascorbic acid (vitamin C) bound at the core-domain substrate-binding site |
| doi/10.1038##nsmb.2975 | 4RP6 | 2.35 A | P2_1 | Full-length E. coli UlaA (residues 1-441); same construct as C2 form; crystallized with beta-NG additive | L-Ascorbic acid (vitamin C) bound at the core-domain substrate-binding site |

 - Data collection: Data collected at SSRF BL17U, SPring-8 BL41XU, or NSLS X29A; processed with HKL2000; structure solved by [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) using gold and platinum derivatives
 - Data collection: Data collected at SSRF BL17U, SPring-8 BL41XU, or NSLS X29A; processed with HKL2000; structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using C2 form as search model

## Expression and Purification

- **Expression system**: E. coli C43(DE3) cells
- **Construct**: Full-length UlaA from E. coli with C-terminal His8 tag; cloned into pET15b or pET21b vectors

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and induction | Bacterial expression |  |  | C43(DE3) cells grown to OD600 ~1.2; induced with 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) |
| Cell lysis | French press |  | 25 mM Tris-Cl pH 8.0, 150 mM NaCl | Two passes at 15,000 p.s.i.; low-speed spin followed by high-speed ultracentrifugation to isolate membranes |
| Membrane solubilization | Detergent extraction |  | 25 mM Tris-Cl pH 8.0, 150 mM NaCl + 1% (w/v) [NM](/xray-mp-wiki/reagents/detergents/nm/) (NM) | Incubated for 1 h at 4 C; insoluble material removed by centrifugation |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA agarose | 25 mM Tris-Cl pH 8.0, 150 mM NaCl, 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.3% NM | Protein eluted with [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); concentrated for gel filtration |
| Size-exclusion chromatography | Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 25 mM Tris-Cl pH 8.0, 150 mM NaCl, 2 mM ascorbic acid + 0.3% NM | Peak fraction collected for crystallization |


## Crystallization

### doi/10.1038##nsmb.2975

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Truncated UlaA (C-terminally cleaved) purified in 1.0% (w/v) n-octyl-beta-D-glucopyranoside (beta-OG) |
| Reservoir | 0.1 M MES pH 6.5, 0.1 M NaCl, 30% (v/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 |
| Temperature | 18 C |
| Growth time | 5 days |
| Cryoprotection | Direct flash freezing in cold nitrogen stream at 100 K |
| Notes | Initial C2 crystals diffracted to 4 A. Resolution improved to 1.65 A (C2) and 2.35 A (P2_1) by adding [NG](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) (beta-NG) at 0.4% (v/v) final concentration. Platinum or gold derivatives obtained by soaking native crystals in 10 mg/ml K2Pt(NO2)4 or 2 mg/ml KAu(CN)2 for 2 h. |


## Biological / Functional Insights

### First structure of the PTS-AG superfamily

UlaA is the first determined structure of any member of the PTS-AG (ascorbate and galactitol) superfamily. The structure reveals a completely new fold distinct from the previously solved PTS-GFL superfamily member ChbC. Each UlaA protomer contains 11 transmembrane segments organized into a V-motif domain (TM1-5) and a core domain (TM6-11, including two reentrant hairpins HP1 and HP2). The V motifs form the dimer interface, while the core domains contain the substrate-binding site.

### Vitamin C coordination and binding

Vitamin C (L-ascorbic acid) is bound at the interface between the V-motif and core domains through polar and van der Waals contacts. The substrate is deeply buried in a pocket formed by residues from the core domain. The high-resolution 1.65 A structure reveals precise coordination geometry involving hydrogen bonds and hydrophobic interactions that confer specificity for L-ascorbic acid with low-micromolar affinity (Km ~9 uM).

### Elevator transport mechanism

Comparison of the outward-open (C2) and occluded (P2_1) conformations suggests that UlaA employs an 'elevator' mechanism for substrate transport. The V-motif domain remains largely stationary while the core domain undergoes a rigid-body rotation of approximately 4.33 degrees relative to the V motif, with a maximum atom translation of ~7 A. The substrate-binding site within the core domain is not perturbed during this movement. This mechanism is a specialized form of the alternating-access mechanism, similar to sugar transport in the PTS-GFL transporter ChbC.

### Domain architecture and dimer interface

UlaA functions as a homodimer, with the V motifs from each protomer forming the dimer interface. The core domain from each protomer is organized around the substrate-binding site. The domain architecture features V motif 1 (cyan), core 1 (yellow), V motif 2 (magenta), core 2 (orange), and TM11 (gray) subdomains. The contracted lengthy loop connecting HP2a and AH2 likely stretches to keep the V-motif and core domains together during elevator motion.

### Structural distinction from PTS-GFL transporters

The UlaA fold is completely different from that of ChbC (a GFL superfamily PTS transporter), demonstrating that the PTS-AG and PTS-GFL superfamilies have distinct evolutionary origins despite performing similar functions. UlaA homologs are found in numerous human and animal pathogens but not in archaea or eukaryotes, making UlaA a potential antimicrobial target.


## Cross-References

- [Uracil:Proton Symporter UraA (E. coli)](/xray-mp-wiki/proteins/slc-transporters/uraA/) — Both are E. coli transporters; UraA belongs to the NAT/NCS2 family, which includes mammalian vitamin C transporters (SVCT1/SVCT2)
- [Elevator Transport Mechanism](/xray-mp-wiki/concepts/elevator-mechanism/) — Central mechanistic finding of this paper; proposed elevator mechanism for substrate translocation
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — General framework for transporter function; elevator mechanism is a specialized form
- [L-Ascorbic Acid (Vitamin C)](/xray-mp-wiki/reagents/ligands/ascorbic-acid/) — Physiological substrate of UlaA; bound in both crystal structures
- [Hanging-Drop Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion-hanging-drop/) — Crystallization method used for UlaA
- [Multiple Isomorphous Replacement with Anomalous Scattering (MIRAS)](/xray-mp-wiki/methods/structure-determination/miras/) — Experimental phasing method used for initial UlaA structure
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
