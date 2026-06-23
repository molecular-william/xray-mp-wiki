---
title: "Maltose Transporter MalFGK2 (E. coli)"
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.molcel.2009.01.035, doi/10.1038##nature12232, doi/10.1073##pnas.1108858108, doi/10.1073##pnas.1311407110, doi/10.1126##science.1200767]
verified: false
---

# Maltose Transporter MalFGK2 (E. coli)

## Overview

The maltose transporter from Escherichia coli (MalFGK2) is a prototype
ATP-binding cassette (ABC) importer. It consists of two integral membrane
proteins (MalF and MalG) forming the transmembrane translocation pathway,
and two copies of the cytoplasmic ATPase component (MalK). The transporter
requires the periplasmic [maltose-binding protein (MBP)](/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/)
for substrate delivery. Crystal structures of the full-length wild-type
MBP-MalFGK2 complex stabilized by AMP-PNP, ADP-BeF3, ADP-VO4, or ADP-AlF4
at 2.2-2.4 A resolution revealed snapshots of the ground state and transition
state during ATP hydrolysis. Subsequent structures with maltoheptaose (4KHZ,
2.9 A) and maltohexaose (4KI0) revealed the structural basis for substrate
specificity, showing that the transmembrane subunits MalF and MalG form
specific interactions with the substrate, contributing to overall selectivity
beyond that provided by MBP alone.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1108858108 | 3RLF | 2.3 | P1 | Full-length wild-type MalFGK2 with MBP | ADP-AlF4 (transition state) |
| doi/10.1073##pnas.1311407110 | 4KHZ | 2.9 | — | MBP-MalFGK2 complex with maltoheptaose | maltoheptaose |
| doi/10.1073##pnas.1311407110 | 4KI0 |  | — | MBP-MalFGK2 complex with maltohexaose | maltohexaose |
| doi/10.1016##j.molcel.2009.01.035 | 3FH6 | 4.5 | I222 | Delta TM1 MalFGK2 (lacking residues 2-35 of MalF) | none (nucleotide-free, inward-facing resting state) |
| doi/10.1126##science.1200767 | 3PV0 | 3.1 | P1 | MBP(G69C/S337C) locked-closed mutant complexed with MalFGK2 | maltose (in MBP and in TM site) |
| doi/10.1038##nature12232 | 4JBW | 3.9 | not specified | Full MalFGK2 complex with two EIIA^Glc molecules (residues 19-168 of EIIA^Glc) | EIIA^Glc (regulatory protein, 2 molecules) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length MalFGK2 complex
- **Notes**: Expressed and purified as described in Oldham et al., Nature 2007

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Full-length MalFGK2

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization | — |  | Two passes through Emulsiflex high-pressure homogenizer |
| Purification | Cobalt affinity chromatography | — |  | As described in Oldham et al. 2007; protein in 0.06% UDM for crystallization |

**Final sample**: 10 mg/mL MalFGK2 in 0.06% UDM


## Crystallization

### doi/10.1073##pnas.1311407110

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | MBP-MalFGK2 at 10 mg/mL in 0.06% UDM with 0.2 mM maltoheptaose, 1:1.25 MBP molar ratio |
| Reservoir | 30% PEG 400, 100 mM NaCl, 10 mM MgCl2, 100 mM sodium Hepes pH 7.5 |
| Mixing ratio | 1:1 |
| Temperature | 20 C |
| Notes | Pretranslocation state crystals (4KHZ); also crystallized outward-facing state with maltohexaose |

### doi/10.1016##j.molcel.2009.01.035

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Delta TM1 MalFGK2 at 11 mg/mL in 0.06% UDM, 20 mM Tris pH 8.0, 50 mM NaCl |
| Reservoir | 11.5% PEG 4000, 0.1 M ADA pH 6.5, 0.1 M NaCl, 0.1 M Li2SO4 |
| Mixing ratio | 2:1 (protein:reservoir) |
| Temperature | 20 C |
| Growth time | 24 hr to 1 week |
| Cryoprotection | 16% ethylene glycol |
| Notes | Nucleotide-free, inward-facing resting state crystals. Construct lacks MalF TM1 (residues 2-35). Crystals diffracted to 4.5 A along c* and 6.5 A along a*. |


## Biological / Functional Insights

### Alternating access via concerted rigid-body rotations

Comparison of the inward-facing (3FH6) and outward-facing (2R6G) structures reveals that alternating access involves rigid-body rotations of the TM subdomains coupled to NBD closure/opening. The MalF core and MalG core rotate by 22 degrees and 23 degrees respectively, each about an axis ~45 degrees to the membrane plane, accompanied by ~4 A translation. This opens the periplasmic side and closes the cytosolic side simultaneously. The transition is described as a concerted motion of the TM cores and NBDs, connected through a ball-and-socket joint at the coupling helix interface.

### Hydrophobic periplasmic gate in the inward-facing conformation

In the inward-facing conformation, access from the periplasm to the maltose-binding site is obstructed by a hydrophobic gate composed of four loops, each at the bend of a kinked TM helix. This gate architecture is conserved in the ModB2C2A molybdate transporter, despite different primary sequences. In contrast, the barrier on the cytoplasmic side in the outward-facing state is much larger, with a bundle of four TM helices beneath the maltose.

### Binding protein-independent (BPI) mutants destabilize resting state contacts

Mutations enabling transport without MBP (BPI mutants) lie at sites of interaction altered during the inward/outward transition. P site mutations (L334W, F336L, G338R of MalF) and L135 of MalG destabilize MalF-MalG contacts at the periplasmic surface in the resting state, facilitating transition to the outward-facing conformation without MBP. Second-site mutations (e.g., V442A of MalF altering a periplasmic gating residue) likely lower the energy barrier between conformations. These mutants may rest closer to the transition state than wild-type.

### General base mechanism of ATP hydrolysis in ABC transporters

ATP hydrolysis proceeds via direct in-line attack of the ATP gamma-phosphate by a hydrolytic water molecule through a pentacovalent transition state. The ground state (tetrahedral gamma-phosphate) has low affinity for the attacking water. The transition state (trigonal bipyramidal) positions a water molecule 2.3 A from the gamma-phosphate, in-line with the beta/gamma bridging oxygen. The conserved glutamate following the Walker B motif (E159 in the maltose transporter) acts as the general base to polarize the attacking water.

### Structural role of conserved residues in the NBD

The Q-loop glutamine (Q82) interacts with Mg2+ and the gamma-phosphate of ATP, playing an essential role in ATP hydrolysis. The switch histidine functions as a 'linchpin' holding together the gamma-phosphate, attacking water, and catalytic glutamate. The LSGGQ motif of one NBD and the Walker A, Q-loop, and switch histidine of the other NBD tightly tether the two NBDs.

### Transition state does not induce conformational changes

The ground-state and transition-state complexes are in the same outward-facing conformation. Formation of the transition state does not induce or require any further structural rearrangements; the transition state is only a chemical step for hydrolysis with no special functional properties for substrate translocation.

### ATP stoichiometry in the transport cycle

All crystal structures showed clear electron density for maltose, two ADP, and two gamma-phosphate analog molecules, suggesting ADP is trapped at both nucleotide-binding sites. Anomalous difference Fourier maps at the vanadium edge showed peaks of similar intensity at both ATP-binding sites. However, the possibility of 0.5 occupancy at each site with equal distribution between both sites could not be ruled out.

### Pretranslocation intermediate state reveals allosteric communication in ABC transporters

The crystal structure of the pre-T complex (Science 2011, 3.1 A) captures the maltose transporter in an intermediate step between inward- and outward-facing states. Substrate-loaded MBP in the periplasm induces a partial closure of the MalK dimer in the cytoplasm, bringing the D loop residues (D165, A166) into contact with Walker A S38 and switch H192 of the opposite subunit. ATP binding to this conformation promotes progression to the outward-facing state. The structure shows that MBP binding lowers the energy barrier for NBD dimer closure, explaining how substrate binding on the periplasmic surface influences NBD conformation at the intracellular surface over 80 A away. AMP-PNP soaking experiments with locked-closed MBP (G69C/S337C) revealed that the gamma-phosphate is disordered in the semi-open MalK configuration, indicating that full NBD closure is necessary to orient ATP for hydrolysis.

### Substrate specificity is conveyed by both MBP and MalFGK2

The transmembrane subunits MalF and MalG contribute to substrate selectivity beyond that of MBP alone. In the pretranslocation state, the scoop loop of MalG (Q256) hydrogen bonds to the reducing end glucosyl unit (g1), explaining why maltose analogs with a modified reducing end are not transported despite binding to MBP. In the outward-facing state, MalF binds three glucosyl units from the nonreducing end through aromatic stacking (F435, F436) and hydrogen bonds (S433, Y325), conferring specificity for the alpha-1,4 linkage. The substrate-binding cavity of ~2,400 A3 in the pretranslocation state limits substrate size to approximately seven glucosyl units.


## Cross-References

- [MBP (Escherichia coli Maltose-Binding Protein)](/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/) — MBP is the periplasmic binding protein that delivers maltose to the MalFGK2 complex
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) — Maltose is the physiological substrate delivered to the transmembrane cavity
- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — The maltose transporter is a prototype ABC importer
- [n-Undecyl-beta-D-maltoside (UDM)](/xray-mp-wiki/reagents/detergents/udm/) — Detergent used for protein solubilization and crystallization
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Crystallization buffer at pH 7.5
- [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malF/) — Transmembrane subunit; forms substrate translocation pathway
- [MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malG/) — Transmembrane subunit; contains P3 loop for substrate scoop
- [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) — ATP-binding subunit; EIIA^Glc binds to MalK NBD and regulatory domain
- [EIIA^Glc (Escherichia coli Enzyme IIA^Glc)](/xray-mp-wiki/proteins/abc-transporters/eiiaglc/) — Regulatory protein; allosteric inhibitor of MalFGK2
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization and purification
- [DMPC (1,2-Dimyristoyl-sn-glycero-3-phosphocholine)](/xray-mp-wiki/reagents/lipids/dmpc/) — Lipid component of bicelles used for crystallization
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — EIIA^Glc acts as a classical MWC allosteric inhibitor of the transporter
- [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) — Iptg used in purification or crystallization buffer
- [Magnesium Chloride (MgCl₂)](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Mgcl2 used in purification or crystallization buffer
