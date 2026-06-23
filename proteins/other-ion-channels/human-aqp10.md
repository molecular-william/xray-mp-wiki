---
title: "Human Aquaporin 10 (AQP10)"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-018-07176-z]
verified: false
---

# Human Aquaporin 10 (AQP10)

## Overview

Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 10 (AQP10) is an
aquaglyceroporin expressed in human adipocytes and the small intestine that
facilitates glycerol transport. Unlike other human aquaglyceroporins, AQP10
is uniquely stimulated by low pH, with increased glycerol release during
lipolysis (fat burning) correlating with intracellular acidification. The
crystal structure of human AQP10 was determined at 2.3 Å resolution (space
group P2_1_2_1_2_1, cell dimensions a=97.1 Å, b=116.8 Å, c=138.5 Å),
revealing an exceptionally wide ar/R selectivity filter and a unique
cytoplasmic gate. Functional and structural analyses identified His80 as
the pH sensor, with protonation of His80 triggering gate opening via
interaction with Glu27 and concerted rearrangements of Phe85 and the
V76-S77 loop. This pH-gating mechanism is glycerol-specific, allowing
water but not glycerol passage at neutral pH, and represents a unique type
of aquaporin regulation important for controlling body fat mass.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-018-07176-z | 6F7H | 2.3 | P2_1_2_1_2_1 | Human AQP10 C-terminally truncated construct (residues 1-270), wild-type | Glycerol (1 molecule per monomer) |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae (strain PAP1500)
- **Construct**: Human AQP10 (wild-type) with C-terminal His tag or GFP fusion

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Homogenization | — | Lysis buffer | Yeast cells harvested and disrupted |
| Affinity purification | Immobilized metal affinity chromatography | Ni-NTA resin | Standard His-tag purification buffer | Purified via C-terminal His tag |
| Tag removal | Thrombin cleavage | — | Cleavage buffer | His tag removed by thrombin for crystallization |
| Size-exclusion chromatography | SEC | — | SEC buffer with detergent | Final polishing step |

**Final sample**: Purified AQP10 in detergent solution


## Crystallization

### doi/10.1038##s41467-018-07176-z

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | Purified AQP10 at appropriate concentration |
| Reservoir | Optimized crystallization condition |
| Temperature | 277 |
| Notes | Data collected at SLS beamline X06SA, Paul Scherrer Institut, Villigen, Switzerland. Phased by molecular replacement using GlpF (pdb-id 1LDI). Space group P2_1_2_1_2_1 with cell a=97.1 Å, b=116.8 Å, c=138.5 Å, one tetramer in the asymmetric unit. Model built in COOT and refined in phenix.refine to Rwork 18.9%. |


## Biological / Functional Insights

### pH-dependent glycerol gating through His80 pH sensor

AQP10 displays pH-dependent glycerol-specific gating at the intracellular
interface, in contrast to other known aquaporin structures. His80 serves as
the pH sensor: at low pH, His80 becomes protonated (double protonated state),
triggering interaction with Glu27. This causes concerted structural changes
in nearby Phe85 and the cytoplasmic V76-S77 loop, opening the gate for
glycerol passage. At neutral pH (mono protonated state), the gate remains
closed to glycerol while remaining permeable to water.

### Unusually wide ar/R selectivity filter

The aromatic/arginine (ar/R) selectivity filter of AQP10 is exceptionally
wide compared to other aquaporins. While orthodox aquaporins (e.g., hAQP2)
and other aquaglyceroporins (e.g., GlpF, AqpM, PfAQP) have narrower
constrictions, AQP10's ar/R filter has a larger minimal diameter, enabling
efficient glycerol passage when the cytoplasmic gate is open.

### Cytoplasmic gate architecture

The cytoplasmic gate region is formed by residues H80, F85, R94, E27, V76
and S77. The G73G74 motif in TM2 is critical for kinking the helix and
allowing loop B to participate in gating. MD simulations with different
protonation states of H80 identified four main conformational clusters,
ranging from closed to fully open, providing a detailed model of the
gating mechanism.

### Physiological role in adipocyte glycerol release

In human adipocytes, lipolysis (induced by isoproterenol) causes
intracellular acidification, which correlates with increased glycerol
release through AQP10. Targeting the cytoplasmic gate to induce
constitutive glycerol secretion may offer an attractive option for
treating obesity and related complications.


## Cross-References

- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — AQP10 belongs to the aquaglyceroporin subfamily of the aquaporin superfamily
- [Human Aquaporin 7 (AQP7)](/xray-mp-wiki/proteins/other-ion-channels/human-aqp7/) — AQP7 is another human aquaglyceroporin; structural comparison with AQP10 reveals differences in selectivity filter and gating
- [pH-Dependent Gating](/xray-mp-wiki/concepts/transport-mechanisms/ph-dependent-gating/) — AQP10 exhibits pH-dependent glycerol gating via His80 protonation sensor
