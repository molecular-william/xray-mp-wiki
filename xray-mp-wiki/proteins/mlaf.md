---
title: "E. coli MlaF ABC ATPase"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.60030]
verified: agent
uniprot_id: P64602
---

# E. coli MlaF ABC ATPase

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P64602">UniProt: P64602</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

MlaF is the cytoplasmic ABC ATPase (nucleotide binding domain, NBD) component of the MlaFEDB ABC transporter complex from Escherichia coli. Together with the transmembrane domain protein MlaE, the periplasmic MCE domain protein [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaD/), and the STAS domain regulatory protein [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/), MlaF drives phospholipid trafficking across the bacterial envelope to maintain outer membrane integrity. MlaF exhibits a canonical ABC ATPase fold with catalytic and helical subdomains, and possesses a unique ~25 amino acid C-terminal extension (CTE) that forms a domain-swapped reciprocal 'handshake' with the adjacent MlaF subunit, stabilizing the MlaF dimer. The signature motif of MlaF (LSGGM) contains a rare methionine instead of the consensus glutamine at its final position, a feature conserved in Mla and TGD-like MCE transport systems.


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
      <td>Full-length E. coli MlaF (269 residues), residues 5-267 resolved, co-expressed with <a href="/xray-mp-wiki/proteins/structural-adhesion/mlab/">MLAB</a> with N-terminal His-TEV tag</td>
      <td>ADP, Mg²⁺</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xgz">6XGZ</a></td>
      <td>2.6 A</td>
      <td>P2_1 2_1 2_1</td>
      <td>Full-length E. coli MlaF (269 residues), residues 5-267 resolved, co-expressed with <a href="/xray-mp-wiki/proteins/structural-adhesion/mlab/">MLAB</a>, apo form (no nucleotide)</td>
      <td>None (apo)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli Rosetta 2 (DE3), T7-based expression
- **Construct**: Full-length MlaF (269 residues) co-expressed with [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) from a bicistronic operon. MlaF with N-terminal Strep tag (optional), [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) with N-terminal His6-TEV tag. For MlaFEDB complex purification, constructs encoded the entire mlaFEDCB operon with N-terminal His-TEV tag on [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaD/).


**Purification:**

- **Expression system**: E. coli Rosetta 2 (DE3)
- **Tag info**: His6-TEV tag on [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) (for MlaFB complex), His-TEV tag on [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaD/) (for MlaFEDB complex)

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
      <td>Freeze-thaw lysis for small-scale. Emulsiflex-C3 for large-scale. Clarified by centrifugation at 15,000g.</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose (GE Healthcare)</td>
      <td>Ni Wash Buffer (50 mM Tris pH 8.0, 300 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>); Ni Elution Buffer (50 mM Tris pH 8.0, 300 mM NaCl, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>) + --</td>
      <td>Batch binding at 4°C, followed by wash and elution</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 16/60 (GE Healthcare)</td>
      <td>20 mM Tris pH 8.0, 150 mM NaCl, 2 mM TCEP + --</td>
      <td>MlaFB complex elutes at ~40 kDa (1:1 heterodimer)</td>
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
      <td>MlaFB complex at 24 mg/ml in 20 mM Tris pH 8.0, 150 mM NaCl, 2 mM TCEP</td>
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
      <td>Reservoir solution supplemented with 5% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of apo MlaFB (MlaF_1B_1, PDB 6XGZ). 100 nL + 100 nL drop.</td>
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
      <td>MlaFB complex at 24 mg/ml supplemented with 2 mM ADP and 2 mM magnesium acetate in 20 mM Tris pH 8.0, 150 mM NaCl, 2 mM TCEP</td>
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
      <td>Reservoir solution supplemented with 35% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of ADP-bound MlaFB (MlaF_2B_2, PDB 6XGY). 100 nL + 100 nL drop. Phased using BALBES with search models 2OUK (MlaF) and 3F43 (<a href="/xray-mp-wiki/proteins/structural-adhesion/mlab/">MLAB</a>).</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Unique C-terminal extension handshake

MlaF possesses a unique ~25 amino acid C-terminal extension (CTE, residues
247-269) that wraps around the neighboring MlaF subunit in a domain-swapped
reciprocal 'handshake'. Three hydrophobic residues (Tyr261, Leu265, Leu266)
at the tip of the CTE dock into a pocket at the MlaF-[MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) interface of the
adjacent subunit. Deletion of the CTE completely abolishes MlaF function in
cellular assays and prevents MlaF from stably associating with MlaE in the
MlaFEDB complex, despite having no effect on MlaF-[MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) binding. Artificial
dimerization via GCN4 leucine zipper partially rescues ΔCTE function,
suggesting the CTE promotes NBD dimerization.

### MlaF signature motif variation

MlaF contains a rare substitution in its ABC signature motif: 145-LSGGM-149
instead of the consensus LSGGQ. The methionine at the final position cannot
hydrogen bond to the 2' and 3' hydroxyls of the ATP ribose as glutamine does.
This substitution may impair MlaF's ability to discriminate between ATP and
deoxyATP or decrease its affinity for NTPs. Methionine at this position is
conserved in Mla and TGD-like MCE systems, as well as O-antigen and teichoic
acid transporters, suggesting functional similarity.

### MlaF-MlaB interaction defines a novel regulatory site

[MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) binds to the helical subdomain of MlaF at a site that is distant from
the ATP-binding pocket (~30 Å from nearest ADP). The binding interface
involves contributions from both MlaF subunits in the dimer, with the helical
subdomain making extensive contacts with all three [MLAB](/xray-mp-wiki/proteins/structural-adhesion/mlab/) helices, and the CTE
of the opposite MlaF subunit providing additional contacts. This binding site
is distinct from all previously characterized ABC transporter regulatory
interactions, defining a potentially novel mechanism of ABC transporter
regulation through STAS domain proteins.


## Cross-References

- <a href="/xray-mp-wiki/proteins/mlaB/">E. coli MlaB STAS Domain Protein</a> — Binding partner that stabilizes MlaF and promotes MlaFEDB complex assembly
- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaD/">E. coli MlaD MCE Protein</a> — Transmembrane/periplasmic component of the MlaFEDB complex
- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaC/">E. coli MlaC Periplasmic Lipid-Binding Protein</a> — Periplasmic shuttle protein in the Mla lipid transport pathway
- <a href="/xray-mp-wiki/proteins/miscellaneous/mlaA/">E. coli MlaA Outer Membrane Lipoprotein</a> — Outer membrane component of the Mla lipid transport system
- <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a> — Bound nucleotide in the MlaF_2B_2 dimeric structure (post-hydrolysis state)
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter</a> — MlaF is the NBD of the MlaFEDB ABC transporter complex
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlab/">MLAB</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
