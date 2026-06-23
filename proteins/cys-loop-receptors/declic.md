---
title: "DeCLIC (Desulfofustis deltaproteobacterium Pentameric Ligand-Gated Ion Channel)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1922701117]
verified: false
---

# DeCLIC (Desulfofustis deltaproteobacterium Pentameric Ligand-Gated Ion Channel)

## Overview

DeCLIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from a Desulfofustis deltaproteobacterium (closely related to Desulfofustis glycolicus), identified through a BLAST search on [Stelic](/xray-mp-wiki/proteins/cys-loop-receptors/stelic/). It is a multidomain pLGIC that incorporates a large periplasmic amino-terminal domain (NTD) accounting for approximately 50% of the total receptor mass. The NTD consists of two jelly-roll domains (NTD1, NTD2) that interact across each subunit interface. X-ray structures were determined in two conformational states: a Ca2+-bound closed-pore state at 3.55 A (PDB 6V45) and a Ca2+-free wide-open pore state at 3.83 A (PDB 6V4A). The NTD1 domain was also solved independently at 1.75 A (PDB 6V4B). DeCLIC is inhibited by extracellular Ca2+ (IC50 ~90 uM) and conducts currents upon Ca2+ depletion in Xenopus oocytes that are insensitive to quaternary ammonium blockers. The structures illustrate dramatic conformational state transitions and diverse regulatory mechanisms available to pLGICs, particularly involving Ca2+ modulation and periplasmic NTDs.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1922701117 | 6V45 | 3.55 | Not specified | Full-length DeCLIC in Ca2+-bound closed-pore conformation | Ca2+ (five symmetry-related Ca2+ ions at LBD subunit interfaces) |
| doi/10.1073##pnas.1922701117 | 6V4A | 3.83 | Not specified | Full-length DeCLIC in Ca2+-free wide-open pore conformation |  |
| doi/10.1073##pnas.1922701117 | 6V4B | 1.75 | Not specified | DeCLIC NTD1 domain (residues 34-202), SeMet-labeled | None |

## Expression and Purification

- **Expression system**: E. coli C43
- **Construct**: Full-length DeCLIC expressed as fusion with [Maltose](/xray-mp-wiki/reagents/additives/maltose/) binding protein (MBP) in C43 E. coli, solubilized, cleaved, and purified in n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/))
- **Notes**: A soluble NTD fragment (residues 33-202) was also expressed for independent crystallization and structure determination using SeMet SAD phasing.


### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Full-length DeCLIC expressed as MBP fusion in C43 E. coli. Soluble NTD fragment (residues 33-202) expressed separately.
 | Not specified | Not specified + Not specified | MBP fusion enabled solubilization and purification of full-length DeCLIC |
| Solubilization and purification | Standard [DDM](/xray-mp-wiki/reagents/detergents/ddm/) solubilization following protocols for other prokaryotic pLGICs | Not specified | Not specified + n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Full-length DeCLIC purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |


## Crystallization

### doi/10.1073##pnas.1922701117

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization |
| Protein sample | Purified DeCLIC in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 250 mM Ca2+ (for Ca2+-bound form); no Ca2+ (for Ca2+-free form) |
| Temperature | Not specified |
| Growth time | Not specified (extensive seeding and systematic screening required) |
| Cryoprotection | Not specified |
| Notes | Initial hits with 250 mM Ca2+. Extensive seeding and systematic screening required for diffracting crystals. NTD1 fragment crystals grew from independent crystallization setup. Ba2+ anomalous datasets confirmed Ca2+ binding sites. Data collected at synchrotron sources.
 |


## Biological / Functional Insights

### Ca2+-dependent gating mechanism

DeCLIC is inhibited by extracellular Ca2+ with IC50 ~90 uM. Ca2+ binds at the LBD subunit interface coordinated by E347 (beta1-beta2 loop), D437 and backbone carbonyls P434, P436 (Pro-loop), and E479 (complementary loop F). Upon Ca2+ depletion, loop F swings inward 8 A toward the channel axis, disrupting the Ca2+-mediated intersubunit contacts. A conserved electrostatic network between the F, beta1-beta2, and Pro-loops, homologous to the pH-sensing network in [Glic](/xray-mp-wiki/proteins/cys-loop-receptors/glic/), reorganizes to form intrasubunit contacts (Q344/E481), liberating arginines (R345, R569) that orient toward expanded TMD subunit interfaces to facilitate intercalation of lipid head groups.

### Multidomain allosteric transitions

DeCLIC exhibits state-dependent conformational changes across all three domains. The NTD undergoes radial contraction upon Ca2+ depletion, bringing NTD2 beta''1-beta''2 loops into proximity with LBD loop C (near the orthosteric agonist-binding site). The LBD exhibits domain contraction with decreased center-of-mass distance between adjacent subunits, and the amphipathic alpha1 helix translates and rotates ~40 degrees counter-clockwise toward the channel axis. The TMD exhibits outward twist and blooming with increased intersubunit distances, relieving all three hydrophobic constriction gates to create a wide-open pore.

### Reclassification of ELIC as 'locally closed' conformation

Based on the DeCLIC structures, the authors reclassify the previous structure of bacterial [Elic](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) (the first high-resolution pLGIC structure) as a 'locally closed' conformation rather than a fully closed state. ELIC's pore aligns closely with Ca2+-bound DeCLIC, including hydrophobic constrictions at 16' and 9' positions. [Elic](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) has been crystallized under numerous conditions but always in a nonconducting state, consistent with reclassification as a locally closed conformation that does not fully represent the resting state.

### Normal mode analysis of allosteric coupling

Torsional normal mode analysis predicted atomic fluctuations correlating well with B-factors (correlation factors 0.94 and 0.88 for closed and open states). A limited set of normal modes described 80% of the torsional component of both gating transitions. The analysis revealed that the vestibular site shows the largest couplings among all functional sites (orthosteric, vestibular, and pore), consistent with a role in allosteric modulation. Directionality and coordination couplings decreased in the open state while deformation coupling increased, consistent with the closed-to-open transition.


## Cross-References

- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related prokaryotic pLGIC; reclassified as 'locally closed' conformation based on DeCLIC structures
- [sTeLIC (Tevnia jerichonana Endosymbiont Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/stelic/) — Related prokaryotic pLGIC; DeCLIC identified via BLAST search on sTeLIC
- [GLIC (Gloeobacter violaceus Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Related prokaryotic pLGIC; gating mechanism compared in functional analysis
- [Cys-Loop Receptor Family](/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/) — pLGIC family classification; DeCLIC is a prokaryotic Cys-loop receptor homolog
- [Hydrophobic Gating](/xray-mp-wiki/concepts/transport-mechanisms/hydrophobic-gating/) — Pore constriction gates at F16' and L9' positions controlled by hydrophobic residues
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) — Referenced in context related to Maltose
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in context related to DDM
