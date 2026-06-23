---
title: Human AE1 Anion Exchanger (Band 3) - C-Terminal Membrane Domain
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aaa4335]
verified: false
---

# Human AE1 Anion Exchanger (Band 3) - C-Terminal Membrane Domain

## Overview

Human AE1 (anion exchanger 1, also known as Band 3) is the most abundant membrane protein in erythrocytes, where it catalyzes the electroneutral exchange of bicarbonate and chloride ions across the plasma membrane. This exchange is essential for CO2 transport from tissues to lungs. AE1 is a 110-kD glycoprotein built from a cytosolic N-terminal domain (residues 1-360) and a C-terminal integral membrane domain (AE1_CTD, residues 361-911) that performs anion exchange. The crystal structure of AE1_CTD was determined at 3.5 Å resolution in an outward-facing open conformation, locked by the covalent inhibitor [H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)](/xray-mp-wiki/reagents/additives/h2dids/) and in complex with a monoclonal antibody Fab fragment. The structure reveals 14 transmembrane segments arranged in two inverted repeats of seven TMs, forming core and gate domains. AE1_CTD is a physiological homodimer with the dimer interface formed exclusively through gate domain residues (TMs 5, 6, 7).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aaa4335 | — | 3.5 | — | AE1_CTD (residues 381-887), N-terminally cleaved by [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) | [H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)](/xray-mp-wiki/reagents/additives/h2dids/) |

## Expression and Purification

- **Expression system**: Native human erythrocytes
- **Construct**: AE1_CTD (residues 381-887) - C-terminal membrane domain cleaved by [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) from full-length AE1 purified from erythrocyte ghost membranes
- **Notes**: Protein purified directly from human erythrocyte white ghost membranes, not recombinantly expressed

### Purification Workflow

- **Expression system**: Native (human erythrocytes)
- **Expression construct**: Full-length AE1, C-terminal domain cleaved by [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/)
- **Tag info**: No affinity tag used (native purification)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Ghost membrane preparation | Hypotonic lysis and membrane isolation | — | — + — | White ghost membranes prepared from human erythrocytes |
| Proteolytic cleavage | [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) digestion | — | — + — | N-terminus of AE1_CTD cleaved by [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) to release the C-terminal membrane domain |
| Inhibitor treatment | Chemical modification | — | — + — | Treated with [H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)](/xray-mp-wiki/reagents/additives/h2dids/) (4,4-diisothiocyanatodihydro-stilbene-2,2-disulfonic acid) to irreversibly lock the outward-facing conformation |
| Deglycosylation | Enzymatic deglycosylation | — | — + — | Deglycosylated with N-glycosidase F to obtain well-diffracting crystals |

**Final sample**: Deglycosylated AE1_CTD-[H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)](/xray-mp-wiki/reagents/additives/h2dids/) complex
**Yield**: —
**Purity**: —


## Crystallization

### doi/10.1126##science.aaa4335

| Parameter | Value |
|---|---|
| Method | Co-crystallization |
| Protein sample | AE1_CTD-[H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)](/xray-mp-wiki/reagents/additives/h2dids/) complex with monoclonal antibody Fab fragment |
| Temperature | — |
| Growth time | — |
| Cryoprotection | — |
| Notes | Co-crystallized with a monoclonal antibody Fab fragment that binds tightly to a conformational epitope of AE1_CTD. The antibody was selected from a panel raised by inoculation of mice with AE1_CTD-displaying baculovirus. Two steps were required for crystallization: (1) deglycosylation with N-glycosidase F, (2) co-crystallization with Fab fragment. |


## Biological / Functional Insights

### Inverted Repeat Architecture and Structural Homology to UraA

AE1_CTD comprises 14 transmembrane segments built from two inverted repeats of seven TMs (TMs 1-7 and TMs 8-14). The repeat is difficult to superpose as a unit but can be treated as a two-component module: TMs 1-4 superpose on TMs 8-11 (RMSD 2.1 Å for 62/103 Cα atoms) and TMs 5-7 onto TMs 12-14 (RMSD 2.1 Å for 53/100 Cα atoms). Despite only 12% sequence identity, AE1_CTD shares the same overall fold as the [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) transporter [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/), with core domain RMSD of 1.8 Å for 145/268 Cα atoms.

### Core-Gate Domain Architecture

The inverted repeat units intertwine to form two structural domains: the core (TMs 1-4 and 8-11) and the gate (TMs 5-7 and 12-14), following the convention of [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/). Within the core domain, the N-termini of two half-helices (TMs 3 and 10) face each other at ~10 Å, creating the appearance of a continuous helix. The gate domains are directly involved in substrate binding, and structural variation between AE1 and [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/) gate domains reflects their different substrates.

### Outward-Facing Conformation and Alternating Access Mechanism

The AE1_CTD structure is in an outward-facing open conformation. Comparison with the inward-facing [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/) structure suggests a transport mechanism where the core domain rotates against the gate domain to alternate between outward- and inward-facing states. This movement is similar to that observed in [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) family transporters. Starting from the outward-facing open conformation, chloride at high plasma concentration binds to the anion-binding site, causing local conformational changes that enable the core domain to rotate relative to the gate domain to form the inward-facing structure. Chloride then diffuses out and is replaced by bicarbonate to reverse the process.

### Disease-Associated Mutations

Specific mutations in AE1_CTD are related to red cell diseases including spherocytosis, stomatocytosis, and Southeast Asian ovalocytosis (SAO). Mutations causing spherocytosis often lead to misfolding, while others exhibit abnormal transport kinetics. A cation leak phenotype caused by AE1 mutations is observed in dominantly inherited hemolytic anemia. Key mutations include Arg730Cys (putative bicarbonate-binding residue), Ser731Pro, His734Arg on half-helix TM10, and deletion of residues 400-408 (SAO) at the TM1 N terminus.


## Cross-References

- [Alternating Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — AE1 structure in outward-facing conformation provides a structural basis for the alternating access mechanism of anion exchange
- [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) — Related protein structure
- [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/) — Related protein structure
- [H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)](/xray-mp-wiki/reagents/additives/h2dids/) — Additive used in purification or crystallization buffers
- [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) — Additive used in purification or crystallization buffers
- [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) — Related ligand or cofactor
