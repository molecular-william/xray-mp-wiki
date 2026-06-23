---
title: MsbA Lipid A Flippase
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, pump, xray-crystallography]
sources: [doi/10.1038##s41586-018-0083-5, doi/10.1016##j.str.2019.04.007]
verified: false
---

# MsbA Lipid A Flippase

## Overview

MsbA is an essential ATP-binding cassette (ABC) transporter in Gram-negative bacteria that transports [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) and lipopolysaccharide (LPS) from the cytoplasmic leaflet to the periplasmic leaflet of the inner membrane. MsbA functions as a homodimeric lipid flippase powered by ATP binding and hydrolysis in the nucleotide-binding domains (NBDs). The 2.8 A crystal structure of MsbA from Salmonella typhimurium (PDB 6BL6) captured in an inward-facing conformation with [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) bound reveals a large amplitude opening in the transmembrane portal likely required for [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) access. The 2.9 A crystal structure of E. coli MsbA in complex with the quinoline inhibitor G907 (PDB 6BPL) reveals an unprecedented mechanism of ABC transporter inhibition, trapping MsbA in an inward-facing LPS-bound conformation and uncoupling the nucleotide-binding domains.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2019.04.007 | 6BL6 | 2.8 | P2(1)2,2 | Full-length MsbA from Salmonella typhimurium; co-crystallized with [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) in facial amphiphile [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/) |  |
| doi/10.1016##j.str.2019.04.007 | 6O30 | 4.46 | P2(1)2,2 | Full-length MsbA; apo (no [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) added) |  |
| doi/10.1038##s41586-018-0083-5 | 6BPL | 2.9 |  | E. coli MsbA in complex with G907 and LPS | G907 |
| doi/10.1038##s41586-018-0083-5 | 6BPP |  |  | E. coli MsbA in complex with G247 and LPS | G247 |
| doi/10.1038##s41586-018-0083-5 | 6BPM |  |  | E. coli MsbA in complex with G592 and LPS | G592 |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3); expression in LB medium; induction with [IPTG](/xray-mp-wiki/reagents/additives/iptg/)

- **Construct**: Full-length MsbA from S. typhimurium with N-terminal His10 tag in pET19b vector

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Full-length MsbA with N-terminal His10 tag
- **Tag info**: N-terminal His10 tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer | — |  | Membranes isolated by ultracentrifugation |
| Membrane solubilization | Detergent solubilization | — | [UDM](/xray-mp-wiki/reagents/detergents/udm/) (n-undecyl-beta-D-maltopyranoside) | Membrane pellets solubilized in 1.5% [UDM](/xray-mp-wiki/reagents/detergents/udm/) |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Ni-NTA agarose |  | Column washed with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in buffer containing 0.1% [UDM](/xray-mp-wiki/reagents/detergents/udm/) |
| Detergent exchange | Exchange to [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/) | — | [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/) (Facade-EM, 0.04 wt%) | Detergent exchanged from [UDM](/xray-mp-wiki/reagents/detergents/udm/) to [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/) using 100 kD cutoff centrifugal filters |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | — |  | Polishing step in buffer containing [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/) |

**Final sample**: MsbA in buffer with 0.04% [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/), supplemented with 5 uM [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/), concentrated to ~12 mg/ml


## Crystallization

### doi/10.1016##j.str.2019.04.007

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | MsbA (12 mg/ml) in 0.04% [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/), 5 uM [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) |
| Reservoir | 0.1 M Tris, 0.2 M tri-sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) (pH 6.34-7.0), 0.12 M LiSO4, 32.5% [PEG](/xray-mp-wiki/reagents/additives/peg/) 300 |
| Mixing ratio | 1:1 to 1:0.7 |
| Temperature | 4 |
| Growth time | 5 days to ~2 months |
| Cryoprotection | Not specified |
| Notes | Crystals grew to 200-500 um. Apo crystals grown under same conditions without [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/). |


## Biological / Functional Insights

### Intermediate inward-facing conformation with open membrane portals

The MsbA structure at 2.8 A reveals an inward-facing conformation with NBD separation of 75.6 A (between T561 Calpha), intermediate between the wide-open 5.3 A structure (PDB 3B5W) and the more closed [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure (PDB 5TV4). Large portals open between TM4 and TM6 on opposite sides, lined by positively charged residues (K194, R190, K187, R183 on TM4; R310, Q309, N305, N303, K299 on TM6) that may recognize the negatively charged sugar groups of LPS/lipid A. This intermediate state is proposed to represent an active transport-competent conformation.

### Putative lipid A binding sites inside and outside MsbA

Electron density attributed to [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) was observed both inside the TM cavity (canonical binding site) and on an outer surface cleft at the periplasmic ends of TM1-3. The internal binding site is consistent with the trap and flip model. The external surface site, formed upon closure of the V-shaped opening between TM1 and TM3 as MsbA resets from outward- to inward-facing, may serve as a post-transport docking site where [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) briefly resides after export, prior to downstream processing by LPS transport proteins.

### Dual-mode inhibition by quinoline compounds

The 2.9 A structure of E. coli MsbA in complex with G907 (PDB 6BPL) reveals dual-mode inhibition: (1) transmembrane trapping - G907 wedges into an architecturally conserved transmembrane pocket, locking MsbA in an inward-facing, LPS-bound conformation that prevents transition to the outward-facing state; (2) NBD uncoupling - the two NBDs adopt an asymmetric conformation not previously observed, uncoupling ATP binding/hydrolysis from the LPS transport cycle.

### Conformational cycle for lipid A transport

Based on comparative analysis with existing MsbA structures, a sequential transport pathway is proposed: (1) lateral opening of membrane portals allows bulky [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) entry from the cytoplasmic leaflet; (2) inward motion of TMDs increases affinity for bound [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) and shuttles it toward the periplasmic side; (3) ATP binding dimerizes NBDs, switching to an outward-facing conformation; (4) ATP hydrolysis and phosphate/ADP release resets the transporter to inward-facing. The inward-facing state may represent both the starting and end state of one complete transport cycle.

### Facial amphiphile FA-3 enables high-resolution MsbA structure

The facial amphiphile [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/) (Facade-EM, 3alpha-hydroxy-7alpha,12alpha-di-((O-beta-D-maltosyl)-2-hydroxyethoxy)-cholane) was essential for obtaining well-diffracting crystals of MsbA. [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/) maintained MsbA ATPase activity comparable to lipid bilayer conditions (~200 nmol/min/mg at 5 mM ATP) and provided superior thermal stability (Tm ~57 C) compared to conventional detergents. Co-crystallization with [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) further stabilized the protein, enabling 2.8 A resolution.


## Cross-References

- [ABC Transporter Allosteric Regulation](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-allosteric-regulation/) — MsbA is an ABC transporter; its conformational cycle involves allosteric coupling between NBDs and TMDs
- [POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine)](/xray-mp-wiki/reagents/lipids/pope/) — POPE lipids used in MD simulations to study MsbA-lipid A interactions and in ATPase activity measurements
- [Dual-Mode Inhibition of ABC Transporters](/xray-mp-wiki/concepts/transport-mechanisms/dual-mode-inhibition-abc-transporters/) — Quinoline inhibitors (G907, G247) exhibit dual-mode inhibition of MsbA
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in purification or crystallization
