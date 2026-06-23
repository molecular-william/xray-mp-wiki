---
title: Angiotensin II Type 1 Receptor
created: 2026-05-27
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2015.04.011, doi/10.1016##j.cell.2018.12.006, doi/10.1016##j.str.2019.12.003, doi/10.1038##nature22035, doi/10.1074##jbc.M115.689000, doi/10.1126##science.aay9813]
verified: false
---

# Angiotensin II Type 1 Receptor

## Overview

The [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) type 1 receptor (AT1R) is a class A G protein-coupled receptor that serves as the primary regulator of blood pressure maintenance. AT1R mediates most of the physiological effects of [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/), the endogenous agonist, including vasoconstriction, aldosterone secretion, and sodium retention. The first crystal structure of AT1R was determined in complex with the inverse agonist [olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) (Benicar) at 2.8 A resolution by conventional synchrotron cryo-crystallography (Zhang et al., 2015, JBC), revealing the molecular basis for ligand recognition and functional selectivity. A room temperature structure in complex with the antagonist [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/) was subsequently solved at 2.9 A using serial femtosecond crystallography. Dysregulation of AT1R signaling contributes to hypertension, cardiac hypertrophy, heart failure, and renal disease. AT1R is a major therapeutic target, with angiotensin receptor blockers (ARBs, or sartans) being among the most widely prescribed anti-hypertensive drugs worldwide.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1074##jbc.M115.689000 | 4ZUD | 2.8 | P32 | BRIL-AT1R fusion; N-terminal truncations: Met1, Thr7-Asp16; C-terminal truncation: residues 320-359 (4 residues shorter than construct used for 4YAY); HA signal sequence, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10x [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (cleaved), TEV cleavage site | [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) |
| doi/10.1016##j.cell.2015.04.011 | 4YAY | 2.9 |  | BRIL-AT1R fusion; N-terminal truncations: residue 1, residues 7-16; C-terminal [Protein Truncation for Crystallography](/xray-mp-wiki/concepts/truncation/): residues 320-359; HA signal sequence, FLAG tag, 10x His tag (cleaved), TEV cleavage site | [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/) |
| doi/10.1016##j.cell.2018.12.006 | 6DO1 | 2.9 | P21212 | AT1R with BRIL inserted into ICL3 (residues 226-227); I320 stop codon; N-terminal HA signal sequence, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/); no N-terminal deletion | S1I8 (Sarcosine1,Isoleucine8-[Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/)) |
| doi/10.1126##science.aay9813 | 6OS0 | 2.9 |  | AT1R-AT110i1 nanobody complex | Angiotensin II (AngII) |
| doi/10.1126##science.aay9813 | 6OS1 | 2.9 |  | AT1R-AT110i1 nanobody complex | TRV023 |
| doi/10.1126##science.aay9813 | 6OS2 | 2.9 |  | AT1R-AT110i1 nanobody complex | TRV026 |

## Expression and Purification

- **Expression system**: Sf9 insect cells (Bac-to-Bac [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: BRIL-AT1R chimera with N-terminal HA signal, FLAG, [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tags, TEV site
- **Notes**: AT1R gene sequence optimized for insect cell expression. [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (apocytochrome b562RIL, M7W, H102I, R106L) fused to N-terminus. Truncations: Met1, Thr7-Asp16, residues 320-359 after helix VIII. Full glycosylation retained (no PNGase F treatment).


### Purification Workflow

*Source: doi/10.1074##jbc.M115.689000*

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)
- **Expression construct**: [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)-AT1R chimera with HA/FLAG/His tags (olmesartan-bound)
- **Tag info**: [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (N-terminal, cleaved by TEV)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell infection | [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) infection |  |  | 2-3 x 10^6 cells/mL infected with [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) at 27C, harvested at 48 hr |
| Membrane preparation | Hypotonic and high osmotic buffer washes |  | Hypotonic: 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl; High osmotic: 10 mM HEPES pH 7.5, 1.0 M NaCl, 10 mM MgCl2, 20 mM KCl | Added EDTA-free protease inhibitor cocktail; membranes incubated with 100 uM [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) for 1 h at 4C before solubilization |
| Solubilization | Detergent solubilization |  | 50 mM HEPES pH 7.5, 500 mM NaCl + 1% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% CHS | BRIL-AT1R in complex with [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) solubilized from membranes; buffer contained 20 uM [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) IMAC | 50 mM HEPES pH 7.5, 500 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.05% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) + 0.01% CHS | [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) capture; buffer contained [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) 100 uM; wash with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), elute with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag cleavage and deglycosylation | Protease and glycosidase treatment |  | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 0.02% DDM, 0.004% CHS + 0.02% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) + 0.004% CHS | Overnight treatment with His-tagged [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) and PNGase F to cleave N-terminal tags and glycosylation sites |
| Concentration | Centrifugal concentration |  |  | Concentrated to 30 mg/ml with [Vivaspin](/xray-mp-wiki/reagents/additives/vivaspin/) 100 kDa cutoff concentrator; monodispersity tested by analytical [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) |

**Final sample**: 30 mg/ml
**Purity**: Tested by analytical [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)

### Purification Workflow

*Source: doi/10.1016##j.cell.2015.04.011*

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)
- **Expression construct**: [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)-AT1R chimera with HA/FLAG/His tags
- **Tag info**: FLAG, [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (N-terminal, cleaved by TEV)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell infection | [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) infection |  |  | 2-3 x 10^6 cells/mL infected with [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) at 27C, harvested at 48 hr |
| Membrane isolation | Cell lysis and membrane preparation |  |  | Isolated membranes from Sf9 cells |
| Solubilization | Detergent solubilization |  | 1% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% CHS | BRIL-AT1R in complex with [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/) solubilized from membranes |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) IMAC | 1% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% CHS | [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) capture |
| Desalting | Size exclusion (column) | PD MiniTrap G-25 |  | Remove [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag cleavage | Protease cleavage |  |  | Overnight treatment with His-tagged [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) to cleave N-terminal FLAG/His |
| Tag removal | [Immobilized Metal Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) flow-through | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) IMAC |  | Cleaved FLAG/His tags and [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) removed by TALON resin |

**Final sample**: 30 mg/ml
**Purity**: Tested by analytical [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)

### Purification Workflow

*Source: doi/10.1016##j.cell.2018.12.006*

- **Expression system**: Expi293F mammalian cells (tetracycline-inducible)
- **Expression construct**: AT1R with N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), BRIL inserted into ICL3 (residues 226-227), I320 stop codon
- **Tag info**: N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Mammalian transient expression |  | Expi293F expression media | Tetracycline-inducible Expi293F cells; induced with 4 mg/mL doxycycline, 5 mM [Sodium Butyrate](/xray-mp-wiki/reagents/additives/sodium-butyrate/), 1 uM losartan |
| Cell lysis | Hypotonic lysis |  | 10 mM Tris pH 7.4, 2 mM EDTA, 10 mM MgCl2, benzonase, [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine/), leupeptin, 5 uM losartan | Frozen cell pellets lysed under hypotonic conditions at room temperature |
| Membrane isolation | Centrifugation |  |  | 30,000 x g for 15 min |
| Solubilization | Detergent solubilization |  | 20 mM HEPES pH 7.4, 500 mM NaCl, 10 mM MgCl2, benzonase, [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine/), leupeptin, 5 uM losartan + 0.5% MNG + 0.05% [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | 2 h stirring at room temperature then 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) affinity | [M1 FLAG Affinity Resin](/xray-mp-wiki/reagents/protein-tags/m1-flag-resin/) | 20 mM [HEPES (HEPES Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 500 mM NaCl, 0.01% MNG, 0.01% CHS, 2 mM CaCl2 + 0.01% MNG + 0.01% [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | FLAG-tagged AT1R captured on [M1 FLAG Affinity Resin](/xray-mp-wiki/reagents/protein-tags/m1-flag-resin/) |
| Elution | [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) peptide elution | [M1 FLAG Affinity Resin](/xray-mp-wiki/reagents/protein-tags/m1-flag-resin/) | 20 mM [HEPES (HEPES Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 500 mM NaCl, 0.01% MNG, 0.01% CHS, 0.2 mg/mL FLAG peptide, 5 mM EDTA + 0.01% MNG + 0.01% [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | AT1R eluted with [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) peptide |
| [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM [HEPES (HEPES Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 100 mM NaCl, 0.01% MNG, 0.001% CHS (HNM buffer) + 0.01% MNG + 0.001% [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Monomeric [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) isolated; for crystallography, treated with EndoH for 90 min prior to SEC |

**Final sample**: 30 uM
**Purity**: Monomeric peak by [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)


## Crystallization

### doi/10.1074##jbc.M115.689000

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase ([Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) |
| Protein sample | [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)-AT1R + [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/), 30 mg/ml |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) supplemented with 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) |
| Protein-to-lipid ratio | 1:1 |
| Temperature | 20 |
| Growth time | Crystals appeared and grew over several weeks |
| Notes | Crystals harvested from LCP using micromounts; cryo-cooled at 100K. Data collected at GM/CA@APS (23ID-D), Advanced Photon Source, using 10 um minibeam at 1.0330 A wavelength, 1 s exposure, 1.0 oscillation. Detector: Pilatus3 6M. Space group P32, merohedral twinning (twin law h,k,l and k,h,-l) refined with phenix.xtriage and Refmac5. Single crystal of 70x70x15 um3, 4 non-overlapping spots used. |

### doi/10.1016##j.cell.2015.04.011

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase ([Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) |
| Protein sample | BRIL-AT1R + [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/), 30 mg/ml |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | 1:1 |
| Temperature | 20 |
| Growth time | 2-4 weeks |

### doi/10.1016##j.cell.2018.12.006

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase ([Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) |
| Protein sample | AT1R-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)(ICL3) + S1I8 + Nb.AT110i1, 30 uM |
| Lipid | 10:1 monoolein:[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) |
| Protein-to-lipid ratio | 1.5:1 by mass |
| Temperature | 20 |
| Growth time | 6-11 days |

### doi/10.1126##science.aay9813

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | AT1R-AT110i1 nanobody complex + AngII, TRV023, or TRV026 |
| Lipid | Monoolein |
| Notes | Crystal structures of AT1R bound to three ligands with divergent bias profiles. Data collected at APS GM/CA beamlines. Structures deposited as PDB 6OS0 (AngII), 6OS1 (TRV023), 6OS2 (TRV026). |


## Biological / Functional Insights

### Olmesartan binding mode and conserved ARB recognition

The AT1R-[Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) structure (PDB 4ZUD, 2.8 A) confirmed the binding mode of ARBs. [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) is anchored by three critical residues: Tyr35^1.39, Trp84^2.60, and Arg167^ECL2, which form hydrogen bonds, salt bridges, and pi-pi interactions with the biphenyl-tetrazole scaffold. Comparison with the [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/)-bound structure (PDB 4YAY) showed RMSD of 0.85 A over 92% of Calpha atoms, supporting a conserved binding mode for different ARBs. The Lys199^5.42 side chain was ordered in the cryo-cooled structure but did not directly contact [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/).

### ZD7155 binding pocket architecture

[ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/) binds in a prominent ligand-binding pocket formed by residues from helices
I, II, III, VII, and ECL2. Key interactions: Arg167^ECL2 forms an extensive network
with the acidic tetrazole and naphthyridin-2-one moieties; Tyr35^1.39 hydrogen-bonds
with the naphthyridin-2-one; Trp84^2.60 forms a pi-pi interaction with the
naphthyridin-2-one. Mutagenesis confirmed that Arg167^ECL2A, Tyr35^1.39A, and
Trp84^2.60A all abolish peptide and non-peptide ligand binding.

### Functional selectivity of olmesartan derivatives

Modifications of the [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) scaffold yield ligands with distinct pharmacological properties. R781253 (additional 4-hydroxybenzyl group) retains inverse agonism. R239470 (carbamoyl group replacing carboxyl) is a neutral antagonist. R794847 (both modifications) is a weak partial agonist. Docking simulations predicted that the 4-hydroxybenzyl groups of R781253 and R794847 extend to a sub-pocket formed by Leu112^3.36, Lys199^5.42, Asn200^5.43, Trp253^6.48, His256^6.51, Gln257^6.52, and Thr260^6.55. Trp253^6.48 (toggle switch) was identified as a key determinant of functional selectivity.

### Sodium binding site

A conserved allosteric sodium-binding site is observed in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/), structurally
superimposable with the sodium pocket in the delta-opioid receptor (PDB 4N6H).
The pocket includes Asp74^2.50, Asn111^3.35, Asn295^7.46, Trp253^6.48, and
Asn298^7.49. Asn111^3.35 and Asn295^7.46 form two intramolecular hydrogen bonds
stabilizing the inactive conformation.

### Allosteric sodium modulation of peptide ligand binding

The Asn111^3.35Ala sodium pocket mutant showed ~300-fold higher affinity for [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) in the absence of sodium ions compared to physiological Na+ concentration. This effect was absent for the beta-arrestin biased agonist TRV120027, suggesting different mechanisms for AT1R modulation by its natural ligand and biased ligands. The sodium ion may allosterically stabilize the inactive conformation of AT1R.

### ECL2 as autoantibody epitope

ECL2 of [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) serves as an epitope for harmful agonistic autoantibodies in
preeclampsia and malignant hypertension. The atomic details of ECL2 and the
extracellular ligand-binding region provide guidance for designing antigens against
these autoantibodies.

### Activation mechanism

The inactive conformation is stabilized by the Asn111^3.35-Asn295^7.46 hydrogen
bond network. Binding of [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) disrupts this interaction, allowing
Asn295^7.46 to interact with Asp74^2.50. The conserved D(E)RY motif (helix III)
and NPxxY motif (helix VII) are present. The ionic lock between Arg^3.50 and
Asp/Glu^6.30 is not possible in AT1R due to lack of acidic residue at 6.30.
Helix VIII angles away from the membrane, resembling CCR5 orientation.

### Beta-arrestin signaling

G protein-independent [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin/) mediated signaling by AT1R confers
cardio-protective benefits. Thr336Pro and Pro341His (in the C-terminal tail not
included in the crystallized construct) affect GPCR kinase-dependent phosphorylation,
necessary for [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin/) recruitment.

### Active-state conformational changes

The active-state AT1R (PDB 6DO1) shows an 11 angstrom outward displacement of TM6,
rotation of TM5 away from the transducer binding pocket, and inward rotation of TM7.
ICL2 reorganizes to form a short alpha helix. Helix 8 repositions from a bent
conformation away from the membrane to a conventional position parallel to the
membrane near the TM1-TM7 interface. Y302^7.53 of the [NPxxY Motif](/xray-mp-wiki/concepts/npxxy-motif/) rotates 10
angstroms inward to hydrogen bond with Y215^5.58 in TM5.

### Peptide binding mode

[S1I8 Peptide](/xray-mp-wiki/reagents/ligands/s1i8/) binds in an extended conformation with N terminus facing the solvent and C
terminus buried deep in the receptor core. The peptide forms a half-beta-barrel
with the receptor N terminus and ECL2 beta-hairpin. Key interactions: H183^ECL2
hydrogen bonds with the peptide N terminus; W84^2.60, V108^3.32, L112^3.36, and
I288^7.38 interact with P7 and I8 of [S1I8 Peptide](/xray-mp-wiki/reagents/ligands/s1i8/); R2 of the peptide engages D281^7.32
and D263^6.58; the terminal carboxylate interacts with K199^5.42.

### Phenylalanine ratchet mechanism

[Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) activation involves a phenylalanine ratchet between TMs 5 and 6: I8 of S1I8
forces W253^6.48 and Y292^7.43 downward, causing F249^6.44 and F250^6.45 to ratchet
past F208^5.51. This creates a void filled by N295^7.46 moving inward, breaking the
N111^3.35-N295^7.46 hydrogen bond present in the inactive structure. This mechanism
diverges from other GPCRs and explains the diversity of allosteric mechanisms among
GPCRs.

### Biased agonism and C-terminal residue 8

The C-terminal residue 8 of AngII determines signaling bias. Ile8 (S1I8) produces
partial Gq agonism; Phe8 (AngII) produces full Gq agonism but the phenyl ring
slightly exceeds the cavity size shaped by TM3. Smaller residues or deletions at
position 8 produce [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin/)-biased ligands. The I8 side chain fits closely
into a TM3-shaped cavity, and the cavity size relative to residue 8 side chain
determines the conformational changes propagated through the receptor.

### Molecular recognition paradigm for ARBs

Docking simulations and mutagenesis of multiple ARBs (candesartan, telmisartan, valsartan, losartan, eprosartan) revealed a molecular recognition paradigm: the biphenyl-tetrazole scaffold employs three critical residues Arg167^ECL2, Trp84^2.60, and Tyr35^1.39, but relative binding energy contributions vary per ARB. Derivative moieties extend to additional sub-pockets, allowing wobbling of the core structure. Naturally occurring SNPs in the AGTR1 gene (Leu48^1.52Val, Ala163^4.60Thr, Leu222^5.65Val, Ala244^6.39Ser, Thr282^7.33Met, Cys289^7.40Trp) near the orthosteric pocket may affect ARB binding and efficacy in humans.

### AngII induces distinct active conformations of AT1R

Crystal structures of AT1R bound to angiotensin II (AngII), TRV023, and TRV026 reveal that AngII promotes more substantial rearrangements at the bottom of the ligand-binding pocket and in a key polar network in the receptor core. The AngII F8 residue is conformationally heterogeneous with high B-factors, while TRV026 and TRV023 show clear density for all residues. TM3 rotates in the AngII-bound structure, moving L112^3.36 past W253^6.48 and repositioning N111^3.35 outside the receptor core.

### Bipartite activation mechanism for biased signaling

The AT1R contains a divergent sodium-binding site polar core. Substitution of the highly conserved S^7.46 with N295^7.46 disrupts the sodium coordination sphere, replacing sodium with a hydrogen bond between N295^7.46 and N111^3.35. This creates a bipartite activation mechanism: N295^7.46 rearrangement is sufficient for beta-arrestin coupling, while N111^3.35 flipping is essential for Gq signaling. This predisposes AT1R to biased signaling.

### Structural basis of beta-arrestin-biased agonism

Beta-arrestin-biased ligands (TRV023, TRV026) trigger TM6 outward rotation and N295^7.46 conformational changes, which are sufficient for beta-arrestin coupling. However, they fail to induce the N111^3.35 outward movement that is essential for Gq signaling. This provides a structural mechanism for biased agonism at AT1R, where the partial or beta-arrestin-biased peptide agonists activate only a subset of the full conformational changes induced by AngII.

### Divergent sodium-binding motif in GPCRs and biased signaling

Deviations from the conserved sodium-binding motif are enriched in peptide- and protein-binding family A GPCRs related to AT1R. Only 3 out of 22 chemokine receptors possess all conserved residues for tight sodium binding. The chemokine receptor family contains atypical receptors that signal through beta-arrestins without G proteins, and endogenous chemokines function as biased ligands at many chemokine receptors. Substitutions in and around the sodium-binding site can bias receptor signaling.


## Cross-References

- [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/) — Primary ligand bound in PDB 4YAY structure
- [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) — Endogenous agonist of [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [S1I8](/xray-mp-wiki/reagents/ligands/s1i8/) — Partial agonist peptide used in active-state PDB 6DO1 crystallization
- [Nb.AT110i1 Synthetic Nanobody](/xray-mp-wiki/reagents/antibodies/nb-at110i1/) — Conformation-specific [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) stabilizing active-state AT1R (PDB 6DO1)
- [Lauryl Maltose Neopentyl Glycol (MNG)](/xray-mp-wiki/reagents/detergents/mng/) — Detergent used for [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) solubilization and purification in PDB 6DO1
- [Losartan](/xray-mp-wiki/reagents/ligands/losartan/) — ARB used for [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) expression stabilization and comparison with peptide ligands
- [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) — Inverse agonist ARB bound in PDB 4ZUD structure; used for functional selectivity studies
- [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) — Thermostabilization fusion partner inserted into [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) ICL3 for PDB 6DO1
- [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) — Close homolog with distinct signaling; AT2R structure reveals helix 8 canonical conformation upon [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) binding
- [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [NPxxY Motif](/xray-mp-wiki/concepts/npxxy-motif/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [Immobilized Metal Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [M1 FLAG Affinity Resin](/xray-mp-wiki/reagents/protein-tags/m1-flag-resin/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [PEG 300](/xray-mp-wiki/reagents/additives/peg-300/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
