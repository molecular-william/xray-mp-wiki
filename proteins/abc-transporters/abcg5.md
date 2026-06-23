---
title: ABCG5
created: 2026-05-27
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2022.167795, doi/10.1038##nature17666]
verified: false
---

# ABCG5

## Overview

ABCG5 is a member of the ATP-binding cassette (ABC) G subfamily of transporter proteins. It functions as an obligate heterodimer with ABCG8 to form the ABCG5/G8 complex, which mediates selective sterol excretion by preferentially effluxing dietary plant sterols over [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol). The ABCG5/G8 heterodimer is localized on canalicular membranes of the bile ducts in the liver and the brush border of enterocytes in the small intestines, where it plays a critical role in reverse cholesterol transport and prevents abnormal accumulation of plant sterols in the human body.
The first X-ray crystal structure of human ABCG5/G8 was determined at 3.9 Å resolution (PDB 5DO7) using bicelle crystallization and tungstate-based SAD phasing. The structure revealed a new transmembrane fold characteristic of the ABC2 exporter superfamily, with the NBD N-terminal to the TMD and six transmembrane helices per subunit. The nucleotide-free state adopts an inward-facing conformation. The structure provides a mechanistic framework for understanding sterol transport and the disruptive effects of mutations causing sitosterolaemia.
A highly conserved phenylalanine array on transmembrane helix 2, termed the phenylalanine highway, supports sterol transport function. The orthogonal cholesterol-binding site near residue A540 is central to sterol recognition and transport. 

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature17666 | 5DO7 | 3.9 | I 2 2 2 | Human ABCG5/G8 heterodimer, nucleotide-free inward-facing state (bicelle crystallization) | Cholesterol (putative, in sterol vestibules) |
| doi/10.1016##j.jmb.2022.167795 | 8CUB | 4.051 | I 2 2 2 | Human ABCG5/G8 heterodimer in complex with [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) | [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) |
| doi/10.1016##j.jmb.2022.167795 | 7JR7 | not specified | not specified | Human ABCG5/G8 heterodimer (cryo-EM structure used as [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) model) | not specified |

## Expression and Purification

- **Expression system**: Pichia pastoris (yeast)
- **Construct**: Human ABCG5 (UniProt P45844) with C-terminal His₁₂ tag; ABCG8 (UniProt Q9UNQ0) with C-terminal calmodulin-binding peptide (CBP) tag. CBP tag and N-linked glycans cleaved by Endo H and HRV-3C protease. Protein treated by reductive methylation and cysteine alkylation before crystallization.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Membrane preparation | -- | 20 mM HEPES pH 7.5, 150 mM NaCl, protease inhibitors ([Leupeptin](/xray-mp-wiki/reagents/additives/leupeptin), pepstatin A, PMSF) + -- | Insoluble membranes removed by ultracentrifugation |
| Solubilization | Detergent solubilization | -- | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM NaCl, 0.1 mM TCEP + Not specified | Solubilized supernatant treated with 0.1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Ni-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) (Ni-NTA) | 20-mL [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) column | Not specified + Not specified | Peak fractions from [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) eluates collected |
| Calmodulin-binding peptide (CBP) chromatography | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) (CBP) | 5-mL CBP column | 50 mM HEPES pH 7.5, 100 mM NaCl, 0.1% beta-DDM, 0.05% [Cholate](/xray-mp-wiki/reagents/detergents/cholate), 0.01% CHS, 0.1 mM TCEP, 1 mM CaCl2, 1 mM MgCl2 + beta-DDM, [Cholate](/xray-mp-wiki/reagents/detergents/cholate), CHS | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) eluates mixed with CBP wash buffer and loaded onto CBP column |
| Detergent exchange | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | CBP column | [DMNG](/xray-mp-wiki/reagents/detergents/dmng)-containing buffer + [DMNG](/xray-mp-wiki/reagents/detergents/dmng) | CBP column washed sequentially to exchange detergents to decyl [Maltose](/xray-mp-wiki/reagents/additives/maltose) neopentyl glycol (DMNG) |
| Elution from CBP column | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | CBP column | 50 mM HEPES pH 7.5, 300 mM NaCl, 2 mM EGTA, 0.1% DMNG, 0.05% [Cholate](/xray-mp-wiki/reagents/detergents/cholate), 0.01% CHS, 1 mM TCEP + DMNG, [Cholate](/xray-mp-wiki/reagents/detergents/cholate), CHS | ABCG5/G8 proteins eluted from CBP column |
| Tag cleavage | Protease digestion (Endo H and HRV-3C protease) | -- | Not specified + Not specified | N-linked glycans and CBP tag cleaved overnight at 4 C; Endo H (~0.2 mg per 10-15 mg protein) and HRV-3C protease (~2 mg per 10-15 mg protein) |
| Gel filtration chromatography | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200) 30/100 GL column | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DMNG, 0.05% [Cholate](/xray-mp-wiki/reagents/detergents/cholate), 0.01% CHS + DMNG, [Cholate](/xray-mp-wiki/reagents/detergents/cholate), CHS | CBP tag-free proteins purified by [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography); peak fractions pooled |
| Reductive methylation and cysteine alkylation | Chemical modification | 2-mL [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) column | Not specified + Not specified | Methylated proteins relipidated with DOPC:DOPE (3:1, w/w), purified by Ni-NTA, treated with [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide) |
| [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) incubation | Ligand incubation | -- | Not specified + Not specified | Proteins incubated with [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) (prepared in isopropanol) overnight at 4 C |


## Crystallization

### doi/10.1038##nature17666

| Parameter | Value |
|---|---|
| Method | Bicelle crystallization (vapor diffusion, hanging drop) |
| Protein sample | G5G8 heterodimers coexpressed in P. pastoris, purified by tandem affinity chromatography (Ni-NTA + CBP), treated by reductive methylation and cysteine alkylation, reconstituted into DMPC bicelles (10% bicelle stock, lipids containing 5 mol% cholesterol and 95 mol% DMPC), ATP added at 10 mM before mixing, final protein concentration 5-10 mg ml⁻¹, protein/bicelle mixed 1:4 (v/v) |
| Reservoir | 1.7-2.0 M ammonium sulfate, 100 mM MES pH 6.5 (or HEPES pH 7.0), 2-5% PEG400 (or PEG350 MME), 1 mM TCEP |
| Temperature | 20-22 °C |
| Growth time | 3 days to 2 weeks; maximum size 75-150 × 40-60 × 10-20 μm in 1-2 months |
| Cryoprotection | 25% glycerol, 2 M (NH₄)₂SO₄, 100 mM MES pH 6.5, 2-4% PEG400 |
| Notes | Crystals only diffracted to 3.9 Å when cholesterol was present in bicelles. Two heterodimers in asymmetric unit. Tungsten SAD phasing using sodium phosphotungstate derivative. Native data merged from 19 crystals to 3.9 Å resolution. Space group I 2 2 2. Structure refined to R/Rfree = 0.242/0.328. |

### doi/10.1016##j.jmb.2022.167795

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) with bicelles |
| Protein sample | [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol)-treated ABCG5/G8 reconstituted into 10% DMPC/CHAPSO bicelles (lipids:detergents 3:1 w/w, lipids containing 5 mol% cholesterol and 95 mol% DMPC), mixed 1:4 (v/v) with protein/bicelle stock, final protein concentration ~10 mg/ml |
| Reservoir | 1.8-2.0 M [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate), 100 mM MES pH 6.5, 2-5% PEG400, 1 mM TCEP |
| Temperature | 20 C |
| Growth time | 1-2 weeks |
| Cryoprotection | 0.2 M sodium malonate |
| Notes | Crystals harvested by submersion in 0.2 M sodium malonate. Space group I 2 2 2. Solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) using PDB 7JR7. |


## Biological / Functional Insights

### First X-ray structure of an ABC sterol transporter

The G5G8 structure at 3.9 Å resolution (PDB 5DO7) is the first atomic model of an ABC sterol transporter. It reveals a new transmembrane fold characteristic of the ABC2 exporter superfamily (ABCG and ABCA subfamilies). Unlike type I and type II ABC importers or type I ABC exporters, no transmembrane helix crosses over into the opposite subunit. The NBD is N-terminal to the TMD, with six transmembrane helices per subunit. The extracellular domain (ECD) between TMH5 and TMH6 forms distinct α-helical structures.

### Nucleotide-free inward-facing conformation with closed NBDs

The G5G8 structure adopts an inward-facing conformation analogous to other nucleotide-free ABC exporters. Despite the lack of nucleotide and spatial separation between Walker A and Signature motifs, the two NBDs contact each other at the extreme cytoplasmic end to form a closed conformation through a pair of conserved NPXDF motifs (G5: NPFDF; G8: NPADF), which are conserved in the ABCG family.

### Asymmetric TMD/NBD interfaces and catalytic asymmetry

G5 and G8 exhibit distinct architectures at their TMD/NBD interfaces, reflecting the asymmetry in catalytic sites. G5 forms a stabilized three-helix bundle (CnH, CpH, and E-helix) adjacent to the inactive G5 Signature motif (NBS1), while G8 has a rotated CpH with greater flexibility near the catalytically active NBS2. The connecting helix (CnH), coupling helix (CpH), and E-helix elements mediate allosteric communication between nucleotide binding and sterol transport.

### TMD polar relay couples ATP hydrolysis to sterol transport

A network of conserved polar residues in both G5 and G8 forms hydrogen bonds and salt bridges extending from the CnH and CpH to the TMD interface. This polar relay may serve as a flexible hinge for subunit motions. Molecular dynamics simulations show inward movement of CnH/CpH elements (bringing Walker A and Signature motifs closer) coupled to upward movement of TMD elements. The sitosterolaemia-causing mutation R543S would disrupt interaction with E503 and destabilize the polar relay.

### Sterol-binding vestibules at the TMD dimer interface

Electron density features consistent with cholesterol were identified at symmetrical vestibules on opposing faces of the TMD dimer, opening to the bilayer and extending into the dimer interface. Each vestibule is flanked by TMH1-2 of one TMD and TMH4-6 of the other TMD, with a ceiling formed by an ECD α-helix. In vivo functional assays confirmed that mutation A540F, which occludes the putative cholesterol-binding site, abolishes biliary cholesterol transport.

### ABC2 exporter superfamily fold

The G5G8 TMD fold differs from previously known ABC transporter structures and defines the ABC2 exporter superfamily. This superfamily includes ABCA and ABCG eukaryotic subfamilies and diverse prokaryotic transporters (teichoic acid exporters, lipo-oligosaccharide exporters, mutacin and bacitracin transporters). The structure enables homology modelling of related transporters such as the Drosophila white/brown eye pigment transporter.

### Orthogonal cholesterol-binding site near A540

ABCG5 contains a conserved orthogonal [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol)-binding site at the transporter-membrane interface, with residue ABCG5_A540 making direct contact with the bound cholesterol molecule. The cholesterol extends across the interfacial space, with its hydroxyl group forming a hydrogen bond with ABCG8_T430, while the hydrocarbon tail remains in contact with hydrophobic residues on ABCG5 including L516, L537, I562, F565, and F567. The sterol fits into an indented planar cleft within the upper region of the vestibule formed by the re-entry and transmembrane helices.

### Phenylalanine highway on TMH2

A highly conserved phenylalanine array on transmembrane helix 2 (TMH2) of ABCG transporters forms a structural motif termed the phenylalanine highway (PH). In ABCG5, the aromatic tyrosine residues at positions Y432 (equivalent to F1) and Y424 (equivalent to F4) replace the phenylalanines found in other ABCG members. The PH creates a highway-shaped open space at the TMD dimer interface, with aromatic side chains pointing inward. This motif may serve as a conserved molecular clamp mediating pi-pi interactions with sterol molecules during transport.

### A540F loss-of-function mutation

The A540F mutation in ABCG5 causes a loss-of-function phenotype that suppresses [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) efflux in vivo and inhibits sterol-coupled ATPase activity by ~90% in vitro. The large aromatic phenylalanine side chain at position 540 introduces steric hindrance, disabling cholesterol docking onto the orthogonal binding site. The mutation causes a 180-degree flipping of cholesterol orientation at the sterol-binding site and prevents interactions between cholesterol and polar residues such as ABCG8_T430. The Kd value is similar for WT and mutant, but Bmax is reduced approximately twofold.

### Asymmetric sterol binding on ABCG5/G8

Sterol docking poses on ABCG5/G8 are distributed asymmetrically at the opposing membrane-transporter interfaces, with more conformations on the ABCG5-dominant side. Cholesterol and [Stigmasterol](/xray-mp-wiki/reagents/lipids/stigmasterol) show distinct binding preferences on either side of the transporter, with plant sterols showing higher binding preferences. The ABCG5-dominant side shows a continuous cholesterol binding pattern from P415 (ABCG8) to A540 (ABCG5), while the ABCG8-dominant side shows less specific sterol orientations.


## Cross-References

- [ABCG8](/xray-mp-wiki/proteins/abc-transporters/abcg8/) — Obligate heterodimer partner; ABCG5/G8 heterodimer crystallized together in PDB 5DO7 (first ABC sterol transporter structure) and PDB 8CUB
- [ABCG1](/xray-mp-wiki/proteins/abc-transporters/abcg1/) — Homodimeric ABCG sterol transporter; extensively compared for sterol binding patterns and PH motif
- [ABCG2](/xray-mp-wiki/proteins/abc-transporters/abcg2/) — Multidrug transporter ABCG member; shares hydrophobic valve and PH motif for comparison
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Central ligand; binds to orthogonal site near A540; used in crystallization and incubation
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/additives/cholesterol-hydrogen-succinate/) — [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) derivative used in purification and crystallization buffers (0.01% w/v)
- [Decyl Maltose Neopentyl Glycol (DMNG)](/xray-mp-wiki/reagents/detergents/dmng/) — Primary detergent used in final purification and crystallization sample buffer
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — Crystallization buffer (100 mM, pH 6.5)
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Crystallization precipitant (1.8-2.0 M)
- [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) — G5G8 was crystallized using bicelle crystallization with DMPC/cholesterol bicelles
- [ABC Transporter Family](/xray-mp-wiki/concepts/abc-transporter-family/) — G5G8 is an ABCG subfamily member; structure reveals the ABC2 exporter superfamily fold
