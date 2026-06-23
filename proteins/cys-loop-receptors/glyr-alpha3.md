---
title: Human Glycine Receptor Alpha 3 (GlyRα3)
created: 2026-05-28
updated: 2026-05-28
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.04.007]
verified: false
---

# Human Glycine Receptor Alpha 3 (GlyRα3)

## Overview

Human [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) receptor alpha 3 (GlyRα3) is a [Pentameric Ligand-Gated Ion Channel (pLGIC)](/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/) belonging to the [Cys-Loop Receptor Family](/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/) family. It mediates fast inhibitory neurotransmission in the central nervous system by allowing chloride ions to flow through its transmembrane pore upon [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) binding. GlyRα3 is the primary isoform responsible for the analgesic effects of delta-9-tetrahydrocannabinol, making it a therapeutic target for neuropathic pain. Crystal structures of GlyRα3 in complex with [Glycine](/xray-mp-wiki/reagents/buffers/glycine/), the potentiator [AM-3607](/xray-mp-wiki/reagents/ligands/am-3607), and [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) have revealed the molecular basis of channel gating and [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) in vertebrate Cys-loop receptors.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2017.04.007 | 5VDH | 2.85 A | P43212 | GlyRα3 crystallization construct | AM-3607, glycine, ivermectin |
| doi/10.1016##j.str.2017.04.007 | 5VDI | 3.08 A | P2121 | GlyRα3 crystallization construct with N38Q mutation | AM-3607, glycine, ivermectin |

## Expression and Purification

- **Expression system**: Not specified in this paper
- **Construct**: GlyRα3 crystallization construct and N38Q mutant. Construct details from Huang et al., 2016.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | As described in Huang et al., 2016 | -- | -- + -- | Construct details from Huang et al., 2016 |
| Purification | As described in Huang et al., 2016 | -- | -- + -- | Purification protocol from Huang et al., 2016 |

**Final sample**: --


## Crystallization

### doi/10.1016##j.str.2017.04.007

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) |
| Protein sample | GlyRα3cryst or GlyRα3crystN38Q pre-equilibrated with [AM-3607](/xray-mp-wiki/reagents/ligands/am-3607), [Glycine](/xray-mp-wiki/reagents/buffers/glycine/), and [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) |
| Reservoir | 100 mM [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) pH 6.5, 50 mM CaCl2 |
| Mixing ratio | 1:1 protein to reservoir |
| Temperature | 4 C |
| Cryoprotection | [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg)350MME |
| Notes | Two crystal forms solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with Phaser. 5VDH in space group P43212 at 2.85 A resolution. 5VDI in space group P2121 at 3.08 A resolution. |


## Biological / Functional Insights

### Ivermectin binding site and pore expansion mechanism

[Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) binds in the transmembrane domain of GlyRα3 at the interface between adjacent subunits, acting as a positive [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/). The binding pocket is formed by the M2, M3, and M4 helices at the plus subunit interface. Key residues include Ser267 on M2 and Ala288 on M3. Binding of [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) causes the M2 helices to tilt outward at the extracellular end while tapering inward at the intracellular end, rotating the 9' Leu261 residues out of the pore and expanding the extracellular portion of the channel. The expanded extracellular pore is stabilized by inter-subunit hydrogen bonds between Arg271 (M2+) and Gln226 (M1-). The direct binding of [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) wedges apart M3(+) and M1(-) by about 3 Angstroms and drags M2 away from the pore axis, opening the ion channel.

### Desensitized state of GlyRα3

The crystal structures of AM-3607/glycine/ivermectin-bound GlyRα3 delineate a partially open or desensitized state. While the M2 helices tilt outward and the 9' Leu261 residues rotate out of the pore, the radius at the intracellular end defined by the -2' Pro250 is only 1.4 A, too narrow to permit chloride passage. Thus -2' Pro250 serves as the desensitization gate. The desensitized state is essentially identical to the desensitized GlyRα1 structure, with the intracellular half of the TMD tilting away from the pore in both open and desensitized states.

### Structural basis for ivermectin selectivity between GlyR and GluCl

Comparison with the [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/)-bound [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl) structure reveals why [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) activates GlyRs less potently than invertebrate glutamate-gated chloride channels. Ala288 in the M3 helix of GlyRα3 at the mouth of the [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) binding cleft is replaced by a smaller Gly281 in [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl). As a result, [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) is buried about 1 A deeper in the cleft of [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl) than in GlyRα3, leading to higher [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) potency for [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl). C10 of [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) is 4.7 A from the C-alpha of Ala288 in GlyRα3 but only 3.5 A from the C-alpha of Gly281 in [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl). This is consistent with functional data where wild-type [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl) and the Ala288Gly mutant of GlyRα1 show an [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) EC50 of around 40 nM, while wild-type GlyRα1 has an EC50 of 1.2 uM.

### Therapeutic implications for neuropathic pain

The analgesic effects of delta-9-tetrahydrocannabinol are mediated through potentiation of GlyRα3, particularly via binding in the transmembrane domain with Ser296 of M3 being critical for THC potentiation. Ser296 is only about 7 A from the [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) binding site in the GlyRα3 crystal structures. These structures provide a valuable structural basis for screening and designing novel pain therapeutics that act on the transmembrane domain of GlyRα3.


## Cross-References

- [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Prokaryotic Cys-loop receptor homolog; model system for anesthetic action on pLGICs
- [GLIC ECD](/xray-mp-wiki/proteins/cys-loop-receptors/glic-ecd/) — Isolated extracellular domain of GLIC; related Cys-loop receptor structure
- [Ketamine](/xray-mp-wiki/reagents/ligands/ketamine/) — Anesthetic ligand binding to Cys-loop receptors; related allosteric modulation
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — Ivermectin acts as a positive allosteric modulator of GlyR
- [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) — Positive allosteric modulator binding to transmembrane domain of GlyRα3
- [AM-3607](/xray-mp-wiki/reagents/ligands/am-3607/) — Novel analgesic potentiator binding to GlyRα3 transmembrane domain
- [2-(N-Morpholino)ethanesulfonic Acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Crystallization buffer at pH 6.5 used for GlyRα3 crystal forms 5VDH and 5VDI
- [Calcium Chloride (CaCl₂)](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Crystallization additive (50 mM) used for GlyRα3 crystal forms 5VDH and 5VDI
- [Pentameric Ligand-Gated Ion Channel (pLGIC)](/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/) — Referenced in glyr-alpha3
- [Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) — Referenced in glyr-alpha3
