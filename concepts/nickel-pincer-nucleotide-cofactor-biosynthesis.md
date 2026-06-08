---
title: Nickel-Pincer Nucleotide Cofactor Biosynthesis
created: 2026-05-29
updated: 2026-05-29
type: concept
category: concepts
layout: default
tags: [concept-protein-family, subdirectory-concepts]
sources: [doi/10.1021##acs.biochem.3c00242]
verified: false
---

# Nickel-Pincer Nucleotide Cofactor Biosynthesis

## Overview

The nickel-pincer nucleotide (NPN) cofactor biosynthesis pathway is a multi-step enzymatic
process that produces a unique nickel-containing cofactor required by a large family of
lactate racemases and epimerases. The pathway was first characterized in
[Lactiplantibacillus plantarum](/xray-mp-wiki/proteins/larB/), where the NPN cofactor is
covalently attached to a lysyl side chain in the active site of lactate racemase. The pathway
involves three dedicated enzymes (LarB, LarE, and LarC) that sequentially modify nucleotide
substrates to produce the final nickel-pincer cofactor.

## Mechanism/Details

The NPN biosynthesis pathway proceeds through the following steps:

1. **LarB-catalyzed carboxylation and hydrolysis**: LarB initiates the pathway by carboxylating
   nicotinic acid adenine dinucleotide (NaAD) at the C5 position of the pyridinium ring and
   hydrolyzing the phosphoanhydride bond, producing pyridinium-3,5-biscarboxylic acid
   mononucleotide (P2CMN) and AMP. The revised mechanism involves a Cys221-Glu180 catalytic
   dyad and a CO2 binding site coordinated by Arg159 and Mg2+.

2. **LarE-dependent sulfur insertion**: LarE activates each carboxyl group of P2CMN by
   adenyllylation (using ATP) and inserts sulfur atoms to release AMP and form
   pyridinium-3,5-bisthiocarboxylic acid mononucleotide (P2TMN). LarE is a [4Fe-4S]-dependent
   sulfur insertase of the N-type ATP pyrophosphatase family.

3. **LarC-catalyzed cytidinylation and nickel insertion**: LarC catalyzes the cytidinylation
   of P2TMN (releasing pyrophosphate), inserts nickel, and then hydrolyzes the phosphoanhydride
   to produce the final NPN cofactor and CMP.

The NPN cofactor then incorporates into its target enzyme, where it becomes covalently attached
to a lysyl side chain in a thioamide linkage. The cofactor contains a nickel-carbon bond, which
is unusual in biological systems.

## Examples in Membrane Protein Work

- [LarB](/xray-mp-wiki/proteins/larB/) from *Lactiplantibacillus plantarum* catalyzes the first
  step of NPN biosynthesis and has been structurally characterized with its substrate NaAD and
  the substrate analogue NAD+
- [Lactate racemase](/xray-mp-wiki/proteins/lactate-racemase/) from *L. plantarum* incorporates
  the NPN cofactor covalently into its active site (PDB: 5HUQ)

## Related Concepts

- Nickel-pincer nucleotide cofactor
- Cys221-Glu180 catalytic dyad
- Metal-carbon bond enzymes

## Cross-References

- [LarB](/xray-mp-wiki/proteins/larB/) — Enzyme that initiates NPN biosynthesis pathway
- [NaAD](/xray-mp-wiki/reagents/cofactors/nicotinic-acid-adenine-dinucleotide/) — Substrate for the first step of NPN biosynthesis
