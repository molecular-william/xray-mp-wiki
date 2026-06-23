---
title: Maltose Transporter (MalFGK2, Escherichia coli)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12232]
verified: false
---

# Maltose Transporter (MalFGK2, Escherichia coli)

## Overview

The [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter (MalFGK2) is an [ATP](/xray-mp-wiki/reagents/ligands/atp)-binding cassette (ABC) importer in Escherichia coli responsible for [Maltose](/xray-mp-wiki/reagents/additives/maltose) and malto-oligosaccharide uptake. It consists of two transmembrane subunits ([MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/malF) and [MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/malG)) forming the substrate translocation pathway and two cytoplasmic [ATP](/xray-mp-wiki/reagents/ligands/atp)-binding cassette subunits ([MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK)) that hydrolyze [ATP](/xray-mp-wiki/reagents/ligands/atp) to power transport. The transporter undergoes conformational changes between inward-facing (resting) and outward-facing (pre-translocation) states, driven by [ATP](/xray-mp-wiki/reagents/ligands/atp) binding and hydrolysis at the [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK) dimer interface. MalFGK2 is uniquely inhibited by the regulatory protein EIIA^Glc through carbon catabolite repression, where two EIIA^Glc molecules bind to the [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK) subunits and lock the transporter in an inward-facing conformation, preventing the NBD closure required for [ATP](/xray-mp-wiki/reagents/ligands/atp) hydrolysis.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12232 | not specified | 3.9 | not specified | Full MalFGK2 complex with two EIIA^Glc molecules (residues 19-168 of EIIA^Glc) | EIIA^Glc (regulatory protein, 2 molecules) |
| doi/10.1038##nature12232 | 3FH6 | not specified | not specified | Resting state MalFGK2 (nucleotide-free, inward-facing) | none |

## Expression and Purification

- **Expression system**: E. coli HN741
- **Construct**: MalF/MalG (Ampicillin^R), MalK (Chloramphenicol^R), lacIq (Spectinomycin^R) on compatible plasmids; MalK has C-terminal 6x-His tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | Terrific Broth with [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin), [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol), spectinomycin + -- | Grown at 37 C to D600nm = 0.7-0.9, induced with 50 uM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg) at 22 C for 20 h |
| Membrane isolation | High-pressure homogenization and centrifugation | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 100 mM NaCl, 5 mM [Magnesium Chloride (MgCl₂)](/xray-mp-wiki/reagents/additives/mgcl2), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + -- | 80,000g for 40 min to isolate membrane fraction |
| Membrane solubilization | Detergent solubilization | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 100 mM NaCl, 5 mM [Magnesium Chloride (MgCl₂)](/xray-mp-wiki/reagents/additives/mgcl2), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 0.3% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Solubilized at 5 mg/ml total protein concentration |
| Affinity chromatography | Cobalt-affinity chromatography | Cobalt-affinity resin (Clontech) | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 200 mM NaCl, 0.012% [DDM](/xray-mp-wiki/reagents/detergents/ddm) + 0.012% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | His-tag affinity purification of [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK) |
| Size-exclusion chromatography | Size-exclusion chromatography (SEC) | Superdex 200 (GE Healthcare) | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 200 mM NaCl, 0.012% [DDM](/xray-mp-wiki/reagents/detergents/ddm) + 0.012% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Final polishing step |

**Final sample**: Not specified
**Yield**: Not specified


## Crystallization

### doi/10.1038##nature12232

| Parameter | Value |
|---|---|


## Biological / Functional Insights

### EIIA^Glc locks transporter in inward-facing state

Two EIIA^Glc molecules bind to the cytoplasmic ATPase subunits ([MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK)), stabilizing the transporter in an inward-facing conformation. Each EIIA^Glc is wedged between the NBD of one [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK) and the regulatory domain of the opposite [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK), linking these two domains together and preventing NBD closure. The [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK) subunits resemble tweezers with regulatory domains as fulcrum points; EIIA^Glc fastens the tweezers open. By preventing closure of the NBDs, EIIA^Glc prevents formation of the outward-facing conformation, a key step for [ATP](/xray-mp-wiki/reagents/ligands/atp) hydrolysis and [Maltose](/xray-mp-wiki/reagents/additives/maltose) translocation.

### EIIA^Glc binding site is distant from functional sites

The EIIA^Glc-binding sites on [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK) are distant from the Walker A motifs that bind [ATP](/xray-mp-wiki/reagents/ligands/atp), the [Maltose](/xray-mp-wiki/reagents/additives/maltose)-binding site in [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/malF), and the periplasmic loops to which MBP docks. This confirms that EIIA^Glc is a classical Monod-Wyman-Changeux allosteric inhibitor. All mutations that render resistance to EIIA^Glc inhibition reside in the [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK) subunit, with five making direct interactions with EIIA^Glc in the crystal structure.

### MWC allosteric inhibition mechanism

The structure reveals that EIIA^Glc binds to an allosteric site on the [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK) regulatory domain and NBD, stabilizing the open (inward-facing) dimer conformation. In the outward-facing state, the two NBDs contact each other with two ATPs buried along the NBD interface. EIIA^Glc prevents this closure by physically linking the NBD of one [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK) to the regulatory domain of the opposite [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK), thus inhibiting the transport cycle at the ATPase level.


## Cross-References

- [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malF/) — Transmembrane subunit; forms substrate translocation pathway
- [MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malG/) — Transmembrane subunit; contains P3 loop for substrate scoop
- [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) — ATP-binding subunit; EIIA^Glc binds to MalK NBD and regulatory domain
- [MBP (Escherichia coli Maltose-Binding Protein)](/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/) — Periplasmic binding protein; docks onto MalF/MalG and stimulates ATP hydrolysis
- [EIIA^Glc (Escherichia coli Enzyme IIA^Glc)](/xray-mp-wiki/proteins/abc-transporters/eiiaglc/) — Regulatory protein; allosteric inhibitor of MalFGK2
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization and purification
- [DMPC (1,2-Dimyristoyl-sn-glycero-3-phosphocholine)](/xray-mp-wiki/reagents/lipids/dmpc/) — Lipid component of bicelles used for crystallization
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — EIIA^Glc acts as a classical MWC allosteric inhibitor of the transporter
- [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) — Iptg used in purification or crystallization buffer
- [Magnesium Chloride (MgCl₂)](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Mgcl2 used in purification or crystallization buffer
