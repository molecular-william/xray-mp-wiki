---
title: Human BK (Slo1/MaxiK) Large-Conductance Ca2+-Gated K+ Channel
created: 2026-06-16
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [ion-channel, potassium-channel, membrane-protein]
sources: [doi/10.1038##nature09252, doi/10.1038##nature10670]
verified: false
---

# Human BK (Slo1/MaxiK) Large-Conductance Ca2+-Gated K+ Channel

## Overview

BK channels (also called MaxiK or Slo1, gene KCNMA1) are large-conductance Ca2+-gated K+ channels essential for smooth muscle contraction and neurotransmitter release. They are activated synergistically by both voltage and intracellular Ca2+. The channel comprises a transmembrane voltage sensing domain (S1-S4) and a large C-terminal intracellular ligand-binding domain (two-thirds of the full channel) responsible for sensing Ca2+. The crystal structure of the entire cytoplasmic region of the human BK channel was determined at 3.1 Å resolution in a Ca2+-free state (PDB 3NAF), revealing a gating ring formed by four intracellular subunits, each comprising two tandem RCK domains. Three Ca2+ binding sites (the Ca2+ bowl, Asp 367, and Glu 374/Glu 399) were mapped onto the structure. The Ca2+ bowl within the second RCK domain forms an EF-hand-like motif positioned near the assembly interface. This structure provided the first detailed view of the BK ligand-binding domain and enabled docking with a voltage-gated K+ channel pore to generate a full-channel model.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09252 | 3NAF | 3.10 | I422 | Human SLO1 (KCNMA1) intracellular domain residues 329-1113 (C-terminus), with N-terminal GCN4_LI leucine zipper fusion for crystallization | None (Ca2+-free state) |
| doi/10.1038##nature10670 |  | 3.60 | P21212 | Zebrafish BK channel cytoplasmic domain residues 341-1060 with loop deletion (residues 839-872) | Ca2+ (Ca2+-bound open state) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf9 insect cells (baculovirus expression system using pFastBac-HTa vector)
- **Construct**: Intracellular fragment of human SLO1 gene (GI:26638650) residues 329-C-terminus, N-terminal His tag, TEV cleavage site, and 32-aa GCN4_LI leucine zipper

### Purification Workflow

*Source: doi/10.1038##nature09252*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Affinity purification | Co2+ affinity resin | — | Standard His-tag purification buffer | Purified via N-terminal His tag |
| 2. Tag removal | TEV protease cleavage | — | Cleavage buffer | Overnight TEV cleavage at 4°C to remove His tag |
| 3. Phosphatase treatment | Lambda protein phosphatase | — | Phosphatase buffer | 100 units/mg protein at room temp for 1 h; essential for obtaining diffracting crystals |
| 4. Size-exclusion chromatography | Gel filtration | — | Gel filtration buffer | Final purification step |

**Final sample**: Purified BK intracellular domain at approximately 7 mg/mL

### Purification Workflow

*Source: doi/10.1038##nature10670*

- **Expression system**: Escherichia coli
- **Expression construct**: Zebrafish BK channel cytoplasmic domain (residues 341-1060) with loop deletion (839-872)
- **Tag info**: Not specified

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Size-exclusion chromatography | Gel filtration | — | 20 mM HEPES pH 8.0, 150 mM NaCl, 20 mM dithiothreitol | Purified as described previously (Yuan et al., 2010) |

**Final sample**: ~6 mg/ml in SEC buffer with 10 mM CaCl2 added for Ca2+-bound open conformation


## Crystallization

### doi/10.1038##nature09252

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified BK intracellular domain at ~7 mg/mL |
| Reservoir | 3.5 M sodium formate, 0.1 M Tris-HCl pH 8.5 |
| Temperature | 4 °C |
| Notes | Crystals equilibrated overnight with sodium formate increased to 4.8 M before flash freezing. Space group I422 with cell dimensions a=b=134.1 Å, c=231.6 Å, one subunit per asymmetric unit. Structure determined by SAD using selenomethionine-substituted protein. 17 Se sites found with SHELXD, phases by autoSHARP, model built in Coot, refined in PHENIX to 3.1 Å with Rwork 23.8% and Rfree 28.9%. Data collected at APS beamlines 23ID and 19ID. |

### doi/10.1038##nature10670

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Zebrafish BK CTD at ~6 mg/ml in 20 mM HEPES pH 8.0, 150 mM NaCl, 20 mM DTT, plus 10 mM CaCl2 |
| Reservoir | 50 mM MES pH 6.3, 4% (v/v) PEG 4000, 100 mM potassium sodium tartrate |
| Temperature | 20 °C |
| Growth time | ~3 days |
| Cryoprotection | 50 mM MES pH 6.3, 6% (w/v) PEG 4000, 100 mM potassium sodium tartrate, 150 mM NaCl, 10 mM CaCl2, 30% ethylene glycol |
| Notes | Crystals grown to ~0.2 x 0.2 x 0.3 mm. Space group P21212 with cell dimensions a=137.65, b=210.82, c=238.76 Å. Eight subunits per asymmetric unit forming two gating rings. Structure determined by molecular replacement using monomeric Ca2+-bound human BK CTD (PDB 3MT5). Refined to 3.6 Å with Rwork=0.260 and Rfree=0.289. Data collected at NSLS beamline X29. |


## Biological / Functional Insights

### Gating ring architecture of BK channel

The cytoplasmic domain forms a tetrameric gating ring (four-fold symmetry) with each subunit comprising two tandem RCK domains (RCK1 and RCK2). RCK domains from adjacent subunits interact in a head-to-tail fashion via hydrophobic contacts (Ile441, Met442, Ile445 on RCK1 αD; Ile821, Leu822, Leu825, Phe890 on RCK2 αE). The gating ring has a diagonal distance of ~82 Å and a central hole of ~20 Å, allowing ion passage. This assembly resembles the MthK channel gating ring but is more expanded.

### Ca2+ bowl: an EF-hand-like calcium sensing motif

The Ca2+ bowl is a stretch of conserved aspartate residues within RCK2 located after αE, followed by a short helix (αEF). Together αE, the Ca2+ bowl loop, and αEF form a helix-loop-helix motif similar to EF-hand proteins like calmodulin. In the Ca2+-free (apo) state, the Ca2+ bowl is disordered and becomes ordered upon Ca2+ binding. Its strategic location beside the inter-subunit assembly interface suggests Ca2+ binding triggers conformational changes at the interface, altering gating ring size and leading to channel activation.

### Asp 367 high-affinity Ca2+ binding site on RCK1

Asp 367, located on the loop between αA and βB of RCK1, forms a high Ca2+ sensitivity site. Positioned in the groove between N- and C-terminal subdomains of RCK1, it is exposed to the space between the membrane and peripheral C-terminal subdomain. The surrounding chemical environment includes His365, Met513, and Glu535. His365 is involved in pH activation of BK and may interact electrostatically with Asp367 upon protonation. Met513 mutations profoundly affect Ca2+ sensitivity by maintaining local structural integrity. Glu535 may participate in Ca2+ chelation together with Asp367.

### Glu374/Glu399 low-affinity Mg2+/Ca2+ binding site

A low-affinity divalent cation binding site formed by Glu374 and Glu399 on β-strands βB and βC of RCK1. This site is positioned on the upper plateau of the gating ring near the membrane surface and close to the linker connecting the gating ring to the channel pore. Ser337 on the linker may also serve as a ligand. This site is physiologically regulated by Mg2+ and may involve residues from the intracellular-facing part of the membrane-spanning channel.

### Full BK channel model by docking pore domain

The structure includes the linker connecting the transmembrane and intracellular domains (starting from Arg329 after the pore-lining inner helix), enabling docking of a voltage-gated K+ channel pore onto the gating ring with reasonable accuracy. This generated a structural model for the full BK channel, providing insights into how the channel integrates voltage and Ca2+ signals.

### Ca2+-bound open gating ring reveals flower-petal opening of RCK1 layer

The Ca2+-bound (open) structure of the zebrafish BK gating ring (3.6 Å) shows that Ca2+ binding causes only the RCK1 layer (facing the membrane) to undergo a substantial conformational change, opening like the petals of a flower. The diagonal distance between N-terminal residues (Lys343) increases from ~70 Å in the closed state to ~82 Å in the open state. In contrast, the RCK2 layer remains nearly invariant. This asymmetric conformational change differs from prokaryotic MthK, where both layers change equally. The degree of RCK1 opening explains how Ca2+ binding can exert a force on the transmembrane pore to open it.

### Flexible interface and assembly interface in gating ring opening

The BK gating ring contains two types of inter-subunit interfaces: the flexible interface (between RCK1 N-lobe and RCK2 C-lobe of adjacent subunits) and the assembly interface (between RCK1 and RCK2 within a subunit). Ca2+ binding at the assembly interface causes conformational changes that propagate through the flexible interface, expanding the RCK1 layer. Large disordered regions at the flexible interface allow this asymmetric opening while maintaining the structural integrity of the gating ring.

### BK gating ring-MthK gating ring comparison

The MthK gating ring has eight identical RCK domains arranged with higher molecular symmetry, causing Ca2+ binding to shrink the ring's height and expand its diameter equally on both layers. In contrast, the BK gating ring has distinct RCK1 (top) and RCK2 (bottom) layers, so Ca2+ binding only opens the RCK1 layer. This comparison illustrates how evolution of molecular structure has given rise to distinct mechanical properties within the RCK domain family.


## Cross-References

- [RCK Domain Gating Ring](/xray-mp-wiki/concepts/rck-domain-gating-ring/) — The CTD gating ring houses Ca2+ sensors and transduces Ca2+ binding to pore opening
- [BK Channel Gating Mechanism](/xray-mp-wiki/concepts/bk-channel-gating/) — Structural basis for Ca2+-induced gating ring opening and pore activation
- [Allosteric Coupling](/xray-mp-wiki/concepts/allosteric-coupling/) — Gating ring expansion exerts allosteric force on the transmembrane pore
- [MthK Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) — Prokaryotic RCK-gated channel used for comparison and modeling
- [KcsA Potassium Channel](/xray-mp-wiki/proteins/kcsaa/) — Closed pore model used in BK channel gating model
- [Human BK (Slo1/MaxiK)](/xray-mp-wiki/proteins/voltage-gated-channels/bk-channel/) — Same protein family; zebrafish BK is 93% identical
- [Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) — Method used to crystallize the zebrafish BK gating ring
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phasing method using PDB 3MT5 as search model
