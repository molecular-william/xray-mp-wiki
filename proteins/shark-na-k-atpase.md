---
title: Na+,K+-ATPase (Shark Rectal Gland)
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms9004]
verified: false
---

# Na+,K+-ATPase (Shark Rectal Gland)

## Overview

The Na+,K+-ATPase from shark (Squalus acanthias) rectal gland is a P-type ATPase pump that maintains electrochemical gradients of Na+ and K+ across the plasma membrane. It is the principal active transport system in animal cells, pumping three Na+ out and two K+ in per ATP hydrolyzed. The shark rectal gland isoform has been extensively studied as a model for Na+,K+-ATPase structural biology because the rectal gland is enriched in these pumps. The enzyme consists of a catalytic alpha subunit (~110 kDa) with 10 transmembrane helices and three cytoplasmic domains (A, N, P), a glycosylated beta subunit (~55 kDa) with a single transmembrane helix, and in some preparations a regulatory gamma (FXYD) subunit. Crystal structures in the E2.MgF4(2-).2K+ state revealed the conformational basis for the sequential substitution of bound K+ ions from the extracellular medium, mediated by thermally-driven fluctuations of the M4E helix acting as an extracellular gate.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms9004 | 5AVQ | 2.9 A | Not specified | Shark (Squalus acanthias) rectal gland Na+,K+-ATPase in E2.MgF4(2-).2K+ state | MgF4(2-) (phosphate analog), K+ (two ions at transmembrane binding sites I and II), one K+ at cytoplasmic regulatory site C |

## Expression and Purification

- **Expression system**: Native extraction from Squalus acanthias (spiny dogfish) rectal gland
- **Construct**: Native Na+,K+-ATPase; no heterologous expression, mutations, or fusion tags

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Microsome preparation | Homogenization of shark rectal gland followed by washing and isolation by centrifugation in 30 mM histidine, 1 mM EDTA, 0.25 M sucrose, pH 6.8. Microsomes purified by sucrose flotation (40% sucrose layered on 60% sucrose, with 35% sucrose and histidine/EDTA buffer above). Bands at 0/35 and 35/40% interfaces collected. | -- | 30 mM histidine, 1 mM EDTA, 0.25 M sucrose, pH 6.8 + -- | Sucrose flotation purification of microsomal fractions from rectal gland tissue |
| Deoxycholate treatment | Purified microsomes incubated with ~0.15% deoxycholate for 30 min at 20 degC to remove extrinsic proteins and open sealed vesicles | -- | Histidine/EDTA buffer + Deoxycholate (~0.15%) | Deoxycholate treatment opens sealed vesicles and removes extrinsic membrane proteins |
| Glycerol resuspension and homogenization | Membrane fraction resuspended in histidine/EDTA with 25% glycerol, homogenized, centrifuged at 220,000g for 1 h at 10 degC. Repeated three times. | -- | Histidine/EDTA with 25% glycerol + -- | Final preparation suspended in histidine/EDTA with 25% glycerol, stored at -20 to -80 degC. Turnover number: 200 s-1 at 37 degC |
| Solubilization | Solubilization with octaethyleneglycol mono-n-dodecylether (C12E8) at 15 mg/mL | -- | 100 mM KCl, 4 mM MgCl2, 8 mM KF, 5 mM glutathione, 20 mM Tris-HCl pH 7.0 + C12E8 (15 mg/mL, ~1.2%) | Final protein concentration 2.5 mg/mL; phosphatidylcholine at 2.1 mg/mL |


## Crystallization

### doi/10.1038##ncomms9004

| Parameter | Value |
|---|---|
| Method | Dialysis (dialysis button) against crystallization buffer; crystals then soaked in dehydration buffer with K+ congeners (Tl+ or Rb+) |
| Protein sample | Solubilized shark Na+,K+-ATPase with C12E8 and phosphatidylcholine |
| Reservoir | 18% (w/v) PEG 3,000, 25% glycerol (w/v), 5% (v/v) 2-methyl-2,4-pentanediol, 100 mM potassium acetate, 10 mM KCl, 4 mM MgCl2, 4 mM KF, 0.1 mM EGTA, 10 mM glutathione, 2.6 ug/mL 2,6-di-t-butyl-p-cresol, 20 mM MES/Tris buffer pH 7.0 |
| Temperature | 25 degC |
| Growth time | 1-2 months |
| Cryoprotection | Crystals soaked overnight in dehydration buffer (crystallization buffer with 40% w/v PEG 3,000), then flash-frozen in cold nitrogen gas |
| Notes | Crystals of E2.MgF4(2-).2K+ state formed by dialysis. For substitution experiments, crystals soaked in dehydration buffer containing 100 mM Tl+ or Rb+ acetate for 0.75-100 min, then flash-frozen. Diffraction data collected at BL41XU, SPring-8 synchrotron at absorption peak of Tl or Rb. Multiple PDB entries deposited: 5AVQ, 5AVR, 5AVS, 5AVT, 5AVU, 5AVV, 5AVW, 5AVX, 5AVY, 5AVZ, 5AW0-5AW9. |


## Biological / Functional Insights

### Sequential K+ substitution at extracellular gate

The E2.MgF4(2-).2K+ state of shark Na+,K+-ATPase reveals that the two K+ ions at transmembrane binding sites I and II are substituted sequentially from the extracellular medium, with site II K+ exchanging substantially faster than site I. This was visualized by X-ray crystallography using Tl+ and Rb+ congeners, with time-resolved difference and anomalous electron density maps showing progressive substitution at site II first.

### M4E helix as extracellular gate

Thermal motion analysis using TLSMD and REFMAC revealed that the M4E helix (extracellular third of M4) undergoes collective swinging movements of ~5 deg within the yz-plane, pivoting around Val342. This movement shifts M4E by ~2A at Phe323, creating a transient ion pathway connecting the extracellular medium to K+ at site II. The M4E helix acts as the extracellular gate, and its restricted interdigitation with M1 and M5 helices allows this fluctuating-gate mechanism.

### Flickering-gate model supported

The crystallographic data provide strong structural support for the 'flickering-gate' model of K+ exchange. The gate (M4E) moves perpendicular to the row of two K+ ions, allowing only one K+ at a time to enter the extracellular pathway. This movement is restricted by tight crystal packing around the A-domain and by the highly viscous medium (40% PEG 3,000 and 25% glycerol), which suppresses rapid thermal movements.

### E2.MgF4(2-).2K+ is not an occluded state

The E2.MgF4(2-).2K+ state is not truly occluded. Unlike the E2 state where the A-N interface is stabilized by seven hydrogen bonds locking the A-domain, the E2.MgF4(2-).2K+ state has a small A-N interface stabilized by only one salt bridge (Glu223-Arg551). The A-domain is fixed primarily by MgF4(2-) rather than by inter-domain hydrogen bonds, allowing the extracellular gate to remain accessible.

### Three K+ binding sites

Three K+ binding sites were identified: two high-affinity transmembrane sites (I and II) and one lower-affinity cytoplasmic regulatory site (C). All three sites become occupied by K+ congeners (Tl+ or Rb+) upon full substitution, with site II being substituted first, followed by site I, and finally site C.


## Cross-References

- [Na+,K+-ATPase (Pig Kidney)](/xray-mp-wiki/proteins/na-k-atpase-pig-kidney/) — Related P-type ATPase; comparison of E2 state structures across species and tissue isoforms
- [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase 1a)](/xray-mp-wiki/proteins/serca1a/) — Related P-type ATPase; structural comparison of gating mechanisms between Na+,K+-ATPase and Ca2+-ATPase
- [P-type ATPase Family](/xray-mp-wiki/concepts/p-type-atpase/) — Na+,K+-ATPase is a member of the P-type ATPase family that forms a covalent aspartyl-phosphate intermediate
- [Large Domain Motion in P-type ATPases](/xray-mp-wiki/concepts/large-domain-motion-in-p-type-atpases/) — The E1-E2 conformational transitions and domain motions are central to the transport mechanism
