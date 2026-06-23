---
title: Human TREK-2 Potassium Channel (KCNK10)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1261512, doi/10.1038##s41467-024-48536-2]
verified: false
---

# Human TREK-2 Potassium Channel (KCNK10)

## Overview

TREK-2 (KCNK10) is a member of the Two-Pore Domain (K2P) potassium
channel subfamily that plays crucial roles in controlling the electrical
activity of many different cell types. TREK-2 is regulated by a wide
variety of physical and chemical stimuli and is expressed within the
central and peripheral nervous systems, with involvement in pain
perception, neuroprotection, and anaesthesia. Like other K2P channels,
each gene encodes a subunit with two pore-forming domains that dimerise
to create a single pseudo tetrameric K+-selective channel. The channel
features a large extracellular Cap domain that is a defining feature of
K2P channels and is gated primarily by structural changes in the
selectivity filter region. TREK-2 gating involves two major
conformations: an up state (conductive) and a down state
(non-conductive), with coordinated movement of transmembrane helices
M2, M3, and M4. The down state features intramembrane-side fenestrations
that serve as binding sites for state-dependent inhibitors including
[Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/) and [Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1261512 | Not deposited | 3.4 | Not specified | Human TREK-2 up state | K⁺ (four ions in filter, conductive state) |
| doi/10.1126##science.1261512 | Not deposited | 3.9 | Not specified | Human TREK-2 down state | K⁺ (three ions in filter, non-conductive state), lipid-like molecules in fenestration |
| doi/10.1126##science.1261512 | Not deposited | 3.7 | Not specified | Human TREK-2 in complex with [Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) (down state) | [Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) |
| doi/10.1126##science.1261512 | Not deposited | 3.64 | Not specified | Human TREK-2 in complex with Br-[Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/) (down state) | Br-[Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/) |
| doi/10.1038##s41467-024-48536-2 | 8QZ1 | Not specified | Not specified | Human TREK-2 residues Gly67 to Glu340 in complex with Nb-Binder-58 (Nb58) | [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) Nb58 |
| doi/10.1038##s41467-024-48536-2 | 8QZ2 | Not specified | Not specified | Human TREK-2 residues Gly67 to Glu340 in complex with Nb-Inhibitor-61 (Nb61) | [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) Nb61 |
| doi/10.1038##s41467-024-48536-2 | 8QZ3 | Not specified | Not specified | Human TREK-2 residues Gly67 to Glu340 in complex with Nb-Activator-67 (Nb67) | [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) Nb67 |
| doi/10.1038##s41467-024-48536-2 | 8QZ4 | Not specified | Not specified | Human TREK-2 residues Gly67 to Glu340 in complex with Nb-Activator-76 (Nb76) | [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) Nb76 |

## Expression and Purification

- **Expression system**: Not detailed in source texts
- **Construct**: Human TREK-2 (KCNK10) with various truncations and modifications
- **Notes**: For [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) structures (doi/10.1038##s41467-024-48536-2), construct was residues Gly67 to Glu340. A glycosylation mutant (N149Q, N152Q, N153Q) was used for some complexes. For the gating structures (doi/10.1126##science.1261512), full functional channel was used.

No purification described.

## Crystallization

### doi/10.1126##science.1261512

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified TREK-2 |
| Notes | Structures solved at 3.4 Å (up state), 3.9 Å (down state), 3.7 Å ([Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) complex), and 3.64 Å (Br-[Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/) complex). Four chains in asymmetric unit. Up state has kinked M4 at Gly312 hinge. Down state similar to [TRAAK](/xray-mp-wiki/proteins/voltage-gated-channels/traak/) and TWIK-1 structures. |

### doi/10.1038##s41467-024-48536-2

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Human TREK-2 (Gly67-Glu340) mixed with [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) in 1:2 TREK-2:[Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) molar ratio |
| Reservoir | Not specified in detail |
| Notes | Crystals of TREK-2/nanobody complexes obtained by vapor diffusion. For Nb67 and Nb61, glycosylation mutant (N149Q, N152Q, N153Q) used. Crystals for Nb76 used crystallisation solution containing Ba²⁺. |


## Biological / Functional Insights

### Two-state gating mechanism (up and down conformations)

TREK-2 adopts two major conformations: the up state (3.4 Å) and
down state (3.9 Å). In the down state, the C-terminal ends of M2,
M3, and M4 project further into the cytoplasm. In the up state,
M4 is kinked at Gly312, and M2/M3 hinge at Gly201/Gly206 and
Gly248 respectively. The up state is conductive with four K⁺ ions
in the filter; the down state is non-conductive with only three
K⁺ ions. This movement represents a C-type gate mechanism at the
selectivity filter.

### Intramembrane fenestrations as drug binding sites

The down state features intramembrane-side fenestrations just
below the selectivity filter. These fenestrations provide a
hydrophobic environment for state-dependent inhibitor binding.
In the up state, the fenestration is closed by upward movement
and rotation of M4, which places Phe316 and Leu320 side chains
into the fenestration. [Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) and [Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/) bind within
the fenestration in the down state, interacting with residues
Ile194, Pro198, Cys249, Val253, Phe316, Leu320, Val276,
Leu279, and Thr280.

### State-dependent inhibition by fluoxetine/norfluoxetine

[Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/) and [Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) exhibit state-dependent inhibition
of TREK-2 by selectively binding to the closed (down) state.
The L320W mutation reduces [Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) inhibition. Channel
activation by membrane stretch or arachidonic acid reduces
[Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) efficacy, consistent with the up state being
the activated conformation that lacks the fenestration binding
site.

### Mechanosensitivity and pH regulation

TREK-2 is sensitive to membrane stretch, arachidonic acid, and
pH. The cytoplasmic end of M4 (Trp326) inserts into the bilayer
in the up state, coupling the cytoplasmic domain to the filter
gate. Extracellular pH sensing involves His156 in a
solvent-accessible extracellular cavity. Lipid-like density on
the channel surface in grooves at the top and bottom of M3 and
M4 may stabilize the down state.

### Nanobody modulation of TREK-2

Four nanobodies were characterized against TREK-2:
Nb-Activator-67 (partial selective activator binding to Cap
domain), Nb-Activator-76 (highly selective EC50 412 nM,
inserting W98 into intersubunit groove), Nb-Inhibitor-61
(IC50 685 nM, inserting K103 into extracellular ion exit
pathway in toxin-like mechanism), and Nb-Binder-58 (functionally
inactive tight binder). A biparatropic [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) (Nb6158) was
engineered with improved inhibitory efficacy.

### Concerted motion of M2, M3, and M4

Transition between up and down states involves coordinated
movement of all three transmembrane helices (M2, M3, M4) in
both chains of the dimer. This is supported by MD simulations
showing downward movement in the up state to adopt a
down-like conformation. Key interactions include Trp326 packing
between Met322 (M4) and Arg327 (M3) in the down state, and
Tyr315 hydrogen bonding with backbone carbonyl of Phe244 (M3)
in the up state.


## Cross-References

- [Human TRAAK Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/traak/) — Related K2P channel with shared fenestration gating mechanism
- [K2P 2.1 (TREK-1) Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/k2p-2-1-trek-1/) — Related TREK subfamily member; TREK-1 I110D mutant structure
- [C-Type Inactivation](/xray-mp-wiki/concepts/c-type-inactivation/) — TREK-2 gating involves selectivity filter (C-type) gating mechanism with up/down state transitions
- [K2P Modulator Pocket](/xray-mp-wiki/concepts/k2p-modulator-pocket/) — The fenestration binding site and nanobody modulation involve the K2P modulator pocket behind the selectivity filter
- [Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) — Additive used in purification or crystallization buffers
- [Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/) — Related ligand or cofactor
- [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) — Fusion tag for crystallization or purification
