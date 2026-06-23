---
title: "SiaT Sialic Acid Transporter from Proteus mirabilis"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##s41467-018-04045-7]
verified: false
---

# SiaT Sialic Acid Transporter from Proteus mirabilis

## Overview

SiaT is a secondary active sialic acid transporter from the uropathogen Proteus mirabilis, belonging to the sodium solute symporter (SSS) family. It uses Na+ electrochemical gradients to drive the uptake of extracellular sialic acids, which bacteria utilise as an energy source or for molecular mimicry. The substrate-bound outward-open structure of SiaT was determined at 1.95 Å resolution, revealing the LeuT-fold with 14 transmembrane helices and a central substrate-binding site for N-acetylneuraminic acid (Neu5Ac) coordinated by Thr58, Thr63, Ser60, Gln82, and Arg135. A distinctive feature is the identification of two Na+ binding sites: the conserved Na2 site and a newly identified Na3 site positioned close to Na2 but not in contact with the substrate. The Na3 site is conserved in ~19.6% of SSS family members, including hSGLT1 (which transports 2 Na+ per substrate) but not in vSGLT or hSGLT2 (which transport 1 Na+). Molecular dynamics simulations demonstrate that Na3 binding allosterically stabilizes the substrate and pre-organises the binding site. This structure provides the first high-resolution view of a bacterial sialic acid SSS transporter and reveals how stoichiometric variation in Na+ coupling arises within the SSS family.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-018-04045-7 | 5NV9 | 1.95 | C2 | Full-length SiaT from Proteus mirabilis with C-terminal His6 tag | Neu5Ac (N-acetylneuraminic acid), 2 Na+ |
| doi/10.1038##s41467-018-04045-7 | 5NVA | 2.26 | P22_12_1 | Full-length SiaT from Proteus mirabilis with C-terminal His6 tag | Neu5Ac, 2 Na+ |

## Expression and Purification

- **Expression system**: Escherichia coli Lemo21(DE3) (NEB)
- **Construct**: Full-length SiaT from Proteus mirabilis (strain HI4320) with C-terminal His6 tag
- **Notes**: Grown in Terrific Broth with kanamycin (50 µg/mL), chloramphenicol (34 µg/mL), L-rhamnose (250 µM). Induced with 0.4 mM IPTG at 25°C overnight with shaking at 200 rpm. SeMet protein produced using PASM-5052 autoinduction media.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Cell lysis | Emulsiflex-C3 homogenizer at 20,000 psi | — | PBS supplemented with cOmplete EDTA-free protease inhibitors, lysozyme (0.5 mg/mL), DNaseI (5 µg/mL), MgCl2 (2 mM) | Cell debris removed at 24,000×g |
| 2. Membrane preparation | Ultracentrifugation at 235,000×g for 2 h | — |  | Membranes stored at -80°C until use |
| 3. Solubilization | Detergent solubilization for 2 h at 4°C | — | 2% (w/v) DDM | Unsolubilized material removed at 150,000×g |
| 4. Affinity chromatography | Immobilized metal affinity chromatography | Ni-NTA | PBS, 0.03% DDM; eluted with 250-300 mM imidazole in PBS, 0.03% DDM | Purified protein buffer exchanged into PBS, 0.03% DDM |


## Crystallization

### doi/10.1038##s41467-018-04045-7

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | Purified SiaT at ~9 mg/mL in PBS, 0.03% DDM |
| Reservoir | 0.1 M HEPES pH 7.5, 30% PEG 400, 0.2 M MgCl2 (SeMet crystals); varying conditions for native crystals |
| Temperature | 20°C |
| Notes | Cryoprotection: 30% PEG 400 in mother liquor. SeMet data from 13 crystals merged using BLEND. Native data collected from space group P22_12_1. Structure determined by SeMet-SAD at 1.95 Å. |


## Biological / Functional Insights

### LeuT-fold and outward-open conformation

SiaT adopts the canonical LeuT-fold with 14 transmembrane helices (Tm0-Tm13) arranged in two inverted five-helix repeats (Tm1-Tm5 and Tm6-Tm10). The structure is in an outward-open conformation with a substrate-binding site accessible from the extracellular side. The substrate Neu5Ac is coordinated by residues from Tm1 (Thr58, Leu59, Ser60, Thr63) and Tm2 (Gln82), and forms a salt bridge with Arg135 from Tm3.

### Neu5Ac substrate binding site

The sialic acid N-acetylneuraminic acid (Neu5Ac) is bound in an extended conformation with its N-acetyl group pointing toward Tm10. Key interactions include hydrogen bonds with Thr58 (hydroxyl of Neu5Ac), Thr63 (glycerol moiety), Ser60, and Gln82, plus a salt bridge between Arg135 and the carboxylate group of Neu5Ac. Water-mediated hydrogen bonds further stabilize binding via Gln82, Asn247, Gln250, and Phe78. Binding affinity measured by MST (Kd = 58 ± 1 µM) and ITC (Kd = 50 ± 4 µM). SiaT also binds Neu5Gc (Kd = 85 ± 2 µM) but much more weakly binds KDN (Kd > 10 mM).

### Na2 sodium binding site

The Na2 site is the conserved sodium binding site found in all LeuT-fold transporters. It is located ~7 Å from the substrate between Tm1 and Tm8 at a prominent kink in Tm1. The Na+ is coordinated by the backbone carbonyls of Leu59, Gly61, and Ser342, and the side chain hydroxyls of Ser342 and Ser343. This site is universally conserved among SSS family members.

### Na3 novel sodium binding site

A second Na+ binds to a newly identified Na3 site positioned close to the Na2 site but not contacting the substrate. The Na3 site is coordinated by Asp182 (side chain), Ser345 and Ser346 (side chain hydroxyls), and Ser342 (main chain carbonyl). Bioinformatic analysis of 39,612 SSS sequences shows Na3 is present in 19.6% of sequences (4,212) including hSGLT1 (2 Na+:1 substrate) but absent in vSGLT and hSGLT2 (1 Na+:1 substrate). The Na3 site is unique to a SSS family subgroup and distinct from the Na1/Na1' sites found in LeuT, dDAT, and BetP.

### Allosteric role of Na3 in substrate binding

Molecular dynamics simulations demonstrate that Na3 binding allosterically stabilizes the substrate without directly coordinating it. When both Na2 and Na3 are bound, Neu5Ac remains stably bound. In the absence of Na3, the substrate shows higher conformational flexibility. The Na3 site may help pre-organise the binding site through effects on the Leu59 backbone (φ/ψ angles), which in turn affects the unwound region of Tm1 that coordinates the substrate.

### Structural basis for Na+ stoichiometry variation in SSS family

The discovery of the Na3 site provides a structural explanation for the variable Na+:substrate stoichiometry within the SSS family. Members with the Na3 site (conserved D182, S345, S346) can couple 2 Na+ per transport cycle, while those lacking the Na3 site (conserved hydrophobic residues at corresponding positions) couple only 1 Na+. This suggests that evolutionary acquisition of the Na3 site allows transporters to harness additional energy from the Na+ gradient, enabling transport against steeper substrate concentration gradients.

### Inward-open model and gating mechanism

An inward-open model of SiaT was generated using molecular dynamics, showing predicted movement of transmembrane helices. The periplasmic gate helices (Ilh0, Tm7, Tm8, Tm10) close during the transition, while the cytoplasmic gate opens via movement of Ilh0, Tm1, Tm6, and Tm8. Arg260 (Tm6) stabilizes the inner gate in a closed conformation through interactions with Ser53, Asp256, and Ser346. The inward-open model reveals how the alternating access mechanism operates in this SSS family member.


## Cross-References
