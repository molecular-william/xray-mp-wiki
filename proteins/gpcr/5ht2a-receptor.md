---
title: "Human 5-HT2A Receptor"
created: 2026-05-27
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-022-00796-6, doi/10.1016##j.cell.2016.12.033, doi/10.1038##s41594-018-0180-z, doi/10.1126##science.abl8615]
verified: false
---

# Human 5-HT2A Receptor

## Overview

The human [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin) 2A (5-HT2A) receptor is a class A GPCR and a major drug target for antipsychotics and hallucinogens. Crystal structures have been determined in complex with the second-generation antipsychotics [risperidone](/xray-mp-wiki/reagents/ligands/risperidone) (PDB 6A93, 3.0 A) and zotepine (PDB 6A94, 2.9 A), revealing the inactive state conformation and a unique side-extended cavity near the orthosteric binding site. Cryo-EM structures of the 5-HT2A receptor in complex with miniGo and the psychedelic agonists lisuride and methylgeromertrine have been determined, revealing the active-state conformation and G protein coupling interface. High-resolution X-ray structures of 5-HT2AR complexed with serotonin, psilocin, LSD, lisuride, lumateperone, and the β-arrestin-biased agonist IHCH-7086 (PDB 7WC4-7WC9) revealed a second binding mode (extended binding pocket, EBP) for serotonin and psilocin, and enabled the structure-based design of nonhallucinogenic psychedelic analogs with antidepressant-like activity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41594-018-0180-z | 6A93 | 3.0 A | C2 | Human 5-HT2A receptor with N-terminal (1-69) and C-terminal (404-471) deletions, ICL3 (Thr266-Met312) replaced with mbIIG fusion (modified apocytochrome b562 IIG), thermostability mutations S162K^3.39 and M164W^3.41. N-terminal HA signal sequence + [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag) + 10xHis tag + TEV protease recognition site. | [Risperidone](/xray-mp-wiki/reagents/ligands/risperidone) |
| doi/10.1038##s41594-018-0180-z | 6A94 | 2.9 A | C2 | Human 5-HT2A receptor with N-terminal (1-69) and C-terminal (404-471) deletions, ICL3 (Thr266-Met312) replaced with mbIIG fusion (modified apocytochrome b562 IIG), thermostability mutations S162K^3.39 and M164W^3.41. N-terminal HA signal sequence + [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag) + 10xHis tag + TEV protease recognition site. | Zotepine |
| doi/10.1038##s41594-022-00796-6 | 7UM4 |  |  | Human 5-HT2A receptor in complex with miniGo and lisuride (5-HTSAR-miniGo-Lisuride) | lisuride |
| doi/10.1038##s41594-022-00796-6 | 7UM4 |  |  | Human 5-HT2A receptor in complex with miniGo and methylgeromertrine (5-HTSAR-miniGo-Methylgeromertrine) | methylgeromertrine |
| doi/10.1038##s41594-022-00796-6 | 7UM4 |  |  | Human 5-HT2A receptor in complex with miniGo (apo-like state, CT designation) |  |
| doi/10.1126##science.abl8615 | 7WC4 | 3.0 A |  | Human 5-HT2AR in complex with serotonin | [Serotonin](/xray-mp-wiki/reagents/ligands/serotonin) |
| doi/10.1126##science.abl8615 | 7WC5 | 3.0 A |  | Human 5-HT2AR in complex with psilocin | Psilocin |
| doi/10.1126##science.abl8615 | 7WC6 | 2.6 A |  | Human 5-HT2AR in complex with LSD | [LSD](/xray-mp-wiki/reagents/ligands/lsd) |
| doi/10.1126##science.abl8615 | 7WC7 | 2.6 A |  | Human 5-HT2AR in complex with lisuride | Lisuride |
| doi/10.1126##science.abl8615 | 7WC8 |  |  | Human 5-HT2AR in complex with lumateperone | Lumateperone |
| doi/10.1126##science.abl8615 | 7WC9 |  |  | Human 5-HT2AR in complex with IHCH-7086 | IHCH-7086 |

## Expression and Purification

- **Expression system**: [Sf9 Cells](/xray-mp-wiki/methods/expression-systems/sf9-expression-system) (Bac-to-Bac Baculovirus Expression System)
- **Construct**: Human 5-HT2A receptor with N-terminal (1-69) and C-terminal (404-471) deletions, ICL3 (Thr266-Met312) replaced with mbIIG fusion, thermostability mutations S162K^3.39 and M164W^3.41
- **Notes**: Cloned into pFastBacI vector with HA signal sequence, FLAG tag, 10xHis tag, TEV protease recognition site. Sf9 cells cultured in PMSF-J1 medium with 2% FBS, infected at MOI of 2, harvested 48 h post-infection.

### Purification Workflow

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: 5-HT2A R-mbIIG with N/C-terminal truncations, thermostability mutations, and mbIIG fusion in ICL3
- **Tag info**: N-terminal HA signal + FLAG tag + 10xHis tag + TEV site

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Thawing and hypotonic lysis | -- | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 10 mM MgCl2, 20 mM KCl, EDTA-free protease inhibitor cocktail + -- | Thawed cell pellets disrupted in hypotonic buffer. Extensive washing by centrifugation. |
| High-salt wash | Centrifugation wash | -- | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 1 M NaCl, 10 mM MgCl2, 20 mM KCl, protease inhibitor + -- | Removes soluble and membrane-associated proteins |
| Solubilization | Detergent solubilization | -- | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 800 mM NaCl, 10% glycerol, protease inhibitor, 25 µM risperidone or zotepine + DDM (n-Dodecyl-beta-D-maltopyranoside) | Ligand pre-incubated with membranes before solubilization to stabilize the receptor |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [TALON](/xray-mp-wiki/reagents/additives/talon) IMAC resin | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 800 mM NaCl, 10% glycerol + DDM | C-terminal 10xHis tag used for affinity capture |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | SEC column | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 800 mM NaCl, 10% glycerol + DDM | Final purification step to obtain monodisperse 5-HT2A-R-mbIIG complex |


## Crystallization

### doi/10.1038##s41594-018-0180-z

| Parameter | Value |
|---|---|
| Method | [LCP Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) |
| Protein sample | 5-HT2A R-mbIIG-risperidone or 5-HT2A R-mbIIG-zotepine complex |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Temperature | 20 C |
| Notes | Structures solved by molecular replacement. Data collected at SPring-8 beamlines. Space group C2 for both complexes. |


## Biological / Functional Insights

### Side-extended cavity unique to 5-HT2A

Comparison of the 5-HT2A and 5-HT2C receptor structures reveals a unique side-extended cavity near the orthosteric binding site in 5-HT2A. This cavity is formed by residues Phe234^5.38, Phe213^4.63, and the rotameric conformation of Phe234^5.38, which differs from the equivalent residues in 5-HT2B and 5-HT2C. Docking studies suggest that the 5-HT2A-selective antagonist pimavanserin binds to this side-extended cavity, with the fluorobenzyl ring engaging Trp336^6.48 through edge-to-face pi interactions.

### Antipsychotics stabilize inactive conformation via PIF motif

Risperidone and zotepine effectively stabilize the inactive conformation of 5-HT2A by forming direct contacts with residues at the bottom of the ligand-binding pocket, particularly those in the PIF motif (Ile163^3.40, Phe332^6.44, Trp336^6.48). Both antipsychotics make direct contacts with Phe332^6.44 and are sandwiched between residues at positions 5.46 and 7.39. Mutation of these residues to alanine or leucine substantially decreases or abolishes inverse agonist activity, confirming their importance in stabilizing the inactive state.

### Conformational differences among 5-HT2 receptors

Among aminergic receptor structures, 5-HT2A is most similar to 5-HT2C and less similar to 5-HT2B. The 5-HT2B receptor exhibits outward shifts of TM5 and TM6 and an inward shift of TM3 compared with 5-HT2A, similar to differences observed between inactive and agonist-bound 5-HT2C structures. The extracellular loop 2 (ECL2) of 5-HT2B contains six additional residues and one turn shorter TM4 compared to 5-HT2A, resulting in a unique ECL2 conformation that influences the ligand-binding pocket architecture.

### Comparison with D2R binding site

Comparison of 5-HT2A and D2 dopamine receptor structures reveals that while risperidone occupies a similar position in both receptors (fluorobenzisoxazol ring in the bottom hydrophobic cleft), significant differences exist around extracellular loops 1 and 2 (ECL1 and ECL2). The structure of the ligand-binding pocket at these regions differs substantially between 5-HT2A and D2R, providing a structural basis for developing receptor-selective antipsychotics.

### LSD binding mode in 5-HT2A homology model

Homology modeling of 5-HT2A based on 5-HT2B-R/LSD crystal structure shows that [LSD (Lysergic Acid Diethylamide)](/xray-mp-wiki/reagents/ligands/lsd) binding mode is recapitulated in the 5-HT2A receptor. Key interactions include a salt bridge between the basic amine and D138^3.32, and a hydrogen bond between the indole nitrogen and S242^5.42 (versus G221^5.42 in 5-HT2B). Docking of LSD and its derivatives (SSAz, RRAz, LSA) into the 5-HT2A model confirms that the crystallographic 5-HT2B binding mode is conserved. The rigidified substituent of SSAz adopts an almost identical orientation to LSD in receptor-bound form, while RRAz and LSA show different orientations with reduced receptor engagement.

### Extremely slow LSD dissociation kinetics at 5-HT2A

LSD dissociates exceptionally slowly from 5-HT2A receptors with a residence time of approximately 221 minutes at 37 degrees C. The EL2 lid residue L229 at position EL2 (equivalent to L209^EL2 in 5-HT2B) forms a structural latch. Mutation of L229A^EL2 decreases LSD residence time to 50 minutes, a 4.4-fold acceleration. This accelerated kinetics selectively disrupts [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin)2 recruitment while leaving Gq function intact, mirroring the phenotype observed at 5-HT2B receptors.

### Time-dependent augmentation of signaling

At wild-type 5-HT2A receptors, LSD potency and efficacy for [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin)2 recruitment increase with longer compound stimulation, exhibiting time-dependent augmentation. This is abrogated by the L229A^EL2 mutation, which results in weak LSD potency and efficacy that does not change over time. Gq-mediated IP accumulation shows time-dependent augmentation at wild-type but is not substantially affected by the EL2 mutation. This indicates that EL2-mediated residence time selectively controls the time-dependency of beta-arrestin2 translocation.

### Lipid activation of 5-HT2AR via side-extended pocket (SEP)

Crystal structures revealed that monoolein binds to a side-extended pocket (SEP) in 5-HT2AR, formed by a conserved glycine at position G238^5.42. This SEP is distinct from the orthosteric binding pocket (OBP) and extended binding pocket (EBP). Monoolein acts as a G protein-mediated calcium flux partial agonist at 5-HT2AR. The endogenous fatty acid amide oleamide, OEA, and 2OG also activate 5-HT2AR-mediated signaling via the SEP. Introducing a G238^5.42S substitution abolished the agonist activity of lipids but not of serotonin. Lipids did not induce robust G protein signaling at 5-HT2BR or 5-HT2CR, where the glycine is not conserved. These results provide a structural basis for the long-standing observation that 5-HT2AR signaling is modulated by lipids.

### Second binding mode of serotonin and psilocin at the EBP

Unlike previous docking results, crystal structures showed that the indole core of serotonin or psilocin fits into a narrow cleft previously described as the extended binding pocket (EBP), lined mainly by hydrophobic side chains from residues in EL2 and transmembrane helices TM3, TM6, and TM7. Both ligands form a salt bridge between D155^3.32 and the terminal basic nitrogen as well as an extra hydrogen bond between N352^6.55 and the hydroxyl group on the indole core. Mutagenesis of EBP residues (W151^3.28, L362^7.35) substantially decreased or abolished agonist activity. The L362^7.35F substitution did not affect the potency of Gq agonism, but abolished psilocin and lisuride β-arrestin association, indicating that ligand recognition in the EBP, specifically at L362^7.35, affects ligand bias.

### Structure-based design of nonhallucinogenic psychedelic analogs

Targeting the EBP enabled identification of β-arrestin-biased ligands at 5-HT2AR. After analyzing available 5-HT2AR 4-fluorophenyl antipsychotics, three rigid moieties were identified for binding the EBP: IHCH-7113 (moiety from lumateperone), IHCH-7117 (from spiperone), and IHCH-7125 (from pimozide and benperidol). IHCH-7113 was a 5-HT2AR agonist (Ki = 758.58 nM) with weak preference for β-arrestin2 over Gq signaling (bias factor = 1.52). Further optimization yielded IHCH-7079 and IHCH-7086, which showed β-arrestin2 partial agonist activity without Gq dissociation activity. Unlike IHCH-7113 and hallucinogens, IHCH-7079 and IHCH-7086 failed to produce any head-twitch response (HTR) in mice, even at doses up to 10 mg/kg. The designed compounds also blocked LSD-induced HTR and showed antidepressant-like effects in both ARS-induced and corticosterone-induced depression models, comparable to LSD microdosing.

### Hallucinogenic effect is not required for antidepressant-like activity

Acute administration of LSD at low doses (0.0075-0.015 mg/kg ip) significantly attenuated acute restraint stress (ARS)-induced depression-like freezing behavior in both wild-type and 5-HT2AR Y370^7.43W mutant mice, without inducing HTR. These data suggest that the hallucinogenic effect may not be required for the antidepressant-like effect of LSD, consistent with clinical trials of microdosing. The nonhallucinogenic analogs lisuride, IHCH-7079, and IHCH-7086 also showed antidepressant-like effects in both ARS and corticosterone-induced depression models, with effects blocked by the 5-HT2AR-selective antagonist MDL100907.


## Cross-References

- [Risperidone](/xray-mp-wiki/reagents/ligands/risperidone) — Co-crystallized antipsychotic in PDB 6A93
- [LSD (Lysergic Acid Diethylamide)](/xray-mp-wiki/reagents/ligands/lsd) — Primary ligand studied in earlier work; extremely slow off-rate at 5-HT2A
- [Human 5-HT2B Receptor](/xray-mp-wiki/proteins/gpcr/5ht2b-receptor/) — Related 5-HT2 family member; template for homology model
- [Human 5-HT2C Receptor](/xray-mp-wiki/proteins/gpcr/5ht2c-receptor/) — Related 5-HT2 family member; most similar structure to 5-HT2A
- [GPCR Inactive Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-inactive-conformation/) — Risperidone and zotepine stabilize the inactive state of 5-HT2A
- [Ergotamine](/xray-mp-wiki/reagents/ligands/ergotamine) — Related ergoline ligand compared in functional assays
- [bRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril) — mbIIG fusion (BRIL variant) used for crystallization
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) — Crystallization method used for both structures
- [Nonhallucinogenic Psychedelic Analog Design](/xray-mp-wiki/concepts/construct-design/nonhallucinogenic-psychedelic-analog-design/) — Structure-based design strategy leveraging the EBP for biased agonism
- [Lipid Activation of 5-HT2A Receptor](/xray-mp-wiki/concepts/signaling-receptors/lipid-activation-5ht2a-receptor/) — Monoolein and oleamide activate 5-HT2AR via the SEP pocket
