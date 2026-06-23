---
title: Na+/H+ Antiporter NhaA from Escherichia coli
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1085##jgp.201411219, doi/10.1038##nature03692, doi/10.1038##s41467-022-34120-z]
verified: false
---

# Na+/H+ Antiporter NhaA from Escherichia coli

## Overview

NhaA from Escherichia coli is a Na+/H+ antiporter belonging to the Major Facilitator Superfamily (MFS). It catalyzes the electroneutral exchange of one Na+ ion for two H+ ions across the cytoplasmic membrane, playing a critical role in intracellular pH homeostasis and Na+ tolerance. The protein consists of 10 transmembrane helices organized into two pseudo-symmetric domains of five helices each, reflecting an ancient gene duplication event. NhaA functions as a homodimer and is activated at alkaline pH through a pH-sensing mechanism involving His322. The structure revealed the alternating access mechanism for MFS transporters, with the substrate-binding site alternating between inward-open and outward-open conformations.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature03692 | 1YQY | 2.3 A | P 21 21 21 | Wild-type NhaA from E. coli K-12 (residues 1-393) | not specified |
| doi/10.1038##s41467-022-34120-z | 7S24 | 2.2 | P 1 | EcNhaA WT-like triple mutant (A109T, Q277G, L296M) in [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) | not specified |
| doi/10.1085##jgp.201411219 | 4AU5 | 3.7 | P 21 | Wild-type NhaA dimer from E. coli | not specified |
| doi/10.1085##jgp.201411219 | 4ATV | 3.5 | P 21 | NhaA triple mutant (A109T, Q277G, L296M) selenomethionine derivative | not specified |

 - R-work 23.2%, R-free 25.8%; Data collection: X-ray diffraction at 2.3 A resolution, solved by Se-MAD phrasing
 - R-work 20.9%, R-free 23.5%; Data collection: X-ray diffraction at 2.2 A resolution, space group P1, 2923 atoms
 - R-work 31.8%, R-free 34.2%
 - R-work 28.7%, R-free 31.3%

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Wild-type NhaA from E. coli K-12, cloned into pET vector for overexpression

### Purification Workflow

*Source: doi/10.1038##nature03692*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane fractionation | not specified | 20 mM [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl + not specified | Membrane fractions collected by ultracentrifugation |
| Solubilization | Detergent solubilization | not specified | 20 mM [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Solubilized with 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm) (n-dodecyl-beta-D-maltopyranoside) |
| Purification | Chromatography | not specified | 20 mM [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, 0.02% DDM + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Purified by chromatography; final sample in 20 mM [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, 0.02% DDM |

### Purification Workflow

*Source: doi/10.1038##s41467-022-34120-z*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane fractionation | not specified | 20 mM Tris-HCl pH 8.0, 200 mM [Potassium Acetate](/xray-mp-wiki/reagents/additives/potassium-acetate), 1 mM EDTA, 1 mM PMSF, 5 mM MgCl2, 20 ug/mL DNase I, 0.23 mg/mL lysozyme + not specified | Cells disrupted with Emulsiflex C-5; debris removed by centrifugation at 9,600xg for 30min; membranes at 185,000xg for 1h |
| Solubilization | Detergent solubilization with [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin) | not specified | 20 mM HEPES-KOH pH 8.0, 200 mM [Potassium Acetate](/xray-mp-wiki/reagents/additives/potassium-acetate), 10 mM potassium oxalate, 20% glycerol + 40 mM DDM, 2% (w/v) [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin) (18:1) | Solubilized in buffer A with DDM and [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin) |
| IMAC purification | Nickel-nitrilotriacetic acid [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) Superflow (QIAGEN) or HisTrap FF crude (GE Healthcare) | 20 mM HEPES-KOH pH 8.0, 200 mM [Potassium Acetate](/xray-mp-wiki/reagents/additives/potassium-acetate), 10 mM potassium oxalate, 20% glycerol, 1 mM DDM, 30-50 mM imidazole (wash), 250 mM imidazole (elution) + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | WT-like triple mutant (A109T, Q277G, L296M) purified with TEV-cleavable C-terminal GFP-His8 tag |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | HiLoad 16/60 Superdex200 pg column (GE Healthcare) | 20 mM MES-KOH pH 6.2, 200 mM [Potassium Acetate](/xray-mp-wiki/reagents/additives/potassium-acetate), 10 mM potassium oxalate, 20% glycerol, 0.51 mM DDM + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Concentrated to 36 mg/mL for [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) crystallization |


## Crystallization

### doi/10.1038##nature03692

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | NhaA in 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| Reservoir | [PEG 400](/xray-mp-wiki/reagents/additives/peg400) |
| Temperature | 18 C |
| Growth time | not specified |
| Notes | Crystals grew in space group P 21 21 21. Data collected and structure solved by Se-MAD phrasing at 2.3 A resolution. R-work 23.2%, R-free 25.8%. |

### doi/10.1038##s41467-022-34120-z

| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) (LCP) |
| Protein sample | EcNhaA WT-like triple mutant (A109T, Q277G, L296M) at 36 mg/mL with 2% [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin) |
| Temperature | 20 C |
| Notes | Crystals grown in [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) at pH 6.5 (active pH). Space group P1. R-work 20.9%, R-free 23.5%. 2923 atoms total. |


## Biological / Functional Insights

### Structural symmetry and gene duplication

The NhaA structure reveals a striking internal pseudo-symmetry between two halves of the protein. Transmembrane segments III, IV, and V superimpose onto segments X, XI, and XII with an RMSD of 2.8 A for CA atoms, as determined by DALI structural comparison. This symmetry supports the hypothesis that the 10-TM NhaA arose from an ancient gene duplication and fusion event. The two pseudo-symmetric domains form the core of the transport pathway, with the substrate-binding site located at their interface.

### Alternating access mechanism

NhaA operates by an alternating access mechanism, where the substrate-binding site alternates between inward-open and outward-facing conformations. The structure solved in this paper represents the inward-open conformation. The mechanism involves rigid-body movements of the core and gate domains, exposing the binding site alternately to the cytoplasmic and periplasmic sides of the membrane. This mechanism is conserved across the MFS family of transporters.

### pH-dependent activation and regulation

NhaA is activated at alkaline pH (above 7.5) to maintain intracellular pH homeostasis under alkaline stress. The pH sensor involves His322, which acts as a key residue in the pH-dependent activation mechanism. At alkaline pH, conformational changes are triggered that shift the equilibrium toward the active conformation. This regulatory mechanism allows the cell to respond dynamically to environmental pH changes.

### Homodimeric assembly and topology

NhaA functions as a homodimer in the membrane. The topology shows both N- and C-termini located on the cytoplasmic side of the membrane. The periplasmic and cytoplasmic orientation of the termini was confirmed by the crystal structure, with the periplasmic loops forming the outer boundary of the transport pathway and the cytoplasmic loops involved in regulatory interactions.

### pH gate mechanism and histidine residues

The structure at active pH 6.5 reveals that the pH sensor functions as a pH gate that opens the intracellular funnel to allow hydrated Na+ access to the ion-binding site. At active pH, residues His253, His256 (in the dimer domain) and Lys153 (in the core domain) rearrange to form new salt-bridge interactions that widen the inward-facing cavity. MD simulations showed that at pH 4.0 the funnel is too narrow for hydrated Na+, while at pH 6.5 it is wide enough. The cytoplasmic funnel remained open in MD simulations at active pH even when the binding site was modelled with protons bound.

### Salt-bridge breakage mechanism for Na+ binding

At active pH, Asp163 forms a salt bridge with Lys300. Na+ binding catalyzes breakage of this salt bridge, an essential step in the transport cycle. MD simulations showed the D163-K300 salt bridge distance shifts from ~2.6 A (intact) to >4 A (broken) as protons are released from the binding site. When Lys300 is deprotonated, Na+ may be directly coordinated by the lysine epsilon-amino nitrogen lone pair electrons, completely disrupting the salt bridge. This mechanism is less pronounced in EcNhaA than in the thermophilic homolog TtNapA, where the stronger salt bridge creates a significant activation barrier.

### Cardiolipin stabilizes the NhaA dimer

[Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin) stabilizes the NhaA homodimer and compensates for the destabilizing effect of monoolein during LCP crystallization. Arg203 and Arg204, which are thought to coordinate cardiolipin in the dimerization interface, are located proximal to the pH gating region. Mutations Arg203Ala and Arg204Ala shift the pH for activation from 6.5 to 7-7.5. Addition of cardiolipin to detergent-purified NhaA increases the apparent binding affinity of Na+.

### Salt-bridge switch mechanism for Na+ binding and transport

At low pH, Asp164 is protonated and Asp163 forms a salt bridge with Lys300. MD simulations showed that when Asp164 becomes deprotonated (active pH), Na+ ions bind spontaneously to Asp164, destabilizing the salt bridge. Asp163 switches from interacting with Lys300 to coordinating the Na+ ion. Upon Na+ release on the opposite side, the salt bridge can reform. pKa calculations suggest Asp163 is unlikely to be protonated when involved in the salt bridge, implying Lys300 may participate in proton transport.


## Cross-References

- [Major Facilitator Superfamily](/xray-mp-wiki/concepts/mfs-transporter) — NhaA is a member of the MFS, a large family of secondary transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism) — NhaA operates via alternating access between inward-open and outward-open states
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/rocker-switch-mechanism) — NhaA uses rocker-switch motions of core and gate domains for transport
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm) — Primary detergent used for NhaA membrane solubilization and purification
- [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris) — Buffer used for NhaA purification and crystallization
- [Substrate-Protonation Coupling](/xray-mp-wiki/concepts/substrate-protonation-coupling) — NhaA exchanges Na+ for H+, coupling sodium transport to proton gradient
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) — Purification method used in protein preparation
- [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) — Crystallization method used for structure determination
- [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) — Purification method used in protein preparation
- [Potassium Acetate](/xray-mp-wiki/reagents/additives/potassium-acetate) — Additive used in purification or crystallization buffers
