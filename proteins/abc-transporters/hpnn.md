---
title: HpnN Hopanoid Transporter from Burkholderia multivorans
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1073##pnas.1619660114]
verified: false
---

# HpnN Hopanoid Transporter from Burkholderia multivorans

## Overview

HpnN from *Burkholderia multivorans* is a member of the hopanoid biosynthesis-associated RND (HpnN) subfamily of transporters. It is responsible for shuttling hopanoids from the cytoplasmic membrane to the outer membrane, playing a critical role in cell wall remodeling and multidrug resistance in *Burkholderia* species, including the opportunistic pathogen *B. cepacia* complex (Bcc). The crystal structure reveals a dimeric molecule with an overall butterfly shape, where each subunit contains 12 transmembrane helices and two large periplasmic loops. Two distinct conformations (forms I and II) were captured, representing open and closed states of the transporter, suggesting a rigid-body swinging motion of the periplasmic domain drives substrate translocation.


## Structure Determination

No structure determined.

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length HpnN (877 residues)
- **Notes**: Detailed expression conditions described in SI Appendix

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — |  | Detailed purification protocol described in SI Appendix |

**Final sample**: 20 mg/mL HpnN in 20 mM Na-Hepes pH 7.5, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)


## Crystallization

### doi/10.1073##pnas.1619660114

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 20 mg/mL HpnN in 20 mM Na-Hepes pH 7.5, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 16% [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/), 0.1 M sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 3.5, 0.2 M Li2SO4 |
| Mixing ratio | 1:1 (protein:reservoir) |
| Temperature | 25 °C |
| Growth time | 1 month |
| Cryoprotection | [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) stepwise to 30% |
| Notes | Form I crystals. Dimersions ~0.2 mm. SeMet-HpnN crystallized under form II conditions. |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 20 mg/mL HpnN in 20 mM Na-Hepes pH 7.5, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 15% [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/), 0.1 M sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 4.0, 0.2 M (NH4)2SO4 |
| Mixing ratio | 1:1 (protein:reservoir) |
| Temperature | 25 °C |
| Growth time | 1 month |
| Cryoprotection | [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) stepwise to 30% |
| Notes | Form II crystals. Dimersions ~0.2 mm. |


## Biological / Functional Insights

### Dimeric Butterfly Architecture

HpnN forms a dimer with a butterfly shape (110 Å tall, 100 Å wide, 52 Å thick). Each protomer has 12 transmembrane helices. The dimer interface involves TMs 7-9 and several α-helices and β-strands, primarily through van der Waals interactions.

### Open and Closed Conformations

Two crystal forms capture different transient states. Form I represents an open state with an elongated channel for hopanoid transport, while form II represents a closed state. A rigid-body swinging motion of the periplasmic domain converts between these conformations.

### Proton-Relay Network

Conserved residues D344, T818, and T819 form a hydrogen-bonded triad within the transmembrane region, likely establishing a proton-relay network for energy coupling. Mutagenesis of these residues (D344Y, T818A, T819A) abolishes transporter function.

### Conserved Channel Residues

Conserved aromatic residues F117, F541, and W661 line the exit site of the channel, while L48 and L826 are critical for gating. Mutations L48F and L826F abrogate multidrug resistance.

### Role in Multidrug Resistance

HpnN is critical for mediating resistance to [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/), novobiocin, and polymyxin B in *Burkholderia*. Knockout of *hpnN* in *B. thailandensis* severely attenuates growth in the presence of these antibiotics.


## Cross-References

- [RND Efflux Pumps](/xray-mp-wiki/concepts/transport-mechanisms/rnd-efflux-pumps/) — HpnN is a member of the RND superfamily of transporters
- [DDM (n-Dodecyl-β-D-Maltoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Used for solubilization and crystallization of HpnN
- [Buffer HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Used in purification buffer for HpnN
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Crystallization method used for HpnN
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/) — Additive used in purification or crystallization buffers
- [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/) — Antibiotic used in selection
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in purification or crystallization
