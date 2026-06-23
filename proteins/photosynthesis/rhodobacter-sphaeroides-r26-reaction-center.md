---
title: Rhodobacter sphaeroides R-26 Reaction Center
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1021##bi00236a005, doi/10.1073##pnas.85.21.7993]
verified: false
---

# Rhodobacter sphaeroides R-26 Reaction Center

## Overview

The reaction center (RC) from the purple bacterium Rhodobacter sphaeroides R-26 is a membrane protein complex that mediates the primary steps of photosynthetic electron transfer. The RC is composed of three subunits (L, M, and H) and eight cofactors: a special pair of bacteriochlorophylls, two accessory bacteriochlorophylls, two bacteriopheophytins, two ubiquinones (Q_A and Q_B), and a non-[HEME](/xray-mp-wiki/reagents/ligands/heme) Fe2+ ion. The structure was determined at 3.1 A resolution by molecular replacement using the Rps. viridis RC structure as search model.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##bi00236a005 |  | 3.1 A |  | Wild-type RC from Rb. sphaeroides R-26 strain; L, M, and H subunits | Bacteriochlorophyll, bacteriopheophytin, ubiquinone, non-heme Fe2+ |
| doi/10.1073##pnas.85.21.7993 |  | 2.8 | P2_12_12_1 | Wild-type RC from Rb. sphaeroides R-26 (carotenoidless mutant strain); L, M, and H subunits | Bacteriochlorophyll dimer (D), bacteriochlorophyll monomers (BA, BB), bacteriopheophytin monomers (phiA, phiB), ubiquinones (QA, QB), non-heme Fe2+ |

## Expression and Purification

- **Expression system**: Rhodobacter sphaeroides R-26 (purple bacterium)
- **Construct**: Wild-type RC; native L, M, and H subunits without tags

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| RC isolation and purification | As described in Wraight (1979) | -- | -- + 1-octyl beta-D-glucopyranoside (OG) | RC isolated and purified following Wraight (1979) protocol; OG used as detergent |


## Crystallization

### doi/10.1021##bi00236a005

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified RC from Rb. sphaeroides R-26 |
| Reservoir | [PEG](/xray-mp-wiki/reagents/additives/peg) 4000 at pH 8 |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Needle-shaped crystals grown by vapor diffusion with [PEG](/xray-mp-wiki/reagents/additives/peg) 4000 at pH 8; crystals up to 2 mm long |


## Biological / Functional Insights

### Subunit architecture and transmembrane helix arrangement

The RC is formed from three protein subunits: L, M, and H. The L and M chains are homologous transmembrane proteins, each containing five transmembrane helices. A local noncrystallographic 2-fold axis relates the M and L subunits. The H chain has only one transmembrane helical segment; most of the H subunit is on the cytoplasmic side of the membrane. The local 2-fold axis does not apply to the H chain. The complex can function in vitro without the H chain, though with diminished efficiency.

### Cofactor arrangement and electron transfer pathway

The RC contains eight chromophores: two bacteriochlorophylls forming the special pair, two accessory bacteriochlorophylls, two bacteriopheophytins, and two ubiquinones. A non-[HEME](/xray-mp-wiki/reagents/ligands/heme) Fe2+ atom is also present. The H chain does not directly accommodate chromophores but increases the barrier between Fe2+ and quinones with respect to the cytoplasm. The H chain is important for proper assembly of the complex in the membrane.

### L-M interface and complex stability

The tertiary structure is stabilized by hydrophobic interactions between the L and M chains, interactions of pigments with each other and with the L and M chains, residues from L and M that coordinate to Fe2+, and salt bridges between L/M and H chains. The buried surface area between L and M chains is 3990 A^2, between H and L is 1870 A^2, and between H and M is 2770 A^2. The L and M chains, four bacteriochlorophylls, and two bacteriopheophytins are required together for assembly.

### Periplasmic amphipathic helices and cytochrome c2 binding

Two helical regions on the periplasmic surface form amphipathic helices (CD helices from residues L155-L163 and M179-M188). These have a well-defined hydrophobic side and polar side; the polar side points toward the periplasm and can form the surface of contact with the soluble cytochrome c2 molecule.

### Conserved residues and N-terminal structure

The N- and C-terminal ends of the L and M chains are highly conserved among purple photosynthetic bacteria (Rb. sphaeroides, Rb. capsulatus, Rps. viridis, Rhodospirillum rubrum). Among 31 conserved residues, only five differ among four species. The M chain has 51 amino acids from the N-terminus to the A helix, with little sequence homology for the 43 N-terminal residues but good homology for the eight amino acids before the A helix.

### H chain cytoplasmic domain and membrane orientation

The cytoplasmic domain of the H chain is asymmetrically located and does not conform to the local 2-fold axis. It contacts the L-chain segment including residues 1-26 (23 of which are conserved) and the first 15 residues of the M chain (less extensive contacts). Conservation of amino acid sequences in the N-terminal segments of L and M chains is important for recognition and interaction with the H chain. The single membrane-spanning helix of the H subunit likely maintains the RC in proper functional orientation in the membrane.

### Protein-cofactor interactions and asymmetric electron transfer

The first structure of the Rb. sphaeroides RC at 2.8 A (R-26) and 3.0 A (2.4.1) revealed detailed protein-cofactor interactions. The bacteriochlorophyll dimer (D) interacts with C, D, E, and cd helices of L and M subunits. Key interactions include His M202 coordinating Mg of DB, while His L173 is too far (4.0 A) to coordinate DA Mg directly — a critical asymmetry. Tyr M210 forms a hydrogen bond with DA and lies ~4.5 A from both D and phiA, potentially playing a role in electron transfer. The preferential electron transfer along the A branch is explained by: (i) asymmetric dimer structure with different Mg coordination and hydrogen bonding; (ii) larger overlap between DB and BA than DA and BB; (iii) phiA is 1-1.5 A closer to both BA and Tyr M210 than phiB is to BB and Phe L181; (iv) asymmetric distribution of charged amino acids.

### Carotenoid binding site in the wild-type RC (2.4.1)

The carotenoid (spheroidene) in the wild-type RC from Rb. sphaeroides 2.4.1 was located near cofactor BB between the B and C helices of the M subunit at 3.0 A resolution. The nearby residues have mostly aromatic side chains (Phe, Trp, Tyr) that place strong steric constraints on the carotenoid conformation. A 15-15-prime cis bond (identified by Raman spectroscopy) is consistent with the electron density. The constrained conformation may cause a red shift in the carotenoid absorption spectrum. No charged residues are located within 10 A of the carotenoid. The position of beta-octyl glucoside detergent molecules in the R-26 structure corresponds to the central region of the carotenoid in the 2.4.1 structure, explaining the preferential ease of BB removal from the R-26 strain.

### Bound beta-octyl glucoside molecules and BB accessibility

Two bound beta-octyl glucoside (beta-OG) detergent molecules were identified in the RC R-26 structure, near BA and BB respectively. beta-OG_B lies within 7 A of BB with a closest approach of 3.5 A, while beta-OG_A is further from BA (7.5 A). The close proximity of beta-OG_B to BB suggests BB is more accessible to solvent, consistent with the preferential removal of BB from the R-26 strain (and in the wild-type, removal of BB is accompanied by removal of the carotenoid).


## Cross-References

- [Rps. viridis Photosynthetic Reaction Centre](/xray-mp-wiki/proteins/photosynthesis/rps-viridis-reaction-centre/) — Used as molecular replacement search model; structures are very similar
- [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) — Primary cofactor; special pair and accessory BChls in the RC
- [Bacteriopheophytin](/xray-mp-wiki/reagents/ligands/bacteriopheophytin/) — Primary electron acceptor cofactors in the RC
- [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) — Primary (Q_A) and secondary (Q_B) quinone electron acceptors
- [Iron (Fe)](/xray-mp-wiki/reagents/additives/iron/) — Non-heme Fe2+ ion between quinone binding sites
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used for RC solubilization and purification
- [Polyethylene Glycol (PEG)](/xray-mp-wiki/reagents/additives/peg/) — PEG 4000 used as crystallization precipitant
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phasing method used to solve the RC structure
- [HEME](/xray-mp-wiki/reagents/ligands/heme) — Entity mentioned in text
