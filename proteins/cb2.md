---
title: Cannabinoid Receptor 2 (CNR2/CB2)
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.01.008]
verified: false
---

# Cannabinoid Receptor 2 (CNR2/CB2)

## Overview

Cannabinoid receptor 2 (CNR2, commonly known as CB2) is a class A G protein-coupled receptor that is the principal peripheral target of cannabinoids. Unlike CB1, CB2 is primarily expressed in the immune system and periphery, with minimal expression in the central nervous system. CB2 modulates immune responses, inflammation, and pain sensation without psychoactive effects. CB2 shares 44% total sequence identity and 68% sequence similarity in the transmembrane regions with CB1. CB2 is activated by endogenous cannabinoids and synthetic agonists, coupling primarily to Gi proteins. CB2 has therapeutic potential for inflammatory and neuropathic pain management without CB1 psychoactivity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2020.01.008 | 6KPC | 3.2 |  | Wild-type human CB2 (14656 construct); N-terminal BRIL fusion for stability; agonist AM12033 bound | AM12033 |
| doi/10.1016##j.cell.2020.01.008 | 6KPF | 2.9 |  | CB2-N-BRIL fusion; co-expressed with heterotrimeric Gi protein and scFv16 antibody fragment; agonist AM12033 bound; active state | AM12033 |

## Expression and Purification

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus expression system)
- **Construct**: N-BRIL fused wild-type human CB2; N-terminal HA signal sequence followed by 10x His-tag and Flag-tag; human Gαi1 and Gβ1γ2 subunits cloned into pFastBac1 and pFastDual vector individually
- **Notes**: CB2 and Gi heterotrimer co-expressed in Sf9 insect cells at 27C for 48 h. Sf9 cells infected at 2-2.5 x 10^6 cells/mL with three separate virus preparations for CB2, Gαi1, and Gβ1γ2 at ratio of 1:2:2.

### Purification Workflow

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus expression system)
- **Expression construct**: CB2-N-BRIL fusion with HA signal, 10x His-tag, Flag-tag
- **Tag info**: HA signal, 10x His (N-terminal), Flag-tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell infection | Baculovirus infection |  |  | Sf9 cells infected at 2-2.5 x 10^6 cells/mL with CB2, Gαi1, Gβ1γ2 viruses at 1:2:2 ratio, 27C for 48 h |
| Cell lysis | Cell lysis |  |  | Infected cells cultured at 27C for 48 h, harvested by centrifugation, pellets stored at -80C |
| Membrane isolation | Centrifugation |  |  | Cell pellets harvested by centrifugation |
| Solubilization | Detergent solubilization |  | 0.01% LMNG + 0.001% CHS | CB2-Gi-scFv16 complex solubilized with LMNG and CHS |
| Affinity chromatography | Metal affinity chromatography | TALON IMAC | 25 mM HEPES pH 7.5, 100 mM NaCl, 10% glycerol, 0.1% LMNG, 0.02% CHS, 30 mM imidazole, 20 uM AM841 + 0.1% LMNG + 0.02% CHS | His-tag capture on TALON IMAC resin overnight at 4C |
| Tag cleavage | Protease cleavage |  |  | C-terminal 10x His tag cleaved by human rhinovirus 3C protease |
| SEC | Size exclusion chromatography | Hiload Superdex 75 10/300 | 20 mM HEPES pH 7.5, 100 mM NaCl | Monomeric fractions pooled, concentrated, flash frozen |

**Final sample**: not specified
**Purity**: Monomeric fractions by SEC


## Crystallization

### doi/10.1016##j.cell.2020.01.008

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | AM12033-bound CB2 |
| Lipid | monoolein |
| Protein-to-lipid ratio | not specified |
| Temperature | not specified |
| Growth time | 2 weeks; dehydrated to 40 mm x 20 mm after 2 weeks |
| Notes | Crystals grown by LCP; harvested with micro-mounts (MiTeGen) and flash frozen in liquid nitrogen; data collected at Spring-8 beamline 41XU with Pilatus3 6M detector at 1.0000 A wavelength |


## Biological / Functional Insights

### CB2-Gi complex structure and interaction interface

The CB2-Gi complex reveals extensive contacts mediated through the Gαi subunit.
The primary interaction interface comprises TM3, TM5, TM6, and ICL2 of CB2 and the
α5 helix, αN helix, and αN-β1 loop of Gαi. Two large hydrophobic side chains
L353 and L348 of the Gαi α5 helix are directed toward a hydrophobic pocket formed
by Val212^5.61, Leu243^6.33, Leu247^6.37, Leu239^6.29, and Leu135^3.54 from the
cytosolic ends of TM5, TM6, and TM3 of CB2. The Gi proteins in CB2-Gi complex show
a ~20 degree anticlockwise rotation when aligned with other GPCR-Gi complexes.
No electron density for GDP is observed, suggesting Gi is nucleotide-free.

### AM12033 binding in CB2

AM12033 adopts an L-shape conformation in the orthosteric binding pocket.
Interactions are mainly hydrophobic and aromatic, involving residues from ECL2,
TM3, TM5, TM6, and TM7. The tricyclic tetrahydrocannabinol system forms pi-pi
interactions with Phe183^ECL2, Phe281^7.35, and Phe94^2.64. The phenolic hydroxyl
at C1 forms a hydrogen bond with Ser285^7.39. The alkyl chain extends into a long
channel forming hydrophobic interactions with TM3, TM5, and TM6 residues. The
agonist-bound CB2 crystal structure shares almost identical binding pose with the
cryo-EM structure.

### CB2 activation mechanism

CB2 activation involves the "toggle switch" residue Trp258^6.48 undergoing major
conformational change, accompanied by a large outward movement of the intracellular
part of TM6 by 11 angstroms (Arg238 as reference) to accommodate the α5 helix from
Gαi. The cytoplasmic portion of TM5 extended and moved outward by about 6 angstroms
(V220 as reference) to form extensive interactions with the α5 helix of Gαi. Unlike
CB1 which uses a "twin toggle switch" (Phe3.36 and Trp6.48), CB2 requires only the
single "toggle switch" Trp6.48 to trigger activation and downstream signaling.

### CB2 activation vs CB1 activation differences

CB2 and CB1 exhibit distinct activation processes. CB1 shows a more complicated
activation involving synergistic conformational change of the "twin toggle switch"
(Phe3.36 and Trp6.48) to unleash large conformational changes. CB2 experiences
only minor conformational changes upon agonist binding, behaving like most class A
GPCRs. The extracellular region of CB2, including the N terminus, undergoes very
minor changes during activation. CB1 displays larger conformational changes when
modulated by agonists, suggesting a "balloon-like plasticity" that facilitates
CB1's ability to respond to diverse ligands.

### Thr3.46 role in Gi coupling

An atypical polar amino acid Thr3.46 exists in both CB2 and CB1, compared to
conserved non-polar residues (I/L/M/V) in 95% of class A GPCRs. T3.46A mutation
disables CB2 and CB1 in coupling to Gi. Upon activation, Tyr7.53 establishes new
contacts with Thr3.46, Leu3.43, and Arg3.50. Asp6.30 in TM6 interrupts its
salt-bridge interaction with Arg3.50, strengthening TM3-TM7 interaction, weakening
TM6 constraint from TM3, and unlocking outward movement of TM6.

### CB2-Gi complex rotation compared to other GPCRs

The Gi proteins in CB2- and CB1-Gi complexes show a ~20 degree anticlockwise
rotation when viewed from intracellular to extracellular direction, compared to
mu-opioid receptor, A1 adenosine, 5HT1B, and M2 Gi complexes. This distinct
orientation may contribute to G protein selectivity differences between cannabinoid
receptors and other Gi-coupled GPCRs.

### CB1 cholesterol binding as endogenous allosteric modulation

Cholesterol binds to CB1 at a specific site involving Phe155^2.42 and Phe237^4.46.
In the CB1-Gi complex structure, these side chains undergo large conformational
changes and occupy the same position that cholesterol had in agonist-bound crystal
structures. Phe4.46 is unique to CB1 in class A GPCRs. Cholesterol is not observed
in CB2 structures, suggesting CB1-specific allosteric modulation. Pregnenolone, a
cholesterol derivative, may also bind to the same region and act as a CB1 allosteric
modulator.

### CB1 and CB2 G protein coupling diversity

CB2 couples specifically to Gi only, while CB1 can couple to Gi, Gs, and Gq. The
single residue difference in ICL2 (L222 in CB1 and P139 in CB2) may contribute to
this G protein-coupling diversity. L222 in CB1 facilitates its coupling with Gs and
likely Gq as well. The high structural similarity in orthosteric binding pockets
between agonist-bound CB2 and CB1 imposes challenges for highly selective agonist
design.


## Cross-References

- [Cannabinoid Receptor 1 (CNR1/CB1)](/xray-mp-wiki/proteins/cnr1/) — CB1 shares 44% sequence identity and 68% TM similarity; compared in activation and signaling
- [AM12033](/xray-mp-wiki/reagents/ligands/am12033/) — Synthetic cannabinoid agonist bound in both cryo-EM (6KPF) and crystal (6KPC) structures
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for CB2-Gi complex solubilization and purification
- [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Cholesterol derivative used as stabilizer in CB2-Gi complex purification
- [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) — N-terminal fusion partner used to improve CB2 expression and stability
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — CB2-AM12033 crystal structure (6KPC) determined by LCP method
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — CB2-Gi-scFv16 complex (6KPF) solved by cryo-EM at 2.9 A resolution
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used in LCP crystallization matrix for CB2-AM12033
