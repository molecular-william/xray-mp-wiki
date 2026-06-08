---
title: LeuT Amino Acid Transporter from Aquifex aeolicus
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature03978, doi/10.1038##nature12179, doi/10.1038##NSMB.2894, doi/10.1038##nature10737, doi/10.1038##nature17629, doi/10.1038##ncomms11673, doi/10.1038##nsmb.1788]
verified: false
---

# LeuT Amino Acid Transporter from Aquifex aeolicus

## Overview

LeuT is a bacterial amino acid transporter from Aquifex aeolicus that belongs to the neurotransmitter/sodium symporter (NSS) family. It was the first crystal structure of an NSS family member, revealing the general architecture of Na+-coupled neurotransmitter transporters. LeuT mediates the Na+-dependent uptake of L-leucine and has served as the primary structural template for understanding the entire NSS family, including human serotonin, dopamine, and GABA transporters.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature03978 | 2A65 | 1.65 A | C2 | LeuT from A. aeolicus, residues 5-133 and 135-513, occluded outward-facing state | L-leucine, Na+ (2 ions), Cl- |
| doi/10.1038##nature12179 | 3TT3 | 2.4 A | not specified | LeuT from A. aeolicus, apo inward-open state | none (apo state) |
| doi/10.1038##nature10737 | not specified | 3.10 A | P2(1)2(1)2(1) | LeuT^K(Y108F) Fab complex, outward-open state | L-leucine, Na+, 2B12 Fab |
| doi/10.1038##nature10737 | not specified | 3.23 A | C222(1) | LeuT^K(TSY)-6A10 Fab complex, inward-open state | Na+ |
| doi/10.1038##nature10737 | not specified | 3.00 A | C2 | LeuT^K(TS)-alanine complex, outward-occluded state | L-alanine, Na+ |
| doi/10.1038##ncomms11673 | 5JAE | 2.50 A | P21 | LeuT from A. aeolicus, outward-oriented Na+- and substrate-free state at pH 6.5, two molecules in asymmetric unit (A and B) | none (Na+- and substrate-free state) |
| doi/10.1038##ncomms11673 | 5JAF | 3.08 A | C2 | LeuT from A. aeolicus, outward-oriented Na+- and substrate-free state at pH 5.0, two molecules in asymmetric unit | none (Na+- and substrate-free state) |
| doi/10.1038##ncomms11673 | 5JAG | 2.58 A | C2 | LeuT T354H mutant from A. aeolicus, outward-oriented Na+- and substrate-free state at pH 6.5 | none (Na+- and substrate-free state) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: LeuT from A. aeolicus, heterologously expressed in C41 cells

### Purification Workflow

*Source: doi/10.1038##nature03978*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell membrane isolation | Cell lysis and membrane fractionation | not applicable | not specified + DDM | Cells cultured in Terrific broth, induced with 0.1 mM IPTG at 20 C for 20 h; membranes isolated from disrupted C41 cells |
| Affinity chromatography | Ni-NTA metal ion affinity chromatography | Ni-NTA | 20 mM Tris-HCl pH 8.0, 190 mM NaCl, 10 mM KCl, 300 mM imidazole, 1 mM DDM + DDM | Membrane solubilized with 40 mM DDM; eluted from Ni-NTA in buffer containing imidazole and DDM |
| Thrombin digestion and SEC | Size exclusion chromatography | Size exclusion column | 20 mM Tris-HCl pH 8.0, 190 mM NaCl, 10 mM KCl, 40 mM beta-OG + beta-OG | After thrombin cleavage of C-terminal His-tag, purified by SEC in beta-OG |

### Purification Workflow

*Source: doi/10.1038##nature12179*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization and purification | Detergent solubilization and affinity chromatography | Ni-NTA affinity resin | not specified + DDM | LeuT purified in DDM detergent |

### Purification Workflow

*Source: doi/10.1038##ncomms11673*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption and membrane isolation | High-pressure homogenization and ultracentrifugation | not applicable | 50 mM Tris-HCl pH 8, 200 mM KCl, 20% glycerol, 1 mM PMSF + not specified | leuT gene expressed in E. coli C41 (DE3) cells; membranes collected by ultracentrifugation at 243,500g for 2 h at 4 C |
| Membrane solubilization | Detergent solubilization | not applicable | 50 mM Tris-HCl pH 8, 200 mM KCl, 20% glycerol + 40 mM n-dodecyl-beta-D-maltoside (DDM) | Membranes incubated with 40 mM DDM for 1 h at 4 C with stirring |
| Ni-NTA affinity chromatography | Ni-NTA metal ion affinity chromatography | Ni-NTA resin (1 ml per 10 mg protein) | 50 mM Tris-HCl pH 8, 200 mM NaCl, 20% glycerol, 10 uM L-leucine, 1 mM, supplemented with 50 mM imidazole for wash and 300 mM imidazole for elution + DDM | His6-tagged LeuT purified on GE Healthcare C column connected to Aka purifier system; eluted in 300 mM imidazole |
| His-tag removal | Thrombin protease digestion | Ni-NTA column (second pass) | 50 mM Tris-HCl pH 8, 200 mM NaCl, 20% glycerol, DDM + DDM | Thrombin protease used to cleave C-terminal His6 tag; flow-through collected after second Ni-column pass |
| Size exclusion chromatography | Size exclusion chromatography | 15 ml KW803 silica column (Shodex) | 10 mM Tris-HCl pH 8, 150 mM NaCl, 0.05% DDM + 0.05% DDM | Protein concentrated to 4 mg/ml using Viva-spin 50 kDa MWCO device before SEC; monodisperse fractions collected |


## Crystallization

### doi/10.1038##nature03978

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | LeuT in 40 mM beta-OG, ~7 mg/ml |
| Reservoir | 0.1 M HEPES-NaOH pH 7.0, 18-22% PEG 550 MME, 0.2 M NaCl |
| Temperature | 18 C |
| Growth time | not specified |
| Notes | Crystals grown by hanging-drop vapor diffusion at 18 C. Cryoprotected with reservoir solution containing 35% PEG 550 MME and 40 mM beta-OG. Space group C2, cell dimensions a=87.9 A, b=86.3 A, c=81.0 A, beta=95.7 degrees. Phased by MAD using SeMet-Labeled protein. |

### doi/10.1038##nature12179

| Parameter | Value |
|---|---|
| Method | detergent crystallization |
| Protein sample | Apo LeuT in detergent |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystal structure of LeuT in substrate-free outward-open and apo inward-open states. PDB 3TT3. |

### doi/10.1038##nature10737

| Parameter | Value |
|---|---|
| Method | detergent crystallization |
| Protein sample | LeuT^K(Y108F) in complex with 2B12 Fab |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | LeuT^K(Y108F)-2B12 Fab complex crystallized at APS-24-ID-E beamline. Space group P2(1)2(1)2(1), cell dimensions 102.9, 162.8, 210.1 A, 90, 90, 90 degrees. Resolution 3.10 A. Used to capture the outward-open conformation. |

| Parameter | Value |
|---|---|
| Method | detergent crystallization |
| Protein sample | LeuT^K(TSY) in complex with 6A10 Fab |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | LeuT^K(TSY)-6A10 Fab complex crystallized at ALS 5.0.2 beamline. Space group C222(1), cell dimensions 128.8, 169.8, 130.4 A, 90, 90, 90 degrees. Resolution 3.23 A. The 6A10 Fab binds the intracellular cavity of the inward-open state, burying 1020 A^2 of surface area. Antiparallel LeuT dimer mediated by TM12 formed in C222(1) crystals. |

| Parameter | Value |
|---|---|
| Method | detergent crystallization |
| Protein sample | LeuT^K(TS) in complex with alanine and sodium |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | LeuT^K(TS)-alanine complex crystallized at ALS 5.0.2 beamline. Space group C2, cell dimensions 89.3, 87.3, 81.7 A, 90, 95.7, 90 degrees. Resolution 3.00 A. Captures the outward-occluded conformation with alanine at the S1 site and Na+ at the Na1 site. |

### doi/10.1038##ncomms11673

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization at acidic pH |
| Protein sample | LeuT from A. aeolicus in 0.05% DDM, purified in Na+-free conditions |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystallization experiments performed at pH 6.5 (PDB 5JAE, 2.50 A, space group P21) and pH 5.0 (PDB 5JAF, 3.08 A, space group C2). Both structures show Leu25 rotated into the substrate-binding pocket and Glu290 buried from extracellular environment. Data collected at DLS I24 beamline. The T354H mutant structure (PDB 5JAG, 2.58 A, space group C2) was also determined at pH 6.5 and adopts the same outward-oriented Na+-free conformation. |


## Biological / Functional Insights

### NSS family structural template

The LeuT crystal structure revealed an inverted pseudo-two-fold symmetry relating two transmembrane domains comprising transmembrane helices (TMs) 1-5 and 6-10. The Na1- and Na2-binding sites as well as the primary substrate-binding site (S1) are situated between the scaffold domain (TM3-TM4 and TM8-TM9) and bundle domain (TM1-TM2 and TM6-TM7). This architecture is conserved across the NSS family including human neurotransmitter transporters.

### Transport cycle conformational states

Available LeuT structures revealed multiple main states of the NSS transport cycle: outward-open with bound Na+, occluded outward-oriented with bound Na+ and L-leucine, and inward-open apo state. The transition between these states provides a structural framework for understanding the alternating access mechanism of NSS transporters.

### Na2 site as essential driver of ion-coupled transport

The Na2 site of LeuT is conserved as a Na+- or H+-binding site in different LeuT-fold transporters, highlighting its central role as the essential driver of ion-coupled transport. The Na1 site coordinates octahedral geometry by side chains of Asn31, Thr231, and Asp263, backbone carbonyls of Ala26 and Thr231, and the substrate carboxyl group.

### Substrate binding site architecture

The L-leucine-occupied S1 site in LeuT provides the structural basis for substrate recognition in NSS transporters. Comparison with MhsT reveals that bulky side chains (Phe259 and Ile359 in LeuT) cannot accommodate larger substrates like L-tryptophan, explaining substrate selectivity differences between NSS family members.

### Unwound transmembrane helices for substrate coordination

The leucine binding site is defined by partially unwound transmembrane helices TM1 and TM6. Main-chain atoms from the unwound regions make most contacts with the alpha-amino and alpha-carboxy groups of bound leucine. The unwinding affords direct hydrogen-bonding partners and allows the charged groups to bind close to the ends of helical segments, exploiting alpha-helix dipole moments. The binding site is completely dehydrated with leucine bound as a zwitterion.

### Sodium ion binding sites and ion selectivity

Two sodium ion binding sites (Na1 and Na2) were identified in the LeuT structure. The Na1 site is coordinated by residues in TM1, TM6, and TM7 and is conserved in eukaryotic NSS members. The Na2 site is coordinated by residues in TM7 and TM8. Sodium binding is required to organize the substrate binding site. The Na1 site is present in all NSS members, while Na2 site conservation varies (e.g., GlyT1b lacks the threonine hydroxyl found in other NSS members).

### Extracellular and intracellular gate architecture

The LeuT structure defines the extracellular and intracellular gates. The extracellular gate is formed by Tyr108, Phe253, and the charged pair Arg30-Asp404. The cytoplasmic gate involves the charged pair Arg5-Asp369. The structure captures an occluded state with both gates closed, defining the three iconic states of the transport cycle: open-to-outside, occluded, and open-to-inside.

### Conformation-specific Fab stabilization of transport states

Two conformation-specific antibody fragments were developed to trap distinct states of the LeT transport cycle. The 2B12 Fab selectively binds the outward-open state, contacting the N-terminus, TM2, TM6-TM7 loop, and IL5, burying 827 A^2 of surface area. The 6A10 Fab selectively binds the inward-open state, with its CDR region inserted into the intracellular cavity, burying 1020 A^2 of surface area and involving residues from IL1, TM4/TM5 loop, TM5, TM6, TM8, TM9, IL5, and TM12. These Fabs enabled the first structures of the outward-open (LeuT^K(Y108F)-2B12, 3.10 A) and inward-open (LeuT^K(TSY)-6A10, 3.23 A) states of LeuT. FSEC analysis confirmed the conformation specificity: 2B12 binds LeuT in the presence of substrate and sodium but not to the inward-open mutant, while 6A10 binds in the absence of substrate and sodium but not with substrate and sodium present.

### Na2 site mutations shift conformational equilibrium

Mutations at the Na2 site (Thr354Val, Ser355Ala) in the LeuT^K(TS) variant weaken substrate binding (Kd = 41.5 uM vs 53.2 nM for LeuT^K) but retain measurable transport activity. The Na2 site mutant shifts the conformational equilibrium away from the outward-open state, as shown by diminished 2B12 Fab binding in the absence of substrate. Adding the Tyr268Ala mutation (LeuT^K(TSY)) further weakens the intracellular gate, producing a variant that binds 6A10 Fab in the absence of substrate but not in its presence, yet is unable to drive sodium-coupled transport. These results demonstrate that the Na2 site is a key driver of conformational equilibrium in the transport cycle.

### TM1 conformational change during transport

TM1 undergoes significant conformational changes during the transition from the outward-occluded to the inward-open state in LeuT. Unlike Mhp1 where TM1 moves as a rigid body, TM1 in LeuT does not move as a rigid body. The unwound region of TM1 is critical for coordinating the Na1 site and substrate. In the inward-open structure, the S2 site is collapsed with no room for leucine binding, explaining why only one substrate binding site is functional in the LeuT transport cycle.

### Leu25 rotation into the empty substrate-binding site

Crystal structures of LeuT in the outward-oriented, Na+- and substrate-free state (PDB 5JAE at pH 6.5 and 5JAF at pH 5.0) reveal that the conserved Leu25 residue of the unwound TM1 region rotates and occupies the empty substrate-binding pocket (S1 site). This rotation was observed in both molecules of the P21 crystal form and in the C2 form. Leu25 overlaps with the position where L-leucine binds in the Na+- and L-leucine-bound occluded state (PDB 2A65). The Na+ binding sites (Na1 and Na2) remain empty and show rearrangements compared to Na+-bound states. Leu25 rotation and Na+ binding are mutually exclusive.

### Glu290 protonation and H+-occluded state

Glu290 is buried from the extracellular environment in the Na+-free return state, with no positive charges to compensate a negatively charged carboxylate. Increased predicted pKa indicates that Glu290 is protonated and neutral, suggesting the structure represents an H+-occluded state of counter-transport. This is consistent with the proposed mechanism where bacterial NSS extrude H+ in return for Na+-dependent amino acid uptake. The Arg30-Asp404 extracellular gate is only semi-closed in this state.

### Leu25 as gatekeeper for Na+ binding

Molecular dynamics simulations (1.2 microseconds total) show that Leu25 remains stably positioned in the S1 site in the Na+-free return state, preventing Na+ ions from accessing the Na1 and Na2 binding sites. Na+ ions interact with extracellular vestibule residues (Asp401, Asp404) but cannot reach the binding sites. When Leu25 is manually rotated out of the S1 site, Na+ enters the central binding sites in simulations, with binding observed at the Na1 site. Leu25 rotation must precede Na+ binding, identifying Leu25 as a gatekeeper for extracellular Na+ binding in the outward-facing return state.

### T354H mutant adopts return state conformation

The LeuT T354H mutant (PDB 5JAG, 2.58 A) was prepared by site-directed mutagenesis and purified in Na+-free conditions. The structure adopts the same outward-oriented Na+-free conformation as the wild-type structures, with Leu25 rotated into the substrate-binding pocket. This mutant was originally used as a starting point for MD simulations and later found to be structurally equivalent to the wild-type return state.


## Cross-References

- [MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans](/xray-mp-wiki/proteins/mhsT/) — NSS family member with 33% sequence identity to LeuT; used for structural comparison
- [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/nss-family/) — LeuT is the NSS family prototype and structural template
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Core transport mechanism revealed by LeuT structures
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for LeuT purification and crystallization
- [n-Octyl-beta-D-glucopyranoside (beta-OG)](/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/) — Detergent used in size exclusion chromatography and crystallization
- [L-Leucine](/xray-mp-wiki/reagents/ligands/l-leucine/) — Endogenous substrate and ligand of LeuT
- [LeuT Return State Mechanism](/xray-mp-wiki/concepts/leut-return-state-mechanism/) — Return state mechanism defined in LeuT structures 5JAE and 5JAF
- [Leu25 Gatekeeper Mechanism in NSS Transporters](/xray-mp-wiki/concepts/leu25-gatekeeper/) — Leu25 serves dual role as substrate-site compensator and Na+ binding gatekeeper
