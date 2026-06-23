---
title: "NavAb Bacterial Voltage-Gated Sodium Channel"
created: 2026-06-08
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein]
sources: [doi/10.1038##nature11077, doi/10.1073##pnas.1700761114, doi/10.1073##pnas.1814928115, doi/10.1038##s41586-018-0120-4, doi/10.1085##jgp.201711884]
verified: false
---

# NavAb Bacterial Voltage-Gated Sodium Channel

## Overview

NavAb is a bacterial voltage-gated sodium channel (BacNav) from Arcobacter butzleri
that serves as a model for vertebrate voltage-gated sodium channels. NavAb forms a
homotetramer of four identical subunits, each with six transmembrane segments (S1-S6).
The landmark wild-type NavAb structure at 3.2 A resolution captured the channel in two potentially slow-inactivated states, revealing an asymmetric dimer-of-dimers S6 activation gate collapse and providing the first structural insights into Nav channel slow inactivation. Using two Na_vAb mutants (Na_vAb/FY: T206F/V213Y and Na_vAb/1-226: C-terminal
[Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/)), additional structures were determined that capture tightly closed and open states
of the activation gate at 2.8-3.2 A resolution, allowing completion of a closed-open-inactivated
conformational cycle in a single voltage-gated sodium channel. Additional high-resolution
structures of NavAb with gating-charge mutations (R2G and R3G) analogous to those
causing periodic paralysis in human Nav1.4 reveal the structural basis of pathogenic
gating pore currents in the voltage sensor domain.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11077 | 4EKW | 3.20 | P4(3)2(1)2 | Wild-type NavAb (full-length), expressed in Trichoplusia ni insect cells, purified via anti-Flag resin + SEC, reconstituted in DMPC:CHAPSO bicelles | None (apo, potentially slow-inactivated states) |
| doi/10.1073##pnas.1700761114 | 5VB2 | 2.80 | P2(1)22(1) | NavAb/FY (T206F/V213Y double mutant), full-length, homotetramer |  |
| doi/10.1073##pnas.1700761114 | 5VB2 | 2.85 | — | NavAb/1-226 (C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) at Lys-227 + I217C mutation) |  |
| doi/10.1073##pnas.1814928115 | 6MVV | not specified | — | NavAb/I217C/Delta40 in complex with [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/) |  |
| doi/10.1073##pnas.1814928115 | 6MVV | not specified | — | NavAb/I217C/Delta40 in complex with [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/) |  |
| doi/10.1038##s41586-018-0120-4 | 6C1E | 2.50 | not specified | NavAb(R2G) double mutant (R1G/R2G) in complex with guanidinium |  |
| doi/10.1038##s41586-018-0120-4 | 6C1E | 2.70 | not specified | NavAb(R3G) gating-charge mutant |  |
| doi/10.1085##jgp.201711884 | 6MWA | 2.30 | not specified | NavAbDelta28 (C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) of last 28 residues) |  |
| doi/10.1085##jgp.201711884 | 6MWA | not specified | — | NavAbDelta28/T206A |  |
| doi/10.1085##jgp.201711884 | 6MWA | not specified | — | NavAbDelta28/T206S |  |
| doi/10.1085##jgp.201711884 | 6MWA | not specified | — | NavAbDelta28/T206V |  |

## Expression and Purification

- **Expression system**: Trichoplusia ni insect cells (Bac-to-Bac baculovirus system)
- **Construct**: Full-length Na_vAb wild-type and mutants
- **Notes**: Na_vAb/FY constructed by site-directed mutagenesis (QuikChange); Na_vAb/1-226 constructed by introduction of stop codon at Lys-227

### Purification Workflow

- **Expression system**: Trichoplusia ni insect cells
- **Expression construct**: Full-length Na_vAb with T206F/V213Y mutations (Na_vAb/FY) or C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) to residue 226 (Na_vAb/1-226)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein production | Baculovirus infection of T. ni cells | — |  | Recombinant baculovirus generated using Bac-to-Bac system (Invitrogen) |
| Purification | As described in Payandeh et al. (2012) Nature | — |  | Protien produced and purified as described in reference 8 |


## Crystallization

### doi/10.1038##nature11077

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Wild-type NavAb at ~20 mg/mL reconstituted in DMPC:CHAPSO bicelles |
| Reservoir | ~2 M ammonium sulfate, 100 mM sodium citrate pH 4.75 |
| Mixing ratio | 1:1 |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | 28% glucose (wt/v) in reservoir solution, added in ~6% increments; nicotinic acid at saturating concentration in cryo solution prolonged crystal lifetime |
| Notes | Over 1,500 crystals screened at ALS (BL8.2.1, BL8.2.2). Most WT crystals did not diffract beyond 3.5 A. Best SAD data from single SeMet-labeled crystal at Se edge (lambda=0.9792 A). Initial rigid-body refinement with NavAb-I217C model stalled at Rfree ~40% due to perfect merohedral twinning. Manual placement into experimentally phased SAD map with PHENIX resolved twinning. S5 gating hinge boundaries defined rigid bodies, leading to immediate ~6% drop in Rfree. |

### doi/10.1073##pnas.1700761114

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | NavAb reconstituted in [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/):[CHAPSO](/xray-mp-wiki/reagents/detergents/chapso/) bicelles |
| Reservoir | 1.8 M [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/), 100 mM [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) pH 4.8 |
| Mixing ratio | 1:2 protein:bicelle mix in hanging drop |
| Temperature | not specified |
| Growth time | 3-5 days to appear, ~1 week to full size (~50x100 um) |
| Cryoprotection | Slow addition of well solution supplemented with [Glucose](/xray-mp-wiki/reagents/additives/glucose/) to 30% final |
| Notes | Crystals highly radiation sensitive; data collected at ALS beamlines BL821 and BL822 at 0.9999-1.1000 Å wavelength |


## Biological / Functional Insights

### Wild-type NavAb in two potentially slow-inactivated states

The WT NavAb structure captured two distinct potentially inactivated conformations (NavAb-AB and NavAb-CD) at 3.2 A resolution, revealing asymmetric collapse of the S6 activation gate into a dimer-of-dimers arrangement. Two diagonal S6 helices moved toward the central pore axis while the other two shifted outward, unlike the square array of closed NavAb-I217C. This unprecedented asymmetric activation gate collapse is proposed as a hallmark of the slow-inactivated state in Nav channels, consistent with biophysical studies and disease mutations that affect slow inactivation. (DOI: 10.1038/nature11077)

### Selectivity filter destabilization during slow inactivation

Structural changes in the selectivity filter of WT NavAb include disengagement of the Gln172-Glu177 backbone interaction in NavAb-CD and unlatching of the Thr175-Trp179 network in NavAb-AB. These changes destabilize the selectivity filter, correlating with increased B-factors along the P-helix. This destabilization of the selectivity filter and remodelling of the outer pore vestibule may be required for entry into the inactivated state, consistent with effects of toxin binding, permeant ions, and selectivity filter mutations on slow inactivation in mammalian Nav channels. (DOI: 10.1038/nature11077)

### Evolutionarily conserved network coupling activation gate to selectivity filter

Structure-based alignment identified a conserved network of residues in the NavAb pore module that scaffold the selectivity filter and line surrounding S5/S6 segments: Phe144, Phe152 (S5), Leu170, Phe171 (P-helix), Trp179 (P2-helix), Phe198, Ile202 (S6). Mutations of Leu170 and Ile202 equivalents in Nav1.4 dramatically alter slow inactivation. This network couples intracellular activation gate conformation to the selectivity filter through a mechanism resulting in collapse into a dimer-of-dimers arrangement of all pore functional elements. (DOI: 10.1038/nature11077)

### VSD displacement and coupling to pore during inactivation

The voltage-sensing domains (VSDs) shifted around the perimeter of the pore module in WT NavAb compared to the I217C mutant, with displacements up to ~5 A. A major hinge point at the base of the S5 segment was identified. The VSDs remained in activated conformation but were repositioned relative to the PM, suggesting that pivoting of the VSD around the PM at the S5 gating hinge forces collapse of two S6 segments into the asymmetric dimer-of-dimers conformation at the activation gate. This gating movement is a potential target for next-generation Nav blocking drugs. (DOI: 10.1038/nature11077)

### Closed and open states of the BacNav activation gate

Na_vAb/FY (T206F/V213Y) captures a tightly closed activation gate with I217 and M221
narrowing the pore orifice to 3.2 Å, occluding hydrated Na+ permeation. Na_vAb/1-226
(C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/)) captures an open activation gate with an orifice of ~10.3 Å,
allowing hydrated Na+ permeation. The S6 helix in the closed state is straight, while
in the open state it develops a kink at T206, the hinge residue. These structures
establish the full range of motion of the activation gate from closed (fully occluded)
to open (~10 Å) in a single BacNav channel.

### Hydrophobic gating mechanism for ion permeation

Molecular dynamics and free-energy simulations confirmed that Na_vAb/1-226 represents
an open state allowing permeation of hydrated Na+. The results support a hydrophobic
gating mechanism where changes in the size of a narrow hydrophobic lumen segment shift
the equilibrium between hydrated (wetted) and dehydrated (dewetted) states, enabling or
precluding ion passage. The activation gate induces a small desolvation penalty of
~2 kcal/mol for Na+ in the open state, which doubles to ~4 kcal/mol upon structural
relaxation toward a partially collapsed state.

### C-terminal domain structure of NavAb

The Na_vAb/FY structure reveals the complete four-helix bundle of the C-terminal domain
(CTD). The CTD has a proximal "neck" portion with hydrophilic residues (N225, E228)
on the interior and a distal portion forming a classical four-helix bundle with
hydrophobic residues. Unlike Na_vAep1, NavAb contains only alpha helices in the neck
region (no pi-helix). Removing the CTD in Na_vAb/1-226 favored channel activation and
pore-opening, indicating the CTD influences voltage-dependent activation.

### Closed-open-inactivated conformational cycle

Comparison of NavAb/FY (closed), NavAb/1-226 (open), and NavAb/WT (inactivated) structures
reveals distinct pore diameters: closed (3.2 Å at M221), open (10.3 Å at C217), and
inactivated (intermediate, asymmetric). The S6 segment undergoes twisting/bending motions
that change side chain positions at the central cavity (CC), a target site for sodium
channel-blocking drugs. The transition from open to deep resting states likely has
substantial effects on drug binding, providing structural basis for hyperpolarization-
dependent drug dissociation.

### Drug binding site for local anesthetics and antiarrhythmic drugs in NavAb

Crystal structures of NavAb in complex with [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/) and [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/) reveal the receptor site for LAs and AADs in the central cavity of the pore, on the intracellular side of the selectivity filter. The positively charged amino groups of both drugs point toward the selectivity filter (formed by backbone carbonyl groups of T175). Mutation of T206 to alanine reduces drug potency 17.8-fold for [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/) and 18.5-fold for [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/). [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/) shows fourfold-averaged electron density, while [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/) shows a single well-defined pose.

### Fenestrations control resting-state block by LAs and AADs

Fenestrations in the NavAb pore connect the lipid phase to the central cavity. Mutations of the fenestration cap residue F203 change fenestration size (F203A widens, F203W narrows) without altering pore conformation. For [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/), these cause a 51-fold range in drug potency: F203A IC50 0.9 uM (7.7-fold more potent) to F203W IC50 46 uM (6.5-fold less potent). For [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/), F203W shifts potency 3.4-fold (IC50 458 uM vs 135 uM WT). Effects scale with molecular size.

### Implications for structure-based drug design targeting sodium channels

Fenestration size modulation of drug potency introduces a new concept for structure-based design of LAs, AADs, analgesics, and antiepileptics. Fenestration architecture varies between Nav channel isoforms and can be altered by disease mutations. Differences in binding poses between [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/) (class IB, ventricular arrhythmias) and [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/) (class IC, atrial arrhythmias) may underlie their distinct clinical uses.

### Structural basis of gating pore current in periodic paralysis

High-resolution structures of NavAb with R2G and R3G gating-charge mutations, analogous to those causing hypokalaemic and normokalaemic periodic paralysis in human Nav1.4, reveal the atomic mechanism of pathogenic gating pore currents. The R2G and R3G mutations have no effect on the backbone structure of the voltage sensor but create an aqueous cavity near the hydrophobic constriction site (HCS) that controls gating charge movement. R3G extends the extracellular aqueous cleft through the entire activated voltage sensor, creating a continuous aqueous path. R2G creates a continuous path only in the resting state. Crystal structures of NavAb(R2G) in complex with guanidinium define a potential drug target site. MD simulations show Na+ permeation through the mutant gating pore in concert with conformational fluctuations of gating charge R4.

### Thr206 as a molecular hub for activation-inactivation coupling

Mutation of Thr206 in the S6 segment to Ala or Ser (small side-chain volume ~88-92 A^3) abolishes the early voltage-dependent inactivation during single depolarizations, while mutation to Val (larger volume 141.7 A^3) preserves it. This reveals a size-dependent mechanism: the S6 helix kinks at Thr206 during activation and unkinks during inactivation. In the closed state, Thr206 is ~5 A from Met174 carbonyl; in the open/activated state, it moves to 3.6 A (forming a potential weak H-bond); in the inactivated state, it is 6.1 A away. Smaller side chains at position 206 prevent proper kinking/unkinking dynamics, thereby uncoupling activation from early inactivation. T206A also shifts activation V1/2 by ~25 mV in the negative direction. (DOI: 10.1085/jgp.201711884)

### Two-step model of multiphase inactivation in NavAb

The multiphase slow inactivation of NavAb proceeds via a two-step mechanism. (1) Early voltage-dependent inactivation (during a single depolarization) is triggered by bending of the S6 segment at Thr206, followed by local protein interactions and exchange of hydrogen-bonding partners. The side-chain volume at position 206 determines the kinetics of this early phase. (2) Late use-dependent inactivation (during repetitive depolarizations) requires the C-terminal tail. [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) of 10 residues (NavAbDelta10) from the distal CTD abolishes late use-dependent inactivation at 0.2 Hz, while deleting 3, 7, 28, or 40 residues has graded effects. The C-terminal tail forms a four-helix bundle that is maintained even in large truncations. The hydrophobic distal 20 residues of the CTD (coiled-coil region) stabilize this late inactivation phase. Asymmetric pore collapse occurs during the open-to-inactivated transition, with two S6 segments moving toward the pore axis and two moving away. (DOI: 10.1085/jgp.201711884)


## Cross-References

- [CHAPSO](/xray-mp-wiki/reagents/detergents/chapso/) — Detergent used for bicelle reconstitution and crystallization
- [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/) — Lipid used for bicelle formation in crystallization
- [NavMs Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/navms/) — Related bacterial sodium channel for pore gating comparison
- [Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/) — Local anesthetic and class IB antiarrhythmic drug co-crystallized with NavAb
- [Flecainide](/xray-mp-wiki/reagents/ligands/flecainide/) — Class IC antiarrhythmic drug co-crystallized with NavAb
- [Gating Pore Current (Omega Current)](/xray-mp-wiki/concepts/transport-mechanisms/gating-pore-current/) — NavAb R2G and R3G mutant structures reveal structural basis of gating pore currents in periodic paralysis
- [NCS](/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/) — Related biological concept
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Additive used in purification or crystallization buffers
