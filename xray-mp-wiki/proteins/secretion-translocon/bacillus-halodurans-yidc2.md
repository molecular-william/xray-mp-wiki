---
title: "Bacillus halodurans YidC2 (BhYidC2)"
created: 2026-06-16
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##nature13167]
verified: agent
uniprot_id: ['Q9SZU7', 'O26232']
---

# Bacillus halodurans YidC2 (BhYidC2)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<span class="badge badge-uniprot badge-uniprot-none" title="Bacillus halodurans">No UniProt</span> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9SZU7" title="Arabidopsis thaliana">UniProt: Q9SZU7</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O26232" title="Methanothermobacter thermautotrophicus">UniProt: O26232</a>

<span class="expr-badge">Bacillus halodurans</span>

## Overview

YidC is a conserved membrane protein insertase that inserts its substrates into the membrane, thereby facilitating membrane protein assembly in bacteria. The 2.4 Å crystal structure of Bacillus halodurans YidC2 reveals a novel fold with five conserved transmembrane helices forming a positively charged hydrophilic groove that is open towards both the lipid bilayer and the cytoplasm but closed on the extracellular side. The conserved arginine residue R72 in the groove is critical for substrate recognition and membrane protein insertion. YidC functions as both a Sec-independent insertase and a Sec-dependent membrane chaperone.

## Publications

### doi/10.1038##nature13167

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3w06">3W06</a></td>
      <td>2.4</td>
      <td></td>
      <td>B. halodurans YidC2 residues 27-266</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3w07">3W07</a></td>
      <td>2.4</td>
      <td></td>
      <td>B. halodurans YidC2 residues 27-267 (with GFP tag)</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41(DE3) + pRARE
- **Construct**: B. halodurans YidC2 residues 1-266 (or 1-267) with N-terminal His8 tag or GFP-His8 tag, cleaved by TEV protease

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified YidC in 300 mM NaCl, 20 mM Tris-HCl pH 8.0, mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (2:3 protein:lipid w/w)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein-lipid mixture (50 nl) overlaid with 800 nl precipitant solution. Crystals grown at 20°C. Structure determined by multi-wavelength anomalous diffraction using methyl-mercury-chloride-derivatized YidC (Y150C mutant). Diffraction data at SPring-8 BL32XU.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Hydrophilic groove mechanism for membrane protein insertion

YidC contains a positively charged hydrophilic groove (~2,000 Å³) formed by TM1-5. The groove contains conserved hydrophilic residues (T68, R72, Q82, Q142, Q187, N248, Q254) and is filled with ~20 water molecules. The conserved R72 creates a strong positive electrostatic potential. The groove is open to the cytoplasm and membrane interior but sealed on the extracellular side by a rigid hydrophobic core. Substrate proteins with acidic N-terminal extracellular regions are transiently captured in this groove.

### C1 region function

The C1 region (cytosolic domain between TM2 and TM3, containing CH1 and CH2 helices) is crucial for YidC-mediated membrane insertion of single-spanning membrane proteins like MifM. Deletion mutants of the C1 region substantially impair insertion activity.

### Substrate recognition via electrostatic interactions

The conserved arginine R72 in the groove interacts with acidic residues in the N-terminal extracellular tails of substrates such as MifM and Pf3 coat protein. In vivo photo-crosslinking using pBpa introduced at Q187 and W244 in the groove confirmed direct substrate binding at the groove.


## Cross-References

- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Additive used in purification or crystallization buffers
