---
title: YajR Transporter (E. coli MFS Drug Efflux Transporter)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1308127110]
verified: false
---

# YajR Transporter (E. coli MFS Drug Efflux Transporter)

## Overview

YajR is a 49-kDa putative proton-driven MFS (Major Facilitator Superfamily) drug efflux
transporter from Escherichia coli. It consists of 454 amino acid residues and features
the canonical 12-transmembrane (TM) helix core characteristic of MFS transporters,
as well as a unique 65-residue C-terminal YAM domain (YajR/AraEP/MBD) with a
ferredoxin-like fold. The crystal structure of YajR was determined at 3.15 Å resolution
in an outward-facing conformation, revealing the functional role of the conserved
"sequence motif A" in stabilizing the outward conformation and suggesting a general
mechanism for the conformational change between inward and outward states of MFS
transporters. YajR belongs to the DHA12 (12-TM drug-resistance H+-driven antiporter)
subfamily and shares highest sequence homology with EmrD (21% identity).



## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1308127110 | TBD | 3.15 A | TBD | Full-length YajR (residues 1-454) from E. coli, including YAM domain (residues 389-454) | None |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length YajR (wild-type and mutants G69W, D73R, G55C-G355C)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Overexpression in E. coli | -- | Standard culture media | YajR expressed in E. coli cells |
| Purification | Standard affinity purification | Ni-NTA (presumed, based on His-tag immunoblot) | Not explicitly reported in main text + Not explicitly reported | Purification details in SI Appendix |


## Crystallization

### doi/10.1073##pnas.1308127110

| Parameter | Value |
|---|---|
| Method | Standard crystallization |
| Protein sample | Purified YajR |
| Reservoir | Not explicitly reported in main text |
| Temperature | Not reported |
| Growth time | Not reported |
| Notes | Crystals diffracted to 3.15 Å resolution. The structure reveals an outward-facing conformation with the cytoplasmic side closed and the periplasmic side accessible to solvent.
 |


## Biological / Functional Insights

### Outward-facing conformation with 12-TM core and C-terminal YAM domain

The YajR structure features 12 canonical TM helices organized as N-domain (TMs 1-6)
and C-domain (TMs 7-12), forming a central TM channel. The structure also includes
a unique 65-residue C-terminal domain (YAM domain, residues 389-454) with a
ferredoxin-like fold, located cytoplasmically. The central cavity between the N and C
domains is closed on the cytoplasmic side and open to the periplasm, defining the
outward-facing conformation. Based on sequence analysis, the TM core of YajR shares
highest homology with EmrD (21% identity), a DHA12 subfamily member.

### Motif A stabilizes the outward conformation via interdomain interactions

The conserved MFS motif A (G69LLSD73RIGR77KP in YajR) is located in the loop L2-3
connecting TMs 2 and 3. Key interactions: (i) Gly69(+1) of TM2 forms close helix-helix
contacts with conserved Gly337 and Gly341 of TM11, creating an interdomain helical
bundle essential for the outward conformation. (ii) Asp73(+5) is completely buried in
the domain interface in the outward conformation (zero side-chain solvent-accessible
surface) and acts as an N-cap for TM11, stabilizing the helix via a charge-helix dipole
interaction. A D73R mutation decreased melting temperature by ~20 °C. (iii) Arg77(+9)
interacts with both Asp73(+5) and conserved Asp126 at the C-terminal end of TM4,
forming a charge-relay system. (iv) The charge-helix dipole interaction provides
~4 kJ/mol stabilization energy.

### Transport mechanism based on membrane potential and protonation

The paper proposes that for H+-driven electrogenic MFS transporters: (i) The outward
conformation is the ground state. (ii) The inward conformation is an excited state.
(iii) The outward-to-inward transition is triggered by protonation inside the central
cavity (by His225-Glu320 pair in YajR) combined with the negative-inside membrane
potential (ΔΨ ~150 mV). The membrane potential applies an electrostatic force on the
protonated residue, producing ~15 kJ/mol (FΔΨ) energy. (iv) The inward-to-outward
return is driven by deprotonation (due to alkaline cytosol) and basic residue
distribution on the cytoplasmic side. Motif A functions as a molecular switch
regulating these conformational changes.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/major-facilitator-superfamily/) — YajR is an MFS transporter; the paper elucidates MFS transport mechanisms
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — MFS transporters including YajR use the rocker-switch mechanism for alternating access
- [MFS Motif A and Charge-Helix Dipole Interactions](/xray-mp-wiki/concepts/motif-a-mfs/) — The paper is the primary structural elucidation of motif A function in MFS transporters
