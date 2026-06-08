---
title: GltPh (Glutamate Transporter Homologue from Pyrococcus horikoshii)
created: 2026-06-02
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature05455, doi/10.1038##nature14158, doi/10.1038##ncomms13420, doi/10.1038##nsmb.2233]
verified: false
---

# GltPh (Glutamate Transporter Homologue from Pyrococcus horikoshii)

## Overview

GltPh is a sodium-coupled aspartate transporter from the archaeon Pyrococcus horikoshii. It is a homologue of mammalian excitatory amino acid transporters (EAATs) in the SLC1A family. GltPh functions as a homotrimer, with each protomer containing eight transmembrane segments, two re-entrant helical hairpins (HP1 and HP2), and an asymmetric transport mechanism. The protein couples aspartate transport to the co-transport of sodium ions, and has been instrumental in defining the structural basis of sodium-coupled substrate transport and the extracellular gate mechanism in secondary transporters.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature05455 | not specified in paper | not specified in paper | not specified in paper | His8-tagged wild-type GltPh | TBOA (DL-threo-beta-benzyloxyaspartate) |
| doi/10.1038##nature05455 | not specified in paper | not specified in paper | not specified in paper | His8-tagged wild-type GltPh | L-aspartate |
| doi/10.1038##nature05455 | not specified in paper | not specified in paper | not specified in paper | His8-tagged wild-type GltPh | none (apo state) |
| doi/10.1038##nature05455 | not specified in paper | not specified in paper | not specified in paper | GltPh D405N mutant, His8-tagged | L-aspartate |
| doi/10.1038##nsmb.2233 | not specified in paper | not specified in paper | not specified in paper | GltPh V198C A380C_Hg cross-linked mutant (Hg-mediated intramolecular cross-link) | L-aspartate, Na+ |
| doi/10.1038##nsmb.2233 | not specified in paper | not specified in paper | not specified in paper | GltPh Y195C A364C_Hg cross-linked mutant | L-aspartate, Na+ |
| doi/10.1038##nsmb.2233 | not specified in paper | not specified in paper | not specified in paper | GltPh V216C M385C_Hg cross-linked mutant | L-aspartate, Na+ |

## Expression and Purification

- **Expression system**: Escherichia coli (E. coli)
- **Construct**: His8 fusion protein (wild-type and D405N mutant)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Ni-NTA affinity chromatography | His8-tag affinity purification using TALON or Ni-NTA resin with imidazole gradient elution | Ni-NTA or TALON | Not specified (standard His-tag purification) + 1 mM n-dodecyl-beta-D-maltopyranoside (DDM) | Purified as described in Yernool et al. (2004) |
| Size-exclusion chromatography / dialysis | Concentrated and dialysed against HEPES/Tris buffer | SEC column | 200 mM choline chloride, 1 mM NaCl, 1 mM DDM, HEPES/Tris pH 7.4 + 1 mM DDM | Final buffer for assays and crystallization |


## Crystallization

### doi/10.1038##nature05455

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | GltPh in complex with TBOA |
| Reservoir | Not specified in paper |
| Temperature | Not specified in paper |
| Growth time | Not specified in paper |
| Cryoprotection | Not specified in paper |
| Notes | TBOA-bound structure; HP2 in open conformation |

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | GltPh co-crystallized with L-aspartate |
| Reservoir | Not specified in paper |
| Temperature | Not specified in paper |
| Growth time | Not specified in paper |
| Cryoprotection | Crystallization buffer supplemented with 10% glycerol |
| Notes | Aspartate-bound structure; HP2 in closed conformation |

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Substrate-depleted GltPh (apo state) |
| Reservoir | Not specified in paper |
| Temperature | Not specified in paper |
| Growth time | Not specified in paper |
| Cryoprotection | Not specified in paper |
| Notes | Apo structure; HP2 predominantly in open conformation |


## Biological / Functional Insights

### Extracellular gate (HP2) controls substrate access

HP2 (helical hairpin 2) acts as the extracellular gate controlling access of substrate and ions to the internal binding sites. In the TBOA-bound state, HP2 adopts an open conformation, moving up to 10 A from its position in the aspartate-bound complex towards the 3L4 loop. The bulky benzyl group of TBOA lodges against the tip of HP2, propping it in an open conformation and preventing gate closure. In the apo state, HP2 predominantly occupies an open conformation, rendering the substrate-binding site accessible to extracellular solution. Closure of HP2, as seen in the aspartate-bound state, creates a crevice between HP2, the 3L4 loop and TM4a.

### Sodium-dependent substrate binding with two sodium sites

Aspartate binding to GltPh is sodium-dependent. Fluorescence binding assays and isothermal titration calorimetry (ITC) revealed that aspartate binds with Kd of approximately 1 nM for L-aspartate and 10 nM for D-aspartate in 200 mM NaCl. Sodium titrations yielded Hill coefficients of about 2, suggesting coupled binding of at least two sodium ions. Two sodium-binding sites were identified by anomalous difference Fourier maps from crystals soaked in Tl+ (a sodium analogue). Sodium site 1 is located below aspartate, closer to the cytoplasm, while sodium site 2 is above aspartate, nearer to the extracellular solution. Site 2 functions as a lock on the HP2 gate, providing additional energy for its closure.

### Unwound alpha-helix in TM7 as sodium-binding motif

The sodium-binding sites in GltPh share structural similarity with those in LeuT (PDB 2A65). The unwound region of TM7 (NMDGT motif) in GltPh and TM1 in LeuT define an unwound alpha-helix as the central element of the ion-binding motif. This motif is well suited to sodium binding and participates in conformational changes during the transport cycle. TM8 in GltPh fits into a groove created by the unwound portions of TM7. Sodium site 1 is defined by coordinating carbonyl oxygen atoms, and sodium site 2 is coordinated by an equivalently positioned carbonyl oxygen atom.

### D405N mutation weakens sodium binding at site 1

The D405N mutation, which replaces a conserved aspartate with asparagine (found in some bacterial proton-dependent transporters), weakened Tl+ binding at sodium site 1 while preserving binding at site 2. The mutation diminished aspartate binding about 100-fold (Kd approximately 100 nM in 200 mM NaCl). Sodium dependence for aspartate and TBOA binding was decreased, suggesting that sodium site 1 binding is only partly coupled to substrate binding and that a third sodium site may exist that is resistant to Tl+ substitution.

### Substrate binding site architecture

Aspartate is completely buried within a polar chamber located halfway across the membrane bilayer, formed by the tips of HP1 and HP2, the unwound region of TM7 (NMDGT motif), and polar residues of amphipathic TM8. Key interactions involve the alpha-amino and carboxylate groups of aspartate with R276 (HP1), V355 (HP2), and D394/N401 (TM8), as well as the beta-carboxylate with T314 (TM7), G359 (HP2), and R397 (TM8). The D394 carboxylate group coordinates sodium site 1.

### State-dependent lipid binding pocket

In the crevice between HP2, the 3L4 loop, and TM4a formed upon HP2 closure, an elongated electron density feature was modelled as the alkyl chain of a lipid molecule. This state-dependent lipid binding pocket may exist in eukaryotic transporters and could provide sites for lipid binding and modulation of transporter activity.

### Transport cycle conformational states

The structures of GltPh and LeuT indicate that the reaction cycle of these secondary transporters involves at least three states: open to the outside, occluded, and open to the inside. In the transport cycle, sodium ions bind to sites 1 and 2 together with aspartate binding to the substrate site, inducing closure of HP2. TBOA inhibits transport by blocking HP2 in an open conformation, preventing sodium from binding to site 2 and halting further conformational changes. Sodium site 2 serves as a gate-keeper for HP2 closure.

### Asymmetric trimer captures intermediate outward-facing state (iOFS)

The V198C A380C_Hg cross-linked mutant of GltPh forms an asymmetric trimer with two protomers in the inward-facing state (IFS) and one protomer in an intermediate outward-facing state (iOFS). The iOFS protomer has moved approximately 3.5 A toward the cytoplasm and rotated approximately 15 degrees relative to the outward-facing state (OFS). This rearrangement corresponds to one-fourth of the complete translation and one-half of the complete rotation of the transport domain transitioning from OFS to IFS. The iOFS is a relatively low-energy, accessible state stabilized by crystal-packing contacts.

### Interfacial cavity in iOFS accessible to both solutions

In the iOFS, a cavity forms at the domain interface lined by conserved hydrophobic residues in TM2 and TM5 of the trimerization domain. The cavity is flanked on the cytoplasmic side by Ser65 and Tyr195, which are exposed to the cytoplasm and potentially accessible to the extracellular solvent through the interfacial cavity. Ser65 has been implicated in anion permeation in EAATs and is thought to be part of the selectivity filter. In the OFS and IFS, these residues are occluded from at least one solution.

### Structural principle for uncoupled permeation of polar solutes

The iOFS structure demonstrates how potentially solvent-accessible cavities may form in glutamate transporters during transport, possibly accounting for their reported sodium- and substrate-gated permeability to a range of polar solutes including water, urea, and anions. Such cavities may either yield a conducting channel or harbor binding sites with alternate accessibility to extracellular and intracellular solutions. Multiple transitions between OFS and IFS before substrate release could account for nonstoichiometric transport of these solutes.

### Hydrophobic crevice at domain interface

The transition from OFS to iOFS involves substantial widening of the crevice between the transport and trimerization domains. Helices TM1, TM2, and TM5 of the trimerization domain lean away from the trimer center by up to 7.0 A to accommodate rearrangement of the TM5-TM6 loop. This exposes part of the interface to the membrane core, potentially allowing lipophilic molecules to enter and stabilize intermediate states. EAATs are modulated by polyunsaturated fatty acids, consistent with this mechanism.


## Cross-References

- [TBOA (DL-threo-beta-benzyloxyaspartic acid)](/xray-mp-wiki/reagents/ligands/tboa/) — Competitive inhibitor that binds substrate site and props HP2 gate open; IC50 = 3.3 uM
- [GltTk (Glutamate Transporter Homologue from Thermococcus kodakarensis)](/xray-mp-wiki/proteins/glt-tk/) — Related glutamate transporter homologue; similar elevator mechanism and inhibitor binding
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut/) — Sodium-coupled amino acid transporter with structurally similar sodium-binding motif in unwound helix
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM used at 1 mM for GltPh purification and crystallization
- [Sodium Ion](/xray-mp-wiki/reagents/ligands/sodium-ion/) — Two sodium-binding sites identified in GltPh structure; essential for aspartate binding
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — GltPh operates through open-outside, occluded, and open-inside conformational states
- [Rocker-Switch Mechanism in MFS Transporters](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — Related transport mechanism concept; GltPh uses a distinct but analogous mechanism
- [Potassium Chloride (KCl)](/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/) — Potassium used in transport assays; K+ does not support aspartate binding to GltPh
- [H276,395-GltPh (Humanized GltPh Mutant, R276S/M395R)](/xray-mp-wiki/proteins/h276395-glt-ph/) — Humanized mutant variant with 1000-fold decreased substrate affinity and fourfold faster uptake rate
- [Elevator Mechanism](/xray-mp-wiki/concepts/elevator-mechanism/) — GltPh transport domain undergoes elevator-like motion across the membrane bilayer
