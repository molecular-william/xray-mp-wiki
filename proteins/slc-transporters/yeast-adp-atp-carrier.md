---
title: Yeast ADP/ATP Carrier (Aac2p and Aac3p)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1320692111]
verified: false
---

# Yeast ADP/ATP Carrier (Aac2p and Aac3p)

## Overview

The yeast ADP/ATP carriers (Aac2p and Aac3p) are archetypal members of the
mitochondrial carrier family that import ADP from the cytosol into the
mitochondrial matrix and export newly synthesized ATP to the cytosol. These
carriers cycle between a cytoplasmic state (c-state), in which the carrier
accepts ADP from the intermembrane space, and a matrix state (m-state), in
which it accepts ATP from the mitochondrial matrix. The crystal structures
of carboxyatractyloside (CATR)-inhibited Aac2p and Aac3p were determined at
2.5–3.4-Å resolution. Each carrier consists of six transmembrane α-helices
(H1–H6) arranged with threefold pseudosymmetry, forming a central cavity
open to the cytoplasmic side but closed to the mitochondrial matrix by three
interdomain salt-bridge interactions. A conserved glutamine residue braces
one of these salt bridges, contributing to an energy barrier that prevents
conversion to the m-state without substrate binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1320692111 | not specified | 2.5 | C2221 | Full-length Saccharomyces cerevisiae Aac2p with N-terminal His tag | CATR (carboxyatractyloside) |
| doi/10.1073##pnas.1320692111 | not specified | 3.2 | P212121 | Full-length S. cerevisiae Aac2p with N-terminal His tag | CATR |
| doi/10.1073##pnas.1320692111 | not specified | 3.4 | P212121 | Full-length S. cerevisiae Aac3p with N-terminal His tag | CATR |
| doi/10.1073##pnas.1320692111 | not specified | 3.2 | P21 | Full-length S. cerevisiae Aac3p with N-terminal His tag | CATR |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae strain WB12
- **Construct**: AAC2 or AAC3 gene in modified pYES3 vector with N-terminal His tag and Factor Xa cleavage site
- **Notes**: Mitochondria prepared from disrupted cells

### Purification Workflow

- **Expression system**: S. cerevisiae WB12
- **Expression construct**: Aac2p or Aac3p with N-terminal His tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Mitochondrial preparation | Cell disruption | — |  | Mitochondria isolated from disrupted yeast cells |
| Solubilization | Detergent solubilization | — | undecyl-beta-D-maltoside | Protein solubilized with undecyl-beta-D-maltoside |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni Sepharose [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — |  | Purified by Ni Sepharose; detergent exchanged on-column |
| Detergent exchange (Aac2p) | On-column detergent exchange | — | 5-cyclohexyl-1-pentyl-beta-D-maltoside (CYMAL-5) | Exchanged while bound to Ni Sepharose resin |
| Detergent exchange (Aac3p) | On-column detergent exchange | — | [n-Decyl-β-D-maltoside](/xray-mp-wiki/reagents/detergents/dm/) (DM) | Exchanged while bound to Ni Sepharose resin |
| Tag cleavage | Factor Xa protease cleavage | — |  | N-terminal His tag cleaved by Factor Xa |
| Concentration | Concentration | — |  | Protein concentrated for crystallization |

**Final sample**: Purified Aac2p or Aac3p in respective maltoside detergent


## Crystallization

### doi/10.1073##pnas.1320692111

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Notes | Both proteins crystallized in two different crystal forms; data collected at ESRF beamline ID23-2 |


## Biological / Functional Insights

### Domain-based alternating-access mechanism

The structures support a domain-based alternating-access transport
mechanism for mitochondrial carriers. The three homologous sequence
repeats fold into three structural domains, each comprising two
transmembrane helices and a matrix helix. The odd-numbered α-helices
(H1, H3, H5) contain kinks at proline or serine residues, functioning
as lever arms that couple substrate-induced disruption of the matrix
salt-bridge network to formation of the cytoplasmic salt-bridge network.
The simultaneous movement of three domains around a central translocation
pathway is unique among transport proteins.

### Matrix salt-bridge network and glutamine brace

The matrix side of the cavity is closed by a salt-bridge network formed
by charged residues of the Px[DE]xx[KR] signature motifs. A conserved
glutamine residue braces the salt bridge between domains 1 and 3,
forming hydrogen bonds with both charged residues. This glutamine brace
contributes to an energy barrier that must be overcome by substrate
binding, enforcing a strict equimolar exchange. Yeast ADP/ATP carriers
have one brace, while carriers such as the [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) carrier Ctp1 may
have two or three.

### Cytoplasmic salt-bridge network forms during transport

Experimental evidence demonstrates that a conserved YFxx[KR] motif on
the cytoplasmic side forms a salt-bridge network when the carrier is
in the m-state. Mutagenesis with charge-reversed networks showed that
mutants with all positively or all negatively charged cytoplasmic
networks were inactive, but when the network residues were interchanged
(six mutations), transport activity was restored to ~14% of wild-type.
The restored activity remained sensitive to CATR and [Bongkrekic Acid](/xray-mp-wiki/reagents/ligands/bongkrekic-acid/),
confirming specific transport.

### Cardiolipin binding and structural role

Three [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) molecules bind in pockets between the matrix helices
and the matrix end of the even-numbered transmembrane helices. The
[Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) phosphate groups are positioned near the N-terminal ends of
helices, interacting with helix dipoles and forming hydrogen bonds to
exposed amide groups. Conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues (including those in
YWFG and [YF]xG motifs) are key to forming the binding sites.
[Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) may act as 'grease' at a dynamic interface, protecting
mobile regions and allowing close packing.

### Serine kink in H3 mimics proline

In over 40% of ADP/ATP carrier sequences, the conserved proline on H3
is substituted by serine (Ser147 in Aac2p). The serine side-chain makes
an unusual hydrogen bond to its own backbone amide group, mimicking the
structure of proline and maintaining the ~50° kink angle. This rare
arrangement is stabilized by a network of side-chain interactions,
including a hydrogen bond to Tyr177 on matrix helix h34.

### C-terminal region folds into the cavity

The yeast ADP/ATP carrier structures reveal the complete C-terminal
region, which is missing from bovine AAC1 structures. H6 adopts a sharp
turn at Gly314 and folds back into the central cavity, where Phe317
forms hydrophobic contacts with Met29 and an anion-π interaction with
Asp26. This C-terminal region may form an additional component of the
cytoplasmic gate.


## Cross-References

- [Bovine ADP/ATP Carrier (AAC1)](/xray-mp-wiki/proteins/slc-transporters/bovine-adp-atp-carrier/) — Orthologous carrier; used as molecular replacement search model; structural comparison
- [Thermothelomyces thermophila ADP/ATP Carrier](/xray-mp-wiki/proteins/slc-transporters/thermothelomyces-thermophila-adp-atp-carrier/) — Related fungal ADP/ATP carrier for structural comparison
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — Yeast ADP/ATP carriers provide structural basis for domain-based alternating-access transport
- [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) — Three cardiolipin molecules tightly bound at interdomain interfaces
- [Bongkrekic Acid](/xray-mp-wiki/reagents/additives/bongkrekic-acid/) — Specific inhibitor that locks the carrier in the matrix state (m-state)
- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — ADP/ATP carriers and ABC transporters both exemplify alternating-access transport mechanisms
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in purification or crystallization
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Buffer component in purification or crystallization
- [n-Decyl-β-D-maltoside](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used in purification or crystallization
