---
title: SERCA1a E309Q Mutant
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##emboj.2013.250]
verified: false
---

# SERCA1a E309Q Mutant

## Overview

The [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) E309Q mutant is a point mutant of the sarcoplasmic reticulum Ca²⁺-ATPase in which Glu309 (a key residue in Ca²⁺ site II) is replaced by glutamine. Despite previously being thought to bind only one Ca²⁺ ion, crystallographic and functional studies revealed that this mutant binds two Ca²⁺ ions with micromolar affinity but lacks cooperativity. The mutant adopts a catalytically incompetent Ca2E1 conformation due to impaired A-domain positioning and loss of the M1 helix kink, providing insight into the signal transmission mechanism between Ca²⁺ binding sites and the catalytic site in wild-type SERCA.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##emboj.2013.250 | TBD | 3.5 A | C2 | [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) E309Q mutant, 994 residues, with biotin acceptor domain at C-terminus | Two Ca2+ ions (sites I and II), [AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/) |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae (yeast)
- **Construct**: [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) E309Q mutant, 994 residues, with biotin acceptor domain linked to C-terminus by thrombin cleavage site
- **Notes**: Biotinylated in vivo in yeast; enables biotin-based affinity purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Biotin-based affinity purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (biotin-streptavidin) | Streptavidin resin | 100 mM MOPS/Tris pH 6.8, 80 mM KCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM CaCl2, 1 mM MgCl2 + [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) (octaethylene glycol dodecylether), ~36 mg/ml | Biotinylated in vivo in yeast; typical yield ~1 mg pure protein per preparation |

**Final sample**: ~36 mg/ml in 100 mM MOPS/Tris pH 6.8, 80 mM KCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM CaCl2, 1 mM MgCl2, ~36 mg/ml [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/)
**Yield**: ~1 mg per preparation


## Crystallization

### doi/10.1038##emboj.2013.250

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | E309Q mutant replicated with [DOPC](/xray-mp-wiki/reagents/lipids/dopc/) at [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/)/DOPC ratio 3:1 (w/w), supplemented with 10 mM CaCl2, 3 mM MgCl2, 1 mM [AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/) |
| Reservoir | [PEG6000](/xray-mp-wiki/reagents/additives/peg6000/), 27 mM MgCl2 |
| Mixing ratio | 1:1 |
| Temperature | 4 °C (cryoprotected by 10-20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), pre-cooled 24-48 h) |
| Growth time | 24-48 h |
| Cryoprotection | Addition of 10-20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) to reservoir, pre-cooling to 4 °C for 24-48 h |
| Notes | Crystals are hexagonal plates in space group C2. Unit cell: a = 167.0 Å, b = 55.8 Å, c = 161.8 Å, β = 109.3°. Resolution 70-3.5 Å (outer shell 3.60-3.5 Å). Unique reflections: 18,252 (1,438 in outer shell). I/σI: 20.84 (2.74). CC(1/2): 99.9 (83.4). A lipid molecule ([DOPC](/xray-mp-wiki/reagents/lipids/dopc/)) was observed between transmembrane domains of crystallographically related SERCA molecules, coordinated by Arg989 in M10. The A-domain electron density was weakly defined, indicating flexible positioning. Nucleotide ([AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/)) was partially disordered.
 |


## Biological / Functional Insights

### E309Q mutant binds two Ca²⁺ ions with micromolar affinity but without cooperativity

Contrary to previous studies suggesting that E309Q binds only one Ca²⁺ ion at site I, crystallographic and equilibrium 45Ca²⁺ binding measurements demonstrate that both Ca²⁺ sites are occupied at full occupancy. Ca²⁺ binds with micromolar affinity at both sites, but the cooperative binding seen in wild-type SERCA (Hill coefficient ~1.4) is lost (Hill coefficient close to 1). The affinity is only three-fold lower than wild type. The Gln309 side chain has considerably higher B-factors (~107 Å²) than other Ca²⁺-coordinating residues (~43-73 Å²), reflecting higher mobility and the fact that it can only coordinate Ca²⁺ at site II through the amide oxygen, not in a bidentate manner as wild-type glutamate.

### Catalytically incompetent conformation with defective A-domain positioning

The E309Q mutant can slowly form a stable phosphoenzyme by phosphorylation with ATP, at a very low maximal rate, in contrast to the previously held view that it is completely unable to undergo Ca²⁺-activated phosphorylation. The mutant is closer to saturation with ATP than wild type at low ATP concentrations. The N-domain position is roughly halfway between that seen in wild-type Ca2E1 and [Ca2]E1P. The A-domain assumes a flexible position, and its core is approximately 10 Å closer to the membrane surface relative to its position in wild-type Ca2E1 structures. This defective A-domain positioning impairs the phosphorylation checkpoint.

### M1 helix shift and absence of M1 kink impair signal transmission

In wild-type [Ca2]E1-[AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/), the cytosolic part of M1 is kinked at an ~90° angle near Leu61, and the M1/M2 helix bundle shifts toward the cytosolic side. In the E309Q mutant, the M1 helix shows a slight shift relative to wild-type but lacks the characteristic kink near Leu61. This transition of M1 into an up and kinked position is required for correct A-domain positioning and phosphorylation competence. The impaired M1 transition is most likely due to lack of charge neutralization and altered hydrogen bonding at Ca²⁺ site II following the E309Q mutation.

### Glu309 is a critical mediator of long-distance signal transmission

The E309Q mutation disrupts the coupled activity between Ca²⁺ binding at the transmembrane sites and ATP phosphorylation at the catalytic site, despite both Ca²⁺ sites being occupied. Glu309 in M4 acts as a gating residue at the cytosolic entrance of the Ca²⁺ sites and is directly involved in proton countertransport. The mutation causes defective Ca²⁺ occlusion and severely retarded E2P dephosphorylation. The signaling between transport sites and catalytic domains depends critically on the range of movement of the A-domain, which is in turn determined by the hydrogen bonding pattern and charge neutralization around Glu309. The central core stretching from Ca²⁺ site I (Glu771) to the C-terminal part of the P-domain containing the long (699-721) signature motif of P-type ATPases enables cooperatively interacting Ca²⁺ ions to transmit the long-distance signal that triggers the reaction of Asp351 with ATP.


## Cross-References

- [SERCA1a (Sarcoplasmic Reticulum Ca²⁺-ATPase 1a)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) — Wild-type parent protein; structural and functional comparison
- [P-type ATPase Family](/xray-mp-wiki/concepts/protein-families/p-type-atpase/) — SERCA belongs to the P-type ATPase family; E309Q mutation studies illuminate P-type ATPase mechanism
- [Phosphoenzyme E2P State](/xray-mp-wiki/concepts/enzyme-mechanisms/phosphoenzyme-e2p-state/) — E309Q mutation severely retards E2P dephosphorylation
- [AMP-PNP (Adenylyl-Imidodiphosphate)](/xray-mp-wiki/reagents/ligands/amp-pnp/) — ATP analog used during crystallization and functional assays
- [Calcium Chloride](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Essential substrate; two Ca2+ ions bound in transmembrane domain
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Cofactor; Mg2+ required for ATP hydrolysis and crystallization
- [Phosphatidylcholine](/xray-mp-wiki/reagents/lipids/phosphatidylcholine/) — DOPC lipid used in crystallization, coordinated by Arg989 in M10
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — Transport mechanism shared by P-type ATPases
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
