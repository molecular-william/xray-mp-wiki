---
title: IMAC (Immobilized Metal Affinity Chromatography)
created: 2026-04-28
updated: 2026-04-28
type: method
tags: [purification-method, affinity-chromatography, chromatography]
sources: []
category: methods
layout: default
---


# IMAC — Immobilized Metal Affinity Chromatography

## Overview

IMAC (Immobilized Metal Affinity Chromatography) is a type of affinity chromatography used to purify proteins containing polyhistidine tags (His-tags). The technique exploits the coordination chemistry between histidine imidazole side chains and immobilized transition metal ions (Ni2+, Co2+, Cu2+, Zn2+) chelated on a solid support matrix.

## Principle

- **Matrix**: Typically agarose or sepharose beads functionalized with chelating groups (iminodiacetic acid [IDA] or nitrilotriacetic acid [NTA])
- **Metal ions**: Ni2+ (most common, Ni-NTA), Co2+ (TALON resin), Cu2+, Zn2+
- **Binding**: Histidine residues (typically 6xHis tag) coordinate with the immobilized metal ions
- **Elution**: Competitive displacement using imidazole (150-500 mM) or pH reduction
- **Selectivity**: His-tagged proteins bind; untagged proteins flow through

## Common Variants

### Ni-NTA (Nickel-Nitrilotriacetic Acid)
- **Matrix**: Agarose/sepharose with NTA chelator
- **Metal**: Ni2+
- **Advantages**: High binding capacity, tight metal chelation (low elution)
- **Applications**: Most widely used His-tag purification system

### TALON (Cobalt Affinity)
- **Matrix**: Agarose with iminobiotin ligand
- **Metal**: Co2+
- **Advantages**: Higher specificity than Ni-NTA (reduced background binding)
- **Applications**: Purification of difficult-to-purify proteins, reduced nonspecific binding

### IDA (Iminodiacetic Acid)
- **Matrix**: Agarose with IDA chelator
- **Metal**: Ni2+ or other transition metals
- **Advantages**: Higher metal loading capacity than NTA
- **Disadvantage**: Less tight metal chelation (more metal leaching)

## Typical Protocol

### Equilibration
- Buffer: 20-50 mM Tris-HCl pH 7.5-8.0, 150-300 mM NaCl, 10-20 mM imidazole (wash buffer)
- Detergent: Appropriate concentration for membrane proteins (e.g., 0.03-0.05% DDM)

### Binding
- Load clarified lysate or membrane solubilization supernatant onto equilibrated column
- Incubate 30-60 min at 4°C with gentle mixing
- Collect flow-through (contains unbound proteins)

### Wash
- 5-10 column volumes of wash buffer (10-40 mM imidazole)
- Removes weakly bound contaminants
- For membrane proteins: maintain detergent in wash buffer

### Elution
- 3-5 column volumes of elution buffer (150-500 mM imidazole)
- Collect 1-2 mL fractions
- His-tagged protein elutes at characteristic imidazole concentration

### Regeneration
- Strip bound protein with 100-250 mM EDTA (chelates metal ions)
- Recharge with 50-100 mM NiCl2 or CoCl2
- Re-equilibrate in binding buffer

## Applications in Membrane Protein Work

- **Expression systems**: E. coli, Sf9, HEK293, Pichia pastoris
- **Fusion tags**: C-terminal or N-terminal His6 tag, often with TEV protease cleavage site
- **Detergent compatibility**: Works with most non-ionic detergents (DDM, LMNG, OG, etc.)
- **SEC coupling**: Often followed by size-exclusion chromatography for final polishing

## Limitations

- **Background binding**: Some endogenous E. coli proteins bind Ni-NTA (especially in crude lysates)
- **Metal leaching**: IDA matrices can lose metal ions during purification
- **Histidine-rich native proteins**: Some proteins have native histidine clusters that cause nonspecific binding
- **Tag requirement**: Requires engineered His-tag (may need cleavage for structural studies)

## Related Methods

- [affinity-chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Broad category of purification methods using specific binding interactions
- [talon-resin](/xray-mp-wiki/methods/purification/talon-resin/) — TALON cobalt affinity resin (Co2+ IMAC variant)
- [superdex-columns](/xray-mp-wiki/methods/purification/superdex-columns/) — SEC for final polishing after IMAC
- [size-exclusion-chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Alternative/complementary purification method
- [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Common elution agent for IMAC