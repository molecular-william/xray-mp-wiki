---
title: GluCl (C. elegans Glutamate-Gated Chloride Channel)
created: 2026-06-02
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10139, doi/10.1038##emboj.2013.17]
verified: false
---

# GluCl (C. elegans Glutamate-Gated Chloride Channel)

## Overview

GluCl is the glutamate-gated chloride channel from Caenorhabditis elegans, a pentameric ligand-gated ion channel (pLGIC) belonging to the Cys-loop receptor superfamily. It mediates fast inhibitory neurotransmission and is the molecular target of [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/), a broad-spectrum antiparasitic agent used to treat river blindness. The first X-ray structure of an inhibitory anion-selective Cys-loop receptor was determined for the GluCl-Fab complex at 3.3 A resolution (Nature 2011), revealing mechanisms of activation, permeation, and allosteric modulation by [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/), glutamate, and picrotoxin.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10139 | 3RIF | 3.3 A | Not specified | GluCl_cryst — residues 41–343 of C. elegans GluCl alpha with M3–M4 loop (K345–K402) replaced by Ala-Gly-Thr tripeptide; complexed with Fab | [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) (allosteric agonist), [L Glutamate](/xray-mp-wiki/reagents/substrates/l-glutamate/), picrotoxin |
| doi/10.1038##emboj.2013.17 | 3RHW | 3.3 A | Not specified in supplementary paper | Full-length GluCl from Caenorhabditis elegans | GABA, [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) |

## Expression and Purification

- **Expression system**: Baculovirus-infected Sf9 insect cells
- **Construct**: Codon-optimized full-length C. elegans GluCl alpha with native signal peptide and C-terminal 8xHis tag; M3–M4 loop (K345–K402) replaced by AGT tripeptide for crystallization; 41 N-terminal and 6 C-terminal residues deleted

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Emulsiflex-C5 homogenization | — | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 150 mM NaCl, 1 mM [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/) | Cells harvested 72-96 h post-infection |
| Membrane preparation | Differential centrifugation | — |  | Crude membranes collected at 125,000g |
| Solubilization | Detergent solubilization | — | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 150 mM NaCl + 0.25 g C12M (n-dodecyl-beta-D-maltopyranoside) per g membranes | Solubilized membranes clarified at 125,000g |
| Affinity purification | Immobilized metal affinity chromatography | [Talon](/xray-mp-wiki/reagents/additives/talon/) Co2+-affinity resin | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 150 mM NaCl, 1 mM C12M, 25 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash); 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) |  |
| Fab complex formation | Mixing with excess Fab, size-exclusion chromatography | Superose 6 10/300 GL | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 150 mM NaCl, 1 mM C12M |  |


## Crystallization

### doi/10.1038##nature10139

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion at 4 C |
| Protein sample | GluCl_cryst–Fab complex at 1–2 mg/ml with synthetic lipids ([Popc](/xray-mp-wiki/reagents/lipids/popc/) or DPPC at 0.02%) and 0.1 mM [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) |
| Reservoir | 21–23% [Peg](/xray-mp-wiki/reagents/additives/peg/) 400, 50 mM sodium [Citrate](/xray-mp-wiki/reagents/buffers/citrate/) pH 4.5, 70 mM sodium chloride |
| Temperature | 4 C |
| Growth time | Not specified |
| Notes | Crystals diffracted to ~3.3 A resolution. Additional structures obtained by soaking with glutamate, picrotoxin, or iodide. Fab derived from mouse monoclonal antibody against properly folded pentameric GluCl. |


## Biological / Functional Insights

### First structure of an inhibitory anion-selective Cys-loop receptor

The 3.3 A X-ray structure of the GluCl-Fab complex with [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) represents the first three-dimensional structure of an inhibitory anion-selective Cys-loop receptor. The homopentameric receptor reveals the architecture of the neurotransmitter-binding sites, the transmembrane pore, and the allosteric [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) binding site at the protein-lipid interface between M1, M2, and M3 helices.

### Ivermectin binds at subunit interfaces in the transmembrane domain

[Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/), a macrocyclic lactone used to treat river blindness, binds at each GluCl subunit interface on the periphery of the transmembrane domains, wedged between M3 on the principal (+) subunit and M1 on the complementary (-) subunit. It makes hydrogen bonds with the main-chain carbonyl of Leu218 (M1) and contacts with M2 and the M2-M3 loop. [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) acts as a partial allosteric agonist, stabilizing an open-pore conformation and pre-organizing the glutamate binding site ~30 A away.

### Glutamate binding site and specificity

Glutamate binds in the classical agonist site at subunit interfaces in the extracellular domain, between loops from the (+) subunit and beta strands from the (-) subunit. Loop C adopts a closed conformation. The alpha-amino group interacts with Tyr200 via cation-pi interaction, and the alpha- and gamma-carboxylates are coordinated by Arg37 and Arg56. The binding pocket has strong positive electrostatic potential and is selective for small dicarboxylate L-amino acids.

### Picrotoxin occludes the open pore

Picrotoxin, an open-channel blocker, binds at the cytosolic base of the transmembrane pore on the five-fold symmetry axis. The fused tricyclic rings point toward the extracellular side near 2' Thr residues, while the isoprenyl tail points toward the cytoplasm near -2' Pro residues. Picrotoxin binding confirms the pore is in an open, conducting conformation with a minimum diameter of ~4.6 A at the -2' Pro girdle.

### Ion selectivity mechanism

The pore constriction at -2' Pro residues (diameter ~4.6 A) and positive electrostatic potential from oriented M2 helix dipoles confer anion selectivity without any positively charged pore-lining residues. Four iodide (heavy atom analog of chloride) binding sites were identified at the cytosolic base of the pore in electropositive pockets formed by -2' Pro, -1' Ala, and -3' Ile residues. The -1' position preserves the anion pocket in chloride- selective channels, while cation channels have a conserved glutamate at this position that fills the pocket and imposes negative potential.

### Comparison of GluCl with GLIC reveals conserved pore architecture

The 3.3 A resolution structure of GluCl was used as a comparison to the 2.4 A [Glic](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) structure in molecular dynamics simulations and electrostatics calculations. AquaSol and MD simulations of GluCl revealed anion density within the pore, with the Thr6' and Thr2' side chains actively contributing to anion translocation. This contrasts with [Glic](/xray-mp-wiki/proteins/cys-loop-receptors/glic/), where Ser6' and Thr2' contribute to cation translocation. The conserved cis-proline in the Cys-loop was also confirmed in GluCl, with the Phe/Tyr-Pro motif at the apex of the Cys-loop adopting a cis conformation that forms a hydrogen bond with M3, similar to [Glic](/xray-mp-wiki/proteins/cys-loop-receptors/glic/).

### Ivermectin binding site in GluCl (archetypal eukaryotic pLGIC)

GluCl serves as the archetypal eukaryotic pLGIC structure, revealing an [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) binding site at the interface between the extracellular and transmembrane domains. This site is distinct from the orthosteric neurotransmitter-binding site and represents an allosteric modulator pocket. The GluCl structure has been instrumental in understanding the mechanism of [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) action as an antiparasitic agent and its selectivity for invertebrate channels.

### Cis-proline in the Cys-loop of GluCl

The high-resolution [Glic](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) structure confirmed that the conserved proline residue in the Phe/Tyr-Pro-Phe/Met motif at the apex of the Cys-loop adopts a cis conformation in GluCl, contrary to earlier structures that built it in trans. Residual electron density in the original GluCl structure showed both positive and negative peaks near the carbonyl group of this proline, indicating the trans conformation should be inverted. The cis conformation makes the residual density vanish after refinement. This cis-proline forms a hydrogen bond with residue 20' in the M3 helix, extending M3 through the Cys-loop and articulating the transmembrane domain with respect to the extracellular domain.


## Cross-References

- [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Bacterial pLGIC homolog; used for direct structural comparison
- [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) — High-affinity allosteric modulator of GluCl; antiparasitic drug target
- [L-Glutamate](/xray-mp-wiki/reagents/ligands/glutamate/) — Endogenous neurotransmitter that activates GluCl
- [Picrotoxin](/xray-mp-wiki/reagents/ligands/picrotoxin/) — Open-channel blocker confirming the pore is in an open conformation
- [Channel Gating via Plug Domain Displacement](/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/) — Related gating mechanism in Cys-loop receptors
- [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) — Referenced in glucl text
- [L Glutamate](/xray-mp-wiki/reagents/substrates/l-glutamate/) — Referenced in glucl text
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Referenced in glucl text
- [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/) — Referenced in glucl text
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in glucl text
