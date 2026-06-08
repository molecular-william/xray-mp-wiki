---
title: Human P2X3 Receptor (hP2X3)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19367]
verified: false
---

# Human P2X3 Receptor (hP2X3)

## Overview

The human P2X3 receptor (hP2X3) is a ligand-gated ion channel from Homo sapiens that belongs to the P2X family of ATP-gated cation channels. P2X3 receptors form homotrimers, with each subunit containing two transmembrane helices (TM1 and TM2), a large extracellular ATP-binding domain, and intracellular N- and C-terminal tails. hP2X3 is activated by extracellular ATP and is permeable to monovalent and divalent cations (Na+, K+, Ca2+). It plays critical roles in pain sensation, inflammation, and cardiovascular regulation. hP2X3 undergoes rapid and nearly complete desensitization upon ATP activation, distinguishing it from P2X2, P2X4, P2X5, and P2X7 subtypes. This paper reports the first X-ray crystal structures of a human P2X receptor, capturing four major conformational states: apo/resting, agonist-bound/open-pore, agonist-bound/closed-pore/desensitized, and antagonist-bound/closed states.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature19367 | not specified | not specified | not specified | hP2X3-MFC_slow (Delta N5/Delta C33/P19V/S15V/V16I) | ATP (open state) |
| doi/10.1038##nature19367 | not specified | not specified | not specified | hP2X3-MFC_slow (Delta N5/Delta C33/P19V/S15V/V16I) | ATP or 2-methylthio-ATP (desensitized state) |
| doi/10.1038##nature19367 | not specified | not specified | not specified | hP2X3-MFC_slow (Delta N5/Delta C33/P19V/S15V/V16I) | None (apo/resting state) |
| doi/10.1038##nature19367 | not specified | not specified | not specified | hP2X3-MFC_slow (Delta N5/Delta C33/P19V/S15V/V16I) | TNP-ATP or A-317491 (antagonist-bound/closed state) |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus-mediated gene transduction of HEK293S GNTI- cells with N-terminal EGFP fusion and octa-histidine affinity tag | Not specified | Not specified | Cells grown to 3.0 x 10^6/ml, infected with P2 BacMam virus, grown at 37C for 16h, 10 mM sodium butyrate added, shifted to 30C for 72h
 |
| Solubilization | Membrane fraction solubilized in 40 mM dodecyl-3-D-maltopyranoside (C12M) after sonication with protease inhibitors | Not specified | 40 mM C12M | Protease inhibitors: 1 mM PMSF, 0.05 mg/ml aprotinin, 2 ug/ml pepstatin A, 2 ug/ml leupeptin
 |
| Affinity Purification | Incubation with TALON resin at 4C for 1-2h, elution with 250 mM imidazole pH 8.0 | TALON resin | Wash: 1 mM C12M, 30 mM imidazole, 5% glycerol in TBS. Elution: 250 mM imidazole pH 8.0
 | Column packed into XK-16 |
| Tag Removal | Thrombin (1:25, w/w) and Endo H (1:3, w/w) digestion at room temperature for approximately 16h | Not specified | pH lowered to 6.5 by addition of 500 mM MES pH 6.5 before digestion | Thrombin cleaves N-terminal EGFP-His8 tag |
| Size Exclusion Chromatography | Superdex 200 10/300 GL column pre-equilibrated with buffer | Superdex 200 | 20 mM HEPES pH 7.0, 100 mM NaCl, 0.5 mM C12M | Monodispersed trimeric fractions collected; protein concentrated to 2-3 mg/ml |


## Crystallization

### doi/10.1038##nature19367

| Parameter | Value |
|---|---|
| Notes | Four crystal structures determined: open state (ATP-bound), desensitized state (ATP-bound), apo/resting state (no ligand), and antagonist-bound state (TNP-ATP or A-317491). Crystals were soaked with 2-methylthio-ATP derivative for anomalous sulfur diffraction to confirm ATP identity in the desensitized state. For ion binding studies, apo hP2X3-MFC_slow was grown in presence of CsCl instead of NaCl to probe for anomalous scattering from Cs+ ions.
 |


## Biological / Functional Insights

### Cytoplasmic cap stabilizes the open state

The open state structure of hP2X3 visualizes an intracellular motif termed the cytoplasmic cap, which stabilizes the open state of the ion channel pore. The cytoplasmic cap includes elements of secondary structure from both termini, including two sequential beta-strands from the N terminus and a beta-strand from the C terminus. The tertiary structure is defined by a network of three beta-sheets that sit beneath the transmembrane domain. The C-terminal beta-strand of each protomer interacts with the N-terminal beta-strands of the other two protomers to form a small beta-sheet. Three beta-sheets incorporate one beta-strand from each protomer, illustrating domain swapping that knits receptor subunits together on the cytoplasmic side of the membrane. The cytoplasmic cap is observed only in the ATP-bound open state structure, suggesting that the cap-forming elements are flexible and disordered in the apo state. The three mutations (P19V, S15V, V16I from rat P2X2) that slow desensitization provide main chain conformational rigidity and make key hydrophobic interactions that stabilize the cap structure.

### Helical recoil model of receptor desensitization

Transition from the open to the desensitized state has two major features: the cytoplasmic cap unfolds or disassembles, and TM2 recoils upward, reverting the short stretch of 3_10-helix to an alpha-helix and allowing the pore to close at a new constriction site. V334 defines the constriction site of the desensitized state with a pore radius of 1.5 A, too narrow to pass hydrated Na+ ions. From the open to the desensitized states, V334 translates upward towards the extracellular surface and rotates inward to block the pore. The formation of the 3_10-helix occurred as a result of stretching of the top half of TM2 upward while the cytoplasmic surface was anchored by the cytoplasmic cap. The transition from open to desensitized reverts TM2 to an ideal helix by recoiling the cytoplasmic half of the helix upward, resembling a spring being released. The conserved N-terminal glycine (G24 in P2X3) and C-terminal glycine (G349 in P2X3) act as hinges providing flexibility for these dynamic conformational changes.

### Ion channel pore architecture and gating

Transmembrane helix 2 (TM2) lines the pore lumen, with residues I323, V326, T330, and V334 facing the pore. I323 defines the extracellular boundary of the gate in the apo state (pore radius 0.3 A), while T330 defines the cytoplasmic gate. In the open state, TM2 rotates counterclockwise by 15 degrees, promoting translation of I323 upward by 6.3 A and T330 upward by 5.3 A. In addition to rigid-body translation, TM2 undergoes a transition from an alpha-helix to a 3_10-helix centered within G333-V334-G335. ATP binding induces cleft closure between the head and dorsal fin domains while pushing the left flipper domain outward, transmitting structural rearrangements to the lower body and causing outward flexing of beta strands that pull on TM1 and TM2 helices.

### Competitive antagonism mechanism

The competitive antagonists TNP-ATP and A-317491 bind to the orthosteric ligand-binding pocket and stabilize the apo/resting state. Both ATP and antagonists occupy the same pocket at the interface between two protomers. The key difference is deeper penetration of the antagonists into the binding cleft. While ATP adopts a U-shape, TNP-ATP and A-317491 bind in a Y-shape, with the trinitrophenyl moiety of TNP-ATP and the phenoxy-benzyl moiety of A-317491 acting as the trunk. The antagonists form hydrophobic interactions with F174 and prevent the ATP-induced upward movement of the dorsal fin of protomer B, blocking cleft closure. TNP-ATP binds with Ki of 94 nM to hP2X3-MFC_slow and 118 nM to hP2X3-MFC.

### Ion access and permeation pathways

Ions enter the channel pore from the extracellular milieu via three lateral fenestrations located directly above the transmembrane domains at the extracellular vestibule. Anomalous scattering from Cs+ ions in the apo structure was present in a cavity made by the extracellular vestibule, consistent with Na+ ions entering through lateral fenestrations. Ion egress to the cytoplasm occurs through triangular-shaped cytoplasmic fenestrations formed by the cytoplasmic cap and TM2 helices from adjacent protomers. Molecular dynamics simulations in a POPC lipid bilayer confirmed that water and Na+ ions exit through these cytoplasmic fenestrations rather than along the threefold axis. Polar lipid head groups line the protein at the fenestrations and assist in water permeation.

### Mg2+ binding in the apo state

The apo structure of hP2X3 reveals a Mg2+ ion bound in the head domain, a feature not observed in the zfP2X4 apo structure. The Mg2+ is located in proximity to the ATP binding site, but its presence does not alter the affinity of hP2X3 for ATP. This Mg2+ binding site represents a unique feature of the hP2X3 apo structure compared to zfP2X4.


## Cross-References

- [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/zfp2x4/) — zfP2X4 is the first solved P2X receptor structure; hP2X3 structures compared extensively to zfP2X4 apo and open states
- [P2X Receptor Family](/xray-mp-wiki/concepts/p2x-receptor-family/) — hP2X3 is a member of the P2X receptor family; first human P2X receptor structure solved
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — Orthosteric agonist of hP2X3; Kd of 2.8 nM for hP2X3-MFC and 3.3 nM for hP2X3-MFC_slow
- [2'3'-O-(4,5-Dinitrobenzoyl)adenosine 5'-triphosphate (TNP-ATP)](/xray-mp-wiki/reagents/ligands/tnp-atp/) — Competitive antagonist of hP2X3 with Ki of 94 nM; binds deeper into the ATP pocket
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Related maltoside detergent to C12M used in hP2X3 purification
- [1-Palmitoyl-2-Oleoyl-sn-Glycero-3-Phosphocholine (POPC)](/xray-mp-wiki/reagents/lipids/popc/) — POPC lipid bilayer used in molecular dynamics simulations of hP2X3 open state
- [Cesium Chloride](/xray-mp-wiki/reagents/additives/cesium-chloride/) — CsCl used in place of NaCl for anomalous scattering studies of ion binding sites in apo hP2X3
- [Channel Gating via Plug Domain Displacement](/xray-mp-wiki/concepts/channel-gating/) — Comparison of gating mechanisms between P2X and other ion channel families
