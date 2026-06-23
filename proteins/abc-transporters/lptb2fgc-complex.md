---
title: "LptB2FGC LPS Transport Complex from Enterobacter cloacae and Vibrio cholerae"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-019-1039-0]
verified: false
---

# LptB2FGC LPS Transport Complex from Enterobacter cloacae and Vibrio cholerae

## Overview

The LptB2FGC complex is the inner membrane component of the lipopolysaccharide (LPS) transport machinery in Gram-negative bacteria, comprising an ABC transporter (LptB2FG) and an accessory protein LptC. This complex powers the unidirectional extraction of LPS from the inner membrane and its transfer to the periplasmic bridge protein LptA, which ultimately delivers LPS to the outer membrane translocon LptDE. Crystal structures of the LptB2FGC complex from Enterobacter cloacae (3.2 A, PDB 6MIT) and Vibrio cholerae (2.85 A, PDB 6MJP) reveal that LptC inserts a single transmembrane helix between LptG TM1 and LptF TM5, breaking the pseudosymmetry of the transporter and defining a single pathway for LPS entry into the cavity. ATP binding and hydrolysis by the cytoplasmic ATPase LptB provides the energy to extract LPS from the membrane, while a gate in the beta-jellyroll domain of LptF prevents backward movement, ensuring unidirectional transport.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-019-1039-0 | 6MIT | 3.2 A | P212121 | E. cloacae LptB2FGC complex, LptC with C-terminal thrombin cleavage site and hepta-histidine tag | Novobiocin (involved in crystal contacts only) |
| doi/10.1038##s41586-019-1039-0 | 6MJP | 2.85 A | P212121 | V. cholerae LptB(E163Q)2FGC complex (catalytically inactive ATPase mutant), LptC with C-terminal thrombin cleavage site and hepta-histidine tag | AMPPNP (non-hydrolysable ATP analog) |

## Expression and Purification

- **Expression system**: E. coli C43
- **Construct**: LptB and LptFG cloned into pCDFduet; LptC with C-terminal thrombin-his7 tag in pBADHisA. Co-transformed into C43 E. coli.
- **Induction**: 200 uM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) + 0.02% L-arabinose for 12 h at 30 C for E. cloacae; 20 C for V. cholerae in LB
- **Media**: M9 minimal media with trace elements, carbenicillin (50 ug/mL), spectinomycin (50 ug/mL) for E. cloacae; LB for V. cholerae

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex C3 homogenizer (3x passes at 15,000 psi) | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl, 0.2 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 1 mM PMSF, lysozyme (100 ug/mL), DNAse I (50 ug/mL), cOmplete protease inhibitors | Debris removed by 12,000 x g spin; membranes pelleted at 100,000 x g for 1 h |
| Membrane solubilization | Detergent solubilization | — | 20 mM Tris pH 7.4, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM MgCl2, cOmplete protease inhibitors + 1% w/v [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Supplemented with 2 mM ATP; rocked at 4 C for 2 h |
| Ni-NTA affinity | Ni-NTA agarose gravity flow | — | 20 mM Tris pH 7.4, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Washed with 20 CV of 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), then 30 CV wash buffer |
| Gel filtration | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) Increase 10/300 | 300 mM NaCl, 20 mM Tris pH 7.4, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Supplemented with 0.5 mM THP. Tag cleaved with thrombin, then flowed through Ni-NTA to remove uncleaved protein |
| Tag removal | Thrombin cleavage | — |  | Incubated overnight at 4 C with restriction grade thrombin; removed by passing through Ni-NTA with 8 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |

**Final sample**: 10-15 mg/mL in gel filtration buffer using 100-kDa cut-off concentrator


## Crystallization

### doi/10.1038##s41586-019-1039-0

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | E. cloacae LptB2FGC at 14 mg/mL, supplemented with 2 mM Na-novobiocin |
| Reservoir | 500 mM Li2SO4, 100 mM MES pH 6.5, 21% v/v [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Temperature | 4 C |
| Growth time | 3 weeks |
| Cryoprotection | Stepwise dehydration by increasing [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) concentration by 2% per day to 35%; crystals frozen directly from drops |
| Notes | Streak-seeding improved crystal morphology. Novobiocin involved in crystal contacts only, not in a functionally significant site. |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | V. cholerae LptB(E163Q)2FGC at 10 mg/mL with 2 mM AMPPNP |
| Reservoir | 200 mM CaCl2, 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.5, 40% v/v [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Temperature | 20 C |
| Growth time | 1-6 weeks |
| Cryoprotection | Cryo-solution of 41% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 200 mM CaCl2, 300 mM NaCl, 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.5 |
| Notes | Long, fragile plate crystals. Crystals also obtained with wild-type protein and AMPPNP. |


## Biological / Functional Insights

### LptC inserts a transmembrane helix into the transporter core, breaking pseudosymmetry

LptC, an accessory protein with a single transmembrane helix, inserts this helix between LptG TM1 and LptF TM5 in the ABC transporter, breaking the two-fold pseudosymmetry of the LptB2FG core. This defines a single entry path for LPS between LptG TM1 and LptF TM5, while the alternate path (between LptG TM5 and LptF TM1) is blocked by the convex surface of the LptC-LptF beta-jellyroll. No other ABC system incorporates a transmembrane helix from a separate protein directly into the transporter core.

### ATP-independent entry into the cavity

LPS entry into the transporter cavity does not require ATP hydrolysis. Crosslinking experiments showed LPS binding at the base of the cavity (near LptC TM helix) in both active and inactive (LptB E163Q) complexes. However, ATP-dependent extraction moves LPS from the membrane into the beta-jellyroll domain of LptF and LptC. This two-step mechanism separates substrate entry from energy-dependent translocation.

### LptF gate prevents backward LPS flow

The beta-jellyroll domain of LptF exists in two conformations: open (E. cloacae structure) and closed (V. cholerae structure). A disulfide crosslink trapping LptF in the closed state prevented LPS transport but not ATP hydrolysis, demonstrating that gate-opening is not directly coupled to ATP hydrolysis. Gate closure behind the substrate provides a mechanism to prevent backward flow when the cavity reopens, ensuring unidirectional transport.

### LptC TM helix modulates ATPase efficiency

The LptC TM helix coordinates ATP hydrolysis with LPS extraction from the membrane. Complexes with Delta-TM LptC showed substantially higher ATPase activity compared to full-length LptB2FGC, yet supported comparable LPS transport to LptA. This suggests the TM domain of LptC modulates ATP hydrolysis to achieve more efficient coupling of ATP consumption and LPS movement, providing a fitness advantage that is conserved in the wild.

### Structural model of LPS transport

(1) Newly synthesized LPS binds at the entry point defined by the LptC TM segment intercalated between LptG TM1 and LptF TM5. (2) ATP-independent entry of LPS into the cavity occurs past the LptC TM segment. (3) ATP-dependent cavity constriction provides the force to push LPS out of the membrane. (4) The LptC TM helix coordinates ATP hydrolysis with membrane extraction. (5) The LptF beta-jellyroll gate closes behind the substrate, preventing backward flow. (6) LPS moves from LptC to LptA and through LptDE to the outer membrane.


## Cross-References

- [LPS Transport](/xray-mp-wiki/concepts/lps-transport/) — LptB2FGC is the inner membrane motor for LPS transport in Gram-negative bacteria
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA affinity chromatography used for purification of His-tagged complex
- [Hanging Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — E. cloacae LptB2FGC crystallized by hanging-drop vapor diffusion
- [Sitting Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — V. cholerae LptB2FGC crystallized by sitting-drop vapor diffusion
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
