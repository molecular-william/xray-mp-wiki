---
title: Escherichia coli Apolipoprotein N-Acyl Transferase (Lnt)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms15948]
verified: false
---

# Escherichia coli Apolipoprotein N-Acyl Transferase (Lnt)

## Overview

Apolipoprotein N-acyl transferase (Lnt) from Escherichia coli is a 512-residue integral membrane enzyme (57 kDa) that catalyses the third and final step of lipoprotein biogenesis in Gram-negative bacteria. Lnt transfers an acyl chain from the sn-1 position of a phospholipid donor (e.g. phosphatidylglycerol) to the alpha-amine group of the N-terminal cysteine residue of an apolipoprotein, completing the formation of a mature triacylated lipoprotein. Lnt belongs to the ninth branch of the nitrilase superfamily and contains a catalytic triad of E267-K335-C387. The enzyme consists of an eight-helix transmembrane (TM) domain fused to a periplasmic nitrilase (Nit) catalytic domain. A lid loop from the Nit domain interacts with the lipid bilayer, forming an interfacial entrance from the membrane to the catalytic centre.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms15948 | 5XHQ | 2.6 | P212121 | Full-length E. coli Lnt (512 residues) | none |

## Expression and Purification

- **Expression system**: E. coli C41 (DE3)
- **Construct**: Full-length lnt gene (GenBank ID: 946201) amplified from E. coli K-12 genome and ligated into pET-22b(+) vector. C-terminal His6-tagged for purification and immunoblotting.

- **Induction**: 0.5 mM IPTG, 16 h culture

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization | -- | 50 mM HEPES pH 7.5, 100 mM NaCl, 10% glycerol, 20 mM imidazole, 1 mM PMSF + -- | Cells centrifuged at 18,000g for 20 min to remove debris |
| Membrane fraction collection | Ultracentrifugation | -- | Lysis buffer + -- | Supernatant centrifuged at 100,000g for 1 h; membrane pellet collected |
| Solubilization | Detergent solubilization | -- | Lysis buffer + 2% n-decyl-beta-D-maltopyranoside | Membrane pellet dissolved in buffer with 2% n-decyl-beta-D-maltopyranoside at 4 C for 1 h |
| Affinity chromatography | Ni-affinity chromatography | Ni-NTA | Lysis buffer with 2% n-decyl-beta-D-maltopyranoside + 2% n-decyl-beta-D-maltopyranoside | Tagged proteins in supernatant purified by Ni-affinity chromatography |


## Crystallization

### doi/10.1038##ncomms15948

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | 12 mg/ml E. coli Lnt in 50 mM HEPES pH 7.5, 100 mM NaCl, 20 mM imidazole, 2% n-decyl-beta-D-maltopyranoside
 |
| Reservoir | 30% PEG 400, 0.2 M sodium acetate pH 4.6
 |
| Temperature | 4 |
| Growth time | not specified in paper |
| Cryoprotection | Crystals cryoprotected and flash-frozen in liquid nitrogen |
| Notes | Native data collected at BL17U at SSRF (wavelength 0.9793 A). Se-Met SAD data collected at BL1A at KEK (wavelength 0.9791 A). Space group P212121. Resolution 50-2.59 A. R_work/R_free: 23.2/28.9%.
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
interacts with the head-group of a phosphatidylglycerol molecule, and the
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


## Cross-References

- [Phosphatidylglycerol (PG)](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) — Primary acyl-donor lipid substrate for Lnt
- [N-Decyl-beta-D-maltopyranoside](/xray-mp-wiki/reagents/detergents/n-decyl-beta-d-maltopyranoside/) — Detergent used for membrane solubilization
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in lysis, purification, and crystallization
