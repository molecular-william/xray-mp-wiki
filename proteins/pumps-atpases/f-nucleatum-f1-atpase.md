---
title: F1-ATPase from Fusobacterium nucleatum
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1098##rsob.190066]
verified: false
---

# F1-ATPase from Fusobacterium nucleatum

## Overview

The [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) from Fusobacterium nucleatum is the water-soluble catalytic domain of the
F1Fo- synthase from the obligately anaerobic opportunistic periodontal pathogen
F. nucleatum. The F1-catalytic domain was expressed in E. coli, purified, and its crystal
structure determined at 3.6 A resolution. The enzyme can hydrolyse  but is partially
inhibited. The structure is similar to those of F1-ATPases from Caldalkalibacillus thermarum
(more strongly inhibited) and Mycobacterium smegmatis (very low  hydrolytic activity).
The betaE-subunit in all three enzymes is in the conventional 'open' state. In
F. nucleatum, occupancy by  in the betaE site appears to be partial (unlike
C. thermarum and M. smegmatis where betaE is occupied by  and phosphate/sulfate).
The hydrolytic activity is likely regulated by  concentration, as in mitochondria.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1098##rsob.190066 | 6q45 | 3.6 | P2_1 | F. nucleatum [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) (alpha3beta3gammaepsilon subunits, His10-tagged epsilon-subunit) |  (alpha-subunits), +Mg2+ (betaTP, betaDP), partial  or  (betaE) |

## Expression and Purification

- **Expression system**: Escherichia coli DK8 (Delta-unc) with pRARE helper plasmid
- **Construct**: F. nucleatum atpAGDC genes (alpha, gamma, beta, epsilon) cloned into pTrc99a. His10-tag with TEV cleavage site on epsilon-subunit.
- **Notes**: Expressed from pJP3 and pJP5 constructs. Cells grown in 2x YT medium with , , 0.2% . Induced with 1 mM  at 37 C for 3-4 h then 16 h at 30 C.

### Purification Workflow

- **Expression system**: Escherichia coli DK8 (Delta-unc)
- **Expression construct**: F. nucleatum [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) with His10-TEV tag on epsilon-subunit
- **Tag info**: His10 tag on epsilon-subunit, cleavable by [TEV Protease (Tobacco Etch Virus Protease)](/xray-mp-wiki/reagents/protein-tags/tevp-protease/)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane isolation | French press or sonication | — | 50 mM  Hcl]] pH 8.0, 100 mM NaCl, 20 mM , 10% , 2 mM  | Cells resuspended and lysed; membranes isolated by ultracentrifugation |
| Nickel [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | 50 mM  Hcl]] pH 8.0, 100 mM NaCl, 20-250 mM , 10% , 2 mM  | His10-tagged [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) bound and eluted with  gradient |
| [TEV Protease (Tobacco Etch Virus Protease)](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) cleavage | On-column or dialysis cleavage | — |  | His10 tag removed by [TEV Protease (Tobacco Etch Virus Protease)](/xray-mp-wiki/reagents/protein-tags/tevp-protease/); further polishing by size exclusion chromatography |


## Crystallization

### doi/10.1098##rsob.190066

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, hanging drop |
| Protein sample | 2-2.5 mg/ml [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) in 20 mM  Hcl]] pH 8.0, 100 mM NaCl, 2 mM , 10%  |
| Reservoir | 100 mM sodium  pH 6.0, 100 mM magnesium , 15.5% (w/v)  5000 monomethyl ether |
| Mixing ratio | 1:0.8:0.2 (protein:precipitant:0.2% low melting-point agarose) |
| Temperature | 18 |
| Growth time | 3-4 days |
| Cryoprotection | 30% (v/v) [Ethylene Glycol](/xray-mp-wiki/reagents/ethylene-glycol/) in reservoir buffer |
| Notes | Crystals harvested after 3-4 days. Diffraction data collected at Australian Synchrotron MX2 beamline. Four datasets merged due to radiation damage. |


## Biological / Functional Insights

### Partial ADP occupancy in betaE site

Unlike the F1-ATPases from C. thermarum and M. smegmatis where the betaE site is clearly occupied by  + phosphate (or sulfate), the betaE site in F. nucleatum shows only weak density that may be  at low occupancy or a  molecule from the crystallization buffer. This partial occupancy correlates with the intermediate level of  hydrolysis inhibition in F. nucleatum compared to C. thermarum (strong inhibition) and M. smegmatis (very low activity).

### ADP-dependent regulation of ATP hydrolysis

The  hydrolase activity of F. nucleatum [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) (specific activity 3.5 U/mg) was inhibited by Mg2+-: 2.5 mM Mg2+- inhibited 45% of activity, and 25 mM Mg2+- inhibited completely. Basal activity was stimulated 3-fold by 0.05% .  hydrolysis depended on Mg2+ or Ca2+ ions, with Ca2+ showing lower Km and higher Vmax than Mg2+. The enzyme is likely regulated by intracellular  concentration, similar to the mitochondrial enzyme.

### Structural comparison with other bacterial F1-ATPases

The F. nucleatum [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) structure (6q45) is most similar to M. smegmatis (6foc) and C. thermarum (5ik2) F1-ATPases. The gamma-subunit most closely resembles bacterial orthologues. The epsilon-subunit is in the 'down' conformation, with its two C-terminal alpha-helices lying alongside the beta-sandwich, similar to the epsilon-subunits from E. coli and C. thermarum. The betaE adenine-binding pocket has Phe-411 displaced outward by ~4 A relative to C. thermarum, explaining weaker nucleotide binding in the betaE site.

### Crystallization in sodium citrate explains potential citrate in betaE

The crystallization buffer contained 100 mM sodium  pH 6.0, and the weak density observed in the betaE nucleotide-binding site may be partially accounted for by a  molecule rather than . This ambiguity was noted by the authors and could not be definitively resolved at 3.6 A resolution.


## Cross-References

- [F1-ATPase from Caldalkalibacillus thermarum](/xray-mp-wiki/proteins/pumps-atpases/c-thermarum-f1-atpase/) — Most similar F1-ATPase structure; betaE occupied by ADP+phosphate; used as MR search model
- [Bovine F1-ATPase (Mitochondrial ATP Synthase Catalytic Domain)](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — Homologous enzyme; F. nucleatum F1-ATPase regulation by ADP concentration similar to mitochondrial enzyme
- [F1-ATPase Rotary Catalytic Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/) — The rotary catalytic mechanism is the fundamental operating principle of F1-ATPases
- [ADP](/xray-mp-wiki/reagents/ligands/adp/) — Referenced in f-nucleatum-f1-atpase text
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Referenced in f-nucleatum-f1-atpase text
- [Citrate](/xray-mp-wiki/reagents/buffers/citrate/) — Referenced in f-nucleatum-f1-atpase text
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in f-nucleatum-f1-atpase text
- [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) — Referenced in f-nucleatum-f1-atpase text
- [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/) — Referenced in f-nucleatum-f1-atpase text
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Referenced in f-nucleatum-f1-atpase text
