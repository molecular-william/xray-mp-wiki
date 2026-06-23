---
title: LEXSY Leishmania tarentolae Expression System
created: 2026-06-08
updated: 2026-06-08
type: method
category: methods
layout: default
tags: [expression-system, subdirectory-expression-systems]
sources: [doi/10.1038##s42003-021-02326-4, doi/10.1038##s41467-020-19457-7]
verified: false
---

# LEXSY Leishmania tarentolae Expression System

## Overview

The LEXSY (Leishmania Expression System) is a eukaryotic protein expression platform
based on the protozoan Leishmania tarentolae. It offers rapid, high-yield expression
of eukaryotic membrane proteins, including rhodopsins, with proper post-translational
modifications, at lower cost and higher growth densities compared to insect or
mammalian cell systems. LEXSY has been successfully used for the expression of
[Leptosphaeria rhodopsin (LR/Mac)](/xray-mp-wiki/proteins/rhodopsins/leptosphaeria-rhodopsin/)
and [OLPVR1](/xray-mp-wiki/proteins/rhodopsins/olpvr1/) for structural studies.

## Protocol

### Steps

1. {'step': 'Gene synthesis and vector design', 'method': 'Codon optimization and cloning', 'notes': 'Genes are synthesized de novo with codon optimization for L. tarentolae\n(e.g., using GeneOptimizer software). The gene of interest is fused with\na C-terminal polyhistidine tag (H6 or H9) and introduced into the\npLEXSY_I-blecherry3 integrative inducible expression vector through\nBgIII and NotI restriction sites.\n'}
2. {'step': 'Transformation and clonal selection', 'method': 'Electroporation', 'notes': 'LEXSY host T7-TR cells are transformed with the expression plasmid\nlinearized by Swal restriction enzyme. Clonal selection follows standard\nLEXSY protocols.\n'}
3. {'step': 'Cell culture and induction', 'method': 'Shake-flask fermentation', 'notes': 'Transformed cells are grown at 26°C in the dark in shaking baffled flasks\nin Brain-Heart-Infusion Broth supplemented with 5 mg/mL Hemin, 50 U/mL\npenicillin, and 50 mg/mL streptomycin. When OD600 = 1.0 is reached,\n10 mg/mL tetracycline is added for induction. For rhodopsin expression,\n10 µM all-trans-retinal is also added. Incubation continues for a further\n24 h.\n'}
4. {'step': 'Cell harvesting and lysis', 'method': 'Microfluidizer or similar', 'notes': 'Cells are disrupted at 10,000 psi in lysis buffer. Typical yields for\nrhodopsin constructs range from 10-20 mg per liter of culture.\n'}


## Advantages

- Rapid growth to high cell densities (OD600 ~1.0 within days)
- Lower cost compared to baculovirus/insect cell or mammalian expression
- Proper eukaryotic post-translational modifications
- Inducible expression under tetracycline control
- Scalable from shake flasks to bioreactors

## Disadvantages

- Limited host range (Leishmania tarentolae specific)
- Requires specialized LEXSY host strains and vectors (commercial system)
- Not all membrane proteins express well; optimization may be needed
- Less established than E. coli or Pichia pastoris systems
