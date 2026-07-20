---
title: "Yeast V-ATPase Subunits D and F (ScDF Assembly)"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, pump]
sources: [doi/10.1074##jbc.M114.622688]
verified: agent
uniprot_id: ['P32610', 'P39111']
---

# Yeast V-ATPase Subunits D and F (ScDF Assembly)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P32610">UniProt: P32610</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P39111">UniProt: P39111</a>

<span class="expr-badge">Saccharomyces cerevisiae</span>

## Overview

The DF assembly of the Saccharomyces cerevisiae V-ATPase (ScDF) is a central stalk subcomplex essential for coupling ATP hydrolysis in the V1 domain to proton pumping in the VO domain. The crystal structure of ScDF was determined at 3.1 A resolution using [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) multi-wavelength anomalous dispersion (MAD) phasing. Two conformations (ScDF1 and ScDF2) were observed in the asymmetric unit. Subunit D (ScD, 163 residues) consists of a long pair of alpha-helices connected by a short helix and a beta-hairpin region flanked by flexible loops. Subunit F (ScF, 118 residues) comprises an N-terminal globular domain of four beta-strands and four alpha-helices, connected via a flexible loop (Pro-95 to Asp-106) to a C-terminal alpha-helix (alpha5). The structures reveal that the C-terminal helix of ScF can adopt both perpendicular and parallel orientations relative to the ScD helices. Solution SAXS data confirm the flexibility of the C-terminal segment, enabling rearrangements between compact and extended conformations important for rotary catalysis and reversible V1VO disassembly.


## Publications

### doi/10.1074##jbc.M114.622688

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4rnd">4RND</a></td>
      <td>3.1</td>
      <td>P6(1)</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21 (DE3)
- **Construct**: Recombinant ScDF heterodimer (subunits D and F from S. cerevisiae V-ATPase); SeMet-labeled version produced for MAD phasing

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
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Nickel-nitrilotriacetic acid (<a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a>) chromatography</td>
      <td>—</td>
      <td></td>
      <td>As described previously (ref 18). <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> used in all buffers for SeMet protein to avoid selenium oxidation.</td>
    </tr>
    <tr>
      <td>Buffer exchange</td>
      <td>Buffer exchange into crystallization buffer</td>
      <td>—</td>
      <td>50 mM Tris/HCl pH 8.5, 250 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> (plus 2 mM TCEP for SeMet)</td>
      <td>For SeMet ScDF, buffer contained 2 mM tris(2-carboxyethyl)-phosphine (TCEP)</td>
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
      <td>ScDF (5-8 mg/ml) in 50 mM Tris/HCl pH 8.5, 250 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> tribasic dihydrate pH 5.6, 1.2 M ammonium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> monobasic</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>25% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> in crystallization buffer</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial hits from Hampton Crystal Screen 1, condition 11 (0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 5.6, 1.0 M ammonium phosphate monobasic). Optimized with additives (NDSB-201). SeMet crystals grown with 2 mM TCEP.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Subunit D structure

ScD (163 residues) consists of a long pair of alpha-helices (N-terminal alpha1 and C-terminal helix) connected by a short helix (79IGYQVQE85) and a beta-hairpin region flanked by two flexible loops. The r.m.s.d. between ScD in ScDF1 and ScDF2 is 6.3 A for 161 Calpha atoms, but only 1.0 A for the first 117 equivalent Calpha atoms, indicating the C-terminal helix moves around a hinge region beginning after Ala-155. The exposed N-terminal helix is basic, while the C-terminal helix is predominantly acidic.

### Subunit F structure

ScF (118 residues) has an N-terminal globular domain (residues 1-94) with four parallel beta-strands enveloped by four alpha-helices (alpha1-alpha4). The structure contains a unique loop between alpha1 and beta2 (26GQITPETQEK35) and a conserved 60ERDD63 motif between alpha2 and beta3, found only in eukaryotic V-ATPases. The N-terminal domain connects via a flexible loop (Pro-95 to Asp-106) to the C-terminal alpha-helix alpha5 (107SVLKVRKL115) of mostly positively charged residues.

### Two conformations of the DF assembly

Two conformations (ScDF1 and ScDF2) were observed. In ScDF1, the flexible loop (Pro-95 to Asp-106) of ScF is bent at Lys-105, placing the C-terminal helix alpha5 perpendicular to the ScD helices. In ScDF2, alpha5 is almost parallel to the ScD helices. The r.m.s.d. between ScF in ScDF1 and ScDF2 is 3.5 A for 115 residues, but only 0.3 A for the N-terminal 94 Calpha atoms, confirming flexibility is confined to the C-terminal region.

### Solution SAXS confirms C-terminal flexibility

Small-angle X-ray scattering (SAXS) data on ScF alone confirmed the flexibility of the Pro-95 to Asp-106 loop and alpha5. The SAXS-derived model showed both compact and extended monomer conformations. Guinier analysis gave Rg = 19.3-19.6 A, Dmax = 67.5 A, and Porod volume ~32,831 A3. The calculated Mr from I(0) was 21,305 Da (monomer Mr from sequence: 13,144 Da), indicating a dimer in solution.

### Functional implications for rotary catalysis

Fitted into the A3B3 structure of related A-ATP synthase from E. hirae, the ScDF2 (extended) conformation positions ScF alpha5 in contact with the tight nucleotide-binding interface of the A and B subunits. In this arrangement, ScF is in close proximity to the tight form of the nucleotide-binding site, and ScD lies between the empty and bound forms, reflecting their central function in ATPase-coupled ion conduction. The flexibility of alpha5 and the 26GQITPETQEK35 loop provides information about the regulatory step of reversible V1VO disassembly.

### Subunit D and F interface

The interface between ScD and ScF involves hydrophobic residues including Leu-31, Leu-32, Lys-33, Leu-39, Phe-43, Thr-47, Ile-50, Met-57, Met-61, Ala-64, Leu-68, Val-71, Ala-74 (ScD alpha1), Phe-92, Val-94, Ala-96, Val-101, Val-104, Leu-106, Phe-109 (ScD beta-hairpin), and Val-143, Thr-145, Leu-146, Leu-149, Leu-152, Phe-156, Ile-157, Leu-160 (ScD C-terminal helix).

### Structural similarity to F-ATPase gamma subunit

Superposition of ScF with the gamma subunit of E. coli F-ATP synthase reveals a shared fold in the globular domain, suggesting a conserved structural role for the central stalk subunits across F- and V-type ATPases.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/yeast-v1-atpase/">Yeast V1-ATPase from S. cerevisiae</a> — ScDF is a subcomplex of the yeast V-ATPase central stalk; the DF assembly couples ATP hydrolysis in V1 to ion pumping in VO
- <a href="/xray-mp-wiki/proteins/pumps-atpases/enterococcus-hirae-v1-atpase/">Enterococcus hirae V1-ATPase</a> — Related A-ATP synthase A3B3 structure used for fitting ScDF (PDB 3VR6); comparison of DF assembly across species
- <a href="/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/">V1-ATPase from Thermus thermophilus</a> — Related bacterial V-ATPase; comparison of central stalk structure and rotary mechanism
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/rotary-atpase-mechanism/">Rotary ATPase Mechanism</a> — ScDF is the central motor element coupling ATP hydrolysis to proton pumping in the rotary mechanism
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/peripheral-stalk-elasticity/">Peripheral Stalk Elasticity in ATP Synthase</a> — Flexibility of the ScF C-terminal region and its role in reversible V1VO disassembly relates to elastic energy transmission in the stalk
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> — Crystallization method for ScDF
- <a href="/xray-mp-wiki/methods/structure-determination/multi-wavelength-anomalous-diffraction/">Multi-Wavelength Anomalous Diffraction (MAD)</a> — MAD phasing with SeMet was essential for solving the ScDF structure
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Used in purification of ScDF
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Additive used in purification or crystallization buffers
