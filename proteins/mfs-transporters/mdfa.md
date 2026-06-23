---
title: Multidrug Transporter MdfA (E26T/D34M/A150E) from Escherichia coli
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##s41598-020-60332-8]
verified: false
---

# Multidrug Transporter MdfA (E26T/D34M/A150E) from Escherichia coli

## Overview

[MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) is a prototypical H+-dependent multidrug transporter from Escherichia coli belonging to the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/)), specifically the drug/H+ antiporter-1 (DHA1) subfamily. It exports physicochemically diverse substrates by utilizing the H+ electrochemical gradient. This work describes the X-ray structures of a redesigned [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) triple mutant (E26T/D34M/A150E) wherein the substrate-binding and protonation sites were rearranged while retaining multidrug transport function. Structures bound to [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/) (Cm), [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/) ([DXC](/xray-mp-wiki/reagents/additives/deoxycholate/)), and lauryldimethylamine N-oxide ([LDAO](/xray-mp-wiki/reagents/detergents/ldao/)) reveal intermediate states during antibiotic recognition and suggest structural changes accompanying substrate-evoked deprotonation, highlighting the remarkable mechanistic flexibility in drug/H+ coupling.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41598-020-60332-8 | 6VRZ | 2.0 | — | E26T/D34M/A150E triple mutant with C-terminal deca-histidine tag (thrombin-cleaved) | [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/) (Cm) |
| doi/10.1038##s41598-020-60332-8 | 6VS2 |  | — | E26T/D34M/A150E triple mutant | [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/) (Cm) |
| doi/10.1038##s41598-020-60332-8 | 6VS0 |  | — | E26T/D34M/A150E triple mutant | [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/) ([DXC](/xray-mp-wiki/reagents/additives/deoxycholate/)) |
| doi/10.1038##s41598-020-60332-8 | 6VS1 | 3.0 | — | E26T/D34M/A150E triple mutant | [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) |

## Expression and Purification

- **Expression system**: E. coli BL21 (DE3) ΔacrABΔmacABΔyojHI
- **Construct**: E26T/D34M/A150E triple mutant in modified pET28b with C-terminal cleavable deca-histidine tag
- **Notes**: Induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 30°C for 4 h in LB media

### Purification Workflow

- **Expression system**: E. coli BL21 (DE3) ΔacrABΔmacABΔyojHI
- **Expression construct**: E26T/D34M/A150E with C-terminal deca-histidine tag
- **Tag info**: Deca-histidine tag (C-terminal, removed by thrombin)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French pressure cell | — |  | Multiple passages through pre-chilled French press |
| Membrane extraction | Solubilization | — | 20 mM HEPES-NaOH pH 7.5, 500 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1.5 mM TCEP + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membranes collected by ultracentrifugation at 100,000g |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Ni-NTA column | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 1.5 mM TCEP | Eluted with 450 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag removal | Thrombin cleavage | — |  | Incubated with thrombin overnight to remove deca-histidine tag |
| Size-exclusion chromatography | SEC ([Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/)) | — | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.2% NG, 0.025% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), 0.05% [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/), 1.5 mM TCEP |  |

**Final sample**: ~10 mg/mL in crystallization buffer


## Crystallization

### doi/10.1038##s41598-020-60332-8

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | ~10 mg/mL E26T/D34M/A150E in 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.2% NG, 0.025% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), 0.05% [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/), 1.5 mM TCEP |
| Reservoir | 100 mM MES-NaOH pH 6.0, 150 mM NaCl, 150 mM MgCl2, 20 mM Pr(OAc)3 |
| Temperature | 24 |
| Notes | 10 µL hanging drops with equal volumes of protein and reservoir. Crystals obtained at pH 8.0 (Cm-bound), pH 5.0 (Cm-bound), pH 6.0 (DXC-bound), and pH 8.0 (LDAO-bound). Phase solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) combined with SAD phasing. |


## Biological / Functional Insights

### Polyspecific multidrug recognition via a large binding pocket

E26T/D34M/A150E uses a large, voluminous substrate-binding pocket (~3000 Å³) to interact with physicochemically disparate drugs. Substrates such as Cm, [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/), and [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) bind in partially overlapping sites using only a small set (typically ≤3) of H-bonding interactions, contrasting with the extensive H-bonding networks of substrate-specific [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) transporters like LacY. Most interactions are van der Waals and charge-charge in nature, enabling substantial flexibility in substrate recognition.

### Direct-competition-based drug/H+ coupling mechanism

A150E serves as the protonation site in E26T/D34M/A150E. Electroneutral Cm and anionic [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/) trigger deprotonation by forming a direct H-bond with the side-chain carboxylate of A150E. Zwitterionic [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) promotes deprotonation through long-range charge-charge interactions (4.3 Å between [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) N1 and A150E carboxylate). All three substrates induce stoichiometric release of one proton per protein molecule.

### Fully loaded intermediate state captured

A Cm-bound, protonated structure of E26T/D34M/A150E (at pH 5.0) represents a fully loaded intermediate where both substrate and proton are bound simultaneously. This was unexpected since substrate and H+ binding to [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) was believed to be mutually exclusive, suggesting that drug-induced deprotonation involves more intermediate states than previously envisioned.

### Structural changes accompanying deprotonation

Comparison of Cm-bound structures at pH 8.0 (deprotonated) and pH 5.0 (protonated) reveals structural changes in the transporter, particularly in Y30 and the nitryl group of Cm. As the transporter transitions from the low to high pH state, Cm forms a direct H-bond with A150E, and the nitryl group of Cm interacts with the edge of the Y30 aromatic ring. These changes have not been observed in the Q131R [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) variant.


## Cross-References

- [DDM (n-Dodecyl-β-D-Maltopyranoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for membrane extraction and initial purification
- [LDAO (Lauryldimethylamine N-oxide)](/xray-mp-wiki/reagents/detergents/ldao/) — Co-detergent in SEC buffer and co-crystallization ligand/substrate
- [Deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/) — Co-detergent/additive in SEC buffer and co-crystallization substrate
- [Chloramphenicol](/xray-mp-wiki/reagents/ligands/chloramphenicol/) — Primary substrate used for co-crystallization at pH 8.0 and pH 5.0
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Used in protein purification and crystallization buffer at pH 8.0
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Used in membrane extraction and Ni-NTA purification at pH 7.5
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — Used in crystallization reservoir at pH 6.0
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method used for all MdfA structures
- [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
