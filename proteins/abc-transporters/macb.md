---
title: MacB ABC Transporter from Aggregatibacter actinomycetemcomitans
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1712153114]
verified: false
---

# MacB ABC Transporter from Aggregatibacter actinomycetemcomitans

## Overview

MacB is an ABC transporter from Aggregatibacter actinomycetemcomitans that forms a tripartite efflux pump with the MacA adaptor protein and TolC exit duct. It belongs to the type VII ABC transporter superfamily, characterized by a unique four-transmembrane-helix topology, a periplasmic domain between TM1 and TM2, and a [Mechanotransmission](/xray-mp-wiki/concepts/mechanotransmission/) mechanism that couples cytoplasmic ATP hydrolysis to extracytoplasmic conformational change. Unlike canonical ABC transporters, MacB lacks a central transmembrane cavity and does not transport substrates across the inner membrane; instead, it powers the expulsion of macrolide antibiotics and enterotoxin STII from the periplasm to the extracellular space via a molecular bellows mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1712153114 | Not specified in text | 3.35 | P21 | Full-length AaMacB (ATP-bound) | ATP |
| doi/10.1073##pnas.1712153114 | Not specified in text | 3.90 | P6522 | Full-length AaMacB (ATP-bound) |  |
| doi/10.1073##pnas.1712153114 | 5NLI | Not specified | — | MacAB-TolC complex (nucleotide-free) |  |

## Expression and Purification

- **Expression system**: E. coli C43 (DE3)
- **Construct**: Full-length AaMacB with N-terminal His-tag
- **Notes**: Expressed in E. coli C43 (DE3) cells

### Purification Workflow

- **Expression system**: E. coli C43 (DE3)
- **Expression construct**: Full-length AaMacB with N-terminal His-tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression | — |  | Expressed in E. coli C43 (DE3) |
| Purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) and SEC | — | Lauryl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol ([LMNG](/xray-mp-wiki/reagents/detergents/lmng/)) | Purified in lauryl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol ([LMNG](/xray-mp-wiki/reagents/detergents/lmng/)) as a stabilizing detergent |


## Crystallization

### doi/10.1073##pnas.1712153114

| Parameter | Value |
|---|---|
| Method | Not specified in text |
| Protein sample | Purified AaMacB in [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) |
| Notes | Crystallized in two distinct crystal forms (P6522 and P21) in the presence of either ATPgammaS or ATP |


## Biological / Functional Insights

### Mechanotransmission mechanism of MacB

MacB defines a noncanonical ABC transporter (type VII) with a unique four-transmembrane-helix topology and a periplasmic domain. The structure of ATP-bound MacB reveals no central pore for substrate passage. Instead, reversible dimerization of the NBDs drives opening and closing of the periplasmic domains via concerted movements of TM2 and the major coupling helix — a process termed [Mechanotransmission](/xray-mp-wiki/concepts/mechanotransmission/). This contrasts with the alternating-access mechanism used by other ABC transporters.

### MacB is the type specimen for type VII ABC transporter superfamily

MacB's novel topology, dimerization interface, and transmembrane fold define it as the type VII ABC transporter superfamily. Homologs sharing these features include LolCDE (lipoprotein trafficking), FtsEX (cell division signaling), PvdT, and AatP. The LolC periplasmic domain was solved at 1.88 A and confirmed a MacB-like fold.

### Molecular bellows mechanism for MacAB-TolC efflux

The assembled MacAB-TolC complex acts as a molecular bellows. Substrates enter the interior cavity through openings between parted periplasmic domains. ATP binding causes closure of the periplasmic domain via [Mechanotransmission](/xray-mp-wiki/concepts/mechanotransmission/), reducing cavity volume and forcing contents through the MacA gate ring. ATP hydrolysis resets the system.

### MacB confers resistance to cyclic peptides

In addition to the known macrolide [Erythromycin](/xray-mp-wiki/reagents/ligands/erythromycin/), MacB confers resistance to cyclic peptides including bacitracin and colistin, expanding the known substrate range of MacB. Structure-guided mutagenesis identified a periplasmic hotspot (Tyr376, Phe444, Trp505, Thr349) essential for [Erythromycin](/xray-mp-wiki/reagents/ligands/erythromycin/) tolerance.


## Cross-References

- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for MacB purification and crystallization
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — ATP bound in the MacB NBD dimer interface; ATPgammaS used for crystallization
- [Erythromycin](/xray-mp-wiki/reagents/ligands/erythromycin/) — MacB confers resistance to erythromycin; used in functional assays
- [Mechanotransmission](/xray-mp-wiki/concepts/mechanotransmission/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) — Additive used in purification or crystallization buffers
