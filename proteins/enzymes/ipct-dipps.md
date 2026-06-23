---
title: "IPCT/DIPPS from Archaeoglobus fulgidus (Bifunctional CTP:Inositol-1-Phosphate Cytidylyltransferase/CDP-Inositol:Inositol-1-Phosphate Phosphotransferase)"
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms5169]
verified: false
---

# IPCT/DIPPS from Archaeoglobus fulgidus (Bifunctional CTP:Inositol-1-Phosphate Cytidylyltransferase/CDP-Inositol:Inositol-1-Phosphate Phosphotransferase)

## Overview

IPCT/DIPPS is a bifunctional membrane enzyme from the hyperthermophilic archaeon Archaeoglobus fulgidus that catalyses two consecutive steps of di-myo-inositol-1,3-phosphate (DIP) biosynthesis. The N-terminal IPCT domain (CTP:L-myo-inositol-1-phosphate cytidylyltransferase) activates inositol-1-phosphate to CDP-inositol, while the C-terminal DIPPS domain (CDP-L-myo-inositol:myo-inositolphosphotransferase, also called DIPP synthase) displaces CMP from CDP-inositol by a second inositol-1-phosphate to form DIPP-phosphate (DIPP). The DIPPS domain is a membrane-embedded CDP-alcohol phosphatidyltransferase with 6 transmembrane helices that dimerizes through its domains. The catalytic mechanism follows an SN2-like displacement with Mg2+ coordinated by four conserved aspartate residues (Asp357, Asp360, Asp378, Asp382) at the membrane interface.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms5169 | 4MND | 2.65 A | P2;2,2 | IPCT/DIPPS bifunctional enzyme from Archaeoglobus fulgidus (AF0263); N-terminal Strept tag II, C-terminal His10 tag; DIPPS domain comprises 6 transmembrane helices (TM1-TM6) | Mg2+ (1 ion), 4 lipid fragments, CTP, inositol-1-phosphate, CDP-inositol, DIPP |

## Expression and Purification

- **Expression system**: E. coli C43 DE3
- **Construct**: A. fulgidus AF0263 gene cloned into PET52b(+) expression vector (Novagen) with N-terminal Strept tag II and C-terminal His10 tag; induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600=1.0, grown at 30 C for 6 h

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and lysis | Fermentation and cell disruption | -- | terrific broth medium; lysis buffer: 50 mM sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/), 50 mM [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/), 200 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 100 mM [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/), 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 0.5 mM PMSF, 2 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), SIGMAFAST protease inhibitor cocktail; pH 7.5 + -- | Cells cultivated at 37 C in 30 L fermentor, pH 7.4; induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600=1.0; temperature lowered to 30 C; harvested 6 h post-induction; disrupted by constant flow cell disrutor; membranes isolated by ultracentrifugation at 200,000 g for 2 h |
| Membrane solubilization | Detergent solubilization | -- | 2% Triton X-100, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 M NaCl, 50 mM phosphate buffer, 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 100 mM [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/), 2 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 1 mM MgCl2; final pH 7.4 at 277 K + 2% Triton X-100 | Solubilized for 2 h at 277 K; insoluble fraction removed by centrifugation at 100,000 g for 1 h |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | HisTrap HP column (GE Healthcare) | Wash buffer A: 0.1% Triton X-100, 50 mM phosphate buffer, 5 mM MgCl2, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1 M NaCl, pH 7.5; Elution buffer B: 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.1% Triton X-100 | Loaded supernatant washed with buffer A, eluted with buffer B containing 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |


## Crystallization

### doi/10.1038##ncomms5169

| Parameter | Value |
|---|---|
| Method | [HiLiDe Crystallization](/xray-mp-wiki/methods/crystallization/hilide-crystallization/) |
| Protein sample | Purified IPCT/DIPPS in detergent |
| Reservoir | [PEG200](/xray-mp-wiki/reagents/additives/peg200/) |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystallized using HiLiDe method in detergent conditions |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified IPCT/DIPPS |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystallized in meso using lipidic cubic phase method |


## Biological / Functional Insights

### Bifunctional enzyme architecture with cytoplasmic and membrane domains

IPCT/DIPPS is a single polypeptide comprising two distinct domains. The N-terminal IPCT domain is cytoplasmic and catalyses the activation of inositol-1-phosphate to CDP-inositol using CTP as a cofactor. The C-terminal DIPPS domain is a membrane-embedded protein with 6 transmembrane helices (TM1-TM6) that catalyses the phosphotransfer reaction. The two domains dimerize through the DIPPS domains, with each monomer contributing 6 transmembrane helices. The interface between IPCT and DIPPS domains is relatively weak (479 A^2 interface area, -7.3 kcal/mol solvation free energy). The entries to the active sites of the two domains are oriented in different directions, suggesting no direct cross-talk between domains.

### Magnesium-dependent catalytic mechanism at the membrane interface

The DIPPS active site cavity is hydrophilic, widely open to the cytoplasm, and located at the membrane interface. A magnesium ion is coordinated by three conserved aspartate residues (Asp357, Asp360, Asp378) from helices TM2 and TM3, with a fourth conserved aspartate (Asp382) nearby. Mg2+ is expected to decrease the pKa of surrounding aspartate residues, enabling them to function as base catalysts. The catalytic mechanism is proposed to be a single displacement SN2-like reaction where Asp357/Asp382 promote direct nucleophilic attack of the hydroxyl group (C3) of inositol-1-phosphate on the beta-phosphoryl of CDP-inositol, forming DIPP and CMP. Magnesium is essential for enzymatic activity.

### Substrate binding pockets and conserved sequence motif

Three substrate binding pockets were identified by HOLLOW analysis. Pocket 1 (cytidine binding) is flanked by the TM2-TM3 loop and lined by conserved residues Gly361, Ala364, Gly374 from the family consensus motif DG(x)2AR(x)7,8G(x)3D(x)3D. Pocket 2 (inositol-1-phosphate binding) is at the bottom of the hydrophilic cavity formed by Asn304, Arg305, Ser308, Ser354, Asp357, Arg443. Pocket 3 is non-conserved and unlikely to bind substrate. The conserved sequence pattern was proposed to be extended to D(x)2DG(x)2AR(x)7-12G(x)3D(x)3D to include the additional Asp357 (D1) residue.

### Structure-based mutagenesis validation

Site-directed mutagenesis validated functional importance of conserved residues. Mutations S308A and S308M (pocket 2) reduced or abolished activity by disrupting inositol-1-phosphate binding. Mutation S371P in the TM2-TM3 loop reduced activity by constraining loop flexibility. Mutations A364M and R365M (pocket 1) likely obstruct active site access or substrate capture. R443A abolished activity completely. These results confirm the proposed substrate binding model and catalytic mechanism, and agree with equivalent mutation studies in yeast CPT1, E. coli phosphatidylglycerophosphate synthase, and Sinorhizobium meliloti CPT.


## Cross-References

- [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100/) — Nonionic detergent used for membrane solubilization of IPCT/DIPPS at 2%
- [Sodium Phosphate Buffer](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) — Buffer component in lysis buffer (50 mM) and solubilization buffer (50 mM)
- [Citrate Buffer](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in lysis buffer (50 mM sodium citrate)
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Stabilizer in lysis buffer (5%) and solubilization buffer (20%)
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt in lysis buffer (200 mM) and solubilization buffer (1 M)
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Chelator in lysis buffer (1 mM)
- [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) — Osmoprotectant in lysis buffer (100 mM) and solubilization buffer (100 mM)
- [PEG200](/xray-mp-wiki/reagents/additives/peg200/) — Crystallization precipitant in HiLiDe method
- [Magnesium Chloride (MgCl2)](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Essential catalytic cofactor; present in solubilization buffer (1 mM) and purification wash buffer (5 mM)
- [Imidazole](/xray-mp-wiki/reagents/additives/ptg/) — Component of solubilization buffer (50 mM) and elution buffer (500 mM) for His-tag purification
- [Beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) — Reducing agent in lysis buffer (2 mM) and solubilization buffer (2 mM)
- [Phenylmethanesulfonylfluoride (PMSF)](/xray-mp-wiki/reagents/additives/pmsf/) — Protease inhibitor in lysis buffer (0.5 mM)
- [Isopropyl beta-D-1-Thiogalactopyranoside (IPTG)](/xray-mp-wiki/reagents/additives/isopropyl-beta-d-thiogalactoside/) — Inducer for protein expression (0.5 mM)
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — HisTrap HP Ni-affinity column used for His-tagged IPCT/DIPPS purification
- [HiLiDe Crystallization](/xray-mp-wiki/methods/crystallization/hilide-crystallization/) — Crystallization method used for IPCT/DIPPS in detergent conditions
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — In meso crystallization method used for IPCT/DIPPS
- [Molecular Replacement (MR)](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Structure determination method used for 4MND
- [CDP-Alcohol Phosphotransferase Family](/xray-mp-wiki/concepts/protein-families/cdp-alcohol-phosphotransferase-family/) — IPCT/DIPPS DIPPS domain belongs to the CDP-alcohol phosphatidyltransferase family (CDP-OH_P_trans)
- [SN2-Like Displacement Mechanism](/xray-mp-wiki/concepts/structural-mechanisms/sn2-like-displacement-mechanism/) — Proposed catalytic mechanism for DIPPS domain of IPCT/DIPPS
