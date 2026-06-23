---
title: Escherichia coli Site-2 Protease Homolog RseP (EcRseP)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1126##sciadv.abp9011]
verified: false
---

# Escherichia coli Site-2 Protease Homolog RseP (EcRseP)

## Overview

EcRseP is the E. coli homolog of [Site-2 Protease (mjS2P) from Methanocaldococcus jannaschii](/xray-mp-wiki/proteins/enzymes/mjs2p/) (S2P), a conserved zinc metalloprotease family that performs [Intramembrane Proteolysis](/xray-mp-wiki/concepts/intramembrane-proteolysis/) of transmembrane substrates. EcRseP catalyzes the second step of the extracytoplasmic stress response by cleaving the anti-sigma factor RseA after its periplasmic region has been removed by DegS. It contains a conserved catalytic core with a zinc-binding HEXXH motif, an MRE beta-sheet, two tandem periplasmic PDZ domains that serve as a size exclusion filter, and a PCT (PDZ C-terminal) region with two helices (H1 and H2). The crystal structure of EcRseP in complex with the peptide-mimetic inhibitor  revealed the architecture of a group I S2P family member with extracytoplasmic PDZ domains.


## Structure Determination

No structure determined.

## Expression and Purification

- **Expression system**: E. coli C43(DE3)
- **Construct**: Full-length EcRseP with C-terminal TEV-His8-Myc-PA tag
- **Induction**: 0.1 mM  at 30°C for 4 hours
- **Media**: LB medium with 50 ug/ml 

### Purification Workflow

- **Expression system**: E. coli C43(DE3)
- **Expression construct**: Full-length EcRseP with C-terminal TEV consensus sequence, His8 tag, Myc epitope, and PA tag
- **Tag info**: C-terminal TEV-His8-Myc-PA, TEV cleaved for crystallization

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | — | 10 mM  Hcl]] pH 7.4, 150 mM NaCl | Lysed cells centrifuged at 40,000g for 45 min, supernatant ultracentrifuged at 200,000g for 90 min |
| Membrane solubilization | Detergent extraction | — | 40 mM  Hcl]] pH 8.5, 150 mM NaCl + 1%  monododecanoate (SM) | Equal volume of solubilization buffer added to membrane suspension |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Ni-NTA agarose | 20 mM  Hcl]] pH 8.0, 300 mM NaCl, 10%  + 0.03% , 0.006% [CHS](/xray-mp-wiki/reagents/cholesterol-hydrogen-succinate/) | Wash with 50 mM , elute with 300 mM ; His8 tag cleaved with [TEV Protease (Tobacco Etch Virus Protease)](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) overnight at 20°C |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | Superdex 200 10/300 GL | 20 mM  Hcl]] pH 8.0, 300 mM NaCl, 10%  + 0.03% , 0.006% [CHS](/xray-mp-wiki/reagents/cholesterol-hydrogen-succinate/) |  added to SEC buffer for co-crystallization |
| Reverse Ni-NTA | Ni-NTA (flow-through) | — |  | Tag-cleaved protein collected in unbound fraction after TEV cleavage |


## Crystallization

### doi/10.1126##sciadv.abp9011

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | EcRseP- complex |
| Reservoir | Not specified in extracted text |
| Temperature | 20°C |
| Notes | Crystals obtained in space group P1, diffracted to 3.20 A resolution; data collected at SPring-8 BL32XU |


## Biological / Functional Insights

### Gating mechanism for substrate entry

The PDZ tandem, PCT-H2, and TM4 form a gate that regulates substrate access to the active center. In the gate-closed conformation, the active center is covered and inaccessible. Upon substrate binding, the PDZ tandem separates from the PCT region, and PCT-H2 with TM4 move away, exposing the substrate-binding site.

### Substrate unwinding and clamping

The substrate TM segment is unwound by strand addition to the MRE beta-sheet and clamped at the active center by conserved residue N394, which forms a hydrogen bond with the substrate backbone. This mechanism appears conserved across S2P family members and other intramembrane protease families.

### Three-step substrate accommodation model

EcRseP regulates substrate cleavage through three processes: (1) size exclusion by the PDZ tandem restricting bulky intact substrates, (2) gating by PDZ tandem/PCT-H2/TM4 rearrangement, and (3) unwinding of the substrate TM helix by the MRE beta-sheet edge strand.


## Cross-References

- [Kangiella koreensis RseP (KkRseP)](/xray-mp-wiki/proteins/enzymes/kkrsep/) — Orthologous S2P used for comparative structural analysis
- [Batimastat](/xray-mp-wiki/reagents/ligands/batimastat/) — Peptide-mimetic inhibitor bound in crystal structure
- [Intramembrane Proteolysis](/xray-mp-wiki/concepts/intramembrane-proteolysis/) — EcRseP is a member of the S2P family of intramembrane proteases
- [Site-2 Protease Family Mechanism](/xray-mp-wiki/concepts/site-2-protease-family-mechanism/) — EcRseP is the defining bacterial group I S2P member
- [GlpG Rhomboid Intramembrane Protease](/xray-mp-wiki/proteins/enzymes/glpg/) — Another intramembrane protease family with analogous gating mechanism
- [Batimastat](/xray-mp-wiki/reagents/batimastat/) — Referenced in ecrsep text
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in ecrsep text
- [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) — Referenced in ecrsep text
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in ecrsep text
- [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) — Referenced in ecrsep text
