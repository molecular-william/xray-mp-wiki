---

title: NupG Nucleoside Transporter
created: 2026-04-27
updated: 2026-04-27
type: protein
tags: [transporter, membrane-protein]
sources: [doi/10.1016##j.jbc.2021.100479]

---
layout: default


# NupG Nucleoside Transporter

## Overview

NupG is the nucleoside proton symporter from *Escherichia coli*, the prototype of the nucleoside proton symporter (NHS) family within the major facilitator superfamily (MFS). It mediates the uptake of nucleosides (adenosine, guanosine, cytidine, thymidine, uridine) across the plasma membrane. NupG is one of two nucleoside delivery systems in *E. coli* alongside NupC (a concentrative nucleoside transporter homol[[og]]).

## Structure Determination

- **PDB IDs**: To be deposited (WT and D323A structures solved)
- **Resolution**: 3.0 Å (P1 space group, two molecules in ASU); 3.8 Å (P2₁ space group, one molecule in ASU)
- **Method**: [[xray-crystallography]], LCP (meso-phase) crystallation, [[molecular-replacement]] using AlphaFold-predicted model
- **Conformation**: Inward-open (both WT and D323A structures)
- **Space groups**: P1 (two molecules, 3.0 Å) and P2₁ (one molecule, 3.8 Å)
- **Expression**: *E. coli* C43(DE3) cells, IPTG-induced

## Structural Architecture

- **Architecture**: Canonical MFS fold with 12 transmembrane helices (TM1–12)
- **Domains**: N domain (TM1–6) and C domain (TM7–12) connected by a flexible loop
- **Cavity**: Between N and C domains, faces the cytoplasm
- **Comparison**: Structurally similar to XylE and LacY (other inward-open MFS transporters)

## Substrate Binding

### Binding Affinities (ITC, 25 °C)

| Substrate | Kd (μM) |
|-----------|---------|
| Guanosine | 46.67 ± 6.66 |
| Adenosine | 99.67 ± 14.57 |
| Cytidine | 143.67 ± 19.66 |
| Thymidine | 162.5 ± 19.16 |
| Uridine | 199.67 ± 15.01 |
| Xanthosine | No binding |

### Binding Pocket Residues

The uridine binding site is in the central cavity between N and C domains:

- **Direct contacts**: R136, T140, F143, Q225, N228, Q261, E264, Y318, F322
- **Essential for binding** (ITC mutants): R136A, T140A, F143A, N228A, Q261A, E264A, Y318A, F322A all abolished binding
- **Not essential**: Q225A (Kd = 227.67 ± 88.34 μM, similar to WT)
- **Increased [[affinity-chromatography]]**: D323A mutant bound uridine with Kd = 9.67 ± 2.87 μM (20-fold increase)

### Binding Pocket Architecture

- **Ribose recognition**: Polar residues (R136, T140, F143) contact the ribose moiety
- **Base recognition**: Q225, N228, Q261, Y318 form H-bonds with the nucleobase
- **Aromatic stacking**: F143 and F322 likely form π–π interactions with uridine, restricting orientation
- **pH dependence**: Binding affinity ~200 μM at pH 5.0–6.0, drops to ~3 mM at pH 8.0 (Tris buffer)

### D323 Role

- D323 does NOT directly contact uridine but is critical for transport
- D323A increases binding affinity 20-fold
- D323N decreases affinity (Kd = 1109 ± 192 μM), mimicking protonation
- **Proposed role**: Proton-escaping site during proton-coupled transport, analogous to E325 in LacY

## Crystallization

- **Method**: Meso-phase (LCP) crystallization
- **Detergent**: [[ddm]] (2%) for solubilization; [[ng]] (0.4%) for purification
- **Protein:lipid ratio**: 1:1.5 (w/w) protein to [[monoolein]] (Nu-Chek)
- **Crystallization conditions**:
  - WT P2₁: 0.1 M [[sodium-citrate]] pH 5.0, 28% [[peg-300]]
  - WT P1: 0.1 M [[sodium-chloride]], 0.1 M MgCl₂, 0.1 M [[sodium-citrate]] pH 5.0, 30% [[peg-6000]]
  - D323A: 0.1 M [[sodium-chloride]], 0.1 M MgCl₂, 0.1 M MES pH 6.0, 30% PEG550 MME
- **Crystal morphology**: Grew in 1 week at room temperature in glass sandwich plates

## Solubilization and Purification

- **[[ddm]]** (2% w/v) — solubilization from *E. coli* membranes
- **[[talon-resin]]** — His-tag capture, elution with 250 mM [[imidazole]]
- **Wash buffer**: 25 mM MES pH 6.0, 150 mM [[sodium-chloride]], 20 mM [[imidazole]], 0.02% [[ddm]]
- **Elution buffer**: 25 mM MES pH 6.0, 150 mM [[sodium-chloride]], 250 mM [[imidazole]], 0.4% [[ng]]
- **Gel filtration**: [[superdex-columns]] 200 10/300 increase, buffer: 25 mM MES pH 6.0, 150 mM [[sodium-chloride]], 0.4% [[ng]]
- **Concentration**: ~20 mg/mL (pre-GF), ~30 mg/mL (post-GF, for crystallization)

## Related NHS Transporters in E. coli

| Transporter | Identity with NupG | Substrate |
|-------------|-------------------|-----------|
| NupG | — | Adenosine, guanosine, cytidine, thymidine, uridine |
| XapB | 58% | Xanthosine (specific) |
| YegT | 27% | Unknown |

## Cross-References

- [[sotb]] — E. coli MFS antiporter; rocker-switch mechanism
- [[nTMATE2-transporter]] — MATE family transporter; [[alternating-access]]
- [[adenine-nucleotide-transporter]] — Mitochondrial carrier (different family)
- [[mfs-transporter]] — Major facilitator superfamily
- [[ddm]] — Solubilization detergent
- [[ng]] — Detergent used in purification
- [[monoolein]] — LCP crystallization lipid
- [[superdex-columns]] — SEC column type concept page