---
title: KcsA Potassium Channel
created: 2026-06-10
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1021##bi500525s, doi/10.1073##pnas.2009624117, doi/10.1073##pnas.1901888116, doi/10.1126##science.280.5360.69, doi/10.1016##j.jmb.2020.06.012, doi/10.1016##j.str.2012.03.027, doi/10.1038##nature01580, doi/10.1038##nature04508, doi/10.1038##nature09136, doi/10.1038##nsmb.1531, doi/10.1038##nsmb.1703, doi/10.1016##j.str.2016.02.021, doi/10.1038##35102009, doi/10.1038##s41467-022-28866-9, doi/10.1038##NSMB929, doi/10.1073##pnas.0810663106, doi/10.1073##pnas.1314356110, doi/10.7554##eLife.28032, doi/10.1371##journal.pbio.0050121, doi/10.1073##pnas.1800559115, doi/10.1016##j.jmb.2021.167296, doi/10.1038##nsmb.1968, doi/10.1073##pnas.1105112108]
verified: false
---

# KcsA Potassium Channel

## Overview

KcsA is a prokaryotic potassium channel from Streptomyces lividans that serves as a model system for understanding potassium channel structure, gating, selectivity, and ion permeation. Cocrystal structures with symmetrical quaternary ammonium (QA) compounds TBA, THA, and TOA (Lenaeus et al., 2014) revealed a hydrophobic binding pocket between the inner helices and a lateral fenestration connecting the central cavity to the lipid bilayer. Long-chain QAs induce a nonconducting collapsed state of the selectivity filter, showing that QA compounds inhibit KcsA through both physical occlusion and allosteric regulation. The G77A and G77C mutant structures (PDB 6NFU, 6NFV) provided the first direct structural evidence for the 2,4-ion-bound configuration (water-K+-water-K+) within the selectivity filter, validating the alternating ion-bound configurations proposed by the canonical model of ion conduction. The channel forms a homotetramer with a central pore lined by the highly conserved TVGYG selectivity filter motif. It has been extensively studied by X-ray crystallography to understand ion conduction, selectivity, C-type inactivation, and the allosteric coupling between the activation gate and selectivity filter. Key studies have also revealed the structural basis of modal gating behavior, where Glu71 mutations stabilize distinct gating modes (high-Po, low-Po, and flicker) through changes in selectivity filter dynamics and ion occupancy.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##bi500525s | 2JKS | 2.40 | I4 | KcsA-L90C mutant with Fab, cocrystallized with TBA | [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/), K+ |
| doi/10.1021##bi500525s | 4UUJ | 2.40 | I4 | KcsA-L90C mutant with Fab, cocrystallized with THA | THA, K+ |
| doi/10.1021##bi500525s | 2W0F | 2.40 | I4 | KcsA-L90C mutant with Fab, cocrystallized with TOA | TOA, K+ |
| doi/10.1126##science.280.5360.69 |  | 3.2 | C2 | Wild-type KcsA, L90C mutant used for native data collection | K+ |
| doi/10.1016##j.jmb.2020.06.012 | 6W0A | 3.2 | I4 | Wild-type KcsA | Ba2+ (1 mM BaCl2, 5 mM KCl, open-gate, constricted filter) |
| doi/10.1016##j.jmb.2020.06.012 | 6W0B | 3.6 | I4 | Wild-type KcsA | Ba2+ (2 mM BaCl2, 5 mM KCl, open-gate, constricted filter) |
| doi/10.1016##j.jmb.2020.06.012 | 6W0C | 3.5 | I4 | Wild-type KcsA | Ba2+ (4 mM BaCl2, 5 mM KCl, open-gate, constricted filter) |
| doi/10.1016##j.jmb.2020.06.012 | 6W0D | 3.6 | I4 | Wild-type KcsA | Ba2+ (5 mM BaCl2, 5 mM KCl, open-gate, constricted filter) |
| doi/10.1016##j.jmb.2020.06.012 | 6W0E | 3.5 | I4 | Wild-type KcsA | Ba2+ (10 mM BaCl2, 5 mM KCl, open-gate, constricted filter) |
| doi/10.1016##j.str.2012.03.027 | not specified (Cd2+-bound Y82C) | 2.4 | I4 | Y82C mutant of KcsA with Fab fragments | Cd2+ (100 uM) |
| doi/10.1016##j.str.2012.03.027 | not specified (spin label-bound Y82C) | 2.5 | I4 | Y82C mutant of KcsA with nitroxide spin label and Fab | Nitroxide spin label |
| doi/10.1038##nature09136 | not specified (OM-Rb) | 3.3 | I4 | Wild-type KcsA | Rb+ (fully open state) |
| doi/10.1038##nature09136 | not specified (E71H-F103A) | 3.2 | I4 | E71H-F103A double mutant | Rb+ (closed state) |
| doi/10.1016##j.str.2016.02.021 | 5EC1 | 2.9 | I4 | KcsA V76ester mutant (S3 occupancy reduced) | K+ |
| doi/10.1016##j.str.2016.02.021 | 5EC2 | 2.5 | I4 | KcsA V76ester + G77dA double mutant | K+ |
| doi/10.1016##j.str.2016.02.021 | 5EBW | 2.3 | I4 | KcsA G77ester mutant (S2 occupancy eliminated) | K+ |
| doi/10.1016##j.str.2016.02.021 | 5EBL | not specified | I4 | KcsA T75G mutant (S4 occupancy reduced) | K+ |
| doi/10.1016##j.str.2016.02.021 | 5EBM | not specified | I4 | KcsA backbone mutant | K+ |
| doi/10.1038##35102009 | 1K4C | 2.0 | I4 | KcsA-Fab complex, wild-type, high K+ (~200 mM) | K+ |
| doi/10.1038##35102009 | 1K4D | 2.3 | I4 | KcsA-Fab complex, wild-type, low K+ (~3 mM) | K+, Na+ |
| doi/10.7554##eLife.28032 | 5VK6 | 2.25 | I4 | Locked-open KcsA E71A mutant (O/O state), chymotrypsin-truncated, Fab complex | K+ |
| doi/10.7554##eLife.28032 | 5VKE | 2.37 | I4 | Locked-open KcsA Y82A mutant (O/I state), chymotrypsin-truncated, Fab complex | K+ |
| doi/10.7554##eLife.28032 | 5VKH | 2.25 | I4 | KcsA Y82A mutant, closed state, Fab complex | K+ |
| doi/10.1038##s41467-022-28866-9 | 7MHR | 2.9 | I4 | E71V KcsA mutant, closed-gate, 5 mM K+ | K+ |
| doi/10.1038##s41467-022-28866-9 | 7MHX | 3.3 | I4 | E71V KcsA mutant, open-gate | Ba2+ |
| doi/10.1038##s41467-022-28866-9 | 7MJT | 2.7 | I4 | E71V KcsA mutant, closed-gate | Ba2+ |
| doi/10.1038##s41467-022-28866-9 | 7MK6 | 3.0 | I4 | E71V KcsA mutant, open-gate, 0 mM K+/150 mM NaCl | Na+ |
| doi/10.1038##s41467-022-28866-9 | 7MUB | 3.0 | I4 | E71V KcsA mutant | Ba2+ |
| doi/10.1038##NSMB929 | 2BOB | 2.75 | I4 | KcsA-L90C mutant with Fab | [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/), Tl+ |
| doi/10.1038##NSMB929 | 2BOC | 2.75 | I4 | KcsA-L90C mutant with Fab | TEAs, Tl+ |
| doi/10.1038##nsmb.1703 | not specified (NoK-Li+) | 2.8 | I4 | Wild-type KcsA, Fab complex, Li+ only | Li+ |
| doi/10.1038##nsmb.1703 | not specified (LowK-Li+) | 2.75 | I4 | Wild-type KcsA, Fab complex, 3 mM K+ with Li+ | K+, Li+ |
| doi/10.1073##pnas.0810663106 | not specified (FL KcsA-Fab2) | 3.8 | I222 | Full-length KcsA (residues 22-160) with Fab2 | -- |
| doi/10.1073##pnas.0810663106 | not specified (CDKcsA-Fab4) | 2.6 | I4 | C-terminal domain fragment (residues 129-158) with Fab4 | -- |
| doi/10.1073##pnas.1314356110 | not specified (Y78-ester KcsA) | 2.1 | — | KcsA Y78-ester mutant (amide-to-ester at 2' bond, between Y78 and G79), Fab complex, 300 mM KCl | K+ (reduced S2 occupancy) |
| doi/10.1073##pnas.1800559115 | 6BY2 | not specified | I4 | KcsA T75A mutant, closed state, Fab complex | K+ |
| doi/10.1073##pnas.1800559115 | 6BY3 | not specified | I4 | KcsA T75A mutant, locked-open (disulfide-bridged), open state | K+ |
| doi/10.1016##j.jmb.2021.167296 | 7M2H | 2.64 | P4 | KcsA W67F mutant, pre-open state, +TBA +Fab | K+, [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) |
| doi/10.1016##j.jmb.2021.167296 | 7M2I | 2.72 | I4 | KcsA W67F mutant, locked-open (disulfide crosslinked), pre-inactivated state | K+ (reduced occupancy at S2 site) |
| doi/10.1016##j.jmb.2021.167296 | 7M2J | 3.20 | I4 | Wild-type KcsA, locked-open (disulfide crosslinked), inactivated state | K+ |
| doi/10.1016##j.jmb.2021.167296 | 7RP0 | not specified | I4 | KcsA Y82A mutant, closed state, +TBA +Fab | K+, [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) |
| doi/10.1038##nsmb.1968 | 3OR7 | 2.30 | I4 | KcsA E71I mutant in complex with Fab fragment | K+ |
| doi/10.1038##nsmb.1968 | 3OR6 | 2.70 | I4 | KcsA E71Q mutant in complex with Fab fragment | K+ |
| doi/10.1073##pnas.1105112108 |  | 3.9 | I222 | Constitutively open FL KcsA mutant with Fab2, full-length (residues 22-160) | K+ |

## Expression and Purification

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

### Purification Workflow

*Source: doi/10.1126##science.280.5360.69*

- **Expression system**: E. coli

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt affinity column | — |  | Used for initial purification of KcsA |
| Proteolytic cleavage | Chymotrypsin proteolysis | — |  | 35 C-terminal amino acids cleaved |
| Gel filtration | Size-exclusion chromatography | — |  | Purified to homogeneity |
| Detergent exchange | Dialysis | — | 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) | Final dialysis step against 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) |

**Final sample**: KcsA in 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), 150 mM KCl, 50 mM Tris pH 7.5
**Purity**: Homogeneous by SDS-PAGE

### Purification Workflow

*Source: doi/10.1016##j.jmb.2020.06.012*

- **Expression system**: E. coli XL-1 Blue
- **Expression construct**: Wild-type KcsA from pQE32 vector
- **Tag info**: Untagged

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Avestin Emulsiflex C5 homogenizer | — | 20 mM Tris pH 8.0, 0.2 M NaCl, 1 mM PMSF, 20 ug/ml DNase I | 2L culture |
| Membrane collection | Centrifugation | — |  | 100,000g at 4 C for 1 h |
| Solubilization | Detergent solubilization | — | 20 mM Tris pH 7.5, 0.15 M KCl + 40 mM [n-Decyl-β-D-maltoside](/xray-mp-wiki/reagents/detergents/dm/) (DM) | Overnight incubation at 4 C |

### Purification Workflow

*Source: doi/10.1038##35102009*

- **Expression system**: E. coli

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| KcsA purification | Affinity + size exclusion | — | 50 mM Tris pH 7.5, 150 mM KCl + 5 mM DM | KcsA purified as described. 35 C-terminal amino acids cleaved by chymotrypsin. |
| Fab purification | Protein A affinity + ion exchange | — |  | Mouse IgG from hybridoma culture. Fab by papain proteolysis + Q-Sepharose. |
| KcsA-Fab complex formation | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 50 mM Tris pH 7.5, 150 mM KCl + 5 mM DM |  |

### Purification Workflow

*Source: doi/10.1073##pnas.0810663106*

- **Expression construct**: Full-length KcsA (residues 22-160)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Fab selection | Phage display | — |  | Biotinylated FL KcsA on streptavidin beads. 3 rounds selection. |
| KcsA-Fab complex formation | Complex formation | — | 5 mM dodecyl maltopyranoside |  |

### Purification Workflow

*Source: doi/10.1073##pnas.1314356110*

- **Expression system**: E. coli / in vitro
- **Expression construct**: KcsA residues 1-123, semisynthetic with ester substitutions at selectivity filter
- **Tag info**: Synthetic peptide with N-terminal Cys, recombinant thioester peptide (residues 1-69)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein semisynthesis | Native chemical ligation | — |  | Recombinant thioester peptide (residues 1-69) ligated to synthetic peptide (residues 70-123) containing ester linkage |
| Folding | Lipid vesicle folding | — |  | Ligation product folded to native tetrameric state using lipid vesicles |
| Purification | Lipid vesicle reconstitution | — |  | Semisynthetic KcsA ester mutants purified and reconstituted into lipid vesicles for recording |
| In vivo nonsense suppression (alternative) | Amber suppression | — |  | Used orthogonal tRNA/tRNA synthetase pair (Schultz group) to incorporate HPLA at amber stop codon, for full-length KcsA Y78-ester mutant |

### Purification Workflow

*Source: doi/10.7554##eLife.28032*

- **Expression system**: E. coli XL10-gold
- **Expression construct**: Locked-open KcsA (KcsA-OM, double-cysteine 28-118) with E71A or Y82A mutations, pQE70 vector
- **Tag info**: C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/), chymotrypsin-cleaved for crystallization

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Overnight culture at 37 C with 2% [Glucose](/xray-mp-wiki/reagents/additives/glucose/) and 0.4 mg/ml [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) | — |  | Diluted 100x next day |
| Cell lysis | Emulsiflex C3 homogenizer | — | 50 mM Tris pH 8.0, 150 mM KCl, 1 mM PMSF (Buffer A) | Passed 3 times. Membranes collected at 100,000g for 1 hr. |
| Solubilization | Detergent solubilization | — | Buffer A + 20 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | 2 hr incubation, insoluble spun down at 100,000g |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt affinity resin | — | Buffer A, 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Washed with 10 CV buffer A + 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/). Eluted with buffer A + 400 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/). |
| Fab complex formation and detergent exchange | Chymotrypsin cleavage + Fab complex | — | 5 mM DM | Chymotrypsin-cut KcsA complexed with Fab antibody fragment. Exchanged into 5 mM DM for crystallization. |

**Final sample**: KcsA-Fab complex in 5 mM DM

### Purification Workflow

*Source: doi/10.1371##journal.pbio.0050121*

- **Expression system**: E. coli
- **Expression construct**: KcsA A98G mutant (referred to as wild-type), residues 1-123
- **Tag info**: Untagged, chymotrypsin-cleaved

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression and lysis | Standard KcsA expression and purification | — |  | Expressed and purified as described in Zhou Y, MacKinnon R (2003) |
| Proteolytic cleavage | Chymotrypsin proteolysis | — |  | C-terminal residues cleaved to produce truncated KcsA tetramer |
| Size-exclusion chromatography | Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 50 mM Tris pH 7.5, 20 mM KCl, 100 mM NaCl + 5 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) (DM) | Purified tetramer concentrated to 10 mg/ml |
| Buffer exchange | Dialysis | — | 5 mM DM | Extensively dialyzed against desired [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) buffer (25 mM HEPES pH 7.5, 100 mM NaCl or LiCl, 5 mM DM) |

**Final sample**: KcsA at 71-142 uM in 25 mM HEPES pH 7.5, 100 mM NaCl (or LiCl), 5 mM DM
**Purity**: Homogeneous

### Purification Workflow

*Source: doi/10.1038##nsmb.1968*

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: KcsA Glu71 mutants (E71I, E71Q) cloned in pQE32 vector
- **Tag info**: Co2+-based metal-chelate chromatography (Talon resin)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and membrane preparation | Homogenization and centrifugation | — | PBS buffer | Cells homogenized, membranes pelleted at 100,000g for 1 h |
| Solubilization | Detergent solubilization | — | PBS buffer + Dodecylmaltoside | Membrane pellets solubilized with PBS buffer containing dodecylmaltoside at room temperature |
| Affinity purification | Co2+-based metal-chelate chromatography | Talon resin (Clontech) | PBS with dodecylmaltoside | Purified via metal-chelate chromatography |
| Quality check | Gel-exclusion chromatography | Superdex-200 column (GE Healthcare) |  | Quality of purified protein checked by gel-exclusion chromatography |


## Crystallization

### doi/10.1126##science.280.5360.69

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | KcsA at 5-10 mg/ml in 150 mM KCl, 50 mM Tris pH 7.5, 2 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) |
| Reservoir | 200 mM CaCl2, 100 mM Hepes pH 7.5, 48% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 |
| Temperature | 20 C |
| Notes | Crystals space group C2, a=128.8Å, b=68.9Å, c=112.0Å, beta=124.6°. For ion sites, crystals transferred to solutions where 150 mM KCl replaced by 150 mM RbCl or 150 mM CsCl. |

### doi/10.1016##j.jmb.2020.06.012

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (soak) |
| Protein sample | Solubilized wt KcsA in DM |
| Notes | Wild-type KcsA crystallized in open-gate and closed-gate conformations under identical conditions. Open-gate obtained by soaking pre-grown crystals in BaCl2 solutions. |

### doi/10.1038##NSMB929

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Fab-KcsA-L90C complex at ~10 mg/ml in 150 mM TlNO3, 50 mM HEPES pH 7.5, 5 mM DM, with 5 mM [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) nitrate or 50 mM TEAs nitrate |
| Reservoir | 20-25% (v/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 50 mM magnesium acetate, 50 mM [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/), pH 5-5.6 |
| Temperature | Room temperature |
| Cryoprotection | Incrementally increasing precipitant, flash-cooled in liquid nitrogen |

### doi/10.1016##j.str.2012.03.027

| Parameter | Value |
|---|---|
| Method | Co-crystallization / Cd2+ soaking with Fab |
| Protein sample | Y82C-KcsA mutant in detergent |

### doi/10.1038##35102009

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | KcsA-Fab complex at 7-15 mg/mL in 5 mM DM |
| Reservoir | 20-25% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 50 mM magnesium acetate, 50 mM [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/), pH 5.0-5.6 |
| Temperature | 20 C |
| Cryoprotection | [PEG](/xray-mp-wiki/reagents/additives/peg/) concentration increased to 40% in 2.5% increments |

### doi/10.1038##s41467-022-28866-9

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (soak) |
| Protein sample | E71V KcsA mutant in DM |

### doi/10.1073##pnas.0810663106

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | FL KcsA-Fab2 complex (7 mg/ml) or FL KcsA-Fab4 complex |
| Reservoir | 340 mM (NH4)2SO4, 11% [PEG](/xray-mp-wiki/reagents/additives/peg/) 4000, 100 mM sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 5.6 |
| Temperature | 20 C |

### doi/10.1073##pnas.1314356110

| Parameter | Value |
|---|---|
| Method | Fab complex crystallization |
| Protein sample | Y78-ester KcsA-Fab complex in 300 mM KCl |
| Temperature | Not specified |
| Notes | Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) and refined to 2.1 A resolution. Electron density omit map confirmed transplanar Y78-ester linkage. |

### doi/10.7554##eLife.28032

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Locked-open KcsA-Fab complex (E71A or Y82A mutant) in 5 mM DM |
| Reservoir | 24-27% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) (v/v), 50 mM magnesium acetate, 50 mM [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) pH 5.4-6.0 |
| Temperature | 20 C |
| Notes | E71A mutant diffracted to 2.25 A (PDB 5VK6), Y82A mutant to 2.37 A (PDB 5VKE), and Y82A-F103A closed mutant to 2.25 A (PDB 5VKH). |

### doi/10.1073##pnas.1901888116

| Parameter | Value |
|---|---|

| Parameter | Value |
|---|---|

### doi/10.1038##nsmb.1968

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | KcsA E71I or E71Q mutant in complex with Fab fragment |
| Reservoir | Not specified in paper |
| Temperature | Not specified |
| Notes | Crystals of E71I (2.3 A) and E71Q (2.7 A) obtained as Fab complexes. Structures solved by molecular replacement using WT KcsA (1K4C) as search model. Selectivity filter built with side chain density corresponding to Val76, Tyr78 and Asp80 as markers. |

### doi/10.1073##pnas.1105112108

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | FL KcsA-Fab2 complex from constitutively open mutant |
| Reservoir | 0.2 M Na/K phosphate, 0.1 M [Bis-Tris Propane](/xray-mp-wiki/reagents/buffers/bis-tris-propane/) pH 7.5, 10% PEG3350 |
| Temperature | Not specified |
| Cryoprotection | Series of modified well solutions with increasing glycerol |
| Notes | Isomorphous with closed FL KcsA-Fab2 (3EFF) crystals. Data collected at APS beamline 23ID, processed by HKL2000. Structure solved by molecular replacement using Fab2 and closed FL KcsA as search models. Refined with CNS. |


## Biological / Functional Insights

### Hydrophobic binding pocket for quaternary ammonium compounds

Cocrystal structures of KcsA with TBA, THA, and TOA (PDB 2JKS, 4UUJ, 2W0F) reveal a hydrophobic binding pocket between the inner helices of KcsA. The pocket provides insight into the binding site and blocking mechanism of hydrophobic QAs. Access to the pocket is controlled by the rotameric state of residue F103, which is altered by binding of long-chain blockers. The octyl chain of TOA interacts with outer helix residue L36, demonstrating that drug binding is not confined to the inner helix but involves outer helix residues when the ligand penetrates deeply.

### Lateral fenestration connecting central cavity to lipid bilayer

Structures of KcsA with THA and TOA reveal a structurally hidden pathway between the central cavity and the outside membrane environment, reminiscent of lateral fenestrations observed in bacterial sodium channels. Access to this fenestration is controlled by small conformational changes in the pore wall, specifically the rotameric state of F103.

### Long-chain QAs induce selectivity filter collapse and nonconducting state

TBA binding does not alter the conductive state of the selectivity filter in the presence of 150 mM K+. In contrast, TOA (and THA) induce a collapsed, nonconducting conformation characterized by only two K+ ions bound, an altered hydrogen bond network, and binding of three water molecules. The octyl chain of TOA pushes the pore helix upward, forcing the selectivity filter into a nonconducting state. This demonstrates that long-chain QAs inhibit KcsA through two mechanisms: physical occlusion and allosteric regulation via promotion of slow inactivation.

### Increasing QA binding affinity with alkyl-chain length

Functional stopped-flow fluorescence assays with ANTS-loaded vesicles show incremental increase in QA binding affinity with increasing alkyl-chain length. TBA has an inhibition constant of ~120 uM. The number of van der Waals interactions increases incrementally from TBA to THA to TOA, consistent with the observed increase in affinity. The hexyl chain of THA interacts with T74, G99, I100, and F103; the octyl chain of TOA adds interactions with L36, S102, and additional main-chain contacts.

### Stabilization of the 2,4-ion-bound configuration by G77A and G77C mutants

Tilegenova et al. (2019) solved the crystal structures of KcsA G77A (PDB 6NFU, 2.09 A) and G77C (PDB 6NFV, 2.13 A) mutants that stabilize the 2,4-ion-bound configuration (water-K+-water-K+) of the selectivity filter. In these structures, K+ ions are bound only at the S2 and S4 sites, with water molecules at S1 and S3. This directly contradicts the direct knock-on model (which predicts 3 K+ ions bound in these mutants) and provides strong structural evidence for the canonical model of alternating 1,3- and 2,4-ion-bound configurations. The G77A mutant showed wild-type-like ion selectivity and apparent K+-binding affinity (Kd = 0.29 mM by [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/)), but lacked C-type inactivation and had markedly reduced single-channel conductance (~1.95 pS vs ~63 pS for WT).

### Inverted teepee architecture of the K+ channel pore

The KcsA structure revealed that four identical subunits create an inverted teepee, or cone, cradling the selectivity filter at its outer end. The inner helices are tilted ~25 degrees from the membrane normal and packed as a bundle near the intracellular side. This architecture likely generalizes to cyclic nucleotide-gated channels, Na+ and Ca2+ channels.

### Selectivity filter mechanism: carbonyl oxygen coordination and structural rigidity

The selectivity filter is lined exclusively by main chain carbonyl oxygen atoms from the K+ channel signature sequence (TVGYG). The filter is held open by structural constraints (aromatic cuff of Tyr and Trp residues acting like molecular springs) so that dehydrated K+ ions fit precisely but smaller Na+ ions cannot be properly coordinated. This explains the 10,000-fold selectivity for K+ over Na+.

### Water-filled cavity and helix dipoles overcome electrostatic barrier

A large 10-A diameter water-filled cavity at the membrane center surrounds a hydrated cation, overcoming the electrostatic destabilization of the low-dielectric bilayer. Four pore helices point at the cavity center with their C-termini, providing a cation-attractive helix dipole potential that further stabilizes the ion.

### Multi-ion conduction and electrostatic repulsion

The selectivity filter contains two K+ ions about 7.5 A apart. Electrostatic repulsion between the two ions overcomes the attractive force between each K+ and the carbonyl oxygens, allowing rapid conduction (up to 10^8 ions/s) despite high selectivity. This resolves the apparent paradox of how a highly selective filter can conduct at near-diffusion-limited rates.

### K+ hydration in the central cavity

The 2.0 A resolution KcsA-Fab structure revealed a fully hydrated K+ ion at the centre of the central cavity, coordinated by eight discrete water molecules in square antiprism geometry.

### Two selectivity filter structures under high and low K+

Low-K+ structure (1K4D, 3 mM K+) shows pinched non-conductive filter. High-K+ structure (1K4C, 200 mM K+) shows conductive conformation. This provides physical mechanism for filter response to channel gating.

### Individual ion binding sites play distinct roles in C-type inactivation

Amide-to-ester backbone mutagenesis reveals specific roles: V76ester (S3) slows recovery ~30-fold; G77ester and Y78ester (S2) impair inactivation; T75G (S4) slows recovery; G79ester (S1) has no effect on inactivation or recovery.

### S2 site occupancy is linked to C-type inactivation

Using amide-to-ester substitutions in the KcsA selectivity filter, the Y78-ester mutation (2' amide bond) eliminates K+ binding at the S2 site and dramatically reduces C-type inactivation. The G79-ester (1' amide bond) does not affect inactivation despite reduced S1 occupancy. The G77-ester (3' amide bond) also reduces inactivation. These results link C-type inactivation to ion occupancy specifically at the S2 site. A [KVAP](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) Y199-ester mutant (equivalent to Y78 in KcsA) also shows slowed inactivation, demonstrating conservation of the S2-dependent mechanism.

### Open-gate conformation of wild-type KcsA

Wild-type KcsA crystallized in both open-gate and closed-gate conformations. Open-gate has C-alpha distance at Thr112 of ~23 A vs closed-gate ~12 A.

### Cd2+-induced C-type inactivation and metal bridge formation

External Cd2+ enhances C-type inactivation rate in Y82C-KcsA via metal-bridge formation between adjacent subunits.

### Conformational coupling between activation gate and selectivity filter

The gating cycle of K+ channels is defined by four kinetic states. Opening of the activation gate stabilizes the non-conductive filter conformation; filter inactivation stabilizes the closed activation gate.

### TEA blockade mechanism via potassium analog mechanism

Co-crystal structures with [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) (2BOB) and TEAs (2BOC) reveal [TEA](/xray-mp-wiki/reagents/ligands/tetraethylammonium/) blocks by acting as a potassium analog at the dehydration transition step.

### Full-length KcsA C-terminal 4-helix bundle structure

Full-length KcsA (3.8 A) reveals a well-defined 4-helix bundle projecting ~70 A toward cytoplasm, formed by residues 136-160.

### Ion selectivity by size recognition rather than charge density

Using isothermal titration calorimetry ([ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/)) and X-ray crystallography, Lockless et al. (2007) showed that KcsA selectivity depends on ion size (volume) rather than charge density. K+ (1.33 A) and Rb+ (1.48 A) bind and stabilize the conductive filter conformation, while Na+ (0.95 A) cannot. Ba2+ (1.35 A) binds like K+ despite double charge, while smaller Mg2+ (0.65 A) and Ca2+ (0.99 A) do not bind. This demonstrates the channel recognizes ionic radius, not electrostatic field strength, consistent with the "snug fit" hypothesis.

### Atomic-resolution gating cycle of KcsA

The gating cycle comprises four states: C/O (closed-conductive), O/O (open-conductive), O/I (open-inactivated), and C/I (closed-inactivated). The Locked-open E71A mutant (PDB 5VK6, 2.25 A) captures the transient O/O state with a fully conductive selectivity filter containing 4 K+ ions in canonical 1,3 and 2,4 configurations and a 22 A activation gate opening. The Locked-open Y82A mutant (PDB 5VKE, 2.37 A) captures the O/I state with collapsed filter at Gly77 (6 A Cα-Cα vs 8 A in conductive), Val76 carbonyl flipped out, and 2 K+ ions at positions 1 and 4 only.

### Inactivating water network stabilizes collapsed filter

Three 'inactivating water molecules' were resolved behind the selectivity filter in the O/I state, hydrogen-bonded to Val76 carbonyl, Glu71 carbonyl, Gly77 amide nitrogen, and Asp80 side chains. These waters stabilize the collapsed filter conformation. Diffusion of water into the 'inactivation cavity' guarded by Tyr82 (Thr449 in Shaker) determines the rate and magnitude of C-type inactivation.

### Allosteric coupling between activation gate and selectivity filter

Phe103 clashes with Ile100 and Thr74/75 of the signature sequence upon gate opening, deforming the pore helix and triggering compensatory structural changes at the selectivity filter. This coupling underlies the mechanistically-linked activation and C-type inactivation gating processes.

### T75A mutation inverts allosteric coupling between activation gate and selectivity filter

Substitution of the second Threonine (Thr75 in KcsA, Thr480 in hKv1.5, Thr442 in Shaker) within the TTVGYGD signature sequence with Alanine inverts the allosteric coupling between the activation gate and selectivity filter. In these T-to-A mutants, the selectivity filter is inactive (C-type inactivated) in the closed state and becomes conductive and noninactivating upon activation gate opening. Crystal structures of KcsA T75A closed (PDB 6BY2) show a deep C-type inactivated conformation with filter constriction at Gly77 and only two K+ ions bound, while the open T75A structure (PDB 6BY3) shows a fully conductive filter with three K+ ions bound, essentially identical to the noninactivating E71A mutant (PDB 5VK6). This demonstrates that closed-state inactivation can occur via structural collapse of the selectivity filter.

### W67F mutation reveals pre-open and pre-inactivated gating intermediates

The KcsA W67F mutant (Trp67Phe in the pore helix) shows severely reduced C-type inactivation and enhanced activation rate. The 2.64 A structure (PDB 7M2H) captures a "pre-open" state — an intermediate along the activation gate opening trajectory where the F103 side chain has flipped but the inner helices are only partially displaced. The 2.72 A locked-open structure (PDB 7M2I) captures a "pre-inactivated" state where the E71 side chain has switched to the rotamer associated with filter constriction, but the selectivity filter remains conductive because S2 site ion occupancy is lost. CW-EPR spectroscopy shows altered pH dependence of activation (pKa 4.51 vs 4.18 for WT). These findings identify F103, E71, and the S2 site as three key nodes in the allosteric pathway coupling the activation gate to the selectivity filter.

### Glu71 mutations stabilize three distinct gating modes in KcsA

Chakrapani et al. (2011) showed that mutations at the pore-helix position Glu71 unmask a series of kinetically distinct gating modes in KcsA in a side chain-specific way. E71A stabilizes high-Po (open probability) mode with long opening bursts and few short intraburst closures. E71I stabilizes a low-Po mode with similar mean open and closed times. E71Q stabilizes a high-frequency flicker mode with very short open and closed sojourns. These three gating modes mirror those seen in wild-type KcsA and are defined by three nonconductive states: slow inactive (Is, tau ~100 ms), intermediate inactive (Ii, tau 1-10 ms), and flicker (F, tau 0.1-0.5 ms). The results demonstrate that specific interactions in the side chain network surrounding the selectivity filter, in concert with ion occupancy, alter the relative stability of pre-existing conformational states of the pore.

### Crystal structures of E71I and E71Q reveal subtle changes in ion occupancy

Crystal structures of KcsA E71I (PDB 3OR7, 2.3 A) and E71Q (PDB 3OR6, 2.7 A) show no major backbone conformational changes in the selectivity filter, which adopts a conductive conformation similar to closed KcsA structures. However, one-dimensional electron density profiles along the central symmetry axis reveal subtle differences in ion occupancy at binding sites S1-S4. The E71Q mutant shows altered ion distribution compared to WT, with changes in the relative peak heights at the K+ binding sites. These occupancy differences correlate with the distinct gating kinetics observed electrophysiologically.

### Val76 carbonyl reorientation associated with flicker gating in E71Q

Molecular dynamics simulations of KcsA mutants revealed that only the flicker-prone E71Q mutant shows a considerable increase in the frequency and lifetime of Val76 carbonyl reorientation compared to WT, E71A, and E71I. The dwell-time ratio between the flicker and open states in E71Q (~40:60) mirrors the ratio of outward-facing to straight conformations of the Val76 carbonyl. This suggests that reorientation of the Val76 carbonyl is associated with the conformational changes leading to short-lived flicker states in single-channel recordings.

### Asp80 side chain flipping in gating mode mutants

Molecular dynamics simulations show that the Cα-Cα distance between Glu71 and Asp80 has a very narrow distribution in WT KcsA, indicative of a strong interaction. In contrast, E71Q and E71I show a broader distribution with a distinct second population corresponding to channels with flipped Asp80 side chain. This dual-population behavior is observed in all gating mode mutants at position 71, suggesting that overall mobility of the Asp80 side chain is enhanced when interaction with Glu71 is lost.

### Open conformation of full-length KcsA solved at 3.9 A

Using a constitutively open mutant and chaperone-assisted crystallography with Fab2 antibody fragments, the structure of full-length KcsA in the open conformation was determined at 3.9 A resolution in space group I222. The crystals were highly isomorphous with the closed FL KcsA-Fab2 form (3EFF), allowing direct comparison via Fourier difference maps in the same unit cell. The structure reveals that the activation gate expands approximately 20 A and generates side windows large enough to accommodate hydrated K+ ions.

### Activation gate expansion strains C-terminal bulge helices

Movement of the inner gate helix (TM2) is transmitted to the C-terminus as a straightforward expansion, leading to an upward movement and insertion of the top third of the bulge helix (residues 118-135) into the membrane. The four-helix bundle of the C-terminal domain (residues 136-160) preserves its fourfold symmetry during opening, while the bulge helix region undergoes a twofold-symmetric expansion.

### C-terminal domain modulates C-type inactivation kinetics

Patch clamp experiments on reconstituted KcsA with varying C-terminal domain stability revealed that the C-terminal domain modulates the rate and extent of C-type inactivation. In the absence of the C-terminal domain (truncated KcsA), the channel inactivates rapidly and fully. The presence of the C-terminus slows inactivation and increases steady-state current three- to fourfold. Additional strain from Fab4 binding further slows inactivation, reaching ~40% steady-state current. This demonstrates that the steric limits imposed by the C-terminal bundle determine the degree of gate opening, which in turn controls C-type inactivation at the selectivity filter.

### EPR spectroscopy confirms partial bundle expansion during gating

Site-directed spin labeling and EPR spectroscopy of the C-terminal domain showed that the extent of spectral broadening due to dipolar coupling decreases throughout the C-terminal domain during opening, but does not disappear. This confirms that the bundle expands partially but remains as a unit. There is no significant rotation in either the bulge helix or the lower bundle associated with the opening conformation, suggesting that the inner gate helix motion is directly transmitted to the C-terminus as a simple radial expansion without rotation.

### Physiological gate opening likely intermediate between truncated and Fab-bound states

The fact that steady-state inactivation of full-length KcsA displays an intermediate value between truncated KcsA (rapid inactivation) and Fab-bound KcsA (slow inactivation) suggests that under physiological conditions, the inner bundle gate in WT KcsA opens at an intermediate level between 21 and 32 A. This generates side windows that easily accommodate hydrated ions and small blockers like 4-aminopyridine and quaternary ammonium ions.


## Cross-References

- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Crystallization detergent (5 mM) for KcsA-Fab complex
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Solubilization detergent (20 mM) for KcsA extraction from membranes
- [Barium Chloride](/xray-mp-wiki/reagents/additives/barium-chloride/) — Ba2+ blocker used in soak experiments (0-10 mM)
- [Cadmium Chloride](/xray-mp-wiki/reagents/additives/cadmium-chloride/) — Cd2+ ions form metal bridges in Y82C-KcsA
- [C-type Inactivation](/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/) — KcsA is the primary model system for studying C-type inactivation
- [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) — Selectivity filter structure essentially identical; glycine-gating hinge mechanism shared
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — Conformational coupling between activation gate and selectivity filter
- [NaK Channel from Bacillus cereus](/xray-mp-wiki/proteins/voltage-gated-channels/nak-channel/) — Closed NaK superimposes with KcsA (r.m.s.d. 0.73 A)
- [MthK Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) — Open NaK superimposes with open MthK; glycine-gating hinge comparison
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Modal Gating in K+ Channels](/xray-mp-wiki/concepts/transport-mechanisms/modal-gating-in-k-channels/) — KcsA Glu71 mutant structures (3OR7, 3OR6) reveal structural basis of modal gating
