---
title: ABC Transporter Substrate Specificity
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-functional, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.2006526117, doi/10.1073##pnas.1311407110]
verified: false
---

# ABC Transporter Substrate Specificity

## Overview
Substrate specificity in ABC transporters is not determined solely by
the periplasmic binding protein (or substrate-binding protein). Instead,
the transmembrane domains also contribute to selectivity, forming a
multi-tiered specificity filter. This concept is best exemplified by the
E. coli maltose transport system, where both [MBP](/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/)
and [MalFGK2](/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/) contribute
to the overall substrate selectivity.


## Mechanism/Details
In the maltose transport system, substrate specificity is achieved through three components:

**1. Outer membrane channel (maltoporin):** Allows nonspecific permeation of ions and monosaccharides. For larger molecules, maltoporin preferentially conducts maltodextrin over other oligosaccharides via a "greasy slide" of aromatic residues that bind g2-g4 glucosyl units.

**2. Periplasmic binding protein (MBP):** Binds linear malto-oligosaccharides (maltose to maltoheptaose) with high affinity through 14 direct hydrogen bonds and extensive van der Waals interactions. Four stacking aromatic residues form a continuous surface matching the left-handed helix of malto-oligosaccharides. However, MBP's affinity alone does not fully account for transport selectivity — some maltose analogs bind MBP tightly but are not transported.

**3. Inner membrane transporter (MalFGK2):** Provides additional specificity through two mechanisms:
   - In the pretranslocation state, the MalG scoop loop (Q256) hydrogen bonds to the reducing end glucosyl unit, restricting modifications at the reducing end.
   - In the outward-facing state, MalF binds three glucosyl units from the nonreducing end via aromatic stacking (F435, F436) and hydrogen bonds (S433, Y325), conferring specificity for the alpha-1,4 linkage.

The substrate-binding cavity (~2,400 A3) in the pretranslocation state limits substrate size to approximately seven glucosyl units. Larger malto-oligosaccharides that bind MBP cannot stimulate ATPase activity because they hinder MBP-MalFGK2 interactions.

## Examples in Membrane Protein Work
- [Maltose Transporter MalFGK2 (E. coli)](/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/) — ABC importer where both MBP and TM domains contribute to specificity

## Related Concepts
- [ABC Transporter Family](/xray-mp-wiki/concepts/abc-transporter-family/) — Parent family; this concept describes a specific functional aspect of ABC transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — The transport mechanism by which ABC transporters move substrates across the membrane

## Cross-References
- [Maltose Transporter MalFGK2 (E. coli)](/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/) — Primary system illustrating this concept
- [MBP (Escherichia coli Maltose-Binding Protein)](/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/) — Periplasmic binding protein that contributes to specificity
- [ABC Transporter Family](/xray-mp-wiki/concepts/abc-transporter-family/) — Parent family of ATP-binding cassette transporters
