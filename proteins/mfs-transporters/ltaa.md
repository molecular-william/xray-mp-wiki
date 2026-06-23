---
title: "LtaA — S. aureus Lipid-Linked Disaccharide Flippase"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-020-0425-5]
verified: false
---

# LtaA — S. aureus Lipid-Linked Disaccharide Flippase

## Overview

LtaA is a proton-coupled antiporter flippase from Staphylococcus aureus
that translocates the lipid-linked disaccharide gentiobiosyl-diacylglycerol
(anchor-LLD) across the plasma membrane, a rate-limiting step in
lipoteichoic acid (LTA) biogenesis. LtaA belongs to the Major Facilitator
Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)) of transporters and is essential for S. aureus survival
under acidic physiological conditions encountered in the human nasopharynx,
mucous membranes, and skin. Its structure reveals an amphiphilic central
cavity with an N-terminal hydrophilic pocket that binds the gentiobiosyl
headgroup and a C-terminal hydrophobic pocket that accommodates the
diacylglycerol lipid tails.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41594-020-0425-5 | 6S7V | 3.3 | C2221 | Full-length S. aureus LtaA with N-terminal His10 tag (removed post-purification) | None (apo structure) |

## Expression and Purification

- **Expression system**: E. coli BL21-Gold (DE3)
- **Construct**: Full-length S. aureus LtaA with N-terminal His10 affinity tag and TEV protease cleavage site
- **Notes**: SeMet derivative produced in M9 medium with amino acids/SeMet cocktail
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/)
- **Media**: Terrific Broth supplemented with 1% [Glucose](/xray-mp-wiki/reagents/additives/glucose/)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane isolation | Ultracentrifugation | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl, 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 0.5 mM PMSF | Cells resuspended and disrupted; membranes collected by ultracentrifugation |
| Solubilization | Detergent extraction | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 200 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) + 1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Incubated for 2 h at 4°C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA affinity | Ni-NTA Superflow | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 200 mM NaCl, 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 0.02% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Wash followed by elution with 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag removal | TEV protease cleavage | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 200 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Overnight treatment; TEV removed by secondary Ni-NTA pass |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) Increase 10/300 GL | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.02% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) | Main peak collected; buffer exchanged to 0.1% Cymal-7 using PD-10 desalting column |


## Crystallization

### doi/10.1038##s41594-020-0425-5

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | LtaA at 6.0 mg/mL in 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.1% Cymal-7 |
| Reservoir | 30-70 mM magnesium acetate, 80-120 mM [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) pH 9.5, 30-34% [PEG](/xray-mp-wiki/reagents/additives/peg/) 300 |
| Temperature | 16 |
| Growth time | 3-4 days to appearance, 1 week to full size |
| Notes | Plate-shaped crystals; dehydrated and cryoprotected by increasing [PEG](/xray-mp-wiki/reagents/additives/peg/) 300 concentration; in situ annealing performed |


## Biological / Functional Insights

### Proton-Coupled Lipid Flipping Mechanism

LtaA is identified as a new class of flippase that energizes lipid translocation
by coupling to a transmembrane proton gradient. The mechanism follows an
antiporter alternating-access cycle: deprotonated LtaA in an inward-facing
conformation binds anchor-LLD, transitions to an outward-facing state,
releases the substrate into the membrane, and becomes protonated at residue
E32 to facilitate the return to the inward-facing state. This represents the
first description of a proton-coupled lipid flippase.

### pH Sensing Role in S. aureus Survival

LtaA acts as a pH-sensing flippase that increases anchor-LLD transport under
low pH conditions, enlarging the LTA population at the outer leaflet. Increased
LTA provides a buffering mechanism against acidification via the highly
negatively charged LTA backbone polymer. Deletion of ltaA causes strong growth
retardation at low pH (5.0-6.5) and at 5% CO2, conditions encountered in
human nasopharynx and skin. This establishes LtaA as essential for S. aureus
survival under physiologically relevant acidic conditions.

### Substrate Selectivity and Inhibitor Design

LtaA displays high selectivity for the gentiobiosyl headgroup of anchor-LLD.
Flipping activity is inhibited by gentiobiose (beta-D-Glc-(1,6)-D-Glc) in a
concentration-dependent manner, but not by other disaccharides (lactose,
[Trehalose](/xray-mp-wiki/reagents/additives/trehalose/), [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/)). This provides the structural basis for designing
inhibitors targeting LTA assembly.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — LtaA is an MFS family transporter
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — LtaA follows the antiporter alternating-access cycle
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) — Additive used in purification or crystallization buffers
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
