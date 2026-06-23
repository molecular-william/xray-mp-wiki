---
title: A. fulgidus AglB-L Oligosaccharyltransferase
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1309777110]
verified: false
---

# A. fulgidus AglB-L Oligosaccharyltransferase

## Overview

AglB-L (archaeal glycosylation B, Long form) from Archaeoglobus fulgidus is a single-subunit membrane oligosaccharyltransferase (OST) that transfers oligosaccharide chains to asparagine residues in proteins (N-linked glycosylation). The full-length crystal structures were determined at 2.5 A and 3.41 A resolutions in two crystal forms. The structures reveal 13 transmembrane helices with a characteristic long plastic loop (EL5) in the transmembrane region. The catalytic center consists of conserved acidic residues (Asp47, Glu360) coordinating a divalent metal ion (Zn2+ or Mg2+). AglB-L shares high structural similarity with the eubacterial PglB from Campylobacter lari, despite less than 20% sequence identity, indicating a conserved catalytic mechanism across archaeal, eubacterial, and eukaryotic (STT3) OSTs.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1309777110 | unknown | 2.50 A | C2 | A. fulgidus AglB-L full-length; C-terminal His10-tag after thrombin cleavage site; crystal form 1 in n-octyl-beta-D-glucopyranoside (OG); Zn2+ and sulfate ion bound; EL5 loop disordered | Zn2+ (catalytic site, six-coordinated, distorted octahedral), sulfate ion (mimics dolichol-phosphate phosphate group) |
| doi/10.1073##pnas.1309777110 | unknown | 3.41 A | P4_3_2_1_2 | A. fulgidus AglB-L full-length; crystal form 2 in [LDAO](/xray-mp-wiki/reagents/detergents/ldao/); resting state with well-ordered EL5 plastic loop | unknown metal ion; no sulfate ion bound |

## Expression and Purification

- **Expression system**: Escherichia coli C43 (DE3)
- **Construct**: A. fulgidus AglB-L (O29867_ARCFU) cloned into pET-52b(+) between NcoI and XhoI sites; C-terminal His10-tag after thrombin cleavage site; cultured in Terrific Broth with [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) (100 mg/L) at 310 K overnight

### Purification Workflow

- **Expression system**: E. coli C43 (DE3)
- **Expression construct**: C-terminal His10-tag
- **Tag info**: C-terminal His10-tag, removable by thrombin cleavage

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Overnight expression | not applicable | Terrific Broth with 100 mg/L [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) + not applicable | Overnight culture at 310 K |
| Protein extraction and purification | Detergent solubilization and affinity purification | not specified | not specified + not specified (monodisperse in various detergents by gel filtration) | Monodisperse and monomeric in various detergents by gel filtration chromatography |

**Final sample**: Purified in n-dodecyl-beta-D-maltopyranoside (DDM) for activity assays
**Yield**: Highest yield among three A. fulgidus AglB paralogs


## Crystallization

### doi/10.1073##pnas.1309777110

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | A. fulgidus AglB-L in [OG](/xray-mp-wiki/reagents/detergents/og/) |
| Reservoir | 0.2 M zinc sulfate, 0.1 M sodium [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate/) buffer pH 4.6, 15% (vol/vol) polyethylene glycol 4000 |
| Temperature | 293 K |
| Cryoprotection | 0.2 M zinc sulfate, 0.1 M sodium [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate/) pH 4.6, 15% [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) 4000, 1% [OG](/xray-mp-wiki/reagents/detergents/og/), 15% ethylene glycol |
| Notes | Crystal form 1; space group C2; contains 0.06% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) added; Zn2+ and sulfate bound; EL5 disordered |

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | A. fulgidus AglB-L in [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) |
| Reservoir | 0.02 M [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) HCl pH 8.0, 22% (wt/vol) polyethylene glycol 550MME |
| Temperature | 293 K |
| Cryoprotection | 0.02 M [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) HCl pH 8.0, 28% [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) 550MME, 0.06% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) |
| Notes | Crystal form 2; space group P4_3_2_1_2; resting state with well-ordered EL5 plastic loop; no sulfate bound |


## Biological / Functional Insights

### Conserved 13-TM architecture across archaeal and eubacterial OSTs

The A. fulgidus AglB-L structure reveals 13 transmembrane helices with a topology nearly identical to C. lari PglB, despite <20% sequence identity. The TM domain comprises ca. 400-500 residues, and the characteristic long EL1 (extracellular loop 1) and EL5 loops are conserved. This striking similarity indicates that eukaryotic STT3 catalytic subunits share the same 13-TM + CC (central core) architecture.

### Plastic EL5 loop dynamics in catalytic cycle

The EL5 loop is completely disordered in crystal form 1 (sulfate-bound, representing the lipid-phosphate bound state) but well-ordered in crystal form 2 (resting state). This conformational flexibility suggests that EL5 becomes unstructured upon ligand binding, disrupting the porthole structure to facilitate release of the glycosylated product. The conserved Glu360 in the TIXE motif on EL5 serves as a coordination switch responding to ligand binding.

### Metal coordination by conserved DXD/DXH motifs

The catalytic site contains a divalent metal ion (Zn2+ in crystal form 1, substituting for the natural cofactor Mg2+) coordinated by Asp47 (first DXD motif on EL1), Asp161 and His163 (second DXH motif on EL2), and three water molecules in a distorted octahedral geometry. Glu360 on the EL5 loop completes the carboxylate dyad. Mutagenesis confirms Asp47 and Glu360 are critical for activity; charge-preserving mutations (Asp47Glu, Glu360Asp) retain partial activity.

### Ser/Thr-binding pocket in sequon recognition

The C-terminal globular domain contains a Ser/Thr-binding pocket formed by the WWD motif (part of the WWDYG motif) and a second signature residue (Lys or Ile) of the DK/MI motif. In crystal form 2, the pocket adopts a Lys-type conformation with W550, W551, D552, and K618 forming the binding site (compared to W463, W464, D465, I572 in C. lari PglB). The Lys-type pocket is proposed to be more dynamic on millisecond timescales, enabling efficient scanning of nascent polypeptide chains during co-translational glycosylation in eukaryotes.

### Sulfate ion mimics dolichol-phosphate binding

In crystal form 1, a sulfate ion is bound 5.0 A from the Zn2+ ion, interacting with His81, His162, Trp215, and Arg426. Mutagenesis of these residues (particularly His81Ala, His162Ala, Arg426Ala) severely impairs activity. The sulfate is proposed to mimic the phosphate group of the dolichol-phosphate carrier. A docking model shows the isoprene units of dolichol phosphate fitting within a hydrophobic groove on the protein surface.


## Cross-References

- [N-Glycosylation Sequon](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/n-glycosylation-sequon/) — AglB-L recognizes the N-glycosylation sequon (Asn-X-Ser/Thr) via the Ser/Thr-binding pocket in its C-terminal domain
- [Catalytic Cycle of Oligosaccharyltransferase](/xray-mp-wiki/concepts/enzyme-mechanisms/ost-catalytic-cycle/) — The AglB-L crystal structures in two forms provide structural snapshots of different states in the OST catalytic cycle
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for AglB-L purification and activity assays
- [n-Octyl-beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/) — Detergent used in crystal form 1 crystallization
- [LDAO (Lauryldimethylamine-N-oxide)](/xray-mp-wiki/reagents/detergents/ldao/) — Detergent used in crystal form 2 crystallization
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [N-Glycosylation Sequon](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/n-glycosylation-sequon/) — Key concept related to this protein
- [Catalytic Cycle of Oligosaccharyltransferase](/xray-mp-wiki/concepts/enzyme-mechanisms/ost-catalytic-cycle/) — Key concept related to this protein
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein mentioned in the study
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein mentioned in the study
