---
title: "Zebrafish P2X4 Receptor (zfP2X4)"
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08198, doi/10.1038##nature11010]
verified: false
---

# Zebrafish P2X4 Receptor (zfP2X4)

## Overview

The zebrafish P2X4 receptor (zfP2X4) is a ligand-gated ion channel from Danio rerio that belongs to the P2X family of [ATP](/xray-mp-wiki/reagents/ligands/atp)-gated cation channels. P2X receptors form homotrimers, with each subunit containing two transmembrane helices (TM1 and TM2), a large extracellular [ATP](/xray-mp-wiki/reagents/ligands/atp)-binding domain, and intracellular N- and C-terminal tails. zfP2X4 was the first P2X receptor structure to be solved, providing the first atomic-level view of this important class of ionotropic receptors. The receptor is activated by extracellular [ATP](/xray-mp-wiki/reagents/ligands/atp) and is permeable to monovalent and divalent cations. zfP2X4 shares approximately 86% sequence identity with human P2X4 and serves as a valuable structural model for the entire P2X receptor family.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature08198 | 3PHV | 3.46 A | R3 | Delta zfP2X4-A (Delta N27/Delta C8) | ATP (in related functional studies; structure is apo) |
| doi/10.1038##nature08198 | 3PHV | 3.10 A | R32 | Delta zfP2X4-B (Delta N27/Delta C8/C51F/N78K/N187R) | ATP (in related functional studies; structure is apo) |
| doi/10.1038##nature11010 | 3H9V | 2.80 A | R32 | Delta zfP2X4-C | ATP |
| doi/10.1038##nature11010 | 3H9V | 2.90 A | R32 | Delta zfP2X4-C | None (apo) |

## Expression and Purification

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Transfection of tsA201 cells (derived from HEK293) with zfP2X4-EGFP constructs | Not specified | Not specified | 250,000 cells transfected with 1 ug construct; expression analyzed 36 hours post-transfection |
| Solubilization | Membrane fraction isolated by centrifugation at 66,000 x g for 40 min, solubilized in detergent | Not specified | 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm) or 0.5% [Digitonin](/xray-mp-wiki/reagents/detergents/digitonin) | Cross-linking with glutaraldehyde (GA) at room temperature for 30 min showed rP2X4 is a trimer before solubilization; only stable in [Digitonin](/xray-mp-wiki/reagents/detergents/digitonin) after solubilization |
| Purification | Affinity purification followed by size exclusion chromatography | Not specified | Not specified | EGFP-tagged constructs used for affinity purification; Endo H treatment and thrombin cleavage performed; Coomassie Brilliant Blue staining confirmed purity |


## Crystallization

### doi/10.1038##nature08198

| Parameter | Value |
|---|---|
| Notes | Two crystal forms obtained. Form A (R3) from Delta zfP2X4-A construct. Form B (R32) from Delta zfP2X4-B construct with additional C51F, N78K, N187R mutations. SAD phasing used [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine) derivatives at 0.9787 A wavelength. Anomalous maps confirmed methionine locations in parent, C51M, and L349M derivatives. |

### doi/10.1038##nature11010

| Parameter | Value |
|---|---|
| Notes | [ATP](/xray-mp-wiki/reagents/ligands/atp)-bound and apo structures of Delta zfP2X4-C in space group R32. [ATP](/xray-mp-wiki/reagents/ligands/atp)-bound form has larger unit cell with a=128.8, c=252.1 A and contains 31 [ATP](/xray-mp-wiki/reagents/ligands/atp) molecules and 92 waters. Apo form has more compact unit cell with a=99.6, c=441.5 A and contains no [ATP](/xray-mp-wiki/reagents/ligands/atp) and 79 waters. PDB ID: 3H9V. |


## Biological / Functional Insights

### ATP dose-dependent activation and EC50 values

Whole-cell patch-clamp recordings showed [ATP](/xray-mp-wiki/reagents/ligands/atp) dose-dependent activation of zfP2X4 constructs. zfP2X4.1-EGFP had an EC50 of 1730 uM with a Hill slope of 0.9. The deletion construct Delta zfP2X4-EGFP-A had an EC50 of 27.4 uM with a Hill slope of 1.6, indicating improved [ATP](/xray-mp-wiki/reagents/ligands/atp) sensitivity upon [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation). The thermostabilized Delta zfP2X4-EGFP-B construct had an EC50 of 3.4 uM with a Hill slope of 1.3, showing dramatically enhanced [ATP](/xray-mp-wiki/reagents/ligands/atp) sensitivity while maintaining cooperative activation.

### Closed pore conformation and gate architecture

The zfP2X4 structure reveals a closed conformation of the ion channel pore with the gate located approximately halfway across the membrane bilayer. Three vestibules (upper, central, and extracellular) are positioned on the molecular 3-fold axis, with the extracellular vestibule connected to bulk solution through a fenestration. Pore lining surface analysis showed a closed pore with potential gate residues including L340, G343, A344, and A347 in the TM2 helix. Solvent-facing residues L340 and N341 in TM2 were identified as key gate components.

### Gadolinium inhibition mechanism

Gadolinium (Gd3+) inhibits [ATP](/xray-mp-wiki/reagents/ligands/atp)-evoked currents in a concentration-dependent, voltage-independent manner and accelerates the rate of deactivation. At 100 uM, GdCl3 completely abolished currents evoked by 30 uM [ATP](/xray-mp-wiki/reagents/ligands/atp) and partially inhibited currents evoked by 100 uM [ATP](/xray-mp-wiki/reagents/ligands/atp), while currents evoked by 1 mM [ATP](/xray-mp-wiki/reagents/ligands/atp) were seemingly unaffected. The inhibition was not due to sequestration of [ATP](/xray-mp-wiki/reagents/ligands/atp) by gadolinium, as GdCl3 present only in the control solution (without [ATP](/xray-mp-wiki/reagents/ligands/atp)) was sufficient to largely abolish [ATP](/xray-mp-wiki/reagents/ligands/atp)-evoked currents.

### N-glycosylation and oligomeric state

Western blot analysis showed that P2X4 receptors are glycosylated and tend to aggregate. rP2X4 was found to be a trimer before solubilization. After solubilization, the trimeric state was maintained only in [Digitonin](/xray-mp-wiki/reagents/detergents/digitonin) but not in [DDM](/xray-mp-wiki/reagents/detergents/ddm), beta-octyl-glucoside, or CHAPS. Affinity purified Delta zfP2X4 treated with Endo H showed glycosylation removal, and thrombin cleavage confirmed the construct design. Size exclusion chromatography was used to verify monodispersity.

### Thermostabilization mutations

The Delta zfP2X4-B construct incorporated three additional mutations beyond the Delta N27/Delta C8 truncations: C51F, N78K, and N187R. These mutations were designed to improve crystallographic properties and thermostability. C51F replaces a surface cysteine to prevent non-specific disulfide formation. N78K and N187R introduce charged residues that may stabilize inter-subunit contacts. The B construct crystallized in a different space group (R32) with higher resolution (3.10 A vs 3.46 A) and fewer solvent-exposed residues.

### Sequence conservation across P2X receptors

Sequence alignment showed zfP2X4 shares significant homology with P2X receptors from multiple species including human (hP2X4), rat (rP2X4), chicken (ckP2X4), and Xenopus (xpP2X4), as well as other P2X subtypes (P2X1, P2X2, P2X3, P2X5). Conserved cysteine residues forming disulfide bonds in the extracellular domain were identified across all P2X receptors. Variable residues were distributed throughout the extracellular domain, with clusters of non-conserved residues forming surface-exposed loops.

### Pore architecture and ion pathways

The zfP2X4 structure revealed the architecture of the ion conduction pathway. Pore radius calculations using the Hole program showed a closed pore with radii less than 1.15 A at the gate region. Solvent-facing residues in TM2 (L340 and N341) were identified as key determinants of pore accessibility. The helical net diagram of TM2 showed that residues occluding the transmembrane pore are positioned on one face of the helix, with gating residues analogous to those in cASIC1mfc.

### Nucleotide recognition and base selectivity

The [ATP](/xray-mp-wiki/reagents/ligands/atp) binding site in zfP2X4 exhibits strong selectivity for [ATP](/xray-mp-wiki/reagents/ligands/atp) over other nucleotides. Competition assays showed IC50 values of 14.2 nM for [ATP](/xray-mp-wiki/reagents/ligands/atp), 391.0 nM for CTP, 55.5 uM for GTP, and 64.8 uM for UTP. The binding pocket involves hydrogen bonding interactions with residues including T189, K72, R143, K70, K193 and hydrophobic interactions with I232, L191, L217, A292, V291. The purine ring of [ATP](/xray-mp-wiki/reagents/ligands/atp) forms specific contacts while the triphosphate group engages multiple charged residues. CTP, GTP, and UTP show progressively weaker binding due to non-complementary hydrogen bonding partners in the binding site.

### Conformational changes upon ATP binding

Comparison of [ATP](/xray-mp-wiki/reagents/ligands/atp)-bound and apo Delta zfP2X4-C structures reveals a 5 degree rotation movement of the lower body domain (residues 56-74, 93-104, 188-207, 254-281, 320-333) upon [ATP](/xray-mp-wiki/reagents/ligands/atp) binding. This motion is classified as 99.9% closure motion and 0.1% twist motion by Dyndom analysis. Structural coupling between the dorsal fin and lower body domains, as well as between the left flipper and lower body domains, transmits the [ATP](/xray-mp-wiki/reagents/ligands/atp)-binding signal to the transmembrane domain. Binding of [TNP-ATP](/xray-mp-wiki/reagents/ligands/tnp-atp) precludes the dorsal fin movement induced by [ATP](/xray-mp-wiki/reagents/ligands/atp) binding, suggesting steric constraints on the binding pocket.

### Ivermectin binding site

Residues implicated in [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin) binding in rat P2X4 are conserved in zfP2X4. The transmembrane domain contains a cleft between adjacent subunits at the extracellular side of the membrane that is implicated as the [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin) binding site. This binding site is distinct from the orthosteric [ATP](/xray-mp-wiki/reagents/ligands/atp) binding site in the extracellular domain and is located in the transmembrane region.


## Cross-References

- [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Bacterial pLGIC homolog; comparison of extracellular domain architecture between pLGIC and P2X families
- [GluCl (GABA-Gated Chloride Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glucl/) — Pentameric ligand-gated ion channel homolog; comparison of gating mechanisms across pLGIC and P2X families
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — Orthosteric agonist of zfP2X4; EC50 values measured by patch-clamp
- [Digitonin](/xray-mp-wiki/reagents/detergents/digitonin/) — Only detergent maintaining zfP2X4 trimeric state after solubilization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization; disrupts zfP2X4 trimeric state
- [AMP-PNP (Adenylyl-Imidodiphosphate)](/xray-mp-wiki/reagents/ligands/amp-pnp/) — Non-hydrolyzable ATP analogue; related to ATP-binding studies in ion channels
- [2'3'-O-(4,5-Dinitrobenzoyl)adenosine 5'-triphosphate (TNP-ATP)](/xray-mp-wiki/reagents/ligands/tnp-atp/) — Fluorescent ATP analog that precludes dorsal fin movement upon binding
- [P2X Receptor Family](/xray-mp-wiki/concepts/signaling-receptors/p2x-receptor-family/) — zfP2X4 is the first solved member of the P2X receptor family
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine) — Entity mentioned in text
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation) — Entity mentioned in text
