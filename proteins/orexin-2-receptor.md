---
title: Human Orexin 2 Receptor
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.11.005, doi/10.1016##j.str.2022.11.001, doi/10.1021##acs.jmedchem.9b01787]
verified: false
---

# Human Orexin 2 Receptor

## Overview

The human orexin 2 receptor (OX2R, HCRTR2) is a class A GPCR that binds the neuropeptide orexin A and orexin B. It is a key regulator of the sleep-wake cycle and is expressed throughout the central nervous system. OX2R is a therapeutic target for insomnia, and subtype-selective antagonists (SORAs) and dual orexin receptor antagonists (DORAs) have been developed as sleep-promoting drugs. The crystal structures of OX2R bound to the subtype-selective antagonist EMPA were determined by both XFEL serial femtosecond crystallography (LCP-SFX) and synchrotron-based methods. A large set of 14 unique ligand-bound OX1R and OX2R co-crystal structures represents one of the most comprehensive structural sets currently available for a GPCR with diverse chemotypes, revealing that lipophilic hotspots drive GPCR ligand binding and water-mediated networks determine binding diversity and selectivity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2017.11.005 | 5WS3 | 2.30 A | C2 | Human OX2R with P. abyssi glycogen synthase (PGS) fusion in ICL3 (residues 255-293 replaced), N-terminal HA signal sequence, N-terminal FLAG tag, C-terminal His-tag. Full-length receptor sequence used. | EMPA |
| doi/10.1016##j.str.2017.11.005 | 5WQC | 1.96 A | C2 | Human OX2R with P. abyssi glycogen synthase (PGS) fusion in ICL3 (residues 255-293 replaced), N-terminal HA signal sequence, N-terminal FLAG tag, C-terminal His-tag. Full-length receptor sequence used. | EMPA |
| doi/10.1016##j.str.2022.11.001 | 7XRR | 2.89 A | P212121 | Human OX2R-i3d (ICL3 deletion), N-terminal HA signal sequence, N-terminal FLAG tag, C-terminal His10 tag. Asn202Gln glycosylation mutation. Crystallized without fusion partner. No PGS or BRIL fusion. | lemborexant |
| doi/10.1021##acs.jmedchem.9b01787 | 6M4W | 2.76 A | P212121 | OX2 StaR with 12 thermostabilizing mutations. C-terminal residues 389-444 removed, ICL3 replaced with P. abyssi glycogen synthase residues 218-413, N14D/N22D/N30D/N202D, C381W/C382W/C383W. Crystallized by LCP. | suvorexant |
| doi/10.1021##acs.jmedchem.9b01787 | 6M4X | 2.74 A | P212121 | OX2 StaR with 12 thermostabilizing mutations. Same as 6M4W. Crystallized by LCP. | EMPA |
| doi/10.1021##acs.jmedchem.9b01787 | 6M4Y | 2.61 A | P212121 | OX2 StaR with 12 thermostabilizing mutations. Same as 6M4W. Crystallized by LCP. | HTL6641 |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: OX2R-i3d (ICL3 deletion mutant). N-terminal HA signal sequence followed by FLAG epitope tag and HRV 3C protease cleavage site. C-terminal HRV 3C protease cleavage site followed by His10 tag. Asn202Gln glycosylation mutation. Cloned into pVL1393 baculovirus expression vector. Sf9 cells infected at 2.0-3.0 x 10^6 cells/mL, grown 60-72 hr at 27C, 125rpm.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell infection and membrane preparation | Baculovirus expression in Sf9 cells | -- | -- + -- | Cells infected at 2.0-3.0 x 10^6 cells/mL with baculovirus (1/200 media volume), grown 60-72 hr at 27C, 125rpm. Harvested by centrifugation (7,000 x g, 10 min, 4C), flash-frozen at -80C. |
| Membrane solubilization | Detergent solubilization | -- | 30 mM HEPES pH 7.5, 750 mM NaCl, 5 mM imidazole + 1% DDM, 0.2% sodium cholate, 0.3% CHS | Membranes solubilized 1 hr at 4C with 1% DDM, 0.2% sodium cholate, 0.3% CHS, 1 mg/mL iodoacetamide, and 10 uM lemborexant. Ultracentrifugation 30 min at 140,000 x g. |
| Ni-NTA affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA Sepharose Superflow (Qiagen) | 30 mM HEPES pH 7.5, 750 mM NaCl, 0.1% DDM, 0.02% sodium cholate, 0.03% CHS, 5 mM imidazole + 0.1% DDM | Binding overnight at 4C. Washed with 15 column volumes. Eluted with 500 mM imidazole. Supplemented with 2 mM CaCl2 for next step. |
| Anti-FLAG affinity chromatography | Anti-FLAG affinity chromatography | anti-FLAG M1 affinity resin (Sigma) | 30 mM HEPES pH 7.5, detergent gradually exchanged to 0.01% L-MNG + 0.01% L-MNG | Detergent gradually exchanged from DDM to 0.01% L-MNG on-column in presence of 50 uM lemborexant. Eluted with 0.2 mg/mL FLAG peptide, 5 mM EDTA, and 50 uM lemborexant. |
| Protease cleavage and SEC | HRV 3C protease cleavage followed by size-exclusion chromatography | -- | 50 mM HEPES pH 7.5, 150 mM NaCl, 0.01% L-MNG, 0.5 mM lemborexant + 0.01% L-MNG | HRV 3C protease and 0.5 mM lemborexant added overnight at 4C to cleave tags. Concentrated in 50 kDa cutoff Amicon Ultra concentrator and run on Superdex 200 Increase 10/300 GL column. |


## Crystallization

### doi/10.1016##j.str.2022.11.001

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization (no fusion partner) |
| Protein sample | OX2R-i3d-lemborexant complex in 0.01% L-MNG |
| Reservoir | not specified in paper |
| Temperature | 4 C |
| Growth time | not specified in paper |
| Cryoprotection | not specified in paper |
| Notes | Crystallized without fusion partner (no BRIL or PGS). Crystal contacts formed between N terminus (Leu43, Trp44, Tyr47) and ICL2 (His158, Pro159, Leu160), ECL2 (Thr195), ICL1 (His83) and TM4 (Arg168^4.41) and ICL3 (Gln254) of symmetric molecules. Optimal ICL3 deletion enabled crystal packing. PDB 7XRR, 2.89 A resolution, space group P212121. |

### doi/10.1021##acs.jmedchem.9b01787

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | OX2 StaR complex with ligand in LCP matrix |
| Lipid | Monoolein (MAG 8.7) |
| Temperature | 20 C |
| Notes | OX2 StaR crystallized in LCP with suvorexant (6M4W, 2.76 A), EMPA (6M4X, 2.74 A), and HTL6641 (6M4Y, 2.61 A). Structures solved by molecular replacement using OX1-suvorexant co-ordinates as search model. All structures display canonical 7TM arrangement and inactive receptor state hallmarks. |


## Biological / Functional Insights

### Lemborexant binding mode with unique hydrogen bonding

In OX2R bound by lemborexant, a hydrogen bond is formed between the nitrogen atom of
the carboxamide moiety of the ligand and the oxygen atom of the side chain of Gln134^3.32.
The amide group in the side chain of Gln134^3.32 is also hydrogen bonded to the fluorine
atom of the fluorophenyl group (halogen bond). These interactions distinguish lemborexant
from other orexin receptor ligands such as EMPA which binds through nonpolar interactions only.

### Pi-stacking interaction unique to lemborexant

A unique feature of lemborexant not found in other ligands was that the pyrimidine and
pyridine rings were stabilized within the molecule by pi-pi interactions, and this stack
was sandwiched by the side chains of His350^7.39 and Pro131^3.29. MD simulations showed
the two aromatic rings of lemborexant remained stacked for a long period in solution,
indicating the bound state conformation was pre-organized. This intramolecular stacking
contributes to favorable entropy of binding.

### Binding mode differences between lemborexant and suvorexant

Lemborexant and suvorexant bind to the same pocket in OX2R but with different binding
modes. The pi-pi interaction between the two-ring system of lemborexant does not exist
in suvorexant, as the 1,4-diazepane linking the two ring structures of suvorexant are
not optimized for proper ring stacking. Hydrogen bonding with Gln134^3.32 was observed
in lemborexant but not suvorexant, while hydrogen bonding between Asn324^6.55 and
suvorexant was noticed. The contact surface area was 607.8 A^2 for lemborexant and
641.3 A^2 for suvorexant.

### Subtype selectivity determined by Gln134 conformation

The conformation of Gln134^3.32 in OX2R (vs Gln125 in OX1R) and Thr135^3.33 in OX2R
(vs Ala127 in OX1R) determines the binding mode and selectivity of lemborexant. The
binding mode of lemborexant differs between OX1R and OX2R due to different Gln3,32
conformations. The T135A mutant reduced binding by more than 10-fold compared to
wild-type OX2R.

### HTL6641 binds without intramolecular pi-stacking

HTL6641 binds to OX2R in a departure from the horseshoe conformation seen with other
DORAs. Instead of intramolecular pi-stacking, the aromatic portion of the central core
and the benzyl substituent form an aromatic offset and edge-face pi-stacking clamp
around F227^5.42. One sulfonamide oxygen forms a direct hydrogen bond with Q187^4.60,
and the pyridine nitrogen forms a hydrogen bond with N324^6.55. The dimethoxypyridyl
group occupies the same region as the benzoxazole of suvorexant but sits higher in
the orthosteric pocket.


## Cross-References

- [Lemborexant](/xray-mp-wiki/reagents/ligands/lemborexant/) — Co-crystallized dual orexin receptor antagonist in PDB 7XRR
- [Suvorexant](/xray-mp-wiki/reagents/ligands/suvorexant/) — Dual orexin receptor antagonist; suvorexant-OX2R structure (PDB 6M4W) compared with lemborexant-OX2R
- [EMPA](/xray-mp-wiki/reagents/ligands/empa/) — OX2R-selective antagonist; OX2R structures at 2.74 A (6M4X) and 1.96 A (5WQC)
- [Human Orexin 1 Receptor](/xray-mp-wiki/proteins/orexin-1-receptor/) — OX1R compared extensively; subtype selectivity determined by structural differences
- [HTL6641](/xray-mp-wiki/reagents/ligands/htl6641/) — Dual orexin receptor antagonist; OX2R structure (PDB 6M4Y) shows distinct binding mode
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Primary detergent used in OX2R final purification and crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Initial solubilization detergent for OX2R
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — OX2 StaR structures crystallized in LCP using monoolein (MAG 8.7)
