---
title: "PfHT1 (Plasmodium falciparum Hexose Transporter 1)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-020-1963-z, doi/10.1073##pnas.2017749118]
verified: false
---

# PfHT1 (Plasmodium falciparum Hexose Transporter 1)

## Overview

PfHT1 (PF3D7_0204700) is the sole hexose transporter in Plasmodium falciparum,
the deadliest species of malaria parasite. It is a member of the major facilitator
superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)) and is essential for the survival of the blood-stage parasite by
importing D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) as the primary energy source. The crystal structure of PfHT1
in complex with D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) was determined at 3.6 A resolution (Qureshi et al., Nature
2020, PDB 6RW3), revealing a fully occluded conformation with TM7b positioned as an
extracellular substrate-gating helix. Unlike human GLUT transporters which rely on
conserved tyrosine residues for gating, PfHT1 has evolved polar residues (Ser315,
Asn316) at these positions that form allosteric contacts with TM1 residues (Lys51,
Asn48) — located approximately 15 A from the D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) binding site. These TM1-TM7b
interactions are equally critical for transport as the sugar-coordinating residues
themselves, demonstrating strong allosteric coupling between sugar binding and gating.
PfHT1 achieves broad substrate promiscuity not through modifications to its sugar-binding
site (which is remarkably similar to [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) and [GLUT5 Fructose Transporter](/xray-mp-wiki/proteins/mfs-transporters/glut5/)), but through evolved substrate-gating
dynamics. The protein was also crystallized in complex with D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) at 2.6 A resolution
(PDB 6M20) and with the inhibitor [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) at 3.7 A resolution (PDB 6M2L). Structural
comparison with human [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) revealed a unique allosteric pocket adjacent to the
glucose-binding site that is more hydrophobic than the corresponding region in [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/),
exploited to design orthosteric-allosteric dual inhibitors (TH-PF series) with potent
antiplasmodial activity. PfHT1 has been genetically validated as a drug target and is
the subject of a selective starvation antimalarial strategy.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.2017749118 | 6M20 | 2.6 |  | Full-length PfHT1 | D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) |
| doi/10.1073##pnas.2017749118 | 6M2L | 3.7 |  | Full-length PfHT1 | [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) |
| doi/10.1038##s41586-020-1963-z | 6RW3 | 3.6 |  | Full-length PfHT1 crystallized in D-glucose-bound occluded conformation | D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) |

## Expression and Purification


No purification described.

## Crystallization

### doi/10.1073##pnas.2017749118

| Parameter | Value |
|---|---|
| Notes | Structures reported previously in Jiang et al., Cell 2020 (ref 20). PfHT1 was crystallized in complex with D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) (2.6 A) and [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) (3.7 A). |


## Biological / Functional Insights

### Allosteric coupling between TM1 and TM7b drives sugar transport in PfHT1

The 3.6 A crystal structure of PfHT1 (PDB 6RW3) revealed that polar contacts
between the extracellular gating helix TM7b (residues Asn311, Asn316, Ser317, Asn318)
and TM1 (residues Lys51, Asn48) — located approximately 15 A from the D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) binding
site — are just as critical for transport as residues that directly coordinate D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/).
In human GLUT transporters, two conserved tyrosine residues on TM7b form occlusion
contacts, but in PfHT1 these are replaced by Ser315 and Asn316. Substitution of either
with tyrosine abolished transport. Asn316 interacts with Lys51 on TM1, and mutations
of Lys51 (to Ala or Gln) also rendered PfHT1 non-functional. Molecular dynamics
simulations (1 microsecond) showed that TM7b in human [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) is highly mobile and moves
apart from TM1 to release D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/), whereas TM7b in PfHT1 maintains an occluded
conformation. This demonstrates strong allosteric coupling between sugar binding and
gating, suggesting that TM1-TM7b interactions should be considered more closely in
establishing transport mechanisms in general.

### Sugar promiscuity in PfHT1 is achieved through gating dynamics, not binding-site modification

Unlike human GLUT transporters which show narrow substrate specificity, PfHT1
transports both D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) and [D-Fructose](/xray-mp-wiki/reagents/ligands/d-fructose/) with kinetics similar to dedicated [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/)
and [GLUT5 Fructose Transporter](/xray-mp-wiki/proteins/mfs-transporters/glut5/). The sugar-binding site in PfHT1 is remarkably similar to those of
distantly related [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) and [GLUT5 Fructose Transporter](/xray-mp-wiki/proteins/mfs-transporters/glut5/), and engineered PfHT1 mutations to match GLUT
sugar-binding sites did not shift sugar preferences. The C3-hydroxyl group orientation
was determined as the most critical for D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) recognition. PfHT1 achieves substrate
promiscuity by evolving substrate-gating dynamics rather than modifying its binding site.
The C3- and C4-hydroxyl groups hydrogen bond to Asn311 and Gln306, while C1- and C2-
hydroxyl groups bond to Gln169, Gln305 and Trp412. Asn311 in TM7b is the only binding-site
residue that moves substantially during the transport cycle, forming hydrogen bonds with
the critically important C3- and C4-hydroxyl groups during transition to the occluded state.

### PfHT1 is the sole hexose transporter in P. falciparum

PfHT1 is transcribed from a single-copy gene with no close paralogue and is
essential for the survival of the blood-stage parasite. [Glucose](/xray-mp-wiki/reagents/additives/glucose/) is the primary
energy source for blood-stage P. falciparum, making PfHT1 a validated antimalarial
target. The blood-stage parasites depend on constant [Glucose](/xray-mp-wiki/reagents/additives/glucose/) supply, and PfHT1
inhibition leads to glycolysis shutdown and parasite death.

### Unique allosteric pocket in PfHT1 enables selective inhibitor design

Structural comparison between PfHT1 and [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) revealed an additional pocket
adjacent to the substrate-binding site, linked by a narrow hydrophobic channel.
This allosteric site is highly hydrophobic in PfHT1 but more hydrophilic in [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/),
providing a structural basis for designing selective PfHT1 inhibitors. The allosteric
pocket was exploited to design dual orthosteric–allosteric inhibitors (TH-PF series)
that simultaneously block both the glucose-binding site and the adjacent allosteric
pocket, achieving high selectivity over human GLUT transporters.

### Selectivity over human GLUT transporters

The TH-PF series of compounds showed selective inhibition of PfHT1 over [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/).
Key residues in the connecting channel (F85, V44 in PfHT1) are responsible for the
hydrophobic nature of the allosteric pocket. Mutating these residues to their human
[SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) counterparts (F85S, V44T) decreased inhibitor potency, confirming that the
hydrophobicity of the allosteric channel is critical for selectivity.


## Cross-References

- [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) — Human ortholog used for selectivity comparison in drug design
- [hGLUT3 (Human Glucose Transporter 3)](/xray-mp-wiki/proteins/mfs-transporters/hglut3/) — Crystal structure of hGLUT3-C3361 complex (2.3 A) used to confirm PfHT1-specific allosteric pocket
- [Selective Starvation of Malaria Parasites](/xray-mp-wiki/concepts/miscellaneous/selective-starvation/) — PfHT1 inhibition is the basis of the selective starvation antimalarial strategy
- [Orthosteric–Allosteric Dual Inhibition](/xray-mp-wiki/concepts/transport-mechanisms/orthosteric-allosteric-dual-inhibition/) — TH-PF series compounds simultaneously target orthosteric and allosteric sites of PfHT1
- [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) — Reference compound used to identify the allosteric pocket in PfHT1
- [TH-PF01](/xray-mp-wiki/reagents/ligands/th-pf01/) — Lead dual inhibitor targeting PfHT1 orthosteric and allosteric pockets
- [TH-PF02](/xray-mp-wiki/reagents/ligands/th-pf02/) — Lead dual inhibitor targeting PfHT1 orthosteric and allosteric pockets
- [TH-PF03](/xray-mp-wiki/reagents/ligands/th-pf03/) — Lead dual inhibitor targeting PfHT1 orthosteric and allosteric pockets
- [Major Facilitator Superfamily Transport Mechanism](/xray-mp-wiki/concepts/mfs-transporter-mechanism/) — PfHT1 exhibits rocker-switch alternating-access mechanism typical of MFS transporters
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/alternating-access/) — The occluded PfHT1 structure combined with previous sugar-porter structures reconstructs the MFS transport cycle
- [Allosteric Coupling in Transporters](/xray-mp-wiki/concepts/allosteric-coupling/) — TM1-TM7b interactions 15 A from the sugar site demonstrate long-range allosteric coupling between sugar binding and gating
- [MMV009085 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/mmv009085/) — MMV009085 binds in the sugar-binding pocket and its inhibition depends on Trp412
- [Cytochalasin B](/xray-mp-wiki/reagents/ligands/cytochalasin-b/) — Cytochalasin B inhibits PfHT1 by binding to the hydrophobic-side vestibule adjacent to the sugar-binding site
