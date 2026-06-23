---
title: Chloride-Pumping Rhodopsin (ClR) from Nonlabens marinus
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NCOMMS12677]
verified: false
---

# Chloride-Pumping Rhodopsin (ClR) from Nonlabens marinus

## Overview

Chloride-pumping rhodopsin (ClR) from the marine flavobacterium Nonlabens marinus S1-08T is a light-driven inward chloride ion pump containing an NTQ motif (Asn98, Thr102, Gln109) in its ion conduction pathway. It belongs to the NQ family of microbial rhodopsins discovered in marine bacteria, which are evolutionarily distinct from archaeal rhodopsins. Crystal structures determined at 2.0 A and 1.56 A resolution reveal seven transmembrane helices (A-G), an all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore bound via Schiff base to Lys235, and two chloride-binding sites: Cl-I near the protonated Schiff base and Cl-II on the A-B loop at the cytoplasmic surface. The NTQ motif residues Asn98 and Thr102 directly coordinate Cl-I, and the structure includes a C-terminal amphipathic helix important for stability.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NCOMMS12677 | 5G28 | 2.0 | P1 (type A crystal, pH 6.0) | Full-length ClR from N. marinus S1-08T; residues 1-272 | All-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion |
| doi/10.1038##NCOMMS12677 | 5G54 | 1.56 | P1 (type B crystal, pH 4.5) | Full-length ClR from N. marinus S1-08T; residues 1-272 | All-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion |
| doi/10.1038##NCOMMS12677 | 5G2A | 2.0 | P1 (bromide-soaked type A crystal) | Full-length ClR from N. marinus S1-08T | All-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), bromide ion (anomalous map) |
| doi/10.1038##NCOMMS12677 | 5G2D | 2.0 | P1 (T102N mutant crystal) | ClR T102N mutant | All-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion |
| doi/10.1038##NCOMMS12677 | 5G2C | 2.0 | P1 (T102D mutant crystal) | ClR T102D mutant | All-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) (chloride binding prevented) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21-CodonPlus with [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) induction
- **Construct**: Full-length ClR (residues 1-272) expressed with all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) supplementation

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane extraction | Standard membrane protein purification | Ni-NTA affinity | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl + n-Dodecyl-beta-D-maltopyranoside (DDM) 1% | Protein purified by Ni-NTA affinity chromatography and size-exclusion chromatography |


## Crystallization

### doi/10.1038##NCOMMS12677

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (in meso) |
| Protein sample | Purified ClR reconstituted into lipidic cubic phase |
| Temperature | 20 |
| Cryoprotection | Paratone-N or 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Notes | Two crystal forms obtained at different pH values; type A diffracted to 2.0 A, type B to 1.56 A; bromide soaking for anomalous map |


## Biological / Functional Insights

### NTQ motif chloride coordination

ClR contains an NTQ motif (Asn98, Thr102, Gln109) in its ion conduction pathway, distinct from the DTD motif of [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (proton pump) and TSA motif of [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) (chloride pump). Asn98 and Thr102 directly coordinate the chloride ion (Cl-I) at the protonated Schiff base via hydrogen bonds. Mutation of either residue eliminates or substantially reduces chloride pumping activity. The T102N mutant retains ~70% activity but T102D loses all activity by blocking chloride binding.

### Two chloride-binding sites

Two chloride-binding sites were identified: Cl-I at the protonated Schiff base (3.1 A from PSB) and Cl-II on the A-B loop at the cytoplasmic surface, coordinated by Ala44, Pro45, and Lys46. The Cl-II site is not essential for pumping activity (P45A and K46A mutants retain activity). Three internal cavities (IC1, IC2, IC3) suggest a chloride transduction pathway from the extracellular surface to the Schiff base and then to the cytoplasm.

### 3 omega motif

A '3 omega motif' formed by three conserved aromatic residues (Phe15 in TM A, Trp72 in TM B, Tyr83 in B-C loop) through pi-stacking interactions correlates with the B-C loop orientation. Mutating these residues (F15A, W72A, Y83A) reduces protein stability, suggesting a structural role.

### C-terminal helix

ClR has an additional amphipathic C-terminal alpha-helix (residues 255-272) after TM G, reminiscent of helix 8 in eukaryotic GPCRs. This helix interacts with an oleic acid molecule located on TM A. Deletion of the C-terminal helix reduces the melting temperature from 75 degrees C to 61 degrees C, indicating it is important for protein stability.

### Convergent evolution of chloride pumps

Despite having different key residues (NTQ vs TSA motifs), ClR and [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) (HR) both function as light-driven chloride pumps, suggesting convergent evolution. The chloride-binding site at the PSB compensates for the absence of a negatively charged counterion (like Asp85 in BR), an important principle for chloride transport in NTQ rhodopsins.


## Cross-References

- [Bacteriorhodopsin (BR)](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal outward proton pump; comparison of DTD vs NTQ motifs
- [pharaonis Halorhodopsin (phR)](/xray-mp-wiki/proteins/rhodopsins/pharaonis-halorhodopsin/) — Archaeal inward chloride pump with TSA motif; convergent evolution comparison
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Solubilization and purification detergent
- [Lipidic Cubic Phase (In Meso) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for ClR structures
- [Retinal Chromophore Conformation](/xray-mp-wiki/concepts/retinal-chromophore-conformation/) — All-trans retinal is the chromophore in ClR
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Related protein structure
- [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) — Related protein structure
- [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) — Related protein structure
- [pharaonis Halorhodopsin (phR)](/xray-mp-wiki/proteins/rhodopsins/pharaonis-halorhodopsin/) — Related protein structure
