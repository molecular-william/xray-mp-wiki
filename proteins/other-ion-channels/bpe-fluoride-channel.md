---
title: "Fluoride Channel from B. pertussis (Bpe)"
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2018.02.004, doi/10.1038##NATURE14981]
verified: false
---

# Fluoride Channel from B. pertussis (Bpe)

## Overview

The fluoride channel from [Bordetella pertussis](/xray-mp-wiki/organisms/bordetella-pertussis) (Bpe) is a member of the Fluc family of fluoride-specific ion channels. Bpe assembles as a symmetrical homodimer with antiparallel transmembrane topology, such that the channel's intracellular and extracellular ion entryways are structurally identical. Each subunit contributes residues to both of the channel's two F- permeation pathways. Bpe crystallization requires engineered monobody chaperones (S7, L2, S8, etc.) that bind to both ends of the channel dimer. The channel forms a dual-topology homodimer where each subunit spans the membrane in opposite orientation, a defining feature of the Fluc family. High-resolution structures (PDB 5A40 at 3.6 A, 5A41 at 2.1 A) reveal a double-barrelled architecture with two F- permeation pathways, a centrally coordinated Na+ ion in the channel plug, and F- ion binding sites at conserved positions involving phenylalanine quadrupole interactions.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2018.02.004 | 6BQO | 2.8 | C 1 2 1 | Bpe fluoride channel homodimer from B. pertussis with monobody S8 bound to one end | Monobody S8 (~950 A^2 hydrophobic interface, peripheral hydrogen bonds and salt bridges) |
| doi/10.1038##NATURE14981 | 5A40 | 3.6 | P 21 21 2 | Bpe fluoride channel homodimer from B. pertussis with monobody S7 bound to both ends | Monobody S7, Na+ (centrally coordinated), Hg (labelling site) |
| doi/10.1038##NATURE14981 | 5A41 | 2.1 | P 1 | Bpe fluoride channel homodimer from B. pertussis with monobody L2 bound to both ends | Monobody L2, Na+ (centrally coordinated), F- (putative, F1 and F2 sites) |

## Expression and Purification

- **Expression system**: Escherichia coli. Bpe from B. pertussis was expressed from pET21c vector with C-terminal hexahistidine tag, as described in Stockbridge et al. 2013.

- **Construct**: Bpe fluoride channel homodimer from B. pertussis, full-length with C-terminal hexahistidine tag.


### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression | -- | -- + -- | Bpe expressed from pET21c with C-terminal hexahistidine tag in E. coli, as described in Stockbridge et al. 2013 |
| Purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) (via hexahistidine tag) | -- + -- | Purification as described in Stockbridge et al. 2013 |


## Crystallization

### doi/10.1016##j.str.2018.02.004

| Parameter | Value |
|---|---|
| Method | In meso ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase)) crystallization |
| Protein sample | Bpe-Fluc homodimer in detergent, co-complexed with monobody S8 |
| Temperature | Not specified |
| Growth time | 2-3 days |
| Notes | Crystals appeared in 2-3 days in several low molecular weight PEGs including 30% PEG 400, 550MME, and 600. Final optimized crystals grown in 26% PEG 550MME, 0.1M sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate) pH 5.0. Data collected at beam-line I04 Diamond Light Source, UK. Space group C 1 2 1. |

### doi/10.1038##NATURE14981

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) (sitting drop) |
| Protein sample | Bpe-Fluc homodimer in detergent, co-complexed with monobody S7 |
| Reservoir | Not specified in detail |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Crystals grown from detergent micelles. Monobody S7 was required for crystallization; crystals could not be grown without monobody. SAD phasing with Hg-labelled Bpe at unique cysteine residue (E94C). Space group P21212. Resolution 3.6 Angstrom. |

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) (sitting drop) |
| Protein sample | Bpe-Fluc homodimer in detergent, co-complexed with monobody L2 |
| Reservoir | Not specified in detail |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | In meso crystallization attempt. Crystals diffracting to 2.1 Angstrom obtained in presence of 20 mM F-. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement). Space group P1. Monobody L2 binds in different orientation than S7 but also extends long loop into vestibule. |


## Biological / Functional Insights

### Double-barrelled channel architecture

The 2.1 A Bpe-L2 structure reveals a surprising double-barrelled channel architecture in which two F- ion pathways span the membrane. The channel is hourglass-shaped, with wide vestibules symmetrically opening to two aqueous solutions separated by a solid plug of protein 10-15 A thick. Each F- permeation pathway is lined with H-bond donors along TM4, creating a polar track through which largely dehydrated F- ions move across the membrane. The narrow pores and unusual anion coordination exploiting quadrupolar edges of conserved phenylalanine rings provide the basis for F- selectivity over Cl- by >10^4.

### Centrally coordinated Na+ ion in the channel plug

A prominent electron density resides in the centre of the plug separating the vestibules, precisely on the homodimer's two-fold non-crystallographic axis. This density is identified as a Na+ ion coordinated by four backbone carbonyl groups from residues in each subunit associated with the conserved TM3 break (G77 and T80). This coordination is inconsistent with F-, water, a divalent metal, or K+. The deeply buried cation could not exchange with aqueous solution if the plug remained intact, and it is proposed to be an important structural component incorporated irreversibly upon dimer assembly.

### F- ion binding sites at F1 and F2 positions

Four electron densities in the Bpe-L2 structure are identified as F- ions at F1 and F2 sites in non-crystallographic symmetry-related pairs. These sites are located in crevices between TM2, TM3b, and TM4 near the periphery of the channel. The crevice-facing surface of TM4 is lined with H-donating side chains (Y104, S108, S112, T116 in Bpe), creating a polar track along which F- ions move. The conserved phenylalanine residues (F82, F85) provide unusual edge-on coordination exploiting their quadrupolar edges for F- recognition. Mutations F85I and F82I reduce F- efflux by two and three orders of magnitude, respectively.

### Channsporter mechanism for F- permeation

The conduction mechanism for F- transport through Fluc channels is proposed to be distinct from classic diffusion through a fixed, water-filled channel. Instead, F- moves along the pore concomitant with a rotameric switch of the conserved N43 side chain, such that the amide nitrogen remains H-bonded as the anion moves along the pore. This mechanism incorporates a central feature of membrane transporters: substrate transport coupled to concerted movement of the protein. The four F- ions observed probably occupy the channel simultaneously, suggesting multi-ion conduction phenomena akin to those in K+ channels.

### Cork-in-bottle occlusion mechanism

The Bpe-S8 structure provides direct structural evidence that monobody binding does not induce local structural changes in the fluoride channel. Only one end of the channel binds a monobody, yet both ends are structurally identical and identical to all previously solved doubly complexed structures. The monobody's diversified loop physically occludes the aqueous vestibule through which fluoride ions enter and leave the transport pathway, acting as a "cork" in a bottle. This mechanism of physical occlusion rather than allosteric closure explains why the channel structure represents the functional, F- conducting conformation.

### Dual-topology homodimer structure

Bpe assembles as a symmetrical homodimer with antiparallel transmembrane topology. The two subunits are arranged such that intracellular and extracellular ion entryways are structurally identical. The channel dimer contains two F- permeation pathways, with each subunit contributing residues to both pathways. This dual-topology arrangement is a defining feature of the Fluc family of fluoride channels.

### Monobody-channel interface

The Bpe-S8 monobody interface is ~950 A^2 and mainly hydrophobic. Hydrogen bonds and salt bridges between S8 and the channel are rare and peripheral. The only polar monobody/channel interactions within H-bonding distance are between D80 (S8) and T3 (channel) at the periphery, the carbonyl oxygen of Y43 (S8) and the backbone amide of Y98 (channel) at the opposite periphery, and a salt bridge between E48 (S8) and the channel at the periphery.


## Cross-References

- [Monobody S7](/xray-mp-wiki/reagents/protein-tags/monobody-s7/) — Engineered protein inhibitor used to crystallize Bpe-S7 complex (PDB 5A40, 3.6 A)
- [Monobody L2](/xray-mp-wiki/reagents/protein-tags/monobody-l2/) — Engineered protein inhibitor used to crystallize Bpe-L2 complex (PDB 5A41, 2.1 A)
- [Monobody S9](/xray-mp-wiki/reagents/protein-tags/monobody-s9/) — Engineered protein inhibitor used to crystallize Ec2-S9 complex (PDB 5A43); homologous monobody family
- [Fluoride Channel from E. coli (Ec2)](/xray-mp-wiki/proteins/other-ion-channels/fluc-ec2/) — Ec2 is the E. coli Fluc homologue; identical fold with 33% sequence identity; Ec2-S9 structure confirms conserved F- binding sites
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for Bpe purification and crystallization (5 mM)
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in Bpe purification and crystallization (10 mM, pH 7.0)
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — NaF used in Bpe purification buffer (100 mM) for fluoride channel activity
- [Dual-Topology Channels](/xray-mp-wiki/concepts/transport-mechanisms/dual-topology-channels/) — Bpe is a dual-topology homodimer; 2.1 A structure confirms double-barrelled architecture
- [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) — Crystallization method used for structure determination
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) — Structure determination method used
