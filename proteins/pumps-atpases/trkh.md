---
title: "TrkH (Potassium Channel from Klebsiella pneumoniae)"
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

TrkH is a potassium channel protein from the bacterium Klebsiella pneumoniae that forms a homodimer and associates with the cytoplasmic ATPase [TRKA](/xray-mp-wiki/proteins/trka) to form the functional TrkH-[TRKA](/xray-mp-wiki/proteins/trka) potassium transporter complex. TrkH contains a single transmembrane helix per subunit in the membrane and a large cytoplasmic domain that forms a dimeric structure. The channel conducts monovalent cations including K+, Na+, and Li+ and is regulated by [ATP](/xray-mp-wiki/reagents/ligands/atp) and [ADP](/xray-mp-wiki/reagents/ligands/adp) through binding to the associated [TRKA](/xray-mp-wiki/proteins/trka) subunit.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12056 | 4J9U | 3.8 | P21 | TrkH-TrkA complex, TrkH subunit, 28,063 protein atoms in asymmetric unit | NADH |
| doi/10.1038##nature12056 | 3PJZ | Not specified | Not specified | Isolated TrkH, compared with TrkH in TrkH-TrkA complex | None |

## Expression and Purification

### Purification Workflow

- **Expression system**: Not specified
- **Expression construct**: His-tagged TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex
- **Tag info**: His-tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity chromatography | Immobilized metal affinity chromatography | Co2+ IMAC column |  | His-tagged TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex purified on Co2+ IMAC |
| Size-exclusion chromatography | Size-exclusion chromatography | -- |  | 10.2 mL peak fraction collected; TrkH and [TRKA](/xray-mp-wiki/proteins/trka) both ~50 kD by SDS-PAGE |

**Final sample**: TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex, both subunits ~50 kD


## Crystallization

### doi/10.1038##nature12056

| Parameter | Value |
|---|---|
| Method | Not specified |
| Protein sample | TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex with [NADH](/xray-mp-wiki/reagents/cofactors/nadh) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Notes | Crystallized with Ta6Br12 for anomalous phasing; 3.8 A resolution; P21 space group; 28,063 protein atoms in asymmetric unit |


## Biological / Functional Insights

### TrkH-TrkA complex architecture

The TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex crystallizes in P21 space group with four TrkH subunits and four [TRKA](/xray-mp-wiki/proteins/trka) subunits in the asymmetric unit, likely forming two biological units. Each TrkH subunit contributes a helix (D3M2b) to the TrkH-[TRKA](/xray-mp-wiki/proteins/trka) interface, and salt bridges form between TrkH and [TRKA](/xray-mp-wiki/proteins/trka) subunits. The dimer interface in TrkH is formed by two helices visible in electron density maps.

### Ion selectivity of TrkH-TrkA

Single-channel recordings show the TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex conducts K+, Na+, and Li+ under bi-ionic conditions. The channel was recorded at +50 mV in symmetrical 200 mM KCl, with current amplitudes of ~9.6 pA (Level 1) and ~18.8 pA (Level 2). Under bi-ionic conditions with 200 mM K+ in the pipette and 200 mM Na+ or Li+ in the bath, the reversal potential shifted by about 10 mV, indicating selectivity for these monovalent cations.

### Redox regulation via cysteine modification

The TrkH I220C mutant was used to study redox regulation. [MTSET](/xray-mp-wiki/reagents/additives/mtset) (1 mM) treatment reduced channel activity (Level 1 current from 9.7 to 5.6 pA for TrkH I220C alone, and from 9.7 to 4.6 pA for TrkH I220C-[TRKA](/xray-mp-wiki/proteins/trka) complex). Activity was reversible upon addition of 20 mM [DTT](/xray-mp-wiki/reagents/additives/dtt), indicating disulfide-linked modification.

### Comparison with isolated TrkH structure

The TrkH structure in the TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex was compared with isolated TrkH from PDB 3PJZ. Superposition of the TrkH dimers and of domains D1 and D3, including the intramembrane loop and D3M2b, reveals conformational differences between the isolated and complexed states.


## Cross-References

- [TrkA (ATP-binding Regulatory Subunit from Klebsiella pneumoniae)](/xray-mp-wiki/proteins/pumps-atpases/trka/) — TrkA forms the cytoplasmic ATPase component that associates with TrkH to form the functional TrkH-TrkA potassium transporter complex
- [ATPγS (Adenosine 5'-O-(3-thiotriphosphate))](/xray-mp-wiki/reagents/ligands/atp-gamma-s/) — ATPγS binds to TrkA in the isolated TrkA tetramer structure, providing structural basis for ATP recognition
- [NADH (Nicotinamide Adenine Dinucleotide, Reduced Form)](/xray-mp-wiki/reagents/cofactors/nadh/) — NADH binds to the TrkH-TrkA complex and was used for anomalous phasing in the 3.8 A structure
- [Dithiothreitol (DTT)](/xray-mp-wiki/reagents/additives/dtt/) — DTT (20 mM) reverses MTSET-induced modification of TrkH I220C, restoring channel activity
- [MTSET (2-trimethylammonium)ethyl methanethiosulfonate)](/xray-mp-wiki/reagents/additives/mtset/) — MTSET (1 mM) covalently modifies TrkH I220C cysteine, reducing channel activity in a reversible manner
- [Single-Wavelength Anomalous Diffraction](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Ta6Br12 clusters used for anomalous dispersion phasing of the TrkH-TrkA complex structure
- [ADP](/xray-mp-wiki/reagents/ligands/adp) — Entity mentioned in text
- [ATP](/xray-mp-wiki/reagents/ligands/atp) — Entity mentioned in text
- [DTT](/xray-mp-wiki/reagents/additives/dtt) — Entity mentioned in text
- [NADH](/xray-mp-wiki/reagents/cofactors/nadh) — Entity mentioned in text
