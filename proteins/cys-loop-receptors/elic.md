---
title: "ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.51511, doi/10.1038##s41589-019-0369-4, doi/10.1074##jbc.M112.424507]
verified: false
---

# ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)

## Overview

ELIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from the bacterium Erwinia chrysanthemi (now Dickeya dadantii). It is a homopentameric channel gated by GABA that serves as a bacterial homolog of eukaryotic Cys-loop receptors including nicotinic  receptors,  5-HT3 receptors, GABA-A receptors, and  receptors. ELIC has been extensively used as a model system for understanding pLGIC structure, allosteric modulation, and ion channel gating. The channel exhibits distinct Ω-loop conformations at the vestibule entrance that determine access to an allosteric binding site, with ELIC adopting the Ω-open conformation that creates an accessible vestibule site.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.51511 | 6SSI | 2.59 | Not specified | ELIC + PAM-Nb complex |  |
| doi/10.7554##eLife.51511 | 6SSP | 3.25 | Not specified | ELIC + NAM-Nb complex |  |
| doi/10.1074##jbc.M112.424507 | 3ZKR | 3.65 | P2_1 | Full-length ELIC (wild-type) in complex with  |  (three binding sites: channel pore, transmembrane intersubunit, extracellular domain) |
| doi/10.1038##ncomms1703 | 2VL0 | 3.28 | — | ELIC wild-type |  |
| doi/10.1038##s41589-019-0369-4 | 6HJX | 2.50 | Not specified | ELIC 7'C pore mutant (L238C) bound to  72 (Nb72); highest resolution ELIC structure to date |  (PE), [Sodium Ion (Na+)](/xray-mp-wiki/reagents/ligands/sodium-ion/) |
| doi/10.1038##s41589-019-0369-4 | 6HJY | 2.78 | Not specified | ELIC Delta8 deletion mutant (M4 C-terminal 8 residues deleted) bound to Nb72 |  |
| doi/10.1038##s41589-019-0369-4 | 6HK0 | Not specified | Not specified | ELIC F16'S mutant with alternative unkinked M4 conformation |  |

## Expression and Purification

- **Expression system**: E. coli C43
- **Construct**: Signal sequence of human α7 nAChR followed by mature ELIC sequence, pGEM-HE plasmid
- **Notes**: Also expressed in Xenopus oocytes for electrophysiology using the pGEM-HE expression plasmid

### Purification Workflow

#### Source: doi/10.7554##eLife.51511

- **Expression system**: E. coli C43
- **Expression construct**: Full-length ELIC in pGEM-HE or similar expression vector

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | LB medium | — |  | Expression induced with 200 uM  |
| Cell lysis | Not detailed in this paper | — |  | Referenced to Spurny et al. 2012 methods |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | IMAC | Ni-NTA |  | Referenced to Spurny et al. 2012 for standard ELIC purification protocol |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | — |  | ELIC purified in detergent solution prior to  complex formation |
|  complex formation | Co-incubation | — |  | Purified ELIC incubated with excess PAM-Nb or NAM-Nb prior to crystallization |

#### Source: doi/10.1038##s41589-019-0369-4

- **Expression system**: E. coli C43
- **Expression construct**: MBP-ELIC fusion with 3C protease cleavage site; ELIC cDNA cloned into pET-11a with N-terminal [MBP (Escherichia coli Maltose-Binding Protein)](/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/) fusion tag
- **Tag info**: N-terminal [MBP (Escherichia coli Maltose-Binding Protein)](/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/) fusion tag removed by 3C protease

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | LB medium | — |  | C43 E. coli grown to A600 ~1.8, induced with 200 uM  at 20 C overnight |
| Membrane preparation | Ultracentrifugation | — |  | Membrane fraction collected at 125,000g |
| Membrane solubilization | Detergent solubilization | — | 10 mM Na-phosphate pH 8.0, 150 mM NaCl, 0.15%  + 2% [UDM](/xray-mp-wiki/reagents/undecylmaltoside/) () | Solubilized at 4 C overnight |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Amylose resin affinity | Amylose resin (New England Biolabs) |  | Batch purification on amylose resin; column-bound ELIC cleaved by 3C protease in presence of 1 mM  + 1 mM  at 4 C overnight |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | Superdex 200 10/300 GL | 10 mM Na-phosphate pH 8.0, 150 mM NaCl, 0.15%  | Final purification step; concentrated protein (10 mg/mL) supplemented with 0.5 mg/mL E. coli lipids |

#### Source: doi/10.1074##jbc.M112.424507

- **Expression system**: E. coli
- **Expression construct**: ELIC cDNA in pGEM-HE or similar vector

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Referenced to previously described protocols | — |  | Expression and purification of ELIC performed as described in the original ELIC structure paper |
| Purification | Referenced to previously described protocols (Hilf and Dutzler, 2008) | — |  | Purified ELIC protein concentrated and exchanged into buffer containing  for crystallization |
| Electrophysiology | [TEVC](/xray-mp-wiki/methods/quality-assessment/two-electrode-voltage-clamp/) in Xenopus oocytes | — |  | cRNA transcribed from linearized pGEM-HE plasmids. Oocytes injected with 30 nl cRNA (100 ng/nl). Recordings at -60 mV (ELIC) or -80 mV (GlyR) using Axoclamp 900A or HiClamp apparatus. Currents sampled at 100 Hz, low pass-filtered at 10 Hz. |


## Crystallization

### doi/10.7554##eLife.51511

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | ELIC + PAM-Nb complex |
| Temperature | Room temperature |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | ELIC + NAM-Nb complex |
| Temperature | Room temperature |

### doi/10.1038##s41589-019-0369-4

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | ELIC 7'C mutant + Nb72 complex, 10 mg/mL supplemented with 0.5 mg/mL E. coli lipids |
| Temperature | Room temperature |
| Notes | Crystals grown using E. coli lipid extract (58% PE, 15% PG, 10% ) as essential crystallization additive. Structure solved at 2.5 A resolution. |

### doi/10.1074##jbc.M112.424507

| Parameter | Value |
|---|---|
| Method | Not specified (likely vapor diffusion) |
| Protein sample | Purified ELIC with 1 mM  |
| Notes | Crystals of ELIC- complex. Two data sets collected: crystal 1 at 3.65 A resolution (P2_1, a=105.11, b=266.25, c=110.75 A, beta=109.78 deg) and merged data from three crystals at 5.0 A resolution (a=105.63, b=266.33, c=110.97 A, beta=108.63 deg). Data collected at Swiss Light Source X06A beamline. |


## Biological / Functional Insights

### Nanobodies as allosteric modulators of ELIC

PAM-Nb acts as a positive allosteric modulator with EC50 of 4.2 uM (pEC50 5.37) and Imax of 257%, enhancing GABA-evoked responses. NAM-Nb acts as a negative allosteric modulator with IC50 of 0.13 uM (pIC50 6.89) and inhibition to 34% of control, with inhibition plateauing at ~70% of GABA alone, consistent with NAM mechanism rather than competitive antagonism.

### PAM-Nb and NAM-Nb bind distinct allosteric sites on ELIC

PAM-Nb binds at an intrasubunit site in the ELIC extracellular ligand binding domain, overlapping with the CU2017 small molecule fragment binding site (a NAM in related pLGICs). NAM-Nb binds at the channel vestibule entrance near the N-terminal alpha-helix, adjacent to the flurazepam binding site (a PAM in ELIC). Remarkably, each  has the opposite functional effect of the small molecule at the same site, demonstrating that the same allosteric site can support both positive and negative modulation depending on side chain interactions.

### Omega-loop conformations control vestibule site access

The outer rim of the vestibule site (residues N60-F95 in ELIC) adopts one of three conformations across pLGICs: Ω-in, Ω-out, and Ω-open. ELIC and 5-HT3A receptors adopt the Ω-open conformation, creating an accessible vestibule site. Anionic receptors (GlyR, GABA-AR, ) adopt Ω-out which occludes access. Some nAChR subunits adopt Ω-in which also occludes access. The Ω-open conformation is the only one that leaves the vestibule site accessible for allosteric modulation.

### Vestibule site modulation is conserved between ELIC and human 5-HT3A receptor

Cysteine-scanning mutagenesis (SCAM) of the 5-HT3A receptor vestibule site showed that modification of residues L151C, T112C, and K149C with MTSEA-biotin causes a leftward shift of the concentration-activation curve (PAM effect), confirming functional conservation of the vestibule allosteric site between ELIC and an evolutionarily distant human pLGIC. L151C showed the largest effect (~50-fold EC50 decrease toward wild-type value).

### Phospholipid binding site at M1-M4 interface shapes ELIC function

A high-resolution (2.5 A) structure of ELIC 7'C mutant bound to Nb72 reveals a  (PE) molecule at a site in the lower half of the TMD, located between M1 and M4 helices of one subunit and M3 of the neighboring subunit. The lipid site is shaped by a conserved M4-helix Pro kink (P305) and a Trp-Arg-Pro triad (W224-R301-P305) that is highly conserved in eukaryotic GABA-A/C and  receptors. This site overlaps with known binding sites for neurosteroids in GABA-A receptors and  in the alpha1beta2gamma2 GABA-A receptor, suggesting functional conservation across prokaryote and eukaryote channels.

### M4 helix dynamics and lipid interactions regulate ELIC desensitization

Mutagenesis of the lipid-binding site residues (F274A, I281A, W220A, P305A, W224R) each accelerates desensitization in ELIC. The P305A mutation, which disrupts the M4-helix Pro kink that shapes the lipid-binding site, exhibits a particularly rapid desensitization rate. Reconstitution of ELIC into liposomes with different lipid compositions also alters desensitization kinetics, with PE-containing lipids slowing desensitization. Deletion of up to 7 C-terminal M4 residues has little effect on expression or function, but deletion of 8+ residues or the entire M4 helix (DeltaM4) produces rapid desensitization similar to alpha7 nAChR.

### Alternative unkinked M4 conformation reveals mechanism of lipid regulation

An alternate crystal structure (PDB 6HK0) and MD simulations reveal that M4 can adopt an unkinked conformation, tilting by up to 19.4 A (measured at I317 C-alpha) to interact with M3 of the neighboring subunit. In this conformation, M4 is pinched between W220 and W224 in M1, sterically hindering access to the lipid-binding site. Disulfide crosslinking experiments (L278C/F308C and F274C/I311C) confirm that this alternate conformation is sampled under detergent-solubilized conditions. Voltage clamp fluorometry (VCF) studies show conformational changes in post-M4 residues during channel opening.

### Conservation of kinked M4 fold in anion-selective pLGICs

The architectural feature of a kinked M4 helix with a Pro kink and Trp-Arg triad is conserved in eukaryotic anion-selective pLGICs (GABA-A/C and  receptors) but not in cation-selective pLGICs (nAChR, 5-HT3R). This suggests that the mechanistic insights from ELIC about lipid modulation of channel desensitization extend across the anion-selective subfamily of pLGICs. The phospholipid-binding site closely overlaps with known sites for neurosteroids, , and general anesthetics, offering strategies for designing therapeutics that modulate channel function in human disease.

### Multisite binding of general anesthetics to ELIC

The -bound ELIC structure reveals three distinct anesthetic binding sites, supporting a multisite model of allosteric modulation in pLGICs. Site 1 (channel pore):  binds between 9'L and 16'F near 13'A of the M2-helix, constricting the pore radius (to 1.1-2.5 A vs 1.5-3.3 A in apoELIC). The L9'S mutation eliminates  inhibition, and F16'S significantly reduces it. Site 2 (transmembrane intersubunit): a novel site at the interface between M1/M4 of one subunit and M3 of the neighboring subunit, lined by Trp-221, Trp-225, Phe-275, and Pro-307. This pre-existing cavity is absent in  and . Site 3 (extracellular): a hydrophobic pocket between beta7-beta10 strands involving Leu-128 and Ile-195. Equivalent sites in human  receptors (F295, Y301 in alpha1 GlyR) affect  modulation when mutated. Together with previously identified propofol/desflurane and alcohol/ sites, these findings substantiate multisite allosteric modulation by general anesthetics in the pLGIC family.


## Cross-References

- [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Homologous prokaryotic pLGIC often studied alongside ELIC
- [HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid)](/xray-mp-wiki/reagents/buffers/hepes/) — Used in electrophysiology recording buffers
- [n-Undecyl-beta-D-maltoside (UDM)](/xray-mp-wiki/reagents/detergents/udm/) — Detergent used for ELIC purification
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in nanobody expression and purification
- [MES (2-(N-Morpholino)ethanesulfonic Acid) Buffer](/xray-mp-wiki/reagents/buffers/buffer-mes/) — Buffer used in ELIC-PAM-Nb crystallization
- [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) — PAM-Nb and NAM-Nb are camelid-derived nanobodies engineered as allosteric modulators
- [Negative Allosteric Modulation](/xray-mp-wiki/concepts/signaling-receptors/negative-allosteric-modulation/) — NAM-Nb is a negative allosteric modulator of ELIC
- [Positive Allosteric Modulation](/xray-mp-wiki/concepts/structural-mechanisms/positive-allosteric-modulation/) — PAM-Nb is a positive allosteric modulator of ELIC
- [sTeLIC (Tevnia jerichonana Endosymbiont pLGIC)](/xray-mp-wiki/proteins/cys-loop-receptors/stelic/) — Homologous prokaryotic pLGIC with 28% sequence identity; crystallized in an open/active conformation
- [Phosphatidylethanolamine (PE)](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) — Phospholipid bound at ELIC M1-M4 interface revealed in 2.5 A crystal structure
