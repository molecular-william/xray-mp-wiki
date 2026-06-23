---
title: NorM-NG (Neisseria gonorrhoeae NorM) - MATE Family Na+-Coupled Transporter
created: 2026-06-05
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11403, doi/10.1038##ncomms8995, doi/10.1073##pnas.1219901110]
verified: false
---

# NorM-NG (Neisseria gonorrhoeae NorM) - MATE Family Na+-Coupled Transporter

## Overview

NorM-NG is a multidrug and toxic compound extrusion (MATE) family transporter from Neisseria gonorrhoeae that functions as a Na+-coupled multidrug efflux pump. It belongs to the NorM subfamily of MATE transporters and exports a broad range of organic cations including ethidium bromide, [Doxorubicin - Anthracycline Anticancer Drug](/xray-mp-wiki/reagents/ligands/doxorubicin), and rhodamine 6G. NorM-NG features the characteristic bilobate 12-transmembrane-helix architecture of the MATE family with pseudo-symmetric N- and C-lobes (TM1-6 and TM7-12), residues 5-230 and 231-459 respectively. In the [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil)-bound structure, NorM-NG undergoes pronounced conformational changes in two extracellular loops (L3-4 and L9-10) that cap the multidrug-binding cavity. Crystal structures of NorM-NG in complexes with three distinct translocation substrates (ethidium, rhodamine 6G, and tetraphenylphosphonium) and Cs+ (a Na+ congener) revealed an extracellular-facing, drug-bound state with a multidrug-binding cavity lined by four negatively charged amino acids and surprisingly limited hydrophobic moieties. An uncommon cation-pi interaction between Na+ and Y294 was identified in the Na+-binding site located outside the drug-binding cavity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11403 | 3P3M | 3.0 | P 212121 | NorM-NG wild type, residues 5-459 | Rhodamine 6G (R6G) |
| doi/10.1038##ncomms8995 | 5C6P | 3.0 | P 212121 | NorM-NG wild type, residues 5-459 | [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) |
| doi/10.1073##pnas.1219901110 | 4HUK | 3.5 | -- | NorM-NG (residues 5-459) with C-terminal hexahistidine tag; crystallized with monobody chaperone | Ethidium |
| doi/10.1073##pnas.1219901110 | 4HUL | 3.65 | -- | NorM-NG with C-terminal hexahistidine tag; monobody complex | Rhodamine 6G (R6G) |
| doi/10.1073##pnas.1219901110 | 4HUM | 3.55 | -- | NorM-NG with C-terminal hexahistidine tag; monobody complex | Tetraphenylphosphonium (TPP) |
| doi/10.1073##pnas.1219901110 | 4HUN | 3.9 | -- | NorM-NG with C-terminal hexahistidine tag; monobody complex | Cs+ (sodium congener) |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) transformed with membrane protein expression vectors
- **Construct**: [IPTG](/xray-mp-wiki/reagents/additives/iptg) induction at 37 C for 3 h

### Purification Workflow

*Source: doi/10.1038##ncomms8995*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and induction | E. coli BL21(DE3) in LB media to OD600 = 0.5; induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at 37 C for 3 h | -- | LB media + -- |  |
| Cell lysis | Multiple passages through pre-cooled microfluidizer | -- | -- + -- |  |
| Membrane extraction | Ultracentrifugation for membrane collection; extracted with 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | -- | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes)-NaOH pH 7.5, 100 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm) (Anatrace) |  |
| Ni-NTA affinity chromatography | Ni-NTA resin; eluted with 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) | Ni-NTA | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes)-NaOH pH 7.5, 100 mM NaCl, 25% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm) |  |
| Thrombin cleavage | Incubated with thrombin protease overnight | -- | -- + -- |  |
| Size-exclusion chromatography | Superdex 200 SEC | Superdex 200 | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes)-NaOH pH 7.5, 100 mM NaCl, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm) |  |

### Purification Workflow

*Source: doi/10.1073##pnas.1219901110*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and induction | E. coli BL21(DE3) transformed with pET-15b-NorM-NG | -- | LB media + -- |  |
| Cell lysis | -- | -- | -- + -- |  |
| Membrane extraction and purification | Ni-NTA affinity chromatography | Ni-NTA | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm) |  |
| Thrombin cleavage | Overnight incubation with thrombin protease | -- | -- + -- |  |
| Size-exclusion chromatography | Superdex 200 | Superdex 200 | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes)-NaOH pH 7.5, 100 mM NaCl, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm) |  |


## Crystallization

### doi/10.1038##ncomms8995

| Parameter | Value |
|---|---|
| Method | Co-crystallization with [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil); hanging-drop vapor diffusion at 22 C |
| Protein sample | NorM-NG incubated with [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) |
| Reservoir | -- |
| Temperature | 22 C |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Phasing by molecular replacement and [MIRAS](/xray-mp-wiki/methods/structure-determination/miras); [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil)-bound structure differs from R6G-bound by rmsd >2 A over 459 aligned Ca positions; notable conformational changes in L3-4 and L9-10 loops |

### doi/10.1073##pnas.1219901110

| Parameter | Value |
|---|---|
| Method | Crystallization with monobody chaperone; drug/substrate co-crystallization |
| Protein sample | NorM-NG-monobody complex incubated with substrate |
| Reservoir | -- |
| Mixing ratio | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Structures captured in extracellular-facing, drug-bound states. NorM-NG crystallized in absence of Na+ (1 mM Na+ precluded crystallization). Four substrate-bound structures: ethidium, R6G, TPP (substrate analog), and Cs+ (Na+ congener). Monobody used as crystallization chaperone (engineered binding protein). |


## Biological / Functional Insights

### Na+-coupled transport mechanism via transmembrane helix shifting

NorM-NG uses a Na+-coupled mechanism distinct from the H+-coupled [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh). Cation binding triggers substrate unbinding by shifting several transmembrane helices, contrasting with the direct-competition mechanism of [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh) where protonation of D40 triggers release without substantial conformational changes. The D41 residue (equivalent to [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh) D40) is essential for transport but is substituted by asparagine in eukaryotic MATE members.

### Verapamil-binding site and folded ligand conformation

[Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) in NorM-NG adopts a folded conformation with both aromatic rings stacked on top of each other — a double-layered conformation unlike the extended form seen in [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh). Direct contacts involve S61 (TM2), Q284 (TM8) via H-bonding and A57 (TM2), F265, V269 (TM7), P357 (L9-10) via van der Waals. D41 (TM1) and D356 (L9-10) carboxylate groups are ~6 and 3.5 A from [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) N8, implying moderate electrostatic attraction.

### Extracellular loop dynamics upon verapamil binding

Upon [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) binding, NorM-NG undergoes pronounced conformational changes in L3-4 and L9-10 extracellular loops. L3-4 shifts the most, losing ability to insert side chains into the central cavity. L9-10 also shifts away from the multidrug-binding cavity, interacting with [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) only modestly. These changes contrast with [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh) which remains largely unaltered upon ligand exchange.

### Mutational analysis of the verapamil-binding site

Mutations of D41, S61, F265L, V269, Q284, D356 and P357 abolished cellular resistance to [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil), confirming these residues as essential for [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil) transport. Unlike [DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter](/xray-mp-wiki/proteins/dinf-bh), none of the tested NorM-NG mutations enabled drug resistance in the presence of [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil), underscoring mechanistic differences between the NorM and DinF subfamilies.

### Multidrug-binding cavity with four acidic residues

Crystal structures of NorM-NG bound to ethidium, rhodamine 6G, and TPP revealed a multidrug-binding cavity lined by four negatively charged amino acids (D41, D130, D355, D356) and surprisingly limited hydrophobic moieties. This contrasts with the general belief that aromatic amino acids play a prominent role in multidrug recognition. The cavity is capped by extracellular loops L3-4 and L9-10. F265 makes an edge-to-face aromatic stacking interaction with substrates. Mutagenesis confirmed D41, F265, Q284, D355, and D356 as critical for transport function.

### Uncommon Na+-pi interaction in the cation-binding site

A Na+-binding site was identified outside the drug-binding cavity, involving E261 and Y294. Y294 makes an uncommon cation-pi interaction with Na+, the first observation of a Na+-pi interaction in any membrane protein. The cation-binding site is distinct from the substrate-binding residues, supporting an indirect coupling mechanism. D377, while essential for transport, is positioned >7.2 A from the bound Cs+ in the NorM-NG structure, suggesting TM rearrangement is required for D377 to participate in Na+ coordination during transport.

### Unconventional antiport mechanism - indirect coupling

NorM-NG employs an unconventional antiport mechanism where Na+ and substrate bind to distinct amino acids and can bind simultaneously. Na+ binding induces conformational changes in TM7 and TM8 (tilting ~20 degrees relative to membrane normal) that disrupt the drug-binding site, rather than directly competing for shared binding residues. This indirect coupling mechanism is distinct from the canonical antiport mechanism observed in transporters like NhaA and EmrE where counterion and substrate compete for a shared binding site. Na+-induced TM rearrangement pulls F265 (TM7), Q284, and S288 (TM8) away from the central cavity to disrupt drug binding.


## Cross-References

- [DinF-BH (Bacillus halodurans DinF)](/xray-mp-wiki/proteins/abc-transporters/dinf-bh/) — Co-reported in same paper; mechanistic comparison between NorM and DinF subfamilies
- [NorM-VC (Vibrio cholerae NorM)](/xray-mp-wiki/proteins/norm-vc/) — Earlier NorM subfamily structure; Na+-coupled MATE transporter; comparison of cation-bound states
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for NorM-NG solubilization and purification
- [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) — Broad-spectrum MATE inhibitor that co-crystallized with NorM-NG
- [MATE Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/mate-transporter-family/) — NorM-NG is a NorM subfamily member of the MATE family
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — MATE transporters operate via alternating access mechanism
- [IPTG](/xray-mp-wiki/reagents/additives/iptg) — Entity mentioned in text
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) — Entity mentioned in text
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes) — Entity mentioned in text
- [Doxorubicin - Anthracycline Anticancer Drug](/xray-mp-wiki/reagents/ligands/doxorubicin) — Entity mentioned in text
- [Monobody](/xray-mp-wiki/reagents/protein-tags/monobody/) — Engineered crystallization chaperone used for NorM-NG structure determination
- [Cation-pi Interaction](/xray-mp-wiki/concepts/cation-pi-interaction/) — Na+-pi interaction with Y294 is a key mechanistic feature
