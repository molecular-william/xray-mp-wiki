---
title: MexB Multidrug Exporter from Pseudomonas aeruginosa
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography, rnd-transporter, multidrug-resistance]
sources: [doi/10.1016##J.JMB.2009.04.001]
---

# MexB Multidrug Exporter from Pseudomonas aeruginosa

## Overview

MexB is the inner-membrane component of the MexAB-OprM tripartite efflux pump in
Pseudomonas aeruginosa, a major multidrug resistance system. It belongs to the resistance-
nodulation-cell division (RND) superfamily of secondary active transporters. The structure
was determined at 3.0 A resolution in space group P1, revealing an asymmetric homotrimer
where each subunit adopts a different conformation representing three snapshots of the
transport cycle. Each subunit contains 1046 amino acids with 12 transmembrane helices and
an extensive periplasmic domain. The structure shows a large multidrug-binding cavity in
the pore domain and a DDM molecule bound in subunit B, supporting the model that RND
transporters can transport detergent molecules as substrates. MexB is 69.8% identical and
83.2% similar to its E. coli counterpart AcrB.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##J.JMB.2009.04.001 | not specified (deposited; search model was 2J8S from AcrB) | 3.0 A | P1 | MexB from P. aeruginosa PAO1 (1046 amino acids); C-terminal hexahistidine tag | DDM (n-dodecyl-D-maltoside) bound in binding cavity of subunit B |

## Expression and Purification

- **Expression system**: Escherichia coli strain C43 (DE3)
- **Construct**: MexB from P. aeruginosa PAO1 genomic DNA cloned into pET28 vector with C-terminal hexahistidine tag

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press in buffer with DNase I and PMSF | -- | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 1 mM PMSF, complete protease inhibitor cocktail | Membranes collected by centrifugation at 100,000g for 1 h |
| Solubilization | DDM solubilization | -- | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 10 mM imidazole, 1 mM PMSF, 10% glycerol, 1% DDM | Solubilized for 2 h at 4 deg.C with 1% DDM |
| Ni-NTA affinity chromatography | Ni-NTA column (Qiagen) | Ni-NTA | Equilibration with 0.03% DDM; wash with 30 mM imidazole; elution with 200 mM imidazole | C-terminal hexahistidine tag purification |
| Size-exclusion chromatography | Superdex 200 SEC column (Amersham Biosciences) | Superdex 200 | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 10% glycerol, 0.03% DDM | Further purification and buffer exchange for crystallization |


## Crystallization

### doi/10.1016##J.JMB.2009.04.001

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (specific setup not detailed) |
| Protein sample | Concentrated and SEC-purified MexB in 0.03% DDM |
| Reservoir | not specified |
| Mixing ratio | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Crystals in space group P1 with two trimers in asymmetric unit. Molecular replacement from 2J8S (asymmetric AcrB). |


## Biological / Functional Insights

### Asymmetric trimer mechanism

MexB adopts an asymmetric homotrimeric conformation where each subunit represents a
different state in the transport cycle. Subunit B (binding) has a channel open to the
periplasm for substrate capture. Subunit C (extrusion) has a channel open toward the
outer-membrane factor docking site. Subunit A shows an altered conformation, likely
representing a transitional state, potentially influenced by crystal packing. The
progression through conformations is ABC rather than BAC.

### Multidrug-binding cavity

A large drug-binding cavity is formed by the four pore domain subdomains (PN1, PN2,
PC1, PC2). A DDM molecule was observed bound in subunit B, with the maltoside group
interacting with Val47, Ser48, Gln125, Val177, Gly179, Ser180, Gln273, and Arg620.
The binding site corresponds to minocycline and doxorubicin sites in AcrB, demonstrating
the ability of RND transporters to transport detergent molecules as substrates. The
cavity is rich in polar residues at the distal end and aromatic residues at the proximal
end, providing multiple overlapping binding sites for diverse substrates.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization and crystallization; also observed bound in the multidrug-binding cavity
- [n-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/beta-ddm/) — Same detergent as DDM; alternative naming convention
