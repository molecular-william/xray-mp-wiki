---
title: A. borkumensis YdaH transporter
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms7874]
verified: false
---

# A. borkumensis YdaH transporter

## Overview

YdaH is an integral membrane protein from Alcanivorax borkumensis encoded by the ydaH gene. It belongs to the AbgT family of transporters and was the first member of this family to have a crystal structure reported. YdaH is a 492-amino acid dimeric transporter that forms a bowl-shaped structure with a solvent-filled basin extending from the cytoplasm to halfway across the membrane bilayer. Each subunit contains nine transmembrane helices and two hairpins. Functional assays demonstrate that YdaH functions as a proton-motive-force (PMF)-dependent efflux pump that exports p-aminobenzoic acid (PABA) and confers resistance to sulfonamide antimetabolites, suggesting a role in antibiotic resistance.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms7874 | not specified | 2.96 A | P2$_{1}$ | Full-length A. borkumensis YdaH with N-terminal 6xHis tag | None (apo structure) |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) delta [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/acrB)
- **Construct**: Full-length YdaH with N-terminal 6xHis tag, cloned into pET15b vector as pET15b_Omega ydaH. Expressed in E. coli BL21(DE3) delta acrB strain which harbors a deletion in the chromosomal acrB gene. Cells grown in 12 L LB medium with 100 ug/mL ampicillin. Induced with 0.2 mM IPTG at OD600=0.5.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane isolation | Cells grown in 12 L LB medium with 100 ug/mL [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin) at 37 C. Induced with 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at OD600=0.5, harvested within 2 h. Membranes isolated by ultracentrifugation.
 | -- | -- + -- | E. coli BL21(DE3) delta [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/acrB) strain transformed with pET15b_Omega ydaH |
| Solubilization | Membrane solubilization | -- | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm) (n-Dodecyl-beta-D-maltopyranoside) | Membranes solubilized with [DDM](/xray-mp-wiki/reagents/detergents/ddm) detergent |
| Ni-affinity chromatography | Ni-affinity chromatography (Ni-NTA) | Ni-NTA agarose | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | His-tag purification using Ni-NTA resin |
| Size exclusion chromatography | Superdex 200 16/60 column (GE Healthcare) with mobile phase containing 20 mM Na-[HEPES](/xray-mp-wiki/reagents/buffers/hepes) (pH 7.5) and 0.05% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm). Blue dextran used to determine column void volume.
 | Superdex 200 16/60 (GE Healthcare) | 20 mM Na-[HEPES](/xray-mp-wiki/reagents/buffers/hepes) (pH 7.5), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Gel filtration suggested an average molecular weight of 107.0 +/- 8.8 kDa, in good agreement with the theoretical value of 105.6 kDa for two YdaH protomers (dimer).
 |


## Crystallization

### doi/10.1038##ncomms7874

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Purified YdaH in Na-[HEPES](/xray-mp-wiki/reagents/buffers/hepes) buffer with [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| Reservoir | -- |
| Mixing ratio | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Native crystals grown in space group P2_1. Additional crystals obtained with [beta-SiW9O34H]9- polyoxometalate (7.70 A) and Se-derivative (4.10 A) for phasing. Na+ ions present at all stages of purification and crystallization. A strong spherical electron density was observed in the flexible loops between HP2 and TM8, identified as a Na+ ion coordinated by N390, D429, N433, backbone carbonyl oxygens of G394 and D429, and a water molecule.
 |


## Biological / Functional Insights

### Bowl-shaped dimer architecture

YdaH forms a dimeric molecule with a bowl-shaped architecture distinct from other families of transporters. The dimer creates a concave aqueous basin facing the intracellular solution. Each protomer forms an internal cavity accessible to the cytoplasm, constituted by loop regions of HP1, HP2, TM3 and TM8. The inner core comprises TMs 1, 2, 5, 6 and 7 contributing to dimerization and a frame-like structure. The outer core cylinder (TMs 3, 4, 8, 9 and HPs 1 and 2) forms a channel spanning approximately from the middle of the inner membrane up to the periplasmic space.

### Conserved channel residues

Several conserved residues line the wall of the outer core channel: D180, W400, P418 and R426. These residues are expected to play an important role in the function of the transporter. Mutational analysis of D180A, W400A, P418A, and R426A showed that R426A retained partial function in decreasing PABA concentration while D180A, W400A, and P418A showed significantly increased intracellular PABA levels, indicating loss of efflux function.

### Na+ binding site

Each protomer of YdaH binds a Na+ ion in the flexible loops between HP2 and TM8. The Na+ coordination sphere includes side chains of N390, D429, N433 and backbone carbonyl oxygens of G394 and D429, plus a water molecule forming a coordinate bond. Valence calculations indicated this site is Na+ specific. Functional assays showed that 5 or 100 mM NaCl significantly decreased intracellular sulfamethazine accumulation compared to YdaH-producing strain without Na+, and efflux assays confirmed Na+ but not K+ has a strong effect on sulfamethazine efflux, indicating YdaH functions more efficiently in the presence of Na+.

### PMF-dependent efflux mechanism

YdaH functions as a proton-motive-force (PMF)-dependent efflux pump. The uncoupler CCCP (carbonyl cyanide m-chlorophenylhydrazone) drastically increased intracellular sulfamethazine accumulation in YdaH-expressing cells, confirming PMF dependence. This is consistent with the hypothesis that AbgT family members use the PMF to transport substrates across the membrane.

### Sulfonamide efflux and antibiotic resistance

YdaH acts as an antibiotic efflux pump capable of extruding sulfonamide antimetabolites. It exports PABA (p-aminobenzoic acid) from the cell and confers resistance to sulfonamides including sulfanilamide (Ki=0.41 uM), sulfathiazole (Ki=0.60 uM), sulfadiazine (Ki=4.97 uM), and sulfamethazine (Ki=7.04 uM). All mutants D180A, N390A, W400A, P418A, R426A, D429A and N433A showed hypersensitivity to sulfonamides compared to wild-type YdaH, confirming these residues are essential for drug resistance function.

### AbgT family functional diversity

The AbgT family (~13,000 putative members) includes both transporters and resistance proteins. E. coli AbgT imports p-aminobenzoyl-glutamate for de novo folate synthesis, while N. gonorrhoeae MtrF confers high-level resistance to hydrophobic antimicrobials. YdaH represents a third functional class: an efflux pump for sulfonamide antimetabolites. This suggests other AbgT family members may also serve as antimetabolite efflux pumps.


## Cross-References

- [AbgT Family of Transporters](/xray-mp-wiki/concepts/transport-mechanisms/abgt-family/) — YdaH is the first structurally characterized member of the AbgT family
- [Antibiotic Efflux Pumps](/xray-mp-wiki/concepts/transport-mechanisms/antibiotic-efflux-pump/) — YdaH functions as a sulfonamide efflux pump
- [Sulfonamide Resistance](/xray-mp-wiki/concepts/miscellaneous/sulfonamide-resistance/) — YdaH confers resistance to sulfonamide antimetabolites
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for YdaH solubilization and purification
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Na-HEPES buffer (pH 7.5) used in SEC and purification
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) — Ni-NTA used for His-tag purification of YdaH
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Superdex 200 16/60 used for size exclusion chromatography of YdaH
- [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) — 0.2 mM IPTG used for induction of ydaH expression
- [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) — 100 ug/mL ampicillin used for selection during YdaH expression
- [CCCP (Carbonyl Cyanide m-Chlorophenylhydrazone)](/xray-mp-wiki/reagents/additives/cccp/) — Protonophore uncoupler used to demonstrate PMF-dependence of YdaH
- [Sulfanilamide](/xray-mp-wiki/reagents/ligands/sulfanilamide/) — YdaH binds sulfanilamide with Ki=0.41 uM and exports it from cells
- [Sulfamethazine](/xray-mp-wiki/reagents/ligands/sulfamethazine/) — YdaH binds sulfamethazine with Ki=7.04 uM and exports it from cells
- [Sulfathiazole](/xray-mp-wiki/reagents/ligands/sulfathiazole/) — YdaH binds sulfathiazole with Ki=0.60 uM
- [Sulfadiazine](/xray-mp-wiki/reagents/ligands/sulfadiazine/) — YdaH binds sulfadiazine with Ki=4.97 uM
- [p-Aminobenzoic Acid (PABA)](/xray-mp-wiki/reagents/additives/paba/) — YdaH exports PABA from bacterial cells
- [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrB/) — Related efflux pump; E. coli BL21(DE3) delta acrB strain used for YdaH expression
- [Sodium Motive Force](/xray-mp-wiki/concepts/miscellaneous/sodium-motive-force/) — Na+ enhances YdaH transporter function
