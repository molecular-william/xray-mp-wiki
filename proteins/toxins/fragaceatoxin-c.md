---
title: "Fragaceatoxin C (FraC) from Actinia fragacea"
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2010.11.013, doi/10.1038##ncomms7337]
verified: false
---

# Fragaceatoxin C (FraC) from Actinia fragacea

## Overview

Fragaceatoxin C (FraC) is a potent haemolytic pore-forming toxin (PFT) from the sea anemone Actinia fragacea, belonging to the actinoporin family of alpha-helical PFTs. The 20 kDa water-soluble protein self-assembles into transmembrane pores on target cell membranes. The pore is an octameric alpha-helical barrel with a unique hybrid architecture composed of both protein and lipid molecules. Sphingomyelin (SM) acts not only as a binding receptor but also as a structural cofactor, with specific lipid molecules (L1) lining the pore wall. The pore exhibits lateral fenestrations that expose the hydrophobic core of the membrane to the aqueous environment. Four crystal structures capturing different stages of the activation mechanism have been determined: water-soluble monomer, lipid (DHPC)-bound monomer, a dimeric assembly intermediate, and the fully assembled octameric transmembrane pore at 3.1 A.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2010.11.013 | 3LIM | 1.8 | P 6 2 2 | Full-length Fragaceatoxin C (FraC) from Actinia fragacea | [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) detergent molecules |
| doi/10.1038##ncomms7337 | 3W9P | 1.7 | P 1 2(1) 1 | Full-length FraC | None |
| doi/10.1038##ncomms7337 | 3VWI | 2.1 | P 2(1) 2(1) 2(1) | Full-length FraC | None |
| doi/10.1038##ncomms7337 | 4TSP | 2.3 | P 3 2 1 | Full-length FraC | DHPC lipid (up to 4 molecules bound per chain) |
| doi/10.1038##ncomms7337 | 4TSQ | 2.15 | P 4(2) 2(1) 2 | Full-length FraC | DHPC |
| doi/10.1038##ncomms7337 | 4TSO | 1.6 | P 3 2 | Full-length FraC | DHPC |
| doi/10.1038##ncomms7337 | 4TSL | 1.57 | P 1 2(1) 1 | Full-length FraC | POC (phosphocholine headgroup analog) |
| doi/10.1038##ncomms7337 | 4TSN | 1.6 | P 4(3) 2(1) 2 | Full-length FraC | POC |
| doi/10.1038##ncomms7337 | 4TSY | 3.14 | C 2 2 2(1) | Full-length FraC | SM-like lipid (L1, bridging/non-annular); annular lipids (L2, L3) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length FraC with no affinity tag

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Full-length FraC (no tag)
- **Tag info**: None

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and protein extraction | High-pressure homogenization | — | 50 mM Tris pH 8.0, 200 mM NaCl, 1 mM CaCl2 | Cells harvested and disrupted |
| Ion exchange chromatography | [Ion Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) | Resource S column | Buffer A: 50 mM Tris pH 8.0, 200 mM NaCl, 1 mM CaCl2; Buffer B: same with 1 M NaCl | Eluted with gradient of Buffer B |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL | SEC buffer: 50 mM Tris pH 8.0, 200 mM NaCl, 1 mM CaCl2 | Final purification step. For oligomeric pore, monomeric FraC was incubated with LUVs (lipid/protein 200:1), solubilized with Triton X-100, then purified by Resource S column with LDAO (3 mM) and analytical SEC. |


## Crystallization

### doi/10.1038##ncomms7337

| Parameter | Value |
|---|---|
| Method | [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | Purified FraC at 10 mg/ml in 10 mM Tris HCl pH 8.0 |
| Reservoir | 16% PEG 8000, 200 mM (NH4)2SO4, 100 mM sodium cacodylate pH 7.4; or 20% Jeffamine, 100 mM HEPES pH 7.4 (with microseeding) |
| Temperature | 20C |
| Growth time | 2-3 weeks |
| Cryoprotection | 20% glycerol |
| Notes | Water-soluble FraC crystals. Two forms obtained: form I (P 1 2(1) 1) and form II (P 2(1) 2(1) 2(1)). Microseeding improved crystal quality. |

| Parameter | Value |
|---|---|
| Method | [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | FraC with 10 mM DHPC |
| Reservoir | Varied conditions across 3 crystal forms |
| Temperature | 20C |
| Notes | Lipid-bound FraC crystals obtained in three space groups (P 3 2 1, P 4(2) 2(1) 2, P 3 2). DHPC present at 10 mM in protein sample. |

| Parameter | Value |
|---|---|
| Method | [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | FraC with 10 mM POC |
| Reservoir | Varied conditions |
| Temperature | 20C |
| Notes | Dimeric assembly intermediate crystals. POC (phosphocholine) mimics lipid headgroup. Two crystal forms obtained (P 1 2(1) 1 at 1.57 A, P 4(3) 2(1) 2 at 1.6 A). |

| Parameter | Value |
|---|---|
| Method | Lipidic mesophase (in meso) |
| Protein sample | Purified oligomeric FraC pore in LDAO |
| Reservoir | Various conditions |
| Temperature | 20C |
| Notes | Transmembrane pore crystallized in lipidic mesophases. Pore particles prepared by incubating FraC with DOPC/SM (1:1) liposomes, solubilized with Triton X-100, and purified in LDAO. Octameric pore refined at 3.14 A resolution in space group C 2 2 2(1). |


## Biological / Functional Insights

### Octameric pore with hybrid protein-lipid architecture

The FraC transmembrane pore is an octamer with a unique architecture composed of both protein and lipid. Eight N-terminal alpha-helices form a transmembrane barrel. The bridging lipid L1 (SM-like) lines the pore wall and acts as an assembly cofactor, occupying 37% of the total contact interface (449 A2 per lipid). L1 interacts with conserved residue Arg31; hydrogen bonds with L1 are absent when modelled as phosphatidylcholine, explaining the specificity for sphingomyelin. Annular lipids L2 and L3 occupy peripheral sites. This hybrid architecture is unprecedented among pore-forming toxins.

### Stepwise pore assembly mechanism

Four crystallographic snapshots reveal the stepwise mechanism: (1) Water-soluble monomer: N-terminal helix packed against beta-core, Phe16 inserted in a hydrophobic cavity. (2) Lipid-bound monomer: up to four DHPC molecules bind (multivalency), orienting the protein on the membrane surface. (3) Dimeric intermediate: Val60 from a second chain displaces Phe16, causing localized unfolding at residues 14-17 and initiating N-terminal helix release. (4) Octameric pore: eight N-terminal helices form a transmembrane barrel with lipid L1 incorporated. Protein-protein contact interface is 777 A2 per pair.

### Lipid multivalency in membrane recognition

FraC binds up to four lipid molecules per chain (L2-L5). Two high-affinity sites (L2, L3) bind the POC headgroup of SM/DOPC, corresponding to the constant sites also observed in the pore. Two low-affinity sites (L4, L5) bind additional lipids. This multivalent lipid recognition increases the affinity of FraC for target membranes, particularly important for specific recognition of sphingomyelin-containing membranes.

### Fenestrations in the pore wall

The FraC pore exhibits lateral fenestrations (windows) in the walls, approximately 5 x 11 A in cross-section. These fenestrations are partially occupied by the hydrophobic acyl chains of lipid L1 but are not fully sealed. The fenestrations may facilitate diffusion of small hydrophobic molecules (e.g., from sea anemone venom) directly into the membrane core, intensifying cell damage. They may also catalyze transbilayer lipid flip-flop movement. Such fenestrations have not been previously documented in PFTs or viroporins.

### Sphingomyelin as a structural cofactor

Sphingomyelin (SM) is not merely a binding receptor but a bona fide structural element of the FraC pore. Pore formation is enhanced in membranes with SM/DOPC mixtures (phase coexistence) compared to pure SM or pure DOPC. The L1 lipid (modelled as SM-like) is essential for pore integrity and acts as an assembly cofactor, ensuring the pore assembles only in target membranes containing SM. This provides a sophisticated membrane-specific trigger for toxin activation.

### Hierarchy of haemolytic activity determinants

Mutagenesis studies reveal a hierarchy of haemolytic activity determinants: (1) Membrane binding: W112R/W116F mutein loses lipid binding and is completely inactive. (2) N-terminal helix release: V8C/K69C disulfide crosslink blocks helix release and reduces activity to 1% of wild type. (3) Pore stability: V60E/W149A weakens protein-protein interfaces, reducing activity to 16% of wild type. This hierarchy corresponds to the stepwise assembly mechanism from membrane binding to pore formation.


## Cross-References

- [Actinoporin](/xray-mp-wiki/concepts/actinoporin/) — FraC is a member of the actinoporin family of pore-forming toxins
- [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) — Detergent used for pore purification and crystallization
- [Sphingomyelin](/xray-mp-wiki/reagents/lipids/sphingomyelin/) — Key lipid that acts as both receptor and structural cofactor
- [Lipidic Mesophase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-mesophase/) — Method used to crystallize the transmembrane pore
