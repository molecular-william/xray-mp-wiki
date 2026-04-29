---


title: Dialysis
created: 2026-04-26
updated: 2026-04-27
type: method
tags: [purification-buffer-exchange]
sources: [doi/10.1038##ncomms9004, doi/10.7554##eLife.36758, doi/10.1038##nature02680]


category: methods
---
layout: default



# Dialysis in Membrane Protein Workflows

## Overview

Dialysis is a fundamental technique for buffer exchange, detergent removal, and sample equilibration in membrane protein biochemistry. It is used at multiple stages: after [affinity-chromatography](/methods/purification/affinity-chromatography/) purification, for detergent-to-lipid exchange, and for crystal cryoprotection.

## Common Dialysis Applications

### 1. Imidazole/Detergent Removal After Affinity Purification
- [nTMATE2-transporter](/proteins/nTMATE2-transporter/) — Imidazole removed after affinity purification
- General: Dialysis against detergent-containing buffer to maintain solubility after His-tag elution

### 2. Detergent-to-Lipid Exchange (Reconstitution)
- Proteins reconstituted into liposomes/nanodiscs by dialysis against detergent-free buffer
- Detergent slowly removed (overnight to several days) while lipids form around protein
- Molecular weight cutoff (MWCO): 10-14 kDa typical

### 3. Crystal Cryoprotection
- Crystals soaked in cryoprotectant via dialysis
- Stepwise increase in cryoprotectant concentration (e.g., 2% increments of PEG 400)

### 4. Buffer Exchange for Crystallization
- Dialysis buttons for micro-scale buffer exchange
- Equilibration against crystallization buffer

## Dialysis Parameters (from this wiki)

| Application | MWCO | Duration | Buffer |
|-------------|------|----------|--------|
| Imidazole removal | 10-14 kDa | 3 hours | 20 mM Tris, 0.3 M NaCl, 0.1% DDM |
| Detergent removal ([dialysis](/methods/purification/dialysis/)) | 10-14 kDa | 7 days | 10 mM HEPES pH 7.0, 150 mM KCl |
| Lipid exchange | 14 kDa | Overnight | 10 mM HEPES, 400 mM NaCl/KCl |
| Cryoprotection | N/A | Stepwise | PEG 400, TEG, [glycerol](/reagents/additives/glycerol/) |

## Related Methods

- [size-exclusion-chromatography](/methods/purification/size-exclusion-chromatography/) — Alternative to dialysis for buffer exchange
- [amicon-filters](/methods/purification/amicon-filters/) — Faster concentration and buffer exchange
- [microbatch](/methods/crystallization/microbatch/) — Crystallization method often paired with dialysis