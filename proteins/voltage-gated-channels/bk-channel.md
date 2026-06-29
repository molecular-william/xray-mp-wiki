---
title: "Human BK (Slo1/MaxiK) Large-Conductance Ca2+-Gated K+ Channel"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, potassium-channel, membrane-protein]
sources: [doi/10.1038##nature09252, doi/10.1038##nature10670]
verified: false
---

# Human BK (Slo1/MaxiK) Large-Conductance Ca2+-Gated K+ Channel

## Overview

BK channels (also called MaxiK or Slo1, gene KCNMA1) are large-conductance Ca2+-gated K+ channels essential for smooth muscle contraction and neurotransmitter release. They are activated synergistically by both voltage and intracellular Ca2+. The channel comprises a transmembrane voltage sensing domain (S1-S4) and a large C-terminal intracellular ligand-binding domain (two-thirds of the full channel) responsible for sensing Ca2+. The crystal structure of the entire cytoplasmic region of the human BK channel was determined at 3.1 Å resolution in a Ca2+-free state (PDB 3NAF), revealing a gating ring formed by four intracellular subunits, each comprising two tandem RCK domains. Three Ca2+ binding sites (the [Ca2+ Bowl](/xray-mp-wiki/concepts/miscellaneous/calcium-bowl/), Asp 367, and Glu 374/Glu 399) were mapped onto the structure. The [Ca2+ Bowl](/xray-mp-wiki/concepts/miscellaneous/calcium-bowl/) within the second RCK domain forms an EF-hand-like motif positioned near the assembly interface. This structure provided the first detailed view of the BK ligand-binding domain and enabled docking with a voltage-gated K+ channel pore to generate a full-channel model.

## Publications

### doi/10.1038##nature09252

**Structures:**

<table class="wiki-table">
  <thead><tr>
    <th>PDB ID</th>
    <th>Resolution</th>
    <th>Space Group</th>
    <th>Construct</th>
    <th>Ligand/Co-factor</th>
  </tr></thead>
  <tbody>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3naf">3NAF</a></td>
      <td>3.10</td>
      <td>I422</td>
      <td>Human SLO1 (KCNMA1) intracellular domain residues 329-1113 (C-terminus), with N-terminal GCN4_LI leucine zipper fusion for crystallization</td>
      <td>None (Ca2+-free state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 insect cells (baculovirus expression system using pFastBac-HTa vector)
- **Construct**: Intracellular fragment of human SLO1 gene (GI:26638650) residues 329-C-terminus, N-terminal His tag, TEV cleavage site, and 32-aa GCN4_LI leucine zipper

**Purification:**

<table class="wiki-table">
  <thead><tr>
    <th>Step</th>
    <th>Method</th>
    <th>Resin / Column</th>
    <th>Buffer + Detergent</th>
    <th>Notes</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1. Affinity purification</td>
      <td>Co2+ affinity resin</td>
      <td>—</td>
      <td>Standard His-tag purification buffer</td>
      <td>Purified via N-terminal His tag</td>
    </tr>
    <tr>
      <td>2. Tag removal</td>
      <td>TEV protease cleavage</td>
      <td>—</td>
      <td>Cleavage buffer</td>
      <td>Overnight TEV cleavage at 4°C to remove His tag</td>
    </tr>
    <tr>
      <td>3. Phosphatase treatment</td>
      <td>Lambda protein phosphatase</td>
      <td>—</td>
      <td>Phosphatase buffer</td>
      <td>100 units/mg protein at room temp for 1 h; essential for obtaining diffracting crystals</td>
    </tr>
    <tr>
      <td>4. Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td>—</td>
      <td>Gel filtration buffer</td>
      <td>Final purification step</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified BK intracellular domain at approximately 7 mg/mL

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified BK intracellular domain at ~7 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>3.5 M sodium formate, 0.1 M Tris-HCl pH 8.5</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 °C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals equilibrated overnight with sodium formate increased to 4.8 M before flash freezing. Space group I422 with cell dimensions a=b=134.1 Å, c=231.6 Å, one subunit per asymmetric unit. Structure determined by SAD using selenomethionine-substituted protein. 17 Se sites found with SHELXD, phases by autoSHARP, model built in Coot, refined in PHENIX to 3.1 Å with Rwork 23.8% and Rfree 28.9%. Data collected at APS beamlines 23ID and 19ID.</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##nature10670

**Structures:**

<table class="wiki-table">
  <thead><tr>
    <th>PDB ID</th>
    <th>Resolution</th>
    <th>Space Group</th>
    <th>Construct</th>
    <th>Ligand/Co-factor</th>
  </tr></thead>
  <tbody>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3u6n">3U6N</a></td>
      <td>3.60</td>
      <td>P21212</td>
      <td>Zebrafish BK channel cytoplasmic domain residues 341-1060 with loop deletion (residues 839-872)</td>
      <td>Ca2+ (Ca2+-bound open state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 insect cells (baculovirus expression system using pFastBac-HTa vector)
- **Construct**: Intracellular fragment of human SLO1 gene (GI:26638650) residues 329-C-terminus, N-terminal His tag, TEV cleavage site, and 32-aa GCN4_LI leucine zipper

**Purification:**

- **Expression system**: Escherichia coli
- **Expression construct**: Zebrafish BK channel cytoplasmic domain (residues 341-1060) with loop deletion (839-872)
- **Tag info**: Not specified

<table class="wiki-table">
  <thead><tr>
    <th>Step</th>
    <th>Method</th>
    <th>Resin / Column</th>
    <th>Buffer + Detergent</th>
    <th>Notes</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td>—</td>
      <td>20 mM HEPES pH 8.0, 150 mM NaCl, 20 mM dithiothreitol</td>
      <td>Purified as described previously (Yuan et al., 2010)</td>
    </tr>
  </tbody>
</table>
**Final sample**: ~6 mg/ml in SEC buffer with 10 mM CaCl2 added for Ca2+-bound open conformation

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Zebrafish BK CTD at ~6 mg/ml in 20 mM HEPES pH 8.0, 150 mM NaCl, 20 mM DTT, plus 10 mM CaCl2</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM MES pH 6.3, 4% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000, 100 mM potassium sodium tartrate</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>50 mM MES pH 6.3, 6% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000, 100 mM potassium sodium tartrate, 150 mM NaCl, 10 mM CaCl2, 30% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown to ~0.2 x 0.2 x 0.3 mm. Space group P21212 with cell dimensions a=137.65, b=210.82, c=238.76 Å. Eight subunits per asymmetric unit forming two gating rings. Structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using monomeric Ca2+-bound human BK CTD (PDB 3MT5). Refined to 3.6 Å with Rwork=0.260 and Rfree=0.289. Data collected at NSLS beamline X29.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Gating ring architecture of BK channel

The cytoplasmic domain forms a tetrameric gating ring (four-fold symmetry) with each subunit comprising two tandem RCK domains (RCK1 and RCK2). RCK domains from adjacent subunits interact in a head-to-tail fashion via hydrophobic contacts (Ile441, Met442, Ile445 on RCK1 αD; Ile821, Leu822, Leu825, Phe890 on RCK2 αE). The gating ring has a diagonal distance of ~82 Å and a central hole of ~20 Å, allowing ion passage. This assembly resembles the [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) channel gating ring but is more expanded.

### Ca2+ bowl: an EF-hand-like calcium sensing motif

The [Ca2+ Bowl](/xray-mp-wiki/concepts/miscellaneous/calcium-bowl/) is a stretch of conserved aspartate residues within RCK2 located after αE, followed by a short helix (αEF). Together αE, the [Ca2+ Bowl](/xray-mp-wiki/concepts/miscellaneous/calcium-bowl/) loop, and αEF form a helix-loop-helix motif similar to EF-hand proteins like calmodulin. In the Ca2+-free (apo) state, the [Ca2+ Bowl](/xray-mp-wiki/concepts/miscellaneous/calcium-bowl/) is disordered and becomes ordered upon Ca2+ binding. Its strategic location beside the inter-subunit assembly interface suggests Ca2+ binding triggers conformational changes at the interface, altering gating ring size and leading to channel activation.

### Asp 367 high-affinity Ca2+ binding site on RCK1

Asp 367, located on the loop between αA and βB of RCK1, forms a high Ca2+ sensitivity site. Positioned in the groove between N- and C-terminal subdomains of RCK1, it is exposed to the space between the membrane and peripheral C-terminal subdomain. The surrounding chemical environment includes His365, Met513, and Glu535. His365 is involved in pH activation of BK and may interact electrostatically with Asp367 upon protonation. Met513 mutations profoundly affect Ca2+ sensitivity by maintaining local structural integrity. Glu535 may participate in Ca2+ chelation together with Asp367.

### Glu374/Glu399 low-affinity Mg2+/Ca2+ binding site

A low-affinity divalent cation binding site formed by Glu374 and Glu399 on β-strands βB and βC of RCK1. This site is positioned on the upper plateau of the gating ring near the membrane surface and close to the linker connecting the gating ring to the channel pore. Ser337 on the linker may also serve as a ligand. This site is physiologically regulated by Mg2+ and may involve residues from the intracellular-facing part of the membrane-spanning channel.

### Full BK channel model by docking pore domain

The structure includes the linker connecting the transmembrane and intracellular domains (starting from Arg329 after the pore-lining inner helix), enabling docking of a voltage-gated K+ channel pore onto the gating ring with reasonable accuracy. This generated a structural model for the full BK channel, providing insights into how the channel integrates voltage and Ca2+ signals.

### Ca2+-bound open gating ring reveals flower-petal opening of RCK1 layer

The Ca2+-bound (open) structure of the zebrafish BK gating ring (3.6 Å) shows that Ca2+ binding causes only the RCK1 layer (facing the membrane) to undergo a substantial conformational change, opening like the petals of a flower. The diagonal distance between N-terminal residues (Lys343) increases from ~70 Å in the closed state to ~82 Å in the open state. In contrast, the RCK2 layer remains nearly invariant. This asymmetric conformational change differs from prokaryotic [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/), where both layers change equally. The degree of RCK1 opening explains how Ca2+ binding can exert a force on the transmembrane pore to open it.

### Flexible interface and assembly interface in gating ring opening

The BK gating ring contains two types of inter-subunit interfaces: the flexible interface (between RCK1 N-lobe and RCK2 C-lobe of adjacent subunits) and the assembly interface (between RCK1 and RCK2 within a subunit). Ca2+ binding at the assembly interface causes conformational changes that propagate through the flexible interface, expanding the RCK1 layer. Large disordered regions at the flexible interface allow this asymmetric opening while maintaining the structural integrity of the gating ring.

### BK gating ring-MthK gating ring comparison

The [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) gating ring has eight identical RCK domains arranged with higher molecular symmetry, causing Ca2+ binding to shrink the ring's height and expand its diameter equally on both layers. In contrast, the BK gating ring has distinct RCK1 (top) and RCK2 (bottom) layers, so Ca2+ binding only opens the RCK1 layer. This comparison illustrates how evolution of molecular structure has given rise to distinct mechanical properties within the RCK domain family.


## Cross-References

- <a href="/xray-mp-wiki/concepts/rck-domain-gating-ring/">RCK Domain Gating Ring</a> — The CTD gating ring houses Ca2+ sensors and transduces Ca2+ binding to pore opening
- <a href="/xray-mp-wiki/concepts/bk-channel-gating/">BK Channel Gating Mechanism</a> — Structural basis for Ca2+-induced gating ring opening and pore activation
- <a href="/xray-mp-wiki/concepts/allosteric-coupling/">Allosteric Coupling</a> — Gating ring expansion exerts allosteric force on the transmembrane pore
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mthk/">MthK Potassium Channel</a> — Prokaryotic RCK-gated channel used for comparison and modeling
- <a href="/xray-mp-wiki/proteins/kcsaa/">KcsA Potassium Channel</a> — Closed pore model used in BK channel gating model
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/bk-channel/">Human BK (Slo1/MaxiK)</a> — Same protein family; zebrafish BK is 93% identical
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion Crystallization</a> — Method used to crystallize the zebrafish BK gating ring
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Phasing method using PDB 3MT5 as search model
- <a href="/xray-mp-wiki/concepts/miscellaneous/calcium-bowl/">Ca2+ Bowl</a> — Related biological concept
- <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a> — Additive used in purification or crystallization buffers
