---
title: "NorM-VC (Vibrio cholerae NorM) - MATE Family Multidrug Efflux Transporter"
created: 2026-06-02
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09408]
verified: regex
uniprot_id: Q9R381
---

# NorM-VC (Vibrio cholerae NorM) - MATE Family Multidrug Efflux Transporter

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9R381">UniProt: Q9R381</a>

<span class="expr-badge">Salmonella CHOLERAESUIS</span>

## Overview

NorM-VC is a multidrug and toxic compound extrusion (MATE) family transporter from Vibrio cholerae that functions as a drug efflux pump. It is a secondary transporter with 12 transmembrane helices that exports a broad range of organic cations including [Ethidium - Fluorescent Intercalating Dye](/xray-mp-wiki/reagents/ligands/ethidium/) bromide, [Doxorubicin - Anthracycline Anticancer Drug](/xray-mp-wiki/reagents/ligands/doxorubicin/), and rhodamine 6G. NorM-VC represents the first crystal structure of a prokaryotic MATE family member and revealed the bilobate architecture characteristic of the MATE family with pseudo-symmetric N- and C-lobes (TM1-6 and TM7-12). The structure was solved in two crystal forms: a native crystal and a rubidium-bound crystal, revealing a cation-binding site centered on D371.


## Publications

### doi/10.1038##nature09408

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2vbq">2VBQ</a></td>
      <td>3.65</td>
      <td>P 212121</td>
      <td>Full-length NorM from Vibrio cholerae (V. cholerae), residues 1-458</td>
      <td>Rb+ in Crystal 2; no ligand in Crystal 1 (native)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 DE3 transformed with pET19b-norM-VC expression vector
- **Construct**: pET19b-norM-VC fusion expression in E. coli BL21 DE3

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
      <td>Recombinant NorM-VC production and native NorM-VC purification</td>
      <td>Expression in E. coli BL21 DE3 / pET19b-norM-VC; native NorM-VC purified from V. cholerae membrane fraction</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Details not available in supplementary information; main paper required for full purification protocol</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion crystallization; two crystal forms obtained</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Native NorM-VC for Crystal 1; NorM-VC soaked with Rb+ for Crystal 2</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal 1 (native): P 212121, a=142.8, b=240.8, c=45.7 A; Crystal 2 (Rb+-bound): P 212121, a=159.6, b=241.7, c=46.2 A. Phasing by <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> averaging using PHASER. Data collection at CLS (08ID-1), ALS (BL 8.2.2), and SSRL (BL 11-1).</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Bilobate 12-TM architecture with pseudo-symmetry

NorM-VC adopts the characteristic bilobate MATE family architecture with two pseudo-symmetric domains: an N-lobe (TM1-6) and a C-lobe (TM7-12) related by a pseudo-2-fold rotation axis. The structure contains two monomers (NorM1 and NorM2) in the asymmetric unit, each with 12 transmembrane helices. The internal cavity between the two lobes forms the substrate-binding pocket, which is accessible from the extracellular side in the outward-facing conformation.

### Cation-binding site centered on D371

A cation-binding site was identified in the internal cavity of NorM-VC, centered on residue D371 in TM10. Soaking crystals with Rb+ and Cs+ revealed distinct anomalous peaks at 5.5 sigma and 5.0 sigma respectively. Mutational analysis (D371N and D371A) abolished cation binding, confirming D371 as essential for cation coordination. This site is located near the proposed substrate-binding region and may play a role in the transport mechanism.

### Substrate binding profile

NorM-VC binds multiple drug substrates with measurable affinity. Fluorescence polarization assays revealed a Kd of 1.00 +/- 0.08 uM for [Doxorubicin - Anthracycline Anticancer Drug](/xray-mp-wiki/reagents/ligands/doxorubicin/) and a Kd of 2.09 +/- 0.0115 uM for rhodamine 6G. Functional assays showed that recombinant NorM-VC expressed in E. coli BL21 DE3 delta acrAB significantly reduces [Ethidium - Fluorescent Intercalating Dye](/xray-mp-wiki/reagents/ligands/ethidium/) bromide accumulation compared to vector-only controls, confirming its role as a multidrug efflux pump.

### Topology and membrane orientation

Topology was verified using single-cysteine mutagenesis combined with [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) labeling. Sixteen cysteine mutants (K10C, S26C, V76C, E91C, L101C, S103C, A149C, M164C, V182C, V216C, A260C, A296C, M323C, Y367C, S397C, F429C) were generated and analyzed by [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) difference Fourier maps. All 16 mutants showed [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) peaks consistent with the predicted topology: extracellular loops at positions 10, 76, 149, 216, 296, 397, and 429; cytoplasmic loops at positions 26, 91, 103, 164, 182, 260, 323, and 367.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/doxorubicin/">Doxorubicin</a> — NorM-VC binds doxorubicin with Kd = 1.00 +/- 0.08 uM (Table S1)
- <a href="/xray-mp-wiki/reagents/ligands/rhodamine-6g/">Rhodamine 6G</a> — NorM-VC binds rhodamine 6G with Kd = 2.09 +/- 0.0115 uM (Table S1)
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/mate-transporter-family/">MATE Transporter Family</a> — NorM-VC is the first prokaryotic MATE family member with a crystal structure
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily</a> — MATE transporters are secondary transporters related to MFS family
- <a href="/xray-mp-wiki/proteins/abc-transporters/ntmate2/">NtMATE2 (Nicotiana tabacum MATE2)</a> — Another MATE family member with crystal structure for comparison
- <a href="/xray-mp-wiki/proteins/abc-transporters/casmate/">CasMATE (Camelina sativa MATE Transporter)</a> — Eukaryotic MATE transporter for structural comparisons
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> — Related biological concept
- <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury (HgCl2) - Aquaporin Inhibitor</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/ligands/ethidium/">Ethidium - Fluorescent Intercalating Dye</a> — Related ligand or cofactor
