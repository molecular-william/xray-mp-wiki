---
title: Krokinobacter eikastus Rhodopsin 2 (KR2) — Light-Driven Sodium Pump
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [pump, transporter, membrane-protein]
sources: [doi/10.1038##s41586-020-2307-8]
verified: false
---

# Krokinobacter eikastus Rhodopsin 2 (KR2) — Light-Driven Sodium Pump

## Overview

Krokinobacter eikastus rhodopsin 2 (KR2) is a prototypical light-driven sodium pump from marine bacteria that actively transports small cations across cellular membranes. It converts light into membrane potential and has become a valuable optogenetic tool for neuronal inhibition. Using time-resolved serial femtosecond crystallography (TR-SFX) at SwissFEL, structural snapshots spanning from femtoseconds to milliseconds (10 time delays: 800 fs to 20 ms) were collected at up to 1.6 Å resolution, revealing how retinal isomerization drives sodium translocation against a concentration gradient. Resting state structures were determined at both acidic pH (PDB 6TK7) and neutral pH (PDB 6TK6). Five intermediate structures at combined time delays (800 fs+2 ps — 6TK5; 1 ns+16 ns — 6TK4; 30 µs+150 µs — 6TK3; 1 ms — 6TK2; 20 ms — 6TK1) show the stepwise mechanism: retinal isomerization within femtoseconds, structural rearrangements via V117 in helix C at microseconds, transient sodium binding between N112 and D251 at 1 ms, and a second sodium-binding site near E11/N106/E160 at 20 ms on the extracellular side.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-020-2307-8 | 6TK7 | 1.60 | I4 | Full-length KR2 with C-terminal 6×His tag (TEV-cleavable) | All-trans retinal, sodium ions |
| doi/10.1038##s41586-020-2307-8 | 6TK6 | 1.60 | I4 | Full-length KR2 with C-terminal 6×His tag (TEV-cleavable) | All-trans retinal, sodium ions |
| doi/10.1038##s41586-020-2307-8 | 6TK5 | 2.25 | I4 | Full-length KR2 with C-terminal 6×His tag (TEV-cleavable) | 13-cis retinal, sodium ions |
| doi/10.1038##s41586-020-2307-8 | 6TK4 | 2.25 | I4 | Full-length KR2 with C-terminal 6×His tag (TEV-cleavable) | 13-cis retinal, sodium ions |
| doi/10.1038##s41586-020-2307-8 | 6TK3 | 2.25 | I4 | Full-length KR2 with C-terminal 6×His tag (TEV-cleavable) | 13-cis retinal, sodium ions |
| doi/10.1038##s41586-020-2307-8 | 6TK2 | 2.50 | I4 | Full-length KR2 with C-terminal 6×His tag (TEV-cleavable) | 13-cis retinal, sodium (transient binding site near N112/D251) |
| doi/10.1038##s41586-020-2307-8 | 6TK1 | 2.50 | I4 | Full-length KR2 with C-terminal 6×His tag (TEV-cleavable) | 13-cis retinal, sodium (second binding site near E11/N106/E160) |

## Expression and Purification

- **Expression system**: C41(DE3) Escherichia coli cells (pStaby1.2 vector)
- **Construct**: Full-length KR2 gene with TEV-cleavable C-terminal 6×His tag; expression with 10 µM all-trans retinal at 37°C overnight

### Purification Workflow

*Source: doi/10.1038##s41586-020-2307-8*

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Membrane preparation | Homogenization and ultracentrifugation | — | 20 mM Tris pH 8.0, 5% glycerol, 0.5% Triton X-100, DNase I | Cells disrupted at 15,000 psi; membranes collected at 90,000g |
| 2. Membrane solubilization | DDM/CHS extraction | — | 50 mM Tris pH 8.0, 300 mM NaCl, 1.0% DDM, 0.2% CHS | Overnight stirring at 4°C |
| 3. Immobilized metal affinity chromatography (IMAC) | Ni-NTA resin | — | 50 mM Tris pH 8.0, 150 mM NaCl, 100-500 mM imidazole, 0.02% DDM, 0.04% CHS | Eluted with 500 mM imidazole step gradient |
| 4. TEV cleavage and dialysis | TEV protease + dialysis | — | 50 mM Tris pH 8.0, 150 mM NaCl, 0.02% DDM, 0.04% CHS | Overnight dialysis in 8 kDa MWCO membrane |
| 5. Reverse IMAC | Ni-NTA flow-through | — | — | Cleaved His tag removed; flow-through collected |
| 6. Size-exclusion chromatography | HiLoad Superdex 75 prep grade 16/600 | — | 20 mM Tris pH 8.0, 150 mM NaCl, 0.02% DDM, 0.04% CHS | Final purification step |

## Crystallization

### doi/10.1038##s41586-020-2307-8

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified KR2 in 20 mM Tris pH 8.0, 150 mM NaCl, 0.02% DDM, 0.04% CHS |
| Reservoir | 200 mM sodium acetate pH 4.4, 150 mM MgCl2, 35% PEG 200 |
| Temperature | 20°C (overnight in dark) |
| Notes | LCP formed with monoolein at 4:7 v/v (protein:lipid). Blue plate-like crystals 10-30 × 10-25 × 1-3 µm³. Crystals treated by washing with 150 mM NaCl, 35% PEG 200 for neutral pH experiments. TR-SFX data collected at SwissFEL; 158,832 dark and 496,904 light patterns analyzed. Data processed with CrystFEL, structures refined in PHENIX. |

## Biological / Functional Insights

### Retinal isomerization drives the photocycle

Retinal isomerization from all-trans to 13-cis is completed within femtoseconds. The isomerized retinal in KR2 points in the opposite direction compared to bacteriorhodopsin (bR): the C20 methyl group tilts towards helix C (via V117) instead of helix G (via W182 in bR). This early event translates light energy into structural changes in the protein.

### Electrostatic gating mechanism for unidirectional sodium transport

After retinal Schiff base (SB) deprotonation in the M intermediate, an electrostatic gate opens in microseconds. The proton transfer from SB to counterion D116 creates a transient sodium-binding site. At 1 ms, sodium binds between N112 and D251 (confirmed by QM/MM calculations showing the sodium ion produces a 55-66 nm red shift matching the O intermediate absorption maximum at 592 nm). At 20 ms, a second sodium-binding site appears between E11, N106, and E160 near the extracellular exit. Reprotonation of the SB blocks backflow, ensuring unidirectional transport.

### V117 as the key mechanical transducer

Unlike bR where W182 in helix F mediates force transmission, KR2 uses V117 in helix C as the primary mechanical transducer. Starting at 1 µs, the retinal C20 methyl group pushes sideways against V117, causing a flip that propagates structural changes into helix C and the helical bundle. This represents a distinct mechanism for coupling retinal isomerization to protein conformational change.

### Sodium translocation pathway and gating

The program Caver identified a putative sodium translocation pathway across the membrane. A rotamer change of R109 and Q78, together with a shift of helix D at 20 ms, opens a connection between the retinal-proximal water-filled cavity and a second cavity near E11/N106/E160/R243 towards the extracellular exit. R109 corresponds to R82 in bR (critical for proton transfer), suggesting conserved functional sites across rhodopsin families.

## Cross-References
