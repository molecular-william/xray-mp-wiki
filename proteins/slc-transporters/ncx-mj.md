---
title: NCX_Mj Sodium/Calcium Exchanger from Methanococcus jannaschii
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1215759]
verified: false
---

# NCX_Mj Sodium/Calcium Exchanger from Methanococcus jannaschii

## Overview

NCX_Mj is a sodium/calcium exchanger (NCX) from the archaeon Methanococcus jannaschii, belonging to the cation-Ca2+ exchanger superfamily. It is a membrane transporter that catalyzes the electrogenic exchange of three Na+ ions for one Ca2+ ion across the cell membrane, playing an essential role in maintaining Ca2+ homeostasis. Like all NCX proteins, it contains two highly conserved homologous alpha repeat sequence motifs arising from a gene-duplication event. NCX_Mj lacks the large intracellular regulatory domain found in eukaryotic NCX homologs, making it a minimal functional unit for ion transport. Its 1.9 A crystal structure revealed an outward-facing conformation with 10 transmembrane helices and four clustered ion-binding sites, providing the first structural insight into the NCX ion-exchange mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1215759 | not specified in raw text | 1.9 | P212121 | Full-length NCX_Mj | Ca2+, Na+ (modeled in binding sites) |
| doi/10.1126##science.1215759 | not specified in raw text | 3.6 | P212121 | Full-length NCX_Mj (conventional crystallization in detergent) | Cd2+ or Mn2+ (at divalent blockage site) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length NCX_Mj from Methanococcus jannaschii
- **Notes**: Expressed in E. coli cells for functional characterization via 45Ca2+ flux assays. Purification and crystallization construct details not specified in main text.

### Purification Workflow

- **Expression system**: Escherichia coli
- **Expression construct**: Full-length NCX_Mj

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli expression | — |  | NCX_Mj expressed in E. coli cells |
| Purification | Not detailed in main text | — |  | Purification details in Supporting Online Material. Protein used for both LCP and conventional crystallization. |


## Crystallization

### doi/10.1126##science.1215759

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified NCX_Mj in detergent (buffer details not specified in main text) |
| Temperature | 20 |
| Notes | LCP crystallization yielded well-diffracting crystals of P212121 space group with one subunit per asymmetric unit. Structure determined by SIRAS using samarium-derivatized crystals and refined to 1.9 A resolution. |

| Parameter | Value |
|---|---|
| Method | [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | Purified NCX_Mj in detergent |
| Notes | Conventional crystallization in detergent yielded crystals diffracting to 3.6 A. Structure determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using LCP structure as search model. CdCl2 or MnCl2 were essential additives, binding at the Smid site (divalent blockage site). Structure virtually identical to LCP structure. |


## Biological / Functional Insights

### Overall architecture and topology

NCX_Mj exists as a monomer with 10 transmembrane (TM) helices and
both termini on the extracellular side. Eight helices (TMs 2-5 and
7-10) form a tightly packed core perpendicularly embedded in the
membrane. TMs 1 and 6 are exceptionally long (~35 residues each),
oriented at ~45 degrees to the membrane surface, and loosely packed
against the core. The two alpha repeats (TMs 2-3 for alpha-1 and
TMs 7-8 for alpha-2) are bundled in the center surrounded by other
helices. Based on sequence similarity, eukaryotic NCX likely shares
the same 10-TM topology rather than the previously predicted 9-TM
topology.

### Four ion-binding sites with distinct specificities

Four ion-binding sites cluster at the center of NCX_Mj, related by
a two-fold rotational axis. SCa is specifically designed for Ca2+
binding with six oxygen ligands (backbone carbonyls of Thr50 and
Thr209, carboxylates of Glu54 and Glu213) from the GTSLPE signature
sequence within the alpha repeats. Three Na+ sites (Sext, Smid, Sint)
are arranged in a winding single file. Sext and Sint are optimized
for Na+ with five coordinating ligands. Smid has only four oxygen
ligands (tetradentate), making it suboptimal and allowing Na+
binding only at high concentration. The four sites share ligands -
Glu54 and Glu213 are shared by multiple sites, creating competition
between Na+ and Ca2+ binding.

### Outward-facing conformation and ion passageways

The NCX_Mj structure represents an outward-facing conformation with
two deep cavities on the extracellular surface providing independent
solvent-accessible passageways for external ion access to the
central binding sites. One passage connects to Sext and is surrounded
by TMs 3A, 7A, 7B, 9, and 10. The second connects to SCa and is
surrounded by TMs 3A, 7A, 5, and 6.

### Proposed inward-facing model and alternating access mechanism

Based on the two-fold symmetry of NCX_Mj, an inward-facing model
was proposed involving a simple sliding motion of TMs 1, 2A, 6,
and 7A hinged at bends between TMs 2A-2B and 7A-7B. The movement
slides these peripheral helices across a central hydrophobic patch,
closing the two outward-facing passageways and forming two
inward-facing ones. This rapid interchange between outward and
inward conformations enables the [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) for
consecutive ion-exchange reactions.

### Mechanism of 3:1 Na+:Ca2+ exchange stoichiometry

The exchange mechanism explains the 3:1 stoichiometry. Starting
with Ca2+ bound at SCa in the outward-facing state, two Na+ ions
first occupy Sext and Sint, competing for negatively charged ligands
shared with SCa and reducing Ca2+ affinity. A third Na+ occupies
Smid, further reducing Ca2+ affinity and causing Ca2+ release to the
extracellular side. After conformational change to the inward-facing
state, bound Na+ ions are released sequentially into the low
intracellular Na+ environment. Na+ release restores high Ca2+
affinity at SCa, and the cycle repeats. The mechanism does not
preclude alternative exchange ratios (e.g., transport of four Na+
ions when Ca2+ site is occupied by Na+).


## Cross-References

- [Na+/H+ Antiporter NhaA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/nhaa/) — Related Na+-coupled membrane transporter with alternating access mechanism
- [CLC-ec1 Cl-/H+ Antiporter](/xray-mp-wiki/proteins/slc-transporters/clc-ec1/) — Another ion-coupled antiporter with known structure and mechanistic studies
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/) — NCX_Mj alternating access transport mechanism shares principles with rocker-switch
- [Maltose Transporter MalFGK2 (E. coli)](/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/) — ABC transporter with alternating access mechanism for comparison
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — Related biological concept
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
