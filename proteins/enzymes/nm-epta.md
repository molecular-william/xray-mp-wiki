---
title: "NmEptA - Lipid A Phosphoethanolamine Transferase from Neisseria meningitidis"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1073##pnas.1612927114]
verified: false
---

# NmEptA - Lipid A Phosphoethanolamine Transferase from Neisseria meningitidis

## Overview

NmEptA is a [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) phosphoethanolamine (PEA) transferase from *Neisseria meningitidis* that catalyzes the transfer of phosphoethanolamine from [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) to the 1 and 4' headgroup positions of [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/). This modification masks the negatively charged phosphate groups on the bacterial surface, conferring resistance to cationic antimicrobial peptides (CAMPs) such as colistin. The full-length X-ray crystal structure at 2.75 Å resolution reveals a helical transmembrane domain and a periplasmic-facing soluble hydrolase-fold domain connected by a bridging helix. A Zn2+ ion is tetrahedrally coordinated at the active site, with Thr280 serving as the catalytic nucleophile. The structure provides insights into conformational dynamics that enable binding of two differently-sized lipid substrates and informs structure-guided drug design for treating multidrug-resistant bacterial infections.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1612927114 | 5FGN | 2.75 | — | Full-length NmEptA (hexahistidine-tagged) | Zn2+, [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Full-length NmEptA with N-terminal hexahistidine tag

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Full-length NmEptA with hexahistidine tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent extraction | — | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Enzyme expressed recombinantly and purified in presence of [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni2+-NTA | Ni-NTA | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | Not specified | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |

**Final sample**: Purified NmEptA in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) micelles
**Purity**: Monodisperse and thermally stable


## Crystallization

### doi/10.1073##pnas.1612927114

| Parameter | Value |
|---|---|
| Method | Not specified in main text |
| Protein sample | Purified full-length NmEptA in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Notes | Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using soluble domain structure (PDB 4KAV). Data collected at Diamond Light Source and Australian Synchrotron. |


## Biological / Functional Insights

### Full-length structure reveals membrane domain architecture

The 2.75 Å crystal structure of full-length NmEptA reveals a previously uncharacterized helical membrane domain comprising five transmembrane helices (TMH1-5), two periplasmic-facing helices (PH1-PH2 and PH2'), and a bridging helix that connects to the soluble domain. The soluble domain adopts a hydrolase-type fold with a bound Zn2+ ion at the active site. A large interdomain interface (~1,200 Å2) with high sequence conservation suggests functional coupling between domains.

### Substrate binding by PH2 and PH2' helices

Two amphipathic helices located in a periplasmic loop between TMH3 and TMH4 (PH2 and PH2') contain conserved charged residues implicated in lipid substrate binding. A bound [DDM](/xray-mp-wiki/reagents/detergents/ddm/) molecule was observed in the active site between these helices, with the carbohydrate moiety forming hydrogen bonds with three invariant residues. The O3B hydroxyl of [DDM](/xray-mp-wiki/reagents/detergents/ddm/) is positioned 3.72 Å from the bound Zn2+ and 2.96 Å from the catalytic Thr280.

### Conformational dynamics enable dual substrate recognition

[Limited Proteolysis](/xray-mp-wiki/methods/purification/limited-proteolysis/), intrinsic tryptophan fluorescence, and molecular dynamics simulations suggest NmEptA samples different conformational states. In [DDM](/xray-mp-wiki/reagents/detergents/ddm/) and [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/), the enzyme adopts a conformation conducive to PEA hydrolysis, while in Fos-choline-12 it adopts a non-productive state. MD simulations show the soluble domain can dissociate from the membrane domain and "roll" over the membrane surface, suggesting a range of conformations for binding two differently-sized lipid substrates (PE and [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/)).

### Comparison with ArnT

[ARNT](/xray-mp-wiki/proteins/enzymes/arnt/) is a related lipid-to-lipid glycosyltransferase that modifies the same sites on [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) with 4-amino-4-deoxy-L-arabinose. While both enzymes are located in the periplasmic membrane with TM and soluble domains, [ARNT](/xray-mp-wiki/proteins/enzymes/arnt/) has 13 TM helices and a smaller soluble domain. NmEptA employs a ping-pong mechanism via a Thr280-PEA intermediate, whereas [ARNT](/xray-mp-wiki/proteins/enzymes/arnt/) requires both substrates to bind simultaneously for direct transfer.


## Cross-References

- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization, purification, and crystallization of NmEptA
- [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) — Alternative maltoside detergent used in conformational studies
- [Foscholine-12](/xray-mp-wiki/reagents/detergents/foscholine-12/) — Zwitterionic detergent used in conformational studies showing non-productive state
- [His6-tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — Affinity tag used for purification
- [Nickel-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) — Affinity resin for purification of hexahistidine-tagged NmEptA
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Limited Proteolysis](/xray-mp-wiki/methods/purification/limited-proteolysis/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [ARNT](/xray-mp-wiki/proteins/enzymes/arnt/) — Related protein structure
