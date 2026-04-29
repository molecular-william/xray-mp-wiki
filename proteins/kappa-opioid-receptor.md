---

title: Kappa Opioid Receptor (KOP)
created: 2026-04-27
updated: 2026-04-27
type: protein
tags: [gpcr, receptor]
sources: [doi/10.1016##j.cell.2017.12.011]

---
layout: default


# Kappa Opioid Receptor (KOP)

## Overview

The kappa opioid receptor (KOP, also known as OPK) is a class A GPCR that mediates the actions of opioids with hallucinogenic, dysphoric, and analgesic activities. It is one of the four canonical opioid receptors (alongside MOP, DOP, and NOP).

## Structure Determination

- **PDB ID**: 6B73
- **Resolution**: 3.1 Å
- **Space group**: P2₁
- **Complexes/ASU**: 2
- **Beamline**: APS GMCA/CAT 23ID-B/D, 1.033 Å, 10-μm microfocus beam
- **Construct**: [bril](/reagents/protein-tags/bril/)-fused KOP (thermostabilized with Apafant [bril](/reagents/protein-tags/bril/))
- **Ligand**: [mp1104](/reagents/ligands/mp1104/) (potent epoxymorphinan opioid agonist)
- **Transducer mimic**: [nanobody](/reagents/antibodies/nanobody/) (active-state-stabilizing nanobody)
- **Total reflections**: 89,325; Unique reflections: 30,278
- **R-work/R-free**: 25.4%/27.5%

## Expression and Purification

- **Expression system**: [hek293-cells](/methods/expression-systems/hek293-cells/) (mammalian, stable expression)
- **Construct design**:
  - N-terminal FLAG tag
  - [bril](/reagents/protein-tags/bril/) (thermostabilized apocytochrome b562RIL) fused into ICL3
  - C-terminal His-tag on [bril](/reagents/protein-tags/bril/)
- **Detergent**: [ddm](/reagents/detergents/ddm/) (n-dodecyl-β-D-maltopyranoside) for membrane solubilization
- **Purification**: Anti-FLAG [affinity-chromatography](/methods/purification/affinity-chromatography/), [affinity-chromatography](/methods/purification/affinity-chromatography/) (His-tag on [bril](/reagents/protein-tags/bril/)), followed by [size-exclusion-chromatography](/methods/purification/size-exclusion-chromatography/) (Superdex 200)
- **SEC buffer**: 20 mM [hepes-buffer](/reagents/buffers/hepes-buffer/) pH 7.5, 150 mM [sodium-chloride](/reagents/additives/sodium-chloride/), 0.05% [ddm](/reagents/detergents/ddm/), 1 μM [mp1104](/reagents/ligands/mp1104/)

## Crystallization

- **Method**: [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) (LCP) — [monoolein](/methods/crystallization/monoolein/)-based mesophase
- **Lipid**: [monoolein](/methods/crystallization/monoolein/) (Sigma M8410)
- **Protein-to-lipid ratio**: 1:1.5 (w/w)
- **Precipitant**: 0.1 M [tris-buffer](/reagents/buffers/tris-buffer/)-HCl pH 8.5, 0.2 M MgCl₂, 18–22% PEG 300
- **Temperature**: 20 °C
- **Crystal growth**: 1–2 weeks

## Active-State Conformational Changes

Comparison of active-state KOP (6B73) with inactive-state KOP (PDB: 4DJH) reveals:

- **TM6 outward displacement**: ~10 Å at intracellular end — hallmark of GPCR activation
- **7TM bundle expansion**: Intracellular expansion of the transmembrane bundle
- **Binding pocket contraction**: Extracellular region contracts upon agonist binding
- **Key measurements**: I58¹·³¹–Q115²·⁶⁰ distance, Q213ᴱᶜˡ², D223⁵·³⁵, L299⁶·⁶⁰, S310⁷·³³

## Activation Signal Propagation

The activation cascade proceeds through interconnected motifs:

1. **D³·³²YYNM³·³⁶ motif** (TM3): Anchoring motif that rearranges upon agonist binding; forms a hub for GPCR structural rearrangements
2. **CWxP motif** (TM6): W287⁶·⁴⁸ interacts with MP1104's cyclopropylmethyl group, coupling ligand binding to activation
3. **P⁵·⁵⁰-I³·⁴⁰-F⁶·⁴⁴ microswitch**: P238⁵·⁵⁰ moves inward, I146³·⁴⁰ changes rotameric state, promoting F283⁶·⁴⁴ rotation → TM6 swivel
4. **Sodium pocket** (TM2/TM3/TM7): D105²·⁵⁰–N141³·³⁵–S145³·³⁹; collapses upon activation; D105²·⁵⁰–S145³·³⁹ H-bond replaces Na⁺ coordination; N141³·³⁵ A mutation converts classic antagonists into full agonists
5. **NPxxY motif** (TM7): Rearranges during activation
6. **DRY motif** (TM3/ICL2): Classic GPCR activation motif

## Ligand Binding Pocket

**MP1104 interactions**:
- Ionic interaction between epoxymorphinan nitrogen and D138³·³² (conserved in opioid receptors)
- Cyclopropylmethyl group: hydrophobic pocket formed by W287⁶·⁴⁸, G319⁷·⁴², Y320⁷·⁴³
- Iodobenzamide moiety: stabilized by water-mediated H-bond with Y312⁷·³⁵

**Key pocket residues**:
- D138³·³² — ionic anchor for basic nitrogen (mutating to Ala strongly reduces agonist binding)
- W287⁶·⁴⁸ — aromatic cluster center, hydrophobic contact with cyclopropylmethyl
- Y312⁷·³⁵ — water-mediated H-bond with ligand carbonyl; Y312W mutation attenuates β-arrestin recruitment
- Y320⁷·⁴³ / G319⁷·⁴² — form hydrophobic pocket for cyclopropylmethyl group
- H291⁶·⁵² and Y139³·³³ — interact with phenol moiety of classical opioids (dynorphin)

## Biased Signaling

KOP engages both G protein (Gαi1) and β-arrestin2 signaling pathways. [nanobody](/reagents/antibodies/nanobody/) binding is:
- Inhibited by Gαi1 (competitive with transducer)
- Promoted by β-arrestin2 (allosteric enhancement)

[mp1104](/reagents/ligands/mp1104/) is a balanced full agonist for both pathways (bias factor ~0.6 toward G protein).

## Cross-References

- [a2a-adenosine-receptor](/proteins/a2a-adenosine-receptor/) — Another class A GPCR with nanobody/stabilizer approach (Rag31, PSB1-bRIL)
- [p2y12-receptor](/proteins/p2y12-receptor/) — GPCR with ligand-bound structure showing pocket plasticity
- [5ht2b-receptor](/proteins/5ht2b-receptor/) — Serotonin GPCR with [bril](/reagents/protein-tags/bril/) fusion and [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) crystallization
- [fab-fragments](/reagents/antibodies/fab-fragments/) — Antibody fragments for GPCR stabilization (alternative to nanobodies)