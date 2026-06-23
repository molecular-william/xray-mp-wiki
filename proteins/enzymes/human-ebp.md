---
title: "Human Emopamil-Binding Protein (EBP)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-10279-w]
verified: false
---

# Human Emopamil-Binding Protein (EBP)

## Overview

Emopamil-Binding Protein (EBP), also known as 3-beta-hydroxysteroid-Delta8,Delta7-isomerase, is an endoplasmic reticulum membrane protein that catalyzes the conversion of Delta8-sterols to Delta7-isomers in the [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) biosynthesis pathway. EBP is a five-transmembrane helix protein that adopts an unreported fold. It binds a structurally diverse array of pharmacologically active compounds including [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/), antidepressants, antipsychotics, and opioid analgesics, mediating drug resistance. Mutations in EBP cause Conradi-Hunermann syndrome, an X-linked dominant chondrodysplasia punctata.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-019-10279-w | (U18666A-bound structure) | 3.2 | P2(1)2(1)2 | Full-length human EBP (residues 1-230), residues 1-6, 53-59, 220-230 not visible | [U18666A](/xray-mp-wiki/reagents/ligands/u18666a/) |
| doi/10.1038##s41467-019-10279-w | (tamoxifen-bound structure) | 3.5 | P2(1)2(1)2 | Full-length human EBP (residues 1-230), residues 1-6, 53-59, 220-230 not visible | [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/) |

## Expression and Purification

- **Expression system**: Baculovirus-mediated transduction of HEK-293S GnTI- cells
- **Construct**: Full-length human EBP with N-terminal Strep-tag (crystallization) or N-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (binding assays)
- **Notes**: Cells harvested 48 h post-infection

### Purification Workflow

- **Expression system**: HEK-293S GnTI- (baculovirus-mediated)
- **Expression construct**: N-terminal Strep-tag or [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/)
- **Tag info**: Strep-tag II (crystallization), [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (binding assays)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication |  | 20 mM HEPES pH 7.5, 150 mM NaCl, 1 mM PMSF, 5 ug/mL leupeptin, 10 uM ligand | 10 uM [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/) or [U18666A](/xray-mp-wiki/reagents/ligands/u18666a/) added in all purification steps |
| Solubilization | Detergent extraction |  | 20 mM HEPES pH 7.5, 150 mM NaCl + 1% (w/v) [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) | Incubated 1 h at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Strep-Tactin or Ni-NTA affinity | Strep-Tactin (IBA) or Ni-NTA (Qiagen) | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) | Eluted with 2.5 mM [Desthiobiotin](/xray-mp-wiki/reagents/ligands/desthiobiotin/) (Strep) or 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (Ni-NTA) |


## Crystallization

### doi/10.1038##s41467-019-10279-w

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | Purified EBP in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) with 10 uM [U18666A](/xray-mp-wiki/reagents/ligands/u18666a/) or [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals obtained only with [U18666A](/xray-mp-wiki/reagents/ligands/u18666a/) or [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/) present. Structure determined by Se-SAD and refined at 3.2 A ([U18666A](/xray-mp-wiki/reagents/ligands/u18666a/)) and 3.5 A ([Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/)). Final models: 93.07%/6.93%/0.0% and 91.09%/8.74%/0.17% in favored/allowed/outlier Ramachandran regions. |


## Biological / Functional Insights

### Catalytic mechanism of sterol isomerization

EBP catalyzes the conversion of Delta8-sterols to Delta7-isomers through a putative mechanism involving a catalytic triad (His76, Glu80, Glu122). His76 acts as a proton donor, protonating Delta8-sterol at C9a to generate a carbocationic intermediate at C8, which is stabilized by Trp196 through pi-cation interaction. Glu80 (stabilized by Glu122) then deprotonates at C7-beta. The helix H1 linker between TM2 and TM3 serves as a gate allowing proton/water access from the ER lumen.

### Multidrug recognition mechanism

EBP binds structurally diverse compounds including [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/), [U18666A](/xray-mp-wiki/reagents/ligands/u18666a/), antidepressants, and antipsychotics. These compounds share a positively-charged amine group that mimics the carbocationic sterol intermediate. Trp196 stabilizes compounds through pi-cation interactions, while His76, Glu80, Glu122, and Asn193 form electrostatic and hydrogen bond interactions. The large hydrophobic membrane cavity formed by TMs 2-5 accommodates the structurally diverse ligands.

### Disease relevance - Conradi-Hunermann syndrome

Mutations in the EBP gene cause Conradi-Hunermann syndrome (X-linked dominant chondrodysplasia punctata), characterized by bone, skin, and eye abnormalities. Biochemical studies show increased 8,9-unsaturated sterols in plasma and tissues of affected patients. Disease mutations map to various regions including solvent entry, sterol binding/entry, catalytic sites, and dimerization interfaces.


## Cross-References

- [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/) — EBP binds tamoxifen; crystal structure of EBP-tamoxifen complex determined
- [U18666A](/xray-mp-wiki/reagents/ligands/u18666a/) — EBP binds U18666A; crystal structure of EBP-U18666A complex determined
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used in purification or crystallization
- [Desthiobiotin](/xray-mp-wiki/reagents/ligands/desthiobiotin/) — Related ligand or cofactor
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Additive used in purification or crystallization buffers
- [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — Fusion tag for crystallization or purification
