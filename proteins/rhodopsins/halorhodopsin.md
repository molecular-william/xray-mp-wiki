---
title: Halorhodopsin (HR) from Halobacterium salinarum
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.288.5470.1390]
verified: false
---

# Halorhodopsin (HR) from Halobacterium salinarum

## Overview

Halorhodopsin (HR) is a light-driven chloride pump from Halobacterium
salinarum, belonging to the archaeal rhodopsin family of
seven-transmembrane helix proteins. It uses light energy to transport
chloride ions into the cell against their electrochemical gradient,
contributing to osmotic balance under hypersaline conditions. The
structure was determined at 1.8 Å resolution by X-ray
crystallography using a cubic lipidic phase crystallization approach,
revealing the molecular mechanism of chloride binding and transport
through a protonated Schiff base [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.288.5470.1390 |  | 1.8 | — | Mature HR (253 amino acids), Val229Ala mutant | [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), Chloride |

## Expression and Purification

- **Expression system**: Halobacterium salinarum D2
- **Notes**: Homologous overexpression of mature HR; DNA sequencing of the hop gene revealed a single point mutation Val229Ala in the FG loop

### Purification Workflow

- **Expression system**: H. salinarum D2

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Solubilization | — | 4 M KCl, 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.2 + 5% cholate |  |
| Hydrophobic interaction chromatography | Column chromatography | Phenyl-sepharose CL-4B | 0.4% phosphate buffer (wash) | Eluted by changing to 1% beta-octyl-glucoside in the same buffer |
| Concentration | Ultrafiltration | — |  | Concentrated on 50 kDa cutoff Amicon membrane filters |


## Crystallization

### doi/10.1126##science.288.5470.1390

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | 1-monoleoyl-rac-[Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) ([Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)) |
| Protein-to-lipid ratio | 58-62% [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (w/w) |
| Temperature | 22°C |
| Growth time | ~2 weeks |
| Notes | HR concentration 3.3-4.0 mg/ml. Crystals grew in dark. Final size 0.1 x 0.1 x 0.02 mm. Space group P6_322, a=b=67.3 Å, c=209.2 Å. |


## Biological / Functional Insights

### Chloride binding and electrostatic stabilization

The chloride ion CL501 binds 18 Å below the extracellular membrane surface, stabilized by a combination of ion-ion and ion-dipole interactions. Hydrogen bonds are donated by WAT508, WAT512, and Ser115, while aliphatic hydrogen atoms from methylene groups of Ser73, Ser76, Ser115, and the indole of Trp112 contribute hydrophobic contacts. The protonated Schiff base (PSB) of Lys242 is closely associated with CL501 (3.75 Å) but unfavorably oriented for a regular hydrogen bond. Electrostatic calculations show that the PSB contributes -13 kcal/mol to chloride binding, nearly balanced by repulsion from Asp238. Arg108 provides an additional -4.6 kcal/mol through a water-mediated interaction. The overall free energy of transfer from bulk water is -1.3 kcal/mol, corresponding to a dissociation constant of ~0.1 M.

### Mechanistic equivalence of chloride and proton pumping

Comparison of HR with [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (BR) reveals a common mechanism for ion transport in archaeal rhodopsins. The chloride in HR occupies an almost identical position as the OD1 atom of Asp85 in BR (Δx = 0.34 Å). After photoisomerization flips the N-H dipole of the PSB from extracellular to cytoplasmic orientation, chloride is electrostatically dragged along the PSB by ion-dipole interaction, while in BR the fixed negative charge of Asp85 attracts a proton from the PSB. Single-site mutants of BR (Asp85→Thr/Ser) can switch to chloride transport, demonstrating that replacing a negatively charged oxygen with chloride changes ion specificity from cations to anions.

### HR trimer and palmitate binding

HR assembles as trimers around a central patch containing three molecules of palmitic acid (palmitate). Unlike BR which shows a different trimerization mode, HR is tilted by 11° compared with BR, causing the internal compartment encircled by the trimer to open toward the extracellular side like a funnel. Palmitate carboxylates hydrogen bond to Ser75 and Thr111, positioned close to the Schiff base and transport site, and removal of palmitate has been shown to affect the photocycle and spectral characteristics of HR.


## Cross-References

- [Microbial Rhodopsins](/xray-mp-wiki/concepts/microbial-rhodopsins/) — HR is a member of the archaeal rhodopsin subfamily of microbial rhodopsins; comparison with BR reveals mechanistic equivalence of ion transport
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — BR is the proton-pumping archaeal rhodopsin; structural comparison reveals the mechanistic basis for chloride vs proton transport
- [Pharaonis Halorhodopsin (phR)](/xray-mp-wiki/proteins/rhodopsins/pharaonis-halorhodopsin/) — Homologous light-driven chloride pump from Natronobacterium pharaonis; related halorhodopsin with similar function
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Related ligand or cofactor
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Additive used in purification or crystallization buffers
