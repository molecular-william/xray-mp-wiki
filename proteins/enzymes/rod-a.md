---
title: "Thermus thermophilus RodA"
created: 2026-06-03
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature25985, doi/10.1038##s41564-020-0687-z]
verified: false
---

# Thermus thermophilus RodA

## Overview

RodA is a 359-residue transmembrane peptidoglycan polymerase from the Shape, Elongation, Division, and Sporulation (SEDS) protein family. It is an essential bacterial enzyme that catalyzes the glycosyl transfer reaction in peptidoglycan cell wall synthesis. RodA was the first SEDS protein to be structurally characterized, revealing a unique ten-pass transmembrane fold with a large extracellular cavity and a lipid binding groove. The protein forms a complex with class B penicillin binding proteins (bPBPs) to coordinate glycan strand elongation and peptide crosslinking during cell wall biogenesis. The crystal structure of the RodA-PBP2 complex at 3.3 A resolution reveals a 1:1 stoichiometric complex with two extensive interaction interfaces and a large membrane-accessible cavity formed by a 10 A shift of TM7 when bound to PBP2. RodA and other SEDS proteins represent promising targets for next-generation antibiotics.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature25985 | 6BAR | 2.9 | C2 | Thermus thermophilus RodA, 359 residues, N-terminal SUMO-FLAG-3C protease cleavage site tag | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (tentatively modeled) |
| doi/10.1038##nature25985 | 6BAS | 3.2 | C2 | Thermus thermophilus RodA D255A catalytically inactive mutant, 359 residues, N-terminal SUMO-FLAG-3C protease cleavage site tag | None resolved |

## Expression and Purification

- **Expression system**: Escherichia coli C43 (DE3) derivative harboring arabinose-inducible Ulp1 protease plasmid (pAM174)
- **Construct**: Thermus thermophilus rodA (Uniprot Q5SIX3) cloned into pAM172 plasmid with N-terminal SUMO-FLAG-3C protease cleavage site tag (SUMO-FLAG-3C-RodA)

### Purification Workflow

#### Source: doi/10.1038##nature25985


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication of resuspended cells in lysis buffer containing lysozyme and benzonase nuclease | -- | 50 mM HEPES pH 7.5, 150 mM NaCl, 20 mM MgCl2, 100 ug/mL lysozyme, 2 mg/mL [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) + -- | Membranes collected by ultracentrifugation at 100,000xg for 1 h at 4 C |
| Solubilization | Glass dounce tissue grinder extraction in solubilization buffer | -- | 20 mM HEPES pH 7.5, 500 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mg/mL [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) + 1% n-Dodecyl beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Samples stirred for 2 h at 4 C, centrifuged at 100,000xg for 1 h |
| Affinity purification | Anti-FLAG antibody [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Anti-Flag antibody affinity resin (4 mL) | 20 mM HEPES pH 7.0, 500 mM NaCl, 2 mM CaCl2, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Washed extensively, then in buffer supplemented with 10 mM ATP magnesium salt and 20 mM KCl to remove bacterial chaperones GroEL and DnaK |
| Elution and tag removal | Elution with Flag peptide, followed by 3C protease cleavage | -- | 20 mM HEPES pH 7.0, 500 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 0.2 mg/mL Flag peptide + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | 3C protease added at 1:1000 w:w ratio, incubated at 4 C overnight |

#### Source: doi/10.1038##s41564-020-0687-z


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | -- | 20 mM Tris pH 7.5, 400 mM NaCl, 1 mM PMSF, benzonase nuclease + -- | Cell lysate pelleted by centrifugation at 50,000g for 45 min at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA affinity | Ni Sepharose Excel resin (GE Healthcare) | 20 mM Tris pH 7.5, 400 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (load), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash) + -- | Eluted in 20 mM Tris pH 7.5, 400 mM NaCl, 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Dialysis | Dialysis | -- | 20 mM Tris pH 7.5, 400 mM NaCl + -- | Dialyzed overnight at 4 C; protein flash-frozen in liquid nitrogen |


## Crystallization

### doi/10.1038##nature25985

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization using coupled syringe reconstitution |
| Protein sample | Purified T. thermophilus RodA reconstituted in 10:1 [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/):[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) (w:w) at 1.0:1.5 protein:lipid ratio by mass |
| Temperature | Room temperature (not specified) |
| Growth time | 2-4 weeks for diffraction-quality crystals |
| Cryoprotection | Crystals harvested with mesh loops and stored in liquid nitrogen |
| Notes | Initial crystallization hits grew within 24 h. Crystals diffracted to 2.9 A (wild-type) and 3.2 A (D255A mutant). Both crystallized in C2 space group with one molecule in the asymmetric unit and approximately 60% solvent content. Data collected at Advanced Photon Source GM/CA beamline 23ID-B at wavelength 1.033 A. |

### doi/10.1038##s41564-020-0687-z

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified T. thermophilus WT RodA-PBP2 or RodA D255A-PBP2 complex at 35 mg/ml |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (Hampton Research) |
| Temperature | Not specified (presumed room temperature) |
| Growth time | 1-4 weeks for diffraction-quality crystals |
| Cryoprotection | Crystals collected using mesh loops and stored in liquid nitrogen |
| Notes | D255A mutant complex incubated with 5 mM [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) before reconstitution. D255A reservoir: 35-45% [PEG](/xray-mp-wiki/reagents/additives/peg/) 300, 100 mM sodium sulfate, 100 mM MES pH 5.8-6.8, 10 mM strontium chloride. Complete dataset from 2 (WT) and 5 (D255A) crystals. Data collected at APS GM/CA 23ID-B and 23ID-D at 1.033 A wavelength. |


## Biological / Functional Insights

### Unique ten-pass transmembrane fold with large extracellular loops

RodA possesses a novel ten-pass transmembrane fold with largely straight helices perpendicular to the membrane plane, except TM3 which runs diagonally with a 45 degree kink at Pro71. Extracellular loops 2, 4, and 5 are large and contain many functionally essential residues, consistent with catalytic activity at the extracytoplasmic face. ECL2 includes a highly conserved beta-hairpin capped by Gly100 and Pro101. ECL4 is the largest at 80 residues but is partially disordered (residues 189-227 and 237-251 unresolved). ECL5 is buried within the protein core, unlike other ECLs.

### Central water-filled cavity with essential salt bridge for catalysis

A large water-filled cavity open to the extracellular face is flanked by Glu108, Met306, Leu307, Gln310, and Thr342. Glu108 and Lys111 form an absolutely conserved salt bridge on the cavity edge. Mutagenesis of these residues (E108A, K111A, E108K/K111E double swap) results in dominant-negative phenotypes and abolishes peptidoglycan polymerization activity in vitro. Additional essential cavity residues include Asp255 and Asp152. The cavity is catalytically essential, not merely structural, making it a prime target for antibiotic discovery.

### Hydrophobic groove as lipid-anchored substrate binding site

Between TM2 and TM3 is a long hydrophobic groove containing electron density suggestive of a bound lipid molecule, tentatively modeled as [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) from the crystallization conditions. This groove is adjacent to a collection of highly conserved residues and may represent the binding site for lipid-anchored substrates of RodA, such as lipid II.

### RodA-PBP2 complex structure reveals 1:1 stoichiometry and allosteric activation

The crystal structure of the T. thermophilus RodA-PBP2 complex at 3.3 A resolution reveals a 1:1 stoichiometric complex with two extensive interaction interfaces: one in the membrane plane (TM8-TM9 of RodA interacting with PBP2 transmembrane helix) and one at the extracytoplasmic surface (PBP2 pedestal domain contacting RodA ECL4). When bound to PBP2, RodA shows an approximately 10 A shift of TM7 that exposes a large membrane-accessible cavity (~15 x 30 A) sufficient to accommodate a lipid II molecule. The bPBP pedestal domain acts as the key allosteric activator of RodA both in vitro and in vivo, explaining how the SEDS-bPBP complex coordinates polymerization and crosslinking. Disrupting the pedestal-ECL4 interface by mutating hydrophobic residues (L43R, A186R) in PBP2 abolishes RodA glycosyltransferase activity. Negative-stain EM reveals the complex can adopt compact and extended conformations, with the extended form potentially reaching ~100 A above the membrane plane.

### SEDS proteins as essential cell wall polymerases

SEDS proteins (Shape, Elongation, Division, and Sporulation) are a ubiquitous and essential family of transmembrane enzymes with critical roles in bacterial cell wall biology. RodA was the first SEDS protein demonstrated to be a peptidoglycan polymerase, a role previously attributed exclusively to penicillin binding proteins. SEDS proteins are even more widely distributed than class A penicillin binding proteins and represent promising targets for next-generation antibiotic development.


## Cross-References

- [SEDS Protein Family](/xray-mp-wiki/concepts/protein-families/sed-s-protein-family/) — RodA is the prototypical member of the SEDS protein family of peptidoglycan polymerases
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Structure solved using molecular replacement with RodA as search template
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — RodA and RodA-PBP2 complex crystallized in LCP with monoolein
- [n-Dodecyl beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for membrane solubilization during protein purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Host lipid for LCP crystallization; tentatively modeled as bound lipid in structure
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Added to monoolein for LCP reconstitution at 10:1 lipid ratio
- [Circular Dichroism Spectroscopy](/xray-mp-wiki/methods/quality-assessment/circular-dichroism-spectroscopy/) — Used to verify proper folding of RodA mutants
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
