---


title: Affinity Chromatography
created: 2026-04-26
updated: 2026-04-27
type: method
tags: [purification-affinity]
sources: [doi/10.1002##1873-3468.14136, doi/10.1016##j.bbabio.2023.148986, doi/10.1016##j.bbrc.2019.12.091]


---
layout: default



# Affinity Chromatography

## Overview

Affinity chromatography exploits specific interactions between a protein and a ligand immobilized on a resin. For membrane proteins, His-tag affinity (metal chelation) is the most common first-step purification.

## Common Affinity Methods

| Method | Tag/Interaction | Resin | Elution |
|--------|----------------|-------|---------|
| His-tag (TALON) | Polyhistidine-Co2+ | TALON cobalt | Imidazole |
| GFP-His10 (TALON) | GFP-His10-Co2+ | TALON cobalt | Imidazole (15 mM wash, 200 mM elution) |
| GST-tag | Glutathione | Glutathione-sepharose | Glutathione |
| Strep-tag | StrepII peptide | StrepTactin | Desthiobiotin |

## Proteins Using Affinity (from this wiki)

- [[nTMATE2-transporter]] — TALON cobalt affinity for His8-tagged protein
  - Wash: 20-40 mM [[imidazole]]
  - Elution: 200 mM imidazole
  - Buffer: 300 mM NaCl, 50 mM HEPES-Na pH 7.0, 5% [[glycerol]], 0.05% DDM, 0.003% CHS
- [[a2a-adenosine-receptor]] — bRIL fusion used for crystallization construct stabilization
- [[psi-lhci-supercomplex]] — column-free isolation (no affinity step — very mild purification)
- [[etb-receptor]] — GFP-His10 tag captured on TALON resin; washed with 15 mM imidazole, eluted with 200 mM imidazole

## IMAC (Immobilized Metal Affinity Chromatography)

IMAC exploits the affinity of polyhistidine tags for immobilized metal ions (Ni²⁺, Co²⁺, Cu²⁺, Zn²⁺).

- **Resin**: Agarose or sepharose beads chelated with metal ions (most commonly Ni²⁺ via NTA or IDA ligands)
- **Binding**: Polyhistidine tag (typically 6×His) coordinates with the immobilized metal through nitrogen lone pairs
- **Elution**: Imidazole competes with His residues for metal binding; alternatively, low pH protonates histidines
- **Specificity**: His-tagged proteins bind while most contaminants flow through

TALON cobalt resin (Co²⁺) has higher selectivity than Ni-NTA for His-tagged proteins.

### IMAC Example: KirBac3.1

- **Resin**: Ni²⁺-loaded IMAC resin
- **Protein**: Full-length histidine-tagged KirBac3.1 from *E. coli*
- **Solubilization**: 1% Anzergent 3,12
- **Subsequent step**: Size-exclusion chromatography after IMAC
- **Final concentration**: ~8 mg/mL in detergent for crystallization

### Comparison with Other Affinity Methods

| Method | Tag | Resin | Elution | Specificity |
|--------|-----|-------|---------|-------------|
| IMAC | His-tag | Ni²⁺/Co²⁺ NTA | Imidazole | High |
| TALON | His-tag | Co²⁺ | Imidazole | Higher than Ni-NTA |
| GST | GST tag | Glutathione | Reduced glutathione | Very high |
| Strep | Strep-tag II | Strep-Tactin | Desthiobiotin | Very high |

## Related Methods

- [[size-exclusion-chromatography]] — SEC after affinity capture
- [[talon-resin]] — TALON cobalt resin details
- [[superdex-columns]] — Superdex SEC columns
- [[tev-protease]] — Tag removal after affinity purification