---
title: "Sigma-1 Receptor from Xenopus laevis (xlS1R)"
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-022-28946-w, doi/10.1038##s41467-024-49894-7]
verified: false
---

# Sigma-1 Receptor from Xenopus laevis (xlS1R)

## Overview

The sigma-1 receptor (S1R) from Xenopus laevis (xlS1R) is a non-opioid transmembrane receptor that shares 67% sequence identity and 89% sequence homology with the human sigma-1 receptor. It is an ER-resident receptor implicated in neurodegenerative disorders and cancer. This paper presents multiple crystal structures of xlS1R in both closed and open-like conformations, providing experimental evidence for the ligand entry pathway. Subsequent structures bound to endogenous neurosteroid ligands progesterone (putative antagonist) and dehydroepiandrosterone sulfate (DHEAS) (putative agonist) reveal the binding mechanisms of endogenous ligands and a two-part-interaction model for sigma-1 receptor ligand binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-022-28946-w | 7W2B | 3.33 | P21 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | unknown endogenous molecule (closed-endo conformation) |
| doi/10.1038##s41467-022-28946-w | 7W2C | 3.33 | P21 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | PRE084 (closed conformation, soaked) |
| doi/10.1038##s41467-022-28946-w | 7W2D | 3.47 | P21 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | S1RA (closed conformation) |
| doi/10.1038##s41467-022-28946-w | 7W2E | 3.56 | P222 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | unknown endogenous molecule (open-endo conformation) |
| doi/10.1038##s41467-022-28946-w | 7W2F | 3.10 | P222 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | PRE084 (open conformation, co-crystallized) |
| doi/10.1038##s41467-022-28946-w | 7W2G | 2.85 | P222 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | PRE084 (open conformation, soaked) |
| doi/10.1038##s41467-022-28946-w | 7W2H | 3.80 | P21 | xlS1R C179/C203 double mutant with C91S background, full-length | S1RA |
| doi/10.1038##s41467-024-49894-7 | 8W4B | 2.15 | I 4 3 2 | Wild-type xlS1R, full-length, co-crystallized with progesterone | Progesterone (xlS1Rprog-co) |
| doi/10.1038##s41467-024-49894-7 | 8W4C | 2.68 | I 4 3 2 | Wild-type xlS1R, full-length, progesterone soaked into crystals | Progesterone (xlS1Rprog-soak) |
| doi/10.1038##s41467-024-49894-7 | 8W4D | 2.17 | I 4 3 2 | Wild-type xlS1R, full-length, unknown endogenous ligand | Unknown endogenous molecule |
| doi/10.1038##s41467-024-49894-7 | 8WWB | 2.50 | I 4 3 2 | Wild-type xlS1R, full-length, DHEAS soaked into I432 crystals | DHEAS (xlS1RDHEAS-I432) |
| doi/10.1038##s41467-024-49894-7 | 8WUE | 3.09 | C 1 2 1 | Wild-type xlS1R, full-length, DHEAS soaked into C2 crystals | DHEAS (xlS1RDHEAS-C2) |
| doi/10.1038##s41467-024-49894-7 | 8W4E | 2.81 | C 1 2 1 | Wild-type xlS1R, full-length | None (side-open conformation) |
| doi/10.1038##s41467-024-49894-7 | 8YBB | 2.32 | C 1 2 1 | Wild-type xlS1R, full-length | None (side-open-all conformation) |

## Expression and Purification

- **Expression system**: Pichia pastoris yeast strain GS115
- **Construct**: Full-length xlS1R with N-terminal decahistidine tag and TEV protease recognition site following hemagglutinin signal peptide; cysteine mutants introduced by site-directed mutagenesis
- **Induction**: 1% [Methanol](/xray-mp-wiki/reagents/additives/methanol) and 2.5% DMSO at OD600 of ~1, 20 C for 48 h

### Purification Workflow

#### Source: unknown


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization (ATS AH-1500) | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf), 2 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) | Cell pellets resuspended and lysed |
| Solubilization | Detergent solubilization | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm), 0.005% CHS | Membranes solubilized |
| Affinity chromatography | Ni-NTA affinity resin | Ni-NTA | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm), 0.005% CHS, 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) (elution) |  |
| Tag cleavage | TEV protease | — |  |  |
| Size-exclusion chromatography | Superose 6 Increase column | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm), 0.005% CHS |  |

#### Source: doi/10.1038##s41467-024-49894-7

- **Expression system**: Pichia pastoris
- **Expression construct**: Full-length xlS1R with N-terminal decahistidine tag and TEV protease recognition site after hemagglutinin signal peptide
- **Tag info**: Decahistidine tag, TEV cleaved

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | High-pressure homogenization | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf), 2 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) | Same protocol as previous study |
| Solubilization | Detergent extraction | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm), 0.005% CHS | Membranes stirred 2-3 hr at 4 C |
| Ni-NTA affinity | Nickel affinity chromatography | Ni-NTA | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm), 0.005% CHS, 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) (elution) | Wash with 20 mM imidazole, elute with 250 mM imidazole |
| TEV cleavage | TEV protease digestion | — |  | Overnight at 4 C to remove decahistidine tag |
| Size-exclusion chromatography | Superose 6 Increase (GE Healthcare) | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm), 0.005% CHS | Final purification step |

**Final sample**: ~15 mg/mL for crystallization
**Yield**: Not specified
**Purity**: Not specified


## Crystallization

### doi/10.1038##s41467-022-28946-w

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified xlS1R at ~15 mg/mL mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) at 2:3 protein:lipid ratio by mass |
| Temperature | 4 C |
| Notes | Crystals grew over 2-4 weeks; some structures obtained by soaking ligands ([PRE084](/xray-mp-wiki/reagents/additives/pre084), [S1RA](/xray-mp-wiki/reagents/additives/s1ra)) into pre-formed crystals |

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | xlS1R C179/C203 mutant |
| Reservoir | 1.5 M ammonium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate), 0.1 M [MES](/xray-mp-wiki/reagents/buffers/mes) pH 5.5, 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) |
| Temperature | Not specified |
| Notes | 5.0 mM 06:0 Lyso PC (Avanti) used as additive for final data |

### doi/10.1038##s41467-024-49894-7

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified xlS1R at ~15 mg/mL mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) at 2:3 protein:lipid ratio by mass |
| Temperature | 4 C |
| Notes | Crystals appeared in 2-3 days and reached full size in one week. For progesterone co-crystallization (8W4B), 1 mM progesterone added to protein before LCP reconstitution. For soaking experiments, ligands added at 1 mM to crystallization drops. Cryoprotected by raising glycerol to 16% in 2% increments before flash-freezing in liquid nitrogen. DHEAS complex (8WWB) obtained by soaking DHEAS into I432 crystals; DHEAS-C2 (8WUE) from C2 crystals. |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified xlS1R at ~15 mg/mL mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Temperature | Not specified |
| Notes | Crystals used for DHEAS soaking experiments and side-open conformations. Soaked with 1 mM DHEAS before data collection. xlS1Rside-open (8W4E) and xlS1Rside-open-all (8YBB) crystals grown in same condition as xlS1Runknown-lig. |


## Biological / Functional Insights

### Ligand entry pathway (PATH2)

The xlS1R structures support PATH2, where ligands access the binding site through the opening between alpha4 and alpha5 helices of the carboxy-terminal two-helix bundle. The open-like conformation shows a solvent pathway connecting the ligand binding site to the extracellular milieu. Blocking the entrance between alpha4 and alpha5 (via disulfide crosslinking or PEGylation of Cys179/Cys203) significantly reduces ligand binding, confirming this pathway.

### Cupin-fold domain rigidity

Crystal packing analysis shows that the [Cupin Fold](/xray-mp-wiki/concepts/cupin-fold) domain tip region (Trp133-Tyr144) is tightly buried by adjacent protomers, preventing the conformational changes required for PATH1 ([Cupin Fold](/xray-mp-wiki/concepts/cupin-fold) domain rearrangement). This steric hindrance from crystal packing supports the PATH2 hypothesis as the physiological ligand entry mechanism.

### Homotrimeric organization

xlS1R crystallizes as a homotrimer in all conformations. Each protomer comprises a single transmembrane helix (alpha1), a [Cupin Fold](/xray-mp-wiki/concepts/cupin-fold) beta-barrel body containing the ligand-binding site, and a membrane-adjacent V-shaped two-helix bundle (alpha4/alpha5) at the carboxy-terminus. Superposition of xlS1R and human S1R (excluding alpha1) yields an all-Ca RMSD of 0.35 A, indicating high structural conservation.

### Endogenous neurosteroid binding — progesterone and DHEAS

Crystal structures of xlS1R bound to two endogenous neurosteroid ligands, progesterone (putative antagonist, 2.15 A) and DHEAS (putative agonist, 2.50 A), reveal that both bind in a similar location of the beta-barrel lumen but with opposite orientations. Progesterone binds mainly through hydrophobic interactions with residues W86, M90, L92, Y100, L102, F104, Y117, I175, F181, A182, and Y203, and does not interact directly with the conserved E169 side chain. DHEAS binds with its C3 sulfuric ester group forming hydrogen bonds with E169. Water molecules in the distal beta-barrel lumen contribute to ligand binding energetics.

### Water-mediated ligand binding and potential water entry pathways

Six water molecules were observed in the distal beta-barrel lumen of the xlS1R-progesterone structure, forming hydrogen bonds with residues S114, Y117, D123, and H151. These water molecules contribute energetically to progesterone binding (interaction energy improves from -58.6 to -62.0 kcal/mol). A side-entrance between the beta4/beta5 loop and alpha4 helix (near S177 and F181) was identified as a potential water entry pathway, supported by molecular dynamics simulations. Two additional entrances (alpha4/alpha5-entrance and hinge-entrance) were also identified.

### Two-part-interaction model for sigma-1 receptor ligands

A generalized two-part-interaction model was proposed based on the neurosteroid complex structures. The beta-barrel lumen is divided into a hydrophobic zone (proximal to membrane, ~10 A) that interacts with hydrophobic ligand moieties, and a polar zone (distal region, ~8 A) that accommodates polar ligand groups or water molecules. E169 is located near the junction. This model is compatible with synthetic ligand binding modes and may help rationalize sigma-1 receptor ligand design.


## Cross-References

- [PD144418](/xray-mp-wiki/reagents/ligands/pd144418/) — Sigma-1 antagonist used in human S1R structures (PDB 5HK1) for comparison
- [Human Sigma-1 Receptor](/xray-mp-wiki/proteins/receptors-signaling/sigma-1-receptor/) — Human ortholog used for structural comparison (PDB 5HK1)
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for xlS1R crystallization
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) — Entity mentioned in text
- [PMSF](/xray-mp-wiki/reagents/additives/pmsf) — Entity mentioned in text
- [Cupin Fold](/xray-mp-wiki/concepts/cupin-fold) — Entity mentioned in text
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) — Entity mentioned in text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm) — Entity mentioned in text
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate) — Entity mentioned in text
- [MES](/xray-mp-wiki/reagents/buffers/mes) — Entity mentioned in text
