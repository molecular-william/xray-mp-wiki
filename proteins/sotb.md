---

title: SotB
created: 2026-04-27
updated: 2026-04-28
type: protein
tags: [transporter, membrane-protein, pump]
sources: [doi/10.1016##j.bbrc.2020.11.096]
---
layout: default


# SotB

## Overview

SotB is a drug-proton antiporter (DHA) from *Escherichia coli*, belonging to the DHA1 family (TCDB: 2.A.1.2) within the major facilitator superfamily (MFS). DHA transporters utilize the proton-motive force to drive the expulsion of toxic compounds, including antibiotics and drugs, contributing to multi-drug resistance in bacteria.

## Structure

- **PDB IDs**: 6Y5X–6Y5C (four structures in different conformations)
- **Resolution**: 2.7–3.5 Å (range across four crystal structures)
- **Space group**: Not specified in available source material
- **Conformations captured**:
  - Substrate-bound occluded state
  - Inward-facing state
  - Inward-open state
- **Architecture**: 12 transmembrane helices divided into two six-helix bundles (N and C domains) connected by a cytosolic loop — the canonical MFS fold

> **Note**: Source paper appears truncated (only abstract/first page extracted). Structural details (exact resolutions, crystallization conditions, solubilization, purification) may be incomplete. Additional raw papers needed to enrich this page.

## Solubilization and Purification

> **Incomplete** — raw paper truncated. No experimental procedures available in source.
>
> Based on MFS transporter conventions and related E. coli transporters:
> - Likely expressed in *E. coli* with N- or C-terminal His-tag
> - Likely solubilized with DDM or similar mild detergent
> - Likely purified by affinity chromatography followed by SEC

## Crystallization

> **Incomplete** — raw paper truncated. No crystallization conditions available in source.
>
> Based on MFS transporter conventions:
> - Likely crystallized by vapor diffusion
> - Likely required substrate analog for stabilizing specific conformations

## Transport Mechanism

### MFS Alternating Access Model

MFS transporters deliver substrates via the **rocker-switch mechanism**:
1. **Inward-open**: Substrate binding site accessible from the cytoplasm
2. **Occluded**: Both gates closed, substrate trapped
3. **Outward-open**: Substrate binding site accessible from the periplasm/extracellular space

### SotB-Specific Findings

This study reveals **nonlinear rigid-body movements** during the transition from inward-open to occluded conformation:
- The conformational change is not a simple rigid-body rocker-switch
- Nonlinear movements suggest additional local conformational adjustments beyond the global domain rearrangement
- This challenges the simple [alternating-access](/concepts/alternating-access/) model and suggests MFS antiporters may require local gating movements

### Proton-Coupled Antiport

- Substrate binding and protonation compete with each other
- Substrate binding-induced deprotonation triggers the conformational change from inward-facing to outward-facing
- The proton-motive force drives the expulsion of toxic molecules

## Comparison with Other Transporters

| Transporter | Family | Mechanism | States Captured |
|-------------|--------|-----------|-----------------|
| SotB | MFS (DHA1) | Drug-proton antiport | Occluded, inward-facing, inward-open |
| [nTMATE2-transporter](/proteins/nTMATE2-transporter/) | MATE | Nicotine-H⁺ antiport | Two outward-facing conformations |
| [adenine-nucleotide-transporter](/proteins/adenine-nucleotide-transporter/) | Mitochondrial carrier | Nucleotide antiport | Matrix-open, cytoplasmic-open |
| [mmpL3](/proteins/mmpL3/) | Resistin-like membrane protein | Lipid flippase | Apo + 4 inhibitor-bound |

## Related Transporters

- [nTMATE2-transporter](/proteins/nTMATE2-transporter/) — MATE family transporter from tobacco
- [adenine-nucleotide-transporter](/proteins/adenine-nucleotide-transporter/) — Mitochondrial ADP/ATP carrier
- [mmpL3](/proteins/mmpL3/) — Mycobacterial lipid transporter
- [nupg-nucleoside-transporter](/proteins/nupg-nucleoside-transporter/) — E. coli MFS nucleoside transporter

## Concepts

- [mfs-transporter](/concepts/mfs-transporter/) — Major facilitator superfamily
- [dha-antiporter](/concepts/dha-antiporter/) — Drug-proton antiporter family
- [alternating-access](/concepts/alternating-access/) — Alternating access mechanism

## References

- Xiao et al. (2020) Biochem. Biophys. Res. Commun. — SotB structures (this paper)
- Abramson et al. (2003) Science 301:610–615 — LacY structure (MFS model)
- Abramson et al. (2006) Nature 440:347–350 — GlpT structure (MFS model)

## Cross-References

- [mfs-transporter](/concepts/mfs-transporter/) — Major facilitator superfamily
- [dha-antiporter](/concepts/dha-antiporter/) — Drug-proton antiporter family
- [alternating-access](/concepts/alternating-access/) — Alternating access mechanism
- [ddm](/reagents/detergents/ddm/) — Common solubilization detergent for MFS transporters