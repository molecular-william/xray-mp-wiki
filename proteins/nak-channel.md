---
title: NaK Channel from Bacillus cereus
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature04508, doi/10.1038##nsmb.1531]
verified: false
---

# NaK Channel from Bacillus cereus

## Overview

NaK is a non-selective tetrameric cation channel from Bacillus cereus that conducts both Na+ and K+ ions. It shares high sequence homology and overall architecture with the bacterial KcsA K+ channel, but its selectivity filter adopts a different architecture that results in loss of ion selectivity. The NaK selectivity filter resembles that of cyclic nucleotide-gated (CNG) channels. This structure provides key insights into the structural basis of ion selectivity in cation channels and demonstrates that protein atoms surrounding the ion-binding site confer size-selectivity through geometric constraints, rather than electrostatic repulsion between carbonyl oxygen atoms.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature04508 | 2NKA | 2.4 | C2221 | NaK channel from Bacillus cereus, residues 1-103 | Na+ |
| doi/10.1038##nature04508 | 2NKB | 2.8 | C2221 | NaK channel from Bacillus cereus, residues 1-104 | K+ |
| doi/10.1038##nsmb.1531 | 2AHY (closed conformation, PDB 2AHY) / NaKN delta 19 (open conformation, 1.6 A) | 1.6 | I4 | NaKN delta 19 (lacks N-terminal M0 helix) — open conformation at intracellular gate | Various monovalent cations (NaCl, KCl, RbCl); Ca2+ in crystallization |

## Expression and Purification

- **Expression system**: E. coli XL1-Blue
- **Construct**: NaK channel from Bacillus cereus cloned into pQE60 vector. Expressed in E. coli XL1-Blue cultures. Purified as a tetramer in n-decyl-beta-D-maltoside with NaCl or KCl as the monovalent salt.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent solubilization | -- | NaCl or KCl + n-decyl-beta-D-maltoside | Protein purified as a tetramer |


## Crystallization

### doi/10.1038##nature04508

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | NaK channel at 30-35 mg/mL |
| Reservoir | 36-42% PEG 400, 200 mM CaCl2, 100 mM Tris-HCl pH 7.5-8.5, 4% t-butanol |
| Temperature | 20 C |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals of space group C2221 with cell dimensions a = 81.5 A, b = 85.5 A, c = 129.6 A, alpha = beta = gamma = 90 degrees, containing two subunits per asymmetric unit. The four-fold axis of the channel tetramer coincides with one of the crystallographic dyads.
 |

### doi/10.1038##nsmb.1531

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | NaKN delta 19 (truncated construct lacking N-terminal M0 helix) |
| Reservoir | 55-70% (v/v) MPD, 1 mM CaCl2, 100 mM glycine pH 9.5 |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Crystals frozen in liquid propane; crystallization solution served as cryoprotectant |
| Notes | Open conformation structure determined at 1.6 A resolution. Space group I4 with unit cell dimensions a = b = 68 A, c = 89 A, alpha = beta = gamma = 90 degrees, two subunits per asymmetric unit. The four-fold axis of the channel tetramer coincided with the crystallographic tetrad. Protein packing in the crystal likely contributed to stabilization of the open conformation.
 |


## Biological / Functional Insights

### Selectivity filter architecture of NaK

The NaK selectivity filter preserves only two cation-binding sites equivalent to sites 3 and 4 of a K+ channel selectivity filter. The region corresponding to sites 1 and 2 of a K+ channel becomes a vestibule in which ions can diffuse but not bind specifically. Unlike K+ channel selectivity filters that contain four equivalent K+-binding sites, NaK's GDG residues adopt different backbone conformations. The carbonyl groups from Gly 65 and Asp 66 align tangentially to the ion conduction pathway, and their oxygen atoms do not point towards the centre to coordinate ions. Furthermore, the C-alpha of Asp 66 is directed away from the centre and its side chain protrudes upward and is exposed to the extracellular solution, creating a vestibule where ions can diffuse but not bind very specifically. At the entryway to the filter from the extracellular solution, the main chain at Gly 67 pinches inwards so that its carbonyl oxygen points towards the pore axis, forming an ion-binding site.

### Ion conduction properties

Functional analysis using 86Rb flux assays shows that NaK can conduct both Na+ and K+ ions. A truncated form (NaKN delta 19) lacking the N-terminal M0 helix showed higher flux rates than full-length NaK, suggesting the M0 helices may lock the channel in a closed conformation. Competition assays indicate that K+ has a greater effect on 86Rb flux than Na+, and the channel conducts K+ ions better than Na+ ions. The channel is unable to conduct Li+ or NMG+ (N-methyl-D-glucamine). Na+ and K+ ions bind at sites 3, 4 and the central cavity without preference, consistent with the non-selective nature of the channel.

### Structural basis of ion selectivity in K+ channels

Comparison of NaK and KcsA provides experimental demonstration that electrostatic repulsion between carbonyl oxygen atoms is not the origin of K+ over Na+ selectivity in K+ channels. Instead, protein atoms surrounding the ion-binding site must confer size-selectivity through geometric constraints. This resolved a long-standing debate about the mechanism of K+ selectivity. The structural differences between NaK and KcsA selectivity filters arise mainly from the last three residues, which have an r.m.s.d. of 2.1 A. The NaK filter superimposes with KcsA with an r.m.s.d. of 1.6 A in main-chain positions.

### Cyclic nucleotide-gated channel pore architecture

The NaK selectivity filter sequence (TVGDG or TVGDA in homologs) resembles that of cyclic nucleotide-gated (CNG) channels, which also lack the tyrosine and glycine residues from the conserved TVGYG sequence present in K+ channels. The NaK structure may represent the architecture of a CNG channel pore. CNG channels are non-selective and permeable to most group IA monovalent cations, consistent with the NaK channel properties. The external Ca2+-binding site in NaK reveals the structural basis of external divalent cation blockage observed in CNG channels, which is physiologically significant for visual transduction.

### Ion binding sites and divalent cation block

Electron density maps show ions binding at the extracellular entrance, along the selectivity filter, and in the central cavity. Monovalent cations (Na+, K+, Rb+, Cs+, Tl+) bind at sites 3, 4 and the central cavity, while divalent cations (Ca2+) bind only at the extracellular entrance to the filter. The Ca2+-binding site is formed by the four carbonyl oxygen atoms from Gly 67 residues. Divalent cations can bind at this position to block monovalent cation conduction, a property relevant to CNG channels. The NaK selectivity filter retains its proper conformation for ion conduction in both Na+ and K+ environments, unlike KcsA which requires K+ to stabilize the selectivity filter.

### Open conformation and inner helix bending at Gly87 gating hinge

The NaKN delta 19 structure reveals the intracellular gate in an open state. Inner helices develop a 34 degree bend at Gly87 (the conserved gating hinge) that splays the intracellular gate wide open, analogous to the open-pore structure of MthK. In addition to bending, the inner helices undergo a 45 degree clockwise twist around their helical axis. Outer helices tilt tangentially by about 11 degrees without twisting. The open NaK structure superimposes with MthK (PDB 1LNQ) with an r.m.s.d. of 0.74 A for all three components (outer, inner, and pore helices).

### Phe92 constriction point in open pore

In the open NaK pore, Phe92 forms a constriction point with an ion-pathway diameter of about 6.5 A — narrower than the open MthK channel (~9.5 A). In most other cation channels, the equivalent position to Phe92 is occupied by smaller residues (e.g., alanine in MthK). The F92A mutation increases the ion-conduction pathway diameter to 10.5 A and enhances ion conduction rates as measured by 86Rb flux assays. In the closed conformation, Phe92 from each inner helix forms hydrophobic contacts with a neighboring inner helix; upon opening, Phe92 swings toward the central ion-conduction pathway.

### Inter- and intrasubunit rearrangements during gating

Comparison of closed and open NaK structures reveals distinct rearrangements. Intrasubunit interactions between inner and outer helices remain similar. However, intersubunit interactions at the bundle crossing are disrupted upon pore opening. A major change occurs just above the bundle crossing: in the closed state, Phe92 contacts a hydrophobic patch on the neighboring helix; in the open state, the hydrophobic patch slides two helical turns and forms new van der Waals contacts with Phe85.

### Conservation of gating mechanics with K+ channels

The closed NaK structure (PDB 2AHY) superimposes well with closed KcsA (PDB 1K4C) with an r.m.s.d. of 0.73 A for inner and pore helices. The open NaKN delta 19 structure superimposes with open MthK (PDB 1LNQ) with an r.m.s.d. of 0.74 A. These structural correlations confirm that gating mechanics are conserved between NaK and K+ channels. Global twisting of inner helices (~42 degrees) matches the ~40 degree twisting motion observed in single-molecule KcsA studies.


## Cross-References

- [KcsA Potassium Channel](/xray-mp-wiki/proteins/kcsa/) — NaK shares high sequence homology and similar overall architecture with KcsA; structural comparison reveals selectivity filter differences
- [MthK (Methanobacterium thermoautotrophicum K+ Channel)](/xray-mp-wiki/proteins/mthk/) — Open NaK structure superimposes with open MthK (PDB 1LNQ, r.m.s.d. 0.74 A); MthK serves as model for open tetrameric cation channel pore
- [Dodecanoylmorpholine (DM)](/xray-mp-wiki/reagents/detergents/dodecanoylmorpholine/) — Detergent used for NaK channel purification and reconstitution into liposomes
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Crystallization buffer (100 mM, pH 9.5) for open NaK structure
- [2-Methyl-2,4-pentanediol (MPD)](/xray-mp-wiki/reagents/additives/mpd/) — Primary crystallization precipitant (55-70%) for open NaK channel
- [Calcium Chloride (CaCl2)](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Crystallization additive (1 mM) for open NaK structure
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Reconstitution buffer (10 mM, pH 7.4) for 86Rb flux assay
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Monovalent salt used in crystallization, purification, and flux assay buffers
- [Potassium Chloride (KCl)](/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/) — Monovalent salt used in crystallization and as the primary ion in 86Rb flux assay liposomes
- [POPE](/xray-mp-wiki/reagents/lipids/pope/) — Cationic lipid component (7.5 mg/mL) for NaK channel liposome reconstitution
- [POPG](/xray-mp-wiki/reagents/lipids/popg/) — Anionic lipid component (2.5 mg/mL) for NaK channel liposome reconstitution
- [Valinomycin](/xray-mp-wiki/reagents/ligands/valinomycin/) — K+ ionophore used for normalization in 86Rb flux assays
- [Sorbitol](/xray-mp-wiki/reagents/additives/sorbitol/) — Osmotic agent (400 mM) in 86Rb flux assay buffers
- [N-Methyl-D-Glucamine (NMG)](/xray-mp-wiki/reagents/additives/n-methyl-d-glucamine/) — Impermeant counter-ion (4 mM) in reconstitution and flux assay buffers
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method used for open NaK structure
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Structure determination method used for NaKN delta 19
- [Proteoliposome Reconstitution](/xray-mp-wiki/methods/proteoliposome-reconstitution/) — NaK channel reconstituted into POPE/POPG liposomes for flux assays
