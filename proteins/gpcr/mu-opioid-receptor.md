---
title: Murine Mu-Opioid Receptor
created: 2026-06-03
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11111, doi/10.1038##nature14886, doi/10.1038##nature10954]
verified: false
---

# Murine Mu-Opioid Receptor

## Overview

The murine mu-opioid receptor (muOR, MOP) is a class A G-protein-coupled receptor that mediates the analgesic and addictive properties of opiate alkaloids. The first X-ray crystal structure of muOR was determined at 2.8 A resolution in complex with the covalent antagonist [beta-FNA](/xray-mp-wiki/reagents/ligands/beta-fna) (Manglik et al., 2012, PDB 4DKL), revealing an inactive-state conformation with a large solvent-exposed binding pocket and a TM5-TM6 four-helix bundle dimer interface. An active-state structure was later solved at 2.1 A resolution in complex with the morphinan agonist [BU72](/xray-mp-wiki/reagents/ligands/bu72) and the G-protein mimetic [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody) Nb39 (Huang et al., 2015, PDB TBD). The active-state structure reveals conformational changes associated with receptor activation, including a 10 A outward displacement of transmembrane helix 6 and rearrangement of the conserved core triad (F6.44, P5.50, I3.40). The inactive structure crystallizes as a two-fold symmetrical dimer through a TM5-TM6 interface, providing structural insights into opioid receptor oligomerization and allosteric regulation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature14886 | TBD | 2.1 | I212121 | Full-length murine muOR with N-term Flag tag, C-term 6xHis tag, TEV site after residue 51, 3C site before residue 359 | BU72, Nb39 |
| doi/10.1038##nature10954 | 4DKL | 2.8 | C 1 2 1 | Murine muOR with N-term TEV site after residue G51, C-term truncation after Q360, ICL3 (residues 264-269) replaced with T4L (residues 2-161), N-term Flag M1 tag, C-term octa-histidine tag | beta-FNA (covalent, linked to K233^5.39) |

 - R-work 18.53%, R-free 22.15%; Atoms: 3278 protein atoms, 32 ligand ([BU72](/xray-mp-wiki/reagents/ligands/bu72)) atoms, 208 lipid/water/other atoms; Data collection: Merged from four crystals at 2.1 A resolution
 - R-work 0.2326%, R-free 0.2753%; Data collection: Merged from 25 crystals at 2.8 A resolution

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### Inactive-State Conformation and beta-FNA Binding

The inactive muOR structure reveals an exposed, solvent-accessible binding pocket, in stark contrast to the buried pockets of aminergic receptors. [Beta-FNA](/xray-mp-wiki/reagents/ligands/beta-fna) (beta-funaltrexamine) binds deeply in the orthosteric pocket with its morphinan core engaging D147^3.32 (charge-charge interaction with the amine) and H297^6.52 (pi-stacking with the aromatic ring). The covalent bond to K233^5.39 positions the ligand irreversibly. The fumarate moiety extends toward the extracellular surface. Fourteen residues within 4 A of the ligand, of which 11 are identical between muOR and delta-OR, explain the high conservation of opioid binding across subtypes.

### TM5-TM6 Four-Helix Bundle Dimer Interface

The muOR crystallizes as a two-fold symmetrical dimer through a TM5-TM6 four-helix bundle interface with a buried surface area of 1,492 A^2 per protomer (92% of total inter-molecular contact). A secondary TM1-TM2-H8 interface contributes 615 A^2. The dimeric arrangement would likely preclude G-protein coupling, consistent with inverse agonists stabilizing receptor oligomers. Residues at the interface show high homology with delta-OR, suggesting heterodimeric muOR-deltaOR complexes could share the same interface. The two binding sites are coupled through packing interactions at the dimeric interface, providing a structural basis for allosteric cross-talk between protomers.

### Active-State Conformational Changes

Upon activation, muOR undergoes a 10 A outward displacement of TM6 and smaller inward movements of TM5 and TM7. The extracellular domain shows minimal changes except at the proximal N terminus. The conserved E/DRY motif rearranges: in the inactive state, R165^3.50 forms a hydrogen bond with T279^6.34; in the active state, R3.50 forms a hydrogen bond with Y5.58^5.58, stabilizing inward movement of TM5. A parallel dimer interface involving TM1, TM2, ECL1, and H8 is observed in both inactive and active states with 460 A^2 buried surface area.

### Ligand-Binding Pocket and Polar Interactions

[BU72](/xray-mp-wiki/reagents/ligands/bu72) binds in the orthosteric pocket with its morphinan core interacting with hydrophobic residues I296^6.51, V300^6.55 in TM6 and W318^7.35, I322^7.39 in TM7. The phenolic hydroxyl engages in a water-mediated interaction with H297^6.52. The tertiary amine forms an ionic interaction with D147^3.32. An unexpected interaction between [BU72](/xray-mp-wiki/reagents/ligands/bu72) and the amino terminus (H54) was observed, with H54 positioned 2.6 A from the [BU72](/xray-mp-wiki/reagents/ligands/bu72) secondary amine, though this is unlikely physiologically relevant.

### Conserved Core Triad Rearrangement

A triad of conserved amino acids F6.44, P5.50, and I3.40 (the conserved core triad) undergoes rearrangement upon activation. In the active state, the morphinan scaffold of [BU72](/xray-mp-wiki/reagents/ligands/bu72) adopts a pose sterically incompatible with the inactive position of TM3, causing TM3 residues D147^3.32 and M151^3.36 to shift 1.5 A toward TM2. W293^6.48 serves as a link between the ligand-binding pocket and the triad, with its rotameric state stabilized by agonist binding.

### Polar Network in Signal Propagation

An extensive polar network connects the orthosteric binding pocket to the G-protein-coupling interface. In the active state, the sodium-binding site (coordinated by D2.50, N3.35, S3.39, and W6.48) collapses and rearranges to preclude sodium binding. The [NPxxY Motif](/xray-mp-wiki/concepts/npxxy-motif) in TM7 moves inward toward TM5, with N332^7.49 and Y336^7.53 participating in a hydrogen-bond network involving Y252^5.58 and backbone carbonyls of L158^3.43 and V285^6.40.

### Opioid Receptor Subtype Selectivity

Comparison of muOR with delta-OR sequences shows that of the 14 residues within 4 A of [beta-FNA](/xray-mp-wiki/reagents/ligands/beta-fna), only three differ: E229^ECL2 (Asp in delta-OR), K303^6.58 (Trp in delta-OR), and W318^7.35 (Leu in delta-OR). The W318L mutation markedly increases the affinity of the delta-selective antagonist naltrindole at muOR, as the larger W318 side chain in muOR would clash with naltrindole while leucine accommodates it. This structural insight explains the molecular basis for subtype-selective opioid pharmacology.

### Peptide Agonist Binding Determinants

The muOR-selective synthetic peptide agonist DAMGO (ID-Ala2,N-MePhe4,Gly-ol5] enkephalin) occupies a space overlapping with the [beta-FNA](/xray-mp-wiki/reagents/ligands/beta-fna) binding pocket but extends beyond it. Mutations that impair DAMGO binding include H297^6.52 (near the pocket bottom) and K303^6.58, W318^7.35, and H319^7.36 (positioned above the pocket). Endomorphins 1 and 2, endogenous muOR-selective peptides, exhibit 4,000- and 15,000-fold selectivity over delta-OR and kappa-OR, respectively.


## Cross-References

- [BU72](/xray-mp-wiki/reagents/ligands/bu72/) — Co-crystallized agonist ligand in active muOR structure
- [BU74](/xray-mp-wiki/reagents/ligands/bu74/) — Antagonist counterpart used in MD simulations to demonstrate instability in active state
- [beta-FNA](/xray-mp-wiki/reagents/ligands/beta-fna/) — Covalent antagonist co-crystallized with inactive muOR structure
- [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) — Nb39 nanobody used as G-protein mimetic for active-state stabilization
- [Human Beta2-Adrenergic Receptor](/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/) — Comparative analysis of activation mechanism
- [Human Delta-Opioid Receptor](/xray-mp-wiki/proteins/gpcr/delta-opioid-receptor/) — High-resolution inactive structure used for polar network comparison
- [Kappa Opioid Receptor](/xray-mp-wiki/proteins/gpcr/kappa-opioid-receptor/) — Related classical opioid GPCR
- [Conserved Core Triad](/xray-mp-wiki/concepts/conserved-core-triad/) — Key mechanistic concept from muOR activation studies
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) — Entity mentioned in text
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) — Entity mentioned in text
