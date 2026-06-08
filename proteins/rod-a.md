---
title: Thermus thermophilus RodA
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature25985]
verified: false
---

# Thermus thermophilus RodA

## Overview

RodA is a 359-residue transmembrane peptidoglycan polymerase from the Shape, Elongation, Division, and Sporulation (SEDS) protein family. It is an essential bacterial enzyme that catalyzes the glycosyl transfer reaction in peptidoglycan cell wall synthesis. RodA was the first SEDS protein to be structurally characterized, revealing a unique ten-pass transmembrane fold with a large extracellular cavity and a lipid binding groove. The protein forms a complex with class B penicillin binding proteins (bPBPs) to coordinate glycan strand elongation and peptide crosslinking during cell wall biogenesis. RodA and other SEDS proteins represent promising targets for next-generation antibiotics.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature25985 | 6BAR | 2.9 | C2 | Thermus thermophilus RodA, 359 residues, N-terminal SUMO-FLAG-3C protease cleavage site tag | Monoolein (tentatively modeled) |
| doi/10.1038##nature25985 | 6BAS | 3.2 | C2 | Thermus thermophilus RodA D255A catalytically inactive mutant, 359 residues, N-terminal SUMO-FLAG-3C protease cleavage site tag | None resolved |

## Expression and Purification

- **Expression system**: Escherichia coli C43 (DE3) derivative harboring arabinose-inducible Ulp1 protease plasmid (pAM174)
- **Construct**: Thermus thermophilus rodA (Uniprot Q5SIX3) cloned into pAM172 plasmid with N-terminal SUMO-FLAG-3C protease cleavage site tag (SUMO-FLAG-3C-RodA)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication of resuspended cells in lysis buffer containing lysozyme and benzonase nuclease | -- | 50 mM HEPES pH 7.5, 150 mM NaCl, 20 mM MgCl2, 100 ug/mL lysozyme, 2 mg/mL iodoacetamide + -- | Membranes collected by ultracentrifugation at 100,000xg for 1 h at 4 C |
| Solubilization | Glass dounce tissue grinder extraction in solubilization buffer | -- | 20 mM HEPES pH 7.5, 500 mM NaCl, 20% glycerol, 2 mg/mL iodoacetamide + 1% n-Dodecyl beta-D-maltoside (DDM) | Samples stirred for 2 h at 4 C, centrifuged at 100,000xg for 1 h |
| Affinity purification | Anti-FLAG antibody affinity chromatography | Anti-Flag antibody affinity resin (4 mL) | 20 mM HEPES pH 7.0, 500 mM NaCl, 2 mM CaCl2, 20% glycerol, 0.1% DDM + 0.1% DDM | Washed extensively, then in buffer supplemented with 10 mM ATP magnesium salt and 20 mM KCl to remove bacterial chaperones GroEL and DnaK |
| Elution and tag removal | Elution with Flag peptide, followed by 3C protease cleavage | -- | 20 mM HEPES pH 7.0, 500 mM NaCl, 20% glycerol, 0.1% DDM, 5 mM EDTA, 0.2 mg/mL Flag peptide + 0.1% DDM | 3C protease added at 1:1000 w:w ratio, incubated at 4 C overnight |


## Crystallization

### doi/10.1038##nature25985

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization using coupled syringe reconstitution |
| Protein sample | Purified T. thermophilus RodA reconstituted in 10:1 monoolein:cholesterol (w:w) at 1.0:1.5 protein:lipid ratio by mass |
| Temperature | Room temperature (not specified) |
| Growth time | 2-4 weeks for diffraction-quality crystals |
| Cryoprotection | Crystals harvested with mesh loops and stored in liquid nitrogen |
| Notes | Initial crystallization hits grew within 24 h. Crystals diffracted to 2.9 A (wild-type) and 3.2 A (D255A mutant). Both crystallized in C2 space group with one molecule in the asymmetric unit and approximately 60% solvent content. Data collected at Advanced Photon Source GM/CA beamline 23ID-B at wavelength 1.033 A.
 |


## Biological / Functional Insights

### Unique ten-pass transmembrane fold with large extracellular loops


RodA possesses a novel ten-pass transmembrane fold with largely straight helices perpendicular to the membrane plane, except TM3 which runs diagonally with a 45 degree kink at Pro71. Extracellular loops 2, 4, and 5 are large and contain many functionally essential residues, consistent with catalytic activity at the extracytoplasmic face. ECL2 includes a highly conserved beta-hairpin capped by Gly100 and Pro101. ECL4 is the largest at 80 residues but is partially disordered (residues 189-227 and 237-251 unresolved). ECL5 is buried within the protein core, unlike other ECLs.

### Central water-filled cavity with essential salt bridge for catalysis


A large water-filled cavity open to the extracellular face is flanked by Glu108, Met306, Leu307, Gln310, and Thr342. Glu108 and Lys111 form an absolutely conserved salt bridge on the cavity edge. Mutagenesis of these residues (E108A, K111A, E108K/K111E double swap) results in dominant-negative phenotypes and abolishes peptidoglycan polymerization activity in vitro. Additional essential cavity residues include Asp255 and Asp152. The cavity is catalytically essential, not merely structural, making it a prime target for antibiotic discovery.

### Hydrophobic groove as lipid-anchored substrate binding site


Between TM2 and TM3 is a long hydrophobic groove containing electron density suggestive of a bound lipid molecule, tentatively modeled as monoolein from the crystallization conditions. This groove is adjacent to a collection of highly conserved residues and may represent the binding site for lipid-anchored substrates of RodA, such as lipid II.

### Interaction interface with class B penicillin binding proteins


Evolutionary coupling analysis maps the binding site between bPBPs and RodA to TM8 and TM9. SEDS proteins and bPBPs likely form a complex in cells that contains both glycan strand polymerization and peptide crosslinking active sites. Mutations in this interface (e.g., L240S, S326A, L281A in E. coli RodA) exhibit dominant-negative effects in vivo. However, mutation of this site does not prevent RodA-mediated peptidoglycan polymerization in vitro, confirming the functional importance of coordinated glycan strand elongation and peptide crosslinking in cells.

### SEDS proteins as essential cell wall polymerases


SEDS proteins (Shape, Elongation, Division, and Sporulation) are a ubiquitous and essential family of transmembrane enzymes with critical roles in bacterial cell wall biology. RodA was the first SEDS protein demonstrated to be a peptidoglycan polymerase, a role previously attributed exclusively to penicillin binding proteins. SEDS proteins are even more widely distributed than class A penicillin binding proteins and represent promising targets for next-generation antibiotic development.


## Cross-References

- [SEDS Protein Family](/xray-mp-wiki/concepts/sed-s-protein-family/) — RodA is the prototypical member of the SEDS protein family of peptidoglycan polymerases
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Structure solved using evolutionary coupling enabled molecular replacement (EC-MR)
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — RodA crystallized in LCP with monoolein:cholesterol mixture using coupled syringe method
- [n-Dodecyl beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for membrane solubilization during protein purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Host lipid for LCP crystallization; tentatively modeled as bound lipid in structure
- [Cholesterol](/xray-mp-wiki/reagents/additives/cholesterol/) — Added to monoolein for LCP reconstitution at 10:1 lipid ratio
- [Circular Dichroism Spectroscopy](/xray-mp-wiki/methods/quality-assessment/circular-dichroism-spectroscopy/) — Used to verify proper folding of RodA mutants (e.g., E108K/K111E swap)
