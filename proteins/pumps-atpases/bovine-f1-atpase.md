---
title: Bovine F1-ATPase (azide-inhibited form)
created: 2026-06-08
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0602915103, doi/10.1073##pnas.1506465112, doi/10.1073##pnas.93.14.6913, doi/10.1074##jbc.M700203200]
verified: false
---

# Bovine F1-ATPase (azide-inhibited form)

## Overview

Bovine F1-ATPase is the catalytic domain of the mitochondrial F1Fo-ATP synthase, an enzyme that synthesizes [ATP](/xray-mp-wiki/reagents/ligands/atp/) using the proton motive force across the inner mitochondrial membrane. This structure was determined at 1.95 A resolution from crystals grown in the presence of [ADP](/xray-mp-wiki/reagents/ligands/adp/), [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), and azide. The azide anion binds between the beta-phosphate of [ADP](/xray-mp-wiki/reagents/ligands/adp/) and the catalytically essential residues beta-Lys-162 (P loop) and alpha-Arg-373 (arginine finger) in the ADP-binding catalytic subunit betaDP, occupying a position similar to the gamma-phosphate in the ATP-binding subunit betaTP. Azide binding tightens the interaction of these residues with the nucleotide, stabilizing the ADP-bound state and inhibiting [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis. This mechanism appears to be common to many ATPases including ABC transporters, SecA, and DNA topoisomerase IIalpha.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0602915103 | not stated in raw paper | 1.95 A | P2$_1$2$_1$2$_1$ | Bovine mitochondrial F1-ATPase (alpha3beta3gamma subunit complex) | [ADP](/xray-mp-wiki/reagents/ligands/adp/), [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), azide (N3-) |
| doi/10.1073##pnas.1506465112 |  | 3.1 |  | Bovine F1-ATPase (a3b3gde subunits) with Mg-AMP-PNP and thiophosphate | Mg-AMP-PNP (3 noncatalytic + 2 catalytic sites), thiophosphate (beta-E) |
| doi/10.1073##pnas.1506465112 |  | 3.3 |  | Bovine F1-ATPase with I1-60His-K39A inhibitor (F1-I3-ThioP) | [ATP](/xray-mp-wiki/reagents/ligands/atp/) |
| doi/10.1073##pnas.93.14.6913 |  | 3.1 | P2$_1$2$_1$2$_1$ | Bovine mitochondrial F1-ATPase (alpha3beta3gamma subcomplex) in complex with aurovertin B. | Aurovertin B, [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), [ADP](/xray-mp-wiki/reagents/ligands/adp/) |

## Expression and Purification

- **Expression system**: Bovine heart mitochondria (native source)
- **Construct**: Native F1-ATPase purified from bovine heart mitochondria

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification of F1-ATPase from bovine heart mitochondria | Standard mitochondrial F1-ATPase purification protocol | -- | -- + -- | F1-ATPase was purified from bovine heart mitochondria. The alpha3beta3gamma subcomplex was used for crystallization. |


## Crystallization

### doi/10.1073##pnas.0602915103

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified F1-ATPase with [ADP](/xray-mp-wiki/reagents/ligands/adp/), [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/), and azide |
| Reservoir | -- |
| Mixing ratio | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Crystals grown in the presence of [ADP](/xray-mp-wiki/reagents/ligands/adp/), [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/) (5-adenyl-imidodiphosphate), and azide. Space group P2_1_2_1_2_1. |


## Biological / Functional Insights

### Mechanism of azide inhibition

Azide inhibits [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis by binding between the beta-phosphate of [ADP](/xray-mp-wiki/reagents/ligands/adp/) and the catalytically essential residues beta-Lys-162 (P loop) and alpha-Arg-373 (arginine finger) in the betaDP subunit. This position mimics the gamma-phosphate of [ATP](/xray-mp-wiki/reagents/ligands/atp/). Azide binding tightens the interaction of these residues with the nucleotide, enhancing [ADP](/xray-mp-wiki/reagents/ligands/adp/) affinity and stabilizing the ADP-inhibited state of the enzyme. The refined B factors for azide (<20 A^2) are below those of the bound nucleotide (~30 A^2), indicating very tight binding. This is a unique mechanism of azide inhibition - primarily through hydrogen bonds rather than metal binding.

### ADP inhibition enhancement

The ADP-inhibited state (betaDP conformation) is a natural regulatory state of F1-ATPase that prevents wasteful [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis. Azide stabilizes this state by preventing conversion of the betaDP tight-binding site to the betaE empty conformation. During [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthesis, rotation of the gamma-subunit expels [ADP](/xray-mp-wiki/reagents/ligands/adp/) from this site, so synthesis is not inhibited by either [ADP](/xray-mp-wiki/reagents/ligands/adp/) or azide. This explains the classic observation that azide inhibits [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis but not synthesis by F-ATPases.

### General mechanism for ATPase inhibition by azide

The same mechanism likely applies to many other ATPases inhibited by azide, including ABC transporters, SecA preprotein translocase, DNA topoisomerase IIalpha, and ecto-ATPases. All contain a P loop (Walker A motif) with a lysine residue near the phosphate-binding site. Azide probably enhances the inhibitory effect of [ADP](/xray-mp-wiki/reagents/ligands/adp/) by binding at or near the gamma-phosphate position in all these enzymes. Thiocyanate and cyanate likely have similar mechanisms due to similar shapes and charge distributions.

### Phosphate Release Generates a 25-30 Degree Rotary Substeps

Phosphate release from the beta-E-subunit generates a 25-30 degree rotary substep. In F1-ThioP (pre-phosphate release), thiophosphate is bound at the beta-E catalytic site via interactions with beta-E-R189, beta-E-K162, beta-E-R260, and beta-E-D256. In F1-I3-ThioP (post-release), the binding site is rearranged: beta-E-E188 moves toward the site while beta-E-R189 and beta-E-R260 move away, preventing phosphate rebinding. The gamma-subunit rotates 30 degrees between the two states.

### Loop Extrusion Opens the alpha-E-beta-E Interface

Phosphate release triggers extrusion of the beta-E loop (residues 187-189) toward the alpha-E-subunit. This movement rotates the nucleotide-binding and C-terminal domains of alpha-E by 7 and 11 degrees relative to beta-E, opening the alpha-E-beta-E interface to its fullest extent. Without gamma-subunit rotation, the alpha-E C-terminal domain rotation would remove packing interactions with the gamma-subunit N-terminal helix (residues 18-30), reducing the interaction area from 650 A^2 to 407 A^2.

### Aurovertin B inhibition mechanism

The uncompetitive inhibitor aurovertin B binds to bovine F1-ATPase at two equivalent sites in the betaTP and betaE subunits, in a cleft between the nucleotide binding and C-terminal domains. The binding pocket in betaDP is incomplete and inaccessible due to the closed interface with alphaDP. Aurovertin B interacts mainly via hydrophobic contacts (Leu342, Ile344, Pro350, Leu351) and two hydrogen bonds (Gln411, Arg412) plus a stacking interaction with Tyr458. In betaTP, the pyrone ring also contacts alphaTP-Glu399. Aurovertin acts by preventing closure of the catalytic interfaces, a step essential for the cyclic interconversion of catalytic sites during [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthesis/hydrolysis. The differential affinities for the betaTP (loose) and betaE (empty) sites explain why [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthesis is more sensitive to aurovertin than [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis.


## Cross-References

- [ATP Synthase Mechanism](/xray-mp-wiki/concepts/atp-synthase-mechanism/) — F1-ATPase is the catalytic domain of the F1Fo-ATP synthase, the central enzyme of oxidative phosphorylation
- [ADP Inhibition](/xray-mp-wiki/concepts/adp-inhibition/) — Azide inhibition of F1-ATPase works by enhancing the natural ADP-inhibited state
- [F1-ATPase Rotary Catalytic Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/) — Structural basis of phosphate release generating rotary substep
- [AMP-PNP (Adenylyl Imidodiphosphate)](/xray-mp-wiki/reagents/additives/amp-pnp/) — AMP-PNP used to trap the phosphate release dwell state
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Referenced in the context of ATP
- [ADP](/xray-mp-wiki/reagents/ligands/adp/) — Referenced in the context of ADP
- [Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/) — Referenced in the context of Amp Pnp
