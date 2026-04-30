---
title: MexB (RND Multidrug Exporter from P. aeruginosa)
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [transporter, rnd-transporter, membrane-protein, multidrug-resistance, xray-crystallography]
sources: [doi/10.1016##J.JMB.2009.04.001]
category: proteins
layout: default
---


# MexB — RND Multidrug Exporter from *Pseudomonas aeruginosa*

## Overview

MexB is the inner membrane component of the MexAB-OprM tripartite efflux pump from *Pseudomonas aeruginosa*. It belongs to the resistance-nodulation-cell division (RND) superfamily of secondary active transporters and is the major pump mediating intrinsic multidrug resistance in *P. aeruginosa*. It extrudes antibiotics, biocides, dyes, organic solvents, and detergents directly from the cell, bypassing the periplasm.

## Structure

- **Resolution**: 3.0 Å
- **Space group**: P1 (triclinic)
- **Asymmetric unit**: 2 almost identical trimers (rmsd 0.1 Å for Cα)
- **Architecture**: Homotrimer, each monomer contains 12 transmembrane (TM) helices and an extensive periplasmic domain
- **Sequence**: 1046 amino acids (vs 1049 in *E. coli* AcrB), 69.8% identity, 83.2% similarity
- **PDB**: Not explicitly stated in paper (solved by MR from 2J8S)

### Periplasmic Domain Subdomains

- **Pore domain**: PN1, PN2, PC1, PC2 — forms the multidrug-binding cavity
- **Docking domain**: DN, DC — mediates interaction with outer membrane factor OprM
- The DN subdomain has an elongated β-sheet that protrudes into the neighboring subunit, interlocking the trimer

### Transmembrane Domain

- 12 TMs (TM1–TM12) with pseudo-2-fold symmetry (TM1–TM7 related to TM8–TM12)
- **Proton translocation site**: Asp407, Asp408 (TM4) and Lys939 (TM10) — conserved and essential for function
- TM8 N-terminal end connects TM domain to PC2 subdomain — trigger for large conformational changes

## Conformational States (Asymmetric Trimer)

MexB adopts an asymmetric homotrimer where each subunit represents a different conformational snapshot of the transport cycle — the same mechanism observed in AcrB:

- **Subunit C (Extrusion)**: Channel opens toward OprM docking domain — substrate released to external medium
- **Subunit B (Binding)**: Channel open to periplasm — captures substrates from periplasm/inner membrane leaflet; contains bound DDM molecule
- **Subunit A (Intermediate)**: Unique conformational shift in MexB not seen in AcrB; PC2 subdomain shifted, closing the periplasmic portal; may represent an intermediate state or be influenced by crystal packing (~700 Å² buried at trimer-trimer interface)

### Transport Cycle

The progression is ABC (not BAC), with each subunit cycling through binding → extrusion → intermediate states.

## Substrate Binding Cavity

- **Volume**: Large cavity rich in polar and aromatic residues
- **Accessibility**: Only accessible in binding subunit (B)
- **DDM-bound residues**: Val47, Ser48, Gln125 (PN1); Val177, Gly179, Ser180 (PN2); Gln273, Arg620 (PC1)
- **Electrostatics**: Slightly more positive than AcrB binding pocket (two exposed arginine residues)
- **Binding mode**: Maltoside headgroup forms H-bonds with asparagines and serines — no aromatic stacking (weaker, less specific binding)
- **Corresponds to**: Minocycline and doxorubicin binding sites in AcrB

## Expression and Purification

- **Expression**: *E. coli* C43 (DE3), pET28 vector, C-terminal hexahistidine tag
- **Induction**: 1 mM IPTG, 4 h at 30°C (OD600 = 0.8)
- **Cell lysis**: French press in 20 mM Tris-HCl pH 7.5, 150 mM NaCl, DNase I, 1 mM PMSF
- **Membrane prep**: 1 h at 100,000g
- **Solubilization**: 1% DDM (Anatrace D310LA Anagrade), 2 h at 4°C in buffer A (20 mM Tris-HCl pH 7.5, 150 mM NaCl, 10 mM imidazole, 1 mM PMSF, 10% glycerol)
- **Clarification**: 1 h at 100,000g
- **Affinity chromatography**: Ni-NTA (Qiagen), equilibrated with 0.03% DDM, washed with 30 mM imidazole, eluted with 200 mM imidazole
- **SEC**: Tricorn Superdex 200 (Amersham Biosciences), 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 10% glycerol, 0.03% DDM
- **DDM maintained**: 0.03% DDM throughout purification and crystallization

## Crystallization

- **Space group**: P1 (triclinic)
- **Resolution**: 3.0 Å
- **Phasing**: Molecular replacement with AcrB (PDB 2J8S)
- **Refinement**: R = 24.3%, R-free = 28.7%, 2-fold NCS restraints
- **Data collection**: Swiss Light Source (SLS) X06SA beamline

## Biological Context

- **Organism**: *P. aeruginosa* — opportunistic human pathogen with intrinsic multidrug resistance
- **Tripartite system**: MexAB-OprM = MexB (inner membrane RND) + MexA (periplasmic MFP) + OprM (outer membrane channel)
- **Clinical significance**: Major contributor to intrinsic resistance against antibiotics, biocides, dyes
- **Comparison with AcrB**: Similar substrate specificity but different resistance patterns; cannot interchange proteins between systems despite high sequence identity
- **Specificity**: Determined by subtle differences in binding pockets (e.g., position 616 determines macrolide resistance); MFPs (not OMFs) likely determine tripartite specificity

## Related Systems

- **AcrAB-TolC** (*E. coli*) — homologous tripartite efflux system
- **CmeAB** (*Campylobacter jejuni*) — RND efflux pump
- **AdeABC** (*Pseudomonas aeruginosa*) — another RND system in same organism
- **MexXY-OprM** (*P. aeruginosa*) — inducible RND system

## Related Transporters

- [acrB](/xray-mp-wiki/proteins/acrB/) — *E. coli* RND multidrug exporter (69.8% identity with MexB)
- [mmpL3](/xray-mp-wiki/proteins/mmpL3/) — Mycobacterial drug transporter

### Paper Details

- Sennhauser et al. (2009) JMB 389:134–145 — MexB crystal structure at 3.0 Å
- Murakami et al. (2002) Nature 419:587–593 — First AcrB structure
- Yu et al. (2003) Science 300:976–980 — AcrB multidrug binding site