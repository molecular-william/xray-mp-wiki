---
title: Porin B (PorB) from Corynebacterium glutamicum
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [porin, membrane-protein, xray-crystallography]
sources: [doi/10.1016##JMB.2008.04.017]
verified: false
---

# Porin B (PorB) from Corynebacterium glutamicum

## Overview

Porin B (PorB) is an alpha-helical porin from Corynebacterium glutamicum, a mycolata bacterium with a mycolic acid cell wall layer similar to the outer membrane of Gram-negative bacteria. PorB forms an anion-selective channel in the bacterial outer envelope. The crystal structure was determined at 1.8 A resolution (crystal form I) using a platinum derivative for phasing, with 16 independent molecular structures solved in four different crystal forms. The core structure consists of 70 residues forming four alpha-helices tied together by a disulfide bridge (Cys22-Cys81). The native channel is proposed to be a pentameric oligomer based on conductivity measurements and crystal packing analysis. This is the first reported alpha-helical porin in a bacterial outer envelope, as all other known porins from mycolata consist of beta-barrels.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##JMB.2008.04.017 | 2K5A (Form I), 2K5B (Form II), 2K5C (Form III), 2K5D (Form IV) | 1.8 A (Form I), 2.9 A (Form II), 3.2 A (Form III), 4.2 A (Form IV) | P41212 (I), P6522 (II), P43212 (III), P6422 (IV) | Mature PorB (99 residues, 10,638 Da); 70-residue core (residues 18-87) defined in all forms | 42 Zn2+ ion sites; platinum derivative; [cacodylate](/xray-mp-wiki/reagents/buffers/cacodylate/) |

## Expression and Purification

- **Expression system**: Escherichia coli (recombinant expression as GST fusion)
- **Construct**: PorB fused to glutathione S-transferase (GST), cleaved with [factor Xa](/xray-mp-wiki/reagents/enzymes/factor-xa/) protease; 3 additional N-terminal linker residues (Gly, Ile, Leu) retained

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| GST affinity chromatography | [Affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) using GST affinity column (GE Healthcare) | Glutathione-Sepharose | Buffer A: 140 mM [sodium chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 2.7 mM KCl, 10 mM [sodium phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) pH 7.3, 0.1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf/), Benzonase | GST fusion protein expressed in E. coli; cleaved on-column with factor Xa (11 U per gram wet cells) in buffer B |
| Size-exclusion chromatography | [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) using S75-26/60 SEC column (GE Healthcare) | Sephacryl S-75 | 150 mM [sodium chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl pH 8.0 | Separated monomer (11 +/- 2 kDa, major peak) from dimer/trimer (29 +/- 3 kDa, minor peak); only monomer peak yielded analyzable crystals. Purification performed without detergent. |


## Crystallization

### doi/10.1016##JMB.2008.04.017

| Parameter | Value |
|---|---|
| Method | Sitting-drop and hanging-drop vapor diffusion |
| Protein sample | PorB monomer peak at 1.0-3.5 mg/mL |
| Reservoir | Multiple crystal forms with different conditions (see Tables in paper); screens from [Hampton Research](/xray-mp-wiki/reagents/crystallization-hampton-research/), Jena Bioscience, and Emerald |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Reservoir buffer with [MPD](/xray-mp-wiki/reagents/additives/mpd/) increased by 2% (v/v); shock-frozen in nitrogen at 100 K |
| Notes | Four crystal forms obtained from monomer peak material; dimer/trimer peak yielded only disordered crystals. Platinum derivatives obtained by adding solid K2Pt(NO2)4 to the drop. |


## Biological / Functional Insights

### Pentameric channel model

The native PorB channel is proposed as a C5-symmetric pentamer based on conductivity measurements (0.7 nS), anion selectivity, and crystal packing analysis. Contact type C from crystal forms (polar interior, nonpolar exterior) was expanded from C2 to C5 symmetry. The channel is ~40 A long, matching the [mycolic acid](/xray-mp-wiki/concepts/mycolic-acid/) layer thickness. Arg42 defines the channel constriction. The channel is inactivated by [citrate](/xray-mp-wiki/reagents/buffers/citrate/) (chelating divalent cations) and by EDTA (~35 mM), suggesting the native channel is stabilized by divalent metal ion cross-links.

### Alpha-helical porin architecture

PorB represents a novel porin architecture: all four alpha-helices surround a nonpolar interior with a conserved disulfide bridge (Cys22-Cys81). The strictly conserved core residues (Cys22, Gly33, Leu44, Ala45, Ala75, Arg77, Ala78, Cys81, Gly82, Val84) maintain structural stability. The N- and C-terminal extensions (29 residues total) are highly variable in conformation across crystal forms but conserved in sequence, suggesting a role in oligomerization.


## Cross-References

- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC used to separate monomer from dimer/trimer peaks using Sephacryl S-75 column
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — GST affinity column (Glutathione-Sepharose) used for initial purification
- [Tris (Tris-HCl buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Used in SEC buffer (50 mM Tris-HCl pH 8.0)
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Major salt component in all purification buffers
- [Calcium Chloride (CaCl2)](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Required for factor Xa cleavage (1 mM CaCl2 in buffer B)
- [PMSF (Phenylmethylsulfonyl fluoride)](/xray-mp-wiki/reagents/additives/pmsf/) — Used as protease inhibitor during cell lysis (0.1 mM)
- [Cacodylate (Sodium Dimethylarsenate)](/xray-mp-wiki/reagents/buffers/cacodylate/) — Observed as bound ligand in crystal form I contact type C dimers alongside Zn2+ ion sites
- [MPD (2-Methyl-2,4-pentanediol)](/xray-mp-wiki/reagents/additives/mpd/) — Used as cryoprotectant for all crystal forms (increased by 2% v/v)
