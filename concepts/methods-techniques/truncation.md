---
title: Protein Truncation for Crystallization
created: 2026-06-02
updated: 2026-06-02
type: concept
category: concepts
layout: default
tags: [concept-construct-design]
sources: [doi/10.1038##nature06163, doi/10.1038##nature12357, doi/10.1085##jgp.201711884]
verified: false
---

# Protein Truncation for Crystallization

## Overview
Protein truncation is a construct design strategy in which flexible, unstructured, or disordered regions of a protein are removed to produce a more rigid, crystallization-competent core. Many membrane proteins contain large extracellular domains, long N- or C-terminal tails, or flexible linkers that impede crystal formation. By systematically deleting these regions and identifying the minimal stable fragment, researchers can dramatically improve the chances of obtaining well-ordered crystals.


## Mechanism/Details
Flexible regions contribute entropic disorder that prevents the formation of regular crystal contacts. Truncation removes these mobile elements, reducing conformational heterogeneity and increasing the population of a single, well-defined conformation. The optimal truncation boundary must preserve the protein's structural core and functional domains while eliminating only the disordered elements. Truncation is often guided by sequence analysis (predicting disordered regions), limited proteolysis (identifying protease-resistant cores), and empirical screening of deletion variants.

## Examples in Membrane Protein Work
- **Chicken Acid-Sensing Ion Channel 1a (cASIC1a)**: Residues 1-146 (large
  extracellular N-terminal domain) were deleted, yielding delta ASIC1
  (residues 147-526). This truncated construct retained the complete
  extracellular domain (palm, wrist, finger, thumb, and beta-ball domains)
  and the full transmembrane region, but removed the unstructured N-terminal
  extension. The delta ASIC1 construct crystallized at 1.9 A resolution,
  revealing the first open state structure of an ASIC.
  [cASIC1a](/xray-mp-wiki/proteins/other-ion-channels/asic1a/)
- **Beta-2 Adrenergic Receptor**: The long C-terminal tail and parts of the
  third intracellular loop were deleted to produce a thermostabilized construct
  that crystallized in the inactive state.
  [Beta-2 AR](/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/)
- **NavAb (Arcobacter butzleri)**: C-terminal truncation of 28 residues
  (NavAbDelta28) enabled crystallization of a closed state at 2.3 A resolution,
  with preserved four-helix bundle structure. Truncation of 40 residues
  (NavAbDelta40, residues 1-226) captured an open state. Progressive truncations
  (Delta3, Delta7, Delta10, Delta28, Delta40) revealed graded effects on early
  and late phases of voltage-dependent inactivation, dissecting the functional
  roles of proximal vs distal C-terminal tail regions.
  [NavAb](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) (DOI: 10.1085/jgp.201711884)
- **Aquaporin Z**: Flexible loop regions were trimmed to produce a compact
  construct suitable for crystallographic analysis.
  [Aquaporin Z](/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/)

## Related Concepts
- [Fusion Partners (BRIL, T4 Lysozyme)](/xray-mp-wiki/concepts/fusion-partners/) —
  Alternative construct design strategy using fusion proteins to stabilize
  flexible regions
- [Domain Swapping](/xray-mp-wiki/concepts/structural-mechanisms/domain-swapping/) — Related
  construct modification strategy for improving crystallization

## Cross-References
- [Chicken Acid-Sensing Ion Channel 1a (cASIC1a)](/xray-mp-wiki/proteins/other-ion-channels/asic1a/) — First ASIC structure solved using truncated delta ASIC1 construct (residues 147-526)
- [Fusion Partners (BRIL, T4 Lysozyme)](/xray-mp-wiki/concepts/fusion-partners/) — Alternative construct design strategy for stabilizing flexible regions
