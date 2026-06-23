---
title: LarB (Lactiplantibacillus plantarum)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1021##acs.biochem.3c00242, doi/10.1021##acs.biochem.5b01345]
verified: false
---

# LarB (Lactiplantibacillus plantarum)

## Overview

LarB is an enzyme from Lactiplantibacillus plantarum (formerly Lactobacillus plantarum) that catalyzes the first step in the biosynthesis of the nickel-pincer nucleotide (NPN) cofactor. LarB carboxylates [Nicotinic Acid Adenine Dinucleotide (NaAD)](/xray-mp-wiki/reagents/cofactors/nicotinic-acid-adenine-dinucleotide/) at the C5 position of the pyridinium ring and hydrolyzes the phosphoanhydride bond, producing pyridinium-3,5-biscarboxylic acid mononucleotide ([P2CMN](/xray-mp-wiki/reagents/ligands/pyridinium-3-5-biscarboxylic-acid-mononucleotide/)) and AMP. The enzyme uses CO2 for substrate carboxylation and employs a Cys221 nucleophile for covalent intermediate formation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##acs.biochem.3c00242 | S127A-LarB-NaAD | 2.5 | P212121 | S127A variant with Strep II tag | NaAD |
| doi/10.1021##acs.biochem.5b01345 | 7MJ2 | 2.1 | P212121 | Wild-type with Strep II tag | NAD+ |

## Expression and Purification

- **Expression system**: E. coli BL21 (DE3)
- **Construct**: Strep II-tagged LarB

### Purification Workflow

- **Expression system**: E. coli BL21 (DE3)
- **Expression construct**: Strep II-tagged LarB

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | — | LB medium with [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) |  |
| Cell lysis | Sonication | — |  |  |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Strep-Tactin affinity | Strep-Tactin | 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl |  |
| Size-exclusion chromatography | Size-exclusion chromatography | — | 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl |  |

**Final sample**: 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl


## Crystallization

### doi/10.1021##acs.biochem.3c00242

| Parameter | Value |
|---|---|
| Method | [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | ~12 mg/mL S127A LarB |
| Reservoir | 2 mM nitrilotriacetic acid, 0.7 mM ZnSO4, 100 mM magnesium formate, 10-20% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350 |
| Temperature | 4 |
| Cryoprotection | 25% [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/), 10 mM NaAD, 10-20% [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350, 25 mM magnesium formate |
| Notes | Crystals soaked overnight in 5-10 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) (pH 8), 10 mM NaAD, 10-20% [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350, 25 mM magnesium formate before cryoprotection. Zn2+ required for crystallization but must be removed for active site substrate binding. |

### doi/10.1021##acs.biochem.5b01345

| Parameter | Value |
|---|---|
| Method | [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Notes | NAD+ soaked into LarB crystals to form LarB-NAD+ complex. Cys221 covalently attaches to C4 of the pyridine ring. |


## Biological / Functional Insights

### Revised Catalytic Mechanism

The S127A LarB-NaAD structure revealed a revised catalytic mechanism. The carboxylate of
NaAD is oriented in the same manner as the amide of NAD+, pointing away from the metal ion.
The conserved Glu180 residue is improperly positioned to serve as a general base to abstract
the C5 proton (average distance 4.9 A). Instead, Glu180 is within hydrogen bond distance
of the thiol group of Cys221 (3.1-3.4 A), suggesting that Cys221 and Glu180 form a catalytic
dyad that facilitates nucleophilic attack of the thiolate anion on C4 of NaAD. No Cys221-pyridine
ring linkage was observed in the S127A LarB-NaAD structure, unlike the WT LarB-NAD+ structure.

### DaAD Intermediate Trapping

The S127A variant exhibits ~90% reduction in nonproductive NaAD hydrolysis activity compared
to WT LarB, allowing accumulation and identification of the DaAD intermediate by mass
spectrometry. The S127A variant was capable of carboxylating ~75% of the NaAD substrate,
whereas only ~20% was carboxylated by the WT enzyme.

### CO2 Binding Site

A tentative CO2 binding mode was identified in the S127A LarB-NaAD structure. CO2 forms
electrostatic interactions with Mg2+, Arg159, and the hydroxyl and phosphate groups of NaAD.
Arg159, which is essential for LarB activity, uses its flexible long arm to recruit and
hand over CO2 to the bound Mg2+. The Mg2+ bound to NaAD, together with Ala155, Gly156,
and Arg159, forms the entrance of a narrow pathway for CO2 access to C5 of NaAD.


## Cross-References

- [NaAD](/xray-mp-wiki/reagents/cofactors/nicotinic-acid-adenine-dinucleotide/) — Authentic substrate of LarB
- [DaAD](/xray-mp-wiki/reagents/ligands/dinicotinic-acid-adenine-dinucleotide/) — Reaction intermediate identified by MS
- [P2CMN](/xray-mp-wiki/reagents/ligands/pyridinium-3-5-biscarboxylic-acid-mononucleotide/) — Product of LarB-catalyzed reaction
- [NAD+](/xray-mp-wiki/reagents/ligands/nicotinamide-adenine-dinucleotide/) — Substrate analogue that covalently binds to Cys221
- [NPN Cofactor Biosynthesis](/xray-mp-wiki/concepts/enzyme-mechanisms/nickel-pincer-nucleotide-cofactor-biosynthesis/) — Pathway initiated by LarB-catalyzed reaction
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Method used in structure determination or purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) — Additive used in purification or crystallization buffers
- [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) — Additive used in purification or crystallization buffers
