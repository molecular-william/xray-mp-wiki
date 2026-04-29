---

title: LPA1 Receptor (Lysophosphatidic Acid Receptor 1)
created: 2026-04-26
updated: 2026-04-27
type: protein
tags: [gpcr, membrane-protein, receptor]
sources: [doi/10.1016##j.cell.2015.06.002]

---
layout: default


# LPA1 Receptor

## Overview

LPA1 (lysophosphatidic acid receptor 1) is a GPCR that binds lysophosphatidic acid (LPA), a pleiotropic bioactive lipid. LPA is produced by autotaxin from lysophospholipids and is present in nearly all cells, tissues, and body fluids. LPA1 couples to Gq/Gi/G12/13 proteins and is implicated in hydrocephalus, cancer, and fibrosis.

## Structure Determination

- **PDB IDs**: 4Z34 (LPA1-ONO-9780307), 4Z35 (LPA1-ONO-9910539), 4Z36 (LPA1-ONO-308053)
- **Resolutions**: 3.0 Å, 2.9 Å, 2.9 Å
- **Method**: X-ray crystallography, lipidic cubic phase (LCP) crystallization
- **Constructs**: LPA1-bRIL (b562RIL fusion in ICL3, 38-residue C-terminal truncation); dsLPA1-mbRIL (disulfide-engineered)
- **Space group**: P2₁2₁2₁ for all three structures

## Expression and Purification

- **Expression system**: [[hek293-cells]] (mammalian, stable expression)
- **Construct design**:
  - LPA1-bRIL: b562RIL (thermostabilized [[bril]]) inserted into ICL3 at positions 5.66 (R233) and 6.24 (R247); 38-residue C-terminal truncation
  - dsLPA1-mbRIL: Additional engineered disulfide bond (D204A/V282A → Cys-Cys) between TMV and TMVI; modified [[bril]] (mbRIL) with disordered loop replaced by short linker
- **Detergent**: [[ddm]] (n-dodecyl-β-D-maltopyranoside) for membrane solubilization
- **Purification**: [[affinity-chromatography]] (His-tag on [[bril]]), followed by [[size-exclusion-chromatography]] (Superose 6)
- **SEC buffer**: 20 mM [[hepes-buffer]] pH 7.5, 150 mM [[sodium-chloride]], 0.05% [[ddm]], 10 μM [[cholesterol-hydrogen-succinate]]

## Crystallization

- **Method**: [[lipidic-cubic-phase]] (LCP) — [[monoolein]]-based mesophase
- **Lipid**: [[monoolein]] supplemented with **cholesterol** (10% w/w final)
- **Protein-to-lipid ratio**: 1:1 (w/w)
- **Precipitant**:
  - ONO-9780307: 0.1 M [[hepes-buffer]] pH 7.0, 18–20% [[peg-400]]
  - ONO-9910539: 0.1 M [[sodium-citrate]] pH 5.6, 18–20% [[peg-400]]
  - ONO-3080573: 0.1 M [[sodium-acetate]] pH 4.5, 18–20% PEG 3350
- **Temperature**: 20 °C
- **Crystal growth**: 1–3 weeks

## Antagonists Co-crystallized

- **ONO-9780307**: Indane-containing antagonist; binds in strained eclipsed conformation (9.6 kcal/mol torsional strain)
- **ONO-9910539**: Acetyl group for enhanced polar interactions; reduced lipophilicity
- **ONO-3080573**: Ether and phenyl ring substitution; reduced torsional strain

## Key Structural Features

- **Binding pocket**: Spherical (vs. linear in S1P1); ligand access from extracellular space
- **TM1 positioning**: 3 Å closer to TMVII than S1P1, closing membrane-access gap
- **Disulfide bonds**: Three native disulfides in extracellular region; engineered disulfide in dsLPA1
- **N-terminal helix**: Six-turn alpha helix capping ECL1/ECL2; additional disulfide to ECL2 in dsLPA1

## Comparison with S1P1 (Sphingosine 1-Phosphate Receptor 1)

| Feature | LPA1 | S1P1 |
|---------|------|------|
| Binding pocket | Spherical | Linear |
| TM1 position | 3 Å closer to TMVII | Further from TMVII |
| Ligand access | Extracellular space | Membrane |
| ECL0 | Loop (no secondary structure) | Helical |
| Position 3.33 | Aspartate | Phenylalanine |
| Position 5.43 | Tryptophan | Cysteine |
| Position 6.51 | Glycine | Leucine |

## Related GPCRs

- [[a2a-adenosine-receptor]] — Class A GPCR with bRIL fusion construct
- [[5ht2b-receptor]] — Serotonin GPCR with [[bril]] fusion
- [[opsin-gpcr]] — Class A GPCR structural template
- [[cd81-tetraspanin]] — Cholesterol-binding membrane protein
- [[angiotensin-ii-type-1-receptor]] — GPCR with SFX/XFEL and LCP crystallization