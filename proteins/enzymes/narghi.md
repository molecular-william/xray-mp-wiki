---
title: "Nitrate Reductase A (NarGHI) from Escherichia coli"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsb969, doi/10.1074##jbc.M410457200, doi/10.1021##bi049938l]
verified: false
---

# Nitrate Reductase A (NarGHI) from Escherichia coli

## Overview

Nitrate reductase A (NarGHI) is a membrane-bound quinol:nitrate oxidoreductase from Escherichia coli that reduces nitrate to nitrite under anaerobic conditions. The heterotrimeric enzyme (Mr 223,921) is composed of a molybdenum cofactor-containing catalytic subunit (NarG, 1246 residues), an [Fe-S] cluster-containing electron transfer subunit (NarH, 512 residues), and a heme-containing membrane anchor subunit (NarI, 225 residues). NarGHI forms part of a redox loop with formate dehydrogenase N (FdnGHI) to generate a proton-motive force, as proposed by Mitchell's chemiosmotic theory.

The crystal structure solved at 1.9 A resolution reveals eight redox centers aligned on a single chain spanning ~74.5 A, including two b-type hemes, four [4Fe-4S] clusters, one [3Fe-4S] cluster, and a Mo-bisMGD cofactor. A unique finding is the open bicyclic form of the molybdo-bis(molybdopterin guanine dinucleotide) cofactor and a novel fold of the membrane anchor subunit. EPR spectroscopic and crystallographic analysis of the FS0 [4Fe-4S] cluster in NarG revealed a novel His3Cys coordination and a high-spin (S=3/2) ground state.

The structure in complex with the inhibitor pentachlorophenol (PCP) at 2.0 A resolution provided the first molecular characterization of a quinol binding and oxidation site (Q-site) in NarGHI. PCP binds in a narrow hydrophobic cleft (cleft B) in NarI between helices II, III, and IV', in proximity to heme bD (edge-to-edge distance 2.8 A). A possible proton conduction pathway linked to electron transfer reactions has also been defined, providing fundamental atomic details of ubiquinol oxidation by NarGHI at the bacterial membrane.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsb969 | 1Q16 | 1.9 | C2221 | Full-length NarGHI heterotrimer encoded by the narGHJI operon, expressed in E. coli LCB2048 from vector pVA700 | Mo-bisMGD, two hemes b (bP and bD), five [Fe-S] clusters (FS0-FS4) |
| doi/10.1074##jbc.M410457200 | 1Y4Z | 2.0 |  | Wild-type NarGHI complex with pentachlorophenol (PCP) inhibitor | PCP (pentachlorophenol), two hemes b (bP and bD) |
| doi/10.1074##jbc.M410457200 | 1Y4Z | 1.9 |  | NarI-K86A mutant | Two hemes b |
| doi/10.1074##jbc.M410457200 | 1Y4Z | 2.5 |  | NarI-H66Y mutant | Two hemes b |
| doi/10.1021##bi049938l | 1SIW | 2.2 |  | Apomolybdo-NarGHI (tungstate-substituted, Mo-bisMGD absent) | FS0 [4Fe-4S] cluster (partial occupancy 0.5), no Mo-bisMGD |

## Expression and Purification

- **Expression system**: Escherichia coli LCB2048 (Delta narGHJI, Delta narZYWV)
- **Construct**: Full narGHJI operon under tac promoter in vector pVA700
- **Notes**: Native and selenomethionine-substituted protein expressed

### Purification Workflow

#### Source: doi/10.1038##nsb969

- **Expression system**: E. coli LCB2048
- **Expression construct**: Full narGHJI operon

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane purification | Centrifugation | -- | 100 mM MOPS, 5 mM EDTA (pH 7.0) + Thesit | Membrane fraction isolated after cell lysis by French pressure cell |
| Detergent extraction | Solubilization | -- | -- + 0.7 mM Thesit (polyoxyethylene 9-dodecyl ether) | Detergent extraction from membranes |
| Anion exchange chromatography | DEAE-Sepharose | DEAE-Sepharose | pH 6.5 and pH 7.5 + 0.7 mM Thesit | Two sequential anion exchange steps at different pH |
| Gel filtration | SEC (Superdex 200) | Superdex 200 | -- + 0.7 mM Thesit | Used to determine optimal detergent concentration for crystallization |

#### Source: doi/10.1021##bi049938l

- **Expression system**: E. coli TP1000 (mobAB mutant, deficient in Mo-bisMGD synthesis)
- **Expression construct**: Full narGHJI operon from pVA700

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | 100 mM MOPS, 5 mM EDTA (pH 7.0) + -- | Grown in Terrific Broth with 15 mM sodium tungstate; induction with 0.2 mM IPTG at inoculation |
| Membrane preparation | French pressure cell lysis and differential centrifugation | -- | 100 mM MOPS, 5 mM EDTA (pH 7.0) + -- | Crude membrane vesicles prepared as previously described |
| Anion exchange chromatography | DEAE-FF (Pharmacia) | DEAE-FF | 50 mM Tricine, 5 mM EDTA, 10% (v/v) glycerol, 0.05% Thesit (pH 8.0) + 0.05% Thesit | Purified as described by Bertero et al. (2003) with modified buffer |


## Crystallization

### doi/10.1038##nsb969

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified NarGHI in 0.7 mM Thesit |
| Reservoir | 100 mM HEPES pH 7.0, 20% (w/v) PEG 3000, 200 mM Sodium Acetate, 200 mM KCl, 5 mM EDTA |
| Temperature | 20 |
| Growth time | -- |
| Cryoprotection | Crystals soaked in reservoir solution with 35% PEG 3000 |
| Notes | Crystals belong to space group C2221 with unit cell dimensions a=154.175 A, b=241.376 A, c=139.494 A, one complex per asymmetric unit. Native and selenomethionine-substituted crystals grown under same conditions. Structure determined by MAD near Fe K-edge and MIRAS. Data collected at SSRL beamline 9-2 and NSLS X25 at 100 K. |


## Biological / Functional Insights

### Redox loop mechanism for proton-motive force generation

NarGHI completes the electron transfer chain from formate to nitrate, coupling quinol oxidation to nitrate reduction via a redox loop mechanism. Two electrons from formate oxidation at the periplasmic site of FdnGHI are transferred to menaquinone, which diffuses across the membrane to NarGHI. Quinol oxidation at the periplasmic side of NarI releases protons to the periplasm, while electrons flow through the eight redox centers (hemes -> [Fe-S] clusters -> Mo-bisMGD) to reduce nitrate to nitrite in the cytoplasm. This vectorial electron transfer generates a proton-motive force across the cytoplasmic membrane.

### Unique Mo-bisMGD cofactor conformation

The structure reveals an open bicyclic form of the molybdo-bis(molybdopterin guanine dinucleotide) (Mo-bisMGD) cofactor, where one of the pterin rings adopts a dihydropterin form with a cleaved pyran ring. This bicyclic form represents the first structural evidence for the cofactor's direct involvement in the catalytic mechanism, with scission and condensation reactions of the pyran ring participating in handling protons necessary for nitrate reduction.

### Previously undetected [4Fe-4S] cluster FS0 in NarG

A novel [4Fe-4S] cluster (FS0) was identified in domain I of NarG, coordinated by one histidine (His50) and three cysteines (Cys54, Cys58, Cys93). This unusual coordination scheme places FS0 between the Mo-bisMGD and FS1 cluster of NarH (edge-to-edge distances of 7 A and 11 A), establishing a direct role in electron transfer. The H50S mutation leads to loss of enzyme activity.

### High-spin EPR characterization of the FS0 cluster

EPR spectroscopy of reduced NarGHI revealed a previously unobserved signal comprising peaks at g = 5.023 and g = 5.556 at cryogenic temperatures (<15 K). These features were assigned to a [4Fe-4S]+ cluster with an S = 3/2 high-spin ground state. Both peaks exhibit midpoint potentials of approximately -55 mV at pH 8.0 and are eliminated in apomolybdo-NarGHI.

### NarI membrane anchor structure

NarI contains five transmembrane helices with two b-type hemes (bP and bD) oriented perpendicular to the membrane surface. Each heme is coordinated by two conserved histidine residues (His-56 and His-205 for bP; His-66 and His-187 for bD). A strong kink at Ser201 in TM V allows shorter inter-heme distances (16 A center-to-center) than observed in cytochrome bc1 complexes.

### Quinol binding site (Q-site) characterization

The structure of NarGHI in complex with pentachlorophenol (PCP) at 2.0 A resolution revealed the quinol binding and oxidation site (Q-site) in NarI. PCP binds in a narrow hydrophobic cleft (cleft B) between helices II, III, and IV', with an edge-to-edge distance of only 2.8 A to heme bD. The binding pocket is distinct from the wider cleft A that exposes both hemes. PCP exhibits mixed but primarily competitive inhibition with a Kic of 57 nM. His-66, which coordinates heme bD, is positioned within hydrogen-bonding distance from the hydroxyl group of PCP, suggesting a dual role as both heme ligand and quinone ligand. Mutation of Lys-86, which lines the proposed Q-site, to alanine (K86A) reduces plumbagin:nitrate oxidoreductase activity from 68 s-1 to 10 s-1 and attenuates inhibitor binding. A chain of water molecules between the propionates of heme bD and bulk solvent suggests a proton wire mechanism for proton release into the periplasm during quinol oxidation.


## Cross-References

- [NarGHI Quinol Binding Site](/xray-mp-wiki/concepts/structural-mechanisms/narghi-quinol-binding-site/) — Detailed concept page for the Q-site architecture and mechanism
