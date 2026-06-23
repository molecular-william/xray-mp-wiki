---
title: Aquifex aeolicus TatC
created: 2026-05-28
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2013.03.004, doi/10.1038##NATURE11683]
verified: false
---

# Aquifex aeolicus TatC

## Overview

TatC is the largest and most conserved integral membrane protein component of the twin-arginine translocation (TAT) pathway in bacteria. It serves as the initial binding site for signal sequences containing a conserved twin-arginine motif prior to pore assembly. The crystal structure of TatC from the thermophilic bacterium Aquifex aeolicus reveals a distinctive cupped-hand architecture with seven transmembrane helices that form a lipid-exposed pocket for signal sequence recognition.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2013.03.004 | 4HTS | 4.0 | P4122 | Aquifex aeolicus TatC; full-length; expressed in E. coli; solubilized in DHPC | None |
| doi/10.1016##j.str.2013.03.004 | 4HTT | 6.8 | I4122 | Aquifex aeolicus TatC; full-length; expressed in E. coli; solubilized in DDM | None |
| doi/10.1038##NATURE11683 | TBD | 3.5 | H32 | Aquifex aeolicus TatC; N-terminal 8 residues removed (MSQEKLPE); expressed in E. coli Lemo56(DE3); solubilized in LMNG; Se-MAD phasing | None |

## Expression and Purification

- **Expression system**: Escherichia coli Lemo56(DE3)
- **Construct**: Aquifex aeolicus TatC; N-terminal 8 residues removed (MSQEKLPE); N-terminal octahistidine-tagged GFP fusion (TatC-GFP-8His); TEV protease-cleavable linker

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and induction | IPTG induction | -- | Terrific Broth; 50 ug/mL kanamycin; 0.1 mM IPTG | Cells cultured at 37 C to OD600=5.0, induced with 0.1 mM IPTG, cultured 16 h at 24 C |
| Membrane preparation | Differential centrifugation | -- | -- | Cells disrupted by homogenization (Emulsifex C5); membranes recovered by differential centrifugation |
| Solubilization | Detergent solubilization | -- | 1% w/v LMNG; PBS; 20 mM imidazole | Solubilized at 4 C for 2 h |
| Affinity purification | Ni-NTA affinity chromatography | 5 mL Ni-NTA column (Qiagen) | PBS; 0.02% LMNG; 25-250 mM imidazole gradient | Washed with 25 mM imidazole, eluted with 250 mM imidazole |
| TEV protease cleavage | Protease cleavage | -- | 2 mg His-tagged TEV protease; 5 mM sodium citrate pH 6.3; 0.3 mM oxidized glutathione; 3 mM reduced glutathione | Dialysed overnight against SEC buffer at 4 C |
| Removal of His-tags | Ni-NTA affinity chromatography | 5 mL Ni-NTA column | SEC buffer (20 mM HEPES pH 7.5; 150 mM NaCl; 0.02% w/v LMNG) | Removed His-tagged GFP and His-tagged TEV protease |
| Size exclusion chromatography | Size-exclusion chromatography | Superdex 200 16/60 column (GE Healthcare) | SEC buffer (20 mM HEPES pH 7.5; 150 mM NaCl; 0.02% w/v LMNG) | Final peak fractions concentrated to ~8 mg/mL |


## Crystallization

### doi/10.1038##NATURE11683

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Aquifex aeolicus TatC solubilized in LMNG; ~8 mg/mL |
| Reservoir | 0.02 M NaCl; 0.02 M sodium acetate pH 4.0; 33% v/v PEG 200 |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Space group H32; cryoprotected in mother liquor; data collected at Diamond light source (Beamline I04-1) at 120 K; Molprobity Score 3.1 (84th percentile for structures 3.5 A +/- 0.25 A) |


## Biological / Functional Insights

### Seven transmembrane helix architecture

The A. aeolicus TatC structure reveals seven transmembrane helices (TM1-TM7), with TM1 forming an interfacial helix (helix 1b) on the periplasmic side. The six canonical transmembrane helices, with the exception of the C-terminal half of TM2 following the kink, are tilted at angles between 20 and 40 degrees to the membrane normal. TM5 and TM6 are too short to span the membrane bilayer fully. The overall shape resembles a cupped hand with transmembrane helices forming a curved wall overhung by the periplasmic cap.

### Periplasmic cap structure

The periplasmic face features elaborate loops including the interfacial helix 1b and succeeding loop into TM2, making extensive interactions with the TM3-TM4 loop. This creates a structured periplasmic cap that stabilizes the relative positions and tilted orientations of the transmembrane helices. The presence of the cap explains why insertions and deletions in this region are not tolerated and why these loops are hotspots for inactivating mutations.

### Signal peptide binding site (surface site 1)

Two clusters of conserved and functionally important residues on the surface of TatC correspond to sites of interactions with partner proteins. Surface site (1) on the cytoplasmic face of TM1-TM3 coordinates the twin-arginine-containing signal peptide via negatively charged amino acids Glu 9 and Glu 96, which are appropriately positioned to coordinate the positively charged guanidinium groups of the sequential arginine residues of the signal peptide.

### Glu 165 in the hydrophobic bilayer interior

The side chain of Glu 165 is exposed at the centre of the concave face, placing an ionisable group in the hydrophobic interior of the bilayer. This residue is highly conserved as glutamate or glutamine. In MD simulations Glu 165 is hydrated and perturbs the local bilayer environment by attracting a lipid head group, suggesting that Glu 165 has an interaction partner in the cell. Glu 170 equivalent in E. coli TatC substitution with alanine severely compromises overall Tat transport activity.

### TatB and TatA interaction sites

The TatB binding site is localized to the opposite end of the TatC molecule from the signal peptide binding site. Crystallographic contacts between TatC molecules in the crystal show packing of an inverted TM5 from one TatC molecule against the proposed TatB contact site in the other, demonstrating that a transmembrane helix with the same orientation as TatB(TM) can pack at this site. This provides a model for the TatB(TM)-TatC complex.

### Limited conformational flexibility

Crystallographic B-factors suggest that A. aeolicus TatC has very restricted structural flexibility. MD simulations in a phospholipid bilayer show limited deformation modes. TatC is unlikely to undergo large conformational changes as typically found in small-molecule transporters. This rigidity may be important for maintaining the membrane permeability barrier during transport of folded proteins.

### TM5-TM6 bilayer distortion

TM5 and TM6 are too short to span the membrane bilayer fully, and in MD simulations the membrane is distorted inwards at the ends of these helices. The restricted length of these helices is probably required, in part, to accommodate the TatB partner, and the bilayer distortion caused by TM5 and TM6 may assist in forming the protein translocation pathway.


## Cross-References

- [Thermus thermophilus SecY Core Channel Subunit](/xray-mp-wiki/proteins/secretion-translocon/secy/) — TM3 of TatC is reminiscent of SecE TM in the SecY translocon, suggesting a role in stabilization
- [Thermus thermophilus SecE Accessory Subunit](/xray-mp-wiki/proteins/secretion-translocon/sece/) — SecE TM structure is mentioned as a structural analogue for TatC TM3
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — LMNG used to solubilize TatC for crystallization (doi/10.1038##NATURE11683)
- [Polyethylene Glycol (PEG 200)](/xray-mp-wiki/reagents/additives/peg/) — PEG 200 used as crystallization precipitant
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — NaCl component of TatC crystallization buffer
- [4-(2-Hydroxyethyl)-1-Piperazineethanesulfonic Acid (HEPES)](/xray-mp-wiki/reagents/buffers/hepes/) — HEPES component of TatC SEC buffer
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — SeMet used for Se-MAD phasing of TatC structure
- [Twin-Arginine Translocation (TAT) Pathway](/xray-mp-wiki/concepts/transport-mechanisms/tat-pathway/) — TatC is the central signal peptide binding component of the TAT pathway
