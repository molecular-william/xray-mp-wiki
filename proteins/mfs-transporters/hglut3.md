---
title: hGLUT3 (Human Glucose Transporter 3)
created: 2026-06-11
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.2017749118, doi/10.26508##lsa.202000858, doi/10.1038##nature14655]
verified: false
---

# hGLUT3 (Human Glucose Transporter 3)

## Overview

Human [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transporter 3 (hGLUT3, encoded by SLC2A3) is a member of the GLUT/SLC2
family of facilitative [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transporters. hGLUT3 shares ~80% sequence similarity
with [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) and is highly expressed in neurons and other tissues with high [Glucose](/xray-mp-wiki/reagents/additives/glucose/) demand.
The high-resolution structure of human GLUT3 in complex with D-glucose was determined at 1.5 Å resolution in an outward-occluded conformation, allowing discrimination of both α- and β-anomers of D-glucose. Two additional structures of GLUT3 bound to the exofacial inhibitor maltose were obtained at 2.6 Å in the outward-open and 2.4 Å in the outward-occluded states. Comparison of the outward-facing GLUT3 structures with the inward-open GLUT1 provides insights into the alternating access cycle for GLUTs, whereby the C-terminal domain provides the primary substrate-binding site and the N-terminal domain undergoes rigid-body rotation with respect to the C-terminal domain.
In the context of antimalarial drug design, the crystal structure of hGLUT3 in complex with the [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) inhibitor [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) was determined at 2.3 Å resolution to study whether the
allosteric pocket found in [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) is conserved in human GLUT transporters. The structure
(outward-occluded conformation) revealed that [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) binds differently in hGLUT3 compared
to [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/): the tail of [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) occupies the monoolein-binding pocket at the TM2–TM11
interface in hGLUT3, whereas it projects into the central cavity in [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/). These
structural differences confirmed the unique inhibitor-binding-induced pocket specific
to [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/), providing the basis for selective inhibitor design.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature14655 | 4ZW9 | 1.5 | P2₁ | Human GLUT3(N43T) in complex with D-glucose, outward-occluded conformation | D-Glucose (α- and β-anomers), monoolein |
| doi/10.1038##nature14655 | 4ZWB | 2.6 | P2₁ | Human GLUT3(N43T) in complex with maltose, outward-open conformation | Maltose |
| doi/10.1038##nature14655 | 4ZWC | 2.4 | P2₁ | Human GLUT3(N43T) in complex with maltose, outward-occluded conformation | Maltose |
| doi/10.1073##pnas.2017749118 |  | 2.3 |  | hGLUT3 | [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf-9 insect cells (baculovirus)
- **Construct**: Human GLUT3(N43T) with N-terminal 10×His tag; N43T mutation eliminates N-glycosylation site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Dounce homogenization (80 cycles on ice) | -- | 25 mM MES pH 6.0, 150 mM NaCl, protease inhibitors (aprotinin 0.8 μM, pepstatin 2 μM, leupeptin 5 μg ml⁻¹) + -- | Sf-9 cells collected 72 h after infection; membrane pellets collected after centrifugation |
| Solubilization | Detergent solubilization | -- | 25 mM MES pH 6.0, 150 mM NaCl, 50 mM D-glucose or maltose + 2% (w/v) n-dodecyl-β-D-maltoside (DDM) | Solubilized at 4°C for 2 h; insoluble fraction removed by ultracentrifugation (150,000g, 30 min) |
| Ni-NTA affinity chromatography | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) (Ni-NTA) | Ni-NTA resin (Qiagen) | 25 mM MES pH 6.0, 500 mM NaCl, 30 mM imidazole + 0.06% (w/v) 6-cyclohexyl-1-hexyl-β-D-maltoside (CYMAL-6) | Incubated 30 min at 4°C; rinsed 3 times; eluted with 300 mM imidazole; concentrated to 10 mg ml⁻¹; 50 mM D-glucose or maltose present throughout |
| Size-exclusion chromatography | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200) 10/300 GL | 25 mM MES pH 6.0, 150 mM NaCl + 0.06% (w/v) CYMAL-6 | Pre-equilibrated with same buffer; peak fractions collected for transport assay or crystallization |


## Crystallization

### doi/10.1038##nature14655

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | GLUT3(N43T) concentrated to 30-40 mg ml⁻¹, mixed with monoolein in 1:1.5 protein:lipid ratio (w/w) using syringe lipid mixer |
| Temperature | 20 °C |
| Growth time | 1 week (glucose-bound); overnight (maltose-bound) |
| Notes | Crystals grown in LCP using glass sandwich plates. Glucose-bound crystals diffracted to 1.5 Å at SSRF BL17U. Maltose-bound crystals: outward-occluded form appeared with 38-40% PEG400, 100 mM Mg(CHO₂)₂, 50 mM maltose; outward-open form in similar conditions. Two molecules per asymmetric unit in outward-open form (P2₁), one in outward-occluded form. Solved by molecular replacement. |

### doi/10.1073##pnas.2017749118

| Parameter | Value |
|---|---|
| Notes | The hGLUT3-[C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) complex structure was determined at 2.30 A resolution. The overall structure adopts a similar conformation to the glucose-bound form (PDB 4ZW9). The sugar moiety of [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) is coordinated nearly identically to D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) by conserved residues. The tail of [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) occupies the monoolein-binding pocket at the TM2-TM11 interface, distinct from its binding mode in [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/). |


## Biological / Functional Insights

### Recognition of α- and β-anomers of D-glucose

The 1.5 Å resolution structure of glucose-bound GLUT3 enabled discrimination of both α- and β-D-glucose anomers. Despite the prevailing presence of β-D-glucose in aqueous solution, the α-anomer exhibits dominant occupancy of approximately 69% in the refined structure. D-glucose is bound asymmetrically within the central cavity, coordinated predominantly by polar residues from the C-terminal domain. Key coordinating residues include Gln280 and Gln281 on TM7b, Asn315 on TM8, and Glu378 on TM10a. The high-resolution structure resolves the long-standing question of whether GLUTs require anomerization for transport — both anomers are recognized, so anomerization may not be required for D-glucose transport.

### Conformational transition from outward-open to outward-occluded

Comparison of the outward-open and outward-occluded GLUT3 structures reveals the molecular basis for the conformational switch. TM7b, consisting of four helical turns, is partly unwound and bent in the middle such that the first two helical turns tilt inwards, undergoing an axial rotation by approximately 60 degrees. This leads to relocation of Tyr290 and the substrate-coordinating residue Asn286 into the transport path. An invariant glycine (Gly284) constitutes the kink preceding TM7b, providing flexibility for the structural shift. The N-terminal domain remains nearly rigid throughout, while the ICH domain exhibits minor intra-domain rearrangements.

### Alternating access mechanism for GLUTs

Comparison of glucose-bound outward-occluded GLUT3 with inward-open GLUT1 (PDB 4PYP) provides the framework for alternating access in GLUTs. The C-terminal domain provides the primary substrate-binding site, while the N-terminal domain undergoes rigid-body rotation with respect to the C-terminal domain. TM7b and TM10b undergo prominent conformational changes during the outward-to-inward transition. The N-terminal domain core is relatively hydrophilic with a continuous strip of hydrogen-bonded water molecules, supporting its rigidity. The C-terminal domain is highly hydrophobic, enabling structural adaptability during conformational change.

### Substrate selectivity and ligand design

The structures provide molecular interpretation for the asymmetry of ligand binding from endo- and exofacial sides of GLUTs. The C-terminal domain provides a partial substrate-binding site composed of polar residues on TM7b, TM8, and TM10a. Arrival of substrate at this primary site induces conformational changes including local shifts of TM7b and TM10b along with relative domain rotation. These insights provide a framework for rational design of ligands targeting GLUTs, particularly relevant for cancer therapy via the Warburg effect.

### Structural comparison confirms PfHT1-specific allosteric site

The hGLUT3-[C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) co-crystal structure at 2.3 A resolution revealed that [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) binds
differently in hGLUT3 compared to [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/). In hGLUT3, the tail of [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) points toward
the TM2-TM11 interface, occupying the pocket that accommodates [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) in the
glucose-bound structure. In [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/), the tail projects into the central cavity of the
occluded structure. This differential binding confirms that [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) possesses unique
intra-domain flexibility that can be exploited for designing selective inhibitors
targeting the allosteric site without inhibiting human GLUTs.

### SP-A network and kinetic differences from GLUT1

Direct comparison of [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) and [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) under identical experimental conditions
(doi/10.26508##lsa.202000858) revealed that [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) has ~3.7-fold higher apparent
affinity (Km = 2.6 mM vs 9.5 mM for [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/)) but ~2.2-fold lower Vmax. These
differences arise from the SP-A network: the C-domain SP motif contains Arg454 in
[GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) versus Lys456 in [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/). The [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) R454K mutation (mimicking [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/)) decreased
affinity sixfold to Km = 17 mM, while the reciprocal [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) K456R mutation produced
GLUT3-like kinetics (Km = 4.2 mM). This demonstrates that a single residue in the
C-domain SP motif determines the isoform-specific kinetic properties. In the N-domain,
both [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) and [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) have identical SP-A networks with Glu209/Glu207 interacting
with the A motif to stabilize the outward conformation.


## Cross-References

- [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) — Structural comparison between hGLUT3-C3361 and PfHT1-C3361 confirmed the unique allosteric pocket in PfHT1
- [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) — hGLUT3 shares 80% sequence similarity with hGLUT1 and was used as a surrogate for structural studies; comparison of outward-facing GLUT3 with inward-open GLUT1 reveals alternating access mechanism
- [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) — C3361 bound to hGLUT3 was used to study the structural basis of PfHT1 selectivity
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — GLUT3 structures in outward-open, outward-occluded, and comparison with inward-open GLUT1 provide key structural evidence for alternating access in MFS transporters
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) — GLUT3 is a member of the MFS with canonical 12-TM fold; the high-resolution structure reveals details of the MFS alternating access cycle
- [Sugar Porter (SP) Family](/xray-mp-wiki/concepts/protein-families/sugar-porter-family/) — hGLUT3 is a member of the Sugar Porter family within MFS; structures provide insights into SP motif function
