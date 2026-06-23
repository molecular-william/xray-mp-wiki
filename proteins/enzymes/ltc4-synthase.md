---
title: Human Leukotriene C4 Synthase (LTC4S)
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature05936, doi/10.1038##NATURE06009, doi/10.1074##jbc.M113.534628]
verified: false
---

# Human Leukotriene C4 Synthase (LTC4S)

## Overview

Leukotriene C4 synthase (LTC4S) is a membrane-bound enzyme in the MAPEG (Membrane-Associated Proteins in Eicosanoid and [GSH](/xray-mp-wiki/reagents/additives/glutathione/) metabolism) family that catalyzes the conjugation of leukotriene A4 (LTA4) with [GSH](/xray-mp-wiki/reagents/additives/glutathione/) to form leukotriene C4 (LTC4), a key step in the biosynthesis of cysteinyl leukotrienes. LTC4 is a potent lipid mediator involved in bronchoconstriction, vascular permeability, and inflammation in asthma and allergic diseases. The enzyme forms a homotrimer, with four trimers assembling into a dodecameric arrangement in the crystal lattice. The first structure was solved at 3.3 Å resolution (PDB 2PNO, space group C2221) by SeMet SAD phasing, with 12 LTC4S molecules forming four trimers in the asymmetric unit. Each subunit adopts an integral membrane protein fold with four transmembrane helices. The active site contains a bound [GSH](/xray-mp-wiki/reagents/additives/glutathione/) molecule that is coordinated by residues from adjacent subunits within the trimer, consistent with the catalytic mechanism involving [GSH](/xray-mp-wiki/reagents/additives/glutathione/) conjugation. A V-shaped valley between monomers serves as the putative LTA4 binding site, with a bound DDM molecule mimicking the substrate lipid tail. LTC4S is homologous to other MAPEG family members including [FLAP](/xray-mp-wiki/proteins/enzymes/flap/) (5-lipoxygenase activating protein) and microsomal [GSH](/xray-mp-wiki/reagents/additives/glutathione/) S-transferases (MGST1-3). Structure-function studies with Trp-116 mutants (W116A, W116F) and product analogs (hexyl-[GSH](/xray-mp-wiki/reagents/additives/glutathione/), 4-phenylbutyl-[GSH](/xray-mp-wiki/reagents/additives/glutathione/), 2-hydroxy-4-phenylbutyl-[GSH](/xray-mp-wiki/reagents/additives/glutathione/)) revealed the binding mode of LTA4 and LTC4 at the active site and a mechanism for product release aided by Trp-116 acting as a gate to the lipid bilayer.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature05936 | 2PNO | 3.3 | C2221 |  |  |
| doi/10.1038##NATURE06009 | Not specified in raw paper (apo form, 2.0 A) | 2.0 | F23 |  |  |
| doi/10.1038##NATURE06009 | Not specified in raw paper (GSH-bound, 2.15 A) | 2.15 | F23 |  |  |
| doi/10.1074##jbc.M113.534628 | 4JCZ | 2.75 | Not specified |  |  |
| doi/10.1074##jbc.M113.534628 | Not specified | 2.7 | Not specified |  |  |
| doi/10.1074##jbc.M113.534628 | Not specified | 2.4 | Not specified |  |  |
| doi/10.1074##jbc.M113.534628 | Not specified | 3.2 | Not specified |  |  |
| doi/10.1074##jbc.M113.534628 | Not specified | 2.9 | Not specified |  |  |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: Wild type human LTC4S; W116A and W116F mutants

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | S-hexylglutathione-agarose [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — |  | Two-step affinity purification as previously described |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC on [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 16/60 | — | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.2, 0.03% (w/v) dodecyl maltoside, 300 mM NaCl | Buffer exchange for crystallization. Proteins concentrated to 1-3 mg/ml. |


## Crystallization

### doi/10.1074##jbc.M113.534628

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | LTC4S (3.5 mg/ml) supplemented with 1 mM [GSH](/xray-mp-wiki/reagents/additives/glutathione/) |
| Reservoir | 1.8-2.2 M NH4SO4, 0.2 M NaCl, 0.1 M [Sodium Cacodylate](/xray-mp-wiki/reagents/buffers/sodium-cacodylate/) pH 6.1-6.8 |
| Temperature | Room temperature |
| Growth time | 1 day to maturation in 4 days |
| Cryoprotection | Not specified |
| Notes | Soaks conducted in reservoir solution with 1 mM hexyl-[GSH](/xray-mp-wiki/reagents/additives/glutathione/) (30 s to 24 h). Crystals of WT, W116F, and W116A LTC4S obtained. |


## Biological / Functional Insights

### First crystal structure of LTC4S reveals MAPEG fold with V-shaped LTA4 binding valley

The 3.3 Å structure of human LTC4S (PDB 2PNO) was the first atomic-resolution structure of LTC4S, solved by SeMet SAD phasing. Each monomer consists of four transmembrane helices. Four trimers assemble in the asymmetric unit (space group C2221). A V-shaped valley between adjacent monomers, lined by conserved residues, serves as the putative LTA4 binding site. A bound DDM molecule occupies this valley, mimicking the lipid tail of the LTA4 substrate. The GSH co-substrate is bound at the active site, coordinated by polar residues from neighboring subunits.

### Trimeric organization and metal-mediated crystal packing

LTC4 synthase forms a homotrimer in solution, and three trimers assemble into a dodecamer in the crystal lattice. Crystal packing is largely governed by metal clusters (8 metal ions per dodecamer) coordinated by N-terminal hexahistidine tags, with metal binding sites at the interfaces between trimers.

### Glutathione binding at the active site

The [GSH](/xray-mp-wiki/reagents/additives/glutathione/) ([GSH](/xray-mp-wiki/reagents/additives/glutathione/))-bound structure reveals the ligand coordinated by residues from multiple subunits within the trimer, including Arg104 from an adjacent monomer that interacts with the cysteinyl sulfur of [GSH](/xray-mp-wiki/reagents/additives/glutathione/). This inter-subunit coordination explains the trimer-dependence of catalytic activity and provides a structural basis for substrate recognition in the MAPEG family.

### Trp-116 is not essential for catalysis but positions the omega-end of LTA4

Mutational analysis of Trp-116 (W116A, W116F) revealed no major kinetic alterations, demonstrating Trp-116 is not essential for catalysis. The 3-fold increased LTA4 turnover of W116F may reflect a Phe configuration that leaves the active site open to the lipid bilayer, facilitating product release. The W116A mutant shows the acyl chain of analog I is less ordered, confirming Trp-116 anchors the omega-end of LTA4.

### Tilted GSH conformation in product-bound state

Crystal structures with product analogs I-III reveal a tilited binding configuration of the [GSH](/xray-mp-wiki/reagents/additives/glutathione/) moiety compared to GSH-bound structures. The sulfur atom shifts by approximately 7 A from its position in GSH-bound LTC4S (PDB 2UUH). This tilted conformation is not observed in other GST family members and likely reflects the product state as LTC4 exits the active site.

### Trp-116 as a gate for product release

In the W116F structure, the phenyl ring adopts a tilted rotamer that opens the protein cavity toward the lipid bilayer. This suggests Trp-116 acts as a lid/gate that rotates outward to expose the nascent LTC4 product to the membrane, facilitating product release. A mechanistic model is proposed: (1) [GSH](/xray-mp-wiki/reagents/additives/glutathione/) binds and is activated by Arg-104; (2) LTA4 slides into the hydrophobic crevice with its omega-end under Trp-116; (3) the thiolate attacks C6 of the epoxide; (4) the evolving product tilts toward Trp-116, which rotates outward to allow product release into the lipid bilayer.

### MAPEG family conservation

LTC4S shares structural homology with other MAPEG family members including [FLAP](/xray-mp-wiki/proteins/enzymes/flap/), MGST1, [MGST2](/xray-mp-wiki/proteins/enzymes/mgst2/), and MGST3. The four-helix transmembrane bundle is conserved throughout the family, with sequence variations at the active site determining substrate specificity for [GSH](/xray-mp-wiki/reagents/additives/glutathione/) conjugation versus other MAPEG-catalyzed reactions.


## Cross-References

- [MAPEG Superfamily](/xray-mp-wiki/concepts/protein-families/mapag-superfamily/) — LTC4S is a member of the MAPEG superfamily
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — Product release from LTC4S may involve conformational changes akin to alternating access
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM used in purification buffer and as a crystallization additive; DDM molecule in PDB 2UUH mimics LTA4 binding
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Precipitant used in crystallization
- [Sodium Cacodylate](/xray-mp-wiki/reagents/additives/sodium-cacodylate/) — Buffer used in crystallization reservoir
- [Sitting-drop vapor diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Crystallization method for LTC4S complexes
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final polishing step in purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [FLAP](/xray-mp-wiki/proteins/enzymes/flap/) — Related protein structure
- [MGST2](/xray-mp-wiki/proteins/enzymes/mgst2/) — Related protein structure
