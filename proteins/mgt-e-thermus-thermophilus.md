---
title: MgtE Mg2+ Transporter from Thermus thermophilus
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature06093]
verified: false
---

# MgtE Mg2+ Transporter from Thermus thermophilus

## Overview

MgtE from Thermus thermophilus is a magnesium transporter (Mg2+ influx system) belonging to the MIT (Metal Ion Transporter) superfamily. The protein functions as a dimer and contains a transmembrane domain (TM1-TM5 helices), an N domain, and CBS (cyclic nucleotide-binding) domains connected by helices. Structures of the full-length protein and isolated cytosolic domains reveal the architecture of a Mg2+ transporter and provide insights into ion selectivity and regulatory Mg2+ coordination. The cytosolic domain structures were determined with and without Mg2+ bound, revealing conformational changes associated with ion binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature06093 | TBD | 3.5 A | C2221 | Full-length MgtE dimer from Thermus thermophilus (TM domain, N domain, CBS domains, connecting helices) | Putative Mg2+ (Mg1 site in ion-conducting pore) |
| doi/10.1038##nature06093 | TBD | 2.3 A | P6522 | Cytosolic domain of MgtE from Thermus thermophilus (with Mg2+) | Mg2+ (bound at regulatory sites Mg4 and Mg6) |
| doi/10.1038##nature06093 | TBD | 3.9 A | P212121 | Cytosolic domain of MgtE from Thermus thermophilus (Mg2+-free) | Apo (no Mg2+) |

## Expression and Purification

- **Expression system**: Not specified in supplementary information
- **Construct**: Cytosolic domain construct and full-length MgtE from Thermus thermophilus

No purification described.

## Crystallization

### doi/10.1038##nature06093

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (selenomethionine labeling, SAD phasing) |
| Protein sample | Full-length MgtE (SeMet) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Full-length MgtE crystallized in space group C2221 at 3.5 A resolution.
SeMet derivative data collected at Peak, Inflection, and Low-remote wavelengths.
Rwork/Rfree was 0.294/0.341. 13884 protein atoms and 18 ligand/ion atoms
in final model. B-factors: protein 115.4, ligand/ion 65.4. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (selenomethionine labeling, SAD phasing) |
| Protein sample | Cytosolic domain with Mg2+ (SeMet) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Cytosolic domain with Mg2+ crystallized in space group P6522 at 2.3 A resolution.
Native and SeMet data collected. Rwork/Rfree was 0.243/0.273 for native,
0.251/0.278 for SeMet peak. 2887 protein atoms in final model. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (selenomethionine labeling, SAD phasing) |
| Protein sample | Cytosolic domain without Mg2+ (SeMet) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Cytosolic domain without Mg2+ crystallized in space group P212121 at 3.9 A resolution.
SeMet data at Peak, Inflection, and High-remote wavelengths.
Rwork/Rfree was 0.347/0.369. 3984 protein atoms.
B-factors: protein 226.8. |


## Biological / Functional Insights

### Mg2+ coordination in the ion-conducting pore

The full-length MgtE structure at 3.5 A resolution reveals putative Mg2+ binding at the Mg1 site within the ion-conducting pore. The pore diameter at this site is approximately 8 A, which is too large for a fully-dehydrated Mg2+ ion. Two coordination models are proposed: the fully-hydrated model, where Mg2+ retains its hydration shell with bond lengths of 1.9-2.1 A and angles around 90 degrees characteristic of Mg2+ coordination, and the partially-hydrated model, where Mg1 is directly coordinated to Ala428 and Asp432 of subunit A or B, with intervening water molecules. The strong residual electron density peaks (4.0 sigma) beside conserved acidic residues support the Mg2+ assignment. The pore selectivity site (Asp432) may discriminate Mg2+ from Ni2+ based on hydrated radius differences (Mg2+ at 4.28 A vs Ni2+ at 4.04 A). Unlike CorA, Ni2+ is not transported by MgtE.

### Regulatory Mg2+ coordination sites

Multiple regulatory Mg2+ binding sites (Mg2-Mg6) were identified. In the full-length MgtE structure, Mg2 is coordinated near side chains of Asp214, Glu255, and Glu258, while Mg3 is coordinated near Glu216, Glu259, and Asp418. Distances from protein ligands to Mg2 range from 2.55 to 3.78 A. In the Mg2+-bound cytosolic domain, Mg4 is coordinated by Asp91 and Glu247 (2.19 and 2.34 A), and Mg6 by Asp95 and the main-chain carbonyl of Gly136 (1.79 and 2.06 A), with no water molecules intervening. Mg5 is coordinated by the main-chain carbonyl of Ala223 and side chain of Asp226 (1.85 and 2.18 A), consistent with the Enterococcus faecalis MgtE structure (2OUX).

### CBS domain conformational dynamics and ion selectivity

The CBS domains undergo Mg2+-dependent conformational rearrangement that influences pore opening. At low intracellular Mg2+ concentration, Mg2+ binding triggers domain rearrangement including pore-forming TM2 and TM5 helices, opening the pore on the cytosolic side. The periplasmic entrance of the pore is broadened to approximately 15 A, sequestering conserved Glu307 residues. The current structure likely represents the closed, inactive state. In the open, active state, a selectivity filter may form on the periplasmic side involving Glu307. The preceding portion of TM2 helix adopts a non-helical, flexible structure that might be restructured in the open state.


## Cross-References

- [Metal Ion Transporter (MIT) Superfamily](/xray-mp-wiki/concepts/mit-superfamily/) — MgtE is a member of the MIT superfamily of metal ion transporters
- [CorA Mg2+ Transporter](/xray-mp-wiki/concepts/cora-mg-transporter/) — CorA is the best-characterized MIT superfamily member; MgtE compared for ion selectivity
- [Escherichia coli CorA Mg2+ Channel](/xray-mp-wiki/proteins/ec-cor-a/) — Related Mg2+ transporter from the MIT superfamily
- [Magnesium Chloride (MgCl2)](/xray-mp-wiki/reagents/additives/mgcl2/) — Mg2+ is the physiological substrate transported by MgtE
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/allosteric-regulation/) — CBS domain-mediated allosteric regulation of ion transport
