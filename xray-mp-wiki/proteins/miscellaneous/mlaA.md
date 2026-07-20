---
title: "E. coli MlaA Outer Membrane Lipoprotein"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, porin, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.019, doi/10.1038##s41564-017-0046-x]
verified: agent
uniprot_id: P02931
---

# E. coli MlaA Outer Membrane Lipoprotein

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P02931">UniProt: P02931</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

MlaA is an [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) lipoprotein from Escherichia coli that forms a complex with the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) porin proteins OmpC and OmpF. MlaA is a key component of the Mla lipid transport system, where it functions at the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) as a monomeric alpha-helical phospholipid translocation channel embedded in the inner leaflet of the OM with a doughnut-shaped architecture. The central amphipathic pore allows selective removal of misplaced outer leaflet phospholipids while preventing access of inner leaflet phospholipids. Enterobacterial MlaA proteins form stable complexes with OmpF/C, though the porins do not play an active role in phospholipid transport.

## Publications

### doi/10.1016##j.cell.2017.03.019

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5uw8">5UW8</a></td>
      <td>not determined</td>
      <td>not applicable</td>
      <td>Mature MlaA (signal peptide-cleaved, residues 1-251) in complex with OmpF porin</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Mature MlaA (residues 1-251), signal peptide-cleaved, cloned into custom pET vector (pDCE587)

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
      <td>Co-expression and solubilization</td>
      <td>Co-expression of MlaA with OmpF, solubilization with detergent</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>MlaA-OmpF complex solubilized from <a href="/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/">outer membrane</a> fraction</td>
    </tr>
    <tr>
      <td>Complex purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> and gel filtration</td>
      <td>Not specified</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>MlaA-OmpC/OmpF complex purified for <a href="/xray-mp-wiki/methods/quality-assessment/biolayer-interferometry/">biolayer interferometry</a> studies</td>
    </tr>
  </tbody>
</table>

### doi/10.1038##s41564-017-0046-x

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5nuo">5NUO</a></td>
      <td>3.0</td>
      <td>Not specified</td>
      <td>Klebsiella pneumoniae MlaA (KpMlaA) in complex with E. coli OmpF trimer, full-length mature protein</td>
      <td>none</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5nuo">5NUO</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>Serratia marcescens MlaA (SmMlaA) in complex with E. coli OmpF trimer, full-length mature protein</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Mature MlaA (residues 1-251), signal peptide-cleaved, cloned into custom pET vector (pDCE587)

**Purification:**

- **Expression system**: E. coli BL21
- **Expression construct**: KpMlaA (Klebsiella pneumoniae) or SmMlaA (Serratia marcescens) orthologues with N-terminal hexahistidine tag, cloned into pBAD24 vector
- **Tag info**: N-terminal hexahistidine tag

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
      <td>Expression</td>
      <td>Arabinose-inducible expression in E. coli BL21</td>
      <td>—</td>
      <td>Low-salt LB medium (tryptone 10 g/L, NaCl 5 g/L, yeast extract 5 g/L)</td>
      <td>Expression induced with 0.2% arabinose at OD600 ~0.6, 20 C for 4-16 hr</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>High-pressure homogenization (Constant Systems, 20,000-23,000 psi)</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> buffered saline pH 7.5, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a></td>
      <td>Membranes harvested by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> buffered saline pH 7.5, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.5% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (for KpMlaA-syn), 1% DDM (for native complexes)</td>
      <td>Stirred 1 hr at 4 C</td>
    </tr>
    <tr>
      <td>Nickel affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> (Qiagen)</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> buffered saline pH 7.5, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.15% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 25 mM imidazole (wash), 250 mM imidazole (elution)</td>
      <td>MlaA-OmpF complex eluted as stable complex</td>
    </tr>
    <tr>
      <td>Buffer exchange</td>
      <td>Amicon Ultra-15 concentrator (100 kDa cutoff)</td>
      <td>—</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.4% C8E4</td>
      <td>For KpMlaA; SmMlaA further purified by <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography (SmMlaA only)</td>
      <td>HiLoad 26/600 <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>—</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.4% C6H12</td>
      <td>SmMlaA-OmpF complex purified by <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: ~10 mg/mL, flash-frozen in liquid nitrogen
**Purity**: >95% by SDS-PAGE, confirmed by mass spectrometry

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KpMlaA-OmpF complex at ~10 mg/mL in 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.4% C8E4</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.5, 0.2 M lithium sulfate, 24% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals also obtained for SmMlaA-OmpF complex. LPS molecules observed in porin LPS-binding site in one KpMlaA-OmpF structure.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### MlaA-OmpC/OmpF outer membrane complex

MlaA forms a stable complex with the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) porin proteins OmpC and OmpF.
This complex serves as the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) anchor of the Mla lipid transport system,
receiving phospholipids from the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) shuttle protein [MLAC](/xray-mp-wiki/proteins/mlaC) and inserting
them into the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) leaflet. The MlaA-OmpF complex was used in biolayer
interferometry experiments to demonstrate direct interaction with [MLAC](/xray-mp-wiki/proteins/mlaC).

### Direct interaction with periplasmic lipid shuttle MlaC

[biolayer interferometry](/xray-mp-wiki/methods/quality-assessment/biolayer-interferometry/) (Octet RED384) demonstrated that [MLAC](/xray-mp-wiki/proteins/mlaC) interacts directly
with the MlaA-OmpC/OmpF [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) complex. Biotinylated [MLAC](/xray-mp-wiki/proteins/mlaC) loaded onto
streptavidin-coated biosensors showed binding to the MlaA-OmpF complex, supporting
the model where [MLAC](/xray-mp-wiki/proteins/mlaC) ferries lipids from the [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membrane/) MlaFEDB complex to
the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) MlaA-OmpC/OmpF complex. This interaction is essential for maintaining
[outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) [lipid asymmetry](/xray-mp-wiki/concepts/structural-mechanisms/lipid-asymmetry/).

### Non-essential but critical for outer membrane integrity

While individual MCE system components are non-essential for E. coli growth in rich
media, mutations in mla genes result in increased sensitivity to [SDS](/xray-mp-wiki/reagents/detergents/sds/) and [EDTA](/xray-mp-wiki/reagents/additives/edta/),
indicative of [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/) defects. The MlaA-OmpC/OmpF complex is required for
the complete Mla system to function, and its disruption leads to accumulation of
phospholipids in the outer leaflet of the [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/), disrupting [lipid asymmetry](/xray-mp-wiki/concepts/structural-mechanisms/lipid-asymmetry/).

### Doughnut-shaped alpha-helical architecture

X-ray crystal structures of KpMlaA-OmpF and SmMlaA-OmpF complexes reveal MlaA as a monomeric alpha-helical OM protein with a ring-shaped (doughnut) structure. The protein is ~20 A thick (spanning one leaflet of the OM) and predominantly alpha-helical, with most helices oriented parallel to the membrane plane. Helix 6 (H6) is perpendicular to the membrane and spans the lipid bilayer. A central channel approximately 5 A wide at its narrowest point is lined with hydrophilic residues from H2, the pore loop (between H4 and H5), H5, and H6. The extracellular end of the channel features a pronounced ridge (H5, top of H6, connecting loop) with Trp160 and Trp163 embedded in the outer leaflet interface. The entire MlaA surface is hydrophobic except for the periplasmic face.

### Phospholipid translocation mechanism

Molecular dynamics simulations (atomistic and coarse-grained) show that outer leaflet phospholipids bind specifically to the MlaA ridge, with the PE head group moving ~15 A down the channel towards the bilayer center coupled with tilting of acyl chains by 45-90 degrees. The doughnut architecture prevents inner leaflet phospholipid access to the channel while allowing outer leaflet phospholipids to diffuse to the central channel. The pore can enlarge via conformational rearrangements of the pore loop and/or H6, as demonstrated by the Y138C/W170C disulfide lock mutant which is inactive but rescued by reducing agent. MlaA functions in an energy-independent fashion as a phospholipid translocation channel.

### MlaA* variant and scramblase activity

The N26-F27 deletion variant (MlaA*) shows a more severe phenotype than the mlaA knockout, likely due to disruption of helix H1 and/or its interaction with the pore loop, creating a breach that allows lateral access of inner leaflet phospholipids to the central channel. This would cause rapid, reversed flow to the outer leaflet driven by the steep concentration gradient, effectively functioning as a scramblase.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaC/">E. coli MlaC Lipid-Binding Protein</a> — MlaC directly interacts with MlaA-OmpF complex to deliver lipids to the outer membrane
- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaD/">E. coli MlaD MCE Protein</a> — MlaA is the outer membrane partner of MlaD at the inner membrane in the Mla system
- <a href="/xray-mp-wiki/proteins/structural-adhesion/yebT/">E. coli YebT Tube-like MCE Protein</a> — YebT may associate with YebS in the inner membrane and PqiC in the outer membrane similarly
- <a href="/xray-mp-wiki/proteins/structural-adhesion/pqiB/">E. coli PqiB Syringe-like MCE Protein</a> — PqiB may interact with outer membrane lipoprotein PqiC similarly to MlaA
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — DDM used for MlaA-OmpF complex solubilization from membranes
- <a href="/xray-mp-wiki/concepts/protein-families/mce-protein-family/">MCE Protein Family</a> — MlaA is a key component of the Mla system, an MCE protein family member
- <a href="/xray-mp-wiki/reagents/buffers/tris/">TRIS</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/concepts/miscellaneous/gram-negative/">Gram-negative</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/methods/quality-assessment/biolayer-interferometry/">biolayer interferometry</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/lipid-asymmetry/">Lipid Asymmetry</a> — MlaA functions to maintain outer membrane lipid asymmetry
