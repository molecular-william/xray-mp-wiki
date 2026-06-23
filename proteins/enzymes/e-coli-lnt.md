---
title: Escherichia coli Apolipoprotein N-Acyl Transferase (Lnt)
created: 2026-06-03
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms15948, doi/10.1038##ncomms15952, doi/10.1126##sciadv.adf5799]
verified: false
---

# Escherichia coli Apolipoprotein N-Acyl Transferase (Lnt)

## Overview

Apolipoprotein N-acyl transferase (Lnt) from Escherichia coli is a 512-residue integral membrane enzyme (57 kDa) that catalyses the third and final step of lipoprotein biogenesis in Gram-negative bacteria. Lnt transfers an acyl chain from the sn-1 position of a phospholipid donor (e.g. [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol)) to the alpha-amine group of the N-terminal cysteine residue of an apolipoprotein, completing the formation of a mature triacylated lipoprotein. Lnt belongs to the ninth branch of the nitrilase superfamily and contains a catalytic triad of E267-K335-C387. The enzyme consists of an eight-helix transmembrane (TM) domain fused to a periplasmic nitrilase (Nit) catalytic domain. A lid loop from the Nit domain interacts with the lipid bilayer, forming an interfacial entrance from the membrane to the catalytic centre.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms15948 | 5XHQ | 2.6 | P212121 | Full-length E. coli Lnt (512 residues) | none |
| doi/10.1038##ncomms15952 | 5N6H | 2.9 | P212121 | Full-length E. coli Lnt (512 residues), N-terminal thrombin-cleavable His-tag | none (apo) |
| doi/10.1038##ncomms15952 | 5N6L | 2.9 | P212121 | Full-length E. coli Lnt C387A mutant (512 residues), N-terminal thrombin-cleavable His-tag | monoolein (structured lipids in active site portal) |
| doi/10.1038##ncomms15952 | 5N6M | 3.1 | C2 | Full-length P. aeruginosa Lnt (514 residues), N-terminal thrombin-cleavable His-tag | none |
| doi/10.1126##sciadv.adf5799 | 8B0K | 3.0 | — | Full-length E. coli Lnt WT, HA-treated (deacylated) | none (apo) |
| doi/10.1126##sciadv.adf5799 | 8AQ3 | 2.4 | Not specified | Full-length E. coli Lnt C387A mutant | PE (phosphatidylethanolamine) |
| doi/10.1126##sciadv.adf5799 | 8B0M | 3.0 | — | Full-length E. coli Lnt C387S mutant | PE |
| doi/10.1126##sciadv.adf5799 | 8B0L | 3.1 | — | Full-length E. coli Lnt C387A mutant | PE |
| doi/10.1126##sciadv.adf5799 | 8B0N | 2.7 | — | Full-length E. coli Lnt WT (acyl-Lnt) | S-acyl chain (palmitate at C387), lyso-PE |
| doi/10.1126##sciadv.adf5799 | 8AQ4 | 2.6 | — | Full-length E. coli Lnt with TITC modification | TITC, lyso-PE |
| doi/10.1126##sciadv.adf5799 | 8AQ2 | 2.7 | — | Full-length P. aeruginosa Lnt with TITC modification | TITC, monoolein (2 molecules) |
| doi/10.1126##sciadv.adf5799 | 8B0P | 2.9 | — | Full-length E. coli Lnt C387A mutant | Pam3CSK4 |
| doi/10.1126##sciadv.adf5799 | 8B0O | 3.0 | — | Full-length E. coli Lnt C387S mutant | FP3 (TA-BLPtide product) |

## Expression and Purification

- **Expression system**: E. coli C43(DE3) / C41(DE3)
- **Construct**: Full-length lnt gene (GenBank ID: 946201 for E. coli; synthetic gene for P. aeruginosa) cloned into pET28a vector. N-terminal thrombin-cleavable His-tag for purification.

- **Induction**: 0.5 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg), 20 h at 20 C post-induction

### Purification Workflow

*Source: doi/10.1038##ncomms15948*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization | -- | 50 mM HEPES pH 7.5, 100 mM NaCl, 10% glycerol, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 1 mM PMSF + -- | Cells centrifuged at 18,000g for 20 min to remove debris |
| Membrane fraction collection | Ultracentrifugation | -- | Lysis buffer + -- | Supernatant centrifuged at 100,000g for 1 h; membrane pellet collected |
| Solubilization | Detergent solubilization | -- | Lysis buffer + 2% n-decyl-beta-D-maltopyranoside | Membrane pellet dissolved in buffer with 2% n-decyl-beta-D-maltopyranoside at 4 C for 1 h |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | Ni-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) | Lysis buffer with 2% n-decyl-beta-D-maltopyranoside + 2% n-decyl-beta-D-maltopyranoside | Tagged proteins in supernatant purified by Ni-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) |

### Purification Workflow

*Source: doi/10.1038##ncomms15952*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization (Emulsiflex-CS) | -- | 20 mM Tris-HCl pH 8.0, 50 mM NaCl, 0.5 mM EDTA, 1 mM PMSF + -- | Cells lysed at 1000-1750 bar at 4 C |
| Membrane isolation | Ultracentrifugation | -- | 20 mM Tris-HCl pH 8.0, 50 mM NaCl, 0.5 mM EDTA, 1 mM PMSF + -- | Membranes pelleted at 120,000g for 2 h at 4 C |
| Solubilization | Detergent solubilization (dodecyl-beta-D-maltoside, DDM) | -- | 20 mM Tris-HCl pH 8.0, 50 mM NaCl, 0.5 mM EDTA, 1 mM PMSF + 1% (w/v) n-dodecyl-beta-D-maltopyranoside (DDM) | membranes solubilized by stirring for 2 h at 4 C; insoluble material removed by centrifugation at 120,000g |
| Affinity chromatography | Ni-NTA affinity | Ni-NTA agarose | 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 20 mM imidazole, 0.5 mM EDTA, 0.3% (w/v) DDM + 0.3% DDM | Protein eluted with 300 mM imidazole in same buffer |
| Size-exclusion chromatography | SEC | Superdex 200 10/300 GL | 20 mM Tris-HCl pH 8.0, 50 mM NaCl, 0.5 mM EDTA, 0.3% (w/v) DDM + 0.3% DDM | Peak fractions concentrated to 5-10 mg/ml for crystallization |


## Crystallization

### doi/10.1038##ncomms15948

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | 12 mg/ml E. coli Lnt in 50 mM HEPES pH 7.5, 100 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 2% n-decyl-beta-D-maltopyranoside
 |
| Reservoir | 30% PEG 400, 0.2 M sodium [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate) pH 4.6
 |
| Temperature | 4 |
| Growth time | not specified in paper |
| Cryoprotection | Crystals cryoprotected and flash-frozen in liquid nitrogen |
| Notes | Native data collected at BL17U at SSRF (wavelength 0.9793 A). Se-Met SAD data collected at BL1A at KEK (wavelength 0.9791 A). Space group P212121. Resolution 50-2.59 A. R_work/R_free: 23.2/28.9%.
 |

### doi/10.1038##ncomms15952

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) |
| Protein sample | Lnt in 20 mM Tris-HCl pH 8.0, 50 mM NaCl, 0.5 mM EDTA, 0.3% DDM, reconstituted into monoolein (9.9 MAG) cubic mesophase (2:3 v/v protein:lipid)
 |
| Temperature | 20 |
| Growth time | ~2 weeks |
| Cryoprotection | Crystals harvested from LCP and snap-cooled in liquid nitrogen without added cryoprotectant |
| Notes | Data collected at Swiss Light Source (X06SA-PXI, X10SA-PXII). SeMet SAD at 0.9792 A for phasing. LntEco and LntEcoC387A in P212121; LntPae in C2.
 |


## Biological / Functional Insights

### Structural architecture of Lnt

E. coli Lnt contains an eight-helix transmembrane (TM) domain that forms a
membrane-embedded cavity with a lateral opening and a periplasmic exit. The
nitrilase (Nit) catalytic domain is located on the periplasmic side of the
membrane, with its catalytic cavity connected to the periplasmic exit of the
TM domain. The Nit domain contains the characteristic alpha-beta-alpha folding
topology of the nitrilase superfamily and a conserved Glu-Lys-Cys catalytic
triad (E267-K335-C387).

### Amphipathic lid loop mediates membrane interaction

An amphipathic lid loop (residues F357-D359) from the Nit domain interacts
with the periplasmic lipid leaflet, forming an interfacial entrance from the
lipid bilayer to the catalytic centre. The lid loop anchors the Nit domain
to the outer leaflet through multiple interactions: aromatic residues F357
and F358 interact with lipid molecules, the acidic sidechain of D359
interacts with the head-group of a [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol) molecule, and the
basic sidechain of R352 interacts with the phosphate-group of a lipid
molecule. The lid loop protects the catalytic site from exposure to the
solvent phase.

### Ping-pong catalytic mechanism

Lnt uses a two-step ping-pong mechanism. In the first step, the lipid donor
substrate enters the catalytic cavity through the interfacial opening, and
an acyl-enzyme thioester intermediate is formed with C387. The leaving group
(sn-2-lyso-glycerolphosphate) is released to the lipid bilayer. In the
second step, the lipid-acceptor substrate (apolipoprotein) enters the
reaction cavity and its N-terminal amine group attacks the reaction-centre
carbon atom, resulting in cleavage of the C-S bond and formation of the
mature triacylated lipoprotein.

### Functional residues identified by mutagenesis

Mutagenesis studies identified several functionally important residues. P147
at the TM-Nit domain interface is important for full Lnt activity. The double
mutant F357A/F358A in the lid loop is inactive. Residues S78 (in TM3),
V339 (lid loop), Y388 (near catalytic Cys), and E389 (alpha3') were shown
to maintain the ability to form the acyl-enzyme intermediate, suggesting
they are involved in the second step of the reaction (substrate recognition
and binding of the apolipoprotein substrate).

### Substrate portal defined by structured lipids

In the LntEco-C387A mutant structure, structured monoolein lipid molecules line up in single file along a hydrophobic pocket connecting the bulk membrane to the active site. This portal is formed by periplasmic extensions of TM3 and TM4 (Arm 1), L1 between H5 and H6 (Arm 2), and loops in the Nit domain (Arm 3). Lipids enter this region from the bulk membrane via the H4-H5 cleft, defining the route for phospholipid substrates to access the active site.

### Conserved nitrilase superfamily fold

Lnt is a member of the nitrilase superfamily with a four-layer alphabeta betaalpha sandwich fold in the Nit domain. The catalytic Cys387 resides in a nucleophilic elbow (beta-strand-turn-helix motif) characteristic of nitrilases. The oxyanion hole is formed by backbone amides of I390, I391, and L392 in alpha3'. Structure-based pKa calculations support the proposed catalytic roles of Glu267 (proton abstraction) and Lys335 (oxyanion stabilization).

### Complete structural snapshots of the ping-pong reaction cycle (2023)

A comprehensive structural study (Smithers et al., Sci. Adv. 2023) used MX and cryo-EM to capture nine structures representing all six states of the Lnt N-acylation ping-pong reaction: Apo (8B0K), M1 (8AQ3/8B0M/8B0L), P1 (8B0N/8AQ4), M2 mimic (8AQ2), and P2 (8B0P/8B0O). The study identified a single active site that binds GPL and BLP substrates sequentially. Three distinct acyl chain binding sites were defined. Arm 3 (residues 348-363) was shown to be flexible in apo and becomes ordered upon substrate binding. The structures validate the ping-pong mechanism, explain substrate promiscuity, and should facilitate antibiotic design.

### Apo state captured by cryo-EM after hydroxylamine treatment

Hydroxylamine (HA) treatment was implemented to remove thioacylation and adventitious phospholipids from Lnt. Cryo-EM analysis provided a 3.0 A reconstruction of the apo state with an active site free of thioacylation, lipids, and substrates. The HA-treated protein was enzymatically active only with added GPLs. Arm 3 was partly disordered in the apo state (16 residues without density: Glu348-Ser363), suggesting it is flexible and involved in substrate binding.

### M1 state reveals PE binding and arm 3 ordering

The M1 (first Michaelis complex) structures show PE bound with its glyceryl phosphoethanolamine headgroup positioned in front of the catalytic triad and acyl chains extending into the hydrophobic groove. The sn-1 ester is positioned next to C387 for reaction. Arm 3 becomes stably folded over the PE molecule. The MX structure (8AQ3, 2.4 A) is the highest resolution Lnt structure to date.

### P1 and acyl-enzyme intermediate states

The P1 (first product complex) structures capture the acyl-enzyme intermediate with a palmitoyl thioester at C387 and lyso-PE bound adjacent. Interactions between enzyme and lyso-PE are fewer than for PE in M1, consistent with lyso-PE release. The S-acyl chain at C387 and lyso-PE occupy distinct volumes in the binding pocket. Native MS confirmed palmitate modification of Lnt.

### P2 state reveals TA-BLP product binding and arm rearrangements

The P2 (second product complex) structures show the triacylated BLP product (Pam3CSK4 or FP3) bound in the pocket. The acyl amide linkage is positioned within a few angstroms of the catalytic site. The diacylated glyceryl moiety extends away from the catalytic center with acyl chains running parallel. The peptide part extends through an opening at the top of the binding pocket created by conformational changes in arm 3 and arm 7. Comparison of P1 and P2 states shows the biggest changes in arms 1, 3, and 9.


## Cross-References

- [Phosphatidylglycerol (PG)](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) — Primary acyl-donor lipid substrate for Lnt
- [N-Decyl-beta-D-maltopyranoside](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used for membrane solubilization
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in lysis, purification, and crystallization
- [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) — Crystallization method used for structure determination (ncomms15948)
- [Lipidic Cubic Phase (LCP)](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) — Crystallization method used for structure determination (ncomms15952)
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) — Purification method used in protein preparation
- [IPTG](/xray-mp-wiki/reagents/additives/iptg) — Additive used in purification or crystallization buffers
- [Acetate](/xray-mp-wiki/reagents/buffers/acetate) — Buffer component in purification and crystallization
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) — Additive used in purification or crystallization buffers
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) — Additive used in purification or crystallization buffers
- [Pseudomonas aeruginosa Apolipoprotein N-Acyl Transferase (LntPae)](/xray-mp-wiki/proteins/enzymes/pseudomonas-aeruginosa-lnt/) — Orthologous Lnt from P. aeruginosa with 39% sequence identity
- [Ping-Pong Catalytic Mechanism](/xray-mp-wiki/concepts/ping-pong-mechanism/) — Lnt N-acylation cycle provides definitive structural evidence for ping-pong mechanism; 9 structures capturing all reaction states
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Six of nine structures determined by cryo-EM showing all states of the Lnt reaction cycle
