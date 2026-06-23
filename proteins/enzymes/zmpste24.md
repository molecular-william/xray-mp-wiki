---
title: "Human ZMPSTE24 (Zinc Metalloprotease)"
created: 2026-06-10
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1231513, doi/10.1107##s2059798318003431]
verified: false
---

# Human ZMPSTE24 (Zinc Metalloprotease)

## Overview

ZMPSTE24 (zinc metalloprotease STE24) is a human integral membrane zinc metalloprotease that catalyzes the proteolytic processing of prelamin A, a critical step in the maturation of lamin A, a key structural component of the nuclear lamina. The enzyme is embedded in the inner nuclear membrane and performs two sequential cleavages of the C-terminal 15 residues of farnesylated prelamin A. Mutations in ZMPSTE24 cause a spectrum of laminopathies ranging from restrictive dermopathy (RD) and Hutchinson-Gilford progeria syndrome (HGPS) to milder forms including mandibuloacral dysplasia (MAD-B), lipodystrophy (LD), and metabolic syndrome (MS). The 3.4 A crystal structure reveals a seven-transmembrane α-helical barrel enclosing a large, water-filled chamber (12,000 A³; 40 A deep by 25 A wide) that spans the membrane. The chamber is sealed on the nucleoplasmic side by an M48 zinc metalloprotease domain and on the ER lumenal side by three lumenal helices, with four fenestrations providing access from the nucleoplasm and membrane.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1231513 | 4AW6 | 3.40 | -- | Full-length human ZMPSTE24 | Zn2+ (catalytic zinc) |
| doi/10.1107##s2059798318003431 | 6BH8 | 3.85 | P2_1 | Full-length human ZMPSTE24 in complex with phosphoramidon | Phosphoramidon, Zn2+ |

## Expression and Purification

- **Expression system**: Not specified (purified from human cells or recombinant system — see supplementary materials)
- **Construct**: Full-length human ZMPSTE24

### Purification Workflow

#### Source: doi/10.1126##science.1231513

- **Expression system**: Not specified
- **Expression construct**: Full-length human ZMPSTE24

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | Detergent-lipid system purification | -- | Not detailed in main text + Two different detergent-lipid systems (see supplementary materials) | Two independent crystal packing arrangements obtained, each with four copies per asymmetric unit. Phases from ethylmercury thiosalicylate derivative and eightfold averaging. |

**Final sample**: Purified ZMPSTE24 in detergent-lipid system

#### Source: doi/10.1107##s2059798318003431

- **Expression system**: Saccharomyces cerevisiae BJ5460 (overexpression)
- **Expression construct**: Full-length human ZMPSTE24 with C-terminal His6 tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer (three passes at 193 MPa) | -- | 20 mM HEPES, 50 mM NaCl, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mM MgCl2, 2 mM beta-ME, 100 uM PMSF, 2.5 ug/mL leupeptin, 100 U benzonase, pH 7.5 + -- | Cells resuspended with hand-held glass homogenizer |
| Membrane isolation | Ultracentrifugation | -- | 50 mM HEPES, 150 mM NaCl, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mM beta-ME, 100 uM PMSF, 2.5 ug/mL leupeptin, pH 7.5 + -- | 205,000g for 90 min at 4 C to isolate membrane fraction (~25 g membranes) |
| Solubilization | Detergent extraction | -- | 50 mM HEPES, 500 mM NaCl, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 2 mM beta-ME, 100 uM PMSF, pH 7.5 + 1.5% (w/v) n-Dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Incubated at room temperature on benchtop [ROCKER](/xray-mp-wiki/proteins/miscellaneous/rocker/) |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) cobalt metal-affinity | [TALON](/xray-mp-wiki/reagents/additives/talon/) cobalt resin (Takada) | 50 mM HEPES, 500 mM NaCl, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 2 mM beta-ME, 100 uM PMSF, pH 7.5 + 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), exchanged to 0.04% C12E7 | Incubated 4 h at 4 C. Washed with 30 CV wash buffer twice. Detergent exchanged from [DDM](/xray-mp-wiki/reagents/detergents/ddm/) to C12E7 on-column. |
| Elution | [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) elution | -- | 50 mM HEPES, 150 mM NaCl, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 2 mM beta-ME, 100 uM PMSF, pH 7.5 + 0.04% C12E7 | Eluted with 5 CV elution buffer. Concentrated to ~10 mL using Amicon 50 kDa MWCO. |
| Desalting | Desalting column | HiPrep 26/10 (GE Healthcare) | 50 mM HEPES, 150 mM NaCl, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mM beta-ME, 100 uM PMSF, pH 7.5 + 0.04% C12E7 | Followed by SEC on [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) column equilibrated with same buffer |

**Final sample**: Purified ZMPSTE24 in C12E7 detergent


## Crystallization

### doi/10.1126##science.1231513

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified ZMPSTE24 in two different detergent-lipid systems |
| Reservoir | Not specified in main text (see supplementary materials) |
| Temperature | Not specified |
| Cryoprotection | Not specified |
| Notes | Two independent crystal packing arrangements obtained at 3.4 A resolution. Crystals belong to a lattice with four copies per asymmetric unit. Phasing by ethylmercury thiosalicylate MIR with eightfold non-crystallographic symmetry averaging. A 3.8 A complex with CSIM tetrapeptide (Cys-Ser-Ile-Met from prelamin A C-terminus) was also obtained. |

### doi/10.1107##s2059798318003431

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 5.5 mg/mL (98.5 uM) ZMPSTE24 incubated with 845 uM phosphoramidon (5% DMSO) for 1 h on ice. Diluted with detergent-free buffer (20 mM HEPES, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mM beta-ME, pH 7.5) |
| Reservoir | 27% [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350, 170 mM [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/), 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 50 mM HEPES pH 7.5 |
| Temperature | 23 C (setup), then immediately transferred to 4 C for crystal growth |
| Cryoprotection | None (plunge-cooled directly in liquid nitrogen) |
| Notes | Needle-like crystals of 50-400 um appeared 1-3 d. Harvested 21 d post-setup. Data collected at APS GM/CA CAT 23-ID-D (1.03 A, 10 um beam). Helical data collection across crystal body. Resolution truncated to 3.85 A based on CC1/2 > 0.3 and I/sigma(I) > 0.5. Two copies per asymmetric unit, space group P2_1. |


## Biological / Functional Insights

### Seven-transmembrane barrel with large internal chamber

ZMPSTE24 adopts a seven-transmembrane α-helical barrel enclosing an unusually large chamber (12,000 A³; 40 A deep by 25 A wide) that spans the entire membrane. The chamber is sealed on the nucleoplasmic side by the M48 zinc metalloprotease domain (inserted between TMH5 and TMH6) and on the ER lumenal side by three lumenal helices (LH1, LH2, TMH7A). Four fenestrations allow access from the nucleoplasm and the membrane. Molecular dynamics simulations confirmed the structure is stable with the chamber filled with water. The interior has mixed polar-nonpolar character with a charged patch between TMH1 and TMH7 and three hydrophobic patches.

### Catalytic mechanism and active site architecture

The catalytic zinc is coordinated by His335 and His339 from the HEXXH motif (H335ELGH) and Glu415 from TMH7. Glu336 is predicted to be the catalytic residue, aligning and activating the catalytic water molecule that attacks the substrate. Structural alignments predict that Asn265 and His459 stabilize the transition state during catalysis. The active site lies at the apex of the chamber on the nucleoplasmic side of the membrane. The potential substrate-binding site was inferred from a 3.8 A structure of the E336A mutant in complex with a CSIM tetrapeptide from the C-terminus of prelamin A, revealing hydrophobic pockets that dictate specificity for residues adjacent to the cleavage sites, analogous to thermolysin-like metalloproteases.

### Structural basis of laminopathy-causing mutations

Six disease-causing point mutations in ZMPSTE24 reduce enzymatic activity: five in the zinc metalloprotease domain (N265S, L438F, L462R, W340R, P248L) and one at the ER lumen end of the barrel (L94P). N265S (causing MAD-B or atypical HGPS) reduces activity to 5% and likely disrupts a main-chain hydrogen bond stabilizing the transition state. L438F and L462R (restrictive dermopathy) insert bulky side chains into the peptide-binding site, with L462R potentially displacing the catalytic His459. W340R (MAD-B, activity reduced to 1/6) disrupts the hydrophobic cluster positioning the HEXXH helix. P248L (MAD-B) disrupts a tight turn near the substrate entry fenestration. L94P (MAD-B, near-complete loss of activity) disrupts the elbow joint between TMH2 and LH1, likely destabilizing the protein fold.

### Phosphoramidon inhibition and gluzincin relationship

The natural product inhibitor phosphoramidon (N-(alpha-rhamnopyranosyl-oxy-hydroxyphosphinyl)-Leu-Trp), a transition-state analog competitive inhibitor of soluble gluzincins ([Thermolysin](/xray-mp-wiki/reagents/additives/thermolysin/), neprilysin), also inhibits ZMPSTE24 with IC50 values of 7.6-10.5 uM. A 3.85 A co-crystal structure (PDB 6bh8) reveals phosphoramidon bound at the active site within the intramembrane cavity, coordinating the zinc center through its phosphoramidate moiety. The binding mode is conserved with soluble gluzincins: the tryptophan (P2') and leucine (P1') moieties occupy specificity pockets S2' and S1', respectively. However, the ZMPSTE24 specificity pocket differs in composition (Leu438 substitutes for Phe130/Phe106 in [Thermolysin](/xray-mp-wiki/reagents/additives/thermolysin/)/neprilysin), predicting diminished potency. Despite its novel intramembranous reaction chamber architecture, ZMPSTE24 shares fundamental catalytic and specificity pocket features with soluble gluzincins, confirming it as a membrane-embedded member of this protease family.


## Cross-References

- [Site-2 Protease Family Mechanism](/xray-mp-wiki/concepts/protein-families/site-2-protease-family-mechanism/) — ZMPSTE24 is a member of the M48 family of metalloproteases, related to site-2 proteases (S2P)
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [ROCKER](/xray-mp-wiki/proteins/miscellaneous/rocker/) — Related protein structure
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [TALON](/xray-mp-wiki/reagents/additives/talon/) — Additive used in purification or crystallization buffers
