---
title: "De Novo Design of Transmembrane Pores"
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-structural-mechanisms]
sources: [doi/10.1038##s41586-020-2646-5]
verified: regex
---

# De Novo Design of Transmembrane Pores

## Overview
De novo design of transmembrane pores involves the computational design and
experimental validation of protein pores that span the lipid bilayer. The
approach uses parametric coiled-coil parameterization to generate backbone
geometries, Rosetta HBNet for hydrogen-bond network design, and combinatorial
sequence optimization to create stable, well-defined homo-oligomeric helical
bundles with central pores. The method was demonstrated with two designs: a
12-helix hexameric pore (TMHC6) that functions as a K+-selective ion channel,
and a 16-helix tetrameric pore (TMH4C4) large enough to transport small-molecule
fluorophores (~1 kDa). Crystal structures of the water-soluble forms (WSHC6 at
2.4 A, PDB 6TJ1 and 6TMS; WSHC8 at 2.4 A, PDB 6O35) closely matched the design
models, and a [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of TMH4C4 (5.9 A, PDB 6M6Z, EMD-30126) confirmed
the transmembrane 16-helix assembly. This work represents a major advance in
membrane protein engineering, laying the foundation for designer channels and
pores for biotechnological applications.


## Mechanism/Details
The design strategy uses a two-ring concentric helix architecture to overcome
the thermodynamic challenges of creating large transmembrane pores. Key design
elements include:
- Homo-oligomeric assembly of identical subunits, each containing 2-4 helices
  bridged by short loops
- Coiled-coil parametrization for backbone generation, sampling helical and
  superhelical parameters
- Hydrogen-bond networks across intermolecular interfaces designed via Rosetta
  HBNet for stability
- Charged residue rings (glutamate E-ring, lysine K-rings) at pore entrances
  to create polar entry/exit points, inspired by the Orai calcium channel
- For the transmembrane form, lipid-exposed residues are redesigned for
  membrane compatibility while preserving the soluble-form packing

For the 12-helix TMHC6 pore:
- C6-symmetric hexameric assembly (6 subunits x 2 helices each)
- Narrowest constriction ~3.3 A (E44 ring) enabling K+/Na+ selectivity
- K+ conductance blocked by Cd2+ and MTS reagents at the pore entrance
- Patch-clamp electrophysiology in insect cells showed K+ selectivity over
  Na+, Cs+, and Ba2+

For the 16-helix TMH4C4 pore:
- C4-symmetric tetrameric assembly (4 subunits x 4 helices each)
- Larger pore (~10 A constriction) allowing transport of ~1 kDa fluorophores
- Functional in liposomes via in vitro protein synthesis
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure confirmed 16-helix assembly with central pore


## Examples in Membrane Protein Work
- TMHC6 (12-helix Transmembrane Pore) — 
- TMH4C4 (16-helix Transmembrane Pore) — 

## Related Concepts


## Cross-References
- [Pore-Forming Toxins](/xray-mp-wiki/concepts/structural-mechanisms/pore-forming-toxins/) — Natural pore-forming proteins provide inspiration for designed transmembrane pore architectures
- [Cryo-Electron Microscopy (Cryo-EM)](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Cryo-EM was used to determine the TMH4C4 structure at 5.9 A resolution
- [Proteoliposome Reconstitution](/xray-mp-wiki/methods/quality-assessment/proteoliposome-reconstitution/) — Liposome-based assays were used to demonstrate TMH4C4 fluorophore transport
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Nickel-affinity chromatography was used to purify all designed pore proteins
- [Size-Exclusion Chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC was used for purification and monodispersity assessment of all pore constructs
- [Circular Dichroism (CD) Spectroscopy](/xray-mp-wiki/methods/quality-assessment/circular-dichroism-spectroscopy/) — CD spectroscopy confirmed the designed proteins are alpha-helical and thermally stable
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Method used in structure determination or purification
