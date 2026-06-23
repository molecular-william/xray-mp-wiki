---
title: ABCG1
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2022.167795]
verified: false
---

# ABCG1

## Overview

ABCG1 is a member of the ATP-binding cassette (ABC) G subfamily of lipid transporter proteins. It functions as a homodimeric floppase that translocates [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) within the plasma membrane and in endosomes, playing a key role in regulating cholesterol balance in the lung, the brain, and in macrophage-rich tissues. ABCG1 redistributes cell cholesterol to domains removable by high-density lipoproteins and is involved in reverse cholesterol transport. The phenylalanine at position F455 (F4 of the phenylalanine highway) is critical for ABCG1 function, with F455A mutation inhibiting ATPase activity. ABCG1 shows distinct sterol binding patterns compared to ABCG5/G8, with sterols clustering closer to the central cavity around PH's F4 position.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2022.167795 | 7OZ1 | not specified | not specified | Human ABCG1 homodimer (AlphaFold2 model, pLDDT > 90) | None |
| doi/10.1016##j.jmb.2022.167795 | 7R8D | not specified | not specified | Human ABCG1 homodimer (nucleotide-free structure) | None |
| doi/10.1016##j.jmb.2022.167795 | 7R8E | not specified | not specified | Human ABCG1 homodimer ([ATP](/xray-mp-wiki/reagents/ligands/atp)-bound structure) | [ATP](/xray-mp-wiki/reagents/ligands/atp) |

## Expression and Purification

- **Expression system**: Not specified
- **Construct**: Human ABCG1 homodimer; AlphaFold2 predictions used for modeling

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Not specified | Not specified | -- | Not specified + Not specified | ABCG1 structures from PDB used for molecular docking analysis; purification details not reported in this paper |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Sterol binding at cytoplasmic end of TMD

Unlike ABCG5/G8 which binds sterols at the membrane-transporter interface, ABCG1 sterol binding occurs at the cytoplasmic end of the transmembrane domain. Cholesterol and [Stigmasterol](/xray-mp-wiki/reagents/lipids/stigmasterol) cluster around F455 (F4 of the phenylalanine highway) in an increasingly linear shape, with the sterol cloud angled towards the putative sterol binding cavity at the NBD-TMD interface in the membrane's lower leaflet. Both sterols show similar binding conformations on both sides of the transporter-membrane interface, unlike the asymmetric binding observed for ABCG5/G8.

### Lower transmembrane sterol-binding cavity

ABCG1 has a wider transmembrane sterol-binding cavity compared to [ABCG5/G8](/xray-mp-wiki/proteins/abcg5). The equivalent residues to ABCG5_Y432 and ABCG8_N564 in ABCG1 are F455 and P558, separated by 6.9 A compared to the 4.0 A separation in ABCG5/G8. This wider cavity allows sterols to bind deeper within the transmembrane domain. Mutating ABCG5/Y432 and ABCG8/N564 to F/P to mimic ABCG1 widens the cavity but does not fully reproduce ABCG1 binding patterns, suggesting multiple conformations during the transport cycle.

### Phenylalanine highway F455 critical for function

The phenylalanine at position F455 (F4 of the PH) in ABCG1 is critical for transporter function. The F455A mutation inhibits ATPase activity, indicating that the aromatic side chain at this position participates in substrate binding or catalysis. The lower PH terminus may serve as a molecular clamp for substrates, similar to the role observed in [ABCG2](/xray-mp-wiki/proteins/abcg2).

### Sterol selectivity compared to ABCG5/G8

ABCG1 shows similar binding conformations for both cholesterol and [Stigmasterol](/xray-mp-wiki/reagents/lipids/stigmasterol), with a decreased amount of stigmasterol binding poses compared to ABCG5/G8. In contrast, ABCG5/G8 displays distinct selectivity for plant sterols (stigmasterol) with preferred association of different sterol species on either side of the transporter-membrane interface. This suggests that sterol selectivity differentiates ABCG5/G8 from other ABCG sterol transporters.


## Cross-References

- [ABCG5](/xray-mp-wiki/proteins/abc-transporters/abcg5/) — [ABCG5/G8](/xray-mp-wiki/proteins/abcg5) heterodimer; extensively compared for sterol binding patterns and PH motif
- [ABCG8](/xray-mp-wiki/proteins/abc-transporters/abcg8/) — [ABCG5/G8](/xray-mp-wiki/proteins/abcg5) heterodimer; cavity width comparison (ABCG1 F455/P558 vs ABCG5_Y432/ABCG8_N564)
- [ABCG2](/xray-mp-wiki/proteins/abc-transporters/abcg2/) — Multidrug transporter ABCG member; shares PH motif and hydrophobic valve
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Substrate; binds at cytoplasmic end of TMD in ABCG1
- [Stigmasterol](/xray-mp-wiki/reagents/lipids/stigmasterol/) — Plant sterol substrate; docked on ABCG1 for selectivity comparison
- [Membrane Mimetics and Structural Biology](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics) — Bicelles, nanodiscs, and other membrane mimetics used in membrane protein studies
- [Atp](/xray-mp-wiki/reagents/ligands/atp) — Ligand or small molecule used in this study
