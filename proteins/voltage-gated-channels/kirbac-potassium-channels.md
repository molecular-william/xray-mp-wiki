---
title: "KirBac Potassium Channels"
created: 2026-05-26
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##J.CELL.2010.05.003, doi/10.1038##NSMB.2208, doi/10.3390##ijms23010335, doi/10.1038##s41467-020-16842-0, doi/10.1126##science.1085028, doi/10.1074##jbc.M113.501833, doi/10.1038##s41467-022-28148-4]
verified: false
---

# KirBac Potassium Channels

## Overview

KirBac1.1 and KirBac3.1 are prokaryotic inward-rectifier potassium channels from Magnetospirillum magnetotactium that serve as structural models for eukaryotic Kir channels. A comparative analysis of 11 KirBac crystal structures (KirBac1.1 at 3.7 A and multiple KirBac3.1 structures at 2.6-4.2 A resolution) revealed interdependent gates in the conduction pathway and the mechanism of polyamine block, including interdomain conformational changes coupled to ion configuration in the selectivity filter, identification of two polyamine-binding sites, and a staged activation pathway via two-fold symmetric intermediates. The first open-state structure of a KirBac channel was obtained using the S129R gating mutant of KirBac3.1 (3.05 A resolution), which traps the helix bundle crossing in an open conformation. This structure demonstrates that TM2 bends at a conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) hinge (Gly120) and rotates approximately 25 degrees to open both the bundle-crossing gate (Tyr132) and a secondary constriction at Leu124. Contrary to prior models, this open structure adopts a twist conformation yet maintains a conductive selectivity filter with all four K+ binding sites occupied. A network of interactions between the TMD and CTD — involving the C-linker, slide helix, G-loop, and CD loop — couples rotational movement of the cytoplasmic domain to opening of the bundle-crossing gate. Crosslinking experiments on KirBac3.1 (PDB 6O9T, 6O9U, 6O9V) challenged the canonical gating model by showing that covalently constraining the Tyr132 intracellular collar to prevent widening does not impair K+ conduction. MD simulations reveal that K+ ions transiently lose 3-4 water molecules from their hydration shell to pass through the constriction, with a low free-energy barrier to partial dehydration. These findings demonstrate that Kir channels do not require the canonical pore-dilation gating mechanism and suggest the selectivity filter or lipid-mediated changes may be the primary gate.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1085028 | 1P7B | 3.65 A | I222 | Full-length KirBac1.1 | Mg2+ ions |
| doi/10.1016##J.CELL.2010.05.003 | 1P7B | 3.7 A | I222 | Full-length KirBac1.1 with His-tag | Mg2+ (blocked configuration) |
| doi/10.1016##J.CELL.2010.05.003 | 1XL4 | 2.6 A | P21212 | Full-length KirBac3.1 with His-tag | Ca2+ (blocked), [Spermine](/xray-mp-wiki/reagents/additives/spermine/) |
| doi/10.1016##J.CELL.2010.05.003 | 1XL6 | 2.8 A | C2221 | Full-length KirBac3.1 with His-tag | [Spermine](/xray-mp-wiki/reagents/additives/spermine/) (conduction-compromised) |
| doi/10.1016##J.CELL.2010.05.003 | Structure III | 3.1 A | P21212 | Full-length KirBac3.1 with His-tag | none (stalled twist conformation) |
| doi/10.1016##J.CELL.2010.05.003 | Structure IV | 3.3 A | I222 | Full-length KirBac3.1 with His-tag | none (stalled twist conformation) |
| doi/10.1016##J.CELL.2010.05.003 | Structure V | 3.5 A | C2221 | Full-length KirBac3.1 with His-tag | none (stalled twist conformation) |
| doi/10.1016##J.CELL.2010.05.003 | Structure VI | 3.8 A | P1 | Full-length KirBac3.1 with His-tag | none (unlatched, conducting twist conformation) |
| doi/10.1016##J.CELL.2010.05.003 | Structure VII | 4.2 A | P212121 | Full-length KirBac3.1 with His-tag | none (stalled twist conformation) |
| doi/10.1016##J.CELL.2010.05.003 | Structure IX | 3.2 A | P21212 | Full-length KirBac3.1 with His-tag | none (twist conformation) |
| doi/10.1016##J.CELL.2010.05.003 | Structure X | 3.0 A | P21212 | Full-length KirBac3.1 with His-tag | Ba2+ (blocked configuration) |
| doi/10.1016##J.CELL.2010.05.003 | Structure XI | 2.9 A | P21212 | Full-length KirBac3.1 with His-tag | Sm3+ (nontwist, conducting conformation) |
| doi/10.1038##NSMB.2208 | S129R mutant (open state) | 3.05 A | P42_12 | KirBac3.1 S129R gating mutant, codon-optimized for E. coli expression in pET30a vector | K+ ions in selectivity filter (S1-S4 occupied, conductive conformation) |
| doi/10.3390##ijms23010335 | 7ADI | 2.80 A | P2_1_2_1_2 | KirBac3.1 W46R mutant, full-length with His-tag, expressed in E. coli in pET30a vector | K+ and Mg2+ ions |
| doi/10.1038##s41467-020-16842-0 | 6O9T | 3.1 A | P4(3)2(1)2 | KirBac3.1 S129C-F135C with MTS-1-MTS crosslinker, C262S/C71V/C119V background | K+ ions |
| doi/10.1038##s41467-020-16842-0 | 6O9U | 2.0 A | P4(3)2(1)2 | Full-length wild-type KirBac3.1 (C262S/C71V/C119V background) | K+ ions |
| doi/10.1038##s41467-020-16842-0 | 6O9V | 4.1 A | P4(3)2(1)2 | KirBac3.1 A133C-T136C with dibromobimane crosslinker, C262S/C71V/C119V background | K+ ions |
| doi/10.1074##jbc.M113.501833 | 4LP8 | 2.46 A | P4_2_1_2 | KirBac3.1 S129R/S205L double mutant, full-length, expressed in E. coli | K+ ions in selectivity filter, K+ ion in CTD pore coordinated by Glu173 and Asp175 |

 - R-work 0.183%, R-free 0.248%; Data collection: Diamond Light Source I-24 beamline (lambda=0.978 A), 100 K, Pilatus 6M detector

## Expression and Purification

- **Expression system**: E. coli BL21 (DE3) star
- **Construct**: Full-length histidine-tagged recombinant KirBac3.1 from Magnetospirillum magnetotactium. Q170A mutant expressed separately for comparison.

### Purification Workflow

#### Source: doi/10.1016##J.CELL.2010.05.003


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization | -- | Not specified + -- | Cells lysed at 20,000 psi in a high-pressure homogenizer |
| Solubilization | Detergent solubilization | -- | -- + 1% [Anzergent 3,12](/xray-mp-wiki/reagents/detergents/anzergent-3-12/) at room temperature for 1 hr | Cellular debris removed by centrifugation after solubilization |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni2+-loaded IMAC resin | Ni2+-IMAC | -- + 1% [Anzergent 3,12](/xray-mp-wiki/reagents/detergents/anzergent-3-12/) | His-tagged KirBac3.1 purified by [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) |
| Size-exclusion chromatography | Size-exclusion chromatography | -- | -- + 1% [Anzergent 3,12](/xray-mp-wiki/reagents/detergents/anzergent-3-12/) | Peak fractions pooled after SEC |
| Concentration | Ultrafiltration | Amicon | -- + -- | Concentrated to ~8 mg/ml for crystallization |

#### Source: doi/10.1038##NSMB.2208


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Not specified | -- | Not specified + -- | Expression and purification identical to previously described wild-type KirBac3.1 protocol |
| Gel filtration | Size-exclusion chromatography | -- | Not specified + triDM | Detergent exchanged from triDM into 14 mM [HEGA-10](/xray-mp-wiki/reagents/detergents/hega-10/) using Vivaspin concentrators (100 kDa cutoff) after gel filtration |
| Concentration | Vivaspin concentrators (100 kDa cutoff) | -- | Not specified + 14 mM [HEGA-10](/xray-mp-wiki/reagents/detergents/hega-10/) | Concentrated to 6 mg/ml for crystallization |

#### Source: doi/10.3390##ijms23010335


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press | -- | -- + -- | Cell disruption by French press |
| Solubilization | Detergent solubilization | -- | -- + 45 mM DM (Decyl beta-D-maltopyranoside) | Directly solubilized with 45 mM DM, then centrifuged |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Co2+ affinity column | Co2+ affinity resin | -- + -- | Supernatant loaded onto Co2+ affinity column |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 | 2 mM TriDM + 2 mM TriDM | Purified on [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) column pre-equilibrated with 2 mM TriDM buffer |
| Concentration | Ultrafiltration | -- | 20 mM Tris pH 7.4, 150 mM KCl, 0.2 mM TriDM + 0.2 mM TriDM | Concentrated to 1-2.5 mg/mL, stored at -80 C |

#### Source: doi/10.1074##jbc.M113.501833


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Size-exclusion chromatography | SEC | Not specified | Not specified + tridecyl-beta-maltoside | After elution from SEC, detergent exchanged to 14 mM [HEGA-10](/xray-mp-wiki/reagents/detergents/hega-10/) using Amicon 100-kDa cutoff filtration device |
| Concentration | Amicon 100-kDa cutoff filtration | Amicon | Not specified + 14 mM [HEGA-10](/xray-mp-wiki/reagents/detergents/hega-10/) | Concentrated to 6 mg/ml for crystallization |


## Crystallization

### doi/10.1016##J.CELL.2010.05.003

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified KirBac3.1 at ~8 mg/ml |
| Reservoir | 20% [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350 + 0.2 M calcium chloride + 0.1 M HEPES buffer pH 7.5 (III); 15% [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350 + 0.1 M [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) + 0.1 M [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) buffer pH 5.6 (VI); 20% [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350 + 0.2 M [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) + 0.1 M HEPES buffer pH 7.5 (VIII); 20% [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350 + 0.2 M [Spermine](/xray-mp-wiki/reagents/additives/spermine/) + 0.1 M HEPES buffer pH 8.0 (XI) |
| Temperature | 19-20 C |
| Growth time | Not specified |
| Cryoprotection | Crystals soaked in 50 mM [Spermine](/xray-mp-wiki/reagents/additives/spermine/) prior to data collection (structures II and VIII) |
| Notes | Crystallized at Bio21 C3 facility. Structures III-VII phased by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using 1XL4/1XL6. Q170A mutant crystallized separately. Structure XI soaked with Sm3+ to capture nontwist form. |

### doi/10.1038##NSMB.2208

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | KirBac3.1 S129R at 6 mg/ml in 14 mM [HEGA-10](/xray-mp-wiki/reagents/detergents/hega-10/) |
| Reservoir | 10% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 90 mM HEPES pH 7.2, 20% (v/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 5% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 4000, 2.5% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 8000 |
| Temperature | 20 C |
| Growth time | 3-4 days |
| Cryoprotection | Crystals cryocooled under liquid nitrogen before analysis |
| Notes | Crystals grown using 1:1 protein:reservoir ratio. Data collected at Diamond Light Source I-24 beamline (lambda = 0.9778 A) at 100 K using Pilatus 6M detector. |

### doi/10.3390##ijms23010335

| Parameter | Value |
|---|---|
| Method | Sitting-drop and hanging-drop vapor diffusion |
| Protein sample | KirBac3.1 W46R at 10 mg/mL in 20 mM Tris pH 7.4, 150 mM KCl, 0.2 mM TriDM |
| Reservoir | 15% (w/v) PEG-MME 5k, 15% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 M LiCl, 100 mM MES pH 6.5 |
| Temperature | 18 C |
| Growth time | Not specified |
| Cryoprotection | Reservoir solution used as cryo-protectant |
| Notes | Initial screening with Mosquito nanoliter-dispensing system (672 conditions). Best crystals obtained by hanging-drop vapor diffusion. 400 nL drops (1:1 protein:reservoir) for screening, 4 uL drops for optimization. Crystals in P2_1_2_1_2 space group. Data collected at SOLEIL PROXIMA-1 beamline at 100 K with PILATUS 6M detector at 1.07114 A wavelength. |

### doi/10.1074##jbc.M113.501833

| Parameter | Value |
|---|---|
| Method | Not specified (hanging/sitting drop vapor diffusion) |
| Protein sample | KirBac3.1 S129R/S205L at 6 mg/ml in 14 mM [HEGA-10](/xray-mp-wiki/reagents/detergents/hega-10/) |
| Reservoir | 10% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 90 mM HEPES pH 7, 20% (v/v) [Polyethylene Glycol 400 (PEG 400)](/xray-mp-wiki/reagents/additives/peg-400/), 5% (w/v) [PEG 4000 (Polyethylene Glycol 4000)](/xray-mp-wiki/reagents/additives/peg-4000/), 2.5% (w/v) [Polyethylene Glycol 8000 (PEG 8000)](/xray-mp-wiki/reagents/additives/peg-8000/), 10 mM spermidine |
| Temperature | 20 C |
| Growth time | 2-4 days |
| Cryoprotection | Crystals harvested using LithoLoops (Molecular Dimensions) and immediately cryo-cooled in liquid N2 |
| Notes | Crystals appeared after 2-4 days at room temperature. Data collected at Diamond Light Source I-24 beamline (lambda=0.978 A) at 100 K using Pilatus 6M detector to 2.46 A resolution. |


## Biological / Functional Insights

### Interdependent gates in the conduction pathway

Crystallographic evidence reveals interdependent gates in the Kir channel conduction pathway. Reorientation of the intracellular domains, concomitant with activation, instigates polyamine release from intracellular binding sites to block the permeation pathway. Conformational adjustments of the slide helices, achieved by rotation of the cytoplasmic assembly relative to the pore, are directly correlated to the ion configuration in the selectivity filter. Ion redistribution occurs irrespective of the bundle crossing constriction, suggesting a more expansive role of the selectivity filter in gating than previously appreciated.

### Selectivity filter gating and ion configuration

The ion distribution in the selectivity filter is systematically correlated to global conformational changes. Twist structures (III-VII, IX) have a three-ion configuration (S1, S3, S4) representing stalled conduction. Nontwist structures (II, VIII, X) have four occupied sites (S1, S2, S3, S4) corresponding to conducting or blocked states. Divalent ions (Mg2+, Ca2+, Ba2+) produce cation-specific blocked configurations. The selectivity filter can switch between nonconducting and conducting configurations without significant displacement of the inner helices, suggesting a more prominent role for the selectivity filter in gating than previously appreciated.

### Polyamine binding and rectification mechanism

Two distinct polyamine-binding sites identified at latched intracellular interfaces. [Spermine](/xray-mp-wiki/reagents/additives/spermine/) binds within closed pockets at latched interfaces but not at unlatched interfaces. Unlatching causes the intracellular vestibule to connect with the pore, simultaneously disrupting binding sites and facilitating polyamine release into the conduction path. His177 in KirBac3.1 (counterpart of His216 in Kir6.2) interacts with Asp197 to enclose the binding pocket. Protonation of His177 at low pH offsets the negative charge of Asp197, reducing electrostatic attraction of polyamines and providing a mechanism for pH-titratable rectification.

### Staged activation pathway via symmetric intermediates

Conformational interchange mediated at intracellular subunit interfaces follows a staged path to activation via two-fold symmetric intermediates. In intermediate states, every other subunit is unlatched, distorting symmetry along a cross-sectional diagonal. Only when all four interfaces have eschewed the latched arrangement can the selectivity filter acquire a conducting conformation. Unlatching is concomitant with activation. The Q170A mutant is effectively unlatched at all four interfaces but has fewer molecular constraints, resulting in a 1-2 degree difference in cytoplasmic domain orientation and higher open probability.

### Molecular pulleys link unlatching to domain reorientation

Structural interdependency links rearrangement at subunit interfaces to systematic reorientation of intracellular domains, where latched and unlatched states differ by approximately 5 degrees. Coupling is facilitated by the N and C termini acting as a pulley system. The intracellular domain of each subunit is an immunoglobulin-like beta sandwich overlaid by N and C termini, with the C terminus tethered to both the N terminus and the underlying beta sandwich. Parallel beta sheet interactions formed between betaC_N on one subunit and betaM on another interweave neighboring subunits into a circle, coupling the motion of each subunit to that of its neighbor.

### Open-state gating via TM2 bending and rotation

The first open-state structure of a KirBac channel (S129R mutant) reveals that TM2 bends at Gly120 by up to 20 degrees and rotates approximately 25 degrees along its helical axis to open the bundle-crossing gate. This rotation moves the secondary constriction at Leu124 away from the pore, increasing effective pore diameter from less than 2 A to greater than 8 A. Contrary to a previously proposed gating model, the structure adopts a twist configuration of the CTD yet maintains a fully conductive selectivity filter with all four K+ binding sites (S1-S4) occupied. A network of inter- and intrasubunit interactions involving the C-linker, slide helix, G-loop, and CD loop couples rotational movement of the CTD to opening of the bundle-crossing gate.

### W46R mutation disrupts TM1-TM2 hydrophobic cluster in KirBac3.1

The W46R mutation replaces the highly conserved tryptophan at the cytosolic end of TM1 (equivalent to W68 in Kir6.2) with arginine. In wild-type KirBac3.1, W46 adopts a 'flipped-in' conformation tightly packed against the C-terminal end of TM2, interacting with I131, R134, and F135. In the W46R mutant crystal structure (PDB 7ADI, 2.80 A), R46 points away from the channel pore in a 'flipped-out' conformation (98.68% occupancy in MDeNM), disrupting these hydrophobic contacts and forming new electrostatic interactions with Y38 and D36 on the slide helix of the adjacent subunit.

### Differential flexibility revealed by HDX-MS

[HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/) experiments show that the W46R mutant has reduced flexibility at the mutation site (aa 43-56: 37.9% vs 65.1% normalized HDX rate) due to a stable interaction network around R46. However, this is accompanied by increased flexibility in the slide helix (aa 36-42: 41.57% vs 26.92%), selectivity filter region (aa 93-112: 50.04% vs 30.08%), and CD-loop (aa 162-174: 94.61% vs 83.1%), illustrating long-range conformational effects propagating from the mutation site to the pore and cytoplasmic domains.

### W46R gating mechanism involves synchronized chain movements

MDeNM simulations reveal a multi-step gating mechanism: (1) R46 interacts with D36 on the slide helix of the neighboring subunit; (2) this interaction promotes upward movement of the slide helices; (3) slide helix movement induces tilting of TM1 and TM2; (4) this causes increased opening at the L124 constriction (33% vs 29% WT) but decreased opening at Y132 (11% vs 14% WT). The fully open state population is similar (7.4% vs 6.8% WT). Correlations between chains are more pronounced in the mutant, suggesting synchronized gating steps - a key difference from the uncorrelated chain movements in WT.

### W46R functional characterization and relevance to neonatal diabetes

Single-channel recordings of purified W46R reconstituted in DPhPC lipid bilayers show a single-channel conductance of 36 pS at +100 mV and open probability of 0.071, similar to the WT (0.099). The mutation does not significantly alter the intrinsic open probability of the bacterial KirBac channel. By analogy, the homologous W68R mutation in human Kir6.2 (which causes neonatal diabetes) is hypothesized to reduce ATP sensitivity by disrupting the hydrophobic cluster that couples ATP binding to pore closure, rather than directly increasing open probability.

### Constricted Tyr132 opening does not impede K+ conduction

Crosslinking experiments using disulfide bonds and chemical crosslinkers (MTS-1-MTS, dibromobimane) to covalently link the four inner helices of KirBac3.1 at the Tyr132 collar demonstrate that K+ conduction continues unimpaired even when the intracellular opening is locked in a constricted conformation. Crystal structures of crosslinked mutants S129C-F135C-MTS-1-MTS (PDB 6O9T, 3.1 A) and A133C-T136C-bimane (PDB 6O9V, 4.1 A) confirm the crosslinks encircle the conduction pathway at Tyr132. [Native Mass Spectrometry](/xray-mp-wiki/methods/quality-assessment/native-mass-spectrometry/) and SDS-PAGE verified complete tetrameric crosslinking. Liposomal flux assays using the ACMA fluorimetric assay show that all six crosslinked variants conduct K+ at levels comparable to wild-type channels.

### K+ permeates the narrow collar by partial dehydration

All-atom MD simulations using [Umbrella Sampling](/xray-mp-wiki/methods/structure-determination/umbrella-sampling/) to calculate the potential of mean force (PMF) reveal that K+ passes through the Tyr132 collar in a partially dehydrated state, transiently shedding 3-4 water molecules from its hydration shell. The coordination number drops from approximately six in the cavity to three or four at the constriction. Transient interactions with Tyr132 hydroxyl groups partially compensate for lost waters. The free energy barrier to permeation at the constriction is not prohibitive (low kJ/mol), demonstrating that the narrow opening does not represent a significant energetic barrier to K+ flux.

### Spermine block is prevented by crosslinking but K+ flux is unaffected

[Spermine](/xray-mp-wiki/reagents/additives/spermine/), a narrow polyamine blocker of Kir channels, is able to block wild-type KirBac3.1 but fails to block disulfide-linked A133C-T136C mutants. MD simulations show the disulfide-linked constriction presents a significantly higher PMF barrier to [Spermine](/xray-mp-wiki/reagents/additives/spermine/) penetration (25 kJ/mol vs 15 kJ/mol at site 2, and 45 kJ/mol vs 15 kJ/mol at site 4) compared to wild-type. The cross-sectional width of hydrated K+ (~6.6 A) and [Spermine](/xray-mp-wiki/reagents/additives/spermine/) (~5.6 A) explains this differential effect: K+ can partially dehydrate to pass through the ~4.0-6.0 A opening, while [Spermine](/xray-mp-wiki/reagents/additives/spermine/) as a rigid polyamine cannot. This provides direct experimental verification that the covalent disulfide linkages effectively constrain the pore without preventing K+ conduction.

### Canonical pore-gating model challenged for Kir channels

The finding that Kir channels conduct K+ through a constricted opening challenges the canonical gating model, which posits that a conformational change must widen the intracellular helix bundle crossing to accommodate fully hydrated K+ ions. Instead, these results suggest that the primary gate in Kir channels may be at the selectivity filter, or that gating involves changes in lipid accessibility at the pore entrance rather than pore dilation. The ability of K+ to shed water molecules from its coordination shell, combined with a short bottleneck distance that allows simultaneous access to water on both sides, enables conduction without significant structural rearrangement.

### Closed state architecture of KirBac1.1

The KirBac1.1 closed state structure at 3.65 A resolution reveals four mechanisms preventing ion conduction: (i) occlusion of the ion-conduction pathway by hydrophobic phenylalanine (Phe146) side chains acting as the activation gate, (ii) misalignment of pore helices away from the central cavity, (iii) decreased volume of the central cavity accommodating fewer water molecules (20 vs 27 in [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/)), and (iv) altered conformation of the selectivity filter with a stable K+ ion at the S2 position preventing filter collapse. The total ion conduction path is 88 A from the extracellular turret to the C-terminal domain.

### Slide helix as a gating coupling element

An amphipathic slide helix running parallel to the membrane-cytoplasmic interface serves as a central coupling mechanism between the intracellular domains and the blocking residue. The slide helix interacts with conserved Arg148 via its negative C-terminal end, using helix dipole interactions. Conserved Asp50 on the slide helix hydrogen bonds to the backbone nitrogen of Ser46, stabilizing the connection between the N-terminal strand and the slide helix. When the C-terminal assembly receives a gating signal, outer helices move with the slide helix, creating room for inner helix bending and displacement of Phe146 from the conduction pathway.

### Inner-helix bending at glycine hinges

Gating involves bending of the inner helix at conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues. KirBac1.1 has three [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues on the inner helix at positions 134, 137, and 143. Gly143 is the most highly conserved among Kir channels and is proposed as the primary hinge for helix bending during gating. As the channel opens, the slide helix moves laterally, exerting strain on the bottom of the inner helix and causing distortion at Gly143. This moves the blocking residue Phe146 away from the center of the ion-conduction pathway. Gly134 likely plays a minor role in gating and a more important role in protein packing.

### Dimer-of-dimers architecture and rectification

The KirBac1.1 channel shows a dimer-of-dimers arrangement where the transmembrane section displays four-fold symmetry but the intracellular domains adopt a two-fold arrangement, hinged at the cytosolic face of the membrane. Rectification involves three key residues: Ile138, Glu187, and Glu258. Glu187 and Glu258 form a double ring of negatively charged glutamate side chains in the C-terminal vestibule. These outstretched negatively charged rings, with ~8 A spacing between adjacent glutamate side chains, favor coordination of linear polyamines over compact Mg2+ ions, explaining the slower component of rectification by endogenous polyamines.

### S205L mutation stabilizes a novel open conformation at CTD interface

The S205L activatory mutation in the CTD of KirBac3.1, crystallized in the S129R/S205L double mutant (PDB 4LP8, 2.46 A), stabilizes a novel high-energy open conformation. S205L disrupts the Glu173-His177-Asp175 intersubunit triad, causing His177 to switch rotamer and form a new triad with Asp197 and Arg202. This releases Glu173 and Asp175 into the cytoplasmic pore, where they coordinate a potassium ion and alter the electrostatic potential of the CTD cavity, reducing the energetic barrier to K+ permeation. The S205L mutation increases channel activity in liposomal Rb+ flux assays (p=0.03) and complements growth in K+- auxotrophic E. coli.

### His177 as a pH-sensitive switch at the CTD interface

KirBac3.1 is a pH-sensitive channel with maximal activity at pH 8.0, decreasing at more alkaline pH. His177, equivalent to His216 in Kir6.2, acts as a pH-titratable switch at the CTD intersubunit interface. The H177A mutation mimics aspects of the S205L mutation by preventing formation of the Glu173-His177-Asp175 triad, releasing Glu173 and Asp175 to line the cytoplasmic vestibule. Both S205L and H177A increase activity at pH 7.5 but neither abolishes pH sensitivity, suggesting the pH sensor involves multiple titratable interactions.

### CTD interface dynamics control Kir channel gating

Molecular dynamics simulations (100 ns) of the S129R/S205L double mutant structure (with R129S/L205S reversion) show that the His177 side chain reverts from interacting with Asp197/Arg202 back to interacting with Glu173/Asp175 in three of four subunit interfaces. The G-loop gate closes (radius reduced from 5 to <2.2 A) in the double-mutant simulation but not the single-mutant, indicating the S205L mutant structure represents a higher energy open conformation. No untwisting of the CTD was observed, suggesting the CTD twist is stabilized in this conformation. Glu173 is conserved in strongly rectifying Kir channels (Glu225 in Kir2.2) and serves as a K+ coordination site that influences unitary conductance and polyamine block.

### Lipid acyl tails gate Kir channels by competing with Leu124 collar

Crystal structures of KirBac3.1 show the conduction pathway is occluded by a cluster of four Leu124 branched aliphatic side chains. Unbiased MD simulations revealed that fatty acyl chains of lipids occupying conserved fenestrations in the pore walls naturally interact with Leu124, drawing the leucine side chains away from the conduction pathway and creating an opening of ~5 A diameter. Each K+ permeation event occurred in response to lipid-Leu124 interaction. Umbrella sampling showed the energetic barrier at the Leu124 collar is 13 kJ/mol with native lipid interaction vs 41 kJ/mol when fenestrations are blocked (by Tyr57 gauche rotamer). The L124M mutant (labile methionine side chains) conducts K+ even when fenestrations are blocked, confirming the leucine collar is the primary gate.

### Minimal barrier to K+ permeation is at Leu124, not Tyr132

The canonical gating model posits the inner helix bundle (Tyr132 in KirBac3.1) is the permeation gate. However, Leu124 forms a steric cluster physically occluding the conduction pathway. ACMA fluorimetric population assays comparing Leu124M (exhibits similar activity to wild-type) and Tyr132I (also non-impairing) mutants demonstrate the Leu124 collar - not the Tyr132 bundle crossing - provides the limiting barrier. PMF calculations showed the energetic barrier at the Tyr132 collar is dissipative, confirming it is not a functional gate.

### Alkyl chain length determines gating efficacy

Alkyl-MTS reagents of varying chain lengths (hexyl, octyl, decyl) were covalently attached to Cys119 (adjacent to the fenestrations) to mimic lipid tails. ACMA assays showed decyl chains (C119-decyl) increased activity, while hexyl chains (C119-hexyl) reduced it by blocking fenestrations without reaching Leu124. Single channel recordings revealed C119-decyl has higher open probability (Po=0.69) and more fully open events, while C119-hexyl predominantly operates at lower conductance substrate levels. This demonstrates ion permeation is contingent on lipid tails being of sufficient length to reach the Leu124 occlusion.

### Anionic lipids bind specifically to KirBac3.1 and gate the pore

Coarse-grained MD simulations showed pores preferentially concentrate anionic lipids (PS, PG) around the pore, while zwitterionic PC accumulates at the tetramer interfaces. Native mass spectrometry of purified KirBac3.1 revealed adduct masses of +765, +1513, and +2270 Da, corresponding to 1-3 phospholipids (PE and PG). Lipidomics analysis confirmed PG enrichment and preferential binding of long-chain lipids (>34 total carbons). 95.5% of fenestration-occupying lipids had head groups within 5 A of the Arg137/Trp46/His37 canonical lipid-binding pocket. The nexus of electrostatic contacts between anionic lipid head groups and both pore and intracellular elements couples interdomain motions to the movement of lipid tails engaging Leu124.


## Cross-References

- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni2+-loaded IMAC used for His-tagged KirBac purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC used after affinity chromatography for KirBac purification
- [Anzergent 3,12](/xray-mp-wiki/reagents/detergents/anzergent-3-12/) — Primary solubilization detergent at 1% for KirBac3.1 extraction
- [Calcium Chloride](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Crystallization additive (0.2 M) in structure III
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Crystallization additive (0.1 M) in structure VI
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant (PEG 3350) used in all conditions
- [Spermine](/xray-mp-wiki/reagents/additives/spermine/) — Crystallization additive (0.2 M) and polyamine channel blocker
- [Citrate Buffer](/xray-mp-wiki/reagents/buffers/citrate/) — Crystallization buffer (0.1 M sodium citrate pH 5.6) in structure VI
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Crystallization buffer (0.1 M HEPES pH 7.5/8.0) in multiple structures
- [HEGA-10](/xray-mp-wiki/reagents/detergents/hega-10/) — Detergent for S129R mutant crystallization (14 mM)
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Crystallization additive (10% v/v) for S129R structure
