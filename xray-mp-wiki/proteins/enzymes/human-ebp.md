---
title: "Human Emopamil-Binding Protein (EBP)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-10279-w]
verified: agent
---

# Human Emopamil-Binding Protein (EBP)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-hek293">HEK293</span></div>


## Overview

Emopamil-Binding Protein (EBP), also known as 3-beta-hydroxysteroid-Delta8,Delta7-isomerase, is an endoplasmic reticulum membrane protein that catalyzes the conversion of Delta8-sterols to Delta7-isomers in the [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) biosynthesis pathway. EBP is a five-transmembrane helix protein that adopts an unreported fold. It binds a structurally diverse array of pharmacologically active compounds including [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/), antidepressants, antipsychotics, and opioid analgesics, mediating drug resistance. Mutations in EBP cause Conradi-Hunermann syndrome, an X-linked dominant chondrodysplasia punctata.


## Publications

### doi/10.1038##s41467-019-10279-w

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6oht">6OHT</a></td>
      <td>3.2</td>
      <td>P2(1)2(1)2</td>
      <td>Full-length human EBP (residues 1-230), residues 1-6, 53-59, 220-230 not visible</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/u18666a/">U18666A</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ohu">6OHU</a></td>
      <td>3.5</td>
      <td>P2(1)2(1)2</td>
      <td>Full-length human EBP (residues 1-230), residues 1-6, 53-59, 220-230 not visible</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tamoxifen/">Tamoxifen</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus-mediated transduction of HEK-293S GnTI- cells
- **Construct**: Full-length human EBP with N-terminal Strep-tag (crystallization) or N-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (binding assays)
- **Notes**: Cells harvested 48 h post-infection

**Purification:**

- **Expression system**: HEK-293S GnTI- (baculovirus-mediated)
- **Expression construct**: N-terminal Strep-tag or [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/)
- **Tag info**: Strep-tag II (crystallization), [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (binding assays)

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
      <td></td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl, 1 mM PMSF, 5 ug/mL leupeptin, 10 uM ligand</td>
      <td>10 uM <a href="/xray-mp-wiki/reagents/ligands/tamoxifen/">Tamoxifen</a> or <a href="/xray-mp-wiki/reagents/ligands/u18666a/">U18666A</a> added in all purification steps</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td></td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a></td>
      <td>Incubated 1 h at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Strep-Tactin or <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity</td>
      <td>Strep-Tactin (IBA) or <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> (Qiagen)</td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a></td>
      <td>Eluted with 2.5 mM <a href="/xray-mp-wiki/reagents/ligands/desthiobiotin/">Desthiobiotin</a> (Strep) or 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (<a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a>)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified EBP in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> with 10 uM <a href="/xray-mp-wiki/reagents/ligands/u18666a/">U18666A</a> or <a href="/xray-mp-wiki/reagents/ligands/tamoxifen/">Tamoxifen</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained only with <a href="/xray-mp-wiki/reagents/ligands/u18666a/">U18666A</a> or <a href="/xray-mp-wiki/reagents/ligands/tamoxifen/">Tamoxifen</a> present. Structure determined by Se-SAD and refined at 3.2 A (<a href="/xray-mp-wiki/reagents/ligands/u18666a/">U18666A</a>) and 3.5 A (<a href="/xray-mp-wiki/reagents/ligands/tamoxifen/">Tamoxifen</a>). Final models: 93.07%/6.93%/0.0% and 91.09%/8.74%/0.17% in favored/allowed/outlier Ramachandran regions.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>sitting-drop</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Catalytic mechanism of sterol isomerization

EBP catalyzes the conversion of Delta8-sterols to Delta7-isomers through a putative mechanism involving a catalytic triad (His76, Glu80, Glu122). His76 acts as a proton donor, protonating Delta8-sterol at C9a to generate a carbocationic intermediate at C8, which is stabilized by Trp196 through pi-cation interaction. Glu80 (stabilized by Glu122) then deprotonates at C7-beta. The helix H1 linker between TM2 and TM3 serves as a gate allowing proton/water access from the ER lumen.

### Multidrug recognition mechanism

EBP binds structurally diverse compounds including [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/), [U18666A](/xray-mp-wiki/reagents/ligands/u18666a/), antidepressants, and antipsychotics. These compounds share a positively-charged amine group that mimics the carbocationic sterol intermediate. Trp196 stabilizes compounds through pi-cation interactions, while His76, Glu80, Glu122, and Asn193 form electrostatic and hydrogen bond interactions. The large hydrophobic membrane cavity formed by TMs 2-5 accommodates the structurally diverse ligands.

### Disease relevance - Conradi-Hunermann syndrome

Mutations in the EBP gene cause Conradi-Hunermann syndrome (X-linked dominant chondrodysplasia punctata), characterized by bone, skin, and eye abnormalities. Biochemical studies show increased 8,9-unsaturated sterols in plasma and tissues of affected patients. Disease mutations map to various regions including solvent entry, sterol binding/entry, catalytic sites, and dimerization interfaces.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/tamoxifen/">Tamoxifen</a> — EBP binds tamoxifen; crystal structure of EBP-tamoxifen complex determined
- <a href="/xray-mp-wiki/reagents/ligands/u18666a/">U18666A</a> — EBP binds U18666A; crystal structure of EBP-U18666A complex determined
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/ligands/desthiobiotin/">Desthiobiotin</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a> — Fusion tag for crystallization or purification
