---
title: "SLC26Dg (Deinococcus geothermalis Fumarate Transporter)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3091]
verified: false
---

# SLC26Dg (Deinococcus geothermalis Fumarate Transporter)

## Overview

SLC26Dg is a prokaryotic fumarate transporter from the bacterium Deinococcus geothermalis, representing the first full-length structure of an SLC26 family member. It functions as a proton-coupled fumarate symporter, transporting dicarboxylic acids across the membrane in an electrogenic process. The SLC26 (SulP) family of anion transporters is ubiquitous in pro- and eukaryotes and includes human members whose malfunction causes severe diseases such as growth defects, chronic diarrhea, and deafness. The human protein Prestin, an SLC26 member that confers electromotility to cochlear outer hair cells, shares 46% residue similarity with SLC26Dg in its transmembrane region. The structure reveals a modular architecture combining a 14-helix transmembrane domain with a cytoplasmic STAS domain, providing a common framework for the diverse functional behavior of the SLC26 family.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.3091 | 5DA0 | 3.2 | C2 | Full-length SLC26Dg from D. geothermalis in complex with nanobody Nb5776 | Nanobody Nb5776 (crystallization aid); ligand-free conformation |
| doi/10.1038##nsmb.3091 | 5IOF | 4.2 | P1 | SLC26Dg deltaSTAS (residues 1-401, truncated STAS domain) from D. geothermalis | None |

## Expression and Purification

- **Expression system**: Escherichia coli MC1061
- **Construct**: SLC26Dg with C-terminal HRV 3C protease site, GFP, and His10 tag. Grown in Terrific Broth with ampicillin, induced with 0.005% L-arabinose at 25 C for 16 h.
- **Induction**: 0.005% L-arabinose
- **Media**: Terrific Broth with [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell resuspension and lysis | Osmotic shock and Emulsiflex C3 disruption | -- | 50 mM potassium phosphate pH 7.5, 150 mM NaCl, 1 mM [MGCL2](/xray-mp-wiki/reagents/additives/mgcl2), 1 mg/ml lysozyme + -- | Cells resuspended and incubated with lysozyme at 4 C for 1 h before disruption |
| Membrane vesicle preparation | Ultracentrifugation | -- | 50 mM potassium phosphate pH 7.5, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + -- | Membrane vesicles obtained after low-spin centrifugation and ultracentrifugation |
| Solubilization | Detergent solubilization | -- | 50 mM potassium phosphate pH 7.5, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 1-1.5% n-decyl-beta-D-maltoside (DM, Anatrace) | Membrane proteins extracted for 1 h at 0.1 g/ml in buffer A supplemented with DM |
| Affinity purification | Immobilized metal affinity chromatography (IMAC) | Ni-NTA resin | Buffer containing [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) + DM | Solubilized SLC26Dg purified by IMAC; HRV 3C protease cleavage during dialysis against buffer without [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) |
| Tag removal and SEC | Size-exclusion chromatography | Superdex S200 column (GE Healthcare) | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM NaCl + 0.2% DM | Histidine-tagged GFP and protease removed by IMAC; cleaved protein concentrated and subjected to SEC |


## Crystallization

### doi/10.1038##nsmb.3091

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | SLC26Dg-Nb5776 complex at molar ratio 1:3; full-length monomeric SLC26Dg in complex with Nb5776 |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Full-length transporter initially yielded crystals at 7-A resolution; improved crystals at 3.2-A obtained after generating nanobodies against SLC26Dg and using them as crystallization aids. Space group C2, single copy in asymmetric unit. SAD phasing from [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-derivatized transporter. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | SLC26Dg deltaSTAS (truncated construct, residues 1-401) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Truncated construct crystallized readily in several conditions. Best crystal form space group P1 diffracting to 4.2-A resolution. |


## Biological / Functional Insights

### Inward-facing, ligand-free conformation with potential substrate-binding site

The SLC26Dg structure reveals an inward-facing conformation with a large 28-A-long and 8-A-wide aqueous cavity at the interface between the core and gate domains. A putative substrate-binding site sits at the center of the transporter. The cavity is lined predominantly by hydrophobic residues, with unpaired backbone amides at the N termini of helices 3 and 10 providing hydrogen-bond donors for interaction with the two carboxylates of fumarate. Two pseudosymmetry-related glutamates (E38 and E241) lie adjacent to the ligand-binding site with their carboxylate moieties oriented toward the cytoplasm; these residues are conserved in prokaryotic but not eukaryotic SLC26 transporters and may facilitate substrate release and proton cotransport.

### Transmembrane domain architecture with inverted repeats

The transmembrane domain of SLC26Dg consists of 14 alpha-helices organized into two structurally related halves of seven TM segments each, forming intertwined inverted repeats. The pseudosymmetry-related helices 1-4 and 8-11 fold into a compact core domain, while helices 5-7 and 12-14 form an elongated gate domain that shields one side of the core. This architecture resembles the unrelated [URAA](/xray-mp-wiki/proteins/uraA) transporter (NCS2 family), aligning with an RMS deviation of 3.5 A despite no obvious sequence relationship. This structural conservation supports predictions of relatedness between SLC26, NCS2, and SLC4 families.

### STAS domain regulates transport activity

The cytoplasmic STAS domain is compact, containing four beta-strands and three alpha-helices, and shows structural similarity to STAS domains of Prestin and DauA. Expression of the isolated TM domain (SLC26Dg deltaSTAS) produced a stable protein but with strongly compromised transport activity, demonstrating that the STAS domain regulates the transport activity of the TM domain. The STAS domain interacts exclusively with the [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody) Nb5776 via complementarity determining region 2, burying 1505 A^2 of combined molecular surface.

### Electrogenic proton-fumarate symport mechanism

Transport experiments demonstrate that SLC26Dg functions as a proton-coupled fumarate symporter. Transport is strongly enhanced by an inwardly directed pH gradient and is electrogenic, with fumarate/proton symport increased by positive and decreased by negative membrane potential. The apparent Km for fumarate is 2.7 mM, indicating weak affinity. The cumulative charge of substrates per cycle is negative. Competition assays show specificity for dicarboxylates over other anions.


## Cross-References

- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Primary solubilization detergent (1-1.5%) for SLC26Dg membrane extraction
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Used at 10 mM pH 7.5 in SEC buffer for SLC26Dg purification
- [Potassium Phosphate](/xray-mp-wiki/reagents/buffers/potassium-phosphate/) — Resuspension buffer (50 mM pH 7.5) for cell lysis
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — 150 mM NaCl in purification buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — 10% glycerol in membrane vesicle buffer
- [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) — Nb5776 used as crystallization aid, binds STAS domain
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to obtain improved crystals of SLC26Dg-Nb5776 complex
- [Single Anomalous Dispersion (SAD)](/xray-mp-wiki/methods/structure-determination/single-anomalous-dispersion/) — SAD phasing used from selenomethionine-derivatized SLC26Dg crystals
- [MGCL2](/xray-mp-wiki/reagents/additives/mgcl2) — Entity mentioned in text
- [URAA](/xray-mp-wiki/proteins/uraA) — Related protein
