---
title: "CIR Chloride-Pumping Rhodopsin from Nonlabens marinus"
created: 2026-06-08
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NCOMMS12677, doi/10.1038##ncomms12677, doi/10.1073##pnas.2020486118, doi/10.1073##pnas.2117433119, doi/10.1126##sciadv.aay2042, doi/10.1126##science.abj6663]
verified: false
---

# CIR Chloride-Pumping Rhodopsin from Nonlabens marinus

## Overview

CIR (Chloride-pumping Rhodopsin/rhodopsin 3, also called NmHR) from the
flavobacterium Nonlabens marinus S1-08 is a light-driven inward chloride
pump containing an NTQ motif (Asn98, Thr102, Gln109) in its putative ion
conduction pathway, distinct from the TSA motif of archaeal
[Halorhodopsin](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/). The crystal structures were determined under multiple
conditions using lipidic cubic phase crystallization, revealing
chloride-binding sites around the protonated Schiff base (PSB) of the
[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore. Time-resolved serial femtosecond crystallography
(TR-SFX) combined with time-resolved spectroscopy and multiscale
simulations elucidated the complete molecular mechanism of chloride
transport from picosecond to millisecond timescales. Key features include
an anion-&#x3C0; interaction between chloride and the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) &#x3C0;-system,
a steric molecular gate (Asn98) preventing backflow, and an electrostatic
gate (Arg95-Asp231 salt bridge) ensuring unidirectional transport.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NCOMMS12677 | 5G28 | 2.0 | P 3 2 1 | CIR from Nonlabens marinus S1-08, type A crystal at pH 6.0 | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion |
| doi/10.1038##NCOMMS12677 | 5G54 | 1.56 | P 3 2 1 | CIR from Nonlabens marinus S1-08, type B crystal at pH 4.5 | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion |
| doi/10.1038##NCOMMS12677 | 5G2A |  | — | CIR from Nonlabens marinus S1-08, bromide-soaked | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), bromide ion |
| doi/10.1038##NCOMMS12677 | 5G2D |  | — | CIR T102N mutant | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion |
| doi/10.1073##pnas.2020486118 | 7CRJ | 1.65 | C 1 2 1 | CIR dark state (TR-SFX reference structure) | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion |
| doi/10.1073##pnas.2020486118 | 7CRI | 1.85 | C 1 2 1 | CIR 1 ps after photoactivation (TR-SFX) | 13-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion (dissociating) |
| doi/10.1073##pnas.2020486118 | 7CRK | 1.85 | C 1 2 1 | CIR 2 ps after photoactivation (TR-SFX) | 13-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion (moving toward Thr102) |
| doi/10.1073##pnas.2020486118 | 7CRL | 1.85 | C 1 2 1 | CIR 50 ps after photoactivation (TR-SFX) | 13-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion (near Thr102) |
| doi/10.1073##pnas.2020486118 | 7CRS | 1.85 | C 1 2 1 | CIR 100 ps after photoactivation (TR-SFX, 0.90 mJ/mm2) | 13-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion (relaxed at Thr102) |
| doi/10.1073##pnas.2117433119 | 7VGT | 2.1 | — | NM-R3 resting state (XFEL structure, bromide-bound) | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), bromide ion |
| doi/10.1073##pnas.2117433119 | 7VGU | 2.1 | — | NM-R3 1 ms after photoactivation (TR-SFX, O1 intermediate) | 13-cis/15-syn [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), bromide ion (released) |
| doi/10.1073##pnas.2117433119 | 7GVG |  | — | NM-R3 anion-depleted form (P2(1)2(1)2(1) crystal form) | 13-cis/15-syn [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), no halide bound (Asn98 occupies anion site) |
| doi/10.1126##science.abj6663 | 7O8F |  | — | NmHR dark state and time-resolved structures at 10 ps, 1 us, 20 us, 300 us, 12.5 ms, 22.5-45 ms (TR-SFX at SwissFEL and SLS) | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride/bromide ion |
| doi/10.1038##NCOMMS12677 | 5G2C | 2.0 | P1 (T102D mutant crystal) | ClR T102D mutant | All-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) (chloride binding prevented) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21-CodonPlus
- **Construct**: CIR from Nonlabens marinus S1-08 with C-terminal 6xHis tag (residues 1-272)
- **Induction**: 0.5 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) + 50 uM all-trans-retinal for 6-8 h at 30 C

### Purification Workflow

#### Source: doi/10.1038##NCOMMS12677


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest and lysis | Centrifugation and mechanical disruption | — |  |  |
| Solubilization and affinity chromatography | Ni-NTA affinity chromatography | — | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |

#### Source: doi/10.1073##pnas.2020486118


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and expression | E. coli expression with [Iptg](/xray-mp-wiki/reagents/additives/iptg/) induction | — |  | Cells grown in high-salt LB medium at 37 C; induced at OD600 > 1.0 |
| Cell lysis and membrane isolation | Sonication and ultracentrifugation | — | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) HCl pH 7.0, 150 mM NaCl | Membrane fraction isolated by ultracentrifugation at 370,000 x g for 40 min at 4 C |
| Membrane solubilization | Detergent extraction | — | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) HCl pH 7.0, 150 mM NaCl + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% CHS | Solubilization for 2 h at 4 C |
| Affinity purification and SEC | [Talon](/xray-mp-wiki/reagents/additives/talon/) affinity chromatography followed by size-exclusion chromatography | [Talon](/xray-mp-wiki/reagents/additives/talon/) affinity resin; [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluate applied to [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) column for final purification |

#### Source: doi/10.1073##pnas.2117433119


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and purification | E. coli expression with [Iptg](/xray-mp-wiki/reagents/additives/iptg/) induction, Ni-NTA affinity, SEC | Ni-NTA; [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | NM-R3 purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for LCP crystallization. Crystals grown in 1500 mM NaBr or NaI for halide replacement. |

#### Source: doi/10.1126##science.abj6663


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and purification | E. coli expression and purification for TR-SFX | — | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Purified NmHR used for LCP crystallization and TR-SFX experiments at SwissFEL and SLS |


## Crystallization

### doi/10.1038##NCOMMS12677

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (in meso) crystallization |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Temperature | 20 |
| Cryoprotection | 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) in reservoir solution |
| Notes | Type A crystals at pH 6.0 diffracted to 2.0 A; type B crystals at pH 4.5 diffracted to 1.56 A. Data at Pohang Accelerator Laboratory. Structures solved by molecular replacement using [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (PDB 1C3W). |

### doi/10.1073##pnas.2020486118

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization for TR-SFX |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Temperature | Room temperature |
| Notes | Microcrystals grown in LCP for TR-SFX at LCLS. Dark state at 1.65 A; time delays: 1 ps to 100 ps after 550 [NM](/xray-mp-wiki/reagents/detergents/nm/) fs-pumping laser. |

### doi/10.1073##pnas.2117433119

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization for TR-SFX at SACLA |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Temperature | Room temperature |
| Notes | Microcrystals grown in LCP for TR-SFX at SACLA BL3. Time delays: 10 us and 1 ms after 540 [NM](/xray-mp-wiki/reagents/detergents/nm/) or 532 [NM](/xray-mp-wiki/reagents/detergents/nm/) pump laser. |

### doi/10.1126##sciadv.aay2042

| Parameter | Value |
|---|---|
| Method | Single-crystal microspectrophotometry and cryo-crystallography |
| Temperature | 95 K and 140 K |
| Cryoprotection | Cryocooled under cold nitrogen gas stream |
| Notes | Single crystals subjected to CW laser (532 [NM](/xray-mp-wiki/reagents/detergents/nm/)) or pulsed laser (532 [NM](/xray-mp-wiki/reagents/detergents/nm/), 10 kHz). Data at Pohang Accelerator Laboratory. |

### doi/10.1126##science.abj6663

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization for TR-SFX |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Temperature | Room temperature |
| Notes | NmHR crystallized in LCP for time-resolved serial crystallography at SwissFEL XFEL and Swiss Light Source synchrotron. Bromide-soaked crystals continuously illuminated with 520-nm laser diode during delivery for photostationary state data. Time delays from picoseconds to milliseconds. Crystals in space group with chloride/bromide concentration affecting kinetics. |


## Biological / Functional Insights

### NTQ motif and chloride binding at the Schiff base

The CIR structure reveals a chloride ion (Cl-I) bound at the protonated Schiff base (PSB), positioned 3.1 A from the Schiff base nitrogen. Cl-I directly interacts with the conserved Asn98 and Thr102 of the NTQ motif, as well as PSB. This is distinct from archaeal [Halorhodopsin](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) where chloride is coordinated by the TSA motif. Mutation of Asn98 or Thr102 eliminates or substantially reduces chloride-pumping activity, demonstrating the essential role of these residues in chloride binding and transport.

### Anion-&#x3C0; interaction with the retinal chromophore

Time-resolved crystallography and QM/MM simulations revealed that the transient Cl352-binding site at 1 us is stabilized by an anion-&#x3C0; interaction between the chloride ion and the conjugated &#x3C0;-electron system of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore. The stabilization is dominated by the electrostatic component between chloride and the protonated Schiff base (PSB), with additional contribution from the C14-C15=N fragment of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/). The polarization of the &#x3C0;-electron density by the negative charge of the chloride resembles common interactions between anions and &#x3C0; electrons of aromatic rings. This interaction supports transient chloride ion binding across a major bottleneck in the transport pathway, enabling the anion to pass over the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore.

### PSB flip drives the first step of chloride transport

At 10 ps after photoactivation, the protonated Schiff base of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) flips from pointing toward the extracellular side to pointing toward the cytoplasm. The chloride ion Cl351 shifts away from the PSB (distance increases from 3.1 A to 4.1 A), breaking the hydrogen bond. QM/MM simulations indicate 28.2 kcal/mol of energy is stored upon charge separation between the PSB and Cl351 at 10 ps, corresponding to more than half of a green light photon (530 [NM](/xray-mp-wiki/reagents/detergents/nm/), 53.9 kcal/mol). At 1 us, the chloride is dragged through the Cl352-binding site over the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore via the anion-&#x3C0; interaction.

### Steric molecular gate prevents chloride backflow

At 20 us, the relaxation of a kink in helix C moves the side chain of Asn98 into the chloride-free Cl351 site, acting as a sterically closing molecular gate that prevents reverse flow of chloride. Asn98 replaces Cl351 and interacts with water molecules Wat484 and Wat407. Additional stabilization is achieved by a new hydrogen bond between Thr102 and the carbonyl group of the Asn98 backbone, sealing the gate. Thr102 plays multiple roles: coordinating Cl351 in the resting state, assisting chloride transfer to Cl352 by rotamericization, and sealing the molecular gate to prevent backflow.

### Cl- release through Gln109 of the NTQ motif

At 20 us, the Cl353-binding site emerges above the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/), 14 A from Cl352 toward the cytoplasm. The site is accessed through water molecules Wat401 and Wat402 and formed by Gln109 of the conserved NTQ motif, Ser54, and Thr243. Gln109 is at a strategic position for ion pumps: the equivalent residue in [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) is Asp96 (internal proton donor), and in [Kr2](/xray-mp-wiki/proteins/rhodopsins/kr2/) is Gln123 (involved in sodium transport). This suggests that pumping rhodopsins share sections of the transport pathway despite different substrate charge and size.

### Electrostatic gate at Arg95-Asp231 ensures unidirectional transport

An electrostatic gate formed by a salt bridge between Arg95 and Asp231 controls chloride uptake from the extracellular side. QM/MM simulations confirmed Asp231 is in anionic form, supporting the presence of this salt bridge. When chloride diffuses to the Wat409 position, it interferes with the Arg95-Asp231 electrostatic attraction, causing Asp231 to rotate and interact with His29 instead. This opens the electrostatic gate, creating a pathway for the anion to the Cl355-binding site (4 A from Cl351). After recharging the resting state, the electrostatic gate closes again, preventing anion leakage back into bulk solvent and ensuring vectorial transport.

### Complete chloride transport pathway

The combined time-resolved experiments enabled tracing of five transient anion-binding sites (Cl351-Cl355) and elucidation of the complete chloride transport pathway in NmHR. The pathway involves: (1) PSB flip at 10 ps, storing photon energy as charge separation; (2) chloride passage over the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) via anion-&#x3C0; interaction at 1 us; (3) steric gate closure by Asn98 at 20 us preventing backflow; (4) release through Gln109 to Cl353 site; (5) ordering of surface residues for Cl- release at 300 us; (6) electrostatic gate opening at Arg95-Asp231 for chloride uptake from extracellular side; (7) recharging of Cl351 site and gate closure. The mechanism combines steric and electrostatic gating with anion-&#x3C0; interactions to achieve light-driven unidirectional chloride transport.

### NM-R3 chloride pathway mapping by cryo-crystallography

Single-crystal cryo-crystallography with difference Fourier maps (light-minus-dark) at multiple laser intensities revealed the chloride ion conduction pathway of NM-R3. On photoexcitation, the Schiff base chloride (Cl-1) moves slightly to Cl-1B, then to Cl-5 (between Ser60 and Cys105) and Cl-6 (near Cys105, Ala125, Ile129) toward the cytoplasmic face. An additional chloride ion (Cl-3) enters near Phe90 from the extracellular side, and Cl-4 arrives near the PSB region from the extracellular face via Cl-3. These five discrete chloride positions map the complete anion conduction pathway in a light-driven chloride pump.

### TR-SFX reveals picosecond chloride dissociation dynamics

Time-resolved serial femtosecond crystallography (TR-SFX) captured the dynamics of Cl- ion transport upon photoactivation. [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomerization from all-trans to 13-cis occurs in 1 ps, flipping the C12-C13=C14-C15 torsion angle from 179 degrees to 4 degrees. The Cl- ion dissociates from the PSB within 1 ps, moving 1.3 A toward the extracellular side as the electrostatic interaction with the protonated Schiff base is abruptly lost. By 50-100 ps, the Cl- ion moves toward Thr102, revealing a dissociation-diffusion mechanism rather than the dipole switching model.

### TR-SFX reveals millisecond-scale gating dynamics during chloride pumping

TR-SFX data at 10 us and 1 ms after photoactivation of NM-R3 revealed the conformational alterations during ion transfer and after ion release. At 10 us (L/N intermediate), the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomerizes and moves toward helix C, the iodide ion bound to the PSB displaces toward Thr102, and Trp201 shifts toward the cytoplasmic side. Asn98 moves toward the anion binding site, distorting helix C. At 1 ms (O1 intermediate), the halide ion is released from the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) binding pocket. The [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) adopts a 13-cis/15-syn configuration. Inward movements of helix C and helix G and lateral displacements of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) block access from the extracellular side, preventing backflow of anions.

### Comparison with KR2 and archaeal halorhodopsins

NM-R3 and [Kr2](/xray-mp-wiki/proteins/rhodopsins/kr2/) share identical key ion transfer residues except Thr102 versus Asp116, yet pump oppositely charged ions. In [Kr2](/xray-mp-wiki/proteins/rhodopsins/kr2/), the O1 state at 1 ms shows Na+ near Asn112 and Asp251; in NM-R3, the O1 state shows larger inward movements of helix C and helix G, and [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) adopts 13-cis/15-syn configuration (versus 13-cis/15-anti in [Kr2](/xray-mp-wiki/proteins/rhodopsins/kr2/)). NM-R3 shares structural similarities with NpHR despite low sequence identity and different key motifs (NTQ vs TSA). The chloride-binding site coordinated by Gln105 in HsHR does not align with the anion uptake pathway in NmHR, whereas the NpHR N-state site is near Cl352 in NmHR. Large conformational changes in helix C of NpHR and the existence of a salt bridge next to the resting-state chloride-binding site in HsHR and NpHR suggest that molecular gates may be a general feature of [Halorhodopsin](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) ion pumps.

### Hydrophobic gate opening at Leu106

Leu106 on TM-C is a major hydrophobic residue on the chloride pathway to the cavity near Gln109. In the dark state, the channel between Cl-1 and the cavity near Gln109 is blocked. At 100 ps after activation, the Leu106 side chain moves away from TM-G by about 0.6 A, suggesting the initial stages of hydrophobic gate opening that may facilitate Cl- migration to the cytoplasmic side in later stages of the photocycle.


## Cross-References

- [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) — CIR/NmHR is a member of the microbial rhodopsin family of light-driven ion pumps
- [NTQ Motif in Chloride Pumping Rhodopsins](/xray-mp-wiki/concepts/transport-mechanisms/ntq-motif/) — The NTQ motif (Asn98, Thr102, Gln109) defines the chloride-pumping rhodopsin family and plays multiple roles in chloride binding, transport, and gating
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal microbial rhodopsin; comparison reveals mechanistic equivalence and differences in ion transport
- [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) — Archaeal halorhodopsin with TSA motif; convergent evolution for chloride pumping
- [Lipidic Cubic Phase (In Meso) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for all CIR/NmHR structures including TR-SFX experiments
- [Time-Resolved Serial Femtosecond Crystallography (TR-SFX)](/xray-mp-wiki/methods/structure-determination/time-resolved-serial-femtosecond-crystallography/) — Primary method used to capture picosecond to millisecond dynamics of chloride transport
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Referenced in the context of Retinal
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in the context of Iptg
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in the context of DDM
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in the context of Hepes
- [pharaonis Halorhodopsin (phR)](/xray-mp-wiki/proteins/rhodopsins/pharaonis-halorhodopsin/) — Archaeal inward chloride pump with TSA motif; convergent evolution comparison
- [Retinal Chromophore Conformation](/xray-mp-wiki/concepts/structural-mechanisms/retinal-chromophore-conformation/) — All-trans retinal is the chromophore in ClR
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) — Related protein structure
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — CIR functions through a rhodopsin photocycle
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Used in cell wash buffers
- [Oleic Acid](/xray-mp-wiki/reagents/lipids/oleic-acid/) — Binds to CIR C-terminal helix on TM A
