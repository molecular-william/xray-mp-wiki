---
title: Melibiose Permease from Salmonella typhimurium (MelBSt)
created: 2026-06-04
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms4009, doi/10.1038##s42003-021-02462-x]
verified: false
---

# Melibiose Permease from Salmonella typhimurium (MelBSt)

## Overview

[Melibiose](/xray-mp-wiki/reagents/ligands/melibiose) permease (MelB) from Salmonella typhimurium is a Na+-coupled sugar symporter belonging to the glycoside-pentoside-hexuronide:cation symporter family (TC 2.A.2), a subgroup of the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)). MelB catalyzes the electrogenic symport of galactosides coupled to Na+, Li+, or H+, transducing the free energy of downhill cation translocation to drive sugar accumulation against a concentration gradient. The protein shares >85% primary sequence identity with the well-studied E. coli MelB and adopts the typical [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) fold of 12 transmembrane helices organized in two pseudo-symmetrical alpha-helical bundles. Crystal structures in two outward conformations reveal a previously unidentified pyramidal cation-binding site formed by three conserved acidic residues and illuminate the structural basis for Na+/melibiose symport and conformational cycling in [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) transporters.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms4009 | not specified | 3.35 A | P3221 | Full-length MelBSt, Leu5->Met mutation, [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [His10](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag | [2NPG](/xray-mp-wiki/reagents/ligands/2npg) (4-nitrophenyl-alpha-D-galactopyranoside) |
| doi/10.1038##s42003-021-02462-x | 7L17 | 3.05 A | P 31 2 1 | D59C MelB_St mutant with bound alpha-NPG | alpha-NPG (4-nitrophenyl-alpha-D-galactopyranoside) |
| doi/10.1038##s42003-021-02462-x | 7L16 | 3.15 A | P 31 2 1 | D59C MelB_St mutant with bound DDMB (dodecyl-beta-D-melibioside) | DDMB (dodecyl-beta-D-melibioside) |

## Expression and Purification

- **Expression system**: Escherichia coli DW2 strain (melA+, delta melB, delta lacZY)
- **Construct**: Full-length MelBSt with Leu5->Met mutation and [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [His10](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | Fermentation and membrane fractionation | not specified | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 200 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + not specified | Cells grown in LB broth with 50 mM KP(i), 45 mM (NH(4))(H(2)PO(4)), 0.5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 100 mg/L [ampicillin](/xray-mp-wiki/reagents/additives/ampicillin/) at 30 C. Membranes harvested by [ultracentrifugation](/xray-mp-wiki/methods/purification/ultracentrifugation/) at 144,651 g for 3 h. |
| Solubilization | Detergent solubilization | not specified | not specified + 1.5% [UDM](/xray-mp-wiki/reagents/detergents/udm/) ([UDM](/xray-mp-wiki/reagents/detergents/udm)) | Membranes at 14 mg/ml extracted with 1.5% [UDM](/xray-mp-wiki/reagents/detergents/udm) followed by [ultracentrifugation](/xray-mp-wiki/methods/purification/ultracentrifugation/) at 265,000 g for 30 min. |
| Cobalt-[affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) ([Talon](/xray-mp-wiki/reagents/additives/talon/) resins) | [Talon](/xray-mp-wiki/reagents/additives/talon/) resins (cobalt-affinity) | 50 mM NaP(i) pH 7.6, 200 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.035% [UDM](/xray-mp-wiki/reagents/detergents/udm), 5 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.035% [UDM](/xray-mp-wiki/reagents/detergents/udm) | Column pre-equilibrated with buffer containing 5 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/). Wash with 35 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) buffer. Elution with 200 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/). |
| Concentration and dialysis | Concentration and buffer exchange | not specified | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.1, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + not specified | Concentrated with VIVASPIN 20 (50 kDa cutoff), dialyzed twice against 1 L of buffer. |

**Final sample**: MelBSt in 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.1, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/)


## Crystallization

### doi/10.1038##ncomms4009

| Parameter | Value |
|---|---|
| Method | [hanging-drop](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) [vapor diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) |
| Protein sample | Phospholipid-treated MelBSt at 7 mg/ml with 5 mM [2NPG](/xray-mp-wiki/reagents/ligands/2npg) |
| Reservoir | 100 mM [MOPS](/xray-mp-wiki/reagents/buffers/mops/) pH 6.5, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM CaCl2, 35-37% [PEG 400](/xray-mp-wiki/reagents/additives/peg-400/), 0.08% [Octyl-beta-D-galactopyranoside](/xray-mp-wiki/reagents/detergents/octyl-beta-d-galactopyranoside) |
| Temperature | 23 C |
| Growth time | not specified |
| Notes | [hanging-drop](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) [vapor diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) method. Protein mixed 2 ul with 2 ul reservoir. Crystals frozen with liquid nitrogen. Data collected at ALS BL 5.0.2 (wavelength 1.004 A, 100 K). Asymmetric unit contains four molecules (Mol-ABCD) with twinning and pseudo-translation symmetries. Two conformations observed: outward partially occluded (Mol-A/C) and partial outward (Mol-B/D). |


## Biological / Functional Insights

### Pyramidal cation-binding site

Three conserved acidic residues (Asp19, Asp55, Asp59) form a pyramidal-shaped cation-binding site for Na+, Li+, or H+. This site is in close proximity to the sugar-binding site and represents a previously unidentified cation-binding motif. The small ionic radius of Na+ and Li+ requires coordination ligands in closer distance, and metal binding induces relatively large movement of helices. Asp124 is required for completion of the Na+-binding site. Na+ binding recruits Asp124, resulting in movement of helix IV with Tyr120 and Trp128 for aromatic stacking with the bound sugar. Na+ and Li+ are more effective activators than H+.

### Sugar-binding site and aromatic stacking

The sugar-binding site is located mainly in the amino-terminal domain. Asp124, Tyr120, Trp128, and Arg149 contribute to sugar selectivity and affinity. The aromatic residues Trp128 and Tyr120 contribute to affinity by CH/pi-interactions with the pyranosyl ring of the sugar. The [salt bridge](/xray-mp-wiki/concepts/salt-bridge/) between Asp19 and Arg149 is involved in sugar binding. In the Mol-B conformation (inactive state), this [salt bridge](/xray-mp-wiki/concepts/salt-bridge/) is broken and Trp128 is displaced from the cavity, suggesting deformation of the sugar-binding site. Helix IV physically connects both cosubstrate sites.

### Helix IV as a mechanical linker

Helix IV, in the middle of the [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) domain, physically connects both cosubstrate sites (cation and sugar). In addition to Tyr120 and Asp124, Lys18 H-bonds with the backbone atom of Met123, which links helices I-IV. This underscores the crucial role of helix IV in cooperative binding and transport. Na+ binding leads to movement of helix IV, which recruits Asp124, optimizing the pyramidal shape of the cavity with Asp55 and Asp59, and aligning Tyr120 and Trp128 for aromatic stacking with the sugar, thereby increasing affinity. Sugar affinity is increased by more than threefold in the presence of Na+ or Li+.

### Ionic locks and conformational cycling

Three cytoplasmic interdomain ionic locks stabilize the outward-facing conformation. Lock-1 (L-1): Arg295 (helix IX) forms H-bonds with Gln143 (helix V) and Pro287 (helix VIII). Lock-2 (L-2): Arg141 (helix V) forms four H-bonded ion pairs with Asp351 and Asp354 (helix X). Lock-3 (L-3): Arg363 (loop10-11) forms ion pair and two H-bonding interactions with Val204, Asp208, and Gly74, holding the [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) domain in outward-facing conformation. On the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) side, Asp35 (helix I) organizes L-4 by forming a [salt bridge](/xray-mp-wiki/concepts/salt-bridge/) and H-bond with Arg175 (helix VI). Replacing Arg363, Arg141, or Arg295 with Cys yields conformationally compromised mutants that fail to transport but retain affinity. These ionic locks are not present in inward conformers, suggesting a sequential lock formation mechanism for the outward state.

### Sugar specificity determinant pocket from high-resolution D59C structures

Two high-resolution X-ray structures of the D59C MelB_St mutant bound to alpha-NPG (PDB 7L17, 3.05 A) or DDMB (PDB 7L16, 3.15 A) reveal a narrow sugar specificity determinant pocket formed by residues from five transmembrane helices (I, IV, V, X, XI). The galactosyl moiety is recognized through a comprehensive salt-bridge-assisted H-bonding network involving Lys18, Asp19 (helix I), Tyr120, Asp124, Trp128 (helix IV), Arg149 (helix V), Trp342 (helix X), and Thr373, Val376 (helix XI). This explains MelBs specificity for galactosides over glucosides.

### Structural basis for cooperative binding between sugar and cation sites

The conserved cation-binding pocket is proposed to involve Asp55, Asp59, Gly117, Thr121, and Lys377 from helices II, IV, and XI. The C6-OH of the galactosyl ring approaches within 6.9 A of the cation site, providing a direct structural connection. Four out of six cation-site positions are conserved in human MFSD2A, suggesting a common cation-binding mechanism across the GPH family. The close connection between the two specificity determinant pockets provides the structural foundation for the obligatory coupling of this transporter family.

### D59C mutation converts symport to uniport enabling crystallization

The D59C mutation abolishes cation binding and all three modes of cation-coupled melibiose transport (Na+, Li+, H+ symport) while retaining sugar binding and translocation. Asp59 is proposed as the H+-binding residue. This uncoupling made crystallization feasible, yielding reproducible high-quality crystals. The D59C mutant exhibits improved thermostability (Tm = 60 C, 6 C higher than WT) as detected by CD spectroscopy. A transport kinetic model was proposed: an 8-step cycle for symport (WT) and a 6-step cycle for uniport (D59C).

### Alternating access mechanism for Na+/melibiose symport

A sequential binding kinetic model explains reversible cation/melibiose symport based on an alternating-access mechanism. The structural and functional studies integrate conformational states with kinetic steps. [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose) influx down a sugar concentration gradient starts from an intermediate state and proceeds via the outward-facing conformation. Active transport of [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose) against a concentration gradient is driven by the electrochemical gradient of Na+, Li+, or H+. In the absence of sugar, MelB/Na+ complexes preferentially populate outward conformations, preventing bound Na+ from futile cycling. Sugar binding to the cytoplasmic stretch of helix V (Arg141-Arg149) triggers locking/unlocking processes associated with cascade of structural rearrangements for reorientation of the sugar-binding pocket.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — MelB belongs to the glycoside-pentoside-hexuronide:cation symporter family, a subgroup of MFS
- [Conformational Dynamics in MFS Transporters](/xray-mp-wiki/concepts/transport-mechanisms/conformational-dynamics-mfs/) — MelB structures reveal outward partially occluded and outward inactive conformations
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — MelB operates by alternating access between inward- and outward-facing conformations
- [Lactose Permease of Escherichia coli (LacY)](/xray-mp-wiki/proteins/mfs-transporters/lac-y/) — Closely related MFS transporter with similar sugar specificity and location of sugar-recognition sites
- [n-Undecyl-beta-D-maltoside (UDM)](/xray-mp-wiki/reagents/detergents/udm/) — Primary detergent used for MelBSt solubilization during purification
- [Dansyl-galactopyranoside (D2G)](/xray-mp-wiki/reagents/ligands/dansyl-galactopyranoside-d2g/) — Fluorescent galactopyranoside probe used in FRET and binding assays for MelB
- [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose/) — Primary sugar substrate transported by MelB, Kd ~1 mM with Na+ or Li+
- [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) — Entity mentioned in text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Entity mentioned in text
- [vapor diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) — Entity mentioned in text
