---
title: mTMEM16A (Murine TMEM16A Calcium-Activated Chloride Channel)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09280, doi/10.1038##nature13984]
verified: false
---

# mTMEM16A (Murine TMEM16A Calcium-Activated Chloride Channel)

## Overview

mTMEM16A is the murine ortholog of TMEM16A (Ano1), the long sought-after Ca2+-activated chloride channel (CaCC). TMEM16A is a member of the TMEM16 (anoctamin) protein family, which includes both Ca2+-activated chloride channels and lipid scramblases. TMEM16A is activated from the intracellular side at sub-micromolar Ca2+ concentrations with a voltage-dependent EC50. It contributes to diverse physiological processes including epithelial chloride secretion, electrical signaling in smooth muscles, and potentially nociception. The calcium binding site in mTMEM16A is structurally equivalent to that in nhTMEM16, and mutations of residues involved in Ca2+ coordination affect ion conduction in mTMEM16A, demonstrating a common activation mechanism across the TMEM16 family.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.2350 | 3JFQ | 3.7 A | TBD | Full-length mTMEM16A (isoform a) from Mus musculus | TBD |
| doi/10.1038##nature13984 | TBD | TBD | TBD | Full-length mTMEM16A (isoform ac) from Mus musculus, expressed in HEK293T cells | TBD |

## Expression and Purification

- **Expression system**: HEK293T cells (human embryonic kidney)
- **Construct**: mTMEM16A (isoform ac) expressed with C-terminal HRV 3C cleavage site, Myc tag, and SBP tag (scrambling assay construct); mTMEM16A (isoform ac) fused to Venus-YFP with Myc and SBP tags (electrophysiology construct)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell transfection | Transfection of HEK293T cells with plasmid DNA | -- | Transfection buffer with 2.8 mM Na2HPO4 + -- | mTMEM16A-YFP expressed in HEK293T cells for electrophysiology |
| Electrophysiology | Patch-clamp recordings | -- | Standard external solution (140 mM NaCl, 4 mM KCl, 2 mM CaCl2, 1 mM MgCl2, 10 mM glucose, 10 mM HEPES pH 7.4) + -- | mTMEM16A-YFP currents recorded in excised inside-out patches at 80 mV |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Ca2+ activation from intracellular side at sub-micromolar concentrations

TMEM16A is activated from the intracellular side by Ca2+ at sub-micromolar concentrations. The EC50 is voltage-dependent and decreases upon depolarization. This voltage-dependence is explained by the intramembrane location of the Ca2+ binding site, where the ion must cross a fraction of the transmembrane electric field to reach the binding site.

### Shared Ca2+ binding site with nhTMEM16

Mutations of residues in the Ca2+ binding site of mTMEM16A (equivalent to nhTMEM16) affect ion conduction, demonstrating that Ca2+ binding by equivalent residues regulates both functional branches of the TMEM16 family (chloride channels and lipid scramblases) by a common mechanism. Strongest effect observed for E654Q mutant, which showed no activation at any Ca2+ concentration.

### Physiological roles in epithelial chloride secretion and nociception

TMEM16A contributes to epithelial chloride secretion, electrical signaling in smooth muscles, and potentially nociception. It is expressed in diverse tissues and is implicated in various pathophysiological conditions including asthma, cancer, and pain.


## Cross-References

- [nhTMEM16 (TMEM16 Lipid Scramblase from Nectria haematococca)](/xray-mp-wiki/proteins/nhtmem16/) — Homologous TMEM16 protein; Ca2+ binding site mutations affect both ion conduction and lipid scrambling
- [TMEM16 Family](/xray-mp-wiki/concepts/tmem16-family/) — mTMEM16A is the prototype of the TMEM16 chloride channel subfamily
- [Calcium Chloride](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Ca2+ is the activating ligand for TMEM16A channel activity
- [EGTA (Ethylene Glycol Tetraacetic Acid)](/xray-mp-wiki/reagents/additives/egta/) — Ca2+ chelator used in TMEM16A patch-clamp experiments to control free Ca2+
