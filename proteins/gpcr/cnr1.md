---
title: Cannabinoid Receptor 1 (CNR1/CB1)
created: 2026-05-27
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2015.06.002, doi/10.1016##j.cell.2020.01.008, doi/10.1038##nature20613, doi/10.1016##j.cell.2016.10.004, doi/10.1038##s41589-019-0387-2, doi/10.1038##s41589-022-01038-y, doi/10.1038##nature23272]
verified: false
---

# Cannabinoid Receptor 1 (CNR1/CB1)

## Overview

Cannabinoid receptor 1 (CNR1, commonly known as CB1) is a class A G protein-coupled receptor that is the principal target of Delta-9-tetrahydrocannabinol (THC), the psychoactive compound from Cannabis sativa. CB1 is activated by endogenous cannabinoids (endocannabinoids) including anandamide (AEA) and 2-arachidonoylglycerol ([2-AG](/xray-mp-wiki/reagents/ligands/2-ag)). CB1 is widely distributed in the central nervous system and periphery, and mediates functions including pain modulation, appetite regulation, memory, and motor control. CB1 shares 42% sequence identity with CB2. CB1 can couple to Gi, Gs, and Gq proteins. CB1 has therapeutic potential for pain management, inflammation, obesity, and substance abuse disorders. CB1 is the most abundant GPCR in the central nervous system.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2015.06.002 | 5ZTY | 3.0 |  | CB1 with N-terminal deletion and C-terminal [Truncation](/xray-mp-wiki/concepts/truncation); antagonist AM10257 bound; inactive state | [Am10257](/xray-mp-wiki/reagents/ligands/am10257) |
| doi/10.1016##j.cell.2020.01.008 | 6KPG | 3.0 |  | CB1-Gi-[SCFV16](/xray-mp-wiki/reagents/antibodies/scfv16) complex; agonist AM841 bound; active state; complex constituted in vitro from purified protein components | [AM841](/xray-mp-wiki/reagents/ligands/am841) |
| doi/10.1038##nature20613 | 5KPR | 2.6 | P21 | CB1(T210A)-PGS fusion construct; N-terminal 89 residues truncated; C-terminal 51 residues truncated; ICL3 replaced with PGS; T210A thermostabilizing mutation; [Taranabant](/xray-mp-wiki/reagents/ligands/taranabant) bound; inactive state | [Taranabant](/xray-mp-wiki/reagents/ligands/taranabant) |
| doi/10.1016##j.cell.2016.10.004 | 5TGZ | 2.8 | C2 | CB1-Flavodoxin fusion in ICL3 (between Val306 and Pro332); N-terminal 98 residues truncated; C-terminal 58 residues truncated; AM6538 bound; inactive state; four thermostabilizing mutations (T210A, etc.) | [AM6538](/xray-mp-wiki/reagents/ligands/am6538) |
| doi/10.1038##s41589-019-0387-2 | 6KQI | 3.0 | C2 | CB1-PGS^CM (CB1 with T210A, S203K, E273K, T283V, R340E mutations; ICL3 replaced with PGS); CP55940 agonist and ORG27569 NAM bound | CP55940, ORG27569 |
| doi/10.1038##s41589-022-01038-y | 7FEE | Not specified |  | CB1 bound with CP55940 and ZCZ011 (positive allosteric modulator) | [CP55940](/xray-mp-wiki/reagents/ligands/cp55940), [ZCZ011](/xray-mp-wiki/reagents/ligands/zcz011) |
| doi/10.1038##s41589-022-01038-y | 7WV9 | Not specified |  | CP55940-ZCZ011 bound CB1-Gi complex | [CP55940](/xray-mp-wiki/reagents/ligands/cp55940), [ZCZ011](/xray-mp-wiki/reagents/ligands/zcz011) |
| doi/10.1038##nature23272 | 5XRA | 2.80 | P2_122_1 | CB1-Flavodoxin fusion in ICL3; N-terminal 98 residues truncated; C-terminal 58 residues truncated; AM11542 agonist bound; active-like state | [AM11542](/xray-mp-wiki/reagents/ligands/am11542) |
| doi/10.1038##nature23272 | 5XR8 | 2.95 | P2_122_1 | CB1-Flavodoxin fusion in ICL3; N-terminal 98 residues truncated; C-terminal 58 residues truncated; AM841 agonist bound; active-like state | [AM841](/xray-mp-wiki/reagents/ligands/am841) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus expression system)
- **Construct**: CB1 expressed in central nervous system and peripheral tissues; structural studies use recombinant expression in insect cells
- **Notes**: CB1-Gi-[SCFV16](/xray-mp-wiki/reagents/antibodies/scfv16) complex constituted in vitro from purified CB1, Gi heterotrimer, and scFv16 antibody fragment; CB1(T210A)-PGS construct expressed via Bac-to-Bac system in Sf9 cells; CB1-Flavodoxin construct expressed in HEK293T cells using PEI transfection

### Purification Workflow

*Source: doi/10.1016##j.cell.2020.01.008*

- **Expression system**: Sf9 insect cells
- **Expression construct**: CB1 purified from recombinant expression
- **Tag info**: Not specified

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Complex formation | In vitro reconstitution |  |  | CB1-Gi-[SCFV16](/xray-mp-wiki/reagents/antibodies/scfv16) complex constituted in vitro from purified CB1, Gi heterotrimer, and scFv16 |
| SEC | Size exclusion chromatography | Superdex 200 10/300 GL | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 100 mM NaCl, 0.00075% LMNG, 0.00025% GDN, 0.0001% CHS, 100 uM TCEP, 5 uM AM841 + 0.00075% [LMNG](/xray-mp-wiki/reagents/detergents/lmng) + 0.00025% GDN + 0.0001% CHS | Monomeric CB1-Gi-scFv16 complex isolated; concentrated to 1 mg/mL for [Cryo em](/xray-mp-wiki/methods/structure-determination/cryo-em) |

**Final sample**: 1 mg/mL
**Purity**: Peak fractions concentrated for [Cryo em](/xray-mp-wiki/methods/structure-determination/cryo-em) studies

### Purification Workflow

*Source: doi/10.1038##nature20613*

- **Expression system**: Sf9 insect cells
- **Expression construct**: CB1(T210A)-PGS fusion; N-terminal HA signal + Flag tag; C-terminal 10x His-tag; N-terminal 89 residues truncated; C-terminal 51 residues truncated; ICL3 (residues 302-332) replaced with PGS; T210A mutation
- **Tag info**: HA signal, Flag epitope (N-term), 10x His-tag (C-term), TEV site

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization |  | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 160 ug/mL benzamidine, 100 ug/mL leupeptin, 2 mg/mL [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide) + 1% DDM, 0.2% sodium cholate, 0.2% CHS, 10 uM [Taranabant](/xray-mp-wiki/reagents/ligands/taranabant) | Sf9 cell membranes solubilized 1 hr at 4C; ultracentrifugation 30 min at 100,000g |
| Ni-NTA affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA agarose (GE Healthcare) | 50 mM HEPES pH 7.5, 500 mM NaCl, 0.05% DDM, 0.01% sodium cholate, 0.01% CHS, 10% glycerol, 50 mM imidazole, 160 ug/mL [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine), 100 ug/mL leupeptin, 1 uM taranabant + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm) + 0.01% sodium cholate + 0.01% CHS | Batch incubation 3 hr at 4C; washed with 15 column volumes; eluted with 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) and 2 mM calcium |
| Anti-Flag affinity chromatography | Anti-Flag M1 affinity chromatography | Anti-Flag M1 affinity resin | 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng) (detergent exchanged from DDM on M1 resin) + 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng) | Detergent exchanged from 0.05% DDM to 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng) on resin |
| Tag cleavage | Enzymatic cleavage |  | 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng) | TEV protease (1:10 w/w) and PNGase F added to remove Flag tag and deglycosylate; receptor eluted with 0.2 mg/mL Flag peptide and 5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta) |
| SEC | Size exclusion chromatography | Superdex 200 | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% LMNG, 0.005% CHS, 1 uM [Taranabant](/xray-mp-wiki/reagents/ligands/taranabant) + 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng) + 0.005% CHS | Final polishing step; LCP microcrystals obtained from purified sample |

**Final sample**: Purified CB1(T210A)-PGS in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% LMNG, 0.005% CHS, 1 uM [Taranabant](/xray-mp-wiki/reagents/ligands/taranabant)
**Purity**: Monodisperse peak by SEC; SDS-PAGE verified

### Purification Workflow

*Source: doi/10.1016##j.cell.2016.10.004*

- **Expression system**: HEK293T cells (mammalian)
- **Expression construct**: CB1-Flavodoxin fusion; N-terminal HA signal + Flag tag; C-terminal 10x His-tag; ICL3 (Val306-Pro332) replaced with Flavodoxin; N-terminal 98 residues truncated; C-terminal 58 residues truncated
- **Tag info**: HA signal, Flag epitope (N-term), 10x His-tag (C-term)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization |  | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, protease inhibitors + 1% DDM, 0.2% sodium cholate, 0.2% CHS, 10 uM AM6538 | Membranes solubilized for 1 hr at 4C; ultracentrifugation at 100,000g |
| TALON IMAC affinity chromatography | Immobilized metal affinity chromatography | TALON IMAC resin | 50 mM HEPES pH 7.5, 500 mM NaCl, 0.05% DDM, 0.01% sodium cholate, 0.01% CHS, 10% glycerol, 50 mM imidazole + 0.05% DDM, 0.01% sodium cholate, 0.01% CHS | Batch incubation for 3 hr at 4C; washed with 15 column volumes; eluted with 200 mM imidazole and 2 mM calcium |
| Anti-Flag M1 affinity chromatography | Anti-Flag M1 affinity chromatography | Anti-Flag M1 affinity resin | 0.05% LMNG (detergent exchanged from DDM on M1 resin) + 0.05% LMNG | Detergent exchanged from 0.05% DDM to 0.05% LMNG on resin |
| SEC | Size exclusion chromatography | Superdex 200 | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% LMNG, 0.005% CHS, 1 uM AM6538 + 0.05% LMNG, 0.005% CHS | Final polishing step; concentrated to ~50 mg/mL for LCP crystallization |

**Final sample**: Purified CB1-Flavodoxin in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% LMNG, 0.005% CHS, 1 uM AM6538
**Purity**: Monodisperse by analytical SEC; SDS-PAGE verified


## Crystallization

### doi/10.1016##j.cell.2020.01.008

| Parameter | Value |
|---|---|
| Method | [Cryo em](/xray-mp-wiki/methods/structure-determination/cryo-em) (single particle analysis) |
| Protein sample | CB1-Gi-[SCFV16](/xray-mp-wiki/reagents/antibodies/scfv16) complex with AM841, 1 mg/mL |
| Reservoir | not applicable ([Cryo em](/xray-mp-wiki/methods/structure-determination/cryo-em)) |
| Notes | Sample applied to glow-discharged holey carbon grid (CryoMatrix Amorphous alloy film R1.2/1.3, 300 mesh), vitrified using Vitrobot Mark IV at 100% humidity, 4C; blotting 2.5 s with blot force 2; images collected on Titan [Cryo em](/xray-mp-wiki/methods/structure-determination/cryo-em) |

### doi/10.1038##nature20613

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | CB1(T210A)-PGS at 15 mg/mL with 1 uM [Taranabant](/xray-mp-wiki/reagents/ligands/taranabant) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Protein-to-lipid ratio | 2:1 (protein:lipid) |
| Temperature | 20 C |
| Notes | LCP microcrystals diffracted to 2.6 A resolution; 42 crystals merged into single dataset; molecular replacement solved structure; Rwork/Rfree = 0.19/0.23 |

### doi/10.1038##nature23272

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified CB1-Flavodoxin at ~35 mg/mL with 20 uM AM11542 or AM841 |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) (90% w/w) + [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) (10% w/w) |
| Protein-to-lipid ratio | 2:3 (protein:lipid) |
| Temperature | 20 C |
| Growth time | 1 wk |
| Notes | AM11542 crystals grew to full size in 1 week. AM841 crystals appeared after 2 days, full size after 1 week. 16 crystals (AM11542) and 10 crystals (AM841) merged for final datasets. Data collected at APS GM/CA-CAT 23ID-B and SLS X06SA. |

### doi/10.1016##j.cell.2016.10.004

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | CB1-Flavodoxin at ~50 mg/mL with 10 uM AM6538 |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) (90% w/w) + [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) (10% w/w) |
| Protein-to-lipid ratio | 2:3 (protein:lipid) |
| Temperature | 20 C |
| Growth time | 2 wk |
| Notes | 29 crystals merged into single dataset; molecular replacement with LPA1 (PDB 4Z34) and Flavodoxin (PDB 1I1O) as search models; Rwork/Rfree = not specified; data collected at Spring-8 BL41XU |


## Biological / Functional Insights

### CB1-Gi complex structure

The CB1-Gi-scFv16 complex was solved by [Cryo em](/xray-mp-wiki/methods/structure-determination/cryo-em) at 3.0 A resolution. The complex
was constituted in vitro from purified CB1, Gi heterotrimer, and scFv16 antibody
fragment. AM841 was used as the agonist. The scFv16 binds at the interface
comprising the alpha N helix of Gαi and the beta-propeller of Gβ, as previously
reported.

### CB1 activation mechanism with twin toggle switch

CB1 activation involves a "twin toggle switch" mechanism (Phe3.36 and Trp6.48)
that undergoes synergistic conformational changes to unleash large conformational
changes and induce G protein coupling. This is distinct from [CB2](/xray-mp-wiki/proteins/cb2) which uses only
the single "toggle switch" Trp6.48. The DRY and NPxxY motifs show similar
rearrangements between active and active-like states.

### CB1 balloon-like plasticity

CB1 exhibits "balloon-like plasticity" during transitions between different
conformational states, facilitating its inherent ability to respond to a diverse
array of ligands compared to [CB2](/xray-mp-wiki/proteins/cb2). Large conformational changes occur in both
extracellular and intracellular domains from inactive to active states.

### Cholesterol as endogenous allosteric modulator of CB1

[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) binds to CB1 at a specific site involving Phe155^2.42 and Phe237^4.46.
In the CB1-Gi complex structure, these side chains undergo large conformational
changes and occupy the same position that cholesterol had in agonist-bound crystal
structures. Phe4.46 is unique to CB1 in class A GPCRs. Cholesterol binding is
not observed in CB2, suggesting CB1-specific allosteric modulation. Pregnenolone,
a cholesterol derivative, may also bind to the same region and act as a CB1
allosteric modulator.

### CB1 G protein coupling diversity

CB1 can couple to Gi, Gs, and Gq proteins, while [CB2](/xray-mp-wiki/proteins/cb2) couples specifically to Gi
only. The single residue difference in ICL2 (L222 in CB1 and P139 in CB2) may
contribute to this G protein-coupling diversity. L222 in CB1 facilitates its
coupling with Gs and likely Gq as well.

### Structural overlap with LPA1 binding pocket

The CB1 and [LPA1](/xray-mp-wiki/proteins/lpa1) binding pockets share substantial overlap in ligand specificity
for polyunsaturated acyl chains. Both receptors recognize similar hydrophobic
acyl chains but differ in head group requirements. The biosynthetic pathways for
LPA and cannabinoid agonists intersect through common phospholipid precursors.
LPA receptors, S1P receptors, and cannabinoid receptors are grouped in the same
clade based on sequence alignment of the transmembrane region.

### Thr3.46 role in Gi coupling

An atypical polar amino acid Thr3.46 exists in both CB1 and [CB2](/xray-mp-wiki/proteins/cb2), compared to
conserved non-polar residues in 95% of class A GPCRs. T3.46A mutation disables
CB1 and CB2 in coupling to Gi. Upon activation, Tyr7.53 establishes new contacts
with Thr3.46, Leu3.43, and Arg3.50. Asp6.30 in TM6 interrupts its salt-bridge
interaction with Arg3.50, unlocking outward movement of TM6.

### CB1 inactive state structure with taranabant

The CB1(T210A)-PGS structure (2.6 A, PDB 5KPR) represents an inactive conformation
with a canonical ionic lock between Arg214^3.50 and Asp338^6.30. The extracellular
surface, including the membrane-proximal N-terminal region and ECL2, forms a lid
over the orthosteric pocket, almost completely shielding [Taranabant](/xray-mp-wiki/reagents/ligands/taranabant) from solvent.
The orthosteric pocket is highly hydrophobic with 24 residues within 4 A of the
ligand. A gap between TM1 and TM7 may contribute to a membrane-embedded access
channel for lipophilic agonists.

### Taranabant and rimonabant binding modes

[Taranabant](/xray-mp-wiki/reagents/ligands/taranabant) makes multiple contacts with TM1 and TM7 of CB1. Rimonabant docking
yields a low-energy pose overlapping almost completely with taranabant, contacting
the same constellation of residues. Mutagenesis studies identified residues whose
mutation caused loss in binding affinity, many of which are in contact with the
ligand in the CB1 structure: Phe170^2.57, Phe174^2.61, Leu193^3.29, Trp279^5.43,
Trp356^6.48, Phe379^7.35, and Leu387^7.42.

### THC docking into CB1 binding pocket

Docking studies of THC (partial agonist) into the CB1 crystal structure show the
tricyclic core binding between TM1, TM2 and TM7, with the C3 alkyl chain
overlapping with the chlorophenyl moiety of [Taranabant](/xray-mp-wiki/reagents/ligands/taranabant) and extending towards
Trp356^6.48. Conformational changes in Trp356 and its surroundings have been
proposed as a trigger for CB1 activation.

### CB1-AM6538 crystal structure (first CB1 structure)

The 2.8 A crystal structure of human CB1 in complex with the tight-binding antagonist AM6538 (PDB 5TGZ) represents the first high-resolution structure of CB1. The receptor was stabilized using a Flavodoxin fusion partner inserted in ICL3, and crystallized in lipidic cubic phase. The structure reveals an orthosteric binding pocket partially occluded by the N-terminal loop and ECL2, providing the molecular basis for antagonist binding and enabling docking studies of THC and synthetic cannabinoids. The AM6538 antagonist extends deep into the binding pocket, making extensive contacts with residues from TM1, TM2, TM3, TM5, TM6, and TM7. 

### CB1 allosteric modulation by ORG27569 at extrahelical site

The crystal structure of CB1 bound to CP55940 and ORG27569 (PDB 6KQI, 3.0 A) reveals that the NAM binds at an extrahelical site within the inner leaflet of the membrane, partially overlapping a conserved cholesterol interaction site at W241^4.50. The chloro-indole group of ORG27569 packs against the indole side chain of W241^4.50, and the piperidinylphenyl chain extends across TM4 residues T242^4.51 and I245^4.54.

### Intermediate conformational state captured by NAM

CB1 bound to CP55940 and ORG27569 adopts an intermediate conformation: the orthosteric pocket contracts to fit the agonist (as in active state), but the dual aromatic toggle switch (F200^3.36 and W356^6.48) remains in the inactive 'off' conformation. TM6 does not undergo the outward movement required for G protein coupling, explaining how ORG27569 acts as a NAM despite increased agonist binding (Bmax effect).

### W241^4.50 as hotspot for CB1 allosteric modulation

The tryptophan at position 4.50 (W241) is among the most highly conserved residues in class A GPCRs. A cholesterol molecule from the LCP matrix packs against W241^4.50 in agonist-only CB1 structures. ORG27569 binds at the same site but is skewed relative to cholesterol. This suggests that the surface surrounding W241^4.50 represents a general hotspot for allosteric modulation of GPCRs by lipids or lipophilic small molecules.

### F237^4.46 mutation alters allosteric modulation

The F237L mutation at the CB1 allosteric site increases agonist affinity and decreases inverse agonist affinity. F237^4.46 helps position F155^2.42 in the inactive conformation but shifts in the Gi-bound active state. The mutation reduces the Bmax effect of ORG27569 while increasing its potency, suggesting tighter NAM binding to the mutant surface.

### ZCZ011 positive allosteric modulation of CB1

ZCZ011 is a positive allosteric modulator (PAM) of CB1. The crystal structure of CB1 bound to CP55940 and ZCZ011 (PDB 7FEE, X-ray) and the cryo-EM structure of the CB1-Gi complex bound to CP55940 and ZCZ011 (PDB 7WV9, EMDB EMD-32850) reveal the structural basis for PAM action at CB1. ZCZ011 binds at an allosteric site distinct from the orthosteric CP55940 binding pocket. The structures were determined using synchrotron X-ray diffraction (beamline 32XU at SPring-8) and single-particle cryo-EM (Titan Krios at 300 kV). Data for the X-ray structure was merged from 94 individual microcrystals due to radiation damage. The cryo-EM reconstruction used over 5500 individual movies.

### Agonist-bound CB1 structures reveal twin toggle switch activation

Crystal structures of CB1 bound to the agonists AM11542 (2.80 A, PDB 5XRA) and AM841 (2.95 A, PDB 5XR8) reveal important conformational changes compared to the antagonist-bound state, including a 53% reduction in ligand-binding pocket volume (from 821.8 to 383.5 A^3) and an increase in surface area of the G-protein-binding region. A "twin toggle switch" of Phe200^3.36 and Trp356^6.48 is experimentally observed and essential for receptor activation. The DRY motif polar network is disrupted: Arg214^3.50 adopts an extended conformation, the intra-helical salt bridge between Asp213^3.49 and Arg214^3.50 is broken, and the "ionic lock" between Arg214^3.50 and Asp338^6.30 is disrupted, resulting in helix VI movement. CB1 shows the largest helix VI bending angle among all known agonist-bound (without G protein or mimic) class A GPCRs. A partial "unwinding" of helix VII around Tyr397^7.53 is also observed.

### CB1 binding pocket plasticity accommodates diverse ligands

The agonist-bound CB1 structures reveal a 53% volume reduction in the ligand-binding pocket compared to the antagonist-bound state, representing the largest change among all class A GPCR structural pairs. This balloon-like flexibility is contributed mainly by movements of the extracellular half of helices I and II. The plasticity enables CB1 to respond to a diverse array of ligands with considerably different sizes, shapes and functions, consistent with the repertoire of CB1 to modulate varied physiological and psychological activities. This feature may also occur in other GPCRs, suggesting that multiple structurally varied receptor models should be considered when designing agonists and antagonists.

### DMH alkyl chain interactions extend agonist binding

The 1,1-gem-dimethylheptyl (DMH) alkyl chain of AM11542 and AM841 plays a key role in CB1 activation. The C1-gem-dimethyl group forms hydrophobic interactions with Phe200^3.36, Leu259^6.5 and Met363^6.55. The DMH moiety occupies a similar position as "arm 2" of the antagonist AM6538 and the alkyl chain of ML056 in S1P1, suggesting a conserved binding pocket for alkyl chains among lipid-binding GPCRs. Docking of representative agonists from three different scaffolds (classical cannabinoids, endocannabinoids and aminoalkylindoles) was validated with 1 us molecular dynamics simulations.

### Conserved twin toggle switch in other class A GPCRs

Sequence analysis among class A GPCRs shows that CB2 as well as certain beta-type receptors (such as CCR2 and CCR5) possess an aromatic residue at position 3.36 (Phe/Tyr) to synergize with the highly conserved Trp^6.48 on helix VI, suggesting the twin toggle switch mechanism extends beyond CB1. This structural feature contrasts with receptors that lack an aromatic at position 3.36 and may rely on a single Trp6.48 toggle switch.


## Cross-References

- [Cannabinoid Receptor 2 (CNR2/CB2)](/xray-mp-wiki/proteins/gpcr/cb2/) — CB2 shares 42% sequence identity; subtype selectivity of ligands
- [Taranabant](/xray-mp-wiki/reagents/ligands/taranabant/) — Inverse agonist used to crystallize CB1 at 2.6 A resolution (PDB 5KPR)
- [Rimonabant](/xray-mp-wiki/reagents/ligands/rimonabant/) — Related inverse agonist with overlapping binding mode in CB1
- [CP55,940](/xray-mp-wiki/reagents/ligands/cp55940/) — Agonist used in competition binding assays; Ki = 384 nM for CB1(T210A)-PGS
- [2-AG (2-Arachidonoylglycerol)](/xray-mp-wiki/reagents/ligands/2-ag/) — Endogenous cannabinoid agonist activated by CB1
- [AEA (Anandamide)](/xray-mp-wiki/reagents/ligands/aea/) — Endogenous cannabinoid agonist activated by CB1
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used in CB1(T210A)-PGS purification
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for initial membrane solubilization of CB1
- [LPA1](/xray-mp-wiki/proteins/lpa1) — Entity mentioned in overview or biological insights
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em) — Entity mentioned in overview or biological insights
- [AM6538](/xray-mp-wiki/reagents/ligands/am6538/) — Tight-binding antagonist used in first CB1 crystal structure (PDB 5TGZ, 2.8 A)
- [ORG27569](/xray-mp-wiki/reagents/ligands/org27569/) — NAM co-crystallized with CB1; allosteric modulator binding at extrahelical site (PDB 6KQI)
- [ZCZ011](/xray-mp-wiki/reagents/ligands/zcz011/) — Positive allosteric modulator (PAM) of CB1; co-crystallized with CP55940 in CB1 X-ray (PDB 7FEE) and CB1-Gi cryo-EM (PDB 7WV9) structures
