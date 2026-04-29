---
title: Cannabinoid Receptor CB1
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [gpcr, membrane-protein]
sources: [doi/10.1016##j.cell.2020.01.008]
---
layout: default

# Cannabinoid Receptor CB1

## Overview

CB1 (Cannabinoid Receptor 1) is a Class A GPCR that serves as the principal target of Delta-9-THC, the psychoactive compound from Cannabis sativa. CB1 is widely expressed in the central nervous system and modulates appetite, pain sensation, memory, and other physiological processes. CB1 couples to G(i), G(s), and G(q) proteins, unlike CB2 which is G(i)-selective.

## Structure

### Hua et al. (Cell 2020) — CB1-AM841-Gi-scFv16 Complex (Cryo-EM)

- **Resolution**: 3.0 Å
- **PDB ID**: 6KPG
- **Architecture**: 7 transmembrane helices (TM1–TM7) with short N-terminal helix over the binding pocket
- **Ligand**: AM841 (THC-like cannabinoid agonist) bound in orthosteric pocket
- **G protein**: Heterotrimeric G(i) (G(alpha)i1, G(beta)1, G(gamma)2) — nucleotide-free (no GDP density)
- **Stabilizer**: scFv16 antibody fragment binds at interface of G(alpha)i alpha N helix and G(beta) beta-propeller
- **Complex formation**: Assembled *in vitro* from purified components (receptor + G(i) + AM841 + scFv16)

### Hua et al. (Cell 2020) — CB1-AM841 Crystal Structure (Active-like State)

- **Resolution**: Not explicitly stated (close to active state)
- **Architecture**: 7TM GPCR with AM841 agonist bound
- **Key features**: "Twin toggle switch" (Phe3.36 and Trp6.48) both adopt active conformations; DRY and NPxxY motifs rearranged
- **Comparison**: Shows larger conformational changes than CB2 upon agonist binding

### Inactive State (Hua et al., Nature 2017)

- **PDB ID**: 5ZTY
- **Architecture**: 7TM with N-terminal helix covering orthosteric site
- **Ligand**: Antagonist-bound conformation

## Activation Mechanism

### CB1 vs CB2 Activation

CB1 exhibits a more complex activation process than CB2:

- **"Twin toggle switch"**: Both Phe3.36 and Trp6.48 undergo synergistic conformational changes to unleash large structural rearrangements
- **Large outward TM6 movement**: Accommodates G(alpha)i alpha 5 helix mounting
- **Balloon-like plasticity**: CB1 shows extensive conformational changes across both extracellular and intracellular domains from inactive to active states
- **G protein coupling diversity**: CB1 couples to G(i), G(s), and G(q); CB2 is G(i)-selective only
- **Single residue in ICL2**: Leu222 in CB1 (vs Pro139 in CB2) may contribute to G protein-coupling diversity and enable G(s)/G(q) coupling

### Activation Motifs

- **DRY motif**: Rearranges upon activation
- **NPxxY motif**: Conformational change at intracellular end of TM7
- **Tyr7.53**: Establishes new contacts with Thr3.46, Leu3.43, and Arg3.50 upon activation
- **Asp6.30**: Interrupts salt-bridge with Arg3.50, unlocking TM6 outward movement

## Cholesterol Binding

- **Endogenous allosteric modulator**: Cholesterol binds to an allosteric site in CB1 (not observed in CB2)
- **Binding site**: Between TM2 and TM4; key residues Phe155(2.42) and Phe237(4.46)
- **Phe4.46**: Unique to CB1 among Class A GPCRs
- **Conformational change**: In CB1-Gi complex, Phe155 and Phe237 move to occupy the cholesterol-binding position
- **Pregnenolone**: Cholesterol derivative that also acts as CB1 allosteric modulator (binds same region)
- **Not in CB2**: Key cholesterol-binding residues not conserved in CB2; cholesterol not observed in any CB2 structure

## Ligand Binding

### AM841 (Agonist)

- THC-like cannabinoid agonist
- Binds in orthosteric pocket with hydrophobic and aromatic interactions
- Binding pose superimposable with AM12033 in CB2

### AM10257 (Antagonist)

- Antagonist-bound CB2 structure (PDB: 5ZTY) used as search model for molecular replacement
- Binding pocket similar to agonist-bound but more compact

## Solubilization and Purification

### Hua et al. (Cell 2020)

- **Expression**: HEK293F human cells (CB1-Gi-scFv16 complex assembled *in vitro*)
- **Detergent**: [lmng](/reagents/detergents/lmng/) (Lauryl Maltose Neopentyl Glycol) for membrane solubilization
- **Lipid**: [cholesterol-hydrogen-succinate](/reagents/lipids/cholesterol-hydrogen-succinate/) (CHS) added for stability
- **Additional detergent**: [gdn](/reagents/detergents/gdn/) (glycol-diosgenin) in cryo-EM purification buffer
- **Antibody**: scFv16 fragment for complex stabilization during cryo-EM
- **G protein**: Heterotrimeric G(i) co-expressed and purified separately, then assembled *in vitro*
- **Purification**: [size-exclusion-chromatography](/methods/purification/size-exclusion-chromatography/) on Superdex 200 10/300 GL column
- **SEC buffer**: 20 mM [hepes-buffer](/reagents/buffers/hepes-buffer/) pH 7.5, 100 mM [sodium-chloride](/reagents/additives/sodium-chloride/), 0.00075% LMNG, 0.00025% GDN, 0.0001% CHS, 100 μM TCEP, 5 μM AM841
- **Cryo-EM grid**: CryoMatrix Amorphous alloy film, 300 mesh; vitrified on Vitrobot Mark IV (100% humidity, 4°C)

## Cross-References

- [cb2-receptor](/proteins/cb2-receptor/) — Cannabinoid Receptor 2 (44% sequence identity, 68% TM similarity)
- [bril-fusion](/concepts/bril-fusion/) — BRIL fusion used for CB2 stabilization (alternative to scFv16)
- [scfv16](/reagents/antibodies/scfv16/) — scFv16 antibody fragment for GPCR-Gi complex stabilization
- [lmng](/reagents/detergents/lmng/) — Detergent used for CB1 solubilization
- [cholesterol-hydrogen-succinate](/reagents/lipids/cholesterol-hydrogen-succinate/) — CHS added for membrane protein stability
- [gdn](/reagents/detergents/gdn/) — Glycol-diosfenin used in cryo-EM buffer
- [monoolein](/methods/crystallization/monoolein/) — Lipid used in LCP crystallization
- [cryoem](/methods/structure-determination/cryoem/) — Cryo-EM structure determination (3.0 Å for CB1-Gi-scFv16)
- [xray-crystallography](/methods/structure-determination/xray-crystallography/) — X-ray crystallography for CB1 active-like structure
- [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method
- [size-exclusion-chromatography](/methods/purification/size-exclusion-chromatography/) — SEC for complex purification
- [hek293-cells](/methods/expression-systems/hek293-cells/) — HEK293 expression system (indirectly referenced via CB1 work)
- [sf9-cells](/methods/expression-systems/sf9-cells/) — Sf9 cells used for CB2-Gi complex expression