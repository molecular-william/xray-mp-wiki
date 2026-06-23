---
title: PbgA (YejM) Cardiolipin Transport Protein
created: 2026-06-08
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##srep30815, doi/10.1128##mBio.03277-19]
verified: false
---

# PbgA (YejM) Cardiolipin Transport Protein

## Overview

PbgA (formerly YejM) is an inner membrane protein in Gram-negative bacteria containing
five transmembrane helices and a C-terminal globular periplasmic domain. It functions
as a [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) (CL) transporter, moving CL from the inner membrane to the outer
membrane. This process is regulated by the PhoPQ two-component system and is critical
for outer membrane biogenesis, bacterial pathogenesis, and resistance to cationic
antimicrobial peptides. The crystal structures of the periplasmic globular domain from
Salmonella typhimurium and Escherichia coli revealed a fold resembling arylsulfatases
and lipoteichoic acid synthases, with a novel hydrophobic pocket that binds and
transports [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/). The full-length S. Typhimurium PbgA structure (Fan et al., 2020,
mBio) at 2.7 A resolution revealed a unique five-TM fold, two CL-binding sites (site 1
in the TM domain, site 2 at the membrane-periplasm interface), a long and deep cleft
spanning the TM and periplasmic domains, a putative catalytic Asp-His dyad (D104-H114),
and the critical C-terminal region (residues 557-586) required for PhoPQ-regulated
barrier function and macrophage survival.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##srep30815 |  | 1.64 | P2<sub>1</sub> | StPbgA245-586 (S. typhimurium residues 245-586) |  |
| doi/10.1038##srep30815 |  | 1.67 | P3<sub>1</sub>2<sub>1</sub> | EcPbgA245-586 (E. coli residues 245-586) |  |
| doi/10.1038##srep30815 |  | 2.19 | P2<sub>1</sub> | StPbgA191-586 (S. typhimurium residues 191-586) |  |
| doi/10.1128##mBio.03277-19 | 6V8Q | 2.7 | P2<sub>1</sub> | Full-length PbgA (residues 1-586) from S. Typhimurium 14028s, cloned into pBAD24 with C-terminal His6 tag, expressed in E. coli DH5alpha, crystallized with [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) | [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) (CL1 in TM domain, CL2 at membrane-periplasm interface) |
| doi/10.1128##mBio.03277-19 |  | 1.7 |  | PbgA periplasmic domain (residues 245-586) from S. Typhimurium 14028s, cloned into pET28a with C-terminal His6 tag, expressed in E. coli BL21(DE3) |  |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) (periplasmic domain); E. coli DH5alpha (full-length)
- **Construct**: PbgA245-586 cloned into pET28a (periplasmic domain); full-length PbgA (1-586) cloned into pBAD24 (full-length), both with C-terminal His6 tag
- **Induction**: 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 16C overnight (periplasmic domain); 0.2% arabinose at 37C for 4 h (full-length)
- **Media**: LB medium; SeMet-labeled protein expressed in minimal medium with seleno-[L-Methionine](/xray-mp-wiki/reagents/ligands/l-methionine/)

### Purification Workflow

*Source: doi/10.1038##srep30815*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Cell disruption at 30,000 psi |  | 20 mM Tris-Cl pH 7.8, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 500 mM NaCl, cOmplete protease inhibitors, 1 mM DNase, 1 mM PMSF | Cells harvested by centrifugation at 5000 × g for 20 min; debris removed at 120,000 × g for 25 min |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Ni-NTA agarose (Qiagen) | 20 mM Tris-Cl pH 7.8, 500 mM NaCl, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (wash); 20 mM Tris-Cl pH 7.8, 500 mM NaCl, 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (elution) |  |
| Buffer exchange | Gel filtration / dialysis |  | 20 mM Tris-Cl pH 7.8, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) | Buffer exchanged using desalting column |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM Tris-Cl pH 7.8, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Further purification step not fully detailed in this paper |

### Purification Workflow

*Source: doi/10.1128##mBio.03277-19*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press high-pressure homogenization (10,000-15,000 psi, two runs) |  | PBS (periplasmic domain); 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (full-length) | Cells resuspended in ice-cold buffer. Homogenate centrifuged at 17,000 × g for 40 min at 4C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Ni-NTA agarose (Qiagen) | PBS + 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash); PBS + 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) for periplasmic domain; similar for full-length | Periplasmic domain: incubated 1 h, washed with 50 ml PBS + 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), eluted with 10 ml PBS + 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/30 (GE Healthcare) | 20 mM HEPES pH 7.0, 150 mM NaCl | Concentrated to 0.5 ml before loading. Peak fractions pooled and concentrated to 30 mg/ml (periplasmic domain) or prepared for crystallization with CL (full-length) |


## Crystallization

### doi/10.1038##srep30815

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | StPbgA245-586 and EcPbgA245-586 at ~10 mg/ml in 20 mM Tris-Cl pH 7.8, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Reservoir | See crystallization conditions (not specified in detail in text) |
| Temperature | 20C |
| Notes | SeMet-labeled StPbgA245-586 used for SAD phasing |

### doi/10.1128##mBio.03277-19

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | Full-length PbgA premixed with [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) (CL), concentrated in 20 mM HEPES pH 7.0, 150 mM NaCl |
| Reservoir | 0.4 M (NH4)2SO4, 0.1 M MES pH 6.5, 10% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350 |
| Temperature | 20C |
| Growth time | 7-30 days |
| Cryoprotection | Mother liquor supplemented with 20% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Notes | Plate-shaped crystals (typically 400 x 50 x 20 um^3). Full-length structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using periplasmic domain as search model. |


## Biological / Functional Insights

### Cardiolipin transport mechanism

PbgA transports [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) (CL) from the inner membrane to the outer membrane
in Gram-negative bacteria through a hydrophobic pocket between the second and third
structural layers of the periplasmic globular domain. Key hydrophobic residues
(F292, F349, F362, F519) line this binding pocket and are essential for CL transport.
A flexible loop formed by residues D347-Q370 acts as a conformational "lid" that
opens to allow CL access to the binding site. This represents the first structural
characterization of a bacterial protein involved in phospholipid transport from the
inner membrane to the outer membrane.

### Full-length structure reveals two CL-binding sites

The full-length PbgA-CL complex (2.7 A) reveals two CL-binding sites: site 1 in
the TM domain and site 2 at the membrane-periplasm interface. Site 1 involves CL1
bound at the N-terminal end of TM2, with R50 forming ionic bonds to the phosphate
moiety and W43 forming a hydrogen bond with an ester linkage. Site 2 is formed
almost exclusively by the loop between alpha2 and alpha3 of the linker region,
with key residues I189, W190, Y210, M212, R215, R216, F217, and L218. R215 and
R216 are essential for CL binding, bacterial growth, and barrier function. Site 2
is the physiologically relevant CL-binding site.

### Long deep cleft spanning TM and periplasmic domains

PbgA contains a long and deep cleft on the protein surface extending from the
TM domain into the periplasmic domain. The interior of the cleft is primarily
hydrophobic in the TM region (likely exposed to the lipid bilayer hydrophobic
core) and becomes negatively charged in the periplasmic domain. The C-terminal
residues 581-584 fill the back side of the deepest area of the cleft at the
TM-periplasmic domain interface, critical for PhoPQ-regulated barrier function.

### Putative catalytic Asp-His dyad (D104-H114)

The PbgA TM region contains a conserved D-X9-H motif (D104, H114) characteristic
of the DUF3413 family. These residues are spatially proximal and interact in a
manner similar to catalytic centers of phospholipases. Located at the
membrane-periplasm interface near the V-shaped cleft formed by TM2 and TM3,
this putative active site could be involved in an unknown enzymatic reaction.

### C-terminal region (557-586) critical for barrier function and virulence

The C-terminal 30 amino acids of PbgA form a flexible loop (residues 557-570)
and an amphipathic helix (residues 571-582) followed by a short loop (583-586).
Deletion of residues 557-586 results in bacteria with increased OM permeability
(higher [Ethidium - Fluorescent Intercalating Dye](/xray-mp-wiki/reagents/ligands/ethidium/) bromide uptake) and significantly reduced intracellular survival
within macrophages at 18 h post-infection, mimicking the larger Delta328-586
deletion phenotype. The last residues (581-584) fill the deepest area of the cleft.


## Cross-References

- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [Ethidium - Fluorescent Intercalating Dye](/xray-mp-wiki/reagents/ligands/ethidium/) — Related ligand or cofactor
- [L-Methionine](/xray-mp-wiki/reagents/ligands/l-methionine/) — Related ligand or cofactor
