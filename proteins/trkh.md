---
title: TrkH (Potassium Channel from Klebsiella pneumoniae)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12056]
verified: false
---

# TrkH (Potassium Channel from Klebsiella pneumoniae)

## Overview

TrkH is a potassium channel protein from the bacterium Klebsiella pneumoniae that forms a homodimer and associates with the cytoplasmic ATPase TrkA to form the functional TrkH-TrkA potassium transporter complex. TrkH contains a single transmembrane helix per subunit in the membrane and a large cytoplasmic domain that forms a dimeric structure. The channel conducts monovalent cations including K+, Na+, and Li+ and is regulated by ATP and ADP through binding to the associated TrkA subunit.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12056 | Not specified | 3.8 | P21 | TrkH-TrkA complex, TrkH subunit, 28,063 protein atoms in asymmetric unit | NADH |
| doi/10.1038##nature12056 | 3PJZ | Not specified | Not specified | Isolated TrkH, compared with TrkH in TrkH-TrkA complex | None |

## Expression and Purification

### Purification Workflow

- **Expression system**: Not specified
- **Expression construct**: His-tagged TrkH-TrkA complex
- **Tag info**: His-tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity chromatography | Immobilized metal affinity chromatography | Co2+ IMAC column |  | His-tagged TrkH-TrkA complex purified on Co2+ IMAC |
| Size-exclusion chromatography | Size-exclusion chromatography | -- |  | 10.2 mL peak fraction collected; TrkH and TrkA both ~50 kD by SDS-PAGE |

**Final sample**: TrkH-TrkA complex, both subunits ~50 kD


## Crystallization

### doi/10.1038##nature12056

| Parameter | Value |
|---|---|
| Method | Not specified |
| Protein sample | TrkH-TrkA complex with NADH |
| Reservoir | Not specified |
| Temperature | Not specified |
| Notes | Crystallized with Ta6Br12 for anomalous phasing; 3.8 A resolution; P21 space group; 28,063 protein atoms in asymmetric unit |


## Biological / Functional Insights

### TrkH-TrkA complex architecture

The TrkH-TrkA complex crystallizes in P21 space group with four TrkH subunits and four TrkA subunits in the asymmetric unit, likely forming two biological units. Each TrkH subunit contributes a helix (D3M2b) to the TrkH-TrkA interface, and salt bridges form between TrkH and TrkA subunits. The dimer interface in TrkH is formed by two helices visible in electron density maps.

### Ion selectivity of TrkH-TrkA

Single-channel recordings show the TrkH-TrkA complex conducts K+, Na+, and Li+ under bi-ionic conditions. The channel was recorded at +50 mV in symmetrical 200 mM KCl, with current amplitudes of ~9.6 pA (Level 1) and ~18.8 pA (Level 2). Under bi-ionic conditions with 200 mM K+ in the pipette and 200 mM Na+ or Li+ in the bath, the reversal potential shifted by about 10 mV, indicating selectivity for these monovalent cations.

### Redox regulation via cysteine modification

The TrkH I220C mutant was used to study redox regulation. MTSET (1 mM) treatment reduced channel activity (Level 1 current from 9.7 to 5.6 pA for TrkH I220C alone, and from 9.7 to 4.6 pA for TrkH I220C-TrkA complex). Activity was reversible upon addition of 20 mM DTT, indicating disulfide-linked modification.

### Comparison with isolated TrkH structure

The TrkH structure in the TrkH-TrkA complex was compared with isolated TrkH from PDB 3PJZ. Superposition of the TrkH dimers and of domains D1 and D3, including the intramembrane loop and D3M2b, reveals conformational differences between the isolated and complexed states.


## Cross-References

- [TrkA (ATP-binding Regulatory Subunit from Klebsiella pneumoniae)](/xray-mp-wiki/proteins/trka/) — TrkA forms the cytoplasmic ATPase component that associates with TrkH to form the functional TrkH-TrkA potassium transporter complex
- [ATPγS (Adenosine 5'-O-(3-thiotriphosphate))](/xray-mp-wiki/reagents/ligands/atp-gamma-s/) — ATPγS binds to TrkA in the isolated TrkA tetramer structure, providing structural basis for ATP recognition
- [NADH (Nicotinamide Adenine Dinucleotide, Reduced Form)](/xray-mp-wiki/reagents/cofactors/nadh/) — NADH binds to the TrkH-TrkA complex and was used for anomalous phasing in the 3.8 A structure
- [Dithiothreitol (DTT)](/xray-mp-wiki/reagents/additives/dithiothreitol/) — DTT (20 mM) reverses MTSET-induced modification of TrkH I220C, restoring channel activity
- [MTSET (2-trimethylammonium)ethyl methanethiosulfonate)](/xray-mp-wiki/reagents/additives/mtset/) — MTSET (1 mM) covalently modifies TrkH I220C cysteine, reducing channel activity in a reversible manner
- [Single-Wavelength Anomalous Diffraction](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Ta6Br12 clusters used for anomalous dispersion phasing of the TrkH-TrkA complex structure
