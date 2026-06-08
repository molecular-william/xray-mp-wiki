---
title: Fluorescence Size-Exclusion Chromatography (FSEC)
created: 2026-05-29
updated: 2026-06-02
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1038##nmeth.1251, doi/10.1038##NATURE11683, doi/10.1038##NATURE12179, doi/10.1038##nature06163, doi/10.1038##nature10737, doi/10.1038##nature12357]
verified: false
---

# Fluorescence Size-Exclusion Chromatography (FSEC)

## Overview

Fluorescence size-exclusion chromatography (FSEC) is a high-throughput screening method for identifying optimal detergents and buffer conditions that maintain membrane proteins in a monodisperse, folded state. FSEC couples size-exclusion chromatography with fluorescence detection using GFP-fused membrane proteins. As the GFP-fusion protein elutes from the SEC column, fluorescence is measured in real-time, providing a direct readout of properly folded and monodisperse protein. FSEC has become the gold standard for rapid assessment of membrane protein solubility and stability during detergent screening.

## Principle

Membrane proteins are expressed in E. coli as N-terminal or C-terminal fusions to green fluorescent protein (GFP). The fusion protein is solubilized from membranes in various detergents, and samples are injected onto a SEC column. Properly folded membrane proteins elute as sharp, symmetric fluorescence peaks at the expected elution volume, while aggregated or misfolded proteins elute earlier (higher molecular weight) or as broad, irregular peaks. The fluorescence signal is proportional to the amount of properly folded GFP-fusion protein in solution, enabling rapid comparison of multiple detergents and buffer conditions.

## Protocol

### Reagents and Materials

- {'expression_plasmid': 'Membrane protein gene cloned into a GFP-fusion expression vector (e.g., pWaldo-TEV-GFP), typically as an N-terminal or C-terminal fusion with a TEV protease-cleavable linker.'}
- {'e_coli_strain': 'E. coli expression strain (e.g., BL21(DE3), Lemo21(DE3), or Lemo56(DE3)) grown in LB or Terrific Broth medium with appropriate antibiotic selection.'}
- {'detergents': 'Panel of detergents to screen (typically 10-30 detergents), including common choices such as DDM, LMNG, OG, C12E8, and others.'}
- {'sec_buffer': 'SEC running buffer containing the test detergent at a concentration above its CMC (typically 0.02-0.05% w/v).'}

### Steps

1. {'step': 'Protein expression', 'description': 'Transform E. coli with GFP-fusion plasmid. Inoculate culture and grow to OD600 of 0.6-0.8, then induce with IPTG (typically 0.1-0.5 mM). Continue culture for 16-20 h at reduced temperature (16-25 C) for proper folding.'}
2. {'step': 'Membrane preparation', 'description': 'Harvest cells by centrifugation, resuspend in lysis buffer, and disrupt by sonication or homogenization. Collect membranes by ultracentrifugation at 100,000 x g for 1 h.'}
3. {'step': 'Solubilization', 'description': 'Resuspend membrane pellet in solubilization buffer containing the test detergent at 1-2% w/v. Incubate on ice or at 4 C for 1-2 h with gentle mixing. Clarify by centrifugation at 100,000 x g for 30 min.'}
4. {'step': 'FSEC injection', 'description': 'Inject 100-500 uL of solubilized sample onto SEC column (e.g., Superdex 200 Increase 10/300 GL) pre-equilibrated in SEC buffer containing the same detergent. Collect fluorescence (GFP excitation 485 nm, emission 510 nm) and UV absorbance (280 nm) traces.'}
5. {'step': 'Data analysis', 'description': 'Identify detergent conditions that produce sharp, symmetric fluorescence peaks at the expected elution volume for the monomeric GFP-fusion protein. Select top candidates for downstream purification and further characterization.'}


## Advantages

- High-throughput screening of detergents and buffer conditions
- Direct readout of properly folded protein (GFP fluorescence)
- Non-denaturing, native conditions
- Rapid (results in 1-2 h per condition)
- Requires small amounts of protein (microgram scale)
- Can be automated for large detergent panels

## Disadvantages

- Requires GFP fusion construct (may affect protein behavior)
- GFP fusion may interfere with some membrane proteins
- Limited to proteins that can tolerate GFP fusion
- Fluorescence quenching by some detergents
- Does not provide information about oligomeric state without calibration

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Aquifex aeolicus TatC](/xray-mp-wiki/proteins/tatc/) | N/A | N/A | FSEC used to identify LMNG as the optimal detergent for maintaining A. aeolicus TatC-GFP fusion protein in a monodisperse state. SEC-MALLS confirmed that LMNG maintained TatC in monodisperse form after TEV protease cleavage of the GFP tag. |
| [Chicken Acid-Sensing Ion Channel 1a (cASIC1)](/xray-mp-wiki/proteins/asic1a/) | N/A | 3HV4 | FSEC used to screen N- and C-terminally EGFP-tagged chicken ASIC1 and delta ASIC1 constructs. Whole cells solubilized in phosphate buffered saline with 20 mM DDM and protease inhibitors for 1 h. Supernatant loaded onto Superose 6 10/300 column equilibrated with 20 mM Tris pH 8.0, 150 mM NaCl, and 1 mM DDM. Delta ASIC1-EGFP fusion showed a monodisperse peak, guiding subsequent purification and crystallization. |
| [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut/) | N/A | N/A | FSEC used to characterize conformation-specific Fab binding to LeuT variants. 2B12 Fab bound LeuT^K in the presence of 10 mM leucine and 200 mM NaCl (left shift of peak retention volume), but not in apo state. 6A10 Fab bound LeuT^K(TSY) in the absence of leucine and sodium, but not in their presence. Titration experiments with molar excess of Fab (0x to 10x) confirmed conformation specificity of both Fabs. |

## Related Methods

- [Size-Exclusion Chromatography with Multi-Angle Light Scattering (SEC-MALS)](/xray-mp-wiki/methods/quality-assessment/sec-mals/) — SEC-MALS used downstream of FSEC to confirm monodispersity and determine oligomeric state
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC is the core separation technique used in FSEC

## Related Reagents

- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Optimal detergent identified by FSEC for TatC
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Optimal detergent identified by FSEC for chicken ASIC1a
