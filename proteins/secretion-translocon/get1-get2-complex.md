---
title: Get1/Get2 GET Insertase Complex
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-023-42867-2]
verified: false
---

# Get1/Get2 GET Insertase Complex

## Overview

The Get1/Get2 complex (also known as WRB/CAML in metazoans) is the membrane protein insertase of the eukaryotic [GET pathway](/xray-mp-wiki/concepts/miscellaneous/get-pathway/), responsible for inserting tail-anchored (TA) membrane proteins into the endoplasmic reticulum (ER) membrane. The complex forms a 2:2 heterotetramer of Get1 and Get2 subunits, with each Get1/Get2 heterodimer containing a membrane-embedded hydrophilic groove that facilitates TA protein insertion. The GET insertase exhibits conformational plasticity (state 1 and state 2) dictated by interactions of the Get2 helix alpha3' with Get3.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-023-42867-2 | 8CR1 | 3.2 | not reported | H. sapiens Get2^DeltaN-Get1/Get3 in PMAL-C8 amphipol (wild type, state 2) | phosphatidylinositol at heterotetramer interface |
| doi/10.1038##s41467-023-42867-2 | 8CR2 | 4.2 | not reported | H. sapiens Get2^DeltaN/Deltaalpha3'-Get1/Get3 in PMAL-C8 amphipol (Deltaalpha3' mutant, state 1) | lipid/amphipathic density in central membrane cavity |
| doi/10.1038##s41467-023-42867-2 | 8ODU | 5.0 | not reported | C. thermophilum Get2^DeltaN-Get1/Get3 in A835 amphipol (state 1) |  |
| doi/10.1038##s41467-023-42867-2 | 8ODV | 4.7 | not reported | C. thermophilum Get2^DeltaN-Get1/Get3 in nanodisc (state 1) |  |

## Expression and Purification

- **Expression system**: S. cerevisiae (for ctGet1/Get2); Sf9 insect cells (for hsGet1/Get2)
- **Construct**: Codon-optimized ctGet1/ctGet2 in pMT929 vector under GAL1 promoter (yeast); hsGet2^DeltaN-Get1 fusion in pFastBac1 (insect cells)
- **Induction**: Galactose induction (yeast); Baculovirus infection (insect cells)

### Purification Workflow

- **Expression system**: S. cerevisiae / Sf9 insect cells
- **Expression construct**: Get1/Get2 complex with C-terminal tags
- **Tag info**: His6-tag or Strep-tag II, cleavable

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization | — | DDM (for amphipol reconstitution) or LMNG (for nanodisc) |  |
| Affinity chromatography | Ni-NTA / Strep-Tactin | — |  |  |
| Amphipol reconstitution or nanodisc assembly | Bio-beads detergent removal | — |  | Reconstituted in PMAL-C8 amphipol or A835 amphipol for cryo-EM; nanodisc assembled with MSP1E3D1 scaffold protein |
| Size-exclusion chromatography | SEC | — | 20 mM HEPES pH 7.5, 150 mM NaCl, 2 mM DTT |  |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### GET insertase conformational states (state 1 and state 2)

The GET insertase adopts two distinct conformations: state 1 (observed in C. thermophilum and hsGet1/Get2^Deltaalpha3') where the hydrophilic grooves point inward toward each other and helix alpha3' interacts with Get1 TMD2 of the opposing heterodimer; and state 2 (observed in wild type hsGet1/Get2) where the grooves point outward and helix alpha3' binds the Get3 TABD, enabling lateral release of the TA protein.

### Membrane thinning by the GET insertase

The GET insertase induces significant thinning of the lipid bilayer in the vicinity of the hydrophilic groove and Get2 TMD3. Atomistic MD simulations show the membrane is notably thinner near hsGet1/Get2, independent of lipid composition. This thinning lowers the energetic barrier for TA protein insertion by reducing the hydrophobic distance the polar C-terminal extension must cross.

### Conserved core fold of Get1/Get2 heterodimer

The core fold of the Get1/Get2 heterodimer is conserved from lower to higher eukaryotes, maintaining key features including the hydrophilic groove, helix alpha3', the ER cap, and the amphipathic helix (AH). The structure from C. thermophilum shows the same overall architecture as the human complex.


## Cross-References

- [Get3 (TRC40) TA Protein Targeting Factor](/xray-mp-wiki/proteins/secretion-translocon/get3/) — Get3 delivers TA proteins to the Get1/Get2 insertase complex
- [Hydrophilic Groove Insertion Mechanism](/xray-mp-wiki/concepts/miscellaneous/hydrophilic-groove-insertion/) — The GET insertase uses a hydrophilic groove to facilitate TA protein membrane insertion
- [GET Pathway for Tail-Anchored Protein Insertion](/xray-mp-wiki/concepts/miscellaneous/get-pathway/) — Get1/Get2 is the membrane insertase complex of the GET pathway
