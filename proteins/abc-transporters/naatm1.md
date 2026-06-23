---
title: "NaAtm1 ABC Exporter from Novosphingobium aromaticivorans"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, pump, membrane-protein]
sources: [doi/10.1073##pnas.2006526117, doi/10.1126##science.1246489]
verified: false
---

# NaAtm1 ABC Exporter from Novosphingobium aromaticivorans

## Overview

NaAtm1 is an Atm1/ABCB7/HMT1/ABCB6-family ABC exporter from the Gram-negative bacterium *Novosphingobium aromaticivorans* DSM 12444. An initial 2.4 Å inward-facing structure (2014) was followed by eight additional structures (2020) determined by X-ray crystallography and [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) across the transport cycle, revealing a TM6 kinking mechanism that enforces export directionality. The structure was solved at 2.4 Å resolution in an inward-facing conformation, revealing the molecular basis for substrate recognition and heavy metal detoxification by this family of ABC transporters. NaAtm1 shares ~45% sequence identity with *Saccharomyces cerevisiae* Atm1, human ABCB7, and HMT-1, making it a useful model for eukaryotic transporters of this family. Functional studies demonstrate that [GSH](/xray-mp-wiki/reagents/additives/glutathione/) ([GSH](/xray-mp-wiki/reagents/additives/glutathione/)) derivatives, including metallated and oxidized [GSH](/xray-mp-wiki/reagents/additives/glutathione/) (GSSG), serve as substrates, and overexpression of NaAtm1 in *Escherichia coli* confers protection against silver and [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) toxicity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.2006526117 | 6PAM | 3.7 |  | NaA527C mutant with MgADP (state | MgADP |
| doi/10.1073##pnas.2006526117 | 6PAM | 3.7 |  | NaA527C mutant with MgADP (state | MgADP |
| doi/10.1073##pnas.2006526117 | 6PAM | 3.4 |  | NaS526C mutant with ATP | ATP |
| doi/10.1073##pnas.2006526117 | 6PAM | 3.4 |  | NaT525C mutant with ATP | ATP |
| doi/10.1073##pnas.2006526117 | 6PAM | 3.3 |  | NaE523Q (Walker-B mutant) with ATP | ATP |
| doi/10.1073##pnas.2006526117 | 6PAM |  |  | Wild-type NaAtm1 with MgAMPPNP | MgAMPPNP |
| doi/10.1073##pnas.2006526117 | 6PAM |  |  | Wild-type NaAtm1 with MgADPVO4 ([Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/)) | MgADPVO4, [POPC](/xray-mp-wiki/reagents/lipids/popc/) nanodisc |
| doi/10.1073##pnas.2006526117 | 6PAM |  |  | Wild-type NaAtm1 wide-open inward-facing ([Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/)) | [POPC](/xray-mp-wiki/reagents/lipids/popc/) nanodisc |
| doi/10.1126##science.1246489 | 4MRN | 2.40 | — | Full-length NaAtm1 | GSSG |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Full-length NaAtm1
- **Notes**: Overexpressed in E. coli for functional studies; purification details in Supporting Online Material

### Purification Workflow

- **Expression system**: E. coli

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — |  | Full details in Supporting Online Material; protein purified for crystallographic and functional studies |

**Final sample**: Purified NaAtm1 for crystallization and ATPase assays


## Crystallization

### doi/10.1126##science.1246489

| Parameter | Value |
|---|---|
| Method | — |
| Temperature | — |
| Notes | Crystallization details in Supporting Online Material. Structure determined at 2.4 Å resolution. |


## Biological / Functional Insights

### GSH/GSSG Binding Site Architecture

The primary GSSG binding site is located ~5 Å into the transmembrane region, dominated by interactions from helices TM5 and TM6 and accessible from the cytoplasmic side. Key interactions include hydrogen bonds between the α-carboxyl group of γ-Glu and the amide NHs of Gly319 and Met320 in TM6 and the side chain of Gln272 (TM5). The α-amino group of Glu interacts with the peptide carbonyl of Asp316 (TM6) and side chains of Asn269 and Gln272. A second, lower-occupancy binding site is positioned ~5 Å toward the cytoplasmic surface, involving conserved arginine residues 206, 210, and 323.

### Heavy Metal Detoxification Mechanism

NaAtm1 mediates resistance to silver (Ag⁺) and [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) (Hg²⁺) toxicity through export of metallated [GSH](/xray-mp-wiki/reagents/additives/glutathione/) complexes. The greatest stimulation of ATP hydrolysis was observed for Ag- and Hg-[GSH](/xray-mp-wiki/reagents/additives/glutathione/) complexes. Expression of NaAtm1 in metal-sensitive E. coli strains conferred protection against otherwise toxic concentrations of these metals, consistent with a physiological role in cellular detoxification of heavy metals.

### Articulated Design of ABC Exporters

Structural comparisons of NaAtm1 with other ABC exporters ([Sav1866 Multidrug ABC Transporter](/xray-mp-wiki/proteins/abc-transporters/sav1866/), TM287/288, [Human ABCB10 Mitochondrial ATP-Binding Cassette Transporter](/xray-mp-wiki/proteins/abc-transporters/abcb10/), mouse Pgp, C. elegans Pgp, [MSBA](/xray-mp-wiki/proteins/abc-transporters/msba/)) reveal four conserved structural elements: TM1-2, TM3&6, and TM4-5. Although individual elements are structurally conserved, substantial changes in their relative orientations are observed between inward- and outward-facing conformations. The GSSG binding site spans between these elements, coupling ligand binding to conformational rearrangements during the transport cycle.

### Mutational Analysis of Substrate Coupling

Residues Asn269, Gln272, and Gly319 form hydrogen bonds to the α-amino and carboxylate groups of the γ-Glu moiety of [GSH](/xray-mp-wiki/reagents/additives/glutathione/) and are highly conserved. Substitution of these residues alters ATPase activity and eliminates [GSH](/xray-mp-wiki/reagents/additives/glutathione/) stimulation. The Tyr195→Phe variant exhibits substrate-insensitive ATPase hyperactivity, suggesting the native Tyr195 contact to TM6 stabilizes the inward-facing conformation. The Gln272→Ala variant is essentially ATPase-inactive, indicating this residue may be required to unlock the protein from the cytoplasm-facing conformation.

### TM6 kinking regulates glutathione binding and export directionality

Eight structures across the transport cycle reveal that TM6 kinking controls substrate
binding and enforces export directionality. In inward-facing states, kinked TM6 (adjacent
to a 310 helix at residues 314-317) creates a GSSG binding site. In occluded prehydrolysis
states, TM6 straightens, restructuring the binding site for substrate release. In the
posthydrolysis MgADPVO4 state, kinked TM6 eliminates the substrate-binding cavity entirely
(< 740 A3, insufficient for GSSG), preventing re-binding during the return stroke.

### Disulfide-crosslinked NaAtm1 retains transport activity

NaS526C retained ~60% of wild-type transport activity (0.9 nmol GSSG/min/mg), demonstrating
that ATP hydrolysis and substrate transport may involve limited conformational states without
wide NBD separation. NaT525C retained ~30% activity; NaA527C and NaE523Q showed ~10%.

### Cavity volume dynamics across transport states

Cavity volumes (CastP, 2.5 A probe): wide-open inward-facing ~2800 A3, inward-facing ~1600 A3,
inward-occluded ~1900-2000 A3, occluded ~1100-1500 A3. The MgADPVO4 posthydrolysis state
lacks a viable cavity (< 740 A3 vs ~740 A3 for GSSG), preventing substrate binding during reset.


## Cross-References

- [Yeast Mitochondrial ABC Transporter Atm1](/xray-mp-wiki/proteins/abc-transporters/yeast-atm1/) — Closest structurally characterized eukaryotic homolog; companion paper in same Science issue
- [Human ABCB10 Mitochondrial ATP-Binding Cassette Transporter](/xray-mp-wiki/proteins/abc-transporters/abcb10/) — Related eukaryotic ABC exporter structure for comparison
- [Mouse P-glycoprotein (Pgp, ABCB1)](/xray-mp-wiki/proteins/abc-transporters/mouse-p-glycoprotein/) — ABC exporter used for structural comparison of gating mechanisms
- [Sav1866 Multidrug ABC Transporter](/xray-mp-wiki/proteins/abc-transporters/sav1866/) — Outward-open ABC transporter used for conformational comparison
- [Glutathione (GSH)](/xray-mp-wiki/reagents/additives/glutathione/) — GSH and its derivatives (GSSG, Ag-GSH, Hg-GSH) are the transported substrates of NaAtm1
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Method used in structure determination or purification
- [MSBA](/xray-mp-wiki/proteins/abc-transporters/msba/) — Related protein structure
- [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) — Additive used in purification or crystallization buffers
- [POPC](/xray-mp-wiki/reagents/lipids/popc/) — Additive used in purification or crystallization buffers
