---
title: Human Adenosine A2A Receptor (A2AR)
created: 2026-05-26
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NATURE18966, doi/10.1016##j.bbrc.2023.149393, doi/10.1016##j.str.2017.06.012, doi/10.1016##j.str.2017.12.013, doi/10.1021##acs.jmedchem.0c01856, doi/10.1021##acs.jmedchem.2c00462]
verified: false
---

# Human Adenosine A2A Receptor (A2AR)

## Overview

The human adenosine A2A receptor (A2AR) is a class A G protein-coupled receptor that regulates glutamate and dopamine release in the brain and is a therapeutic target for Parkinson's disease and cancer. Multiple structures have been solved for the thermostabilized A2AR-StaR2-b562RIL construct complexed with xanthine ligands including PSB36 (2.8 A), caffeine (2.1 A), and theophylline (2.0 A), revealing details of ligand binding and subtype selectivity determinants.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NATURE18966 | -- | 3.4 A | P 2₁ 2₁ 2₁ | Wild-type human A2AR (residues 1-308), C-terminal His10 tag with TEV protease cleavage site, N154A mutation to remove N-linked glycosylation site, in complex with engineered mini-Gs (construct 414 with L63Y mutation) | NECA (A2AR), GDP (mini-Gs) |
| doi/10.1016##j.bbrc.2023.149393 | 8WDT | 3.34 A | -- | Thermostabilized mutant A2AR-Rag31 | trans-photoNECA (blue) |
| doi/10.1016##j.str.2017.06.012 | -- | 2.0 A | C2221 | Human A2AR-StaR2-b562RIL thermostabilized mutant | Theophylline |
| doi/10.1016##j.str.2017.06.012 | -- | 2.1 A | C2221 | Human A2AR-StaR2-b562RIL thermostabilized mutant | Caffeine |
| doi/10.1016##j.str.2017.06.012 | -- | 2.8 A | C2221 | Human A2AR-StaR2-b562RIL thermostabilized mutant | PSB36 |
| doi/10.1016##j.str.2017.12.013 | 5WF5 | 2.60 A | P21 | A2AAR-T4L D52N variant truncated after residue 316, N-terminal FLAG tag, C-terminal His10 tag, K209-A221 replaced by cysteine-free T4 lysozyme | UK432097 |
| doi/10.1016##j.str.2017.12.013 | 5WF6 | 2.90 A | P21 | A2AAR-T4L S91A variant truncated after residue 316, N-terminal FLAG tag, C-terminal His10 tag, K209-A221 replaced by cysteine-free T4 lysozyme | UK432097 |
| doi/10.1021##acs.jmedchem.0c01856 | 7ARO | 1.9 A | P212121 | A2A-StaR2-bRIL: human A2AR with 9 thermostabilizing mutations (A54L, T88A, R107A, K122A, N154A, L202A, L235A, V239A, S277A), N-terminal deletion of first 3 residues, C-terminal truncation after L315 with His10 tag, bRIL fused into ICL3 | LUF5833 (compound 8) |
| doi/10.1021##acs.jmedchem.2c00462 | 8CU7 | 2.05 A | -- | A2A-StaR2-bRIL: human A2AR with StaR2 mutations (including S277A), N-terminal deletion, C-terminal truncation after L315 with His10 tag, bRIL fused into ICL3 | LJ-4517 (compound 2) |
| doi/10.1021##acs.jmedchem.2c00462 | 8CU6 | 2.80 A | -- | A2A-StaR2-S277-bRIL: human A2AR with StaR2 mutations including S277A, N-terminal deletion, C-terminal truncation after L315 with His10 tag, bRIL fused into ICL3 | LJ-4517 (compound 2) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2AR-StaR2-b562RIL thermostabilized mutant of human adenosine A2A receptor

### Purification Workflow

*Source: doi/10.1038##NATURE18966*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| A2AR expression | Baculovirus expression in Sf9 insect cells (flashBAC ULTRA system); cells infected and incubated 72 h | -- | 20 mM HEPES pH 7.5, 1 mM EDTA, 1 mM PMSF + -- | Membranes prepared from 3 L cells; solubilized with 2% n-decyl-beta-D-maltopyranoside (DM) on ice for 1 h |
| A2AR purification | Ni-NTA affinity chromatography; SEC on Superdex-200 | Ni-NTA; Superdex-200 26/600 | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.05% DM, 100 uM NECA + DM | A2AR purified to homogeneity and concentrated to 10 mg/mL |
| mini-Gs expression | E. coli BL21(DE3)RIL expression upon IPTG induction for 20 h at 25 C; N-terminal His10 tag with TEV site; L63Y mutation included | -- | 40 mM HEPES pH 7.5, 100 mM NaCl, 10% glycerol, 10 mM imidazole, 5 mM MgCl2, 50 uM GDP + -- | Cells lysed by sonication; lysate clarified by centrifugation |
| mini-Gs purification | Ni2+ Sepharose FF affinity chromatography; TEV protease cleavage; negative Ni-NTA purification; SEC on Superdex-200 | Ni2+ Sepharose FF; Ni-NTA; Superdex-200 26/600 | 10 mM HEPES pH 7.5, 100 mM NaCl, 10% glycerol, 1 mM MgCl2, 1 uM GDP, 0.1 mM TCEP + -- | Typical yield 100 mg pure mini-Gs per litre of culture; concentrated to 100 mg/mL |
| Complex formation | A2AR and mini-Gs mixed in presence of NECA; complex stabilized by 3H-NECA binding assay and thermostability | -- | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.05% OG, 100 uM NECA + Octylthioglucoide (OG) | Complex thermostability measured in DDM, DM, and OG detergents; OG provided highest delta Tm (13.4 C) |

### Purification Workflow

*Source: doi/10.1016##j.str.2017.06.012*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Sf9 cell expression; membranes prepared in 40 mM Tris-HCl pH 7.6, 1 mM EDTA with protease inhibitors | -- | 40 mM Tris-HCl pH 7.6, 1 mM EDTA + -- | Membranes prepared from 2 L culture |
| Solubilization | Membranes solubilized with detergent in presence of 3 mM theophylline or caffeine during solubilization | -- | -- + DM | 3 mM xanthine ligand present during solubilization |
| Ni-NTA affinity chromatography | Ni-NTA purification with xanthine ligand present | Ni-NTA superflow cartridge | -- + DM | 1 mM xanthine ligand during purification |
| Size-exclusion chromatography | SEC in presence of xanthine ligand | -- | -- + DM | Final protein concentrated to 20-25 mg/mL |


## Crystallization

### doi/10.1038##NATURE18966

| Parameter | Value |
|---|---|
| Method | Vapor diffusion [crystallization](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | A2AR-mini-Gs complex in octylthioglucoide |
| Reservoir | -- |
| Temperature | -- |
| Growth time | Two crystals used for data collection |
| Cryoprotection | -- |
| Notes | A2AR in complex with engineered mini-Gs and agonist NECA, with GDP bound to mini-Gs. Crystallized in the detergent octylthioglucoide by vapour diffusion. Two datasets collected from two crystals, structure determined by molecular replacement and refined to 3.4 A resolution. Of the two A2AR-mini-Gs complexes per crystallographic asymmetric unit, the density in complex AC was better defined and used for all subsequent analyses.
 |

### doi/10.1016##j.bbrc.2023.149393

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) [crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) |
| Protein sample | A2AR-StaR2-b562RIL in complex with xanthine ligand |
| Temperature | -- |
| Growth time | Single crystal for each structure |
| Cryoprotection | -- |
| Notes | Four structures solved: theophylline (2.0 A, 1 crystal), caffeine (2.1 A, 1 crystal), PSB36 (2.8 A, 1 crystal, obtained by soaking theophylline crystals with PSB36). All in space group C2221.
 |

### doi/10.1016##j.str.2017.12.013

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | A2AAR-T4L D52N and S91A variants in complex with UK432097 |
| Lipid | Monoolein (40% protein + 54% monoolein + 6% cholesterol) |
| Protein-to-lipid ratio | 40:60 (w/w) |
| Temperature | 23 C |
| Growth time | Crystals appeared in ~1 hour, full size within one week |
| Cryoprotection | Flash frozen in liquid nitrogen |
| Notes | Two structures solved: A2AAR-D52N-UK432097 (PDB 5WF5, 2.6 A, 24 crystals) and A2AAR-S91A-UK432097 (PDB 5WF6, 2.9 A, 25 crystals). Both in space group P21. Solved by molecular replacement using A2AAR-ZM241385 (PDB 3EML) as search model. These structures revealed changes in the NPxxY activation motif and hydrogen bonding network near the allosteric sodium site.
 |


## Biological / Functional Insights

### A2AR-mini-Gs complex structure at 3.4 A resolution

The first structure of a GPCR bound to an engineered G protein, mini-Gs, at 3.4 A resolution. The interface between A2AR and mini-Gs spans 1,048 A^2 buried surface area, involving 20 receptor residues and 17 mini-Gs residues. The transition from active-intermediate state to G-protein-bound state is characterized by a 14 A shift of the cytoplasmic end of transmembrane helix 6 (H6) away from the receptor core, rotamer changes of Arg3.50, Tyr5.58 and Tyr7.53, and slight changes in H5 and H7 cytoplasmic ends. No substantial differences in the extracellular ligand binding pocket.

### GPCR-G-protein interface diversity and similarity

Superposition of A2AR-mini-Gs with beta2AR-Gs (PDB 3SN6) shows similar receptor architectures (r.m.s.d. 1.7 A over 1,239 atoms) but mini-Gs does not superimpose exactly on G alpha s (15 degree orientation difference). The interface differs in specific atoms involved in contacts, reflecting differences in amino acid sequences between A2AR and beta2AR. This highlights both diversity and similarity in G-protein coupling to GPCRs and hints at the potential complexity of the molecular basis for G-protein specificity.

### H6 outward bending mechanism in GPCR activation

Comparison of active-intermediate state (UK432097-bound A2AR) with G-protein-bound state reveals major rearrangements: H6 cytoplasmic end moves 14 A away from receptor core through outward bending with little rotation. The extent of H6 movement is dictated by van der Waals interactions between Lys6.29, Ala6.33, Leu6.37 in A2AR and Leu5.25 and C-terminus of mini-Gs. Tyr5.58 and Tyr7.53 adopt new rotamers to fill space previously occupied by Leu6.37 and Ile6.40. The Tyr7.53 shift allows Arg3.50 of the conserved DRY motif to adopt fully extended conformation, packing against Tyr391 H5.23 of mini-Gs alpha 5 helix.

### Conformational energy landscape differences between A2AR and beta-ARs

A2AR exhibits a different energy landscape to beta-adrenergic receptors. While betaAR agonist-bound structures are similar to inactive state, A2AR agonist-bound structures represent an active-intermediate state very similar to the fully active G-protein-bound state. This suggests that A2AR more readily samples active conformations even without G-protein binding, unlike beta2AR which requires G-protein stabilization to adopt the active state.

### Caffeine dual binding mode in A2AR

At 2.1 A resolution, caffeine occupies the orthosteric pocket in two orientations (caffeine A and B) at approximately 50:50 ratio. The two orientations are related by 180 degree rotation around the N1-C10 bond. In caffeine A, O13 forms hydrogen bond to N253(6.55) at 3.35 A. In caffeine B, O11 forms hydrogen bond to N253(6.55) at 2.9 A. Both orientations have O11 interacting with H278(7.43) and A81(3.29) through water molecules.

### Theophylline binding mode

Theophylline (1,3-dimethylxanthine) binds in the orthosteric pocket with the fused rings sandwiched between F168 and L249(6.51). The xanthine plane is slightly tilted and theophylline is not as deep in the pocket as PSB36 in A1R. O13 forms hydrogen bond to N253(6.55) at 2.9 A. O11 interacts with H278(7.43) and A81(3.29) through two water molecules.

### PSB36 binding in A2AR

PSB36 binds in A2AR with submicromolar affinity, higher than caffeine and theophylline but much lower than in A1R (0.7 nM). PSB36 sits slightly higher and rotated ~5 degrees compared to its position in A1R. The noradamantyl group prevents formation of the E169-H264 salt bridge. PSB36 forms two hydrogen bonds to N253(6.55) but is not located as deeply in the pocket as in A1R.

### M270(7.35) selectivity determinant

Methionine at position 7.35 in A2AR confers high affinity for A2AR-selective ligands. M270T substitution reduces A2AR selectivity for xanthine ligands. The bulky methionine creates unfavorable steric interactions with the C8 noradamantyl group of PSB36, reducing affinity relative to A1AR where T270 is present. Movement of TM7 into the binding pocket in A2AR brings M270 closer to the ligand.

### Y271(7.36) conformational changes

The side chain of Y271(7.36) changes conformation depending on bound ligand. With ZM241385, the phenol is held by water-mediated hydrogen bond to the exocyclic amine. Without this interaction (theophylline, caffeine, PSB36), the phenol ring moves toward the lipid bilayer (3 A difference). PSB36 binding also causes rearrangement of E169 side chain.

### D52N mutation enhances GPCR stability

The D52N mutation in the allosteric sodium binding site confers enhanced thermal stability to A2AR. Apo A2AAR-D52N showed a nearly 8 C increase in melting temperature compared to apo A2AAR. The mutation disrupts sodium-dependent G-protein signaling while maintaining ligand binding affinity. The D52N mutation is proposed as a general strategy for stabilizing class A GPCRs for crystallization and drug discovery.

### NPxxY motif structural rearrangement in D52N variant

Structural comparison of D52N-UK432097 with antagonist-bound and agonist-bound A2AR reveals key changes in the NPxxY motif in helix VII. The D52N mutation causes local conformational changes in the NPxxY motif that suggest coupling between the sodium site (D2.50) and the activation microswitch. New hydrogen bonds form between N52 and residues in helices II, III, and VII, altering the interhelical packing near the activation microswitch.

### Nucleoside antagonist LJ-4517 binding mechanism

The nucleoside antagonist LJ-4517 (compound 2) was co-crystallized with A2A-StaR2-bRIL (PDB 8CU7, 2.05 A) and A2A-StaR2-S277-bRIL (PDB 8CU6, 2.80 A). The C8-thiophene substitution converts an agonist scaffold into an antagonist by restricting receptor conformational rearrangements. The truncated ribose moiety only transiently contacts His278(7.43), unlike agonists that simultaneously engage both Ser277(7.42) and His278(7.43). This demonstrates that a single functional group can shift the ligand's mode of action from agonism to antagonism.


## Cross-References

- [LJ-4517 (Compound 2)](/xray-mp-wiki/reagents/ligands/lj-4517/) — Nucleoside antagonist co-crystallized with StaR2-bRIL (PDB 8CU7) and S277-bRIL (PDB 8CU6)
- [PSB36](/xray-mp-wiki/reagents/ligands/psb36/) — A1-selective xanthine antagonist that binds A2AR with submicromolar affinity (2.8 A structure)
- [ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/) — A2AR-selective xanthine antagonist; reference structure (PDB 5IU4/6WQA)
- [Human Adenosine A1 Receptor (A1AR)](/xray-mp-wiki/proteins/human-adenosine-a1-receptor-a1ar/) — Comparison structure for selectivity determinants
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification
- [HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid)](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in purification buffers for both A2AR and mini-Gs
- [NECA](/xray-mp-wiki/reagents/ligands/neca/) — Non-selective adenosine receptor agonist; bound in A2AR-mini-Gs complex (3.4 A structure)
- [Guanosine Diphosphate (GDP)](/xray-mp-wiki/reagents/ligands/gdp/) — Nucleotide bound to mini-Gs in A2AR-mini-Gs complex
