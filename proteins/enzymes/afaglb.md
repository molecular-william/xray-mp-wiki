---
title: "Archaeoglobus fulgidus Oligosaccharyltransferase AfAglB"
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, enzyme]
sources: [doi/10.1038##s42003-021-02473-8, doi/10.1021##acs.biochem.6b00901]
verified: false
---

# Archaeoglobus fulgidus Oligosaccharyltransferase AfAglB

## Overview

AfAglB is the catalytic subunit of the oligosaccharyltransferase (OST) from the archaeon Archaeoglobus fulgidus. It catalyzes the transfer of oligosaccharides from a dolichol-phosphate-linked oligosaccharide (LLO) donor to the asparagine residue in the N-glycosylation sequon (Asn-X-Ser/Thr), where X is any amino acid except proline. The structure of AfAglB in complex with a sequon-containing acceptor peptide and dolichol-phosphate was solved at 2.7 Å resolution using lipidic cubic phase (LCP) crystallization. The structure reveals the molecular basis for the strict exclusion of proline from the N-glycosylation sequon through the TIXE motif in the external loop 5 (EL5), which forms two inter-chain hydrogen bonds with the sequon. The conserved motifs (two DXD motifs, TIXE, WWDYG, DGGK, and DK motifs) are spatially arranged similarly across archaeal, eukaryotic, and eubacterial OST enzymes, suggesting a conserved catalytic mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s42003-021-02473-8 | 7E9S | 2.7 |  | AfAglB G617C mutant with tethered sequon peptide (TAMRA-APY(Dab)VTASCR-OH) and bound dolichol-phosphate | Dolichol-phosphate, Mn2+ |

## Expression and Purification

- **Expression system**: E. coli C43 (DE3)
- **Construct**: Full-length AfAglB (868 residues, UniProt O29867) with C-terminal His-tag in pET-52b(+)
- **Induction**: 1 mM IPTG at OD600 0.8-1.0
- **Media**: Terrific Broth

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth | E. coli C43 (DE3) fermentation | — |  | Induced at OD600 0.8-1.0 with 1 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) |
| Cell lysis | Microfluidizer or sonication | — | Standard lysis buffer |  |
| Membrane solubilization | Detergent extraction | — | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (n-Dodecyl β-D-maltopyranoside) |  |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA resin |  | C-terminal His-tag purification |
| Size-exclusion chromatography | SEC | — |  | Final polishing step |


## Crystallization

### doi/10.1038##s42003-021-02473-8

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | 7.7 MAG (1-(7Z-tetradecenoyl)-rac-glycerol) |
| Protein-to-lipid ratio | Not specified |
| Temperature | 20°C (cryo stream at 100 K) |
| Cryoprotection | [PEG400](/xray-mp-wiki/reagents/peg400/) in crystallization condition |
| Notes | Crystals grown in lipidic sponge mesophase. Microcrystals identified by magenta color of TAMRA dye. Data collected from 2529 microcrystals at microfocus beamline BL32XU, SPring-8. 483 datasets merged and scaled to 2.7 Å using KAMO. |


## Biological / Functional Insights

### TIXE motif forms inter-chain hydrogen bonds with the sequon

The TIXE motif (Thr357-Ile-Ala-Glu360) in the EL5 loop of AfAglB forms two inter-chain hydrogen bonds with the sequon-containing acceptor peptide. The carbonyl oxygen of Thr357 hydrogen bonds with the amide group of Ala+3, and the carbonyl oxygen of Val+1 hydrogen bonds with the amide group of Ala359, creating an antiparallel β-sheet-like arrangement. This interaction forces the sequon segment (Dab-Val-Thr) to adopt an extended conformation. The essential role of the TIXE motif was confirmed by extensive alanine-scanning mutagenesis of 44 residues in the EL5 loop, where the C-terminal segment containing TIXE (Leu356-Phe365) showed the most critical activity decreases.

### Structural basis for proline exclusion from the N-glycosylation sequon

The rigid sequon-TIXE frame structure forces the amino acid residues at positions +1 (middle of sequon) and +3 to adopt high φ dihedral angles around -150°. A Ramachandran plot analysis reveals that the ring structure of the proline side chain is incompatible with this φ backbone dihedral angle, as the proline φ angle is constrained to approximately -60° due to its pyrrolidine ring. This provides the structural basis for the absolute exclusion of proline from the N-glycosylation sequon observed across all domains of life — no glycosylated Asn-Pro-Thr or Asn-Pro-Ser sites exist in the N-GlycositeAtlas database of over 35,000 reviewed N-glycosylated sequences from human glycoproteins.

### Conserved catalytic architecture across domains of life

The spatial arrangements of conserved amino acid motifs — two DXD motifs, TIXE/SVSE, WWDYG, DGGK/DNXTZNX[T/S], and DK/MI motifs — are strikingly similar between archaeal AfAglB and eubacterial ClPglB. The metal ion (Mn2+) is coordinated by Asp47 in the first DXD motif, Asp161 and His163 in the second DXD motif, and three water molecules in a regular octahedral arrangement. Glu360 in the TIXE motif indirectly participates in metal coordination through two of the three water molecules. The phosphate group of dolichol-phosphate also interacts with the metal ion through two water molecules. The WWDYG and DK/MI motifs form the Ser/Thr-binding pocket in the C-terminal globular domain, explaining the requirement for hydroxy amino acids at position +2 of the sequon.

### LLO entry gate mechanism

The dolichol-phosphate ω-terminus binds in a tunnel structure at the interface between TM helices 8 and 9, suggesting that the LLO molecule enters the binding site through the gap between these helices. TM helix 9 must move in concert with the conformational change of the EL5 loop to enlarge the gap upon LLO binding. A similar mechanism was proposed for the Stt3 subunit in yeast OST. This differs from ClPglB where LLO was assumed to thread into the binding site under the disordered EL5 while TM helix 9 stayed in place, reflecting the different LLO structures (dolichol-based in Archaea/Eukarya vs. polypropenol-based in Eubacteria).


## Cross-References

- [N-Glycosylation](/xray-mp-wiki/concepts/n-glycosylation/) — AfAglB catalyzes the central oligosaccharide transfer step in N-glycosylation
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — The AfAglB structure was solved using LCP crystallization
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Method used in the study
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein mentioned in the study
- [A. fulgidus AglB-L Oligosaccharyltransferase](/xray-mp-wiki/proteins/enzymes/aglB/) — Related protein mentioned in the study
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein mentioned in the study
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Reagent used in the study
- [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) — Reagent used in the study
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Reagent used in the study
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in purification
