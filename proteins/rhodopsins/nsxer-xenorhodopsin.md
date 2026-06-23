---
title: "NsXeR (Xenorhodopsin from Nanosalina)"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.1603187]
verified: false
---

# NsXeR (Xenorhodopsin from Nanosalina)

## Overview

NsXeR is a light-driven inward proton pump (xenorhodopsin) from the nanohaloarchaeon Nanosalina, belonging to the xenorhodopsin (XeR) family of microbial rhodopsins. It functions as an inwardly directed H+ pump, generating a depolarizing current that can elicit action potentials in rat hippocampal neurons. The crystal structure was determined at 2.5 Å resolution by the in meso (LCP) method, revealing a seven-transmembrane α-helix architecture (A-G) with a covalently bound all-trans retinal cofactor via Lys213 Schiff base. The protein forms a trimer in the asymmetric unit (P2₁2₁2₁ space group). Key structural features include a proton uptake cavity accessible from the bulk through Gln122, a unique His48-Asp220 proton acceptor pair (analogous to PRs), and a chain of strong hydrogen bonds (Ile6-Thr199-w5-Ser13-Ser202-w3-Trp73) connecting the extracellular side with the active center. Pro209 is critical for pumping activity, replacing the Asp212 found in bacteriorhodopsin. The photocycle has a turnover rate of ~160 s⁻¹, making NsXeR suitable for optogenetic applications at neuronal firing frequencies up to 40-80 Hz.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##sciadv.1603187 | 6EYU | 2.50 | P2_12_12_1 | Full-length NsXeR from Nanosalina with C-terminal LEHHHHHH tag | all-trans retinal (covalently bound to Lys213) |

## Expression and Purification

- **Expression system**: Escherichia coli C41 (DE3)
- **Construct**: NsXeR with C-terminal LEHHHHHH tag in pET15b

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and membrane preparation | E. coli cells transformed with pET15b-NsXeR, grown in autoinducing medium ZYP-5052 at 37°C with 100 mg/L ampicillin. Induced at OD600 0.6-0.7 with 1 mM IPTG. 10 μM all-trans retinal supplemented. Cells disrupted in M-110P Lab Homogenizer at 25,000 psi. Membrane fraction isolated by ultracentrifugation at 90,000g for 1 h at 4°C. | -- | 20 mM Tris-HCl pH 8.0, 5% glycerol, 0.5% Triton X-100, 50 mg/L DNase I + 0.5% Triton X-100 | Cells disrupted in lysis buffer |
| Solubilization | Membrane pellet resuspended in solubilization buffer and stirred overnight at 4°C. Insoluble fraction removed by ultracentrifugation at 90,000g for 1 h. | -- | 50 mM NaH2PO4/Na2HPO4 pH 8.0, 0.1 M NaCl, 1% DDM + 1% DDM |  |
| Affinity chromatography (Ni-NTA) | Supernatant loaded onto Ni-NTA column. Eluted with imidazole. | Ni-NTA (Qiagen) | 50 mM NaH2PO4/Na2HPO4 pH 7.5, 0.1 M NaCl, 0.3 M imidazole, 0.2% DDM + 0.2% DDM | Eluate dialyzed against 100 volumes of 50 mM NaH2PO4/Na2HPO4 pH 7.5, 0.1 M NaCl buffer twice for 2 h to remove imidazole. Protein concentrated to 70 mg/mL for crystallization. |


## Crystallization

### doi/10.1126##sciadv.1603187

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization (in meso) |
| Protein sample | 30 mg/mL NsXeR (mixed with monoolein-based LCP at 1:1 ratio) |
| Temperature | 22°C |
| Growth time | 1-4 weeks |
| Notes | Crystals grown in 96-well LCP glass sandwich plates using NT8 crystallization robot. 150 nL protein-mesophase mixture overlaid with 600 nL precipitant. Crystal appearance in 1-4 weeks. Space group P2₁2₁2₁ with one trimer per asymmetric unit. X-ray data collected at ESRF ID23-1, ID29, and ID30B beamlines at 0.969 and 0.972 Å with PILATUS 6M detector. Structure solved by molecular replacement using archaerhodopsin-2 (PDB 2EI4) with MoRDa pipeline. Refined with REFMAC5 and PHENIX. |


## Biological / Functional Insights

### Inward proton pumping mechanism

NsXeR is an inwardly directed proton pump, demonstrated by pH changes in E. coli cell suspensions and liposome experiments. Upon illumination, the pH of the cell suspension increases (H+ uptake), opposite to the behavior of outward pumps like bacteriorhodopsin. The effect is abolished by CCCP, confirming active proton transport. Pumping activity is maintained across a wide pH range (pH 5-9).

### Unique proton acceptor pair His48-Asp220

NsXeR features a His48-Asp220 pair as the proton acceptor, analogous to proteorhodopsins but unique among known microbial rhodopsins. His48 is not present at a similar position in other rhodopsins and is essential for retinal binding. Asp220 substitution with Asn completely disrupts pumping. These residues are connected via a hydrogen bond and located 10-12 Å from the Schiff base.

### Distinct proton translocation pathway

The NsXeR structure reveals a proton translocation pathway distinct from bacteriorhodopsin. A proton uptake cavity accessible through Gln122 is filled with water molecules. Pro209 replaces the conserved Asp212 of BR and is critical for pumping. The protein lacks an ionizable residue at the position equivalent to BR Asp96 (Ala71 in NsXeR). A chain of strong hydrogen bonds (Ile6-Thr199-w5-Ser13-Ser202-w3-Trp73) connects the extracellular bulk to the active center. Trp73 separates the active center from the proton uptake pathway and substitution of this residue disrupts pumping.

### Optogenetic application for neuronal activation

NsXeR was functionally expressed in HEK293 cells, NG108-15 cells, and rat hippocampal neurons using adeno-associated virus-mediated gene transfer. Photocurrents of 40-150 pA at -60 mV (current density 1.4 ± 0.5 pA/pF) were recorded in HEK cells. In rat hippocampal neurons, photocurrents of -189 ± 80 pA at -70 mV (6.7 ± 4.4 pA/pF) were sufficient to elicit action potentials at frequencies up to 40-80 Hz, matching the maximal intrinsic firing frequency of hippocampal neurons. Light pulses as short as 3 ms were sufficient to trigger spiking, shorter than the pump turnover time (6.2 ± 2.8 ms).

### Photocycle with 160 s⁻¹ turnover rate

The NsXeR photocycle in nanodiscs is 27 ms (faster than in liposomes at 50 ms). The 160 s⁻¹ turnover rate is approximately 10-fold faster than PoXeR from Parvularcula oceani. Time-resolved photocurrent measurements reveal two relaxation times: τ₁ = 1.1 ms (MI/MII transition) and τ₂ = 11.6 ms (M2 decay). At physiological membrane potential (-60 mV), τ₂ = 6.2 ms, enabling the high turnover rate.


## Cross-References

- [BcXeR (Xenorhodopsin from Bacillus coahuilensis)](/xray-mp-wiki/proteins/rhodopsins/bcxer/) — Related bacterial xenorhodopsin with similar inward proton pumping function and detailed proton wire mechanism
- [Schizorhodopsin SzR4](/xray-mp-wiki/proteins/rhodopsins/schizorhodopsin/) — Another class of inward proton pumps from Asgard archaea, providing a mechanistic comparison to XeRs
- [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) — NsXeR is a member of the microbial rhodopsin family
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — NsXeR exhibits a photocycle with MI and M2 intermediate states
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — All-trans retinal is the chromophore covalently bound via Schiff base to Lys213
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — NsXeR was crystallized using the in meso (LCP) method
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal outward proton pump for comparison of pumping mechanisms
