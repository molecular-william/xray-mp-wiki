---
title: Vrg4 GDP-Mannose Transporter (Saccharomyces cerevisiae)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature24464]
verified: false
---

# Vrg4 GDP-Mannose Transporter (Saccharomyces cerevisiae)

## Overview

Vrg4 is a GDP-mannose transporter from the yeast Saccharomyces cerevisiae, belonging to the SLC35 family of nucleotide sugar transporters. It is a 10-transmembrane helix protein that shuttles activated monosaccharides (nucleotide sugars) across the Golgi membrane, providing substrates for glycosyltransferases. Vrg4 displays strict specificity for guanine-containing nucleotides and recognizes both GMP and GDP-mannose. The transporter operates via an alternating-access mechanism with two structural repeats (TM1-TM5 and TM6-TM10). Vrg4 requires short-chain lipids for activity and was crystallized in the lipidic cubic phase.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature24464 | 5OGE | 3.22 | P212121 | Full-length Vrg4 | None (apo) |
| doi/10.1038##nature24464 | 5OGK | 3.60 | P1 | Full-length Vrg4 | GDP-mannose |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae
- **Construct**: C-terminal GFP-His6 fusion
- **Induction**: 1.5% galactose
- **Media**: Medium minus leucine with 2% lactate, induced with galactose

### Purification Workflow

- **Expression system**: Saccharomyces cerevisiae
- **Expression construct**: C-terminal GFP-His6 fusion
- **Tag info**: His6-tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | Medium minus leucine, 2% lactate + -- | 15L fermentation vessel, 24h growth |
| Induction | Chemical induction | -- | -- | 1.5% galactose from 25% w/v stock, 24h post-induction |
| Membrane preparation | Cell harvesting | -- | -- | Yeast collected after induction |
| Affinity chromatography | Immobilized metal-affinity chromatography | Ni-NTA | -- + 0.02% DDM | Standard IMAC protocols |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 (10/300) SEC column | -- + 0.3% DM | Detergent exchanged for reconstitution |

**Final sample**: 40 mg/ml in DDM
**Purity**: >95% by SDS-PAGE


## Crystallization

### doi/10.1038##nature24464

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase |
| Protein sample | 40 mg/ml Vrg4 in DDM |
| Lipid | Monoolein |
| Protein-to-lipid ratio | 60:40 |
| Temperature | 4 |
| Growth time | 4 days |
| Cryoprotection | Cryo-cooled directly in liquid nitrogen |
| Notes | Heavy-atom screening with 1-5 mM mercury derivatives; phases determined by long-wavelength anomalous dispersion (Hg/S-SAD) at 2.7 A |


## Biological / Functional Insights

### Nucleotide recognition via FYNN motif

The nucleotide pocket is formed by side chains from TM7 and TM8, interacting via the O6 carbonyl group with Asn221 (TM7) and Ser266 (TM8) and via the N2 amine group with Asn220 (TM7). These specific interactions with the O6 carbonyl of the guanine ring explain the lower IC50 values for GMP compared to AMP, which lacks an oxygen at this position. These asparagine residues are located within a conserved FYNN motif (F218-YNN), present only in transporters that recognize guanine-containing nucleotide sugars. Transport assays on alanine variants of Asn220 or Asn221 show equal reduction in overall transport, while removal of both results in complete loss of function.

### Ribose positioning

The ribose group forms interactions with side chains from both the N- and C-terminal halves of the transporter. The O2 oxygen resides within hydrogen-bonding distance of Tyr28 (TM1), Ser269 (TM8), and Tyr281 (TM9). Tyr28 is strictly conserved and its replacement with alanine abolishes transport. Tyr281 is semi-conserved but generally a bulky side chain; a phenylalanine substitution maintains function while alanine abolishes it, suggesting a bulky side chain is required to optimally position the ribose group and/or the nearby conserved Tyr28.

### Sugar recognition via GALNK motif

The first phosphate is positioned close to Met35 (TM1), while the second phosphate interacts with Lys289 (TM9), which forms part of the GALNK motif (G285-ALNK). Lys289 interacts with both the beta-phosphate and the glycosidic-bond oxygen. Both Lys289Ala and Gly285Ala reduced activity, with the lysine replacement being more severe. The sugar pocket also includes a conserved tyrosine, Tyr114 (TM4), which makes a hydrogen bond to the C2 hydroxyl on the mannose ring. A Tyr114Phe variant displayed reduced transport, highlighting the importance of a hydrogen-bond donor at this position.

### Disease mutations in human SLC35C1

Homology modeling of the human GDP-fucose transporter (SLC35C1) reveals the GTAKA motif replacing GALNK in the sugar pocket. Disease mutations causing leukocyte adhesion deficiency II (Arg147Cys and Thr308Arg) map to residues near the sugar binding site. Thr308 is on the same helix as the GTAKA motif and packs against TM10, while Arg147 is equivalent to Lys118 in Vrg4 and resides close to the sugar binding site. These mutations likely disrupt the sugar binding site.

### Alternating-access mechanism

Vrg4 uses an alternating-access mechanism with two structural repeat units (TM1-TM5 and TM6-TM10) related by a two-fold rotation in the plane of the membrane. The bound GDP-mannose sits at the center of rotation. The crystal structure captures the open-to-lumen state, with TM6-TM7 packed against TM8-TM9 to seal the cavity from the cytoplasm, while TM1-TM2 and TM3-TM4 are opened out. Repeat-swapped modeling reveals the open-to-cytoplasm state.

### Lipid dependence

Vrg4 requires short-chain-length lipids for function. Monoolein lipids were observed at the dimer interface in the crystal structure, contributing ~60% to the total buried surface area of 1514 A2. The hydrophobic belt is notably shorter (~30 A) than that observed for plasma or inner membrane transporters (~40 A). Lipid-mediated dimerization was suggested by the absence of lipid density at these sites in monomeric molecules in the unit cell.


## Cross-References

- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — LCP crystallization lipid
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent for purification
- [Decyl Maltoside (DM)](/xray-mp-wiki/reagents/detergents/decyl-maltoside/) — Detergent for reconstitution
- [PEG 400](/xray-mp-wiki/reagents/additives/peg-400/) — Crystallization precipitant
- [Sodium Citrate](/xray-mp-wiki/reagents/buffers/sodium-citrate/) — Crystallization buffer
- [Guanosine Diphosphate (GDP)](/xray-mp-wiki/reagents/ligands/gdp/) — Substrate analog
- [Guanosine Monophosphate (GMP)](/xray-mp-wiki/reagents/ligands/gmp/) — Substrate analog
- [SLC35 Family (Nucleotide Sugar Transporters)](/xray-mp-wiki/concepts/sl35-family/) — Transporter family classification
