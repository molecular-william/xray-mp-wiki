---
title: "CAX_Af H+/Ca2+ Exchanger (Archaeoglobus fulgidus)"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1239002]
verified: false
---

# CAX_Af H+/Ca2+ Exchanger (Archaeoglobus fulgidus)

## Overview

CAX_Af is a H+/Ca2+ exchanger from the hyperthermophilic archaeon Archaeoglobus
fulgidus, belonging to the Ca2+:cation antiporter (CaCA) superfamily. It catalyzes
the exchange of Ca2+ for H+ across biological membranes to regulate cytosolic
calcium levels. The crystal structure at 2.3 A resolution (PDB 4KPP), determined
by the lipidic cubic phase (LCP) method, revealed an inward-facing conformation
with 12 transmembrane helices. Structural comparison with the Na+/Ca2+ exchanger
[NCX_Mj](/xray-mp-wiki/proteins/slc-transporters/ncx-mj/) in the outward-facing state showed that
the first and sixth transmembrane helices alternately create hydrophilic cavities
on the intra- and extracellular sides. The structures and functional analyses
provide insight into how the inward- to outward-facing state transition is triggered
by Ca2+ and H+ binding. CAX_Af is one of only two CAX family structures determined
(alongside [Vcx1](/xray-mp-wiki/proteins/slc-transporters/vcx1/)) and represents the first H+/Ca2+
exchanger structure captured in an inward-facing conformation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1239002 | 4KPP | 2.3 | P212121 | Full-length CAX_Af (residues 1-301) | none (H+ bound state) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length CAX_Af from Archaeoglobus fulgidus
- **Notes**: Expressed in E. coli for functional characterization; purified and crystallized via LCP method. Mutants (E78A, E78Q, E255A, E255Q, E258A, E258Q) were generated for functional studies.

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Full-length CAX_Af

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli expression | — |  | Expressed in E. coli cells for 45Ca2+ uptake assays using IPTG induction |
| Purification | Affinity chromatography | — |  | Purified protein crystallized by LCP method. Details in Supporting Online Material. |


## Crystallization

### doi/10.1126##science.1239002

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified CAX_Af in detergent |
| Temperature | 20 |
| Notes | Crystallized under low-pH conditions (pH 6.0-6.5) which stabilizes the H+ bound state. Structure determined by multiple anomalous dispersion (MAD) using mercury derivatives. Final model refined to 2.3 A resolution. Crystallographic asymmetric unit contained two molecules. |


## Biological / Functional Insights

### Inward-facing conformation with 12 transmembrane helices

CAX_Af contains 12 TM helices with both N and C termini on the intracellular side. The structure comprises a core domain (TMs 2-5, 7-10) homologous to NCX_Mj, a gating bundle (TMs 1 and 6), and two additional N- and C-terminal helices. The gating bundle (TM1 and TM6) creates hydrophilic cavities alternately on the intra- and extracellular sides during the transport cycle. In the inward-facing conformation, TM1 adopts a straight conformation creating an inward-facing cavity, while TM6 is bent and packed against the extracellular halves of TM2 and TM7.

### Mutually exclusive Ca2+ and H+ binding

The crystal structure reveals two hydrogen-bonding networks (Hext and Hmid) involving Glu78, Glu255, and Glu258 that function as H+ binding sites. These residues are also involved in Ca2+ coordination, making Ca2+ and H+ binding mutually exclusive. The structure was obtained under low pH (6.0-6.5) and represents the H+ bound state, which cannot accommodate Ca2+. This mutually exclusive binding is consistent with the counter-transport mechanism of the CaCA superfamily — H+ and Ca2+ compete for the same binding pocket.

### Two protonation states: mol A (fully protonated) and mol B (partially protonated)

The asymmetric unit contains two CAX_Af molecules. Mol A represents a 'fully' protonated state with intact Hext and Hmid hydrogen-bonding networks bridging TM7 and TM8. Mol B represents a 'partially' protonated state where Glu258 is deprotonated and the Hmid network is partially disrupted, causing TM7 to twist and create a gap between Pro77 and Pro257. This gap splits the hydrophobic patch that enables the gating bundle to slide, suggesting that H+ binding closes the hydrophobic patch and enables transition to the outward-facing state.

### Alternating access via gating bundle sliding

Comparison of the inward-facing CAX_Af structure with the outward-facing NCX_Mj structure (PDB 3V5U) revealed a common alternating access mechanism. The gating bundle helices (TM1 and TM6) slide relative to the core domain, alternately creating hydrophilic cavities for cation access. In CAX_Af, a hydrophilic cluster on TM1 (Ser47, Ser51, Glu55, Glu58) faces the inward cavity. In NCX_Mj, a hydrophilic cluster on TM6 faces the outward cavity. The transition involves a sliding motion of the gating bundle across a central hydrophobic patch formed by Pro residues and neighboring hydrophobic side chains.

### Functional importance of conserved glutamate residues

Alanine or glutamine mutations of Glu78, Glu255, or Glu258 decreased H+/Ca2+ exchange activity in liposome-based 45Ca2+ uptake assays. These residues are at equivalent positions to Na+ coordinating residues in NCX_Mj and are involved in both Ca2+ and H+ binding. The results demonstrate the importance of protonation and deprotonation of these conserved carboxylates during the exchange cycle.


## Cross-References

- [NCX_Mj Sodium/Calcium Exchanger](/xray-mp-wiki/proteins/slc-transporters/ncx-mj/) — Homologous CaCA superfamily member; outward-facing structure used for structural comparison revealing the alternating access mechanism
- [Ca2+:Cation Antiporter (CaCA) Superfamily](/xray-mp-wiki/concepts/transport-mechanisms/caca-superfamily/) — CAX_Af is a member of the CAX family within the CaCA superfamily
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — CAX_Af operates via alternating access with gating bundle sliding
- [Vcx1](/xray-mp-wiki/proteins/slc-transporters/vcx1/) — Another CAX family structure; cytosol-facing conformation for comparison
