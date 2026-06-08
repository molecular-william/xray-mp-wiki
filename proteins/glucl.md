---
title: GluCl (GABA-Gated Chloride Channel from C. elegans)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##emboj.2013.17]
verified: false
---

# GluCl (GABA-Gated Chloride Channel from C. elegans)

## Overview

GluCl is the GABA-gated chloride channel from Caenorhabditis elegans. It is a pentameric ligand-gated ion channel (pLGIC) belonging to the Cys-loop receptor superfamily, which also includes nicotinic acetylcholine receptors (nAChR), glycine receptors, and GABA_A receptors. GluCl is activated by GABA and glycine, and is the molecular target of ivermectin, a widely used antiparasitic drug. The high-resolution crystal structure of GluCl provided important insights into the architecture of eukaryotic pLGICs and the mechanism of ivermectin binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##emboj.2013.17 | 3RHW | 3.3 A | Not specified in supplementary paper | Full-length GluCl from Caenorhabditis elegans | GABA, glycine |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### Comparison of GluCl with GLIC reveals conserved pore architecture

The 3.3 A resolution structure of GluCl was used as a comparison to the 2.4 A GLIC structure in molecular dynamics simulations and electrostatics calculations. AquaSol and MD simulations of GluCl revealed anion density within the pore, with the Thr6' and Thr2' side chains actively contributing to anion translocation. This contrasts with GLIC, where Ser6' and Thr2' contribute to cation translocation. The conserved cis-proline in the Cys-loop was also confirmed in GluCl, with the Phe/Tyr-Pro motif at the apex of the Cys-loop adopting a cis conformation that forms a hydrogen bond with M3, similar to GLIC.

### Ivermectin binding site in GluCl

GluCl serves as the archetypal eukaryotic pLGIC structure, revealing an ivermectin binding site at the interface between the extracellular and transmembrane domains. This site is distinct from the orthosteric GABA-binding site and represents an allosteric modulator pocket. The GluCl structure has been instrumental in understanding the mechanism of ivermectin action as an antiparasitic agent and its selectivity for invertebrate channels.

### Cis-proline in the Cys-loop of GluCl

The high-resolution GLIC structure confirmed that the conserved proline residue in the Phe/Tyr-Pro-Phe/Met motif at the apex of the Cys-loop adopts a cis conformation in GluCl, contrary to earlier structures that built it in trans. Residual electron density in the original GluCl structure showed both positive and negative peaks near the carbonyl group of this proline, indicating the trans conformation should be inverted. The cis conformation makes the residual density vanish after refinement. This cis-proline forms a hydrogen bond with residue 20' in the M3 helix, extending M3 through the Cys-loop and articulating the transmembrane domain with respect to the extracellular domain.


## Cross-References

- [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic/) — Bacterial pLGIC homolog; used for direct structural comparison
- [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) — High-affinity allosteric modulator of GluCl; antiparasitic drug target
- [Glycine](/xray-mp-wiki/reagents/ligands/glycine/) — Co-agonist that activates GluCl alongside GABA
- [Channel Gating via Plug Domain Displacement](/xray-mp-wiki/concepts/channel-gating/) — Related gating mechanism in Cys-loop receptors
