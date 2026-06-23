---
title: Stearoyl-CoA Desaturase-1 (hSCD1)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3049]
verified: false
---

# Stearoyl-CoA Desaturase-1 (hSCD1)

## Overview

[Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) desaturase-1 (SCD1) is an integral membrane enzyme in the endoplasmic reticulum that catalyzes the delta-9 desaturation of saturated fatty acyl-CoA substrates ([Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) and palmitoyl-CoA) to produce monounsaturated fatty acids ([Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) and palmitoleoyl-CoA). SCD1 belongs to the di-iron-containing desaturase family but uses a unique histidine-coordinated dimetal center rather than the carboxylate-bridged [IRON](/xray-mp-wiki/reagents/additives/iron/) center found in soluble forms. SCD1 maintains the cellular balance of saturated and monounsaturated lipids and is implicated in metabolic diseases including diabetes, obesity, and cancer. Inhibitors of SCD1 are under active investigation as therapeutic agents.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.3049 | 4ZYO | 3.25 | P3_121 | N-terminal 45 residues truncated; K60A, K62A, E63A surface mutations; residues 53-350 in final model | [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/), 2 Zn2+ |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: N-terminal hexahistidine tag with TEV protease cleavage site; N-term 45 truncated; K60A, K62A, E63A mutations
- **Notes**: SeMet labeling achieved by growing Sf9 cells in methionine-free medium with 70 mg/L SeMet before infection

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| solubilization | membrane solubilization | none | 25 mM Tris pH 7.6, 800 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.25 mM TCEP, 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membranes extracted from Sf9 cell pellets; solubilized with [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA Superflow (Qiagen) | 25 mM Tris pH 7.6, 200 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.25 mM TCEP, 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) | Eluted with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| tag cleavage | TEV protease cleavage | none | 25 mM Tris pH 7.6, 200 mM NaCl, 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.25 mM TCEP | Hexahistidine tag cleaved by TEV protease |
| flow-through purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (flow-through) | Ni-NTA Superflow (Qiagen) | 25 mM Tris pH 7.2, 200 mM NaCl, 1 mM TCEP, 0.02% [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) | Tag-free hSCD1 collected in flow-through after TEV cleavage |
| desalting | PD-10 column | none | 25 mM Tris pH 7.2, 200 mM NaCl, 1 mM TCEP, 0.02% [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) | Desalted using PD-10 column (GE Healthcare) |
| size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL (GE Healthcare) | 25 mM Tris pH 7.2, 200 mM NaCl, 1 mM TCEP, 0.02% [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) | Final polishing step; peak fractions concentrated to 8.5 mg/ml |


## Crystallization

### doi/10.1038##nsmb.3049

| Parameter | Value |
|---|---|
| Method | vapor diffusion |
| Protein sample | 8.5 mg/ml hSCD1 in 25 mM Tris pH 7.2, 200 mM NaCl, 1 mM TCEP, 0.02% [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) |
| Reservoir | 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.5, 30-35% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 220 mM sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) |
| Temperature | 4 C |
| Notes | Both native and SeMet-labeled crystals; native crystals soaked in 1 mM Ta6Br12 overnight for phasing |


## Biological / Functional Insights

### Mushroom-like architecture with transmembrane anchor

hSCD1 folds into a mushroom-like architecture consisting of a stem of four transmembrane
alpha-helices (TM stem) and a cytoplasmic domain (cap). The four transmembrane helices
form a tight hydrophobic core that presumably functions as an anchor spanning the
endoplasmic reticulum membrane. The cytoplasmic cap domain contains the catalytic center
and substrate binding site.

### Unique histidine-coordinated dimetal catalytic center

The hSCD1 structure reveals a new dimetal catalytic center coordinated by histidine
residues in histidine-box motifs (HXXXXH, HXXHH, HXXHH), rather than the carboxylate-
bridged di-[IRON](/xray-mp-wiki/reagents/additives/iron/) center found in soluble desaturases. Zn1 is coordinated by five
histidine residues, while Zn2 is coordinated by four histidine residues and a water
molecule. The dimetal center is buried among TM2, CH2, TM4, and CH8.

### Substrate binding site with hydrophobic tunnel

The [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) binding site is located at the surface of the cytoplasmic cap domain
with a prominent internal hydrophobic tunnel extending from the CoA-binding site toward
the dimetal center. The CoA head group interacts with polar residues via hydrogen bonds
and electrostatic interactions, while the acyl chain extends into the hydrophobic tunnel.
The tunnel geometry determines the regioselective cis dehydrogenation at the delta-9
position of the fatty acid chain.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane solubilization (1%) and Ni-NTA elution (0.025%)
- [Octaethylene Glycol Monododecyl Ether (C12E8)](/xray-mp-wiki/reagents/detergents/c12e8/) — Final SEC detergent (0.02%) replacing DDM for improved resolution
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer throughout purification (25 mM) and crystallization (100 mM)
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Ni-NTA affinity elution at 20 mM (solubilization) and 250 mM (elution)
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Included in Ni-NTA elution buffer (5%) for protein stabilization
- [TEV Protease](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) — Cleaved N-terminal hexahistidine tag after affinity purification
- [Tris(2-carboxyethyl)phosphine (TCEP)](/xray-mp-wiki/reagents/additives/tcep/) — Reducing agent (0.25-1 mM) in all purification buffers
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Final SEC polishing step using Superdex 200 10/300 GL column
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [IRON](/xray-mp-wiki/reagents/additives/iron/) — Additive used in purification or crystallization buffers
