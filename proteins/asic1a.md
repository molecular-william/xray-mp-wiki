---
title: ASIC1a (Acid-Sensing Ion Channel 1a)
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [ion-channel, membrane-protein, xray-crystallography, degenerin-epithelial-sodium-channel]
sources: [doi/10.1016##j.cell.2014.01.011]
category: proteins
---
layout: default

# ASIC1a — Acid-Sensing Ion Channel 1a

## Overview

Acid-sensing ion channels (ASICs) are voltage-independent, sodium-selective ion channels that detect extracellular protons produced during inflammation or ischemic injury. They belong to the degenerin/epithelial sodium channel (DEG/ENaC) superfamily. This paper reports the cocrystal structure of chicken ASIC1a with MitTx (Texas coral snake toxin) — the first structure of the open state of an ASIC.

## Structure

- **Protein**: Chicken ASIC1a (Δ13 construct, residues 13–456, with C-terminal truncation)
- **Ligand**: MitTx (heterodimeric snake toxin, α and β subunits)
- **Resolutions**: 2.1 Å (native), 2.3 Å (amiloride-bound), 2.6 Å (Cs⁺-soaked)
- **PDB IDs**: 4NTW (native), 4NTX (amiloride), 4NTY (Cs⁺)
- **Space group**: R3 (3-fold symmetry)
- **Asymmetric unit**: One Δ13 subunit + one MitTx heterodimer

### Architecture

- **Trimeric channel** with triskelion-like shape viewed down 3-fold axis
- **MitTx binding**: One toxin heterodimer per ASIC1a subunit, 800 Å² (α) + 550 Å² (β) buried surface area
- **Toxin contact region**: Channel "wrist" (proximal to membrane) to knuckle and thumb domains (~60 Å from membrane)

### GAS Selectivity Filter — Open State

- **TM2 is discontinuous**: Breaks into TM2a and TM2b segments ~2/3 across membrane
- **GAS motif** (Gly-Ala-Ser): Extended, belt-like conformation
- **TM2 swap**: Cytoplasmic 1/3 of TM2 swaps with adjacent subunit
- **Gly 443 carbonyl oxygens**: Form 3-fold symmetric triangle, 7.1 Å apart, 4.1 Å from Cs⁺ site
- **Selectivity mechanism**: Barrier mechanism — hydrated Na⁺ radius (~3.6 Å) matches filter radius; hydrated ions excluded by size

### Ion Sites

- **Cs⁺ site**: On 3-fold axis at GAS filter plane, 15 Cs⁺ ions total in Cs⁺-soaked structure
- **Na⁺ site**: Weak/no density in native crystals (possibly disordered at 100–150 mM Na⁺)
- **Amiloride sites**: Two in acidic pocket of extracellular domain; one in fenestration of extracellular vestibule

### Ion Conduction Pathway

- **Cation-π interactions**: Ions exploit cation-π interactions within lateral fenestrations to enter/exit extracellular vestibule
- **Hydrophobic seal**: Tight interactions (Val49-Leu93) shelter Schiff base from cytosol (analogous to bR)

## Expression and Purification

**Note**: Methods refer to previous publications (Baconguis and Gouaux, 2012; Bohlen et al., 2011).

- **Δ13 cASIC1a**: Expressed and purified as previously described
- **MitTx**: Native toxin from Texas coral snake (*Micrurus fulvius*)
- **Complex formation**: Pre-mixed Δ13 + MitTx at ~1.0 Δ13 subunit : 1.5 MitTx molar ratio before crystallization

### Recombinant MitTx Expression

- **Constructs**: Mature MitTxα (JN613325) and MitTxβ (JN613326) with N-terminal enterokinase cleavage sites
- **Vector**: pET32b
- **Expression**: E. coli Rosetta-gamiB (DE3) pLysS, 0.1 mM IPTG induction
- **Inclusion bodies**: Sonication in 20 mM Tris pH 8, 150 mM NaCl, 1 mM PMSF, 5 mM MgCl₂, 20 μg/ml DNase-I, 0.4 mg/ml lysozyme
- **Solubilization**: 300 mM β-mercaptoethanol (supplemented buffer)
- **Refolding**: As previously described (Chen and Gouaux, 1997)

## Crystallization

- **Complex**: Δ13-MitTx at pH 5.5
- **Crystallization method**: Not explicitly stated (referenced as previous work)
- **Data collection**: Multiple crystal forms (native, amiloride-bound, Cs⁺-soaked)
- **Phasing**: Molecular replacement using truncated ΔASIC1 extracellular domain + MitTx α (residues 13–38) and β (helices α1–α3) models
- **Refinement**: COOT + PHENIX, iterative manual building

## Functional Assays

- **Electrophysiology**: Whole-cell recordings in CHO-K1 cells
- **Ion selectivity**: NaCl substituted with LiCl, KCl, RbCl, CsCl, hydrazine, hydroxylamine, methylamine
- **MitTx concentrations**: 600 nM α, 300 nM β
- **Reversal potentials**: Voltage ramps from –100 to 40 mV (RbCl/CsCl) or –60 to 70 mV (other cations)

## Biological Significance

- **Pain initiation**: ASIC1a activated by tissue acidosis during inflammation, ischemia, stroke
- **Toxin mechanism**: MitTx allosterically stabilizes open state, slows channel closure, increases steady-state current at pH 5.5
- **Selectivity filter**: Defines architecture of voltage-independent, Na⁺-selective channels
- **Open state**: First captured open state of an ASIC (vs. previously known closed and desensitized states)

## Related Channels

- [kirbac](/proteins/kirbac.html) — KirBac potassium channel (ion channel)
- [navab-sodium-channel](/proteins/navab-sodium-channel.html) — NaVAb sodium channel
- [ion-channels](/concepts/ion-channels/) — Ion channels concept page

## References

- Baconguis et al. (2014) Cell — ASIC1a-MitTx open state structure
- Baconguis and Gouaux (2012) — Δ13 construct methods
- Bohlen et al. (2011) — MitTx toxin characterization