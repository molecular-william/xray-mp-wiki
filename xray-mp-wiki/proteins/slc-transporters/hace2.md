---
title: "Human Angiotensin-Converting Enzyme 2 (hACE2)"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.03.045, doi/10.1038##s41586-020-2180-5, doi/10.1038##s41586-020-2179-y]
verified: agent
uniprot_id: Q9BYF1
---

# Human Angiotensin-Converting Enzyme 2 (hACE2)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9BYF1">UniProt: Q9BYF1</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human angiotensin-converting enzyme 2 (hACE2) is a membrane-bound zinc metalloprotease that plays a key role in the renin-angiotensin system by converting [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) to angiotensin-(1-7). It also serves as the cellular entry receptor for [SARS-CoV](/xray-mp-wiki/concepts/miscellaneous/sars-cov/) and [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) coronaviruses. The structure of hACE2 reveals an N-terminal peptidase domain that mediates viral spike protein binding.


## Publications

### doi/10.1016##j.cell.2020.03.045

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6lzg">6LZG</a></td>
      <td>2.5</td>
      <td>P41212</td>
      <td>hACE2 residues 19-615, N-terminal peptidase domain in complex with <a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/">SARS-CoV-2</a> CTD</td>
      <td><a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/">SARS-CoV-2</a> CTD (spike protein residues 319-541)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Hi5 Insect Cells](/xray-mp-wiki/methods/expression-systems/hi5-expression-system/) ([Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/))
- **Construct**: hACE2 residues Ser19-Asp615, N-terminal [gp67 Signal Peptide](/xray-mp-wiki/reagents/additives/gp67-signal-peptide/), C-terminal 6xHis tag

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
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/histrap/">HisTrap</a> HP 5 mL column</td>
      <td>Buffer not specified + --</td>
      <td>Soluble proteins from <a href="/xray-mp-wiki/methods/expression-systems/hi5-expression-system/">Hi5</a> cell supernatant purified by metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a></td>
      <td>Final purification step; samples pooled and concentrated</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/">SARS-CoV-2</a> CTD/hACE2 complex, protein concentration 15 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 10% w/v <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 5000 MME, 12% v/v <a href="/xray-mp-wiki/reagents/additives/1-propanol/">1-Propanol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir solution supplemented with 20% v/v <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> before <a href="/xray-mp-wiki/methods/crystallization/flash-cooling/">Flash-Cooling</a> in <a href="/xray-mp-wiki/reagents/cryogens/liquid-nitrogen/">Liquid Nitrogen</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Diffraction data collected at SSRF BL17U (wavelength 0.97919 A)</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##s41586-020-2180-5

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6m0j">6M0J</a></td>
      <td>2.45</td>
      <td>P4₁2₁2</td>
      <td>hACE2 residues Ser19-Asp615, N-terminal peptidase domain in complex with <a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/">SARS-CoV-2</a> RBD (residues Arg319-Phe541)</td>
      <td><a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/">SARS-CoV-2</a> RBD (spike protein residues 319-541), zinc ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Hi5 Insect Cells](/xray-mp-wiki/methods/expression-systems/hi5-expression-system/) ([Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/))
- **Construct**: hACE2 residues Ser19-Asp615, N-terminal [gp67 Signal Peptide](/xray-mp-wiki/reagents/additives/gp67-signal-peptide/), C-terminal 6xHis tag

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
      <td>Secretion and concentration</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus</a> expression in <a href="/xray-mp-wiki/methods/expression-systems/hi5-expression-system/">Hi5</a> cells</td>
      <td>--</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/hbs/">HBS</a> (10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.2, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>)</td>
      <td>Supernatant collected 60 h post-infection, concentrated and buffer-exchanged to <a href="/xray-mp-wiki/reagents/buffers/hbs/">HBS</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) resin (GE Healthcare)</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/hbs/">HBS</a> (10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.2, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>) + --</td>
      <td>Eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in <a href="/xray-mp-wiki/reagents/buffers/hbs/">HBS</a> buffer</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Gel Filtration</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column (GE Healthcare)</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/hbs/">HBS</a> (10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.2, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>) + --</td>
      <td>Pre-equilibrated with <a href="/xray-mp-wiki/reagents/buffers/hbs/">HBS</a> buffer; complex formed by incubating ACE2 with <a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/">SARS-CoV-2</a> RBD for 1 h on ice before <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/">SARS-CoV-2</a> RBD-ACE2 complex at 13 mg/ml in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 10% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 5000 MME, 12% <a href="/xray-mp-wiki/reagents/additives/1-propanol/">1-Propanol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir solution supplemented with 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> before <a href="/xray-mp-wiki/methods/crystallization/flash-cooling/">Flash-Cooling</a> in <a href="/xray-mp-wiki/reagents/cryogens/liquid-nitrogen/">Liquid Nitrogen</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in sitting drops; 200 nl complex + 200 nl well solution; diffraction data at 100 K, wavelength 1.07180 A on BL17U1 at SSRF</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##s41586-020-2179-y

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6vw1">6VW1</a></td>
      <td>2.68</td>
      <td>P 21 21 21</td>
      <td>hACE2 residues 1-615 in complex with <a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/">SARS-CoV-2</a> <a href="/xray-mp-wiki/concepts/construct-design/chimeric-rbd/">Chimeric RBD</a></td>
      <td><a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/">SARS-CoV-2</a> <a href="/xray-mp-wiki/concepts/construct-design/chimeric-rbd/">Chimeric RBD</a> (<a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/">SARS-CoV-2</a> core + <a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov/">SARS-CoV</a> side loop), zinc ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Hi5 Insect Cells](/xray-mp-wiki/methods/expression-systems/hi5-expression-system/) ([Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/))
- **Construct**: hACE2 residues Ser19-Asp615, N-terminal [gp67 Signal Peptide](/xray-mp-wiki/reagents/additives/gp67-signal-peptide/), C-terminal 6xHis tag

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
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus</a> expression</td>
      <td>Expression in <a href="/xray-mp-wiki/methods/expression-systems/sf9-expression-system/">Sf9 Insect Cells</a> via <a href="/xray-mp-wiki/methods/expression-systems/bac-to-bac-system/">Bac-to-Bac</a> system (Life Technologies)</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.2, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a></td>
      <td><a href="/xray-mp-wiki/reagents/vectors/pfastbac/">pFastBac</a> vector with <a href="/xray-mp-wiki/reagents/peptides/honeybee-melittin-signal-peptide/">Honeybee Melittin Signal Peptide</a> and C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a>; ACE2 and RBD separately expressed and secreted into medium</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.2, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + --</td>
      <td>His6-tagged ACE2 and RBD purified from cell culture medium supernatant</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Gel Filtration</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.2, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + --</td>
      <td>ACE2 and RBD incubated together; complex purified by Superdex200 gel-filtration; concentrated to 13 mg/ml</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/">SARS-CoV-2</a> chimeric RBD-ACE2 complex at 13 mg/ml in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.2, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.5, 18-20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 6000, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.5, 30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 6000, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 30% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a>; flash-frozen in <a href="/xray-mp-wiki/reagents/cryogens/liquid-nitrogen/">Liquid Nitrogen</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>X-ray diffraction data collected at Advanced Photon Source beamline 24-ID-E; structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using <a href="/xray-mp-wiki/concepts/miscellaneous/sars-cov/">SARS-CoV</a> RBD-ACE2 (PDB 2AJF)</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Structural basis for SARS-CoV-2 receptor recognition

The crystal structure of the [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) CTD in complex with hACE2 at 2.5 A resolution reveals the molecular basis for viral entry. hACE2 binds to the C-terminal domain of the [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) spike protein via its N-terminal peptidase domain. The binding interface involves extensive hydrophobic contacts and hydrogen bonds between hACE2 residues (including F28, Y41, H34, D38, Y41) and [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) CTD residues (including Y453, L455, F456, Y489, Q498). The [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) CTD displays stronger affinity for hACE2 compared to SARS-RBD due to key residue substitutions that slightly strengthen the interaction.

### Comparison of SARS-CoV and SARS-CoV-2 receptor binding

Despite both [SARS-CoV](/xray-mp-wiki/concepts/miscellaneous/sars-cov/) and [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) utilizing hACE2 as their entry receptor, the atomic details at the binding interface demonstrate notable differences. [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) CTD residue substitutions lead to higher affinity for receptor binding compared to SARS-RBD. The overall binding mode is similar, but key contacts differ at the residue level, explaining the higher infectivity of [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/). The [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) CTD is antigenically distinct from SARS-RBD, as shown by the inability of SARS-CoV-directed monoclonal and polyclonal antibodies to bind [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) spike protein.

### Convergent evolution of SARS-CoV-2 and SARS-CoV RBDs for ACE2 binding

The 2.45 A crystal structure of the [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) RBD-ACE2 complex (PDB 6M0J) reveals that the overall ACE2-binding mode is nearly identical to [SARS-CoV](/xray-mp-wiki/concepts/miscellaneous/sars-cov/) RBD. Residues in the [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) RBD essential for ACE2 binding are either highly conserved or share similar side chain properties with [SARS-CoV](/xray-mp-wiki/concepts/miscellaneous/sars-cov/) RBD. A unique ACE2-interacting residue, Lys417, in [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) forms salt-bridge interactions with Asp30 of ACE2 — this position is Val404 in [SARS-CoV](/xray-mp-wiki/concepts/miscellaneous/sars-cov/) and fails to participate in ACE2 binding. Despite high structural similarity, the binding affinity of ACE2 for [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) RBD (KD 4.7 nM) is ~6.6-fold tighter than for [SARS-CoV](/xray-mp-wiki/concepts/miscellaneous/sars-cov/) RBD (KD 31 nM). The study also mapped the epitopes of [SARS-CoV](/xray-mp-wiki/concepts/miscellaneous/sars-cov/) antibodies (m396, S230, 80R, CR3014) on the [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) RBD, providing structural explanation for their lack of cross-reactivity.

### ACE2-binding ridge compaction and hotspot stabilization in SARS-CoV-2

The 2.68 A structure of the [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) chimeric RBD-ACE2 complex (PDB 6VW1) reveals that the ACE2-binding ridge in [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) RBD has a more compact conformation than [SARS-CoV](/xray-mp-wiki/concepts/miscellaneous/sars-cov/) RBD. Residue changes in the [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) RBM stabilize two key hotspots at the RBD-ACE2 interface: hotspot 31 (centered on ACE2 Lys31-Glu35) and hotspot 353 (centered on ACE2 Lys353). SPR measurements show the [Chimeric RBD](/xray-mp-wiki/concepts/construct-design/chimeric-rbd/) has higher ACE2-binding affinity than wild-type [SARS-CoV-2](/xray-mp-wiki/concepts/miscellaneous/sars-cov-2/) RBD (KD 23.2 nM vs 44.2 nM), both significantly higher than [SARS-CoV](/xray-mp-wiki/concepts/miscellaneous/sars-cov/) RBD (KD 185 nM). RaTG13 (bat coronavirus) also uses human ACE2 as its receptor, suggesting possible direct bat-to-human transmission without an intermediate host.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/sars-cov-2-ctd/">SARS-CoV-2 Spike Protein C-Terminal Domain</a> — Co-crystallized with hACE2 in PDB 6LZG, 6M0J and 6VW1
- <a href="/xray-mp-wiki/reagents/buffers/mes/">2-(N-Morpholino)ethanesulfonic Acid (MES)</a> — Crystallization buffer at pH 6.5
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — PEG 5000 MME used as crystallization precipitant
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Cryoprotectant (20% v/v) for flash-cooling crystals
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — 150 mM in SEC purification buffer
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — 20 mM Tris-HCl pH 8.0 in SEC buffer; 20 mM Tris pH 7.5 in complex buffer
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — 500 mM imidazole used for elution from Ni-NTA resin
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — 10 mM HEPES pH 7.2 used in HBS purification buffer
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
