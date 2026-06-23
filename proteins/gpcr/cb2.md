---
title: "Cannabinoid Receptor 2 (CNR2/CB2)"
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.01.008, doi/10.1016##j.cell.2018.12.011]
verified: false
---

# Cannabinoid Receptor 2 (CNR2/CB2)

## Overview

[Cannabinoid](/xray-mp-wiki/concepts/cannabinoid) receptor 2 (CNR2, commonly known as CB2) is a class A G protein-coupled receptor that is the principal peripheral target of cannabinoids. Unlike CB1, CB2 is primarily expressed in the immune system and periphery, with minimal expression in the central nervous system. CB2 modulates immune responses, inflammation, and pain sensation without psychoactive effects. CB2 shares 44% total sequence identity and 68% sequence similarity in the transmembrane regions with CB1. CB2 is activated by endogenous cannabinoids and synthetic agonists, coupling primarily to Gi proteins. CB2 has therapeutic potential for inflammatory and neuropathic pain management without CB1 psychoactivity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2020.01.008 | 6KPC | 3.2 |  | Wild-type human CB2 (14656 construct); N-terminal BRIL fusion for stability; agonist [AM12033](/xray-mp-wiki/reagents/ligands/am12033) bound | [AM12033](/xray-mp-wiki/reagents/ligands/am12033) |
| doi/10.1016##j.cell.2020.01.008 | 6KPF | 2.9 |  | CB2-N-BRIL fusion; co-expressed with heterotrimeric [Gi Protein](/xray-mp-wiki/proteins/gi-protein) and scFv16 antibody fragment; agonist AM12033 bound; active state | [AM12033](/xray-mp-wiki/reagents/ligands/am12033) |
| doi/10.1016##j.cell.2018.12.011 | 5ZTY | 2.8 | P2(1)2(1)2(1) | CB2-T4L fusion (ICL3 replaced with T4L); N-term 1-20 and C-term 326-360 truncated; G78L, T127A, T153L, R242E, G304E mutations | [AM10257](/xray-mp-wiki/reagents/ligands/am10257) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (Bac-to-Bac [Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression))
- **Construct**: N-BRIL fused wild-type human CB2; N-terminal HA signal sequence followed by 10x His-tag and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag); human Gαi1 and Gβ1γ2 subunits cloned into pFastBac1 and pFastDual vector individually
- **Notes**: CB2 and Gi heterotrimer co-expressed in [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells) at 27C for 48 h. Sf9 cells infected at 2-2.5 x 10^6 cells/mL with three separate virus preparations for CB2, Gαi1, and Gβ1γ2 at ratio of 1:2:2.

### Purification Workflow

#### Source: doi/10.1016##j.cell.2020.01.008

- **Expression system**: Sf9 insect cells (Bac-to-Bac [Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression))
- **Expression construct**: CB2-N-BRIL fusion with HA signal, 10x His-tag, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag)
- **Tag info**: HA signal, 10x His (N-terminal), [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell infection | [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) infection |  |  | Sf9 cells infected at 2-2.5 x 10^6 cells/mL with CB2, Gαi1, Gβ1γ2 viruses at 1:2:2 ratio, 27C for 48 h |
| Cell lysis | Cell lysis |  |  | Infected cells cultured at 27C for 48 h, harvested by centrifugation, pellets stored at -80C |
| Membrane isolation | Centrifugation |  |  | Cell pellets harvested by centrifugation |
| Solubilization | Detergent solubilization |  | 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng) + 0.001% CHS | CB2-Gi-[scFv16](/xray-mp-wiki/reagents/antibodies/scfv16) complex solubilized with LMNG and CHS |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | Metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [TALON](/xray-mp-wiki/reagents/additives/talon) IMAC | 25 mM HEPES pH 7.5, 100 mM NaCl, 10% glycerol, 0.1% LMNG, 0.02% CHS, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 20 uM AM841 + 0.1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng) + 0.02% CHS | [His Tag](/xray-mp-wiki/reagents/protein-tags/his-tag) capture on TALON IMAC resin overnight at 4C |
| Tag cleavage | Protease cleavage |  |  | C-terminal 10x His tag cleaved by human [Human Rhinovirus 3C Protease](/xray-mp-wiki/reagents/additives/human-rhinovirus-3c-protease) |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | Hiload Superdex 75 10/300 | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 100 mM NaCl | Monomeric fractions pooled, concentrated, flash frozen |

**Final sample**: not specified
**Purity**: Monomeric fractions by [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)

#### Source: doi/10.1016##j.cell.2018.12.011

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells) (Bac-to-Bac [Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression))
- **Expression construct**: CB2-T4L fusion (ICL3 residues 222-235 replaced by T4L); N-term residues 1-20 and C-term 326-360 truncated; G78L, T127A, T153L, R242E, G304E mutations
- **Tag info**: None (no affinity tag)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell infection | [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) infection |  |  | Sf9 cells infected at 2-2.5 x 10^6 cells/mL with high-titer viral stock, MOI 5.0; harvested 48 h post-infection |
| Membrane preparation | Centrifugation and washing |  | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl (hypotonic); 10 mM HEPES pH 7.5, 1.0 M NaCl, 10 mM MgCl2, 20 mM KCl (high osmotic) | Membranes lysed by repeated washing and centrifugation; incubated with 20 uM AM10257 and inhibitor cocktail at 4C for 3 h; 1.0 mg/mL iodoacetamide added for 1 h |
| Solubilization | Detergent solubilization |  | 50 mM HEPES pH 7.5, 500 mM NaCl + 0.75% (w/v) [LMNG](/xray-mp-wiki/reagents/detergents/lmng) + 0.15% (w/v) CHS | Membranes solubilized for 2.5-3 h at 4C; supernatant isolated by ultracentrifugation |
| [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [TALON](/xray-mp-wiki/reagents/additives/talon) [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [TALON](/xray-mp-wiki/reagents/additives/talon) IMAC resin | 25 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) glycerol, 0.1% (w/v) LMNG, 0.02% (w/v) CHS, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 20 uM AM10257 + 0.1% LMNG + 0.02% CHS | Wash I: 15 CV wash buffer I; Wash II: 15 CV wash buffer II (0.03% LMNG, 0.006% CHS, 50 mM imidazole); elution with 250 mM imidazole |
| Concentration | 100 kDa cutoff concentrator | — | 25 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) glycerol, 0.01% (w/v) LMNG, 0.002% (w/v) CHS, 25 uM AM10257 + 0.01% LMNG + 0.002% CHS | Concentrated to 20 mg/mL for crystallization |

**Final sample**: CB2-T4L-AM10257 complex at 20 mg/mL


## Crystallization

### doi/10.1016##j.cell.2020.01.008

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) (LCP) |
| Protein sample | [AM12033](/xray-mp-wiki/reagents/ligands/am12033)-bound CB2 |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Protein-to-lipid ratio | not specified |
| Temperature | not specified |
| Growth time | 2 weeks; dehydrated to 40 mm x 20 mm after 2 weeks |
| Notes | Crystals grown by [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase); harvested with micro-mounts (MiTeGen) and flash frozen in liquid nitrogen; data collected at Spring-8 beamline 41XU with Pilatus3 6M detector at 1.0000 A wavelength |

### doi/10.1016##j.cell.2018.12.011

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) (LCP) |
| Protein sample | [AM10257](/xray-mp-wiki/reagents/ligands/am10257)-bound CB2-T4L |
| Lipid | 90% (w/v) [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) + 10% (w/v) [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) |
| Protein-to-lipid ratio | 2:3 (w/w) |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystals grown by [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) using syringe mixer; 96-well glass sandwich plates; 50 nL protein-lipid mesophase dispensed per well; data collected at Spring-8 BL32XU; 7 crystals merged; multiple small wedge data collection scheme |


## Biological / Functional Insights

### CB2-Gi complex structure and interaction interface

The CB2-Gi complex reveals extensive contacts mediated through the Gαi subunit.
The primary interaction interface comprises TM3, TM5, TM6, and ICL2 of CB2 and the
α5 helix, αN helix, and αN-β1 loop of Gαi. Two large hydrophobic side chains
L353 and L348 of the Gαi α5 helix are directed toward a hydrophobic pocket formed
by Val212^5.61, Leu243^6.33, Leu247^6.37, Leu239^6.29, and Leu135^3.54 from the
cytosolic ends of TM5, TM6, and TM3 of CB2. The Gi proteins in CB2-Gi complex show
a ~20 degree anticlockwise rotation when aligned with other GPCR-Gi complexes.
No electron density for [GDP](/xray-mp-wiki/reagents/ligands/gdp) is observed, suggesting Gi is nucleotide-free.

### AM12033 binding in CB2

[AM12033](/xray-mp-wiki/reagents/ligands/am12033) adopts an L-shape conformation in the orthosteric binding pocket.
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
[CB1](/xray-mp-wiki/proteins/cnr1) which uses a "twin toggle switch" (Phe3.36 and Trp6.48), CB2 requires only the
single "toggle switch" Trp6.48 to trigger activation and downstream signaling.

### CB2 activation vs CB1 activation differences

CB2 and [CB1](/xray-mp-wiki/proteins/cnr1) exhibit distinct activation processes. CB1 shows a more complicated
activation involving synergistic conformational change of the "twin toggle switch"
(Phe3.36 and Trp6.48) to unleash large conformational changes. CB2 experiences
only minor conformational changes upon agonist binding, behaving like most class A
GPCRs. The extracellular region of CB2, including the N terminus, undergoes very
minor changes during activation. CB1 displays larger conformational changes when
modulated by agonists, suggesting a "balloon-like plasticity" that facilitates
CB1's ability to respond to diverse ligands.

### Thr3.46 role in Gi coupling

An atypical polar amino acid Thr3.46 exists in both CB2 and [CB1](/xray-mp-wiki/proteins/cnr1), compared to
conserved non-polar residues (I/L/M/V) in 95% of class A GPCRs. T3.46A mutation
disables CB2 and CB1 in coupling to Gi. Upon activation, Tyr7.53 establishes new
contacts with Thr3.46, Leu3.43, and Arg3.50. Asp6.30 in TM6 interrupts its
salt-bridge interaction with Arg3.50, strengthening TM3-TM7 interaction, weakening
TM6 constraint from TM3, and unlocking outward movement of TM6.

### CB2-Gi complex rotation compared to other GPCRs

The Gi proteins in CB2- and CB1-Gi complexes show a ~20 degree anticlockwise
rotation when viewed from intracellular to extracellular direction, compared to
mu-opioid receptor, A1 adenosine, 5HT1B, and M2 Gi complexes. This distinct
orientation may contribute to G protein selectivity differences between [Cannabinoid](/xray-mp-wiki/concepts/cannabinoid)
receptors and other Gi-coupled GPCRs.

### CB1 cholesterol binding as endogenous allosteric modulation

[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) binds to CB1 at a specific site involving Phe155^2.42 and Phe237^4.46.
In the CB1-Gi complex structure, these side chains undergo large conformational
changes and occupy the same position that cholesterol had in agonist-bound crystal
structures. Phe4.46 is unique to CB1 in class A GPCRs. Cholesterol is not observed
in CB2 structures, suggesting CB1-specific allosteric modulation. Pregnenolone, a
cholesterol derivative, may also bind to the same region and act as a CB1 allosteric
modulator.

### CB1 and CB2 G protein coupling diversity

CB2 couples specifically to Gi only, while [CB1](/xray-mp-wiki/proteins/cnr1) can couple to Gi, Gs, and Gq. The
single residue difference in ICL2 (L222 in CB1 and P139 in CB2) may contribute to
this G protein-coupling diversity. L222 in CB1 facilitates its coupling with Gs and
likely Gq as well. The high structural similarity in orthosteric binding pockets between agonist-bound CB2 and CB1 imposes challenges for highly selective agonist design.

### Antagonist-bound CB2 structure reveals binding pocket differences from CB1

The crystal structure of human CB2 bound to the antagonist [AM10257](/xray-mp-wiki/reagents/ligands/am10257) at 2.8 A resolution (PDB 5ZTY) reveals a distinctly different binding pose compared to CB1. The CB2 antagonist-binding pocket (447 A^3) is smaller than the CB1 antagonist-binding pocket (822 A^3) and is more similar in size to the CB1 agonist-binding pocket (384 A^3). The toggle switch residue Trp258^6.48 adopts a relatively rare rotamer that confines helix VI in the inactive state. The unique yin-yang relationship between CB2 and CB1 - where [AM10257](/xray-mp-wiki/reagents/ligands/am10257) is an inverse agonist at CB2 but a partial agonist at CB1 - provides insights for selective [Cannabinoid](/xray-mp-wiki/concepts/cannabinoid) drug design.


## Cross-References

- [Cannabinoid Receptor 1 (CNR1/CB1)](/xray-mp-wiki/proteins/gpcr/cnr1/) — [CB1](/xray-mp-wiki/proteins/cnr1) shares 44% sequence identity and 68% TM similarity; compared in activation and signaling
- [AM12033](/xray-mp-wiki/reagents/ligands/am12033/) — Synthetic [Cannabinoid](/xray-mp-wiki/concepts/cannabinoid) agonist bound in both cryo-EM (6KPF) and crystal (6KPC) structures
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for CB2-Gi complex solubilization and purification
- [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) derivative used as stabilizer in CB2-Gi complex purification
- [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) — N-terminal fusion partner used to improve CB2 expression and stability
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — CB2-[AM12033](/xray-mp-wiki/reagents/ligands/am12033) crystal structure (6KPC) determined by LCP method
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — CB2-Gi-scFv16 complex (6KPF) solved by [Cryo-EM](/xray-mp-wiki/methods/structure-determination/cryo-em) at 2.9 A resolution
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used in LCP crystallization matrix for CB2-[AM12033](/xray-mp-wiki/reagents/ligands/am12033)
- [Cannabinoid](/xray-mp-wiki/concepts/cannabinoid) — Related structural or functional concept
- [Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) — Expression system used for protein production
