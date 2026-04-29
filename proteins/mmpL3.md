---

title: MmpL3
created: 2026-04-27
updated: 2026-04-27
type: protein
tags: [transporter, membrane-protein, pump]
sources: [doi/10.1073##pnas.1901346116, doi/10.1016##j.cell.2019.01.003, doi/10.1016##j.jmb.2020.05.019]

---
layout: default


# MmpL3 (Mycobacterial Membrane Protein Large 3)

## Overview

MmpL3 is an essential membrane protein transporter in *Mycobacterium tuberculosis* and *M. smegmatis* required for cell-wall biogenesis. It transports trehalose monomycolates (TMMs), precursors of mycolic acids, across the inner membrane. MmpL3 is a validated drug target for anti-tuberculosis therapy.

## Structure

### Su et al. (PNAS 2019)

- **Resolution**: 2.59 Å
- **Architecture**: 12 transmembrane helices (TMs 1–12) with two periplasmic loops (loops 1 and 2)
- **Periplasmic domains**: PD1 (4 α-helices + 3 β-strands) and PD2 (3 α-helices + 3 β-strands)
- **Oligomerization**: Monomeric in detergent solution (confirmed by native MS)
- **Truncated construct**: MmpL3₇₇₃ (residues 1–773) used for crystallization; C-terminal proline-rich region (733–1013) was proteolytically clipped

### Zhang et al. (Cell 2019) — MsMmpL3-T4L (M. smegmatis)

- **Resolution**: 2.59 Å (MmpL3₇₇₃)
- **Architecture**: 12 transmembrane helices with [[t4-lysozyme]] (T4L) fusion
- **Periplasmic pore domain**: Subdomains PN and PC, both adopt β-α-β-α-β fold
- **Three openings**: G_T (funnel at top), G_F (opening in front), G_B (opening at back)
- **Substrate mimic**: 6-DDTre (6-n-dodecyl-α,α-trehalose) bound in cavity and G_T

### Yang et al. (JMB 2020) — MmpL3 with NITD-349 and SPIRO

- **NITD-349-bound**: 3.1 Å resolution, space group P2₁2₁2₁
- **SPIRO-bound**: 2.8 Å resolution, space group P2₁2₁2₁
- **Binding pocket volume**: ~206 Å³ (NITD-349), ~214 Å³ (SPIRO)
- **PDB IDs**: 7C2M (NITD-349), 7C2N (SPIRO)

### Su et al. (PNAS 2019)

- **Expression**: *E. coli* BL21(DE3)Δ*acrB* cells (full-length) or *M. smegmatis* mc²155 cells (MmpL3₇₇₃)
- **Construct**: C-terminal 6xHis-tag; MmpL3₇₇₃ (residues 1–773) for crystallization
- **Detergent**: [[ddm]] (n-dodecyl-β-D-maltopyranoside)
- **Purification**: Ni²⁺-[[affinity-chromatography]], Superdex size-exclusion chromatography
- **SEC buffer**: 20 mM Na-[[hepes-buffer]] pH 7.5, 150 mM [[sodium-chloride]], 0.05% [[ddm]]

### Zhang et al. (Cell 2019) / Yang et al. (JMB 2020)

- **Expression**: *M. smegmatis* mc²155 cells (4-day growth)
- **Construct**: MmpL3₁₋₇₄₈aa-T4 (C-terminal domain substituted by [[t4-lysozyme]]), 10×His tag
- **Cell lysis**: French Press at 1,200 bars
- **Detergent**: 1% [[ddm]] (Anatrace) for membrane solubilization
- **Purification**: [[affinity-chromatography]] agarose (GE Healthcare), elution with 300 mM [[imidazole]]
- **Wash buffer**: 20 mM [[tris-buffer]]-HCl pH 8.0, 150 mM [[sodium-chloride]], 10% [[glycerol]], 0.05% [[ddm]], 50 mM [[imidazole]]
- **SEC**: [[superdex-columns]]-6 increase 10/300 GL, buffer: 20 mM [[tris-buffer]]-HCl pH 8.0, 150 mM [[sodium-chloride]], 10% [[glycerol]], 0.05% [[ddm]], 6-DDTre
- **Concentration**: 15 mg/mL for crystallization (100 kDa cut-off spin [[amicon-filters]])

## Crystallization

### Su et al. (PNAS 2019)
- **Method**: [[vapor-diffusion]] (hanging drop)
- **Protein concentration**: 20 mg/mL MmpL3₇₇₃ in 20 mM Na-[[hepes-buffer]] pH 7.5, 0.05% [[ddm]]
- **Reservoir**: 25% [[peg-400]], 0.1 M [[sodium-acetate]] pH 5.4, 0.05 M magnesium acetate
- **Temperature**: 25 °C
- **Cryoprotection**: Raised [[peg-400]] to 30%

### Yang et al. (JMB 2020)
- **Method**: Hanging-drop [[vapor-diffusion]]
- **Protein**: 6–8 mg/mL MmpL3-T4L + 0.5 mM ligand (NITD-349 or SPIRO), incubated 30 min at 4 °C
- **Reservoir**: 10–20% PEGMME 350, 50 mM ADA pH 6.0–7.0, 7.5–17.5% [[peg-2000]]
- **Temperature**: 16 °C
- **Cryo-protection**: 25% [[glycerol]]
- **Data collection**: SSRF BL17U, BL18U1, BL19U1; Spring-8 BL41XU

## Ligand Binding

### Phosphatidylethanolamine (PE)

- Discovered inside the MmpL3 structure by electron density (Su et al., 2019)
- Native MS: Kd = 19.5 ± 6.3 μM for first PE binding
- Second PE molecule binds at ≥20 μM PE concentration
- Binding residues: F134, S136, D144, L171, L174, A175, Q421, I427, S428, E429, F445, F452, R453, T454, P456, R501, P502, A503, N504, Q517, T549, Q40

### Trehalose Monomycolate (TMM)

- Native MS: Kd = 3.7 ± 1.3 μM for first TMM binding
- Prefers short-chain TMM lipids (~1,428 Da)
- **Does NOT bind TDM** (trehalose dimycolate) — specificity confirmed by native MS

### Other Lipids

Native MS shows MmpL3 binds: PG (phosphatidylglycerol), PI (phosphatidylinositol), DAG (diacylglycerol), [[cardiolipin]] — suggesting MmpL3 is a promiscuous lipid-binding protein.

## Proton-Relay Network

MmpL3 is a proton-motive-force–dependent transporter that functions via an antiport mechanism:

- **Key residues**: D256–Y646, Y257–D645, S293–D645, E647–K591
- These conserved residues form a hydrogen-bonded network for proton transfer
- Proton import into cytoplasm is coupled to substrate export toward periplasm

## Drug Targets and Inhibitors

### SQ109 (diamine, Kd = 1.65 μM)
- Extended conformation in TMH bundle
- Geranyl tail: hydrophobic subsite (Ile249, Ile319, Ala637, Val638, Ser301)
- Adamantine group: held by "V"-shaped Phe260-Phe649
- Pocket volume: ~282 Å³

### AU1235 (adamantyl urea, Kd = 0.29 μM)
- Similar binding position to SQ109
- Adamantyl group in hydrophobic subsite

### ICA38 (indolcarboxamide)
- Bulky indole group in hydrophobic subsite
- Amide H-bonds to Asp645; carbonyl H-bonds to Tyr646
- Carbocyclic spiro group in bottom hydrophobic subsite

### Rimonabant (CB1 antagonist, Kd = 29 μM)
- Three "arms": 2,4-dichlorophenyl, 4-chlorophenyl, pi-peridinyl-1-carbamoyl
- Pyrazole core inserts at TMH bundle center
- Pocket volume: ~305 Å³

### NITD-349 (indole-2-carboxamide, Kd = 0.05 μM)
- Indole group: hydrophobic subsite (Ile249, Ile253, Ile297, Val638, Gly641, Leu642, Leu686, Leu708)
- Amide nitrogen and indole nitrogen: H-bonds to Asp645
- Amide oxygen: H-bond to Asp256
- Dimethylcyclohexane: hydrophobic downside pocket
- Disrupts both Asp-Tyr pairs

### SPIRO (spiropiperidine, Kd = 0.8 μM)
- Benzodioxane: hydrophobic subsite (Ile249, Ile253, Ile297, Val638, Gly641, Leu642, Leu686)
- 4-oxygen of dioxane: H-bond to Leu642 main chain
- Thiophene: π-π stacking with Tyr257 and Phe649
- Piperidine nitrogen: H-bond to Asp645; π-cation with Tyr646
- Pocket volume: ~214 Å³ (slightly larger than NITD-349)

## Inhibitor Binding Mechanism

All inhibitors bind deep in the central transmembrane channel, disrupting the proton-relay network:

1. **Common features**: Hydrophobic head and tail, nitrogen atom in central part that H-bonds to Asp645
2. **Effect**: Disrupt hydrogen bonds between conserved Asp-Tyr pairs (D256-Y646, Y257-D645)
3. **Result**: Blocks proton motive force required for substrate translocation

## Resistance Mutations

### NITD-349 resistance:
- L194R, G258E, S293T, T316I, S596I, V688G, V689G
- S293T: prevents binding by disrupting H-bond network stabilizing Tyr257 and Asp645

### SPIRO resistance:
- Y257C, F260V/L, I297S/T, S596I
- Aromatic residues Tyr257 and Phe260: critical for inhibitor binding

## Cross-References

- [[sotb]] — E. coli antiporter (MFS family)
- [[nTMATE2-transporter]] — Tobacco MATE family transporter
- [[sq109]] — Anti-TB diamine drug; MmpL3 inhibitor in clinical trials
- [[rimonabant]] — CB1 antagonist repurposed as MmpL3 inhibitor
- [[ica38]] — Indolcarboxamide MmpL3 inhibitor
- [[au1235]] — Adamantyl urea MmpL3 inhibitor
- [[linezolid]] — Another bacterial drug target (AcrB)
- [[mfs-transporter]] — Major facilitator superfamily
- [[cardiolipin]] — Lipid that binds to MmpL3
- [[ddm]] — Solubilization detergent
- [[t4-lysozyme]] — T4L fusion used in Zhang et al. construct