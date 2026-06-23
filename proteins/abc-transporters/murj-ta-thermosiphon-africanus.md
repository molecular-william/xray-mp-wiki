---
title: MurJ from Thermosiphon africanus (MurJ_TA) — Lipid II Flippase
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, enzyme]
sources: [doi/10.1038##nsmb.3346]
verified: false
---

# MurJ from Thermosiphon africanus (MurJ_TA) — Lipid II Flippase

## Overview

[MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/) from Thermosiphon africanus (MurJ_TA) is a lipid II flippase belonging to the multidrug/oligosaccharidyl-lipid/polysaccharide (MOP) transporter superfamily. [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/) flips the peptidoglycan precursor lipid II from the cytoplasmic leaflet to the periplasmic leaflet of the bacterial inner membrane, a critical step in peptidoglycan biogenesis. The crystal structure of MurJ_TA was solved at 2.0 A resolution in an inward-facing conformation, revealing a large central cavity divided into a cationic proximal site and a distal site, connected to a hydrophobic groove formed by two C-terminal transmembrane helices (TMs 13-14) that accommodates the undecaprenyl tail of lipid II.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.3346 | 5T77 | 2.0 | C2 | Full-length [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/) (residues 1-475) from Thermosiphon africanus with N-terminal His10-MBP tag removed by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) | Chloride ion, [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |

## Expression and Purification

- **Expression system**: Escherichia coli C41(DE3)
- **Construct**: His10-MBP-PPX-MurJ-PPX-His10 (N-terminal His10-MBP tag and C-terminal His10 tag, both cleavable by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/))
- **Notes**: SeMet-labeled protein expressed in B834(DE3) by autoinduction with 125 mg/L L-[Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/)
- **Induction**: 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600 0.8
- **Media**: Terrific broth (LB for autoinduction with [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/))

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer | Not specified | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl | Including 10 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 1 ug/mL leupeptin, 1 ug/mL pepstatin, 5 uU/mL aprotinin, 20 ug/mL DNase I, 2.5 mM PMSF |
| Membrane extraction | Detergent solubilization | Not specified | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + 30 mM n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Stirring for 1 h at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (IMAC) | [TALON](/xray-mp-wiki/reagents/additives/talon/) Cobalt resin | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl, 15 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Wash buffer: 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 15 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/). Eluted with 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/). Incubated overnight with 40 ug/mL [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) and 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/). |
| Size-exclusion chromatography | Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 2 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/) + 0.3 mM decyl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol ([DMNG](/xray-mp-wiki/reagents/detergents/dmng/)) | Final purification step; detergent exchanged from [DDM](/xray-mp-wiki/reagents/detergents/ddm/) to [DMNG](/xray-mp-wiki/reagents/detergents/dmng/) |


## Crystallization

### doi/10.1038##nsmb.3346

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | MurJ_TA at 15 mg/mL in 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 2 mM TCEP, 0.3 mM [DMNG](/xray-mp-wiki/reagents/detergents/dmng/) |
| Temperature | Room temperature |
| Notes | Protein mixed with molten [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) in 2:3 (w/w) protein:lipid ratio. 150 nL LCP drops overlaid with 1 uL precipitant. Crystals grew to full size in 4 weeks. Native crystals supplemented with 1.5 mM lipid II in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/). |


## Biological / Functional Insights

### Inward-facing conformation of a MOP transporter

The structure of MurJ_TA represents the first structure of a MOP transporter captured in an inward-facing conformation, contrasting with the outward-facing V-shape observed in MATE transporters. The N-lobe (TMs 1-6) and C-lobe (TMs 7-14) are arranged in an inward-facing N-shape. TM7 is bent by approximately 45 degrees about Ser228, which likely acts as a hinge for the rocker-switch motion between inward- and outward-facing states.

### Substrate recognition and binding

A hydrophobic groove formed by C-terminal TMs 13-14 binds the undecaprenyl tail of lipid II. The groove connects via a membrane portal (between TMs 1 and 8) to a large central cavity. The proximal site of the cavity is highly cationic (Arg18, Arg24, Arg52, Arg255), serving to recognize the diphosphate and sugar moieties of lipid II. A chloride ion was observed in the proximal site. The distal site accommodates the pentapeptide moiety.

### Alternating-access rocker-switch mechanism

Based on the inward-facing structure, MTSES accessibility data, and an outward-facing homology model, a rocker-switch mechanism was proposed for lipid II flipping. The N-lobe and C-lobe rotate about a TM7 hinge (Ser228), translocating lipid II across the membrane. The hydrophobic groove retains the undecaprenyl tail during the transition. This mechanism differs from the [PGLK](/xray-mp-wiki/proteins/abc-transporters/pglk/) flippase which operates via only an outward-facing state.


## Cross-References

- [MOP Transporter Superfamily](/xray-mp-wiki/concepts/mop-transporter-superfamily/) — MurJ is a member of the MOP superfamily, specifically the MVF family
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used for membrane extraction of MurJ_TA
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Host lipid for LCP crystallization
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Used throughout purification and crystallization buffers
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/) — Related protein structure
- [PGLK](/xray-mp-wiki/proteins/abc-transporters/pglk/) — Related protein structure
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) — Additive used in purification or crystallization buffers
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
