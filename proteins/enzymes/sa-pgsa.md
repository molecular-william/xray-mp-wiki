---
title: Phosphatidylglycerol Phosphate Synthase PgsA from Staphylococcus aureus
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.crstbi.2021.11.005]
verified: false
---

# Phosphatidylglycerol Phosphate Synthase PgsA from Staphylococcus aureus

## Overview

[Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol) phosphate synthase (PgsA) from Staphylococcus aureus (SaPgsA) is a membrane-embedded enzyme that catalyzes the conversion of cytidine diphosphate-diacylglycerol (CDP-DAG) and [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) 3-phosphate (G3P) into [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol) phosphate (PGP) and cytidine monophosphate (CMP). PgsA forms a homodimer and is essential for [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol) biosynthesis in bacteria. Mutations in pgsA are frequently associated with [Daptomycin](/xray-mp-wiki/reagents/ligands/daptomycin) resistance in pathogenic Gram-positive bacteria, making SaPgsA a potential antibacterial target.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.crstbi.2021.11.005 | 7DRJ | 2.5 A | not specified | Full-length SaPgsA, homodimer, 6 transmembrane helices per protomer | phosphatidylglycerol phosphate (PGP) |
| doi/10.1016##j.crstbi.2021.11.005 | 7DRK | 3.0 A | not specified | Full-length SaPgsA, homodimer, 6 transmembrane helices per protomer | cytidine diphosphate-diacylglycerol (CDP-DAG) |

## Expression and Purification

- **Expression system**: E. coli C41(DE3) or C43(DE3)
- **Construct**: Full-length SaPgsA with N-terminal His-tag, codon-optimized for E. coli expression

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | E. coli expression in Terrific Broth, [IPTG](/xray-mp-wiki/reagents/additives/iptg) induction | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 200 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) + -- | Induction at 37 C for 2-3 h or 16 C for 12-15 h; cells harvested by centrifugation |
| Cell lysis | French press at 900-1000 bar, 4-5 passes | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 200 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) + -- | Membrane fraction pelleted at 160,000xg for 1 h |
| Solubilization | Detergent solubilization | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 200 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) + 1.5% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm) | Solubilization for 2-3 h at 4 C |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 300 mM NaCl, 10% glycerin, 0.1% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm) (wash); 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 0.05% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm) (elution) + beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm) | Protein eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl, 0.05% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm) + beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm) | SaPgsA eluted as dimer confirmed by [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals) |


## Crystallization

### doi/10.1016##j.crstbi.2021.11.005

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase |
| Protein sample | SaPgsA reconstituted in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) LCP |
| Temperature | not specified in main text |
| Growth time | not specified in main text |
| Cryoprotection | not specified in main text |
| Notes | SaPgsA-PGP complex (7DRJ) at 2.5 A resolution; SaPgsA-CDP-DAG complex (7DRK) at 3.0 A resolution. Initial phases solved by ab initio phasing with ARCIMBOLDO-LITE. |


## Biological / Functional Insights

### Homodimeric structure with 6 transmembrane helices

SaPgsA forms a homodimer with two protomers related by a central pseudo two-fold symmetry axis. Each monomer contains six transmembrane alpha-helices (TM1-TM6) forming a compact fold. The dimer interface is stable in both detergent micelles (confirmed by [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals)) and the crystal lattice.

### Trifurcated amphipathic cavity for catalysis

The active site is embedded in a large intracellular trifurcated amphipathic cavity. The hydrophilic head groups of substrate/product occupy distinct pockets while the fatty acyl chains extend into membrane-exposed grooves. An elongated membrane-exposed surface groove accommodates the fatty acyl chains and opens a lateral portal for lipid entry and release.

### Bimetal zinc-binding catalytic center

A conserved DxxD motif (D57xxD60G61xxA64R65...G74xxxD78xxxD82) coordinates two zinc ions at the active site center. Zn1 is coordinated by Asp57, Asp78, Asp82 and the beta-phosphoryl moiety of CDP-DAG, while Zn2 is coordinated by Asp57, Asp60, Asp78 and the alpha-phosphoryl moiety. This bimetal center increases the pKa of surrounding residues, creating an acidic microenvironment to facilitate bond formation. The zinc binding mode closely resembles the physiologically relevant magnesium binding.

### Substrate-dependent conformational changes

The PGP-bound and CDP-DAG-bound structures reveal substrate-dependent conformational changes. In the PGP-bound state, the TM4-5 loop shifts toward TM6 by 1-3 A, expanding the CMP release channel (Channel 1) while diminishing the G3P entrance channel (Channel 2). In the CDP-DAG-bound state, the reverse occurs: Channel 1 closes while Channel 2 opens. This reversible seesaw-like movement facilitates the substrate entry and product release cycle during catalysis.

### Daptomycin resistance mutations cluster around active site

Eight [Daptomycin](/xray-mp-wiki/reagents/ligands/daptomycin) resistance-related mutations from clinical S. aureus, Streptococcus oralis, and Staphylococcus capitis strains were mapped onto the SaPgsA structure. Seven of eight tested mutants (V59D, V59N, G61S, A64V, K75N, K135E, S177F, D187E) exhibited reduced enzymatic activity compared to wild type, except A64V and D187E. Mutations V59, G61, and A64 are located on TM2 near the conserved helix kink essential for catalysis, within the DxxD motif. The clustering of resistance mutations around the active site suggests a trade-off mechanism where reduced PgsA activity lowers membrane anionic lipid content, conferring [Daptomycin](/xray-mp-wiki/reagents/ligands/daptomycin) resistance at the cost of reduced enzymatic function.

### Key catalytic residues identified

The 3-phosphoryl moiety of PGP is sandwiched between TM3 and TM5, interacting with Lys83, Arg110, Arg118, Lys137, and Tyr181. Mutations K83A, R110A, R118A, and K137A exhibited reduced activity. Tyr181A mutation increased activity by facilitating G3P entry. Thr138 on TM5 hydrogen bonds to the 2-hydroxyl of PGP; T138A showed slightly higher activity. For CDP-DAG binding, Asn5, Phe58, Arg65, and Lys135 directly interact with the substrate. N5A and R65A showed much lower activity in LCP but near wild-type activity in detergent, indicating their role in attracting CDP-DAG head group in the membrane environment.


## Cross-References

- [Phosphatidylglycerol Phosphate](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol-phosphate/) — Product of SaPgsA enzymatic reaction
- [Cytidine Diphosphate Diacylglycerol](/xray-mp-wiki/reagents/lipids/cytidine-diphosphate-diacylglycerol/) — Substrate of SaPgsA enzymatic reaction
- [Glycerol 3-Phosphate](/xray-mp-wiki/reagents/additives/glycerol-3-phosphate/) — Second substrate of SaPgsA enzymatic reaction
- [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) — Downstream product of PG biosynthesis pathway catalyzed by PgsA
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for SaPgsA structures
- [n-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for SaPgsA solubilization and purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of LCP crystallization matrix
- [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals) — Entity mentioned in text
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) — Entity mentioned in text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm) — Entity mentioned in text
