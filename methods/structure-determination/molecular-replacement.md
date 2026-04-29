---

title: Molecular Replacement
created: 2026-04-26
updated: 2026-04-27
type: method
tags: [structure-xray, structure-molecular-replacement]
sources: [doi/10.1002##1873-3468.14136, doi/10.1016##j.bbabio.2023.148986]

---


# Molecular Replacement

## Description

Molecular replacement (MR) is an X-ray crystallography phasing method that uses a known homologous structure as a search model to determine phases for a new structure.

## Key Software

- **PHASER** (CCP4) — most widely used MR program
- Used by: [[nTMATE2-transporter]] (CasMATE model, PDB 5YCK)
- Used by: [[psi-lhci-supercomplex]] (plant PSI-LHCI, PDB 4XK8)

## Advantages

- Fast and computationally efficient
- No need for heavy atom derivatization or SAD/MAD experiments
- Works well when homologous structures (>25% identity) are available

## Limitations

- Requires a suitable search model (homologous structure)
- Can fail for very distantly related proteins
- May require ensemble models or rigid-body refinement

## Related Methods

- [[xray-crystallography]] — SAD and MAD phasing methods (consolidated under X-ray Crystallography)
- [[xray-crystallography]] — General X-ray structure determination
