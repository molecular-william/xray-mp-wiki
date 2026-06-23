---
title: "MacB ABC Transporter from Acinetobacter baumannii"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-017-01399-2]
verified: false
---

# MacB ABC Transporter from Acinetobacter baumannii

## Overview

MacB from Acinetobacter baumannii is an ATP-binding cassette (ABC) transporter that functions as part of the tripartite MacA-MacB-TolC efflux complex. It actively extrudes macrolide antibiotics, virulence factors, peptides, and cell envelope precursors across both the plasma membrane and outer membrane. The crystal structure at 3.4 Å resolution reveals a homodimer in which each protomer contains a nucleotide-binding domain (NBD) and four transmembrane helices that protrude into the periplasm to form a periplasmic binding domain (PLD) for interaction with the membrane fusion protein MacA. MacB represents a structurally unique ABC transporter with the smallest number of transmembrane helices (four) among characterized ABC exporters.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-017-01399-2 | 5GKO | 3.40 | P4₁2₁2 | Full-length A. baumannii MacB (Se-Met derivative) | Se-Met |
| doi/10.1038##s41467-017-01399-2 | 5WS4 | 3.40 | P4₁2₁2 | Full-length A. baumannii MacB | ADPβS |

## Expression and Purification

- **Expression system**: E. coli C43(DE3)
- **Construct**: Full-length A. baumannii MacB with C-terminal His6-tag
- **Notes**: Expressed in E. coli C43(DE3) cells

### Purification Workflow

- **Expression system**: E. coli C43(DE3)
- **Expression construct**: Full-length A. baumannii MacB with C-terminal His6-tag
- **Tag info**: C-terminal His6-tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Ultracentrifugation | — | 50 mM Tris pH 7.0, 10% (v/v) glycerol | Membranes collected after French press lysis and low-speed centrifugation |
| Solubilization | Detergent solubilization | — | 50 mM Tris pH 7.0, 10% (v/v) glycerol + 2% (w/v) n-undecyl-β-D-maltoside (UDM) | Solubilized on ice for 1 h with protease inhibitors (Roche) |
| Affinity chromatography | Ni-NTA affinity chromatography | Chelating Sepharose resin immobilized with Ni2+ | 20 mM Tris pH 7.5, 100 mM NaCl, 25 mM imidazole, 10% (v/v) glycerol + 0.05% (w/v) UDM | Eluted with 300 mM imidazole in wash buffer |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex-200 Increase 10/300 GL | 20 mM Tris pH 7.5, 100 mM NaCl, 10% (v/v) glycerol + 0.05% (w/v) UDM | Flow rate 0.3 ml/min using AKTA explorer 10 S |

**Final sample**: ~24 mg/ml MacB in 20 mM Tris pH 7.5, 100 mM NaCl, 10% (v/v) glycerol, 0.05% (w/v) UDM
**Yield**: Not specified
**Purity**: >95% by SDS-PAGE


## Crystallization

### doi/10.1038##s41467-017-01399-2

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified MacB at ~24 mg/ml with 10 mM ADPβS and 2 mM MgCl2 |
| Reservoir | 1.2-1.3 M sodium citrate, 100 mM Na-HEPES pH 7.2 |
| Mixing ratio | 1:1 (protein:reservoir) |
| Temperature | 25 °C |
| Growth time | 1 week |
| Cryoprotection | Glycerol gradually increased to 30% (v/v) by soaking in several steps |
| Notes | Crystals grown by sitting-drop vapor diffusion technique. For Se-Met labeling, M9 minimal medium with seleno-L-methionine; 2 mM ATP added instead of ADPβS before crystallization. |


## Biological / Functional Insights

### Unique four-TM architecture of MacB

MacB has only four transmembrane helices per monomer, the smallest number among characterized ABC exporters. The TMs are not swapped between half-transporters, and the structure lacks helical extensions into intracellular domains found in most type-I ABC exporters. Despite having only one cytoplasmic loop, MacB preserves two coupling helices (CH1 and CH2). CH1 is in the intracellular loop between TM2 and TM3, while CH2 is located at the carboxy terminus. Both CHs contact only one NBD within the same monomer, unlike Sav1866 and MsbA where CHs contact opposite monomers.

### MacB defines a unique ABC transporter structural class

Comparison with other ABC transporters shows MacB is structurally distinct from both type-I and type-II ABC exporters and importers. The NBD arrangement in the MacB dimer is most similar to the ADP-bound outward-occluded state of the lipid-linked oligosaccharide flippase PglK. The periplasmic domain fold and the arrangement of TMs are unique among bacterial ABC exporters.

### Coupling helix function and importance

Removal of CH2 by truncation of the carboxy terminus of MacB leads to inactivation of drug export, demonstrating the functional importance of the coupling helices. The positions of the CHs and their interactions with the NBDs are similar to other ABC exporters, but the connecting TMs are completely different, and the order of the CHs is opposite due to topological differences.

### Tripartite complex function

MacB functions as part of the MacA-MacB-TolC tripartite complex that spans both the plasma membrane and outer membrane of Gram-negative bacteria. The complex confers resistance to macrolide antibiotics including erythromycin, clarithromycin, azithromycin, roxithromycin, and spiramycin, as confirmed by MIC measurements in drug-sensitive E. coli ΔacrAB ΔmacAB cells expressing A. baumannii MacAB-TolC.


## Cross-References

- [MacB ABC Transporter from Aggregatibacter actinomycetemcomitans](/xray-mp-wiki/proteins/abc-transporters/macb/) — Orthologous MacB from related bacterial species with structural comparison
- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — MacB is a member of the ABC transporter superfamily with unique structural features
- [Mechanotransmission](/xray-mp-wiki/concepts/miscellaneous/mechanotransmission/) — Related biological concept for MacB-type ABC transporters
- [n-Undecyl-β-D-Maltoside (UDM)](/xray-mp-wiki/reagents/detergents/udm/) — Detergent used for MacB purification and crystallization
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in purification buffers
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in crystallization reservoir
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Method used for crystallization of MacB
- [Selenomethionine SAD Phasing](/xray-mp-wiki/methods/structure-determination/semet-sad-phasing/) — Phase determination method used for MacB structure
