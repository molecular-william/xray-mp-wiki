---
title: NaK Channel from Bacillus cereus
created: 2026-06-02
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature04508, doi/10.1038##nsmb.1531, doi/10.1073##pnas.0707324104, doi/10.1073##pnas.1013636108, doi/10.1073##pnas.1013643108, doi/10.1073##pnas.1111688108]
verified: false
---

# NaK Channel from Bacillus cereus

## Overview

NaK is a non-selective tetrameric cation channel from Bacillus cereus that conducts both Na+ and K+ ions. It shares high sequence homology and overall architecture with the bacterial [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) K+ channel, but its selectivity filter adopts a different architecture that results in loss of ion selectivity. Engineering of NaK mutants has enabled systematic analysis of ion selectivity mechanisms, including the NaK2K mutant which recapitulates a K+-selective filter with four contiguous ion binding sites. This paper demonstrates that a bridging hydrogen bond between an aromatic residue on the pore helix (Tyr55) and an acidic residue following the TVGYG signature sequence (Asp68) is essential for maintaining the four-sited K+ selective filter configuration.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature04508 | 2NKA | 2.4 | C2221 | NaK channel residues 1-103 | Na+ |
| doi/10.1038##nature04508 | 2NKB | 2.8 | C2221 | NaK channel residues 1-104 | K+ |
| doi/10.1038##nsmb.1531 | 2AHY | 1.6 | I4 | NaKN delta 19 open conformation | Various monovalent cations |
| doi/10.1073##pnas.1013636108 | not specified | 1.62 | I4 | NaK2CNG-D mutant on NaKN delta 19 background | K+ |
| doi/10.1073##pnas.1013636108 | not specified | not specified | I4 | NaK2K (D66Y/N68D) on NaKN delta 19 background | K+ |
| doi/10.1073##pnas.1013643108 | not specified | 1.62 | not specified | NaK2CNG-D on NaKN delta 19 background | K+, Na+, Ca2+ |
| doi/10.1073##pnas.1013643108 | not specified | 1.58-1.95 | not specified | NaK2CNG-E chimera on NaKN delta 19 background | K+, Na+, Ca2+ |
| doi/10.1073##pnas.1013643108 | not specified | 1.58-1.95 | not specified | NaK2CNG-N chimera on NaKN delta 19 background | K+, Na+, Ca2+ |
| doi/10.1073##pnas.1111688108 | 3E8H | 1.80 | not specified | NaK_D66Y mutant | not specified |
| doi/10.1073##pnas.1111688108 | not specified | 1.95 | not specified | NaK_N68D mutant | not specified |
| doi/10.1073##pnas.1111688108 | 3OUF | 1.55 | not specified | NaK2K (D66Y/N68D) double mutant | K+ |
| doi/10.1073##pnas.1111688108 | not specified | not specified | not specified | NaK2K mutants (Y66F, Y55F, Y55W, D68E) and Kir-mimicking NaK (V59E/D66Y/F69R, Y55L/V59E/D66Y/F69R) | not specified |
| doi/10.1107##s205225252100213x | 6v8y | 1.53 | C2221 | NaKΔ19 (truncated NaK, residues 20-103) crystallized with both K+ and Na+ present | K+, Na+ |

## Expression and Purification

### Purification Workflow

*Source: doi/10.1038##nature04508*

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: NaK channel in pQE60 vector

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent solubilization |  | NaCl or KCl + [n-Decyl-β-D-maltoside](/xray-mp-wiki/reagents/detergents/dm/) | Protein purified as a tetramer |

### Purification Workflow

*Source: doi/10.1073##pnas.0707324104*

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: NaK channel mutants in pQE60 vector

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli culture |  |  | Cloned into pQE60, expressed in E. coli XL1-Blue cells |
| Purification | Detergent solubilization and purification |  | Monovalent salt (NaCl, RbCl, or LiCl) + n-Decyl-β-D-maltoside (DM) | Purified as tetramers in DM with monovalent salt for crystallization |

### Purification Workflow

*Source: doi/10.1073##pnas.1013643108*

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: NaK2CNG chimeras on NaKN delta 19 background with F92A mutation

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli culture |  |  | Cloned into pQE60, expressed in E. coli XL1-Blue cells |
| Purification | Detergent solubilization and purification |  | Monovalent salt (NaCl, KCl) + n-Decyl-β-D-maltoside (DM) | Purified as tetramers |
| Reconstitution | [Proteoliposome Reconstitution](/xray-mp-wiki/methods/quality-assessment/proteoliposome-reconstitution/) |  | HEPES pH 7.4 | Reconstituted into 3:1 [POPE](/xray-mp-wiki/reagents/lipids/pope/):[POPG](/xray-mp-wiki/reagents/lipids/popg/) lipid vesicles at 0.1 ug/mg protein/lipid ratio for functional studies |

### Purification Workflow

*Source: doi/10.1073##pnas.1013636108*

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: NaK mutants on NaKN delta 19 background

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli culture |  |  | Cloned into pQE60, expressed in E. coli XL1-Blue cells |
| Purification | Detergent solubilization and purification |  | Monovalent salt + n-Decyl-β-D-maltoside (DM) | Same procedures as NaKN delta 19 |

### Purification Workflow

*Source: doi/10.1073##pnas.1111688108*

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: NaK mutants on NaKN delta 19 background with F92A mutation

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli culture |  |  | All NaK mutants cloned into pQE60 |
| Purification | Detergent solubilization and purification |  | Monovalent salt + n-Decyl-β-D-maltoside (DM) | Protein purification followed NaKN delta 19 protocol |
| Reconstitution | [Proteoliposome Reconstitution](/xray-mp-wiki/methods/quality-assessment/proteoliposome-reconstitution/) |  | Not specified | Reconstituted into 3:1 [POPE](/xray-mp-wiki/reagents/lipids/pope/):[POPG](/xray-mp-wiki/reagents/lipids/popg/) lipid vesicles at 0.2 ug/mg protein/lipid ratio for giant liposome patch clamp |


## Crystallization

### doi/10.1038##nature04508

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | NaK channel at 30-35 mg/mL |
| Reservoir | 36-42% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 200 mM CaCl2, 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5-8.5, 4% t-butanol |
| Temperature | 20 C |
| Notes | Crystals of space group C2221 |

### doi/10.1073##pnas.0707324104

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Wild-type and mutant NaK channels at 30-35 mg/mL |
| Reservoir | 200 mM CaCl2, 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 37-42% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 4% [tert-Butanol](/xray-mp-wiki/reagents/additives/tert-butanol/) |
| Temperature | 20 C |
| Notes | Space group C2221 |

### doi/10.1038##nsmb.1531

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | NaKN delta 19 (truncated construct) |
| Reservoir | 55-70% (v/v) [MPD](/xray-mp-wiki/reagents/additives/mpd/), 1 mM CaCl2, 100 mM [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) pH 9.5 |
| Cryoprotection | Crystals frozen in liquid propane; crystallization solution served as cryoprotectant |
| Notes | Open conformation, space group I4 |

### doi/10.1073##pnas.1013636108

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | NaK2CNG-D and NaK2K mutants at 30-35 mg/mL |
| Reservoir | [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, CaCl2, [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0 |
| Temperature | 20 C |
| Notes | Space group I4, same conditions as NaKN delta 19 |

### doi/10.1073##pnas.1013643108

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | NaK2CNG chimeras at 30-35 mg/mL |
| Reservoir | [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, CaCl2, [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0 |
| Temperature | 20 C |
| Notes | Structures between 1.58 and 1.95 A resolution |

### doi/10.1073##pnas.1111688108

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | NaK mutants at 30-35 mg/mL |
| Reservoir | Similar to NaKN delta 19 conditions |
| Temperature | 20 C |
| Notes | All mutant structures determined in open conformation between 1.70 to 1.95 A resolution |


## Biological / Functional Insights

### Ion conduction properties of NaK

Functional analysis using 86Rb flux assays shows that NaK can conduct both Na+ and K+ ions. A truncated form (NaKN delta 19) lacking the N-terminal M0 helix showed higher flux rates than full-length NaK. The channel conducts K+ ions better than Na+ ions and is unable to conduct Li+ or [NMG](/xray-mp-wiki/reagents/additives/n-methyl-d-glucamine/)+. Na+ and K+ ions bind at sites 3, 4 and the central cavity without preference, consistent with the non-selective nature of the channel.

### Cyclic nucleotide-gated channel pore architecture

The NaK selectivity filter sequence (TVGDG) resembles that of cyclic nucleotide-gated (CNG) channels, which also lack the tyrosine and [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues from the conserved TVGYG sequence. The external Ca2+-binding site in NaK reveals the structural basis of external divalent cation blockage observed in CNG channels, relevant for visual transduction.

### Ion binding sites and divalent cation block

Electron density maps show ions binding at the extracellular entrance, along the selectivity filter, and in the central cavity. Monovalent cations bind at sites 3, 4 and the central cavity, while divalent cations (Ca2+) bind only at the extracellular entrance to the filter, formed by four carbonyl oxygen atoms from Gly67 residues. The NaK selectivity filter retains its proper conformation in both Na+ and K+ environments, unlike [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) which requires K+ to stabilize the filter.

### Open conformation and inner helix bending at Gly87 gating hinge

The NaKN delta 19 structure reveals the intracellular gate in an open state. Inner helices develop a 34 degree bend at Gly87 (the conserved gating hinge) that splays the gate wide open. Inner helices also undergo a 45 degree clockwise twist. Outer helices tilt tangentially by about 11 degrees without twisting. The open NaK structure superimposes with [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) (PDB 1LNQ) with an r.m.s.d. of 0.74 A.

### Phe92 constriction point in open pore

In the open NaK pore, Phe92 forms a constriction point with an ion-pathway diameter of about 6.5 A — narrower than the open [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) channel (~9.5 A). The F92A mutation increases the ion-conduction pathway diameter to 10.5 A and enhances ion conduction rates as measured by 86Rb flux assays.

### Inter- and intrasubunit rearrangements during gating

Comparison of closed and open NaK structures reveals distinct rearrangements. In the closed state, Phe92 contacts a hydrophobic patch on the neighboring helix; in the open state, the hydrophobic patch slides two helical turns and forms new van der Waals contacts with Phe85. Intrasubunit interactions between inner and outer helices remain similar.

### Conservation of gating mechanics with K+ channels

The closed NaK structure (PDB 2AHY) superimposes well with closed [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) (PDB 1K4C) with an r.m.s.d. of 0.73 A. The open NaKN delta 19 structure superimposes with open [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) (PDB 1LNQ) with an r.m.s.d. of 0.74 A. These structural correlations confirm that gating mechanics are conserved between NaK and K+ channels.

### Mechanism of Ca2+ specificity at the NaK selectivity filter

The external Ca2+ binding site is formed by four backbone carbonyl oxygen atoms from Gly-67 of each subunit. The conserved acidic residue Asp-66 does not directly chelate Ca2+ but instead forms a hydrogen bond with the amide nitrogen of the Gly-67/Asn-68 peptide bond, polarizing the backbone and placing a partial negative charge on the Gly-67 carbonyl oxygen. D66N abolished Ca2+ binding, D66E enhanced it, and D66AS70E restored it.

### Second Ca2+ binding site within the NaK selectivity filter

In addition to the external site, a second Ca2+ binding site was identified at site 3 within the NaK selectivity filter. This intrapore site lacks acidic residues and can also bind monovalent cations, providing a structural basis for Ca2+ permeation through the NaK pore. The existence of two Ca2+ binding sites is consistent with functional studies of CNG channels.

### Ca2+ permeation demonstrated by 45Ca flux assay

Direct measurement of Ca2+ permeation through NaK was achieved using 45Ca flux assays in liposomes. Time-dependent accumulation of 45Ca was observed in NaK-containing liposomes but not in control liposomes. These data support the 'permeating block' model where Ca2+ both blocks monovalent currents and permeates the channel.

### CNG channel pore architecture revealed by NaK2CNG chimeras

The NaK2CNG-D, NaK2CNG-E, and NaK2CNG-N chimeras faithfully represent the pore architecture of cyclic nucleotide-gated (CNG) channels. Their selectivity filters contain three contiguous ion binding sites with a distinct architecture intermediate between NaK and [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/). Although NaK2CNG chimeras permeate Na+ and K+ equally well, Na+ and K+ bind with different ion-ligand geometries.

### Ca2+ binding mechanism in CNG channel selectivity filter mimics

High-resolution structures of NaK2CNG chimeras reveal that Ca2+ is exclusively chelated by backbone carbonyl oxygen atoms and not directly by the conserved acidic side chain (Glu/Asp). In NaK2CNG-E, the glutamate side chain (Glu66) is oriented tangential to the ion conduction pathway. Ca2+ binding positions differ among chimeras: NaK2CNG-E binds Ca2+ at site 3 only, NaK2CNG-D binds Ca2+ at sites 2, 3, and above the external entrance, and NaK2CNG-N binds Ca2+ only at the external funnel.

### Selectivity filter architecture of NaK

The NaK selectivity filter preserves only two cation-binding sites equivalent to sites 3 and 4 of a K+ channel selectivity filter. Unlike K+ channel selectivity filters that contain four equivalent K+-binding sites, NaK's GDG residues adopt different backbone conformations.

### Structural basis of ion selectivity in K+ channels

Comparison of NaK and [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) provides experimental demonstration that electrostatic repulsion between carbonyl oxygen atoms is not the origin of K+ over Na+ selectivity. Instead, protein atoms surrounding the ion-binding site confer size-selectivity through geometric constraints.

### Number of contiguous ion binding sites determines K+ selectivity

Engineering of NaK-based cation channel pores with two (NaK), three (NaK2CNG-D), or four (NaK2K) contiguous ion binding sites demonstrated that only the channel with four sites is K+ selective. Single channel electrophysiology revealed that NaK2K has higher single channel conductance for K+ than NaK2CNG-D.

### Bridging hydrogen bond between Tyr55 and Asp68 is essential for K+ selectivity

The Tyr66 side chain in NaK2K points into a hydrophobic pocket and forms a hydrogen bond with Thr60. The Asp68 side chain forms a bridging hydrogen bond with Tyr55 on the pore helix. Both interactions work in concert to maintain the filter architecture in a K+ selective four-sited configuration. Single mutations at either position (D66Y or N68D alone) are insufficient to render NaK K+ selective. Neutralizing Asp68 to Asn or extending to Glu both abolish K+ selectivity, demonstrating that both the negative charge and precise distance are essential.

### Conservation of bridging H-bond in eukaryotic Kv channels

The equivalent Trp415-Asp428 hydrogen bond in rat Kv1.6 is also essential for K+ selectivity. Mutations that disrupt this bond (W415F, D428N, D428E) led to significant loss of K+ selectivity. The W415Y mutant preserved selectivity but exhibited fast C-type inactivation, suggesting that destabilization of filter packing can trigger inactivation.

### Kir channels use a distinct salt bridge mechanism

Inward-rectifier K+ (Kir) channels use a conserved acid-base salt bridge (Glu-Arg) instead of the Tyr-Asp bridging H-bond to stabilize the filter in a four-sited configuration. Kir-mimicking NaK mutants (V59E/D66Y/F69R) retained selectivity, but additional mutations (Y55L) were needed to fully recapitulate Kir properties.

### Structural plasticity of the selectivity filter enables nonselective cation conduction

The 1.53 A X-ray structure of NaKΔ19 crystallized in space group C2221 (PDB 6v8y) reveals asymmetric conformations of Asp66 and Asn68 in the selectivity filter between the two subunits in the asymmetric unit, demonstrating structural plasticity. This asymmetry reveals a previously unseen side-entry Na+ ion binding site adjacent to the SF, formed by a backbone carbonyl flip of Asp66. MD simulations and ssNMR data confirm the dynamic nature of the top part of the selectivity filter. K+ ions bind at sites 3 and 4 (coordinated by Thr63, Val64 carbonyls and Thr63 hydroxyls), while Na+ is found in the vestibule (site 2) and at the side-entry binding site. No Na+ permeation was observed in MD simulations even at high voltage, suggesting the Na+-conductive state requires larger conformational plasticity throughout the SF. The coupling between inner helix opening and SF width is weaker in NaK than in K+-selective channels.


## Cross-References

- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — NaK shares sequence homology and overall architecture with KcsA; structural comparison reveals selectivity filter differences
- [MthK (Methanobacterium thermoautotrophicum K+ Channel)](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) — Open NaK structure superimposes with open MthK (PDB 1LNQ)
- [n-Decyl-β-D-maltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used for NaK channel purification and crystallization
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Reconstitution buffer for functional studies
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Crystallization buffer for NaK structures
- [Human TRAAK Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/traak/) — Related K+ channel family
- [Shaker Kv1.2 Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/shaker-kv1-2/) — Related voltage-gated K+ channel
- [Proteoliposome Reconstitution](/xray-mp-wiki/methods/quality-assessment/proteoliposome-reconstitution/) — Method used in structure determination or purification
- [MPD](/xray-mp-wiki/reagents/additives/mpd/) — Additive used in purification or crystallization buffers
- [NMG](/xray-mp-wiki/reagents/additives/n-methyl-d-glucamine/) — Additive used in purification or crystallization buffers
