---
title: Delta14-sterol reductase MaSR1 from Methylomicrobium alcaliphilum
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13797]
verified: false
---

# Delta14-sterol reductase MaSR1 from Methylomicrobium alcaliphilum

## Overview

MaSR1 is a Delta14-sterol reductase from the methanotrophic bacterium Methylomicrobium alcaliphilum 20Z, a homologue of human C14SR (TM7SF2), LBR (lamin B receptor) and DHCR7 (7-dehydrocholesterol reductase). The structure, determined at 2.6 A resolution, reveals ten transmembrane segments (TM1-10) with the catalytic domain comprising the C-terminal half (TM6-10). The enzyme contains two interconnected pockets: one facing the cytoplasm that houses the NADPH cofactor, and another accessible from the lipid bilayer for sterol substrate binding. MaSR1 can reduce the double bond of a [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) biosynthetic intermediate, demonstrating functional conservation with human C14SR.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13797 | unknown | 2.6 | unknown | Full-length MaSR1 with N-terminal 8-His tag, NADPH-bound | NADPH |

## Expression and Purification

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: MaSR1 from Methylomicrobium alcaliphilum 20Z (NCBI GI: 503913803), cloned into pET-21b with N-terminal 8-His tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | French press cell disruption and differential centrifugation | -- | 25 mM Tris-Cl pH 8.0, 150 mM NaCl + -- | Two passes at 15,000 p.s.i.; low-speed spin followed by high-speed ultracentrifugation |
| Membrane solubilization | Detergent solubilization | -- | 25 mM Tris-Cl pH 8.0, 150 mM NaCl + 2% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Incubated for 1 h at 4 C; then centrifuged to obtain solubilized fraction |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni2+-NTA agarose (Qiagen) | 25 mM Tris-Cl pH 8.0, 150 mM NaCl + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in same buffer |
| Size-exclusion chromatography | Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (GE Healthcare) | 25 mM Tris-Cl pH 8.0, 150 mM NaCl + 0.4% beta-NG ([NG](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/)) | Peak fraction collected for crystallization |


## Crystallization

### doi/10.1038##nature13797

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | MaSR1 in 25 mM Tris-Cl pH 8.0, 150 mM NaCl, 0.4% beta-NG, 2 mM NADPH |
| Reservoir | 0.1 M Tris-Cl pH 7.0, 0.2 M NH4Ac, 30% (v/v) pentaerythritol ethoxylate (15/4 EO/OH) |
| Temperature | 20 C |
| Growth time | 5 days |
| Cryoprotection | Direct flash-freezing in cold nitrogen stream at 100 K |
| Notes | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) added to crystallization buffer at 1% (v/v) final concentration to improve diffraction. SeMet-labelled protein crystallized in same buffer plus 6 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/). Platinum derivatives obtained by soaking native crystals for 12 h in mother liquor plus 10 mg/ml K2Pt(NO2)4. |


## Biological / Functional Insights

### Two-pocket catalytic architecture

The C-terminal half (TM6-10) of MaSR1 contains two interconnected pockets. The NADPH-binding pocket faces the cytoplasm and houses the adenine-ribose moiety of NADPH (the nicotinamide ring is disordered in the absence of substrate). The sterol-binding pocket is accessible from the lipid bilayer. The reducing end of NADPH meets the sterol substrate at the juncture of the two pockets.

### Signature motif for sterol recognition

The sterol binding pocket contains a signature motif of Tyr241 bonded to Asp363 that forms triangular hydrogen bonds coordinating the beta-3 hydroxyl of the sterol substrate. This is analogous to Tyr58-Glu120 in soluble steroid 5-beta-reductase (AKR1D1). The Y241F/D363A double mutant loses sterol reductase activity.

### Disease relevance

Mutations in human homologues LBR and DHCR7 cause genetic diseases including Pelger-Huet anomaly (PHA), Greenberg skeletal dysplasia (HEM), and Smith-Lemli-Opitz syndrome (SLOS). Structural models based on MaSR1 map these disease mutations to the sterol reductase catalytic domain, affecting cofactor binding or sterol entry/binding sites.

### Structural homology with ICMT

A DALI search identified isoprenylcysteine carboxyl methyltransferase (ICMT, PDB 4A2N) as the closest structural homologue for the TM6-10 segments, suggesting a similar role for the C14SR domain of LBR in recognizing farnesylated cysteine substrates such as prelamin A or lamin B.

### Substrate promiscuity

MaSR1 can reduce the double bond of both C27Delta8,14 (a [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) intermediate) and yeast ergosta-8,14-dien-ol, demonstrating broad substrate recognition consistent with LBR which compensates for C14SR function in knockout mice.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane protein solubilization
- [n-Octyl-beta-D-glucopyranoside (OG/beta-NG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in final purification and crystallization
- [NADPH](/xray-mp-wiki/reagents/ligands/nadph/) — Reducing cofactor bound in the NADPH-binding pocket
- [Nickel-NTA Affinity Chromatography](/xray-mp-wiki/methods/purification/nickel-nta-affinity-chromatography/) — Primary purification method via His-tag
- [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final purification step on Superdex-200
- [Dithiothreitol (DTT)](/xray-mp-wiki/reagents/additives/dtt/) — Reducing agent used in SeMet crystallization
- [ICMT from beetles](/xray-mp-wiki/proteins/enzymes/beetle-icmt/) — Closest structural homologue identified by DALI search
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
