---
title: Noble Gas Anaesthetic Mechanism via Membrane Protein Surface Binding
created: 2026-06-09
updated: 2026-06-09
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-concepts]
sources: [doi/10.1038##s42003-022-03233-y]
verified: false
---

# Noble Gas Anaesthetic Mechanism via Membrane Protein Surface Binding

## Overview
Noble gases (xenon, krypton, argon) are general anaesthetics whose mechanism of action has remained debated for over a century. High-pressure X-ray crystallography of three well-studied membrane proteins — [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (tmBR), the sodium-pumping rhodopsin [KR2 (Krokinobacter eikastus Rhodopsin 2) — Light-Driven Sodium Pump](/xray-mp-wiki/proteins/rhodopsins/kr2/), and the proton-pumping rhodopsin MAR — revealed that krypton and argon atoms bind predominantly to the hydrophobic surface of membrane proteins, occupying sites normally accommodating the acyl chains of annular lipids. Molecular dynamics simulations predicted even more extensive noble gas binding across the protein surface within the bilayer. Noble gas binding suppresses membrane protein dynamics, as shown by both coarse-grained normal mode analysis and all-atom MD, suggesting that anaesthetics act by reducing the conformational dynamics of membrane proteins through non-specific allosteric modulation at the protein-lipid interface.


## Mechanism/Details
The Meyer-Overton rule established a century ago that anaesthetic potency correlates with lipid solubility, but whether the primary target is the lipid bilayer itself or membrane proteins remained unresolved. This study provides structural evidence for a protein-centric mechanism that also explains the Meyer-Overton correlation: noble gases bind to the hydrophobic surface of membrane proteins — the same surface that accommodates annular lipid chains. This protein-lipid interface is the site of action.
Key findings from the crystallographic analysis:
- **tmBR ([Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/))**: 47 argon atoms and 35 krypton atoms were
  identified in derivative structures at 1.65 A and 2.0 A resolution,
  respectively. The vast majority of binding sites were on the outer
  hydrophobic surface. At 11 sites (argon) and 13 sites (krypton), noble gas
  atoms replaced lipid acyl chain fragments, with altered lipid chain
  conformations visible.

- **[KR2 (Krokinobacter eikastus Rhodopsin 2) — Light-Driven Sodium Pump](/xray-mp-wiki/proteins/rhodopsins/kr2/) (Krokinobacter eikastus rhodopsin 2)**: 11 krypton atoms bound at
  2.6 A resolution, predominantly on the surface. Notably, krypton binding
  near helix E caused a ~1 A displacement of the backbone in a pocket
  proximal to the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) beta-ionone ring.

- **MAR (proton-pumping rhodopsin)**: 19 krypton atoms identified at
  2.25 A resolution, with 8 surface site matches in MD simulations.

MD simulations predicted that noble gas atoms massively populate the hydrophobic surface with binding free energies of -16 to -19 kJ/mol, forming contacts lasting 10-100 ns. Normal mode analysis revealed a uniform suppression of protein dynamics upon noble gas binding, more pronounced for tmBR.
This dynamics-inhibition hypothesis unifies several observations: (1) the Meyer-Overton correlation (higher lipid solubility = more surface binding); (2) reversal of anaesthesia by high pressure (pressure enhances conformational dynamics); (3) the lack of a single specific binding site (non-specific surface binding explains why structurally diverse anaesthetics produce similar effects); and (4) the observation that xenon does not affect GABA_A receptors while other anaesthetics do (some target selectivity remains despite the general mechanism).


## Examples in Membrane Protein Work
- **[Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (tmBR)**: 47 argon and 35 krypton binding sites
  identified on the hydrophobic surface; noble gases displace lipid acyl
  chains and suppress dynamics; photocycle kinetics modified.

- **[KR2 (Krokinobacter eikastus Rhodopsin 2) — Light-Driven Sodium Pump](/xray-mp-wiki/proteins/rhodopsins/kr2/) (Krokinobacter eikastus rhodopsin 2)**: 11 krypton sites; helix E
  displaced ~1 A near retinal-binding pocket; no noble gas atoms in central
  cavities.

- **MAR (proton-pumping rhodopsin)**: 19 krypton sites; 8 of 8 surface
  sites reproduced in MD.


## Related Concepts
- Force-from-lipid principle (contrasting lipid-mediated mechanism)
- Allosteric regulation in membrane proteins
- Protein-lipid interactions
- Dynamics suppression as a mechanism of action
- Lipidic cubic phase crystallization (method used for in meso crystals)


## Cross-References
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Model membrane protein system used in high-pressure noble gas derivatization study
- [KR2 — Light-Driven Sodium Pump](/xray-mp-wiki/proteins/rhodopsins/kr2/) — Model membrane protein used in high-pressure noble gas derivatization study
- [Force-from-Lipid Principle in Mechanosensation](/xray-mp-wiki/concepts/force-from-lipid-principle/) — Related concept involving lipid-protein interactions in membrane protein gating
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/allosteric-regulation/) — Noble gas binding represents a form of allosteric modulation at the protein-lipid interface
- [Selective Lipid Binding in Membrane Protein](/xray-mp-wiki/concepts/selective-lipid-binding/) — Related concept of lipid-protein interactions on MP surface
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Related ligand or cofactor
