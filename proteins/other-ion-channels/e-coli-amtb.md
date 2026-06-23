---
title: AmtB ammonium transporter / ammonia channel from Escherichia coli
created: 2026-06-08
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0406475101, doi/10.1074##jbc.M608325200]
verified: false
---

# AmtB ammonium transporter / ammonia channel from Escherichia coli

## Overview

AmtB is an ammonium transport protein (methylamine permease/ammonium transporter/Rhesus family member) from Escherichia coli that functions as an ammonia gas channel. The structure was determined in two crystal forms (R3 at 2.1 A and P6_3 at 1.8 A resolution), revealing a homotrimeric assembly with each monomer containing 11 transmembrane helices. Substrate transport occurs through a narrow hydrophobic pore at the center of each monomer, blocked on the periplasmic side by two phenylalanine residues (F107 and F215). Two highly conserved histidine residues (H168 and H318) form a hydrogen-bonded twin-His pair within the pore that is essential for substrate conductance. Site-directed mutagenesis of these histidines to 14 different polar and non-polar residues (H168A, H168E, H168F, H168Q, H168N, H168K, H168D, H168T, H318A, H318F, H318E, H168E/H318E) demonstrated that both histidines are absolutely required for optimum substrate conductance. Crystal structures of variants (H168A, H168E, H168F, H318A, H318F, H168A/H318A) confirmed that substitutions do not affect overall AmtB structure. The H168E variant showed partial activity, and its structure suggests the glutamate side chain can make similar interactions to histidine, explaining the natural Glu substitution found in some fungal Amt proteins. Residual electron density analysis in the pore revealed that inactive variants show no density at the central pore site S4, whereas wild-type and partially active H168E show strong peaks, correlating pore hydration with transport activity.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0406475101 | not stated in raw paper | 1.8 A | P6$_3$ | Wild-type full-length E. coli AmtB | None (apo structure) |
| doi/10.1074##jbc.M608325200 | not stated in raw paper | 2.0 A (best) | — | AmtB variants: H168A, H168E, H168F, H318A, H318F, H168A/H318A | None (apo structures) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Wild-type full-length AmtB

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and purification | Standard E. coli expression and membrane protein purification | -- | -- + [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) (lauryldimethylamine oxide) | AmtB was solubilized and purified in [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) detergent |


## Crystallization

### doi/10.1073##pnas.0406475101

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified AmtB in [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) |
| Reservoir | -- |
| Mixing ratio | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Crystals obtained in two forms: (1) R3 form using ammonium sulfate as precipitant at pH 4.6, (2) P6_3 form using MgSO4 as precipitant at pH 4.6. Both crystal forms grown at pH 4.6. |

### doi/10.1074##jbc.M608325200

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hexagonal crystal form) |
| Protein sample | Purified AmtB variants in [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) |
| Notes | Five functionally characterized His variants (H168A, H168E, H168F, H318A, H318F) and double mutant H168A/H318A crystallized in previously reported hexagonal form. Data collected at Swiss Light Source. Structures determined to 2.0-2.2 A resolution. Some crystals grown with ~150 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in buffer. |


## Biological / Functional Insights

### Ammonia gas channel mechanism

AmtB facilitates conduction of uncharged NH3 rather than NH4+ ions. The narrow hydrophobic pore is blocked by F107 and F215 on the periplasmic side, requiring transient structural fluctuations for substrate entry. Two conserved histidine residues (H168 and H318) form a lateral H-bonded pair in the pore, creating an electrostatic barrier of approximately 10 kcal/mol for NH4+ while permitting uncharged NH3 passage. This supports the model that Mep/Amt/Rh family proteins are ammonia gas channels rather than active transporters.

### Dual conformation at cytoplasmic exit

The cytoplasmic pore exit adopts two conformational states between the R3 (open exit) and P6_3 (closed exit) crystal forms. This conformational difference may be related to inactivation by a regulatory partner protein ([Glnk](/xray-mp-wiki/proteins/other-ion-channels/glnk/)). In the P6_3 structure, the pore exit is narrower and more hydrophobic compared to the R3 structure.

### Conserved pore architecture

The AmtB structure revealed a pseudo-twofold symmetry within each monomer, with TM1-TM5 related to TM6-TM10. The pore-lining residues are predominantly hydrophobic and highly conserved across the Mep/Amt/Rh family. Strictly conserved residues T234 and T273 are strategically positioned to orient conserved residues around the periplasmic pore entry, suggesting functional importance of this precisely packed structure.

### Ammonium binding site

A putative NH4+ binding site was identified at the bottom of the periplasmic depression, surrounded by F103, F107, W148, S219, and a water molecule. This site likely controls entry into the pore and accounts for observed saturation of transport rate. No significant competitive inhibition by alkali cations (Na+, K+) was observed, suggesting specificity for ammonium.

### Twin-His motif is essential for optimum substrate conductance

Mutagenesis of His-168 and His-318 to 14 different polar and non-polar residues (Ala, Glu, Phe, Gln, Asn, Lys, Asp, Thr) in E. coli AmtB demonstrated that both histidines are absolutely required for optimum methylammonium transport activity. Crystal structures of variants confirmed no structural perturbation beyond the mutated residue. In a subgroup of fungal Amt proteins, one histidine is naturally replaced by glutamate, and the equivalent H168E substitution is partially active (~30% of WT), suggesting the Glu side chain can make similar interactions to His. Rh30 proteins (RhD, RhCE) lack the twin-His motif entirely and likely do not function as ammonium channels.

### Pore hydration correlates with transport activity

Residual difference electron density analysis in the pore at sites S2, S3, and S4 showed a strong correlation between pore hydration and transport activity. Inactive variants (H168A, H318A, H168F, H318F) show no density above 2sigma at site S4, whereas wild-type and partially active H168E show peaks above 4sigma at S3 and S4. The double mutant H168A/H318A shows no significant peak in the widened pore. The H168E variant shows enhanced pore hydration with a larger peak at site S2, consistent with the charged glutamate side chain attracting water/ammonia molecules. These results link the twin-His motif to the structural hydration of the pore required for NH3 conductance.


## Cross-References

- [Ammonia Channel Mechanism](/xray-mp-wiki/concepts/ammonia-channel-mechanism/) — AmtB is the prototype ammonia channel; this paper established the mechanistic basis for NH3 transport through the Amt/Mep/Rh family
- [Ammonium Transport](/xray-mp-wiki/concepts/ammonium-transport/) — AmtB is an ammonium transport protein from the Mep/Amt/Rh family
- [Rh/Amt/MEP Protein Family](/xray-mp-wiki/concepts/protein-families/rh-amt-mep-protein-family/) — AmtB is the paradigm Amt family member; twin-His mechanism is conserved across the family
- [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) — Referenced in context related to LDAO
- [Glnk](/xray-mp-wiki/proteins/other-ion-channels/glnk/) — Referenced in context related to Glnk
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in context related to Imidazole
