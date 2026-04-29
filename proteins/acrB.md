---

title: AcrB
created: 2026-04-27
updated: 2026-04-27
type: protein
tags: [transporter, membrane-protein]
sources: [doi/10.1007##s10969-013-9154-x, doi/10.1016##J.JMB.2009.04.001]

---


# AcrB (Acriflavine Resistance Protein B)

## Overview

AcrB is the inner membrane resistance-nodulation-cell division (RND) efflux pump in *Escherichia coli*. It forms the core component of the AcrAB-TolC tripartite efflux system, which extrudes a broad spectrum of cytotoxic substances including antibiotics, organic solvents, dyes, and detergents directly from the cell into the extracellular medium, bypassing the periplasm. Overexpression of AcrAB-TolC is a major mechanism of multidrug resistance (MDR) in Gram-negative bacteria.

## Structure

- **PDB ID**: 4K7Q (AcrB-Linezolid complex)
- **Resolution**: 3.5 Å
- **Space group**: R32
- **Architecture**: Symmetric trimer, each monomer contains 12 transmembrane (TM) helices, a porter domain, and a TolC-binding domain
- **Conformation**: Symmetric (closed) state — not the functional alternating conformation seen in other AcrB structures

Each protomer binds one drug molecule in the upper portion of the central cavity near residues A385 and F386. The three protomers interlock via TolC-binding domains forming a funnel-like structure at the top and a connected tunnel leading to the central cavity formed by the TM domains. Three vestibules at subunit interfaces serve as substrate capture sites.

## Solubilization and Purification

- **Solubilization**: 2% [[ddm]] (n-dodecyl-β-D-maltopyranoside) from *E. coli* membranes
- **Expression**: Wild-type AcrB with C-terminal polyhistidine tag, overproduced in *E. coli* JM109
- **Purification**: Metal [[affinity-chromatography]] (His-tag) with [[imidazole]] elution (300 mM)
- **Buffers**: 20 mM [[tris-buffer]]-HCl pH 7.5, 0.3 M [[sodium-chloride]], 10% [[glycerol]], 0.2% [[ddm]] during purification

## Crystallization

- **Method**: Sitting-drop [[vapor-diffusion]]
- **Condition**: 0.1 M [[sodium-chloride]], [[sodium-phosphate]] pH 6.2, 8% [[peg-4000]]
- **Soaking**: Apo crystals soaked with 6 mM [[linezolid]] prior to data collection
- **Cryoprotectant**: Crystallization reagents plus 25% [[glycerol]]
- **Data collection**: 100 K

## Drug Binding

Linezolid binds to the A385/F386 loop in each protomer. The three aromatic rings of Linezolid lie approximately parallel to the F386 binding loop, allowing maximum hydrophobic contact. The binding interface buries approximately 140 Å² of surface. This binding site is shared with several other drugs including ethidium, nafcillin, and ampicillin — all previously found to bind to the same symmetric AcrB trimer location.

## Conformational Changes

A local conformational change of up to 4 Å in backbone position was observed at residues 670–675 (a loop at the bottom of the porter domain cleft). This loop is thought to be important for substrate transport and AcrA binding but is not near crystal contacts, suggesting a genuine ligand-induced conformational change.

## Related Systems

- **AcrA** — Periplasmic membrane fusion protein linking AcrB to TolC
- **TolC** — Outer membrane factor forming the complete efflux channel
- **Other RND pumps**: CmeAB (*Campylobacter*), AdeABC (*Pseudomonas*), MexAB-OprM (*P. aeruginosa*)
- **MexB** — *P. aeruginosa* RND exporter (69.8% identity to AcrB); asymmetric trimer with DDM bound in binding cavity

## Related Transporters

- [[mmpL3]] — Mycobacterial drug transporter (anti-TB drug target)
- [[sotb]] — E. coli antiporter (MFS family)

## References

- Murakami et al. (2002) Nature 419:587–593 — First AcrB structure
- Murakami et al. (2006) Nature 443:173–179 — Drug-bound AcrB structures
- Seeger et al. (2006) Science 313:1295–1298 — AcrB-TolC complex