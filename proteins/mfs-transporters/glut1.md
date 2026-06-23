---
title: Human Glucose Transporter GLUT1 (SLC2A1)
created: 2026-06-03
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13306, doi/10.1073##pnas.1603735113, doi/10.26508##lsa.202000858]
verified: false
---

# Human Glucose Transporter GLUT1 (SLC2A1)

## Overview

The human [Glucose](/xray-mp-wiki/reagents/additives/glucose) transporter GLUT1 (encoded by SLC2A1) catalyses facilitative diffusion of [Glucose](/xray-mp-wiki/reagents/additives/glucose) into erythrocytes and is responsible for [Glucose](/xray-mp-wiki/reagents/additives/glucose) supply to the brain and other organs. Dysfunctional mutations lead to GLUT1 deficiency syndrome (De Vivo syndrome), characterised by early-onset seizures, microcephaly and retarded development. Over-expression of GLUT1 is a prognostic indicator for cancer. GLUT1 belongs to the sugar porter subfamily of the [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) ([Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/)) and has a canonical [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) fold with 12 transmembrane segments organised into amino- and carboxy-terminal domains. The crystal structure was determined at 3.2 A resolution in an inward-open conformation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13306 | unknown | 3.2 | C2 | Full-length human GLUT1, residues 1-492, N45T and E329Q mutations, C-terminal 10x His tag | n-Nonyl-beta-D-glucopyranoside (beta-NG) |
| doi/10.1073##pnas.1603735113 |  | 3.0 | — | Full-length WT hGLUT1 (residues 1-455), C-terminal 10x His tag | cytochalasin B |
| doi/10.1073##pnas.1603735113 |  | 2.9 | — | Full-length WT hGLUT1 (residues 1-455), C-terminal 10x His tag | GLUT-i1 |
| doi/10.1073##pnas.1603735113 |  | 3.0 | — | Full-length WT hGLUT1 (residues 1-455), C-terminal 10x His tag | GLUT-i2 |
| doi/10.26508##lsa.202000858 | 6THA | 2.4 | C2 | Human GLUT1 residues 9-455 (of 492 total), C-terminal 10x His tag, expressed in S. cerevisiae | n-Nonyl-beta-D-glucopyranoside (NG), chloride ion (Cl-), PEG molecule |

## Expression and Purification

- **Expression system**: High Five insect cells (baculovirus); Saccharomyces cerevisiae
- **Construct**: Full-length human GLUT1, residues 1-492, C-terminal 10x His tag
- **Notes**: Two expression systems used: (1) High Five insect cells via baculovirus, N45T/E329Q mutations, 48h post-infection. (2) S. cerevisiae, WT protein with no mutations, not glycosylated at N45.

### Purification Workflow

*Source: doi/10.1038##nature13306*

- **Expression system**: High Five insect cells ([Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/))
- **Expression construct**: Full-length human GLUT1, residues 1-492, C-terminal 10x [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/)
- **Tag info**: 10x [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/), C-terminal

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Dounce homogenization | — | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) | 80 cycles on ice |
| Membrane preparation | Ultracentrifugation | — | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) | 150,000g for 1 h; membrane fraction harvested |
| Membrane solubilization | Detergent solubilization | -- | TBS (25 mM [Tris (Hydroxymethyl) Aminomethane](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/)) + 2% (w/v) [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) | 2 h at 4 C with protease inhibitors (aprotinin 0.8 uM, pepstatin 2 uM, leupeptin 5 ug/ml) |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Ni-NTA Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Ni-NTA Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) (Qiagen) | 25 mM [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) pH 6.0, 150 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/), 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) + 0.05% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) | 30 min at 4 C; elute with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200) (GE Healthcare) | 25 mM [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) pH 6.0, 150 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.4% beta-NG + 0.4% beta-NG | Concentrated to 10 mg/ml before [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) |

**Final sample**: 10 mg/ml in 25 mM [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) pH 6.0, 150 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.4% beta-NG

### Purification Workflow

*Source: doi/10.1073##pnas.1603735113*

- **Expression system**: Saccharomyces cerevisiae
- **Expression construct**: Full-length WT hGLUT1 (residues 1-504), C-terminal 10x His tag
- **Tag info**: 10x His tag, C-terminal, thrombin-cleavable

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity chromatography | Ni-NTA | Ni-NTA (GE Biosciences, 1 mL column) | not specified + n-dodecyl-beta-D-maltopyranoside (beta-DDM) | Protein was not glycosylated at N45 despite known glycosylation site |


## Crystallization

### doi/10.1038##nature13306

| Parameter | Value |
|---|---|
| Method | Hanging-drop [Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) |
| Protein sample | GLUT1 (N45T, E329Q) purified in 0.4% beta-NG |
| Reservoir | 30% (w/v) [PEG 400](/xray-mp-wiki/reagents/additives/peg-400/), 0.1 M [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) pH 6.0, 0.1 M [Magnesium Chloride (MgCl2)](/xray-mp-wiki/reagents/additives/magnesium-chloride/) |
| Temperature | 4 C |

### doi/10.1073##pnas.1603735113

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | WT-hGLUT1 with inhibitor (cytochalasin B, GLUT-i1, or GLUT-i2) |
| Notes | Structures determined by molecular replacement using 4PYP (apo-hGLUT1) as search model; all three inhibitor complexes crystallized isomorphously |

### doi/10.26508##lsa.202000858

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, hanging drop |
| Protein sample | 5 mg/ml GLUT1 in G-buffer (20 mM MES pH 6.5, 250 mM NaCl, 10% glycerol, 0.2% NG, 0.02% CHS, 0.5 mM TCEP, 40 mM D-glucose) |
| Reservoir | 42-46% PEG 400, 100-200 mM MgCl2, 100 mM Mops pH 7.4 |
| Temperature | 17 |
| Growth time | 1-3 days |
| Cryoprotection | none needed (PEG 400 at 42-46% acts as cryoprotectant) |
| Notes | Cubic crystals ~100 x 100 x 100 um. Space group C2. Anomalous experiments to confirm Cl- site used MgBr2 instead of MgCl2 in reservoir. Data collected from single crystals at Diamond Light Source. |


## Biological / Functional Insights

### Inward-open conformation with beta-NG bound

The full-length human GLUT1 structure was captured in an inward-open conformation. A beta-NG molecule binds in the inward-open cavity, with its D-glucopyranoside moiety positioned at the C domain of GLUT1 at approximately the centre of the membrane, while the aliphatic tail points to the intracellular side. The sugar moiety is hydrogen-bonded to polar residues in the C domain including Gln 282/Gln 283/Asn 288 from TM7, Asn 317 from TM8, and Asn 415 from TM11. The similar coordination of D-glucopyranoside by inward-open GLUT1 and D-[Glucose](/xray-mp-wiki/reagents/additives/glucose) by outward-facing [XylE (Escherichia coli Sugar Transporter)](/xray-mp-wiki/proteins/xyle) supports the notion of a single sugar-binding site alternately accessible from either side of the membrane.

### Alternating access mechanism via N/C domain rotation

Structural comparison of inward-open GLUT1 and outward-facing [XylE (Escherichia coli Sugar Transporter)](/xray-mp-wiki/proteins/xyle) reveals an approximately 16 degree concentric rotation of the N and C domains. The C domain provides the primary substrate-binding site while the relative motion of the N domain results in [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/). In the inward-open GLUT1, residues from the N domain are not involved in ligand binding. The ligand-free protein may prefer an outward-open conformation; substrate binding at the primary site on the C domain induces closure of N and C domains on the extracellular side, leading to rearrangement of interactions on both sides of the bound substrate.

### Disease-related mutations in three clusters

Disease-derived mutations from GLUT1 deficiency syndrome map to three clusters: Cluster I comprises substrate-binding residues; Cluster II is located at the interface between the transmembrane domain and the ICH domain; Cluster III comprises residues lining the transport path, mostly committed to interactions between the N and C domains on the extracellular side. Mutations affecting Asn 34, Ser 66, Arg 126, Glu 146, Gly 130, Arg 223, Lys 256, Ala 275, Tyr 292, Ser 294, Thr 295, Val 303, Thr 310, Gly 314, Asn 317, Ser 324, Asp 329, and Asn 45 have been identified from patients.

### ICH domain as intracellular gate latch

The intracellular helix (ICH) domain represents a unique feature of the sugar porter subfamily and functions as a latch to secure closure of the intracellular gate in the outward-facing conformation. The ICH domain forms hydrogen bonds from the backbone amide groups of Gly 154 and Lys 155, stabilized by charge-stabilized hydrogen bonds between Asp 329 and Arg 333. Disease-related mutations in this interface (E329Q) are predicted to weaken these interactions, favouring the inward-facing conformation and impeding the transport cycle.

### Extracellular gate structure

In the inward-open conformation, TM1 and TM7 contact each other on the extracellular side, forming the major constituents of the extracellular gate. Asn 34 on TM1 appears to be an organizing centre mediating hydrogen bonds to Ser 294 and Thr 295 on TM7 and Thr 310 on TM8. Arg 126 on TM4 may form a cation-pi interaction with Tyr 292 on TM7 of the C domain, contributing to the affinity of the extracellular gate. TM7 of GLUT1 contains one extra kink close to its extracellular end compared to outward-facing [XylE (Escherichia coli Sugar Transporter)](/xray-mp-wiki/proteins/xyle).

### Comparison of uniporter GLUT1 with proton symporter XylE

Structural comparison of the proton-independent uniporter GLUT1 and its bacterial homologue [XylE (Escherichia coli Sugar Transporter)](/xray-mp-wiki/proteins/xyle) (a proton-coupled xylose symporter), obtained in distinct conformations, allows mechanistic analysis of facilitative diffusion versus active transport. In [XylE (Escherichia coli Sugar Transporter)](/xray-mp-wiki/proteins/xyle), Asp 27 is critical for proton coupling; this residue corresponds to Asn 29 in GLUT1. The structure of GLUT1 provides an opportunity to understand the protonated state of proton symporters. Uniporters catalyse substrate translocation down its concentration gradient, while proton symporters exploit the transmembrane proton gradient to drive uphill translocation.

### Inhibitor-bound structures of WT-hGLUT1 with distinct chemical classes

Three inhibitor-bound crystal structures of WT (no mutations) hGLUT1 were determined in complex with cytochalasin B (3.0 A), GLUT-i1 (2.9 A), and GLUT-i2 (3.0 A), all in inward-open conformations. Despite very different chemical backbones (cytochalasin B is a macrocyclic fungal metabolite; GLUT-i1/i2 are phenylalanine amides), all three inhibitors bind in the same central cavity overlapping the glucose-binding site. Key interactions include pi-pi stacking with conserved Trp388 and Trp412, hydrophobic contacts with Asn411 and Phe379, and hydrogen bonds with Thr137 and Trp388. The WT structures confirm that the N45T/E329Q mutations used in the apo structure were not necessary for crystallization.

### Structural basis for isoform selectivity across hGLUT1-4

IC50 values against hGLUT1-4 show sub-micromolar inhibition of hGLUT1 and hGLUT4, with 10-100 fold weaker inhibition of hGLUT2 and intermediate potency against hGLUT3. Homology models of hGLUT2-4 based on the hGLUT1 inhibitor-bound structures reveal that sequence differences in the binding pocket, particularly residues lining the central cavity, explain the differential isoform selectivity. Trp388 (TM10) is a key binding determinant for all three inhibitors and likely blocks the inward-to-occluded conformational transition required for glucose transport.

### Conserved inhibitor-binding mode despite diverse scaffolds

Comparison of all three inhibitor-bound structures by Fo-Fo difference maps confirmed that all three compounds occupy the same binding pocket. The inhibitors compete with glucose by binding at the central substrate-binding site in the inward-open conformation. Trp388 and Trp412 are conserved across homologous sugar transporters including E. coli GalP, and mutation of equivalent residues in GalP decreases affinity for cytochalasin B, supporting a conserved mechanism of inhibition across the sugar porter family.

### High-resolution GLUT1 structure reveals novel chloride binding site

The 2.4 A resolution crystal structure of human GLUT1 (PDB 6THA) in the inward-open conformation revealed a previously undescribed Cl- ion binding site located between the SP motif (residue Glu209) and the A motif (Arg92, Arg93) in the N-domain. The Cl- site was confirmed by anomalous diffraction experiments using bromide (MgBr2) substitution, which showed a single strong anomalous peak (7.3 sigma) at the equivalent position. In the outward-facing conformation (GLUT3, PDB 4ZW9), the glutamate residue of the SP motif (Glu209 in GLUT1, Glu207 in GLUT3) interacts directly with the A motif, forming the "SP-A network" that stabilizes the outward state. In the inward conformation, a Cl- ion replaces the glutamate, neutralizing the A-motif charge and stabilizing the inward-open state.

### SP-A network controls conformational equilibrium between inward and outward states

The SP-A network involves interactions between the conserved glutamate residue of the Sugar Porter (SP) motif and the arginine/glycine-rich A motif. In the N-domain, Glu209 of GLUT1 (Glu207 of GLUT3) establishes hydrogen bonds with Arg92 and Arg93 of the A motif in the outward conformation, stabilizing the outward-facing state ready to receive glucose. The GLUT1 E209Q mutation (neutralizing the acidic group) reduced apparent affinity: Km increased from 9.5 mM to 17 mM, with only a modest effect on Vmax (6,473 vs 5,988 pmol/oocyte/30 min). Similarly, GLUT3 E207Q increased Km from 2.6 mM to 6.2 mM with reduced Vmax (1,418 vs 2,731 pmol/oocyte/30 min). These results confirm that disruption of the SP-A network destabilizes the outward conformation, decreasing transport affinity.

### Single-point mutation K456R converts GLUT1 to GLUT3-like kinetics

Sequence analysis of the C-domain SP motif revealed a key difference: Lys456 in GLUT1 is replaced by Arg454 in GLUT3. The GLUT1 K456R mutation (mimicking GLUT3) produced a dramatic shift in transport properties: Km improved from 9.5 mM to 4.2 mM (similar to GLUT3 wild-type at 2.6 mM), while Vmax decreased from 5,988 to 2,427 pmol/oocyte/30 min (approaching GLUT3 Vmax of 2,731). Conversely, the reverse mutation GLUT3 R454K (mimicking GLUT1) decreased affinity sixfold to Km = 17 mM. This demonstrates that a single residue in the C-domain SP motif can largely determine the kinetic differences between GLUT1 and GLUT3, likely by modulating stabilization of the outward conformation.

### Intracellular glucose/lipid binding site at the SP motif

The 2.4 A structure revealed an intracellular secondary binding site where a nonyl-beta-D-glucopyranoside (NG) molecule binds at the SP motif in the N-domain. The glucose headgroup of NG interacts with Arg93, Asn94, Glu209, Arg218, and Arg223 from the SP motif and ICH1-2 loops, stabilizing the inward-open conformation. This site may represent a physiological endofacial regulatory site where intracellular glucose or lipid headgroups can modulate GLUT kinetics by stabilizing the inward-open conformation.

### Kinetic comparison of GLUT1 and GLUT3 in identical experimental conditions

Direct side-by-side comparison of GLUT1 and GLUT3 expressed in Xenopus oocytes under identical conditions confirmed GLUT3 has ~3.7-fold higher apparent affinity (Km = 2.6 mM vs 9.5 mM for GLUT1) and ~2.2-fold lower turnover (Vmax = 2,731 vs 5,988 pmol/oocyte/30 min). Both transporters show similar substrate selectivity profiles, with glucose and mannose as the strongest competitors. These kinetic differences cannot be explained by the substrate-binding site (structurally identical) but arise from the SP-A network-mediated conformational equilibrium.


## Cross-References

- [XylE (Escherichia coli Sugar Transporter)](/xray-mp-wiki/proteins/mfs-transporters/xyle/) — Bacterial homologue; structural comparison reveals 16 degree domain rotation
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) — GLUT1 belongs to the MFS, specifically the sugar porter subfamily
- [Sugar Porter (SP) Family](/xray-mp-wiki/concepts/sugar-porter-family/) — GLUT1 is a member of the sugar porter subfamily of MFS transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — GLUT1 transports glucose via the alternating access mechanism
- [Conformational Dynamics in MFS Transporters](/xray-mp-wiki/concepts/conformational-dynamics-mfs/) — N/C domain rotation of 16 degrees observed between inward-open and outward-facing states
- [Rocker-Switch Mechanism in MFS Transporters](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — MFS-specific variant of alternating access mechanism employed by GLUT1
- [n-Nonyl-beta-D-glucopyranoside (beta-NG)](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) — Detergent used for crystallization; binds to substrate-binding site
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane solubilization and purification
- [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Referenced in glut1
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Referenced in glut1
- [hGLUT3 (Human Glucose Transporter 3)](/xray-mp-wiki/proteins/mfs-transporters/hglut3/) — Structural and functional comparison with GLUT3 revealed the SP-A network mechanism of transport regulation
