---
title: "MjCorA — CorA Mg2+ Transporter from Methanocaldococcus jannaschii"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, channel, membrane-protein]
sources: [doi/10.1073##pnas.1210076109]
verified: false
---

# MjCorA — CorA Mg2+ Transporter from Methanocaldococcus jannaschii

## Overview

CorA is the primary Mg2+ transport system in most prokaryotes and is conserved throughout the CorA family including eukaryotic homologs. The structure of MjCorA from Methanocaldococcus jannaschii was determined at 3.2 Å resolution, revealing the complete architecture including the conserved extraplasmic loop containing the signature GMN motif that functions as a selectivity filter. The structure shows a pentameric arrangement with two transmembrane helices per monomer. Polar residues facing the channel coordinate a partially hydrated Mg2+ during transport. A unique gating mechanism is proposed involving a helical turn upon Mg2+ binding to regulatory intracellular binding sites, converting a polar ion passage into a narrow hydrophobic pore.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1210076109 | not in raw text | 3.20 | — | Full-length MjCorA | Mg2+ |

## Expression and Purification

- **Expression system**: Heterologous expression in Escherichia coli (strain not specified)


### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein purification | Standard purification (details in SI) | — | HEPES-NaOH buffer with MgCl2 + Dodecyl-maltoside | Full-length MjCorA purified in solubilization buffer containing dodecyl-maltoside |


## Crystallization

### doi/10.1073##pnas.1210076109

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Full-length MjCorA in solubilization buffer |
| Reservoir | 30% PEG8000, HEPES-NaOH, 60 mM MgCl2 |
| Notes | Crystallized in 30% PEG8000, HEPES-NaOH, 60 mM MgCl2 |


## Biological / Functional Insights

### GMN motif as selectivity filter

The conserved GMN (Gly-Met-Asn) motif in the extraplasmic loop forms
the selectivity filter of CorA. The Asn280 ring (N280-ring) creates a
narrow entry that allows only partially hydrated Mg2+ to pass. The
carbonyl groups of Gly278 attract ions, while Met279 anchors the
filter in a hydrophobic environment. The YGMNF and LPLA motifs create
a rigid scaffold maintaining the Asn-ring position. This arrangement
explains the strict conservation of the GMN motif across all CorA
family members including eukaryotic homologs.

### Helical turn gating mechanism

A unique gating mechanism is proposed where Mg2+ binding to
intracellular regulatory sites (the Mg2+-binding grooves at monomer
interfaces) induces a clockwise helical turn of helix 6. This
rotation moves polar residues away from the pore and replaces them
with hydrophobic residues, blocking the passage. In the open state,
the pore is polar and allows partially hydrated Mg2+ passage. The
gating converts a polar ion passage into a narrow hydrophobic pore
rather than using the iris-like sideways movement previously proposed
for TmCorA.

### Mg2+ transport as partially hydrated ion

The structure reveals that Mg2+ is taken up and transported as a
partially hydrated ion. The Asn280-ring replaces water molecules in
the second hydration shell. A wide internal cavity (~23 Å long)
allows the ion to potentially return to fully hydrated state after
passing the selectivity filter. The filter discriminates against
Ca2+ and Mn2+ based on differences in first hydration shell radii,
while allowing Mg2+, Co2+, and Ni2+ which have similar radii
(~2.05-2.1 Å).


## Cross-References

- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
