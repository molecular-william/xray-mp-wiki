---
title: ECF-FoIT Energy-Coupling Factor Transporter for Folate from Lactobacillus delbrueckii
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms11072]
verified: false
---

# ECF-FoIT Energy-Coupling Factor Transporter for Folate from Lactobacillus delbrueckii

## Overview

ECF-FoIT is a group II energy-coupling factor (ECF) transporter from Lactobacillus delbrueckii that mediates high-affinity uptake of folate. The transporter consists of the S-component FolT (which binds and transports folate) and the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module (EcfA, EcfA', and EcfT) that energizes transport via  hydrolysis. Crystal structures of solitary FolT1 in the folate-bound state (3.01 A), and of the complete ECF-FoIT2 complex in both the apo (3.00 A) and -bound (3.30 A) states, reveal the structural basis of the toppling transport mechanism. The S-component topples in the membrane to alternately expose its binding site to the extracellular side (outward-facing) or the cytosolic side (inward-facing, captured in the complex). Association with the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module allosterically disrupts the high-affinity folate-binding site, allowing substrate release into the cytosol.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms11072 | 5D0Y | 3.01 | C121 | Solitary FolT1 (folate-bound) | folate |
| doi/10.1038##ncomms11072 | 5D3M | 3.30 | P1 | ECF-FoIT2 complex (-bound) |  |
| doi/10.1038##ncomms11072 | 5D7T | 3.00 | P1 | ECF-FoIT2 complex (apo) | none (apo) |

## Expression and Purification

- **Expression system**: E. coli MC1061 with p2BAD vector; arabinose induction at 25 C for 3 h
- **Construct**: ECF-FoIT1/2: N-terminal His10-tag on EcfA, C-terminal StrepII-tag on FolT1/2; solitary FolT1/2: N-terminal His10-tag in L. lactis NZ9000

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### Toppling mechanism for substrate transport

The S-component FolT undergoes a dramatic reorientation in the membrane, rotating approximately 90 degrees so that its six transmembrane helices lie roughly parallel to the membrane plane in the toppled state. This movement alternately exposes the folate-binding site to the extracellular side for substrate capture (outward-facing) or to the cytosolic side for substrate release (inward-facing, post-translocation state). The toppled state is captured in the crystal structures of the full ECF-FoIT2 complex.

### Allosteric disruption of the folate-binding site by ECF module binding

In solitary FolT1, folate is bound with high affinity in a binding site formed by loops L1 and L3. When FolT docks onto the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module via complementary hydrophobic surfaces (the coupling helices of EcfT form a hydrophobic platform that binds helices 1 and 3 of FolT), loops L1 and L3 are displaced because they would sterically clash with TMH3 of EcfT at the conserved P71 position. This displacement disrupts the folate-binding site, allowing substrate release into the cytosol. High-affinity folate binding and [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module interaction are mutually exclusive.

### Transport cycle model and competition among S-components

The working model proposes: (1)  binding drives release of the empty S-component from the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module by disrupting the hydrophobic interface. (2) The solitary S-component reorients to an outward-facing state and binds substrate from the extracellular side. (3)  hydrolysis resets the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module. (4) Substrate-bound S-components have an intrinsic ability to topple spontaneously and are trapped by the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module's binding platform, which simultaneously destroys the binding site and releases substrate. Substrate-loaded S-components out-compete empty ones for [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module binding, explaining the preferential transport of scarce nutrients. The [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module exhibits high futile ATPase activity characteristic of this transporter family.


## Cross-References

- [Amp Pnp](/xray-mp-wiki/reagents/amp-pnp/) — Referenced in ecf-foit-lactobacillus-delbrueckii text
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Referenced in ecf-foit-lactobacillus-delbrueckii text
- [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) — Referenced in ecf-foit-lactobacillus-delbrueckii text
