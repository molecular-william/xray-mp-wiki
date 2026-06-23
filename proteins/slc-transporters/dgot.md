---
title: DgoT (E. coli D-galactonate Transporter)
created: 2019-05-13
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1371##journal.pbio.3000260]
verified: false
---

# DgoT (E. coli D-galactonate Transporter)

## Overview

DgoT (D-galactonate transporter) is a proton-coupled D-galactonate/H+ symporter from
Escherichia coli that belongs to the solute carrier 17 (SLC17) family within the major
facilitator superfamily (MFS). The structure was determined in two conformations: an
inward-open apo state (PDB 6E9N) at 2.9 x 3.8 x 3.8 A resolution and an outward-facing,
substrate-bound occluded state (PDB 6E9O) at 3.5 A resolution. DgoT is composed of 12
transmembrane helices with an MFS fold and contains two intracellular helices (ICH1 and
ICH2). The structures reveal a putative H+ tunnel connecting the periplasm to a polar
pocket in the N-terminal lobe containing key protonatable residues Asp46 (TM1) and
Glu133 (TM4). Substrate recognition involves a salt bridge between Arg47 (TM1) and the
carboxyl group of D-galactonate, with nine hydrogen bonds from residues in both N- and
C-terminal domains conferring high specificity for D-galactonate over its epimer
gluconate. The transport mechanism couples H+ flux to substrate translocation via
reversible protonation of Asp46 and Glu133, with Glu133 protonation releasing Arg47 to
bind the anionic substrate.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1371##journal.pbio.3000260 | 6E9N | 2.9 x 3.8 x 3.8 (anisotropic) | P 1 21 1 | Wild-type DgoT (residues 27-443) from E. coli, C-terminal decahistidine tag with thrombin cleavage site | beta-nonylglucoside (beta-NG), gluconate (nonspecific binding in cavity) |
| doi/10.1371##journal.pbio.3000260 | 6E9O | 3.5 | C 1 2 1 | E133Q mutant DgoT (residues 24-443) from E. coli, C-terminal decahistidine tag with thrombin cleavage site | D-galactonate |

## Expression and Purification

- **Expression system**: E. coli C41(DE3)
- **Construct**: Full-length DgoT with C-terminal decahistidine tag and thrombin cleavage site (pQE60)
- **Induction**: 0.5-1 mM IPTG at OD600 0.6-0.8, 18C for 16 h
- **Media**: Terrific Broth (TB) supplemented with 2 mM MgSO4

### Purification Workflow

- **Expression system**: E. coli C41(DE3)
- **Expression construct**: Full-length DgoT with C-terminal decahistidine tag (pQE60)
- **Tag info**: C-terminal decahistidine tag with thrombin cleavage site

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex C3 homogenizer | — | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl | 5-6 cycles at 15,000-20,000 psi; debris removed at 10,000-18,000g for 20 min |
| Membrane preparation | Ultracentrifugation | — | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl | 185,500g for 1 h; membranes flash frozen in liquid N2 and stored at -80C |
| Membrane solubilization | Detergent solubilization | — | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1.4% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (n-dodecyl-beta-D-maltoside) | 2 h stirring at 4C; insoluble material removed at 185,500g for 20 min |
| Affinity chromatography | Cobalt affinity chromatography | [Talon](/xray-mp-wiki/reagents/additives/talon/) cobalt affinity resin (Clontech) | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Wash with 10 CV wash buffer + 500 mM NaCl; elute with 150 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Desalting | Desalting column | 10-DG desalting column (Bio-Rad) | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) removed prior to tag cleavage |
| Tag removal | Thrombin cleavage | — |  | Overnight digestion at 4C with alpha-thrombin |
| Concentration | Centrifugal concentration | — |  | Concentrated to 5 mg/ml using 100 kDa MWCO concentrator |


## Crystallization

### doi/10.1371##journal.pbio.3000260

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion (HiLiDe method) |
| Protein sample | WT DgoT at 5 mg/ml, repipidated into E. coli polar lipids (2.33:1 protein:lipid, 5:1 detergent:lipid) |
| Reservoir | 39% [Peg](/xray-mp-wiki/reagents/additives/peg/) 400, 100 mM sodium [Acetate](/xray-mp-wiki/reagents/buffers/acetate/) pH 5.35 |
| Temperature | 4C |
| Growth time | 2-3 days (small rod-shaped crystals) |
| Cryoprotection | Well solution used as cryoprotectant |
| Notes | HiLiDe-treated DgoT crystallized via hanging drop; Al's oil placed over well solution to slow vapor diffusion; protein pre-incubated with 10 mM sodium gluconate; space group P2_1; data collected at ALS Beamline 8.3.1 at wavelength 1.1159 A |

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | DgoT E133Q at 7-8 mg/ml (not lipidated) |
| Reservoir | 32% [Peg](/xray-mp-wiki/reagents/additives/peg/) 1000, 100 mM [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) pH 9.0 |
| Temperature | 4C |
| Growth time | 3-4 weeks to 9 months (150-200 um rectangular crystals) |
| Cryoprotection | Well solution used as cryoprotectant |
| Notes | Protein pre-incubated with 10 mM Na galactonate; space group C2; data collected at ALS Beamline 8.3.1 at wavelength 1.1158 A |


## Biological / Functional Insights

### Two conformations capture alternating access mechanism

The two crystal structures of DgoT (inward-open apo and outward-facing substrate-bound
occluded) capture snapshots of the alternating access transport cycle. In the
inward-open conformation, the cytoplasmic side is open with a wide aqueous cavity,
while the periplasmic side is sealed. In the outward-facing occluded state (E133Q
mutant with D-galactonate bound), the substrate is occluded within the central
binding site, with TM7 bending inward over the substrate to form a periplasmic gate.

### Proton translocation pathway via N-terminal polar pocket

The inward-facing structure reveals a putative water-filled H+ tunnel connecting the
periplasmic surface (near Glu180 in TM5) to a membrane-embedded polar pocket in the
N-terminal lobe containing Asp46 (TM1) and Glu133 (TM4). The tunnel has an entrance
diameter of 3.6 A, a constriction of 2.4 A (near Phe278, Pro279, and Thr297), and
an exit at Asp46 of 5.0 A. Polar residues including Glu59, Gln179, Glu180 at the
entrance and Thr172, Thr297 in the interior potentially facilitate H+ movement.
Asp46 (predicted pKa ~6.0) is likely protonated in the inward-open structure.

### Substrate recognition by both N- and C-terminal domains

Unlike sugar transporters that segregate H+ and substrate translocation to different
lobes, DgoT uses both N-terminal (Tyr44, Arg47 from TM1; Tyr79 from TM2; Gln164 from
TM5) and C-terminal domains (Gln264 from TM7; Ser370 from TM10; Asn393 from TM11) for
substrate recognition. Arg47 forms a salt bridge with the D-galactonate carboxyl group
(3.6 A), while four residues (Asn393, Gln264, Ser370, Gln164) provide eight hydrogen
bonds with the five substrate -OH groups, conferring high specificity for D-galactonate
over the epimer gluconate.

### H+/substrate coupling mechanism via Asp46-Glu133-Arg47 triad

A mechanism for coupling H+ flux to substrate translocation is proposed. In the
outward-facing conformation, Glu133 is protonated, allowing Arg47 to provide the
positive charge to bind the anionic substrate carboxyl. Substrate binding stabilizes
the protonated state of Glu133. After reorientation to the cytoplasmic side, substrate
and H+ are released. Glu133 deprotonation enables formation of a charge pair with Arg47,
facilitating reorientation of the empty carrier. Both Asp46 (D46N) and Glu133 (E133Q)
mutations eliminate active transport, supporting their essential roles.

### Electrogenic transport with H+/substrate stoichiometry >1

DgoT catalyzes electrogenic transport with H+/D-galactonate stoichiometry greater
than 1. The H+ ionophore nigericin (dissipates DeltapH) and the K+ ionophore
[Valinomycin](/xray-mp-wiki/reagents/ligands/valinomycin/) (dissipates Deltapsi) both eliminate galactonate uptake, demonstrating
electrogenic H+ cotransport. Thermodynamic calculations suggest that the H+
stoichiometry of >1 enables DgoT to generate approximately 50:1 substrate gradients
under physiological conditions (external pH ~5.5, internal pH ~7.5, Deltapsi = -60 mV).

### VGLUTs and sialin divergence from bacterial SLC17 transporters

The DgoT structures suggest a common mechanism for divergent ionic coupling in the
SLC17 family. The VGLUTs (vesicular glutamate transporters) lack the TM1 acidic
residue equivalent to Asp46 but retain Glu133, which may serve as an allosteric
H+ activation site rather than a coupled transport residue. Sialin retains both
Asp46 and Glu133 for coupled H+ symport. The H183R mutation in sialin corresponds
to Asn141 in DgoT, which forms hydrogen bonds positioning Trp373 for substrate
interaction, explaining the loss of transport in infantile sialic acid storage disease
(ISSD).


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) — DgoT belongs to the MFS fold with 12 TM helices arranged in 2 six-helix bundles
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Two structures capture inward-open and outward-facing states of the transport cycle
- [XylE (E. coli Sugar Transporter)](/xray-mp-wiki/proteins/mfs-transporters/xyle/) — Related MFS transporter; structural comparison for periplasmic gating via TM7 bending
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for DgoT solubilization and purification
- [beta-Octylglucoside (OG) / beta-Nonylglucoside (beta-NG)](/xray-mp-wiki/reagents/detergents/og/) — Beta-NG identified in aqueous cavity of WT DgoT structure
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used for cobalt affinity elution at 150 mM
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Used for induction of DgoT expression at 0.5-1 mM
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer used in purification (20 mM Tris pH 7.4)
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Used at 10% in purification buffers for protein stability
- [Thrombin Protease](/xray-mp-wiki/reagents/protein-tags/thrombin-protease/) — Used to cleave decahistidine tag from DgoT
