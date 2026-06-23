---
title: "Gdx-Clo SMR Transporter (Clostridales oral taxon 876)"
created: 2026-06-09
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-19820-8, doi/10.1073##pnas.2403273121]
verified: false
---

# Gdx-Clo SMR Transporter (Clostridales oral taxon 876)

## Overview

Gdx-Clo is a small multidrug resistance (SMR) family transporter from *Clostridales* oral taxon 876, belonging to the guanidinium (Gdx) subtype of SMR transporters. It is a dual-topology antiparallel homodimer with each subunit comprising 4 transmembrane helices (4-TM). Gdx-Clo functions as a Gdm⁺/H⁺ antiporter and exhibits promiscuous transport of hydrophobic substituted cations. The crystal structure of Gdx-Clo in complex with a synthetic monobody (Clo-L10) was determined at up to 2.3 Å resolution, revealing the molecular basis for substrate promiscuity. A membrane portal between the TM2 helices provides direct access for hydrophobic substrate substituents from the lipid bilayer. The two subunits adopt non-equivalent A and B conformations, with the strictly conserved substrate- and proton-binding glutamate E13ₐ and E13₆ accessible at the bottom of a large aqueous chamber open to one side of the membrane.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-020-19820-8 | 6XGQ | 3.50 | C121 | Full-length Gdx-Clo (residues 1-108) with Clo-L10 monobody | None (apo) |
| doi/10.1038##s41467-020-19820-8 | 6XGR | 2.30 | C121 | Full-length Gdx-Clo with Clo-L10 monobody | Phenylguanidinium (phenylGdm⁺) |
| doi/10.1038##s41467-020-19820-8 | 6XGS | 2.30 | C121 | Full-length Gdx-Clo with Clo-L10 monobody | Octylguanidinium (octylGdm⁺) |
| doi/10.1073##pnas.2403273121 | 8VXU | 2.5 |  | Gdx-Clo A60T mutant in complex with cetrimonium (CTA⁺). Structure determined at ~2.5 Å resolution (SI Appendix, Table S1). The CTA⁺ quaternary ammonium headgroup binds ~2.5 Å higher and ~4 Å farther back in the pocket than guanidinyl substrates, with the alkyl tail extending through a membrane portal between helices 2A and 2B. | Cetrimonium (CTA⁺) |

## Expression and Purification

- **Expression system**: Escherichia coli C41 (DE3)
- **Construct**: C-terminal hexahistidine tag with LysC recognition site, cloned in pET-21c
- **Induction**: 0.2 mM IPTG for 3 h at 37°C

### Purification Workflow

- **Expression system**: E. coli C41 (DE3)
- **Expression construct**: C-terminal His6-tag with LysC site
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | LB medium + -- | Standard E. coli culture |
| Induction | Chemical induction | -- | -- | 0.2 mM IPTG, 3 h at 37°C |
| Membrane extraction | Detergent solubilization | -- | 100 mM NaCl, 20 mM imidazole + 2% (w/v) [Decyl Maltoside (DM)](/xray-mp-wiki/reagents/detergents/decyl-maltoside) | Cell lysate extracted with DM |
| Affinity chromatography | Immobilized metal-affinity chromatography (IMAC) | Cobalt affinity column | 100 mM NaCl, 20 mM imidazole (wash); 400 mM imidazole (elution) + 5 mM DM | His6-tag purification |
| Tag cleavage | Proteolytic cleavage | -- | -- | LysC protease (200 ng per mg protein, 2 h at room temperature) |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 | 100 mM NaCl, 10 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes)-NaOH, pH 8.1 + 5 mM DM | Final purification step |

**Final sample**: 10 mg/ml in DM
**Purity**: Purified to homogeneity


## Crystallization

### doi/10.1038##s41467-020-19820-8

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 10 mg/ml Gdx-Clo dimer mixed with Clo-L10 monobody at 2:1:1 ratio |
| Reservoir | 200 mM CaCl₂, 0.1 M Tris-HCl pH 8.0, 32-36% PEG 600 |
| Mixing ratio | 0.45 µl protein + 0.3 µl reservoir |
| Temperature | 20 |
| Growth time | 14 days |
| Cryoprotection | Flash-cooled in liquid nitrogen |
| Notes | Initial hits improved by adding charged detergents (LDAO, Apo12) or octylGdm⁺ to protein solution before mixing. For selenomethionine-incorporated protein: 0.1 M LiNO₃, 0.1 M ADA pH 6.8, 35% PEG 600. For phenylGdm⁺-bound: 0.1 M LiNaSO₄, 100 mM Tris pH 8.8, 34% PEG 600. For octylGdm⁺-bound: 0.1 M calcium acetate, 0.1 M HEPES pH 7.5, 33% PEG 600. Data collected at LS-CAT beamline 21-ID-D (APS). |


## Biological / Functional Insights

### Dual topology antiparallel homodimer architecture

Gdx-Clo forms an antiparallel homodimer where the two 4-TM subunits are arranged in opposite orientations relative to the membrane plane. This dual topology architecture is extremely rare and is a defining feature of the SMR family. The two subunits adopt non-equivalent A and B conformations. Transport involves a conformational swap between the two structurally distinct monomers, sealing the substrate binding site on one side of the membrane while opening an identical site on the opposite side. As a consequence of the antiparallel architecture, the inward-open and outward-open conformations are structurally identical, related by twofold symmetry about an axis parallel to the membrane plane.

### GxxxAxxxG packing motifs mediate conformational exchange

The conformational exchange between A and B subunits is facilitated by two GxxxAxxxG packing motifs in TM3. The first motif (G65-I66-G69 in Gdx-Clo, corresponding to G65I G in EmrE numbering) mediates tight helix packing, while the second motif (G72-A76-G79) forms a looser interface. During the conformational swap, regions that alternate in solvent accessibility include TM2, loop 2, and the first GxxxAxxxG motif of TM3 (magenta in the structure), and TM1, loop 1, and the second GxxxAxxxG motif of TM3 (dark blue).

### Minimal substrate coordination enables promiscuity

The strictly conserved E13ₐ and E13₆ form the substrate- and proton-binding site. The guanidinyl group of transported substrates coordinates with E13 via a single hydrogen bond, in contrast to the bidentate coordination observed in solution or by guanidine riboswitches. This minimal coordination explains the permissiveness of Gdx-Clo towards guanidinium ions with methyl, ethyl, or phenyl substitutions. The E13ₐ is deflected by a cross-subunit interaction with Y59₆, and displacement of Y59₆ by the guanidinyl group is proposed to initiate the transport motion.

### Membrane portal for hydrophobic substrate access

A cleft between the antiparallel TM2 helices of the two subunits provides a portal from the membrane to the substrate binding site. This portal accommodates hydrophobic substituents that partition into the lipid bilayer, as demonstrated by the octylGdm⁺-bound structure where the eight-carbon tail protrudes into the detergent micelle. The portal is lined by hydrophobic residues including M39 and F43 on TM2 that undergo rotameric rearrangements to accommodate bulky substituents. This feature provides a selectivity mechanism against physiological guanidinylated metabolites (arginine, creatine, agmatine) that have polar tail groups with high energetic penalty for membrane insertion.

### Functional promiscuity across SMR subtypes

Both the Qac subtype (exemplified by EmrE) and Gdx subtype (Gdx-Clo) of SMR transporters exhibit promiscuous transport of hydrophobic substituted cations. Solid-supported membrane (SSM) electrophysiology and radioactive exchange assays showed that Gdx-Clo transports guanidinyl compounds with hydrophobic single substitutions (methylGdm⁺, ethylGdm⁺, phenylGdm⁺), while EmrE requires additional hydrophobicity and bulk and accommodates substrates with reduced H-bonding capacity (tetramethylGdm⁺, tetramethylammonium). The broad substrate range and presence with horizontal gene transfer elements suggests that promiscuous transport functions contribute to the evolutionary success and dissemination of SMR genes.

### Engineering quaternary ammonium transport via peripheral mutations

Combinatorial mutagenesis and deep sequencing identified seven mutations (G10I, W16G, A17T, M39Y, A60T, A67I, K101N) that convert the selective Gdx-Clo into a promiscuous quaternary ammonium antiseptic exporter (Gdx-Clo-7x). The mutations cluster into three groups: cluster 1 (G10I) at the TM1-TM2 interface, cluster 2 (W16G/A17T/M39Y) near the binding site, and cluster 3 (A60T/A67I/K101N) at the membrane portal. Crucially, substrate preference changes not through modification of residues that directly interact with the substrate but through peripheral mutations that remodel the binding pocket hydrogen bond network and increase sidechain flexibility. Cluster 1 and 2 mutations are necessary and sufficient for polyspecific quaternary ammonium transport, while cluster 3 mutations enhance transport rate. The engineered Gdx-Clo-7x loses Gdm⁺ transport and acquires the substrate preference profile characteristic of EmrE and the SMR_Qac subtype, recapitulating a plausible evolutionary pathway.


## Cross-References

- [EmrE (E. coli SMR transporter)](/xray-mp-wiki/proteins/abc-transporters/emre/) — Prototypical Qac subtype SMR transporter for structural and functional comparison
- [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — Affinity tag for purification
- [Decyl Maltoside (DM)](/xray-mp-wiki/reagents/detergents/decyl-maltoside/) — Detergent for solubilization and purification
- [LDAO (Lauryldimethylamine-N-Oxide)](/xray-mp-wiki/reagents/detergents/ldao/) — Charged detergent additive for crystallization
- [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/) — Crystallization precipitant
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Crystallization buffer
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Purification and crystallization buffer
- [SMR Family (Small Multidrug Resistance Transporters)](/xray-mp-wiki/concepts/smr-family/) — Transporter family classification
