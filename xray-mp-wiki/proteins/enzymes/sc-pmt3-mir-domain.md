---
title: "Pmt3-MIR Domain (S. cerevisiae Protein O-Mannosyltransferase MIR Domain)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.61189]
verified: regex
uniprot_id: P47190
---

# Pmt3-MIR Domain (S. cerevisiae Protein O-Mannosyltransferase MIR Domain)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P47190">UniProt: P47190</a>

<span class="expr-badge">Saccharomyces cerevisiae</span>

## Overview

The Pmt3-MIR domain is the luminal MIR domain of Pmt3, a member of the PMT2 subfamily of protein O-mannosyltransferases (PMTs) from Saccharomyces cerevisiae. Pmt3 is highly homologous to Pmt2 (both PMT2 subfamily members) and its MIR domain adopts the same canonical beta-trefoil fold. The structure was solved at 1.9 A resolution by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using Pmt2-MIR as a search model. Pmt3-MIR is almost identical to Pmt2-MIR in overall fold, differing primarily in MIRm3 loop regions. Pmt3-MIR contains the same conserved carbohydrate-binding sites (sites alpha and beta) and the PMT2-subfamily-specific FKR motif.


## Publications

### doi/10.7554##eLife.61189

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zqq">6ZQQ</a></td>
      <td>1.9</td>
      <td>P 1</td>
      <td>Pmt3-MIR domain</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Pmt3-MIR domain with N-terminal His6 tag and TEV protease cleavage site, expressed in BL21(DE3) or SHuffle T7 Express
- **Notes**: MIR domain was thermostable and readily formed crystals

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: Pmt3-MIR with N-terminal His6 tag and TEV protease cleavage site
- **Tag info**: His6 tag cleaved by TEV protease

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
      <td>Microfluidizer</td>
      <td>—</td>
      <td>20 mM Tris-HCl pH 7.0, 200 mM NaCl, 1 mM MgCl2, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, protease inhibitor cocktail</td>
      <td></td>
    </tr>
    <tr>
      <td>Centrifugation</td>
      <td>Centrifugation at 48,000 x g, 25 min</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HisTrap <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>HisTrap (GE Healthcare)</td>
      <td>20 mM Tris-HCl pH 7.0, 200 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
      <td></td>
    </tr>
    <tr>
      <td>TEV protease cleavage</td>
      <td>TEV protease cleavage overnight at 4 C</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HisTrap reverse purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (flow-through)</td>
      <td>HisTrap</td>
      <td></td>
      <td>TEV protease and cleaved His-tag bind to column, Pmt3-MIR flows through</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>Superdex 75 26/600</td>
      <td>20 mM Tris-HCl pH 7.0, 200 mM NaCl</td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: 15 mg/ml Pmt3-MIR in 20 mM Tris-HCl pH 7.0, 200 mM NaCl

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>15 mg/ml Pmt3-MIR</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M MES pH 6.0, 0.26 M <a href="/xray-mp-wiki/reagents/additives/calcium-acetate/">Calcium Acetate</a>, 15% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 8000</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>2:1 (200 nL protein + 100 nL reservoir)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Quick soak in reservoir supplemented with 20% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> before plunging into liquid nitrogen</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Structural conservation within PMT2 subfamily MIR domains

Pmt3-MIR is structurally almost identical to Pmt2-MIR (rmsd below detection limits for core beta-trefoil fold). Both domains contain conserved carbohydrate-binding sites alpha and beta with identical key residues (histidine pairs H362/H364 in site alpha, H428/H430 in site beta), and the PMT2-specific FKR motif at site delta. The high structural conservation suggests all PMT2 subfamily MIR domains share the same carbohydrate-binding function.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/sc-pmt2-mir-domain/">Pmt2-MIR Domain</a> — Pmt2-MIR is the close homolog with nearly identical structure, solved in the same study
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/mir-domain/">MIR Domain (Mannosyltransferase, IP3R, RyR)</a> — Pmt3-MIR is a member of the MIR domain family
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/calcium-acetate/">Calcium Acetate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
