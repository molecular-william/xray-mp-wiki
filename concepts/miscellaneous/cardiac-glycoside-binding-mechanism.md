---
title: Cardiac Glycoside Binding Mechanism
created: 2026-06-10
updated: 2026-06-10
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-concepts]
sources: [doi/10.1073##pnas.0907054106, doi/10.1073##pnas.2123226119]
verified: false
---

# Cardiac Glycoside Binding Mechanism

## Overview
Cardiac glycosides (e.g., [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain), digoxin, digitoxin) are a class of steroid-like compounds that specifically inhibit the Na⁺,K⁺-ATPase by binding to a cavity formed by transmembrane helices M1-M6 near the K⁺-binding sites. This binding inhibits the ion pump, increasing intracellular Na⁺ and ultimately Ca²⁺, leading to stronger cardiac muscle contraction. The structural mechanism involves a tripartite binding interface: a lactone ring, a steroid core, and a carbohydrate moiety, each contributing differently to affinity and specificity.

## Mechanism/Details
Cardiac glycosides share a common tripartite structure consisting of: (i) a 5- or 6-membered unsaturated lactone ring attached at C17 of the steroid core; (ii) a cis-configured steroid nucleus (A/B and C/D ring junctions); and (iii) a carbohydrate (sugar) moiety of 1-4 residues attached at C3.

In the low-affinity E2·2K⁺·Pi state of Na⁺,K⁺-ATPase, ouabain binds in a cavity formed by transmembrane helices M1-M6. The lactone ring is deeply inserted near the K⁺ binding sites, with the hydroxyl at C14β forming a hydrogen bond with Thr-804 (M6), a critical residue for ouabain sensitivity. The steroid core of ouabain has three hydroxyl groups on the A- and B-rings that project toward the M1-M2 helices. Gln-118 (M1) and Asn-129 (M2) form hydrogen bonds maintaining the V-shaped M1-M2 structure. The rhamnose sugar moiety faces the extracellular medium and forms hydrogen bonds with Arg-887 (L7/8 loop) and Glu-319 (M4), conferring ~300-fold higher affinity compared to the aglycone (ouabagenin).

Ouabain binding induces conformational changes in the transmembrane helices. The M4E helix (extracellular part of M4 between Gly-335 and Gly-314) inclines ~15° away from M6, widening the binding cavity by ~5 Å. M3 moves ~45° relative to M4. These movements resemble the E2·Pi → E2P transition in Ca²⁺-ATPase.

In the high-affinity E2P-like state, the binding cavity is closed around ouabain. The M1-M2 helices come closer to form a complementary surface, stabilized by salt bridges (Asp-128-Arg-979, Asp-123/Glu-124-Arg-893). The high affinity is conferred by a hydrophobic, flat complementary interface between the glycoside and M1-M2 helices, similar to thapsigargin binding to Ca²⁺-ATPase or steroid binding to nuclear receptors.

The antagonism between cardiac glycosides and extracellular K⁺ is structurally explained: K⁺ at the transmembrane binding sites blocks closure of the binding cavity, reducing ouabain affinity from nM (E2P state) to mM (E2·2K⁺·Pi state). Nonetheless, even the low-affinity structure explains most mutagenesis data from high-affinity states, confirming essentially the same binding site.

## Examples in Membrane Protein Work
- [Na⁺,K⁺-ATPase (Shark)](/xray-mp-wiki/proteins/pumps-atpases/shark-na-k-atpase/) — Crystal structure of shark Na⁺,K⁺-ATPase with bound ouabain in E2·2K⁺·Pi state at 2.8 Å
- [Shark Na⁺,K⁺-ATPase](/xray-mp-wiki/proteins/pumps-atpases/shark-na-k-atpase/) — Cryo-EM structures of E2P states with ouabain and istaroxime at 3.4-3.9 Å

## Related Concepts
- []() — 

## Cross-References
- [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) — Prototypical cardiac glycoside; the structural basis of its inhibitory mechanism
- [Na⁺,K⁺-ATPase from Squalus acanthias (Shark)](/xray-mp-wiki/proteins/pumps-atpases/shark-na-k-atpase/) — Crystal structure providing direct structural evidence for cardiac glycoside binding mechanism
- [P-type ATPase Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/p-type-atpase-mechanism/) — Cardiac glycosides inhibit the E2P state of the P-type ATPase catalytic cycle
