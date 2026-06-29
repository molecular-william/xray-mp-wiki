---
title: "Polysulfide Reductase (PsrABC) from Thermus thermophilus"
created: 2026-05-29
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NSMB.1434]
verified: false
---

# Polysulfide Reductase (PsrABC) from Thermus thermophilus

## Overview

Polysulfide reductase (PsrABC) from Thermus thermophilus is an integral membrane protein complex responsible for quinone-coupled reduction of polysulfide (Sn2-). It is a molybdenum/tungsten-containing bis-molybdopterin guanine dinucleotide (bis-MGD) oxidoreductase that uses [MK-7](/xray-mp-wiki/reagents/cofactors/menaquinone-7/) as the endogenous electron donor and polysulfide as the terminal electron acceptor. The enzyme is expressed under aerobic conditions in this thermophilic bacterium and is proposed to function as a key energy-conserving enzyme in the respiratory chain, potentially coupling electron transfer to proton pumping across the membrane.

## Publications

### doi/10.1038##NSMB.1434

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/unknown (not explicitly stated in paper)">UNKNOWN (NOT EXPLICITLY STATED IN PAPER)</a></td>
      <td>2.4 A</td>
      <td>P212121</td>
      <td>Native PsrABC heterotrimeric complex from Thermus thermophilus. The dimeric (ABC)2 configuration has a total molecular weight of approximately 260 kDa. PsrA subunit (733 residues), PsrB subunit (194 residues), and PsrC subunit (integral membrane, 8 transmembrane helices). Each monomer contains two Mo-bis-MGD cofactors, five [4Fe-4S] clusters on PsrB, one [4Fe-4S] cluster on PsrA, and 1,306 resolved water molecules.</td>
      <td><a href="/xray-mp-wiki/reagents/cofactors/menaquinone-7/">MK-7</a>, <a href="/xray-mp-wiki/reagents/ligands/pentachlorophenol/">PCP</a>, <a href="/xray-mp-wiki/reagents/ligands/ubiquinone-1/">UQ1</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Thermus thermophilus (HB27)
- **Construct**: His-tagged PsrABC complex from Thermus thermophilus HB27. The PsrA subunit N-terminus contains a twin-arginine translocase (TAT) motif, suggesting periplasmic localization. N-terminal sequencing confirmed absence of first 28 amino acids including the TAT signal peptide.

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
      <td>French press</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cells lysed by French press</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Differential centrifugation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Membranes isolated by centrifugation</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>-- + n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted with linear gradient from 100-280 mM NaCl</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>30 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 100 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Column pre-equilibrated and run at 0.5 mL/min. Flow rate 0.5 mL/min</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Ultrafiltration</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Concentrated to approximately 15 mg/mL using Amicon Ultra-15 with 10 kDa MWCO filter. Purity approximately 95% by SDS-PAGE</td>
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
      <td>PsrABC complex at 15 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M MES pH 6.5, 30-34% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 200 mM CaCl2</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>48 h for initial appearance; full size in approximately 2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Native crystals and quinone/inhibitor-bound complexes obtained from cocrystallization. <a href="/xray-mp-wiki/reagents/cofactors/menaquinone-7/">MK-7</a>, <a href="/xray-mp-wiki/reagents/ligands/pentachlorophenol/">PCP</a>, and <a href="/xray-mp-wiki/reagents/ligands/ubiquinone-1/">UQ1</a> added to reservoir at 0.5-1 mM.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Dimeric architecture and physiological oligomerization

The crystal packing reveals an (ABC)2 dimer configuration with an extensive interface of 2,614 A2 between the two heterotrimeric monomers and an intricate hydrogen-bond network between PsrB subunits. The dimer is likely physiological, similar to the dimeric configuration found in nitrate reductase ([NARGHI](/xray-mp-wiki/proteins/enzymes/narghi/)), another membrane-bound bis-MGD oxidoreductase. The overall molecular organization of PsrABC resembles those of formate dehydrogenase-N (FdnGHI) and [NARGHI](/xray-mp-wiki/proteins/enzymes/narghi/), with two membrane-associated subunits (PsrA and PsrB) and one integral membrane subunit (PsrC).

### Active site architecture and polysulfide reduction mechanism

The PsrA subunit contains two molybdopterin guanine dinucleotide cofactors (bis-MGD), designated P and Q following DMSO reductase nomenclature, and a cubane-type [4Fe-4S] cluster. The subunit folds into four distinct domains with internal pseudo two-fold symmetry. ArgA332 is key to polysulfide substrate coordination at the active site. During catalysis, molybdenum is proposed to become hexa-coordinated by sulfur atoms, with ArgA332 acting as a direct ligand. Substrate binding cleaves polysulfide, releasing Sn-1 2- and leaving a Mo[S]6 core. Electrons and protons are delivered via five [4Fe-4S] clusters on PsrB to the Mo center, generating H2S and leaving a Mo[S]5 core. HisA145 is proposed to act as a general acid-base catalyst.

### Electron transfer chain through iron-sulfur clusters

Four [4Fe-4S] clusters in PsrB and FeS-0 on PsrA are aligned in a single chain. Distances between adjacent redox centers are within the 14-A limit for physiological electron transfer. Two electrons and two protons are released from [MK-7](/xray-mp-wiki/reagents/cofactors/menaquinone-7/) (the bound substrate) and transferred via the iron-sulfur cluster chain to the bis-MGD cofactor to reduce polysulfide. The enzyme catalyzes: MKH2 → MK + 2H+ + 2e- (in the membrane) and Sn2- + 2e- + 2H+ → S + H2S.

### Menaquinone-7 binding pocket in PsrC

The quinone binding site is situated on the periplasmic side of the membrane in the N-terminal four-helix bundle of PsrC, in close proximity to FeS-4. It is composed of residues from TMII, TMIII, and the horizontal helix hII-III of PsrC, plus a short loop region (residues B91-B95) of the PsrB subunit. The pocket is mainly hydrophobic, with the quinone sandwiched between LeuC64 and IleC89. In the MK-7-bound structure, TyrC130 is a direct ligand of the O1 carbonyl group. HisC21, AspC60, and GluC67 are implicated in quinone coordination and proton removal. The equivalent of HisC21 is a tyrosine in all homologous enzymes.

### Proposed proton-pumping mechanism

PsrC accommodates a possible proton-relay network centered on a hydrophilic cavity partially occupied by water molecules. The relay network starts from GluC224 and ArgC177 on the cytoplasmic surface of the second helix bundle (hb2) and leads through hb2 to ArgC239 via ThrC220, SerC183, a water molecule, and ThrC155. The pathway may cross over to hb1 and connect to AspC60 and HisC21 via three water molecules. This suggests Psr could incorporate proton-translocation machinery energized by redox reactions in the quinone site, analogous to Complex I. Such a mechanism would provide efficient energy conservation in T. thermophilus.


## Cross-References

- <a href="/xray-mp-wiki/reagents/cofactors/menaquinone-7/">Menaquinone-7 (MK-7)</a> — Endogenous quinone substrate and electron donor
- <a href="/xray-mp-wiki/reagents/cofactors/ubiquinone/">Ubiquinone (Coenzyme Q10)</a> — Similar quinone electron carrier; UQ1 used as crystallization analog
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for solubilization and purification
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer component in purification and crystallization
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — Related redox enzyme mechanism principle
- <a href="/xray-mp-wiki/reagents/ligands/menaquinone/">Menaquinone</a> — General menaquinone family; MK-7 is specific isoform used by Psr
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/enzymes/narghi/">NARGHI</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
