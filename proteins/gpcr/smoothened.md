---
title: "Mouse Smoothened (SMO) — Class F GPCR"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein]
sources: [doi/10.1038##s41586-019-1355-4]
verified: false
---

# Mouse Smoothened (SMO) — Class F GPCR

## Overview

Smoothened (SMO) is a seven-transmembrane (7TM) oncoprotein and member of the class F G protein-coupled receptor (GPCR) superfamily that serves as the central signal transducer in the Hedgehog (Hh) signalling pathway. Hh proteins bind to and inhibit the transmembrane cholesterol transporter Patched-1 (PTCH1), which permits activation of SMO. The crystal structure of active mouse SMO (mSMO) bound to the agonist SAG21k and a conformation-specific nanobody (NbSmo8) was determined at 2.8 Å resolution (PDB 6O3C), revealing a cholesterol molecule bound deep within the 7TM pocket that is critical for SMO activation. Activation involves outward displacement of TM6 (8 Å), inward movement of TM5 (6 Å), and upward displacement of TM6 and ECL3. The structure identified a hydrophobic tunnel between TM5 and TM6 connecting the inner membrane leaflet to the 7TM sterol site, providing a direct link between the cholesterol transporter-like activity of PTCH1 and SMO regulation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-019-1355-4 | 6O3C | 2.80 | P2221 | Mouse SMO residues 64-566 with N-terminal HA signal sequence, Flag tag, streptavidin binding peptide, TEV site, and C-terminal Gαo fusion; complexed with SAG21k agonist and NbSmo8 nanobody | SAG21k, cholesterol (7TM site), cholesterol (CRD site) |

## Expression and Purification

- **Expression system**: HEK293S GnTI- cells (BacMam expression system) with 10 mM sodium butyrate; also in Sf9 insect cells for nanobody generation
- **Construct**: Wild-type mouse Smo gene residues 64-566, N-terminal HA/Flag/SBP/TEV tag, C-terminal sortase-3C-Gαo fusion

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Membrane solubilization | [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/[CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) extraction | — | 50 mM HEPES pH 7.5, 300 mM NaCl, 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 5 mM MgCl2, 20 mM KCl, 5 mM ATP, 1 µM vismodegib | Solubilization from frozen cell pellets for 1 h at 4°C |
| 2. Affinity purification | M1 anti-[FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) antibody Sepharose | — | 50 mM HEPES pH 7.5, 300 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Detergent exchange to 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.001% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), ligand exchange from vismodegib to SAG21k on-column |
| 3. Elution and deglycosylation | [FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) peptide elution + endoglycosidase treatment | — | 50 mM HEPES pH 7.5, 150 mM NaCl, 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.001% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 1 pM SAG21k | Deglycosylated with endoglycosidase F1 and H for 30 min at RT |
| 4. Nanobody complex formation | 3-fold molar excess NbSmo8 incubation | — | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.001% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Overnight incubation at 4°C |
| 5. Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) Increase 10/300 GL | — | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.1 pM SAG21k, 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.001% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Peak fractions concentrated to 50 mg/ml for crystallization |

**Final sample**: SMO-SAG21k-NbSmo8 complex at 50 mg/ml


## Crystallization

### doi/10.1038##s41586-019-1355-4

| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) |
| Protein sample | SMO-SAG21k-NbSmo8 complex at 50 mg/ml in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/0.001% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |
| Temperature | 4°C for 10 days, then 20°C for 10 days |
| Notes | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) formed with 90% 9.9 MAG (monoolein) / 10% cholesterol. Data merged from 20 crystals. Structure solved by molecular replacement using hSMO (5L7D) and Nb6B9 (4LDE). Final Rwork/Rfree 24.5%/29.4%. Data collected at APS beamlines 23-ID-B and 23-ID-D. |


## Biological / Functional Insights

### 7TM sterol binding site is critical for SMO activation

A cholesterol molecule was identified deep within the 7TM core of active SMO. The 7TM-bound cholesterol stabilizes the outward displacement of TM6, analogous to agonist action in other GPCRs. Mutations lining the 7TM site (V333F, V408F, I412F, T470Q) ablated GLI activation by SAG21k and Sonic hedgehog. Cholesterol delivered via methyl-β-cyclodextrin activated GLI, and this was fully lost in V333F and T470Q mutants. In cholesterol-laden micelles, NbSmo8 bound wild-type SMO but not V333F SMO.

### Hydrophobic tunnel for sterol access

A hydrophobic tunnel between TM5 and TM6 opens to the inner leaflet of the membrane bilayer, providing a conduit for sterols to reach the deep 7TM site without desolvation from the membrane. Mutations occluding the tunnel entrance (A463F) rendered SMO unresponsive to ShhNp stimulation. The structurally observed tunnel is almost identical to one recently observed in Xenopus SMO.

### CRD sterol binding and allosteric communication

Active SMO binds a second sterol within the conserved CRD lipid-binding site. A resolved N-acetyl glucosamine on N497 forms part of the CRD sterol pocket and relays sterol binding to ECL3. The entire ECL3-TM6 helix is displaced 3 Å upward compared to inactive SMO, illustrating allosteric communication between three distinct binding sites: the deep 7TM sterol pocket, the SAG21k/cyclopamine site, and the CRD sterol pocket.

### NbSmo8 nanobody enables active state capture

A conformation-specific nanobody (NbSmo8) was developed using yeast surface display, selectively binding agonist-occupied SMO but not apo or antagonist-occupied SMO. NbSmo8 recognized a unique 3D epitope with CDR3 reaching deep inside the active SMO cavity to stabilize the outwardly displaced TM6 conformation. In cellular imaging, NbSmo8-GFP plasma membrane recruitment faithfully reflected SMO activation state.

### Relationship to SMO inhibitor resistance

Several clinically observed SMO resistance mutations map to the 7TM sterol pocket. SANT-1 extensively overlaps with 7TM cholesterol binding, and antagonists that are isosteric with 7TM cholesterol may be less susceptible to resistance mutations, since mutations blocking antagonist binding would also prevent sterol binding and SMO activation.


## Cross-References
