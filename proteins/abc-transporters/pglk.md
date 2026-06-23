---
title: "PglK ABC Flippase"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2019.01.013, doi/10.1038##nature14953]
verified: false
---

# PglK ABC Flippase

## Overview

PglK is an ATP-binding cassette (ABC) flippase from Campylobacter jejuni that translocates lipid-linked oligosaccharide (LLO) across the inner membrane, essential for asparagine-linked protein N-glycosylation. The crystal structure of PglK-E510Q bound to ATPgammaS (PDB 6HRC, 3.2 A) captured an outward semi-occluded state with the two nucleotide-binding domains (NBDs) forming an asymmetric closed dimer. The structure reveals a vase-like cavity with an arginine belt that interacts with the pyrophosphate group of LLO. Combined with extensive molecular dynamics simulations, this study supports a non-alternating-access mechanism for LLO translocation and identifies a surface recognition site between TM2 and TM5 for LLO, suggesting a substrate-hunting mechanism.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2019.01.013 | 6HRC | 3.2 A | -- | PglK-E510Q mutant from Campylobacter jejuni, co-crystallized with ATPgammaS and MgCl2 | ATPgammaS (2 molecules), Mg2+ |
| doi/10.1038##nature14953 | 5C78 | 2.9 | P1 | PglK-E510Q mutant, apo-inward-1 state | -- |
| doi/10.1038##nature14953 | 5C78 | 3.9 | P12_1 | PglK-E510Q mutant, apo-inward-2 state | -- |
| doi/10.1038##nature14953 | 5C78 | 5.9 | P4_12_12 | PglK-E510Q mutant, outward-occluded state co-crystallized with ADP and MgCl2 | ADP, Mg2+ |

## Expression and Purification

- **Expression system**: E. coli BL21-Gold (DE3) competent cells
- **Construct**: PglK-E510Q mutant (Walker-B glutamate replaced by Gln) from C. jejuni

### Purification Workflow

#### Source: doi/10.1016##j.str.2019.01.013


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Homogenization and ultracentrifugation | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + -- | Standard membrane protein purification protocol |
| Solubilization | Detergent solubilization | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membranes solubilized in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA superflow | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | His-tag purification with stepwise elution |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (lauryl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol) | Buffer exchanged to [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) for crystallization |

#### Source: doi/10.1038##nature14953

- **Expression system**: E. coli BL21-Gold (DE3)
- **Expression construct**: PglK with N-terminal His10 tag
- **Tag info**: N-terminal His10 affinity tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | Modified TB medium with 1% [Glucose](/xray-mp-wiki/reagents/additives/glucose/) + -- | 30 L fermentor; induced with 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 1 h at 37 C |
| Cell lysis | Microfluidizer | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl, 7 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 0.5 mM PMSF + -- | M-110L microfluidizer at 15,000 psi chamber pressure |
| Membrane preparation | Ultracentrifugation | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl + -- | Membranes pelleted at 100,000g for 30 min |
| Solubilization | Detergent solubilization | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 7 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 1% [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) | Stirring for 2 h at 4 C |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | NiNTA superflow (Qiagen) | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.016-0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (first wash), then 0.016-0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (second wash) | Eluted with 200 mM NaCl, 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL (GE Healthcare) | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 200 mM NaCl + 0.016-0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) | Peak fractions pooled and concentrated to 8-10 mg/ml |

**Final sample**: ~8-10 mg/ml in 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 200 mM NaCl, 0.016-0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)


## Crystallization

### doi/10.1016##j.str.2019.01.013

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization |
| Protein sample | Purified PglK-E510Q in [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) with ATPgammaS and MgCl2 |
| Reservoir | 100 mM Na3Citrate pH 5.5, 100 mM NaCl, 18-22% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 |
| Temperature | 20 C |
| Growth time | Long needle crystals appeared over several days |
| Cryoprotection | Crystals cryoprotected with reservoir solution supplemented with 25% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) and flash-frozen in liquid nitrogen |
| Notes | PglK-E510Q co-crystallized with ATPgammaS and MgCl2 yielded long needle crystals showing anisotropic X-ray diffraction to 3.2 A. Data collected at beamline X06SA at the Swiss Light Source. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/). The structure shows an outward semi-occluded state with a vase-like cavity and arginine belt essential for LLO binding. |

### doi/10.1038##nature14953

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop or hanging drop) |
| Protein sample | PglK-E510Q in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (apo-inward-1, 2.9 A) or [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (apo-inward-2, 3.9 A) |
| Reservoir | Various reservoir conditions (see PDB entries for full details) |
| Temperature | 20 C |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Apo-inward-1 crystallized in [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) at 2.9 A resolution (space group P1). Apo-inward-2 crystallized in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) at 3.9 A (space group P12_1). Outward-occluded state crystallized with 5-10 mM ADP and 5-10 mM MgCl2 at 5.9 A (space group P4_12_12). Side-chain register of outward-occluded model validated by anomalous diffraction data of Hg-soaked crystals and [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) derivative. |


## Biological / Functional Insights

### Outward semi-occluded state with asymmetric NBD dimer

The ATPgammaS-bound PglK structure reveals an asymmetric closed NBD dimer where one ATPgammaS is Mg2+-bound with canonical catalytic residue arrangement, while the other site is Mg2+-free with an alternative Q-loop conformation. This asymmetry suggests non-simultaneous ATP hydrolysis at the two NBDs, supporting an alternating ATP hydrolysis mechanism.

### LLO recognition site and substrate-hunting mechanism

Docking and MD simulations identified a positively charged surface recognition site between TM2 and TM5 (residues H95, R99, R104, K247) that binds the pyrophosphate group of LLO. Mutagenesis of these residues disrupts LLO-stimulated ATPase activity and flipping. The results suggest PglK employs a substrate-hunting mechanism to locally increase LLO concentration before translocation.

### Energetics of LLO flipping

Potential of mean force (PMF) calculations showed an energetic barrier of ~6-8 kBT for LLO translocation. The sugar-first pathway is energetically smoother than pyrophosphate-first. An applied membrane potential (-80 mV) reduces the barrier, consistent with coupling to electrochemical potential. Aromatic residues on the PglK surface facilitate sugar passage via stacking interactions.

### LLO flippase mechanism — credit card swipe model

Crystal structures of PglK in apo-inward (2.9 A, 3.9 A) and ADP-bound outward-occluded (5.9 A) states, combined with in vitro flipping assays and in vivo studies, reveal a unique flipping mechanism distinct from classical alternating access. The pyrophosphate-oligosaccharide head group enters the outward-facing translocation cavity and interacts with positively charged arginine residues (R86, R260, R302, R309), while the polypropenyl lipid tail binds the transporter surface via the external helix (EH) and remains exposed to the lipid bilayer throughout the reaction. The EH forms hydrophobic grooves that anchor the lipid tail and are essential for LLO-stimulated ATPase activity. PglK appears to adopt outward-facing states directly rather than cycling through inward-facing conformations for substrate binding, resembling a credit card swipe model where the lipid tail stays in the membrane while the head group is translocated through a spacious cavity.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for crystallization and activity measurements
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — Extensive MD simulations used to study LLO recognition and translocation
- [Ni-NTA Affinity Chromatography](/xray-mp-wiki/methods/purification/ninta-affinity-chromatography/) — Primary purification method for PglK
- [Size-Exclusion Chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final polishing step
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) — Additive used in purification or crystallization buffers
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
