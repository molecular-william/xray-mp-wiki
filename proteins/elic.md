---
title: ELIC (Erwinia chrysanthemi Ligand-gated Ion Channel)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##emboj.2013.17, doi/10.1038##nature07461]
verified: false
---

# ELIC (Erwinia chrysanthemi Ligand-gated Ion Channel)

## Overview

ELIC is a pentameric ligand-gated ion channel (pLGIC) from the bacterium Erwinia chrysanthemi. It is a homolog of eukaryotic Cys-loop receptors including nicotinic acetylcholine receptors, GABA_A receptors, and glycine receptors. ELIC can be activated by short-chain alcohols such as propanol and butanol, and by the neurotransmitter acetylcholine at high concentrations. It was the first bacterial pLGIC to be structurally characterized in a closed (non-conductive) state, providing a key comparison structure for the open-state GLIC structure. The structural comparison between ELIC and GLIC revealed insights into the gating mechanism of pLGICs.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature07461 | 2VL0 | 2.0 A | P43212 | Full-length ELIC from Erwinia chrysanthemi | None (apo-ELIC, closed-state structure) |
| doi/10.1038##emboj.2013.17 | Not specified in supplementary paper | Not specified in supplementary paper | Not specified in supplementary paper | Full-length ELIC from Erwinia chrysanthemi | Not specified in supplementary paper |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### Cis-proline conformation in the Cys-loop of ELIC

The original ELIC crystal structure built the conserved proline in the Phe/Tyr-Pro-Phe/Met motif at the apex of the Cys-loop in a trans conformation. However, residual Fo-Fc electron density analysis using the deposited structure factors showed both positive and negative peaks next to the carbonyl group of this proline, indicating the trans conformation should be inverted. A cis proline conformation makes the residual density vanish after refinement. This cis-proline conformation is conserved across pLGIC families including GLIC, ELIC, and GluCl, and contributes to a hydrogen bond interaction between the Cys-loop apex and the M3 helix. In ELIC, the distance for this hydrogen bond is 3.6 A, compared to 2.91 A in GLIC and GluCl.

### Comparison of ELIC and GLIC gating mechanisms

ELIC serves as a key comparison structure for GLIC, representing a non-conductive (closed) state versus GLIC's open state. The hydrogen bond between the apex of the Cys-loop and M3 is weaker in ELIC (d=3.6 A) than in the conductive structures of GLIC and GluCl (d=2.91 A), suggesting this interaction may contribute to stabilizing the open conductive form of pLGICs. The RMSD between the GLIC high-resolution structure and the previously published ELIC structure (3EAM) was 0.25 A for backbone and 0.38 A for all heavy atoms, indicating very close structural similarity despite different functional states.

### Structural superposition of ELIC and GLIC pentamers

Stereo view of C-alpha trace superposition of ELIC (closed state) and GLIC (open state) pentamers revealed structural similarities in the overall fold but differences in the transmembrane helix arrangements, particularly in helices alpha1, alpha2, alpha3, and the connecting loops. The pore region comparison showed that ELIC has a more constricted intracellular gate compared to the open GLIC structure, consistent with its non-conductive state.


## Cross-References

- [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic/) — Bacterial pLGIC homolog; direct structural comparison between closed (ELIC) and open (GLIC) states
- [GluCl (GABA-Gated Chloride Channel)](/xray-mp-wiki/proteins/glucl/) — Eukaryotic pLGIC homolog; cis-proline conformation confirmed across all three structures
