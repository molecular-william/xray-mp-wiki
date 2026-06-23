---
title: "AfUbiA - Archaeoglobus fulgidus UbiA Family Prenyltransferase"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1371##journal.pbio.1001911]
verified: false
---

# AfUbiA - Archaeoglobus fulgidus UbiA Family Prenyltransferase

## Overview

AfUbiA is a membrane-embedded prenyltransferase from the archaeon *Archaeoglobus fulgidus*, belonging to the UbiA family that catalyzes Mg2+-dependent transfer of hydrophobic polyprenyl chains onto acceptor molecules. The structure was solved by X-ray crystallography in unliganded form and bound to Mg2+ with either geranyl diphosphate (GPP) or dimethylallyl diphosphate (DMAPP). AfUbiA contains nine transmembrane helices arranged as two pseudosymmetric four-helix bundles, with the active site located in a central cavity at the cytoplasmic interface. The active site contains two conserved aspartate-rich motifs that coordinate Mg2+ ions and the diphosphate moiety of the prenyl donor. AfUbiA is a structural model for understanding the human homolog UBIAD1, mutations in which cause Schnyder crystalline corneal dystrophy.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1371##journal.pbio.1001911 | 4TQ3 | 2.5 | — | Full-length AfUbiA with N-terminal polyhistidine tag (removed) | [GPP](/xray-mp-wiki/reagents/additives/gpp/) (geranyl diphosphate) |
| doi/10.1371##journal.pbio.1001911 | 4TQ3 | 2.4 | — | Full-length AfUbiA with N-terminal polyhistidine tag (removed) | [DMAPP](/xray-mp-wiki/reagents/additives/dmapp/) (dimethylallyl diphosphate) |
| doi/10.1371##journal.pbio.1001911 | 4TQ3 | 3.2 | — | Full-length AfUbiA with N-terminal polyhistidine tag (removed), [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/)-substituted |  |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: N-terminal polyhistidine tag
- **Notes**: pET vector; [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) induction at 20°C for 15 h; also expressed as [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/)-substituted protein in minimal medium

### Purification Workflow

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: N-terminal polyhistidine tag (cleavable by TEV protease)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Solubilization | — | 40 mM [n-Decyl-β-D-maltoside](/xray-mp-wiki/reagents/detergents/dm/) (DM) |  |
| Affinity chromatography | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) Metal Affinity Resin | — |  |  |
| Tag removal | TEV protease cleavage | — |  |  |
| Size exclusion chromatography | Superdex 200 10/300 GL | — | 150 mM NaCl, 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) + 40 mM n-octyl-beta-D-glucopyranoside (OG) |  |


## Crystallization

### doi/10.1371##journal.pbio.1001911

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | 35 mg/ml AfUbiA |
| Lipid | monoolein |
| Protein-to-lipid ratio | 2:3 (w/w) |
| Temperature | 20 |
| Growth time | 2 weeks |
| Cryoprotection | None (LCP crystals flash frozen directly) |
| Notes | Crystals soaked in 1 mM [GPP](/xray-mp-wiki/reagents/additives/gpp/) or 1 mM [DMAPP](/xray-mp-wiki/reagents/additives/dmapp/) before harvesting; LCP crystals do not require additional cryoprotectant |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Reservoir | 12.5% PEG20000, 100 mM [MES](/xray-mp-wiki/reagents/buffers/mes/) pH 6.7 |
| Notes | SeMet-detergent crystal form; used for SAD phasing at 3.2 Å |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Reservoir | 30% [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) 550 MME, 100 mM [MES](/xray-mp-wiki/reagents/buffers/mes/) pH 6.6, 5 mM [Magnesium Chloride (MgCl₂)](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 100 mM CdCl2 |
| Cryoprotection | Serial mother liquor solutions with 5-25% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Notes | Cd2+ co-crystallization for Mg2+ site verification |


## Biological / Functional Insights

### UbiA Family Prenyltransferase Mechanism

The substrate-bound structures reveal a three-stage catalytic mechanism: (i) ionization of the prenyl diphosphate to form a carbocation intermediate, stabilized by the diphosphate leaving group coordinated by Mg2+ and conserved arginine/lysine residues; (ii) condensation of the carbocation with the prenyl acceptor; (iii) elimination of a proton to regenerate the aromatic acceptor. A highly conserved tyrosine (Y139 in AfUbiA, present in 97% of >10,000 UbiA sequences) is proposed to stabilize the carbocation intermediate via cation-pi interactions. The two aspartate-rich motifs (N68/D72 in TM2 and D198/D202 in TM6) coordinate two Mg2+ ions. Functional assays on E. coli MenA confirmed the essentiality of these residues.

### Structural Basis for Schnyder Corneal Dystrophy Mutations

Missense mutations at 19 different residues of human UBIAD1 cause Schnyder crystalline corneal dystrophy (SCD), a genetic disease causing blindness. Of these, 16 map to the active site region of AfUbiA, clustering around the conserved aspartate-rich motifs and substrate-binding cavity. This conservation suggests the catalytic mechanism is shared between archaeal AfUbiA and human UBIAD1, making AfUbiA a valuable structural model for understanding SCD pathology.

### Hydrophobic Tunnel for Long Prenyl Substrates

The central cavity extends into a long, narrow hydrophobic tunnel that opens into the membrane bilayer, allowing the protein to bind significantly longer polyprenyl chains (up to C60). The tunnel can accommodate up to six prenyl units, and even longer polyprenyls could extend directly into the hydrophobic core of the bilayer. This explains how UbiA family members utilize prenyl donors of varying lengths.

### Structural Similarity to Soluble trans-IPPS Enzymes

Despite negligible sequence identity, the four-helix bundles of AfUbiA (helices 1-8) are superposable on those of soluble trans-isoprenyl diphosphate synthases (trans-IPPS) such as farnesyl diphosphate synthase (FPPS). This suggests that the UbiA fold arose from the duplication of an ancient four-helix, dimeric protein and that the catalytic mechanism is evolutionarily conserved between soluble and membrane-embedded prenyltransferases.


## Cross-References

- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein mentioned in the study
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein mentioned in the study
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Reagent used in the study
- [Geranyl Diphosphate (GPP)](/xray-mp-wiki/reagents/additives/gpp/) — Reagent used in the study
- [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) — Reagent used in the study
- [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/) — Reagent used in the study
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in purification
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) — Reagent used in the study
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Reagent used in the study
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Reagent used in the study
