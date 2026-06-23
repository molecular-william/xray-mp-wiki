---
title: Aquaglyceroporin PfAQP from Plasmodium falciparum
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein]
sources: [doi/10.1038##nsmb.1431]
verified: false
---

# Aquaglyceroporin PfAQP from Plasmodium falciparum

## Overview

PfAQP is the sole aquaporin family member in the malarial parasite Plasmodium falciparum. It has the unusual property of conducting both glycerol and water at high rates, making it a benchmark for understanding the determinants of water vs. glycerol selectivity in the aquaporin family. The crystal structure of PfAQP was determined at 2.05 Å resolution, revealing a tetrameric assembly with each monomer containing eight transmembrane helices. The structure shows glycerol and water molecules alternating in single file along the conduction channel, providing a detailed atomic view of the transport mechanism. Unlike its closest structural homolog GlpF (an E. coli aquaglyceroporin with poor water conductance), the selectivity filter arginine (Arg196) in PfAQP donates three hydrogen bonds to protein moieties, matching the hydrogen-bonding pattern of water-selective aquaporins. This decreased desolvation energy of the guanidinium cation may provide the basis for high water conductance. The two NPA regions bear rare substitutions to NLA (Asn-Leu-Ala) and NPS (Asn-Pro-Ser), yet preserve the essential interactions that orient the signature asparagine residues into the channel center. PfAQP is important in malarial biology, facilitating glycerol uptake from host serum and ensuring survival during osmotic stress. The PfAQP knockout in the rodent parasite P. berghei impedes growth and decreases parasitemia.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.1431 | Not specified in publication | 2.05 | I422 | Synthetic gene optimized for E. coli codon usage; full-length PfAQP | Glycerol and water molecules in the conduction channel |

## Expression and Purification

- **Expression system**: Escherichia coli (synthetic gene optimized for codon usage; GeMS software used for gene design)
- **Construct**: Synthetic PfAQP gene designed to match E. coli codon usage and moderate 5′ transcript secondary structure (native A-T content >70%). Full-length protein with no affinity tag.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Membrane preparation | High-pressure homogenization and ultracentrifugation | — | 20 mM Tris pH 7.5, 500 mM NaCl, 10 mM EDTA, 4 mM β-mercaptoethanol, 1 mM PMSF | Cells lysed by Emulsiflex-C5 at 10,000-15,000 psi; membranes pelleted at 160,000g for 1 h |
| 2. Membrane solubilization and purification | Affinity chromatography? (detergent extraction) | — |  | Purified to homogeneity; ~1 mg of purified tetrameric protein from 6 L culture |

**Final sample**: Purified tetrameric PfAQP in detergent solution


## Crystallization

### doi/10.1038##nsmb.1431

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (presumed; crystallization details not fully specified) |
| Protein sample | Purified PfAQP |
| Temperature | Room temperature |
| Notes | Crystals grown in I422 space group with cell dimensions a=b=92.4 Å, c=193.2 Å. Data collected to 2.05 Å. Two crystals used for complete data collection. |


## Biological / Functional Insights

### Triply-satisfied arginine selectivity filter determines high water conductance

PfAQP conducts water as efficiently as water-specific channels, yet also passes glycerol well. A key structural difference from the homologous GlpF (which conducts water poorly) is the hydrogen-bonding network around the conserved selectivity filter arginine (Arg196). In low-water-conductance GlpF, only one of the two guanidinium NH donors (NH₁) is satisfied by protein hydrogen bonds. In PfAQP and all water-specific aquaporins, both NH₁ and NH₂ donate three hydrogen bonds to protein moieties. This triply-satisfied arginine has a decreased desolvation energy cost, allowing more rapid water passage through the channel.

### Compensatory mutations in NPA motifs preserve channel function

All Plasmodium aquaporins bear rare substitutions in the otherwise universally conserved NPA (Asn-Pro-Ala) motifs: NLA (Asn70-Leu71-Ala72) in the M3 half-helix and NPS (Asn193-Pro194-Ser195) in the M7 half-helix. Despite these changes, the essential interactions are preserved: the carbonyl of Asn70 accepts a hydrogen bond from Ala72's backbone amide, and Asn193's carbonyl accepts from Ser195's backbone amide. This maintains the proper orientation of the two signature asparagine N-H donors into the center of the conduction channel, which is essential for proton exclusion and substrate specificity.

### Glycerol and water conduction in proteoliposomes

Reconstituted PfAQP proteoliposomes show high rates of both glycerol and water conductance. Light-scattering assays measure glycerol conductance at 15.8 ± 0.2 (vs. 0.066 ± 0.003 for empty liposomes) and water conductance at 21.5 ± 0.8 (vs. 4.5 ± 0.1 for liposomes). These relative rates confirm that the heterologously expressed eukaryotic protein is fully functional and demonstrate PfAQP's dual high-efficiency conductance.

### Malarial aquaglyceroporin as a virulence factor

PfAQP is expressed on the parasite surface and is maximal during the later blood-stage when parasite growth is greatest. Knocking out the ortholog in P. berghei (PbAQP) impedes parasite growth, decreases parasitemia, and increases survival time of infected mice. The mutant parasites have greatly diminished glycerol uptake. Host AQP9 (the major glycerol uptake pathway in murine erythrocytes) knockout also increases mouse resistance to P. berghei infection, highlighting the importance of glycerol acquisition for malarial virulence.


## Cross-References
