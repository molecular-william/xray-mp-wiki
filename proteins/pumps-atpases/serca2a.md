---
title: SERCA2a (Cardiac Sarco/Endoplasmic Reticulum Ca2+-ATPase)
created: 2026-06-11
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.2006027117, doi/10.15252##embj.2018100020]
verified: false
---

# SERCA2a (Cardiac Sarco/Endoplasmic Reticulum Ca2+-ATPase)

## Overview

SERCA2a is the cardiac isoform of sarco/endoplasmic reticulum Ca2+-ATPase, a P-type ATPase that transports Ca2+ ions
from the cytosol into the sarcoplasmic reticulum lumen using energy from ATP hydrolysis. It is the predominant isoform
in cardiac muscle and is essential for cardiac relaxation (diastole). A 3.0 A crystal structure of SERCA2a in the
E2-ACP state (with adenosine 5'-(beta,gamma-imido)triphosphate, AMPPNP analogue ACP) revealed that ATP binding alone
can properly arrange the cytoplasmic domains (A, N, P) for phosphoryl transfer, even without Ca2+ bound. However,
nonproductive phosphoryl transfer is prevented because bending of the P-domain (required for catalysis) does not occur
until both transmembrane Ca2+-binding sites are occupied. The structure explains how SERCA has high ATP affinity in
the E2 state and how ATP accelerates Ca2+ binding at low pH. The first crystal structures of SERCA2a from native pig
ventricular muscle were determined in the CPA-stabilized E2-AlF4 form (3.3 A, PDB 5MPM) and the Ca2+-occluded
[Ca2]E1-AMPPCP form (4.0 A, PDB 6HXB). These structures are similar to SERCA1a, consistent with a conserved
Ca2+ transport mechanism, but isoform-specific residues provide regulatory control via post-translational modifications
and altered networks of intramolecular interactions.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.2006027117 |  | 3.0 |  | Porcine SERCA2a, wild-type, in E2-ACP state | ACP (adenylyl imidodiphosphate), no divalent cation |
| doi/10.15252##embj.2018100020 | 5MPM | 3.3 | P21 | Full-length porcine SERCA2a (997 residues), E2-AlF4-CPA state, purified from native pig ventricular muscle | AlF4- (aluminum fluoride, phosphate analog), CPA (cyclopiazonic acid), Mg2+, K+ |
| doi/10.15252##embj.2018100020 | 6HXB | 4.0 | P2 | Full-length porcine SERCA2a (997 residues), [Ca2]E1-AMPPCP state, purified from native pig ventricular muscle | AMPPCP (non-hydrolyzable ATP analog), two Ca2+ ions, Mg2+ |

## Expression and Purification

- **Expression system**: Porcine cardiac muscle (native) and pig ventricular muscle
- **Construct**: Wild-type SERCA2a purified from cardiac sarcoplasmic reticulum
- **Notes**: Membrane protein solubilized and purified from native cardiac SR vesicles. For the EMBO J (2019) structures, SERCA2a was purified from pig ventricular muscle as active, native protein. Porcine SERCA2a shares 99% identity with human SERCA2a and 84% identity with rabbit and other mammalian SERCA1a.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Differential centrifugation and sucrose density gradient | — |  | Sarcoplasmic reticulum (SR) vesicles prepared from pig ventricular muscle |
| Solubilization | Detergent solubilization | — | C12E8 (octaethylene glycol dodecylether) | SR membranes solubilized with detergent |
| Affinity purification | Reactive Green agarose bead chromatography | — |  | SERCA2a purified by Reactive Green agarose beads affinity chromatography. The purified enzyme retains high Ca2+-dependent ATPase activity. |

**Final sample**: Purified active SERCA2a. Specific activity 4.3 +/- 0.7 umol Pi/min/mg at 1 uM free Ca2+, Km 0.22 +/- 0.01 uM for Ca2+, Hill coefficient n=1.3.
**Purity**: >95% by SDS-PAGE


## Crystallization

### doi/10.15252##embj.2018100020

| Parameter | Value |
|---|---|
| Method | Dialysis/vapor diffusion |
| Protein sample | Purified SERCA2a from pig ventricular muscle, 10-20 uM, mixed with C12E8 and endogenous lipids |
| Reservoir | E2-AlF4-CPA form: 100 mM MES pH 6.1, 10 mM MgCl2, 10 mM CaCl2, 1 mM CPA, 5 mM NaF, 1 mM AlCl3, 0.5 mM AMPPCP, 15-20% glycerol, 5% PEG 400, with phosphatidylcholine |
| Temperature | 4 deg C |
| Growth time | Several days to weeks |
| Cryoprotection | Glycerol (20%) |
| Notes | Crystals of SERCA2a in the E2-AlF4-CPA state (PDB 5MPM) diffracted to 3.3 A. Crystals of [Ca2]E1-AMPPCP (PDB 6HXB) diffracted to 4.0 A. The E2-AlF4-CPA structure has one molecule per asymmetric unit in space group P21. The [Ca2]E1-AMPPCP structure is in space group P2. CPA was included at 1 mM to stabilize the E2 state. AMPPCP was present at high concentrations in the crystallization conditions but was not observed in the E1 structure electron density. |


## Biological / Functional Insights

### ATP binding alone arranges cytoplasmic domains for phosphoryl transfer

The E2-ACP structure shows that ATP binding without Ca2+ is sufficient to arrange the cytoplasmic domains
(A, N, P) into a configuration suitable for phosphoryl transfer. The N-domain occupies the same position
relative to the P-domain as in E1-ACP-2Ca2+, and the gamma-phosphate of ACP is properly delivered to the
phosphorylation site (Asp351) with the same binding mode as in E1-ACP-2Ca2+. The adenine ring of ACP is
coplanar with Phe487, and the triphosphate chain adopts an extended conformation stabilized by interactions
with Arg489 (alpha-phosphate) and Arg560 (beta-phosphate).

### Nonproductive phosphoryl transfer prevented by P-domain unbent configuration

Despite correct ATP positioning, phosphoryl transfer does not occur because the P-domain remains in the unbent
configuration. The central beta-sheet of the P-domain is split into two staggered halves (PN and PC), and
Asp351 is turned away from the gamma-phosphate. Bending of the P-domain — which aligns the two halves of the
beta-sheet and rotates Asp351 toward the gamma-phosphate — is required for catalysis. This bending requires
a divalent cation coordinating Asp351 and Asp703, which only occurs after Ca2+ binding and associated
conformational changes in the transmembrane domain.

### Thr701 as a molecular switch for P-domain bending

Thr701, located at the top of Pbeta5, acts as a molecular switch for P-domain bending. In the unbent form,
the Asp351 amide hydrogen bonds with the side-chain hydroxyl of Thr701. In the bent (phosphorylated) form,
Asp351 amide hydrogen bonds with the main-chain carbonyl of Thr701 instead. This 3.4 A movement at the
Thr701 Calpha is the key event that aligns the two halves of the central beta-sheet, enabling phosphoryl
transfer. The side chain of Lys684 acts as a linker between the two P-domain halves, pulled 2.8 A toward
Asp351 upon bending.

### P-domain bending couples phosphoryl transfer to Ca2+ occlusion

The bending of the P-domain causes tilting of the A-domain (sitting on the P7 helix) by 30 degrees.
This tilting pulls up the M1 and M2 helices (by two and one turns of alpha-helix, respectively) to lock
the cytoplasmic gate and occlude Ca2+. The aligning of all strands in the central beta-sheet also changes
the direction of N-domain inclination, establishing a different A-N interface from E2 suitable for the
subsequent 90-degree A-domain rotation during E1P->E2P transition.

### ACP crosslinks N- and P-domains in E2

ACP (ATP analogue) crosslinks the N- and P-domains even in E2, placing them in the proper geometry for
phosphoryl transfer. The N-domain inclines more deeply than in E2(TG), pushing the A-domain such that the
M2 side becomes even closer to the membrane. The A-N interface in E2-ACP is very similar to that in
E1-ACP-2Ca2+ but not as tight. A salt bridge between Arg134 (A-domain) and Asp426/Glu429 (N-domain) is
lost in E2-ACP, with contact occurring only around Thr171.

### First crystal structures of cardiac SERCA2a reveal conserved Ca2+ transport mechanism

The first crystal structures of SERCA2a from native pig ventricular muscle were determined in two
conformational states: the CPA-stabilized E2-AlF4 form at 3.3 A (PDB 5MPM) and the Ca2+-occluded
[Ca2]E1-AMPPCP form at 4.0 A (PDB 6HXB). The structures are very similar to the corresponding states
of SERCA1a (rmsd ~0.8 A for C-alpha atoms), consistent with the 84% sequence identity between the
isoforms and confirming that the Ca2+ transport mechanism is conserved. Despite 160 amino acid
differences, the overall fold, domain architecture, and key catalytic residues are structurally
indistinguishable.

### Isoform-specific residues are acceptor sites for post-translational modifications

Analysis of SERCA2a and SERCA1a sequences revealed that many isoform-specific residues are located
in exposed regions and serve as acceptor sites for post-translational modifications (PTMs). Using
online PTM repositories and mass spectrometry of purified proteins, distinct PTM fingerprints were
identified for SERCA2a and SERCA1a, including phosphorylation, ubiquitination, sumoylation,
acetylation, and methylation. New acetylation sites were identified in purified SERCA2a. These
isoform-specific PTM patterns may provide differential regulatory control. The progressive
accumulation of SERCA2a modifications, such as tyrosine nitration during aging and in heart failure,
and decreased sumoylation in heart failure, highlight the pathophysiological relevance of PTMs.

### Isoform-specific residues alter intramolecular interaction networks

Molecular dynamics simulations (3 x 50 ns) of SERCA2a E2-AlF4-CPA and the corresponding SERCA1a
structure (PDB 3FGO) in a phosphatidylcholine membrane showed that the A- and P-domains are more
flexible in SERCA1a than in SERCA2a. Isoform-specific residues participate in distinct networks
of hydrogen bonds and salt bridges: 53.1% of SERCA2a-specific residues participate in hydrogen
bonds vs 36.9% for SERCA1a-specific residues. 96% of all identified Darier disease (DD) mutations
occur on residues predicted to form hydrogen bonds or salt bridges, confirming functional relevance.
These differences in the intramolecular interaction network likely contribute to the slower E2 to E1
conversion rate and distinct kinetic properties of SERCA2a compared to SERCA1a.


## Cross-References

- [SERCA1a (Skeletal Muscle Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) — Paralogous isoform; SERCA2a is the cardiac-specific isoform of the same P-type ATPase family
- [P-type ATPase Mechanism](/xray-mp-wiki/concepts/p-type-atpase-mechanism/) — SERCA2a is a P-type ATPase; this structure reveals how ATP binding and P-domain bending control catalysis
- [Large Domain Motion in P-type ATPases](/xray-mp-wiki/concepts/large-domain-motion-in-p-type-atpases/) — This paper provides direct structural evidence of A-domain tilting and P-domain bending motions
- [Phospholamban (PLB)](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) — PLB is a key regulator of SERCA2a in cardiac muscle; SERCA2a dysfunction is linked to heart failure
- [Cyclopiazonic Acid (CPA)](/xray-mp-wiki/reagents/ligands/cyclopiazonic-acid/) — CPA was used to stabilize the E2 state for crystallization of SERCA2a (PDB 5MPM)
