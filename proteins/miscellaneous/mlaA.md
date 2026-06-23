---
title: "E. coli MlaA Outer Membrane Lipoprotein"
created: 2026-05-27
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, porin, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.019, doi/10.1038##s41564-017-0046-x]
verified: false
---

# E. coli MlaA Outer Membrane Lipoprotein

## Overview

MlaA is an [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) lipoprotein from Escherichia coli that forms a complex with the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) porin proteins OmpC and OmpF. MlaA is a key component of the Mla lipid transport system, where it functions at the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) as a monomeric alpha-helical phospholipid translocation channel embedded in the inner leaflet of the OM with a doughnut-shaped architecture. The central amphipathic pore allows selective removal of misplaced outer leaflet phospholipids while preventing access of inner leaflet phospholipids. Enterobacterial MlaA proteins form stable complexes with OmpF/C, though the porins do not play an active role in phospholipid transport.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2017.03.019 | 5UW8 | not determined | not applicable | Mature MlaA (signal peptide-cleaved, residues 1-251) in complex with OmpF porin | none |
| doi/10.1038##s41564-017-0046-x | 5NUP | 3.0 | Not specified | Klebsiella pneumoniae MlaA (KpMlaA) in complex with E. coli OmpF trimer, full-length mature protein | none |
| doi/10.1038##s41564-017-0046-x | 5NUQ | Not specified | Not specified | Serratia marcescens MlaA (SmMlaA) in complex with E. coli OmpF trimer, full-length mature protein | none |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Mature MlaA (residues 1-251), signal peptide-cleaved, cloned into custom pET vector (pDCE587)

### Purification Workflow

#### Source: doi/10.1016##j.cell.2017.03.019


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Co-expression and solubilization | Co-expression of MlaA with OmpF, solubilization with detergent | -- | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | MlaA-OmpF complex solubilized from [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) fraction |
| Complex purification | [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) and gel filtration | Not specified | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | MlaA-OmpC/OmpF complex purified for [biolayer interferometry](/xray-mp-wiki/methods/quality-assessment/biolayer-interferometry/) studies |

#### Source: doi/10.1038##s41564-017-0046-x

- **Expression system**: E. coli BL21
- **Expression construct**: KpMlaA (Klebsiella pneumoniae) or SmMlaA (Serratia marcescens) orthologues with N-terminal hexahistidine tag, cloned into pBAD24 vector
- **Tag info**: N-terminal hexahistidine tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Arabinose-inducible expression in E. coli BL21 | — | Low-salt LB medium (tryptone 10 g/L, NaCl 5 g/L, yeast extract 5 g/L) | Expression induced with 0.2% arabinose at OD600 ~0.6, 20 C for 4-16 hr |
| Cell lysis | High-pressure homogenization (Constant Systems, 20,000-23,000 psi) | — | [Tris](/xray-mp-wiki/reagents/buffers/tris/) buffered saline pH 7.5, 1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf/) | Membranes harvested by ultracentrifugation |
| Membrane solubilization | Detergent extraction | — | [Tris](/xray-mp-wiki/reagents/buffers/tris/) buffered saline pH 7.5, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.5% DM + 0.5% DDM (for KpMlaA-syn), 1% DDM (for native complexes) | Stirred 1 hr at 4 C |
| Nickel affinity chromatography | Ni-NTA | Ni-NTA (Qiagen) | [Tris](/xray-mp-wiki/reagents/buffers/tris/) buffered saline pH 7.5, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.15% DDM, 25 mM imidazole (wash), 250 mM imidazole (elution) | MlaA-OmpF complex eluted as stable complex |
| Buffer exchange | Amicon Ultra-15 concentrator (100 kDa cutoff) | — | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.4% C8E4 | For KpMlaA; SmMlaA further purified by SEC |
| Size-exclusion chromatography (SmMlaA only) | HiLoad 26/600 Superdex 200 | — | 10 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.4% C6H12 | SmMlaA-OmpF complex purified by SEC |

**Final sample**: ~10 mg/mL, flash-frozen in liquid nitrogen
**Purity**: >95% by SDS-PAGE, confirmed by mass spectrometry


## Crystallization

### doi/10.1038##s41564-017-0046-x

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | KpMlaA-OmpF complex at ~10 mg/mL in 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.4% C8E4 |
| Reservoir | 0.1 M [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.5, 0.2 M lithium sulfate, 24% [PEG](/xray-mp-wiki/reagents/additives/peg/) 4000 |
| Temperature | 20 C |
| Growth time | Not specified |
| Cryoprotection | 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) |
| Notes | Crystals also obtained for SmMlaA-OmpF complex. LPS molecules observed in porin LPS-binding site in one KpMlaA-OmpF structure. |


## Biological / Functional Insights

### MlaA-OmpC/OmpF outer membrane complex

MlaA forms a stable complex with the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) porin proteins OmpC and OmpF.
This complex serves as the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) anchor of the Mla lipid transport system,
receiving phospholipids from the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) shuttle protein [MLAC](/xray-mp-wiki/proteins/mlaC) and inserting
them into the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) leaflet. The MlaA-OmpF complex was used in biolayer
interferometry experiments to demonstrate direct interaction with [MLAC](/xray-mp-wiki/proteins/mlaC).

### Direct interaction with periplasmic lipid shuttle MlaC

[biolayer interferometry](/xray-mp-wiki/methods/quality-assessment/biolayer-interferometry/) (Octet RED384) demonstrated that [MLAC](/xray-mp-wiki/proteins/mlaC) interacts directly
with the MlaA-OmpC/OmpF [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) complex. Biotinylated [MLAC](/xray-mp-wiki/proteins/mlaC) loaded onto
streptavidin-coated biosensors showed binding to the MlaA-OmpF complex, supporting
the model where [MLAC](/xray-mp-wiki/proteins/mlaC) ferries lipids from the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/) MlaFEDB complex to
the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) MlaA-OmpC/OmpF complex. This interaction is essential for maintaining
[outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) [lipid asymmetry](/xray-mp-wiki/concepts/structural-mechanisms/lipid-asymmetry/).

### Non-essential but critical for outer membrane integrity

While individual MCE system components are non-essential for E. coli growth in rich
media, mutations in mla genes result in increased sensitivity to [SDS](/xray-mp-wiki/reagents/additives/sds/) and [EDTA](/xray-mp-wiki/reagents/additives/edta/),
indicative of [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) defects. The MlaA-OmpC/OmpF complex is required for
the complete Mla system to function, and its disruption leads to accumulation of
phospholipids in the outer leaflet of the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/), disrupting [lipid asymmetry](/xray-mp-wiki/concepts/structural-mechanisms/lipid-asymmetry/).

### Doughnut-shaped alpha-helical architecture

X-ray crystal structures of KpMlaA-OmpF and SmMlaA-OmpF complexes reveal MlaA as a monomeric alpha-helical OM protein with a ring-shaped (doughnut) structure. The protein is ~20 A thick (spanning one leaflet of the OM) and predominantly alpha-helical, with most helices oriented parallel to the membrane plane. Helix 6 (H6) is perpendicular to the membrane and spans the lipid bilayer. A central channel approximately 5 A wide at its narrowest point is lined with hydrophilic residues from H2, the pore loop (between H4 and H5), H5, and H6. The extracellular end of the channel features a pronounced ridge (H5, top of H6, connecting loop) with Trp160 and Trp163 embedded in the outer leaflet interface. The entire MlaA surface is hydrophobic except for the periplasmic face.

### Phospholipid translocation mechanism

Molecular dynamics simulations (atomistic and coarse-grained) show that outer leaflet phospholipids bind specifically to the MlaA ridge, with the PE head group moving ~15 A down the channel towards the bilayer center coupled with tilting of acyl chains by 45-90 degrees. The doughnut architecture prevents inner leaflet phospholipid access to the channel while allowing outer leaflet phospholipids to diffuse to the central channel. The pore can enlarge via conformational rearrangements of the pore loop and/or H6, as demonstrated by the Y138C/W170C disulfide lock mutant which is inactive but rescued by reducing agent. MlaA functions in an energy-independent fashion as a phospholipid translocation channel.

### MlaA* variant and scramblase activity

The N26-F27 deletion variant (MlaA*) shows a more severe phenotype than the mlaA knockout, likely due to disruption of helix H1 and/or its interaction with the pore loop, creating a breach that allows lateral access of inner leaflet phospholipids to the central channel. This would cause rapid, reversed flow to the outer leaflet driven by the steep concentration gradient, effectively functioning as a scramblase.


## Cross-References

- [E. coli MlaC Lipid-Binding Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaC/) — MlaC directly interacts with MlaA-OmpF complex to deliver lipids to the outer membrane
- [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaD/) — MlaA is the outer membrane partner of MlaD at the inner membrane in the Mla system
- [E. coli YebT Tube-like MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/yebT/) — YebT may associate with YebS in the inner membrane and PqiC in the outer membrane similarly
- [E. coli PqiB Syringe-like MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/pqiB/) — PqiB may interact with outer membrane lipoprotein PqiC similarly to MlaA
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM used for MlaA-OmpF complex solubilization from membranes
- [MCE Protein Family](/xray-mp-wiki/concepts/protein-families/mce-protein-family/) — MlaA is a key component of the Mla system, an MCE protein family member
- [TRIS](/xray-mp-wiki/reagents/buffers/tris/) — Entity mentioned in text
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Entity mentioned in text
- [Gram-negative](/xray-mp-wiki/concepts/gram-negative/) — Entity mentioned in text
- [biolayer interferometry](/xray-mp-wiki/methods/quality-assessment/biolayer-interferometry/) — Entity mentioned in text
- [Lipid Asymmetry](/xray-mp-wiki/concepts/structural-mechanisms/lipid-asymmetry/) — MlaA functions to maintain outer membrane lipid asymmetry
