---
title: "Human Excitatory Amino Acid Transporter 1 (EAAT1)"
created: 2026-06-08
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography, transporter]
sources: [doi/10.1038##nature22064, doi/10.1038##s41586-021-03240-9, doi/10.15252##embj.2021108341]
verified: false
---

# Human Excitatory Amino Acid Transporter 1 (EAAT1)

## Overview

Human excitatory amino acid transporter 1 (EAAT1, SLC1A3) is a member of the
solute carrier 1 (SLC1) family of transporters that takes up the
neurotransmitter glutamate from the synaptic cleft into astrocytes and
neurons. EAAT1 uses energy stored in sodium, proton and potassium gradients
to maintain steep glutamate gradients. In addition to coupled transport,
EAAT1 conducts chloride ions through a channel-like process thermodynamically
uncoupled from transport. Crystal structures of a thermostabilized
EAAT1 construct (EAAT1_cryst) were determined in outward-facing conformations
with and without the allosteric inhibitor UCPH101, revealing the architecture
of the human transporter including the scaffold domain (ScaD) and transport
domain (TranD), and a mechanism of allosteric inhibition where UCPH101 locks
the transporter in outward-facing states. A co-structure with both UCPH101
and TBOA-TFB revealed how competitive and allosteric inhibitors can bind
simultaneously. [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) and X-ray structures of the archaeal homologue [Gltph](/xray-mp-wiki/proteins/slc-transporters/glt-ph/)
in a chloride ion-conducting state (CICS) revealed the molecular basis for
the uncoupled Cl- conductance, gated by two hydrophobic regions at the
domain interface. X-ray structures of EAAT1_CRYST in multiple ion-bound
states (Na+/L-asp, Rb+/Ba2+, E386Q mutant) and a [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of
wild-type EAAT1 at 3.99 A, combined with [HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/) and mutagenesis, revealed
the ion-coupling mechanism — how Na+, K+, and H+ gradients drive
substrate transport through an elevator-type alternating access mechanism.
The conserved E386 residue in EAAT1_CRYST (E406 in full-length numbering)
plays a critical role in the proton coupling mechanism, and its mutation
to glutamine alters the ion-bound conformation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature22064 | 5LLM | 3.25 | P6_3 | EAAT1_cryst (thermostabilized, N155T/N204T, ASCT2 TM3-4c swap) with UCPH101 and L-Asp bound | UCPH101, [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) |
| doi/10.1038##nature22064 | 5LLM | 3.10 | P6_3 | EAAT1_cryst-II (M231I/F235I mutant) with UCPH101 bound | UCPH101, [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) |
| doi/10.1038##nature22064 | 5LLM | 3.32 | P6_3 | EAAT1_cryst-II (M231I/F235I mutant) UCPH101-unbound | [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) |
| doi/10.1038##nature22064 | 5LLM | 3.71 | P6_3 | EAAT1_cryst with UCPH101 and TBOA-TFB bound | UCPH101, TBOA-TFB |
| doi/10.15252##embj.2021108341 | 7AWM | 3.25 | P6_3 | EAAT1_CRYST Na+/L-asp and UCPH101 bound | Na+, [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/), UCPH101 |
| doi/10.15252##embj.2021108341 | 7AWM | 3.60 | P6_3 | EAAT1_CRYST-E386Q Na+/L-asp and UCPH101 bound | Na+, [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/), UCPH101 |
| doi/10.15252##embj.2021108341 | 7AWM | 3.92 | P6_3 | EAAT1_CRYST Rb+/Ba2+ and UCPH101 bound | Rb+, Ba2+, UCPH101 |
| doi/10.15252##embj.2021108341 | 7AWM | 3.91 | P6_3 | EAAT1_CRYST-II Rb+/Ba2+ and UCPH101 bound | Rb+, Ba2+, UCPH101 |
| doi/10.15252##embj.2021108341 | 7AWM | 3.70 | P6_3 | EAAT1_CRYST-II Ba2+ and UCPH101 bound | Ba2+, UCPH101 |
| doi/10.15252##embj.2021108341 | 7AWM | 3.99 |  | Wild-type human EAAT1 (full-length) |  |

## Expression and Purification

- **Expression system**: HEK293F cells
- **Construct**: EAAT1 with N-terminal Strep-tag II, eGFP, PreScission cleavage site; thermostabilizing consensus mutations; N155T/N204T; ASCT2 TM3-4c swap
- **Notes**: Transient transfection with PEI; cells grown in Excell293 medium; collected 48 h post-transfection

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Resuspension and douce homogenization | — | 50 mM HEPES/Tris-base pH 7.4, 200 mM NaCl, 1 mM L-Asp, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 1 mM [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 2% DDS (dodecanoyl [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/)) + 0.4% CHS | 1 h incubation at 4 C; ultracentrifugation at 247,000g for 45 min |
| Affinity chromatography | Strep-Tactin affinity | Strep-Tactin resin | 50 mM HEPES/Tris-base pH 7.4, 200 mM NaCl, 1 mM L-Asp, 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 3x CMC DDS + 0.01% CHS | Fractions analyzed by FSEC; elution with [Desthiobiotin](/xray-mp-wiki/reagents/ligands/desthiobiotin/) |
| Size exclusion chromatography | SEC polishing | Superose 6 10/300 | 50 mM HEPES/Tris-base pH 7.4, 200 mM NaCl, 1 mM L-Asp, 0.5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.0632% DDS + 0.01264% CHS | Final purification step before crystallization |


## Crystallization

### doi/10.1038##nature22064

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | Purified EAAT1_cryst in 50 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 200 mM NaCl, 1 mM L-Asp, 0.5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/), 0.0632% DDS, 0.01264% CHS, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Reservoir | Not specified in raw paper |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals grown in presence of 0.5 mM UCPH101; space group P6_3 |


## Biological / Functional Insights

### Allosteric inhibition locks EAAT1 in outward-facing states

UCPH101 binds in a hydrophobic pocket at the TranD-ScaD interface between TM3, TM7 and TM4c, wedging the two domains together. The compound makes ring-stacking interactions with Phe369 (TM7a) and hydrophobic contacts with residues in TM3, TM7a and TM4c. [HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/) analysis shows that UCPH101 binding decreases deuterium uptake in the TranD-ScaD interface, consistent with stabilization of the outward-facing state at the expense of inward-facing state(s).

### TM4b-c loop is a eukaryotic-specific insertion

The TM4b-c loop, an insertion in eukaryotic SLC1 transporters, protrudes into the central vestibule of the EAAT1 trimer forming the center of the propeller. It contains a conserved N-glycosylation site (Asn204) and makes extensive inter- and intra-subunit contacts. This architectural feature is absent in the prokaryotic homologue [Gltph](/xray-mp-wiki/proteins/slc-transporters/glt-ph/).

### TM1a forms membrane-interacting amphipathic helix

TM1 bends at the cytoplasmic side with TM1a lying nearly parallel to the
membrane plane, forming the tips of the propeller blades. Its amphipathic
nature and associated non-protein electron density between TM1a and HP1a
suggest interaction with the inner leaflet, likely representing bound
lipid or detergent molecules.

### Cl- channel gated by two hydrophobic regions in EAAT1

[Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) and X-ray structures of the [Gltph](/xray-mp-wiki/proteins/slc-transporters/glt-ph/) homologue revealed a chloride
ion-conducting state (CICS) with an aqueous cavity at the domain interface.
Electrophysiological studies in Xenopus laevis oocytes confirmed that the
same crosslinking strategy (XL2: L244C/G439C in EAAT1) traps EAAT1 in an
open-channel conformation with enhanced Cl- conductance. Mutation of
hydrophobic residues equivalent to those gating the [Gltph](/xray-mp-wiki/proteins/slc-transporters/glt-ph/) channel confirmed
a conserved mechanism: F50A, T54A, L88A, M89A, M286A, and L269A mutations
shifted the reversal potential to more hyperpolarized potentials (increased
Cl- conductance), while A289F essentially eliminated Cl- contribution to
net conductance (reversal potential shift to +76 ± 2 mV). The P290R
mutation associated with episodic ataxia type 6 results in increased Cl-
conductance and reduced glutamate transport, linking channel dysfunction
to neurological pathology.

### Ion-coupling mechanism of EAAT1 revealed by multi-ion bound structures and HDX-MS

X-ray structures of EAAT1_CRYST in multiple ion-bound states (Na+/L-asp,
Rb+/Ba2+, and the E386Q mutant), combined with a [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of
wild-type EAAT1 at 3.99 A and [HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/) analysis, revealed the molecular basis
of ion coupling. The E386 residue (E406 in full-length EAAT1 numbering) is
critical for proton coupling. The E386Q mutant structure shows the E386
sidechain adopts a similar position to wild-type, consistent with H-bonding
between protonated E386 and residues in HP2b, supporting a model where
Glu386 undergoes protonation during the transport cycle. The Rb+/Ba2+-bound
structures probe the K+ counter-transport pathway. [HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/) experiments with
K+-bound, Na+/L-asp-bound, and control conditions identified peptides
exhibiting reversible K+-induced HDX changes, mapping regions that undergo
conformational changes during the transport cycle. The HDX peptide coverage
map covers 55% of the EAAT1_CRYST sequence with 77 unique peptides.

### TM1a deletions impair glutamate transport

N-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) of EAAT1 (labeled with the N-terminal residue) show
that TM1a deletions progressively impair [L Glutamate](/xray-mp-wiki/reagents/substrates/l-glutamate/) uptake in HEK293 cells.
Radioactive [L Glutamate](/xray-mp-wiki/reagents/substrates/l-glutamate/) uptake decreases steeply in incremental N-term
truncated constructs, while protein expression (measured by GFP counts)
remains relatively constant compared to EAAT1_WT. This confirms the
functional importance of the TM1a amphipathic helix in the transport
mechanism.

### Tryptophan fluorescence as a probe of substrate binding

Intrinsic tryptophan fluorescence changes upon L-asp/Na+ binding serve as
a readout of conformational transitions. W287 and W473 mutations greatly
decreased or abolished, respectively, the Trp-intrinsic fluorescence change
associated with L-asp/Na+ binding, indicating these residues report on
substrate-induced conformational changes.


## Cross-References

- [GltPh (Glutamate Transporter Homologue from Pyrococcus horikoshii)](/xray-mp-wiki/proteins/slc-transporters/glt-ph/) — Prokaryotic homologue with same fold; structural basis for elevator mechanism
- [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) — EAAT1 transports substrates via elevator-like rigid-body movements of the transport domain
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — SLC1 transporters operate by alternating access of the substrate binding site
- [UCPH101](/xray-mp-wiki/reagents/ligands/ucph101/) — Selective allosteric inhibitor of EAAT1 bound in the TranD-ScaD interface
- [TBOA (DL-threo-beta-benzyloxyaspartic acid)](/xray-mp-wiki/reagents/ligands/tboa/) — Competitive inhibitor bound in co-structure with UCPH101
- [DDS (Dodecanoyl Sucrose)](/xray-mp-wiki/reagents/detergents/dds/) — Detergent used for solubilization and crystallization
- [Anion Channel Gating](/xray-mp-wiki/concepts/transport-mechanisms/anion-channel-gating/) — EAAT1 Cl- conductance is gated by two hydrophobic regions at the domain interface
- [DTT (Dithiothreitol)](/xray-mp-wiki/reagents/additives/dtt/) — Reducing agent used to test disulfide crosslinking in EAAT1 cysteine mutants
- [Glutamate Transporter Family (SLC1/EAAT)](/xray-mp-wiki/concepts/transport-mechanisms/glutamate-transporter-family/) — EAAT1 is a human SLC1 family member; ion-coupling mechanism is shared across the family
- [Substrate-Protonation Coupling](/xray-mp-wiki/concepts/transport-mechanisms/substrate-protonation-coupling/) — E386 protonation is coupled to substrate binding in EAAT1 transport mechanism
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Cryo-EM structure of wild-type EAAT1 determined at 3.99 A
