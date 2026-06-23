---
title: "Syntaxin17 (STX17)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, receptor]
sources: [doi/10.1073##pnas.2006997117]
verified: false
---

# Syntaxin17 (STX17)

## Overview

Syntaxin17 (STX17) is a key autophagosomal Qa-SNARE protein essential for autophagosome-lysosome
fusion in mammalian macroautophagy. It contains an N-terminal Habc domain, a Qa-SNARE motif,
and two C-terminal transmembrane domains that form a hairpin structure for autophagosome localization.
STX17 coassembles with [SNAP29 (Synaptosomal-Associated Protein 29)](/xray-mp-wiki/proteins/structural-adhesion/snap29/) (Qb/Qc-SNARE) and [VAMP8 (Vesicle-Associated Membrane Protein 8)](/xray-mp-wiki/proteins/structural-adhesion/vamp8/) (R-SNARE) to form the autophagic SNARE core
complex that mediates membrane fusion. The Qa-SNARE motif of STX17 also contains a functional
LC3-interacting region (LIR) motif that preferentially binds [GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/) subfamily members. Binding of
[GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/) to the LIR motif releases STX17 from its autoinhibited conformation. The crystal structure
of the STX17-SNAP29-[VAMP8 (Vesicle-Associated Membrane Protein 8)](/xray-mp-wiki/proteins/structural-adhesion/vamp8/) SNARE core complex was determined at 2.0 A resolution, revealing a
canonical four-helix bundle with 16 hydrophobic layers and a conserved hydrophilic 0 layer.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.2006997117 | 7BV6 | 2.0 |  | STX17 LIR motif (residues 167-188) in complex with [GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/) | none |
| doi/10.1073##pnas.2006997117 | 7BV6 |  |  | STX17 (residues 142-228), [SNAP29 (Synaptosomal-Associated Protein 29)](/xray-mp-wiki/proteins/structural-adhesion/snap29/) (residues 40-126, 191-258), [VAMP8 (Vesicle-Associated Membrane Protein 8)](/xray-mp-wiki/proteins/structural-adhesion/vamp8/) (residues 8-75) SNARE core complex | none |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Human STX17, [SNAP29 (Synaptosomal-Associated Protein 29)](/xray-mp-wiki/proteins/structural-adhesion/snap29/), [VAMP8 (Vesicle-Associated Membrane Protein 8)](/xray-mp-wiki/proteins/structural-adhesion/vamp8/), and ATG8s expressed as recombinant proteins with various affinity tags
- **Notes**: Proteins expressed using in-house modified pET32a vectors. Induced with 100 uM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 16 C.

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### STX17 adopts an autoinhibited closed conformation

NMR titration experiments revealed that the STX17 Qa-SNARE motif (residues 142-228) directly
binds to its N-terminal Habc domain (residues 1-123), inducing partial unfolding of the extreme
C-terminal alpha-helix of the Habc domain. This intramolecular interaction keeps STX17 in an
autoinhibited closed conformation, similar to Syntaxin1 but with the notable difference that
STX17 SNARE motif binding unfolds part of the Habc domain.

### The STX17 Qa-SNARE region contains one functional LIR motif

NMR chemical shift perturbation and [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) binding studies revealed that STX17 contains a single
functional LIR motif (LC3-interacting region) with core sequence 172WETL175 within its
Qa-SNARE region. The second putative LIR motif (189FSLL192) does not contribute to ATG8 binding.
STX17 preferentially binds [GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/) subfamily members (Kd ~4-10 uM) over LC3 subfamily members
(Kd ~22-97 uM). Mutation of W172Q completely abolishes [GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/) binding.

### GABARAP binding relieves STX17 autoinhibition

NMR experiments showed that addition of [GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/) to the STX17 Habc:Qa-[SNARE Complex](/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/) releases
the autoinhibited conformation. [GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/) binds to the LIR motif within the Qa-SNARE region,
competing with the Habc domain and freeing the SNARE motif for assembly with [SNAP29 (Synaptosomal-Associated Protein 29)](/xray-mp-wiki/proteins/structural-adhesion/snap29/) and [VAMP8 (Vesicle-Associated Membrane Protein 8)](/xray-mp-wiki/proteins/structural-adhesion/vamp8/).
This provides a regulatory mechanism where ATG8 family proteins (particularly GABARAPs)
recruit and activate STX17 at the autophagosome surface.

### Unconventional extended LIR motif with C-terminal 310-helix

The crystal structure of the STX17 LIR-[GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/) complex at 2.0 A resolution revealed an
unconventional LIR motif with a C-terminally extended 310-helix following the canonical
WETL core. This extension packs extensively with a solvent-exposed groove formed by the
alpha1, alpha2, and alpha3 helices and beta2-strand of [GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/). The extended interaction
explains both the high affinity and [GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/) selectivity of STX17 binding. Key interface
residues include E170, W172, D178, and L179 of STX17, and K47, K48, L55, L63, K66, and R67
of [GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/).

### Autophagic SNARE core complex structure

The crystal structure of the STX17-SNAP29-[VAMP8 (Vesicle-Associated Membrane Protein 8)](/xray-mp-wiki/proteins/structural-adhesion/vamp8/) SNARE core complex reveals a canonical
four-helix bundle with all four helices aligned in parallel. The interior is formed by
16 layers of interacting side chains (mostly hydrophobic), with a hydrophilic 0-layer
consisting of Q196 (STX17), Q84/Q230 ([SNAP29 (Synaptosomal-Associated Protein 29)](/xray-mp-wiki/proteins/structural-adhesion/snap29/)), and R37 ([VAMP8 (Vesicle-Associated Membrane Protein 8)](/xray-mp-wiki/proteins/structural-adhesion/vamp8/)). Mutagenesis showed that
the N-terminal and central layers (especially -7th, -5th, and 0th) are critical for complex
assembly. The [SNARE Complex](/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/) has a melting temperature of ~85 C and shows characteristic
unfolding-refolding hysteresis. Two highly negatively charged patches on the surface are
implicated in NSF-mediated [SNARE Complex](/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/) disassembly.


## Cross-References

- [GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein)](/xray-mp-wiki/proteins/structural-adhesion/gabarap/) — GABARAP binds STX17 LIR motif and relieves autoinhibition
- [SNAP29 (Synaptosomal-Associated Protein 29)](/xray-mp-wiki/proteins/structural-adhesion/snap29/) — SNAP29 contributes Qb- and Qc-SNARE motifs to the autophagic SNARE complex
- [VAMP8 (Vesicle-Associated Membrane Protein 8)](/xray-mp-wiki/proteins/structural-adhesion/vamp8/) — VAMP8 contributes the R-SNARE motif to the autophagic SNARE complex
- [Autophagic SNARE Fusion Mechanism](/xray-mp-wiki/concepts/construct-design/autophagic-snare-fusion-mechanism/) — STX17 is the central Qa-SNARE in this mechanism
- [SNARE Complex](/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/) — Related biological concept
- [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
