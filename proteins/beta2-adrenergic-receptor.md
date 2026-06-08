---
title: Human Beta2-Adrenergic Receptor (beta2 AR)
created: 2026-05-29
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1021##ja105108q, doi/10.1038##nature06325, doi/10.1038##nature08650, doi/10.1038##nature10361, doi/10.1038##nature12357, doi/10.1038##nature23652, doi/10.1038##ncomms8895]
verified: false
---

# Human Beta2-Adrenergic Receptor (beta2 AR)

## Overview

The human beta2-adrenergic receptor (beta2 AR) is a class A G protein-coupled receptor that plays a central role in sympathetic nervous system signaling, mediating effects on heart rate, bronchodilation, and metabolic processes. Multiple crystal structures have been determined using different stabilization strategies. The first structure (PDB: 2RH1, 3.4 A) used a C-terminal truncated construct (beta2 AR365) in complex with a Fab5 antibody fragment. Subsequent structures employed a T4 lysozyme (T4L) fusion replacing the flexible third intracellular loop (ICL3), crystallized with inverse agonists ICI 118,551, compound 2, and alprenolol at 2.8-3.1 A resolution. The landmark active-state structure (PDB: 3SNY, 3.2 A) captured the first high-resolution view of an agonist-bound GPCR in complex with its Gs heterotrimeric G protein. The structure of beta2 AR bound to the allosteric modulator Cmpd-15PA (PDB: 5X7D, 2.7 A) revealed the mechanism of intracellular allosteric antagonism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature06325 | 2RH1 | 3.4 A | C2 | beta2 AR365-Fab5 complex (truncated at residue 365, with N-terminal HA/FLAG tag, N187E mutation, C-terminal 48 residues deleted) | Carazolol |
| doi/10.1038##nature06325 | 2RH2 | 3.4 A | C2 | beta2 AR24/365-Fab5 complex (TEV-cleavable N-terminus, truncated at residue 365) | Carazolol |
| doi/10.1021##ja105108q | 3NY8 | 2.8 A | P212121 | Human beta2-adrenergic receptor with T4 lysozyme fusion (beta2AR-t4l) | ICI 118,551 |
| doi/10.1021##ja105108q | 3NY9 | 2.8 A | P212121 | Human beta2-adrenergic receptor with T4 lysozyme fusion (beta2AR-t4l) | Compound 2 (Kolb et al., 2009) |
| doi/10.1021##ja105108q | 3NYA | 3.1 A | P212121 | Human beta2-adrenergic receptor with T4 lysozyme fusion (beta2AR-t4l) | Alprenolol |
| doi/10.1038##nature10361 | 3SNY | 3.2 A | P212121 | T4L-beta2 AR fusion (N-terminal T4L, residues 29-365, N187E, M96T, M98T mutations) in complex with Gs heterotrimer (Galpha s short + His6-Gbeta1 + Ggamma2) and Nb35 nanobody | BI-167107 |
| doi/10.1038##nature10361 | 3NY7 | 3.5 A | P212121 | beta2 AR stabilized by G protein mimetic nanobody Nb80 | BI-167107 |
| doi/10.1038##nature23652 | 5X7D | 2.7 A | P212121 | Human beta2-adrenergic receptor with T4 lysozyme fusion (beta2AR-t4l), truncated at residue 365 | Carazolol, Cmpd-15PA |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| FLAG affinity chromatography | M1 FLAG affinity resin (Sigma) | — | Not specified | First purification step for beta2 AR365 from Sf-9 cell lysate |
| Alprenolol-Sepharose affinity chromatography | Alprenolol-Sepharose ligand affinity column | — | Not specified | Ligand-based affinity purification; alprenolol bound to receptor exchanged for carazolol on second M1 resin |
| Deglycosylation | PNGaseF treatment (NEB) | — | Not specified | N-linked glycosylations removed |
| Tag cleavage | AcTEV protease (Invitrogen) | — | Not specified | FLAG epitope removed |
| Concentration | 100 kDa Vivaspin concentrator (Vivascience) | — | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DDM, 10 uM carazolol | Concentrated to ~50 mg/ml |
| Complex formation | Mixing with Fab5 fragment | — | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DDM, 10 uM carazolol | Fab5 added in stoichiometric excess |
| Size-exclusion chromatography | Superdex-200 (10/300GL) | — | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DDM, 10 uM carazolol | Purification of beta2 AR365-Fab5 complex |
| Final concentration | Vivaspin concentrator | — | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DDM, 10 uM carazolol | Concentrated to ~60 mg/ml for crystallization |


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in S9 insect cells (BestBac, Expression Systems) | — | Not specified | T4L-beta2 AR construct (N-terminal T4L fusion, residues 29-365, truncated at 365) |
| Solubilization | DDM (n-dodecyl-beta-D-maltoside) | — | Not specified | Solubilized in DDM according to methods described previously |
| M1 Flag affinity chromatography | M1 Flag affinity resin (Sigma) | — | Not specified | Initial purification step |
| Alprenolol-Sepharose affinity chromatography | Alprenolol-Sepharose ligand affinity column | — | Not specified | Selection of functional receptor |
| Ligand exchange | Second M1 Flag affinity chromatography | — | Not specified | Receptor-bound alprenolol exchanged for high-affinity agonist BI-167107 |
| Dialysis | Dialysis against purification buffer | — | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DDM, 10 uM BI-167107 | Agonist-bound receptor dialyzed |
| Dephosphorylation | Lambda phosphatase (New England Biolabs) | — | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DDM, 10 uM BI-167107 | Phosphorylation removed |
| Concentration | 50 kDa MWCO Millipore concentrator | — | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DDM, 10 uM BI-167107 | Concentrated to ~50 mg/ml |
| Complex formation | Mixing with Gs heterotrimer and Nb35 nanobody | — | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DDM, 10 uM BI-167107 | T4L-beta2 AR-Gs-Nb35 complex formed at 1:1.2 molar ratio (Nb35 excess) |
| Detergent exchange | Exchange into MNG-3 detergent | — | MNG-3 | MNG-3 stabilizes complex during LCP incorporation |


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 insect cells (Expressions Systems, LLC) | — | Not specified | beta2 AR-T4L construct expressed in Sf9 cells |
| Solubilization | DDM (n-dodecyl-beta-D-maltoside) | — | 20 mM HEPES pH 7.5, 100 mM NaCl, 1% DDM | Cell membranes solubilized in DDM; 30 uM atenolol added to stabilize receptor |
| M1 Flag affinity chromatography | M1 Flag affinity resin (Sigma) | — | 20 mM HEPES pH 7.5, 100 mM NaCl, 1% DDM | Initial purification step |
| Elution | HMS-CHS buffer with Flag peptide and EDTA | — | 20 mM HEPES pH 7.5, 350 mM NaCl, 0.1% DDM, 0.02% CHS, 0.2 mg/ml Flag peptide, 5 mM EDTA | Flag peptide and EDTA used for elution |
| Reduction and alkylation | TCEP/iodoacetamide treatment | — | Not specified | Protein treated with TCEP and iodoacetamide |
| Alprenolol-Sepharose affinity chromatography | Alprenolol-Sepharose affinity resin | — | Not specified | Functional protein isolation |
| Detergent and ligand exchange | Second M1 Flag affinity column | — | 0.01% MNG detergent, 20 uM carazolol, 50 uM Cmpd-15PA | Detergent changed from 0.1% DDM to 0.01% MNG; ligand changed from alprenolol to carazolol and Cmpd-15PA |
| Dialysis | Overnight dialysis at 4 C | — | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.003% MNG, 0.0003% CHS, 10 uM carazolol, 10 uM Cmpd-15PA | Excess EDTA and Flag peptide removed; PNGaseF added for N-linked glycosylation removal |
| Concentration | 50 kDa cutoff Amicon centrifugal filters (Millipore) | — | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.003% MNG, 0.0003% CHS, 10 uM carazolol, 10 uM Cmpd-15PA | Concentrated to ~50 mg/ml |


## Crystallization

### doi/10.1038##nature06325

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Notes | Two crystal forms: beta2 AR365-Fab5 (C2, 3.4 A) and beta2 AR24/365-Fab5 (C2, 3.4 A). The Fab5 fragment provided crystallographic contacts enabling structure determination.
 |

### doi/10.1021##ja105108q

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | Monoolein |
| Temperature | 19 C |
| Notes | Three complexes determined: ICI 118,551 (3NY8), compound 2 (3NY9), and alprenolol (3NYA). All in P212121 space group.
 |

### doi/10.1038##nature10361

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | 7.7 MAG (modified monolein) with 10% cholesterol |
| Temperature | Not specified |
| Notes | T4L-beta2 AR-Gs-Nb35 complex crystallized in LCP using twin-syringe mixing method. Protein:lipid ratio 1:1 (w/w), complex concentration ~25 mg/ml. MNG-3 detergent used for stabilization. 7.7 MAG designed to accommodate large hydrophilic component of T4L-beta2 AR-Gs complex.
 |

### doi/10.1038##nature23652

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | Monoolein with 10% cholesterol |
| Temperature | Not specified |
| Notes | beta2 AR-T4L bound to carazolol and Cmpd-15PA crystallized in LCP using two-syringe method. Protein:lipid ratio 2:3 (w/w). Crystallization precipitant: 0.1 M Tris-HCl pH 7.5, 30-37.5% PEG400, 400 mM NH4F, 6% 1,4-butanediol, 1 mM Cmpd-15PA, 1% DMSO. Crystals appeared after 1 day and grew to full size within 1 week. Diffraction data anisotropic (3.1 A, 2.7 A, 2.8 A along a*, b*, c* axes). Data processed with XDS. 43 crystals used for data collection at SPring-8 beamline BL32XU.
 |


## Biological / Functional Insights

### First crystal structure of beta2-adrenergic receptor

The beta2 AR365-Fab5 complex structure (PDB: 2RH1, 3.4 A) represented the first
high-resolution crystal structure of a beta-adrenergic receptor. The C-terminal
truncation (residues 366-413 deleted) removed the intracellular tail that interferes
with crystallization, while the Fab5 antibody fragment bound to the third intracellular
loop provided additional crystallographic contact surfaces.

### Conserved hydroxy-amine binding motif

All three compounds (ICI 118,551, compound 2, and alprenolol) contain a hydroxy-amine
motif that establishes a conserved hydrogen bond network with the receptor. This motif
is a common feature among the 'classical' scaffold of beta2 AR ligands with inverse
agonist, antagonist, or full/partial agonist activities.

### Ligand-specific aromatic interactions define pharmacology

While the hydroxy-amine motif is conserved, distinct interactions between the head groups
of the ligands and the receptor are observed. The aromatic moieties of all compounds are
anchored by strong hydrophobic interactions in the binding cleft. Specific hydrogen bonds
are established by substituent moieties in compound 2, timolol, and carazolol.

### Minor conformational impact of inverse agonists and antagonists

Minimal structural differences between the three complexes indicate that the ligands
studied exert only a minor local impact on the structure of the receptor. The result
that beta2 AR bound to pharmacologically distinct ligands have virtually identical
backbone conformations suggests that conformational changes capable of modifying
signaling properties are very small.

### Ligand-specific extracellular surface (ECS) conformations

NMR spectroscopy of [13C]methyl-beta2 AR revealed three distinct conformations of the
extracellular surface: one for the unliganded receptor or neutral antagonist (alprenolol),
one for the inverse agonist (carazolol), and one for the agonist (formoterol). The
Lys 305-Asp 192 salt bridge, linking extracellular loops 2 and 3, serves as a key
reporter of ECS conformation. Inverse agonists stabilize the salt bridge, while
agonists induce conformational fluctuations that liberate Lys 305 from the salt
bridge. These findings demonstrate conformational coupling between the orthosteric
ligand-binding pocket in the transmembrane core and the extracellular surface,
showing that drugs targeting this diverse surface could function as allosteric
modulators with high subtype selectivity.

### Active-state GPCR structure with Gs protein

The T4L-beta2 AR-Gs-Nb35 complex structure (PDB: 3SNY, 3.2 A) represents the first
high-resolution view of an active-state GPCR coupled to its G protein. Key structural
changes include a 14 A outward movement of TM6 at the cytoplasmic end and a 7-residue
extension of the cytoplasmic end of TM5. The Gs alpha-5 helix docks into a cavity
formed between TM5 and TM6, with 6 A displacement towards the receptor. The largest
conformational change in Gs is a 127-degree rotation of the alpha-helical domain
relative to the Ras domain, attributed to the empty nucleotide-binding pocket.

### GPCR-G protein interface interactions

The principal interactions between the beta2 AR and Gs involve the amino- and
carboxy-terminal alpha-helices of Galpha s. The carboxy-terminal alpha-5 helix of
Galpha s docks into a cavity formed by the opening of TM5 and TM6. A key interaction
involves Phe 139 of the beta2 AR at the beginning of the ICL2 helix, which sits in
a hydrophobic pocket on Galpha s formed by His 41, Val 217, Phe 376, Cys 379,
Arg 380, and Ile 383. The F139A mutation severely impairs Gs coupling.

### MNG-3 detergent stabilization

MNG-3 detergent uniquely stabilizes the beta2 AR even when diluted below its critical
micelle concentration, unlike DDM which rapidly loses binding activity. MNG-3
maintained the structural integrity of the T4L-beta2 AR-Gs complex during its
incorporation into lipidic cubic phase, improving both crystal size and quality.

### Intracellular allosteric modulation mechanism

The structure of beta2 AR-T4L bound to carazolol and Cmpd-15PA (PDB: 5X7D, 2.7 A)
revealed an intracellular allosteric binding pocket formed by the cytoplasmic ends
of TM1, TM2, TM6, TM7, ICL1, and helix 8. Cmpd-15PA stabilizes TM6 in the inactive
conformation through direct polar interactions with Thr274^6.36 and non-polar
interactions with Ala271^6.33 and Leu275^6.37. The compound disrupts a salt bridge
between Arg63^ICL1 and Asp331^8.49, enabling a new salt bridge between Lys267^6.29
and Asp331^8.49. This allosteric pocket is distinct from the orthosteric site and
overlaps with the G-protein-binding interface, explaining how Cmpd-15 inhibits
both G protein and beta-arrestin coupling. Molecular dynamics simulations show
that Cmpd-15 binding stabilizes a more inward conformation of TM6.


## Cross-References

- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion protein used to replace flexible ICL3 for crystallization
- [Fab5 Antibody Fragment](/xray-mp-wiki/reagents/antibodies/fab5/) — Monoclonal antibody fragment used for first beta2 AR crystal structure
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for crystallization of beta2AR-t4l complexes
- [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) — Inverse agonist used in first beta2 AR crystal structure
- [Alprenolol](/xray-mp-wiki/reagents/ligands/alprenolol/) — Beta blocker ligand used in beta2 AR structural studies
- [n-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/beta-ddm/) — Detergent used for solubilization and purification of beta2 AR
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in beta2 AR purification and crystallization
- [Gs Protein Alpha Subunit (Galpha s)](/xray-mp-wiki/proteins/gs-alpha/) — Gs alpha subunit coupled to activated beta2 AR in landmark 3SNY structure
