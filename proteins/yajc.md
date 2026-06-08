---
title: E. coli YajC Transmembrane Protein
created: 2026-05-28
updated: 2026-05-28
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2007.09.023]
verified: false
---

# E. coli YajC Transmembrane Protein

## Overview

YajC is a single transmembrane (TM) protein from Escherichia coli that associates with the AcrB multidrug efflux pump. The crystal structure of the AcrB:YajC complex (PDB 2RDD) revealed YajC as a single elongated TM helix of approximately 37 residues that docks into a highly conserved cavity on the surface of the AcrB trimer. YajC interacts with TM helices 2, 7, 11, 12, and Iα2 of AcrB. Deletion of yajc in E. coli results in a modest increase in susceptibility to beta-lactam antibiotics, suggesting a functional role in the AcrB-mediated efflux system. YajC is known to also interact with SecD and SecF, components of the protein translocase machinery.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2007.09.023 | 2RDD | 3.5 A | P3221 | YajC single transmembrane helix (residues 20-40 modeled), associated with AcrB trimer | Ampicillin |

## Expression and Purification

- **Expression system**: E. coli (endogenous)
- **Construct**: Wild-type YajC, endogenous expression from JM109 strain
- **Notes**: YajC was identified as the novel TM subunit copurifying with endogenous AcrB. The transmembrane region was predicted to cover residues 20-40 with the C terminus on the cytoplasmic side. N-terminal (18 residues) and C-terminal (56 residues) were not modeled due to lack of electron density.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane isolation | Cell disruption with X-Press, membrane fractions collected by ultracentrifugation at 185,000 x g for 90 min | -- | -- + -- | E. coli JM109 strain grown in LB media with 100 mg/L ampicillin for 16 hr |
| Solubilization | Membrane solubilization | -- | -- + 1.75% n-Dodecyl-beta-D-maltopyranoside (DDM) | Membranes solubilized in 1.75% DDM (Anatrace) |
| Ni-affinity chromatography | Ni-affinity chromatography (Chelating Sepharose Fast Flow) | Chelating Sepharose Fast Flow (GE Healthcare) | 60 mM NaPO4 (pH 7.5), 0.7 M NaCl, 33 mM imidazole, 1 mM beta-mercaptoethanol, 0.03% DDM + 0.03% DDM | AcrB bound to Ni2+ media overnight; unbound material washed out. Endogenous AcrB co-purified with YajC transmembrane subunit. |
| Elution | Ni-affinity chromatography elution | Chelating Sepharose Fast Flow (GE Healthcare) | 30 mM NaPO4 (pH 7.5), 0.1 M NaCl, 10 mM imidazole, 1 mM beta-mercaptoethanol, 0.03% DDM (elution with 150 mM imidazole) + 0.03% DDM | AcrB eluted with 150 mM imidazole |
| Size exclusion chromatography | Size exclusion chromatography (Sephacryl S300 16/60) | Sephacryl S300 16/60 (GE Healthcare) | 20 mM HEPES (pH 7.0), 150 mM NaCl, 0.03% DDM + 0.03% DDM | SEC used to improve sample homogeneity. Protein concentrated to 10 mg/mL prior to crystallization. |


## Crystallization

### doi/10.1016##j.str.2007.09.023

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 10 mg/mL AcrB:YajC complex in 20 mM HEPES (pH 7.0), 150 mM NaCl, 0.03% DDM |
| Reservoir | 14%-28% PEG1000 or PEG1500, 0.1 M Tris (pH 7.5), 0.1 M Li2SO4, 18 mM n-Octyl-beta-D-Thioglucopyranoside, 20% 1,2,3-heptanetriol |
| Mixing ratio | equal volumes protein to reservoir |
| Temperature | 293 K |
| Growth time | 3-4 days |
| Cryoprotection | 20% w/v glycerol in reservoir solution, 2 min incubation |
| Notes | Crystals reached maximum size of 0.4 x 0.2 x 0.2 mm. Data collected at 100 K at ESRF ID14-2 beamline. Space group P3221 with unit cell dimensions a=145.1, b=145.1, c=511.6 A, alpha=90, beta=90, gamma=120. Rcryst 27.9%, Rfree 31.7%. The structure revealed YajC as a 37-residue single TM helix interacting with TM helices 2, 7, 11, 12, and Iα2 of AcrB. Six ampicillin molecules were observed bound in the central cavity of the AcrB trimer. |


## Biological / Functional Insights

### YajC interaction with AcrB

YajC associates with the AcrB trimer as a single elongated transmembrane helix that
is approximately 54 A long and extends across the entire width of the membrane. The
helix is highly tilted with respect to the membrane plane. YajC docks into a cavity
formed by TM helices 2, 7, 11, 12, and Iα2 of AcrB. The average Cα-to-Cα distance
from YajC to AcrB is 7.3 A, comparable to the distance between the gamma subunit and
the TM helix bundle of the SecY complex (6.5 A). The binding interface on AcrB is one
of the most conserved regions on its surface, suggesting that YajC:AcrB interaction
may be found in species other than E. coli.

### Conformational twist of the AcrB porter domain

The AcrB:YajC complex structure revealed a significant rotation of the AcrB porter
domain relative to its transmembrane domain. This twist is consistent with the
"twist-to-open" hypothesis for TolC activation, where a specific rotation of the
porter domain could be communicated by AcrA to the superhelical coils of TolC near
the equatorial domain, inducing a twist that opens the exit duct. This represents
another dynamic motion inherent to AcrB, complementary to the cyclic peristaltic
mechanism revealed by asymmetric structures.

### Functional role of YajC in drug resistance

Growth experiments with yajc-deleted E. coli strains showed a modest increase in
susceptibility to beta-lactam antibiotics (ampicillin and nafcillin). However, the
magnitude of this effect did not scale with the relative AcrB transport affinity of
the different beta-lactams, and the functional role of the YajC:AcrB interaction
could not be conclusively assigned. The enhanced susceptibility cannot arise from
failure to translocate beta-lactamase into the periplasm since the deletion strain
does not contain any beta-lactamase.

### YajC classification and conservation

YajC was assigned by mass spectrometry as the novel TM subunit of AcrB. Three
independent mass spectrometry approaches confirmed YajC as the only plausible
candidate. The transmembrane region was predicted by MEMSAT3, Phobius, and TMHMM
to cover residues 20-40. The sequence shows modest homology (14% identical) to the
gamma subunit of the SecY complex, which shares a similar structural arrangement.
SecD and SecF, which are known to interact with YajC, are classified as RND
transporters and are fused into a single polypeptide forming an arrangement similar
to AcrB in certain bacteria.


## Cross-References

- [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/acrB/) — YajC forms a stable complex with AcrB; crystal structure determined together (PDB 2RDD)
- [AcrA multidrug efflux pump periplasmic protein](/xray-mp-wiki/proteins/acra/) — AcrA is the periplasmic adaptor in the AcrAB-TolC efflux complex; hypothesized to interact with YajC
- [Thermus thermophilus SecY Core Channel Subunit](/xray-mp-wiki/proteins/secy/) — YajC structural analogy with the gamma subunit of the SecY translocation channel
- [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) — Ampicillin co-crystallized with AcrB:YajC complex; six molecules observed in the central cavity
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM used for solubilization and purification of the AcrB:YajC complex
