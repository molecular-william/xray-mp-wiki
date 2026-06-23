---
title: "Gs Protein Alpha Subunit (Galpha s)"
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10361]
verified: false
---

# Gs Protein Alpha Subunit (Galpha s)

## Overview

The Gs protein alpha subunit (Galpha s) is the catalytic subunit of the stimulatory heterotrimeric G protein that activates adenylate cyclase. Galpha s is central to GPCR signaling as the primary transducer for Gs-coupled receptors including the beta2-adrenergic receptor. The subunit consists of two distinct domains: a Ras-like GTPase domain (Galpha sRas) that mediates receptor and Gbeta interactions, and an alpha-helical domain (Galpha sAH) that together with Galpha sRas forms the nucleotide binding pocket. The first high-resolution structure of Galpha s in complex with an activated GPCR revealed a dramatic 127-degree rotation of the alpha-helical domain relative to the Ras domain in the nucleotide-free state.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10361 | 3SNY | 3.2 A | P212121 | Gs heterotrimer (Galpha s short + His6-Gbeta1 + Ggamma2) in complex with T4L-beta2AR-[Nb35](/xray-mp-wiki/reagents/antibodies/nb35/) | Nucleotide-free |
| doi/10.1038##nature10361 | 1AZT | 2.0 A | Not specified | Galpha s-GTPgammaS complex | GTPgammaS |

## Expression and Purification

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in HighFive insect cells | — | Insect Xpress serum-free media (Lonza) | Bovine Galpha s short expressed with His6-rat Gbeta1 and bovine Ggamma2 |
| Cell lysis | Nitrogen cavitation bomb (600 p.s.i. N2, 40 min) | — | 50 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 8.0, 65 mM NaCl, 1.1 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 1 mM EDTA, 1x PTT, 1x LS, 5 mM [Beta Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 10 uM GDP | Membranes harvested by ultracentrifugation at 180,000g |
| Membrane solubilization | Detergent solubilization of washed membrane pellet | — | Wash buffer (50 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 8.0, 50 mM NaCl, 100 uM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 1x PTT, 1x LS, 5 mM [Beta Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 10 uM GDP) | Frozen pellet resuspended and flash-frozen with liquid nitrogen |


## Crystallization

### doi/10.1038##nature10361

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | 7.7 [MAG](/xray-mp-wiki/reagents/lipids/mag/) with 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) |
| Temperature | Not specified |
| Notes | Gs alpha subunit crystallized as part of the T4L-beta2AR-Gs-[Nb35](/xray-mp-wiki/reagents/antibodies/nb35/) ternary complex |


## Biological / Functional Insights

### Two-domain architecture of Galpha s

Galpha s consists of two domains: the Ras-like GTPase domain (Galpha sRas) which
interacts with the beta2 AR and Gbeta subunit, and the alpha-helical domain
(Galpha sAH). The interface between these two domains forms the nucleotide-binding
pocket. In the nucleotide-free state, the alpha-helical domain exhibits significant
flexibility, adopting variable positions relative to the Ras domain.

### Large conformational change of alpha-helical domain

The most surprising observation in the beta2 AR-Gs complex is the large displacement
of the Galpha sAH relative to Galpha sRas, representing approximately a 127-degree
rotation about the junction between the two domains. This movement occurs as a rigid
body and is attributed to the empty nucleotide-binding pocket. In the presence of
guanine nucleotide (GTP or [GDP](/xray-mp-wiki/reagents/ligands/gdp/)), the nucleotide-binding pocket is filled and the
two domains adopt a more stable, compact conformation.

### Galpha s amino- and carboxy-terminal helices mediate receptor coupling

The principal interactions between the beta2 AR and Gs involve the amino-terminal
and carboxy-terminal alpha-helices of Galpha s. The carboxy-terminal alpha-5 helix
of Galpha s docks into a cavity formed by the opening of transmembrane helices 5
and 6 of the receptor. The alpha-5 helix is displaced 6 angstroms towards the
receptor and rotated, with its carboxy-terminal end projecting into the transmembrane
core of the beta2 AR.

### Gbeta stabilizes the amino-terminal helix of Galpha s

Although Gbeta does not interact directly with the beta2 AR, it has an important
indirect role in coupling by stabilizing the amino-terminal alpha helix of Galpha s.
This stabilization is critical for efficient receptor-G protein coupling, as the
heterotrimer is required for productive signaling.


## Cross-References

- [Human Beta2-Adrenergic Receptor (beta2 AR)](/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/) — Primary receptor that activates Galpha s
- [Gs Protein Beta Subunit (Gbeta1)](/xray-mp-wiki/proteins/gpcr/gs-beta/) — Gbeta1 forms heterodimer with Galpha s in the Gs heterotrimer
- [Gs Protein Gamma Subunit (Ggamma2)](/xray-mp-wiki/proteins/gpcr/gs-gamma/) — Ggamma2 pairs with Gbeta1 as the Gbeta gamma dimer
- [Guanosine Diphosphate (GDP)](/xray-mp-wiki/reagents/ligands/gdp/) — Nucleotide bound to Galpha s in the inactive state
- [Nb35](/xray-mp-wiki/reagents/antibodies/nb35/) — Referenced in gs-alpha text
- [Beta Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) — Referenced in gs-alpha text
- [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Referenced in gs-alpha text
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in gs-alpha text
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Referenced in gs-alpha text
- [MAG](/xray-mp-wiki/reagents/lipids/mag/) — Referenced in gs-alpha text
