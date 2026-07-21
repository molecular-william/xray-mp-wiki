---
title: "F1-ATPase from Caldalkalibacillus thermarum"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1612035113]
verified: agent
uniprot_id: ['F5LA71', 'F5LA72', 'F5LA73', 'F5LA74']
---

# F1-ATPase from Caldalkalibacillus thermarum

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/F5LA71">UniProt: F5LA71</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/F5LA72">UniProt: F5LA72</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/F5LA73">UniProt: F5LA73</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/F5LA74">UniProt: F5LA74</a>

<span class="expr-badge">Caldalkalibacillus thermarum TA2.A1</span>

## Overview

The F1-ATPase from Caldalkalibacillus thermarum is the water-soluble catalytic domain of the thermoalkaliphilic F1FO-[ATP](/xray-mp-wiki/reagents/ligands/atp/) synthase. It consists of α₃β₃γδε subunits and hydrolyzes [ATP](/xray-mp-wiki/reagents/ligands/atp/) poorly. The crystal structure reveals that although the overall architecture is closely similar to active mitochondrial and bacterial F1-ATPases, the βE-catalytic site is occupied by [ADP](/xray-mp-wiki/reagents/ligands/adp/) (without magnesium ion) and a phosphate ion, which likely forms the basis of inhibition of [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis. Unlike the Geobacillus stearothermophilus enzyme, the ε-subunit does not regulate activity via conformational changes, and neither the γ-subunit nor regulatory [ATP](/xray-mp-wiki/reagents/ligands/atp/) bound to the ε-subunit is involved in the inhibitory mechanism.


## Publications

### doi/10.1073##pnas.1612035113

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5hkk">5HKK</a></td>
      <td>3.0</td>
      <td></td>
      <td>Wild-type C. thermarum F1-ATPase (α₃β₃γδε subunits expressed with His10 tag on ε-subunit, TEV-cleaved)</td>
      <td>Mg-<a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a> (α- and β-subunits), <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a> + phosphate (βE-subunit), <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> + Mg²⁺ (ε-subunit C-terminal helical domain)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5hkk">5HKK</a></td>
      <td>2.6</td>
      <td></td>
      <td>Mutant C. thermarum F1-ATPase (ε-subunit E83A, I88A, D89A, R92A, R99A, R123A, R127A — <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a>-binding deficient ε-subunit)</td>
      <td>Mg-<a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a> (α- and β-subunits), <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a> + phosphate (βE-subunit)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41(Δunc)
- **Construct**: F1-ATPase α₃β₃γδε with His10 tag and TEV protease cleavage site at N-terminus of ε-subunit
- **Notes**: Expressed from pTrc99A plasmid. E. coli C41 strain lacking endogenous unc operon used for overexpression.

**Purification:**

- **Expression system**: Escherichia coli C41(Δunc)
- **Expression construct**: C. thermarum F1-ATPase with His10 tag + TEV site on ε-subunit
- **Tag info**: His10 tag on ε-subunit, removed by TEV protease on-column

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
      <td>Nickel affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a> Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td>Purification buffer (detailed in SI Materials and Methods)</td>
      <td>His10-tagged F1-ATPase bound to <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
    </tr>
    <tr>
      <td>TEV protease cleavage</td>
      <td>On-column cleavage</td>
      <td></td>
      <td></td>
      <td>His10 tag cleaved with <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease while bound to <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> column</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Microbatch</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified F1-ATPase (wild-type or mutant)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown by microbatch method. Data collected at European Synchrotron Radiation Facility, Grenoble, France. Crystallization buffers devoid of nucleotide.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>microbatch</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### ε-subunit does not regulate ATP hydrolysis in C. thermarum F1-ATPase

The ε-subunit is in the down position with an [ATP](/xray-mp-wiki/reagents/ligands/atp/) molecule bound to its C-terminal α-helices. A mutant ε-subunit unable to bind [ATP](/xray-mp-wiki/reagents/ligands/atp/) remains in the down state and does not relieve inhibition. Therefore, unlike G. stearothermophilus F1-ATPase, neither the γ-subunit nor regulatory [ATP](/xray-mp-wiki/reagents/ligands/atp/) bound to ε-subunit mediates the inhibitory mechanism. The enzyme is inhibited by a mechanism independent of ε-subunit conformational changes.

### βE subunit contains bound ADP and phosphate without magnesium ion

The βE catalytic site in both wild-type and mutant structures contains [ADP](/xray-mp-wiki/reagents/ligands/adp/) without a magnesium ion plus a phosphate ion. This occupancy has never been observed in active F1-ATPase structures. The phosphate is ~7 Å from where the γ-phosphate of [ATP](/xray-mp-wiki/reagents/ligands/atp/) would be. Both [ADP](/xray-mp-wiki/reagents/ligands/adp/) and phosphate likely originated from the E. coli overexpression strain. This unique combination of hydrolysis products bound to the βE site is proposed as the basis of inhibition.

### Activated enzyme activity measured with LDAO

[ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis activity of both wild-type and mutant F1-complexes was activated by 0.1% lauryldimethylamine oxide (LDAO) to a specific activity of 33-38 U/mg protein for both enzymes. This confirms that both wild-type and mutant enzymes are in an inhibited basal state that can be artificially activated by detergent.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/">Bovine F1-ATPase (Mitochondrial ATP Synthase Catalytic Domain)</a> — Homologous enzyme from bovine mitochondria with similar α₃β₃γ architecture
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/">F1-ATPase Rotary Catalytic Mechanism</a> — The rotary catalytic mechanism is the fundamental operating principle of F1-ATPases
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">n-Dodecyl-N,N-dimethylamine-N-oxide (LDAO)</a> — LDAO (0.1%) used to activate ATP hydrolysis activity of inhibited F1-ATPase
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/">Bovine F1-ATPase (azide-inhibited form)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)</a> — Related protein structure
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/">F1-ATPase Rotary Catalytic Mechanism</a> — Related concept
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">Lauryldimethylamine N-oxide (LDAO)</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl beta-D-glucopyranoside (OG)</a> — Detergent used in the study
