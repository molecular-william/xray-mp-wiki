---
title: "V1-ATPase from Thermus thermophilus"
created: 2026-05-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##emboj.2009.310, doi/10.1038##embor.2009.202, doi/10.1016##j.jmb.2013.04.022]
verified: regex
uniprot_id: Q56404
---

# V1-ATPase from Thermus thermophilus

<div class="expr-badges"><span class="expr-badge expr-t-thermophilus">T. thermophilus</span> <span class="expr-badge expr-native-tissue">Native tissue</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q56404">UniProt: Q56404</a>

<span class="expr-badge">Thermus thermophilus</span>

## Overview

V-type ATPase (V-ATPase) is a rotary ATPase complex that mediates energy conversion between the chemical energy of ATP and ion gradients across membranes. The extrinsic V1 domain (V1-ATPase) of Thermus thermophilus, composed of A3B3DF subunits, provides structural insight into the torque generation mechanism shared by rotary ATPases. The 2.8 A X-ray crystal structure of the isolated A3B3 subcomplex reveals significant differences from the alpha3beta3 sub-domain in F1-ATPase, including a protruding bulge domain in the catalytic A subunits. Mutational analysis at the catalytic B-A interface identified a hydrophobic cluster essential for ATP hydrolysis. The full 3.9 A V1-ATPase structure (A3B3DF) reveals asymmetric intersubunit interactions and rigid-body rearrangements that underlie the catalytic cycle. The 4.5 A nucleotide-bound V1-ATPase structure reveals inter-subunit interactions and the straight central stalk of the D and F subunits, with small conformational changes of respective subunits and significant quaternary rearrangement of the three AB pairs related to the interaction with the straight central stalk.

## Publications

### doi/10.1038##emboj.2009.310

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3gqb">3GQB</a></td>
      <td>2.8 A</td>
      <td>P321</td>
      <td>A3B3 subcomplex from Thermus thermophilus V-ATPase (cysteine mutant: A/C28S/C255S/C508S, B/C265S); nucleotide-free</td>
      <td>None (nucleotide-free; bound nucleotides removed by Pi-<a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> treatment)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Thermus thermophilus HB8 (native extraction)
- **Construct**: Native V1-ATPase complex consisting of A3B3DF subunits; no heterologous expression tags or mutations

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified A3B3 subcomplex (cysteine mutant: A/C28S/C255S/C508S, B/C265S); nucleotides removed by Pi-<a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> treatment</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not explicitly reported in this paper; crystallization conditions described in earlier work</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not explicitly reported</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not explicitly reported</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash-frozen with nitrogen gas streams</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group P321, unit cell a=b=199.4 A, c=179.0 A. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with PHASER using archaeal A (1VDZ) and B (2C61) subunits as search models. Two AB heterodimers in asymmetric unit. 15% twinning detected. R=25.0%, R_free=28.1%. Data processed to 2.8 A resolution using Denzo and Scalepack.</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##embor.2009.202

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3a5d">3A5D</a></td>
      <td>4.8 A</td>
      <td>P321</td>
      <td>V1-ATPase A3B3DF from Thermus thermophilus; nucleotide-free; two molecules per asymmetric unit</td>
      <td>None (nucleotide-free)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3a5c">3A5C</a></td>
      <td>4.5 A</td>
      <td>P321</td>
      <td>V1-ATPase A3B3DF from Thermus thermophilus; nucleotide-bound (Mg2+ ADP and AlFx)</td>
      <td>ADP + AlFx (nucleotide-bound; Mg2+ ADP and aluminum fluoride co-crystallized)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Thermus thermophilus HB8 (native extraction)
- **Construct**: Native V1-ATPase complex consisting of A3B3DF subunits; no heterologous expression tags or mutations

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified V1-ATPase A3B3DF from Thermus thermophilus; two forms crystallized: nucleotide-free and nucleotide-bound (Mg2+ ADP + AlFx)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM MES buffer (pH 6.0), 1.6 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a>, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/dioxane/">Dioxane</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not explicitly reported; crystals obtained after 45 min for nucleotide-bound form</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals soaked in cryoprotectant solution (100 mM MES pH 6.0, 1.9 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a>, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>) and flash-frozen under nitrogen gas stream at -183 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Nucleotide-free structure refined at 4.8 A resolution (R/Rfree: 44.1/45.2). Nucleotide-bound structure refined at 4.5 A resolution (R/Rfree: 43.0/43.6). Both in space group P321. Two molecules per asymmetric unit. Heavy atom derivatives prepared by soaking in platinum and <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury (HgCl2) - Aquaporin Inhibitor</a> compounds. Structure solved by combination of <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> and <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a>. Beamlines: BL17A (Photon Factory), BL38B1, BL41XU, BL44XU (SPring-8).</td>
    </tr>
  </tbody>
</table>
### doi/10.1016##j.jmb.2013.04.022

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3w3a">3W3A</a></td>
      <td>3.9 A</td>
      <td>P 21 21 21</td>
      <td>V1-ATPase A3B3DF from Thermus thermophilus (three A subunits, three B subunits, one D subunit, one F subunit)</td>
      <td>ADP (bound at two of three catalytic A subunit P-loops)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Thermus thermophilus HB8 (native extraction)
- **Construct**: Native V1-ATPase complex consisting of A3B3DF subunits; no heterologous expression tags or mutations

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
      <td>Native extraction</td>
      <td>Native extraction from Thermus thermophilus HB8 cells</td>
      <td>--</td>
      <td>Buffer composition not explicitly reported in this paper; see Nagamatsu et al. (2010) for detailed protocol + --</td>
      <td>Purification and crystallization procedures were described previously in Nagamatsu et al. 2010 (PDB: 3A5C, 4.5 A resolution). V1-ATPase was purified from Thermus thermophilus HB8 by native extraction.</td>
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
      <td>Purified V1-ATPase complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>1.6 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a>, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/dioxane/">Dioxane</a>, 100 mM MES buffer (pH 6.0), 10 mM ADP, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a>, 1.0 mM aluminum nitrate, 1.0 mM potassium fluoride</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not explicitly reported; large crystals (>0.4 mm x 0.4 mm x 0.4 mm) were obtained</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals were flash-frozen with nitrogen gas streams at -183 C after soaking in cryoprotectant solution (no additional cryoprotectant beyond reservoir solution required)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>More than 100 crystals were used for diffraction screening at SPring-8 beamlines BL41XU and BL44XU. A complete data set (90.3% completeness) was merged from 20 incident points of 7 crystals. Structure determined by <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> phasing with five heavy-atom derivatives, refined with DEN method.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Asymmetric A3B3 subcomplex conformation in the V1 complex

The A3B3 portion undergoes a large conformational change upon binding to the DF subcomplex, with A and B subunits retracting toward the center. This retraction is caused by attractive interactions between A3B3 and DF, making A3B3 in the V1 complex more asymmetric than the isolated A3B3 subcomplex. This asymmetric feature is consistent with [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) analyses of the full V-ATPase complex, indicating the structure represents native V1 features.

### No large interdomain motion in catalytic A subunits

Unlike F1-ATPase from various species and V1-ATPase from Enterococcus hirae, the catalytic A subunits of V1-ATPase from T. thermophilus do not exhibit large interdomain motion. This contrasts with the significant intrasubunit domain motion seen in the catalytic beta subunit of F1-ATPase, suggesting different conformational mechanisms among rotary ATPase families.

### Asymmetry via rigid-body rearrangements of AB pairs

The asymmetry among the three AB pairs (ANBN, AN'BN', and AWBW) is mainly realized by rigid-body rearrangements of the relative positions between A and B subunits, not by large interdomain movements within individual subunits. Two AB pairs (ANBN and AN'BN') take a narrowly closed conformation and bind ADP at their P-loops, while the AWBW pair takes a widely open conformation and does not bind nucleotide. The contact area of AWB-W is smaller than that of AN-BN and AN'-BN' due to absence of interaction at the bottom part of the AWB-W pair.

### ADP binding at catalytic P-loops

Two out of three catalytic A subunits accommodate ADP molecules at their P-loops (AN and AN' sites), while no density is observed at the AW P-loop. The diphosphate moiety shows especially strong electron density. The conformation of ADP is almost identical to that in F1-ATPase. The adenine group interacts with aromatic residues Phe419 and Tyr500 of the A subunit. Other residues including Lys234, Val236, Thr237, Glu261, Asp264, and Ala414 are in proximity of the nucleotide.

### Central stalk DF subcomplex structure

The central stalk consisting of D and F subunits has a more straight conformation than the corresponding gamma subunit of F1-ATPase. The D subunit features a coiled-coil structure with well-determined side chain positions. The lengths of the two helices are about 80 A for the N-terminal helix and 110 A for the C-terminal helix. The F subunit (residues 1-75) forms a Rossmann fold corresponding to the alpha/beta-domain of the gamma subunit of F1-ATPase, but with an orientation differing by about 90 degrees. The foot portion of the central stalk is about 30 A, significantly smaller than that of F1-ATPase at about 50 A. This smaller foot might be a feature of the interaction with the C subunit located between V1-ATPase and Vo as an adaptor, as there is no counterpart for the C subunit in F-ATPases.

### Asymmetric packing as torque generation mechanism

The asymmetric packing of the AB and DF subcomplexes, realized through rigid-body rearrangements of A and B subunits triggered by ATP binding and hydrolysis, is essential for torque generation in rotary ATPases. This mechanism does not require large inter-domain motion of catalytic subunits. The asymmetry is relayed from the P-loop through the intersubunit interfaces to the D subunit. The rotational direction at ATP hydrolysis may be explained by the interaction between the N terminus of D and the P-loop of the adjacent A subunit. The linear feature of the coiled-coil helices of the D subunit causes small ternary changes at A and B subunits. The torque is primarily generated by quaternary rearrangement at the interface between A and B subunits rather than the open-closed transition of the catalytic A subunit.

### B subunit is non-catalytic and does not bind nucleotide

The B subunit in the A3B3 complex is the non-catalytic subunit, equivalent to the F1-alpha subunit. Structural comparison of the P-loop equivalent region in the B subunit with the nucleotide-bound P-loop in yeast F1-alpha shows a totally different main-chain conformation that does not allow hydrogen bonding with a triphosphate group. The B subunit lacks flexible [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues and includes a proline insertion. Mutations of equivalent nucleotide-binding residues (B/N161A, B/E162A) did not affect ATP hydrolysis rate, confirming the B subunit cannot bind nucleotide at the A-B interface. Chemical modification of B subunit by nucleotide analogues occurs at the catalytic B-A interface, not the A-B interface.

### Hydrophobic cluster at B-A interface essential for catalysis

Mutational analysis of the B-A catalytic interface identified a cluster of key hydrophobic residues essential for ATP hydrolysis. A/E257 (equivalent to F1-beta/E188) mutation to aspartate or glutamine caused near-complete loss of ATP-hydrolysis activity. B/R360 (equivalent to F1-alpha/R373) mutation to lysine or leucine caused complete loss of activity. A/F419 (equivalent to F1-beta/Y345) mutation to glutamate caused complete loss. A/S385 and B/Y331 form a conserved serine-aromatic residue pair essential for coordinating catalytic water. A/F230 mutation to alanine caused near-complete loss of ATPase activity, supporting the model that A/F230, A/P387, and B/Y331 form a hydrophobic cluster at the catalytic site analogous to the F1-beta hydrophobic cluster.

### A3B3 subcomplex structure differs from F1 alpha3beta3 domain

The A3B3 subcomplex structure shows clear differences from the alpha3beta3 sub-domain in F1-ATPase. The protruding bulge domain (encoded by the non-homologous region unique to A subunits) makes the A3B3 complex triangular in top view, unlike the orange-like spherical shape of F1. The A3B3 complex maintains a large internal cavity for the DF central shaft, with a diameter larger than F1 alpha3beta3 because all A subunits adopt an open conformation. Three longer helices in the C-terminal domain of A subunits face the Vo domain in the membrane.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/ilyobacter-tartaricus-c-subunit/">C-subunit of F-ATP synthase from Ilyobacter tartaricus</a> — Related rotary ATPase component; the D subunit of V1-ATPase is structurally analogous to the gamma subunit of F1-ATPase
- <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP (Adenosine diphosphate)</a> — Nucleotide substrate; bound at two of three catalytic A subunit P-loops in 3A5C and 3W3A structures
- <a href="/xray-mp-wiki/reagents/ligands/alf4/">AlF4 (Aluminum Fluoride)</a> — Phosphate analog used in nucleotide-bound crystallization (3A5C); 1.0 mM Al(NO3)3 + 1.0 mM KF added to protein solution
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Crystallization precipitant at 1.6 M in sitting-drop and hanging-drop vapor diffusion
- <a href="/xray-mp-wiki/reagents/additives/dioxane/">Dioxane</a> — Crystallization additive at 10% (v/v) in both nucleotide-free and nucleotide-bound forms
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES (2-(N-morpholino)ethanesulfonic acid)</a> — Crystallization buffer at 100 mM, pH 6.0
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a> — Crystallization additive at 10 mM in 3W3A structure; Mg2+ required for ADP binding in 3A5C
- <a href="/xray-mp-wiki/reagents/additives/potassium-fluoride/">Potassium Fluoride</a> — Crystallization additive at 1.0 mM; forms AlFx complex with aluminum nitrate for phosphate analog
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> — Method used in structure determination or purification
