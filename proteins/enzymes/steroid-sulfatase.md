---
title: "Steroid Sulfatase (hSTS)"
created: 2026-05-27
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jsbmb.2022.106228, doi/10.1074##jbc.M211497200]
verified: false
---

# Steroid Sulfatase (hSTS)

## Overview

Steroid sulfatase (hSTS) from human placenta is an integral membrane enzyme of the endoplasmic reticulum that catalyzes the hydrolysis of sulfate esters of [E1](/xray-mp-wiki/reagents/ligands/estrone) sulfate (E1S) and dehydroepiandrosterone sulfate (DHEAS) to yield the unconjugated steroids [E1](/xray-mp-wiki/reagents/ligands/estrone) (E1) and [DHEA](/xray-mp-wiki/reagents/ligands/dhea). These steroids serve as precursors for the biosynthesis of 17β-[E2](/xray-mp-wiki/reagents/ligands/estradiol) (E2) and dihydrotestosterone ([DHT](/xray-mp-wiki/reagents/ligands/dht)), the most potent estrogens and androgens. hSTS is a key enzyme for local production of E2 and [DHT](/xray-mp-wiki/reagents/ligands/dht) in breast and prostate tissues, and is responsible for maintaining high levels of estrogens in breast tumor cells. The enzyme is Ca2+-dependent and contains a post-translationally modified catalytic residue (formylglycine, further activated to hydroxyformylglycine). The tertiary structure consists of a globular polar catalytic domain and two antiparallel transmembrane helices. hSTS forms a stable trimeric oligomer that integrates into the lipid bilayer.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1074##jbc.M211497200 | 1P49 | 2.60 | P3 | Full-length human estrone sulfatase purified from human placenta microsomal fraction | Ca2+, sulfate (covalently linked to FGS75), BOG (detergent) |
| doi/10.1016##j.jsbmb.2022.106228 | 8EG3 | 2.0 A | P321 | Human placental steroid sulfatase (hSTS), full-length, two transmembrane helices (alpha8, alpha9), N47 and N333 glycosylated, purified from human placenta microsomal fraction | Ca2+ (catalytic cofactor), FGS75 (covalently linked sulfate ester at catalytic site), BOG (detergent, two binding sites) |

## Expression and Purification

- **Expression system**: Human placenta (native expression, purified from microsomal fraction)
- **Construct**: Full-length hSTS, two antiparallel transmembrane helices (alpha8 and alpha9), globular lumen-facing polar domain with two subdomains (SD1 and SD2), N47 and N333 glycosylation sites

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Microsomal fraction preparation | Homogenization and differential centrifugation of human placenta | -- | Not specified + -- | hSTS localized to rough endoplasmic reticulum microsomal fraction |


## Crystallization

### doi/10.1074##jbc.M211497200

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | hSTS purified from human placenta, solubilized in 0.3% BOG (n-octyl-beta-D-glucopyranoside) |
| Reservoir | 100 mM Tris-HCl pH 8.5, 0.10-0.20 M ammonium phosphate monobasic, 0.3% BOG |
| Temperature | 20 |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Crystals belong to space group P3 with one molecule per asymmetric unit. Data collected at CHESS (wavelength 0.948 A) and in-house R-AXIS-IV (Cu Kalpha). Structure solved by SIRAS using two HgCl2 derivatives. Initial phase calculation using SOLVE and PHASES. |

### doi/10.1016##j.jsbmb.2022.106228

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization |
| Protein sample | hSTS purified from human placenta microsomal fraction, solubilized in 0.3% n-octyl-beta-D-glucopyranoside (BOG) |
| Reservoir | 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) (pH 8.5), 0.10-0.20 M ammonium phosphate (monobasic), 0.3% BOG |
| Temperature | Not specified (room temperature implied) |
| Growth time | Not specified |
| Cryoprotection | Cryo-cooled with 50% 2-methyl-2,4-pentanediol ([MPD](/xray-mp-wiki/reagents/additives/mpd)) |
| Notes | Six hSTS molecules in unit cell, one per asymmetric unit. Solvent content ~59%. Data collected at Stanford Synchrotron Radiation Light Source beamline 11-1 (wavelength 0.97945 A). Starting model was 2.6 A structure (1P49). |


## Biological / Functional Insights

### Catalytic mechanism with formylglycine active site

The catalytic cysteine in sulfatases is post-translationally modified to formylglycine (FG), which is further activated to hydroxyformylglycine (HFG) by a water molecule. In the hSTS structure, the catalytic residue HFG75 is covalently linked to a sulfate moiety (FGS/HFGS). The metal ion at the catalytic center is Ca2+, coordinated by oxygen atoms from D35, D36, D342, Q343, and FGS75 side chains (seven-coordinated, Ca2+-O distances 2.2-2.8 A). Positively charged side chains K134, K368, and R79 neutralize negative charges of carboxylate and sulfate moieties. The imidazole ring of H136 is within hydrogen-bonding distance (2.8 A) of the FGS75 hydroxyl group, while H290 Ne2 is ~3.2 A from two sulfate oxygens. The main chain NH of FGS75 and K368 side chain amino group point to the sulfate oxygen, forming an amide-linked oxyanion hole at the site of hydrolysis.

### Substrate binding mode and steroid recognition

The substrate binding cleft accommodates E1S and DHEAS with their sulfate groups covalently linked to HFG75. The A-B rings of E1 are sandwiched between L74-V101 and L103-V486 side chain pairs from opposite faces, while aromatic side chains F488 and F178 approach the steroid C-D rings from both sides. The R98 side chain at the catalytic cavity entrance is flexible (broken electron density beyond Cgamma), with the guanidinium group likely involved in interactions with the substrate sulfate moiety and the D ring 17 C=O. A loop between residues 476 and 481, missing in the previous 2.6 A structure, was built into defined electron density.

### Mushroom-like transmembrane architecture

The first crystal structure of human estrone sulfatase at 2.6 A (PDB 1P49) revealed a novel "mushroom-like" architecture. Two antiparallel alpha-helices (helices 8 and 9, residues 179-241), each approximately 40 A long, protrude from the globular polar catalytic domain. These highly hydrophobic helices are capable of traversing the ER membrane, anchoring the functional domain on the membrane surface facing the ER lumen. The two helices interdigitate tightly through hydrophobic interactions (leucine, isoleucine, valine, alanine, phenylalanine), burying 1220 A2 of accessible surface between them. They have a right-handed crossover with a crossing angle of approximately -21 degrees. The opening to the active site, buried deep in the "gill" of the "mushroom," rests near the membrane surface, suggesting a role of the lipid bilayer in catalysis. A constellation of aromatic residues (Phe178, Phe182, Phe187, Phe230, Phe233, Tyr236, Phe237, Phe104, Trp550, Phe553, Leu554) lines the opening to the active site cleft, creating a hydrophobic tunnel connecting the active site to the interior of the lipid bilayer.

### Membrane-associated loops and swing door mechanism

In addition to the transmembrane helices, two hydrophobic regions from the SD2 subdomain show potential membrane association based on their location, hydrophobicity, and high thermal motion (average B-factor 91.7 A2 for SD2 vs 51.9 A2 for SD1). The Phe548-Leu568 segment (including one-turn helices 17 and 18), spatially proximal to the active site groove, positions three tryptophan side chains (Trp555, Trp558, Trp560) at the lipid bilayer interface. The Phe468-Pro500 segment also displays high thermal motion. Three flexible loops are proposed as "swing doors" for substrate entry/exit: (1) a "front swing door" between residues Thr470-Thr495 adjacent to the active site gorge; (2) a "right swing door" between Glu348-Gly358 containing Lys353 that may associate with the membrane surface; and (3) a "left swing door" between residues 94-100 containing Arg98 involved in substrate recognition.

### Secondary ligand binding site at intermolecular interface

A secondary ligand binding pocket is located at the intermolecular interface of the trimeric hSTS, near the active site access channel and buried in the gill of the mushroom-shaped molecule. The site is lined partly by alpha8 of a symmetry-related neighboring molecule. The cavity can accommodate an E1 molecule with its 3-OH and 17 C=O ends hydrogen bonded to N241 side chain amide and C205 thiol from the neighboring alpha8. The site is bordered by W555, F233, F237, F104, L103, F178, and F182 side chains. A phosphate ion bound at H142 is ~16 A away, with stacked ringed side chains W555, P557, and W558 coupling the secondary ligand site to the phosphate ion location, suggesting allosteric communication.

### Trimeric quaternary structure and membrane integration

Three hSTS monomers associate via their pairs of antiparallel hydrophobic helices (alpha8 and alpha9) to form a trimeric oligomer. The trimer has 63,279 A2 of solvent accessible surface area with 10,554 A2 buried primarily at the alpha8-alpha9 interhelical hydrophobic interfaces. The trimer is stable in solution with standard free energy of dissociation Delta G = 19.3 kcal/mole (versus -0.5 kcal/mole for a dimer). The three F217 side chains from helix alpha9 approach each other at the center creating a cavity of 3.92 A diameter. The trimer integrates into the lipid bilayer with the 3-fold axis normal to the membrane surface, with the alpha8-alpha9 helices tilted at about 33 degrees to the membrane plane, without fully traversing the bilayer.


## Cross-References

- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used for solubilization and crystallization of hSTS
- [2-Methyl-2,4-pentanediol (MPD)](/xray-mp-wiki/reagents/additives/mpd/) — Cryoprotectant used for flash-cooling hSTS crystals
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component (100 mM, pH 8.5) in crystallization reservoir
- [Ammonium Phosphate](/xray-mp-wiki/reagents/buffers/ammonium-phosphate/) — Crystallization precipitant (0.10-0.20 M ammonium phosphate monobasic)
- [Calcium Chloride](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Ca2+ ion at catalytic center, seven-coordinated
- [Estrone](/xray-mp-wiki/reagents/ligands/estrone/) — Product of E1S hydrolysis, binds at secondary ligand site
- [Dehydroepiandrosterone (DHEA)](/xray-mp-wiki/reagents/ligands/dhea/) — Substrate of hSTS, hydrolyzed from DHEAS
- [Positive Allosteric Modulation](/xray-mp-wiki/concepts/structural-mechanisms/positive-allosteric-modulation/) — Secondary ligand site and phosphate binding site may regulate hSTS activity allosterically
