---
title: "EcSatP — Bacterial Succinate-Acetate Transporter (AceTr Family)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, channel, membrane-protein]
sources: [doi/10.1074##jbc.RA118.003876]
verified: false
---

# EcSatP — Bacterial Succinate-Acetate Transporter (AceTr Family)

## Overview

SatP (also known as yaaH) is a member of the  uptake transporter (AceTr) family
(TC 2.A.96) from *Escherichia coli*. It functions as a -/proton symporter
and forms a hexameric UreI-like channel structure. The crystal structure of ecSatP was
determined at 2.8 Å resolution using [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with a predicted model from
Baker's group. Each protomer contains six transmembrane (TM) helices surrounding a
central channel pore, with three conserved hydrophobic residues (F17, Y72, L131 — the
"FLY" motif) forming a constriction site in the TM region. Single-channel conductance
recordings of purified ecSatP reconstituted into lipid bilayers demonstrated a conductance
of 1.2 ± 0.34 nS with bidirectional channel activity and substrate selectivity for
carboxylates and chloride. Three conserved polar residues in TM1 (T21, N25, N28) were
shown to be critical for  translocation activity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1074##jbc.RA118.003876 | 5ZUG | 2.80 | P3_2 | Full-length ecSatP (residues 1-182) |  |

## Expression and Purification

- **Expression system**: E. coli C43 (DE3)
- **Construct**: Full-length ecSatP in modified pET15b vector with DrICE cutting site
- **Notes**: Cells induced with 0.2 mM  at 22 °C overnight

### Purification Workflow

- **Expression system**: E. coli C43 (DE3)
- **Expression construct**: Full-length ecSatP with N-terminal 6×His tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | 1% (w/v)  + 1 mM , 1.5 h at 4 °C | — |  | Ultracentrifugation at 150,000×g for 30 min to remove insoluble fraction |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA resin | — |  | Eluted with 270 mM  in 25 mM  pH 7.0, 150 mM NaCl, 0.05%  |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) Increase 10/300 | — | 25 mM  pH 7.0, 150 mM NaCl, 0.05% (w/v)  | N-terminal His tag removed using DrICE prior to crystallization |


## Crystallization

### doi/10.1074##jbc.RA118.003876

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | ecSatP in 25 mM  pH 8.0, 150 mM NaCl, 0.4% (w/v) beta-NG |
| Reservoir | 0.05 M  pH 9.8, 27% (v/v) , 0.1 M NaCl with 0.15 mM n-nonyl-beta-D-thioglucoside |
| Temperature | 18 |
| Growth time | 2-4 days |
| Cryoprotection | Dehydration by adding  to 40% (v/v) over 24 h |
| Notes | Hexagonal-shaped crystals. Additive screening with n-nonyl-beta-D-thioglucoside improved diffraction. Dehydration trials critical for reaching 2.8 Å resolution. |


## Biological / Functional Insights

### Hexameric channel architecture of AceTr family

The ecSatP structure reveals a hexameric arrangement forming a compact cylinder
(~95 Å diameter, ~45 Å height) with a central pore occupied by lipid/detergent.
The protomer serves as the functional unit with six TM helices forming an
hourglass-shaped channel. This architecture is similar to the  channel UreI
but with reverse topology (N/C termini cytoplasmic vs periplasmic in UreI).

### FLY constriction gate and substrate selectivity

Three conserved hydrophobic residues (F17, Y72, L131) form a constriction site
narrowing to ~0.8 Å in the closed state. The "FLY" motif is highly conserved
in the AceTr family. Mutations at L131 (corresponding to L131V) alter substrate
specificity, suggesting the constriction site contributes to substrate selectivity.

### Substrate recognition by TM1 polar residues

Three conserved polar residues in TM1 (T21, N25, N28) on the periplasmic side
are critical for  translocation. Single-channel conductance assays of
T21A and N25A mutants showed reduced substrate blockade frequency compared to
wild-type, with N28A failing to form functional channels, demonstrating their
essential role in substrate recognition and transport.

### Channel-like mechanism vs. transporter

Single-channel conductance measurements (~10^7 ions/s, 1.2 nS conductance)
combined with the channel-like structure suggest ecSatP functions as an 
channel rather than a classical transporter, despite the AceTr family being
annotated as transporters. The bidirectional permeation observed contrasts with
the unidirectional transport reported for the close homolog ckSatP.


## Cross-References

- [Succinate](/xray-mp-wiki/reagents/ligands/succinate/) — Referenced in ecsatp text
- [Acetate](/xray-mp-wiki/reagents/buffers/acetate/) — Referenced in ecsatp text
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in ecsatp text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in ecsatp text
- [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/) — Referenced in ecsatp text
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in ecsatp text
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in ecsatp text
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in ecsatp text
- [PEG300](/xray-mp-wiki/reagents/additives/peg300/) — Referenced in ecsatp text
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Referenced in ecsatp text
