---
title: MtTMEM175 K+ channel from Marivirga tractuosa
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.53683]
verified: false
---

# MtTMEM175 K+ channel from Marivirga tractuosa

## Overview

TMEM175 is a family of non-canonical K⁺ channels found in animals, eubacteria,
and archaea that are essential for lysosomal pH regulation and autophagosome
turnover. Unlike all known K⁺ channels, TMEM175 channels lack a P-loop selectivity
filter. The X-ray crystal structure of MtTMEM175 from Marivirga tractuosa was
determined at 2.4 Å resolution in complex with a novel nanobody-MBP fusion chaperone
('macrobody', Mb₅₁H₀₁). MtTMEM175 assembles as a tetramer with each subunit
containing six transmembrane helices. The structure reveals two K⁺ ion binding
sites: a hydrated K⁺ ion (1K⁺) at the extracellular pore entrance coordinated
by backbone carbonyl oxygens of Leu42, Ser43, and Ser44 in an eightfold square
antiprism geometry, and a second K⁺ ion (2K⁺) deeper in the pore. A highly
conserved threonine layer (Thr38 in MtTMEM175; Thr49/Thr274 in human TMEM175)
conveys basal K⁺ selectivity, with an additional serine layer (Ser45 in human
TMEM175) contributing to the higher selectivity of the human channel (PK/PNa
~10-35 vs ~4 in bacterial channels). A bulky hydrophobic gate formed by Leu35
occludes the pore in the closed state. Channel opening is proposed to involve
iris-like rotation of helix 1, simultaneously relocating the gate and exposing
the selectivity filter residues to the pore lumen. The human TMEM175 channel
is a Parkinson disease risk gene.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.53683 | 6HD8 | 2.4 | P2₁2₁2₁ | MtTMEM175 tetramer in complex with macrobody Mb₅₁H₀₁ (nanobody fused to N-terminally truncated MBP) | K⁺ ions (1K⁺ hydrated at extracellular entrance, 2K⁺ in pore) |
| doi/10.7554##eLife.53683 | 6HD9 | 2.4 | P2₁2₁2₁ | MtTMEM175 tetramer with Rb⁺ soak | Rb⁺ |
| doi/10.7554##eLife.53683 | 6HDA | 2.4 | P2₁2₁2₁ | MtTMEM175 tetramer with Cs⁺ soak | Cs⁺ |
| doi/10.7554##eLife.53683 | 6HDB | 2.4 | P2₁2₁2₁ | MtTMEM175 tetramer with Zn²⁺ soak | Zn²⁺ |
| doi/10.7554##eLife.53683 | 6HDC | 2.4 | P2₁2₁2₁ | MtTMEM175 T38A mutant in complex with Mb₅₁H₀₁ | -- |
| doi/10.7554##eLife.53683 | 6SWR | 2.4 | P2₁2₁2₁ | MtTMEM175 tetramer, additional dataset | K⁺ |

## Expression and Purification

- **Expression system**: E. coli MC1061
- **Construct**: MtTMEM175 (UniProt E4TN31) from Marivirga tractuosa (DSM 4126) cloned into pBXC3H with C-terminal deca-histidine tag and HRV 3C protease cleavage site. For HEK expression, cloned into pcDXC3MS with C-terminal SBP tag.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Microfluidizer | -- | 150 mM KCl, 10 mM Hepes-NaOH pH 7.6, 10% glycerol + -- | Membranes pelleted by ultracentrifugation |
| Solubilization | Detergent solubilization | -- | 150 mM KCl, 10 mM Hepes-NaOH pH 7.6, 10% glycerol + 1% (w/v) n-dodecyl-β-D-maltopyranoside (DDM) | Solubilized for 1 hr at 4°C with protease inhibitors. Insoluble material removed by centrifugation at 42,000 rpm (45 Ti rotor) |
| Streptactin affinity | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | Strep-Tactin Superflow high capacity | 150 mM KCl, 10 mM Hepes-NaOH pH 7.6, 10% glycerol, 50 µg/mL E. coli polar lipids, 0.03% DDM + 0.03% DDM | Eluted with wash buffer containing 5 mM d-desthiobiotin. Tag cleaved with HRV 3C protease |
| Complex formation and SEC | [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | Superdex 200 10/300 | 150 mM KCl, 5 mM Hepes-NaOH pH 7.6, 2.5 mM maltose, 0.03% DDM + 0.03% DDM | MtTMEM175 mixed with Mb₅₁H₀₁ at 2.2-2.5:1 molar ratio. Peak fractions concentrated to 8-16 mg/mL for crystallization |


## Crystallization

### doi/10.7554##eLife.53683

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | MtTMEM175-Mb₅₁H₀₁ complex at 8-16 mg/mL, mixed with E. coli polar lipids (100 µg/mL) and DM (0.3% final) |
| Reservoir | 100 mM Tris-HCl pH 8.5, 150 mM NaCl, 150 mM MgCl₂, 28-30% PEG400 |
| Temperature | 20°C |
| Growth time | 14 days (plus 3-4 hr dehydration with 36% PEG400) |
| Cryoprotection | Cryo-protected with mother liquor at 36% PEG400, flash-frozen in liquid propane or liquid nitrogen |
| Notes | Best crystals obtained after dehydration. Some crystals soaked with 5 mM KPtCl₄ followed by back-soaking for phasing. Crystals soaked with Cs⁺, Rb⁺ by replacing 150 mM KCl in cryo-protecting solution with 150 mM CsCl or RbCl. Zn²⁺ soaks with 0.5-2.5 mM ZnCl₂. |


## Biological / Functional Insights

### Non-canonical K+ selectivity without P-loop

MtTMEM175 achieves K⁺ selectivity without a canonical P-loop selectivity filter — a hallmark of all other known K⁺ channels. Instead, a conserved threonine layer (Thr38 in MtTMEM175, Thr49/Thr274 in hTMEM175) provides selectivity through side-chain hydroxyl groups that are exposed to the pore lumen only in the open (conductive) conformation.

### Two-tier selectivity in human TMEM175

The human TMEM175 channel achieves higher K⁺ selectivity (PK/PNa ~10-35) than bacterial homologs (PK/PNa ~2-5) through an additional serine layer (Ser45 in hTMEM175 first repeat) that works in conjunction with the conserved threonine layer. Mutating Ser45 to alanine reduces selectivity to bacterial levels and abolishes Zn²⁺ and 4-AP sensitivity.

### Hydrophobic gate and iris-like opening mechanism

The pore is occluded by Leu35, a bulky hydrophobic residue that forms a physical gate in the closed state. Channel opening is proposed to involve an 8-15° clockwise rotation of helix 1 (viewed from intracellular), which simultaneously swings the bulky gate residues out of the pathway and exposes the conserved threonine selectivity layer to the pore lumen.

### Macrobody chaperone for crystallization

The structure was solved using a novel 'macrobody' chaperone — a nanobody fused to a C-terminal N-terminally truncated maltose-binding protein (MBP) — which greatly improved crystal diffraction from ~10 Å to 2.4 Å. This chaperone scaffold may have broad applications in membrane protein crystallography.


## Cross-References

- [KcsA K+ channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Canonical P-loop K+ channel with different selectivity filter architecture
- [NaK channel](/xray-mp-wiki/proteins/voltage-gated-channels/nak-channel/) — Non-selective cation channel sharing tetrameric architecture
- [Alternating access mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Channel gating mechanism vs transporter alternating access
