---
title: "KtrB (Potassium Transporter Membrane Subunit from Bacillus subtilis)"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12055]
verified: false
---

# KtrB (Potassium Transporter Membrane Subunit from Bacillus subtilis)

## Overview

KtrB is a membrane protein component of the KtrAB potassium transporter from the bacterium Bacillus subtilis. It assembles as a homodimer and belongs to the Trk/Ktr/HKT superfamily of ion transporters. Each KtrB monomer contains four repeat domains (D1-D4), each with a TM-P loop-TM structural motif that assembles to form an ion pore with a funnel-shaped selectivity filter. KtrB is essential for K+ uptake and plays a key role in osmotic stress resistance and high salinity tolerance. The long C-terminus of KtrB snakes into the cytoplasmic pore of the neighbouring subunit and is involved in gating regulation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12055 | 4J7C | 3.5 | Not specified | KtrB homodimer (residues 1-445) in complex with octameric KtrA-ATP ring | ATP, K+ |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: N-terminal His-tagged KtrB, tag cleaved with thrombin before complex assembly
- **Notes**: Overexpressed in LB media at 37°C for 2.5 h after [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction

### Purification Workflow

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: N-terminal His-tagged KtrB, tag cleaved with thrombin

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | LB media | 37°C for 2.5 h after [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction |
| Cell lysis and membrane extraction | Detergent solubilization | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 120 mM NaCl, 30 mM KCl + 40 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (n-dodecyl-beta-D-maltoside) | Overnight extraction at 4°C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) ([TALON](/xray-mp-wiki/reagents/additives/talon/) resin) | [TALON](/xray-mp-wiki/reagents/additives/talon/) metal affinity resin (Clontech) | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 120 mM NaCl, 30 mM KCl, 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Washed with Buffer B, eluted with 150 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag cleavage | Protease cleavage | -- |  | Incubated overnight at 4°C with thrombin for tag removal |
| Size-exclusion chromatography | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) column |  |  |

**Final sample**: ~2.5 mg/ml in Buffer B supplemented with [DDM](/xray-mp-wiki/reagents/detergents/ddm/)


## Crystallization

### doi/10.1038##nature12055

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | KtrAB complex (KtrB homodimer + [KTRA](/xray-mp-wiki/proteins/pumps-atpases/ktra/) octamer) in Buffer E supplemented with 1 mM ATP, concentrated to ~10 mg/ml, detergent exchanged to [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) |
| Reservoir | 100 mM [ADA](/xray-mp-wiki/reagents/buffers/aces/) (N-(2-acetamido)-iminodiacetic acid) pH 6.5, 20% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 200 mM ammonium sulphate |
| Mixing ratio | 1:1 |
| Temperature | 20 |
| Cryoprotection | Flash-frozen in liquid nitrogen after addition of mother liquor with 45% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 |


## Biological / Functional Insights

### KtrB homodimer architecture

KtrB assembles as a homodimer in the bacterial membrane. Each monomer contains four repeat domains (D1-D4), each with the TM-P loop-TM structural motif. The four subunits (two per monomer) assemble to form an ion pore with a funnel-shaped selectivity filter whose wider mouth (11-13 A across) faces the extracellular side and a single ion-binding site at the narrow end. The overall architecture closely resembles that of potassium channel pores.

### Intramembrane loop and gating

An intramembrane loop (connecting helices M2a to M2b in repeat D3), composed almost exclusively of glycines, alanines and serines, together with a highly conserved arginine (R417), forms a structure that blocks access between the selectivity filter and the cytoplasmic pore. This region has been proposed to function as a transporter gate; mutations or truncations in this region increase ion flux. An open pathway from the R417/intramembrane loop to the cytoplasmic face is ~4 A wide at its narrowest point.

### C-terminal domain interaction

The long C-terminus of KtrB runs from one subunit, forms a lateral contact, and snakes into the cytoplasmic pore of the neighbouring KtrB subunit, finishing just below the intramembrane loop. The last seven residues line the wall of the cytoplasmic pore of the neighbouring subunit. The highly conserved C-terminal [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (G445) has its carboxylate interacting with a lysine (K315 in KtrB) that is part of the intramembrane loop and conserved in both Ktr and Trk transporters. Sequential [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) of up to three C-terminal residues has no effect or only minor effects on K+ transport activity.

### Comparison with TrkH

The monomer and homodimer structures of KtrB and the related [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) (a Trk membrane protein) are very similar. A major difference is in the C terminus: [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) has a much shorter C terminus that does not establish contacts. In [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/), the side-chain carboxylate of a conserved glutamate (E470) occupies the same volume as the [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) carboxylate in KtrB and also interacts with the conserved lysine. Additionally, in [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) the helices M2a and M2b in repeat D1 are continuous, whereas in KtrB they are separated by an ordered amino acid stretch in the D1-D2 loop.

### Ligand binding and activation

KtrB alone allows K+ into cells but less efficiently than the full KtrAB complex. The 86Rb+ flux difference between KtrAB-ATP and KtrB (~2-fold at 30 min) is smaller than expected from K+ uptake measurements in cells (~10-fold difference in Vmax), suggesting that additional activating factors beyond ATP may be required for full transporter activity. Ktr proteins transport K+ but are also permeable to Na+, and K+ transport is ATP and Na+ dependent.


## Cross-References

- [KtrA (Cytosolic Regulatory Protein from Bacillus subtilis)](/xray-mp-wiki/proteins/pumps-atpases/ktra/) — KtrA forms the cytosolic octameric ring that associates with KtrB homodimer to form the KtrAB transporter complex
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — ATP is the activating ligand that binds to KtrA and induces conformational changes in the octameric ring
- [Adenosine Diphosphate (ADP)](/xray-mp-wiki/reagents/ligands/adp/) — ADP binds to KtrA and induces a different conformation from ATP (diamond vs square)
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM used for KtrB membrane protein extraction and solubilization
- [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/) — Cymal-6 detergent used for KtrAB complex crystallization after detergent exchange
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Tris-HCl buffer used throughout KtrB purification (pH 8.0)
- [RCK Domain Activation Mechanism](/xray-mp-wiki/concepts/structural-mechanisms/rck-domain-activation-mechanism/) — KtrA contains RCK domains that form an octameric gating ring; KtrAB activation mechanism differs from MthK and BK channels
- [Ion Channel Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — KtrB selectivity filter is funnel-shaped and shares architectural similarity with potassium channel pores
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
