---
title: "BtuCD-BtuF Complex (E. coli Vitamin B12 ABC Transporter)"
created: 2026-06-08
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1071142, doi/10.1126##science.1145950, doi/10.1038##nature11442]
verified: false
---

# BtuCD-BtuF Complex (E. coli Vitamin B12 ABC Transporter)

## Overview

The BtuCD-BtuF complex is the membrane-bound vitamin B12 (cyanocobalamin) ABC transporter from Escherichia coli. The complex consists of two BtuC transmembrane domain (TMD) subunits, two BtuD nucleotide-binding domain (NBD) subunits, and the periplasmic binding protein BtuF. The crystal structure of the BtuCD-BtuF complex revealed striking asymmetry in the TMDs, with the two BtuC subunits adopting different conformations — one resembling the outward-facing state of BtuCD and the other resembling the inward-facing state of HI1471. This asymmetric occluded conformation is thought to represent an intermediate state during the transport cycle.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1145950 | 2QI9 | ~3.2 | — | Full-length BtuC, BtuD, and BtuF from E. coli |  |
| doi/10.1038##nature11442 | 4FI3 | 3.5 | — | BtuCD(EQNC)-F: BtuC wild-type, BtuD(E159Q/N162C), BtuF wild-type. Double mutant with Walker-B E159Q and D-loop N162C mutations engineered for disulphide crosslinking. | AMP-PNP, Mg2+ |

## Expression and Purification

- **Expression system**: E. coli
- **Notes**: Proteins expressed and purified as described in reference.

### Purification Workflow

#### Source: doi/10.1126##science.1145950


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Complex formation | Affinity purification | — |  | BtuCD-F complex assembled and purified as described in original BtuCD and BtuF studies. |

#### Source: doi/10.1038##nature11442

- **Expression system**: E. coli BL21-CodonPlus (DE3)-RIPL
- **Expression construct**: His6-tagged BtuCD(E159Q/N162C) with BtuF
- **Tag info**: His6-tag, Ni-NTA purification

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and expression | Fermentation | — |  | Expression by IPTG induction in BL21-CodonPlus (DE3)-RIPL cells |
| Affinity chromatography | Ni-NTA | Ni-NTA Superflow (Qiagen) | Buffer with 4 mM β-mercaptoethanol (for disulphide-forming mutants) + 0.1% LDAO | All procedures before oxidative crosslinking performed in presence of 4 mM β-mercaptoethanol |
| Disulphide crosslinking | Cu2+-induced crosslinking | — | Buffer with 1 mM CuCl2 + LDAO | Oxidative crosslinking at 22 °C to trap NBD dimer |
| Detergent exchange and SEC | Size-exclusion chromatography | — | C12E8 (octaethylene glycol monododecyl ether) | Post-crosslinking, protein re-bound to Ni-NTA, detergent exchanged to C12E8, then subjected to SEC |

**Final sample**: 18-25 mg/ml in C12E8


## Crystallization

### doi/10.1038##nature11442

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | Crosslinked BtuCD(EQNC)-F complex at 18-25 mg/ml in C12E8 |
| Reservoir | 20-30% PEG 400, 100 mM ADA (N-(2-acetamido)-iminodiacetic acid) pH 6.8, 100 mM sodium potassium citrate |
| Temperature | Not specified (data collected at cryogenic temperature) |
| Cryoprotection | Cryocooled, microdiffractometer setup at X06SA (Swiss Light Source) |
| Notes | X-ray data collected at Swiss Light Source beamline X06SA. Structure determined by molecular replacement using PHENIX and Coot. Data processed with Denzo/Scalepack (HKL Research). |


## Biological / Functional Insights

### Asymmetric conformation of BtuC subunits

The two BtuC subunits in the BtuCD-F complex adopt different conformations. One BtuC subunit (interacting with the C-lobe of BtuF) is similar to the outward-facing BtuCD conformation, while the other BtuC subunit (interacting with the N-lobe of BtuF) resembles the inward-facing HI1471 conformation. This asymmetry is most pronounced in helices TM3, TM4, TM5, and 5a, and is confirmed by CW EPR spectroscopy in proteoliposomes.

### BtuF lobe opening upon complex formation

Upon binding to BtuCD, BtuF undergoes a hinge-like opening of its two lobes by approximately 4 Å, moving the C-lobe away from the B12 binding site. This opening is critical for substrate delivery and is mediated by salt bridges between Arg56 residues from both BtuC subunits and glutamate residues Glu74 and Glu202 from BtuF.

### Intermediate conformation in the ABC transport cycle

The BtuCD-F complex represents a conformation intermediate between the outward-facing (BtuCD) and inward-facing (HI1470/71) states. The central cavity is accessible to neither side of the membrane. This suggests that during the conversion between inward- and outward-facing conformations, BtuC subunits may not alter their conformations simultaneously.

### NBD conformation in the substrate-bound state

The BtuD subunits (NBDs) show a nucleotide-free "open" conformation in the BtuCD-F complex, similar to that observed in the original BtuCD structure. No substantial structural changes are observed in the NBDs upon BtuF binding, suggesting that substrate-induced ATPase stimulation may involve changes in NBD flexibility rather than distinct structural changes.

### Peristaltic transport mechanism of type II ABC importers

The AMP-PNP-bound BtuCD(EQNC)-F structure reveals an unexpected peristaltic transport
mechanism distinct from other ABC transporters. ATP binding closes the NBD sandwich
dimer, pushing coupling helices together, which forces TM5 gating helices outward.
This creates a cytoplasmic gate II that seals the central B12 translocation cavity.
The B12 substrate is trapped in this cavity when ATP is bound. ATP hydrolysis is
required for release into the cytoplasm. Unlike type I importers (MalFGK2), the
type II mechanism involves a transient occlusion cavity rather than a continuous
pathway.

### Cytoplasmic gate II and B12 translocation cavity

The AMP-PNP-bound structure reveals a previously unrecognized cytoplasmic gate II
formed by loops connecting TM4 and TM5 of BtuC. Closure of this gate creates a
central cavity at the BtuC subunit interface, lined by TM3, TM5 and helix H5a.
The cavity volume is sufficient to harbour a B12 molecule. Radioligand trapping
confirmed that liposome-reconstituted BtuCD-F contains bound B12 in the presence
of AMP-PNP. The cavity functions as a low-affinity intermediate translocation
chamber, not a high-affinity binding site.


## Cross-References

- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein structure
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in the study
- [TES Buffer (N-Tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid)](/xray-mp-wiki/reagents/buffers/tes/) — Reagent used in the study
- [2-(N-Morpholino)ethanesulfonic Acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Reagent used in the study
- [Cobalamin (Vitamin B12)](/xray-mp-wiki/reagents/ligands/cobalamin/) — Reagent used in the study
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — Reagent used in the study
