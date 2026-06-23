---
title: KtrA (Cytosolic Regulatory Protein from Bacillus subtilis)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12055]
verified: false
---

# KtrA (Cytosolic Regulatory Protein from Bacillus subtilis)

## Overview

KtrA is a cytosolic regulatory protein from the bacterium Bacillus subtilis that forms an octameric ring and associates with the [KTRB](/xray-mp-wiki/proteins/pumps-atpases/ktrb/) membrane protein to form the KtrAB potassium transporter complex. KtrA contains RCK (Regulator of K+ conductance) domains and binds ATP and ADP with a strong preference for ATP. Ligand binding induces a ligand-dependent conformational change in the octameric ring: ATP binding produces a four-fold symmetric square conformation, while ADP binding produces a two-fold symmetric diamond conformation. In full-length KtrA, ATP binding induces unique intradimer interactions that determine the conformation of the octameric ring, contrasting with truncated KtrA where ligand binding and ring conformation are uncoupled.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12055 | 4J90 | 3.2 | Not specified | Full-length KtrA octameric ring bound to ATP | ATP |
| doi/10.1038##nature12055 | 4J91 | 2.9 | Not specified | Full-length KtrA octameric ring bound to ADP | ADP |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Tag-less KtrA from Bacillus subtilis
- **Notes**: Overexpressed in LB media at 20°C for 14-16 h after [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction

### Purification Workflow

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: Tag-less KtrA from Bacillus subtilis

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Cell lysis | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 50 mM KCl, 5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/) | Cells lysed in Buffer C |
| Anion exchange chromatography | Ion-exchange chromatography | Anion exchange column | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 50 mM KCl, 5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/) | Cleared lysate loaded into anion exchange column |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (ADP-agarose) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (ADP-agarose matrix) | ADP-agarose resin (Innova Biosciences) | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), 150 mM KCl, 1 mM TCEP | Incubated overnight at 4°C; eluted with 5 mM adenosine-containing nucleotide |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex-S200 column |  |  |

**Final sample**: ~3 mg/ml in appropriate buffer


## Crystallization

### doi/10.1038##nature12055

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | KtrA-ATP octamer, concentrated to ~10 mg/ml, run on SEC in Buffer F |
| Reservoir | 100 mM HEPES pH 7.5, 3% [PEG](/xray-mp-wiki/reagents/additives/peg/) 6000, 2.5% [MPD](/xray-mp-wiki/reagents/additives/mpd/) (2-methyl-2,4-pentanediol) |
| Mixing ratio | Not specified |
| Temperature | 20 |
| Cryoprotection | Flash-frozen in liquid nitrogen after transfer to mother liquor containing 6% [PEG](/xray-mp-wiki/reagents/additives/peg/) 6000 and 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | KtrA-ADP octamer, concentrated to ~10 mg/ml, run on SEC in Buffer F |
| Reservoir | 100 mM [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 5.6, 14.5% [PEG](/xray-mp-wiki/reagents/additives/peg/) 20000 |
| Mixing ratio | Not specified |
| Temperature | 20 |
| Cryoprotection | Flash-frozen in liquid nitrogen |


## Biological / Functional Insights

### ATP-dependent octameric ring conformation

KtrA octameric rings adopt different conformations depending on the bound nucleotide. The KtrA-ATP ring adopts a four-fold symmetric square conformation, whereas the KtrA-ADP ring adopts a two-fold symmetric diamond conformation. This conformational difference is also observed in solution through controlled proteolysis. The gamma- phosphate in ATP occupies the position taken by the beta-phosphate in ADP, accomplished by a shift in G79 and repositioning of the alpha- and beta-phosphates.

### Intradimer interactions mediated by ATP

In the ATP structure, the gamma-phosphate interacts with R16 from its own binding site, while the beta-phosphate interacts with R16 from the neighbouring KtrA subunit binding site. This intradimer interaction brings the two binding sites within a KtrA dimer together through a ~16 degree change in the angle between subunits. The distances separating the conserved D36 in the two binding pockets are ~35 A in the ADP structure and ~30 A in the ATP structure. The absence of the gamma-phosphate in ADP results in lack of ligand-mediated intradimer interactions and relaxation of the ring.

### Full-length vs truncated KtrA conformational coupling

In truncated KtrA (composed of N lobe alone), ligand binding and ring conformation are uncoupled. In contrast, full-length KtrA exhibits conformational coupling: ATP binding induces a unique set of intradimer interactions that determine the conformation of the octameric ring. This suggests that the C-terminal portion of full-length KtrA is essential for transmitting the ligand-binding signal to the ring conformation.

### Asymmetric ring contraction upon ATP binding

Unlike [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) and BK channels where RCK rings expand symmetrically upon binding of activating ligands, the KtrA ring in KtrAB contracts asymmetrically upon ATP binding. In KtrAB, the cytoplasmic loops of the [KTRB](/xray-mp-wiki/proteins/pumps-atpases/ktrb/) homodimer mediate the interaction with the KtrA (RCK) ring, and the ring undergoes asymmetric conformational changes along the diagonal defined by the lateral contacts or tip contacts. This represents a fundamentally different activation mechanism compared to covalently tethered RCK channels.

### Ligand specificity of KtrA

KtrA has a strong binding preference for ATP and ADP over other small molecules, resembling other KtrA proteins. Functional assays with 86Rb+ uptake show that ATP markedly increases flux compared to ADP or [KTRB](/xray-mp-wiki/proteins/pumps-atpases/ktrb/) alone, supporting previous cell-based results showing that ATP is an activator of KtrAB. The functional effect of ATP and ADP was evaluated in liposome reconstitution assays with excess KtrA to minimize formation of the KtrB-KtrA-[KTRB](/xray-mp-wiki/proteins/pumps-atpases/ktrb/) complex.


## Cross-References

- [KtrB (Potassium Transporter Membrane Subunit from Bacillus subtilis)](/xray-mp-wiki/proteins/pumps-atpases/ktrb/) — KtrB forms the homodimeric membrane component that associates with KtrA octameric ring to form the functional KtrAB transporter
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — ATP is the primary activating ligand that binds to KtrA and induces square conformation of the octameric ring
- [Adenosine Diphosphate (ADP)](/xray-mp-wiki/reagents/ligands/adp/) — ADP binds to KtrA and induces diamond conformation of the octameric ring, with lower activating effect
- [HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid)](/xray-mp-wiki/reagents/buffers/hepes/) — HEPES buffer (pH 7.5) used in KtrA-ATP crystallization
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Citrate buffer (pH 5.6) used in KtrA-ADP crystallization
- [Tris-(2-carboxyethyl)phosphine (TCEP)](/xray-mp-wiki/reagents/additives/tcep/) — TCEP used as reducing agent in KtrA purification buffer
- [RCK Domain Activation Mechanism](/xray-mp-wiki/concepts/structural-mechanisms/rck-domain-activation-mechanism/) — KtrA RCK domains form an octameric gating ring with asymmetric contraction mechanism, distinct from MthK/BK symmetric expansion
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) — Related protein structure
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Additive used in purification or crystallization buffers
