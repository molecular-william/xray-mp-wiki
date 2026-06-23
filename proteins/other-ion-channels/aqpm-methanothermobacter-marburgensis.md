---
title: "AqpM (Aquaporin from Methanothermobacter marburgensis)"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0509469102]
verified: false
---

# AqpM (Aquaporin from Methanothermobacter marburgensis)

## Overview

AqpM is the aquaporin from the methanogenic archaeon Methanothermobacter marburgensis, the first structurally characterized archaeal aquaporin. The structure was determined to 1.68-Å resolution by X-ray crystallography, revealing AqpM as a member of a unique subdivision between water-selective aquaporins and water-plus-glycerol-conducting aquaglyceroporins. In AqpM, isoleucine (Ile187) replaces a key histidine residue found in the lumen of water channels (which becomes glycine in aquaglyceroporins). The selectivity filter, formed by R202, F62, I187, and the carbonyl oxygen of S196, has a diameter of 2.54 Å — intermediate between Aqp1 (1.86 Å) and GlpF (3.14 Å). The channel is occupied by water molecules with a single glycerol at the NPA region. Notably, AqpM exhibits extreme stability, maintaining activity after exposure to pH < 4.2, temperatures > 80°C, and resistance to SDS-PAGE dissociation, attributed to a larger monomer-monomer interface (3,629 Å²) than other aquaporins. The histidine-to-isoleucine substitution suggests possible adaptation for conducting larger, less polar permeants such as H₂S or CO₂, in addition to water.



## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0509469102 | 2F2B | 1.68 A | P4₁2₁2 | Full-length AqpM from Methanothermobacter marburgensis with N-terminal 10-His tag removed by Factor Xa digestion | Water and glycerol molecules in the channel; two octyl-β-D-glucoside (OG) detergent molecules (low-resolution structure only) |

## Expression and Purification

- **Expression system**: Escherichia coli, recombinant expression
- **Construct**: Full-length AqpM with N-terminal 10-His tag and Factor Xa cleavage site

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer (3 cycles, 15,000–18,000 psi at 4°C) | -- | 50 mM Tris pH 7.4, 300 mM NaCl, 1 mM PMSF | Cells lysed in solubilization buffer |
| Membrane recovery | Ultracentrifugation | -- | 50 mM Tris pH 7.4, 10% glycerol, 300 mM NaCl, 1 mM PMSF | 138,000 × g for 1 h |
| Solubilization | Solubilization in octyl-β-D-glucoside (OG) | -- | 50 mM Tris pH 7.4, 10% glycerol, 300 mM NaCl, 1 mM PMSF, 5.0% OG | Incubated at 4°C for 3 h with stirring |
| Affinity chromatography | Immobilized metal affinity chromatography (Co²⁺-Sepharose) | Co²⁺-Sepharose | 50 mM Tris pH 7.4, 300 mM NaCl, 1.2% OG, 10% glycerol, 50 mM (wash) / 300 mM (elution) imidazole | Batch binding overnight at 4°C; elution with imidazole gradient |
| Size-exclusion chromatography | SEC | Size-exclusion column | 50 mM Hepes pH 7.4, 100 mM NaCl, 1.2% OG | After tag cleavage by Factor Xa, another SEC step was performed |


## Crystallization

### doi/10.1073##pnas.0509469102

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion (PEG screen) |
| Protein sample | Purified AqpM at ~10 mg/ml in 50 mM Hepes pH 7.4, 100 mM NaCl, 1.2% OG |
| Reservoir | 100 mM Tris pH 9.0, 100 mM NaCl, 20% PEG 4000, 10% glycerol |
| Temperature | 22 °C |
| Growth time | 2-3 days to appear, ~2 weeks to full size (200-300 μm along c axis) |
| Cryoprotection | 10% glycerol in reservoir |
| Notes | Best crystals grew from protein samples dialyzed to avoid phase separation. Crystal form is tetragonal. Highest diffracting crystal grew in Tris pH 8.5, 200 mM MgCl₂, 23% PEG 4000. Data collected at ALS Beamline 8.3.1. Two structures determined: low-resolution (2.3 Å) from a crystal in the detergent-rich phase, and high-resolution (1.68 Å) from a dialyzed sample with no phase separation.
 |


## Biological / Functional Insights

### Unique selectivity filter with Ile187 replaces conserved His in water channels

AqpM's selectivity filter is formed by R202, F62, I187, and the carbonyl oxygen of S196. The critical distinction is I187 replacing the highly conserved His residue found in all water-selective aquaporins (corresponding to H182 in Aqp1). This Ile substitution makes the filter wider (2.54 Å vs. 1.86 Å in Aqp1) and more hydrophobic, creating a channel that is intermediate between water-selective aquaporins and aquaglyceroporins. The hydrophobic nature of I187 reduces water conductance efficiency compared with Aqp1 while enabling possible conductance of less polar permeants.

### Archaeal aquaporins as a distinct subfamily within the aquaporin superfamily

AqpM establishes a unique subdivision between water-selective aquaporins and aquaglyceroporins. Like other archaeal aquaporins (AfAqp from A. fulgidus, MbAqp from M. barkeri), AqpM possesses aliphatic residues at the His/Gly position of the selectivity filter rather than the canonical His of water channels or Gly of glycerol channels. This suggests archaeal aquaporins form a distinct subfamily adapted to the unique lipid environments and physiological needs of archaea.

### Extreme thermostability from large monomer-monomer interface

AqpM exhibits remarkable stability, maintaining tetrameric integrity and activity after exposure to extreme pH (<4.2) and high temperature (>80°C), and resists dissociation in 14% SDS-PAGE. This stability correlates with the largest monomer-monomer interface among structurally characterized aquaporins (3,629 Å² vs. GlpF 3,060 Å², Aqp1 3,180 Å², AqpZ 3,340 Å²). The extended helix M1 and loop A (residues 33–51) make major contributions to this interface.

### Possible gas conductance: H₂S or CO₂ as additional permeants

The substitution of the polar His with hydrophobic Ile187 at the selectivity filter suggests adaptation for less polar permeants. M. marburgensis uses CO₂ as its sole carbon source and H₂S as the terminal electron acceptor, making these molecules candidates for AqpM conductance. The structural similarity of H₂S to H₂O and the intermediate channel diameter (2.54 Å) support the hypothesis that AqpM may function as a multifunctional channel for water and gas molecules, potentially representing a novel subclass of gas-conducting aquaporins.

### Architecture of the conserved NPA motifs and carbonyl ladder

AqpM contains the canonical aquaporin NPA (Asn-Pro-Ala) motifs (N82-P83-A84 from loop B and N199-P200-A201 from loop E). Each loop provides a ladder of four carbonyl oxygens from successive amino acids into the channel lumen, spaced ~2.8 Å apart, forming a helical set of hydrogen-bond acceptors. This carbonyl ladder, together with the NPA motifs and helix dipoles, establishes the electrostatic environment for water coordination and proton exclusion characteristic of the aquaporin family.


## Cross-References

- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — AqpM is a member of the aquaporin superfamily; first structurally characterized archaeal aquaporin
- [Aquaporin-1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) — Water-selective aquaporin used as comparison for selectivity filter dimensions and conductance
- [Aquaporin Z (AqpZ)](/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/) — Bacterial water-specific aquaporin used for comparison of monomer-monomer interface
- [GlpF (Glycerol Facilitator from E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glpf/) — Aquaglyceroporin used as comparison for selectivity filter dimensions and tetramer stability
