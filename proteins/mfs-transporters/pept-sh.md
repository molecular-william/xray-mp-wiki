---
title: PepT_Sh — SLC15/POT Family Peptide Transporter from Staphylococcus hominis
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.7554##eLife.34995, doi/10.1073##pnas.1813715116]
verified: false
---

# PepT_Sh — SLC15/POT Family Peptide Transporter from Staphylococcus hominis

## Overview

PepT_Sh is a prokaryotic homolog of the mammalian proton-coupled oligopeptide transporters
PepT1 (SLC15A1) and PepT2 (SLC15A2), identified from *Staphylococcus hominis*. It belongs to
the POT (Proton-coupled Oligopeptide Transporter) family within the Major Facilitator
Superfamily ([MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/)) of secondary active transporters. PepT_Sh uses the proton electrochemical
gradient to drive concentrative uptake of di- and tripeptides and has proven capable of
recognizing and transporting prodrug molecules including the antiviral prodrug [Valacyclovir](/xray-mp-wiki/reagents/ligands/valacyclovir/)
and the photodynamic therapy agent 5-aminolevulinic acid. Crystal structures of PepT_Sh in
complex with these drugs revealed the structural basis for prodrug recognition by the SLC15
family, including a pharmacophore model for [Valacyclovir](/xray-mp-wiki/reagents/ligands/valacyclovir/) binding mediated through the amino
acid scaffold and ester bond interactions with conserved residues.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1813715116 | 6G29 | 3.10 | — | PepT_Sh in complex with [Valacyclovir](/xray-mp-wiki/reagents/ligands/valacyclovir/) |  |
| doi/10.1073##pnas.1813715116 | 6H7U | 2.50 | — | PepT_Sh in complex with 5-aminolevulinic acid |  |
| doi/10.1073##pnas.1813715116 | 6HZP | 2.80 | — | PepT_Sh in complex with 5-aminolevulinic acid (second structure) |  |
| doi/10.7554##eLife.34995 | 6EXS | 2.50 | — | PepT_Sh (SH1446) in complex with S-Cys-Gly-3M3SH (malodour precursor) | S-Cys-Gly-3M3SH |

## Expression and Purification

- **Expression system**: Not detailed in this study (previously described in ref 22)
- **Construct**: PepT_Sh full-length
- **Notes**: Expression and purification details are provided in reference 22 (Minhas & Newstead, 2018)

### Purification Workflow

- **Expression system**: Not detailed (referenced to ref 22)
- **Expression construct**: PepT_Sh full-length

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | As previously described (ref 22) | — |  | Protein produced and purified as reported in Minhas & Newstead (2018) |


## Crystallization

### doi/10.1073##pnas.1813715116

| Parameter | Value |
|---|---|
| Method | In meso (lipidic cubic phase) crystallization |
| Protein sample | Purified PepT_Sh incubated with 40 mM [Valacyclovir](/xray-mp-wiki/reagents/ligands/valacyclovir/) hydrochloride or 5-aminolevulinic acid for 4 h at 4°C |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Temperature | 4 |
| Growth time | 2-3 days |
| Cryoprotection | Crystals cryocooled directly in liquid nitrogen |
| Notes | Crystallization carried out at 4°C in 96-well glass sandwich plates. Protein-laden mesophase prepared by homogenizing [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) and protein solution using dual syringe mixing device. Data collected at Diamond I24 and ESRF ID23eh2. |


## Biological / Functional Insights

### Prodrug recognition mechanism in the SLC15 family

Crystal structures of PepT_Sh in complex with [Valacyclovir](/xray-mp-wiki/reagents/ligands/valacyclovir/) and 5-aminolevulinic acid
reveal that prodrug recognition is mediated through the amino acid scaffold and the ester
bond commonly used to link drug molecules to physiological ligands. [Valacyclovir](/xray-mp-wiki/reagents/ligands/valacyclovir/) binds in
the central peptide binding site with its L-valine scaffold interacting with conserved
residues E418 (TM10), N347 (TM8), N167 (TM5), Y41 (TM1), and Y79 (TM2). The purine ring
of [Valacyclovir](/xray-mp-wiki/reagents/ligands/valacyclovir/) interacts with Y163 via pi-pi stacking. 5-aminolevulinic acid adopts a
vertical orientation in the binding site, making fewer interactions compared with
physiological peptides.

### Pharmacophore model for valacyclovir binding

Comparison of the [Valacyclovir](/xray-mp-wiki/reagents/ligands/valacyclovir/) complex with previous dipeptide cocrystal structures
reveals a pharmacophore model where the amino terminus of the L-valine scaffold
interacting with N347 and E418, and the carbonyl group interacting with N167, are key
recognition determinants. The ester and ether groups of [Valacyclovir](/xray-mp-wiki/reagents/ligands/valacyclovir/) are accommodated
within the binding site but contribute less to affinity. This model provides a
structure-based route for further prodrug development targeting the SLC15 family.

### Peptide binding diversity in the POT family

Analysis of binding site variants reveals differential effects on di- and tripeptide
recognition, supporting a model where peptides are accommodated in different orientations
within the binding site. The vertical binding mode (observed for 5-aminolevulinic acid
and thioalcohol peptides) is associated with lower affinity compared with the horizontal
configuration observed for dipeptides.

### Structural basis of malodour precursor transport

PepT_Sh transports the human malodour precursor S-Cys-Gly-3M3SH, a dipeptide-conjugated
thioalcohol that is the primary causal molecule of axillary body odour. The 2.5 A
co-crystal structure (PDB 6EXS) reveals the Cys-Gly moiety binds in the conserved
peptide binding site, while the 3M3SH thioalcohol group extends into a ~10 A
hydrophobic pocket between helices H7 and H10. The peptide adopts a vertical
orientation similar to tri-alanine in PepT_St, sitting further up in the binding
site compared to natural peptides. Water-mediated interactions (particularly via
W107 bridging the peptide carboxyl/carbonyl groups to Asn347) are critical for
ligand recognition. This work identifies PepT_Sh as a target for malodour control.

### POT family transporters mediate Cys-Gly-conjugate uptake

This study demonstrated that POT (proton-coupled oligopeptide transporter) family
members, specifically E. coli [DTPB](/xray-mp-wiki/proteins/mfs-transporters/dtpb/) and S. hominis PepT_Sh (SH1446), are responsible
for the transport of Cys-Gly-(S) conjugated malodour precursors. ABC transporters
Opp and Dpp were unable to transport these substrates. This reveals a new biological
role for bacterial POT transporters in the uptake of thiol-conjugated peptides, and
explains why odour-producing Staphylococcus species have adapted to catabolize
the human-specific malodour precursor.


## Cross-References

- [Valacyclovir](/xray-mp-wiki/reagents/ligands/valacyclovir/) — Prodrug co-crystallized with PepT_Sh; reveals structural basis for prodrug recognition
- [5-Aminolevulinic Acid](/xray-mp-wiki/reagents/ligands/5-aminolevulinic-acid/) — Photodynamic therapy agent co-crystallized with PepT_Sh
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used for in meso crystallization of PepT_Sh
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Method used for PepT_Sh crystallization
- [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) — Related biological concept
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [DTPB](/xray-mp-wiki/proteins/mfs-transporters/dtpb/) — Related protein structure
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in purification or crystallization
