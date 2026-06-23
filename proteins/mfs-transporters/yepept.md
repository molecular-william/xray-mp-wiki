---
title: YePEPT (Yersinia enterocolitica Peptide Transporter)
created: 2026-06-11
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [membrane-protein, transporter, transporter, xray-crystallography]
sources: [doi/10.1186##s12915-015-0167-8, doi/10.1038##s42004-022-00636-0]
verified: false
---

# YePEPT (Yersinia enterocolitica Peptide Transporter)

## Overview

YePEPT is a proton-dependent oligopeptide transporter (POT) family member from
the bacterium Yersinia enterocolitica. It is a membrane protein that mediates
the cellular uptake of di- and tripeptides using energy provided by
transmembrane proton gradients. YePEPT belongs to the major facilitator
superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/)) of secondary active transporters. The X-ray crystal structure
of YePEPT at 3.02 A resolution revealed the molecular bases for recognition,
binding and specificity of dipeptides with a charged amino acid residue at the
N-terminal position. Lys314 in the substrate-binding pocket determines
specificity for negatively charged dipeptides (Asp-Ala, Glu-Ala) via
electrostatic interactions. Mutagenesis of Lys314 to Glu (K314E) re-tuned
specificity toward positively charged dipeptides (Lys-Ala), while the K314A
mutation abolished charged dipeptide specificity. The corresponding mutation in
human PEPT1 (Q300K) similarly introduced affinity for Asp-Ala, demonstrating
that this electrostatic recognition mechanism is conserved from bacteria to
humans.
A subsequent structure of the YePEPT K314A variant in complex with the potent
PEPT1/PEPT2 inhibitor Lys[Z(NO2)]-Val (LZNV) at 3.1 A resolution revealed the
molecular details of inhibitor binding and a previously undescribed mostly
hydrophobic pocket, the PZ pocket, that forms upon inhibitor binding. The apo
structure of YePEPT K314A at 2.93 A provided the ligand-free reference.
Comparison showed that the PZ pocket is initially absent and emerges through
conformational changes (rigid body movement of the N-terminal bundle by ~5°
and rotamer changes of F318, Y35, and Y159) upon LZNV binding. The Z(NO2)
moiety of LZNV bound to the PZ pocket acts like a wedge impeding transition
to the inward-open state, revealing the inhibition mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1186##s12915-015-0167-8 | 4W6V | 3.02 | P2_1_2_1_2_1 | Full-length YePEPT with C-terminal HRV3C cleavage site and deca-His tag | -- |
| doi/10.1038##s42004-022-00636-0 | 7PZ3 | 3.10 | P2_1_2_1_2_1 | YePEPT K314A mutant with C-terminal HRV3C cleavage site and deca-His tag | LZNV (Lys[Z(NO2)]-Val) |
| doi/10.1038##s42004-022-00636-0 | 7PZ4 | 2.93 | P2_1_2_1_2_1 | YePEPT K314A mutant with C-terminal HRV3C cleavage site and deca-His tag | -- |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) pLysS
- **Construct**: YePEPT gene (UniProt R9G739) with C-terminal HRV3C protease cleavage site and deca-His tag, cloned into pZUDF21-rbs vector
- **Notes**: Overexpressed at 20 C for 16-20 h with 0.3 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction. K314A mutant purified for LZNV-bound and apo structures.

### Purification Workflow

*Source: doi/10.1186##s12915-015-0167-8*

- **Expression system**: E. coli
- **Expression construct**: YePEPT with C-terminal HRV3C-decaHis tag
- **Tag info**: deca-His tag, cleaved by HRV3C protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer (15,000 psi, 5 passages) | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl |  |
| Membrane isolation | Ultracentrifugation (100,000 x g, 1 h, 4 C) | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl |  |
| Membrane solubilization | Detergent extraction, 1 h at 4 C | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA Superflow Beads | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Washed with 10 CV of washing buffer (20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 5 mM histidine, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)). Eluted by HRV3C protease cleavage overnight. |
| Size-exclusion chromatography | SEC | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Concentrated to ~10 mg/mL for crystallization |

### Purification Workflow

*Source: doi/10.1038##s42004-022-00636-0*

- **Expression system**: E. coli BL21(DE3) pLysS
- **Expression construct**: YePEPT K314A with C-terminal HRV3C cleavage site and deca-His tag in pZUDF21-rbs vector
- **Tag info**: deca-His tag, cleaved by HRV3C protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication (60 min total ON, 5 s ON/3 s OFF) | — | 20 mM Tris-HCl pH 8.0, 50 mM NaCl | Cells thawed and sonicated using Branson 450 Digital Sonifier |
| Membrane isolation | Ultracentrifugation (150,000 x g, 1 h, 4 C) | — | 20 mM Tris-HCl pH 8.0, 500 mM NaCl | Washed once with membrane wash buffer |
| Membrane solubilization | Detergent extraction, 1 h at 4 C | — | 20 mM Tris-HCl pH 8.0, 300 mM NaCl + 2% (w/v) n-undecyl-β-D-maltopyranoside (UDM) |  |
| Ni-NTA affinity chromatography | Affinity chromatography | Ni-NTA Superflow resin | 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 0.075% (w/v) UDM | Washed with 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 5 mM L-histidine, 0.1% (w/v) UDM. Eluted by on-column HRV3C protease cleavage overnight. |

**Final sample**: Purified YePEPT K314A in detergent-containing buffer


## Crystallization

### doi/10.1186##s12915-015-0167-8

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | YePEPT at ~10 mg/mL in 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 0.1 M HEPES pH 7.5, 10% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 10% isopropanol |
| Mixing ratio | 1:1 |
| Temperature | 20 C |
| Growth time | not specified |
| Cryoprotection | not specified |

### doi/10.1038##s42004-022-00636-0

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | YePEPT K314A at ~10 mg/mL in 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 0.075% (w/v) UDM |
| Reservoir | 0.1 M HEPES pH 7.5, 8% PEG 400, 10% isopropanol (for apo); 0.1 M HEPES pH 7.5, 8% PEG 400, 10% isopropanol, 0.5-1.0 mM LZNV (for LZNV-bound) |
| Temperature | 20 |
| Notes | Apo crystals grown as previously described. LZNV-bound crystals obtained by co-crystallization with 0.5-1.0 mM LZNV. Data collected at SLS beamline X06SA. Orthorhombic P2_1_2_1_2_1 space group. |


## Biological / Functional Insights

### Electrostatic recognition of charged dipeptides by Lys314

Lys314 in the YePEPT substrate-binding pocket forms a salt bridge with
negatively charged N-terminal amino acid side chains of dipeptides (Asp-Ala,
Glu-Ala). This electrostatic interaction is the primary determinant of
specificity for charged substrates. In the apo structure, the positive charge
of Lys314 is stabilized by a hydrogen bond and pi-cation interaction with
Phe311. Mutation F311A severely impairs transport function, confirming the
importance of this stabilization.

### Tuning substrate specificity by charge reversal

The K314E charge reversal mutation in YePEPT switches specificity from
negatively charged dipeptides (Asp-Ala, Glu-Ala) to positively charged
dipeptides (Lys-Ala). The K314A mutation abolishes charged dipeptide
specificity entirely. This demonstrates that a single residue at position
314 controls charged dipeptide recognition via electrostatic complementarity.

### Conserved mechanism in human PEPT1

The corresponding residue in human PEPT1 is Gln300. Introduction of the
Q300K mutation into hPEPT1 conferred affinity for Asp-Ala while reducing
affinity for Lys-Ala, demonstrating that the electrostatic recognition
mechanism identified in YePEPT is transferable to the human peptide
transporter PEPT1.

### PZ pocket: a novel inhibitor-induced binding pocket in POTs

The LZNV-bound structure of YePEPT K314A reveals a previously undescribed mostly hydrophobic pocket (PZ pocket) that accommodates the Z(NO2) moiety of LZNV. The PZ pocket is comprised of 9 residues within 4.0 Å of the Z(NO2) moiety: F311, Q313, A314, F318, F386, M389, S412, I413, and L416. Most of these residues are conserved in bacterial peptide transporters as well as in human PEPT1 and PEPT2. A π-stacking interaction between F318 and the 4-nitrophenyl group of LZNV anchors the inhibitor in the PZ pocket. The PZ pocket is absent in the ligand-free (apo) state and forms only upon LZNV binding through conformational changes, suggesting its potential as a target for inhibitor design.

### Conformational changes and PZ pocket formation upon LZNV binding

Comparison of the apo and LZNV-bound structures of YePEPT K314A reveals three key conformational changes: (1) the N-terminal six-helix bundle undergoes a rigid body movement of ~5° towards the C-terminal bundle (hinge at the periplasmic region); (2) F318 adopts a new rotamer conformation to create space for the Z(NO2) moiety and form π-stacking with the 4-nitrophenyl group; (3) the hydroxyl group of Y35 (TM1) moves ~2 Å to interact with the LZNV carboxyl group, and Y159 (TM5) adopts a new rotamer with a 9.5 Å hydroxyl shift to orient E420 for ligand binding. The PZ pocket is initially absent in the apo state and forms upon inhibitor binding.

### Wedge mechanism of POT inhibition by LZNV

LZNV inhibits POTs through a unique mechanism: after the dipeptide backbone of LZNV binds to the conserved substrate-binding pocket, the Z(NO2) moiety induces formation of the initially absent PZ pocket via rotamer changes of specific amino acid side chains. The Z(NO2) moiety anchored deep in the C-terminal bundle acts like a wedge that impedes the transition from the inward-facing occluded state to the inward-open state, thereby blocking the transport cycle. This mechanism is supported by thermal shift assays, uptake competition experiments, and structural analysis of humanised YePEPT variants (K314Q-P315G) confirming relevance to human PEPT1/PEPT2.


## Cross-References

- [POT Family Substrate Specificity](/xray-mp-wiki/concepts/protein-families/pot-family-substrate-specificity/) — YePEPT defines the electrostatic mechanism for charged dipeptide recognition in the POT family
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) — YePEPT belongs to the MFS fold with N- and C-terminal six-helix bundles
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — YePEPT structure is in the inward-open conformation, representing one state of the alternating access cycle
- [Peptide Binding Pocket](/xray-mp-wiki/concepts/structural-mechanisms/peptide-binding-pocket/) — LZNV binds in the conserved substrate-binding pocket with additional PZ pocket interactions
- [PZ Pocket POT Inhibition](/xray-mp-wiki/concepts/structural-mechanisms/pz-pocket-pot-inhibition/) — LZNV-bound structure reveals the PZ pocket, a novel inhibitor-induced binding pocket
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
