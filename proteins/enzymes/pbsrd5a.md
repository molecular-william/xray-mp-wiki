---
title: PbSRD5A Steroid 5α-Reductase (Proteobacteria bacterium)
created: 2026-06-09
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-20675-2]
verified: false
---

# PbSRD5A Steroid 5α-Reductase (Proteobacteria bacterium)

## Overview

PbSRD5A is a steroid 5α-reductase from *Proteobacteria bacterium*, a homolog of human SRD5A1 and SRD5A2. It is a monomeric enzyme with seven transmembrane segments (TM1-7) that catalyzes the NADPH-dependent reduction of the 3-oxo-Δ⁴ carbon-carbon double bond in steroid hormones (testosterone, progesterone, 4-androstene-3,17-dione) to generate their corresponding 3-oxo-5α steroids. The crystal structure of PbSRD5A in complex with NADPH was determined at 2.0 Å resolution. TM1-4 enclose a hydrophobic substrate binding cavity, while TM5-7 coordinate the NADPH cofactor through an extensive hydrogen bond network. A conserved Q-E-Y catalytic motif (Q53-E54-Y87 in PbSRD5A; Q56-E57-Y91 in HsSRD5A2) is essential for substrate recognition and catalysis. The structure provides a framework for understanding disease-related mutations in human SRD5A2 associated with steroid 5α-reductase 2 deficiency.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-020-20675-2 | 7D7L | 2.00 | Unknown | Full-length PbSRD5A with N-terminal 10XHis tag | NADPH |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (SF9) insect cells
- **Construct**: N-terminal 10XHis tag, pFastBac vector, Bac-to-bac system
- **Induction**: Baculovirus infection at 2 × 10⁶ cells/ml
- **Media**: SF9 insect cell medium

### Purification Workflow

- **Expression system**: SF9 insect cells
- **Expression construct**: N-terminal 10XHis tag
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and infection | Baculovirus infection | -- | -- | SF9 cells at 2 × 10⁶ cells/ml, 10 ml virus/L culture, 60 h post-infection |
| Cell harvesting | Centrifugation | -- | -- | Frozen at -80°C until use |
| Protein purification | Affinity chromatography | -- | -- | Purified via N-terminal 10XHis tag |

**Final sample**: Purified PbSRD5A
**Purity**: Purified to homogeneity


## Crystallization

### doi/10.1038##s41467-020-20675-2

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Notes | Crystallization conditions and details not fully specified in extracted text. Structure solved at 2.0 Å resolution. X-ray diffraction data collected at Shanghai Synchrotron Radiation Facility (SSRF). |


## Biological / Functional Insights

### Seven-transmembrane architecture with distinct functional domains

PbSRD5A adopts a fold with seven transmembrane segments divided into two functional domains. TM1-4 form a hydrophobic substrate binding cavity, while TM5-7 coordinate the NADPH cofactor. The TM1 exhibits significantly higher B-factor values, suggesting conformational flexibility important for substrate entry and release. A short intracellular loop 1 (Y32, R34) and loop 3 (Y177) also contribute to NADPH binding. The topology model reveals an extracellular short alpha helix (ECH) and intracellular short alpha helix (ICH), along with short antiparallel beta strands.

### Conserved Q-E-Y catalytic motif

A highly conserved Q-E-Y motif (Q53-E54-Y87 in PbSRD5A; Q56-E57-Y91 in HsSRD5A2) is essential for substrate recognition and catalysis. In the substrate-free PbSRD5A structure, Y87 donates a hydrogen bond to a water molecule, which is in turn hydrogen-bonded with E54. This water molecule occupies a position close to the carbonyl oxygen of substrates observed in docking models, analogous to observations in AKR1D1 structures. The conserved tyrosine (Y91 in HsSRD5A2) acts as a super acidic hydrogen bond donor, and the adjacent protonated glutamate (E57 in HsSRD5A2) helps enolize the alpha,beta-unsaturated ketone moiety for hydride transfer from NADPH to C5. Mutagenesis of Q56A/L, E57L, and Y91F in HsSRD5A2 abolished reductase activity.

### NADPH coordination by TM5-7

The NADPH cofactor is coordinated by an extensive hydrogen bond network involving residues on TM5-7 (N159, D163, R170 on TM5; N192, Y193, E196 on TM6; T219, N222, R226, H230 on TM7) and intracellular loops (Y32, R34 on loop 1; Y177 on loop 3). Additional residues interact with NADPH through water-mediated hydrogen bonds (R34, V100, N192, R226) or hydrophobic effects (W50 on TM2, F94 and M98 on TM3, L166 and L169 on TM5, L223 on TM7). Mutations in these residues impaired the conversion of progesterone to 5alpha-dihydroprogesterone in in vitro reduction assays.

### Substrate binding pocket accommodates steroid substrates

The substrate binding cavity is formed primarily by TM1-4 and is lined by hydrophobic residues. In the crystal structure, a monoolein lipid molecule from the LCP crystallization occupies the steroid binding pocket, with its alkenyl tail accommodated well within the hydrophobic cavity and the glycerol head forming a hydrogen bond with Q53. Docking studies with testosterone, progesterone, and 4-androstene-3,17-dione show that the steroid substrates bind in the same pocket, positioning the 3-oxo-Delta4 group near the NADPH nicotinamide for hydride transfer. The cytosolic half of TM1 and TM2 likely plays critical roles in recognizing the C-17 tail of steroid substrates, with TM1 and TM4 being the most variable regions across SRD5A homologs, potentially encoding substrate specificity.

### Disease-related mutations mapped to HsSRD5A2 model

Thirty-two disease-related loss-of-function mutations in HsSRD5A2 (causing steroid 5alpha-reductase 2 deficiency) were classified into five categories based on the homology model: (1) catalytic site residues (Q56, E57, Y91) in the substrate binding pocket; (2) NADPH-binding residues (N160, D164, R171, N193, E197, R227, H231, Y235); (3) structural destabilization residues forming hydrogen bond networks; (4) C-terminal variants (P181L, S245Y, R246Q/W) that may destabilize NADPH binding; and (5) Gly-to-X and X-to-Gly variants at TM interfaces disrupting tertiary structure. All variants except H231A showed significantly decreased reductase activity in biochemical assays.

### Conserved NADPH-mediated reduction mechanism

The catalytic mechanism of SRD5A involves a two-step reduction. In the first step, NADPH coordinates on the alpha face of the steroid substrate and provides a hydride (H-) to C5 of the 3-oxo-Delta4 steroid. A proton is transferred from the protonated glutamate (E57 in HsSRD5A2) to C4 to complete the Delta4 carbon-carbon double-bond reduction. Molecular dynamics simulations suggest limited space (<15 A3) in the catalytic site to accommodate an additional water molecule as proton donor, supporting direct proton donation by the glutamate side chain. This mechanism is conserved across all SRD5A homologs and is also shared with AKR1D1.

### Inhibitor sensitivity of bacterial SRD5A homolog

PbSRD5A is inhibited by dutasteride (IC50 = 1.59 +/- 0.19 uM), which inhibits both human SRD5A1 and -2, and by finasteride (weaker inhibition), which specifically inhibits human SRD5A2. This inhibitor sensitivity profile of PbSRD5A is similar to human SRD5A1 but not SRD5A2, consistent with the distinct substrate preferences of the isozymes. PbSRD5A primarily converts progesterone to 5alpha-dihydroprogesterone, while HsSRD5A2 prefers testosterone.


## Cross-References

- [NADPH](/xray-mp-wiki/reagents/cofactors/nadph/) — Essential cofactor for steroid reduction
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — LCP crystallization lipid; occupies substrate binding pocket
- [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — Affinity tag for purification
- [Finasteride](/xray-mp-wiki/reagents/ligands/finasteride/) — SRD5A2-specific inhibitor
- [Dutasteride](/xray-mp-wiki/reagents/ligands/dutasteride/) — Dual SRD5A1/SRD5A2 inhibitor
- [Steroid 5alpha-Reductase Family](/xray-mp-wiki/concepts/steroid-reductase-family/) — Enzyme family classification
