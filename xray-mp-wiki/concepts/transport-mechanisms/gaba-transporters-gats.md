---
title: "GABA Transporters (GATs)"
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-protein-family, concept-functional, membrane-protein, subdirectory-transport-mechanisms]
sources: [doi/10.15252##embj.2022110735]
verified: regex
---

# GABA Transporters (GATs)

## Overview
GABA transporters (GATs) are members of the neurotransmitter/sodium symporter (NSS) family (SLC6 family) that mediate the Na+/Cl--dependent reuptake of γ-aminobutyric acid (GABA), the major inhibitory neurotransmitter in the central nervous system. Four GAT isoforms exist: GAT1 (SLC6A1), GAT2 (SLC6A13), GAT3 (SLC6A11), and BGT1 (SLC6A12). GAT1 is the most abundant isoform in the brain and a primary therapeutic target for anti-epileptic drugs. GATs share the conserved LeuT-fold architecture with 12 transmembrane helices and operate via the alternating-access mechanism, but display distinct substrate recognition and inhibition profiles compared to biogenic amine transporters.


## Mechanism/Details
Unlike biogenic amine transporters (DAT, SERT, NET) that have a conserved aspartate (Asp46 in dDAT) in subsite A, GATs have a glycine at this position (Gly63 in hGAT1). This substitution accommodates the carboxylate group of GABA and GAT1 inhibitors, which coordinates the Na1 sodium ion. Subsite B in GATs is substantially occluded compared to biogenic amine transporters due to a hydrogen bond network between residues in TM3 and TM8 (e.g., Asn121, Gln422, Thr425 in dDAT_GAT), limiting the space available for hydrophobic moieties. GAT1-specific inhibitors include tiagabine (a clinical anti-epileptic), NO711, and SKF89976a, all of which are derivatives of nipecotic acid with diaryl linker moieties. The TM6 linker residue is a leucine (Leu300 in hGAT1, Phe325 in dDAT), which allows wider access to the binding pocket compared to the phenylalanine in biogenic amine transporters.


## Examples in Membrane Protein Work
- [dDAT_GAT (Engineered Construct)](/xray-mp-wiki/proteins/slc-transporters/ddat-gat/) — Engineering the GAT1 binding site into dDAT (dDAT_GAT) enabled the first X-ray structures of GAT1 inhibitors NO711 and SKF89976a bound within an NSS family member. The structures revealed how the GAT1 subsite architecture accommodates tiagabine analogs.
- GAT1 (Rattus norvegicus) — Wild-type GAT1 from rat was used for functional validation (³H-GABA uptake, inhibition assays). GAT1 shows KM of 11.4 µM for GABA and Ki values of 725 nM (tiagabine), 1.07 µM (NO711), and 7.3 µM (SKF89976a).

## Related Concepts
- [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/transport-mechanisms/nss-family/) — GATs belong to the NSS/SLC6 family of Na+/Cl--dependent transporters
- [Allosteric Site in NSS Transporters](/xray-mp-wiki/concepts/transport-mechanisms/allosteric-site-in-nss-transporters/) — SKF89976a binds to an allosteric site in the extracellular vestibule of GAT1/dDAT_GAT
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — GATs operate via the alternating-access mechanism shared across the NSS family

## Cross-References
- [dDAT_GAT (GAT1-Engineered dDAT)](/xray-mp-wiki/proteins/slc-transporters/ddat-gat/) — Engineered construct used to determine GAT1 inhibitor-bound structures
- [NO711](/xray-mp-wiki/reagents/ligands/no711/) — GAT1-specific inhibitor; tiagabine analog
- [SKF89976a](/xray-mp-wiki/reagents/ligands/skf89976a/) — GAT1-specific inhibitor; binds both primary and allosteric sites
- [Biogenic Amine Transporters](/xray-mp-wiki/concepts/transport-mechanisms/biogenic-amine-transporters/) — Structural comparison between GATs and biogenic amine transporters reveals differences in subsite architecture
