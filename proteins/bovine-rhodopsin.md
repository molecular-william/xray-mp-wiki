---
title: Bovine Rhodopsin (Trigonal Crystal Form)
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##J.JMB.2004.08.090, doi/10.1016##J.JMB.2007.03.007]
category: proteins
---
layout: default

# Bovine Rhodopsin — Trigonal Crystal Form (P3₁)

## Overview

Bovine rhodopsin is the light-sensitive GPCR in retinal rod cells that initiates vision. This structure represents the **dark state** (11-cis-retinal-bound) in a trigonal crystal form (space group P3₁), refined to 2.65 Å resolution. The structure was determined from **native bovine rod outer segment disk membranes** — no heterologous expression was used.

## Structure Determination

- **Resolution**: 2.65 Å (Native-3 dataset)
- **Space group**: P3₁
- **Unit cell**: a = 103.8 Å, c = 76.6 Å
- **Method**: Molecular replacement from 1F88 (tetragonal P4₁ form, 2.8 Å)
- **Refinement**: R-factor 0.202, R-free 0.235
- **Model**: Residues 1–326 (of 348 total), including N-acetylation of Met1, N-glycosylation of Asn2/Asn15, palmitoylation of Cys322/323, and 11-cis-retinal Schiff base to Lys296
- **Data source**: ESRF ID13 (Synchrotron, Grenoble)
- **Cryo-EM context**: Docked into cryo-EM map of 2D rhodopsin crystals to place in membrane context

## Chromophore and Binding Pocket

- **Chromophore**: 11-cis-retinal, covalently bound to Lys296 (helix 7) via protonated Schiff base
- **Counterion**: Glu113 (helix 3) — forms a complex with a water molecule (Wat16) H-bonded between its main-chain and side-chain oxygen atoms, stabilizing the salt-bridge
- **Key pocket residues**: Trp265 (H6), Phe261, Ala269 (ionone ring contacts), Tyr268 (3.6 Å from 11,12-cis bond)
- **H-bond network**: Trp265 → Wat10 → Asn302 (NPxxY motif in H7), extending from chromophore pocket to cytoplasmic boundary

## Helix Kinks and Packing

All seven transmembrane helices contain kinks (8°–36°) that enable intimate packing and enfold the chromophore:

| Helix | Kink position | Kink angle | Cause |
|-------|--------------|------------|-------|
| H1 | Pro53 | 9° | Proline |
| H2 | Gly89-Gly90 | 33° | Consecutive glycines |
| H3 | Glu113 | 12°/8° | Counterion + chromophore |
| H4 | Pro170-171 | 35° | Proline |
| H5 | Pro215 | 13° | Proline |
| H6 | Pro267 | 35° | Proline (most pronounced kink) |
| H7 | Pro302 | 27° | Proline |

**Functional significance**: Pro267-Tyr268 in H6 provides a pivot for the outward tilt of the cytoplasmic segment during photoactivation (analogous to Tyr185-Pro186 in bacteriorhodopsin).

## Detergent and Lipid Binding

### C8E4 (n-octyltetraoxyethylene)

- **Role**: Primary solubilization detergent for rhodopsin from disk membranes
- **Binding**: Several partially ordered C8E4 molecules bound to each rhodopsin
- **Most complete model**: Octyl chain + 3 ordered oxyethylene groups (of 4 total) intercalated in a tapered crevice between helix bundles along the 3₁-screw axis
- **Interaction**: Hydrophobic-to-hydrophobic and hydrophilic-to-hydrophilic contacts with protein; fills crevice together with palmitoylate chains

### LDAO (Lauryldimethylamine N-Oxide)

- **Concentration**: 0.05% added to C8E4-solubilised rhodopsin — **key to obtaining isotropically diffracting crystals**
- **Binding site**: Bound just to the extracellular side of the H6 kink (Pro267-Tyr268)
- **Conformation**: Kinked at C5 atom; amine oxide arm points along H6 toward extracellular face; hydrocarbon chain wraps around the kink
- **Structural role**: Stabilizes the structure around the potential hinge in H6

### Structural Phospholipids

- One phospholipid with two acyl chains bound to H6 and H7 in the cytoplasmic half of rhodopsin
- Acyl chains inclined relative to membrane normal

## Cytoplasmic Domain

- **H5 and H6 extension**: Cytoplasmic ends extended by one turn beyond the tetragonal form (H5 to residue 230, H6 to residue 276 vs. 226 and 244)
- **C3 loop**: Helix-like spiral path from residue 230 to 236, then parallel to membrane joining H6 at residue 241
- **G-protein interaction sites**: Mapped to cytoplasmic ends of H5 and H6, elevated above the bilayer
- **C1 loop**: Contacts C-terminal tail (residues 334–348 disordered except for di-peptide)
- **Flexibility**: Cytoplasmic loops have highest temperature factors — indicative of flexibility when not interacting with G protein

## Extracellular Domain

- **Pro23**: Most conserved residue in vertebrate opsins (99%); buried turn contacting β2, E1, and E2 loops; Pro23His mutation causes retinitis pigmentosa via misfolding
- **N-linked glycans**: Asn2 and Asn15 — do NOT form ordered crystal contacts in P3₁ form (unlike P4₁)
- **β-hairpin**: β1-β2 hairpin at extracellular surface; invertebrate opsins can accommodate a 13-residue insertion

## Water Molecules

- 20 ordered water molecules per protein chain
- Eight newly identified in this refinement, including Wat10 (Trp265 to NPxxY network) and Wat1 (bridging H6/H7 kinks)
- No cavities remain in the protein

## Comparison with Tetragonal (P4₁) Crystal Form

- RMSD of ordered core (residues 1–137, 154–223, 250–321): 0.36 Å — excellent agreement
- Major differences concentrated in C2 loop, C3 loop, and cytoplasmic ends of H5/H6
- C3 loop is completely absent in P4₁ form (disordered)
- C-terminal tail (334–348) disordered in P3₁ but ordered in P4₁
- Glycans do not form crystal contacts in P3₁

## Activation Mechanism

The structure supports a mechanism where:
1. Photoisomerisation of 11-cis-retinal to all-trans triggers conformational changes
2. Pivoting movements of kinked helices (especially H6 at Pro267-Tyr268) amplify translation of helix ends near membrane surfaces
3. Hydrophobic barrier (Leu76, Leu79, Leu128, Leu131, Met253, Met257) seals transmembrane H-bond network from cytoplasm
4. Met257 is critical — mutation to any residue except Leu causes constitutive Gt activation

## Expression and Solubilization

- **Native source**: Bovine retinal rod outer segment disk membranes (wild-type rhodopsin)
- **Solubilization**: C8E4 (n-octyltetraoxyethylene)
- **Additive**: 0.05% LDAO added to C8E4 — essential for crystal quality
- **No heterologous expression**: Protein extracted directly from native tissue

### Recombinant N2C/D282C Mutant (PDB 2J4Y)

- **Source**: COS-1 mammalian cells, transient expression — first recombinant GPCR structure
- **Expression yield**: ~0.6 mg from 50 plates (15 cm) — 10% higher than native (1%)
- **Solubilization**: C8E4 (after Sephadex G50 detergent exchange from DDM)
- **Purification**: 1D4 immunoaffinity chromatography
- **Concentration**: 10 mg/ml (Centricon 30 / Microcon 30)
- **Crystallization**: Sitting drop vapor diffusion, 1.2–1.7 M Li₂SO₄, 0.1 M Hepes pH 7.5, 0.05% LDAO
- **Data collection**: Microcrystallography (5 µm beam), ESRF ID13, needle crystals 5 × 5 × 90 µm
- **Resolution**: 3.4 Å, P3₁, R-work 0.287, R-free 0.325
- **Key mutation**: N2C/D282C — engineered disulfide between Cys2 and Cys282
  - Fixes N-terminal cap over β-sheet lid of ligand-binding pocket
  - +10°C thermal stability increase
  - Minimal global conformational impact (extracellular domain rmsd 0.599 Å vs native)
- **Triple mutant N2C/N15D/D282C** (fully deglycosylated): Expressed at 50% WT level, homogeneous on SDS-PAGE, but crystals diffracted to LOWER resolution — glycosylation removal did NOT help crystal quality

## Related GPCRs

- [opsin-gpcr](/xray-mp-wiki/proteins/opsin-gpcr/) — Opsin (retinal-free) structure; active state with OG in binding pocket
- [a2a-adenosine-receptor](/xray-mp-wiki/proteins/a2a-adenosine-receptor/) — Class A GPCR with extensive structural biology
- [5ht2b-receptor](/xray-mp-wiki/proteins/5ht2b-receptor/) — Serotonin GPCR with BRIL fusion

## Cross-References

- [lDAO](/xray-mp-wiki/reagents/detergents/lDAO/) — Detergent (0.05%) essential for crystal quality
- [og](/xray-mp-wiki/reagents/detergents/og/) — Related alkylglucoside detergent
- [xray-crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Structure determination method
- [molecular-replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phasing method used
- [vapor-diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) — Common crystallization method for GPCRs