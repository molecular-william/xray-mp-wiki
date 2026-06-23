---
title: "Yeast F1c10-ATP Synthase Subcomplex (Mg-ADP Inhibited)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.m110.124529, doi/10.1126##science.286.5445.1700]
verified: false
---

# Yeast F1c10-ATP Synthase Subcomplex (Mg-ADP Inhibited)

## Overview

The F1c10 subcomplex of the Saccharomyces cerevisiae F1F0-ATP synthase includes the membrane rotor c10-ring linked to the catalytic F1 head (alpha3beta3gamma-delta-epsilon) by a central stalk. This 3.43 A crystal structure captures the Mg-ADP-inhibited state, where ADP is bound in both the beta-DP and beta-TP catalytic sites. The structure reveals the interface between the F1 central stalk and the c10-ring rotor, the proton binding site at cGlu59, and the unique twist of the yeast central stalk compared to the bovine enzyme. DCCD (dicyclohexylcarbodiimide) and azide were present during crystallization to stabilize the inhibited state.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.286.5445.1700 | 1qo1 | 3.9 |  | Saccharomyces cerevisiae F1c10 ATP synthase subcomplex (alpha3beta3gammadelta-epsilon plus c10-ring) with ADP and [AMP-PNP (Adenylyl Imidodiphosphate)](/xray-mp-wiki/reagents/ligands/amp-pnp/) | ADP, [AMP-PNP (Adenylyl Imidodiphosphate)](/xray-mp-wiki/reagents/ligands/amp-pnp/) |
| doi/10.1074##jbc.m110.124529 | 2WPD | 3.43 | P21 | Saccharomyces cerevisiae F1c10-ATP synthase subcomplex (alpha3beta3gammadelta-epsilon plus c10-ring) with Mg-ADP, DCCD, and azide | Mg-ADP |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae (native)
- **Construct**: Native F1F0-ATP synthase purified from mitochondrial membranes; F1c10 subcomplex obtained through crystallization-induced loss of peripheral stalk and subunit a

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Enzyme purification | Nickel-nitrilotriacetic acid [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 100 mM NaCl, 2 mM MgCl2, 25 mM [Trehalose](/xray-mp-wiki/reagents/additives/trehalose/), 0.5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 3 mM sodium azide, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0 + 0.64 mM n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Enzyme purified as described previously (ref 21) |
| Gel filtration | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (HR 10/30) | 0.64 mM n-dodecyl-beta-D-maltoside, 100 mM NaCl, 2 mM MgCl2, 25 mM [Trehalose](/xray-mp-wiki/reagents/additives/trehalose/), 0.5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 3 mM sodium azide, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0 + 0.64 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Fractions containing monomeric F1F0 (subunits alpha, beta, gamma, 4, 6, OSCP, d, delta, h, f, epsilon, i, 8, and 9) pooled |
| Pre-crystallization incubation | Incubation with ADP and DCCD | — |  | Enzyme (9 mg/mL) incubated with 660 uM ADP for 1 h at 20 C, then inhibited with 100 uM DCCD for 1 h in presence of 2.5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/) and 0.5 mM PMSF |


## Crystallization

### doi/10.1074##jbc.m110.124529

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | Yeast F1F0-ATP synthase (9 mg/mL) pre-incubated with ADP and DCCD |
| Reservoir | 100 mM sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 4.6, 300 mM NaCl, 20% (v/v) 2-methyl-2,4-pentanediol ([MPD](/xray-mp-wiki/reagents/additives/mpd/)) |
| Temperature | 20 |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals grown in the presence of 3 mM sodium azide and 0.64 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/). Crystallization resulted in spontaneous loss of peripheral stalk and subunit a, yielding F1c10 subcomplex. Data collected at ESRF and SOLEIL synchrotrons. |


## Biological / Functional Insights

### Discovery of the 10-member c-ring in yeast ATP synthase

The 3.9 A electron density map of the yeast F1c10 subcomplex provided the first direct structural evidence that the c-ring of ATP synthase contains 10 protomers, not the widely anticipated 12. This was an unexpected finding that had profound implications for the H+/ATP stoichiometry. The 10 c-subunits form an almost symmetrical ring, with an outer diameter of 55 A (top) to 42 A (equator) and an inner diameter of 27 A (top) to 17 A (equator). Each c-subunit forms a helical hairpin: the NH2-terminal alpha-helix (58 A long, ~39 residues) forms the inner ring, and the COOH-terminal alpha-helix (47 A long, ~31 residues) forms the outer ring with a ~23 degree kink around Gly62. The conserved carboxylate Glu59 lies about halfway along the outer helix. Five of the ten c-subunits (c1-c5) are covered by the delta subunit via their polar loops, and the gamma subunit contacts c9, c10, and c1, meaning six or seven consecutive c-subunits contact the foot of the central stalk. The exposed c-subunits show weaker density. The central cavity contains elongated density, possibly phospholipid.

### Mg-ADP inhibited state of yeast F1

ADP binds in both the beta-DP and beta-TP catalytic sites, while no nucleotide is observed in the beta-E site. The alpha-DP/beta-DP pair is moderately open (2180 A2 interface), resembling the novel conformation identified in yF1(I). The alpha-TP/beta-TP pair is highly closed (2960 A2 interface), resembling more a DP pair, representing a new Mg-ADP-inhibited state. Azide likely enhances ADP binding as observed in bovine structures.

### Central stalk twist is intrinsic to yeast F1

The foot of the yeast gamma-subunit central stalk is rotated by ~40 degrees relative to bovine structures in the direction of hydrolysis. This twisting is independent of the presence or absence of the c10-ring or crystal packing. The gamma-subunit interacts with the alpha-DP and beta-TP subunits via its N-terminal and C-terminal helices, respectively.

### F1-F0 rotor interface is primarily electrostatic

The interface between the F1 central stalk and the c10-ring is mainly electrostatic in nature. The gamma-subunit loop 195-202 contains three acidic residues (Glu198, Asp200, Asp202) that interact with the positively charged cArg39 residues on the c10-ring. The delta-subunit contributes a larger buried surface area (660 A2) compared to the gamma-subunit (200 A2). The c10-ring axis deviates from the F1 pseudo 3-fold axis by 8.5 degrees.

### Proton binding site at cGlu59

The essential cGlu59 carboxylate group is surrounded by hydrophobic residues (Leu57, Phe59, Ala62, Leu63) and is not involved in hydrogen bonding with adjacent residues. The closest potential H-bond acceptor, cLeu57 carbonyl oxygen of the adjacent c-subunit, is too far away. This hydrophobic environment distinguishes the proton-binding site from the Na+-binding site in I. tartaricus, which has polar residues at equivalent positions.

### c10-ring architecture

Each c-subunit forms a helical hairpin with an N-terminal inner helix (H1) and C-terminal outer helix (H2). A 14-degree kink at cLeu20 produces a two-turn 3_10 helix. A more pronounced 29-degree kink in H2 below cGlu59 creates the pore constriction. The c10-ring has an inner pore diameter of 14-16 A in the middle and 23 A at the bottom, lined by hydrophobic residues.


## Cross-References

- [Yeast Mitochondrial F1 ATPase](/xray-mp-wiki/proteins/pumps-atpases/yeast-f1-atpase/) — Soluble catalytic domain of the same ATP synthase complex; structural comparisons with different nucleotide states
- [Yeast Mitochondrial ATP Synthase c10 Ring](/xray-mp-wiki/proteins/pumps-atpases/yeast-mitochondrial-atp-synthase-c10-ring/) — Same c10-ring component; this structure shows the open conformation for comparison
- [Rotary ATPase Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/rotary-atpase-mechanism/) — The F1c10 subcomplex is the core rotary unit of the ATP synthase; Mg-ADP inhibition captures a paused state in the catalytic cycle
- [Binding-Change Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/binding-change-mechanism/) — ADP occupancy in both beta-DP and beta-TP sites illustrates the nucleotide occupancy pattern in the inhibited state
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Additive used in purification or crystallization buffers
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [MPD](/xray-mp-wiki/reagents/additives/mpd/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
