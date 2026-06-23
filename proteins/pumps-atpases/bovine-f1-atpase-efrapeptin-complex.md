---
title: Bovine F1-ATPase-Efrapeptin Complex
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography, enzyme]
sources: [doi/10.1073##pnas.93.18.9420]
verified: false
---

# Bovine F1-ATPase-Efrapeptin Complex

## Overview

The structure of bovine mitochondrial F1-ATPase complexed with efrapeptin C, a modified linear peptide antibiotic that inhibits both [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthesis and hydrolysis. Efrapeptin binds in the central cavity of F1-ATPase at a unique site formed by the gamma-subunit, the empty beta-E subunit, and the adjacent alpha-E and alpha-TP subunits. The binding is predominantly hydrophobic and prevents conversion of the beta-E subunit to a nucleotide-binding conformation, thereby blocking the cyclic interconversion of catalytic sites required by the binding change mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.93.18.9420 |  | 3.3 |  | Bovine mitochondrial F1-ATPase (alpha3beta3gamma subcomplex) with bound efrapeptin C | Efrapeptin C, [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), [ADP](/xray-mp-wiki/reagents/ligands/adp/) |

## Expression and Purification

- **Expression system**: Bovine heart mitochondria (native source)
- **Construct**: Native F1-ATPase purified from bovine heart mitochondria

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification of F1-ATPase from bovine heart mitochondria | Standard mitochondrial F1-ATPase purification protocol | -- | -- + -- | F1-ATPase was purified from bovine heart mitochondria. The alpha3beta3gamma subcomplex with bound efrapeptin C was used for crystallization. |


## Crystallization

### doi/10.1073##pnas.93.18.9420

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified F1-ATPase with [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), [ADP](/xray-mp-wiki/reagents/ligands/adp/), and efrapeptin |
| Reservoir | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Crystals grown in the presence of [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), [ADP](/xray-mp-wiki/reagents/ligands/adp/), and efrapeptin. Data collected at the Synchrotron Radiation Source, Daresbury, UK (station 9.6) using a MAR Research image plate detector. Diffraction data processed with MOSFLM and programs from the CCP4 suite. |


## Biological / Functional Insights

### Efrapeptin binding site in the central cavity

Efrapeptin C binds in the central cavity of F1-ATPase, making hydrophobic contacts with the alpha-helical structure in the gamma-subunit that traverses the cavity, with the beta-E subunit, and with the two adjacent alpha-E and alpha-TP subunits. Two potential intermolecular hydrogen bonds can form. The binding site is formed by residues from subunits alpha-E, alpha-TP, beta-E, and gamma. Side chain conformational changes occur at beta-E-Phe326, beta-E-Asp352, beta-E-Asp356, alpha-E-Gln349, alpha-E-Phe351, and alpha-TP-Arg171 upon efrapeptin binding.

### Mechanism of efrapeptin inhibition

Efrapeptin inhibits F1-ATPase by blocking the conversion of the empty beta-E subunit to a nucleotide-binding conformation. In the binding change mechanism, the three beta-subunits alternate through open, loose, and tight conformations during catalysis. Efrapeptin binds at the position in beta-E that would be occupied by strand 3 of the beta-sheet in beta-TP and beta-DP, physically preventing the structural transition required for nucleotide binding. This explains why efrapeptin inhibits both [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis and synthesis.

### Role of alpha-TP-Arg171 in efrapeptin binding

The residue alpha-TP-Arg171 is a key component of the efrapeptin binding site. In the native structure, this arginine (part of the P-loop) forms a salt bridge with beta-DP-Asp356 in the beta-DP and beta-TP subunits, but is exposed in the alpha-TP subunit facing the central cavity. Upon efrapeptin binding, the solvent accessibility of alpha-TP-Arg171 decreases by 55 A^2 (six times more than any other arginine), making it the likely primary site of phenylglyoxal reaction that inactivates F1-ATPase and is prevented by efrapeptin binding.

### Two-domain structure of efrapeptin

Efrapeptin C is a 15-amino acid modified linear peptide with two structural domains (residues 1-6 and 9-15) connected by a flexible region at beta-Ala-7 and Gly-8. Intramolecular hydrogen bonds stabilize each domain. The peptide contains unusual residues including pipecolic acid (Pip), alpha-aminoisobutyric acid (Aib), and beta-alanine, with an acetylated N-terminus and a unique heterocyclic X group (isobutyl[2,3,4,6,7,8-hexahydro- 1-pyrrolo]1,2-alpha[pyrimidinyl]ethylamine) at the C-terminus.

### Relationship to binding change mechanism

The efrapeptin-bound structure provides direct structural support for the binding change mechanism of [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthesis/hydrolysis. Efrapeptin traps the enzyme in a state where beta-E cannot adopt a closed nucleotide-binding conformation. This is consistent with the proposed rotary mechanism where the gamma-subunit rotates relative to the alpha3beta3 hexamer, and the three beta-subunits sequentially adopt open, loose, and tight conformations. The efrapeptin binding site does not overlap with substrate binding sites, explaining why inhibition is non-competitive with [ATP](/xray-mp-wiki/reagents/ligands/atp/) but is affected by phosphate.


## Cross-References

- [Bovine F1-ATPase (azide-inhibited form)](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — Same enzyme in different inhibited states provides complementary structural information
- [Binding-Change Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/binding-change-mechanism/) — Efrapeptin inhibits by blocking the beta-E to closed conformation transition required by the binding change mechanism
- [F1-ATPase Rotary Catalytic Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/) — Structural evidence for the rotary mechanism and its inhibition by efrapeptin
- [Rotary ATPase Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/rotary-atpase-mechanism/) — Efrapeptin inhibits the rotary catalytic cycle by preventing beta-subunit conformational changes
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Referenced in the context of ATP
- [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/) — Referenced in the context of Amp Pnp
- [ADP](/xray-mp-wiki/reagents/ligands/adp/) — Referenced in the context of ADP
