---
title: Mep2 Ammonium Transceptor (S. cerevisiae and C. albicans)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms11337]
verified: false
---

# Mep2 Ammonium Transceptor (S. cerevisiae and C. albicans)

## Overview

Mep2 (methylammonium permease) proteins are fungal ammonium transceptors that function both as transporters for ammonium uptake and as sensors/receptors for nitrogen-dependent filamentous growth. Mep2 belongs to the Amt/Mep/Rh family of ammonium transporters present in all kingdoms of life. Unlike bacterial Amt proteins, which are regulated by GlnK binding, fungal Mep2 is regulated by phosphorylation of a C-terminal region (CTR) residue Ser457 (ScMep2) / Ser453 (CaMep2) by the Npr1 kinase. X-ray crystal structures of Mep2 from Saccharomyces cerevisiae and Candida albicans reveal closed, non-phosphorylated conformations with a two-tier channel block on the cytoplasmic side: ICL1 (via Tyr-His hydrogen bond with the twin-His motif) and ICL3. Structure of phosphorylation-mimicking mutants (S453D, R452D/S453D) and a truncation mutant (442Δ) show conformational changes in the CTR that suggest a mechanism for phosphorylation-dependent channel opening.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms11337 | 5AEX | 2.65 A | Not specified | ScMep2 (S. cerevisiae, residues 2-485, N4Q mutant) | none |
| doi/10.1038##ncomms11337 | 5AEZ | 2.4 A | R3 | CaMep2 (C. albicans, residues 2-480, N4Q mutant) | none |
| doi/10.1038##ncomms11337 | 5AF1 | Not specified | P3 | CaMep2 (C. albicans, residues 2-480, N4Q mutant) | none |
| doi/10.1038##ncomms11337 | 5AID | 3.4 A | Not specified | CaMep2 442Δ truncation mutant (lacking AI region residues 443-480) | none |
| doi/10.1038##ncomms11337 | 5AH3 | 2.4 A | Not specified | CaMep2 R452D/S453D (DD mutant, phosphorylation-mimicking) | none |
| doi/10.1038##ncomms11337 | 5FUF | Not specified | Not specified | CaMep2 S453D (single D mutant, phosphorylation-mimicking) | none |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae W303 pep4Δ strain (galactose-inducible expression)
- **Construct**: ScMep2 (residues 2-485, N4Q to prevent glycosylation) or CaMep2 (residues 2-480, N4Q), C-terminal His tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Bead beating or cell disruptor at 35,000 psi | — | 20 mM Tris pH 8.0, 300 mM NaCl | S. cerevisiae cells grown in synthetic minimal medium lacking histidine with 1% glucose, then switched to YP medium with 1.5% galactose for 16-20 h induction. OD600 typically 18-20. |
| Membrane preparation | Ultracentrifugation | — | 20 mM Tris pH 8.0, 300 mM NaCl | Membranes collected at 200,000g for 90 min. Membrane protein extraction in 1:1 (w/w) DDM/DM mixture, 1% total detergent, stirring overnight at 4 C. |
| Nickel affinity chromatography | IMAC | Chelating Sepharose (GE Healthcare) | 20 mM Tris pH 8.0, 300 mM NaCl, 0.2% DDM + 0.2% DDM | Washed with 15 CV buffer containing 30 mM imidazole. Eluted with 250 mM imidazole in 3 CV. |
| Gel filtration | Size-exclusion chromatography | — | 10 mM HEPES pH 7.0-7.5, 100 mM NaCl, 0.05% DDM + 0.05% DDM | Second gel filtration step for detergent exchange. CaMep2 required 0.05% decyl-maltose (DM) for diffracting crystals. |


## Crystallization

### doi/10.1038##ncomms11337

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | Purified ScMep2 or CaMep2 in detergent-containing buffer |
| Temperature | Not specified |
| Notes | ScMep2 crystallized in presence of 0.2 M ammonium ions. CaMep2: R3 and P3 crystal forms obtained. Truncation mutant 442Δ crystallized from a similar condition. DD mutant and S453D mutant crystallized at 2.4 A resolution. Data collected at Newcastle University Structural Biology Laboratory (beamline not specified). Structures solved by molecular replacement using archaeal AfAmt-1 (PDB 2B2H) as search model. |


## Biological / Functional Insights

### Two-tier cytoplasmic channel block in non-phosphorylated Mep2

In the closed, non-phosphorylated state, Mep2 exhibits a two-tier block of the cytoplasmic channel exit. First tier: ICL1 has moved inward (~10 A backbone shift) and unwound relative to bacterial Amts. The side chain hydroxyl of Tyr49 (CaMep2) / Tyr53 (ScMep2) forms a strong hydrogen bond with the epsilon-2 nitrogen of His342 (twin-His motif residue), directly closing the channel. Second tier: ICL3 is shifted up to ~10 A and forms an additional barrier. The conserved RxK motif in ICL1 (Arg54, Lys55, Lys56 in CaMep2) undergoes large conformational changes (Arg54 head group moved ~11 A, Lys55 head group moved ~20 A relative to Amt-1). This two-tier block likely ensures minimal ammonium transport under nitrogen-sufficient conditions.

### C-terminal region (CTR) and AI region structure

The CTR in Mep2 is elongated and makes relatively few contacts with the main body of the transporter compared to bacterial Amts. The phosphorylation target Ser457/453 is located in a well-defined electronegative pocket ~30 A away from the channel exit, formed by backbone carbonyl atoms of Asp419, Glu420, and Glu421 (CaMep2). The adjacent AI (autoinhibitory) region bridges the CTR and the main body of Mep2. Deletion of the AI region (442Δ mutant) results in a constitutively active channel.

### Phosphorylation-mimicking mutants show CTR conformational changes

The S453D and R452D/S453D (DD) mutants of CaMep2 show substantial conformational changes in the conserved part of the CTR. A 12-residue alpha-helix forms from Leu427 to Asp438, and the ExxGxD motif (Glu420-Leu423) undergoes rearrangement. In the DD mutant, the AI segment shows only a slight shift relative to wild-type. MD simulations (200 ns) show that the distance between Asp453 and Glu420 acidic oxygens increases from ~7 to >22 A due to electrostatic repulsion, supporting the model that phosphorylation-induced charge repulsion drives CTR conformational changes.

### Tyr-His hydrogen bond is essential for channel closure

The Tyr49-His342 (CaMep2) / Tyr53-His348 (ScMep2) hydrogen bond is the key interaction closing the Mep2 channel. In bacterial Amts, the equivalent Tyr side chain is rotated ~4 A away, leaving the channel open. The Y53A mutant in ScMep2 results in a constitutively active transporter, confirming the functional importance of this hydrogen bond. The Tyr residue is highly conserved in fungal Mep2 orthologues, suggesting this is a general mechanism for Mep2 channel closure.

### Model for phosphorylation-regulated Mep2 gating

A model is proposed where phosphorylation at Ser453 in the CTR introduces steric clashes and electrostatic repulsion that cause conformational changes in the CTR. These changes allow the CTR to interact with ICL3, which moves inward to open the channel. This is opposite to plant AMT transporters, where phosphorylation closes the channel. In Mep2, the phosphorylation site is peripheral (near the AI region), and phosphorylation drives channel opening; in plant AMTs, the phosphorylation site is central (near the ExxGxD motif), and phosphorylation drives channel closure. The model explains how intra-monomeric CTR-ICL1/ICL3 interactions regulate both fungal and plant ammonium transporters: close interactions generate open channels, while lack of interactions leads to inactive states.


## Cross-References

- [Rh/Amt/MEP Protein Family](/xray-mp-wiki/concepts/rh-amt-mep-protein-family/) — Mep2 is a member of the Amt/Mep/Rh ammonium transporter family
- [Ammonium Transporter AmtB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/amt-b/) — Bacterial orthologue used for structural comparison; bacterial Amts show open channel conformation
- [A. fulgidus Amt-1](/xray-mp-wiki/proteins/other-ion-channels/a-fulgidus-amt1/) — Archaeal orthologue used as molecular replacement search model and for structural comparison
- [Twin-Histidine Motif in Ammonium Channels](/xray-mp-wiki/concepts/twin-histidine-motif/) — The twin-His motif is essential for ammonium transport in Mep2 as in all Amt/Mep/Rh family members
