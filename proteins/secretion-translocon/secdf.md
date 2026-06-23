---
title: "Thermus thermophilus SecDF Protein Translocation Motor"
created: 2026-05-29
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09980, doi/10.1016##j.str.2018.01.002, doi/10.1016##j.celrep.2017.04.030]
verified: false
---

# Thermus thermophilus SecDF Protein Translocation Motor

## Overview

SecDF is a membrane protein belonging to the resistance-nodulation-division (RND) superfamily that enhances protein translocation at the extracytoplasmic side of the bacterial membrane using a proton gradient. It operates as part of the Sec translocon complex, working alongside SecA ATPase and the [SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) channel to drive protein export. The first X-ray crystal structure of full-length SecDF from Thermus thermophilus was determined at 3.3 A resolution (Tsukazaki et al., 2011, PDB 3AQP), revealing 12 transmembrane helices with flexible extracytoplasmic domains (P1-base, P1-head, and P4) and establishing that SecDF is the smallest known motor protein of the RND family. The protein undergoes dramatic conformational transitions between beta-sheet and beta-barrel architectures in its extracellular region, driven by remote coupling between the transmembrane proton transport pathway and the extracytoplasmic domains.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09980 | 3AQP | 3.3 | P43 | Full-length Thermus thermophilus SecDF (residues 2-515 and 522-726); expressed in E. coli | None |
| doi/10.1016##j.str.2018.01.002 | 5YHF | 2.8 | P1 | Thermus thermophilus SecDF residues 1-735 with C-terminal His10 tag; expressed in E. coli BL21(DE3) | None |
| doi/10.1016##j.celrep.2017.04.030 | 5XAM | 2.6 | P2_12_12_1 | Thermus thermophilus SecDF(Met-28-768)-His6 with I143C/L268C mutations; expressed in E. coli BL21(DE3); MolA molecule | None |
| doi/10.1016##j.celrep.2017.04.030 | 5XAN | 2.8 | P2_12_12_1 | Thermus thermophilus SecDF(Met-28-768)-His6 with I143C/L268C mutations; expressed in E. coli BL21(DE3); MolB molecule | [PEG](/xray-mp-wiki/reagents/additives/peg/) fragment (O-(CCO)4) modeled in P1-head cavity |
| doi/10.1016##j.celrep.2017.04.030 | 5XAP | 2.6 | C2 | Thermus thermophilus SecDF(Met-28-768)-His6 with I143C/L268C mutations; expressed in E. coli BL21(DE3); MolC molecule | None |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecDF(1-735)-His10 from plasmid pTV118N; based on NCBI Reference sequence Gene ID 3168575

### Purification Workflow

#### Source: doi/10.1038##nature09980


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | French press | None | Not specified + Not specified | E. coli cells expressing TtSecDF-His6 were disrupted by passage through a French pressure cell |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (His-tag) | Ni-NTA Agarose | Not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | His6-tagged SecDF purified from E. coli membrane fraction in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Size-exclusion chromatography | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | Not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final purification step for crystallization trials |

#### Source: doi/10.1016##j.str.2018.01.002


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (His-tag) | Ni-NTA Agarose | Not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | His10-tagged SecDF purified from E. coli membrane fraction |
| Size-exclusion chromatography | Size-exclusion chromatography | Not specified | Tris buffer + 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final sample in 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for crystallization |

#### Source: doi/10.1016##j.celrep.2017.04.030


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (His-tag) | Ni-NTA Agarose | Not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | DrSecDF(Met-28-768)-His6 purified from E. coli membrane fraction |
| Size-exclusion chromatography | Size-exclusion chromatography | Not specified | 100 mM NH4NO3, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5 + 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final sample in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for crystallization trials |


## Crystallization

### doi/10.1038##nature09980

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | Purified TtSecDF in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) at ~10 mg/mL |
| Reservoir | 28% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 0.5 M NaCl, 0.1 M [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5 |
| Temperature | 20 |
| Growth time | Not specified |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection |
| Notes | PDB 3AQP; F form (original conformation); data collected at SPring-8 BL41XU and PF NW12; refined in space group P43 (pseudo-symmetry from P43212) with 2 molecules per ASU; 50-3.3 A resolution; Rwork/Rfree 0.298/0.319; zonal scaling procedure used to improve electron density; structure includes residues 2-515 and 522-726 |

### doi/10.1016##j.str.2018.01.002

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) |
| Protein sample | Purified SecDF mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) at 1:1 ratio (w/w) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection |
| Notes | 5YHF; Super F form; helical data collection at SPring-8 BL32XU; 1.0 A wavelength; space group P1; 44.1-2.8 A resolution (shell 2.9-2.8 A); Rwork/Rfree 0.202/0.236; 734 protein residues; 5790 non-hydrogen atoms; 132 ligand atoms; 27 solvent molecules |

### doi/10.1016##j.celrep.2017.04.030

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | Purified SecDF with I143C/L268C mutations at ~10 mg/mL |
| Reservoir | 28% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 0.1 M [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 0.5 M NaCl (for P2_12_12_1 crystals) or 40% [PEG](/xray-mp-wiki/reagents/additives/peg/) 200, 0.1 M sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 6.6, 0.1 M Li2SO4 (for C2 crystals) |
| Temperature | 20 |
| Growth time | Not specified |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection |
| Notes | PDB 5XAM, 5XAN, 5XAP; I form crystals; data collected at SPring-8 BL32XU; 1.0 A wavelength; 5XAM (MolA, P2_12_12_1, 2.6 A, Rwork/Rfree 0.188/0.228); 5XAN (MolB, P2_12_12_1, 2.8 A, tunnel-containing conformation); 5XAP (MolC, C2, 2.6 A, Rwork/Rfree 0.189/0.224) |


## Biological / Functional Insights

### First crystal structure of full-length SecDF reveals F-form architecture

The first X-ray crystal structure of full-length SecDF from T. thermophilus was determined at 3.3 A resolution (Tsukazaki et al., 2011, PDB 3AQP), revealing 12 transmembrane helices arranged in a pseudo-symmetrical RND transporter fold. The structure showed two large periplasmic domains (P1, comprising head and base subdomains; P4) connected by flexible linkers. The P1 domain was also solved separately at 2.6 A by X-ray crystallography and the P4 domain by NMR, enabling accurate model building of the full-length structure. The structure established SecDF as the smallest known motor protein of the RND family and provided the first structural framework for understanding how SecDF uses proton motive force to drive protein translocation.

### I-form structures reveal tunnel formation in the transmembrane region

The crystal structures of SecDF in the I form (PDB 5XAM, 5XAN, 5XAP) at 2.6-2.8 A resolution revealed a novel penetrating tunnel through the transmembrane region in the MolB conformation (5XAN). This tunnel is formed by an approximately 4 A shift of TM5 relative to other I-form molecules (MolA, MolC) and the F form. The tunnel center exhibits a negative electrostatic potential arising from the conserved essential Asp365 residue. MD simulations showed that deprotonation of Asp365 attracts water molecules from the cytoplasmic bulk phase, leading to outward TM5 shift and tunnel formation. The conserved Tyr662 residue, whose side chain fluctuates between orientations observed in MolA vs MolB/MolC, is essential for providing sufficient space for tunnel formation. These findings demonstrate that the I-form tunnel functions as a proton pathway, with water molecules forming single-file hydrogen-bonded chains through the tunnel when Asp365 is deprotonated.

### P1-head cavity captures substrate peptides during translocation

The I-form structures revealed a cavity in the P1-head domain that interacts with a polyethylene glycol molecule (modeled as O-(CCO)4 in the 5XAN structure), potentially mimicking a substrate peptide. The P1-head cavity in the I form is larger than in the F form, suggesting that the I form holds substrates more stably. Site-directed photo-crosslinking experiments with pBPA confirmed that the P1-head cavity interacts with translocating polypeptides, supporting a model where the P1-head captures the emerging polypeptide from the [SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) translocon during protein translocation.

### Super-membrane-facing (Super F) form reveals beta-barrel architecture

The crystal structure of SecDF (PDB 5YHF) reveals a novel conformation termed the Super-membrane-facing (Super F) form, in which the extracytoplasmic P1-base and P4 domains adopt a beta-barrel architecture instead of the beta-sheet structure seen in the previously reported F form (PDB 3AQP) and I form structures. This drastic structural transition represents the most extreme conformational change observed in SecDF to date.

### Remote coupling mechanism links proton transport to conformational transitions

The Super F form structure reveals a conserved salt bridge between Asp340 in transmembrane helix 4 (TM4) and Arg671 in transmembrane helix 10 (TM10), with their C-alpha-C-alpha distance reduced from 12.9 A in the F form to 2.6 A in the Super F form.

### Conserved transmembrane regions D1, D5, F1, and F2 transmit structural changes

Comparison of the F form and Super F form structures reveals that highly conserved regions D1, D5, F1, and F2 play an important role in transmitting structural changes from the transmembrane region to the extracytoplasmic side.

### SecDF functions as a proton-activated protein translocation motor

The original 2011 study demonstrated that SecDF conducts protons through its transmembrane region, with conserved charged residues Asp340 and Arg671 being essential for proton transport. Patch-clamp analysis of TtSecDF-containing spheroplasts showed a slope conductance of approximately 102 pS at -60 mV, corresponding to a flow of 4.2 x 10^7 protons per second. The P1 domain was shown to bind unfolded proteins (casein) in a dose-dependent manner, confirming its role in capturing emerging preproteins from the [SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) translocon.


## Cross-References

- [Thermus thermophilus SecYEG Translocon Complex](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) — SecDF operates at the extracytoplasmic side of the SecYEG channel to pull precursor proteins during translocation
- [RND Efflux Pumps](/xray-mp-wiki/concepts/transport-mechanisms/rnd-efflux-pumps/) — SecDF belongs to the RND superfamily; structural insights into remote coupling mechanism
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid used for LCP crystallization of SecDF (PDB 5YHF)
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for SecDF Super F form structure determination
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in purification or crystallization
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
