---
title: "Staphylococcus aureus MscL (Mechanosensitive Channel of Large Conductance)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08277]
verified: false
---

# Staphylococcus aureus MscL (Mechanosensitive Channel of Large Conductance)

## Overview

SaMscL is the mechanosensitive channel of large conductance from Staphylococcus aureus, a bacterial ion channel that protects cells from lysis upon acute osmotic down-shock. The crystal structure of a C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) mutant (CΔ26, residues 1-94) was determined at 3.8 A resolution, revealing a tetrameric channel with both transmembrane helices (TM1 and TM2) tilted away from the membrane normal at angles close to those inferred for the open state. TM1 and TM2 are tilted 49 degrees and 59 degrees with respect to the pore axis, significantly larger than the 36-38 degrees in the closed-state pentameric [MSCL](/xray-mp-wiki/proteins/other-ion-channels/mscl/) from M. tuberculosis. The pore constriction at Val21 is widened to ~6 A diameter compared to ~3 A in the closed state, but remains hydrophobic and likely non-conducting, representing an expanded intermediate state between the closed and open conformations.

## Publications

### doi/10.1038##nature08277

**Structures:**

<table class="wiki-table">
  <thead><tr>
    <th>PDB ID</th>
    <th>Resolution</th>
    <th>Space Group</th>
    <th>Construct</th>
    <th>Ligand/Co-factor</th>
  </tr></thead>
  <tbody>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/(deposited; referenced pdb 2oar for mtmscl comparison)">(DEPOSITED; REFERENCED PDB 2OAR FOR MTMSCL COMPARISON)</a></td>
      <td>3.8 A</td>
      <td>Tetragonal (four-fold crystallographic axis coincides with molecular symmetry)</td>
      <td>SaMscL C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> mutant (CΔ26, residues 1-94); one subunit per asymmetric unit</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21-Gold (DE3)
- **Construct**: SaMscL(CA26) with stop codon at Glu95, cloned into pET15b vector with NdeI and BamHI sites

**Purification:**

<table class="wiki-table">
  <thead><tr>
    <th>Step</th>
    <th>Method</th>
    <th>Resin / Column</th>
    <th>Buffer + Detergent</th>
    <th>Notes</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>Cell lysis</td>
      <td>Sonication</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a>, 200 mM NaCl, 44 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, pH 8.0</td>
      <td>Cells resuspended in lysis buffer and sonicated for 4 min</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA gravity column</td>
      <td>2 ml Ni-NTA (Qiagen)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a>, 300 mM NaCl, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, pH 7.5 (high salt wash); 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a>, 20 mM NaCl, 75 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, pH 7.5 (low <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> wash); 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a>, 20 mM NaCl, 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, pH 7.5 (elution)</td>
      <td>Protein concentrated to ~15 mg/ml</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/30 HR column</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a>, 150 mM NaCl, 2 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, pH 7.5</td>
      <td>Major peak eluting at ~14.3 ml; concentrated to 15-20 mg/ml</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified SaMscL(CA26) at 15-20 mg/ml with 3.0 mM decyl-beta-D-maltoside (DM) added</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>24-30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.0, 150 mM Na2SO4</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 degrees C (crystal crosslinking)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~1 month</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial hits from MemGold screen. Crystals crosslinked with 25% glutaraldehyde through vapor diffusion at 4 C for 1-2 h. Crystals soaked overnight in 10 mM Na2WO4 or Na2MoO4 for phasing. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> using S32C mutant soaked in Na4P2O7 for phasing at 3.8 A resolution.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Tetrameric MscL represents an expanded intermediate state

SaMscL(CΔ26) forms a tetramer in the crystal, in contrast to the pentameric MtMscL closed-state structure. The channel is expanded within the membrane plane and compressed along the pore axis compared to the closed state. TM1 and TM2 are tilted 49 degrees and 59 degrees with respect to the pore axis, close to the ~51 degrees predicted for the open state. However, the pore constriction at Val21 remains narrow (~6 A diameter) and hydrophobic, suggesting the structure is non-conducting and represents an expanded intermediate state.

### Two-step helix-pivoting gating mechanism

The structure supports a two-step gating mechanism: (1) TM1-TM2 pairs tilt outward as rigid bodies, expanding the periplasmic surface area while the pore remains essentially closed at the constriction; (2) a second anticlockwise pivoting of the TM1-TM2 pair around a hinge at Gly48 expands the pore diameter to ~22 A, compatible with the 3 nS conductance. The periplasmic loop acts as a spring limiting the extent of channel expansion. This glycine-pivoting mechanism is analogous to that observed in [MSCS](/xray-mp-wiki/proteins/voltage-gated-channels/mscs/).

### C-terminal truncation traps the intermediate state

Removal of 26 C-terminal residues (residues 95-120) lowers the energy barrier for transition from the closed to expanded state. The C-terminal helical bundle in the full-length protein likely stabilizes the closed conformation and may act as a plug or pre-filter to the permeation pathway. Both full-length and truncated SaMscL rescue an [MSCL](/xray-mp-wiki/proteins/other-ion-channels/mscl/)/MscS/MscK knockout strain from osmotic down-shock, confirming the mutant is functional in vivo.


## Cross-References

- <a href="/xray-mp-wiki/proteins/other-ion-channels/mscl/">MscL (Mycobacterium tuberculosis)</a> — Related mechanosensitive channel from M. tuberculosis; closed-state pentameric structure (PDB 2OAR) compared to the SaMscL expanded intermediate
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/mechanosensitive-gating/">Mechanosensitive Gating</a> — SaMscL is a mechanosensitive ion channel; the structure reveals the expanded intermediate in the gating pathway
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/force-from-lipid-principle/">Force-from-Lipid Principle</a> — MscL is directly gated by membrane tension via the force-from-lipid principle
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO (Lauryldimethylamine Oxide)</a> — Detergent used for SaMscL purification and crystallization
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> — Buffer used in purification (10-50 mM Tris-HCl, pH 7.0-8.0)
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a> — Precipitant used in crystallization (24-30% PEG400)
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mscs/">MSCS</a> — Related protein structure
