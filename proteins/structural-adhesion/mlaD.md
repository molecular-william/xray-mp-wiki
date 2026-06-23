---
title: E. coli MlaD MCE Protein
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.019]
verified: false
---

# E. coli MlaD MCE Protein

## Overview

MlaD is an [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/)-associated MCE (mammalian cell entry) protein from Escherichia coli that forms a homo-hexameric ring with a central hydrophobic pore. MlaD is a key component of the Mla lipid transport system, which maintains [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/outer-membrane/) [lipid asymmetry](/xray-mp-wiki/concepts/structural-mechanisms/lipid-asymmetry/) in [Gram-negative](/xray-mp-wiki/concepts/gram-negative/) bacteria. The protein associates with the MlaFEDB [ABC transporter](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) complex in the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/inner-membrane/) and interacts with the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) lipid-binding protein [MLAC](/xray-mp-wiki/proteins/mlaC), which shuttles phospholipids between the inner and outer membranes. MlaD adopts a seven-stranded beta-barrel MCE domain fold and its hexameric assembly creates a continuous hydrophobic channel from the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/inner-membrane/) into the [periplasm](/xray-mp-wiki/concepts/miscellaneous/periplasm/).

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2017.03.019 | 5UW8 | 2.0 A | C2 | Core MCE domain, residues 32-140 | none |
| doi/10.1016##j.cell.2017.03.019 | 5UW2 | 2.5 A | P212121 | [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) domain, residues 32-183 | none |

## Expression and Purification

- **Expression system**: E. coli Rosetta2 DE3
- **Construct**: Core MCE domain (residues 32-140) or [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) domain (residues 32-183) with [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) signal peptide cleavage, cloned into pET22b(+) with [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) [6xHis](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane fractionation | Emulsiflex-C3 cell disruptor, [ultracentrifugation](/xray-mp-wiki/methods/purification/ultracentrifugation/) at 35,000g and 200,000g | -- | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + -- | Membrane fraction pelleted at 200,000g |
| Solubilization | Membrane solubilization with [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | -- | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Solubilized membrane fraction |
| [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Metal [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) agarose | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash), 250 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | His-tagged MlaD purified from solubilized membranes |
| Gel filtration | Size-exclusion chromatography on [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Hexameric MlaD ring eluted as a single peak |


## Crystallization

### doi/10.1016##j.cell.2017.03.019

| Parameter | Value |
|---|---|
| Method | [sitting-drop](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) [vapor diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) |
| Protein sample | Core MCE domain (residues 32-140), concentrated to 10-60 mg/mL |
| Reservoir | 0.2 M [lithium sulfate](/xray-mp-wiki/reagents/additives/lithium-sulfate/), 0.1 M [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 15% [PEG 400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | Reservoir solution supplemented with 20% [ethylene glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) |
| Notes | [selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/)-derivatized crystals for [MAD phasing](/xray-mp-wiki/methods/crystallography/mad-phasing/) at ALS 8.3.1. Indexed to C2 space group. Phased by MAD using SHELX C/D/E pipeline. Final model: 7 copies of MCE domain forming hexameric ring. |

| Parameter | Value |
|---|---|
| Method | [sitting-drop](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) [vapor diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) |
| Protein sample | [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) domain (residues 32-183), concentrated to 10-60 mg/mL |
| Reservoir | 0.2 M [zinc acetate](/xray-mp-wiki/reagents/additives/zinc-acetate/), 0.1 M [MES](/xray-mp-wiki/reagents/buffers/mes/) pH 6.0, 15% ethanol |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | Reservoir solution supplemented with 20% [ethylene glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) |
| Notes | Native data collected at ALS 8.3.1, indexed to P212121. Phased by [molecular replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using Phaser with core MCE domain as search model. Final model: 3 copies of [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) domain; 2-fold symmetry generates hexameric ring. |


## Biological / Functional Insights

### Hexameric ring architecture with central hydrophobic pore

MlaD forms a homo-hexameric ring where each subunit contributes a seven-stranded
beta-barrel MCE domain. The hexameric assembly creates a central channel lined
with hydrophobic residues including Leu106, Leu107 at the tip of the beta5-beta6
loop, and Phe150 from the [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) helical bundle. Additional pore-lining residues
include Met141, Leu143, Leu146, Ile147, and Leu149. The hydrophobic pore is oriented
toward the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/), poised to facilitate trafficking of small hydrophobic
molecules to or from the membrane.

### Functional role in lipid transport at the inner membrane

MlaD associates with the MlaFEDB [ABC transporter](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) complex (MlaF ATPase, MlaE permease,
MlaB STAS domain) in the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/). The hexameric MlaD ring sits at the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/)
face of the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/), with its [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) [transmembrane helix](/xray-mp-wiki/concepts/transmembrane-helix/) anchoring one
face of the ring near the membrane. Mutagenesis of pore-lining residues (L106N/L107N,
Phe150Asn, [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) deletions) disrupts complementation of a delta mlaD mutant,
demonstrating that the hydrophobic pore is essential for MlaD function in maintaining
[outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) [lipid asymmetry](/xray-mp-wiki/concepts/structural-mechanisms/lipid-asymmetry/).

### MCE domain fold and conservation

The core MCE domain of MlaD adopts a seven-stranded beta-barrel fold with no similarity
to other known protein structures. MCE proteins are ubiquitous among double-membraned
bacteria and eukaryotic chloroplasts. The MlaD MCE domain serves as a structural
template for understanding the entire MCE protein superfamily, including [YEBT](/xray-mp-wiki/proteins/yebT) and
[PQIB](/xray-mp-wiki/proteins/pqiB) which form elongated tube- and syringe-like architectures by stacking multiple
MCE domains.


## Cross-References

- [MCE Protein Family](/xray-mp-wiki/concepts/protein-families/mce-protein-family/) — MlaD is the prototypical characterized member of the MCE protein superfamily
- [E. coli MlaC Lipid-Binding Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaC/) — MlaC ferries lipids between MlaD at the inner membrane and MlaA at the outer membrane
- [E. coli YebT Tube-like MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/yebT/) — YebT shares the same MCE domain fold as MlaD but forms an elongated tube of seven stacked rings
- [E. coli PqiB Syringe-like MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/pqiB/) — PqiB shares the same MCE domain fold as MlaD but forms a needle-and-syringe architecture
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for MlaD solubilization from membranes
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used for Ni-NTA affinity chromatography wash (10 mM) and elution (250 mM)
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — 0.1 M HEPES pH 7.5 used in crystallization reservoir for core MCE domain
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — 0.1 M MES pH 6.0 used in crystallization reservoir for periplasmic domain
- [vapor diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) — Entity mentioned in text
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Entity mentioned in text
