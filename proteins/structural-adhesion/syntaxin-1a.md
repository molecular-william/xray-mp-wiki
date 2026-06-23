---
title: Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08156]
verified: false
---

# Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)

## Overview

Syntaxin-1A is a neuronal Qa-SNARE protein from rat that plays a central role in neurotransmitter release at synaptic terminals. It is a single-pass transmembrane protein containing an N-terminal Habc domain, a SNARE motif, a linker region, and a C-terminal transmembrane domain. In the synaptic terminal, syntaxin-1A assembles with SNAP-25 and [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) into a four-helix bundle [SNARE Complex](/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/) that drives synaptic vesicle fusion with the plasma membrane. The X-ray structure of the syntaxin-1A SNARE motif with linkers and transmembrane region revealed continuous helical extension from the SNARE core through the linker into the membrane.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature08156 | TBA | 3.4 A | C2 | Rat syntaxin-1A residues 183-288 (SNARE motif, linker, transmembrane region) | None |
| doi/10.1038##nature08156 | TBA | 4.3 A | TBA | Selenomethionine-labelled rat syntaxin-1A residues 183-288 (for SAD phasing) | None |

## Expression and Purification

- **Expression system**: Escherichia coli BI21 (DE3)
- **Construct**: Rat syntaxin-1A (residues 180-262 and 183-288) with N-terminal His-tag, expressed from pET28a

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Expression in E. coli BI21 (DE3) from pET28a | -- | -- + -- | His-tagged syntaxin-1A expressed separately |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA agarose | -- + -- | Initial purification of His-tagged syntaxin-1A |
| Tag cleavage and desalting | Tag removal and desalting | HiPrep 26/10 Desalting column | 20 mM Tris pH 8.8, 500 mM NaCl, 50 mM n-octyl beta-D-glucopyranoside, 1 mM TCEP + n-octyl beta-D-glucopyranoside | Tags removed, desalted after Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) |
| Ion-exchange chromatography | Ion-exchange chromatography | Not specified | 20 mM Tris pH 8.8, 500 mM NaCl, 50 mM n-octyl beta-D-glucopyranoside + n-octyl beta-D-glucopyranoside | Further purification by ion exchange |
| Complex assembly | In vitro complex assembly | -- | Assembled by overnight incubation of monomers at 4 C + -- | Syntaxin-1A used as limiting component in complex assembly with [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) and [SNAP-25A (Rat Neuronal Qbc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/snap-25a/) |


## Crystallization

### doi/10.1038##nature08156

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Syntaxin-1A/SNAP-25/synaptobrevin-2 complex with linkers and TMRs in n-nonyl beta-D-glucopyranoside |
| Reservoir | Not specified in main text |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | C2 space group, diffracted to 3.4 A. Also solved SAD structure with SeMet-syntaxin-1A at 4.3 A resolution. Data collected at X10SA beamline, Swiss Light Source. Phases obtained by single-wavelength anomalous dispersion (SAD). |


## Biological / Functional Insights

### Continuous helical extension into the membrane

Syntaxin-1A forms a continuous alpha-helix throughout its SNARE motif, linker region, and transmembrane region. This helical continuity extends the known four-helix core [SNARE Complex](/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/) into the membrane, suggesting that the final phase of SNARE assembly is directly coupled to membrane merger.

### Aromatic layer stabilizes linker region

The linker region contains a collar of aromatic residues surrounded predominantly by basic residues. Tyr 257 is deeply buried in a pocket formed by three flanking lysine residues of syntaxin-1A (Lys 253, Lys 256, Lys 260) and four residues of [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) (Lys 85, Arg 86, Trp 89, Asn 92). Mutation of Tyr 257 to alanine reduced thermal stability, demonstrating that intermolecular side-chain contacts in the aromatic layer are crucial for complex stability.

### Transmembrane region interactions drive complex association

In the crystal, hydrophobic contacts between the transmembrane regions of [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) and syntaxin-1A mediate the association of four complexes through their TMRs, forming an X-shaped assembly. Four [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) TMRs build the core, surrounded by four syntaxin-1A TMRs. Residues Ile 268, Cys 271, Ile 274, and Leu 275 in syntaxin-1A contribute largely to the interaction surface with [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) TMRs.

### Linkers and TMRs add thermal stability

The complex including linkers and TMRs of syntaxin-1A and [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) was significantly more resistant to thermal and chemical denaturation than the core complex alone. The crystallization complex unfolded at approximately 97 C in CD spectroscopy thermal unfolding experiments. Presence of syntaxin-1A TMR alone provided stability comparable to the core complex.


## Cross-References

- [Synaptobrevin-2 (Rat Neuronal Qb-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) — Core SNARE complex partner; forms continuous helical bundle with syntaxin-1A through SNARE motif, linker, and TMR
- [SNAP-25A (Rat Neuronal Qbc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/snap-25a/) — Third component of the neuronal SNARE complex; anchors to plasma membrane via palmitoyl chains
- [Tlg2 (Cryptococcus thermophilum Qa-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/tlg2/) — Homologous Qa-SNARE protein from endosomal system; also has Habc domain and SNARE motif
- [Nonylglucoside (NG)](/xray-mp-wiki/reagents/detergents/nonylglucoside/) — n-nonyl beta-D-glucopyranoside used as detergent for crystallization of SNARE complex
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — n-octyl beta-D-glucopyranoside used in purification buffer (50 mM) for syntaxin-1A
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — 20 mM Tris pH 8.8 used in desalting and ion exchange purification buffer
- [Tris-(2-carboxyethyl)phosphine (TCEP)](/xray-mp-wiki/reagents/additives/tcep/) — 1 mM TCEP used in desalting buffer for syntaxin-1A purification
- [SNARE Complex](/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/) — Syntaxin-1A is the Qa-SNARE component of the four-helix bundle SNARE complex
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
