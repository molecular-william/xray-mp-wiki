---
title: MthK (Methanobacterium thermoautotrophicum K⁺ Channel)
created: 2026-05-28
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein]
sources: [doi/10.1016##j.str.2012.09.014, doi/10.1038##nature01580, doi/10.1038##nsmb.1531]
verified: false
---

# MthK (Methanobacterium thermoautotrophicum K⁺ Channel)

## Overview

MthK is a calcium-activated potassium channel from the archaeon Methanobacterium thermoautotrophicum. It is a prototypical RCK (Regulator of K⁺ conductance)-containing channel whose structure provided foundational insight into mechanisms of channel gating by cytoplasmic ligand-binding domains. The channel consists of a transmembrane pore domain and a tethered octameric gating ring of RCK domains that control channel opening in response to calcium and other divalent cation binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2012.09.014 | 4EI2 | 3.1 | P2₁2₁2₁ | Cytoplasmic RCK domain gating ring (octamer) | Ba²⁺ |

## Expression and Purification

No purification described.

## Crystallization

### doi/10.1016##j.str.2012.09.014

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 6 mg/ml purified MthK RCK domain, 250 mM NaCl, 20 mM Tris pH 8.0 |
| Reservoir | 28% PEG 300, 100 mM BaCl₂, 100 mM Tris pH 8.5 |
| Temperature | 4 C or room temperature |
| Growth time | Several days to weeks |
| Cryoprotection | Rapid freezing in liquid N₂ without additional cryoprotection |


## Biological / Functional Insights

### Ba²⁺ binds to the C1 activation site

Ba²⁺ selectively binds to the C1 activation site in each RCK domain, which overlaps
with the known Ca²⁺ activation site. The C1 site is determined by residues D184 and
E210. Ba²⁺ coordination at C1 involves close contacts with D184(Oδ1) at 2.6 Å, the
main-chain carbonyl of L185 at 2.8 Å, and more distant contacts with D184(Oδ2) at
4.0 Å and E210(Oε1) at 3.8 Å. Additional Ba²⁺ sites (B2-B4) were observed at lower
occupancy but did not exhibit multiple close protein contacts.

### Ba²⁺ activates MthK channels through the C1 site

Electrophysiological recordings show that Ba²⁺ can activate reconstituted MthK
channels, with EC₅₀ values of 54.8-81.1 mM depending on pH. The activation is
completely reversible. Ba²⁺ activation is abolished by the D184N mutation,
confirming that Ba²⁺ activates primarily through the C1 site. Mg²⁺ up to 100 mM
was ineffective at activating MthK channels.

### Intermediate-activated conformation

Comparison of Ca2+-bound and Ba2+-bound gating ring structures reveals that the
Ba2+-bound form exists in an intermediate-activated conformation, distinct from the
fully activated Ca2+-bound form. This suggests a sequential activation mechanism
where binding of additional ligands is required for maximal stability of the fully
activated conformation.

### Open pore comparison with NaK

The open NaK structure (NaKN delta 19, PDB 2AHY open form) superimposes with open MthK (PDB 1LNQ) with an r.m.s.d. of 0.74 A for all three components (outer, inner, and pore helices). This structural equivalence confirms that MthK is a valid model for the open conformation of tetrameric cation channels beyond K+-selective channels. The conserved gating mechanics include inner helix bending at the glycine hinge (Gly87 in NaK) and a 45 degree twist around the helical axis. In MthK, the equivalent position to NaK's Phe92 is occupied by alanine, resulting in a wider pore (~9.5 A vs 6.5 A in NaK).


## Cross-References

- [Barium Chloride](/xray-mp-wiki/reagents/additives/barium-chloride/) — Ba²⁺ used as activator and crystallization ligand for MthK gating ring
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — PEG 300 used as crystallization precipitant at 28% concentration
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Tris buffer at pH 8.0 and 8.5 used in purification and crystallization
- [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/kvap/) — KvAP open pore nearly as wide as opened MthK; glycine-gating hinge mechanism shared between channels
- [NaK Channel from Bacillus cereus](/xray-mp-wiki/proteins/nak-channel/) — Open NaK structure superimposes with MthK (PDB 1LNQ, r.m.s.d. 0.74 A); MthK serves as the model for open tetrameric cation channel pore; both share conserved gating mechanics including glycine-hinge bending and inner helix twisting
