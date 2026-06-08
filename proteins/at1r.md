---
title: Angiotensin II Type 1 Receptor
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2015.04.011, doi/10.1016##j.cell.2018.12.006, doi/10.1016##j.str.2019.12.003, doi/10.1038##nature22035]
verified: false
---

# Angiotensin II Type 1 Receptor

## Overview

The angiotensin II type 1 receptor (AT1R) is a class A G protein-coupled receptor that serves as the primary regulator of blood pressure maintenance. AT1R mediates most of the physiological effects of angiotensin II, the endogenous agonist, including vasoconstriction, aldosterone secretion, and sodium retention. Dysregulation of AT1R signaling contributes to hypertension, cardiac hypertrophy, heart failure, and renal disease. AT1R is a major therapeutic target, with angiotensin receptor blockers (ARBs, or sartans) being among the most widely prescribed anti-hypertensive drugs worldwide.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2015.04.011 | 4YAY | 2.9 |  | BRIL-AT1R fusion; N-terminal truncations: residue 1, residues 7-16; C-terminal truncation: residues 320-359; HA signal sequence, FLAG tag, 10x His tag (cleaved), TEV cleavage site | ZD7155 |
| doi/10.1016##j.cell.2018.12.006 | 6DO1 | 2.9 | P21212 | AT1R with BRIL inserted into ICL3 (residues 226-227); I320 stop codon; N-terminal HA signal sequence, FLAG tag; no N-terminal deletion | S1I8 (Sarcosine1,Isoleucine8-Angiotensin II) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus expression system)
- **Construct**: BRIL-AT1R chimera with N-terminal HA signal, FLAG, 10x His tags, TEV site
- **Notes**: AT1R gene sequence optimized for insect cell expression. BRIL (apocytochrome b562RIL, M7W, H102I, R106L) fused to N-terminus. Truncations: Met1, Thr7-Asp16, residues 320-359 after helix VIII. Full glycosylation retained (no PNGase F treatment).


### Purification Workflow

*Source: doi/10.1016##j.cell.2015.04.011*

- **Expression system**: Sf9 insect cells
- **Expression construct**: BRIL-AT1R chimera with HA/FLAG/His tags
- **Tag info**: FLAG, 10x His (N-terminal, cleaved by TEV)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell infection | Baculovirus infection |  |  | 2-3 x 10^6 cells/mL infected with baculovirus at 27C, harvested at 48 hr |
| Membrane isolation | Cell lysis and membrane preparation |  |  | Isolated membranes from Sf9 cells |
| Solubilization | Detergent solubilization |  | 1% DDM + 0.2% CHS | BRIL-AT1R in complex with ZD7155 solubilized from membranes |
| Affinity chromatography | Metal affinity chromatography | TALON IMAC | 1% DDM + 0.2% CHS | His-tag capture |
| Desalting | Size exclusion (column) | PD MiniTrap G-25 |  | Remove imidazole |
| Tag cleavage | Protease cleavage |  |  | Overnight treatment with His-tagged TEV protease to cleave N-terminal FLAG/His |
| Tag removal | IMAC flow-through | TALON IMAC |  | Cleaved FLAG/His tags and TEV protease removed by TALON resin |

**Final sample**: 30 mg/ml
**Purity**: Tested by analytical SEC

### Purification Workflow

*Source: doi/10.1016##j.cell.2018.12.006*

- **Expression system**: Expi293F mammalian cells (tetracycline-inducible)
- **Expression construct**: AT1R with N-terminal HA signal, FLAG tag, BRIL inserted into ICL3 (residues 226-227), I320 stop codon
- **Tag info**: N-terminal HA signal, FLAG tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Mammalian transient expression |  | Expi293F expression media | Tetracycline-inducible Expi293F cells; induced with 4 mg/mL doxycycline, 5 mM sodium butyrate, 1 uM losartan |
| Cell lysis | Hypotonic lysis |  | 10 mM Tris pH 7.4, 2 mM EDTA, 10 mM MgCl2, benzonase, benzamidine, leupeptin, 5 uM losartan | Frozen cell pellets lysed under hypotonic conditions at room temperature |
| Membrane isolation | Centrifugation |  |  | 30,000 x g for 15 min |
| Solubilization | Detergent solubilization |  | 20 mM HEPES pH 7.4, 500 mM NaCl, 10 mM MgCl2, benzonase, benzamidine, leupeptin, 5 uM losartan + 0.5% MNG + 0.05% CHS | 2 h stirring at room temperature then 4 C |
| Affinity chromatography | FLAG affinity | M1-FLAG resin | 20 mM HEPES pH 7.4, 500 mM NaCl, 0.01% MNG, 0.01% CHS, 2 mM CaCl2 + 0.01% MNG + 0.01% CHS | FLAG-tagged AT1R captured on M1-FLAG resin |
| Elution | FLAG peptide elution | M1-FLAG resin | 20 mM HEPES pH 7.4, 500 mM NaCl, 0.01% MNG, 0.01% CHS, 0.2 mg/mL FLAG peptide, 5 mM EDTA + 0.01% MNG + 0.01% CHS | AT1R eluted with FLAG peptide |
| SEC | Size exclusion chromatography | Superdex 200 Increase | 20 mM HEPES pH 7.4, 100 mM NaCl, 0.01% MNG, 0.001% CHS (HNM buffer) + 0.01% MNG + 0.001% CHS | Monomeric AT1R isolated; for crystallography, treated with EndoH for 90 min prior to SEC |

**Final sample**: 30 uM
**Purity**: Monomeric peak by SEC


## Crystallization

### doi/10.1016##j.cell.2015.04.011

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | BRIL-AT1R + ZD7155, 30 mg/ml |
| Lipid | monoolein |
| Protein-to-lipid ratio | 1:1 |
| Temperature | 20 |
| Growth time | 2-4 weeks |

### doi/10.1016##j.cell.2018.12.006

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | AT1R-BRIL(ICL3) + S1I8 + Nb.AT110i1, 30 uM |
| Lipid | 10:1 monoolein:cholesterol |
| Protein-to-lipid ratio | 1.5:1 by mass |
| Temperature | 20 |
| Growth time | 6-11 days |


## Biological / Functional Insights

### ZD7155 binding pocket architecture

ZD7155 binds in a prominent ligand-binding pocket formed by residues from helices
I, II, III, VII, and ECL2. Key interactions: Arg167^ECL2 forms an extensive network
with the acidic tetrazole and naphthyridin-2-one moieties; Tyr35^1.39 hydrogen-bonds
with the naphthyridin-2-one; Trp84^2.60 forms a pi-pi interaction with the
naphthyridin-2-one. Mutagenesis confirmed that Arg167^ECL2A, Tyr35^1.39A, and
Trp84^2.60A all abolish peptide and non-peptide ligand binding.

### Sodium binding site

A conserved allosteric sodium-binding site is observed in AT1R, structurally
superimposable with the sodium pocket in the delta-opioid receptor (PDB 4N6H).
The pocket includes Asp74^2.50, Asn111^3.35, Asn295^7.46, Trp253^6.48, and
Asn298^7.49. Asn111^3.35 and Asn295^7.46 form two intramolecular hydrogen bonds
stabilizing the inactive conformation.

### ECL2 as autoantibody epitope

ECL2 of AT1R serves as an epitope for harmful agonistic autoantibodies in
preeclampsia and malignant hypertension. The atomic details of ECL2 and the
extracellular ligand-binding region provide guidance for designing antigens against
these autoantibodies.

### Activation mechanism

The inactive conformation is stabilized by the Asn111^3.35-Asn295^7.46 hydrogen
bond network. Binding of angiotensin II disrupts this interaction, allowing
Asn295^7.46 to interact with Asp74^2.50. The conserved D(E)RY motif (helix III)
and NPxxY motif (helix VII) are present. The ionic lock between Arg^3.50 and
Asp/Glu^6.30 is not possible in AT1R due to lack of acidic residue at 6.30.
Helix VIII angles away from the membrane, resembling CCR5 orientation.

### Beta-arrestin signaling

G protein-independent beta-arrestin mediated signaling by AT1R confers
cardio-protective benefits. Thr336Pro and Pro341His (in the C-terminal tail not
included in the crystallized construct) affect GPCR kinase-dependent phosphorylation,
necessary for beta-arrestin recruitment.

### Active-state conformational changes

The active-state AT1R (PDB 6DO1) shows an 11 angstrom outward displacement of TM6,
rotation of TM5 away from the transducer binding pocket, and inward rotation of TM7.
ICL2 reorganizes to form a short alpha helix. Helix 8 repositions from a bent
conformation away from the membrane to a conventional position parallel to the
membrane near the TM1-TM7 interface. Y302^7.53 of the NPxxY motif rotates 10
angstroms inward to hydrogen bond with Y215^5.58 in TM5.

### Peptide binding mode

S1I8 binds in an extended conformation with N terminus facing the solvent and C
terminus buried deep in the receptor core. The peptide forms a half-beta-barrel
with the receptor N terminus and ECL2 beta-hairpin. Key interactions: H183^ECL2
hydrogen bonds with the peptide N terminus; W84^2.60, V108^3.32, L112^3.36, and
I288^7.38 interact with P7 and I8 of S1I8; R2 of the peptide engages D281^7.32
and D263^6.58; the terminal carboxylate interacts with K199^5.42.

### Phenylalanine ratchet mechanism

AT1R activation involves a phenylalanine ratchet between TMs 5 and 6: I8 of S1I8
forces W253^6.48 and Y292^7.43 downward, causing F249^6.44 and F250^6.45 to ratchet
past F208^5.51. This creates a void filled by N295^7.46 moving inward, breaking the
N111^3.35-N295^7.46 hydrogen bond present in the inactive structure. This mechanism
diverges from other GPCRs and explains the diversity of allosteric mechanisms among
GPCRs.

### Biased agonism and C-terminal residue 8

The C-terminal residue 8 of AngII determines signaling bias. Ile8 (S1I8) produces
partial Gq agonism; Phe8 (AngII) produces full Gq agonism but the phenyl ring
slightly exceeds the cavity size shaped by TM3. Smaller residues or deletions at
position 8 produce beta-arrestin-biased ligands. The I8 side chain fits closely
into a TM3-shaped cavity, and the cavity size relative to residue 8 side chain
determines the conformational changes propagated through the receptor.


## Cross-References

- [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/) — Primary ligand bound in PDB 4YAY structure
- [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) — Endogenous agonist of AT1R
- [S1I8](/xray-mp-wiki/reagents/ligands/s1i8/) — Partial agonist peptide used in active-state PDB 6DO1 crystallization
- [Nb.AT110i1 Synthetic Nanobody](/xray-mp-wiki/reagents/antibodies/nb-at110i1/) — Conformation-specific nanobody stabilizing active-state AT1R (PDB 6DO1)
- [Lauryl Maltose Neopentyl Glycol (MNG)](/xray-mp-wiki/reagents/detergents/mng/) — Detergent used for AT1R solubilization and purification in PDB 6DO1
- [Losartan](/xray-mp-wiki/reagents/ligands/losartan/) — ARB used for AT1R expression stabilization and comparison with peptide ligands
- [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) — ARB used in FACS selection for conformation-specific nanobody discovery
- [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) — Thermostabilization fusion partner inserted into AT1R ICL3 for PDB 6DO1
- [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/at2r/) — Close homolog with distinct signaling; AT2R structure reveals helix 8 canonical conformation upon AngII binding
