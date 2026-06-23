---
title: Human Beta-2 Adrenergic Receptor (β2AR)
created: 2026-06-08
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aaw8981, doi/10.1107##S2052252519013137]
verified: false
---

# Human Beta-2 Adrenergic Receptor (β2AR)

## Overview

The human beta-2 adrenergic receptor (β2AR) is a prototypic class A G-protein-coupled receptor that plays essential roles in cardiovascular and respiratory physiology, and is the therapeutic target of beta-blockers and beta-agonists. Multiple crystal structures have been determined using both synchrotron and X-ray free-electron laser (XFEL) sources. The active-state β2AR in complex with orthosteric agonist [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/), [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) 6B9 (Nb6B9), and positive allosteric modulator Compound-6FA was determined at 3.2 A resolution (Liu et al., Science 2019, PDB 6N48). Using [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) (SFX) with lipidic sponge phase ([LSP](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/lipidic-sponge-phase/)) crystallization, eight room-temperature co-crystal structures with six different ligands were determined at 2.8-4.0 A resolution (Ishchenko et al., IUCrJ 2019), including previously unreported structures with [Carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) and propranolol. The LSP-SFX approach enabled rapid determination of multiple GPCR co-crystal structures from submilligram quantities of protein.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aaw8981 | 6N48 | 3.2 | P212121 | T4L-β2AR fusion (N-terminal T4 lysozyme fused to human β2AR) expressed in insect cells; complex formed with orthosteric agonist [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/), [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) 6B9 (Nb6G9), and positive allosteric modulator Cmpd-6FA; [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) occupancy ensures active-state stabilization | [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) (orthosteric agonist), Cmpd-6FA (positive allosteric modulator), Nb6B9 ([Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) G-protein mimetic) |
| doi/10.1107##S2052252519013137 | 6PRZ | 2.9 | -- | T4L-β2AR fusion protein expressed in Sf9 insect cells; purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/CHS; crystallized in lipidic sponge phase ([LSP](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/lipidic-sponge-phase/)) with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)/cholesterol/PEG 400; SFX data collection at SACLA; room temperature structure | [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) (high-affinity agonist) |
| doi/10.1107##S2052252519013137 | 6PS0 | 3.2 | -- | T4L-β2AR as above; crystallized in [LSP](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/lipidic-sponge-phase/) with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)/cholesterol/PEG 400; SFX data collection at SACLA | [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) (inverse agonist, β-blocker) |
| doi/10.1107##S2052252519013137 | 6PS1 | 3.4 | -- | T4L-β2AR as above; LSP-SFX | Timolol (non-selective β-blocker antagonist) |
| doi/10.1107##S2052252519013137 | 6PS2 | 3.2 | -- | T4L-β2AR as above; LSP-SFX | ICI-118,551 (selective β2AR inverse agonist) |
| doi/10.1107##S2052252519013137 | 6PS3 | 3.7 | -- | T4L-β2AR as above; LSP-SFX | [Carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) (biased β-blocker, β-arrestin-biased agonist) |
| doi/10.1107##S2052252519013137 | 6PS4 | 4.0 | -- | T4L-β2AR as above; LSP-SFX | Propranolol (non-selective β-blocker antagonist) |
| doi/10.1107##S2052252519013137 | 6PS5 | 2.8 | -- | T4L-β2AR as above; LSP-SFX; crystallized with [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) and [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) | [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) (competition with [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/)) |
| doi/10.1107##S2052252519013137 | 6PS6 | 2.8 | -- | T4L-β2AR as above; LSP-SFX | [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) (high resolution dataset) |

## Expression and Purification

- **Expression system**: Insect cell expression system (Sf9, baculovirus)
- **Construct**: T4L-β2AR fusion protein; N-terminal T4 lysozyme fused to β2AR for crystallogenesis

### Purification Workflow

*Source: doi/10.1126##science.aaw8981*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and purification | Expression in insect cells; T4L-β2AR purified in presence of agonist [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) | -- | -- + -- | Expression and purification details are described in previous references (Rosenbaum et al., Nature 2011; Rasmussen et al., Nature 2011; Ring et al., Nature 2013). The T4L-β2AR fusion maintains Cmpd-6 PAM activity. |
| Complex formation | T4L-β2AR bound to [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/), Nb6B9; Cmpd-6FA (3 mM) included in crystallization solution | -- | -- + -- | Cmpd-6FA (acetic acid derivative of Cmpd-6) was used at 3 mM (solubility limit) in crystallization condition. Cmpd-6FA has ~6-fold higher solubility than the parent Cmpd-6 and recapitulates its pharmacological properties. |

### Purification Workflow

*Source: doi/10.1107##S2052252519013137*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression in Sf9 insect cells | Baculovirus expression system | -- | -- + -- | T4L-β2AR fusion expressed in Sf9 cells; harvested 48 h post-infection |
| Membrane preparation and solubilization | Differential centrifugation; solubilization in 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | -- | 20 mM HEPES pH 7.5, 100 mM NaCl + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Purified in presence of [Alprenolol](/xray-mp-wiki/reagents/ligands/alprenolol/) to stabilize receptor |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA followed by alprenolol-Sepharose [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA, alprenolol-Sepharose | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Final protein concentrated to ~30 mg/ml with 10 μM [Alprenolol](/xray-mp-wiki/reagents/ligands/alprenolol/) |


## Crystallization

### doi/10.1126##science.aaw8981

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization |
| Protein sample | T4L-β2AR-BI-167107-Nb6B9 complex with 3 mM Cmpd-6FA |
| Reservoir | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Crystals were obtained of the active T4L-β2AR bound to [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) and Nb6B9 in a crystallization condition saturated with 3 mM of Cmpd-6FA. The structure was resolved to 3.2 A by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using the T4L-β2AR-Nb6B9 structure (PDB 4LDO) as the search model. |

### doi/10.1107##S2052252519013137

| Parameter | Value |
|---|---|
| Method | Lipidic sponge phase ([LSP](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/lipidic-sponge-phase/)) crystallization for SFX |
| Protein sample | T4L-β2AR at ~30 mg/ml in 20 mM HEPES pH 7.5, 100 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |
| Temperature | 20 C |
| Growth time | 2-4 days |
| Notes | [LSP](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/lipidic-sponge-phase/) prepared by mixing [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)/cholesterol with buffer containing [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 and sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/). Protein solution mixed with lipid mixture using syringe mixer. Crystallization in 96-well glass sandwich plates. For each ligand, microcrystals grew within 2-4 days. SFX data collected at SACLA BL2, 10 keV, 10 μm beam, 50 mm detector distance. Data indexed with CrystFEL; structures solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using β2AR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) (PDB 4LDO) as search model. |


## Biological / Functional Insights

### Novel intracellular allosteric binding pocket on β2AR

Cmpd-6FA binds in a previously unpredicted allosteric pocket at the interface between the cytoplasm and membrane, formed by transmembrane helices 2, 3, 4, and intracellular loop 2 (ICL2). The pocket was not identified in prior fragment-based molecular dynamics druggability scans (Ivetac & McCammon, 2010), demonstrating that known receptor crystal structures may still harbor unidentified allosteric sites. The binding site is subdivided into three surface regions: membrane-embedded, membrane-proximal, and cytoplasmic surfaces.

### ICL2 alpha-helix stabilization mechanism of PAM activity

Cmpd-6FA stabilizes the active-state conformation of ICL2 as a two-turn alpha-helix, which is required for G-protein engagement. In the inactive-state, ICL2 exists as a random coil. The formation of the ICL2 alpha-helix requires inward displacement of Pro138(ICL2), resulting in ~3 A inward movement of TM3, which dictates outward movement of TM5 and TM6 — a hallmark of GPCR activation. This explains the positive allosteric effect: Cmpd-6FA increases the population of receptors adopting active conformations with higher affinity for agonists.

### Mechanism distinct from M2 muscarinic PAM

Unlike the M2 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptor PAM [LY2119620](/xray-mp-wiki/reagents/ligands/ly2119620/), which binds within the extracellular vestibule to directly prevent agonist dissociation, Cmpd-6FA acts through a distinct mechanism — stabilizing the active-state of the receptor with a closed hormone-binding site, thereby retarding agonist dissociation (agonist trapping effect). This mechanism does not involve direct steric occlusion of the orthosteric site.

### Subtype selectivity determinants between β2AR and β1AR

Only 7 of 14 residues forming the Cmpd-6FA allosteric site are conserved between β2AR and β1AR. Cmpd-6 enhances agonist binding 31-fold for β2AR but only 2.8-fold for β1AR. Mutagenesis studies identified residues at positions 3.52 (Phe133 in β2AR vs Leu158 in β1AR) and 4.41 (Lys149 in β2AR vs Arg174 in β1AR) as the major determinants of subtype selectivity. The double mutant β1AR(L158F/R174K) conferred a 20-fold increase in agonist affinity with Cmpd-6.

### LSP-SFX enables rapid multi-ligand GPCR structure determination

Using [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) (SFX) with lipidic sponge phase ([LSP](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/lipidic-sponge-phase/)) crystallization, eight room-temperature co-crystal structures of β2AR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) were determined with six different ligands at 2.8-4.0 A resolution (Ishchenko et al., IUCrJ 2019). The [LSP](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/lipidic-sponge-phase/) yields thousands of uniformly sized isomorphous microcrystals per microliter of protein solution, requiring only submilligram quantities of protein. This approach enabled the first crystal structures of β2AR with [Carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) and propranolol, and demonstrated the feasibility of rapid multi-ligand SBDD for GPCRs using XFEL sources.

### Carvedilol binding mode reveals biased agonism mechanism

The β2AR-[Carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) structure (PDB 6PS3, 3.7 A) reveals a unique binding mode where the carbazole group extends deep into the orthosteric pocket while the ethanolamine moiety interacts with D113(3.32) and N312(7.39). [Carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) makes an additional hydrogen bond with Y316(7.43), which may contribute to its biased signaling profile as a β-arrestin-biased agonist that inhibits Gs signaling while promoting β-arrestin recruitment.

### Diverse orthosteric binding pocket conformations

The six ligands in the β2AR LSP-SFX study produce distinct conformations of the orthosteric binding pocket. Inverse agonists ([Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/), ICI-118,551) stabilize the inactive conformation with the ionic lock between R131(3.50) and E268(6.30) intact. The agonist [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) shifts the pocket toward an active-like conformation. Propranolol adopts a binding mode similar to [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/). Timolol occupies the pocket with different interactions than the other β-blockers, reflecting its distinct pharmacological profile.


## Cross-References

- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — Method generality demonstrated with A2AR LSP-SFX structures (caffeine, ZM241385)
- [Biased Agonism](/xray-mp-wiki/concepts/signaling-receptors/biased-agonism/) — Carvedilol binding mode reveals structural basis of β-arrestin-biased agonism
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion used for all β2AR structures in this study
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Standard detergent for GPCR purification and stabilization
- [LSP](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/lipidic-sponge-phase/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — Method used in structure determination or purification
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
