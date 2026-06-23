---
title: Human P2X3 Receptor (hP2X3)
created: 2026-06-03
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19367, doi/10.7554##eLife.47060, doi/10.1073##pnas.1800907115]
verified: false
---

# Human P2X3 Receptor (hP2X3)

## Overview

The human P2X3 receptor (hP2X3) is a ligand-gated ion channel from Homo sapiens that belongs to the P2X family of [ATP](/xray-mp-wiki/reagents/ligands/atp/)-gated cation channels. P2X3 receptors form homotrimers, with each subunit containing two transmembrane helices (TM1 and TM2), a large extracellular [ATP](/xray-mp-wiki/reagents/ligands/atp/)-binding domain, and intracellular N- and C-terminal tails. hP2X3 is activated by extracellular [ATP](/xray-mp-wiki/reagents/ligands/atp/) and is permeable to monovalent and divalent cations (Na+, K+, Ca2+). It plays critical roles in pain sensation, inflammation, and cardiovascular regulation. hP2X3 undergoes rapid and nearly complete desensitization upon [ATP](/xray-mp-wiki/reagents/ligands/atp/) activation, distinguishing it from P2X2, P2X4, P2X5, and P2X7 subtypes. Under physiological conditions, ATP largely exists as Ca2+-ATP and Mg2+-ATP complexes. Crystal structures of hP2X3 with Mg2+-ATP (PDB 6AH5, 3.8 A) and Ca2+-ATP (PDB 6AH4, 3.3 A) reveal a unique mode of divalent cation coordination involving an acidic chamber (E156, D158, E109, E111) near the nucleotide-binding pocket. The divalent ion simultaneously interacts with D158 on the receptor and the gamma-phosphate of ATP, a binding mode that is rare in the PDB. This interaction stabilizes ATP on the receptor, slowing ATP unbinding and recovery from desensitization, and is essential for channel activation by divalent-bound ATP.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature19367 | not specified | not specified | not specified | hP2X3-MFC_slow (Delta N5/Delta C33/P19V/S15V/V16I) | ATP (open state) |
| doi/10.1038##nature19367 | not specified | not specified | not specified | hP2X3-MFC_slow (Delta N5/Delta C33/P19V/S15V/V16I) | ATP or 2-methylthio-ATP (desensitized state) |
| doi/10.1038##nature19367 | not specified | not specified | not specified | hP2X3-MFC_slow (Delta N5/Delta C33/P19V/S15V/V16I) | None (apo/resting state) |
| doi/10.1038##nature19367 | not specified | not specified | not specified | hP2X3-MFC_slow (Delta N5/Delta C33/P19V/S15V/V16I) | TNP-ATP or A-317491 (antagonist-bound/closed state) |
| doi/10.7554##eLife.47060 | 6AH5 | 3.8 | not specified | hP2X3-MFC_slow (Delta N5/Delta C33/T13P/S15V/V16I) | Mg2+-ATP (open-like conformation) |
| doi/10.7554##eLife.47060 | 6AH4 | 3.3 | not specified | hP2X3-MFC_slow (Delta N5/Delta C33/T13P/S15V/V16I) | Ca2+-ATP (open-like conformation) |
| doi/10.1073##pnas.1800907115 |  | 3.4 | not specified | hP2X3 | AF-219 (negative allosteric inhibitor) |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)-mediated gene transduction of HEK293S GNTI- cells with N-terminal EGFP fusion and octa-histidine affinity tag | Not specified | Not specified | Cells grown to 3.0 x 10^6/ml, infected with P2 BacMam virus, grown at 37C for 16h, 10 mM sodium butyrate added, shifted to 30C for 72h
 |
| Solubilization | Membrane fraction solubilized in 40 mM dodecyl-3-D-maltopyranoside (C12M) after sonication with protease inhibitors | Not specified | 40 mM C12M | Protease inhibitors: 1 mM [PMSF (Phenylmethylsulfonyl Fluoride)](/xray-mp-wiki/reagents/additives/pmsf/), 0.05 mg/ml aprotinin, 2 ug/ml pepstatin A, 2 ug/ml leupeptin
 |
| Affinity Purification | Incubation with [TALON](/xray-mp-wiki/reagents/additives/talon/) resin at 4C for 1-2h, elution with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) pH 8.0 | [TALON](/xray-mp-wiki/reagents/additives/talon/) resin | Wash: 1 mM C12M, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) in TBS. Elution: 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) pH 8.0
 | Column packed into XK-16 |
| Tag Removal | Thrombin (1:25, w/w) and Endo H (1:3, w/w) digestion at room temperature for approximately 16h | Not specified | pH lowered to 6.5 by addition of 500 mM [MES](/xray-mp-wiki/reagents/buffers/mes/) pH 6.5 before digestion | Thrombin cleaves N-terminal EGFP-His8 tag |
| Size Exclusion Chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL column pre-equilibrated with buffer | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 0.5 mM C12M | Monodispersed trimeric fractions collected; protein concentrated to 2-3 mg/ml |


## Crystallization

### doi/10.1038##nature19367

| Parameter | Value |
|---|---|
| Notes | Four crystal structures determined: open state ([ATP](/xray-mp-wiki/reagents/ligands/atp/)-bound), desensitized state ([ATP](/xray-mp-wiki/reagents/ligands/atp/)-bound), apo/resting state (no ligand), and antagonist-bound state ([TNP-ATP](/xray-mp-wiki/reagents/ligands/tnp-atp/) or [A-317491](/xray-mp-wiki/reagents/ligands/a-317491/)). Crystals were soaked with 2-methylthio-[ATP](/xray-mp-wiki/reagents/ligands/atp/) derivative for anomalous sulfur diffraction to confirm [ATP](/xray-mp-wiki/reagents/ligands/atp/) identity in the desensitized state. For ion binding studies, apo hP2X3-MFC_slow was grown in presence of CsCl instead of [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/) to probe for anomalous scattering from Cs+ ions.
 |

### doi/10.7554##eLife.47060

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Temperature | 20 |
| Notes | Crystals grew over 3 weeks. Cryoprotectant: 0.05 M Mg-acetate (or 0.2 M NaCl for Ca2+), 0.05 M Na-acetate pH 5.0, 40% PEG400, 1 mM ATP |

### doi/10.1073##pnas.1800907115

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | hP2X3 in complex with AF-219 |
| Notes | Crystals diffracted to 3.4-A resolution. Data collected at SPring-8 BL41XU and SSRF beamlines. |


## Biological / Functional Insights

### Cytoplasmic cap stabilizes the open state

The open state structure of hP2X3 visualizes an intracellular motif termed the cytoplasmic cap, which stabilizes the open state of the ion channel pore. The cytoplasmic cap includes elements of secondary structure from both termini, including two sequential beta-strands from the N terminus and a beta-strand from the C terminus. The tertiary structure is defined by a network of three beta-sheets that sit beneath the transmembrane domain. The C-terminal beta-strand of each protomer interacts with the N-terminal beta-strands of the other two protomers to form a small beta-sheet. Three beta-sheets incorporate one beta-strand from each protomer, illustrating domain swapping that knits receptor subunits together on the cytoplasmic side of the membrane. The cytoplasmic cap is observed only in the [ATP](/xray-mp-wiki/reagents/ligands/atp/)-bound open state structure, suggesting that the cap-forming elements are flexible and disordered in the apo state. The three mutations (P19V, S15V, V16I from rat P2X2) that slow desensitization provide main chain conformational rigidity and make key hydrophobic interactions that stabilize the cap structure.

### Helical recoil model of receptor desensitization

Transition from the open to the desensitized state has two major features: the cytoplasmic cap unfolds or disassembles, and TM2 recoils upward, reverting the short stretch of 3_10-helix to an alpha-helix and allowing the pore to close at a new constriction site. V334 defines the constriction site of the desensitized state with a pore radius of 1.5 A, too narrow to pass hydrated Na+ ions. From the open to the desensitized states, V334 translates upward towards the extracellular surface and rotates inward to block the pore. The formation of the 3_10-helix occurred as a result of stretching of the top half of TM2 upward while the cytoplasmic surface was anchored by the cytoplasmic cap. The transition from open to desensitized reverts TM2 to an ideal helix by recoiling the cytoplasmic half of the helix upward, resembling a spring being released. The conserved N-terminal [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (G24 in P2X3) and C-terminal [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (G349 in P2X3) act as hinges providing flexibility for these dynamic conformational changes.

### Ion channel pore architecture and gating

Transmembrane helix 2 (TM2) lines the pore lumen, with residues I323, V326, T330, and V334 facing the pore. I323 defines the extracellular boundary of the gate in the apo state (pore radius 0.3 A), while T330 defines the cytoplasmic gate. In the open state, TM2 rotates counterclockwise by 15 degrees, promoting translation of I323 upward by 6.3 A and T330 upward by 5.3 A. In addition to rigid-body translation, TM2 undergoes a transition from an alpha-helix to a 3_10-helix centered within G333-V334-G335. [ATP](/xray-mp-wiki/reagents/ligands/atp/) binding induces cleft closure between the head and dorsal fin domains while pushing the left flipper domain outward, transmitting structural rearrangements to the lower body and causing outward flexing of beta strands that pull on TM1 and TM2 helices.

### Competitive antagonism mechanism

The competitive antagonists [TNP-ATP](/xray-mp-wiki/reagents/ligands/tnp-atp/) and [A-317491](/xray-mp-wiki/reagents/ligands/a-317491/) bind to the orthosteric ligand-binding pocket and stabilize the apo/resting state. Both [ATP](/xray-mp-wiki/reagents/ligands/atp/) and antagonists occupy the same pocket at the interface between two protomers. The key difference is deeper penetration of the antagonists into the binding cleft. While [ATP](/xray-mp-wiki/reagents/ligands/atp/) adopts a U-shape, [TNP-ATP](/xray-mp-wiki/reagents/ligands/tnp-atp/) and [A-317491](/xray-mp-wiki/reagents/ligands/a-317491/) bind in a Y-shape, with the trinitrophenyl moiety of [TNP-ATP](/xray-mp-wiki/reagents/ligands/tnp-atp/) and the phenoxy-benzyl moiety of [A-317491](/xray-mp-wiki/reagents/ligands/a-317491/) acting as the trunk. The antagonists form hydrophobic interactions with F174 and prevent the [ATP](/xray-mp-wiki/reagents/ligands/atp/)-induced upward movement of the dorsal fin of protomer B, blocking cleft closure. [TNP-ATP](/xray-mp-wiki/reagents/ligands/tnp-atp/) binds with Ki of 94 nM to hP2X3-MFC_slow and 118 nM to hP2X3-MFC.

### Ion access and permeation pathways

Ions enter the channel pore from the extracellular milieu via three lateral fenestrations located directly above the transmembrane domains at the extracellular vestibule. Anomalous scattering from Cs+ ions in the apo structure was present in a cavity made by the extracellular vestibule, consistent with Na+ ions entering through lateral fenestrations. Ion egress to the cytoplasm occurs through triangular-shaped cytoplasmic fenestrations formed by the cytoplasmic cap and TM2 helices from adjacent protomers. Molecular dynamics simulations in a [POPC](/xray-mp-wiki/reagents/lipids/popc/) lipid bilayer confirmed that water and Na+ ions exit through these cytoplasmic fenestrations rather than along the threefold axis. Polar lipid head groups line the protein at the fenestrations and assist in water permeation.

### Mg2+ binding in the apo state

The apo structure of hP2X3 reveals a Mg2+ ion bound in the head domain, a feature not observed in the [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/) apo structure. The Mg2+ is located in proximity to the [ATP](/xray-mp-wiki/reagents/ligands/atp/) binding site, but its presence does not alter the affinity of hP2X3 for [ATP](/xray-mp-wiki/reagents/ligands/atp/). This Mg2+ binding site represents a unique feature of the hP2X3 apo structure compared to [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/).

### Negative allosteric site for drug binding on P2X3

The crystal structure of hP2X3 in complex with AF-219 (a negative allosteric inhibitor under phase II clinical trials for refractory chronic cough and idiopathic pulmonary fibrosis) revealed a druggable allosteric site fostered by the left flipper (LF), lower body (LB), and dorsal fin (DF) domains at the interface between adjacent subunits. This site is distinct from the orthosteric ATP binding site. AF-219 is partially buried by the LF and DF domains, with the 4-isopropyl-2-methoxybenzenesulfonamide ring trapped in the inner part of the pocket. Structurally analogous inhibitors AF-353, RO-51, RO-3, and TC-P 262 share the same binding site. The conserved R264-D266 salt bridge at the beginning of the LF domain is crucial for maintaining the shape of the allosteric site.

### Allosteric inhibition mechanism of P2X3

The identified allosteric cavity collapses during ATP-induced channel gating as the LF domain moves toward the neighboring LB-DF domains. Binding of AF-219 in this pocket not only prevents the collapsing of the cavity but can also enlarge its volume, thereby blocking the conformational changes (LF, DF, LB domain movements) required for coupling ATP binding to channel activation. The V238C mutant covalently modified with N-phenylmaleimide (NPM) confirmed that occupation of this site exerts a negative effect on hP2X3 gating.

### Divalent cation binding chamber and ATP coordination

Crystal structures of hP2X3 with Mg2+-ATP (PDB 6AH5, 3.8 A) and Ca2+-ATP (PDB 6AH4, 3.3 A) reveal a unique divalent cation binding chamber formed by acidic residues E109, E111, E156, and D158 near the nucleotide-binding pocket. In the ATP-bound state (lower mode), the divalent ion simultaneously coordinates with the gamma-phosphate of ATP and D158, with additional interactions via E156. This coordination mode is unusual — a survey of the PDB shows the divalent ion typically interacts with both beta- and gamma-phosphates. In the apo state (upper mode), the ion shifts upward ~9 A to interact with E109 and E111 as well. The D158 side chain acts as a switch, pointing toward E109 in the upper mode or toward the ATP gamma-phosphate in the lower mode. This acidic chamber enables the receptor to accommodate divalent-bound ATP in two distinct binding modes.

### Mg2+ and Ca2+ slow ATP unbinding and recovery from desensitization

Electrophysiological recordings show that Mg2+ slows hP2X3 deactivation by ~8-fold (deactivation time constant increases from 2.1 s to ~17 s) and Ca2+ slows it by ~4-fold at pH 7.3. The lower mode of divalent binding (D158 interaction) is essential for this effect: the D158A mutation eliminates Mg2+-dependent slowing of deactivation. Mg2+ also slows recovery from desensitization (tau increases from 63 s to 248 s), while Ca2+ has a smaller effect (tau = 115 s). In physiological solutions containing both Mg2+ and Ca2+, the effect is intermediate (tau = 140 s), explaining how Ca2+ can facilitate P2X3 activation in the presence of Mg2+. Molecular dynamics simulations reveal that Mg2+ strengthens ATP-receptor interactions cooperatively — the ion holds onto partially unbound nucleotide, fostering rebinding.

### Acidic chamber is critical for activation by divalent-bound ATP

When Mg2+-ATP is the predominant form in solution, the acidic chamber is essential for channel activation. The E156A/D158A double mutant (disrupting the lower mode) shows severely weakened activation by Mg2+-ATP and produces a resurgent current upon Mg2+-ATP removal, indicating that Mg2+-ATP can bind but cannot robustly open the channel. The triple mutant E109A/E156A/D158A eliminates Mg2+ effects entirely but dramatically weakens ATP binding. This demonstrates that the divalent cation bound between ATP and the receptor enables proper channel gating under physiological conditions where ATP is predominantly complexed with Ca2+ or Mg2+.

### Two-mode divalent binding model for P2X3 activation

A model is proposed where Mg2+ (or Ca2+) initially occupies the upper mode in the apo state under physiological conditions. When divalent-bound ATP enters the nucleotide-binding pocket, the ion in the upper mode dissociates, and the ion bound to ATP repositions to the lower mode (coordinated by D158 and the ATP gamma-phosphate). This sandwich configuration between ATP and the receptor stabilizes the nucleotide, slows unbinding, and enables cooperative gating. When ATP dissociates, the ion spontaneously moves from the lower mode back to the upper mode, demonstrating a pathway for divalent ion movement between the two sites.


## Cross-References

- [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/) — zfP2X4 is the first solved P2X receptor structure; hP2X3 structures compared extensively to zfP2X4 apo and open states
- [P2X Receptor Family](/xray-mp-wiki/concepts/p2x-receptor-family/) — hP2X3 is a member of the P2X receptor family; first human P2X receptor structure solved
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — Orthosteric agonist of hP2X3; Kd of 2.8 nM for hP2X3-MFC and 3.3 nM for hP2X3-MFC_slow
- [2'3'-O-(4,5-Dinitrobenzoyl)adenosine 5'-triphosphate (TNP-ATP)](/xray-mp-wiki/reagents/ligands/tnp-atp/) — Competitive antagonist of hP2X3 with Ki of 94 nM; binds deeper into the ATP pocket
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Related maltoside detergent to C12M used in hP2X3 purification
- [1-Palmitoyl-2-Oleoyl-sn-Glycero-3-Phosphocholine (POPC)](/xray-mp-wiki/reagents/lipids/popc/) — POPC lipid bilayer used in molecular dynamics simulations of hP2X3 open state
- [Cesium Chloride](/xray-mp-wiki/reagents/additives/cesium-chloride/) — CsCl used in place of NaCl for anomalous scattering studies of ion binding sites in apo hP2X3
- [Channel Gating via Plug Domain Displacement](/xray-mp-wiki/concepts/channel-gating/) — Comparison of gating mechanisms between P2X and other ion channel families
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Related protein
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Related protein
