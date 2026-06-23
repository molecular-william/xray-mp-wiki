---
title: "Kangiella koreensis Site-2 Protease Homolog (KkRseP)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1126##sciadv.abp9011]
verified: false
---

# Kangiella koreensis Site-2 Protease Homolog (KkRseP)

## Overview

KkRseP is an ortholog of E. coli RseP from the marine bacterium Kangiella koreensis (strain DSM 16069). It is a group I site-2 protease (S2P) family member that performs [Intramembrane Proteolysis](/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-proteolysis/). KkRseP restored the growth deficiency of E. coli rseP mutant cells and cleaved substrates containing TM segments from E. coli RseA, confirming functional conservation. Crystal structures were determined in two crystal forms in complex with [Batimastat](/xray-mp-wiki/reagents/ligands/batimastat/), revealing a PDZ-open conformation distinct from the PDZ-closed conformation of [ECRSEP](/xray-mp-wiki/proteins/enzymes/ecrsep/), suggesting domain rearrangements may occur during substrate accommodation.


## Structure Determination

No structure determined.

## Expression and Purification

- **Expression system**: E. coli C43(DE3) with pRARE2
- **Construct**: Full-length KkRseP with C-terminal TEV-His8 tag
- **Induction**: 0.1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 16°C for 18 hours
- **Media**: LB medium (native) or M9 medium (SeMet) with 50 ug/ml [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) and 34 ug/ml [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/)

### Purification Workflow

- **Expression system**: E. coli C43(DE3) + pRARE2
- **Tag info**: C-terminal TEV-His8, cleaved with TEV for crystallization

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | — | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 150 mM NaCl | Lysed cells centrifuged at 20,000g for 30 min, supernatant ultracentrifuged at 200,000g for 60 min |
| Membrane solubilization | Detergent extraction | — | 40 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Incubation at 4°C for 1 hour |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Ni-NTA agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Wash with 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), elute with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag removal | TEV protease cleavage | — |  | His8 tag cleaved by TEV protease overnight at 20°C; dialyzed against 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) buffer |
| Reverse Ni-NTA | Ni-NTA (flow-through) | — |  | Tag-cleaved KkRseP collected in unbound fraction |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | [Batimastat](/xray-mp-wiki/reagents/ligands/batimastat/) added to SEC buffer |


## Crystallization

### doi/10.1126##sciadv.abp9011

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | KkRseP-[Batimastat](/xray-mp-wiki/reagents/ligands/batimastat/) complex |
| Temperature | 20°C |
| Notes | Two crystal forms obtained: space group P1 (3.10 A) and P2_1 (3.15 A); SeMet-substituted protein used for phasing; data collected at SPring-8 BL32XU |


## Biological / Functional Insights

### PDZ-open conformation

The KkRseP structures revealed a PDZ-open conformation where the PDZ tandem is positioned further from the PCT region compared to [ECRSEP](/xray-mp-wiki/proteins/enzymes/ecrsep/). The C-terminal part of PCT (PCT-loop and H2) is disordered, and TM4 moves away to interact with the cleft between TM1 and TM3-N of a crystal packing neighbor, potentially mimicking substrate binding.

### Functional conservation across species

KkRseP cleaves E. coli RseA substrate and restores rseP mutant growth, demonstrating functional conservation despite ~1.34 A RMSD in domain arrangement compared to [ECRSEP](/xray-mp-wiki/proteins/enzymes/ecrsep/).


## Cross-References

- [Escherichia coli RseP (EcRseP)](/xray-mp-wiki/proteins/enzymes/ecrsep/) — Orthologous S2P used for comparative structural analysis; both determined in same study
- [Batimastat](/xray-mp-wiki/reagents/ligands/batimastat/) — Peptide-mimetic inhibitor bound in crystal structure
- [Intramembrane Proteolysis](/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-proteolysis/) — KkRseP is a member of the S2P family of intramembrane proteases
- [Site-2 Protease Family Mechanism](/xray-mp-wiki/concepts/protein-families/site-2-protease-family-mechanism/) — Structural comparison provided insights into group I S2P mechanism
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
