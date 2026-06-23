---
title: "Nucleoside Inhibitor Binding to MraY: Chemical Logic and Hotspot Barcode"
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-enzyme-mechanism, concept-functional, membrane-protein, subdirectory-enzyme-mechanisms]
sources: [doi/10.1038##s41467-019-10957-9, doi/10.1126##science.1236501, doi/10.1038##nature17636]
verified: false
---

# Nucleoside Inhibitor Binding to MraY: Chemical Logic and Hotspot Barcode

## Overview
MraY (phospho-MurNAc-pentapeptide translocase) is the target of five
classes of naturally occurring nucleoside antibiotics: liposidomycins/
caprazamycins, capuramycins, mureidomycins, muraymycins, and tunicamycins.
Although all share a common uridine moiety, they differ in core structures
and activity profiles. Crystal structures of Aquifex aeolicus MraY (MraY_AA)
bound to carbacaprazamycin, capuramycin, and 3'-hydroxymureidomycin A,
together with previously reported MraY-muraymycin D2 and MraY-tunicamycin
structures, reveal a barcode system of six druggable hotspots (HS1-HS6)
on the shallow cytoplasmic face of MraY. Each inhibitor class exploits
a unique combination of these hotspots, providing a chemical logic for
understanding and rationally designing MraY-targeted antibiotics.


## Mechanism/Details
The MraY inhibitor binding site is a shallow surface on the cytoplasmic face
formed by transmembrane helices 5, 8, and 9b and Loops C, D, and E. Structural
analysis of five inhibitor-bound MraY complexes revealed six druggable hotspots
(HS):

**HS1 (Uridine pocket):** Common to all five classes. Formed by K70, G194,
L195, D196 in Loop C and F262 in Loop D. The uracil moiety is anchored by
pi-pi stacking with F262 and a hydrogen bond with K70. The ribosyl moiety
provides directionality for each inhibitor to reach other pockets.

**HS2 (Uridine-adjacent pocket):** Formed by T75, N190, D193, G264. The most
chemically diverse hotspot - accommodates 5-aminoribose (carbacaprazamycin,
muraymycin D2), meta-tyrosine (3'-hydroxymureidomycin A), the caprolactam
moiety (capuramycin), or the tunicamine sugar (tunicamycin). This pocket
is a key determinant of selectivity over the eukaryotic MraY paralog GPT,
which lacks an equivalent pocket.

**HS3 (TM9b/Loop E pocket):** Capuramycin does not bind this pocket (Loop E
is disordered in its complex). All other inhibitors interact with TM9b/Loop E
to varying degrees, with 3'-hydroxymureidomycin A and muraymycin D2 making
the most extensive interactions via urea dipeptide motifs.

**HS4 (Hydrophobic groove):** The lipid carrier (C55-P) binding site formed
by TMs 5 and 9b. Targeted by liposidomycins/caprazamycins (aliphatic tails)
and tunicamycin (acyl tail). The acyl moiety of carbacaprazamycin definitively
demonstrated binding to this groove, supporting a competitive inhibition
mechanism with respect to C55-P.

**HS5 (Mg2+ site):** The conserved DDD motif (D117, D118, D265) coordinates
an essential Mg2+ cofactor. 3'-Hydroxymureidomycin A uniquely coordinates
the Mg2+ ion via a carboxylate group, representing a generalizable strategy
for inhibitor design.

**HS6 (Caprolactam pocket - unique to capuramycins):** A superficial groove
formed by K121, L122, and K125. The caprolactam moiety of capuramycin binds
here; shape complementarity is a key affinity determinant. Variability of this
pocket among MraY orthologs could guide narrow-spectrum antibiotic design.

The barcode system can guide rational design of MraY inhibitors. Strategies
include introducing additional pharmacophores to capture more HSs, targeting
HS5 for broader activity, engineering selectivity via HS2, and modifying
the caprolactam moiety of capuramycin/SQ641 for improved activity against
specific pathogens (M. tuberculosis, C. difficile).


## Examples in Membrane Protein Work
- [Aquifex aeolicus MraY](/xray-mp-wiki/proteins/enzymes/aquifex-aeolicus-mray/) — Structural studies of MraY_AA bound to five different nucleoside inhibitors revealed the HS1-HS6 hotspot barcode system
- [Clostridium boltrea MraY](/xray-mp-wiki/proteins/enzymes/clostridium-boltrea-mray/) — MraY from C. boltrea with tunicamycin provided the first MraY-inhibitor complex structure and enabled comparison with the A. aeolicus structures

## Related Concepts
- [PNPT Superfamily](/xray-mp-wiki/concepts/protein-families/pnpt-superfamily/) — MraY is the prototypical member of the PNPT superfamily; the nucleoside inhibitor binding mechanism informs understanding of the entire superfamily
- [Antibiotic Efflux Pump](/xray-mp-wiki/concepts/transport-mechanisms/antibiotic-efflux-pump/) — MraY inhibitors must evade efflux pumps for effective antibacterial activity; some nucleoside inhibitors show activity against drug-resistant strains

## Cross-References
- [Aquifex aeolicus MraY](/xray-mp-wiki/proteins/enzymes/aquifex-aeolicus-mray/) — The structures of MraY_AA bound to three inhibitor classes (PDB 6OYH, 6OYZ, 6OZ6) provide the structural basis for the barcode system
- [PNPT Superfamily](/xray-mp-wiki/concepts/protein-families/pnpt-superfamily/) — The MraY binding hotspot barcode informs PNPT family function and inhibitor specificity
- [Capuramycin](/xray-mp-wiki/reagents/additives/capuramycin/) — Capuramycin uniquely targets HS6 (caprolactam pocket) and does not interact with HS3
- [Muraymycin D2](/xray-mp-wiki/reagents/additives/muraymycin-d2/) — Muraymycin D2 binds HS1, HS2, and HS3; its structure was the first MraY-inhibitor complex from A. aeolicus
- [Tunicamycin](/xray-mp-wiki/reagents/antibiotics/tunicamycin/) — Tunicamycin is the only non-selective inhibitor across MraY/GPT; this is attributed to differences in HS2 between MraY and GPT
