---
title: Human Delta-Opioid Receptor (DOP)
created: 2026-06-10
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2965, doi/10.1126##sciadv.aax9115, doi/10.1038##nature11111]
verified: false
---

# Human Delta-Opioid Receptor (DOP)

## Overview

The δ-opioid receptor (DOP) is a class A G protein-coupled receptor (GPCR) that mediates the effects of endogenous enkephalin peptides. DOP is an attractive target for chronic pain treatment due to its anxiolytic and antidepressant-like effects with reduced adverse effects compared to μ-opioid receptor (MOP) agonists. The first crystal structure of the mouse δ-OR was determined at 3.4 Å resolution bound to the subtype-selective antagonist [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) via a T4 lysozyme fusion construct (Granier et al., 2012), revealing the structural basis for the message–address model of opioid pharmacology. This was followed by the first activated-state structures of human DOP bound to the peptide agonist KGCHM07 (2.8 Å resolution) and the small-molecule agonist DPI-287 (3.3 Å resolution), revealing key determinants for agonist recognition, receptor activation, and DOP selectivity. A subsequent XFEL structure of human δ-OR bound to the bifunctional δ-antagonist/μ-agonist tetrapeptide DIPP-NH₂ was determined at 2.73 Å resolution by serial femtosecond crystallography (Fenalti et al., 2015), revealing a cis-peptide bond between H-Dmt and Tic and new molecular determinants of peptide recognition at δ-OR.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11111 |  | 3.4 |  | Mouse δ-OR-T4L fusion: TEV site after residue 35, C-term [Truncation](/xray-mp-wiki/concepts/truncation/) after P342, T4L residues 2-161 inserted in ICL3 between residues 244 and 251, N-terminal Flag tag, C-terminal octa-histidine tag | [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) |
| doi/10.1038##nsmb.2965 |  | 2.73 | P2₁ | BRIL-Δ₃₈δ-OR fusion: residues 1-38 of δ-OR replaced with thermostabilized apocytochrome b562 ([Bril](/xray-mp-wiki/reagents/protein-tags/bril/)), C-terminal [Truncation](/xray-mp-wiki/concepts/truncation/) of residues 339-372 | DIPP-NH₂ (H-Dmt-Tic-Phe-Phe-NH₂) |
| doi/10.1126##sciadv.aax9115 |  | 2.8 |  | BRIL-DOP fusion: residues 1-40 of DOP replaced with thermostabilized apocytochrome b562 ([Bril](/xray-mp-wiki/reagents/protein-tags/bril/)), C-terminal [Truncation](/xray-mp-wiki/concepts/truncation/) of residues 339-372, with sodium pocket mutations N90S, D95G, N131S | KGCHM07 |
| doi/10.1126##sciadv.aax9115 |  | 3.3 |  | BRIL-DOP fusion: residues 1-40 of DOP replaced with thermostabilized apocytochrome b562 ([Bril](/xray-mp-wiki/reagents/protein-tags/bril/)), C-terminal [Truncation](/xray-mp-wiki/concepts/truncation/) of residues 339-372, with sodium pocket mutations N90S, D95G, N131S | DPI-287 |

 - R-work %, R-free %; Data collection: Merged from 20 crystals; GM/CA-CAT beamline 23ID-B, Advanced Photon Source
 - R-work 20.2%, R-free 22.9%; Data collection: Serial femtosecond crystallography (XFEL) at LCLS CXI beamline; 36,083 indexed patterns from 4.6 h collection; CC₁/₂ = 0.538 in highest-resolution shell
 - R-work %, R-free %; Data collection: 
 - R-work %, R-free %; Data collection: 

## Expression and Purification

- **Expression system**: Baculovirus expression system in Sf9 insect cells using pFastBac vector

- **Construct**: Mouse δ-OR-T4L fusion: TEV site after residue 35, C-term [Truncation](/xray-mp-wiki/concepts/truncation/) after P342, T4L residues 2-161 inserted in ICL3 between residues 244 and 251, N-terminal Flag tag, C-terminal octa-histidine tag


### Purification Workflow

- **Expression system**: Sf9 insect cells (Baculovirus)
- **Expression construct**: Mouse δ-OR-T4L fusion (ΔC-term P342, T4L ICL3 insertion)
- **Tag info**: N-terminal Flag tag, C-terminal octa-histidine tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and expression | Baculovirus infection in Sf9 cells | — |  | Cells grown to 4×10^6 cells/mL, infected with δ-OR-T4L baculovirus, shaken at 27°C for 48 h, harvested and stored at -80°C. 10 μM naloxone present during expression. |
| Cell lysis | Osmotic shock | — | 10 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 1 μM [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/), 2 mg/mL [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) | [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) added to block reactive cysteines |
| Membrane solubilization | Detergent extraction | — | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 0.5 M NaCl, 30% v/v [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mg/mL [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/), 1 μM [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) + 1.0% lauryl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol (MNG), 0.3% sodium cholate, 0.03% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) hemisuccinate (CHS) | Membranes homogenized with glass dounce homogenizer, mixed at 4°C for 1 h, centrifuged at high speed |
| Ni-NTA affinity chromatography | Nickel affinity chromatography | — | 0.1% MNG, 0.03% sodium cholate, 0.01% CHS, 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 0.5 M NaCl, 1 μM [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) | Resin washed 3x in batch, eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in washing buffer |
| Anti-Flag M1 affinity chromatography | Flag antibody affinity chromatography | — | 0.1% MNG, 0.01% CHS, 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 1 μM [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/); salt gradient from 0.5 M to 0.1 M NaCl | Eluted with 0.2 mg/mL Flag peptide and 2 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) in 0.01% MNG, 0.001% CHS, 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 0.1 M NaCl, 1 μM [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) |
| TEV protease cleavage | Proteolytic cleavage | — |  | TEV protease added at 1:3 TEV:δ-OR-T4L ratio by weight to remove flexible N and C termini |


## Crystallization

### doi/10.1038##nature11111

| Parameter | Value |
|---|---|
| Method | Lipidic mesophase (in meso) |
| Protein sample | Mouse δ-OR-T4L purified in 0.01% MNG, 0.001% CHS, 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 0.1 M NaCl, 1 μM [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) |
| Temperature | 20 |
| Notes | Crystallized using the lipidic mesophase technique. Diffraction data collected from 20 crystals and merged for structure solution. Structure solved by molecular replacement at 3.4 Å resolution.
 |

### doi/10.1038##nsmb.2965

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) for serial femtosecond crystallography (XFEL) |
| Protein sample | BRIL-Δ₃₈δ-OR purified in 25 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 500 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% CHS, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1 mM DIPP-NH₂ |
| Lipid | Monoolein |
| Protein-to-lipid ratio | 2:3 (protein:lipid) |
| Temperature | 20 |
| Notes | LCP crystals were used for serial femtosecond crystallography at the LCLS CXI beamline. Crystals were injected using an LCP injector. 4.6 h collection yielded 36,083 indexed patterns. Structure determined by molecular replacement using naltindole-bound δ-OR as search model. Two structures determined: XFEL structure at 2.73 Å and synchrotron structure at 3.0 Å; both highly similar (rmsd 0.5 Å).
 |

### doi/10.1126##sciadv.aax9115

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | BRIL-DOP bound to KGCHM07 or DPI-287 in 25 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 500 mM NaCl, 2% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% CHS |
| Lipid | Monoolein with 10% (w/w) cholesterol |
| Protein-to-lipid ratio | 2:3 (protein:lipid) |
| Temperature | 20 |
| Growth time | 10 days |
| Cryoprotection | Flash-frozen in liquid nitrogen |
| Notes | BRIL-DOP-KGCHM07: 27-32% [Peg 400](/xray-mp-wiki/reagents/additives/peg-400/), 100-120 mM potassium [Citrate](/xray-mp-wiki/reagents/buffers/citrate/), 100 mM [MES](/xray-mp-wiki/reagents/buffers/mes/) pH 6.0, crystals ~70 μm. BRIL-DOP-DPI-287: 32-35% [Peg 400](/xray-mp-wiki/reagents/additives/peg-400/), 100-110 mM potassium [Citrate](/xray-mp-wiki/reagents/buffers/citrate/), 100 mM [MES](/xray-mp-wiki/reagents/buffers/mes/) pH 6.0, crystals 100-140 μm. Both crystallized at 20°C. Crystals appeared overnight, full size in ~10 days. 20 μM BMS986187 (PAM) added during DPI-287 purification but no electron density observed.
 |


## Biological / Functional Insights

### Message–Address Model of Opioid Pharmacology Validated Structurally

The δ-OR structure validates the message–address concept of opioid pharmacology, where the ligand contains distinct 'message' (efficacy) and 'address' (selectivity) determinants. The lower part of the binding pocket is highly conserved among opioid receptors and interacts with the morphinan core (message). The upper part contains divergent residues that confer subtype selectivity (address). Comparison with μ-OR and κ-OR structures reveals that residue 7.35 is a key selectivity determinant: L300^7.35 in δ-OR accommodates naltrindole's indole group, while W318^7.35 in μ-OR and Y312^7.35 in κ-OR are sterically incompatible. This structural organization of distinct message and address regions may extend to other GPCR families, analogous to the allosteric site in muscarinic receptors.

### Naltrindole Binding and Selectivity

[Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) binds in a deep but solvent-exposed binding pocket in the δ-OR. The ligand forms key interactions including a salt bridge with D128^3.32 and contacts with H278^6.52, W274^6.48, W284^6.58, and L300^7.35. The high δ-OR selectivity of [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) is primarily determined by L300^7.35, which accommodates the indole group while the larger W318 in μ-OR and Y312 in κ-OR create steric incompatibility. ECL2 contains a conserved β-hairpin across all opioid receptors despite low sequence identity.

### Activation-related conformational changes

Agonist-bound DOP displays large outward movements of intracellular parts of helices V (4.5 Å) and VI (9.4-11.2 Å) and a 3.9 Å inward movement of helix VII. The P-I-F motif (P225^5.50, I136^3.40, F270^6.44) shows characteristic rearrangements with F270 rotating ~3.5 Å toward helix V. Collapse of the sodium-binding pocket is observed with N314^7.49 shifting ~3.5 Å inward. The DRY motif was the only microswitch not predicted to be fully active by the GAUGE machine learning tool.

### Sodium pocket mutations enable thermostabilization

Three mutations in the sodium-binding pocket (N90^2.45S, D95^2.50G, N131^3.35S) facilitate sodium expulsion and pocket collapse, stabilizing the active-like state. The crystal construct shows constitutive G protein signaling activity. Reversing D95^2.50G (G95^2.50D) restores both cAMP and β-arrestin2 signaling.

### Common denominator for opioid receptor activation

A basic, protonated nitrogen forming a salt bridge to D128^3.32 is a hallmark of opioid receptor activation. Agonists extend deeper into the binding pocket compared to structurally similar antagonists, with rearrangements in the polar network around D128^3.32 serving as common denominators for opioid receptor activation.

### DOP agonist selectivity determinants

For the peptide KGCHM07, a 125° rotation of W284^6.58 opens a hydrophobic pocket harboring the bistrifluoromethylated benzyl moiety. R291^ECL3 becomes accessible during activation, likely playing a role in DOP-selective peptide binding. For small-molecule DPI-287 (~10-fold DOP-selective over MOP), the N,N-diethylbenzamide moiety interacts with nonconserved extracellular ends of helices VI and VII, providing structural basis for DOP selectivity.

### Bifunctional Peptide Recognition at δ-OR

The DIPP-NH₂ tetrapeptide (H-Dmt-Tic-Phe-Phe-NH₂) binds δ-OR with a cis-peptide bond between H-Dmt and Tic, revealing peptide-specific recognition determinants distinct from morphinan or peptidomimetic ligands. The Dmt residue reaches deep into the receptor core, while Phe4 sits at the extracellular entrance interacting with ECL2. DIPP-NH₂ binding induces expansion of the orthosteric site through outward movements of TM helices II and VI (1.1 Å increase) and ECL2 (~2 Å). The Phe3 side chain shields the salt bridge between the N-terminal amine and D128^3.32 from solvent. The Tic scaffold is critical for the bifunctional δ-antagonist/μ-agonist profile, and superimposition with μ-OR reveals a clash between Tic and μ-OR Trp318, explaining subtype selectivity.

### XFEL structure determination at δ-OR

The δ-OR-DIPP-NH₂ structure was determined by serial femtosecond crystallography (SFX) using an X-ray free-electron laser (XFEL) at LCLS. Crystals grown in LCP were injected as a microjet using an LCP injector. 36,083 indexed patterns were collected in 4.6 hours, yielding a 2.73 Å structure (CC₁/₂ = 0.538 in highest-resolution shell). This was one of the first GPCR structures solved by SFX, demonstrating the viability of room-temperature serial crystallography for membrane protein structure determination with minimal radiation damage.


## Cross-References

- [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) — Subtype-selective antagonist co-crystallized with mouse δ-OR in the first δ-OR structure
- [T4 Lysozyme](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion inserted in ICL3 enabled crystallization of mouse δ-OR
- [Murine Mu-Opioid Receptor](/xray-mp-wiki/proteins/gpcr/mu-opioid-receptor/) — Classical opioid receptor family member; message-address model comparison
- [Kappa Opioid Receptor](/xray-mp-wiki/proteins/gpcr/kappa-opioid-receptor/) — Classical opioid receptor family member; message-address model comparison
- [beta-FNA](/xray-mp-wiki/reagents/ligands/beta-fna/) — Covalent morphinan ligand bound to μ-OR used for structural comparison
- [JDTic](/xray-mp-wiki/reagents/ligands/jdtc/) — KOR-selective antagonist used for structural comparison across opioid subtypes
- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — Alternative fusion partner used in later human DOP active-state structures; also used in the DIPP-NH₂ XFEL structure
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — In meso crystallization method used for δ-OR structure determination including the XFEL DIPP-NH₂ structure
- [Truncation](/xray-mp-wiki/concepts/truncation/) — Referenced in context related to Truncation
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in context related to Tris Hcl
