---
title: Na+,K+-ATPase (Pig Kidney)
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jsb.2010.12.004]
verified: false
---

# Na+,K+-ATPase (Pig Kidney)

## Overview

The Na+,K+-ATPase is a P-type ATPase pump that maintains the electrochemical gradient across animal cell membranes by transporting three Na+ ions out and two K+ ions into the cell per ATP hydrolyzed. It is a housekeeping enzyme essential for secondary solute transport, cell excitability, and cell volume regulation. The minimal functional unit consists of a catalytic alpha subunit and a beta subunit acting as chaperone, with a regulatory gamma subunit from the FXYD family often present in a tissue-specific manner. The pig kidney isoform was crystallized in the E2P phosphoenzyme state stabilized by the cardiotonic steroid ouabain.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jsb.2010.12.004 | 3N23 | 4.6 A | P 21 21 21 | Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma (FXYD) subunits in E2P phosphoenzyme state | Ouabain (one molecule per alpha subunit) |

## Expression and Purification

- **Expression system**: Pig (Sus scrofa) kidney cortex, native extraction
- **Construct**: Native Na+,K+-ATPase from pig kidney outer medulla; no heterologous expression tags or mutations

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Native extraction | Native extraction from pig kidney outer medulla as described in Klodos et al. (2002) [doi/10.1016##j.bbalip.2002.08.015] | -- | Buffer composition not explicitly reported in this paper; see Klodos et al. (2002) for detailed protocol + -- | Specific ATPase activity of the preparation was about 1800 umol Pi/h per mg of protein at 37 C. Phosphorylation by inorganic phosphate in the presence of Mg2+ induced high affinity binding of CTS (complex II). |


## Crystallization

### doi/10.1016##j.jsb.2010.12.004

| Parameter | Value |
|---|---|
| Method | E2P phosphoenzyme formation followed by ouabain stabilization |
| Protein sample | Purified pig kidney Na+,K+-ATPase |
| Reservoir | Phosphoenzyme formed by Pi-induced phosphorylation in the presence of Mg2+ |
| Temperature | Not explicitly reported |
| Growth time | Not explicitly reported |
| Cryoprotection | Not explicitly reported |
| Notes | The E2P state was induced by inorganic phosphate phosphorylation in the presence of Mg2+, which yields high affinity binding of ouabain (type II complex). The complex adopts P21 21 21 crystal symmetry displaying a Type I crystal packing through stacked lipid-detergent bilayers. The homology model for molecular replacement was built from the shark E2:MgF4 2-:ouabain structure (Shinoda et al., 2009), pig kidney [K2]E2:MgF4 2- structure (Morth et al., 2007), and E2:BeF3- SERCA1a structure (Olesen et al., 2007). |


## Biological / Functional Insights

### High affinity ouabain binding requires E2P conformation

The E2P:ouabain complex represents a type II high affinity complex. Ouabain binds to a site formed at transmembrane segments alphaM1-alphaM6, plugging the ion pathway from the extracellular side. The steroid binds with a stoichiometry of one molecule per alpha subunit. In the E2P conformation, the ouabain molecule appears to be shifted laterally by about 2 A towards alphaM1-2 compared to the low affinity [K2]E2:MgF4 2- complex.

### A domain rotation and alphaM1-2 movement enable high affinity binding

The A domain has rotated in response to phosphorylation and alphaM1-2 move towards the ouabain molecule, providing for high affinity interactions and closing the ion pathway from the extracellular side. Gln111 and Asn122 from alphaM1 and alphaM2 are within direct hydrogen-bonding distances from ouabain; simultaneous mutations of these residues generate a ouabain-resistant enzyme. Phe783 and Phe786 from alphaM5 stabilize the steroid ring through stacking interactions. Gly319, Val322, and Ala323 of alphaM4 surround the lactone ring.

### Phosphorylation site structure

Phosphate is covalently bound to Asp369 in the P domain as an aspartyl phosphoanhydride group, with a stabilizing Mg2+ ion. All critical residues for phosphoanhydride/Mg2+ binding and E2P state stabilization are in close proximity to Asp369, including the TGES motif (212TGES215) in the A domain, the MVTGD motif (608MVTGD612) and Lys691 in the P domain, and the DGVND motif (710DGVND714). The phosphorylation site region displays a similar arrangement to the SERCA1a E2:BeF3- structure representing the E2P ground state.

### Induced fit mechanism for CTS binding

The binding site of the E2P form has high affinity towards cardiotonic steroids (CTS) which is further improved by induced fit rearrangements. The alphaM1-2 segment in the E2P:ouabain complex is bent towards the ouabain molecule, hindering the binding of extracellular ions. This conformation is incompatible with the occluded [K2]E2:MgF4 2- state where alphaM3 and alphaM4 are pulled inward, causing steric clashes with the ouabain lactone ring.

### Beta subunit N-terminal tail visualization

An extended patch of bulging density along the cytoplasmic side of the membrane represents the N-terminal cytoplasmic tail of the beta subunit (26 residues). This structural element runs closely along the TM domain of the alpha subunit and possibly makes direct contacts with alphaM7 (around residue alphaGlu840), alphaM3 (around residue alphaHis286), and the kink region of alphaM1 (around residue alphaPhe90).

### Signal transduction network implications

The observed rearrangements of the Na+,K+-ATPase stabilized by cardiotonic steroids may affect protein-protein interactions within the intracellular signal transduction networks. The enzyme serves as a receptor for endogenous CTS found in human blood at very low concentrations. A proline-rich stretch on the alphaM1 linker is possibly involved in binding of the SH3 domain of Src kinase, and a caveolin-1 binding motif is located nearby.


## Cross-References

- [V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/v1-atpase-t-thermophilus/) — Related ATPase family; comparison of phosphorylation mechanisms between P-type and V-type ATPases
- [ADP (Adenosine diphosphate)](/xray-mp-wiki/reagents/ligands/adp/) — Related nucleotide; ATP hydrolysis drives the Na+,K+-ATPase transport cycle
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/mgcl2/) — Essential cofactor; Mg2+ required for phosphorylation and ATPase activity
- [Potassium Fluoride](/xray-mp-wiki/reagents/additives/potassium-fluoride/) — Related phosphate analog; MgF4 2- used to trap E2 state in Na+,K+-ATPase structural studies
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Common purification method for membrane protein complexes
