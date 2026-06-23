---
title: V1-ATPase from Enterococcus hirae (EhV1)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##ncomms13235, doi/10.1038##nature11778, doi/10.1073##pnas.1108810108]
verified: false
---

# V1-ATPase from Enterococcus hirae (EhV1)

## Overview

[V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/) from Enterococcus hirae (EhV1) is a rotary molecular motor composed of A3B3DF subunits that couples  hydrolysis to Na+ pumping across membranes. The DF complex forms the central axis of the rotor, connecting the catalytic A3B3 head to the membrane-embedded c ring via the d subunit. The crystal structure of the DF complex was determined at 2.0 Å resolution, revealing a long left-handed coiled coil in the D subunit with a unique short β-hairpin region that stimulates ATPase activity two-fold, and an F subunit whose C-terminal helix binds to D by forming a three-helix bundle. Additional structures captured three distinct dwell states of the full V1 complex during the rotary catalytic cycle.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1108810108 | — | 2.0 | — | DF complex (Eh-D residues 7-194, Eh-F residues 1-101) |  |
| doi/10.1038##ncomms13235 | 5KNB | 3.3 | P2_1_2_1_2_1 | [V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/) A3B3DF complex from Enterococcus hirae expressed via E. coli cell-free system; crystal soaked with 20 μM , 3 mM MgSO4; corresponds to -binding dwell state (2ADP-bound) |  + Mg2+ |
| doi/10.1038##ncomms13235 | 5KNC | 3.0 | P2_1_2_1_2_1 | [V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/) A3B3DF complex from Enterococcus hirae; crystal soaked with 2 mM , 3 mM MgSO4; corresponds to -release dwell state (3ADP-bound) |  + Mg2+ + SO4 |
| doi/10.1038##ncomms13235 | 5KND | 2.9 | P2_1_2_1_2_1 | [V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/) A3B3DF complex; crystal soaked with 2 mM Pi, 3 mM ; Pi-bound state | Pi + Mg2+ |
| doi/10.1038##nature11778 | — | 2.8 | P2_1 | A3B3 complex (nucleotide-free eA3B3) | none |
| doi/10.1038##nature11778 | — | 3.4 | P2_1_2_1_2_1 | A3B3 complex with  (bA3B3) |  |
| doi/10.1038##nature11778 | — | 2.2 | P2_1_2_1_2_1 | [V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/) with  (eV1 high resolution) | none (nucleotide-free) |
| doi/10.1038##nature11778 | — | 3.9 | P2_1_2_1_2_1 | [V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/) without nucleotide (eV1(L)) | none |
| doi/10.1038##nature11778 | — | 2.7 | P2_1_2_1_2_1 | [V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/) soaked with  (bV1) |  |

## Expression and Purification

- **Expression system**: Escherichia coli cell-free expression system (for DF complex); E. coli cell-free system for A3B3 and DF complexes

- **Construct**: For DF complex: plasmids harboring Eh-D and Eh-F genes or a mixture of two plasmids. For full V1: A3B3 and DF complexes expressed separately with modified natural poly-histidine tag (MKDHLIHNHHKHEHAHAEH), TEV cleavage site (EHLYFQG), and linker (SSGSSG) at N-terminus.


### Purification Workflow

*Source: doi/10.1073##pnas.1108810108*

- **Expression system**: E. coli cell-free
- **Expression construct**: DF complex (Eh-D + Eh-F)
- **Tag info**: Not specified for DF complex

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell-free expression | Cell-free protein synthesis | — |  | More than 15 mg of DF complex synthesized using 27 mL reaction solution with 0.1 mg of plasmids.  used for phasing. |
| Purification | As previously described (ref 11) | — |  | Eh-D was unstable, could not concentrate beyond 0.1 mg/mL. Low concentration Eh-D immediately reconstituted with A3B3. |
**Yield**: >15 mg per 27 mL reaction

### Purification Workflow

*Source: doi/10.1038##ncomms13235*

- **Expression system**: E. coli cell-free
- **Expression construct**: A3B3 and DF complexes separately; modified natural poly-histidine tag (MKDHLIHNHHKHEHAHAEH), TEV cleavage site, SSGSSG linker
- **Tag info**: His-tag with TEV cleavage site

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | HisTrap HP column | HisTrap HP (GE Healthcare) | 50 mM  Hcl]] pH 8.0, 750 mM NaCl, 5 mM 2-mercaptoethanol, 10 mM  (binding); 50 mM  Hcl]] pH 8.0, 300 mM NaCl, 5 mM 2-mercaptoethanol, 500 mM  (elution) | Loaded with buffer A, eluted with buffer B |
| Size exclusion chromatography | SEC | — | 20 mM  Hcl]] pH 8.0, 200 mM NaCl, 10 mM , 1 mM , 5 mM 2-mercaptoethanol | Peak fractions from Ni-NTA pooled |

**Final sample**: 20 mM  Hcl]] pH 8.0, 200 mM NaCl, 10 mM , 1 mM , 5 mM 2-mercaptoethanol


## Crystallization

### doi/10.1073##pnas.1108810108

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | 10 mg/mL DF complex in 20 mM  Hcl]] pH 8.0, 150 mM NaCl, 2 mM  |
| Reservoir | 0.1 M - pH 6.5, 18% -3350, 0.2 M sodium nitrate |
| Mixing ratio | 1:1 (0.5 μL protein + 0.5 μL reservoir) |
| Temperature | 293 |
| Cryoprotection | Cryogenic temperature (100 K) during data collection |
| Notes | -labeled crystals. Data collected at SPring-8 BL41XU. Phased by MAD at wavelengths 0.9791, 0.9794, 1.000 Å. Data processed with Mosflm and Scala. |

### doi/10.1038##ncomms13235

| Parameter | Value |
|---|---|
| Method | Crystal soaking |
| Protein sample | Purified nucleotide-free [V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/) A3B3DF complex (eV1) crystals |
| Reservoir | 100 mM -NaOH pH 6.0, 1.6 M [Ammonium Sulfate](/xray-mp-wiki/reagents/ammonium-sulfate/), 10% (v/v)  |
| Temperature | 293 |
| Notes | Crystals soaked with various nucleotide concentrations. For 2ADP-V1: 20 μM , 3 mM MgSO4, 4.5 h soak. For 3ADP-V1: 2 mM , 3 mM MgSO4, 4.5 h soak. For Pi-bound: 2 mM Pi, 3 mM , 5.0 h soak. |


## Biological / Functional Insights

### DF complex structure reveals β-hairpin function

The D subunit of EhV1 comprises a long left-handed coiled coil (~100 Å) with a unique short β-hairpin region (residues 89-108). Deletion of the β-hairpin reduced ATPase activity by approximately half, indicating it stimulates activity two-fold. The β-hairpin is not essential for binding of DF to A3B3 (Kd 4.6  vs 0.8  for wild-type), but enhances maximal velocity of  hydrolysis.

### F subunit C-terminal helix forms three-helix bundle with D

The C-terminal α-helix of the F subunit (residues 85-97) forms a three-helix bundle with the coiled coil of the D subunit. This C-terminal helix was previously believed to extend into the catalytic A3B3 complex as a regulatory region, but the structure shows it contributes to tight binding to D. The dissociation constant of A3B3D and F is 3.2 .

### Model of entire rotor complex

Based on the DF complex structure and previously determined c ring and d subunit structures, a model of the entire rotor complex (DFdc ring) was built. The electrostatic surface of DF is largely acidic, while the central cavity of the c ring is basic. The d subunit has a basic concave face that binds the acidic DF bottom (Kd = 82 ), and an acidic convex face that docks into the basic c ring cavity. The relatively weak DF-d interaction (compared to A3B3-D at 0.8 ) may be responsible for the unique regulation of V-ATPases by reversible dissociation.

### Three dwell states of V1 rotary motor

The crystal structures reveal three distinct states in the rotational cycle: catalytic dwell (2ATP-V1/eV1), -binding dwell (2ADP-V1), and -release dwell (3ADP-V1). In 2ADP-V1, two  molecules bind to the 'bound' and 'tight' forms, inducing cooperative conformational changes of the third site to a 'bindable-like' form. In 3ADP-V1, all three nucleotide-binding sites are occupied by .

### ADP-binding induces cooperative conformational changes

[ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) reveals that  binds with high affinity (Kd ~9-40 ) to two sites but very low affinity to the third. In contrast,  shows three distinct binding zones with cooperative changes. Binding of  to the 'tight' form induces the adjacent 'empty' form to become a 'bindable-like' (-accessible) conformation, enabling subsequent  binding and continuation of the rotary cycle.

### Proposed 120-degree rotation model for EhV1

The 120-degree rotation model for EhV1 differs substantially from the [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) rotational mechanism. Pi is released first after  hydrolysis (differing from F1 where  release may come first). The DF axis tilts during the cycle. The model involves:  hydrolysis at the 'tight' form, Pi release, the adjacent 'empty' form becoming 'bindable-like', new  binding inducing the 'bound' form and releasing , and a 120-degree rotation with ~25 pN· torque.


## Cross-References

- [V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/) — Related rotary ATPase; comparative structural analysis
- [Yeast V1-ATPase from Saccharomyces cerevisiae](/xray-mp-wiki/proteins/pumps-atpases/yeast-v1-atpase/) — Eukaryotic V1-ATPase for comparative structural analysis
- [Rotary ATPase Mechanism](/xray-mp-wiki/concepts/rotary-atpase-mechanism/) — EhV1 is a rotary molecular motor
- [Binding-Change Mechanism](/xray-mp-wiki/concepts/binding-change-mechanism/) — Underlies the rotary catalysis of V1-ATPase
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Referenced in enterococcus-hirae-v1-atpase text
- [Selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/) — Referenced in enterococcus-hirae-v1-atpase text
- [ADP](/xray-mp-wiki/reagents/ligands/adp/) — Referenced in enterococcus-hirae-v1-atpase text
- [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Referenced in enterococcus-hirae-v1-atpase text
- [Amp Pnp](/xray-mp-wiki/reagents/amp-pnp/) — Referenced in enterococcus-hirae-v1-atpase text
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in enterococcus-hirae-v1-atpase text
