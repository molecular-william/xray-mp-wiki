---
title: "GltPh (Glutamate Transporter Homologue from Pyrococcus horikoshii)"
created: 2026-06-02
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature03018, doi/10.1038##nature05455, doi/10.1038##nature08616, doi/10.1038##nature14158, doi/10.1038##ncomms13420, doi/10.1038##nsmb.2233, doi/10.1038##nsmb.2548, doi/10.1038##s41586-021-03240-9, doi/10.1126##sciadv.aba9854, doi/10.15252##embj.2020105415, doi/10.7554##eLife.02283]
verified: false
---

# GltPh (Glutamate Transporter Homologue from Pyrococcus horikoshii)

## Overview

GltPh is a sodium-coupled aspartate transporter from the archaeon Pyrococcus horikoshii. It is a homologue of mammalian excitatory amino acid transporters (EAATs) in the SLC1A family. GltPh functions as a homotrimer, with each protomer containing eight transmembrane segments, two re-entrant helical hairpins (HP1 and HP2), and an asymmetric transport mechanism. The protein couples aspartate transport to the co-transport of sodium ions, and has been instrumental in defining the structural basis of sodium-coupled substrate transport and the extracellular gate mechanism in secondary transporters. A combined bioinformatics, single-molecule FRET, and linear free energy relationship (LFER) analysis revealed that the high-energy transition state (TS) for the rate-limiting elevator movement from outward-facing to inward-facing state structurally resembles the inward-facing conformation. Gain-of-function mutations in HP2 (A345V, V366A) and the scaffold TM5 kink (Y204L) increased the transport rate up to 20-fold by accelerating the OFS-to-IFS transition.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature03018 | 2NWX | 3.5 | P3121 | His8-tagged GltPh H7 (C-terminal truncation) | L-aspartate (putative) |
| doi/10.1038##nature05455 | 2NWL | not specified in paper | not specified in paper | GltPh D405N mutant, His8-tagged | L-aspartate |
| doi/10.1038##nsmb.2233 | 3V8F | not specified in paper | not specified in paper | GltPh V216C M385C_Hg cross-linked mutant | L-aspartate, Na+ |
| doi/10.1038##nature08616 | 3KBC | 3.5 | C2221 | GltPh K55C/A364C double cysteine mutant, Hg-cross-linked, inward-facing state (IFS) | L-aspartate, Na+ |
| doi/10.15252##embj.2020105415 | 6V8G | 3.38 | P3121 | GltPh Y204L/A345V/V366A triple mutant, His8-tagged |  |
| doi/10.1038##s41586-021-03240-9 | 6X01 | 3.65 | P6₁ | CLGltPh V216C/A391C double-cysteine mutant (cysteine-less background), His6-tagged, thrombin-cleaved, Hg-crosslinked |  |
| doi/10.1038##s41586-021-03240-9 | 6WZB | 3.45 | C222₁ | CLGltPh L152C/G351C double-cysteine mutant (cysteine-less background), His6-tagged, thrombin-cleaved, Hg-crosslinked |  |
| doi/10.1038##s41586-021-03240-9 | 6WYJ | 3.7 | C1 | CLGltPh L152C/G351C (XL2) reconstituted into nanodiscs (MSP1E3 scaffold) |  |
| doi/10.1038##s41586-021-03240-9 | 6WYK | 4.0 | C1 | CLGltPh L152C/G351C (XL2) reconstituted into nanodiscs |  |
| doi/10.1038##s41586-021-03240-9 | 6WYL | 3.9 | C3 | CLGltPh L152C/G351C (XL2) reconstituted into nanodiscs |  |
| doi/10.7554##eLife.02283 | 4OYE | 3.25 | C2221 | GltPh-R397A (H7 mutant background), His8-tagged, thrombin-cleaved | none (apo state) |
| doi/10.7554##eLife.02283 | 4OYF | 3.75 | C2221 | GltPh-R397A (H7 mutant background), His8-tagged, thrombin-cleaved | Na+ (Na1 site occupied) |
| doi/10.7554##eLife.02283 | 4OYG | 4.0 | C2221 | GltPh-R397A (H7 mutant background), His8-tagged, thrombin-cleaved | Na+, L-aspartate |
| doi/10.7554##eLife.02283 | 4P19 | 3.5 | C2221 | GltPh-K55C/A364C (GltPh_in), Hg-crosslinked | Tl+ (apo-like conformation at Na2' and Ct sites) |
| doi/10.7554##eLife.02283 | 4P1A | 4.15 | C2221 | GltPh-K55C/A364C (GltPh_in), Hg-crosslinked | Tl+ (Na1 and Na2 sites occupied, bound conformation) |
| doi/10.7554##eLife.02283 | 4P3J | 3.5 | C2221 | GltPh-K55C/A364C (GltPh_in), Hg-crosslinked, alkali-free | none (alkali-free) |
| doi/10.7554##eLife.02283 | 4P6H | 5.0 | P21 | GltPh-K55C/A364C (GltPh_in), Hg-crosslinked | Tl+ (Na1 and Na2 sites occupied, bound conformation) |
| doi/10.1126##sciadv.aba9854 | 7AHK | 2.5 | P321 | Wild-type GltPh | Na+ (Na1 and Na3 sites occupied), phosphate (cocrystallized) |
| doi/10.1126##sciadv.aba9854 | 2NWW |  |  | Wild-type GltPh | [TBOA](/xray-mp-wiki/reagents/ligands/tboa/), Na+ (Na1 site) |

## Expression and Purification

- **Expression system**: Escherichia coli (E. coli)
- **Construct**: His8 fusion protein (wild-type and D405N mutant)

### Purification Workflow

#### Source: doi/10.1038##nature05455


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| [Ni-NTA Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/)-tag affinity purification using [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon) or [Ni-NTA Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) resin with [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient elution | [Ni-NTA Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) or [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon) | Not specified (standard [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) purification) + 1 mM [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) ([n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/)) | Purified as described in Yernool et al. (2004) |
| [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) / dialysis | Concentrated and dialysed against HEPES/Tris buffer | [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) column | 200 mM [Choline](/xray-mp-wiki/reagents/ligands/choline) chloride, 1 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/), 1 mM [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), HEPES/Tris pH 7.4 + 1 mM [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) | Final buffer for assays and crystallization |

#### Source: doi/10.1038##s41586-021-03240-9

- **Expression system**: Escherichia coli Top10
- **Expression construct**: CLGltPh (cysteine-less), His6-tagged at C-terminus, thrombin-cleavable
- **Tag info**: His6-tag, removed by thrombin digestion (10 U per mg protein)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and expression | LB culture with 100 ug/ml ampicillin, induced with 0.1% L-arabinose at OD600 0.6-0.8 | -- | LB medium | 4 h post-induction at 37 C |
| Membrane isolation and solubilization | Ultracentrifugation and detergent solubilization | -- | 20 mM HEPES-Tris pH 7.5, 200 mM NaCl, 5 mM Na-Asp + 10 mM n-dodecyl-beta-D-maltoside (C12M, Anatrace) | 1 h solubilization at 4 C |
| Ni-NTA affinity chromatography | Immobilized metal affinity chromatography | Ni-NTA resin (Qiagen) | 20 mM HEPES-Tris pH 7.5, 200 mM NaCl, 5 mM Na-Asp + -- (after solubilization) | His-tag removed by thrombin digestion after elution |
| Size-exclusion chromatography | SEC polishing | Superdex200 16/60 HiLoad (GE Healthcare) | For XL1 and wild-type: 20 mM HEPES-Tris pH 7.5, 25 mM NaCl, 25 mM KCl, 5 mM Na-Asp + 7 mM n-decyl-beta-D-maltopyranoside (C10M, Anatrace) | For XL2 and XL3: SEC buffer 10 mM HEPES-KOH/NaOH pH 7.5, 100 mM NaCl, 0.1 mM Na-Asp + 7 mM C10M. Concentrated to 6-7 mg/ml. |

**Final sample**: 6-7 mg/ml in SEC buffer with C10M


## Crystallization

### doi/10.1038##nature05455

| Parameter | Value |
|---|---|
| Method | Hanging-drop [Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) |
| Protein sample | GltPh in complex with [TBOA](/xray-mp-wiki/reagents/ligands/tboa/) |
| Reservoir | Not specified in paper |
| Temperature | Not specified in paper |
| Growth time | Not specified in paper |
| Cryoprotection | Not specified in paper |
| Notes | [TBOA](/xray-mp-wiki/reagents/ligands/tboa/)-bound structure; HP2 in open conformation |

| Parameter | Value |
|---|---|
| Method | Hanging-drop [Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) |
| Protein sample | GltPh co-crystallized with [L-Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) |
| Reservoir | Not specified in paper |
| Temperature | Not specified in paper |
| Growth time | Not specified in paper |
| Cryoprotection | Crystallization buffer supplemented with 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Notes | Aspartate-bound structure; HP2 in closed conformation |

| Parameter | Value |
|---|---|
| Method | Hanging-drop [Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) |
| Protein sample | Substrate-depleted GltPh (apo state) |
| Reservoir | Not specified in paper |
| Temperature | Not specified in paper |
| Growth time | Not specified in paper |
| Cryoprotection | Not specified in paper |
| Notes | Apo structure; HP2 predominantly in open conformation |

### doi/10.1038##s41586-021-03240-9

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | GltPh-XL1 (V216C/A391C) in SEC buffer with 7 mM C10M |
| Reservoir | Not specified in paper (crystallized via sitting-drop vapor diffusion) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystal structure of crosslinked GltPh-XL1 determined at 3.65 A. Similar to OFS (PDB 2NWX) with Calpha RMSD 0.5 A. Space group P6₁. |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | GltPh-XL3 (L152C/G351C) in SEC buffer with 7 mM C10M |
| Reservoir | Not specified in paper |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystal structure of crosslinked GltPh-XL3 determined at 3.45 A. Similar to IFS (PDB 3KBC) with Calpha RMSD 0.6 A. Space group C222₁. |

| Parameter | Value |
|---|---|
| Method | Cryo-EM single-particle analysis (nanodisc reconstitution) |
| Protein sample | GltPh-XL2 (L152C/G351C) reconstituted into MSP1E3 nanodiscs with POPE:POPG:POPC (2:1:1) lipids |
| Reservoir | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Cryo-EM structures of GltPh-XL2 in iOFS (3.7 A, 105,135 particles) and CICS (4.0 A, 98,093 particles). Data collected at 200 kV on 150,000x magnification. 40 e-/A2 electron exposure. Pixel size 0.986 A. |


## Biological / Functional Insights

### Extracellular gate (HP2) controls substrate access

HP2 (helical hairpin 2) acts as the extracellular gate controlling access of substrate and ions to the internal binding sites. In the [TBOA](/xray-mp-wiki/reagents/ligands/tboa/)-bound state, HP2 adopts an open conformation, moving up to 10 A from its position in the aspartate-bound complex towards the 3L4 loop. The bulky benzyl group of [TBOA](/xray-mp-wiki/reagents/ligands/tboa/) lodges against the tip of HP2, propping it in an open conformation and preventing gate closure. In the apo state, HP2 predominantly occupies an open conformation, rendering the substrate-binding site accessible to extracellular solution. Closure of HP2, as seen in the aspartate-bound state, creates a crevice between HP2, the 3L4 loop and TM4a.

### Sodium-dependent substrate binding with two sodium sites

Aspartate binding to GltPh is sodium-dependent. Fluorescence binding assays and isothermal titration calorimetry (ITC) revealed that aspartate binds with Kd of approximately 1 nM for [L-Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) and 10 nM for D-aspartate in 200 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/). Sodium titrations yielded Hill coefficients of about 2, suggesting coupled binding of at least two sodium ions. Two sodium-binding sites were identified by anomalous difference Fourier maps from crystals soaked in Tl+ (a sodium analogue). Sodium site 1 is located below aspartate, closer to the cytoplasm, while sodium site 2 is above aspartate, nearer to the extracellular solution. Site 2 functions as a lock on the HP2 gate, providing additional energy for its closure.

### Binding thermodynamics of coupled Na+/Asp transport revealed by ITC

Isothermal titration calorimetry (ITC) using conformationally trapped GltPh mutants GltPh^out (L66C/S300C, outward-facing) and GltPh^in (K55C/A364C, inward-facing) provided a complete thermodynamic characterization of coupled Na+/aspartate binding. Three sodium ions bind cooperatively per aspartate molecule, with Hill coefficients of 1.6-1.8 for Na+ binding. The binding free energy (ΔG) of 3Na+/Asp coupling was approximately -10.5 kcal/mol for GltPh^out and -10.1 kcal/mol for GltPh^in. Large negative heat capacity changes (ΔCp) of -300 to -500 cal/mol·K were observed, consistent with significant conformational rearrangements accompanying coupled binding. TBA (tetrapentylammonium) binds competitively with aspartate (KD 3.8 uM for GltPh^out, 1.5 uM for GltPh^in). The potent inhibitor DL-TBOA binds with KD of 2.6 uM (GltPh^out) and 16 uM (GltPh^in), with ΔCp of -148 and -334 cal/mol·K respectively.

### Unwound alpha-helix in TM7 as sodium-binding motif

The sodium-binding sites in GltPh share structural similarity with those in [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut) (PDB 2A65). The unwound region of TM7 (NMDGT motif) in GltPh and TM1 in [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut) define an unwound alpha-helix as the central element of the ion-binding motif. This motif is well suited to sodium binding and participates in conformational changes during the transport cycle. TM8 in GltPh fits into a groove created by the unwound portions of TM7. Sodium site 1 is defined by coordinating carbonyl oxygen atoms, and sodium site 2 is coordinated by an equivalently positioned carbonyl oxygen atom.

### D405N mutation weakens sodium binding at site 1

The D405N mutation, which replaces a conserved aspartate with asparagine (found in some bacterial proton-dependent transporters), weakened Tl+ binding at sodium site 1 while preserving binding at site 2. The mutation diminished aspartate binding about 100-fold (Kd approximately 100 nM in 200 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/)). Sodium dependence for aspartate and [TBOA](/xray-mp-wiki/reagents/ligands/tboa/) binding was decreased, suggesting that sodium site 1 binding is only partly coupled to substrate binding and that a third sodium site may exist that is resistant to Tl+ substitution.

### Substrate binding site architecture

Aspartate is completely buried within a polar chamber located halfway across the membrane bilayer, formed by the tips of HP1 and HP2, the unwound region of TM7 (NMDGT motif), and polar residues of amphipathic TM8. Key interactions involve the alpha-amino and carboxylate groups of aspartate with R276 (HP1), V355 (HP2), and D394/N401 (TM8), as well as the beta-carboxylate with T314 (TM7), G359 (HP2), and R397 (TM8). The D394 carboxylate group coordinates sodium site 1.

### State-dependent lipid binding pocket

In the crevice between HP2, the 3L4 loop, and TM4a formed upon HP2 closure, an elongated electron density feature was modelled as the alkyl chain of a lipid molecule. This state-dependent lipid binding pocket may exist in eukaryotic transporters and could provide sites for lipid binding and modulation of transporter activity.

### Transport cycle conformational states

The structures of GltPh and [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut) indicate that the reaction cycle of these secondary transporters involves at least three states: open to the outside, occluded, and open to the inside. In the transport cycle, sodium ions bind to sites 1 and 2 together with aspartate binding to the substrate site, inducing closure of HP2. [TBOA](/xray-mp-wiki/reagents/ligands/tboa/) inhibits transport by blocking HP2 in an open conformation, preventing sodium from binding to site 2 and halting further conformational changes. Sodium site 2 serves as a gate-keeper for HP2 closure.

### Asymmetric trimer captures intermediate outward-facing state (iOFS)

The V198C A380C_Hg cross-linked mutant of GltPh forms an asymmetric trimer with two protomers in the inward-facing state (IFS) and one protomer in an intermediate outward-facing state (iOFS). The iOFS protomer has moved approximately 3.5 A toward the cytoplasm and rotated approximately 15 degrees relative to the outward-facing state (OFS). This rearrangement corresponds to one-fourth of the complete translation and one-half of the complete rotation of the transport domain transitioning from OFS to IFS. The iOFS is a relatively low-energy, accessible state stabilized by crystal-packing contacts.

### Interfacial cavity in iOFS accessible to both solutions

In the iOFS, a cavity forms at the domain interface lined by conserved hydrophobic residues in TM2 and TM5 of the trimerization domain. The cavity is flanked on the cytoplasmic side by Ser65 and Tyr195, which are exposed to the cytoplasm and potentially accessible to the extracellular solvent through the interfacial cavity. Ser65 has been implicated in anion permeation in EAATs and is thought to be part of the selectivity filter. In the OFS and IFS, these residues are occluded from at least one solution.

### Structural principle for uncoupled permeation of polar solutes

The iOFS structure demonstrates how potentially solvent-accessible cavities may form in glutamate transporters during transport, possibly accounting for their reported sodium- and substrate-gated permeability to a range of polar solutes including water, [Urea](/xray-mp-wiki/reagents/substrates/urea), and anions. Such cavities may either yield a conducting channel or harbor binding sites with alternate accessibility to extracellular and intracellular solutions. Multiple transitions between OFS and IFS before substrate release could account for nonstoichiometric transport of these solutes.

### Hydrophobic crevice at domain interface

The transition from OFS to iOFS involves substantial widening of the crevice between the transport and trimerization domains. Helices TM1, TM2, and TM5 of the trimerization domain lean away from the trimer center by up to 7.0 A to accommodate rearrangement of the TM5-TM6 loop. This exposes part of the interface to the membrane core, potentially allowing lipophilic molecules to enter and stabilize intermediate states. EAATs are modulated by polyunsaturated fatty acids, consistent with this mechanism.

### Gain-of-function mutations in HP2 accelerate transport up to 20-fold

Bioinformatics analysis of 20,000 prokaryotic GltPh homologues from organisms at different growth temperatures identified thermophile-to-psychrophile transition mutations. Subtle packing mutations in HP2 (A345V, A345S, M362V, V366A) increased the transport rate at least 4-fold by accelerating the OFS-to-IFS elevator transition and reducing L-Asp affinity (increased KM). The Y204L mutation in the TM5 kink of the scaffold domain also boosted activity. Combining Y204L, A345V, V366A, and K290A mutations produced the fastest variant with 20-fold increased uptake rate and ~1 s mean turnover time. The K290A mutation disrupts a salt bridge with E192 in the OFS, increasing transport domain dynamics.

### LFER analysis shows transition state structurally resembles the IFS

Linear free energy relationship (LFER) analysis of GltPh mutants revealed that the high-energy transition state for the rate-limiting OFS-to-IFS elevator movement structurally resembles the inward-facing conformation (IFS). Mutations at HP1 (K290A, R276S/M395R) shifted the equilibrium toward IFS with Leffler alpha values of 0.90-0.92, indicating the salt bridge and HP1 interactions are already broken in the TS. Mutations at HP2 (A345, M362, V366) and TM5 (Y204) affected both forward and reverse rates, indicating TS stabilization distinct from both end states. Under apo conditions, Leffler alpha values were 0.5-0.7, suggesting the TS is more central in the absence of substrate.

### Kinetic heterogeneity and static disorder in GltPh dynamics

Single-molecule FRET recordings revealed striking kinetic heterogeneity in GltPh transport domain dynamics, with OFS dwell times ranging from <1 s to hundreds of seconds. Individual molecules showed intrinsically homogeneous dynamics (single-exponential dwell-time distributions) but the population exhibited broad transition frequency distributions spanning two orders of magnitude, indicative of static disorder (persistent kinetic states). A minor fraction (5-20%) showed switching between dynamic modes. The most prevalent mode across all variants was long OFS (10-100 s) and short IFS (0.5-2 s) lifetimes. These multiple kinetic modes parallel the multiple transport activity modes observed in single-molecule transport assays.

### Rationale for allosteric modulator development

Based on the finding that the transition state resembles the IFS, a strategy for developing small-molecule allosteric modulators of transporters was proposed. Ligands binding at the domain interface with higher affinity for IFS than OFS would also bind tighter to the TS, reducing the energy barrier and acting as positive allosteric modulators (PAMs). Conversely, molecules binding tighter to the OFS would increase the barrier and act as negative allosteric modulators (NAMs). This framework rationalizes the action of recently developed EAAT2 PAMs (Kortagere et al., 2018; Falcucci et al., 2019) that bind preferentially to the domain interface in the OFS, and predicts that chemically related compounds can act as either activators or inhibitors depending on their conformational selectivity.

### Cross-linking captures inward-facing state and demonstrates elevator mechanism

The GltPh K55C/A364C double-cysteine mutant was designed to form an intramolecular cross-link between TM2 (residue 55) and HP2 (residue 364), residues that are proximal in the outward-facing state (OFS) but distant in the inward-facing state (IFS). Oxidative cross-linking with CuPhen produced a disulfide bond that trapped the transport domain in the IFS, as confirmed by limited proteolysis and SDS-PAGE. The crystal structure of the Hg-cross-linked variant at 3.5 A resolution (space group C2221) provided the first direct visualization of the IFS of GltPh, showing that the transport domain moves ~16-18 A across the membrane relative to the trimerization domain. This established the elevator mechanism as the basis for substrate transport in glutamate transporter homologues and demonstrated that cross-linking can capture otherwise transient conformational states for structural analysis. The strategy was subsequently used by Verdon and Boudker (2012, NSMB) to capture additional intermediate states.

### CICS (chloride ion-conducting state) reveals uncoupled Cl- channel with two hydrophobic gates

The cryo-EM structure of GltPh-XL2 (L152C/G351C) trapped in the CICS at 4.0 A resolution (PDB 6WYK) revealed an aqueous cavity formed at the interface of the transport and scaffold domains during the glutamate transport cycle. The cavity is continuous and accessible to both extracellular and cytoplasmic solutions, forming a Cl- permeation pathway gated by two hydrophobic regions. Molecular dynamics simulations (1.2 us umbrella sampling) showed that hydrophobic residues V12, I16, F50, V51, M202, A205, and L212 provide energy barriers (~1.9 kcal/mol) against Cl- movement, while basic residues R276, R52, and K55 create energy minima for Cl- interaction. The narrowest pore diameter is ~5 A (Hole), sufficient to accommodate dehydrated thiocyanate (largest permeant anion). S65 at the domain interface plays a key role in anion permeation. In EAAT1, mutation of equivalent hydrophobic residues to alanine (F50A, T54A, L88A, M89A, M286A, L269A) shifted the reversal potential to more hyperpolarized potentials (increased Cl- conductance), while A289F essentially eliminated Cl- contribution to net conductance. These findings demonstrate that the Cl- channel in glutamate transporters is gated by hydrophobic residues at both the extracellular and intracellular ends of the permeation pathway.

### Apo transport domain adopts compact occluded conformation

The apo transport domain in both outward- and inward-facing states is nearly identical and as compact as the fully bound form. The domain traverses the membrane as a rigid body when unloaded. In the apo state, HP2 and the NMD motif collapse: Asn310 rotates to partially fill the empty Na1 site, Met311 flips away from binding sites, and TM3 bends away from the NMD motif. All ligand-binding sites are distorted in the apo form.

### Na+-mediated HP2 gate opening prevents uncoupled Na+ transport

Binding of Na+ at the Na1 site triggers isomerization of the transport domain into a bound-like conformation with straightened TM3, Met311 reoriented toward binding sites, and HP2 adopting an open tip conformation hinged at conserved glycines G351 and G357. This opening impedes inward translocation of Na+-only bound transport domain, preventing uncoupled Na+ uptake. HP2 tip opening is mediated by five conserved glycine residues (G351-G359 consensus) that provide structural flexibility across the glutamate transporter family.

### Met311 couples Na+ and substrate binding through allosteric mechanism

Met311 in the NMD motif is the only residue shared between the Na1, Na2, and substrate binding sites. Structural modeling shows that the conformations of HP2 and the NMD motif are coupled: Met311 clashes with HP2 when one is in apo and the other in bound conformation. M311A mutation substantially reduces coupling between Na+ and L-asp binding, while M311L preserves coupling. This demonstrates that bulky methionine residues at this position (conserved in ~85% of homologues) mediate allosteric coupling between the Na1, L-asp, and Na2 sites.

### Ct site as candidate K+ counter-transport binding site

Two novel cation binding sites (Na2' and Ct) were identified in the apo-like conformation. The Ct site overlaps with the L-asp binding site, coordinated by D394, T398, R276, V355, and P356. Binding at Ct and substrate binding are mutually exclusive. The Ct site is observed in both inward- and outward-facing states, suggesting the apo transport domain could carry a cation across the membrane. In EAATs, K+ likely binds at an analogous Ct site to stabilize the translocation-competent apo state for return to the extracellular side, establishing the structural basis for K+ counter-transport in mammalian glutamate transporters.


## Cross-References

- [TBOA (DL-threo-beta-benzyloxyaspartic acid)](/xray-mp-wiki/reagents/ligands/tboa/) — Competitive inhibitor that binds substrate site and props HP2 gate open; IC50 = 3.3 uM
- [GltTk (Glutamate Transporter Homologue from Thermococcus kodakarensis)](/xray-mp-wiki/proteins/slc-transporters/glt-tk/) — Related glutamate transporter homologue; similar elevator mechanism and inhibitor binding
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/) — Sodium-coupled amino acid transporter with structurally similar sodium-binding motif in unwound helix
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM used at 1 mM for GltPh purification and crystallization
- [Sodium Ion](/xray-mp-wiki/reagents/ligands/sodium-ion/) — Two sodium-binding sites identified in GltPh structure; essential for aspartate binding
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — GltPh operates through open-outside, occluded, and open-inside conformational states
- [Rocker-Switch Mechanism in MFS Transporters](/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/) — Related transport mechanism concept; GltPh uses a distinct but analogous mechanism
- [Potassium Chloride (KCl)](/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/) — Potassium used in transport assays; K+ does not support aspartate binding to GltPh
- [H276,395-GltPh (Humanized GltPh Mutant, R276S/M395R)](/xray-mp-wiki/proteins/slc-transporters/h276395-glt-ph/) — Humanized mutant variant with 1000-fold decreased substrate affinity and fourfold faster uptake rate; characterized in transition state study
- [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) — GltPh transport domain undergoes elevator-like motion across the membrane bilayer
- [Human Excitatory Amino Acid Transporter 1 (EAAT1)](/xray-mp-wiki/proteins/slc-transporters/eaat1/) — GltPh is the prokaryotic homolog of human EAATs and shares the same elevator transport mechanism
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Used as the LCP matrix for GltPh crystallization
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in gltph text
- [TBOA](/xray-mp-wiki/reagents/ligands/tboa/) — Referenced in gltph text
