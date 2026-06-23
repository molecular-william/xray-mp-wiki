---
title: Jumping Spider Rhodopsin-1 (JSR1)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1902192116]
verified: false
---

# Jumping Spider Rhodopsin-1 (JSR1)

## Overview

The jumping spider rhodopsin-1 (JSR1) from Hasarius adansoni is a class A G protein-coupled receptor (GPCR) that functions as a bistable, light-sensitive rhodopsin. The crystal structure of JSR1 bound to the inverse agonist 9-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) was determined at 2.1 Å resolution (Varma et al., 2019, PDB 6I9K). Unlike monostable rhodopsins such as [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/), bistable rhodopsins undergo a two-photon bidirectional photoreaction in which the Schiff base remains protonated and the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) bound throughout the photocycle. The JSR1 structure reveals a water-mediated hydrogen bond network around the Schiff base involving Glu-194 and Ser-199 that serves as the counterion system, with Tyr-126 occupying the proximal counterion position instead of a glutamate. This architecture is similar to squid rhodopsin but distinct from [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/). The transmembrane bundle of JSR1 adopts an "activation-ready" conformation more similar to non-photosensitive class A GPCRs than to [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/). The receptor also contains a DRY motif (rather than the ERY motif in vertebrate opsins) and an extended water trail connecting the ligand-binding pocket to the G protein-binding site, suggesting JSR1 as a potential model system for studying structure-function relationships of both photosensitive and non-photosensitive class A GPCRs.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1902192116 | 6I9K | 2.1 A | P 1 21 1 | Wild-type JSR1 expressed in HEK293 GnTI- cells; reconstituted with 9-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/); purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/); deglycosylated with [ENDOH](/xray-mp-wiki/reagents/additives/endoh/) | 9-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) (inverse agonist) |

## Expression and Purification

### Purification Workflow

- **Expression system**: HEK293 GnTI- cells (mammalian suspension culture)
- **Expression construct**: Wild-type JSR1
- **Tag info**: C-terminal 1D4 tag (for immunoaffinity purification)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Mechanical lysis using handheld dounce homogenizer |  | 50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2, cOmplete EDTA-free protease inhibitors | Frozen cell pellets thawed and lysed; all steps under 640 nm dim red light |
| [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) reconstitution | Incubation with 30 uM 9-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) |  | 50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2 | Overnight incubation at 4 C; identical procedure for 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) sample |
| Membrane isolation | Differential centrifugation |  | 50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2 | Sequential spins at 500 x g and 100,000 x g; membrane resuspended in buffer B |
| Solubilization | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) solubilization |  | 50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2 + 19.5 mM n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | 2 h incubation at 4 C; centrifuged at 100,000 x g for 50 min |
| Immunoaffinity chromatography | Anti-1D4 antibody affinity | CNBr-activated Sepharose 4B conjugated with anti-1D4 antibody | 50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2, 0.195 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.195 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Resin incubated overnight at 4 C; eluted in buffer D (same buffer with 0.8 mg/ml 1D4 peptide) |
| ConA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Concavalin A lectin affinity | Concavalin A Sepharose 4B | 50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2, 0.195 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 1 mM CaCl2, 1 mM MnCl2 + 0.195 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Removes misfolded/non-glycosylated receptor; elution with linear gradient of methyl-alpha-D-mannopyranoside |
| Deglycosylation | Endoglycosidase H treatment |  | 50 mM HEPES pH 6.5, 150 mM NaCl, 3 mM MgCl2, 0.195 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.195 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | 1/500x [ENDOH](/xray-mp-wiki/reagents/additives/endoh/) (2.5 U stock), overnight incubation at 4 C |

**Final sample**: Purified JSiR1 (9-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) bound) in [DDM](/xray-mp-wiki/reagents/detergents/ddm/)
**Purity**: OD 280/505 nm ratio between 2.8 and 3.5


## Crystallization

### doi/10.1073##pnas.1902192116

| Parameter | Value |
|---|---|
| Method | Lipidic Cubic Phase (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (9.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/)) |
| Temperature | 20 C |
| Notes | JSiR1 concentrated to 20-30 mg/ml and mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) in 40:60 ratio (protein:lipid) to form LCP. Crystallization screening using mosquito LCP robot at 4 C with 100 um glass Laminex plates. Optimized conditions: 31-36% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 100 mM Bis-Tris pH 6.5. Data collected at SLS beamline PX1 (wavelength 1.000 A, 16 M Eiger detector). Anisotropic diffraction: 2.5 A, 2.1 A, 2.3 A along a*, b*, c* axes. STARANISO-processed data. Two datasets merged and scaled with Aimless. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using squid rhodopsin (PDB 2Z73).
 |


## Biological / Functional Insights

### Water-mediated counterion system in bistable rhodopsins

The JSR1 structure reveals a water-mediated hydrogen bond network connecting the protonated Schiff base to Glu-194 (distal counterion) via Ser-199. This "Glu-water-Ser" triad differs from [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) where Glu-113 serves as a direct proximal counterion. In JSR1, Tyr-126 occupies the proximal position (3.28), which is Glu-113 in [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/). This water-mediated system is a key feature distinguishing bistable from monostable rhodopsins and enables the two-photon bidirectional photocycle where the Schiff base remains protonated throughout.

### DRY motif and activation-ready conformation

JSR1 contains a DRY motif (Asp-147, Arg-148, Tyr-149) at the cytoplasmic end of TM3, characteristic of ligand-binding class A GPCRs, in contrast to the ERY motif in vertebrate visual opsins. Molecular dynamics simulations show a double ionic lock: an intrahelical salt bridge between Arg-148 and Asp-147, and an interhelical salt bridge between Arg-148 and Glu-272. The interhelical interaction is more stable than the intrahelical component. The transmembrane bundle conformation resembles the inactive state of other class A GPCRs, with conserved tyrosine residues (5.58 and 7.53) oriented toward the DRY motif, unlike [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) where they point away from the bundle.

### Extended water trail connecting ligand pocket to G protein site

A network of ordered water molecules spans the entire length of the transmembrane region, connecting the retinal-binding pocket to the cytoplasmic G protein-binding site. This water trail is more extensive than in [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) and includes water molecules that participate in the Schiff base counterion system. The extensive hydration of the transmembrane region may contribute to the conformational plasticity of bistable rhodopsins and their ability to undergo reversible photocycles.

### G protein promiscuity of JSR1

Functional assays demonstrated that JSR1 activates Gi in vitro, and previous studies suggested it also activates Gq in vivo, indicating inherent promiscuity in G protein activation similar to many class A GPCRs. This is distinct from the highly specialized G protein coupling of [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) (transducin) and highlights the similarity of JSR1 to non-photosensitive GPCRs.

### Conserved structural features between bistable rhodopsins

Comparison of JSR1 with squid rhodopsin reveals shared architectural features: both have a tyrosine at the proximal counterion position (3.28), a distal glutamate counterion (45.44), and a DRY motif. However, they differ at position 45.49 (Ser in JSR1, Asn in squid rhodopsin) and in the presence of an ordered water molecule mediating the Glu-194-Ser-199-Schiff base network in JSR1, which is absent in squid rhodopsin structures. These differences may reflect distinct dynamical properties of the two bistable rhodopsins.


## Cross-References

- [Bovine Rhodopsin (Monostable)](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) — Reference monostable rhodopsin; structural comparison of counterion system and activation mechanism
- [Squid Rhodopsin (Bistable)](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) — Reference bistable rhodopsin; comparison of water-mediated counterion network and retinal-binding pocket
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for crystallization of JSR1
- [n-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification of JSR1
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Lipid component used in LCP crystallization
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in JSR1 purification and crystallization
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [ENDOH](/xray-mp-wiki/reagents/additives/endoh/) — Additive used in purification or crystallization buffers
- [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) — Additive used in purification or crystallization buffers
