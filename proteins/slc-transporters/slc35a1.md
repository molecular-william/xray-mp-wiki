---
title: "SLC35A1 Human CMP-Sialic Acid Transporter (mCST)"
created: 2026-06-03
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature24464, doi/10.7554##eLife.45221]
verified: false
---

# SLC35A1 Human CMP-Sialic Acid Transporter (mCST)

## Overview

SLC35A1 is the human CMP-sialic acid transporter, a member of the SLC35 family of nucleotide sugar transporters (NSTs). It imports CMP-sialic acid into the Golgi apparatus for sialylation reactions using an antiport mechanism exchanging CMP-sialic acid for CMP. SLC35A1 is mutated in congenital disorder of glycosylation IIf, resulting in a lack of sialic acid on the surface of cells. The first crystal structures of the mouse ortholog (mCST, 91% identical to human CST) were determined by Ahuja and Whorton (2019, eLife) at 2.58 A resolution in complex with CMP (PDB 6OH2) and at 2.75 A with CMP-sialic acid (PDB 6OH3) using [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/). These structures reveal a 10-TM bundle adopting the drug/metabolite transporter (DMT) superfamily fold with a pseudo-two-fold inverted symmetry. The structures define the molecular basis for nucleotide selectivity, explain disease-causing mutations, and reveal a unique lumen-facing partially-occluded conformation that represents a key intermediate in the transport cycle.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature24464 | Homology model (based on Vrg4, PDB 5OGE) | N/A | N/A | Full-length SLC35A1 homology model | CMP-sialic acid (predicted binding) |
| doi/10.7554##eLife.45221 | 6OH2 | 2.58 A | C2 | mCST DeltaC (lacking last 15 residues; residues 15-317) | CMP |
| doi/10.7554##eLife.45221 | 6OH3 | 2.75 A | C2 | mCST DeltaC (lacking last 15 residues; residues 7-317) | CMP-sialic acid |
| doi/10.7554##eLife.45221 | 6OH4 | 3.4 x 3.4 x 4.6 A (anisotropic) | P2(1) | Full-length mCST (residues 15-317) | CMP |

## Expression and Purification

- **Expression system**: Pichia pastoris SMD1168H
- **Construct**: mCST with N-terminal GFP-His10 tag and [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) site

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent extraction | -- | 25 mM HEPES pH 7.5, 150 mM NaCl, 5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) + 1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membranes resuspended and homogenized, solubilized for 1.5 hr at 4C |
| IMAC | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA agarose | 25 mM HEPES pH 7.5, 150 mM NaCl, 5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 0.1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Batch binding for 1.5 hr. Washed with 5 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), then 20 mM, then 40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/). Eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag cleavage | Protease digestion | -- | 25 mM HEPES pH 7.5, 150 mM NaCl, 5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 0.1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) added at 1:20 ratio, overnight at 4C to cleave GFP-His10 tag |
| SEC | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (GE Healthcare) | 25 mM HEPES pH 7.5, 150 mM NaCl, 0.1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Concentrated in 50 K MWCO concentrator before SEC |


## Crystallization

### doi/10.7554##eLife.45221

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion (HDVD) |
| Protein sample | mCST at 5 mg/mL in 25 mM HEPES pH 7.5, 150 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), supplemented with 20 mM CMP |
| Reservoir | 25.6-26.8% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 0.1 M Tris pH 8.5, 0.1 M magnesium acetate |
| Temperature | 20 C |
| Growth time | 5-13 days |
| Cryoprotection | Increased [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 concentration in mother liquor |
| Notes | Rectangular rod-shaped crystals. Data from 5 crystals merged. Hg and Pt derivatives prepared by soaking for [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) phasing. Anisotropic diffraction to 3.4 x 3.4 x 4.6 A. |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | mCST DeltaC at 5-7 mg/mL in 25 mM HEPES pH 7.5, 150 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Temperature | 20 C |
| Growth time | 3-6 days |
| Cryoprotection | Crystals harvested directly from LCP drop and flash-frozen in liquid N2 |
| Notes | Protein mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/). LCP crystals diffracted to 2.58 A (CMP complex) and 2.75 A (CMP-Sia complex). Rod-shaped crystals. For CMP-Sia complex, apyrase was added to maintain low CMP levels. Data from 26 crystals merged for CMP complex. |


## Biological / Functional Insights

### First crystal structure of a mammalian nucleotide sugar transporter

The mCST structures (PDB 6OH2, 6OH3) represent the first high-resolution structures of any mammalian NST. The 10-TM bundle adopts the DMT superfamily fold with pseudo-two-fold inverted symmetry between the N-terminal (TMs 1-5) and C-terminal (TMs 6-10) halves, consistent with an ancient gene duplication event.

### Nucleotide selectivity mechanism

CMP is extensively coordinated by at least 15 residues. The cytosine base is recognized by Lys55, Tyr214, and Asn210, explaining the inability to accommodate the larger guanine base of GMP. The [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) base of UMP differs at the C-4 position (carbonyl vs amine), which would alter hydrogen bonding with Asn210 and create electrostatic repulsion with Phe195. These structural features explain the >250-fold selectivity for CMP over UMP and GMP.

### Sialic acid binding cavity

The Sia moiety of CMP-Sia occupies a large cavity that was vacant in the CMP-only structure. The C-1 carboxyl interacts with Lys124 (which shifts 2 A from its position in the CMP-bound structure). The cavity adjacent to the C-5 N-acetyl group can accommodate the Neu5Gc variant, explaining why human CST can transport both Neu5Ac and Neu5Gc conjugates.

### Lumen-facing partially-occluded conformation

The mCST structures reveal a unique lumen-facing partially-occluded state not previously observed in other DMT proteins. The constriction (~6 x 4 A) between TM9 and the protein core allows CMP passage but blocks the larger CMP-Sia. TM9 is dissociated from the core while TMs 1 and 8 remain engaged, forming a lid over the substrate-binding pocket. A fully-open lumen-facing state likely requires dissociation of TMs 1 and 8 as well, resembling the conformations seen in [Vrg4 GDP-Mannose Transporter (Saccharomyces cerevisiae)](/xray-mp-wiki/proteins/slc-transporters/vrg4/) and YddG.

### Obligatory antiport mechanism

mCST functions as a nearly-obligatory antiporter requiring lumenal CMP for efficient CMP-Sia uptake (trans-stimulation). Structural comparison with the algal triose phosphate transporter GsTPT2 suggests that the occluded state involves TM9 associating with the protein core and rearrangement of TMs 5 and 10. The ~500 A2 reduction in buried surface area among TMs 1, 8, and 9 in the partially-occluded state compared to the fully-open state may explain why substrate binding is necessary to stabilize the occluded conformation.

### Disease mutation mapping

Analysis of mCST explains the effects of known disease-causing mutations in human SLC35 genes. Residues interacting with the phosphate group of CMP are hotspots for mutations causing congenital disorders of glycosylation. The T156R and E196K mutations in SLC35A1 likely impair conformational transitions during transport, while Q101H impairs substrate binding.

### Substrate-induced conformational changes detected by tryptophan fluorescence

CMP binding quenches mCST intrinsic tryptophan fluorescence through a single residue, Trp207 located at the cytoplasmic end of TM7. Mutations of Trp207 do not affect CMP binding affinity but eliminate the fluorescence response, confirming that Trp207 senses CMP-induced conformational changes rather than direct ligand contact.


## Cross-References

- [Vrg4 GDP-Mannose Transporter](/xray-mp-wiki/proteins/slc-transporters/vrg4/) — Structural homolog and reference model for the DMT superfamily fold
- [SLC35C1 Human GDP-Fucose Transporter](/xray-mp-wiki/proteins/slc-transporters/slc35c1/) — Related SLC35 family nucleotide sugar transporter
- [SLC35 Family (Nucleotide Sugar Transporters)](/xray-mp-wiki/concepts/transport-mechanisms/sl35-family/) — Transporter family classification
- [Lipidic Cubic Phase (LCP)](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method used to obtain high-resolution structures
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for purification and crystallization
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) — Method used in structure determination or purification
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Additive used in purification or crystallization buffers
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
