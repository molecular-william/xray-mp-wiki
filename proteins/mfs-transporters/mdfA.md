---
title: "MdfA Multidrug Efflux Transporter"
created: 2026-05-27
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2018.02.026, doi/10.1038##cr.2015.94, doi/10.1038##s41467-018-06306-x]
verified: false
---

# MdfA Multidrug Efflux Transporter

## Overview

MdfA is a secondary multidrug efflux transporter from Escherichia coli belonging to the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)). It functions as a drug/proton antiporter that exports a broad spectrum of chemically dissimilar toxic compounds, including neutral, zwitterionic, and monovalent cationic drugs. MdfA is fueled by the proton electrochemical potential. Crystal structures of the MdfA(Q131R) mutant have been determined with bound ligands [deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/) (PDB 4ZP0, 2.0 A), [chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/) (PDB 4ZOW, 2.4 A), and [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) (PDB 4ZP2, 2.2 A), revealing the substrate-binding mode of an [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) antiporter. A double mutant MdfA(Q131R/L339E) was crystallized at 2.2 A resolution (PDB 6EUQ). Studies revealed that membrane-embedded MdfA assumes a relatively stable inward-closed conformation that is further stabilized by substrates and [deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2018.02.026 | 6EUQ | 2.2 A | P21 | MdfA(Q131R/L339E) double mutant with [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [hexahistidine](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag | [deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/) (DXC) |
| doi/10.1038##cr.2015.94 | 4ZP0 | 2.0 A | P212121 | MdfA(Q131R) mutant with [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [hexahistidine](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag | [deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/) (DXC) |
| doi/10.1038##cr.2015.94 | 4ZOW | 2.4 A | P212121 | MdfA(Q131R) mutant with [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [hexahistidine](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag | [chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/) |
| doi/10.1038##cr.2015.94 | 4ZP2 | 2.2 A | P212121 | MdfA(Q131R) mutant with [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [hexahistidine](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag | [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) |
| doi/10.1038##s41467-018-06306-x | 6GV1 | 3.4 A | P6_1_22 | MdfA WT in complex with Fab YN1074 (stabilizing antibody fragment), [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [hexahistidine](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag | none (outward open, substrate-free state) |

## Expression and Purification

- **Expression system**: E. coli UTL2 mdfA::Kan
- **Construct**: MdfA-6His or various mutants overexpressed from multi-copy plasmids (pUC18/Para/mdfA-6His or pT7-5/mdfA-6His) under arabinose-inducible promoter

### Purification Workflow

#### Source: doi/10.1016##j.jmb.2018.02.026


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and membrane preparation | E. coli cells grown at 37 C, diluted and induced with 0.2% arabinose for 18 h at 16 C. Cells disrupted by pressure cell homogenizer at 15 kPsi. Membranes collected by [ultracentrifugation](/xray-mp-wiki/methods/purification/ultracentrifugation/) at 167,000g for 1 h. | -- | 50 mM KPi pH 7.3, 2 mM MgSO4, 10 ug/mL [DNase](/xray-mp-wiki/reagents/additives/dnase/), 1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf/) + -- | Membranes resuspended in 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 0.5 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) and stored at -80 C |
| Solubilization | Membranes solubilized with 1.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (10% stock), insoluble material removed by [ultracentrifugation](/xray-mp-wiki/methods/purification/ultracentrifugation/) at 167,000g for 30 min | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 0.5 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 1.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Solubilized at 4 C for 2 hr |
| [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-[affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) using [Talon](/xray-mp-wiki/reagents/additives/talon/) beads, washed with solubilization buffer, eluted with 200 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) | [Talon](/xray-mp-wiki/reagents/additives/talon/) beads (Clontech) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.2, 0.5 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 200 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Agitated for 2 hr at 4 C, eluted in 30 column volumes of wash buffer |
| Dialysis and concentration | Dialyzed overnight against dialysis buffer at 4 C, protein concentration determined by A280 (1 mg/mL = 2.1 A280) | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.2, 0.12 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Purified MdfA used for binding assays, crystallization, and MD simulations |


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| MdfA(Q131R/L339E) purification for crystallization | Membranes solubilized with 0.5% DM ([DM](/xray-mp-wiki/reagents/detergents/dm/)), [Talon](/xray-mp-wiki/reagents/additives/talon/) [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/), [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) on [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200) 10/30 column | [Talon](/xray-mp-wiki/reagents/additives/talon/) beads (Clontech) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 0.5 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.2% DM, 5 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.2% DM ([DM](/xray-mp-wiki/reagents/detergents/dm/)) | Concentrated to 10 mg/mL before [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) |
| Size-exclusion chromatography | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200) 10/30 column pre-equilibrated with [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) buffer | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200) 10/30 (GE Healthcare) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5 mM [beta-mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 1.2 mM sodium [deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/) (omitted in some experiments), 0.2-0.4% n-nonyl-beta-D-glucopyranoside (Anatrace), 0.025% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) (Anatrace) + 0.2-0.4% NG (n-nonyl-beta-D-glucopyranoside), 0.025% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) | Peak fractions pooled and concentrated to 15 mg/mL for crystallization |

#### Source: doi/10.1038##cr.2015.94


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression and membrane preparation | Full-length MdfA gene cloned from E. coli BL21(DE3) genome. Overexpressed in E. coli C43 (DE3) with [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [His6](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag, induced with 0.5 mM [IPTG](/xray-mp-wiki/methods/expression-systems/iptg-induction/) at OD600 0.8, grown at 16 C for 18 h. Cells homogenized at 10,000-15,000 p.s.i., membrane fraction collected by [ultracentrifugation](/xray-mp-wiki/methods/purification/ultracentrifugation/) at 100,000g for 1 h. | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM [beta-mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) + -- | Incidental Q131R mutation introduced during cloning; considered WT |
| Solubilization | Membrane fraction solubilized with 0.5% DM for 2 h at 4 C, clarified by [ultracentrifugation](/xray-mp-wiki/methods/purification/ultracentrifugation/) at 100,000g for 30 min | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM [beta-mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 0.5% DM + 0.5% DM ([DM](/xray-mp-wiki/reagents/detergents/dm/)) | Solubilized at 4 C for 2 hr |
| [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) affinity resin, washed with 20 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/), eluted with 350 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) (Qiagen) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM [beta-mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 0.2% DM, 350 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.2% DM | Concentrated to 10-15 mg/mL |
| Size-exclusion chromatography | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200) 10/30 column pre-equilibrated with [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) buffer | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200) 10/30 (GE Healthcare) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5 mM [beta-mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 1.2 mM sodium [deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/), 0.2% n-nonyl-beta-D-glucopyranoside, 0.025% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) + 0.2% NG (n-nonyl-beta-D-glucopyranoside), 0.025% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) | Peak fractions pooled and concentrated to 15 mg/mL before crystallization |


## Crystallization

### doi/10.1038##cr.2015.94

| Parameter | Value |
|---|---|
| Method | [hanging-drop](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) [vapor diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) |
| Protein sample | 15 mg/mL MdfA(Q131R) in 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5 mM [beta-mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 1.2 mM sodium [deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/), 0.2% NG, 0.025% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) |
| Reservoir | 50 mM [sodium acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) pH 5.8, 20-24% (v/v) [PEG 400](/xray-mp-wiki/reagents/additives/peg-400/), 10 mM praseodymium [Acetate Buffer](/xray-mp-wiki/reagents/buffers/acetate), 50 mM magnesium [Acetate Buffer](/xray-mp-wiki/reagents/buffers/acetate) |
| Temperature | 16 C |
| Growth time | About 3 days |
| Cryoprotection | Reservoir solution |
| Notes | Crystals grew to 20 x 20 x 50 um in about 3 days. Se-Met derivative crystals grown under same conditions. Cm-containing crystals obtained by [soaking](/xray-mp-wiki/methods/crystallography/soaking/) original crystals in reservoir solution supplemented with 5.0 mM [chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/). [LDAO](/xray-mp-wiki/reagents/detergents/ldao/)-bound structure obtained when crystallization pH was adjusted from 5.8 to 8.5. PDB 4ZOW (Cm complex, 2.4 A), 4ZP0 (Dxc complex, 2.0 A), 4ZP2 ([LDAO](/xray-mp-wiki/reagents/detergents/ldao/) complex, 2.2 A). Phases obtained by [molecular replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/). |


## Biological / Functional Insights

### Substrate-binding mode in MFS antiporters

The crystal structures of MdfA in complex with three distinct ligands ([chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/),
[deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/), and [LDAO](/xray-mp-wiki/reagents/detergents/ldao/)) reveal the substrate-binding mode of an [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) antiporter. The
substrate-binding site sits proximal to the conserved acidic residue D34. Twelve amino
acid residues form the binding cavity, with over two-thirds being hydrophobic. Key
residues Y30, N33, and D34 from motif-D form [hydrogen bonds](/xray-mp-wiki/concepts/hydrogen-bonding/) with [chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/).
D34 directly interacts with the substrate while E26 is not directly involved in binding.
The binding of hydrophobic substrates reduces the dielectric constant inside the cavity,
enhancing the electrostatic field and affecting protonation status.

### Protonation and substrate binding competition

In antiporters, substrate binding and protonation compete with each other. MdfA has
two proton-titratable residues in the central cavity: E26 and D34. D34 is directly
involved in substrate binding while E26 is over 8 A away. Substrate binding induces
deprotonation of D34, triggering the Cin-to-Cout [conformational change](/xray-mp-wiki/concepts/structural-mechanisms/conformational-change/). Motif-B
(R112xxQG) generates a positive electrostatic field that promotes deprotonation of
D34 in the Cin state. A proton-wire mechanism involving conserved Y30 may facilitate
proton transfer between E26 and D34.

### Conformational changes upon substrate binding

[smFRET](/xray-mp-wiki/methods/biophysical/smfret/) imaging revealed that Cm binding induces closure of the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) side of
MdfA, shifting the conformation to the Cin state. Mutations in motif-C (P154A,
P158A) destabilize the Cin state and favor the Cout conformation. Motif-C specifically
evolved to stabilize the hydrophobic inter-domain interaction of [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) antiporters in
the Cin state. The proline residues in motif-C introduce kinks in the TM helix and
participate in water-mediated interactions at the inter-domain interface.

### Outward open conformation and TM5 switching mechanism

The crystal structure of MdfA in the outward open (Oo) conformation (PDB 6GV1, 3.4 A, P6_1_22), trapped by Fab YN1074, reveals the transporter with the N- and C-lobes closely apposed at the intracellular face, sealing off the cytoplasmic entrance via a hydrophobic plug centered around Phe340(TM10). Comparison with the inward-facing (If) state shows the two lobes rotate as rigid bodies by 33.5 degrees about an axis parallel to the membrane. TM5 undergoes a dramatic conformational change: a 15-degree kink and ca. 45-degree clockwise twist, driven by the antiporter motif C (AlaProXaaXaaGlyPro) that is absent in symporters and uniporters. Critical residue Met146(TM5) disengages from the N-terminal domain and engages the C-terminal domain in the Oo state, while Tyr127(TM4) shifts to form a hydrogen bond with Glu26(TM1). MD simulations suggest that protonation of Asp34(TM1) triggers transition from Oo to an occluded state, while Glu26 protonation is not rate-limiting for chloramphenicol transport. These findings establish MdfA as a model system for understanding conformational switching in MFS MDR antiporters.

### Conserved motifs in MFS antiporters

Four motifs (A-D) are conserved in [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) antiporters. Motif-A stabilizes the Cout
state. Motif-B (R112xxQG in TM4) contains an essential basic residue that generates
a positive electrostatic field promoting D34 deprotonation. Motif-C (the antiporter
motif in TM5) stabilizes the Cin state through inter-domain hydrophobic interactions.
Motif-D contains the two titratable acidic residues E26 and D34 essential for
transport activity.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — MdfA belongs to the MFS, the largest family of bacterial drug transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — MdfA functions via alternating access between inward-facing and outward-facing states
- [Rocker-Switch Mechanism in MFS Transporters](/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/) — MFS-specific transport mechanism used by MdfA
- [Substrate-Protonation Coupling in MFS Symporters](/xray-mp-wiki/concepts/transport-mechanisms/substrate-protonation-coupling/) — MdfA substrate binding induces deprotonation of D34, driving transport
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for MdfA solubilization and purification
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Used for MdfA(Q131R) purification for crystallization
- [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/ldao/) — Used as crystallization additive and bound ligand in MdfA-LDAO structure (PDB 4ZP2)
- [Deoxycholate (DXC)](/xray-mp-wiki/reagents/additives/deoxycholate/) — Bound ligand in MdfA-Dxc structure (PDB 4ZP0) and used in SEC buffer
- [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) — Entity mentioned in text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Entity mentioned in text
