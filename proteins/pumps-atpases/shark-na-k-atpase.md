---
title: Na+,K+-ATPase from Squalus acanthias (Shark)
created: 2026-06-05
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms9004, doi/10.1073##pnas.0907054106, doi/10.1073##pnas.2123226119, doi/10.1038##nature07939]
verified: false
---

# Na+,K+-ATPase from Squalus acanthias (Shark)

## Overview

Na+,K+-ATPase from the shark rectal gland (Squalus acanthias) is a P-type ATPase that transports three Na+ from the cytoplasm to the extracellular side and two K+ in the opposite direction per [ATP](/xray-mp-wiki/reagents/ligands/atp) hydrolysed. The shark enzyme has been extensively studied as a model for P-type ATPase mechanism due to its high abundance in rectal gland tissue and favorable crystallization properties. This paper reports multiple crystal structures of the shark enzyme in the E2·MgF4²⁻·2K+ state at 2.9 Å resolution, capturing sequential substitution of bound K+ with Tl+ and Rb+ congeners. Additionally, cryo-EM structures of the shark enzyme in two E2P states (E2P^ATP and E2P^Pi·Mg^2+) with and without cardiotonic steroids (ouabain and istaroxime) were determined at resolutions better than 3.9 Å. PDB IDs: 5AVQ-5AW9 (time-course structures), 2ZXE (shark E2·MgF4²⁻·2K+, 2.4A, previous), 3A3Y (shark with [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain), previous). A crystal structure of the Na+,K+-ATPase with bound [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain) at 2.8 Å resolution in a state analogous to E2·2K+·Pi was determined, revealing the structural basis of cardiac glycoside inhibition.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms9004 | 5AVQ | 2.9 | not specified | E2·MgF4²⁻·2K+ state (shark Na+,K+-ATPase) | K+, MgF4²⁻ |
| doi/10.1038##ncomms9004 | 2ZXE | 2.4 | not specified | E2·MgF4²⁻·2K+ (shark, no ouabain) | K+, MgF4²⁻ |
| doi/10.1038##ncomms9004 | 3A3Y | not specified | not specified | E2·MgF4²⁻·2K+ with ouabain | K+, MgF4²⁻, ouabain |
| doi/10.1073##pnas.0907054106 | not stated in raw paper | 2.8 | C2 | Na+,K+-ATPase (shark) in E2·2K+·Pi analog state with bound ouabain | K+, MgF4²⁻, ouabain |
| doi/10.1073##pnas.2123226119 | not specified | 3.4 | not specified | Shark Na+,K+-ATPase in E2P^ATP state (diprotomer) | ATP, Mg2+ |
| doi/10.1073##pnas.2123226119 | not specified | 3.9 | not specified | Shark Na+,K+-ATPase in E2P^Pi·Mg2+ state (diprotomer) | Mg2+ (at site M and phosphorylation site) |
| doi/10.1073##pnas.2123226119 | not specified | 3.9 | not specified | Shark Na+,K+-ATPase in E2P^ATP state with ouabain (OBN) | ATP, Mg2+, ouabain |
| doi/10.1073##pnas.2123226119 | not specified | 3.9 | not specified | Shark Na+,K+-ATPase in E2P^Pi·Mg2+ state with ouabain (OBN) | Mg2+, ouabain |
| doi/10.1073##pnas.2123226119 | not specified | 3.9 | not specified | Shark Na+,K+-ATPase in E2P^ATP state with istaroxime (IST) | ATP, Mg2+, istaroxime |
| doi/10.1073##pnas.2123226119 | not specified | 3.9 | not specified | Shark Na+,K+-ATPase in E2P^Pi·Mg2+ state with istaroxime (IST) | Mg2+, istaroxime |

## Expression and Purification

- **Expression system**: Squalus acanthias (shark) rectal gland
- **Notes**: Purified from shark rectal gland tissue by homogenization, [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose) flotation, [DXC](/xray-mp-wiki/reagents/additives/deoxycholate) treatment, and repeated centrifugation. Turnover number 200 s⁻¹ at 37°C.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Homogenization | Tissue homogenization in buffer containing 30 mM histidine, 1 mM EDTA, 0.25 M sucrose, pH 6.8 | — | 30 mM histidine, 1 mM EDTA, 0.25 M sucrose, pH 6.8 | Shark rectal gland tissue |
| Membrane preparation | Sucrose flotation | — | 30 mM histidine, 1 mM EDTA, 0.25 M sucrose, pH 6.8 | Microsomes purified by sucrose flotation |
| Solubilization | Detergent solubilization | — | 100 mM KCl, 4 mM MgCl2, 4 mM glutathione, 25% glycerol, 20 mM MOPS-NMDG pH 6.5 + C12E8 at weight ratio 3.5 (C12E8:protein) | Treated with 5.2% (wt/vol) C12E8; insoluble fraction removed by centrifugation at 200,000 × g at 10°C |
| Size-exclusion chromatography | SEC | Superdex 200 Increase (Cytiva) | 1 mM MgCl2, 0.01% C12E8, 1 mM DTT, 20 mM MOPS-NMDG pH 6.1 or 20 mM imidazole-HCl pH 7.5 | Peak fractions concentrated to 8 mg/mL and stored in liquid nitrogen |


## Crystallization

### doi/10.1038##ncomms9004

| Parameter | Value |
|---|---|
| Method | Dialysis button |
| Protein sample | 2.5 mg/ml Na+,K+-ATPase in [C12E8](/xray-mp-wiki/reagents/detergents/octaethyleneglycol-mono-n-dodecylether-c12e8) |
| Reservoir | 18% [PEG300](/xray-mp-wiki/reagents/additives/peg300)0, 25% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 5% [MPD](/xray-mp-wiki/reagents/additives/mpd), 100 mM potassium [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate), 10 mM KCl, 4 mM [MgCl2](/xray-mp-wiki/reagents/additives/magnesium-chloride), 4 mM KF, 0.1 mM [EGTA](/xray-mp-wiki/reagents/additives/egta), 10 mM glutathione, 2.6 μg/ml [2,6-di-t-butyl-p-cresol](/xray-mp-wiki/reagents/additives/2,6-di-t-butyl-p-cresol), 20 mM MES/Tris pH 7.0 |
| Temperature | 25°C |
| Growth time | 1-2 months |
| Notes | Crystals prepared by dialysis against crystallization buffer. Soaked in dehydration buffer with 40% [PEG300](/xray-mp-wiki/reagents/additives/peg300)0, then in Tl+ or Rb+ [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate) for 0.75-100 min before flash-freezing in cold nitrogen gas. Data collected at SPring-8 BL41XU. |


## Biological / Functional Insights

### Ouabain binding mechanism in Na+,K+-ATPase

The 2.8 Å crystal structure of shark Na+,K+-ATPase with bound [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain) in the E2·2K+·Pi state reveals that ouabain binds in a cavity formed by transmembrane helices M1-M6 near the K+-binding sites. Ouabain is deeply inserted into the transmembrane domain with its lactone ring very close to bound K+, explaining the antagonism between cardiac glycosides and extracellular K+. The binding involves the tripartite structure: (i) a lactone ring interacting near the K+ site via hydrogen bonds with Thr-804; (ii) a steroid core stabilized by hydrophobic contacts and hydrogen bonds from hydroxyl groups; and (iii) a rhamnose sugar moiety forming hydrogen bonds with Arg-887 (L7/8 loop) and Glu-319 (M4), contributing ~300-fold higher affinity compared to ouabagenin (aglycone form).

### Conformational changes upon ouabain binding

Ouabain binding induces rearrangement of M1-M4 helices. The M4E helix (extracellular part of M4) between Gly-335 in the PEGL motif and Gly-314 inclines ~15° away from M6, widening the binding cavity by ~5 Å. M3 moves ~45° relative to M4, likely pushed by M4E via a dihedral angle change at Gly-314. These movements are similar to the E2·Pi → E2P transition in Ca²⁺-ATPase (PDB 1WPG → 2ZBE). Homology modeling based on E2·BeF₃⁻ Ca²⁺-ATPase suggests that in the high-affinity state, M1-M2 helices close around ouabain, forming a complementary surface with additional hydrogen bonds (Asp-128-Arg-979, Asp-123/Glu-124-Arg-893).

### Structural basis of cardiac glycoside affinity and inhibition

The low-affinity ouabain-bound state (E2·2K+·Pi) still explains most mutagenesis data from high-affinity states, indicating the binding site is essentially the same. Key findings: (i) Gln-118 and Asn-129 in M1-M2 form hydrogen bonds maintaining the V-shaped M1-M2 structure; (ii) substitution of Gln118Arg-Asn129Asp (found in rodent α1) causes large reduction in ouabain inhibition due to steric hindrance of cavity closure; (iii) evomonoside (with only C14 hydroxyl) has highest affinity among 37 derivatives, suggesting hydrophobic interface is important; (iv) the carbohydrate moiety significantly enhances affinity (~300×) via hydrogen bonds with Arg-887 and Glu-319. Ouabain inhibits the ATPase by binding to a cavity near K+-binding sites with partial unwinding of M4E, explaining the slow binding kinetics.

### Cryo-EM structures of NKA in two E2P states

Cryo-EM was applied to shark Na+,K+-ATPase to determine structures of two E2P states: E2P^ATP (formed by ATP and Mg2+ in the forward reaction) and E2P^Pi·Mg2+ (formed by inorganic phosphate and Mg2+ in the backward reaction), with and without ouabain or istaroxime. The two E2P structures are nearly identical, but Mg2+ in the transmembrane binding cavity (site M) is identified only in E2P^Pi·Mg2+. In E2P^ATP, ATP bridges the actuator (A) and nucleotide binding (N) domains, stabilizing the compact headpiece. No ATP is observed attached to the N domain in any other E2P species.

### CTS binding via conformational selection

CTS binding (ouabain and istaroxime) causes hardly any changes in the structure of NKA, both in E2P^ATP and E2P^Pi·Mg2+, indicating that the binding mechanism is conformational selection. The EM maps resolved mobile parts substantially better than previous X-ray structures, including sugars from the β-subunit and many phospholipid molecules.

### Istaroxime binding mode

Istaroxime (IST), a new-generation cardiotonic steroid, binds to NKA with its aminoalkyloxime group extending deep into the cation binding cavity. In E2P^ATP, IST adopts an upside-down orientation compared to classical CTSs with respect to the steroid ring — the aminoalkyloxime group at C3 extends into the cation binding cavity rather than the lactone ring at C17. The primary amine in the aminoalkyloxime group reaches the cluster of oxygen atoms coordinating Na+ and K+ at site II, forming hydrogen bonds with Glu327/334 and Val325/332. IST achieves fourfold higher affinity to NKA in E2P^ATP than in E2P^Pi·Mg2+.

### K+ sensitivity difference between E2P forms

The absence of transmembrane Mg2+ in E2P^ATP confers K+ sensitivity in dephosphorylation. E2P^Pi·Mg2+ has Mg2+ at site M occupying the cation binding cavity, blocking K+ access and making K+-sensitive acceleration of dephosphorylation not possible. This explains the long-observed biochemical difference between the two E2P forms (Post et al., 1965).

### Original 2.4 Å crystal structure Na+,K+-ATPase in E2·2K+·Pi state

The original crystal structure of shark Na+,K+-ATPase was determined at 2.4 Å resolution (Shinoda et al., 2009; PDB 2ZXE), revealing the α-subunit (10 transmembrane helices M1-M10 with A, N, and P cytoplasmic domains), β-subunit (single transmembrane helix with large glycosylated extracellular domain), and regulatory FXYD10 protein (single transmembrane helix). Details visualized at this resolution include: (i) coordination of two K+ ions in transmembrane sites I and II, with main-chain carbonyls key to K+ selectivity; (ii) a third K+ binding site (site C) in the cytoplasmic domain implicated in activation of dephosphorylation; (iii) the phosphate analogue MgF4²⁻ bound at the phosphorylation site; (iv) a cholesterol molecule shielding the unwound part of M7 from bulk lipid; (v) the β-subunit providing a critical main-chain carbonyl (Gly855) to coordinate K+ at site II — explaining why Ca²⁺-ATPase (lacking a β-subunit) cannot bind K+ and counter-transports H+ instead; and (vi) Pro785 on M5 causing unwinding to enable main-chain carbonyl usage for K+ coordination. The structure also shows the A and N domains hardly interacting (only one salt bridge between Glu223 and Arg551), with the N domain rotated ~22° further from the P domain than in Ca²⁺-ATPase.


## Cross-References

- [Ouabain](/xray-mp-wiki/reagents/additives/ouabain/) — Cardiotonic steroid inhibitor that binds extracellularly and suppresses K+ substitution
- [2-Methyl-2,4-pentanediol (MPD)](/xray-mp-wiki/reagents/additives/2-methyl-2,4-pentanediol/) — Additive used in crystallization buffer
- [Octaethyleneglycol mono-n-dodecylether (C12E8)](/xray-mp-wiki/reagents/detergents/octaethyleneglycol-mono-n-dodecylether-c12e8/) — Detergent used for solubilization
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Used in crystallization and purification buffers
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component (Tris-HCl pH 7.0, Tris pH 7.5)
- [MES](/xray-mp-wiki/reagents/buffers/mes/) — Buffer component (MES/Tris buffer pH 7.0)
- [Magnesium chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — MgCl2 required for MgF4²⁻ formation
- [P-type ATPase Mechanism](/xray-mp-wiki/concepts/p-type-atpase-mechanism/) — Na+,K+-ATPase is a canonical P-type ATPase; Post-Albers cycle
- [Na+,K+-ATPase from Pig Kidney](/xray-mp-wiki/proteins/pumps-atpases/na-k-atpase-pig-kidney/) — Related P-type ATPase; pig enzyme studied by rapid filtration methods
- [PEG300](/xray-mp-wiki/reagents/additives/peg300) — Entity mentioned in text
- [Istaroxime](/xray-mp-wiki/reagents/ligands/istaroxime/) — Next-generation cardiotonic steroid; cryo-EM structures reveal unique upside-down binding mode
- [Phosphoenzyme E2P State](/xray-mp-wiki/concepts/phosphoenzyme-e2p-state/) — Cryo-EM structures of E2P^ATP and E2P^Pi·Mg2+ states of shark NKA
- [Cardiotonic Steroids](/xray-mp-wiki/concepts/cardiotonic-steroids/) — Oubain and istaroxime binding to NKA E2P states studied by cryo-EM
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Primary method used to determine E2P state structures at 3.4-3.9 A resolution
