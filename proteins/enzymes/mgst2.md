---
title: "Human Microsomal Glutathione S-Transferase 2 (MGST2)"
created: 2026-06-09
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-21924-8]
verified: false
---

# Human Microsomal Glutathione S-Transferase 2 (MGST2)

## Overview

Microsomal [GSH](/xray-mp-wiki/reagents/additives/glutathione/) S-transferase 2 (MGST2) is an integral membrane protein belonging to the MAPEG (Membrane Associated Proteins in Eicosanoid and [GSH](/xray-mp-wiki/reagents/additives/glutathione/) metabolism) family. MGST2 catalyzes the conjugation of [GSH](/xray-mp-wiki/reagents/additives/glutathione/) ([GSH](/xray-mp-wiki/reagents/additives/glutathione/)) with leukotriene A4 (LTA4) to produce leukotriene C4 (LTC4), a key mediator of intracrine signaling of ER stress, oxidative DNA damage, and cell death in non-hematopoietic cells. The enzyme forms a homotrimer with each monomer containing four transmembrane alpha-helices, creating three potential active sites at the subunit interfaces. MGST2 exhibits a unique "one-third of the sites" reactivity mechanism where only one of the three active sites is catalytically active at a time, regulated by synchronized conformational changes including local unfolding of a 3-10 helical motif, alpha-H4 tilting, and a Trp-gate that controls solvent access through a biconical central pore.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-021-21924-8 | 6SSS | 2.49 | P1 | Full-length human MGST2 (residues 1-149) | None (apo form) |
| doi/10.1038##s41467-021-21924-8 | 6SSU | 2.49 | C2221 | Full-length human MGST2 (residues 1-149) | [GSH](/xray-mp-wiki/reagents/additives/glutathione/) ([GSH](/xray-mp-wiki/reagents/additives/glutathione/)) — bound at 2 of 3 active sites (one full occupancy, one partial 72%) |
| doi/10.1038##s41467-021-21924-8 | 6SSW | 2.99 | C2221 | Full-length human MGST2 (residues 1-149) | [GSH](/xray-mp-wiki/reagents/additives/glutathione/) sulfonic acid (GSO3-) — full occupancy at all 3 active sites |
| doi/10.1038##s41467-021-21924-8 | 6SSR | 3.8 | C2221 | Full-length human MGST2 (residues 1-149) | None (low-resolution apo form) |

## Expression and Purification

- **Expression system**: E. coli (expression construct)
- **Construct**: Full-length human MGST2 (residues 1-149) with C-terminal hexahistidine tag

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-Sepharose | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.8, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM 2-mercaptoethanol, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 20-40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Elution with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); 0.1 mM [GSH](/xray-mp-wiki/reagents/additives/glutathione/) added to elution buffer for structural studies |
| S-hexylglutathione [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | S-hexylglutathione agarose | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM 2-mercaptoethanol, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1 mM [GSH](/xray-mp-wiki/reagents/additives/glutathione/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Elution with 30 mM probenecid in same buffer |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 16/600 | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1 mM TCEP, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1 mM [GSH](/xray-mp-wiki/reagents/additives/glutathione/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Protein concentrated to 30 mg/ml by ultrafiltration; final sample stored at -80 C |


## Crystallization

### doi/10.1038##s41467-021-21924-8

| Parameter | Value |
|---|---|
| Method | Not specified in raw paper |
| Protein sample | Purified MGST2 at 30 mg/ml in 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1 mM TCEP, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Notes | Four crystal forms obtained: apo form (6SSS, P1, 2.49 A), GSH-bound form (6SSU, C2221, 2.49 A), GSO3--bound form (6SSW, C2221, 2.99 A), and low-resolution form (6SSR, C2221, 3.8 A) |


## Biological / Functional Insights

### One-third of the sites reactivity mechanism in MGST2

MGST2 restricts catalysis to only one of its three active sites at a time. The holo structure reveals asymmetric [GSH](/xray-mp-wiki/reagents/additives/glutathione/) binding: one site has full-occupancy [GSH](/xray-mp-wiki/reagents/additives/glutathione/) with a catalytically productive conformation, a second site has partial (72%) [GSH](/xray-mp-wiki/reagents/additives/glutathione/) occupancy, and the third site is empty. This asymmetry is regulated by a 3-10 helical motif (residues 101-104) at each active site. Only the fully occupied site has a stable 3-10 helix; partially occupied and empty sites show disordered loop conformations. Cooperative local unfolding of the 3-10 helix in one subunit at a time is coupled to global conformational changes including alpha-H4 tilting and loop L opening, enabling sequential substrate binding, catalysis, and product release.

### Conformational changes in the biconical central pore and Trp-gate

The MGST2 central channel formed by alpha-H2 of each monomer has a biconical hourglass shape, with a constricted bottleneck created by Pro61-induced kink. [GSH](/xray-mp-wiki/reagents/additives/glutathione/) binding induces: (1) widening of the cytoplasmic cone (Val57 sidechain reorientation increases gap from ~4.7 A to ~7.8 A); (2) closure of a Trp-gate at the luminal side (Trp72 rotamer transition); (3) stabilization of the Pro61 kink narrowing the central pore; (4) rigidification of the entire complex. These synchronized changes restrict solvent entry to create a hydrophobic environment optimal for binding the hydrophobic second substrate LTA4, while the apo state has an open Trp-gate and increased solvent accessibility facilitating [GSH](/xray-mp-wiki/reagents/additives/glutathione/) entry.

### Role of Arg104 in GSH activation

Arg104 interacts with the [GSH](/xray-mp-wiki/reagents/additives/glutathione/) thiol group and is essential for catalytic activity. Mutation to Ala or Lys renders MGST2 completely inactive and unable to form the thiolate anion (monitored at 239 nm). In the GSH-bound structure, Arg104 is located in the 3-10 helical motif and its interaction with [GSH](/xray-mp-wiki/reagents/additives/glutathione/) stabilizes the catalytically competent conformation. Arg104 is hydrated in a water pocket within the active site, and solvent accessibility increases upon 3-10 helix unfolding in the apo state.

### Trp72 gate mutations impair catalytic activity

Trp72 forms a gate at the luminal side of the central pore that regulates solvent access. Trp72Ala and Trp72Ile mutants exhibit significantly attenuated LTC4 synthase activity (25-50% of wild-type), despite being located far from the catalytic site. This demonstrates that the global conformational changes regulating solvent access through the central pore are essential for catalysis, not just local active site chemistry.


## Cross-References

- [Human Leukotriene C4 Synthase (LTC4S)](/xray-mp-wiki/proteins/enzymes/ltc4-synthase/) — Related MAPEG family enzyme that also catalyzes LTC4 synthesis from LTA4 and GSH; structural comparison
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [GSH](/xray-mp-wiki/reagents/additives/glutathione/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
