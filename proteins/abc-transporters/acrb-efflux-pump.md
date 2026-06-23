---
title: AcrB Multidrug Efflux Transporter (E. coli)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, pump, membrane-protein]
sources: [doi/10.1038##nature13205]
verified: false
---

# AcrB Multidrug Efflux Transporter (E. coli)

## Overview

AcrB is the inner-membrane transporter component of the AcrAB-TolC tripartite multidrug efflux pump in Escherichia coli. It belongs to the hydrophobic/amphiphilic efflux (HAE) subfamily of the resistance-nodulation-cell division (RND) superfamily. AcrB functions as a homotrimer that uses proton motive force to drive export of a broad spectrum of antibiotics and toxic compounds. This paper presents the pseudo-atomic model of the complete AcrAB-TolC assembly determined by cryo-EM combined with X-ray crystallography, as well as the crystal structure of the AcrBZ complex with the modulatory protein AcrZ and a designed ankyrin-repeat protein (DARPin) at 3.3 Å resolution.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13205 | Not specified in publication | 3.3 | Not specified | Full-length AcrB with AcrZ co-expressed, crystallized with DARPin | None (apo) |
| doi/10.1038##nature13205 | Not specified in publication | 3.7 | Not specified | Full-length AcrB with AcrZ co-expressed | None (apo) |
| doi/10.1038##nature13205 | Not specified in publication | 15-20 (pseudo-atomic model) | N/A | Complete AcrABZ-TolC complex assembled from fusion proteins | None (apo) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: AcrB with C-terminal His5 tag (pET21a vector); AcrZ with C-terminal His5 tag (pRSFDuet-1 vector); AcrA-polyGlySer-AcrZ-His5 fusion and TolC co-expressed for the complete assembly

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Affinity chromatography | Ni2+ affinity chromatography (IMAC) | — |  | AcrBZ complex enriched by IMAC before size-exclusion |
| 2. Size-exclusion chromatography | Gel filtration | — |  | Final polishing step for AcrBZ complex |

**Final sample**: Purified AcrBZ complex in buffer with DDM


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Affinity chromatography | Ni2+ affinity chromatography | — |  | Co-purification of TolC with AcrABZ complexes via His-tagged AcrZ |
| 2. Size-exclusion chromatography | Gel filtration | — |  | Final polishing step for AcrABZ-TolC complex |
| 3. GraFix gradient | Glycerol-glutaraldehyde gradient ultracentrifugation | — |  | Crosslinking and gradient fixation for cryo-EM specimen preparation |

**Final sample**: Purified AcrABZ-TolC complex in 50 mM HEPES pH 7.5, 400 mM NaCl, 0.03% DDM


## Crystallization

### doi/10.1038##nature13205

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | AcrBZ-DARPin complex |
| Notes | Co-crystals of AcrBZ with DARPin. Diffraction data collected at Diamond Light Source synchrotron. Structure solved by molecular replacement. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | AcrBZ complex (without DARPin) |
| Notes | AcrBZ complex crystallized by vapor diffusion. Data collected at Diamond Light Source. |


## Biological / Functional Insights

### Pseudo-atomic model of the complete AcrAB-TolC assembly

The cryo-EM model of the complete efflux pump reveals that TolC does not directly interact with AcrB in the assembly. Instead, the two proteins are bridged in the periplasm entirely through AcrA. This is consistent with in vivo crosslinking and pull-down assays. The stoichiometry is an AcrB trimer, an AcrA hexamer, and a TolC trimer. The hexameric AcrA assembly forms an α-helical coiled-coil cylinder that interacts with the periplasmic ends of TolC, while the membrane-proximal and β-barrel domains of AcrA interact with AcrB.

### AcrZ binding and allosteric modulation

AcrZ is a 49-residue, predominantly hydrophobic α-helix that fits into a wide groove in the transmembrane domain of AcrB. Its helical axis is inclined at nearly 45° relative to the membrane normal. The N-terminus is in the periplasm and the C-terminus in the cytoplasm. The interaction surface is conserved among AcrZ homologues, suggesting analogous interactions occur for other RND family proteins. The reported effects of AcrZ on drug sensitivity may originate from allosteric modulation of AcrB.

### TolC opening mechanism

In isolation, TolC assumes a closed resting state. In the assembled pump, the direct interactions with the α-helical hairpins of AcrA switch TolC to an open state. The assembly forms in vivo without substrate or proton-motive force, suggesting exogenous energy may not be required to open TolC. The dilation from closed to open is driven by chelate cooperativity (from the hexameric AcrA) and allosteric cooperativity (breaking interprotomer interactions in TolC).


## Cross-References
