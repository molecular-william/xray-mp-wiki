---
title: Metabotropic Glutamate Receptor 5 (mGlu5)
created: 2026-05-29
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1021##acs.jmedchem.7b01722, doi/10.1038##nature13396]
verified: false
---

# Metabotropic Glutamate Receptor 5 (mGlu5)

## Overview

Metabotropic glutamate receptor 5 (mGlu5) is a Class C G protein-coupled receptor that plays a key role in regulating NMDA receptor activity in the central nervous system. mGlu5 couples via the Gq/11 family of G proteins and is implicated in numerous neurological disorders including fragile X syndrome, Parkinson's disease, anxiety, and chronic pain. The transmembrane domain (TMD) of mGlu5 contains a well-characterized allosteric binding site (the [MPEP](/xray-mp-wiki/reagents/ligands/mpep/) site) where negative allosteric modulators (NAMs) bind in a deep pocket within the transmembrane helix bundle. Multiple high-resolution crystal structures have been determined using a thermostabilized StaR construct fused with [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) in intracellular loop 2. The first TMD structure (PDB 4OO9) established the architecture of class C GPCR transmembrane domains and revealed the conserved ionic lock network.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13396 | 4OO9 | 2.6 A | C 1 2 1 | mGlu5-StaR TMD (residues 569-836) with N-terminal GP64 signal sequence, C-terminal decahistidine tag, [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) inserted into ICL2 between Lys678 and Lys679, ECD and C-terminus [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/), six thermostabilizing mutations (E579A, N667Y, I669A, G675M, T742A, S753A). Complexed with [AFQ056](/xray-mp-wiki/reagents/ligands/mavoglurant/).
 | [AFQ056](/xray-mp-wiki/reagents/ligands/mavoglurant/) |
| doi/10.1021##acs.jmedchem.7b01722 | 6FFI | 2.2 A | C 1 2 1 | mGlu5-StaR TMD (residues 569-832) with N-terminal GP64 signal sequence, C-terminal decahistidine tag, [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) inserted into ICL2 between Lys678 and Lys679, ECD and C-terminus [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/), six thermostabilizing mutations. Complexed with [M-MPEP](/xray-mp-wiki/reagents/ligands/m-mpep/).
 | [M-MPEP](/xray-mp-wiki/reagents/ligands/m-mpep/) |
| doi/10.1021##acs.jmedchem.7b01722 | 6FFH | 2.65 A | C 1 2 1 | mGlu5-StaR TMD (residues 569-832) with N-terminal GP64 signal sequence, C-terminal decahistidine tag, [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) inserted into ICL2 between Lys678 and Lys679, ECD and C-terminus [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/), six thermostabilizing mutations. Complexed with [Fenobam](/xray-mp-wiki/reagents/ligands/fenobam/).
 |  |

## Expression and Purification

- **Expression system**: Sf21 insect cells (baculovirus expression vector system)
- **Construct**: mGlu5-StaR TMD construct with N-terminal GP64 signal sequence, residues 569-836 of mGlu5 receptor (TMD only), C-terminal decahistidine tag. The StaR variant contains six thermostabilizing mutations (E579A, N667Y, I669A, G675M, T742A, S753A) located away from the allosteric ligand binding site. The N-terminal extracellular domain (residues 2-568) and unstructured C-terminus (residues 837-1153) were excised. [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) was inserted into intracellular loop 2 between Lys678 and Lys679.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and infection | Sf21 cells infected with baculovirus at multiplicity of infection ~1, harvested 48 hours post-infection | -- | -- + -- | Cells grown at 27 degrees Celsius in ESF921 medium supplemented with 10% FBS and 1% penicillin/streptomycin |
| Cell disruption and membrane preparation | Cells resuspended in PBS with protease inhibitors and [EDTA](/xray-mp-wiki/reagents/additives/edta/), disrupted by microfluidizer at 14 kPSI, membranes isolated by ultracentrifugation at 204700g for 1 hour | -- | PBS, protease inhibitor cocktail, 5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/); wash buffer: PBS, 500 mM NaCl, protease inhibitor cocktail + -- | Washed membranes resuspended in 40 mM HEPES pH 7.5, 250 mM NaCl and stored at -80 degrees Celsius |
| Solubilization | Membranes supplemented with 40 uM [AFQ056](/xray-mp-wiki/reagents/ligands/mavoglurant/) and 8 mM [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/), incubated on roller, then solubilized with [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for 1 hour at 4 degrees Celsius | -- | 40 mM HEPES pH 7.5, 250 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Insoluble material removed by ultracentrifugation |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Batch binding to Ni-NTA beads, wash with [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), elution with histidine | Ni-NTA beads | 40 mM HEPES pH 7.5, 250 mM NaCl, 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (binding); 40 mM HEPES pH 7.5, 250 mM NaCl, 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 100 mM histidine (elution) + 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | [AFQ056](/xray-mp-wiki/reagents/ligands/mavoglurant/) included in all buffers to maintain receptor-ligand complex |


## Crystallization

### doi/10.1038##nature13396

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | mGlu5-StaR-[AFQ056](/xray-mp-wiki/reagents/ligands/mavoglurant/) complex mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) supplemented with 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) using twin-syringe method
 |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) with 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) |
| Protein-to-lipid ratio | 40:60 (w/w) |
| Temperature | 20.0 degrees Celsius |
| Growth time | Not specified |
| Cryoprotection | Crystals harvested and flash-frozen in liquid nitrogen |
| Notes | Diffraction data from 5 crystals grown in LCP, collected at Diamond Light Source beamline I24. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) and an ensemble of 8 GPCR TMD structures as search models. Rwork/Rfree = 23.9/27.4%.
 |


## Biological / Functional Insights

### Ionic lock network in class C GPCRs

The mGlu5 structure reveals a conserved ionic lock network in the
transmembrane domain that regulates receptor signaling. Lys665^3.50 in
TM3 forms a salt bridge with Glu770^6.35 in TM6 (2.7 A distance),
analogous to the Arg135^3.50-Glu247^6.30 salt bridge in rhodopsin.
Additionally, Arg668^3.53 is within hydrogen bonding distance of
Ser614 in ICL1 (3.1 A), forming a secondary lock that tethers TM6
to TM3 via ICL1. Disruption of this network through mutation of
Ser613, Glu770^6.35, or Lys665^3.50 to alanine significantly increases
constitutive activity, providing functional evidence for the role of
this network in maintaining the inactive state. The network is highly
conserved across class C GPCRs including mGlu, GABA_A, CaS, and TAS1
receptors.

### Allosteric binding site architecture

The [AFQ056](/xray-mp-wiki/reagents/ligands/mavoglurant/) binding pocket is located approximately 8 A from the
receptor surface, spanning ligand positions observed for class A and B
GPCRs. The ligand is oriented with an approximate 30 degree tilt
relative to the TM bundle axis. The 3-methylphenyl ring sits in a
pocket between Ala810^7.40 and Pro655^3.40, bordered by Ile625^2.46,
Gly628^2.49, Ser654^3.39, Ser658^3.43, and Tyr659^3.44. The alkyne
linker traverses a narrow channel between Tyr659^3.44, Ser809^7.39,
Val806^7.36, and Pro655^3.40. The saturated bicyclic ring system sits
within a mainly hydrophobic pocket defined by Val806^7.36, Met802^7.32,
Phe788^6.53, Trp785^6.50, Leu744^5.44, Ile651^3.36, Pro655^3.40, and
Asn747^5.47.

### Class C GPCR transmembrane architecture

Comparison with rhodopsin (PDB 1F88, class A) and [CRF1R](/xray-mp-wiki/proteins/gpcr/crf1r-star-t4l/) (PDB 4K5Y,
class B) reveals distinct features of class C GPCR TMD architecture.
TM5 in mGlu5 is positioned approximately 6 A further inward compared
to both rhodopsin and [CRF1R](/xray-mp-wiki/proteins/gpcr/crf1r-star-t4l/), contributing to a narrow entrance to the
allosteric cavity. TM2 in mGlu5 is straighter than class A receptors
but shifted ~2.5 A closer to the central axis due to packing of
highly conserved Tyr629^2.50 against Gly590^1.50. These structural
features provide a model for all class C G-protein-coupled receptors.


## Cross-References

- [Mavoglurant (AFQ056)](/xray-mp-wiki/reagents/ligands/mavoglurant/) — First NAM co-crystal structure with mGlu5 TMD (PDB 4OO9)
- [M-MPEP](/xray-mp-wiki/reagents/ligands/m-mpep/) — High-affinity NAM; structure 6FFI
- [Fenobam](/xray-mp-wiki/reagents/ligands/fenobam/) — Urea-linked NAM; structure 6FFH
- [HTL14242](/xray-mp-wiki/reagents/ligands/htl14242/) — Pyrimidine-linked NAM; structure 5GCD
- [MPEP](/xray-mp-wiki/reagents/ligands/mpep/) — Reference NAM; defines MPEP allosteric site
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — Fusion partner inserted into ICL2 for crystallization
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method for all mGlu5 structures
- [GPCR Inactive Conformation](/xray-mp-wiki/concepts/gpcr-inactive-conformation/) — Ionic lock network maintains inactive state of mGlu5
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
