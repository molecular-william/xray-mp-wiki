---
title: "VKOR from Synechococcus sp."
created: 2026-06-02
updated: 2026-06-04
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08720, doi/10.1038##ncomms4110]
verified: false
---

# VKOR from Synechococcus sp.

## Overview

VKOR ([Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) Epoxide Reductase) from Synechococcus sp. is a membrane-bound enzyme that catalyzes the reduction of [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide to [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) hydroquinone, a critical step in the [Vitamin K Cycle](/xray-mp-wiki/concepts/enzyme-mechanisms/vitamin-k-cycle/). The enzyme is the target of [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/), a widely used anticoagulant drug. The Synechococcus sp. VKOR was crystallized as a fusion protein with a thioredoxin (Trx)-like domain, with both domains connected by a proline-rich linker. The structure reveals a four-transmembrane-helix core with a unique 1/2-segment between TM1 and TM2 that contains a flexible horizontal helix. A CXXC motif (Cys130 and Cys133) in TM4 forms the active site. The enzyme uses a spring-like mechanism involving winding and unwinding motions of the horizontal helix to promote electron transfer between the Trx domain and the VKOR active site. Three distinct electron-transfer states have been captured using cysteine mutants.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature08720 | Not reported in supplementary information | 3.6 A | P61 | Full-length VKOR from Synechococcus sp. fused with thioredoxin (Trx)-like domain | [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) (UQ) in active site |
| doi/10.1038##nature08720 | Not reported in supplementary information | 1.7 A | P42121 | Isolated Trx-like domain of VKOR from Synechococcus sp. | None |
| doi/10.1038##ncomms4110 | Not reported | 3.6 A | Not specified | Cys56Ala mutant of VKOR from Synechococcus sp. fused with Trx-like domain (State II) | None |
| doi/10.1038##ncomms4110 | Not reported | 4.2 A | P21 | Cys212Ala mutant of VKOR from Synechococcus sp. fused with Trx-like domain (State III) | None |
| doi/10.1038##ncomms4110 | Not reported | 2.8 A | C2221 | Cys50Ala mutant of VKOR from Synechococcus sp. fused with Trx-like domain (State IV) | [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) in active site |

## Expression and Purification

- **Expression system**: BL21(DE3) Escherichia coli
- **Construct**: Full-length VKOR from Synechococcus sp. fused with Trx-like domain; Cys50Ala, Cys56Ala, and Cys212Ala point mutants

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent solubilization | -- | 20 mM Tris/HCl pH 7.5, 0.3 M NaCl + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membrane fraction solubilized in 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-affinity resin | 20 mM Tris/HCl pH 7.5, 0.1 M NaCl, 0.04% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.04% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted with 0.3 M [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Gel filtration chromatography | SEC column | 20 mM Tris/HCl pH 7.5, 0.1 M NaCl, 0.04% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.04% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted without [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); concentrated to approximately 20 mg/ml |


## Crystallization

### doi/10.1038##nature08720

| Parameter | Value |
|---|---|
| Method | Not explicitly reported in supplementary information |
| Protein sample | Full-length VKOR-Trx fusion |
| Reservoir | -- |
| Temperature | Not explicitly reported |
| Growth time | Not explicitly reported |
| Cryoprotection | Not explicitly reported |
| Notes | Space group P61 with cell dimensions a=137.0, b=137.0, c=68.5 A, alpha=90, beta=90, gamma=120. Rwork/Rfree = 25.2/30.8. 1991 protein atoms, 33 ligand/ion atoms, 0 water molecules. B-factor for protein = 53.6. Heavy atom derivatives prepared with ethylmercuricthiosalicylic acid, [Methylmercury Chloride](/xray-mp-wiki/reagents/additives/methylmercury-chloride/), p-chloromercuribenzoic acid, and K2PtCl4. |

| Parameter | Value |
|---|---|
| Method | Not explicitly reported in supplementary information |
| Protein sample | Isolated Trx-like domain |
| Reservoir | -- |
| Temperature | Not explicitly reported |
| Growth time | Not explicitly reported |
| Cryoprotection | Not explicitly reported |
| Notes | Space group P42121 with cell dimensions a=57.2, b=57.2, c=58.1 A, alpha=90, beta=90, gamma=90. Rwork/Rfree = 19.4/21.2. 714 protein atoms, 0 ligand/ion atoms, 53 water molecules. B-factor for protein = 19.5. |

### doi/10.1038##ncomms4110

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion with slow dehydration |
| Protein sample | Cys50Ala mutant VKOR-Trx fusion |
| Reservoir | 12% PEG3350, 0.1 M [Sodium Cacodylate](/xray-mp-wiki/reagents/buffers/sodium-cacodylate/) pH 5.5 |
| Temperature | 22 C |
| Growth time | Dehydration with [PEG300](/xray-mp-wiki/reagents/additives/peg300/) in 5% steps every 12 h to final 40% |
| Cryoprotection | 25% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (initial), then [PEG300](/xray-mp-wiki/reagents/additives/peg300/) dehydration (final) |
| Notes | Crystals diffracted from 3.6 to 2.8 Angstrom after dehydration protocol; Rfree = 24.5% |

| Parameter | Value |
|---|---|
| Method | [HiLiDe Crystallization](/xray-mp-wiki/methods/crystallization/hilide-crystallization/) (lipid and detergent co-crystallization) |
| Protein sample | Cys212Ala mutant VKOR-Trx fusion |
| Reservoir | 11% PEG1500, 8% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5% ethanol, 0.1 M MgCl2, 0.1 M NaCl, 0.1 M [Sodium Cacodylate](/xray-mp-wiki/reagents/buffers/sodium-cacodylate/) pH 5.5 |
| Temperature | 22 C |
| Growth time | Overnight mixing with lipids, then hanging drop crystallization |
| Cryoprotection | Flash-frozen in liquid nitrogen |
| Notes | Protein (20 mg/ml) mixed with 15 mg/ml [DOPC](/xray-mp-wiki/reagents/lipids/dopc/) and 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/); crystals diffracted to 4.2 Angstrom |


## Biological / Functional Insights

### Horizontal helix spring mechanism for electron transfer

The horizontal helix (residues Gly55 to Ser62) at the hydrophobic active site of
VKOR undergoes winding and unwinding conformations to promote electron transfer.
Cys56 is located at the exact N-terminal end of this helix, and its motions are
coupled to the helix conformation. In the wound conformation (Cys50Ala structure),
the helix adopts a typical alpha-helical structure with four hydrogen bonds from
Gly55 to Ser62. In the unwound conformation (Cys56Ala structure), the C-alpha trace
is no longer alpha-helical with only two potential hydrogen bonds. This spring-like
mechanism allows Cys56 to alternatively interact with Cys50 (in the Trx domain) or
Cys130 (in the VKOR active site), which are separated by 16 Angstroms. Inserting
residues between Cys56 and the horizontal helix significantly lowers electron
transfer efficiency but does not affect [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) reduction at the active site.

### Warfarin-resistant mutations affect horizontal helix conformation

Several warfarin-resistant mutations identified in human and rodents map to or
close to the horizontal helix of ssVKOR. The Asp57Leu, Val59Leu, Ser61Phe, and
Arg63Gly mutations in ssVKOR (corresponding to Ser52Leu, Val54Leu, Ser56Phe, and
Arg58Gly in human VKOR) all increase the membrane accessibility of Leu60Cys on
the horizontal helix. This change is explained by a movement of the horizontal helix
that weakens its membrane association. The mutations appear to induce a
conformational change in the horizontal helix region, altering the putative
warfarin-binding pocket and resulting in [Warfarin](/xray-mp-wiki/reagents/ligands/warfarin/) resistance.

### Hydrophobic active site pocket for catalysis

The catalytic residue Cys133 is buried in a hydrophobic pocket formed by Val59 and
Leu60 from the horizontal helix, and Leu37, Met122, and Tyr132 from the
transmembrane helices. Met118 stacks at the bottom of the quinone ring to position
it for reaction with Cys133. The hydrophobic environment lowers the pKa of Cys133
for deprotonation at neutral pH, which is the first step in VKOR catalysis. When
hydrophobic residues Val59 and Leu60 are mutated to expose Cys133 to water, ssVKOR
exhibits much lower enzymatic activity and the pH optimum shifts from 7.5 to 8.5,
reflecting a change in thiol pKa (typically 8.7 in water). The hydrophobicity
surrounding Cys133 is well conserved among VKOR homologues.


## Cross-References

- [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) — Natural substrate that binds in the VKOR active site for reduction
- [Menaquinone](/xray-mp-wiki/reagents/ligands/menaquinone/) — Related quinone electron carrier; bacterial vitamin K analog
- [Cytochrome b](/xray-mp-wiki/proteins/enzymes/cytochrome-b/) — Quinone-binding membrane protein; comparison of quinone binding sites
- [Cytochrome b5 Reductase](/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/) — Related reductase enzyme with flavin-based redox chemistry
- [DsbB](/xray-mp-wiki/proteins/enzymes/dsbB/) — Related intramembrane disulfide bond-forming enzyme; convergent evolution of horizontal helix mechanism
- [DsbA](/xray-mp-wiki/proteins/enzymes/dsbA/) — Periplasmic oxidase that generates disulfide bonds; functional homolog in bacterial oxidative folding
- [HiLiDe Crystallization](/xray-mp-wiki/methods/crystallization/hilide-crystallization/) — Membrane protein crystallization method used for Cys212Ala mutant with DOPC
- [Vitamin K Cycle](/xray-mp-wiki/concepts/enzyme-mechanisms/vitamin-k-cycle/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
