---
title: Cannabinoid Receptor 1 (CNR1/CB1)
created: 2026-05-27
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2015.06.002, doi/10.1016##j.cell.2020.01.008, doi/10.1038##nature20613]
verified: false
---

# Cannabinoid Receptor 1 (CNR1/CB1)

## Overview

Cannabinoid receptor 1 (CNR1, commonly known as CB1) is a class A G protein-coupled receptor that is the principal target of Delta-9-tetrahydrocannabinol (THC), the psychoactive compound from Cannabis sativa. CB1 is activated by endogenous cannabinoids (endocannabinoids) including anandamide (AEA) and 2-arachidonoylglycerol (2-AG). CB1 is widely distributed in the central nervous system and periphery, and mediates functions including pain modulation, appetite regulation, memory, and motor control. CB1 shares 42% sequence identity with CB2. CB1 can couple to Gi, Gs, and Gq proteins. CB1 has therapeutic potential for pain management, inflammation, obesity, and substance abuse disorders. CB1 is the most abundant GPCR in the central nervous system.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2015.06.002 | 5ZTY | 3.0 |  | CB1 with N-terminal deletion and C-terminal truncation; antagonist AM10257 bound; inactive state | AM10257 |
| doi/10.1016##j.cell.2020.01.008 | 6KPG | 3.0 |  | CB1-Gi-scFv16 complex; agonist AM841 bound; active state; complex constituted in vitro from purified protein components | AM841 |
| doi/10.1038##nature20613 | 5KPR | 2.6 | P21 | CB1(T210A)-PGS fusion construct; N-terminal 89 residues truncated; C-terminal 51 residues truncated; ICL3 replaced with PGS; T210A thermostabilizing mutation; taranabant bound; inactive state | Taranabant |

## Expression and Purification

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus expression system)
- **Construct**: CB1 expressed in central nervous system and peripheral tissues; structural studies use recombinant expression in insect cells
- **Notes**: CB1-Gi-scFv16 complex constituted in vitro from purified CB1, Gi heterotrimer, and scFv16 antibody fragment; CB1(T210A)-PGS construct expressed via Bac-to-Bac system in Sf9 cells

### Purification Workflow

*Source: doi/10.1016##j.cell.2020.01.008*

- **Expression system**: Sf9 insect cells
- **Expression construct**: CB1 purified from recombinant expression
- **Tag info**: Not specified

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Complex formation | In vitro reconstitution |  |  | CB1-Gi-scFv16 complex constituted in vitro from purified CB1, Gi heterotrimer, and scFv16 |
| SEC | Size exclusion chromatography | Superdex 200 10/300 GL | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.00075% LMNG, 0.00025% GDN, 0.0001% CHS, 100 uM TCEP, 5 uM AM841 + 0.00075% LMNG + 0.00025% GDN + 0.0001% CHS | Monomeric CB1-Gi-scFv16 complex isolated; concentrated to 1 mg/mL for cryo-EM |

**Final sample**: 1 mg/mL
**Purity**: Peak fractions concentrated for cryo-EM studies

### Purification Workflow

*Source: doi/10.1038##nature20613*

- **Expression system**: Sf9 insect cells
- **Expression construct**: CB1(T210A)-PGS fusion; N-terminal HA signal + Flag tag; C-terminal 10x His-tag; N-terminal 89 residues truncated; C-terminal 51 residues truncated; ICL3 (residues 302-332) replaced with PGS; T210A mutation
- **Tag info**: HA signal, Flag epitope (N-term), 10x His-tag (C-term), TEV site

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization |  | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 160 ug/mL benzamidine, 100 ug/mL leupeptin, 2 mg/mL iodoacetamide + 1% DDM, 0.2% sodium cholate, 0.2% CHS, 10 uM taranabant | Sf9 cell membranes solubilized 1 hr at 4C; ultracentrifugation 30 min at 100,000g |
| Ni-NTA affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA agarose (GE Healthcare) | 50 mM HEPES pH 7.5, 500 mM NaCl, 0.05% DDM, 0.01% sodium cholate, 0.01% CHS, 10% glycerol, 50 mM imidazole, 160 ug/mL benzamidine, 100 ug/mL leupeptin, 1 uM taranabant + 0.05% DDM + 0.01% sodium cholate + 0.01% CHS | Batch incubation 3 hr at 4C; washed with 15 column volumes; eluted with 200 mM imidazole and 2 mM calcium |
| Anti-Flag affinity chromatography | Anti-Flag M1 affinity chromatography | Anti-Flag M1 affinity resin | 0.05% LMNG (detergent exchanged from DDM on M1 resin) + 0.05% LMNG | Detergent exchanged from 0.05% DDM to 0.05% LMNG on resin |
| Tag cleavage | Enzymatic cleavage |  | 0.05% LMNG | TEV protease (1:10 w/w) and PNGase F added to remove Flag tag and deglycosylate; receptor eluted with 0.2 mg/mL Flag peptide and 5 mM EDTA |
| SEC | Size exclusion chromatography | Superdex 200 | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% LMNG, 0.005% CHS, 1 uM taranabant + 0.05% LMNG + 0.005% CHS | Final polishing step; LCP microcrystals obtained from purified sample |

**Final sample**: Purified CB1(T210A)-PGS in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% LMNG, 0.005% CHS, 1 uM taranabant
**Purity**: Monodisperse peak by SEC; SDS-PAGE verified


## Crystallization

### doi/10.1016##j.cell.2020.01.008

| Parameter | Value |
|---|---|
| Method | Cryo-EM (single particle analysis) |
| Protein sample | CB1-Gi-scFv16 complex with AM841, 1 mg/mL |
| Reservoir | not applicable (cryo-EM) |
| Notes | Sample applied to glow-discharged holey carbon grid (CryoMatrix Amorphous alloy film R1.2/1.3, 300 mesh), vitrified using Vitrobot Mark IV at 100% humidity, 4C; blotting 2.5 s with blot force 2; images collected on Titan cryo-EM |

### doi/10.1038##nature20613

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | CB1(T210A)-PGS at 15 mg/mL with 1 uM taranabant |
| Lipid | Monoolein |
| Protein-to-lipid ratio | 2:1 (protein:lipid) |
| Temperature | 20 C |
| Notes | LCP microcrystals diffracted to 2.6 A resolution; 42 crystals merged into single dataset; molecular replacement solved structure; Rwork/Rfree = 0.19/0.23 |


## Biological / Functional Insights

### CB1-Gi complex structure

The CB1-Gi-scFv16 complex was solved by cryo-EM at 3.0 A resolution. The complex
was constituted in vitro from purified CB1, Gi heterotrimer, and scFv16 antibody
fragment. AM841 was used as the agonist. The scFv16 binds at the interface
comprising the alpha N helix of Gαi and the beta-propeller of Gβ, as previously
reported.

### CB1 activation mechanism with twin toggle switch

CB1 activation involves a "twin toggle switch" mechanism (Phe3.36 and Trp6.48)
that undergoes synergistic conformational changes to unleash large conformational
changes and induce G protein coupling. This is distinct from CB2 which uses only
the single "toggle switch" Trp6.48. The DRY and NPxxY motifs show similar
rearrangements between active and active-like states.

### CB1 balloon-like plasticity

CB1 exhibits "balloon-like plasticity" during transitions between different
conformational states, facilitating its inherent ability to respond to a diverse
array of ligands compared to CB2. Large conformational changes occur in both
extracellular and intracellular domains from inactive to active states.

### Cholesterol as endogenous allosteric modulator of CB1

Cholesterol binds to CB1 at a specific site involving Phe155^2.42 and Phe237^4.46.
In the CB1-Gi complex structure, these side chains undergo large conformational
changes and occupy the same position that cholesterol had in agonist-bound crystal
structures. Phe4.46 is unique to CB1 in class A GPCRs. Cholesterol binding is
not observed in CB2, suggesting CB1-specific allosteric modulation. Pregnenolone,
a cholesterol derivative, may also bind to the same region and act as a CB1
allosteric modulator.

### CB1 G protein coupling diversity

CB1 can couple to Gi, Gs, and Gq proteins, while CB2 couples specifically to Gi
only. The single residue difference in ICL2 (L222 in CB1 and P139 in CB2) may
contribute to this G protein-coupling diversity. L222 in CB1 facilitates its
coupling with Gs and likely Gq as well.

### Structural overlap with LPA1 binding pocket

The CB1 and LPA1 binding pockets share substantial overlap in ligand specificity
for polyunsaturated acyl chains. Both receptors recognize similar hydrophobic
acyl chains but differ in head group requirements. The biosynthetic pathways for
LPA and cannabinoid agonists intersect through common phospholipid precursors.
LPA receptors, S1P receptors, and cannabinoid receptors are grouped in the same
clade based on sequence alignment of the transmembrane region.

### Thr3.46 role in Gi coupling

An atypical polar amino acid Thr3.46 exists in both CB1 and CB2, compared to
conserved non-polar residues in 95% of class A GPCRs. T3.46A mutation disables
CB1 and CB2 in coupling to Gi. Upon activation, Tyr7.53 establishes new contacts
with Thr3.46, Leu3.43, and Arg3.50. Asp6.30 in TM6 interrupts its salt-bridge
interaction with Arg3.50, unlocking outward movement of TM6.

### CB1 inactive state structure with taranabant

The CB1(T210A)-PGS structure (2.6 A, PDB 5KPR) represents an inactive conformation
with a canonical ionic lock between Arg214^3.50 and Asp338^6.30. The extracellular
surface, including the membrane-proximal N-terminal region and ECL2, forms a lid
over the orthosteric pocket, almost completely shielding taranabant from solvent.
The orthosteric pocket is highly hydrophobic with 24 residues within 4 A of the
ligand. A gap between TM1 and TM7 may contribute to a membrane-embedded access
channel for lipophilic agonists.

### Taranabant and rimonabant binding modes

Taranabant makes multiple contacts with TM1 and TM7 of CB1. Rimonabant docking
yields a low-energy pose overlapping almost completely with taranabant, contacting
the same constellation of residues. Mutagenesis studies identified residues whose
mutation caused loss in binding affinity, many of which are in contact with the
ligand in the CB1 structure: Phe170^2.57, Phe174^2.61, Leu193^3.29, Trp279^5.43,
Trp356^6.48, Phe379^7.35, and Leu387^7.42.

### THC docking into CB1 binding pocket

Docking studies of THC (partial agonist) into the CB1 crystal structure show the
tricyclic core binding between TM1, TM2 and TM7, with the C3 alkyl chain
overlapping with the chlorophenyl moiety of taranabant and extending towards
Trp356^6.48. Conformational changes in Trp356 and its surroundings have been
proposed as a trigger for CB1 activation.


## Cross-References

- [Cannabinoid Receptor 2 (CNR2/CB2)](/xray-mp-wiki/proteins/cb2/) — CB2 shares 42% sequence identity; subtype selectivity of ligands
- [Taranabant](/xray-mp-wiki/reagents/ligands/taranabant/) — Inverse agonist used to crystallize CB1 at 2.6 A resolution (PDB 5KPR)
- [Rimonabant](/xray-mp-wiki/reagents/ligands/rimonabant/) — Related inverse agonist with overlapping binding mode in CB1
- [CP55,940](/xray-mp-wiki/reagents/ligands/cp55940/) — Agonist used in competition binding assays; Ki = 384 nM for CB1(T210A)-PGS
- [2-AG (2-Arachidonoylglycerol)](/xray-mp-wiki/reagents/ligands/2-ag/) — Endogenous cannabinoid agonist activated by CB1
- [AEA (Anandamide)](/xray-mp-wiki/reagents/ligands/aea/) — Endogenous cannabinoid agonist activated by CB1
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used in CB1(T210A)-PGS purification
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for initial membrane solubilization of CB1
