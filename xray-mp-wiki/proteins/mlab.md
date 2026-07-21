---
title: "E. coli MlaB STAS Domain Protein"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.60030]
verified: agent
uniprot_id: P64602
---

# E. coli MlaB STAS Domain Protein

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P64602">UniProt: P64602</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

MlaB is a small STAS (Sulfate Transporter and Anti-Sigma factor Antagonist) domain protein from Escherichia coli that binds to the ABC ATPase subunit [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) of the MlaFEDB phospholipid transport complex. MlaB consists of a minimalist STAS domain with a four-stranded beta-sheet packed against three alpha-helices, lacking the fifth beta-strand and additional C-terminal helix found in canonical STAS domain proteins. MlaB stabilizes [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) by binding to its helical subdomain and C-terminal extension, promoting the assembly of active MlaFEDB transporter complexes. The MlaB binding site on [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) defines a previously undescribed interaction surface on ABC transporters, suggesting a novel mechanism for post-translational regulation of ABC transporter activity.


## Publications

### doi/10.7554##eLife.60030

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xgy">6XGY</a></td>
      <td>2.9 A</td>
      <td>P3_2 21</td>
      <td>Full-length E. coli MlaB (97 residues), residues 2-97 resolved, co-expressed with <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaf/">MLAF</a>, N-terminal His6-TEV tag</td>
      <td>None (ADP bound to <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaf/">MLAF</a>)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xgz">6XGZ</a></td>
      <td>2.6 A</td>
      <td>P2_1 2_1 2_1</td>
      <td>Full-length E. coli MlaB (97 residues), residues 2-97 resolved, co-expressed with <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaf/">MLAF</a>, apo state</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli Rosetta 2 (DE3), T7-based co-expression with [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/)
- **Construct**: Full-length MlaB (97 residues) with N-terminal His6-TEV tag, co-expressed from a bicistronic operon with [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/). MlaB is not stable when expressed alone and is prone to precipitation; co-expression with [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) is required for purification in good yield.


**Purification:**

- **Expression system**: E. coli Rosetta 2 (DE3)
- **Tag info**: N-terminal His6-TEV tag on MlaB

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
      <td>Freeze-thaw / Emulsiflex</td>
      <td>--</td>
      <td>50 mM Tris pH 8.0, 300 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1 mg/ml lysozyme, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 25U benzonase + --</td>
      <td>Clarified lysate by centrifugation</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>IMAC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose</td>
      <td>50 mM Tris pH 8.0, 300 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash); 50 mM Tris pH 8.0, 300 mM NaCl, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (elution) + --</td>
      <td>MlaB co-purifies with <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaf/">MLAF</a> as a stable complex</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 16/60</td>
      <td>20 mM Tris pH 8.0, 150 mM NaCl, 2 mM TCEP + --</td>
      <td>MlaFB complex elutes at ~40 kDa</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>MlaFB complex at 24 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.7 M ammonium dihydrogen phosphate, 0.07 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 5.6, 30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir + 5% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Co-crystallized with <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaf/">MLAF</a> as MlaFB complex. Apo structure (MlaF_1B_1, PDB 6XGZ).</td>
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
    <tr>
      <td>pH</td>
      <td>5.6</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Citrate: 0.07 M [buffer]  
- Glycerol: 30 % [additive]</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>MlaFB complex at 24 mg/ml + 2 mM ADP + 2 mM magnesium acetate</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M magnesium formate</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir + 35% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>ADP-bound structure (MlaF_2B_2, PDB 6XGY). Phased using BALBES.</td>
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
    <tr>
      <td>Temperature (structured)</td>
      <td>4 C</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Minimalist STAS domain architecture

MlaB is a minimalist member of the STAS domain family, consisting of a
four-stranded beta-sheet packed against three alpha-helices. Unlike canonical
STAS domains such as SpoIIAA which have a fifth beta-strand and an additional
C-terminal helix, MlaB's C-terminus is too short to form these elements.
MlaB is more structurally similar to the smaller STAS domains associated with
SLC26/SulP transporters. The conserved Ser/Thr residue (Thr52) implicated in
phosphoregulation of STAS domains is present in MlaB.

### MlaB stabilizes MlaF for complex assembly

MlaB is required for [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) stability and productive assembly of the MlaFEDB
transporter complex. [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) cannot be expressed and purified alone in significant
quantities, but co-expression with MlaB yields stable MlaFB complex. In cells,
deletion of mlaFEDCB operon components lacking MlaB (MlaFEDC) results in loss
of both [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) and MlaB from purified complexes. Overexpression of [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) fully
suppresses the mlaB knockout phenotype, indicating that MlaB has no essential
function in Mla transport beyond promoting [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) stability and association with
MlaED.

### STAS domain as an ABC transporter regulator

MlaB binds to the helical subdomain of [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) at a site distant from the ATP
binding pocket, defining a previously undescribed interaction surface on ABC
transporters. This binding mode is distinct from all other characterized ABC
transporter regulatory interactions. MlaB may regulate Mla transport activity
indirectly by modulating [MLAF](/xray-mp-wiki/proteins/structural-adhesion/mlaf/) stability and availability for complex assembly
with MlaED. This raises the possibility that STAS domain proteins may regulate
other ABC transporters through analogous mechanisms.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaf/">E. coli MlaF ABC ATPase</a> — Binding partner; MlaF stabilization and complex assembly require MlaB
- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaD/">E. coli MlaD MCE Protein</a> — Transmembrane/periplasmic component of the MlaFEDB complex
- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaC/">E. coli MlaC Periplasmic Lipid-Binding Protein</a> — Periplasmic shuttle protein in the Mla pathway
- <a href="/xray-mp-wiki/proteins/miscellaneous/mlaA/">E. coli MlaA Outer Membrane Lipoprotein</a> — Outer membrane component of the Mla system
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter</a> — MlaB regulates the MlaFEDB ABC transporter complex
- <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a> — ADP-bound state of the MlaF_2B_2 structure
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a> — Additive used in purification or crystallization buffers
