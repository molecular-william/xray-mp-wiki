---
title: Human Angiotensin-Converting Enzyme 2 (hACE2)
created: 2026-05-27
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [enzyme, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.03.045, doi/10.1038##s41586-020-2180-5, doi/10.1038##s41586-020-2179-y]
verified: false
---

# Human Angiotensin-Converting Enzyme 2 (hACE2)

## Overview

Human angiotensin-converting enzyme 2 (hACE2) is a membrane-bound zinc metalloprotease that plays a key role in the renin-angiotensin system by converting [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) to angiotensin-(1-7). It also serves as the cellular entry receptor for SARS-CoV and SARS-CoV-2 coronaviruses. The structure of hACE2 reveals an N-terminal peptidase domain that mediates viral spike protein binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2020.03.045 | 6LZG | 2.50 A | P41212 | hACE2 residues 19-615, N-terminal peptidase domain in complex with SARS-CoV-2 CTD | SARS-CoV-2 CTD (spike protein residues 319-541) |
| doi/10.1038##s41586-020-2180-5 | 6M0J | 2.45 A | P4₁2₁2 | hACE2 residues Ser19-Asp615, N-terminal peptidase domain in complex with SARS-CoV-2 RBD (residues Arg319-Phe541) | SARS-CoV-2 RBD (spike protein residues 319-541), zinc ion |
| doi/10.1038##s41586-020-2179-y | 6VW1 | 2.68 A | P 21 21 21 | hACE2 residues 1-615 in complex with SARS-CoV-2 chimeric RBD | SARS-CoV-2 chimeric RBD (SARS-CoV-2 core + SARS-CoV side loop), zinc ion |

## Expression and Purification

- **Expression system**: Hi5 insect cells (baculovirus)
- **Construct**: hACE2 residues Ser19-Asp615, N-terminal gp67 signal peptide, C-terminal 6xHis tag

### Purification Workflow

*Source: doi/10.1016##j.cell.2020.03.045*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | HisTrap HP 5 mL column | Buffer not specified + -- | Soluble proteins from Hi5 cell supernatant purified by metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) |
| Size-exclusion chromatography | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) column | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl | Final purification step; samples pooled and concentrated |

### Purification Workflow

*Source: doi/10.1038##s41586-020-2180-5*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Secretion and concentration | Baculovirus expression in Hi5 cells | -- | HBS (10 mM HEPES pH 7.2, 150 mM NaCl) | Supernatant collected 60 h post-infection, concentrated and buffer-exchanged to HBS |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA affinity | Ni-NTA resin (GE Healthcare) | HBS (10 mM HEPES pH 7.2, 150 mM NaCl) + -- | Eluted with 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in HBS buffer |
| Size-exclusion chromatography | Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) column (GE Healthcare) | HBS (10 mM HEPES pH 7.2, 150 mM NaCl) + -- | Pre-equilibrated with HBS buffer; complex formed by incubating ACE2 with SARS-CoV-2 RBD for 1 h on ice before SEC |

### Purification Workflow

*Source: doi/10.1038##s41586-020-2179-y*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Baculovirus expression | Expression in Sf9 insect cells via Bac-to-Bac system (Life Technologies) | -- | 20 mM Tris pH 7.2, 200 mM NaCl | pFastBac vector with honeybee melittin signal peptide and C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/); ACE2 and RBD separately expressed and secreted into medium |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA affinity | Ni-NTA column | 20 mM Tris pH 7.2, 200 mM NaCl + -- | His6-tagged ACE2 and RBD purified from cell culture medium supernatant |
| Size-exclusion chromatography | Gel filtration | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) column (GE Healthcare) | 20 mM Tris pH 7.2, 200 mM NaCl + -- | ACE2 and RBD incubated together; complex purified by Superdex200 gel-filtration; concentrated to 13 mg/ml |


## Crystallization

### doi/10.1016##j.cell.2020.03.045

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | SARS-CoV-2 CTD/hACE2 complex, protein concentration 15 mg/ml |
| Reservoir | 0.1 M MES pH 6.5, 10% w/v [PEG](/xray-mp-wiki/reagents/additives/peg/) 5000 MME, 12% v/v 1-propanol |
| Temperature | 18 C |
| Growth time | not specified |
| Cryoprotection | Reservoir solution supplemented with 20% v/v [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) before flash-cooling in liquid nitrogen |
| Notes | Diffraction data collected at SSRF BL17U (wavelength 0.97919 A) |

### doi/10.1038##s41586-020-2180-5

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | SARS-CoV-2 RBD-ACE2 complex at 13 mg/ml in 20 mM Tris pH 7.5, 150 mM NaCl |
| Reservoir | 100 mM MES pH 6.5, 10% [PEG](/xray-mp-wiki/reagents/additives/peg/) 5000 MME, 12% 1-propanol |
| Temperature | Room temperature |
| Growth time | not specified |
| Cryoprotection | Reservoir solution supplemented with 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) before flash-cooling in liquid nitrogen |
| Notes | Crystals grown in sitting drops; 200 nl complex + 200 nl well solution; diffraction data at 100 K, wavelength 1.07180 A on BL17U1 at SSRF |

### doi/10.1038##s41586-020-2179-y

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | SARS-CoV-2 chimeric RBD-ACE2 complex at 13 mg/ml in 20 mM Tris pH 7.2, 200 mM NaCl |
| Reservoir | 100 mM Tris pH 8.5, 18-20% [PEG](/xray-mp-wiki/reagents/additives/peg/) 6000, 100 mM NaCl |
| Temperature | Room temperature |
| Growth time | not specified |
| Cryoprotection | 100 mM Tris pH 8.5, 30% [PEG](/xray-mp-wiki/reagents/additives/peg/) 6000, 100 mM NaCl, 30% [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/); flash-frozen in liquid nitrogen |
| Notes | X-ray diffraction data collected at Advanced Photon Source beamline 24-ID-E; structure determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using SARS-CoV RBD-ACE2 (PDB 2AJF) |


## Biological / Functional Insights

### Structural basis for SARS-CoV-2 receptor recognition

The crystal structure of the SARS-CoV-2 CTD in complex with hACE2 at 2.5 A resolution reveals the molecular basis for viral entry. hACE2 binds to the C-terminal domain of the SARS-CoV-2 spike protein via its N-terminal peptidase domain. The binding interface involves extensive hydrophobic contacts and hydrogen bonds between hACE2 residues (including F28, Y41, H34, D38, Y41) and SARS-CoV-2 CTD residues (including Y453, L455, F456, Y489, Q498). The SARS-CoV-2 CTD displays stronger affinity for hACE2 compared to SARS-RBD due to key residue substitutions that slightly strengthen the interaction.

### Comparison of SARS-CoV and SARS-CoV-2 receptor binding

Despite both SARS-CoV and SARS-CoV-2 utilizing hACE2 as their entry receptor, the atomic details at the binding interface demonstrate notable differences. SARS-CoV-2 CTD residue substitutions lead to higher affinity for receptor binding compared to SARS-RBD. The overall binding mode is similar, but key contacts differ at the residue level, explaining the higher infectivity of SARS-CoV-2. The SARS-CoV-2 CTD is antigenically distinct from SARS-RBD, as shown by the inability of SARS-CoV-directed monoclonal and polyclonal antibodies to bind SARS-CoV-2 spike protein.

### Convergent evolution of SARS-CoV-2 and SARS-CoV RBDs for ACE2 binding

The 2.45 A crystal structure of the SARS-CoV-2 RBD-ACE2 complex (PDB 6M0J) reveals that the overall ACE2-binding mode is nearly identical to SARS-CoV RBD. Residues in the SARS-CoV-2 RBD essential for ACE2 binding are either highly conserved or share similar side chain properties with SARS-CoV RBD. A unique ACE2-interacting residue, Lys417, in SARS-CoV-2 forms salt-bridge interactions with Asp30 of ACE2 — this position is Val404 in SARS-CoV and fails to participate in ACE2 binding. Despite high structural similarity, the binding affinity of ACE2 for SARS-CoV-2 RBD (KD 4.7 nM) is ~6.6-fold tighter than for SARS-CoV RBD (KD 31 nM). The study also mapped the epitopes of SARS-CoV antibodies (m396, S230, 80R, CR3014) on the SARS-CoV-2 RBD, providing structural explanation for their lack of cross-reactivity.

### ACE2-binding ridge compaction and hotspot stabilization in SARS-CoV-2

The 2.68 A structure of the SARS-CoV-2 chimeric RBD-ACE2 complex (PDB 6VW1) reveals that the ACE2-binding ridge in SARS-CoV-2 RBD has a more compact conformation than SARS-CoV RBD. Residue changes in the SARS-CoV-2 RBM stabilize two key hotspots at the RBD-ACE2 interface: hotspot 31 (centered on ACE2 Lys31-Glu35) and hotspot 353 (centered on ACE2 Lys353). SPR measurements show the chimeric RBD has higher ACE2-binding affinity than wild-type SARS-CoV-2 RBD (KD 23.2 nM vs 44.2 nM), both significantly higher than SARS-CoV RBD (KD 185 nM). RaTG13 (bat coronavirus) also uses human ACE2 as its receptor, suggesting possible direct bat-to-human transmission without an intermediate host.


## Cross-References

- [SARS-CoV-2 Spike Protein C-Terminal Domain](/xray-mp-wiki/proteins/slc-transporters/sars-cov-2-ctd/) — Co-crystallized with hACE2 in PDB 6LZG, 6M0J and 6VW1
- [2-(N-Morpholino)ethanesulfonic Acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Crystallization buffer at pH 6.5
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — PEG 5000 MME used as crystallization precipitant
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Cryoprotectant (20% v/v) for flash-cooling crystals
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — 150 mM in SEC purification buffer
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — 20 mM Tris-HCl pH 8.0 in SEC buffer; 20 mM Tris pH 7.5 in complex buffer
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — 500 mM imidazole used for elution from Ni-NTA resin
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — 10 mM HEPES pH 7.2 used in HBS purification buffer
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
