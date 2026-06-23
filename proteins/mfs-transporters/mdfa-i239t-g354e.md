---
title: MdfA Multidrug Transporter I239T/G354E Variant (E. coli)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##s42003-019-0446-y]
verified: false
---

# MdfA Multidrug Transporter I239T/G354E Variant (E. coli)

## Overview

MdfA is a prototypical H+-coupled multidrug transporter from E. coli belonging to the Major Facilitator Superfamily (MFS). The I239T/G354E variant was engineered with altered substrate specificity, including the ability to export short dicationic compounds like methyl viologen (MV) which wild-type MdfA cannot transport. This work presents X-ray crystal structures of I239T/G354E in complexes with three electrically different ligands — LDAO (zwitterionic), MV (dicationic), and DXC (monoanionic) — at resolutions up to 2.2 Å. The structures reveal two discrete, non-overlapping substrate-binding sites (LDAO1 and LDAO2) within the transporter, with D34 and G354E serving as independent protonation sites enabling a drug/H+ stoichiometry of 1:2 or 2:2. The dual drug-binding sites can accommodate one or two drugs of various sizes and shapes, contributing to broad substrate specificity. Long-range electrostatic interactions, enhanced >10-fold by the low-dielectric membrane environment, mediate recognition of zwitterionic and cationic substrates and play a key role in substrate-triggered deprotonation. The study also reveals the mechanistic basis for distinguishing substrates from inhibitors in H+-dependent multidrug transporters.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s42003-019-0446-y | 6OOM | 2.2 | C2 | I239T/G354E mutant with C-terminal deca-histidine tag in modified pET28b vector, thrombin-cleaved | LDAO (n-dodecyl-n,n-dimethylamine-n-oxide) |
| doi/10.1038##s42003-019-0446-y | 6OOP | 2.8 | C2 | I239T/G354E mutant with C-terminal deca-histidine tag | MV (methyl viologen) |
| doi/10.1038##s42003-019-0446-y | 6OOQ | 3.0 | C2 | I239T/G354E mutant with C-terminal deca-histidine tag | DXC (deoxycholate) |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI
- **Construct**: I239T/G354E variant in modified pET28b with C-terminal deca-histidine tag
- **Notes**: Induced with 0.5 mM IPTG at 30°C for 4 h in LB media

### Purification Workflow

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI
- **Expression construct**: I239T/G354E with C-terminal deca-histidine tag
- **Tag info**: Deca-histidine tag (C-terminal)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French pressure cell | — |  | Multiple passages through pre-chilled French press |
| Membrane extraction | Solubilization | — | 1% (w/v) n-dodecyl-β-D-maltopyranoside (DDM) | Membranes collected by ultracentrifugation and extracted with DDM |
| Affinity chromatography | Ni-NTA | Ni-NTA column |  | Purified by Ni-NTA affinity chromatography |
| Size-exclusion chromatography | SEC | — |  | Final polishing step |

**Final sample**: Purified I239T/G354E in detergent-containing buffer


## Crystallization

### doi/10.1038##s42003-019-0446-y

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified I239T/G354E |
| Temperature | 24 °C |
| Notes | All three structures (LDAO-bound, MV-bound, DXC-bound) crystallized in C2 space group. Phase solved by molecular replacement combined with SAD phasing. Data collected at APS beamline 24ID-C. LDAO-bound at pH 8.0 (2.2 Å), MV-bound at pH 8.0 (2.8 Å), DXC-bound at pH 6.0 (3.0 Å). |


## Biological / Functional Insights

### Two discrete non-overlapping substrate-binding sites

The LDAO-bound structure of I239T/G354E reveals two distinct substrate-binding sites (LDAO1 and LDAO2) within the central cavity. LDAO1 is located in the N-domain and interacts primarily with D34; LDAO2 is in the C-domain and interacts with G354E. The two sites are separated by ~20 Å and the transporter can bind and export two LDAO molecules simultaneously, with each substrate molecule triggering proton release from its respective protonation site (D34 for LDAO1, G354E for LDAO2).

### D34 and G354E as dual protonation sites

The LDAO-bound I239T/G354E structure reveals that D34 and G354E serve as independent protonation sites. Upon LDAO binding, two protons are released (one from each site) — confirmed by fluorescence measurement showing 2.0 ± 0.1 H+ released per I239T/G354E molecule. MdfA (lacking G354E) or D34A/I239T/G354E (lacking D34) release only one proton per molecule upon LDAO binding, while D34A/I239T (lacking both) fails to release any protons. This establishes a drug/H+ stoichiometry of 1:2 (short dicationic) or 2:2 (two monocationic drugs) for I239T/G354E.

### Long-range electrostatic interactions in multidrug recognition

The study demonstrates that zwitterionic (LDAO) and cationic (MV) substrates are recognized by I239T/G354E via long-range charge-charge interactions enhanced >10-fold by the low-dielectric membrane environment. For MV binding, D34 and G354E are 8.3 Å and 5.8 Å from the positively charged N2 of MV, respectively, yet these electrostatic interactions effectively mediate substrate-triggered deprotonation. Unlike H-bonds, these interactions lack stringent geometric requirements, enabling the transporter to accommodate structurally diverse cationic drugs and explaining how additional drug-binding/protonation sites can be introduced into MdfA.

### Substrate vs. inhibitor distinction in H+-coupled antiporters

Comparison of DXC binding to MdfA (transportable substrate) vs. I239T/G354E (non-transportable inhibitor) reveals the molecular basis for substrate/inhibitor distinction. In MdfA/Q131R, D34 forms an H-bond with the C1-OH of DXC to trigger deprotonation; in I239T/G354E, G354E alters the DXC binding pose so that no such interaction is made with D34 or G354E, preventing deprotonation. This suggests that potent therapeutics could evade extrusion by H+-coupled antiporters if they lack the ability to trigger deprotonation, e.g., by methylation of key hydroxyl groups.

### Polyspecificity through combined H-bond and electrostatic mechanisms

MdfA interacts with electrically distinct substrates differently: H-bonds for electroneutral (chloramphenicol) and anionic (DXC) substrates; charge-charge interactions for zwitterionic (LDAO) and cationic (MV) substrates. Broad substrate specificity arises from the preponderance of non-specific hydrophobic interactions combined with long-range electrostatic interactions, making MdfA polyspecific rather than truly nonspecific. Specificity arises when H-bonds select certain drugs and size/shape constraints apply; promiscuity exists because many structurally dissimilar cationic compounds are recognized through flexible electrostatic interactions.


## Cross-References

- [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfa/) — Parent/background entity for the I239T/G354E engineered variant
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) — MdfA belongs to the MFS/DHA1 subfamily
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — Relevant transport mechanism for MdfA
