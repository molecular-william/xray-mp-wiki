---
title: "Cry6Aa (Bacillus thuringiensis Pore-Forming Toxin)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, enzyme]
sources: [doi/10.1186##s12915-016-0295-9]
verified: false
---

# Cry6Aa (Bacillus thuringiensis Pore-Forming Toxin)

## Overview

Cry6Aa is a pesticidal crystal (Cry) toxin from Bacillus thuringiensis with
activity against coleopteran insects (e.g., Western Corn Rootworm Diabrotica
virgifera virgifera) and a range of nematodes including Caenorhabditis elegans,
Heterodera [Glycine](/xray-mp-wiki/reagents/buffers/glycine/), and Meloidogyne incognita. The X-ray crystal structures
of Cry6Aa in both trypsin-cleaved (2.0 A) and full-length (2.7 A) forms reveal
that Cry6Aa belongs to the alpha-helical pore-forming toxin family,
structurally homologous to hemolysin E (HlyE) from E. coli, and the B. cereus
toxins HblB and NheA (pfam05791). This represents a new structural paradigm
among B. thuringiensis Cry toxins, distinct from the well-known three-domain
Cry toxins, the aegerolysin-like Cry34, the Toxin_10 family Cry35, the
Etx/Mtx2 family Cry51, and the Cyt family toxins. The structure consists of a
bundle of long (~90 A) amphipathic alpha helices with a head domain at one
end. The putative transmembrane region (residues 250-268) forms a hairpin loop
within the head domain. In vivo pore formation assays in C. elegans confirmed
the pore-forming mechanism of action. The L259D mutation in the putative
transmembrane region abolished toxicity, consistent with a pore-forming mode
of action.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1186##s12915-016-0295-9 | 5KUC | 2.0 | P 65 | Trypsin-cleaved Cry6Aa core (residues 12-390 disulfide bonded to residues 444-475) | -- |
| doi/10.1186##s12915-016-0295-9 | 5KUD | 2.7 | P 21 21 2 | Full-length Cry6Aa (residues Met1-Asn475) | -- |

## Expression and Purification

- **Expression system**: Pseudomonas fluorescens (for crystallography); E. coli Shuffle T7 Express LysY (for recombinant production and bioassays); B. thuringiensis BMB171 (for native crystal production)
- **Construct**: Full-length Cry6Aa1 (GenBank AAA22357) from Dow AgroSciences
- **Notes**: Produced as inclusion bodies in P. fluorescens. Also soluble expression in E. coli Shuffle T7 with [Iptg](/xray-mp-wiki/reagents/additives/iptg/) induction.

### Purification Workflow

- **Expression system**: P. fluorescens (inclusion bodies)
- **Expression construct**: Full-length Cry6Aa1
- **Tag info**: Untagged

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Inclusion body preparation | Microfluidizer (16,000 psi, 2 passes) | — | 50 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 200 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.5% Triton X-100, 20 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) | Washed multiple times with lysis buffer and [EDTA](/xray-mp-wiki/reagents/additives/edta/) buffer |
| Solubilization | Solubilization at pH 11.0 | — | 25 mM CAPS pH 11.0 | Inclusion bodies solubilized at high pH |
| Anion exchange chromatography | Ion exchange | Source 15Q 16/10 | 25 mM CAPS pH 11.0, with 0-1 M NaCl gradient |  |
| Size-exclusion chromatography | SEC | Superdex 75 26/90 | 25 mM CAPS pH 11.0, 50 mM NaCl |  |

- **Expression system**: B. thuringiensis BMB171
- **Expression construct**: Cry6Aa2 in pHT304
- **Tag info**: Untagged

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Bt crystal production | Growth in Embrapa medium to >98% autolysis | — |  |  |
| Crystal purification | Discontinuous [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) density gradient ultracentrifugation | — |  | Cry6Aa crystals purified, then solubilized at pH 10.0 or pH 12.7 or pH 3.0 |


## Crystallization

### doi/10.1186##s12915-016-0295-9

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Trypsin-cleaved Cry6Aa at 100 mg/mL in 25 mM CAPS pH 11.0, 50 mM NaCl |
| Reservoir | 20% [Peg](/xray-mp-wiki/reagents/additives/peg/) 1000, 0.1 M sodium phosphate dibasic/citric acid pH 4.2, 0.2 M lithium sulfate |
| Mixing ratio | 1:1 |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Data collected at LS-CAT (APS) on Mar CCD-300 detector at 100 K |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Full-length Cry6Aa |
| Reservoir | not specified |
| Notes | Full-length structure solved at lower resolution (2.7 A). N-terminal 11 residues, C-terminal 6 residues, and some internal loops not resolved. |


## Biological / Functional Insights

### Cry6Aa is an alpha-helical pore-forming toxin

The structure of Cry6Aa reveals a bundle of five long (~90 A) amphipathic
alpha helices (alphaA, alphaC, alphaD, alphaG, alphaH) with a head domain
folded across one end. This fold is structurally homologous to hemolysin E
(HlyE/ClyA) from E. coli and the B. cereus hemolytic toxin components HblB
and NheA (pfam05791). Cry6Aa is the first B. thuringiensis Cry toxin
identified with this structural fold, representing a new paradigm among
pesticidal proteins.

### Pore-forming mechanism confirmed by in vivo assay

In vivo propidium iodide (PI) uptake assays in C. elegans demonstrated that
Cry6Aa forms pores in intestinal epithelial cells, with 41.5 +/- 9.7% of
treated worms showing PI entry compared to 1.1 +/- 1.1% for empty vector
control. Mutation of the putative transmembrane residue Leu259 to Asp
(L259D) abolished nematotoxicity, consistent with a pore-forming mechanism
of action.

### Unique structural features

Cry6Aa contains several unusual features not seen in homologous toxins:
(1) internal repeat sequences (WATIGAxI(E/Q), TTNMTSNQY, and C-terminal
WYNNSDWYNNSDWYNN repeats); (2) wing-like intra-helical loops bounded by
[Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues in helices alphaC and alphaD; (3) two disulfide bonds
(Cys88-Cys451 and Cys402-Cys404) that confer conformational rigidity;
(4) a disulfide-linked C-terminal fragment that remains attached to the
toxin core after [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) activation. The C-terminal region is absent in
Cry6Ba, which has coleopteran activity but reduced nematode toxicity.


## Cross-References

- [Alpha-Helical Pore-Forming Toxin Family](/xray-mp-wiki/concepts/protein-families/alpha-helical-pore-forming-toxin-family/) — Cry6Aa is a founding member of this structural class among B. thuringiensis Cry toxins
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Trypsin-cleaved Cry6Aa structure solved by MR using hemolysin B (PDB 2NRJ) as search model
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Referenced in the context of Glycine
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in the context of Iptg
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in the context of Tris Hcl
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in the context of Glycerol
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Referenced in the context of EDTA
- [TCEP](/xray-mp-wiki/reagents/additives/tcep/) — Referenced in the context of TCEP
- [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) — Referenced in the context of Sucrose
- [Peg](/xray-mp-wiki/reagents/additives/peg/) — Referenced in the context of Peg
