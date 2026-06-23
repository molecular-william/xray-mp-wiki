---
title: "Mouse P-glycoprotein"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1107##s1399004715000978, doi/10.1002##pro.2387, doi/10.1126##science.1168750, doi/10.1126##sciadv.1600001, doi/10.1107##S2052252520005709]
verified: false
---

# Mouse P-glycoprotein

## Overview

Mouse P-glycoprotein (P-gp; ABCB1; Mdr1a) is an ATP-binding cassette (ABC) transporter that functions as a multidrug efflux pump, exporting a wide array of structurally diverse compounds including chemotherapy drugs, antibiotics, and environmental toxins. It shares 87% sequence identity with human P-gp and serves as the primary structural model for understanding P-gp function. The transporter consists of two transmembrane domains (TMDs) and two nucleotide- binding domains (NBDs), forming a large polyspecific drug-binding cavity enriched in aromatic residues.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1107##s1399004715000978 | 4q9h | 3.4 A | P2_12_12_1 | Mouse P-gp/Mdr1a (ABCB1), reductively methylated, C-terminal His6 tag | None (drug-free, apo) |
| doi/10.1107##s1399004715000978 | 4q9i | 3.8 A | P2_12_12_1 | Mouse P-gp/Mdr1a cocrystallized with QZ-Ala | QZ-Ala (Se-labeled homotrimeric cyclopeptide) |
| doi/10.1107##s1399004715000978 | 4q9j | 3.6 A | P2_12_12_1 | Mouse P-gp/Mdr1a cocrystallized with QZ-Val | QZ-Val (Se-labeled homotrimeric cyclopeptide, formerly QZ59-SSS) |
| doi/10.1107##s1399004715000978 | 4q9k | 3.8 A | P2_12_12_1 | Mouse P-gp/Mdr1a cocrystallized with QZ-Leu | QZ-Leu (Se-labeled homotrimeric cyclopeptide) |
| doi/10.1107##s1399004715000978 | 4q9l | 3.8 A | P2_12_12_1 | Mouse P-gp/Mdr1a cocrystallized with QZ-Phe | QZ-Phe (Se-labeled homotrimeric cyclopeptide) |
| doi/10.1002##pro.2387 | 3G5U | 3.8 A | C2 | Mouse P-gp (ABCB1a), original structure by MAD phasing | None (drug-free) |
| doi/10.1002##pro.2387 | 4M1M | 3.8 A | C2 | Mouse P-gp, improved model with corrected TM registry | None (drug-free) |
| doi/10.1002##pro.2387 | 4M2S | 4.4 A | C2 | Mouse P-gp cocrystallized with QZ59-RRR | QZ59-RRR (cyclic hexapeptide, selenium-labeled) |
| doi/10.1002##pro.2387 | 4M2T | 4.35 A | C2 | Mouse P-gp cocrystallized with QZ59-SSS | QZ59-SSS (cyclic hexapeptide, selenium-labeled) |
| doi/10.1126##science.1168750 | 3GSU | 3.8 A | C2 | Mouse P-gp (ABCB1a), drug-free inward-facing conformation | None (drug-free) |
| doi/10.1126##science.1168750 | 3G60 | 4.4 A | C2 | Mouse P-gp cocrystallized with QZ59-RRR | QZ59-RRR (cyclic hexapeptide) |
| doi/10.1126##science.1168750 | 3G61 | 4.35 A | C2 | Mouse P-gp cocrystallized with QZ59-SSS | QZ59-SSS (cyclic hexapeptide) |
| doi/10.1126##sciadv.1600001 | 4XWK | 3.5 A | P2_12_12_1 | Mouse P-gp N83Q/N87Q/N90Q mutant, expressed in P. pastoris | PBDE-100 |
| doi/10.1107##S2052252520005709 | 6UNJ | 3.98 A | P2_12_12_1 | Mouse P-gp C952A mutant (parent control) | [BDE-100 (2,2',4,4'-Tetrabromodiphenyl Ether)](/xray-mp-wiki/reagents/ligands/bde-100/) |

## Expression and Purification

- **Expression system**: Pichia pastoris (mouse P-gp ABCB1a); also in S. cerevisiae and insect cells
- **Construct**: Mouse ABCB1a with N83Q/N87Q/N90Q mutations (deglycosylated) and C-terminal His6 tag; full-length 1276 residues

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell disruption and membrane fractionation | -- | -- | P-gp expressed in Pichia pastoris; membranes solubilized in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA Superflow | 20 mM HEPES pH 8.0, 100 mM NaCl, 0.2 mM TCEP, 0.04% [Sodium Cholate](/xray-mp-wiki/reagents/detergents/sodium-cholate/), 0.065% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/), 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) | Protein eluted with 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 16/60 | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.2 mM TCEP, 0.01% [Sodium Cholate](/xray-mp-wiki/reagents/detergents/sodium-cholate/), 0.035% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Followed by reductive methylation (borane dimethylamine/formaldehyde) for crystallography |


## Crystallization

### doi/10.1107##s1399004715000978

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Reductively methylated P-gp at ~10-12 mg/ml (1:1 protein:mother liquor) |
| Reservoir | 0.1 M HEPES pH 7-8, 50 mM [Lithium Sulfate](/xray-mp-wiki/reagents/additives/lithium-sulfate/), 10 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 24-29.5% [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/) |
| Temperature | 4°C (277 K) |
| Growth time | ~2 weeks |
| Notes | Crystals typically appeared after 1-3 days, grew to full size in ~2 weeks. Cryoprotected in reservoir solution with 32% [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/). Typical crystal dimensions ~650 x 400 x 300 um. Data collected at SSRL BL11-1 and CLS 08ID-1 at 100 K. For co-crystals, excess cyclopeptide removed before crystallization. |


## Biological / Functional Insights

### TM4 kinking induced by small-molecule ligands

Binding of subset A ligands (QZ-Ala, QZ-Val) induces a large conformational change in TM4, kinking it by up to 11 A at C-alpha positions compared to the straight-helical conformation in apo P-gp and subset B complexes. This kink begins at Pro219 and returns to wild-type topology at Tyr243 near the ball-and- socket region close to NBD2. The movement brings residues 221-228 closer to bound ligands, fostering interaction with Trp228 (implicated in steroid binding). This provides a structural glimpse of the induced-fit model of drug binding in P-gp and suggests a mechanism for transmitting substrate-binding signals from the TMDs to the NBDs.

### EH2 elbow helix as a ligand entry site

A new ligand-binding site was identified on the surface of P-gp facing the inner leaflet of the membrane, involving the elbow helix 2 (EH2, residues 689-694). This site provides vital insights into the entry mechanism of hydrophobic drugs and lipids into P-gp. The EH2 region acts as a portal for substrate entry from the inner leaflet before ligands reach the main drug-binding cavity.

### Multiple binding modes for cyclopeptide substrates

Four homotrimeric cyclopeptide ligands differing only in R-group size (QZ-Ala, QZ-Val, QZ-Leu, QZ-Phe) revealed distinct binding modes. Smaller ligands (subset A: QZ-Ala, QZ-Val) share upper and lower binding sites, while larger ligands (subset B: QZ-Leu, QZ-Phe) bind at a different upper site, with QZ-Phe also occupying a unique lower site. This demonstrates the polyspecific nature of the P-gp binding cavity, accommodating diverse substrates through overlapping but distinct binding subsites.

### Ligand size inversely correlates with ATPase stimulation

QZ-Ala potently stimulated ATP hydrolysis (~16-fold, EC50=0.92 uM), with smaller ligands being more stimulatory. QZ-Val showed ~7-fold stimulation, while QZ-Leu and QZ-Phe were weak stimulators or inhibitors. This correlates with the structural observation that subset A ligands induce TM4 kinking (proposed to transmit a signal to NBDs), while subset B ligands do not. Calcein-AM transport inhibition followed the same trend: QZ-Ala IC50=140 nM, QZ-Val 1.7 uM, QZ-Leu 5.4 uM, QZ-Phe 24 uM.


## Cross-References

- [P-glycoprotein Induced-Fit Binding](/xray-mp-wiki/concepts/miscellaneous/p-glycoprotein-induced-fit-binding/) — TM4 kinking provides structural evidence for induced-fit model of drug binding in P-gp
- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — P-gp is a member of the ABCB/MDR subfamily of ABC transporters
- [QZ-Ala](/xray-mp-wiki/reagents/ligands/qz-ala/) — Se-labeled homotrimeric cyclopeptide ATPase stimulator; cocrystal structure determined
- [QZ-Val](/xray-mp-wiki/reagents/ligands/qz-val/) — Se-labeled homotrimeric cyclopeptide; cocrystal structure determined
- [QZ-Leu](/xray-mp-wiki/reagents/ligands/qz-leu/) — Se-labeled homotrimeric cyclopeptide; cocrystal structure determined
- [QZ-Phe](/xray-mp-wiki/reagents/ligands/qz-phe/) — Se-labeled homotrimeric cyclopeptide; cocrystal structure determined
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [Lithium Sulfate](/xray-mp-wiki/reagents/additives/lithium-sulfate/) — Additive used in purification or crystallization buffers
