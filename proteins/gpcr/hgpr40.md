---
title: Human Free Fatty Acid Receptor 1 (GPR40)
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein]
sources: [doi/10.1038##nature13494, doi/10.1038##nsmb.3417, doi/10.1038##s41467-017-01240-w]
verified: false
---

# Human Free Fatty Acid Receptor 1 (GPR40)

## Overview

Human GPR40 (Free Fatty Acid Receptor 1, FFAR1) is a G-protein-coupled receptor that binds medium- to long-chain free fatty acids and is primarily expressed in pancreatic beta cells and intestinal enteroendocrine cells. It couples mainly to the G-alpha-q pathway to mediate glucose-stimulated insulin secretion, making it a therapeutic target for type 2 diabetes mellitus. The receptor can be activated by partial agonists (e.g., MK-8666/TAK875) that bind in the orthosteric transmembrane pocket, and by allosteric AgoPAMs that bind to a novel lipid-facing pocket between TM3, TM4, TM5 and ICL2, exhibiting positive binding cooperativity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13494 | 4PHU | 2.3 | Not specified | Human GPR40 with L42(2.40)A, F88(3.34)A, G103(3.49)A, Y202(5.58)F mutations; [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fused into ICL3 between residues 213-214; N-terminal Flag tag; C-terminal octa-histidine tag | [TAK-875](/xray-mp-wiki/reagents/ligands/tak-875) (fasiglifam) |
| doi/10.1038##nsmb.3417 | 5TZY | 3.2 | P2_1 | Triple mutant L42A/G103A/Y202F, [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion in ICL3 | MK-8666 (partial agonist), AP8 (AgoPAM) |
| doi/10.1038##nsmb.3417 | 5TZR | 2.2 | C2 | Triple mutant L42A/G103A/Y202F, [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion in ICL3 | MK-8666 (partial agonist) |
| doi/10.1038##s41467-017-01240-w | 5KW2 | 2.76 | C2 | Human GPR40 (residues 1-211 with L42A/F88A/G103A/Y202F and 214-300), with T4L fusion in ICL3. Expressed in Sf9 cells using baculovirus system. Same stabilized construct as 4PHU. | Compound 1 (full agonist at A2 site) |

## Expression and Purification

- **Expression system**: HEK293 cells (mammalian)
- **Construct**: hGPR40 triple mutant (L42A, G103A, Y202F) with [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion in ICL3, C-terminal His tag and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/)
- **Notes**: Receptor was purified from cell culture supernatant
- **Induction**: Transient transfection with Lipofectamine 2000
- **Media**: DMEM with 10% FBS, 1% penicillin/streptomycin, nonessential amino acids

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (IMAC) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Buffer containing [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) exchanged to [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) during IMAC | Receptor purified from supernatant after expression |
| Deglycosylation | PNGase F | — |  | 20 microM PNGase F at 4 °C for 6 h |
| FLAG [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Anti-FLAG resin |  | [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) purification |
| Size-exclusion chromatography (SEC) | Gel filtration | SEC column | 20 mM HEPES pH 7.5, 300 mM NaCl, 0.02% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0003% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Polishing step, monomeric fractions pooled |


## Crystallization

### doi/10.1038##nsmb.3417

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | hGPR40-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) triple mutant with 100 microM MK-8666 and 100 microM AP8 (ternary) or 100 microM MK-8666 (binary) |
| Temperature | 20 °C |
| Notes | LCP matrix: 9:1 (w/w) [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/):[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/). Crystals appeared in 1-2 days, reached full size in 2+ weeks. Six crystals merged for ternary dataset, ten crystals for binary. |


## Biological / Functional Insights

### Cooperative allosteric activation mechanism

Partial agonists (MK-8666) bind in the orthosteric transmembrane pocket, while AgoPAMs (AP8) bind to a novel lipid-facing pocket between TM3, TM4, TM5 and ICL2. AgoPAM binding induces an upward shift of TM5 along its helical axis by about half a turn relative to TM4, and stabilizes ICL2 into a short helical conformation. This conformational coupling explains the positive cooperativity between the two classes of ligands. The AgoPAM-binding pocket is not fully formed in the absence of AP8; in the binary complex, a [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) molecule occupies the partially formed pocket.

### First GPCR agonist in a lipid-facing pocket

This is the first example of a GPCR agonist binding to a lipid-facing pocket outside the transmembrane helical bundle. The AgoPAM AP8 binds parallel to the transmembrane helices (TM4 and TM5), in contrast to extrahelical antagonists that bind perpendicularly. The binding mode and pocket geometry match selectivity toward medium- to long-chain free fatty acids.

### Full agonist compound 1 activates dual Gαq/Gαs pathways via A2 allosteric site

Compound 1 [DOI: 10.1038/s41467-017-01240-w] is a synthetic full agonist that binds to the second allosteric site (A2) of GPR40, distinct from the TAK-875/A1 site. Unlike TAK-875 (a partial Gαq agonist), compound 1 activates both Gαq/Ca²⁺ and Gαs/cAMP pathways, leading to robust incretin secretion (GLP-1 and GIP) in vivo. The A2 site is a lipid-facing pocket between TM3-5 and ICL2, where compound 1 forms four hydrogen bonds with Tyr44(2.42), Tyr114(ICL2), Ser123(4.42) and a water molecule. Oral administration of compound 1 in mice significantly increases insulin secretion and reduces glucose excursion in wild-type but not GPR40-KO mice.

### ICL2 stabilization is the mechanism for enhanced G protein coupling

Compound 1 binding stabilizes ICL2 into a short α-helical conformation through a hydrogen bond from its carboxylate to Tyr114 in ICL2. In contrast, ICL2 is disordered in the 4PHU (TAK-875 bound) structure. The stabilized ICL2 contacts Gαs via hydrophobic interactions, explaining the dual Gαq/Gαs coupling and the full agonist pharmacology of compound 1. This contrasts with TAK-875 which binds at the A1 site between TM3-5 and ECL2, does not affect ICL2, and only activates Gαq. The A2 site also accommodates endogenous free fatty acids such as γ-linolenic acid, which shows positive cooperativity with TAK-875.

### Positive cooperativity between A1 and A2 site ligands

Compound 1 and TAK-875 exhibit positive allosteric cooperativity (α = 2.1, β = 14) in Ca²⁺ mobilization assays. Thermal denaturation experiments show that dual binding (compound 1 + TAK-875) increases thermostability more than either ligand alone: unliganded Tm = 51.4°C, TAK-875 Tm = 58.4°C, compound 1 Tm = 65.3°C, dual Tm = 68.2°C. This suggests that A2 site agonists could be combined with A1 site partial agonists for enhanced therapeutic effect.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used in initial purification step
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Used in SEC purification buffer
- [Monoolein](/xray-mp-wiki/reagents/buffers/monoolein/) — Host lipid for LCP crystallization
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) — Additive used in purification or crystallization buffers
- [Sodium Malonate](/xray-mp-wiki/reagents/additives/sodium-malonate/) — Additive used in purification or crystallization buffers
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Additive used in purification or crystallization buffers
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Additive used in purification or crystallization buffers
- [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) — Fusion tag for crystallization or purification
- [Extra-helical Binding Site in GPCRs](/xray-mp-wiki/concepts/signaling-receptors/extra-helical-binding-site/) — Compound 1 binds to the A2 extra-helical lipid-facing pocket between TM3-5 and ICL2
