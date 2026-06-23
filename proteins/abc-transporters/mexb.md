---
title: MexB Multidrug Efflux Pump
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##s41598-019-40232-2]
verified: false
---

# MexB Multidrug Efflux Pump

## Overview

[MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/) is a Resistance-Nodulation-Division (RND)-type multidrug efflux pump from
the Gram-negative pathogen Pseudomonas aeruginosa. It forms a tripartite efflux
complex with the periplasmic adaptor protein [MEXA](/xray-mp-wiki/proteins/abc-transporters/mexa/) and the outer membrane channel
OprM to export a broad spectrum of antibiotics and toxic compounds. [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/) is a
homotrimer with each protomer containing voluminous periplasmic drug-binding
pockets — a proximal binding pocket (PBP) and a distal binding pocket (DBP) — that
accommodate diverse substrates. The DBP contains a specific hydrophobic pit for
efflux pump inhibitors such as [ABI-PP (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine)](/xray-mp-wiki/reagents/ligands/abi-pp/). X-ray structures of [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/) bound to
high-molecular-mass compounds [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (MW 1,005) and C7NG (MW 1,028) revealed that
these compounds unexpectedly bind in the distal pocket despite their size, with
one alkyl chain inserted into the inhibitor-binding hydrophobic pit. [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) acts as
a competitive inhibitor of MexB-mediated drug efflux for drugs that bind weakly
to the DBP, and this inhibition depends on insertion of its alkyl chain into the
hydrophobic pit.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41598-019-40232-2 | 6IIA |  |  | Full-length [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/) from P. aeruginosa with His tag, purified in [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) | Lauryl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol ([LMNG](/xray-mp-wiki/reagents/detergents/lmng/)) |

## Expression and Purification

- **Expression system**: Escherichia coli (described previously)
- **Construct**: His-tagged full-length [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/) from P. aeruginosa
- **Notes**: Expressed in E. coli strain as previously described (Nakashima et al., Nature 2013)

### Purification Workflow

- **Expression system**: E. coli
- **Tag info**: His tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent solubilization | -- | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 50 mM NaCl + 1.5% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (or C7NG) | Solubilized with 1.5% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) instead of [DDM](/xray-mp-wiki/reagents/detergents/ddm/); [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/)(F178W)/LMNG and [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/)/C6NG samples were solubilized with [DDM](/xray-mp-wiki/reagents/detergents/ddm/) and detergent-exchanged in the final step |
| Affinity purification | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | -- | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 50 mM NaCl + 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (or corresponding detergent) | Purified as described previously (Nakashima et al., Nature 2013) |

**Final sample**: Concentrated in 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 50 mM NaCl, 0.05% detergent


## Crystallization

### doi/10.1038##s41598-019-40232-2

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/) in 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 50 mM NaCl, 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) |
| Reservoir | Similar conditions as previously described (Nakashima et al., Nature 2013) with slight adjustments of pH and precipitant concentration |
| Cryoprotection | [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) increased to 40% (v/v) in three steps, flash frozen in liquid N2 |
| Notes | Data collected at BL44XU beamline in SPring-8 at 100 K. [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using DDM-bound [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/) structure (PDBID 3W9I) as search model. REFMAC and COOT used for refinement and remodeling. |


## Biological / Functional Insights

### LMNG binds to the distal binding pocket of MexB despite high molecular mass

Contrary to expectations that high-molecular-mass compounds bind the proximal pocket, [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (MW 1,005) was found bound in the distal binding pocket (DBP) of [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/). One of its two alkyl chains inserts into the inhibitor-binding hydrophobic pit (the binding site of [ABI-PP (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine)](/xray-mp-wiki/reagents/ligands/abi-pp/)), while the other extends parallel above the pit. The two [Maltose](/xray-mp-wiki/reagents/additives/maltose/) moieties extend toward the exit and entrance of the DBP, occupying the entire pocket space. [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) forms hydrogen bonds with residues Gln46, Glu81, Thr89, Arg128, Lys134, Ser180, Gln273, and Arg620.

### LMNG competitively inhibits MexB-mediated drug efflux via pit insertion

[LMNG](/xray-mp-wiki/reagents/detergents/lmng/) is a substrate of the MexAB-OprM system and competitively inhibits the export of drugs that bind weakly or transiently to the DBP ([Erythromycin](/xray-mp-wiki/reagents/ligands/erythromycin/), clarithromycin, [Ciprofloxacin - Fluoroquinolone Antibiotic](/xray-mp-wiki/reagents/ligands/ciprofloxacin/), azithromycin, [Ethidium - Fluorescent Intercalating Dye](/xray-mp-wiki/reagents/ligands/ethidium/) bromide, berberine). This inhibition depends on insertion of the [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) alkyl chain into the hydrophobic pit: the F178W mutant, which occludes the pit with a bulky tryptophan side chain, retains [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) export activity but loses LMNG-mediated competitive inhibition. [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) does not inhibit drugs that clearly bind to the DBP ([Doxorubicin - Anthracycline Anticancer Drug](/xray-mp-wiki/reagents/ligands/doxorubicin/), [Minocycline](/xray-mp-wiki/reagents/ligands/minocycline/), rhodamine 6G).

### Molecular shape determines DBP vs PBP binding in RND pumps

Principal moments of inertia (PMI) analysis shows that DBP-binding drugs share rod-like molecular shapes. [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), despite its high molecular mass, can form a rod-like structure and traverse the narrow channel to reach the DBP without requiring the peristaltic motion needed for bulky PBP-binding substrates. The highly flexible structure with many rotatable bonds also contributes to [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)'s ability to reach the DBP.

### C7NG also binds in the distal pocket of MexB

C7NG (CYMAL-7 neopentyl glycol, MW 1,028), an [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) analogue with cyclohexane- terminated alkyl chains, also binds in the DBP with its binding site partially overlapping that of [LMNG](/xray-mp-wiki/reagents/detergents/lmng/). This demonstrates that high-molecular-mass neopentyl glycol derivatives can generally bind in the DBP, and that substrate binding to the distal vs proximal pocket is controlled not only by molecular weight but also by individual molecular characteristics.


## Cross-References

- [MexA multidrug efflux pump periplasmic adaptor](/xray-mp-wiki/proteins/abc-transporters/mexa/) — MexA forms the tripartite MexAB-OprM efflux complex with MexB
- [AcrB Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Homologous RND efflux pump from E. coli; MexB shares the same overall architecture and mechanism
- [LMNG (Lauryl Maltose Neopentyl Glycol)](/xray-mp-wiki/reagents/detergents/lmng/) — High-molecular-mass detergent that binds in the MexB distal pocket and competitively inhibits drug efflux
- [DDM (N-Dodecyl-beta-D-maltoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for initial MexB structures; replaced by LMNG in this study
- [ABI-PP (efflux pump inhibitor)](/xray-mp-wiki/reagents/additives/abi-pp/) — ABI-PP binds the same hydrophobic pit in the DBP; LMNG alkyl chain inserts into the ABI-PP binding site
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Used at 10 mM pH 7.5 for protein purification and final sample buffer
- [RND efflux pumps](/xray-mp-wiki/concepts/rnd-efflux-pumps/) — MexB is a member of the RND transporter superfamily
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/) — Related protein structure
