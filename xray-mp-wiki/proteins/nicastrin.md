---
title: "Nicastrin from Dictyostelium purpureum (DpNCT)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1414837111]
verified: agent
uniprot_id: F0ZBA6
---

# Nicastrin from Dictyostelium purpureum (DpNCT)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/F0ZBA6">UniProt: F0ZBA6</a>

<span class="expr-badge">Dictyostelium purpureum</span>

## Overview

Nicastrin is a type I transmembrane glycoprotein and the largest component of the [Gamma-Secretase Complex](/xray-mp-wiki/concepts/enzyme-mechanisms/gamma-secretase/) complex, which is responsible for generating amyloid-beta peptides from amyloid precursor protein (APP). Nicastrin is the putative substrate-recruiting component of the complex. The crystal structure of the nicastrin extracellular domain (ECD) from Dictyostelium purpureum (DpNCT) was determined at 1.95 A resolution by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) and bromide SAD phasing. The structure reveals a large lobe and a small lobe connected by a hydrophobic pivot. The large lobe contains a putative substrate-binding pocket that is shielded from the small lobe by a lid, suggesting an inactive conformation in which substrate access is blocked. A working model proposes that the lid opens via relative rotation of the lobes around the hydrophobic pivot upon activation, allowing substrate recruitment.

## Publications

### doi/10.1073##pnas.1414837111

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4r12">4R12</a></td>
      <td>1.95 A</td>
      <td></td>
      <td>Nicastrin ECD (residues 19-611) from Dictyostelium purpureum with N-terminal gp67 signal peptide and 8xHis tag</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 insect cells (baculovirus)
- **Construct**: Nicastrin ECD (residues 19-611) fused with N-terminal gp67 signal peptide and 8xHis tag in pFastBac Dual vector
- **Notes**: Bacmid generated in DH10Bac cells. Baculoviruses generated and amplified in Sf9 cells. Hi5 cells transfected with baculovirus for 48 h. Secreted protein purified from medium.

**Purification:**

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: N-terminal gp67 signal peptide + 8xHis tag
- **Tag info**: 8xHis tag

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
      <td>Nickel <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (IMAC)</td>
      <td>Nickel affinity (Qiagen)</td>
      <td></td>
      <td>Secreted protein purified from culture medium.</td>
    </tr>
    <tr>
      <td>Anion exchange chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a></td>
      <td>Source-15Q (GE Healthcare)</td>
      <td></td>
      <td>Anion exchange chromatography for further purification.</td>
    </tr>
    <tr>
      <td>Deglycosylation</td>
      <td>Enzymatic deglycosylation</td>
      <td>--</td>
      <td></td>
      <td>Deglycosylation by endoF3 to remove N-linked glycans just before gel filtration.</td>
    </tr>
    <tr>
      <td>Gel filtration chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (GE Healthcare)</td>
      <td>25 mM Tris pH 8.0, 150 mM NaCl</td>
      <td>Final purification step.</td>
    </tr>
  </tbody>
</table>
**Final sample**: 10 mg/mL in 25 mM Tris pH 8.0, 150 mM NaCl
**Purity**: >95%

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>10 mg/mL nicastrin ECD in 25 mM Tris pH 8.0, 150 mM NaCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M Tris pH 8.0, 0.2 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 20% (wt/vol) <a href="/xray-mp-wiki/reagents/additives/peg3000/">PEG 3000</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3 d (crystals appeared overnight, grew to full size in 3 d)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>0.1 M Tris pH 8.0, 1 M sodium bromide, 20% (wt/vol) <a href="/xray-mp-wiki/reagents/additives/peg3000/">PEG 3000</a>, 10% (vol/vol) <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a> (soak for 1 min)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained by hanging-drop vapor diffusion. Derivative crystals obtained by soaking native crystals for 1 min in cryoprotectant containing 1 M NaBr. Native and bromide-derivatized crystals flash-frozen in cold nitrogen stream at 100 K. Data collected at SSRF beamline BL17U, processed with HKL2000 and CCP4 suite. Br-SAD data used to improve phases for structure determination.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Overall architecture of the nicastrin extracellular domain

The nicastrin ECD comprises a large lobe (alpha/beta fold) and a small lobe (beta-sandwich fold). The large lobe contains a nine-stranded beta-sheet core surrounded by alpha-helices, with three glycosylation sites and two disulfide bonds. Additional structural features include a pair of antiparallel beta-strands and a small globular domain. The small lobe contains five alpha-helices and ten beta-strands forming a seven-stranded beta-sandwich, with two glycosylation sites and one disulfide bond. An extended loop from the small lobe forms a lid that covers the putative substrate-binding site on the large lobe.

### Interface between large and small lobes

The large and small lobes associate through a unique pattern of interactions: a central hydrophobic pivot (Phe244 and Phe245 inserting into a greasy pocket formed by Phe95, Phe152, Phe157, and Ile161) surrounded by eleven hydrogen bonds distributed in a C-shaped pattern at the periphery. The lid from the small lobe extends over the large lobe, with Trp145 nestled in a hydrophobic pocket (His363, Pro399, His421, Tyr423), forming an additional interface that stabilizes the closed conformation.

### Working model for nicastrin function in substrate recruitment

Structural comparison with bacterial aminopeptidase (BAP) revealed that nicastrin's lid covers the putative substrate-binding site, blocking access. The lid-open conformation of BAP suggests a working model where the large and small lobes rotate relative to each other around the central hydrophobic pivot, causing the lid to open and relocate away from the substrate-binding site. This would allow substrate recruitment to the [Gamma-Secretase Complex](/xray-mp-wiki/concepts/enzyme-mechanisms/gamma-secretase/) complex. Consistent with this model, nicastrin was reported to undergo a conformational switch upon inhibitor/substrate binding.

### Updated model of human nicastrin and gamma-secretase TM assignment

The DpNCT crystal structure enabled building an improved atomic model of human nicastrin (HsNCT) ECD containing approximately 100 more amino acids than the previous [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) model. Key conserved features include the hydrophobic pivot, the C-shaped H-bond network, and the lid with conserved Trp164. The nicastrin TM was assigned to the far edge of the thick end of the [Gamma-Secretase Complex](/xray-mp-wiki/concepts/enzyme-mechanisms/gamma-secretase/) TM horseshoe. A revised TM assignment places the Pen-2/PS1-NTF subcomplex at the thin end and PS1-CTF/Aph-1/nicastrin at the thick end.


## Cross-References

- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/gamma-secretase/">Gamma-Secretase Complex</a> — Nicastrin is the substrate-recruiting component of the gamma-secretase complex
- <a href="/xray-mp-wiki/reagents/buffers/buffer-tris/">Tris</a> — Tris buffer used in purification and crystallization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg3000/">PEG 3000</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
