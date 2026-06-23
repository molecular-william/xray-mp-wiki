---
title: "GlpF (Glycerol Facilitator from E. coli)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##414872a, doi/10.1126##science.1067778, doi/10.1126##science.290.5491.481, doi/10.1126##science.290.5497.481]
verified: false
---

# GlpF (Glycerol Facilitator from E. coli)

## Overview

GlpF is the [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) facilitator (aquaglyceroporin) from Escherichia coli, a
member of the [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) (AQP) superfamily. It forms a homotetrameric channel
that facilitates the passive diffusion of glycerol and other small linear
polyols across the membrane, while being impermeable to protons and ions.
The original structure of GlpF with bound glycerol was determined at 2.2 A
resolution (Fu et al., Science 2000), revealing three glycerol molecules in
single file within an amphipathic channel. The selectivity filter, formed by
Trp48, Phe200, and Arg206, creates an electrostatic triangle that polarizes
successive hydroxyl groups of permeant alditols. Later structures of the
water-bound form (GlpF-G) and the W48F/F200T mutant were determined at
2.7-2.8 A and 2.1 A resolution, respectively, revealing the structural
basis for water conduction and proton exclusion. Combined with molecular
dynamics simulations, these structures established the mechanism by which
the conserved NPA (Asn-Pro-Ala) motifs and helix dipoles establish a
bipolar water orientation that blocks proton conduction.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1067778 | 1FX8 | 2.2 | — | Full-length GlpF ([Glycerol](/xray-mp-wiki/reagents/additives/glycerol/)-bound, GlpF+G) | [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |

## Expression and Purification

- **Expression system**: E. coli
- **Notes**: Overexpressed, purified, and crystallized as described in Fu et al. (2000) (PDB 1FX8)

### Purification Workflow

#### Source: doi/10.1126##science.290.5491.481

- **Expression system**: E. coli K12
- **Expression construct**: GlpF with N-terminal [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) and thrombin cleavage site
- **Tag info**: [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/), removed by thrombin cleavage

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Nickel affinity chromatography | Affinity chromatography | Ni-NTA |  | [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) purification |
| Size-exclusion chromatography | SEC | — |  | Purified by SEC after nickel affinity |

**Final sample**: 15-20 mg/ml in crystallization buffer

#### Source: doi/10.1126##science.1067778


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Overexpression and purification | As described in Fu et al. (2000) | — |  | Purification protocol for GlpF from E. coli as previously established |


## Crystallization

### doi/10.1126##science.290.5491.481

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Reservoir | 28% (w/v) [Peg](/xray-mp-wiki/reagents/additives/peg/) 2000, 100 mM [Bicine](/xray-mp-wiki/reagents/buffers/bicine/), 15% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 35 mM [[OG](/xray-mp-wiki/reagents/detergents/og/)](/xray-mp-wiki/reagents/n-octyl-beta-d-glucoside/), 300 mM MgCl2, 5 mM DTT |
| Temperature | 100 K (cryo) |

### doi/10.1126##science.1067778

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Reservoir | 15% (w/w) xylose (for GlpF-G) or 15% (w/w) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (for GlpF+G) |
| Temperature | 100 K (cryo) |
| Notes | Crystals grown in space group I422, isomorphous to crystals previously grown in 15% (w/w) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (PDB 1FX8). Xylose was used as a non-transported substrate replacement for [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) to obtain the water-bound form. |


## Biological / Functional Insights

### Selectivity filter and amphipathic channel mechanism

The GlpF channel is strongly amphipathic, with a hydrophobic corner formed by Trp48 and Phe200 and polar interactions provided by Arg206, Gly199, and Ala201. The selectivity filter is only large enough to accommodate a single CH-OH group at a time, requiring alditols to pass in single file. G2 and G3 are tightly organized in the selectivity filter, where the alkyl backbone of [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) is wedged against the hydrophobic corner and successive hydroxyl groups form hydrogen bonds with acceptor and donor atoms. An electrostatic triangle formed by Glu152 (via main-chain amides of Phe200 and Ala201), Arg206, and the carbonyls of Gly199/Phe200 polarizes successive OH groups on permeant alditols. The structure shows that any permeant molecule must be polarizable in section parallel to the plane of the membrane.

### Stereoselective preference for glycerol and linear carbohydrates

GlpF demonstrates stereoselectivity for linear alditols. Ribitol (all OH groups with same stereospecific relation) shows ~10-fold faster transport than D-arabitol (mixed hydroxyl arrangement), measured by stopped-flow light scattering of reconstituted proteoliposomes. The carbon backbone must line up along the channel axis, and CHOH groups adjacent to the G2 site place carbon in one of two tetrahedrally disposed sites with different environments, explaining the stereoselectivity.

### Bipolar water orientation mechanism for proton exclusion

The mechanism of proton exclusion in aquaporins is based on a bipolar orientation of water molecules within the channel. MD simulations of GlpF-G reveal a hydrogen-bonded single file of water molecules in the 20 A constriction region. Starting from the NPA center (Asn68 and Asn203), water molecules are oriented in opposite directions in the two halves of the channel, with their hydrogen atoms pointing toward the exits. The central water molecule at the NPA motifs is hydrogen bonded to the NH2 groups of both Asn68 and Asn203, with its dipole restrained perpendicular to the channel axis. This arrangement prevents the formation of a Grotthuss-type proton wire, as the bipolar orientation means successive O-H bonds are oriented away from the central water.

### Role of NPA motifs and helix dipoles in water orientation

The conserved NPA (Asn-Pro-Ala) motifs and the alpha-helices M3 and M7 together establish the electrostatic field that maintains bipolar water orientation. The Asn68 and Asn203 NH2 groups specifically hydrogen bond to a single water molecule at the channel center, making its lone electron pairs unavailable as proton acceptors. Opposite the NPA motifs across the channel are only hydrophobic residues (Ile187, Val52, Leu159) that prohibit alternative hydrogen bonding patterns. The dipoles of the half-membrane spanning helices M3 and M7 generate electrostatic fields directed toward the channel center. MD simulations where these charges were turned off resulted in breakdown of the bipolar orientation and formation of a uniform water orientation (potential proton wire).

### Selectivity filter and water permeability

The selectivity filter (SF) region of GlpF shows low water occupancy in both crystal structures and MD simulations, contributing to the low water permeation rate. The SF-lining residues Trp48, Phe200, and Arg206 undergo subtle conformational changes between the [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/)-bound and water-bound states. The W48F/F200T double mutant increases both the size and polarity of the SF region, resulting in a 25% increase in water permeation (light scattering assays) and a 38% increase in permeation events (MD simulations). Water density at the SF region increases significantly in the mutant, while the bipolar water orientation is preserved, predicting that this mutant also remains impermeable to protons.


## Cross-References

- [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — GlpF is a member of the aquaporin superfamily; the proton exclusion mechanism described here applies to the entire AQP family
- [Aquaporin Z (AqpZ)](/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/) — Related aquaporin water channel from E. coli; same superfamily as GlpF
- [Human Aquaporin 2](/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-2/) — Human homolog in the aquaporin family; same NPA motif mechanism
- [Human Aquaporin 4](/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-4/) — Human homolog in the aquaporin family; conserved NPA motif and bipolar water orientation mechanism
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in glpf text
- [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — Referenced in glpf text
- [Bicine](/xray-mp-wiki/reagents/buffers/bicine/) — Referenced in glpf text
- [OG](/xray-mp-wiki/reagents/detergents/og/) — Referenced in glpf text
- [Peg](/xray-mp-wiki/reagents/additives/peg/) — Referenced in glpf text
- [Aquaporin-1 (AQP1)](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) — Water-specific aquaporin used as structural comparison; AQP1 constriction region is narrower and more hydrophilic, excluding glycerol
- [Glpf](/xray-mp-wiki/proteins/other-ion-channels/glpf/) — Referenced in glycerol-facilitator text
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Referenced in glycerol-facilitator text
