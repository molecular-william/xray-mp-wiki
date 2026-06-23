---
title: Escherichia coli CorA Mg2+ Channel (Cytoplasmic Domain)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.05.024]
verified: false
---

# Escherichia coli CorA Mg2+ Channel (Cytoplasmic Domain)

## Overview

CorA from Escherichia coli is the family prototype of the CorA Mg2+ transporter channel, the major Mg2+ uptake system in prokaryotes. This entry documents the first crystal structures of the cytoplasmic domain from E. coli CorA (EcCorA), revealing a pentameric arrangement with novel Mg2+ binding sites at subunit interfaces and within the pore. The structures provide structural evidence for cooperative gating and demonstrate that the cytoplasmic domain alone contains all components necessary for the gating motion.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2017.05.024 | 5JML | 2.90 A | C 222_1 | 241EcCorA (residues 1-241 of EcCorA, cytoplasmic domain only, TEV-GFP-His8 tag) | Apo (no Mg2+) |
| doi/10.1016##j.str.2017.05.024 | 5JMM | 2.80 A | P 2_1 | 257EcCorA (residues 1-257 of EcCorA, cytoplasmic domain only, TEV-GFP-His8 tag) | Mg2+ (bound at interfacial and pore sites) |
| doi/10.1016##j.str.2017.05.024 | 5JMN | 2.85 A | P 2_1 | 257EcCorA-Mg2+/CoHex (residues 1-257 of EcCorA, cytoplasmic domain, TEV-GFP-His8 tag, with cobalt hexamine) | Mg2+ and cobalt hexamine (hexaamminecobalt(III)) |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: Cytoplasmic domains of EcCorA (residues 1-241, 1-247, and 1-257) cloned into pGFPe vector with N-terminal TEV-GFP-His8 tag, controlled by T7 promoter. Cells grown in Terrific broth at 37 C, induced with 0.4 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg), grown overnight at 20 C.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.9, 300 mM NaCl, EDTA-free Complete Protease Inhibitor Cocktail, Benzonase Nuclease, Lysozyme + -- | Cells resuspended in lysis buffer, sonicated, unbroken cells removed by centrifugation at 9300 g for 20 min |
| Affinity purification | [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) Agarose (Invitrogen) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.9, 300 mM NaCl + -- | Supernatant applied to 2 ml Ni-NTA Agarose, incubated 30 min. Washed with 2 column volumes of buffer containing 40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole). Eluted with buffer containing 350 mM imidazole. |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8, 100 mM NaCl + -- | Final purification step. [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) performed in presence or absence of Mg2+ depending on construct and experimental condition. |


## Crystallization

### doi/10.1016##j.str.2017.05.024

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | 241EcCorA monomeric construct |
| Reservoir | [PEG 400](/xray-mp-wiki/reagents/additives/peg-400)0 |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Monomeric 241EcCorA crystallized in space group C222_1 at 2.90 A resolution. Solved by SAD phasing with [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-labeled protein. |


## Biological / Functional Insights

### Novel Mg2+ ligand binding site at subunit interfaces

The 257EcCorA-Mg2+ structure reveals a novel putative Mg2+ ligand binding site located at the interface between each of the five subunits. A single Mg2+ ion is coordinated by D58 and E60 from the clutch motif of one subunit and D146 and E149 from helix 4 on the adjacent subunit. This represents a new variant of the regulatory Mg2+ ligand binding site in the CorA family, structurally distinct from the M1/M2 sites identified in TmCorA and MjCorA. ConSurf analysis shows all four Mg2+ binding residues, plus S62 and D222, are highly conserved in the CorA family. The pore helix residue D222 forms a hydrogen bond with S62 of the clutch motif, potentially mediating a subunit contact that stabilizes the pore helix indirectly.

### Mg2+ binding sites within the pore

Two Mg2+ ions are trapped inside the pore at each subunit. At the top site near the membrane interface, a putative substrate-Mg2+ is sandwiched between two polar rings: Q252 (5-fold, ~4.3 A pore diameter) and N249 (5-fold, ~7 A pore diameter). The bound Mg2+ coordinates with multiple amide oxygens from both rings. Below, a 5-fold ring of Q242 residues coordinates another Mg2+ ion in the ion-conduction pathway. The Q242 site has no direct contacts with protein side chains and appears functionally dispensable based on alanine scanning mutagenesis.

### Cobalt hexamine competes with Mg2+ at the pore site

Soaking experiments with cobalt hexamine (hexaamminecobalt(III)) show it outcompetes substrate-Mg2+ at the N249/Q252 site closest to the membrane, while the Q242 site and the five interfacial ligand binding sites retain their Mg2+. Cobalt hexamine binds at the N249/Q252 site and 13 peripheral sites. This provides the first structural evidence that a hexa-hydrated Mg2+ analog can fit inside the cytoplasmic portion of the CorA pore, suggesting Mg2+ is or becomes hexa-hydrated as it enters the pore.

### Cooperative gating by pentamer assembly/disassembly

[SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) shows the 257EcCorA cytoplasmic domain assembles into a pentamer in response to Mg2+ (100 mM) and dissociates to monomer in low Mg2+ (10 mM). The dissociation curve is sigmoidal, occurring between 10-20 mM Mg2+, indicating a cooperative process. Shorter constructs (241EcCorA, 247EcCorA) with truncated pore helices remain monomeric even at 100 mM Mg2+, showing pore helix length is critical for pentamer stabilization. Mutations of the interfacial ligand binding site (D58A/E60A/D146A/E149A) or N249A/Q252A prevent pentamer assembly, confirming both sites are essential for the gating mechanism.

### Full-length protein has 10-fold higher Mg2+ affinity

Protease protection assays comparing the isolated cytoplasmic domain (257EcCorA) with full-length 316EcCorA in native membranes reveal a 10-fold increase in Mg2+ affinity in the full-length protein. The cytoplasmic domain shows Mg2+-dependent protection between 10-20 mM, while full-length EcCorA requires only 0-10 mM Mg2+. This is attributed to structural stabilization of the interfacial ligand binding sites provided by intra- and inter-subunit interactions in the membrane domain. The isolated cytoplasmic domain thus contains all molecular components for gating but with non-physiological Mg2+ affinity.


## Cross-References

- [CorA Mg2+ Transporter](/xray-mp-wiki/concepts/transport-mechanisms/cora-mg-transporter/) — CorA is the prototype family; this paper provides first EcCorA cytoplasmic domain structures
- [Metal Ion Transporter Superfamily](/xray-mp-wiki/concepts/transport-mechanisms/mit-superfamily/) — CorA is the founding member of the MIT superfamily of metal ion transporters
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Used for final purification and [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) analysis of pentamer assembly/disassembly
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Used to solve 257EcCorA-Mg2+ and 257EcCorA-Mg2+/CoHex structures
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) — Used for [His Tag](/xray-mp-wiki/reagents/protein-tags/his-tag) affinity purification of TEV-GFP-His8 tagged constructs
- [Magnesium Chloride (MgCl2)](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Mg2+ is the physiological ligand that drives pentamer assembly and channel gating
- [Channel Gating via Plug Domain Displacement](/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/) — CorA gating mechanism involves rigid-body motion of cytoplasmic domain subunits
- [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) — Crystallization method used for structure determination
- [Immobilized Metal Affinity Chromatography (IMAC)](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) — Purification method used in protein preparation
- [IPTG](/xray-mp-wiki/reagents/additives/iptg) — Additive used in purification or crystallization buffers
