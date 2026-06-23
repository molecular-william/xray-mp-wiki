---
title: NrfH Quinol Dehydrogenase from Desulfovibrio vulgaris
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##SJ.EMBOJ.7601439]
verified: false
---

# NrfH Quinol Dehydrogenase from Desulfovibrio vulgaris

## Overview

NrfH is a membrane-bound cytochrome c quinol dehydrogenase from Desulfovibrio vulgaris Hildenborough that serves as the electron donor to the cytochrome c nitrite reductase NrfA. NrfH belongs to the NapC/NirT family of quinol-oxidizing cytochromes widespread in bacterial respiratory chains. The protein comprises an N-terminal transmembrane helix and a periplasmic globular domain that binds four c-type haems arranged in alternating stacked and perpendicular di-haem motifs. NrfH was crystallized as a stable complex with its physiological partner NrfA, forming a large alpha4beta2 quaternary arrangement (approximately 150 x 120 x 95 A). The 2.3 A crystal structure reveals highly unusual haem coordination: haem 1 is a methionine-coordinated high-spin haem (Met49 as proximal ligand instead of the canonical His from the CXXCH motif, with Asp89 occupying the distal position), which is unprecedented in biological systems. Haem 4 is coordinated by His140 (proximal) and Lys331 from the internal NrfA subunit (distal). A menaquinol-binding cavity near haem 1 includes conserved residues Lys82, Gly86, and Asp89.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##SJ.EMBOJ.7601439 | 2J7A | 2.3 A | P2_12_12_1 | NrfH-NrfA complex from Desulfovibrio vulgaris Hildenborough, native protein solubilized in 0.015% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Four c-type haems per NrfH monomer; menaquinol binding site near haem 1 |

## Expression and Purification

- **Expression system**: Desulfovibrio vulgaris Hildenborough (native)
- **Construct**: Native NrfHA complex isolated from D. vulgaris membranes

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane extraction | Detergent solubilization | -- | Not specified + 0.015% (w/v) dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Native NrfHA complex solubilized from D. vulgaris membranes using [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Purification | Not specified | -- | Not specified + 0.015% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Complex purified as previously described (Rodrigues et al., 2006) |


## Crystallization

### doi/10.1038##SJ.EMBOJ.7601439

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | NrfHA complex at 5 mg/ml in 0.015% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 10% [PEG](/xray-mp-wiki/reagents/additives/peg/) 4K (polyethylene glycol 4000), pH 7.5 |
| Temperature | 277 K |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals belong to space group P2_12_12_1 with cell parameters a = 79.4, b = 256.8, c = 579.2 A. Asymmetric unit contains 12 NrfA and 6 NrfH molecules. Data collected at Swiss Light Source using three-wavelength MAD experiment based on [IRON](/xray-mp-wiki/reagents/additives/iron/) atoms. |


## Biological / Functional Insights

### Novel methionine-coordinated high-spin haem

NrfH haem 1 is a methionine-coordinated high-spin haem, unprecedented in biological systems. The proximal ligand is Met49 (located two residues downstream of the CXXCH motif), not the canonical histidine of the haem c-binding sequence (CXXCHXM). Asp89 occupies the distal position but is not coordinated to the [IRON](/xray-mp-wiki/reagents/additives/iron/) (no continuous electron density). This methionine coordination may be associated with a higher redox potential favouring reduction by menaquinol. EPR studies confirmed the presence of two high-spin haems in the complex, one from NrfA and one from NrfH.

### Menaquinol binding site

A pronounced cavity of 390 A^2 surface area and 430 A^3 volume is located near NrfH haem 1 between the haem and the second membrane helix, proposed as the menaquinol-binding site. The cavity includes highly conserved residues Lys82, Gly86, and Asp89. Mutagenesis of equivalent residues in W. succinogenes NrfH reduced electron transport activity to 1-4% of wild-type. Menaquinol was docked into the cavity, forming potential hydrogen bonds with Asp89 (3.0 A to O4 oxygen) and Lys82 (2.8 A to O1 oxygen). The cavity entrance is directed towards the membrane region, and protons from menaquinol oxidation are likely released to the periplasm.

### Asymmetric haem arrangement in the NrfHA complex

The NrfHA complex forms an alpha4beta2 quaternary arrangement with striking asymmetry: NrfH haem groups are positioned non-symmetrically with respect to the two NrfA molecules. Only the internal NrfA monomer has haems in close proximity to NrfH haems (edge-to-edge distances: NrfH haem 4 to NrfA haem 2 = 12.1 A, to NrfA haem 5 = 8.5 A), while external NrfA haems are >17 A away. This asymmetry suggests electron transfer proceeds from NrfH haem 1 (menaquinol site) through haem 2, 3, 4, then to NrfA haems 5 and 2.

### Haem 4 coordination by NrfA lysine

NrfH haem 4 has a unique inter-protein coordination: the proximal ligand is His140 and the distal ligand is Lys331 from the internal NrfA subunit. This is among the first examples of a lysine serving as a haem [IRON](/xray-mp-wiki/reagents/additives/iron/) ligand in an electron transfer complex, and it ensures efficient directional electron transfer from NrfH to NrfA.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for NrfHA complex solubilization at 0.015% (w/v)
- [Multi-wavelength Anomalous Diffraction (MAD)](/xray-mp-wiki/methods/structure-determination/multi-wavelength-anomalous-diffraction/) — MAD phasing using iron atoms used to solve NrfH structure
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant (10% PEG 4K)
- [IRON](/xray-mp-wiki/reagents/additives/iron/) — Additive used in purification or crystallization buffers
