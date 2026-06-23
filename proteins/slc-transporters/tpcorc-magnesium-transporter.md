---
title: TpCorC Magnesium Transporter from Thermus parvatiensis
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.abe6140]
verified: false
---

# TpCorC Magnesium Transporter from Thermus parvatiensis

## Overview

CorC is a prokaryotic member of the CNNM/CorC family of Mg2+ transporters, widely distributed in all domains of life. The CorC protein from Thermus parvatiensis (TpCorC) is a Mg2+ exporter that shares approximately 30% sequence identity with the S. aureus CorC orthologs MpfA and MpfB. TpCorC consists of a DUF21 transmembrane (TM) domain (3 TM helices per protomer forming a dimer), a cytoplasmic CBS domain, and a CorC/HlyC domain. The crystal structure of the TpCorC TM domain dimer revealed a fully dehydrated Mg2+ ion binding site with octahedral coordination geometry, distinct from the hydrated Mg2+ binding in MgtE and CorA channels. The CBS domain binds ATP with high affinity (~500 nM), and ATP binding is important for Mg2+ export activity. Mg2+ transport by TpCorC is Na+-dependent, suggesting Na+-coupled Mg2+ export.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##sciadv.abe6140 | 7CFF | 2.0 | — | TpCorC TM domain V101A mutant (residues 26-182) | Mg2+ |
| doi/10.1126##sciadv.abe6140 | 7CFG | 3.2 | — | TpCorC TM domain wild-type (residues 26-182) | Mg2+ |
| doi/10.1126##sciadv.abe6140 | 7CFH | Not specified | — | TpCorC CBS domain apo form (residues 183-361) | None |
| doi/10.1126##sciadv.abe6140 | 7CFI | Not specified | — | TpCorC CBS domain ATP-bound (residues 202-361) | ATP |

## Expression and Purification

- **Expression system**: E. coli Rosetta (DE3)
- **Construct**: TpCorC TM domain (residues 26-182) with C-terminal [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/) cleavage site, GFPuv, and octahistidine tag
- **Induction**: 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600 0.6, 18C for 16 hours
- **Media**: LB medium with 50 ug/ml [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/)

### Purification Workflow

- **Expression system**: E. coli Rosetta (DE3)
- **Expression construct**: TpCorC TM domain residues 26-182 with C-terminal HRV 3C site, GFPuv, His8 tag
- **Tag info**: Octahistidine tag, cleaved by [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and harvest | Fermentation | — |  | Induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600 0.6, cultured at 18C for 16 hours, harvested at 5000g for 15 min |
| Cell disruption | High-pressure homogenization | — | 150 mM NaCl, 50 mM Tris pH 8.0, 1 mM PMSF | Cells disrupted in buffer A |
| Membrane isolation | Ultracentrifugation | — | 150 mM NaCl, 50 mM Tris pH 8.0 | Low-speed spin at 20000g for 30 min; membrane pellet isolated at 180000g for 1 hour |
| Solubilization | Detergent solubilization | — | 150 mM NaCl, 50 mM Tris pH 8.0 + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (n-dodecyl-beta-D-maltopyranoside) | Homogenized membranes solubilized for 1 hour at 4C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (Ni-NTA) | Ni-NTA agarose | Buffer B: 150 mM NaCl, 50 mM Tris pH 8.0, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Column washed with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); protein eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag cleavage and reverse IMAC | Protease cleavage and subtractive IMAC | — |  | [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/) digestion to remove His8-GFPuv tag |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) (SEC) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) Increase 10/300 GL | 150 mM NaCl, 50 mM Tris pH 8.0, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted in buffer C |

**Final sample**: TpCorC TM domain in 150 mM NaCl, 50 mM Tris pH 8.0, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)
**Yield**: Not specified
**Purity**: >95% by SDS-PAGE


## Crystallization

### doi/10.1126##sciadv.abe6140

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | TpCorC TM domain (wild-type or V101A mutant) in 150 mM NaCl, 50 mM Tris pH 8.0, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 0.1 M MgCl2, 0.1 M [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) pH 5.0, 12-18% [PEG](/xray-mp-wiki/reagents/additives/peg/) 4000 |
| Mixing ratio | 1:1 (protein:reservoir) |
| Temperature | 20C |
| Growth time | 1 week |
| Cryoprotection | Reservoir solution supplemented with 40% [PEG](/xray-mp-wiki/reagents/additives/peg/) 200 and 50 mM MgCl2 |
| Notes | Crystals appeared specifically in the presence of Mg2+ ions. Crystallization was also tested with Ca2+, Co2+, Ni2+, and Mn2+ but only Mg2+ yielded well-diffracting crystals. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | TpCorC CBS domain (residues 183-361 or 202-361) |
| Reservoir | 0.4 M ammonium thiocyanate, 0.1 M [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) pH 4.5, 15% [PEG](/xray-mp-wiki/reagents/additives/peg/) 4000; or 0.1 M CaCl2, 0.1 M HEPES pH 7.5, 5% [PEG](/xray-mp-wiki/reagents/additives/peg/) 8000 |
| Mixing ratio | 1:1 |
| Temperature | 18C |
| Cryoprotection | 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), reservoir components |
| Notes | CBS domain crystallized in apo and ATP-bound forms. ATP-bound structure used construct residues 202-361 with Y255A mutation. |


## Biological / Functional Insights

### Mg2+ binding site with fully dehydrated Mg2+ ion

The TpCorC TM domain contains a single Mg2+ binding site per protomer with fully dehydrated Mg2+ coordinated in octahedral geometry. Mg2+ is directly coordinated by side chains of Ser43, Ser47, Asn90, and Glu130 and the main chain carbonyl oxygens of Ser43 and Gly129. Bonding distances are 2.1-2.2 A, consistent with canonical Mg2+-oxygen distances. All five residues are strictly conserved in human CNNM2 and CNNM4. Alanine substitution at these positions (S43A, S47A, N90A, G129A, E130A) severely impairs or abolishes Mg2+ export activity. This fully dehydrated Mg2+ recognition contrasts with MgtE and CorA channels where Mg2+ remains hydrated, accounting for differences in transport kinetics between channels and transporters.

### Novel DUF21 TM domain fold with belt helix

The TpCorC TM domain presents a novel protein fold distinct from any previously reported membrane protein structure. Each protomer has three TM helices plus three cytoplasmic helices (CH1, CH2, and belt helix). The belt helix following TM3 is approximately 35 residues long, amphipathic, and nearly parallel to the membrane plane. It interacts with TM1 and TM2 within the protomer and with TM3 of the neighboring subunit. The protein forms a dimer with close intersubunit contacts at the periplasmic side (TM2 and TM3) but loose contacts at the cytoplasmic side, adopting an inward-open conformation.

### Na+-dependent Mg2+ transport

Mg2+ export by TpCorC is Na+-dependent. Depletion of Na+ from the bath solution induces loss of Mg2+ export activity, suggesting the Na+ gradient is a potential driving force for Mg2+ export. The dimer interface near the Mg2+ binding site, containing multiple Asn residues (Asn91, Asn94), is a candidate Na+ binding site. Asn94 is conserved in human CNNM2 and CNNM4, and the N94A mutation reduces Na+ sensitivity and Mg2+ transport activity.

### ATP binding to CBS domain regulates Mg2+ transport

The TpCorC CBS domain binds ATP with high affinity (Kd ~500 nM). ATP is bound at the interface between two tandem CBS repeats, with the adenine base recognized by hydrogen bonds with Val235 and Arg257, and stacking with Tyr255. The ribose interacts with Asp339, and phosphate groups interact with Ser256, Arg257, and Thr336. Mg2+ ions stabilize phosphate conformation. ATP-binding site mutants (Y255A, T336I) reduce ATP binding and impair Mg2+ export activity. Given cytoplasmic ATP concentrations in the millimolar range, ATP likely binds constitutively as a regulatory cofactor.

### CNNM/CorC family disease associations

All five residues of the Mg2+ binding site are strictly conserved in human CNNM2 (Ser269, Ser273, Asn323, Gly356, Glu357) and CNNM4 (Ser196, Ser200, Asn250, Gly283, Glu284). Many known disease-associated mutations in CNNM2 and CNNM4 map to the Mg2+ binding site. CNNM2 mutations cause dominant hypomagnesemia; CNNM4 mutations cause Jalili syndrome. The CNNM2 T568I mutant (corresponding to TpCorC T336I) loses both ATP binding and Mg2+ export activity.


## Cross-References

- [Magnesium Transport](/xray-mp-wiki/concepts/magnesium-transport/) — Concept for Mg2+ transport mechanisms in membrane proteins (placeholder for future creation)
- [MgtE (Magnesium Transport Channel)](/xray-mp-wiki/proteins/other-ion-channels/mgt-e-thermus-thermophilus/) — Comparison of fully dehydrated Mg2+ binding in CorC vs hydrated Mg2+ in MgtE channel
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
