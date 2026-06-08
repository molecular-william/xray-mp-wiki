---
title: EspB
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jsb.2015.06.003]
verified: false
---

# EspB

## Overview

EspB is a secreted virulence factor from Mycobacterium tuberculosis, encoded within the ESX-1 (type VII secretion) locus and classified as one of the Esp (ESX-secreted protein) family. EspB contains a unique PE-PPE fusion architecture in its N-terminal domain, adopting an elongated all-helical fold that structurally resembles the PE25-PPE41 heterodimer despite limited sequence similarity. The mature secreted form is a 50 kDa protein resulting from proteolytic cleavage of the C-terminal domain by the MycP1 serine protease. EspB forms oligomeric donut-shaped particles and has been shown to bind phospholipids including phosphatidylserine and phosphatidic acid. EspB is required for host-cell death, phagosomal escape, and co-dependent secretion of ESAT-6/CFP-10.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jsb.2015.06.003 | 4XWP | 1.82 A | C2221 | EspB residues 7-278 (PE-PPE domains only), N-terminal His6-tag with TEV cleavage site | None |
| doi/10.1016##j.jsb.2015.06.003 | 4XXX | 1.5 A | C2221 | EspB residues 7-278 (PE-PPE domains only), N-terminal His6-tag with TEV cleavage site | None (crystallized with phosphatidylserine additive but no lipid observed in structure) |
| doi/10.1016##j.jsb.2015.06.003 | 4XXN | 2.14 A | I222 | EspB residues 7-278 (PE-PPE domains only), N-terminal His6-tag with TEV cleavage site | None |
| doi/10.1016##j.jsb.2015.06.003 | 4XY3 | 3.04 A | Not specified | Full-length EspB residues 1-460 | None |

## Expression and Purification

- **Expression system**: Escherichia coli Rosetta2(DE3)
- **Construct**: EspB residues 7-278 cloned into modified pET-28b vector with N-terminal His6-tag and TEV protease cleavage site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Cell disruption | -- | 20 mM Tris pH 8.5, 300 mM NaCl, 10 mM imidazole + -- | Cells resuspended and passed five times through cell disrupter at 4 C |
| Affinity purification | Affinity chromatography | Ni-NTA column | 20 mM Tris pH 8.5, 300 mM NaCl, 20 mM imidazole (wash); gradient to 250 mM imidazole (elution) + -- | Lysate applied to pre-equilibrated Ni-NTA column; EspB eluted in gradient with imidazole |
| Tag cleavage | Proteolytic cleavage | -- | 20 mM HEPES pH 7.5, 300 mM NaCl + -- | Cleaved protein dialysed overnight at 4 C with TEV protease |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex200 16/30 column | 20 mM HEPES pH 7.5, 100 mM NaCl + -- | Protein concentrated to 10 mg/mL; purity >90% |


## Crystallization

### doi/10.1016##j.jsb.2015.06.003

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | EspB7-278 at 10 mg/mL |
| Reservoir | 0.2 M calcium acetate, 0.1 M Tris-HCl, 20% PEG3000 |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Reservoir mother liquor supplemented with 25% glycerol; flash cooled in liquid nitrogen |
| Notes | Space group C2221; structure refined to 1.82 A resolution (Rwork 0.199, Rfree 0.234); molecular replacement using PE25-PPE41 heterodimer (PDB 2G38) as search model; loop residues 86-115 and 125-130 missing due to disorder |

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | EspB7-278 at 10 mg/mL with 1 mM L-alpha-phosphatidylserine additive |
| Reservoir | 0.2 M potassium dihydrogen phosphate, 20% w/v PEG3350 |
| Temperature | 291 K |
| Growth time | Not specified |
| Cryoprotection | Reservoir mother liquor supplemented with 25% glycerol; flash cooled in liquid nitrogen |
| Notes | Space group C2221; best dataset diffracted to 1.5 A resolution (Rwork 0.194, Rfree 0.218); refined with seven TLS groups; isomorphous with 4XWP but less disordered (only residues 90-114 missing); no electron density for phosphatidylserine observed despite additive presence |

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | EspB7-278 at 10 mg/mL |
| Reservoir | 0.2 M sodium chloride, 0.1 M CAPS pH 10.5, 1.26 M ammonium sulfate |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Space group I222; structure solved by molecular replacement using EspB7-278 C2221 structure (PDB 4XWP) as search model; refined to 2.14 A resolution (Rwork 0.204, Rfree 0.251); loop residues 82-114 missing |

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | Full-length EspB1-460 |
| Reservoir | 0.1 M CAPSO pH 10.8, 0.2 M sodium chloride, 1.5 M ammonium sulfate |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Space group not specified; structure solved by molecular replacement using EspB7-278 (PDB 4XXN) as search model; refined to 3.04 A resolution (Rwork 0.220, Rfree 0.266); C-terminal domain disordered; only 5 additional C-terminal residues (279-283) added |


## Biological / Functional Insights

### EspB is a PE-PPE fusion protein with heterodimer-like fold

The mature EspB isoform (residues 7-278) represents a fusion of PE and PPE N-terminal regions into a single polypeptide chain. The structure adopts an all-helical, elongated paperclip-like fold superimposable with the PE25-PPE41 heterodimer (RMSD 1.9 A over 249 CA atoms, 17% sequence identity). EspB contains 7 alpha helices: helices alpha1 and alpha2 correspond to PE25 helices and adopt an antiparallel hairpin; helix alpha3 corresponds to PPE41 alpha1. Proline residues P28, P29, P33, and P36 act as knobs-in-the-holes in the groove between helices alpha2 and alpha4. The PE and PPE sequence motifs are not conserved in EspB (residues QQ at 11-12 and DLK at 132-134 replace PE and PPE respectively).

### EspB lacks the EspG chaperone-binding site

EspB is missing residues D121-T129 that contain the characteristic hh motif of PPE proteins and mediate EspG binding. Additionally, EspB lacks about 9 residues compared to the alpha4-alpha5 loop region of PPE41, making it approximately 11 Angstroms shorter at one end. Pull-down experiments confirmed that EspB does not bind the ESX-1-specific chaperone EspG1, indicating that EspB has evolved as a PE-PPE fusion that no longer requires EspG for folding or stability.

### C-terminal domain is disordered and prevents oligomerization

The C-terminal domain of full-length EspB (residues beyond K283) is unstructured in crystal structures and in solution. Mature EspB (50 kDa) forms oligomers in M. tuberculosis culture filtrate, while full-length EspB (60 kDa) in cell lysate does not oligomerize. This suggests the unfolded C-terminal domain prevents self-association in the cytosol. Electron microscopy of the N-terminal fragment (EspB1-338) revealed donut-shaped ring particles approximately 10 x 10 nm in size.

### Putative lipid-binding sites on EspB surface

Structural analysis revealed hydrophobic grooves with adjacent positive charges that may serve as lipid-binding sites. The first groove between helices alpha1 and alpha2 contains residues L60, F159, L163 with a volume of 395 cubic Angstroms. A second smaller groove (53 cubic Angstroms) is located at the tip between helices alpha6 and alpha7 with L232, I246 at the bottom and Y236, Y250 at the rim. This is consistent with previous findings that mature EspB recognizes phosphatidic acid and phosphatidylserine.

### YxxxD/E secretion motif adopts helical conformation

The conserved YxxxD/E secretion motif (residues 81-85) in EspB is located adjacent to the partially disordered PE-PPE linker and adopts a helical conformation in the high-resolution structure. The motif is positioned at the beginning of helix alpha5 where W176 contributes to a tight interface between helices alpha2 and alpha5. The N-epsilon atom of W176 forms a hydrogen bond with the hydroxyl group of Y81, differing from the PE25-PPE41 structure where W56 of PPE41 makes van der Waals contacts with Y87 of PE25.


## Cross-References

- [PE25](/xray-mp-wiki/proteins/pe25/) — PE25-PPE41 heterodimer structure (PDB 2G38) was used as search model for EspB phasing
- [PPE41](/xray-mp-wiki/proteins/ppe41/) — PPE41 forms the heterodimer partner of PE25, structurally compared to EspB
- [PE-PPE Fusion Proteins](/xray-mp-wiki/concepts/pe-ppe-fusion-proteins/) — EspB is the archetypal PE-PPE fusion protein with a heterodimer-like fold
- [ESX-1 Secretion System](/xray-mp-wiki/concepts/esx-1-secretion-system/) — EspB is a central secreted substrate of the ESX-1 type VII secretion system
- [WxG100 Family Proteins](/xray-mp-wiki/concepts/wxg100-family-proteins/) — EspB secretion mechanism is co-dependent with WxG100 proteins EsxA and EsxB
- [Phosphatidylserine](/xray-mp-wiki/reagents/lipids/phosphatidylserine/) — EspB binds phosphatidylserine and crystallized with it as an additive
- [EspG1](/xray-mp-wiki/proteins/espg1/) — EspG1 chaperone does not bind EspB, unlike PE25-PPE41 heterodimer
- [MycP1](/xray-mp-wiki/proteins/mycp1/) — MycP1 protease cleaves full-length EspB to generate the mature 50 kDa isoform
