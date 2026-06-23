---
title: "Vps45 (Cryptococcus thermophilum SM Protein)"
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.60724]
verified: false
---

# Vps45 (Cryptococcus thermophilum SM Protein)

## Overview

Vps45 is a Sec1/Munc18-family (SM) protein from the filamentous fungus Cryptococcus thermophilum that functions as a SNARE chaperone in membrane trafficking from the endosome to the trans-Golgi network. The crystal structures of Vps45 alone and in complex with the Qa-SNARE [TLG2](/xray-mp-wiki/proteins/tlg2) reveal that Vps45 holds [TLG2](/xray-mp-wiki/proteins/tlg2) in an open conformation with its SNARE motif disengaged from its Habc domain, in contrast to the closed (clamped) conformation observed for Munc18-1 with syntaxin-1. Vps45 rescues [TLG2](/xray-mp-wiki/proteins/tlg2) from homo-tetrameric oligomers into stoichiometric 1:1 complexes and its unfurled domain 3a helical hairpin exposes the presumptive R-SNARE binding site for template complex assembly.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.60724 | 6XJL | 2.00 A | P212121 | C. thermophilum Vps45 (XP_006692860.1 homolog) alone, full-length cytoplasmic domain | None |
| doi/10.7554##eLife.60724 | 6XMD | 3.88 A | P21221 | C. thermophilum Vps45 in complex with Qa-SNARE Tlg2 (residues 1-310) cytoplasmic domain | None |
| doi/10.7554##eLife.60724 | 6XM1 | 2.80 A | P212121 | C. thermophilum Vps45 in complex with full-length Qa-SNARE Tlg2 (residues 1-327) cytoplasmic domain | None |

## Expression and Purification

- **Expression system**: Escherichia coli BL21 Rosetta (Novagen) for Vps45 alone; E. coli BL21-Codon Plus (Agilent) for [TLG2](/xray-mp-wiki/proteins/tlg2) and Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2) co-expression
- **Construct**: Vps45 with N-terminal His7 tag for individual expression, or C-terminal His7 tag for co-expression with Tlg2. All constructs cloned into pQLink bacterial expression plasmids. Tlg2 constructs carried N-terminal His7 and MBP tags followed by TEV protease cleavage site. Mutations (V306D, F335R, L258M, I272M) introduced using QuikChange mutagenesis (Agilent). Vps45 overproduced at 25 C for 18 hr; Tlg2 and Vps45-Tlg2 co-expression at 16 C.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Pressure homogenization (Emulsiflex-C5, Avestin) | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl, 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) + -- | Cell pellets resuspended in lysis buffer supplemented with 1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf) and 10 ug/mL DNase. Clarified by centrifugation at 30,000 g. |
| Ni-affinity chromatography | Ni-affinity chromatography | His60 Ni Superflow Resin (ClonTech) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 100 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) (wash); 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) in wash buffer (elution) + -- | Resin washed with wash buffer, eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole). Performed on ice or at 4 C. |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 HR 16/60 (GE Healthcare) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl, 5 mM dithiothreitol ([DTT](/xray-mp-wiki/reagents/additives/dtt)) + -- | Gel filtration buffer. Final purification step. |
| Tag cleavage ([TLG2](/xray-mp-wiki/proteins/tlg2) constructs) | Protease digestion (TEV protease) | His60 Ni Superflow (cleaved His7-MBP tags removed) | 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 50 mM NaCl + -- | TEV protease cleavage site present between tags and protein for tag removal. |


## Crystallization

### doi/10.7554##eLife.60724

| Parameter | Value |
|---|---|
| Method | Vapor diffusion with streak seeding |
| Protein sample | Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2)(1-327) complex at 4 mg/ml in 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 8.0, 50 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Reservoir | 0.2 M potassium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate), 14% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg) 3350, 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Temperature | Room temperature |
| Growth time | ~3 days |
| Cryoprotection | 1:1 mixture of well buffer supplemented with 30% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), then frozen in liquid nitrogen |
| Notes | Diamond-shaped crystals in P212121 space group with two complexes in the asymmetric unit. Improved by streak seeding with Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2) crystals. Data collected at NSLSII FMX beamline. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2)(1-310) complex at 4 mg/ml in 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 8.0, 50 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Reservoir | 0.2 M potassium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate), 14% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg) 3350, 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Temperature | Room temperature |
| Growth time | ~3 days |
| Cryoprotection | 1:1 mixture of well buffer supplemented with 30% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), then frozen in liquid nitrogen |
| Notes | P21221 crystal form with single complex in the asymmetric unit. Streak seeded with Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2) crystals. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Vps45-V306D,F335R-[TLG2](/xray-mp-wiki/proteins/tlg2) complex at 4 mg/ml |
| Reservoir | 0.2 M potassium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate), 14% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg) 3350, 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | 1:1 mixture of well buffer supplemented with 30% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), then frozen in liquid nitrogen |
| Notes | Mutant Vps45-V306D,F335R in complex with [TLG2](/xray-mp-wiki/proteins/tlg2). P21 crystal form. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | SeMet-labeled Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2)(L258M,I272M) complex at 5 mg/ml in 0.1 M [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 0.2 M NaCl, 10% 2-propanol, 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Reservoir | 0.1 M [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 0.2 M NaCl, 10% (v/v) 2-propanol, 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Temperature | Not specified |
| Growth time | ~3 days |
| Cryoprotection | 1:1 mixture of well buffer supplemented with 30% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) plus 10% (v/v) 2-propanol, then frozen in liquid nitrogen |
| Notes | SeMet-labeled for SAD phasing. L258M and I272M mutations confirmed sequence register in SNARE helix. P212121 crystal form. |

| Parameter | Value |
|---|---|
| Method | X-ray crystallography |
| Protein sample | Native Vps45 at ~4 mg/ml |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Vps45 alone crystallized in P212121 space group. Data collected at CHESS F1 beamline (0.9782 A wavelength). Resolution 2.00 A. |


## Biological / Functional Insights

### Vps45 holds Qa-SNARE Tlg2 in an open conformation

Unlike Munc18-1 which clamps syntaxin-1 in a closed conformation where the Habc domain folds back onto the SNARE motif, Vps45 holds [TLG2](/xray-mp-wiki/proteins/tlg2) in an open conformation. The Habc domain makes only a limited contact with the SNARE motif at approximately 45 degrees, and the linker between Habc and SNARE motif is disordered/unfolded. The N-peptide of [TLG2](/xray-mp-wiki/proteins/tlg2) (residues 1-14) binds to the outside of Vps45 domain 1 burying 870 A^2 of surface area, while layers 0 to +4 of the SNARE motif interact with the cleft-facing side of Vps45 domain 1 burying about 930 A^2. The Habc domain interacts with the cleft side of Vps45 domain 1 burying 680 A^2. This demonstrates that Qa-SNARE clamping is a specialized property of Munc18 rather than a general property shared among SM proteins.

### Vps45 prevents Tlg2 homo-oligomerization by rescuing tetramers

[TLG2](/xray-mp-wiki/proteins/tlg2) has a pronounced tendency to form homo-tetramers driven by SNARE motif bundling, as shown by size-exclusion chromatography and sedimentation velocity analytical ultracentrifugation (experimental MW 33.8 kDa vs expected 33.6 kDa for tetramer). The Habc domain alone ([TLG2](/xray-mp-wiki/proteins/tlg2) residues 79-200) sediments as a monomer. Vps45 can rescue [TLG2](/xray-mp-wiki/proteins/tlg2) tetramers into stoichiometric 1:1 complexes, presumably by trapping transiently dissociated monomers. The [TLG2](/xray-mp-wiki/proteins/tlg2) N-peptide is required for this rescue, as N-terminally truncated [TLG2](/xray-mp-wiki/proteins/tlg2) constructs form oligomers that neither bind to nor are rescued by Vps45. Vps45 protects [TLG2](/xray-mp-wiki/proteins/tlg2) from oligomerization by binding to layers 0 to +4 of the SNARE motif.

### Vps45 domain 3a helical hairpin is unfurled and primed for R-SNARE binding

The domain 3a helical hairpin of Vps45 adopts an unfurled, extended conformation in the [TLG2](/xray-mp-wiki/proteins/tlg2)-bound state, exposing the presumptive R-SNARE binding site. This contrasts with the Munc18-Stx1 complex where the hairpin is furled and the R-SNARE binding site is concealed. The unfurled conformation is also seen in Vps33 bound to SNARE motifs, suggesting it may be a well-defined active conformation for SM proteins. The Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2) complex appears primed to bind an R-SNARE (such as Snc2) and catalyze SNARE complex assembly via a template mechanism.

### SM proteins use at least two distinct modes to engage Qa-SNAREs

The Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2) structure establishes that SM proteins can engage the N-peptide, Habc domain, and SNARE motif of a cognate Qa-SNARE without simultaneously clamping that SNARE in a closed conformation. This reveals a second mode of SM-Qa-SNARE interaction beyond the Munc18-Stx1 closed clamp. It is possible that the open mode is the rule and the Munc18 clamp mode is the exception. Munc13-1, which mediates Stx opening in neurons, may function by converting the Munc18-Stx complex into a Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2)-like conformation.


## Cross-References

- [Tlg2 (Cryptococcus thermophilum Qa-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/tlg2/) — Cognate Qa-SNARE partner co-crystallized with Vps45 in PDB entries 6XMD and 6XM1; forms 1:1 complexes with Vps45
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) — Entity mentioned in text
- [PMSF](/xray-mp-wiki/reagents/additives/pmsf) — Entity mentioned in text
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) — Entity mentioned in text
- [TCEP](/xray-mp-wiki/reagents/additives/tcep) — Entity mentioned in text
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate) — Entity mentioned in text
- [PEG](/xray-mp-wiki/reagents/additives/peg) — Entity mentioned in text
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes) — Entity mentioned in text
- [DTT](/xray-mp-wiki/reagents/additives/dtt) — Entity mentioned in text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) — Entity mentioned in text
