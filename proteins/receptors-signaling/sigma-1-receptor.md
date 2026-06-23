---
title: Human Sigma-1 Receptor (SIGMAR1)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17391]
verified: false
---

# Human Sigma-1 Receptor (SIGMAR1)

## Overview

The human sigma-1 receptor (SIGMAR1) is an ER-resident single-pass transmembrane protein and evolutionary isolate with no discernible similarity to other human protein families. It functions as an ER chaperone and regulator of calcium signaling, modulating various ion channels and GPCRs. Mutations in SIGMAR1 are linked to juvenile-onset amyotrophic lateral sclerosis (ALS). The receptor forms a trimer with a cupin-like beta-barrel ligand-binding domain and a single transmembrane helix per protomer, revealing an unexpected single-pass transmembrane topology.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature17391 | 5HK1 | 2.5 A | P21212 | Human sigma-1 receptor with N-terminal hemagglutinin signal sequence, FLAG epitope tag, and 3C protease cleavage site (GPGS scar after tag removal); expressed in Sf9 insect cells | PD144418 |
| doi/10.1038##nature17391 | 5HK2 | 3.2 A | P21212 | Human sigma-1 receptor with N-terminal hemagglutinin signal sequence, FLAG epitope tag, and 3C protease cleavage site (GPGS scar after tag removal); expressed in Sf9 insect cells | 4-IBP |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 insect cells (FastBac system, ThermoFisher) | — | Not specified | Human sigma-1 receptor cloned into pFastbac1 with N-terminal HA signal sequence, FLAG tag, and 3C protease cleavage site; infected at 4x10^6 cells/mL, shaken at 27 C for 2 days |
| Cell lysis | Osmotic shock in 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 2 mM magnesium chloride, benzonase nuclease | — | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 2 mM magnesium chloride | Frozen cell paste thawed and lysed by osmotic shock; centrifuged at 20,000 rpm for 15 min |
| Solubilization | [LMNG](/xray-mp-wiki/reagents/detergents/lmng) (1% w/v) and CHS (0.1% w/v) in 250 mM NaCl, 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) | — | 250 mM NaCl, 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng), 0.1% CHS | Glass dounce tissue grinder, stirred 2 hr at 4 C, centrifuged 20 min, filtered on glass microfiber |
| FLAG affinity chromatography | Anti-FLAG antibody affinity resin (5 mL) | — | 100 mM NaCl, 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 2 mM calcium chloride, 0.2% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng), 0.01% CHS | Gravity flow loading; extensive washing in two buffer conditions; elution with 5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta) and 0.2 mg/mL FLAG peptide |
| Tag cleavage | 3C protease (1:100 w:w) | — | Same as elution buffer without calcium | Incubated at 4 C overnight; resulting protein identical to wild-type except GPGS scar |
| Size-exclusion chromatography | Sephadex S200 column (GE Healthcare) | — | 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng), 0.001% CHS, 100 mM NaCl, 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 1 uM ligand | Protein consistently ran as high molecular weight oligomer during SEC |
| Final concentration | Concentration to 20-30 mg/mL | — | 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng), 0.001% CHS, 100 mM NaCl, 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 1 uM ligand | Flash frozen with liquid nitrogen in 8-9 uL aliquots; stored at -80 C |


## Crystallization

### doi/10.1038##nature17391

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | 10:1 [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein):[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) (w:w) |
| Temperature | Not specified |
| Notes | Purified receptor reconstituted into LCP by mixing with 10:1 [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein):[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) at 1.5:1 lipid:protein ratio by mass using coupled syringe method. Dispersed in 30-40 nL drops overlaid with 600 nL precipitant (40-50% [PEG](/xray-mp-wiki/reagents/additives/peg) 300, 220-250 mM Li2SO4, 0.1 M [MES](/xray-mp-wiki/reagents/buffers/mes) pH 6.5) using Gryphon LCP robot. Crystals grew over 2-4 weeks.
 |


## Biological / Functional Insights

### Cupin-like beta-barrel ligand-binding domain

Each protomer contains a cupin-like beta-barrel fold with the ligand at its center, flanked by four alpha helices. The ligand-binding domain is highly conserved across species. The fold closely resembles cupin family proteins, most of which are oligomeric bacterial enzymes, suggesting the sigma-1 receptor may represent a repurposed enzyme in which the catalytic site inside the beta-barrel has been co-opted as a ligand binding site.

### Ligand-binding pocket architecture

The binding pocket is deeply buried, highly hydrophobic, and completely occluded from solvent. Ligands interact with the receptor through a charge-charge interaction with Glu172. Asp126 forms a 2.7 A hydrogen bond with Glu172. Other binding site residues include Val84, Trp89, Met93, Leu95, Leu105, Phe107, Ile124, Trp164, Leu182 (hydrophobic contacts), and Tyr103 (aromatic stacking). The occluded structure accounts for slow ligand binding kinetics.

### ALS-associated E102Q mutation mechanism

Glu102 is deeply buried, with its carboxyl oxygen atoms accepting hydrogen bonds from backbone amides of Val36 and Phe37, part of a structured tether between the transmembrane and cytosolic domains. The E102Q mutation blocks this interaction, converting a favorable hydrogen bond into an energetically unfavorable juxtaposition of donors, accounting for receptor destabilization, aggregation, and TDP43 mislocalization observed in juvenile-onset ALS.

### Oligomerization state and ligand-mediated regulation

The sigma-1 receptor forms trimers in the crystal with an interface of 9300 A^2 between protomers. [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals) and native PAGE revealed polydisperse oligomers ranging from hexamers to 15-mers (140-400 kDa excluding detergent). In LMNG/CHS mixed micelles, agonists partially disrupt high-order oligomers while antagonists stabilize them, suggesting oligomerization is a key functional property linked to ligand efficacy.

### Single-pass transmembrane topology

The structure reveals a single transmembrane domain per protomer, contrary to prevailing models proposing a two-pass transmembrane architecture. The three transmembrane helices are widely separated at corners of the triangular trimer, mediating lattice contacts rather than inter-protomer interactions. The flat, hydrophobic membrane-proximal cytosolic surface suggests intimate association with the cytosolic surface of the ER membrane.


## Cross-References

- [PD144418](/xray-mp-wiki/reagents/ligands/pd144418/) — High-affinity sigma-1 antagonist used in co-crystallization (PDB 5HK1)
- [4-IBP](/xray-mp-wiki/reagents/ligands/4-ibp/) — Sigma-1 ligand used in co-crystallization (PDB 5HK2)
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Primary detergent for solubilization and purification
- [Cholesterol Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Lipid additive in solubilization and LCP crystallization
- [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals/) — Used to assess oligomerization state of sigma-1 receptor
- [Cupin Fold](/xray-mp-wiki/concepts/structural-mechanisms/cupin-fold/) — Structural fold of the ligand-binding domain
- [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) — Epitope tag used for affinity purification of sigma-1 receptor
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for crystallization of sigma-1 receptor
- [MES](/xray-mp-wiki/reagents/buffers/mes) — Buffer component in crystallization
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) — Entity mentioned in text
