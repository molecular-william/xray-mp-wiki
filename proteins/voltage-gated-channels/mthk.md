---
title: MthK (Methanobacterium thermoautotrophicum K+ Channel)
created: 2026-06-08
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [ion-channel, potassium-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.2009624117, doi/10.1038##417515a, doi/10.1038##nsmb.1865, doi/10.1038##ncomms3621, doi/10.1038##nsmb.2473, doi/10.1038##s41467-019-13227-w]
verified: false
---

# MthK (Methanobacterium thermoautotrophicum K+ Channel)

## Overview

MthK is a calcium-gated potassium channel from the archaeon Methanobacterium thermoautotrophicum. It belongs to the family of tetrameric cation channels and is a founding member of RCK (Regulator of Conductance for K+) domain-containing channels. The channel features a central pore formed by four membrane-spanning subunits and an intracellular gating ring composed of eight RCK domains that regulate channel opening in response to intracellular Ca2+ binding. MthK served as a prototype for understanding the mechanism of ligand-gated channel opening through the gating ring architecture. High-resolution structures of the isolated MthK pore at up to 1.45 A resolution revealed that the selectivity filter maintains a conductive conformation even in the absence of K+, and provided atomic-level insights into K+ selectivity and the anomalous mole-fraction effect in multi-ion pores. A comprehensive structural titration (X-ray crystallography at 150, 50, 11, and 6 mM K+) combined with molecular dynamics simulations revealed that the central S2 binding site has uniquely low K+ affinity (~50 mM) while S1, S3, and S4 have high affinity (sub-mM), leading to selective emptying of S2 at low K+ without SF collapse — explaining why MthK and [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) have different inactivation phenotypes despite identical selectivity filter sequences. Structural and functional analysis of the MthK RCK domain revealed allosteric coupling between two Ca2+-binding sites (C1 and C3) mediated by a carboxyl-carboxylate hydrogen bond between Glu259 and Glu133, providing a mechanism for tuning Ca2+ sensitivity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##417515a |  | 3.3 | P6_6 22 | MthK M107I mutant, residues 19-336 | Ca2+ |
| doi/10.1038##nsmb.1865 |  | 1.45 | P42_12 | MthK pore, S68H V77C mutant (K+ complex, 100 mM KCl) | K+ |
| doi/10.1038##nsmb.1865 |  | 1.45 | P42_12 | MthK pore, S68R V77C mutant (low-K+ complex, 1 mM KCl/99 mM NaCl) | K+/Na+ |
| doi/10.1038##nsmb.1865 |  | 2.2 | P42_12 | MthK pore, S68H V77C mutant (Na+ complex, 100 mM NaCl) | Na+ |
| doi/10.1038##ncomms3621 |  | 2.5 | P3_121 | WT MthK RCK domain, fully Ca2+-bound (C1, C2, C3 sites occupied) | Ca2+ (3 ions per RCK domain) |
| doi/10.1038##ncomms3621 |  | 1.85 | P2_111 | WT MthK RCK domain, Ca2+ bound only at C1 site (200 mM CaCl2) | Ca2+ (1 ion per RCK domain, at C1 site) |
| doi/10.1038##ncomms3621 |  | 2.4 | P6_522 | D184N mutant MthK RCK domain, no Ca2+ at C1, Ca2+ bound at C3 | Ca2+ (C3 site only) |
| doi/10.1038##ncomms3621 |  | 3.0 | P6_522 | E212Q mutant MthK RCK domain, Ca2+ bound at both C1 and C3 | Ca2+ (C1 and C3 sites, altered coordination at C1) |
| doi/10.1038##s41467-019-13227-w | 6OLY |  |  | Full-length MthK M107I mutant with thrombin-cleavable C-terminal 6×His-tag | Ca2+ |
| doi/10.1073##pnas.2009624117 | 6U9P | <2 |  | Wild-type MthK pore, 150 mM K+ | K+ |
| doi/10.1073##pnas.2009624117 | 6U9T | <2 |  | Wild-type MthK pore, 50 mM K+ | K+ |
| doi/10.1073##pnas.2009624117 | 6U9Y | <2 |  | Wild-type MthK pore, 11 mM K+ | K+ |
| doi/10.1073##pnas.2009624117 | 6U9Z | <2 |  | Wild-type MthK pore, 6 mM K+ | K+ |

## Expression and Purification

- **Expression system**: Escherichia coli SG13009 (pREP4)
- **Construct**: Full-length MthK M107I mutant with C-terminal hexahistidine tag and thrombin cleavage site
- **Induction**: 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/)
- **Media**: Standard LB medium

### Purification Workflow

*Source: doi/10.1038##417515a*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Extraction | Cell lysis and solubilization | — | 20 mM Tris pH 8.0, 100 mM KCl + 40 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) (DM) |  |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) Co2+ affinity column | [TALON](/xray-mp-wiki/reagents/additives/talon/) Co2+ resin | 5 mM DM, 20 mM Tris pH 8.0, 100 mM KCl | Wash with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), elute with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| His-tag cleavage | Thrombin digestion | — |  | 1 unit thrombin per 3.0 mg channel, overnight at room temperature |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (10/30) | 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), 20 mM Tris pH 8.0, 100 mM KCl |  |

### Purification Workflow

*Source: doi/10.1038##nsmb.1865*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression and purification | Cell lysis and affinity purification | — | Standard buffer + [n-Decyl-β-D-maltoside](/xray-mp-wiki/reagents/detergents/dm/) (DM) | MthK channel expressed and purified in DM as described previously |
| Limited [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) digestion | Proteolysis | — |  | Membrane-spanning pore obtained by limited [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) digestion of MthK channel |
| Gel filtration | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 100 mM KCl |  |

### Purification Workflow

*Source: doi/10.1038##ncomms3621*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and induction | E. coli XL-1 Blue culture | — |  | Induction with 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) |
| Cell lysis | Sonication | — | 20 mM Tris, 100 mM KCl, pH 7.6 | PMSF and Complete EDTA-free protease inhibitor cocktail added |
| Solubilization | Detergent extraction | — | 20 mM Tris, 100 mM KCl, pH 7.6 + 50 mM decyl maltoside (DM) | Incubation for 2 h, followed by centrifugation at 30,500 g for 45 min |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Co2+-charged HiTrap metal affinity column | Co2+-charged HiTrap (GE Healthcare) | 20 mM Tris, 100 mM KCl, pH 7.6 + 5 mM DM | Wash with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), elute with 400 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| His-tag cleavage | Thrombin digestion | — |  | 2.0 units thrombin per 3.0 mg eluted protein, 2 h at room temperature |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM Tris, 100 mM KCl, pH 7.6 + 5 mM DM | Concentrated to 5 mg/mL after SEC |

**Final sample**: Purified full-length MthK at 5 mg/mL

### Purification Workflow

*Source: doi/10.1073##pnas.2009624117*

- **Expression system**: E. coli

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and extraction | HiTrap Co2+ charged metal-affinity | — | 100 mM KCl, 20 mM Hepes, 5 mM DM, pH 8.0 + [DM](/xray-mp-wiki/reagents/detergents/dm/) (DM) |  |
| Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | — | 100 mM KCl, 20 mM Hepes, pH 8.0 + 5 mM DM |  |
| [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) digestion | [Limited Proteolysis](/xray-mp-wiki/methods/purification/limited-proteolysis/) | — |  | [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) type I at 1:50 [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/):MthK for 2 h. [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) inhibitor type II-O added at 2x mass of [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/). |
| Gel filtration (pore) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | — | 100 mM KCl, 10 mM Mops, pH 8.0 + 5 mM DM |  |
| Detergent exchange | Gel filtration | — | 100 mM KCl, 10 mM Mops, pH 8.0 + 10 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) |  |
| Dialysis (low K+) | Dialysis | — | 100 mM NaCl, 1 mM KCl, 10 mM Mops, pH 8.0 (NaOH), 10 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) | For low [K+] crystallization experiments only |


## Crystallization

### doi/10.1038##417515a

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | MthK M107I at 15 mg/mL in 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), 20 mM Tris pH 8.0, 100 mM KCl |
| Reservoir | 23-26% PEGMME, 100 mM MES pH 6.5, 200 mM CaCl2 |
| Temperature | 20 C |

### doi/10.1038##nsmb.1865

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified MthK pores in [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) at ~8 mg/mL |
| Reservoir | 3.0-3.5 M 1,6-hexanediol, 100 mM HEPES pH 7.5 |
| Notes | Wild-type crystals were space group I4 with anisotropic diffraction; V77C with S68R or S68H mutations improved packing yielding P42_12 space group |

### doi/10.1073##pnas.2009624117

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | MthK pore at ~15 mg/mL in [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) |
| Reservoir | Varied with [K+] condition |
| Notes | Crystals in 150, 50, 11, and 6 mM [K+]. Lower [K+] crystals were very small (~10-15 um) but high-resolution diffraction (<2 A) obtained for all conditions. 1 mM [K+] sample failed to crystallize without K+ supplementation. PDB 6U9P (150 mM), 6U9T (50 mM), 6U9Y (11 mM), 6U9Z (6 mM). |

### doi/10.1038##ncomms3621

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified MthK RCK domain after limited [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) digestion and SEC |
| Reservoir | High CaCl2 buffer for WT-C1C2C3; 200 mM CaCl2 for WT-C1; 200 mM CaCl2 for D184N and E212Q mutants |
| Notes | WT-C1C2C3: P3_121, 2.5 A. WT-C1 (low Ca2+): P2_111, 1.85 A, Rwork/Rfree 0.211/0.253. D184N mutant: P6_522, 2.4 A, Rwork/Rfree 0.197/0.247. E212Q mutant: P6_522, 3.0 A, Rwork/Rfree 0.217/0.263. Mutant and WT RCK domains crystallized under identical conditions for direct comparison. |


## Biological / Functional Insights

### Gating ring mechanism for Ca2+-dependent channel opening

The MthK channel structure revealed that eight RCK domains assemble into a gating ring at the intracellular membrane surface. Four RCK domains are attached to the pore-forming subunits (blue), and four are soluble domains assembled from solution (red). Two distinct protein-protein interfaces hold the ring together: a fixed interface (formed by helices alphaD and alphaE) and a flexible interface (formed by the C-terminal subdomain and helices alphaF and alphaG). Ca2+ binds at the base of a cleft between two RCK domains at the flexible interface, coordinated by Glu210, Glu212, and Asp184.

### Proposed mechanism of mechanical work by the gating ring

The gating ring converts the free energy of Ca2+ binding into mechanical work to open the pore. Ca2+ binding reshapes the ligand-binding cleft at the flexible interface, causing rigid RCK domain pairs (connected by fixed interfaces) to tilt and rotate. This movement expands the diameter of the gating ring, which in turn pulls open the pore's inner helices via the disordered linkers connecting the pore and gating ring. In the Ca2+-bound state, the MthK pore is wide open, with inner helix arrangements distinctly different from the closed [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) K+ channel.

### High-resolution structure of K+ selectivity and the anomalous mole-fraction effect

High-resolution (1.45 A) crystal structures of the MthK pore in three ionic conditions (K+ complex, low-K+/high-Na+ complex, and Na+ complex) revealed that the MthK selectivity filter maintains a conductive conformation even in the absence of K+, unlike the [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) channel whose filter collapses in low K+. At high K+ concentrations, two K+ ions equivalently occupy all four sites in the selectivity filter in 1,3 and 2,4 configurations. At low K+/high Na+ concentrations, a single K+ ion remains bound preferentially at site 1 or site 3, effectively blocking Na+ permeation. This provides the structural basis for the anomalous mole-fraction effect, a defining property of multi-ion pores where a second permeable ion species paradoxically blocks current carried by the first. Na+ ions coordinate in plane with carbonyl oxygen atoms of Tyr62 in a pyramidal geometry, with an additional water ligand from the extracellular side.

### Allosteric coupling between C1 and C3 Ca2+-binding sites in the RCK domain

Crystal structures of WT and mutant MthK RCK domains at varying Ca2+ occupancies revealed that two physically distinct Ca2+-binding sites (C1 in the N-lobe and C3 at the interface between adjacent RCK domains) are allosterically coupled. Ca2+ binding at C1 (the higher-affinity site in WT) makes Ca2+ binding at C3 relatively unfavourable. The D184N mutation, which abrogates Ca2+ binding at C1, makes Ca2+ binding at C3 more favourable. The E212Q mutation, which alters Ca2+ coordination geometry at C1 (Q212 is 3.3 A from Ca2+ vs 2.5 A for E212 in WT), also enhances C3 binding but without eliminating C1 binding, resulting in overall enhanced Ca2+ sensitivity of the channel.

### E259-E133 carboxyl-carboxylate hydrogen bond as mediator of allosteric coupling

Systematic comparison of WT and mutant RCK domain structures identified a carboxyl-carboxylate hydrogen bond between Glu259 and Glu133 that mediates allosteric communication between C1 and C3 calcium-binding sites. When Ca2+ is absent from C3, the Glu259-Glu133 distance is short (2.6-2.9 A, consistent with a hydrogen bond). When Ca2+ is bound at C3, this distance increases to 3.5-4.8 A. Mutation of Glu259 to Ala (E259A) enhances Ca2+ sensitivity similarly to E212Q, and the E212Q/E259A double mutant is indistinguishable from single mutants, indicating that disruption of either the E212-Ca2+ bond or the E259-E133 hydrogen bond is sufficient to abolish allosteric communication.

### Working model of sequential Ca2+ binding and RCK domain activation

A working model for allosteric activation of MthK was derived from structural and functional data. With Ca2+-binding sites empty, RCK domains exist in a range of conformations. Ca2+ initially binds to the C1 sites in the N-lobe (higher affinity), stabilizing a partially activated conformation. The Glu259-Glu133 interaction keeps the C-lobe in a conformation incompatible with Ca2+ binding at C3. At higher Ca2+ concentrations, Ca2+ binds to C3 sites, which bridge the C-lobes of adjacent RCK domains, requiring disruption of the Glu259-Glu133 interaction. Full occupancy of both C1 and C3 is required for maximal channel opening. This inhibitory interaction between two Ca2+-binding sites provides a structural mechanism for tuning Ca2+ sensitivity.

### Voltage-dependent gate localized at the selectivity filter

Electrophysiological analysis of MthK using quaternary ammonium (QA) blockers of varying sizes ([TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/), bTBA, bbTBA) revealed that the voltage-dependent gate is located at the selectivity filter rather than at the intracellular bundle crossing. [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) block displayed strong voltage dependence, with the blocker sensing ~65% of the transmembrane electric field, indicating that blockers access a binding site deep within the pore near the selectivity filter. In contrast, larger blockers (bTBA, bbTBA) showed reduced voltage dependence and trapped the channel in the open state during inactivation, consistent with a binding site at or above the selectivity filter. The apparent affinity of [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) increased substantially during inactivation gating (Kd from ~65 uM open state to ~6 uM inactivated state), suggesting that inactivation involves conformational changes at the selectivity filter that enhance blocker binding. These findings demonstrate that the selectivity filter of MthK serves as both the ion selectivity determinant and the primary voltage-dependent gate, providing a structural basis for C-type inactivation in potassium channels.

### Activation gate–selectivity filter coupling via I84–T59 hydrophobic contact

Systematic MD simulations of MthK at varying levels of activation gate opening, combined with crystal structures (including new structure 6OLY), revealed that ion conductance is primarily controlled at the selectivity filter (SF) rather than by a physical gate at the helix bundle crossing. The SF opening at threonine 59 (T59), which forms ion binding site S4, is coupled to activation gate opening through a collective motion of transmembrane helices M1 and M2. A hydrophobic contact between isoleucine 84 (I84) on the M2 helix and the T59 side chain mediates this allosteric communication. As the activation gate opens, I84 residues move apart, and T59 residues follow to maintain favorable hydrophobic interactions, widening the SF. Mutation of I84 to alanine (I84A) shifts the current–opening relationship to smaller AG openings, confirming the functional role of this interaction. At small AG openings, the SF imposes high energy barriers for ion permeation (especially between sites S4 and S3). At optimal openings, the SF widens sufficiently to lower barriers and enable efficient direct knock-on ion conduction, matching experimental single-channel currents (~25 pA at 200 mV). At wide AG openings beyond those observed in crystal structures, water enters the SF and disrupts the direct knock-on mechanism, reducing outward K+ current. This water-mediated current decline is associated with carbonyl flipping of valine 60 (V60) at the S3 binding site, proposed as the initial step of MthK C-type inactivation. The study establishes a unified gating model for SF-activated potassium channels including MthK, BK, and K2P channels, where the selectivity filter functions as the primary gate regulated allosterically by the activation gate.

### Uneven K+ titration across SF binding sites distinguishes MthK from KcsA

X-ray crystallography at 150, 50, 11, and 6 mM K+ revealed that MthK maintains a conductive SF
conformation across all conditions, unlike [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) whose SF collapses at low K+. The S2 site
selectively loses K+ at low concentrations (apparent Kd ~50 mM), while S1, S3, and S4 remain
nearly fully occupied (sub-mM affinity). This uneven titration differs from [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) where all SF
sites show uniform occupancy decrease with K+ concentration.

### MD simulations show MthK SF can collapse but only when all K+ is removed

Molecular dynamics simulations revealed that the MthK SF can collapse similarly to [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), but
only when all K+ ions are removed from the SF. A single K+ ion binding at any SF site
(except S4) is sufficient to rescue the conductive state. The SF collapse involves loss of
water at S2, water binding behind the SF, and 180-degree carbonyl rotations at the central
[Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (G61), analogous to [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/)'s Gly77 flipping.

### S2 low K+ affinity arises from weaker carbonyl coordination by pore helix interactions

[Free Energy Perturbation](/xray-mp-wiki/methods/structure-determination/free-energy-perturbation/) (FEP) calculations showed K+ preferentially occupies S3 over S2
(Delta_G = -2.5 kcal/mol for vacancy-mediated). The reduced S2 affinity is due to weaker
coordination by G61 and T59 carbonyl groups, arising from different interactions with the
pore helix and water behind the SF. MthK lacks the equivalent of [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/)'s E71 residue,
which stabilizes G77 carbonyl orientation via H-bond with the amide of G77-Y78. Without
this interaction, MthK's Y62 amide binds more weakly to a mobile water molecule.

### Functional significance of low-affinity S2 site for K+ conduction

The existence of a low-affinity K+ binding site at S2 (~50 mM apparent Kd) is important for
rapid K+ conduction — during transport, the low affinity in S2 allows fast release of K+,
enabling high ionic throughput. This site was previously proposed in BK channels as the
"enhancement" site. Under a driving force, ions may exit the SF faster than refilling,
transiently emptying the SF and leading to collapse, which may explain the voltage-dependent
gating observed in MthK.


## Cross-References

- [C-type inactivation](/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/) — MthK undergoes C-type-like inactivation at the selectivity filter
- [Selectivity filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — The SF is the primary gate controlling K+ ion conduction in MthK
- [Channel gating](/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/) — AG-SF coupling is a fundamental gating mechanism in potassium channels
- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — KcsA is the prototypical K+ channel for AG-SF coupling studies referenced in this work
- [Human TRAAK Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/traak/) — TRAAK shows similar SF activation behavior as MthK
- [Alternating Ion-Bound Configurations](/xray-mp-wiki/concepts/transport-mechanisms/alternating-ion-bound-configurations/) — Ion occupancy patterns in the SF determine conduction and inactivation states
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — SF-TM2 coupling mediates allosteric communication during gating and inactivation
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Primary method for structural titration at 4 K+ concentrations (6-150 mM)
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/molecular-dynamics-simulation/) — MD simulations revealed SF collapse mechanism and ion occupancy effects on gating
- [Free Energy Perturbation](/xray-mp-wiki/methods/free-energy-perturbation/) — FEP calculations quantified K+ binding preferences between S2 and S3 sites
- [Decyl maltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Used for MthK solubilization and purification
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Used as purification buffer in all MthK preparations
