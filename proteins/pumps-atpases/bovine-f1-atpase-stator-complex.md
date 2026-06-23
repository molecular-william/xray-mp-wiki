---
title: Bovine Mitochondrial F1-ATPase-Stator Complex (Membrane Extrinsic Region)
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0910365106]
verified: false
---

# Bovine Mitochondrial F1-ATPase-Stator Complex (Membrane Extrinsic Region)

## Overview

The bovine mitochondrial F1-ATPase-stator complex (F1-stator_T) is a subcomplex of the F1Fo-ATP synthase, the enzyme that synthesizes ATP using the proton motive force across the inner mitochondrial membrane. This 3.2 Å resolution structure captures the membrane extrinsic region of the stator, containing residues 122-207 of subunit b, residues 5-25 and 35-57 of F6, three segments of subunit d (residues 30-40, 65-74, 85-91), and residues 1-146 and 169-189 of the oligomycin sensitivity conferral protein (OSCP). Subunit b extends as a continuous 160 Å long α-helix from residue 188 back to residue 79 near the inner mitochondrial membrane surface. The stator is a key structural element that counteracts the rotational torque of the rotor during ATP synthesis.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0910365106 | not stated in raw paper | 3.2 | P2(1)2(1)2(1) | Bovine F1-ATPase (α3β3γδɛ) complexed with stator_T subcomplex (b, d, F6, OSCP). Selenomethionine-substituted stator_T. | AMP-PNP (non-hydrolyzable ATP analog) |

## Expression and Purification

- **Expression system**: Escherichia coli (bacterial overexpression)
- **Construct**: Stator_T subcomplex (b, d, F6, OSCP) expressed from a plasmid encoding all 3 proteins in an operon. OSCP produced separately by bacterial overexpression and refolded.
- **Notes**: Proteins mixed together and stator_T complex purified before assembly with bovine F1-ATPase.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Stator_T complex purification | Ion exchange and gel filtration chromatography | -- | -- | Stator_T complex purified after mixing overexpressed subunits. Purity assessed by SDS/PAGE. Molecular masses verified by mass spectrometry. |
| Assembly with F1-ATPase | Complex formation followed by gel filtration chromatography | -- | -- | Stator_T assembled with native bovine F1-ATPase and purified by gel filtration. |

**Final sample**: 12.5 mg/mL F1-stator_T complex in D2O-based buffer
**Purity**: Intact subunits confirmed by SDS/PAGE analysis of crystals


## Crystallization

### doi/10.1073##pnas.0910365106

| Parameter | Value |
|---|---|
| Method | Microbatch under light paraffin oil |
| Protein sample | 12.5 mg/mL F1-stator_T complex in D2O-based buffer |
| Reservoir | 15-22% (w/v) polyethylene glycol 8000, 300 mM ammonium sulfate, 100 mM [MES](/xray-mp-wiki/reagents/buffers/mes) (pH 6.5), 1 mM [AMP-PNP](/xray-mp-wiki/reagents/ligands/amp-pnp) |
| Mixing ratio | 1:1 protein:reservoir (3 µL drops) |
| Temperature | 23°C |
| Growth time | 14 days |
| Cryoprotection | Crystals passed through cryoprotection solutions: 10 mM [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris-hcl) (pH 8.0), 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride), 25 mM [Sucrose](/xray-mp-wiki/reagents/additives/sucrose), 1 mM [MgSO4](/xray-mp-wiki/reagents/additives/magnesium-sulfate), 2.5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt), 0.5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta), 0.01% NaN3, 0.0005% [PMSF](/xray-mp-wiki/reagents/additives/phenylmethylsulfonyl-fluoride), 20 µM [ADP](/xray-mp-wiki/reagents/ligands/adp), 19-22% (w/v) PEG8000, 150 mM (NH4)2SO4, 50 mM MES (pH 6.5), 0.5 mM AMP-PNP, 5-20% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) (increased in 5% steps) |
| Notes | Crystals grown by microbatch under light paraffin oil in 72-well microbatch plates. 4 crystals harvested, washed, and analyzed by SDS/PAGE (intact subunits confirmed). Data collected at ESRF beamline ID23eh1 (λ=0.9790 Å). |


## Biological / Functional Insights

### Stator architecture and rotary catalysis

The F1-stator_T structure reveals the complete membrane extrinsic part of the bovine ATP synthase stator. The N-terminal domain of OSCP links the stator to F1-ATPase via α-helical interactions with the N-terminal region of subunit αE. Its C-terminal domain makes extensive helix-helix interactions with the C-terminal α-helix of subunit b (residues 190-207). Subunit b extends as a continuous 160 Å α-helix from residue 188 back to residue 79, stiffened by α-helices from subunits d and F6. The structure can bend inward around residue 146 of subunit b, suggesting flexibility in the stator.

### Stator flexibility and functional implications

The C-terminal domain of OSCP forms a 5-helix bundle with subunit b and F6, providing a stable interface. The β-hairpin of OSCP makes few interactions with adjacent domains, suggesting a flexible joint that allows the stator to adjust to the changing surface profile of F1 during catalysis. The linker between the two OSCP domains also appears flexible. The stator likely helps the α₃β₃ domain resist rotational torque rather than storing elastic energy or clamping subunit a to the c-ring.

### Comparison with other ATP synthases

The OSCP interaction with αE involves α-helices 1 and 5 of OSCP and residues 6-17 of subunit αE, accounting for the high-affinity binding site (Kd = 80 nM). Two low-affinity sites (Kd = 6-8 µM) may involve interactions with αDP and αTP. The stator binding interface is predominantly hydrophobic, while the facing surface of F1 is negatively charged with a dimple in the crown region, and the stator surface is positively charged. This differs from proposals in E. coli and chloroplast enzymes.


## Cross-References

- [Bovine F1-ATPase (azide-inhibited form)](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — Catalytic domain of the same ATP synthase; azide-inhibited structure used as MR search model (PDB 2CK3)
- [Rotary ATPase Mechanism](/xray-mp-wiki/concepts/rotary-atpase-mechanism/) — ATP synthase uses a rotary catalytic mechanism driven by the proton motive force
- [Yeast Mitochondrial ATP Synthase c10 Ring](/xray-mp-wiki/proteins/pumps-atpases/yeast-mitochondrial-atp-synthase-c10-ring/) — Membrane rotor component of ATP synthase; the c-ring interacts with the stator via subunit a
