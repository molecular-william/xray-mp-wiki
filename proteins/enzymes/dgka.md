---
title: "E. coli Diacylglycerol Kinase (DgkA)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NATURE12179, doi/10.1038##NCOMMS10140]
verified: false
---

# E. coli Diacylglycerol Kinase (DgkA)

## Overview

Diacylglycerol kinase (DgkA) from Escherichia coli is a 121-residue integral membrane enzyme that catalyses the ATP-dependent phosphorylation of diacylglycerol ([DAG](/xray-mp-wiki/reagents/lipids/dag/)) to phosphatidic acid. For half a century, DgkA has served as a model for investigating membrane protein enzymology, folding, assembly, and stability. The crystal structure reveals a homo-trimeric enzyme with three transmembrane helices (H1-H3) and an N-terminal amphiphilic surface helix per monomer. The three active sites are of the composite, shared-site type, formed between adjacent subunits. The structure was determined by the lipidic cubic phase (in meso) method using 7.8 [MAG](/xray-mp-wiki/reagents/lipids/mag/) as host lipid, with phases obtained by Se-Met SAD.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NATURE12179 | 3ZE4 | 2.05 |  | DgkA Delta7 (Ala41Cys Cys46Ala Ile53Val Ile70Leu Met96Leu Val107Asp Cys113Ala) with 7.8 [MAG](/xray-mp-wiki/reagents/lipids/mag/) | [MAG](/xray-mp-wiki/reagents/lipids/mag/) (monoacylglycerol) |
| doi/10.1038##NCOMMS10140 | 4UXX | 2.7 | P3321 | DgkA Delta4 construct (I53C I70L M96L V107D) co-crystallized with 9.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/) and soaked with zinc-ACP; ternary complex with ACP (non-hydrolysable [ATP](/xray-mp-wiki/reagents/ligands/atp/) analogue) and lipid substrate bound in active site asBC | Zinc-ACP (adenylylmethylenediphosphonate), [MAG](/xray-mp-wiki/reagents/lipids/mag/) (monoacylglycerol lipid substrate) |

## Expression and Purification

- **Expression system**: E. coli B893(DE3) methionine auxotroph pTrcHisB vector
- **Construct**: Wild-type dgkA Delta4 (Ile53Cys Ile70Leu Met96Leu Val107Asp) and Delta7 mutants cloned into pTrcHisB using NcoI and EcoRI sites

### Purification Workflow

#### Source: doi/10.1038##NATURE12179


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein production | Auto-induction or [Iptg](/xray-mp-wiki/reagents/additives/iptg/) induction in E. coli | -- | -- + -- | DgkA proteins expressed and purified as described with an additional size-exclusion chromatography step; Se-Met labelling performed using methionine auxotroph B893(DE3) in M9 minimal media |

#### Source: doi/10.1038##NCOMMS10140


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and purification | Auto-induction in E. coli | -- | -- + -- | Delta4-DgkA expressed and purified as previously described (Nature 2012); co-crystallized with 9.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/) host lipid in LCP; zinc-ACP soaked into crystals |


## Crystallization

### doi/10.1038##NATURE12179

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (in meso) crystallization |
| Protein sample | DgkA (Delta7 Delta4 or wild-type) at 12 mg/ml reconstituted into 7.8 [MAG](/xray-mp-wiki/reagents/lipids/mag/) cubic mesophase |
| Temperature | 4 |
| Cryoprotection | Direct snap-cooling in liquid nitrogen |
| Notes | Crystals grown in glass sandwich plates; initial trials with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (9.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/)) at 20 C yielded minute crystals; optimization with shorter-chain [MAG](/xray-mp-wiki/reagents/lipids/mag/) (7.8 [MAG](/xray-mp-wiki/reagents/lipids/mag/)) at 4 C gave quality crystals; 50 nl protein-lipid mesophase + 800 nl precipitant |

### doi/10.1038##NCOMMS10140

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (in meso) crystallization |
| Protein sample | Delta4-DgkA reconstituted into 9.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/) cubic mesophase at 4 degrees C |
| Temperature | 4 |
| Cryoprotection | Direct snap-cooling in liquid nitrogen |
| Notes | Co-crystallized with 9.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/) host lipid; soaked with zinc-ACP to obtain ternary complex; also obtained room-temperature SFX structure using XFEL (Delta7 construct with 7.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/)) |


## Biological / Functional Insights

### Homo-trimeric architecture with shared active sites

DgkA forms a homo-trimer with approximate three-fold symmetry. Each subunit has a bundle of three transmembrane helices (H1-H3) arranged as an isosceles triangle when viewed from the cytosol. The trimer core consists of H2 from each subunit forming a parallel three-helix bundle. The active sites are composite and shared between subunits: active site AB is formed by the surface helix of subunit A and H1-H3 of subunit B. This matches the biochemical evidence from subunit mixing experiments showing that DgkA has three active sites per trimer with moderate heteroallostery.

### Active site architecture

The putative active site is located at the interface between the N-terminal surface helix of one subunit and the transmembrane helices of an adjacent subunit. Bound [MAG](/xray-mp-wiki/reagents/lipids/mag/) (monoacylglycerol) density in the Delta7 structure identifies the lipid substrate binding region. [ATP](/xray-mp-wiki/reagents/ligands/atp/) was docked with the adenyl moiety interacting with the cytosolic loop and the triphosphate extending toward the lipid-binding pocket. Divalent cations (Zn2+ found coordinated by Glu28 and Glu76) are required for full activation.

### Comparison with solution NMR model

The crystal structure differs significantly from the published solution NMR model of DgkA, particularly in that domain swapping is absent in the crystal structure. In the NMR model, H3 from one subunit contacts H1 and H2 from an adjacent subunit, whereas in the crystal structure, H2 from each subunit forms the trimer core with H1 and H3 extending outward. This results in different active site architecture between the two models.

### Osmotic stress sensor hypothesis

DgkA is probably activated in vivo under hypo-osmotic conditions to enhance production of the osmoregulant membrane-derived oligosaccharide. The N-terminal amphiphilic surface helix connected to H1 by a short hinge may act as a sensor of osmotic stress by responding to bilayer thickness and lateral pressure, adjusting active site architecture and enhancing kinase activity.

### Ternary complex structure and catalytic mechanism

The DgkA ternary complex with ACP (non-hydrolysable [ATP](/xray-mp-wiki/reagents/ligands/atp/) analogue) and lipid substrate reveals a direct in-line phosphoryl transfer mechanism. The gamma-phosphate of [ATP](/xray-mp-wiki/reagents/ligands/atp/) is positioned ~4 A from the 1-OH of the lipid substrate. Glu69 acts as the catalytic base, abstracting a proton from the lipid 1-OH to create a reactive alkoxide that attacks the gamma-phosphorus. The pentavalent transition intermediate is stabilized by Asn72 and/or Arg9.

### Active site comparison with protein kinase A

Striking resemblance exists between DgkA and cAMP-dependent protein kinase A (PKA): Glu69 (DgkA) vs Asp166 (PKA) as catalytic base; Lys94 vs Lys72 for alpha-phosphate coordination; Asp80 vs Glu91 stabilizing the catalytic lysine; Glu76 vs Asp184 chelating metal ions; Asn72 vs Asn171 stabilizing the transition state. This suggests convergent evolution of the kinase active site architecture.

### Zinc coordination in the active site

Two zinc ions (Zn1, Zn2) are bound to ACP, coordinated by Glu28, Glu76, and the triphosphate moiety. Zinc serves the same role as magnesium in other kinases - electrostatic binding to the gamma-phosphate renders the phosphorus more susceptible to nucleophilic attack. Zn1 coordinates alpha- and beta-phosphates while Zn2 coordinates beta- and gamma-phosphates.

### Room-temperature SFX validation

Serial femtosecond crystallography (SFX) at an X-ray free-electron laser (XFEL) confirmed the ternary complex structure at room temperature, ruling out radiation damage artefacts. Alternative conformers for Glu34, Glu69, and Glu76 were observed at RT, suggesting functionally relevant conformational states involved in the catalytic cycle and product release.


## Cross-References

- [Monoolein (9.9 MAG)](/xray-mp-wiki/reagents/lipids/monoolein/) — Host lipid for initial in meso crystallization trials
- [Lipidic Cubic Phase (In Meso) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used to obtain DgkA structures
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Used for Se-Met SAD phasing
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Detergent in enzyme assay mixture
- [DAG](/xray-mp-wiki/reagents/lipids/dag/) — Referenced in context related to DAG
- [MAG](/xray-mp-wiki/reagents/lipids/mag/) — Referenced in context related to MAG
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Referenced in context related to ATP
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in context related to Iptg
- [MPD](/xray-mp-wiki/reagents/additives/mpd/) — Referenced in context related to MPD
- [Acetate](/xray-mp-wiki/reagents/buffers/acetate/) — Referenced in context related to Acetate
- [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) — Component of enzyme assay buffer
- [PIPES Buffer](/xray-mp-wiki/reagents/buffers/pipes/) — Buffer used in kinase and ADP assays
- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Phasing method for Delta7 structure
- [Dgka](/xray-mp-wiki/proteins/enzymes/dgka/) — Referenced in context related to Dgka
