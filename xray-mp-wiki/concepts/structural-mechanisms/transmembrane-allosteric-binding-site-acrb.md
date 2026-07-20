---
title: "Transmembrane Domain Allosteric Binding Pocket (TMD-BP) of AcrB"
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-functional, concept-transport-mechanism, subdirectory-structural-mechanisms]
sources: [doi/10.1038##s41467-021-24151-3]
verified: regex
---

# Transmembrane Domain Allosteric Binding Pocket (TMD-BP) of AcrB

## Overview
The transmembrane domain-binding pocket (TMD-BP) of the AcrB RND multidrug efflux transporter is a deep ~1700 A^3 cavity within the T protomer transmembrane domain, created by substantial displacement of TM11 (~13.6 degrees tilting) and TM12 (~36.7 degrees tilting) toward the periphery of the TMD. The pocket is surrounded by TM2, TM4, TM10-12 and located near the Asp407/Asp408/Lys940 proton relay residues. Co-crystallization of wild-type AcrB with an antibiotic cocktail (erythromycin, linezolid, oxacillin, and fusidic acid) revealed fusidic acid bound at this site. Thiol cross-link substrate protection assays using MTS-rhodamine labeling of Cys981 demonstrated that oxacillin and novobiocin also bind to this pocket (apparent Ki = 446 uM and 95 uM, respectively), while linezolid and chloramphenicol do not. Erythromycin induced increased MTS-rhodamine labeling, suggesting erythromycin-specific TMD alterations.


## Mechanism/Details
The TMD-BP is proposed as an allosteric site in the proton-conducting transmembrane domain of AcrB. In the absence of drugs, the T protomer TMD adopts a compact conformation. Binding of fusidic acid or other suitable drugs at the TMD-BP induces outward tilting of TM11 and TM12, creating the ~1700 A^3 cavity. This conformational change may facilitate H+ translocation via the nearby Asp407/Asp408/Lys940 proton relay residues, triggering the T-to-O state transition and enhancing catalytic efficiency. The partially induced state (observed with beta-lactam mixtures) creates a smaller 304 A^3 cavity, representing a state prior to full drug binding. The pocket is specific: fusidic acid has the highest apparent affinity (Ki = 38 uM), followed by novobiocin (95 uM) and oxacillin (446 uM). FUA-only co-crystallization conditions (without antibiotic cocktail) result in FUA binding only to the TM1/TM2 groove, not the TMD-BP, suggesting cooperativity between multiple drug binding events is required for full TMD-BP occupancy.


## Examples in Membrane Protein Work
- [AcrB Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Co-crystallization with antibiotic cocktail (erythromycin, linezolid, oxacillin, fusidic acid each at 1 mM) yielded fully induced T protomer (PDB 6ZOD) with FUA bound at TMD-BP. FUA bound to TMD-BP + TM1/TM2 groove + TM7/TM8 groove in same protomer.
- [AcrB Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Co-crystallization with beta-lactam mixture (dicloxacillin, oxacillin, piperacillin) produced a partially induced T protomer with 304 A^3 cavity (PDB 6ZOA), representing state prior to full drug binding.
- [AcrB Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Ala981Cys variant in Cys-less background used for MTS-rhodamine labeling. Labeling was concentration-dependently protected by FUA (Ki=38 uM), oxacillin (Ki=446 uM), novobiocin (Ki=95 uM); not protected by linezolid or chloramphenicol.

## Related Concepts


## Cross-References
- [AcrB Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Primary protein system where the TMD-BP was characterized
- [Peristaltic Pump Mechanism of RND Transporters](/xray-mp-wiki/concepts/transport-mechanisms/peristaltic-pump-mechanism/) — The TMD-BP is proposed to trigger the T-to-O transition during peristaltic transport
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — TMD-BP represents a novel allosteric site in a bacterial efflux pump transmembrane domain
- [Fusidic Acid](/xray-mp-wiki/reagents/antibiotics/fusidic-acid/) — Primary ligand used to characterize the TMD-BP
