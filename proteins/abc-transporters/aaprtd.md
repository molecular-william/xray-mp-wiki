---
title: Aquifex aeolicus PrtD (AaPrtD) Type-1 Secretion System ABC Transporter
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.01.010]
verified: false
---

# Aquifex aeolicus PrtD (AaPrtD) Type-1 Secretion System ABC Transporter

## Overview

AaPrtD is the ABC transporter component of the Type-1 secretion system (T1SS) from the hyperthermophilic bacterium Aquifex aeolicus. T1SSs are widespread among Gram-negative bacteria and are responsible for the secretion of virulence factors including proteases, lipases, and scavenging molecules. The crystal structure at 3.15 A resolution reveals a homodimeric ABC exporter fold with each subunit containing six N-terminal transmembrane helices and a C-terminal nucleotide-binding domain (NBD). The structure is in an [ADP](/xray-mp-wiki/reagents/ligands/adp/)-bound occluded conformation. Distinctive features include highly kinked TM3 and TM6 helices that create a narrow interior channel and a highly basic concave surface formed by TM1, TM3, and TM6, which is likely involved in substrate recruitment. The structure supports a polypeptide transport mechanism distinct from alternating access.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2017.01.010 | 5L22 | 3.15 A | C1 2 1 | Full-length AaPrtD from Aquifex aeolicus, residues 11-315 and 326-559, C-terminally His-tagged, [ADP](/xray-mp-wiki/reagents/ligands/adp/)-bound, occluded conformation | [ADP](/xray-mp-wiki/reagents/ligands/adp/) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length AaPrtD from Aquifex aeolicus with C-terminal His-tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity purification | Immobilized metal affinity chromatography | Ni-NTA | Not specified + dodecyl-beta-D-maltoside (DDM) | AaPrtD expressed in E. coli and purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) via metal affinity chromatography |
| SEC | Gel-filtration chromatography | Not specified | Not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final polishing step after IMAC |


## Crystallization

### doi/10.1016##j.str.2017.01.010

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified AaPrtD in [DDM](/xray-mp-wiki/reagents/detergents/ddm/), [ADP](/xray-mp-wiki/reagents/ligands/adp/)-bound |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals optimized in the presence of [ADP](/xray-mp-wiki/reagents/ligands/adp/). Structure determined by SAD phasing using samarium [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate/)-soaked crystals and [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) chloride-soaked single-Cys mutants, and Se-Met-derivatized protein. Initial phases from SAD in ShelX. Model built in Coot and refined in Phenix. Native data to 3.15 A resolution. Unit cell: 118.6, 97.9, 179.8 A, beta=100.5 deg. |


## Biological / Functional Insights

### Distinct T1SS ABC transporter architecture

AaPrtD reveals a distinct transmembrane architecture with highly kinked TM3 and TM6 helices near the cytosolic solvent-lipid interface. These kinks, which point toward the dimer interface, create a highly basic concave bowl on the PrtD surface formed by TM1, TM3, and TM6. The TM3 kink is stabilized by a conserved FxT motif (F128, T130) that interacts with TM6 of both the same and opposite subunit, tethering the protomers together.

### Narrow interior channel

The TM helices frame a narrow channel not observed in canonical peptide ABC transporters. The narrow pore and the highly basic concave surface likely engage acidic T1SS substrates via electrostatic interactions. The structure suggests a substrate entry window just above the NBDs where TM4 separates from TM6, which would need to be flexible to accommodate passage of polypeptide stretches.

### ATP hydrolysis required for secretion

In vivo secretion assays using the homologous DdPrtDEF system from Dickeya dadantii demonstrated that [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis by PrtD is essential for substrate (PrtG) secretion. The catalytically inactive E492Q mutant retained [ATP](/xray-mp-wiki/reagents/ligands/atp/) binding but showed no secretion. Additionally, the entire T1SS complex (PrtD, PrtE, and PrtF) is required for transport across the inner membrane - neither PrtD alone nor PrtD-PrtE complex sufficed.

### Distinct from alternating access

The AaPrtD structure supports a polypeptide transport mechanism distinct from the alternating access mechanism of classical ABC exporters. The broken TM3 and TM6 helices are reminiscent of translocating ATPases such as ClpX or SecA, which interact with unfolded polypeptides at broken helix regions. This suggests that T1SS ABC transporters may use a channel-like mechanism to thread unfolded polypeptide substrates across the membrane.


## Cross-References

- [ABC Transporter Mechanism](/xray-mp-wiki/concepts/abc-transporter-mechanism/) — AaPrtD is a bacterial ABC exporter with a distinct transport mechanism
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — AaPrtD structure supports a T1SS-specific mechanism distinct from alternating access
- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Structure determined by SAD phasing using samarium, mercury, and selenium derivatives
- [Type-1 Secretion System](/xray-mp-wiki/concepts/type-1-secretion-system/) — AaPrtD is the ABC transporter component of the T1SS machinery
- [N-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for purification and crystallization of AaPrtD
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final purification step after IMAC
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — IMAC used for initial purification
- [Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/vapor-diffusion-crystallization/) — Crystallization method used for AaPrtD
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in the study
