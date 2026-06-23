---
title: "BcsA from Rhodobacter sphaeroides (Cellulose Synthase Catalytic Subunit)"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11744]
verified: false
---

# BcsA from Rhodobacter sphaeroides (Cellulose Synthase Catalytic Subunit)

## Overview

BcsA is the catalytically active subunit of the bacterial cellulose synthase complex from Rhodobacter sphaeroides. It is a membrane-embedded glycosyltransferase that uses UDP-activated glucose (UDP-Glc) as donor substrate to synthesize beta-1,4-linked cellulose polymers. BcsA contains a GT-A fold glycosyltransferase domain between transmembrane helices 4 and 5, a PilZ domain at the C-terminus that binds the bacterial secondary messenger [CYCLIC-DI-GMP](/xray-mp-wiki/reagents/ligands/cyclic-di-gmp) for activation, and eight transmembrane helices that form a narrow polysaccharide-conducting channel. The structure of the BcsA-BcsB translocation intermediate reveals how cellulose synthesis is coupled to membrane translocation, with the nascent glucan extended by one glucose molecule at a time.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11744 | 4HG6 | 4.5 A |  | BcsA-[BCSB](/xray-mp-wiki/proteins/bcsb) complex from Rhodobacter sphaeroides; BcsA residues 1-788 with C-terminal dodeca-histidine tag; BcsB residues 21-725 with N-terminal PelB signal sequence | UDP, translocating glucan (18 [GLUCOSE](/xray-mp-wiki/reagents/additives/glucose) units) |

## Expression and Purification

- **Expression system**: E. coli Rosetta 2 cells
- **Construct**: BcsA with C-terminal His12 tag; [BCSB](/xray-mp-wiki/proteins/bcsb) residues 21-725 with N-terminal PelB signal sequence

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and membrane preparation | Auto-induction culture | -- | ZYP-5052 auto-induction medium + -- | Cells grown in ZYP-5052 auto-induction medium at 37 C; crude membranes collected by centrifugation at 120,000g |
| Membrane solubilization | Detergent solubilization | -- | 20 mM sodium phosphate pH 7.2, 0.3 M NaCl, 5 mM [CELLOBIOSE](/xray-mp-wiki/reagents/additives/cellobiose), 5 mM MgCl2, 40 mM imidazole, 10% glycerol + 2% [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100) | Solubilized for 60 min at 4 C; insoluble material cleared by centrifugation |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) agarose (Qiagen) | RB2 buffer (20 mM sodium phosphate pH 7.2, 0.3 M NaCl, 5 mM [CELLOBIOSE](/xray-mp-wiki/reagents/additives/cellobiose), 5 mM MgCl2, 40 mM imidazole, 10% glycerol) + 2% [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100) | Batch incubation with 10 ml [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) agarose for 45 min at 4 C |
| Column washing | Gravity flow chromatography | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) agarose | WB1-buffer (RB2-buffer with 60 mM [IMIDAZOLE](/xray-mp-wiki/reagents/additives/imidazole)) + 2% [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100) | Washed with 75 ml WB1-buffer containing 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/lDAO) |
| Elution | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) affinity elution | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) agarose | RB2 buffer with 1 M NaCl and increasing [IMIDAZOLE](/xray-mp-wiki/reagents/additives/imidazole) + 2% [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100) | Eluted with high [IMIDAZOLE](/xray-mp-wiki/reagents/additives/imidazole) concentration |


## Crystallization

### doi/10.1038##nature11744

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | Purified BcsA-[BCSB](/xray-mp-wiki/proteins/bcsb) complex |
| Reservoir | 30% [PEG200](/xray-mp-wiki/reagents/additives/peg200), 0.1 M MES pH 6.5, 50 mM NaCl |
| Temperature | 4 C |
| Growth time | approximately 7 days for initial crystals |
| Cryoprotection | -- |
| Notes | Initial crystals observed after approximately 7 days; final size about 50 x 50 x 10 micrometers |


## Biological / Functional Insights

### Architecture of the BcsA-[BCSB](/xray-mp-wiki/proteins/bcsb) translocation complex

BcsA and [BCSB](/xray-mp-wiki/proteins/bcsb) form an elongated complex with large cytosolic and periplasmic domains. The transmembrane helices of BcsA (TM1-TM8) form a narrow channel approximately 8 A wide and 33 A long. BcsB anchors to the membrane via a single C-terminal transmembrane helix and contributes two amphipathic interface helices (IF4 and IF5) at the water-lipid interface. The complex accommodates a translocating glucan chain that extends from the intracellular catalytic site to the periplasmic solvent.

### Glycosyltransferase A fold and catalytic mechanism

The GT domain of BcsA adopts a [GT-A Fold](/xray-mp-wiki/concepts/gt-a-fold) fold (GT-A) consisting of a mixed seven-stranded beta-sheet surrounded by seven alpha-helices. The conserved signature D,D,D,Q(Q/R)XRW motif contains three variably spaced aspartic acids (Asp 179, Asp 246, Asp 343) and a pentapeptide (Gln 379-Arg 380-Arg 382-Trp 383). The first two aspartic acids coordinate UDP, while the third (Asp 343) represents the catalytic base. The Q(Q/R)XRW sequence and an FFCGS pentapeptide form a binding site for the terminal disaccharide of the glucan acceptor. The structure superimposes with the inverting glycosyltransferase SpA from Bacillus subtilis with 2.15 A RMSD.

### Polysaccharide-conducting transmembrane channel

TM3-TM8 of BcsA form a narrow channel that accommodates ten [GLUCOSE](/xray-mp-wiki/reagents/additives/glucose) units of the translocating glucan. The glucan enters through the cytoplasmic opening formed by IF1-3 and the N-terminal half of TM5, crosses the membrane parallel to TM5 and TM6, and exits on the periplasmic side between BcsA's 5/6 and 7/8 loops at the BcsA-BcsB interface. All transmembrane helices of BcsA except TM1 and TM2 directly contact the glucan. The periplasmic exit is maintained by the tips of TM6 and TM8 side chains, separated by about 9 A and 15 A at the periplasmic and cytoplasmic sides respectively.

### Activation by [CYCLIC-DI-GMP](/xray-mp-wiki/reagents/ligands/cyclic-di-gmp) via PilZ domain

BcsA activity is stimulated by [CYCLIC-DI-GMP](/xray-mp-wiki/reagents/ligands/cyclic-di-gmp) through a PilZ domain localized within BcsA's C-terminus, right next to the GT domain. The C-terminus extends from TM8 via a short beta-strand forming a two-stranded beta-sheet with the IF3-TM7 loop, before folding into a six-stranded beta-barrel (amino acids 585-675). The beta-barrel points away from the GT domain at approximately 90 degrees. The PilZ domain is the cyclic-di-GMP-responsive sensor that controls cellulose synthase activity.

### Periplasmic domain architecture of [BCSB](/xray-mp-wiki/proteins/bcsb)

The periplasmic region of the cellulose synthase is primarily formed by [BCSB](/xray-mp-wiki/proteins/bcsb) and consists of two carbohydrate binding domains (CBD1 and CBD2) connected by a disulphide bond between conserved Cys 163 and Cys 430, and two flavodoxin-like domains (FD1: amino acids 192-303; FD2: amino acids 457-529 and 598-666). CBD1 contains a cluster of conserved hydrophobic residues (His 159, Arg 160, Ile 161, Leu 171, Trp 172) at its tip that likely interact with the translocating glucan. The repeating structural motif of BcsB contains a CBD linked to an FD domain.

### Model for cellulose synthesis and translocation coupling

The structure suggests a model in which the nascent glucan is extended by one [GLUCOSE](/xray-mp-wiki/reagents/additives/glucose) molecule at a time. After glycosyl transfer, the newly attached terminal glucose rotates around the acetal linkage to align with the glucan in the channel. Steric interactions dictate the rotation direction, leading to the beta-1,4 glucan characteristic 180 degree rotation between individual glucose units. The model represents a cellulose synthase-cellulose translocation intermediate captured after glycosyl transfer and before replacing UDP with UDP-Glc.


## Cross-References

- [UDP-Glucose (UDP-Glc)](/xray-mp-wiki/reagents/substrates/udp-glucose/) — Sugar nucleotide donor substrate for [Cellulose Synthase](/xray-mp-wiki/concepts/cellulose-synthase)
- [Cyclic-di-GMP](/xray-mp-wiki/reagents/ligands/cyclic-di-gmp/) — Bacterial secondary messenger that activates BcsA via PilZ domain
- [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/ldao/) — Zwitterionic detergent used in BcsA-[BcsB from Rhodobacter sphaeroides (Cellulose Synthase Periplasmic Subunit)](/xray-mp-wiki/proteins/bcsb) purification wash buffer
- [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100/) — Nonionic detergent used for membrane solubilization of BcsA-[BcsB from Rhodobacter sphaeroides (Cellulose Synthase Periplasmic Subunit)](/xray-mp-wiki/proteins/bcsb) complex
- [Sodium Phosphate Buffer](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) — Buffer component in purification and solubilization buffers
- [2-(N-Morpholino)ethanesulfonic Acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Crystallization buffer at pH 6.5
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Used for [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine) derivatization for SAD phasing
- [GT-A Fold (Glycosyltransferase A Fold)](/xray-mp-wiki/concepts/structural-mechanisms/gt-a-fold/) — Structural domain of BcsA glycosyltransferase catalytic domain
- [Cellobiose](/xray-mp-wiki/reagents/additives/cellobiose) — Additive used in purification or crystallization buffers
