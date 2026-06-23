---
title: "EIIA^Glc (Escherichia coli Enzyme IIA^Glc)"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12232]
verified: false
---

# EIIA^Glc (Escherichia coli Enzyme IIA^Glc)

## Overview

EIIA^Glc (Enzyme IIA^Glc) is a central signaling protein in the Escherichia coli phosphotransferase system (PTS) that mediates carbon catabolite repression. It is a 168-residue protein that exists in a phosphorylated and unphosphorylated form depending on cellular carbon source availability. Unphosphorylated EIIA^Glc directly binds to and inhibits several non-PTS sugar transporters including the maltose transporter (MalFGK2), lactose permease (LacY), [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose) permease (MelB), and raffinose permease (RafB). The N-terminal 18 residues are disordered in the crystal structure but function as a membrane anchor. The phosphorylation site His90 lies at a canonical surface that also interacts with glycerol kinase, HPr, and EIIB^Glc.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12232 | 4JBW | 3.9 | not specified | EIIA^Glc residues 19-168 (N-terminal 18 residues disordered) in complex with MalFGK2 | MalFGK2 ([Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter, ABC transporter) |
| doi/10.1038##nature12232 | 1F3G | not specified | not specified | Free EIIA^Glc (used as search model for [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement)) | none |

## Expression and Purification

- **Expression system**: E. coli BL21 (DE3) Star
- **Construct**: Full-length EIIA^Glc or Delta(1-18) truncation mutant; N-terminal 10x-His tag with [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease) cleavage site

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | Luria-Bertani medium + -- | Grown at 37 C until D600nm = 0.6-0.8, induced with 100 uM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg) at 16 C for 20 h |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | Cobalt-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | Cobalt-affinity resin (Clontech) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl + -- | Ni2+-[IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) for His-tagged EIIA^Glc |
| Tag removal | [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease) cleavage | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl + -- | [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease) removes N-terminal 10x-His tag |
| Ion-exchange chromatography | Ion-exchange chromatography | Source 15Q (GE Healthcare) | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 200 mM NaCl + -- | FPLC purification |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) (SEC) | Superdex 75 (GE Healthcare) | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 200 mM NaCl + -- | Final polishing step |

**Final sample**: Not specified
**Yield**: Not specified


## Crystallization

### doi/10.1038##nature12232

| Parameter | Value |
|---|---|


## Biological / Functional Insights

### Allosteric inhibition of maltose transporter

Two EIIA^Glc molecules bind to the cytoplasmic ATPase subunits (MalK) of the [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter, stabilizing it in an inward-facing conformation and preventing the structural rearrangements necessary for ATP hydrolysis. Each EIIA^Glc is wedged between the NBD of one MalK and the regulatory domain of the opposite MalK, linking these two domains together. Of the 1,500 A^2 buried surface area on EIIA^Glc, approximately 55% is buried at the NBD interface and 45% at the regulatory domain interface. EIIA^Glc is a classical Monod-Wyman-Changeux allosteric inhibitor of the maltose transporter.

### Canonical binding surface with promiscuous interactions

The NBD of MalK binds to a canonical surface of EIIA^Glc that also interacts with [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) kinase, EIIB^Glc, and histidine protein (HPr). Of the 17 residues making contacts with the NBD, 11 are shared with these other partners (Val 39, Val 40, Phe 41, Ile 45, Val 46, Lys 69, Phe 71, Glu 72, Phe 88, His 90, and Val 96). Most interface residues are hydrophobic, consistent with the promiscuous interactions this surface makes with different proteins.

### Phosphorylation prevents transporter binding

The phosphorylation site His90 is located at the EIIA^Glc-MalK interface and is in its unphosphorylated form, hydrogen bonded with Gln122 of MalK. Adding a negatively charged phosphate group to the side chain of His90 would disrupt the interface, thus relieving the [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter from inducer exclusion.

### N-terminal membrane anchor function

The N-terminal 18 residues are disordered in the crystal structure. Studies of synthetic peptides showed that residues 3-10 form an amphipathic helix in the presence of detergent micelles or lipid vesicles, functioning as a membrane anchor. The first ordered residue Thr19 is approximately 20 A outside the lipid bilayer. The IC50 of full-length EIIA^Glc (1.61 uM) differs by 60-fold from the Delta(1-18) [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation) mutant (91 uM), consistent with the N-terminal region increasing the effective EIIA^Glc concentration at the membrane.


## Cross-References

- [Maltose Transporter (MalFGK2)](/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/) — Primary target of EIIA^Glc inhibition; complex structure solved in this paper
- [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) — EIIA^Glc binds to [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK) NBD and regulatory domain interfaces
- [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malF/) — TM subunit of the [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter complex
- [MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malG/) — TM subunit of the [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter complex
- [Carbon Catabolite Repression](/xray-mp-wiki/concepts/miscellaneous/carbon-catabolite-repression/) — EIIA^Glc is the key regulatory protein in CCR in E. coli
- [Inducer Exclusion](/xray-mp-wiki/concepts/miscellaneous/inducer-exclusion/) — Mechanism by which EIIA^Glc inhibits sugar transporters
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in MalFGK2 purification for complex formation
- [DMPC (1,2-Dimyristoyl-sn-glycero-3-phosphocholine)](/xray-mp-wiki/reagents/lipids/dmpc/) — Lipid component of bicelles used for complex crystallization
- [Immobilized Metal Affinity Chromatography (IMAC)](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) — Purification method used in protein preparation
- [Size-Exclusion Chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) — Purification method used in protein preparation
